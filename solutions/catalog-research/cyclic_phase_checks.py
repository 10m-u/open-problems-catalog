#!/usr/bin/env python3
"""Exact finite audits of the cyclic phase theorem and the catalog hexachords."""

from itertools import combinations_with_replacement, product
import json
from math import gcd, prod
from pathlib import Path

from sympy import Poly, cyclotomic_poly, symbols

from cyclic_phase_lattice import profile


def symmetric_supports(n):
    pieces = [{k, (-k) % n} for k in range(1, (n + 1) // 2)]
    if n % 2 == 0:
        pieces.append({n // 2})
    for chosen in product((False, True), repeat=len(pieces)):
        yield sorted(set().union(*(p for p, yes in zip(pieces, chosen) if yes)))


def phase_grid_count(n, support, degree):
    """Directly evaluate every invariant monomial on an n-th-root phase grid.

    Generates the reality-constrained phases independently of the integer
    matrix and Smith calculation in the solver.
    """
    positive = [k for k in support if 2 * k < n]
    nyquist = n // 2 if n % 2 == 0 and n // 2 in support else None
    monomials = [ks for size in range(1, degree + 1)
                 for ks in combinations_with_replacement(support, size)
                 if sum(ks) % n == 0]
    count = 0
    signs = (0, n // 2) if nyquist is not None else (None,)
    for phases in product(range(n), repeat=len(positive)):
        phase = dict(zip(positive, phases))
        phase.update({n - k: (-v) % n for k, v in zip(positive, phases)})
        for sign in signs:
            if nyquist is not None:
                phase[nyquist] = sign
            count += all(sum(phase[k] for k in ks) % n == 0 for ks in monomials)
    return count


def rotate(mask, amount, n):
    amount %= n
    return ((mask << amount) | (mask >> (n - amount))) & ((1 << n) - 1)


def deck(mask, offsets, n):
    intersection = mask
    for offset in offsets:
        intersection &= rotate(mask, -offset, n)
    return intersection.bit_count()


def main():
    grid_checks = 0
    for n in range(2, 9):
        for support in symmetric_supports(n):
            for degree in range(2, 5):
                result = profile(n, support, degree)
                predicted = n ** result["torus_dimension"] * prod(
                    gcd(n, factor) for factor in result["smith_factors"])
                assert phase_grid_count(n, support, degree) == predicted
                grid_checks += 1

    odd_checks = []
    for n in range(4, 21, 2):
        third = profile(n, range(1, n, 2), 3)
        fourth = profile(n, range(1, n, 2), 4)
        assert third["torus_dimension"] == n // 4
        assert fourth["orbit_count"] == 1
        odd_checks.append({"n": n, "degree_three_dimension": n // 4,
                           "degree_four_orbits": 1})

    n = 12
    groups = {}
    for mask in range(1 << n):
        key = tuple(deck(mask, (a, b), n) for a in range(n) for b in range(n))
        representative = min(rotate(mask, t, n) for t in range(n))
        groups.setdefault(key, set()).add(representative)
    collisions = [sorted(reps) for reps in groups.values() if len(reps) > 1]
    assert len(collisions) == 1 and len(collisions[0]) == 2
    a_set, b_set = [0, 1, 2, 4, 5, 9], [0, 1, 2, 5, 9, 10]
    a = sum(1 << k for k in a_set)
    b = sum(1 << k for k in b_set)
    assert min(rotate(a, t, n) for t in range(n)) != min(
        rotate(b, t, n) for t in range(n))
    assert {min(rotate(a, t, n) for t in range(n)),
            min(rotate(b, t, n) for t in range(n))} == set(collisions[0])
    assert all(deck(a, (i, j), n) == deck(b, (i, j), n)
               for i in range(n) for j in range(n))
    assert [deck(a, (1, 2, 4), n), deck(b, (1, 2, 4), n)] == [1, 0]

    # DFT support certified in Q[z]/Phi_12, with no floating threshold.
    z = symbols("z")
    modulus = Poly(cyclotomic_poly(n, z), z)
    supports = []
    for points in (a_set, b_set):
        support = [k for k in range(n) if not Poly(
            sum(z ** ((j * k) % n) for j in points), z).rem(modulus).is_zero]
        assert support == [0, 1, 3, 5, 7, 9, 11]
        supports.append(support)

    result = {
        "date": "2026-09-30", "status": "all assertions passed",
        "independent_phase_grid_checks": grid_checks,
        "phase_grid_moduli": "n-th roots, n=2..8; every symmetric support; d=2..4",
        "full_odd_support_checks": odd_checks,
        "binary_z12": {
            "subsets": 1 << n,
            "translation_classes": sum(len(reps) for reps in groups.values()),
            "degree_three_collision_groups": len(collisions),
            "exceptional_sets": [a_set, b_set], "exact_fourier_supports": supports,
            "fourth_order_offsets": [0, 1, 2, 4], "fourth_order_counts": [1, 0],
            "degree_four_separates_all_binary_translation_classes": True,
        },
        "limits": "Finite controls support hand proofs; no novelty or formal verification claim.",
    }
    target = Path(__file__).with_name("cyclic-phase-checks.json")
    target.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
