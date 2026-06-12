# Wolffia Project Update With Figures

## Brief Project Introduction

- This project is a computational preparation step for a future single-cell RNA-seq study of *Wolffia australiana*.
- *Wolffia* is an attractive system because it has an extremely simplified plant body, which raises an interesting biological question:
  - does its simplified morphology correspond to a simplified cellular organization,
  - or are major flowering-plant transcriptional programs still present but compressed into fewer or less distinct states?
- Since the real *Wolffia* SMART-seq data have not arrived yet, I am using public Arabidopsis single-cell datasets to build and test the computational workflow in advance.

## Project Aim

- The main aim is to create a workflow that can later be applied directly to *Wolffia* single-cell data.
- More specifically, the project is meant to:
  - prepare and organize single-cell datasets,
  - identify broad transcriptional programs,
  - test whether those programs transfer across datasets,
  - and build a framework for future hypothesis generation in *Wolffia*.
- In the long term, this should support a preliminary *Wolffia* cell atlas and help guide which biological programs or cell states should be prioritized once the real sequencing data are available.

## Brief Workflow Overview

- The full computational workflow has two connected parts.

### Part 1: Future SMART-seq Analysis Scaffold

- This is the workflow intended for the future *Wolffia* data.
- It is designed to run from:
  - raw FASTQ files,
  - to read-level quality control,
  - to alignment,
  - to count matrix generation,
  - to downstream single-cell analysis in Scanpy.
- The downstream steps include:
  - cell quality control,
  - normalization,
  - highly variable gene selection,
  - PCA,
  - clustering,
  - marker analysis,
  - annotation,
  - and robustness checks.

### Part 2: Public Reference Prediction Workflow

- This is the part I have already tested using Arabidopsis public data.
- In this workflow:
  - one dataset is treated as a labeled training reference,
  - a second dataset is treated as an unlabeled target,
  - the model learns transcriptional patterns from the training set,
  - and then predicts which broad programs appear in the target dataset.
- This gives me a practical way to test the computational logic now, before *Wolffia* data arrive.

## Main Point

- I am building a computational single-cell RNA-seq workflow for a future *Wolffia australiana* cell atlas.
- Because the real *Wolffia* SMART-seq data are not available yet, I tested the workflow on public Arabidopsis datasets.
- The current result is a working proof of concept for:
  - reference preparation,
  - program scoring,
  - labeled-to-unlabeled prediction transfer,
  - and basic visualization.

## What I Have Processed So Far

- I downloaded and prepared two public Arabidopsis datasets:
  - `GSE227564_callus.h5ad` as the labeled training dataset
  - `GSE141730_root_phosphate.h5ad` as the unlabeled test dataset

- I ran a prediction workflow that:
  - learns patterns from the labeled training set,
  - applies them to the unlabeled test set,
  - and summarizes the transferred patterns with tables and figures.

- Current run summary:
  - training cells used: `1500`
  - test cells used: `2000`
  - genes used by the classifier: `2000`
  - prediction mode: labeled train set to unlabeled target set

## Small Dataset Samples

### Training Dataset Sample

| cell_id | orig.ident | nCount_RNA | nFeature_RNA | seurat_clusters |
|---|---:|---:|---:|---:|
| `facs_wt04_ATCAATCCTATCTGC` | `f_wt4` | 74161 | 9983 | 0 |
| `facs_wt04_CAGAGCGGCAGTGTT` | `f_wt4` | 91695 | 11369 | 0 |
| `facs_wt04_GTTGCATGGCGCACA` | `f_wt4` | 57552 | 10137 | 0 |
| `facs_wt04_GGATCACCTATGCGG` | `f_wt4` | 64117 | 10465 | 14 |
| `facs_wt04_AACGAGTATGCTCAA` | `f_wt4` | 62154 | 10328 | 11 |

### Test Dataset Gene Sample

| gene_name | gene_id |
|---|---|
| `NAC001` | `AT1G01010` |
| `ARV1` | `AT1G01020` |
| `AT1G03987` | `AT1G03987` |
| `NGA3` | `AT1G01030` |
| `DCL1` | `AT1G01040` |

## Graphs And How To Read Them

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

### 4. Predicted PCA On The Test Dataset

![Predicted Test PCA](../figures/public_reference/test_predicted_broad_program_pca.png)

- **What this graph is:** a PCA plot of the unlabeled test dataset after prediction transfer.
- **What each point means:** one cell from the Arabidopsis target dataset.
- **What the colors mean:** predicted labels assigned by the classifier.
- **How to interpret it:** if colors occupy structured regions of the PCA space, the model is finding reproducible transcriptional programs in the new dataset.
- **Why it matters for the project:** this is the first proof-of-concept for transferring learned patterns from one plant single-cell dataset into another.

## Current Prediction Summary

Top predicted label counts in the test dataset:

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

## What I Would Say About The Current Biological Meaning

- At this stage, I would interpret these outputs as **transfer of broad transcriptional programs**, not definitive cell-type annotation.
- The training dataset is Arabidopsis callus, while the test dataset is Arabidopsis root/phosphate related, so the transfer is biologically informative but not perfectly matched.
- Even so, this is already useful because it shows that the computational workflow is functioning and that plant expression programs can be learned and projected into a second dataset.
- That makes this a reasonable computational starting point for a future *Wolffia* analysis, where the main goal will be to ask whether major flowering-plant programs are preserved, merged, reduced, or novel.

## Key Terms

- **Single-cell RNA-seq**
  - Measures gene expression in individual cells.

- **SMART-seq**
  - A full-length single-cell sequencing approach, often one library per cell.

- **PCA**
  - Principal component analysis, a way to summarize large gene-expression datasets into a few major axes.

- **Labeled training dataset**
  - A dataset where cells already have assigned groups that the model can learn from.

- **Unlabeled test dataset**
  - A dataset where the cells do not yet have labels in the current workflow, so the model predicts them.

- **Transcriptional program**
  - A coordinated gene-expression pattern linked to a biological function or cell state.

- **Transfer learning**
  - Learning patterns in one dataset and using them to make predictions in another dataset.

## Questions I Would Ask For Feedback

- Is this a reasonable proof-of-concept strategy before the real *Wolffia* data arrive?
- Would it be better to use more biologically matched Arabidopsis reference datasets?
- How conservative should I be when interpreting transferred labels as broad programs versus true cell identities?
- Which biological programs should be highest priority once the real *Wolffia* SMART-seq data become available?
