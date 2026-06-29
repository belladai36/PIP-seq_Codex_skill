---
name: pip-seq-single-cell
description: Use this skill when the task is about PIP-seq or templated-emulsification single-cell experiment planning, protocol drafting, QC interpretation, analysis planning, or publication-grounded guidance for plant or related single-cell transcriptomic projects. It is especially useful when the user wants a reusable workflow that can be adapted across projects rather than tied to one repository.
---

# PIP-seq Single-Cell

## Overview

This skill helps Codex work on `PIP-seq` or related templated-emulsification single-cell projects when the task is about experiment planning, sample preparation logic, protocol drafting, QC interpretation, or publication-grounded workflow design.

It is meant to keep the work tied to:

- real publications
- clear separation between platform-level facts and project-specific assumptions
- reusable validation and analysis patterns that can be adapted to a local repository or lab workflow

## When To Use This Skill

Use this skill when the user asks for any of the following:

- a `PIP-seq` protocol or protocol revision
- plant or organism-specific experiment planning for `PIP-seq`
- interpretation of `PIP-seq` QC, clustering, annotation, or transfer-analysis outputs
- publication-backed guidance or citations for `PIP-seq` planning
- conversion of a project idea into a practical computational or experimental workflow
- adaptation of a local repository to better support a `PIP-seq` project

Do not use this skill for generic single-cell requests that are unrelated to `PIP-seq`, templated emulsification, or closely related plant single-cell workflow planning.

## Workflow

### 1. Ground the answer in primary literature first

Before making specific claims, read:

- `references/primary-literature.md`

Use those references for:

- what `PIP-seq` can and cannot support
- what claims are supported at the platform level
- which organism-specific claims come from case-study papers such as `Wolffia`
- what still needs confirmation from the lab, kit documentation, sequencing core, or species-specific literature

### 2. Decide whether the task is generic or project-local

If the user is asking about a specific repository, local scripts, or an in-progress project, read:

- `references/project-adaptation.md`

Use that file to decide:

- which local guides to inspect first
- how to separate reusable logic from repository-specific choices
- when local runtime constraints actually matter

If the user is not working from a specific repository, stay at the generic workflow level and do not invent local paths or environment assumptions.

### 3. Use a portable validation pattern

Use:

- `references/validation-patterns.md`

When editing or extending code, validate at the right level for the current project:

- shell scripts: `bash -n`
- Python scripts: `python3 -m py_compile` on the affected files or package
- document/export scripts: run the generator and confirm the output path is written
- single-cell analysis scripts: prefer at least one real smoke test on a real `h5ad` or count matrix when feasible

Be explicit about what was fully run versus what was only syntax-checked.

### 4. Add optional organism-specific context only when needed

If the task is specifically about `Wolffia`, use:

- `references/wolffia-case-study.md`

Treat it as an example adaptation layer, not as a universal rule for all `PIP-seq` projects.

## Scientific Guardrails

- Do not describe `PIP-seq` as if it were `SMART-seq`.
- Do not invent vendor- or kit-specific parameters that are not in the literature or in confirmed lab docs.
- Separate:
  - publication-backed claims
  - project-specific conventions
  - items that still require confirmation from the lab or core
- Do not assume a species-specific dissociation method transfers cleanly across plant systems.
- If using Wolffia as an example, label it clearly as a case study rather than a default standard for other organisms.

## Common Task Shapes

### Protocol drafting

- start with platform mechanics from the `PIP-seq` paper
- add species or tissue-specific handling only from credible organism papers or confirmed lab practice
- explicitly mark unresolved parameters that require pilot optimization

### Computational analysis planning

- frame the workflow from raw data to QC, dimensionality reduction, clustering, annotation, and cross-dataset validation
- if the dataset is cross-species or non-model, make orthology and annotation uncertainty explicit
- distinguish exploratory outputs from validated biological conclusions

### Repository adaptation

- first identify existing project structure
- then map where protocol docs, analysis scripts, configs, and outputs live
- only after that propose repository-specific commands or paths

## Optional Project Exports

If the current repository already contains export scripts, use the local project-adaptation guide to find them. Do not assume all projects will have the same filenames or output builders.

## References

Read these files as needed:

- `references/primary-literature.md`
- `references/project-adaptation.md`
- `references/validation-patterns.md`
- `references/wolffia-case-study.md`
