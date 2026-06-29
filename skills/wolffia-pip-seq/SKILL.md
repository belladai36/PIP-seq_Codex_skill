---
name: wolffia-pip-seq
description: Use this skill when the task is about Wolffia PIP-seq experiment planning, protocol generation, PIP-seq-aware single-cell QC/interpretation, or connecting repository scripts and docs to the actual Wolffia PIP-seq workflow. Also use it when the user wants publication-grounded guidance or references for PIP-seq and Wolffia transcriptomic planning.
---

# Wolffia PIP-seq

## Overview

This skill helps Codex work on the `Wolffia australiana` project when the task is specifically about `PIP-seq`, Wolffia sample preparation, protocol drafting, repo-aware workflow guidance, or interpretation of PIP-seq-style single-cell outputs.

It is meant to keep the work tied to:

- real publications
- the current repository structure
- the actual runtime constraints already discovered in this project

## When To Use This Skill

Use this skill when the user asks for any of the following:

- a `PIP-seq` protocol or protocol revision
- Wolffia-specific experiment planning for `PIP-seq`
- interpretation of Wolffia `PIP-seq` QC, clustering, or transfer-analysis outputs
- a summary of how the repository supports the PIP-seq project
- publication-backed guidance or citations for PIP-seq and Wolffia planning
- export of Wolffia PIP-seq materials to PDF or DOCX

Do not use this skill for generic plant single-cell requests that are unrelated to Wolffia or unrelated to `PIP-seq`.

## Workflow

### 1. Start from the repository state

Before answering, read the repository-level guides that matter:

- `README.md`
- `docs/README.md`
- `scripts/README.md`
- `output/README.md`

If the task is protocol-facing, also read:

- `docs/wolffia_data_generation_protocol.md`
- `docs/wolffia_data_generation_protocol_detailed.md`

### 2. Ground scientific claims in primary literature

For publication-grounded work, read:

- `references/primary-literature.md`

Use those references for:

- what `PIP-seq` can and cannot support
- which claims are supported by Wolffia-specific publications
- what still needs confirmation from the lab, kit documentation, or core facility

### 3. Choose the right repo path

Use `references/repo-entrypoints.md` to map the task to the right files.

Typical routing:

- protocol drafting: `docs/wolffia_data_generation_protocol*.md`, `scripts/20` to `25`
- public-reference analysis: `scripts/10`, `17`, `19`
- repo/project summary: `docs/project_progress_summary.md`, `docs/project_aims.md`, `docs/prediction_framework.md`

### 4. Respect the runtime environment

For Scanpy-based scripts, do not assume base `python` is sufficient.

Use the environment guidance in:

- `references/runtime-and-validation.md`

In this repository, Scanpy-based scripts were validated with:

- `/opt/anaconda3/envs/py311/bin/python`

### 5. Validate before claiming success

When editing or extending code, validate at the right level:

- shell scripts: `bash -n`
- Python scripts: `python3 -m py_compile scripts/*.py`
- document/export scripts: run the generator and confirm output path is written
- Scanpy analysis scripts: prefer at least one real smoke test using the `py311` environment

Be explicit about what was fully run versus what was only syntax-checked.

## Scientific Guardrails

- Do not describe `PIP-seq` as if it were `SMART-seq`.
- Do not invent vendor- or kit-specific parameters that are not in the literature or in confirmed lab docs.
- Separate:
  - publication-backed claims
  - repository-specific conventions
  - items that still require confirmation from the lab or core
- For Wolffia protocol advice, prefer the project’s formal protocol docs plus the benchmark Wolffia paper rather than generic plant-language guesses.

## Export Tasks

If the task is to generate shareable protocol materials, prefer:

- `scripts/20_generate_wolffia_protocol_pdf.py`
- `scripts/21_generate_stepwise_protocol_pdf.py`
- `scripts/22_generate_plain_protocol_pdf.py`
- `scripts/23_generate_protocol_docx.py`
- `scripts/24_generate_detailed_protocol_pdf.py`
- `scripts/25_build_pipseq_protocol_docx.py`

## References

Read these files as needed:

- `references/primary-literature.md`
- `references/repo-entrypoints.md`
- `references/runtime-and-validation.md`
