#!/usr/bin/env python3
"""Run the four default verification suites and hash their scripts/certificates.

Install requirements.txt in the chosen Python environment, then run this file
from any directory. Z3 exploration is optional and is not invoked here.
The mathematical proofs remain in the reports; numerical diagnostics are
identified separately from exact arithmetic controls in the summary.
"""
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
import hashlib
import json
import subprocess
import sys

ROUND = Path(__file__).resolve().parent
REPOSITORY = ROUND.parents[1]
TASKS = [
    {
        'name': 'dynamics',
        'questions': ['Q132'],
        'script': 'dynamics/verify_q0132.py',
        'support_scripts': [],
        'certificates': ['dynamics/q0132-checks.json'],
        'arithmetic': 'exact',
        'scope': 'Exact rational finite controls for best responses, nonexpansiveness, interval bounds, and weighted variation; not a machine proof of infinite convergence.',
    },
    {
        'name': 'combinatorics',
        'questions': ['Q256', 'Q257'],
        'script': 'combinatorics/verify.py',
        'support_scripts': ['combinatorics/caterpillar.py', 'combinatorics/tree_enumeration.py'],
        'certificates': ['combinatorics/verification.json'],
        'arithmetic': 'exact',
        'scope': 'Exact subset enumeration of unlabeled trees through order 13, caterpillar witnesses, and finite reductions; not a proof at unbounded order.',
    },
    {
        'name': 'algebra',
        'questions': ['Q3101', 'Q3102'],
        'script': 'algebra/verify_semigroups.py',
        'support_scripts': [],
        'certificates': ['algebra/verification.json', 'algebra/finite-examples.json'],
        'arithmetic': 'exact',
        'scope': 'Exact finite multiplication-table, graph, and constructive left-path controls on 13 explicit examples; not an exhaustive classification of finite semigroups.',
    },
    {
        'name': 'analysis',
        'questions': ['Q3286', 'Q3287'],
        'script': 'analysis/checks.py',
        'support_scripts': [],
        'certificates': ['analysis/checks.json'],
        'arithmetic': 'mixed: exact rational and numerical',
        'scope': 'Exact rational small-parameter bound evaluations plus mpmath quadrature/identity diagnostics at 60 decimal digits and absolute tolerance 1e-45; numerical values are not interval-certified.',
    },
]


def fingerprint(relative):
    data = (ROUND / relative).read_bytes()
    return {'path': relative, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def installed_version(distribution):
    try:
        return version(distribution)
    except PackageNotFoundError:
        return None


def main():
    results = []
    for task in TASKS:
        script = task['script']
        completed = subprocess.run(
            [sys.executable, str(ROUND / script)],
            cwd=REPOSITORY,
            text=True,
            capture_output=True,
            check=False,
        )
        scripts = [fingerprint(path) for path in [script] + task['support_scripts']]
        certificates = []
        certificate_errors = []
        if completed.returncode == 0:
            for path in task['certificates']:
                try:
                    json.loads((ROUND / path).read_text(encoding='utf-8'))
                    certificates.append(fingerprint(path))
                except (OSError, ValueError):
                    certificate_errors.append(path)
        passed = completed.returncode == 0 and not certificate_errors
        result = {
            'name': task['name'],
            'questions': task['questions'],
            'status': 'passed' if passed else 'failed',
            'exit_code': completed.returncode,
            'arithmetic': task['arithmetic'],
            'scope': task['scope'],
            'scripts': scripts,
            'certificates': certificates,
        }
        if certificate_errors:
            result['missing_or_invalid_certificates'] = certificate_errors
        results.append(result)
        print(('PASS' if passed else 'FAIL') + ' ' + script, flush=True)
        if not passed:
            detail = (completed.stderr or completed.stdout).strip()
            if detail:
                print(detail[-4000:], file=sys.stderr, flush=True)

    passed = all(item['status'] == 'passed' for item in results)
    summary = {
        'date': '2026-10-09',
        'status': 'passed' if passed else 'failed',
        'suites_passed': sum(item['status'] == 'passed' for item in results),
        'suites_total': len(results),
        'runner': fingerprint('run_all.py'),
        'requirements': fingerprint('requirements.txt'),
        'dependencies': {'mpmath': {'required': '1.3.0', 'installed': installed_version('mpmath')}},
        'optional_z3_exploration_run': False,
        'suites': results,
        'evidence_scope': 'These reproducible checks supplement the written proofs and separate internal reviews. Exact arithmetic and non-certified numerical diagnostics are distinguished per suite.',
    }
    target = ROUND / 'verification-summary.json'
    target.write_text(json.dumps(summary, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(f"{summary['suites_passed']}/{summary['suites_total']} suites passed; verification-summary.json updated.")
    return 0 if passed else 1


if __name__ == '__main__':
    raise SystemExit(main())
