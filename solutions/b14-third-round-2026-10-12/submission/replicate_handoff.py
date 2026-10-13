#!/usr/bin/env python3
"""Validate the original archive and rerun four bounded, non-filing checks.

The original ZIP is opened read-only. Research scripts execute in a temporary
extraction, never against a live catalog. Python 3.10+, standard library only.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import tempfile
import time
import zipfile

BASE = 'solutions/catalog-research/'
JOBS = [
    ('count', 'b14-first-round-2026-10-12/audit_count.py',
     'b14-first-round-2026-10-12/COUNT-CHECK-RESULTS.json'),
    ('elimination', 'b14-first-round-2026-10-12/local-optima/check_elimination.py',
     'b14-first-round-2026-10-12/local-optima/ELIMINATION-CHECK-RESULTS.json'),
    ('p2', 'b14-second-round-2026-10-12/residual-search/check_exponential.py',
     'b14-second-round-2026-10-12/residual-search/EXPONENTIAL-CHECK-RESULTS.json'),
    ('p3', 'b14-second-round-2026-10-12/audit_p3_gain.py',
     'b14-second-round-2026-10-12/P3-INDEPENDENT-CHECK-RESULTS.json'),
]

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--zip', type=Path, required=True, help='The user-provided complete handoff ZIP.')
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name('replication'))
    parser.add_argument('--timeout', type=int, default=60, help='Seconds per checker.')
    args = parser.parse_args()
    if not args.zip.is_file():
        parser.error(f'Archive does not exist: {args.zip}')
    args.output.mkdir(parents=True, exist_ok=True)
    original_hash = hashlib.sha256(args.zip.read_bytes()).hexdigest()
    job_results = []
    with zipfile.ZipFile(args.zip) as z, tempfile.TemporaryDirectory(prefix='b14-replication-') as tmp:
        dest = Path(tmp)
        manifest_path = 'projects/thesis-catalog/exports/b14-handoff-2026-10-12/MANIFEST.json'
        manifest = json.loads(z.read(manifest_path))
        for entry in manifest['files']:
            data = z.read(entry['path'])
            assert len(data) == entry['bytes'], entry['path']
            assert hashlib.sha256(data).hexdigest() == entry['sha256'], entry['path']
        names = {i.filename for i in z.infolist() if not i.is_dir()}
        assert names == {e['path'] for e in manifest['files']} | {manifest_path}
        for entry in z.infolist():
            target = (dest / entry.filename).resolve()
            if not target.is_relative_to(dest.resolve()):
                raise ValueError(f'Unsafe archive path: {entry.filename}')
        z.extractall(dest)
        for name, script, receipt in JOBS:
            before = json.loads(z.read(BASE + receipt))
            start = time.perf_counter()
            result = subprocess.run([sys.executable, str(dest / (BASE + script))],
                                    cwd=dest, text=True, capture_output=True, timeout=args.timeout)
            elapsed = time.perf_counter()-start
            (args.output / f'{name}_stdout.txt').write_text(result.stdout)
            (args.output / f'{name}_stderr.txt').write_text(result.stderr)
            if result.returncode:
                raise RuntimeError(f'{name} checker failed: {result.stderr}')
            after_path = dest / (BASE + receipt)
            after = json.loads(after_path.read_text())
            assert after == before, f'Receipt changed for {name}'
            shutil.copyfile(after_path, args.output / f'{name}_recomputed.json')
            job_results.append({'name': name, 'script': BASE + script, 'receipt': BASE + receipt,
                                'exit_code': result.returncode, 'semantic_receipt_match': True,
                                'elapsed_seconds': elapsed})
    assert hashlib.sha256(args.zip.read_bytes()).hexdigest() == original_hash
    report = {'status': 'passed', 'archive_sha256': original_hash,
              'manifest_payload_files_verified': len(manifest['files']),
              'archive_entries': len(names), 'archive_unchanged': True,
              'python': sys.version, 'platform': platform.platform(), 'jobs': job_results,
              'scope': 'Four finite checker replications, not an independent review of every handoff theorem.'}
    (args.output / 'REPLICATION-RESULTS.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))

if __name__ == '__main__':
    main()
