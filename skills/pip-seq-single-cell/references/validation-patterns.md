# Validation Patterns

Use this file for code or workflow validation in `PIP-seq`-related projects.

## General validation ladder

Choose the strongest validation level that is practical:

1. static check
2. syntax check
3. unit or script smoke test
4. real-data smoke test
5. end-to-end run

State clearly which level you reached.

## Recommended checks

### Shell scripts

- `bash -n` on the affected scripts

### Python scripts

- `python3 -m py_compile` on the affected files

### Single-cell analysis code

Prefer at least one of:

- read a real count matrix or `h5ad`
- run one lightweight plotting or QC step
- run one reduced end-to-end subset if the full dataset is heavy

### Export scripts

- run the builder
- confirm the output file exists
- if layout matters, inspect the rendered result

## Environment handling

Do not assume base `python` contains `scanpy`, `anndata`, plotting backends, or document-generation libraries.

Check the local environment first and document what interpreter was actually used.

## This repository's example runtime notes

In this repository, validated Scanpy runs used:

- `/opt/anaconda3/envs/py311/bin/python`

Several scripts also used writable cache settings:

- `NUMBA_CACHE_DIR=/private/tmp/numba-cache`
- `MPLCONFIGDIR=/private/tmp/mplconfig`

Treat these as local environment notes rather than universal defaults.
