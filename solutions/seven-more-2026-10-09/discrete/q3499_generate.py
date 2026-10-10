#!/usr/bin/env python3
"""Generate the exact polygon-face Ehrhart counterexample (stdlib only).

The generation route uses Newton identities and finite differences.  The
separate q3499_verify.py uses literal matrix products and Lagrange interpolation.
"""

from fractions import Fraction
import json
from math import comb, factorial
from pathlib import Path


def crown_counts(n, largest_q):
    """Return Omega_C(0), ..., Omega_C(largest_q)."""
    counts = [0]
    for q in range(1, largest_q + 1):
        a = [(-1) ** k * comb(q + k, 2 * k) if k <= q else 0
             for k in range(n + 1)]
        powers = [q]
        for r in range(1, n + 1):
            powers.append(-r * a[r] - sum(a[k] * powers[r - k]
                                         for k in range(1, r)))
        counts.append(powers[n])
    return counts


def polygon_values(n, largest_m):
    crown = crown_counts(n, largest_m + 1)
    result = []
    first_sum = second_sum = 0
    for q in range(1, largest_m + 2):
        first_sum += crown[q]
        second_sum += first_sum
        result.append(second_sum)
    return result


def interpolate(values):
    """Convert integer values at 0,...,d to rational monomial coefficients."""
    d = len(values) - 1
    common_denominator = factorial(d)
    differences = []
    current = list(values)
    while current:
        differences.append(current[0])
        current = [b - a for a, b in zip(current, current[1:])]
    coefficients = [0] * (d + 1)
    falling = [1]
    for k, difference in enumerate(differences):
        multiplier = difference * (common_denominator // factorial(k))
        for j, coefficient in enumerate(falling):
            coefficients[j] += multiplier * coefficient
        new_falling = [0] * (len(falling) + 1)
        for j, coefficient in enumerate(falling):
            new_falling[j] -= k * coefficient
            new_falling[j + 1] += coefficient
        falling = new_falling
    return [Fraction(c, common_denominator) for c in coefficients]


def evaluate(coefficients, argument):
    value = Fraction(0)
    for coefficient in reversed(coefficients):
        value = value * argument + coefficient
    return value


def build_certificate():
    controls = []
    for n in range(3, 14):
        degree = 2 * n + 2
        values = polygon_values(n, degree + 2)
        coefficients = interpolate(values[:degree + 1])
        assert all(evaluate(coefficients, m) == value
                   for m, value in enumerate(values))
        negatives = [j for j, c in enumerate(coefficients) if c < 0]
        controls.append({
            "polygon_vertices": n,
            "degree": degree,
            "linear_coefficient": str(coefficients[1]),
            "negative_coefficient_degrees": negatives,
            "all_coefficients_strictly_positive": all(c > 0 for c in coefficients),
        })
        if n == 13:
            assert negatives == [1]
            assert coefficients[1] == Fraction(-298495711, 35302608)
            counterexample = {
                "polygon_vertices": n,
                "poset_elements": degree,
                "degree": degree,
                "ehrhart_values_m_0_through_30": values,
                "coefficients_ascending": [str(c) for c in coefficients],
                "negative_coefficient_degrees": negatives,
            }
    return {
        "problem": "Q3499",
        "date": "2026-10-09",
        "scope": "Counterexample to universal Ehrhart coefficient nonnegativity",
        "arithmetic": "Python arbitrary-precision integers and fractions.Fraction",
        "counterexample": counterexample,
        "family_controls": controls,
    }


if __name__ == "__main__":
    certificate = build_certificate()
    destination = Path(__file__).with_name("q3499_certificate.json")
    destination.write_text(json.dumps(certificate, indent=2) + "\n")
    print("Q3499: 13-gon, [m]E(m) = -298495711/35302608")
    print("All monomial coefficients are positive for 3 <= n <= 12.")
    print("Exact values at two additional interpolation nodes agree.")
    print(f"Wrote {destination.name}")
