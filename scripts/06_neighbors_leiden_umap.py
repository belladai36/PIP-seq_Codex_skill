#!/usr/bin/env python
from __future__ import annotations

import argparse
import os

os.environ.setdefault("NUMBA_CACHE_DIR", "/private/tmp/numba-cache")
os.environ.setdefault("MPLCONFIGDIR", "/private/tmp/mplconfig")

import scanpy as sc

from pipeline_utils import ensure_dirs, load_config, project_path, write_json


def main() -> None:
    parser = argparse.ArgumentParser(description="Construct KNN graph, run Leiden clustering, and compute UMAP.")
    parser.add_argument("--config", default="config/config.yaml")
    args = parser.parse_args()

    config = load_config(args.config)
    ensure_dirs(config)
    analysis = config["analysis"]

    scanpy_dir = project_path(config["paths"]["scanpy_dir"])
    fig_dir = project_path(config["paths"]["figure_dir"]) / "umap"
    sc.settings.figdir = str(fig_dir)

    adata = sc.read_h5ad(scanpy_dir / "02_pca.h5ad")
    sc.pp.neighbors(
        adata,
        n_neighbors=analysis.get("n_neighbors", 15),
        n_pcs=analysis.get("n_pcs", 30),
        random_state=analysis.get("random_state", 42),
    )
    sc.tl.leiden(
        adata,
        resolution=analysis.get("leiden_resolution", 0.8),
        key_added="leiden",
        random_state=analysis.get("random_state", 42),
    )
    sc.tl.umap(adata, random_state=analysis.get("random_state", 42))

    color_fields = ["leiden"]
    for field in ["batch", "condition", "tissue", "passes_qc", "pct_counts_mito", "pct_counts_plastid"]:
        if field in adata.obs:
            color_fields.append(field)
    sc.pl.umap(adata, color=color_fields, wspace=0.4, save="_overview.png", show=False)

    write_json(
        {
            "n_neighbors": analysis.get("n_neighbors", 15),
            "n_pcs": analysis.get("n_pcs", 30),
            "leiden_resolution": analysis.get("leiden_resolution", 0.8),
        },
        scanpy_dir / "graph_cluster_umap_params.json",
    )
    adata.write_h5ad(scanpy_dir / "03_clustered_umap.h5ad")
    print(f"Wrote {scanpy_dir / '03_clustered_umap.h5ad'}")


if __name__ == "__main__":
    main()
