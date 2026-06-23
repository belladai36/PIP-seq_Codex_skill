# Wolffia First Transfer Note

## Current Working Reference Set

For the first Wolffia-facing transfer pass, we should freeze the current broad program set as:

- `proliferative_or_meristematic`
- `photosynthetic_or_assimilation`
- `vascular_like_or_transport`
- `developmental_transition`
- `epidermal_or_surface_identity`
- `reproductive_or_floral`
- `transport_interface_or_water_balance`
- `abiotic_stress_response`

## Why This Is the Right Freeze Point

The Arabidopsis tuning phase already taught us three useful things:

1. callus-trained references over-collapsed root states into a stress-like sink
2. root-derived training references are much more informative
3. splitting interface/water-balance from abiotic-stress biology gives a more believable interpretation than one monolithic stress label

At the same time, the latest reruns suggest we are reaching diminishing returns from repeatedly retuning the same broad marker table.

That means this is a good point to stop optimizing the Arabidopsis layer and start learning from Wolffia-facing transfer.

## How to Interpret the First Wolffia Pass

For the first pass, treat these labels as **transferable biological programs**, not literal one-to-one organ identities.

That matters especially for:

- `vascular_like_or_transport`
- `transport_interface_or_water_balance`
- `abiotic_stress_response`

If Wolffia cells score strongly for these programs, we should interpret them as evidence for:

- transport-associated function
- aquatic interface or water-balance regulation
- dynamic stress-response biology

and not over-claim that they correspond exactly to canonical Arabidopsis tissue classes.

## Primary Questions for the First Wolffia Transfer

1. do proliferative and photosynthetic programs remain easy to recover?
2. are transport-associated and interface-associated signals separated or merged?
3. do developmental signals appear as gradients rather than clean clusters?
4. are apparent stress-like states broad and diffuse, or confined to small subsets?
5. do any Wolffia cells remain weakly mapped or ambiguous under this improved reference?

## Practical Next Execution Step

Once the first public Wolffia dataset is locally available and converted:

1. cluster conservatively
2. compute module scores using the frozen broad program set
3. inspect whether the dominant Wolffia signals are:
   - preserved
   - reduced
   - merged
   - compressed
   - ambiguous
4. only after that decide whether another round of marker refinement is actually necessary

## Bottom Line

The Arabidopsis phase is now strong enough to support a first Wolffia-facing interpretation pass.

We should move forward with this reference set and let the Wolffia data tell us where the next refinement really belongs.
