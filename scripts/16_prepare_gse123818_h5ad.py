#!/usr/bin/env python
from __future__ import annotations

import argparse
import csv
import gzip
from pathlib import Path

import anndata as ad
import pandas as pd
from scipy import sparse

from pipeline_utils import project_path


RAW_DIR = project_path("data/public_references/raw/GSE123818")
PROCESSED_DIR = project_path("data/public_references/processed")

DATASET_FILES = {
    "wt": RAW_DIR / "GSE123818_Root_single_cell_wt_datamatrix.csv.gz",
    "shr": RAW_DIR / "GSE123818_Root_single_cell_shr_datamatrix.csv.gz",
}

DATASET_TITLES = {
    "wt": "Arabidopsis root single-cell atlas (wild type)",
    "shr": "Arabidopsis root single-cell atlas (short-root mutant)",
}


def read_header_cells(path: Path) -> list[str]:
    with gzip.open(path, "rt", newline="") as handle:
        reader = csv.reader(handle)
        header = next(reader)
    if len(header) < 2:
        raise ValueError(f"Unexpected header in {path}")
    return [str(cell_id) for cell_id in header[1:]]


def load_matrix_and_genes(path: Path, chunk_size: int = 500) -> tuple[sparse.csr_matrix, list[str]]:
    chunks: list[sparse.csr_matrix] = []
    gene_ids: list[str] = []

    reader = pd.read_csv(
        path,
        compression="gzip",
        index_col=0,
        chunksize=chunk_size,
    )

    for chunk in reader:
        chunk.index = chunk.index.astype(str)
        gene_ids.extend(chunk.index.tolist())
        chunks.append(sparse.csr_matrix(chunk.to_numpy(dtype="float32", copy=False)))

    if not chunks:
        raise ValueError(f"No expression rows were found in {path}")

    matrix = sparse.vstack(chunks, format="csr")
    return matrix, gene_ids


def build_adata(split: str) -> ad.AnnData:
    input_path = DATASET_FILES[split]
    if not input_path.exists():
        raise FileNotFoundError(f"Missing {input_path}")

    cell_ids = read_header_cells(input_path)
    matrix, gene_ids = load_matrix_and_genes(input_path)

    if matrix.shape != (len(gene_ids), len(cell_ids)):
        raise ValueError(
            f"Matrix shape {matrix.shape} does not match gene/cell counts {(len(gene_ids), len(cell_ids))}."
        )

    obs = pd.DataFrame(index=pd.Index(cell_ids, name="cell_id"))
    obs["source_split"] = split
    obs["genotype"] = "wild_type" if split == "wt" else "short_root_mutant"

    var = pd.DataFrame(index=pd.Index(gene_ids, name="gene_id"))
    var["gene_ids"] = var.index.astype(str)

    adata = ad.AnnData(X=matrix.transpose().tocsr(), obs=obs, var=var)
    adata.layers["counts"] = adata.X.copy()
    adata.var_names_make_unique()
    adata.uns["dataset_accession"] = "GSE123818"
    adata.uns["dataset_title"] = DATASET_TITLES[split]
    adata.uns["source_split"] = split
    return adata


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert GSE123818 root atlas CSV matrices into h5ad.")
    parser.add_argument("--split", default="wt", choices=["wt", "shr", "both"])
    args = parser.parse_args()

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    splits = ["wt", "shr"] if args.split == "both" else [args.split]

    for split in splits:
        adata = build_adata(split)
        output_path = PROCESSED_DIR / f"GSE123818_{split}_root.h5ad"
        adata.write_h5ad(output_path)
        print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()
