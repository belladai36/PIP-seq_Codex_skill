#!/usr/bin/env python
from __future__ import annotations

import argparse

import scanpy as sc

from pipeline_utils import add_gene_flags, ensure_dirs, load_config, project_path, write_json


def optional_bound_mask(values, minimum, maximum):
    mask = values.notna()
    if minimum is not None:
        mask &= values >= minimum
    if maximum is not None:
        mask &= values <= maximum
    return mask


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute cell QC metrics and flag/filter low-quality cells.")
    parser.add_argument("--config", default="config/config.yaml")
    args = parser.parse_args()

    config = load_config(args.config)
    ensure_dirs(config)
    qc = config["qc"]

    scanpy_dir = project_path(config["paths"]["scanpy_dir"])
    fig_dir = project_path(config["paths"]["figure_dir"]) / "qc"

    adata = sc.read_h5ad(scanpy_dir / "00_raw_counts.h5ad")
    add_gene_flags(adata, config)
    sc.pp.calculate_qc_metrics(adata, qc_vars=["mito", "plastid"], inplace=True, percent_top=None)

    adata.obs["passes_gene_filter"] = optional_bound_mask(
        adata.obs["n_genes_by_counts"], qc.get("min_genes_per_cell"), qc.get("max_genes_per_cell")
    )
    adata.obs["passes_count_filter"] = optional_bound_mask(
        adata.obs["total_counts"], qc.get("min_counts_per_cell"), qc.get("max_counts_per_cell")
    )
    adata.obs["passes_mito_filter"] = adata.obs["pct_counts_mito"] <= qc.get("max_percent_mito", 100)
    adata.obs["passes_qc"] = (
        adata.obs["passes_gene_filter"] & adata.obs["passes_count_filter"] & adata.obs["passes_mito_filter"]
    )

    sc.settings.figdir = str(fig_dir)
    sc.pl.violin(
        adata,
        ["n_genes_by_counts", "total_counts", "pct_counts_mito", "pct_counts_plastid"],
        jitter=0.4,
        multi_panel=True,
        save="_cell_qc_metrics.png",
        show=False,
    )
    sc.pl.scatter(adata, x="total_counts", y="n_genes_by_counts", color="passes_qc", save="_counts_vs_genes.png", show=False)

    summary = {
        "input_cells": int(adata.n_obs),
        "passing_cells": int(adata.obs["passes_qc"].sum()),
        "failed_gene_filter": int((~adata.obs["passes_gene_filter"]).sum()),
        "failed_count_filter": int((~adata.obs["passes_count_filter"]).sum()),
        "failed_mito_filter": int((~adata.obs["passes_mito_filter"]).sum()),
        "thresholds": qc,
        "note": "For final analysis, inspect QC plots and tune thresholds from observed distributions.",
    }
    write_json(summary, scanpy_dir / "qc_summary.json")

    if qc.get("filter_to_passing_cells", True):
        adata = adata[adata.obs["passes_qc"]].copy()

    adata.layers["counts"] = adata.X.copy()
    adata.write_h5ad(scanpy_dir / "01_qc_flagged.h5ad")
    print(f"Wrote {scanpy_dir / '01_qc_flagged.h5ad'}")


if __name__ == "__main__":
    main()

