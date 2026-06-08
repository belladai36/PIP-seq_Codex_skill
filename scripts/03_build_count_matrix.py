#!/usr/bin/env python
from __future__ import annotations

import argparse
from pathlib import Path

import anndata as ad
import pandas as pd
from scipy import sparse

from pipeline_utils import ensure_dirs, load_config, project_path


def read_featurecounts_table(path: Path, cell_id: str) -> pd.Series:
    table = pd.read_csv(path, sep="\t", comment="#")
    count_col = table.columns[-1]
    counts = table[["Geneid", count_col]].rename(columns={count_col: cell_id})
    return counts.set_index("Geneid")[cell_id]


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a gene-by-cell matrix from featureCounts outputs.")
    parser.add_argument("--config", default="config/config.yaml")
    args = parser.parse_args()

    config = load_config(args.config)
    ensure_dirs(config)

    samples = pd.read_csv(project_path(config["paths"]["sample_sheet"]))
    counts_dir = project_path(config["paths"]["counts_dir"])
    scanpy_dir = project_path(config["paths"]["scanpy_dir"])

    series = []
    for cell_id in samples["cell_id"].astype(str):
        path = counts_dir / f"{cell_id}.featureCounts.txt"
        if not path.exists():
            raise FileNotFoundError(f"Missing featureCounts output for {cell_id}: {path}")
        series.append(read_featurecounts_table(path, cell_id))

    gene_by_cell = pd.concat(series, axis=1).fillna(0).astype(int)
    matrix_path = counts_dir / "gene_by_cell_counts.csv"
    gene_by_cell.to_csv(matrix_path)

    obs = samples.set_index("cell_id")
    adata = ad.AnnData(
        X=sparse.csr_matrix(gene_by_cell.T.values),
        obs=obs.loc[gene_by_cell.columns].copy(),
        var=pd.DataFrame(index=gene_by_cell.index.astype(str)),
    )
    adata.layers["counts"] = adata.X.copy()
    adata.write_h5ad(scanpy_dir / "00_raw_counts.h5ad")

    print(f"Wrote {matrix_path}")
    print(f"Wrote {scanpy_dir / '00_raw_counts.h5ad'}")


if __name__ == "__main__":
    main()

