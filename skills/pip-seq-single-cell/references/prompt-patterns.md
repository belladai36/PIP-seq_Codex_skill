# Prompt Patterns

Use this file when the request is clearly about `PIP-seq` but the user has not yet phrased the task in a way that naturally maps onto a workflow.

## 1. Protocol drafting

Typical requests:

- "Help me design a PIP-seq experiment"
- "Write a protocol for this plant"
- "What should we do before sequencing?"

Default response shape:

1. define scope
2. separate platform mechanics from organism-specific assumptions
3. identify pilot variables
4. state required validation or go/no-go checkpoints

## 2. Computational workflow planning

Typical requests:

- "Build a pipeline for this dataset"
- "How should we analyze the data when it arrives?"
- "What should the workflow be from FASTQ to annotation?"

Default response shape:

1. data inputs and metadata
2. preprocessing and QC
3. dimensionality reduction and clustering
4. annotation strategy
5. validation and robustness checks
6. expected outputs and figures

## 3. QC or result interpretation

Typical requests:

- "How do I read this UMAP?"
- "What does this cluster separation mean?"
- "Is this a stress signal or a cell type?"

Default response shape:

1. describe what the plot shows
2. separate technical and biological explanations
3. identify confounders
4. suggest the next disambiguating analysis

## 4. Cross-species transfer or prediction

Typical requests:

- "Can we train on Arabidopsis and predict on another plant?"
- "How do we map programs into Wolffia?"
- "How do we decide whether programs are preserved or compressed?"

Default response shape:

1. define reference programs conservatively
2. explain orthology or marker-transfer limits
3. distinguish preserved, merged, weak, and ambiguous mappings
4. tie predictions to future validation experiments

## 5. Repository adaptation

Typical requests:

- "Can you update my repo for PIP-seq?"
- "Where should these scripts go?"
- "How do I organize this project so others can follow it?"

Default response shape:

1. inspect current layout
2. preserve local naming conventions when reasonable
3. separate core analysis, protocol docs, references, and exports
4. validate changed scripts or document builders
