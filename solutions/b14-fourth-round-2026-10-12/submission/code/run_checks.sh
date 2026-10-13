#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
if [[ "${PYTHONOPTIMIZE:-}" != "" && "${PYTHONOPTIMIZE:-0}" != "0" ]]; then
  echo 'Unset PYTHONOPTIMIZE: assertion checks must be active.' >&2
  exit 2
fi
${CXX:-g++} -O3 -std=c++17 code/subset_oracle.cpp -o code/subset_oracle
python code/check_modules.py
python code/check_contracted.py
python code/check_separation.py
python code/check_blocks.py
python code/verify_saved_certificates.py
python code/test_rejection_controls.py
