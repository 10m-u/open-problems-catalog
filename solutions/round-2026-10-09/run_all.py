#!/usr/bin/env python3
"""Run this round's exact controls; only the Python standard library is needed."""

import hashlib
import json
from pathlib import Path
import subprocess
import sys


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    round_dir = Path(__file__).resolve().parent
    repo = round_dir.parents[1]
    manifest = json.loads((round_dir / "RESULTS.json").read_text())
    checker_certificates = {}
    for result in manifest["results"]:
        checker_certificates.setdefault(result["checker"], set()).add(result["certificate"])
    records = []
    for checker, certificates in sorted(checker_certificates.items()):
        completed = subprocess.run(
            [sys.executable, str(round_dir / checker)],
            cwd=repo, text=True, capture_output=True,
        )
        if completed.returncode:
            sys.stdout.write(completed.stdout)
            sys.stderr.write(completed.stderr)
            raise SystemExit(f"FAILED: {checker} (exit {completed.returncode})")
        records.append({
            "checker": checker,
            "checker_sha256": digest(round_dir / checker),
            "exit_code": completed.returncode,
            "certificates": {name: digest(round_dir / name) for name in sorted(certificates)},
        })
        print(f"PASS {checker}", flush=True)
    summary = {
        "date": "2026-10-09",
        "arithmetic": "exact integers/rationals; standard library only",
        "all_passed": True,
        "checkers": records,
        "scope": "Finite controls supplement the written proofs; no formal or external peer review is claimed.",
    }
    (round_dir / "verification-summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(f"All {len(records)} checkers passed for {len(manifest['results'])} problem reports.")


if __name__ == "__main__":
    main()
