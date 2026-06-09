# Dataset Inventory

## Purpose

This table is the working inventory for public reference datasets and Wolffia-related resources that will support a prediction-first cell atlas project.

Use it to track:

- reference single-cell datasets
- Wolffia genome and annotation resources
- duckweed comparative transcriptomic resources
- whether each resource is ready for marker transfer, ortholog mapping, or hypothesis generation

## Column Definitions

- `resource_name`: short name of the dataset, paper, or resource
- `species`: organism represented by the resource
- `resource_type`: for example `scRNA-seq`, `genome`, `annotation`, `bulk RNA-seq`, `review`
- `source_database`: GEO, SRA, ENA, journal supplement, project website, and so on
- `accession_or_doi`: accession number or DOI
- `developmental_context`: tissue, stage, treatment, or system
- `annotation_quality`: `high`, `medium`, `low`, or `unknown`
- `planned_use`: how we expect to use the resource
- `status`: `to review`, `in review`, `usable`, or `not prioritized`
- `notes`: any caveats, questions, or next actions

## Working Table

| resource_name | species | resource_type | source_database | accession_or_doi | developmental_context | annotation_quality | planned_use | status | notes |
|---|---|---|---|---|---|---|---|---|---|
| Arabidopsis reference atlas A | Arabidopsis thaliana | scRNA-seq | GEO / journal supplement | exact accession pending | root or whole-seedling atlas preferred | unknown | primary marker transfer reference | in review | first target for systematic search; exact accession still needs verification |
| Arabidopsis reference atlas B | Arabidopsis thaliana | scRNA-seq | GEO / journal supplement | exact accession pending | developmental atlas preferred | unknown | backup / comparison reference | in review | prioritize datasets with published marker genes and metadata |
| Additional plant single-cell atlas | plant species TBD | scRNA-seq | GEO / journal supplement | exact accession pending | tissue-specific | unknown | cross-species comparison | to review | only include if annotation is clear and useful for marker transfer |
| Genome of the world's smallest flowering plant, Wolffia australiana, helps explain its specialized physiology and unique morphology | Wolffia australiana | genome | Communications Biology | 10.1038/s42003-021-02389-w | species-wide genome and morphology resource | medium | foundational Wolffia background; candidate genome source | usable | important starting point for morphology, genome context, and project justification |
| The genome of Wolffia australiana facilitates discovery of genetic basis for aquatic adaptation in duckweeds | Wolffia australiana | genome / annotation | The Plant Cell | 10.1093/plcell/koac068 | species-wide genome and comparative duckweed resource | medium | ortholog mapping, annotation context, aquatic adaptation interpretation | usable | high-priority paper for genome choice and comparative biology |
| Wolffia transcriptome resource | Wolffia australiana | bulk RNA-seq or transcriptome | SRA / GEO / journal supplement | exact accession pending | any available tissue or condition | unknown | expression support for predicted programs | in review | useful even without public Wolffia scRNA-seq |
| Return of the Lemnaceae: duckweed as a model plant system in the genomics and postgenomics era | duckweed / Lemnaceae | review | The Plant Cell | exact DOI pending | comparative duckweed biology | medium | broad biological and evolutionary context | usable | useful for framing Wolffia as a duckweed model system; exact DOI still needs to be filled in |
| Small but mighty: The genomics of the world's smallest flowering plants | duckweed / Wolffia | review | Current Opinion in Plant Biology | 10.1016/j.pbi.2021.102153 | comparative genomics and evolutionary reduction | high | biological interpretation and literature grounding | usable | strong review for novelty framing and comparative discussion |
| Duckweeds: Omnipresent tiny plants with profound applications in agriculture and food | duckweed / Lemnaceae | review | Plants | 10.3390/plants11121641 | comparative duckweed biology and applied context | medium | supplementary background on duckweed diversity and relevance | usable | less central for cell-state prediction, but helpful for broader context |
| Nutritional value of duckweeds (Lemnaceae) as human food | duckweed / Lemnaceae | review | Frontiers in Chemistry | 10.3389/fchem.2023.1134924 | comparative duckweed physiology and composition | low | optional context only | not prioritized | not directly useful for cell-state prediction, but relevant for duckweed background |

## Near-Term Goals

### Goal 1

Fill in at least 3 strong public plant single-cell references.

### Goal 2

Identify the exact Wolffia genome and annotation resources we will use in the pipeline.

### Goal 3

Add at least 2 duckweed comparative resources that help interpret reduced or aquatic-specific programs.

## Completion Standard

This file becomes useful once each candidate resource has enough information for a yes/no decision about whether it belongs in the project.

## First-Pass Search Notes

- As of `2026-06-09`, a quick current search did **not** reveal an obvious public `Wolffia australiana` single-cell RNA-seq atlas.
- This means the project should continue to assume a prediction-first design unless a dedicated Wolffia single-cell dataset is identified later.
- The next search priority is to verify exact accessions for 1 to 3 public `Arabidopsis thaliana` single-cell reference atlases and any public Wolffia bulk transcriptome datasets.
