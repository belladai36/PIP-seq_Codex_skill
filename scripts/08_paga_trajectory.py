#!/usr/bin/env python
from __future__ import annotations

import argparse

import scanpy as sc

from pipeline_utils import ensure_dirs, load_config, project_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Run PAGA trajectory inference on Leiden clusters.")
    parser.add_argument("--config", default="config/config.yaml")
    args = parser.parse_args()

    config = load_config(args.config)
    ensure_dirs(config)

    scanpy_dir = project_path(config["paths"]["scanpy_dir"])
    fig_dir = project_path(config["paths"]["figure_dir"]) / "paga"
    sc.settings.figdir = str(fig_dir)

    adata = sc.read_h5ad(scanpy_dir / "04_markers_annotated.h5ad")
    sc.tl.paga(adata, groups="leiden")
    sc.pl.paga(adata, threshold=0.03, save="_leiden_graph.png", show=False)

    # Recompute UMAP with PAGA initialization to make broad relationships easier to see.
    sc.tl.umap(adata, init_pos="paga", random_state=config["analysis"].get("random_state", 42))
    sc.pl.umap(adata, color=["leiden", "cell_type"], save="_paga_initialized_umap.png", show=False)

    adata.write_h5ad(scanpy_dir / "05_paga.h5ad")
    print(f"Wrote {scanpy_dir / '05_paga.h5ad'}")


if __name__ == "__main__":
    main()

