# GSE123818 Validation Run Summary

We added `GSE123818` as a broader Arabidopsis root-atlas validation target to test whether the current transfer behavior is specific to earlier validation sets or is a more general feature of the present training setup.

## What We Added

- [scripts/16_prepare_gse123818_h5ad.py](../scripts/16_prepare_gse123818_h5ad.py)
- [config/public_reference_gse123818.yaml](../config/public_reference_gse123818.yaml)
- [config/public_reference_gse123818_shr.yaml](../config/public_reference_gse123818_shr.yaml)
- source dataset: [GSE123818](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE123818)

The GEO supplementary files used here were:

- `GSE123818_Root_single_cell_wt_datamatrix.csv.gz`
- `GSE123818_Root_single_cell_shr_datamatrix.csv.gz`

Both were converted locally into `.h5ad` files:

- `data/public_references/processed/GSE123818_wt_root.h5ad`
- `data/public_references/processed/GSE123818_shr_root.h5ad`

## Atlas Size

- `WT`: 4,727 cells x 27,629 genes
- `SHR`: 1,099 cells x 27,629 genes

The test datasets were treated as unlabeled transfer targets because the processed GEO matrices provide barcode-level cells but not ready-to-use broad cell-type labels in the matrix itself.

## Prediction Results

### WT split

Output directory: `results/public_reference_gse123818`

Predicted broad programs across 3,000 sampled target cells:

- `aquatic_adaptation_or_stress`: 2,855 cells (`95.17%`)
- `developmental_transition`: 77 cells (`2.57%`)
- `proliferative_or_meristematic`: 40 cells (`1.33%`)
- `reproductive_or_floral`: 26 cells (`0.87%`)
- `photosynthetic_or_assimilation`: 2 cells (`0.07%`)

Main figure:

- `figures/public_reference_gse123818/test_predicted_broad_program_pca.png`

### SHR split

Output directory: `results/public_reference_gse123818_shr`

Predicted broad programs across 1,099 target cells:

- `aquatic_adaptation_or_stress`: 1,038 cells (`94.45%`)
- `photosynthetic_or_assimilation`: 36 cells (`3.28%`)
- `developmental_transition`: 21 cells (`1.91%`)
- `reproductive_or_floral`: 3 cells (`0.27%`)
- `proliferative_or_meristematic`: 1 cell (`0.09%`)

Main figure:

- `figures/public_reference_gse123818_shr/test_predicted_broad_program_pca.png`

## Interpretation

This broader developmental atlas gave essentially the same high-level outcome as our earlier validation runs:

1. the large majority of cells map into `aquatic_adaptation_or_stress`
2. only a small minority map into developmental or proliferative programs
3. this pattern holds in both `WT` and `SHR`

That makes the current result harder to explain as a quirk of only one validation accession.

## What This Likely Means

At this stage, the most reasonable interpretation is not that Arabidopsis roots are literally dominated by an aquatic/stress program. Instead, the result suggests that our current training system is still too coarse or too mismatched:

- the training reference (`GSE227564` callus) is not an ideal developmental root reference
- the current broad marker programs are still over-weighting a stress-like axis
- cross-dataset transfer is therefore collapsing many root states into one dominant bucket

## Practical Conclusion

`GSE123818` was still worth adding because it answered an important control question:

> the dominant stress-like mapping is probably a property of the current transfer framework, not just a property of one small validation dataset

That gives us a clear next modeling move:

1. strengthen the reference system with a more developmentally resolved Arabidopsis training set
2. refine the broad program marker table so developmental root identities are better represented
3. then ask whether Wolffia looks preserved, reduced, compressed, or ambiguous relative to that improved reference
