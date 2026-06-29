# Project Adaptation

Use this file when the user is working inside a specific repository or local project.

## Goal

Adapt the generic `PIP-seq` skill to the local project without assuming every project looks like this repository.

## What to inspect first

Start with the top-level project guides if they exist, such as:

- `README.md`
- `docs/README.md`
- `scripts/README.md`
- `config/README.md`
- `output/README.md`

Then locate the files actually relevant to the user request:

- protocol or wet-lab docs
- analysis scripts
- configuration files
- dataset inventories
- output or figures folders

## Routing pattern

Map the task onto one of these buckets:

1. project framing
2. experimental protocol
3. computational workflow
4. validation or debugging
5. export or reporting

Do not assume the project already has all five.

## This repository's example adaptation

In this repository, typical entrypoints are:

- project framing: `README.md`, `docs/project_progress_summary.md`, `docs/project_aims.md`
- prediction layer: `docs/prediction_framework.md`, `docs/candidate_cell_programs.md`, `docs/wolffia_mapping_notes.md`
- protocols: `docs/wolffia_data_generation_protocol.md`, `docs/wolffia_data_generation_protocol_detailed.md`
- core analysis scripts: `scripts/10_public_reference_statistical_prediction.py`, `scripts/17_cluster_public_reference.py`, `scripts/19_generate_public_reference_umaps.py`
- export scripts: `scripts/18_generate_project_progress_pdf.py`, `scripts/20_generate_wolffia_protocol_pdf.py`, `scripts/21_generate_stepwise_protocol_pdf.py`, `scripts/22_generate_plain_protocol_pdf.py`, `scripts/23_generate_protocol_docx.py`, `scripts/24_generate_detailed_protocol_pdf.py`, `scripts/25_build_pipseq_protocol_docx.py`

Treat this as an example mapping, not a required structure.
