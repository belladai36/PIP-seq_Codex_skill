#!/usr/bin/env bash
set -euo pipefail

CONFIG="${1:-config/config.yaml}"

python - <<'PY' "$CONFIG"
import shlex
import subprocess
import sys
from pathlib import Path

import pandas as pd
import yaml

config_path = sys.argv[1]
with open(config_path, "r", encoding="utf-8") as handle:
    config = yaml.safe_load(handle)

samples = pd.read_csv(config["paths"]["sample_sheet"])
alignment_dir = Path(config["paths"]["alignment_dir"])
counts_dir = Path(config["paths"]["counts_dir"])
counts_dir.mkdir(parents=True, exist_ok=True)

gtf = Path(config["paths"]["annotation_gtf"])
if not gtf.exists():
    raise SystemExit(f"Annotation GTF not found: {gtf}")

threads = str(config["featurecounts"].get("threads", 8))
strandedness = str(config["featurecounts"].get("strandedness", 0))
paired = config["featurecounts"].get("paired_end", True)
extra = [str(x) for x in config["featurecounts"].get("extra_args", [])]

for _, row in samples.iterrows():
    cell_id = str(row["cell_id"])
    bam = alignment_dir / cell_id / f"{cell_id}.Aligned.sortedByCoord.out.bam"
    if not bam.exists():
        raise SystemExit(f"Missing aligned BAM for {cell_id}: {bam}")

    out_file = counts_dir / f"{cell_id}.featureCounts.txt"
    cmd = [
        "featureCounts",
        "-T", threads,
        "-s", strandedness,
        "-a", str(gtf),
        "-o", str(out_file),
        *extra,
    ]
    if paired:
        cmd.extend(["-p", "--countReadPairs"])
    cmd.append(str(bam))

    print("Running:", " ".join(shlex.quote(x) for x in cmd))
    subprocess.run(cmd, check=True)
PY

