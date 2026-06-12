# Professor Introduction Script

## Brief Project Introduction

- I wanted to give you a short update on the computational side of my proposed *Wolffia australiana* single-cell atlas project.

- The project is motivated by a core biological question:
  - because *Wolffia* has such a simplified plant body, does it also have a simplified cellular organization,
  - or does it still retain major flowering-plant transcriptional programs in a more compressed or merged form?

- Since the real *Wolffia* SMART-seq data have not arrived yet, I used public Arabidopsis single-cell datasets as a proof of concept so I could build and test the computational workflow in advance.

## Project Aim

- The long-term aim is to build a computational workflow that can be directly applied to future *Wolffia* single-cell data.

- More specifically, the project is meant to:
  - process single-cell RNA-seq data from raw or semi-processed inputs,
  - identify broad transcriptional programs,
  - test whether those programs transfer across datasets,
  - and prepare a framework for future hypothesis generation in *Wolffia*.

- In the long term, this should support a preliminary *Wolffia* cell atlas and help prioritize which biological programs or cell states deserve the most attention once the real sequencing data are available.

## Brief Workflow Overview

- The full workflow currently has two connected parts.

### Part 1: Future SMART-seq Analysis Scaffold

- This is the pipeline intended for the future *Wolffia* data.

- It is designed to go from:
  - raw FASTQ files,
  - to read-level quality control,
  - to alignment,
  - to count matrix generation,
  - to downstream single-cell analysis in Scanpy.

- The downstream analysis includes:
  - cell quality control,
  - normalization,
  - highly variable gene selection,
  - PCA,
  - clustering,
  - marker-gene analysis,
  - annotation,
  - and robustness checks.

### Part 2: Public Reference Prediction Workflow

- This is the part I have already tested using Arabidopsis public data.

- In this workflow:
  - one dataset is treated as a labeled training reference,
  - a second dataset is treated as an unlabeled target,
  - the model learns transcriptional patterns from the training set,
  - and then predicts which broad programs appear in the target dataset.

- This gives me a practical way to test the computational logic now, before the real *Wolffia* data arrive.

## Main Talking Points

- So far, I have completed three practical pieces:
  - a reproducible project structure in GitHub and PyCharm,
  - a preprocessing and analysis scaffold for future SMART-seq data,
  - and a first public-reference transfer workflow using Arabidopsis datasets.

- For the public-reference test, I used two Arabidopsis datasets:
  - `GSE227564_callus.h5ad` as the labeled training dataset,
  - `GSE141730_root_phosphate.h5ad` as the unlabeled test dataset.

- In the current workflow, the labeled training dataset teaches the model broad transcriptional patterns, and the unlabeled test dataset is used to ask whether those patterns can be recognized in a different Arabidopsis context.

- That means the current result is best interpreted as **transfer of transcriptional programs**, not yet definitive cell-type annotation.

- This is useful because it lets me test the computational framework now, before the real *Wolffia* data arrive.

- At this stage, I can already generate:
  - processed `.h5ad` reference files,
  - prediction summaries,
  - and visualization outputs from the public datasets.

- The next steps I see are:
  - improving the biological interpretation of the transferred programs,
  - deciding whether I want more comparable Arabidopsis references,
  - and then adapting the same workflow to *Wolffia* when the SMART-seq data become available.

## Very Short Version

- I built the initial computational framework for a future *Wolffia* single-cell atlas project.

- Since the *Wolffia* data are not available yet, I tested the workflow on two public Arabidopsis single-cell datasets.

- I processed the public datasets into analysis-ready `.h5ad` files, ran a labeled-to-unlabeled prediction workflow, and generated summary tables and visualization outputs.

- So the project is now at the stage of a working computational scaffold rather than final *Wolffia* biological results.

## What Has Already Been Processed

- Public dataset downloads:
  - `GSE227564` callus counts plus metadata
  - `GSE141730` root/phosphate 10x matrix

- Prepared analysis-ready files:
  - `GSE227564_callus.h5ad`
  - `GSE141730_root_phosphate.h5ad`

- Workflow outputs:
  - prediction metrics
  - predicted label counts
  - scored output `.h5ad` files
  - PCA visualizations

## Example Dataset Samples

### Training Dataset Sample

The labeled training dataset contains per-cell metadata such as sequencing depth, feature counts, and cluster assignments. A few example rows are:

| cell_id | orig.ident | nCount_RNA | nFeature_RNA | seurat_clusters |
|---|---:|---:|---:|---:|
| `facs_wt04_ATCAATCCTATCTGC` | `f_wt4` | 74161 | 9983 | 0 |
| `facs_wt04_CAGAGCGGCAGTGTT` | `f_wt4` | 91695 | 11369 | 0 |
| `facs_wt04_GTTGCATGGCGCACA` | `f_wt4` | 57552 | 10137 | 0 |
| `facs_wt04_GGATCACCTATGCGG` | `f_wt4` | 64117 | 10465 | 14 |
| `facs_wt04_AACGAGTATGCTCAA` | `f_wt4` | 62154 | 10328 | 11 |

### Test Dataset Gene Annotation Sample

The unlabeled test dataset stores genes and gene IDs that are then used for normalization and prediction transfer. A few example rows are:

| gene_name | gene_id |
|---|---|
| `NAC001` | `AT1G01010` |
| `ARV1` | `AT1G01020` |
| `AT1G03987` | `AT1G03987` |
| `NGA3` | `AT1G01030` |
| `DCL1` | `AT1G01040` |

## Current Output Summary

- Training cells used in the current prediction run: `1500`
- Test cells used in the current prediction run: `2000`
- Shared highly variable genes used by the classifier: `2000`
- Training labels currently used: clusters `0` through `18`
- The target dataset is currently treated as **unlabeled**

The predicted label counts in the test dataset currently begin like this:

| predicted_broad_program | n_cells |
|---|---:|
| `5` | 475 |
| `3` | 438 |
| `12` | 416 |
| `0` | 163 |
| `6` | 155 |
| `1` | 123 |
| `2` | 63 |
| `13` | 38 |
| `11` | 26 |
| `8` | 25 |

## Visualization Guide

### 1. Training PCA

![Training PCA](../figures/public_reference/train_broad_program_pca.png)

- **What this graph is:** a PCA plot of the training dataset.
- **What each point means:** one cell from the labeled Arabidopsis training reference.
- **What the colors mean:** the training labels used for learning the transcriptional patterns.
- **How to interpret it:** if colored groups separate into recognizable clouds, the training dataset contains structure that the model can learn from.
- **Why it matters for the project:** this tells us whether the reference dataset is coherent enough to support downstream transfer into another dataset.

### 2. Training Program-Score Heatmap

![Training Program Heatmap](../figures/public_reference/train_program_score_heatmap.png)

- **What this graph is:** a heatmap of average program or marker scores across labeled training groups.
- **Rows:** training groups.
- **Columns:** marker programs being scored.
- **How to interpret it:** stronger color means a group has stronger expression of a given marker program.
- **Why it matters for the project:** this checks whether the reference groups are biologically meaningful rather than just technical clusters.

### 3. Training Program-Score Boxplots

![Training Program Boxplots](../figures/public_reference/train_program_score_boxplots.png)

- **What this graph is:** boxplots showing the spread of marker or program scores in the training dataset.
- **How to interpret it:** if one group has clearly higher values for a score than others, that score is useful for distinguishing that group.
- **Why it matters for the project:** this helps show whether the marker-based programs are broad and overlapping or relatively well separated.

### 4. Test Prediction PCA

![Predicted Test PCA](../figures/public_reference/test_predicted_broad_program_pca.png)

- **What this graph is:** a PCA plot of the unlabeled test dataset after prediction transfer.
- **What each point means:** one cell from the Arabidopsis target dataset.
- **What the colors mean:** predicted labels assigned by the classifier.
- **How to interpret it:** if colors occupy structured regions of the PCA space, the model is finding reproducible transcriptional programs in the new dataset.
- **Why it matters for the project:** this is the first proof-of-concept for transferring learned patterns from one plant single-cell dataset into another.

## What I Would Say About The Current Biological Meaning

- At this stage, I would interpret these outputs as **transfer of broad transcriptional programs**, not definitive cell-type annotation.

- The training dataset is Arabidopsis callus, while the test dataset is Arabidopsis root/phosphate related, so the transfer is biologically informative but not perfectly matched.

- Even so, this is already useful because it shows that the computational workflow is functioning and that plant expression programs can be learned and projected into a second dataset.

- That makes this a reasonable computational starting point for a future *Wolffia* analysis, where the main goal will be to ask whether major flowering-plant programs are preserved, merged, reduced, or novel.

## Key Terms And Simple Explanations

- **Single-cell RNA-seq**
  - A method that measures gene expression in individual cells rather than averaging across whole tissues.

- **SMART-seq**
  - A single-cell sequencing approach that captures full-length transcripts, often with one sequencing library per cell.

- **FASTQ**
  - The raw sequencing file format containing read sequences and quality scores.

- **Gene-by-cell count matrix**
  - A table with genes as rows, cells as columns, and expression counts as values.

- **Scanpy**
  - A Python analysis framework for single-cell RNA-seq data.

- **Normalization**
  - A step that makes cells more comparable when sequencing depths differ.

- **Highly variable genes**
  - Genes that vary strongly across cells and are therefore useful for capturing biological differences.

- **PCA**
  - Principal component analysis, a dimensionality-reduction method that summarizes major patterns in the data.

- **Marker genes**
  - Genes associated with specific cell states, cell types, or biological programs.

- **Labeled dataset**
  - A dataset where cells already have some group labels, such as clusters.

- **Unlabeled dataset**
  - A dataset where expression data are available but labels are not yet assigned for the current analysis.

- **Transfer learning**
  - Using patterns learned from one dataset to make predictions in another dataset.

- **Transcriptional program**
  - A coordinated pattern of gene expression linked to a biological function or cell state.

- **Cell atlas**
  - A map of cell populations or cell states in a tissue or organism.

- **`.h5ad`**
  - A standard file format for annotated single-cell data used by AnnData and Scanpy.

## Good Questions To Ask The Professor

- Does this prediction-first approach make sense as preparation for the future *Wolffia* SMART-seq data?

- Are these Arabidopsis public datasets reasonable choices for a proof-of-concept reference workflow?

- Would it be better to use more biologically matched Arabidopsis datasets before trying to generalize toward *Wolffia*?

- How cautious should I be when interpreting transferred labels as broad programs versus true cell identities?

- Which biological programs would be most important to prioritize once the real *Wolffia* data arrive?
