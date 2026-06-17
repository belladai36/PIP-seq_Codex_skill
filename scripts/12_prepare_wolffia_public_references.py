#!/usr/bin/env python
from __future__ import annotations

import argparse
from pathlib import Path

import anndata as ad
import pandas as pd
import scanpy as sc

from pipeline_utils import load_config, project_path


def load_manifest(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    required = {
        "dataset_id",
        "display_name",
        "input_format",
        "local_input_path",
        "processed_output_path",
        "status",
    }
    missing = required.difference(df.columns)
    if missing:
        raise ValueError(f"Manifest is missing columns: {sorted(missing)}")
    return df


def read_dataset(input_path: Path, input_format: str) -> ad.AnnData:
    fmt = input_format.lower().strip()
    if fmt == "h5ad":
        return sc.read_h5ad(input_path)
    if fmt == "10x_h5":
        adata = sc.read_10x_h5(input_path)
        adata.var_names_make_unique()
        return adata
    if fmt == "10x_mtx_dir":
        adata = sc.read_10x_mtx(input_path, var_names="gene_symbols", make_unique=True)
        adata.var_names_make_unique()
        return adata
    if fmt == "raw_fastq_dir":
        raise ValueError(
            "raw_fastq_dir cannot be imported directly into AnnData. Generate a count matrix first, "
            "then update the manifest to h5ad, 10x_h5, or 10x_mtx_dir."
        )
    raise ValueError(
        f"Unsupported input_format '{input_format}'. Supported values: h5ad, 10x_h5, 10x_mtx_dir, raw_fastq_dir."
    )


def prepare_record(row: pd.Series) -> Path | None:
    input_format = str(row["input_format"])
    raw_value = str(row["local_input_path"])
    if not raw_value.strip():
        print(f"SKIP {row['dataset_id']}: local_input_path not finalized yet.")
        return None

    input_path = project_path(raw_value)
    if not input_path.exists():
        print(f"SKIP {row['dataset_id']}: input path does not exist -> {input_path}")
        return None

    output_path = project_path(str(row["processed_output_path"]))
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        adata = read_dataset(input_path, input_format=input_format)
    except ValueError as exc:
        print(f"SKIP {row['dataset_id']}: {exc}")
        return None

    adata.layers["counts"] = adata.X.copy()
    adata.uns["dataset_id"] = str(row["dataset_id"])
    adata.uns["dataset_title"] = str(row["display_name"])
    adata.uns["assay_type"] = str(row.get("assay_type", "unknown"))
    adata.uns["reference_role"] = str(row.get("role", "unspecified"))
    adata.write_h5ad(output_path)
    print(f"WROTE {output_path}")
    return output_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Prepare public Wolffia reference datasets once local files are available.")
    parser.add_argument("--config", default="config/config.yaml")
    args = parser.parse_args()

    config = load_config(args.config)
    section = config.get("wolffia_public_reference_analysis", {})
    if not section:
        raise ValueError("Missing 'wolffia_public_reference_analysis' section in config/config.yaml")

    manifest_path = project_path(section["manifest_csv"])
    manifest = load_manifest(manifest_path)
    written: list[Path] = []
    for _, row in manifest.iterrows():
        result = prepare_record(row)
        if result is not None:
            written.append(result)

    print(f"Prepared {len(written)} Wolffia public reference dataset(s).")


if __name__ == "__main__":
    main()
