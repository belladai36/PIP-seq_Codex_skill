#!/usr/bin/env python
from __future__ import annotations

import argparse
from itertools import product

import pandas as pd
import scanpy as sc
from sklearn.metrics import adjusted_rand_score

from pipeline_utils import ensure_dirs, load_config, project_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Check cluster robustness across PCA dimensions, neighbors, and Leiden resolutions.")
    parser.add_argument("--config", default="config/config.yaml")
    args = parser.parse_args()

    config = load_config(args.config)
    ensure_dirs(config)

    scanpy_dir = project_path(config["paths"]["scanpy_dir"])
    robustness = config["robustness"]
    random_state = config["analysis"].get("random_state", 42)

    base = sc.read_h5ad(scanpy_dir / "02_pca.h5ad")
    default = sc.read_h5ad(scanpy_dir / "03_clustered_umap.h5ad")
    default_labels = default.obs["leiden"].astype(str)

    rows = []
    for n_pcs, n_neighbors, resolution in product(
        robustness.get("pca_dimensions", [30]),
        robustness.get("neighbor_numbers", [15]),
        robustness.get("leiden_resolutions", [0.8]),
    ):
        adata = base.copy()
        n_pcs = min(int(n_pcs), adata.obsm["X_pca"].shape[1])
        key = f"pcs{n_pcs}_n{n_neighbors}_r{resolution}"
        sc.pp.neighbors(adata, n_neighbors=int(n_neighbors), n_pcs=n_pcs, random_state=random_state)
        sc.tl.leiden(adata, resolution=float(resolution), key_added=key, random_state=random_state)
        labels = adata.obs[key].astype(str)
        ari = adjusted_rand_score(default_labels.loc[adata.obs_names], labels)
        rows.append(
            {
                "n_pcs": n_pcs,
                "n_neighbors": int(n_neighbors),
                "leiden_resolution": float(resolution),
                "n_clusters": labels.nunique(),
                "adjusted_rand_vs_default": ari,
            }
        )

    summary = pd.DataFrame(rows).sort_values(["n_pcs", "n_neighbors", "leiden_resolution"])
    out_path = scanpy_dir / "robustness_summary.csv"
    summary.to_csv(out_path, index=False)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()

