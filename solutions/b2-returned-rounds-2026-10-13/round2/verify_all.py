#!/usr/bin/env python3
"""Run the exact verification suite; no third-party packages are required."""
from pathlib import Path
import subprocess
import sys


def main() -> None:
    if not __debug__:
        raise RuntimeError('Run without -O: verification uses assertions.')
    root = Path(__file__).resolve().parent
    for name in ('certify_entropy.py','verify_midpoint.py','verify_entropy_boundary.py'):
        print(f'=== {name} ===', flush=True)
        subprocess.run([sys.executable,str(root/name)],cwd=root,check=True)
    print('All three verification programs passed.')


if __name__ == '__main__':
    main()
