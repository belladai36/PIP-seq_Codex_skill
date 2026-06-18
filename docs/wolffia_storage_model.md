# Wolffia Storage Model

## Purpose

Keep the project organized without trying to force very large sequencing files into GitHub.

## What belongs in GitHub

GitHub should contain:

- analysis scripts
- configuration files
- manifests and accession tables
- small metadata tables
- summary CSV outputs
- figures
- methods notes
- interpretation and result summaries

In this project, examples include:

- [scripts](/Users/bella/Documents/Wolffia%20Single-Cell%20Atlas%20Pipeline%20Before%20the%20Data%20Arrive/scripts)
- [config/config.yaml](/Users/bella/Documents/Wolffia%20Single-Cell%20Atlas%20Pipeline%20Before%20the%20Data%20Arrive/config/config.yaml)
- [data/metadata/wolffia_public_dataset_manifest.csv](/Users/bella/Documents/Wolffia%20Single-Cell%20Atlas%20Pipeline%20Before%20the%20Data%20Arrive/data/metadata/wolffia_public_dataset_manifest.csv)
- [data/metadata/wolffia_public_run_accessions.csv](/Users/bella/Documents/Wolffia%20Single-Cell%20Atlas%20Pipeline%20Before%20the%20Data%20Arrive/data/metadata/wolffia_public_run_accessions.csv)

## What should stay outside GitHub

These should live on external or cloud storage:

- raw FASTQ files
- large BAM files
- large count matrices
- bulky intermediate processing outputs
- downloaded public sequencing archives

For this project, the first four public Wolffia scRNA files alone are about **82.7 GB compressed**,
which is far beyond what should go into the Git repository.

## Recommended storage pattern

### GitHub

Use GitHub for:

- code
- documentation
- manifests
- plots
- small results

### External drive or larger storage

Use external or cloud storage for:

- `data/public_references/raw/PRJNA1124135/scRNA_seq/`
- `data/public_references/raw/PRJNA809022/snRNA_seq/`

The repo now supports this through:

- [docs/wolffia_external_storage_setup.md](/Users/bella/Documents/Wolffia%20Single-Cell%20Atlas%20Pipeline%20Before%20the%20Data%20Arrive/docs/wolffia_external_storage_setup.md)
- `WOLFFIA_PUBLIC_RAW_ROOT`
- `wolffia_public_reference_analysis.external_raw_root`

## Practical rule

If a file is so large that:

- it would noticeably strain local storage,
- it is a downloaded public archive rather than your own small derived result,
- or it is not useful for code review,

then it should not go into GitHub.

## Best workflow for this project

1. keep the repo in GitHub
2. keep raw Wolffia sequencing files on external/cloud storage
3. generate processed summaries and figures
4. commit only the compact, interpretable outputs back to GitHub
