#!/usr/bin/env python3
"""Reproduce supplementary Q3286/Q3287 diagnostics; not a proof checker.

Run from the repository root:
    python solutions/seven-problems-2026-10-09/analysis/checks.py

Requires mpmath. Output is deterministic JSON beside this script. Numerical
quadrature checks are distinguished from exact rational-bound evaluations.
"""

from fractions import Fraction
from itertools import product
import json
from math import comb, factorial, prod
from pathlib import Path

import mpmath as mp


mp.mp.dps = 60
TOLERANCE = mp.mpf("1e-45")


def ga_integral(b, c, z):
    return b * c * mp.quad(
        lambda w: (c + w * (1 - c * z)) ** (-1 - b)
        - (c + w) ** (-1 - b), [0, 1]
    )


def gb_integral(b, c, z):
    return b * mp.quad(
        lambda w: (1 + w * c * (1 - z)) ** (-1 - b)
        - (1 + w * c) ** (-1 - b), [0, 1]
    )


def ga_closed(b, c, z):
    return c / (1 - c * z) * (
        (1 - c * z) * (1 + c) ** (-b)
        - (1 + c - c * z) ** (-b) + z * c ** (1 - b)
    )


def gb_closed(b, c, z):
    return ((1 - z) * (1 + c) ** (-b)
            - (1 + c - c * z) ** (-b) + z) / (c * (1 - z))


def check_close(actual, expected):
    error = abs(actual - expected)
    assert error < TOLERANCE, (actual, expected, error)
    return error


def check_kernels():
    errors = []
    triples = list(product(
        [mp.mpf(1) / 5, mp.mpf(1) / 2, mp.mpf(4) / 5],
        [mp.mpf(1) / 10, mp.mpf(1) / 4, mp.mpf(1) / 2, mp.mpf(9) / 10],
        [mp.mpf(1) / 10, mp.mpf(1) / 4, mp.mpf(1) / 2,
         mp.mpf(3) / 4, mp.mpf(9) / 10],
    ))
    for b, c, z in triples:
        ga = ga_integral(b, c, z)
        gb = gb_integral(b, c, z)
        errors += [check_close(ga, ga_closed(b, c, z)),
                   check_close(gb, gb_closed(b, c, z))]
        delta = (1 + c - c * z) ** (-b) - (1 + c) ** (-b)
        ga_negative = delta + (1 - b) * mp.quad(
            lambda w: (c + w) ** (-b)
            - (c + w * (1 - c * z)) ** (-b), [0, 1]
        )
        gb_negative = delta + (1 - b) * mp.quad(
            lambda w: (1 + w * c) ** (-b)
            - (1 + w * c * (1 - z)) ** (-b), [0, 1]
        )
        errors += [check_close(ga, ga_negative), check_close(gb, gb_negative)]
        assert 0 < ga <= delta <= b * c * z
        assert 0 < gb <= delta <= b * c * z
    for b, c in product(
        [mp.mpf(1) / 5, mp.mpf(1) / 2, mp.mpf(4) / 5],
        [mp.mpf(1) / 10, mp.mpf(1) / 4, mp.mpf(1) / 2, mp.mpf(9) / 10],
    ):
        q = (1 + c) ** (-b) - (1 - c ** (1 - b)) / (1 - c)
        errors.append(check_close(ga_integral(b, c, 1), c * q))
        assert 0 < q < c ** (1 - b)
    return {
        "parameter_triples": len(triples),
        "numeric_identity_checks": len(errors),
        "maximum_absolute_error": mp.nstr(max(errors), 10),
        "kernel_bounds_at_test_points": "passed",
    }


def check_radial_integrals():
    errors = []
    for d, a, rate in [(2, mp.mpf(1) / 4, mp.mpf(2)),
                       (2, mp.mpf(3) / 2, mp.mpf(3) / 2),
                       (3, mp.mpf(1), mp.mpf(1) / 2),
                       (4, mp.mpf(2), mp.mpf(3))]:
        delta = a + d - 1
        b = a / delta
        integral = mp.quad(
            lambda y: y ** (delta + a - 1) * mp.exp(-rate * y ** delta),
            [0, 1, 2, mp.inf],
        )
        expected = mp.gamma(1 + b) / delta * rate ** (-1 - b)
        errors.append(check_close(integral, expected))
    return {"cases": len(errors),
            "maximum_absolute_error": mp.nstr(max(errors), 10)}


def rising(x, d):
    return prod(x + j for j in range(d))


def exact_small_bounds():
    results = []
    for d in range(2, 8):
        rows = []
        for denominator in [10, 100, 1000, 10000]:
            a = Fraction(1, denominator)
            delta = a + d - 1
            b = a / delta
            big_p = rising(a, d)
            weighted = sum(
                Fraction(comb(d, q), factorial(d - q - 1) * factorial(q - 1))
                * (1 / (a + d - q) + 1 / (a + q + delta))
                for q in range(1, d)
            )
            t1_bound = 2 * big_p * b / (delta + 1) * weighted
            t2_bound = 2 * big_p * a / (factorial(d - 1) * (d - 1) ** 2)
            t3_remainder = big_p * b * (b + 1) / rising(2 * a + d - 1, d)
            error_bound = t1_bound + t2_bound + t3_remainder
            lower = 1 - 2 * b
            upper = lower + error_bound
            assert 0 < lower <= upper
            # The theorem says "sufficiently small", not a uniform threshold.
            if denominator == 10000:
                assert upper < 1
            rows.append({
                "a": str(a),
                "exact_lower": str(lower),
                "exact_upper": str(upper),
                "upper_bound_is_less_than_one": upper < 1,
                "exact_error_bound_over_a_squared": str(error_bound / a ** 2),
            })
        results.append({"d": d, "bounds_from_report_equation_14": rows})
    return results


def check_limit_constants():
    values = []
    for p in [1, 2]:
        # Integrating in y in the positive double integral leaves this integral.
        value = mp.quad(lambda x: x ** p / mp.expm1(x), [0, 1, 10, mp.inf])
        expected = mp.factorial(p) * mp.zeta(p + 1)
        error = check_close(value, expected)
        constant = 1 + (2 if p == 1 else 6) * value
        values.append({"dimension": p + 1,
                       "double_integral_reduced_numerically": mp.nstr(value, 45),
                       "C_d": mp.nstr(constant, 45),
                       "absolute_error_against_zeta_identity": mp.nstr(error, 10)})
    return values


def main():
    output = {
        "date": "2026-10-09",
        "scope": "Supplementary checks only; proofs are in REPORT.md.",
        "mpmath_version": mp.__version__,
        "decimal_precision": mp.mp.dps,
        "numerical_absolute_tolerance": str(TOLERANCE),
        "kernels": check_kernels(),
        "radial_integrals": check_radial_integrals(),
        "small_parameter_bounds_exact_arithmetic": exact_small_bounds(),
        "limiting_constants_numerical": check_limit_constants(),
    }
    target = Path(__file__).with_name("checks.json")
    target.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print("All Q3286/Q3287 supplementary checks passed.")
    print(f"Kernel identity checks: {output['kernels']['numeric_identity_checks']}; "
          f"radial integral checks: {output['radial_integrals']['cases']}.")
    print(f"Output: {target}")


if __name__ == "__main__":
    main()
