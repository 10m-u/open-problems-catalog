#!/usr/bin/env python3
"""Exact supplementary certificates for Q3236 and Q3454.

No third-party packages, numerical optimization, or floating-point arithmetic.
The analytical proofs are in the adjacent Markdown files. This script checks
their illustrative algebra and breakpoint formulas, not the infinite theorems.
"""

from fractions import Fraction as F
import json
from pathlib import Path


def frac(x):
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def q3236_example(n):
    # On each high-value rearrangement interval, a*/u and b*/u are
    # fractional-linear functions without a pole. Their extrema are at
    # the endpoints; endpoints include one-sided limits.
    maxima = []
    for right_half in (False, True):
        values = [F(1)]  # The bottom half of each rearrangement is exactly 1.
        for j in range(n):
            s0 = F(n - 1 - j, 2 * n)
            s1 = F(n - j, 2 * n)
            t_top = F(j + 1, n) if right_half else F(2 * j + 1, 2 * n)
            intercept = 1 + t_top + s0
            for s in (s0, s1):
                values.append((intercept - s) / (2 - 2 * s))
        maxima.append(max(values))
    assert maxima[0] == 1
    assert maxima[1] == 1 + F(1, 2 * n)
    return {"n": n, "N_a_n": frac(maxima[0]), "N_b_n": frac(maxima[1]),
            "total_cost": frac(sum(maxima))}


def mat(rows):
    return tuple(tuple(F(x) for x in row) for row in rows)


def add(a, b):
    return tuple(tuple(x + y for x, y in zip(ar, br)) for ar, br in zip(a, b))


def sub(a, b):
    return tuple(tuple(x - y for x, y in zip(ar, br)) for ar, br in zip(a, b))


def mul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(len(b)))
                       for j in range(len(b[0]))) for i in range(len(a)))


def norm_inf(a):
    return max(sum(abs(x) for x in row) for row in a)


def q3454_example(denom):
    d = F(1, denom)
    a = mat([[0, 2, 1], [0, 1, 1], [0, 0, 0]])
    ad = mat([[0, 0, 0], [1, -1, 0], [-1, 2, 0]])
    b = mat([[0, 2 + d, 1], [0, 1, 1 + d], [0, 0, 0]])
    det = (2 + d) * (1 + d) - 1
    bd = mat([[0, 0, 0], [(1 + d) / det, -1 / det, 0],
              [-1 / det, (2 + d) / det, 0]])
    p = mat([[0, 0, 0], [0, 1, 0], [0, 0, 1]])
    q = mat([[1, 0, 0], [0, 1, 0], [0, 0, 0]])
    # The infinity operator norm makes diagonal coordinate projections
    # hermitian: exp(it p), exp(it q) are diagonal isometries.
    for x, xd in ((a, ad), (b, bd)):
        assert mul(mul(x, xd), x) == x
        assert mul(mul(xd, x), xd) == xd
        assert mul(xd, x) == p
        assert mul(x, xd) == q
    epsilon = norm_inf(sub(a, b))
    maximum_inverse = max(norm_inf(ad), norm_inf(bd))
    assert maximum_inverse * epsilon < 1
    assert mul(mul(bd, sub(a, b)), ad) == sub(bd, ad)
    actual = norm_inf(sub(bd, ad))
    bound = norm_inf(bd) * norm_inf(ad) * epsilon
    assert actual <= bound
    return {"perturbation": frac(d), "M_epsilon": frac(maximum_inverse * epsilon),
            "inverse_difference_norm": frac(actual), "proved_bound": frac(bound)}


def main():
    rows = [q3236_example(n) for n in range(1, 129)]
    matrix_rows = [q3454_example(n) for n in (4, 5, 10, 20, 100, 1000)]
    scalar_c = F(3, 7)
    scalar_threshold = scalar_c * (1 / scalar_c)
    assert scalar_threshold == 1
    result = {
        "date": "2026-10-09",
        "arithmetic": "Python fractions.Fraction only",
        "scope": "Supplementary exact examples; general theorems proved analytically.",
        "Q3236": {
            "tested_n": [1, 128],
            "cases_checked": len(rows),
            "formula": "N(a_n)=1; N(b_n)=1+1/(2n)",
            "sample_cases": [r for r in rows if r["n"] in (1, 2, 4, 8, 16, 32, 64, 128)],
            "integral_lower_bound": "(5/2)/(5/4)=2",
            "attainment": "Disproved by the analytic distribution argument in Q3236-proof.md",
        },
        "Q3454": {
            "same_support_matrix_cases": matrix_rows,
            "sharp_threshold_scalar": {"a": "0", "b": frac(scalar_c),
                                      "M_epsilon": frac(scalar_threshold),
                                      "source_and_range_supports_differ": True},
        },
        "all_checks_passed": True,
    }
    output = Path(__file__).with_name("verification.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"all_checks_passed": True, "Q3236_cases": len(rows),
                      "Q3454_matrix_cases": len(matrix_rows), "output": str(output)}))


if __name__ == "__main__":
    main()
