#!/usr/bin/env python3
"""Run this round's exact controls and independently implemented checks.

No third-party packages are needed unless --numeric is supplied. Numerical
Brownian diagnostics require NumPy and SciPy and do not replace the proof.
Run without Python's -O flag, since the exact checkers use assertions.
"""

import argparse
import json
from pathlib import Path
import subprocess
import sys


ROUND = Path(__file__).resolve().parent
ROOT = ROUND.parents[1]
CASES = [
    ("Q212 polynomial identities", "algebra/verify_212.py", None),
    ("Q3893 kernel, cokernel, and shear", "algebra/verify_3893.py", None),
    ("Q726 finite games and posterior geometry", "learning/check_q726.py", "learning/checks.json"),
    ("Q3840/Q3841 exact transfer and constructions", "discrete/verify.py", "discrete/verification.json"),
    ("Q3982/Q3983 saddle, contour, and generator", "probability/verify_brownian.py", "probability/checks.json"),
    ("Independent Q3893 multiplication matrices", "discrete/review_algebra_checks.py", "discrete/review_algebra_checks.json"),
    ("Independent Q3840/Q3841 row enumeration", "probability/review_discrete_checks.py", "probability/review_discrete_checks.json"),
]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--numeric", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if sys.flags.optimize:
        raise SystemExit("Run without -O so all exact assertions are enabled.")
    reports = []
    for title, relative, saved in CASES:
        command = [sys.executable, str(ROUND / relative)]
        numeric = args.numeric and relative == "probability/verify_brownian.py"
        if numeric:
            command.append("--numeric")
        completed = subprocess.run(command, cwd=ROOT, text=True,
                                   capture_output=True, check=True)
        if saved:
            actual = json.loads(completed.stdout)
            expected = json.loads((ROUND / saved).read_text(encoding="utf-8"))
            if relative == "probability/verify_brownian.py":
                # Floating-point diagnostics are independently rerun when asked;
                # only the reproducible exact section is compared byte-for-byte
                # as structured values across library versions.
                assert actual["exact_checks"] == expected["exact_checks"]
            else:
                assert actual == expected, f"Recorded certificate differs: {saved}"
            result = actual
        else:
            result = {"output": completed.stdout.strip()}
        reports.append({"name": title, "script": relative,
                        "exit_code": completed.returncode, "result": result})
        print(f"PASS: {title}", file=sys.stderr)
    report = {
        "round": ROUND.name,
        "all_passed": True,
        "commands_passed": len(reports),
        "numeric_diagnostics_requested": args.numeric,
        "evidence_limit": "Exact controls and independent implementations accompany the written mathematical proofs. This is not formal proof verification or external peer review.",
        "checks": reports,
    }
    serialized = json.dumps(report, indent=2, ensure_ascii=False, allow_nan=False) + "\n"
    if args.output:
        args.output.write_text(serialized, encoding="utf-8")
        print(f"Wrote {args.output}")
    else:
        print(serialized, end="")


if __name__ == "__main__":
    main()
