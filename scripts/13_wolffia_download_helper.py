#!/usr/bin/env python
from __future__ import annotations

import argparse
import csv
from pathlib import Path

from pipeline_utils import project_path


DEFAULT_RUN_TABLE = project_path("data/metadata/wolffia_public_run_accessions.csv")


def load_runs(run_table: Path, dataset_id: str) -> list[dict[str, str]]:
    with open(run_table, newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    filtered = [row for row in rows if row["dataset_id"] == dataset_id]
    if not filtered:
        raise ValueError(f"No runs found for dataset_id={dataset_id}")
    return filtered


def target_dir_for(dataset_id: str) -> Path:
    if dataset_id == "PRJNA1124135_scRNA":
        return project_path("data/public_references/raw/PRJNA1124135/scRNA_seq")
    if dataset_id == "PRJNA809022_snRNA":
        return project_path("data/public_references/raw/PRJNA809022/snRNA_seq")
    raise ValueError(f"No target directory rule defined for dataset_id={dataset_id}")


def print_prefetch_commands(runs: list[dict[str, str]], target_dir: Path) -> None:
    print("# Option 1: SRA Toolkit style download")
    print(f"mkdir -p '{target_dir}'")
    print("")
    for row in runs:
        run = row["run_accession"]
        print(f"prefetch {run}")
        print(f"fasterq-dump {run} -O '{target_dir}' --split-files")
        print(f"gzip '{target_dir}/{run}_1.fastq'")
        print(f"gzip '{target_dir}/{run}_2.fastq'")
        print("")


def print_ena_commands(runs: list[dict[str, str]], target_dir: Path) -> None:
    print("# Option 2: ENA FTP fallback pattern")
    print("# Replace with exact FASTQ links after checking ENA for each SRR accession.")
    print(f"mkdir -p '{target_dir}'")
    print("")
    for row in runs:
        run = row["run_accession"]
        print(f"# {run}")
        print(f"# curl -L 'ENA_FASTQ_URL_FOR_{run}_1' -o '{target_dir}/{run}_1.fastq.gz'")
        print(f"# curl -L 'ENA_FASTQ_URL_FOR_{run}_2' -o '{target_dir}/{run}_2.fastq.gz'")
        print("")


def main() -> None:
    parser = argparse.ArgumentParser(description="Print download commands for public Wolffia reference runs.")
    parser.add_argument(
        "--dataset-id",
        default="PRJNA1124135_scRNA",
        choices=["PRJNA1124135_scRNA", "PRJNA809022_snRNA"],
        help="Which dataset to prepare download commands for.",
    )
    parser.add_argument(
        "--mode",
        default="prefetch",
        choices=["prefetch", "ena"],
        help="Command style to print.",
    )
    parser.add_argument(
        "--make-dirs",
        action="store_true",
        help="Create the target raw-data directory locally.",
    )
    args = parser.parse_args()

    runs = load_runs(DEFAULT_RUN_TABLE, args.dataset_id)
    target_dir = target_dir_for(args.dataset_id)

    if args.make_dirs:
        target_dir.mkdir(parents=True, exist_ok=True)

    print(f"# Dataset: {args.dataset_id}")
    print(f"# Target directory: {target_dir}")
    print(f"# Runs: {', '.join(row['run_accession'] for row in runs)}")
    print("")

    if args.mode == "prefetch":
        print_prefetch_commands(runs, target_dir)
    else:
        print_ena_commands(runs, target_dir)


if __name__ == "__main__":
    main()
