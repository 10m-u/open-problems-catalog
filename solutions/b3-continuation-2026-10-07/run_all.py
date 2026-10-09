#!/usr/bin/env python3
"""Reproduce the mathematical checks; works in an extracted packet offline."""
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
COMMANDS = [
    ('compositions/checks.py',),
    ('stirling/checks.py',),
    ('interpolation/checks.py', '--max-degree', '5'),
    ('audit/eulerian_checks.py',),
    ('audit/independent_checks.py',),
]

if __name__ == '__main__':
    for script, *args in COMMANDS:
        print(f'Checking {script}', flush=True)
        subprocess.run([sys.executable, str(HERE/script), *args],
                       check=True, cwd=HERE, timeout=60)
    print('PASS: all reconstructed mathematical checks completed.')
