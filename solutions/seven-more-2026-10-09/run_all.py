#!/usr/bin/env python3
"""Regenerate and verify this round's mathematical certificates; stdlib only."""

import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    root = Path(__file__).resolve().parent
    manifest = json.loads((root / 'RESULTS.json').read_text())
    steps = {}
    for result in manifest['results']:
        steps.setdefault(result['checker'], set()).add(result['certificate'])
        if result.get('independent_checker'):
            steps.setdefault(result['independent_checker'], set()).add(result['certificate'])
    steps['reviews/check_probability_enumeration.py'] = {'reviews/probability-enumeration-review.json'}
    records = []
    environment = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
    for relative, certificates in steps.items():
        script = root / relative
        completed = subprocess.run([sys.executable, str(script)], cwd=script.parent,
                                   env=environment, capture_output=True, text=True)
        if completed.returncode:
            sys.stdout.write(completed.stdout)
            sys.stderr.write(completed.stderr)
            raise SystemExit(f'FAILED: {relative} (exit {completed.returncode})')
        records.append({
            'checker': relative,
            'checker_sha256': digest(script),
            'exit_code': completed.returncode,
            'certificates': {name: digest(root / name) for name in sorted(certificates)},
        })
        print(f'PASS {relative}', flush=True)
    summary = {
        'date': '2026-10-09',
        'base_commit': manifest['base_commit'],
        'all_passed': True,
        'problem_count': len(manifest['results']),
        'arithmetic': 'Exact integers/rationals; Python standard library only.',
        'scope': 'Computational proofs/controls at the scopes stated in each report; not formal or external peer review.',
        'checks': records,
    }
    (root / 'verification-summary.json').write_text(json.dumps(summary, indent=2) + '\n')
    print(f'All {len(records)} checks passed for {len(manifest["results"])} problems.')


if __name__ == '__main__':
    main()
