#!/usr/bin/env python3
"""Bounded exact checks for the B14 P5 local proof.

Uses the Python standard library. Finite checks corroborate formulas, not their
asymptotic proof. Every probability comparison below uses rational arithmetic.
"""

from fractions import Fraction as F
from itertools import combinations, product
import json
import math
from pathlib import Path
import random


def edge(a, b):
    return tuple(sorted((a, b)))


def tour_edges(n):
    return {edge(i, (i + 1) % n) for i in range(n)}


def is_tour(n, edges):
    if len(edges) != n:
        return False
    adj = [[] for _ in range(n)]
    for a, b in edges:
        if a == b:
            return False
        adj[a].append(b)
        adj[b].append(a)
    if any(len(neighbors) != 2 for neighbors in adj):
        return False
    seen, stack = {0}, [0]
    while stack:
        for neighbor in adj[stack.pop()]:
            if neighbor not in seen:
                seen.add(neighbor)
                stack.append(neighbor)
    return len(seen) == n


def literal_exchanges(n):
    """Find alternatives by reconnecting four endpoints and testing tours."""
    original = tour_edges(n)
    found = []
    for i, j in combinations(range(n), 2):
        a, b, c, d = i, (i + 1) % n, j, (j + 1) % n
        if len({a, b, c, d}) < 4:
            continue
        removed = {edge(a, b), edge(c, d)}
        remaining = original - removed
        alternatives = []
        for pairing in (
            {edge(a, b), edge(c, d)},
            {edge(a, c), edge(b, d)},
            {edge(a, d), edge(b, c)},
        ):
            new = remaining | pairing
            if new != original and is_tour(n, new):
                alternatives.append(tuple(sorted(pairing)))
        assert len(alternatives) == 1, (n, i, j, alternatives)
        found.append(((i, j), alternatives[0]))
    return found


def components(n):
    """Each component contains its chord variables and threshold edge pairs."""
    result = []
    for d in range(2, (n - 1) // 2 + 1):
        result.append((
            [edge(i, (i + d) % n) for i in range(n)],
            [(i, (i + d) % n) for i in range(n)],
        ))
    if n % 2 == 0:
        m = n // 2
        result.append((
            [edge(i, i + m) for i in range(m)],
            [(i, i + m) for i in range(m)],
        ))
    return result


def component_exchanges(n):
    result = []
    for chords, pairs in components(n):
        assert len(chords) == len(pairs) >= 2
        for k, (i, j) in enumerate(pairs):
            result.append((tuple(sorted((i, j))), tuple(sorted((
                chords[k], chords[(k + 1) % len(chords)],
            )))))
    return result


def matrix_product(a, b):
    q = len(a)
    c = [[0] * q for _ in range(q)]
    for i in range(q):
        for k, aik in enumerate(a[i]):
            if aik:
                bk = b[k]
                ci = c[i]
                for j, bkj in enumerate(bk):
                    ci[j] += aik * bkj
    return c


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def kernel(grid, threshold):
    return [[int(a + b >= threshold) for b in grid] for a in grid]


def cycle_probability(grid, thresholds):
    matrices = [kernel(grid, t) for t in thresholds]
    a = matrices[0]
    for b in matrices[1:]:
        a = matrix_product(a, b)
    return F(trace(a), len(grid) ** len(thresholds))


def conditional_probability(n, xs, grid):
    p = F(1)
    independent_product = F(1)
    for chords, pairs in components(n):
        thresholds = [xs[i] + xs[j] for i, j in pairs]
        p *= cycle_probability(grid, thresholds)
        for t in thresholds:
            independent_product *= F(sum(map(sum, kernel(grid, t))), len(grid) ** 2)
    return p, independent_product


def brute_chord_probability(n, xs, grid):
    chords = sorted(set(combinations(range(n), 2)) - tour_edges(n))
    index = {e: i for i, e in enumerate(chords)}
    tests = [(index[a], index[b], xs[i] + xs[j])
             for (i, j), (a, b) in literal_exchanges(n)]
    accepted = 0
    for ys in product(grid, repeat=len(chords)):
        accepted += all(ys[a] + ys[b] >= t for a, b, t in tests)
    return F(accepted, len(grid) ** len(chords))


def quadratic_checks(n, xs):
    pairs = [pair for pair, _ in literal_exchanges(n)]
    q = sum((xs[i] + xs[j]) ** 2 for i, j in pairs)
    a = sum(x * x for x in xs)
    s = sum(xs)
    b = sum(xs[i] * xs[(i + 1) % n] for i in range(n))
    assert q == (n - 4) * a + s * s - 2 * b, (n, xs)
    assert q >= (n - 6) * a + s * s, (n, xs)


def main():
    report = {"status": "passed", "random_seed": 3818, "checks": {}}
    rng = random.Random(3818)

    total_exchanges = 0
    for n in range(3, 41):
        literal = literal_exchanges(n)
        component = component_exchanges(n)
        assert sorted(literal) == sorted(component), n
        assert len(literal) == n * (n - 3) // 2, n
        chords = [c for cs, _ in components(n) for c in cs]
        assert len(set(chords)) == len(chords), n
        assert set(chords) == set(combinations(range(n), 2)) - tour_edges(n), n
        multiplicity = {c: 0 for c in chords}
        for _, added in component:
            for c in added:
                multiplicity[c] += 1
        assert all(count == 2 for count in multiplicity.values()), n
        total_exchanges += len(literal)
    report["checks"]["exchange_accounting"] = {
        "n_range": [3, 40], "total_exchanges_checked": total_exchanges,
        "includes_even_diameter_and_n4_parallel_constraints": True,
    }

    exact_cases = []
    for n, q, samples in [(3, 3, 2), (4, 3, 8), (5, 3, 8), (6, 3, 5), (7, 2, 3)]:
        grid = [F(k, q - 1) for k in range(q)]
        for sample in range(samples):
            xs = [rng.choice(grid) for _ in range(n)]
            factored, _ = conditional_probability(n, xs, grid)
            brute = brute_chord_probability(n, xs, grid)
            assert factored == brute, (n, q, xs, factored, brute)
            exact_cases.append({"n": n, "grid_size": q, "probability": str(brute)})
    report["checks"]["direct_enumeration_vs_cycle_product"] = exact_cases

    hs_cases = 0
    quadratic_cases = 0
    for n in range(3, 25):
        grid = [F(k, 6) for k in range(7)]
        for sample in range(16):
            xs = [rng.choice(grid) for _ in range(n)]
            p, independent_product = conditional_probability(n, xs, grid)
            assert p * p <= independent_product, (n, xs, p, independent_product)
            hs_cases += 1
            quadratic_checks(n, xs)
            quadratic_cases += 1
    report["checks"]["read_two_exact_rational_inequality"] = {
        "n_range": [3, 24], "grid_size": 7, "cases": hs_cases,
        "comparison": "conditional_probability^2 <= product(single_exchange_probability)",
    }
    report["checks"]["quadratic_identity_and_lower_bound"] = {"cases": quadratic_cases}

    known_volumes = {2: F(1, 2), 3: F(1, 4), 4: F(1, 6), 5: F(5, 48), 6: F(1, 15)}
    q = 64
    left = [F(k, q) for k in range(q)]
    right = [F(k + 1, q) for k in range(q)]
    lo_kernel, hi_kernel = kernel(left, F(1)), kernel(right, F(1))
    lo_power, hi_power = lo_kernel, hi_kernel
    volume_bounds = []
    for m in range(2, 7):
        lo_power = matrix_product(lo_power, lo_kernel)
        hi_power = matrix_product(hi_power, hi_kernel)
        lo, hi = F(trace(lo_power), q ** m), F(trace(hi_power), q ** m)
        assert lo <= known_volumes[m] <= hi, (m, lo, known_volumes[m], hi)
        assert known_volumes[m] ** 2 <= F(1, 2) ** m
        volume_bounds.append({
            "cycle_length": m, "target_exact": str(known_volumes[m]),
            "certified_lower": str(lo), "certified_upper": str(hi), "grid_size": q,
        })
    report["checks"]["homogeneous_volume_certified_grid_bounds"] = volume_bounds
    assert F(5, 48) > F(1, 2) ** 5
    report["checks"]["independent_event_upper_bound_counterexample"] = {
        "cycle_length": 5, "true_conditional_volume": "5/48", "independent_product": "1/32",
    }

    assert F(149, 84) ** 2 - F(22, 7) == F(25, 7056)
    assert F(149, 84) - F(11, 12) == F(6, 7)
    assert F(1, 2) - F(1, 24) == F(11, 24)
    report["checks"]["constant_below_one_rational_certificate"] = {
        "gaussian_integral_lower_bound": "11/24",
        "squared_pi_upper_bound_comparison_margin": "25/7056", "c_upper_bound": "6/7",
        "c_float_for_orientation_only": math.sqrt(math.pi) * math.erfc(0.5),
    }

    # Explicit upper bound from (1); floating outputs below are illustration only.
    report["illustrative_upper_bounds_E_M_over_sqrt_factorial"] = {
        str(n): math.exp(6.5) / (2 * math.sqrt(n)) * (math.sqrt(math.pi) * math.erfc(0.5)) ** n
        for n in [12, 20, 40, 80, 160]
    }
    output = Path(__file__).with_name("CHECK-RESULTS.json")
    output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"status": report["status"], "output": str(output),
                      "structural_n": [3, 40], "brute_cases": len(exact_cases),
                      "rational_hs_cases": hs_cases, "quadratic_cases": quadratic_cases}, indent=2))


if __name__ == "__main__":
    main()
