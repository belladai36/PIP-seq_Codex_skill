#!/usr/bin/env python
from __future__ import annotations

import argparse
import os

os.environ.setdefault("NUMBA_CACHE_DIR", "/private/tmp/numba-cache")
os.environ.setdefault("MPLCONFIGDIR", "/private/tmp/mplconfig")

from pathlib import Path

import anndata as ad
import numpy as np
import scanpy as sc
from scipy import sparse

from pipeline_utils import project_path


def cluster_public_reference(
    input_path: Path,
    output_path: Path,
    n_top_hvgs: int = 2000,
    n_pcs: int = 30,
    n_neighbors: int = 15,
    leiden_resolution: float = 0.6,
    random_state: int = 42,
) -> Path:
    adata = sc.read_h5ad(input_path)

    if "counts" in adata.layers:
        adata.X = adata.layers["counts"].copy()

    if sparse.issparse(adata.X):
        adata.X = adata.X.tocsr().astype(np.float32)
        counts_per_cell = np.asarray(adata.X.sum(axis=1)).ravel()
        counts_per_cell[counts_per_cell == 0] = 1.0
        scale = np.divide(10000.0, counts_per_cell, dtype=np.float32)
        adata.X = sparse.diags(scale) @ adata.X
    else:
        adata.X = np.asarray(adata.X, dtype=np.float32)
        counts_per_cell = adata.X.sum(axis=1, keepdims=True)
        counts_per_cell[counts_per_cell == 0] = 1.0
        adata.X = (adata.X / counts_per_cell) * 10000.0

    adata.X = adata.X.log1p() if sparse.issparse(adata.X) else np.log1p(adata.X)
    sc.pp.highly_variable_genes(adata, n_top_genes=min(n_top_hvgs, adata.n_vars), flavor="seurat")

    hvg_mask = adata.var["highly_variable"].to_numpy()
    adata_hvg = ad.AnnData(X=adata.X[:, hvg_mask].copy(), obs=adata.obs.copy(), var=adata.var.loc[hvg_mask].copy())

    sc.pp.scale(adata_hvg, max_value=10)
    sc.tl.pca(adata_hvg, n_comps=min(n_pcs, adata_hvg.n_vars, max(2, adata_hvg.n_obs - 1)), random_state=random_state)
    sc.pp.neighbors(
        adata_hvg,
        n_neighbors=min(n_neighbors, max(2, adata_hvg.n_obs - 1)),
        n_pcs=min(n_pcs, adata_hvg.obsm["X_pca"].shape[1]),
    )
    sc.tl.leiden(adata_hvg, resolution=leiden_resolution, key_added="leiden")

    adata.obs["leiden"] = adata_hvg.obs["leiden"].astype(str).values
    adata.obsm["X_pca"] = adata_hvg.obsm["X_pca"].copy()
    adata.uns["neighbors"] = adata_hvg.uns["neighbors"].copy()
    adata.uns["public_reference_clustering"] = {
        "n_top_hvgs": n_top_hvgs,
        "n_pcs": n_pcs,
        "n_neighbors": n_neighbors,
        "leiden_resolution": leiden_resolution,
        "random_state": random_state,
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    adata.write_h5ad(output_path)
    return output_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Cluster a public reference h5ad for broad-program training.")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--n-top-hvgs", type=int, default=2000)
    parser.add_argument("--n-pcs", type=int, default=30)
    parser.add_argument("--n-neighbors", type=int, default=15)
    parser.add_argument("--leiden-resolution", type=float, default=0.6)
    parser.add_argument("--random-state", type=int, default=42)
    args = parser.parse_args()

    written = cluster_public_reference(
        input_path=project_path(args.input),
        output_path=project_path(args.output),
        n_top_hvgs=args.n_top_hvgs,
        n_pcs=args.n_pcs,
        n_neighbors=args.n_neighbors,
        leiden_resolution=args.leiden_resolution,
        random_state=args.random_state,
    )
    print(f"Wrote {written}")


if __name__ == "__main__":
    main()
