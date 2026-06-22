# Root-Derived Reference Update

We tested whether the dominant stress-like transfer pattern was mainly caused by the current training reference rather than by the target datasets themselves.

## What Changed

Instead of training on the callus dataset `GSE227564`, we:

1. converted `GSE123818 WT` into a local `.h5ad`
2. clustered it with [scripts/17_cluster_public_reference.py](../scripts/17_cluster_public_reference.py)
3. assigned broad programs to `WT` clusters by marker-score dominance
4. used that clustered root atlas as the new training reference

New configs:

- [config/public_reference_gse123818_wt_train_to_shr.yaml](../config/public_reference_gse123818_wt_train_to_shr.yaml)
- [config/public_reference_gse123818_wt_train_to_gse121619.yaml](../config/public_reference_gse123818_wt_train_to_gse121619.yaml)

## Main Comparison

### Old reference: callus -> root atlas

`GSE227564 callus -> GSE123818 WT`

- stress-like: `95.17%`
- developmental transition: `2.57%`
- proliferative: `1.33%`

`GSE227564 callus -> GSE123818 SHR`

- stress-like: `94.45%`
- photosynthetic: `3.28%`
- developmental transition: `1.91%`

### New reference: root WT -> root targets

`GSE123818 WT -> GSE123818 SHR`

- stress-like: `50.23%`
- photosynthetic: `29.75%`
- reproductive/floral: `13.01%`
- proliferative: `7.01%`

`GSE123818 WT -> GSE121619`

- proliferative: `52.20%`
- stress-like: `40.50%`
- reproductive/floral: `7.05%`
- photosynthetic: `0.25%`

## Marker-Refinement Rerun

We then refined the broad-program marker panel to make it more root-aware and tightened the cluster pseudo-label thresholds:

- expanded proliferative markers
- expanded vascular markers
- expanded developmental-transition markers
- replaced weak epidermal markers with more root-relevant epidermal markers
- expanded stress markers
- required a minimum top score of `0.05`
- required a minimum score margin of `0.02`

### Refined `WT -> SHR`

- stress-like: `93.81%`
- proliferative: `6.19%`

### Refined `WT -> GSE121619`

- stress-like: `76.75%`
- proliferative: `23.25%`

### What improved

- spurious `reproductive_or_floral` transfer disappeared
- spurious photosynthetic transfer into root-heavy targets disappeared
- low-signal or ambiguous training clusters were more often marked `unmapped`

### What got worse

- the dominant stress-like mapping returned strongly
- root-state diversity became less visible in the final transfer output

This means the stricter thresholds helped remove obvious annotation artifacts, but the current `aquatic_adaptation_or_stress` module is still too broad and is capturing too much of the root atlas.

## Interpretation

This is the clearest sign yet that the original stress-dominant outcome was heavily influenced by the training reference.

Moving from a callus reference to a root-derived reference:

- sharply reduced the near-total stress collapse in `GSE123818 SHR`
- changed the cross-study `GSE121619` transfer from mostly stress-like to a mixed proliferative-plus-stress pattern
- showed that training context matters at least as much as target-dataset identity

## What It Does Not Mean Yet

This does **not** mean the current broad labels are already biologically correct.

There are still signs that the marker system is too coarse:

- `reproductive_or_floral` appears in root datasets, which is unlikely to be literal
- `developmental_transition` remains underused
- several root identities are still being compressed into a few broad programs
- the current stress module likely mixes water transport / membrane-interface biology with genuine abiotic-stress response

## Practical Conclusion

The project has now passed an important checkpoint:

> the framework is sensitive to reference choice, so improving the reference can materially improve predictions

That is good news for the Wolffia direction, because it means we are not locked into the original stress-heavy outcome.

## Best Next Move

The next high-value step is to refine the marker panel and broad program ontology for root biology, especially:

- proliferative / meristematic
- vascular / transport
- epidermal / surface
- developmental transition
- stress response

The most specific next move is now:

1. split `aquatic_adaptation_or_stress` into a narrower abiotic-stress program and a separate transport / interface-oriented program
2. rerun the same root-derived reference tests
3. only then move on to Wolffia prediction transfer
