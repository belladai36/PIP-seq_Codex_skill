# Runtime And Validation

## Python environment

For Scanpy-based scripts in this repository, use:

- `/opt/anaconda3/envs/py311/bin/python`

Base `python` or `python3` may not include the needed single-cell stack.

## Runtime notes already learned in this repo

### 1. Scanpy / Numba cache

Several Scanpy-based scripts set:

- `NUMBA_CACHE_DIR=/private/tmp/numba-cache`
- `MPLCONFIGDIR=/private/tmp/mplconfig`

This is to avoid runtime failures caused by cache writes in restricted environments.

### 2. Do not disable JIT globally

This project tested `NUMBA_DISABLE_JIT=1` and found that it made UMAP unacceptably slow on the larger public-reference workflow.

Use a writable cache directory instead of disabling JIT.

## Validation checklist

### Shell

- `bash -n scripts/*.sh`

### Python syntax

- `python3 -m py_compile scripts/*.py`

### Export scripts

Run the relevant builder and confirm the output path is written.

### Scanpy smoke tests

For a real functional check, prefer:

1. one direct import/read of a real `.h5ad`
2. one visualization script on a small real subset
3. one end-to-end public-reference prediction run if time allows

## Important current limitations

- the legacy FASTQ-to-count-matrix route still depends on missing local reference files and missing downstream Wolffia `.h5ad` checkpoints
- `scripts/00_preflight_check.py` is the honest place to see which pieces are still missing
