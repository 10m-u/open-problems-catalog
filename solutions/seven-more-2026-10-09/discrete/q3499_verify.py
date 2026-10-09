#!/usr/bin/env python3
"""Independent exact verifier for Q3499; does not import its generator."""

from fractions import Fraction
from itertools import product
import json
from math import comb
from pathlib import Path


def literal_trace(q, exponent):
    matrix = [[min(i + 1, j + 1) for j in range(q)] for i in range(q)]
    power = [[int(i == j) for j in range(q)] for i in range(q)]
    for _ in range(exponent):
        power = [[sum(power[i][k] * matrix[k][j] for k in range(q))
                  for j in range(q)] for i in range(q)]
    return sum(power[i][i] for i in range(q))


def literal_polygon_count(n, m):
    return sum((m - d + 1) * literal_trace(d + 1, n)
               for d in range(m + 1))


def brute_poset_count(n, m):
    """Directly enumerate assignments to all 2n+2 face-poset elements."""
    total = 0
    for assignment in product(range(m + 1), repeat=2 * n + 2):
        bottom, top = assignment[:2]
        vertices = assignment[2:2 + n]
        edges = assignment[2 + n:]
        if (all(bottom <= a for a in vertices)
                and all(edges[i] >= max(vertices[i], vertices[(i + 1) % n])
                        for i in range(n))
                and all(b <= top for b in edges)):
            total += 1
    return total


def evaluate(coefficients, x):
    return sum(coefficient * x ** degree
               for degree, coefficient in enumerate(coefficients))


def main():
    certificate = json.loads(Path(__file__).with_name("q3499_certificate.json").read_text())
    case = certificate["counterexample"]
    n, degree = case["polygon_vertices"], case["degree"]
    assert n == 13 and degree == 28 and case["poset_elements"] == 28

    # Literal matrix multiplication, not the generator's Newton recurrence.
    traces = [literal_trace(q, n) for q in range(1, degree + 4)]
    values = [sum((m - q + 2) * traces[q - 1] for q in range(1, m + 2))
              for m in range(degree + 3)]
    assert values == case["ehrhart_values_m_0_through_30"]
    coefficients = [Fraction(c) for c in case["coefficients_ascending"]]
    assert len(coefficients) == degree + 1
    assert all(evaluate(coefficients, m) == value for m, value in enumerate(values))

    # Derivatives of the Lagrange basis at zero, not finite differences.
    harmonic = sum((Fraction(1, j) for j in range(1, degree + 1)), Fraction(0))
    linear = -values[0] * harmonic
    linear += sum((Fraction((-1) ** (j - 1) * comb(degree, j), j) * values[j]
                   for j in range(1, degree + 1)), Fraction(0))
    assert linear == coefficients[1] == Fraction(-298495711, 35302608)
    assert [j for j, c in enumerate(coefficients) if c < 0] == [1]
    assert all(evaluate(coefficients, m) == 0 for m in (-1, -2, -3, -4))

    # A different representation: literal cover inequalities on small posets.
    brute_cases = [(3, 0), (3, 1), (3, 2), (4, 1), (4, 2)]
    for small_n, m in brute_cases:
        assert brute_poset_count(small_n, m) == literal_polygon_count(small_n, m)

    # Verify the primary source's order-polynomial control.  Omega(t)=E(t-1).
    control = next(c for c in certificate["family_controls"] if c["polygon_vertices"] == 7)
    assert control["negative_coefficient_degrees"] == []
    from_values = [literal_polygon_count(7, m) for m in range(17)]
    # Lagrange derivative at x=-1: l_j'(-1) = l_j(-1)*sum_{r!=j}1/(-1-r).
    order_linear = Fraction(0)
    for j, value in enumerate(from_values):
        lagrange_value = Fraction(1)
        for r in range(17):
            if r != j:
                lagrange_value *= Fraction(-1 - r, j - r)
        logarithmic_derivative = sum((Fraction(-1, r + 1) for r in range(17)
                                      if r != j), Fraction(0))
        order_linear += value * lagrange_value * logarithmic_derivative
    assert order_linear == Fraction(-3, 1430)

    print("PASS Q3499: all 31 exact counts and the complete degree-28 polynomial agree.")
    print("PASS Q3499: independent Lagrange derivative is -298495711/35302608.")
    print("PASS Q3499: five direct face-poset controls and source control -3/1430 agree.")


if __name__ == "__main__":
    main()
