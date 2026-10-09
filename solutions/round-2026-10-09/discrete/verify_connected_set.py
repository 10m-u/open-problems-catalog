#!/usr/bin/env python3
"""Exact, direct finite checks for Q3489 and the rooted-attachment reductions.

No external dependencies. Run from any directory; the result JSON is written
beside this script. A left-side evaluation always enumerates subsets of the
actual constructed graph; no claimed attachment identity computes it.
"""

from fractions import Fraction
from itertools import combinations
import json
from math import comb
from pathlib import Path


def adjacency(n, edges):
    out = [0] * n
    for u, v in edges:
        assert 0 <= u < n and 0 <= v < n and u != v
        out[u] |= 1 << v
        out[v] |= 1 << u
    return out


def is_connected_mask(adj, selected):
    if not selected:
        return False
    seen = selected & -selected
    frontier = seen
    while frontier:
        bit = frontier & -frontier
        frontier -= bit
        v = bit.bit_length() - 1
        newly = adj[v] & selected & ~seen
        seen |= newly
        frontier |= newly
    return seen == selected


def coefficients(n, edges):
    adj = adjacency(n, edges)
    out = [0] * (n + 1)
    for selected in range(1, 1 << n):
        if is_connected_mask(adj, selected):
            out[selected.bit_count()] += 1
    return out


def evaluate(coeffs, x):
    y = 0
    for c in reversed(coeffs):
        y = y * x + c
    return y


def multiply(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def compose(outer, inner):
    out = [0]
    for c in reversed(outer):
        out = multiply(out, inner)
        out[0] += c
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def padded(coeffs, length):
    assert len(coeffs) <= length
    return coeffs + [0] * (length - len(coeffs))


def labeled_graphs(n):
    pairs = list(combinations(range(n), 2))
    for mask in range(1 << len(pairs)):
        yield [edge for j, edge in enumerate(pairs) if mask >> j & 1]


def attach_leaves(n, edges, k=1):
    return n * (k + 1), list(edges) + [
        (v, n + k * v + j) for v in range(n) for j in range(k)
    ]


def attach_c5(n, edges):
    extra = []
    for v in range(n):
        ring = [v] + [n + 4 * v + j for j in range(4)]
        extra += [(ring[j], ring[(j + 1) % 5]) for j in range(5)]
    return 5 * n, list(edges) + extra


def clique_substitute(n, edges, k):
    out = [
        (v * k + i, v * k + j)
        for v in range(n) for i in range(k) for j in range(i + 1, k)
    ]
    out += [
        (u * k + i, v * k + j) for u, v in edges
        for i in range(k) for j in range(k)
    ]
    return n * k, out


def main():
    counts = {
        "pendant_leaf_graphs": 0,
        "two_leaf_graphs": 0,
        "rooted_c5_graphs": 0,
        "clique_substitution_graphs": 0,
        "full_single_call_reductions": 0,
        "exact_unit_circle_norm_checks": 0,
    }
    examples = []

    # Exhaustive, all labeled graphs n <= 5, including disconnected graphs.
    for n in range(6):
        for edges in labeled_graphs(n):
            c = coefficients(n, edges)
            nn, ee = attach_leaves(n, edges)
            actual = coefficients(nn, ee)
            predicted = padded(compose(c, [0, 1, 1]), nn + 1)
            if n:
                predicted[1] += n
            assert actual == predicted, (n, edges, "leaf-polynomial")
            assert evaluate(actual, -2) + 2 * n == evaluate(c, 2)
            counts["pendant_leaf_graphs"] += 1

    # Two independent leaves: root polynomial x(1+x)^2, remainder 2nx.
    for n in range(4):
        for edges in labeled_graphs(n):
            c = coefficients(n, edges)
            nn, ee = attach_leaves(n, edges, 2)
            actual = coefficients(nn, ee)
            predicted = padded(compose(c, [0, 1, 2, 1]), nn + 1)
            if n:
                predicted[1] += 2 * n
            assert actual == predicted, (n, edges, "two-leaf-polynomial")
            counts["two_leaf_graphs"] += 1

    # The actual C5 attachment graphs have up to 15 vertices.
    rooted = [0, 1, 2, 3, 4, 1]
    deleted_root = [0, 4, 3, 2, 1]
    assert evaluate(rooted, -1) == 1
    assert evaluate(deleted_root, -1) == -2
    for n in range(4):
        for edges in labeled_graphs(n):
            c = coefficients(n, edges)
            nn, ee = attach_c5(n, edges)
            actual = coefficients(nn, ee)
            predicted = padded(compose(c, rooted), nn + 1)
            for j in range(min(len(deleted_root), len(predicted))):
                predicted[j] += n * deleted_root[j]
            assert actual == predicted, (n, edges, "C5-polynomial")
            assert evaluate(actual, -1) + 2 * n == sum(c)
            counts["rooted_c5_graphs"] += 1

    for n in range(5):
        for edges in labeled_graphs(n):
            c = coefficients(n, edges)
            for k in (1, 2):
                nn, ee = clique_substitute(n, edges, k)
                actual = coefficients(nn, ee)
                inner = [0] + [comb(k, j) for j in range(1, k + 1)]
                predicted = padded(compose(c, inner), nn + 1)
                assert actual == predicted, (n, edges, k, "clique-polynomial")
                counts["clique_substitution_graphs"] += 1

    # Full actual-oracle construction and integer digit decoding; n <= 2.
    # A separate check of the general formulas above covers much larger inputs.
    for n in range(1, 3):
        for edges in labeled_graphs(n):
            k = n + 1
            nn, ee = clique_substitute(n, edges, k)
            hn, he = attach_leaves(nn, ee)
            oracle_answer = evaluate(coefficients(hn, he), -2)
            y = oracle_answer + 2 * n * k
            base = 3 ** k - 1
            digits = []
            while y:
                y, d = divmod(y, base)
                digits.append(d)
            expected = coefficients(n, edges)
            assert padded(digits, n + 1) == expected
            assert sum(digits) == sum(expected)
            examples.append({
                "input_vertices": n, "input_edges": edges,
                "query_vertices": hn, "base": base,
                "oracle_answer": oracle_answer,
                "decoded_coefficients": padded(digits, n + 1),
            })
            counts["full_single_call_reductions"] += 1

    # Exact rational verification of norm identity with a = Re(zeta) and
    # b^2 = 1-a^2. These controls do not assert a new result from sampling.
    for denominator in range(1, 21):
        for numerator in range(-denominator, denominator + 1):
            a = Fraction(numerator, denominator)
            b_squared = 1 - a * a
            real_part = 2 * a * a - a
            imag_factor = 2 * a - 1
            norm_squared = real_part**2 + imag_factor**2 * b_squared
            assert norm_squared == (2 * a - 1)**2
            counts["exact_unit_circle_norm_checks"] += 1

    result = {
        "problem": 3489,
        "date": "2026-10-09",
        "all_passed": True,
        "arithmetic": "exact integers and fractions; no floating point",
        "left_sides": "direct subset enumeration of constructed graphs",
        "counts": counts,
        "single_call_examples": examples,
        "scope": "Finite controls only; general statements follow from the proof.",
    }
    target = Path(__file__).with_name("connected-set-checks.json")
    target.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
