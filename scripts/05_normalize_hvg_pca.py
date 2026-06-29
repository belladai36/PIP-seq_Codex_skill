#!/usr/bin/env python
from __future__ import annotations

import argparse
import os

os.environ.setdefault("NUMBA_CACHE_DIR", "/private/tmp/numba-cache")
os.environ.setdefault("MPLCONFIGDIR", "/private/tmp/mplconfig")

import scanpy as sc

from pipeline_utils import ensure_dirs, load_config, project_path, write_json


def main() -> None:
    parser = argparse.ArgumentParser(description="Normalize, log-transform, select HVGs, and run PCA.")
    parser.add_argument("--config", default="config/config.yaml")
    args = parser.parse_args()

    config = load_config(args.config)
    ensure_dirs(config)
    analysis = config["analysis"]

    scanpy_dir = project_path(config["paths"]["scanpy_dir"])
    fig_dir = project_path(config["paths"]["figure_dir"]) / "qc"

    adata = sc.read_h5ad(scanpy_dir / "01_qc_flagged.h5ad")
    if "counts" not in adata.layers:
        adata.layers["counts"] = adata.X.copy()

    sc.pp.normalize_total(adata, target_sum=analysis.get("target_sum", 10000))
    sc.pp.log1p(adata)
    adata.raw = adata

    sc.pp.highly_variable_genes(
        adata,
        n_top_genes=analysis.get("n_top_hvgs", 3000),
        flavor="seurat",
    )
    sc.settings.figdir = str(fig_dir)
    sc.pl.highly_variable_genes(adata, save="_highly_variable_genes.png", show=False)

    sc.pp.scale(adata, max_value=10)
    sc.tl.pca(adata, n_comps=analysis.get("n_pcs", 30), svd_solver="arpack", random_state=analysis.get("random_state", 42))
    sc.pl.pca_variance_ratio(adata, log=True, save="_pca_variance_ratio.png", show=False)

    write_json(
        {
            "target_sum": analysis.get("target_sum", 10000),
            "n_top_hvgs": analysis.get("n_top_hvgs", 3000),
            "n_pcs": analysis.get("n_pcs", 30),
        },
        scanpy_dir / "normalization_hvg_pca_params.json",
    )
    adata.write_h5ad(scanpy_dir / "02_pca.h5ad")
    print(f"Wrote {scanpy_dir / '02_pca.h5ad'}")


if __name__ == "__main__":
    main()
