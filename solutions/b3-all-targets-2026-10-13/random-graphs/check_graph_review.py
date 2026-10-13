#!/usr/bin/env python3
"""Independent exact full-row, Bonferroni and isolated-claw audit."""
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha256
from itertools import combinations
from math import comb, factorial
from pathlib import Path
import json
import random

HERE = Path(__file__).resolve().parent


def adjacency(n, edges):
    out = [0] * n
    for u, v in edges:
        out[u] |= 1 << v
        out[v] |= 1 << u
    return out


def minimum_element_row(n, edges):
    """Each nonempty independent set has a unique smallest vertex."""
    adj = adjacency(n, edges)

    @lru_cache(None)
    def visit(mask):
        out = [1]
        while mask:
            bit = mask & -mask
            v = bit.bit_length() - 1
            mask -= bit
            row = visit(mask & ~adj[v])
            if len(out) < len(row) + 1:
                out.extend([0] * (len(row) + 1 - len(out)))
            for j, value in enumerate(row, 1):
                out[j] += value
        return tuple(out)

    answer = list(visit((1 << n) - 1))
    states = visit.cache_info().currsize
    return answer, states


def product_row(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def sum_row(a, b):
    return [(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
            for i in range(max(len(a), len(b)))]


def tree_row_and_aut(n, edges):
    adj = [[] for i in range(n)]
    for i, j in edges:
        adj[i].append(j)
        adj[j].append(i)

    def visit(v, parent):
        child = [visit(w, v) for w in adj[v] if w != parent]
        excluded, included = [1], [0, 1]
        aut = 1
        types = Counter()
        for E, I, code, count in child:
            excluded = product_row(excluded, sum_row(E, I))
            included = product_row(included, E)
            aut *= count
            types[code] += 1
        aut *= prod_factorials(types.values())
        return excluded, included, tuple(sorted(types.elements())), aut

    E, I, code, aut = visit(0, -1)
    return sum_row(E, I), aut  # center0 is unique in both reviewed trees


def prod_factorials(values):
    out = 1
    for value in values:
        out *= factorial(value)
    return out


def claw_components(n, edges):
    adj = adjacency(n, edges)
    remaining = (1 << n) - 1
    count = 0
    while remaining:
        root = remaining & -remaining
        component = root
        frontier = root
        while frontier:
            bit = frontier & -frontier
            frontier -= bit
            v = bit.bit_length() - 1
            new = adj[v] & ~component
            component |= new
            frontier |= new
        remaining &= ~component
        vertices = [v for v in range(n) if component >> v & 1]
        if len(vertices) == 4 and sorted(adj[v].bit_count() for v in vertices) == [1, 1, 1, 3]:
            count += 1
    return count


def main():
    packet = json.loads((HERE / 'GRAPH-PROBE.json').read_text())
    rng = random.Random(2400)
    full_rows = total_states = 0
    for record in packet['records']:
        n, d = record['n'], record['d']
        specified = [[i, j] for i, j in combinations(range(n), 2) if rng.random() < d / n]
        assert specified == record['edges']
        row, states = minimum_element_row(n, record['edges'])
        assert row == record['row']
        assert row[:3] == [1, n, comb(n, 2) - len(specified)]
        assert all(x > 0 for x in row)
        assert all(row[k] ** 2 >= row[k - 1] * row[k + 1] for k in range(1, len(row) - 1))
        assert not record['LC_failures']
        full_rows += 1
        total_states += states

    small_graphs = criterion_indices = curvature_controls = 0
    n = 5
    possible = list(combinations(range(n), 2))
    for mask in range(1 << len(possible)):
        edges = [edge for j, edge in enumerate(possible) if mask >> j & 1]
        row = [0] * (n + 1)
        for vertices in range(1 << n):
            if all(not (vertices >> i & 1 and vertices >> j & 1) for i, j in edges):
                row[vertices.bit_count()] += 1
        m = len(edges)
        # Pair unions counted literally rather than using degree/wedge formulas.
        union_sizes = Counter(len(set(first) | set(second))
                              for first, second in combinations(edges, 2))
        mu = [F(m * comb(k, 2), comb(n, 2)) for k in range(n + 1)]
        nu = [sum(F(number * comb(k, size), comb(n, size))
                  for size, number in union_sizes.items()) for k in range(n + 1)]
        for k in range(n + 1):
            assert 1 - mu[k] <= F(row[k], comb(n, k)) <= 1 - mu[k] + nu[k]
        a = F(m, n * (n - 1))
        for k in range(1, n):
            L = 1 - mu[k]
            assert L ** 2 - (1 - mu[k - 1]) * (1 - mu[k + 1]) == 2 * a * L + 4 * a ** 2 * k * (k - 1)
            curvature_controls += 1
            if mu[k + 1] <= F(1, 2) and nu[k + 1] <= F(1, 12 * (k + 1)):
                assert row[k] ** 2 >= row[k - 1] * row[k + 1]
                criterion_indices += 1
        small_graphs += 1

    probability_controls = []
    for n in (5, 6):
        pairs = list(combinations(range(n), 2))
        count_hist, square_hist = Counter(), Counter()
        for mask in range(1 << len(pairs)):
            edges = [edge for j, edge in enumerate(pairs) if mask >> j & 1]
            count = claw_components(n, edges)
            count_hist[len(edges)] += count
            square_hist[len(edges)] += count ** 2
        p, q, h, aut = F(1, 4), F(3, 4), 4, 6
        EX = sum(value * p ** m * q ** (len(pairs) - m) for m, value in count_hist.items())
        EX2 = sum(value * p ** m * q ** (len(pairs) - m) for m, value in square_hist.items())
        falling = factorial(n) // factorial(n - h)
        absent = h * (n - h) + comb(h, 2) - (h - 1)
        formula = F(falling, aut) * p ** (h - 1) * q ** absent
        assert EX == formula and EX2 == EX  # two disjoint claws require8 vertices
        assert EX2 - EX ** 2 <= EX + EX ** 2 * (q ** (-h * h) - 1)
        probability_controls.append({'n': n, 'graphs': 1 << len(pairs),
                                     'expectation': str(EX), 'second_moment': str(EX2)})

    claw_edges = [(0, 1), (0, 2), (0, 3)]
    claw, claw_aut = tree_row_and_aut(4, claw_edges)
    assert claw == [1, 4, 3, 1] and claw_aut == 6
    assert 18 * 3 * 4 - 4 * 3 ** 3 + 3 ** 2 * 4 ** 2 - 4 * 4 ** 3 - 27 == -31
    weighted = [1, 13, 3, 1]
    assert weighted[2] ** 2 - weighted[1] * weighted[3] == -4
    legal = {(4 - len(S),) + tuple(int(v in S) for v in range(4))
             for k in range(5) for S in combinations(range(4), k)
             if all(not (u in S and v in S) for u, v in claw_edges)}
    first, second = (3, 1, 0, 0, 0), (2, 0, 1, 1, 0)
    assert first in legal and second in legal
    for j in (2, 3):
        A, B = list(first), list(second)
        A[1] -= 1; A[j] += 1; B[1] += 1; B[j] -= 1
        assert tuple(A) in legal and tuple(B) not in legal

    tree = packet['known_26_vertex_tree']
    row, aut = tree_row_and_aut(26, tree['edges'])
    assert row == tree['row'] and aut == 6912
    assert row[-3:] == [2979, 51, 1] and row[-2] ** 2 - row[-3] == -378
    receipt = {'status': 'PASS', 'actual_full_rows_independently_recomputed': full_rows,
        'minimum_element_recursion_total_states': total_states,
        'all_five_vertex_graphs_literal_checked': small_graphs,
        'Bonferroni_sufficient_indices': criterion_indices,
        'exact_curvature_identities': curvature_controls,
        'isolated_claw_expectation_and_variance_literal_random_graph_controls': probability_controls,
        'claw_discriminant': -31, 'weighted_claw_defect': -4,
        'actual_exchange_support_failure': True,
        'tree26_automorphism_count_by_rooted_types': aut,
        'tree26_row_by_included_excluded_tree_DP': row,
        'scope': 'Independent finite witnesses; all-size probability/prefix arguments audited in Q2400-INDEPENDENT-REVIEW.md.',
        'reviewed_sha256': {f: sha256((HERE / f).read_bytes()).hexdigest() for f in
            ['Q2400-ATTEMPTS.md', 'BONFERRONI-PREFIX.md', 'ISOLATED-TREES.md', 'graph_probe.py',
             'GRAPH-PROBE.json', 'check_graph_routes.py', 'GRAPH-ROUTES-CHECK.json']},
        'checker_sha256': sha256(Path(__file__).read_bytes()).hexdigest()}
    (HERE / 'GRAPH-REVIEW-CHECK.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps({k: v for k, v in receipt.items() if k != 'reviewed_sha256'}, indent=2))


if __name__ == '__main__':
    main()
