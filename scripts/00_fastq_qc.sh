#!/usr/bin/env bash
set -euo pipefail

CONFIG="${1:-config/config.yaml}"

python - <<'PY' "$CONFIG"
import os
import shlex
import subprocess
import sys
from pathlib import Path

import pandas as pd
import yaml

config_path = sys.argv[1]
with open(config_path, "r", encoding="utf-8") as handle:
    config = yaml.safe_load(handle)

sample_sheet = Path(config["paths"]["sample_sheet"])
fastqc_dir = Path(config["paths"]["fastqc_dir"])
multiqc_dir = Path(config["paths"]["multiqc_dir"])
log_dir = Path(config["paths"]["log_dir"])
threads = str(config["fastq"].get("fastqc_threads", 4))

fastqc_dir.mkdir(parents=True, exist_ok=True)
multiqc_dir.mkdir(parents=True, exist_ok=True)
log_dir.mkdir(parents=True, exist_ok=True)

samples = pd.read_csv(sample_sheet)
fastqs = []
for _, row in samples.iterrows():
    fastqs.append(str(row["fastq_r1"]))
    if config["fastq"].get("paired_end", True) and pd.notna(row.get("fastq_r2")):
        fastqs.append(str(row["fastq_r2"]))

missing = [path for path in fastqs if not Path(path).exists()]
if missing:
    raise SystemExit("Missing FASTQ files:\n" + "\n".join(missing))

cmd = ["fastqc", "--threads", threads, "--outdir", str(fastqc_dir), *fastqs]
print("Running:", " ".join(shlex.quote(x) for x in cmd))
subprocess.run(cmd, check=True)

cmd = ["multiqc", str(fastqc_dir), "--outdir", str(multiqc_dir), "--filename", "multiqc_fastq_report.html"]
print("Running:", " ".join(shlex.quote(x) for x in cmd))
subprocess.run(cmd, check=True)
PY

