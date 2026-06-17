# Wolffia Next Step: Downloads

## Recommended immediate target

Start with the **four scRNA-seq runs** from `PRJNA1124135_scRNA` only:

- `SRR29417746` `Dawn1`
- `SRR29417745` `Dawn2`
- `SRR29417744` `Dusk1`
- `SRR29417743` `Dusk2`

This is the smallest and most relevant first training set for a Wolffia-native reference.

## Why not download everything first

- `PRJNA1124135` also contains bulk RNA-seq runs
- `PRJNA809022` contains 18 large snRNA-seq runs
- downloading everything at once will create a lot of overhead before we have validated the first intake path

So the efficient sequence is:

1. four `PRJNA1124135` scRNA runs
2. generate counts or a matrix
3. test the Wolffia prep path
4. only then expand to `PRJNA809022`

## Helper script

Use:

[scripts/13_wolffia_download_helper.py](/Users/bella/Documents/Wolffia%20Single-Cell%20Atlas%20Pipeline%20Before%20the%20Data%20Arrive/scripts/13_wolffia_download_helper.py)

### Example

```bash
python scripts/13_wolffia_download_helper.py --dataset-id PRJNA1124135_scRNA --make-dirs
```

That prints download commands and creates the target local directory:

```text
data/public_references/raw/PRJNA1124135/scRNA_seq/
```

## Expected output files after download

```text
data/public_references/raw/PRJNA1124135/scRNA_seq/
  SRR29417743_1.fastq.gz
  SRR29417743_2.fastq.gz
  SRR29417744_1.fastq.gz
  SRR29417744_2.fastq.gz
  SRR29417745_1.fastq.gz
  SRR29417745_2.fastq.gz
  SRR29417746_1.fastq.gz
  SRR29417746_2.fastq.gz
```

## After download

The next project step will be:

1. generate a count matrix from the four scRNA runs
2. update the manifest entry for `PRJNA1124135_scRNA`
3. convert the processed matrix into:

```text
data/public_references/processed/PRJNA1124135_wolffia_time_of_day.h5ad
```

4. cluster and annotate the Wolffia reference
