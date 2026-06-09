# First-Pass Wolffia Mapping Notes

## Purpose

This document completes the third early Phase 1 step: adding first-pass Wolffia mapping notes for the candidate cell programs.

These notes are intentionally conservative. They do not claim that exact one-to-one orthologs or exact cell types have already been proven. They summarize what seems biologically plausible enough to guide prediction building.

## Mapping Confidence Scale

- `high`: expected to be broadly conserved and interpretable even before exact locus-level mapping
- `medium`: plausible and useful at the gene-family or pathway level, but still needs ortholog confirmation
- `low`: biologically interesting but currently speculative in Wolffia

## Program-Level Assessment

### 1. Proliferative / Meristematic Programs

Current support:

- strong at the gene-family level
- basic cell-cycle machinery should be conserved in any actively growing flowering plant

Useful reference markers:

- `CYCB1;1`
- `PCNA`
- histone / replication-associated genes

First-pass Wolffia expectation:

- very likely present
- likely one of the clearest early programs in future SMART-seq data

Interpretation:

- if this program is not detectable, either the sampled material lacked actively dividing cells or the annotation / QC pipeline missed a proliferative population

Mapping confidence:

- medium to high

### 2. Photosynthetic / Assimilation Programs

Current support:

- strong at the pathway level
- Wolffia is a photosynthetic plant with an extremely reduced body plan, so photosynthetic signatures are expected even if cell-type resolution is modest

Useful reference markers:

- `LHCB` family
- `RBCS` family
- broader chloroplast / photosystem programs

First-pass Wolffia expectation:

- very likely present
- may appear as one dominant assimilation state or as several related states

Interpretation:

- if this program is broad and diffuse rather than sharply clustered, that still fits the biology of a small simplified plant body

Mapping confidence:

- medium to high

### 3. Vascular-Like / Transport Programs

Current support:

- plausible but less certain as a discrete program
- this is one of the most interesting tests of hidden cellular complexity in Wolffia

Useful reference markers:

- `SUC2`
- `SWEET` family members
- cell-wall or transport specialization genes such as `CESA7` / `IRX3`

First-pass Wolffia expectation:

- transport-associated genes may be present
- the key uncertainty is whether they define a distinct cluster, a weak subpopulation, or a merged multifunctional state

Interpretation:

- a merged transport signature would support the idea that morphological reduction compressed several canonical plant programs into fewer states

Mapping confidence:

- medium

### 4. Developmental Transition Programs

Current support:

- conceptually strong
- exact marker transfer is less clean than for photosynthesis or cell cycle

Useful reference markers:

- `PLT` family
- `SCR`
- auxin-responsive modules such as `IAA19`

First-pass Wolffia expectation:

- likely visible as gradients or partial continua rather than crisp cluster-specific markers

Interpretation:

- this category directly tests the hypothesis that Wolffia may have fewer sharply separated cell identities and more transitional organization

Mapping confidence:

- medium for the pathway logic
- low to medium for exact gene-level transfer

### 5. Epidermal / Surface Identity Programs

Current support:

- plausible but currently lower confidence than the top four categories

Useful reference markers:

- `ATML1`
- `PDF` family markers

First-pass Wolffia expectation:

- possible surface-associated signal
- may be subtle if body-plan reduction weakens layer-specific specialization

Interpretation:

- worth tracking, but not a good place to over-interpret early clusters

Mapping confidence:

- low to medium

### 6. Reproductive / Floral Programs

Current support:

- biologically important but likely rare in baseline vegetative material

Useful reference markers:

- `AP1`
- `LFY`

First-pass Wolffia expectation:

- absent in many datasets
- condition-specific if detected at all

Interpretation:

- failure to detect this program would not be surprising and should not count as a negative result

Mapping confidence:

- low

### 7. Aquatic Adaptation / Stress-Responsive Programs

Current support:

- potentially novel and important
- much harder to define with standard Arabidopsis cell labels alone

Useful reference markers:

- aquaporin families
- redox / ROS response modules
- duckweed comparative stress and transport signatures

First-pass Wolffia expectation:

- more likely to behave as condition-responsive states than as classic stable cell types

Interpretation:

- this is a major opportunity for genuinely new biology, but also a place where false certainty would be risky

Mapping confidence:

- low to medium

## Ranked Summary for Immediate Prediction Work

Most ready for first-pass prediction:

1. proliferative / meristematic
2. photosynthetic / assimilation
3. vascular-like / transport
4. developmental transition

Worth tracking, but lower-confidence for immediate interpretation:

1. epidermal / surface identity
2. aquatic adaptation / stress-responsive
3. reproductive / floral

## Bottom Line

At this stage, the project already supports a credible first-pass claim:

`Wolffia australiana` is likely to retain strongly conserved proliferative and photosynthetic programs, may show partially merged transport-associated and developmental transition programs, and may contain aquatic or reduced-body-plan states that do not map neatly onto canonical Arabidopsis cell labels.
