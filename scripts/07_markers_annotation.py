#!/usr/bin/env python
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd
import scanpy as sc

from pipeline_utils import ensure_dirs, load_config, project_path


def annotate_from_marker_scores(adata, marker_path: Path) -> pd.Series:
    markers = pd.read_csv(marker_path).dropna()
    cluster_key = "leiden"
    score_columns = []

    for cell_type, group in markers.groupby("cell_type"):
        genes = [gene for gene in group["gene"].astype(str) if gene in adata.var_names]
        if len(genes) < 2:
            continue
        score_col = f"score_{cell_type}"
        sc.tl.score_genes(adata, gene_list=genes, score_name=score_col)
        score_columns.append(score_col)

    if not score_columns:
        return pd.Series("unknown", index=adata.obs[cluster_key].cat.categories)

    cluster_scores = adata.obs.groupby(cluster_key, observed=True)[score_columns].mean()
    labels = {}
    for cluster, row in cluster_scores.iterrows():
        best_score = row.max()
        best_col = row.idxmax()
        labels[cluster] = best_col.replace("score_", "") if best_score > 0 else "unknown"
    return pd.Series(labels)


def main() -> None:
    parser = argparse.ArgumentParser(description="Find marker genes and conservatively annotate clusters.")
    parser.add_argument("--config", default="config/config.yaml")
    args = parser.parse_args()

    config = load_config(args.config)
    ensure_dirs(config)

    scanpy_dir = project_path(config["paths"]["scanpy_dir"])
    fig_dir = project_path(config["paths"]["figure_dir"]) / "markers"
    marker_path = project_path(config["paths"]["marker_genes"])
    sc.settings.figdir = str(fig_dir)

    adata = sc.read_h5ad(scanpy_dir / "03_clustered_umap.h5ad")
    sc.tl.rank_genes_groups(adata, groupby="leiden", method="wilcoxon", use_raw=True)
    sc.pl.rank_genes_groups(adata, n_genes=20, sharey=False, save="_leiden.png", show=False)

    marker_table = sc.get.rank_genes_groups_df(adata, group=None)
    marker_table.to_csv(scanpy_dir / "marker_genes_by_leiden.csv", index=False)

    if marker_path.exists():
        labels = annotate_from_marker_scores(adata, marker_path)
        adata.obs["cell_type"] = adata.obs["leiden"].map(labels).astype("category")
    else:
        adata.obs["cell_type"] = "unknown"

    sc.pl.umap(adata, color=["leiden", "cell_type"], legend_loc="on data", save="_annotated.png", show=False)
    adata.write_h5ad(scanpy_dir / "04_markers_annotated.h5ad")
    print(f"Wrote {scanpy_dir / 'marker_genes_by_leiden.csv'}")
    print(f"Wrote {scanpy_dir / '04_markers_annotated.h5ad'}")


if __name__ == "__main__":
    main()

