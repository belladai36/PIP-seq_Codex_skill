#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
skill_name="pip-seq-single-cell"
src="${repo_root}/skills/${skill_name}"
codex_home="${CODEX_HOME:-${HOME}/.codex}"
dest="${codex_home}/skills/${skill_name}"
tmp_dest="${dest}.tmp"

if [[ ! -d "${src}" ]]; then
  echo "Skill source not found: ${src}" >&2
  exit 1
fi

mkdir -p "${codex_home}/skills"
rm -rf "${tmp_dest}"
cp -R "${src}" "${tmp_dest}"
rm -rf "${dest}"
mv "${tmp_dest}" "${dest}"

echo "Installed ${skill_name} to ${dest}"
echo "Start a new Codex session and invoke it with: \$${skill_name}"
