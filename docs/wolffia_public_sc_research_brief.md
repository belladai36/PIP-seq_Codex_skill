# Wolffia Public Single-Cell Research Brief

## Why this matters

We now know that the project does not need to start from zero. Public archives already contain
usable *Wolffia australiana* single-cell and single-nucleus RNA-seq datasets, plus broader duckweed
genome and epigenome resources that can support annotation and hypothesis generation before our own
data arrive.

Just as important, the attached PIP-seq paper gives us a strong assay-level reason to design the
pipeline as a flexible single-cell workflow rather than a SMART-seq-only workflow.

## What we verified

### 1. There is a public whole-plant *Wolffia australiana* scRNA-seq project

- **BioProject:** `PRJNA1124135`
- **Title:** `Wolffia australiana Time of Day scRNA-seq`
- **Public archive date:** June 14, 2024
- **Study-level description:** the project reports whole-plant single-cell RNA-seq and says that
  *Wolffia* resolves into **four principal clusters** representing above- and below-water
  parenchyma and epidermis, with additional time-of-day-responsive genes detectable at the cell
  level.
- **SRA experiments currently visible:** `SRX24931112` to `SRX24931115`
  - `Wa_SC_Dawn1`
  - `Wa_SC_Dawn2`
  - `Wa_SC_Dusk1`
  - `Wa_SC_Dusk2`
- **Sequencer in SRA metadata:** `NextSeq 2000`

Interpretation:

- This is the strongest starting point for our current project.
- It already suggests a biological framing we can build on:
  **a simplified organism with a small number of major transcriptional compartments, but with
  meaningful cell-specific temporal responses inside them.**

### 2. There is also a public *Wolffia australiana* single-nucleus RNA-seq project

- **BioProject:** `PRJNA809022`
- **Title:** `Wolffia australiana genome: single nucleus RNA-Seq`
- **Public archive date:** 2022
- **SRA study name:** `Wolffia australiana genome: single nucleus RNA-Seq`
- **Visible experiments in SRA:** `Waus_snRNA-Seq_1` through at least `Waus_snRNA-Seq_10`
- **Sequencer in SRA metadata:** `DNBSEQ-T7`

Interpretation:

- This is useful as a second reference dataset.
- It gives us a way to test whether broad programs are reproducible across
  **single-cell versus single-nucleus** capture.
- It may be especially useful for validating major cell programs even if its annotation is less
  polished than the 2024 time-of-day dataset.

### 3. We also have broader duckweed genomics and epigenomics resources that include *Wolffia*

- **GEO SuperSeries:** `GSE238136`
- **Linked paper:** `Duckweed genomes and epigenomes underlie triploid hybridization and clonal reproduction`
- **PubMed:** `40174586`
- The series includes *Wolffia australiana* together with other duckweeds and contains:
  - WGS
  - WGBS
  - Hi-C
  - small RNA
  - other genome/epigenome resources

Interpretation:

- This is not a replacement for single-cell expression data.
- But it is valuable for:
  - improving genome/annotation confidence,
  - cross-checking gene models,
  - and generating regulatory hypotheses once candidate cell programs are defined.

## Important caveat about "10x Genomics"

At the moment, I can confirm that public *Wolffia* **single-cell** and **single-nucleus** datasets
exist. I **cannot yet confirm from the archive metadata alone** that the public *Wolffia* datasets
used **10x Genomics chemistry specifically**.

What the public metadata clearly show is:

- `PRJNA1124135`: single-cell RNA-seq, sequenced on `NextSeq 2000`
- `PRJNA809022`: single-nucleus RNA-seq, sequenced on `DNBSEQ-T7`

So the safest wording is:

> Public *Wolffia* single-cell and single-nucleus transcriptomic datasets already exist and can be
> reused in our pipeline, but the archive metadata do not by themselves prove that all of them used
> 10x Genomics chemistry.

## What the PIP-seq paper changes for our project

### Verified points from the 2023 Nature Biotechnology paper

- **Paper:** `Microfluidics-free single-cell genomics with templated emulsification`
- **DOI:** `10.1038/s41587-023-01685-z`
- **GEO accession from the paper PDF:** `GSE202919`

Core technical points:

- PIP-seq is **microfluidics-free**
- single cells are encapsulated by **particle-templated emulsification**
- emulsification can be done with a **standard vortexer**
- it supports **large-volume tubes** and **plate-based formats**
- the paper states that **full-length cDNA is synthesized, amplified, and prepared for sequencing**
- the method is presented as flexible across low-input and large-scale settings

Why this is exciting for *Wolffia*:

- *Wolffia* is tiny, structurally reduced, and likely difficult to process in the same way as
  larger tissues
- an assay that is fast, scalable, and less dependent on specialized microfluidic hardware may be a
  particularly good fit
- if multiple time points or environmental conditions are planned, PIP-seq's plate/tube flexibility
  is a practical advantage

## What we can do with these public *Wolffia* datasets right now

### Immediate computational use

1. **Build a Wolffia-native reference before our own data arrive**
   - preprocess the public *Wolffia* scRNA/snRNA datasets
   - run QC, normalization, PCA, clustering, and marker detection
   - create a first-pass broad annotation using program-level labels

2. **Test the "compression" hypothesis directly**
   - ask whether the public *Wolffia* dataset resolves into only a few broad states
   - test whether markers from normally separate plant programs appear in the same cluster/state
   - quantify whether the dataset looks more discrete or more continuous than Arabidopsis

3. **Use Arabidopsis only as an external reference, not the whole story**
   - map Arabidopsis broad programs onto *Wolffia*
   - identify which programs transfer cleanly
   - identify which ones collapse, mix, or fail to transfer

4. **Compare scRNA and snRNA views of the same organism**
   - this is a nice built-in robustness check
   - if the same broad programs appear in both datasets, confidence increases
   - if only some programs recur, that tells us something about assay sensitivity and cell-state
     stability

## Best next predictions to test

These are the predictions I think are most worth carrying into the next phase:

### Prediction 1

*Wolffia* will show **fewer major transcriptional compartments** than Arabidopsis, but not
trivially few.

What would support this:

- a small number of dominant broad clusters
- reproducible major programs across replicates and across scRNA/snRNA datasets

### Prediction 2

Some *Wolffia* states will look **hybrid or compressed**, rather than matching canonical
Arabidopsis cell types one-to-one.

What would support this:

- mixed module scores
- weak marker specificity
- uncertain cross-species label transfer
- trajectory structures with fewer branch points

### Prediction 3

Time-of-day or aquatic-position effects may be detectable **within** a small number of broad cell
programs rather than by creating many additional cell types.

What would support this:

- the same broad cluster appearing at dawn and dusk with different DE genes
- condition-responsive substructure inside otherwise stable compartments

## Recommended next computational plan

### Phase A: public *Wolffia* dataset intake

- download `PRJNA1124135` metadata and counts if available in processed form
- download `PRJNA809022` metadata and determine the most workable entry point
- create a local manifest with:
  - accession
  - assay type
  - replicate
  - condition
  - read structure
  - reference genome/annotation used

### Phase B: first-pass Wolffia atlas

- run QC and filtering
- cluster each dataset independently
- compute marker genes
- assign broad labels conservatively:
  - epidermis-like
  - parenchyma-like
  - submerged/underwater-associated
  - proliferative/transition-like
  - stress/circadian-responsive

### Phase C: transfer and compression analysis

- project Arabidopsis program scores onto *Wolffia*
- compute mixed-program cells
- calculate separability metrics
- compare cluster structure between:
  - Arabidopsis references
  - *Wolffia* scRNA-seq
  - *Wolffia* snRNA-seq

### Phase D: prepare for our future PIP-seq data

- adapt the repository so it can support:
  - public reference analysis
  - future PIP-seq count matrices
  - future SMART-seq data if needed
- keep the analysis modular so assay-specific preprocessing is separate from downstream biology

## Recommendation for project framing

The most interesting way to position the project is:

> Use public *Wolffia* single-cell and single-nucleus datasets to build a preliminary cell-state
> map and test whether extreme morphological simplification corresponds to true loss of canonical
> plant programs or compression of those programs into fewer hybrid transcriptional states. Then use
> future PIP-seq data to validate and refine those predictions.

That framing is stronger than simply saying:

> We want to cluster Wolffia cells.

## Sources

- Nature Biotechnology PIP-seq article:
  https://www.nature.com/articles/s41587-023-01685-z
- NCBI BioProject `PRJNA1124135`:
  https://www.ncbi.nlm.nih.gov/bioproject/PRJNA1124135
- NCBI SRA study `SRP514015`:
  https://www.ncbi.nlm.nih.gov/sra/?term=SRP514015
- NCBI BioProject `PRJNA809022`:
  https://www.ncbi.nlm.nih.gov/bioproject/PRJNA809022
- NCBI GEO `GSE238136`:
  https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE238136
- PubMed `40174586`:
  https://pubmed.ncbi.nlm.nih.gov/40174586/
