#!/usr/bin/env python3
"""Main-thread finite audit; imports neither B14 research implementation."""
from collections import Counter
from itertools import combinations, product
import json
from pathlib import Path
from random import Random

HERE = Path(__file__).resolve().parent


def edge(a, b):
    return tuple(sorted((a, b)))


def connected(n, edges):
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    seen, pending = {0}, [0]
    while pending:
        for v in adj[pending.pop()]:
            if v not in seen:
                seen.add(v)
                pending.append(v)
    return len(seen) == n


def exchanges(n):
    tour = {edge(i, (i + 1) % n) for i in range(n)}
    out = []
    for i, j in combinations(range(n), 2):
        a, b, c, d = i, (i + 1) % n, j, (j + 1) % n
        if len({a, b, c, d}) != 4:
            continue
        remainder = tour - {edge(a, b), edge(c, d)}
        candidates = [(edge(a, c), edge(b, d)), (edge(a, d), edge(b, c))]
        valid = [p for p in candidates if connected(n, remainder | set(p))]
        assert len(valid) == 1
        assert not (set(valid[0]) & tour)
        out.append(((i, j), valid[0]))
    return out


def audit():
    constraints = 0
    for n in range(3, 31):
        ex = exchanges(n)
        counts = Counter(chord for _, chords in ex for chord in chords)
        assert len(ex) == n * (n - 3) // 2
        assert len(counts) == len(ex)
        assert all(k == 2 for k in counts.values())
        constraints += len(ex)

    grid_cases = 0
    for n, q in [(4, 3), (5, 3), (6, 2)]:
        ex = exchanges(n)
        chord_list = sorted({e for _, es in ex for e in es})
        indices = {e: i for i, e in enumerate(chord_list)}
        indexed = [(pair, tuple(indices[e] for e in es)) for pair, es in ex]
        sums = [a + b for a, b in product(range(q), repeat=2)]
        for x in product(range(q), repeat=n):
            requirements = [(k, l, x[i] + x[j]) for (i, j), (k, l) in indexed]
            good = sum(all(y[k] + y[l] >= t for k, l, t in requirements)
                       for y in product(range(q), repeat=len(chord_list)))
            individual_product = 1
            for _, _, t in requirements:
                individual_product *= sum(s >= t for s in sums)
            # Same number of independent chord variables and exchange constraints.
            # Squaring clears the read-two square roots and all denominators.
            assert good * good <= individual_product
            grid_cases += 1

    rng = Random(1414)
    quadratic_cases = 0
    for n in range(3, 101):
        pairs = [(i, j) for i, j in combinations(range(n), 2)
                 if (i - j) % n not in (1, n - 1)]
        for _ in range(8):
            x = [rng.randrange(21) for _ in range(n)]
            a = sum(v * v for v in x)
            s = sum(x)
            b = sum(x[i] * x[(i + 1) % n] for i in range(n))
            quadratic = sum((x[i] + x[j]) ** 2 for i, j in pairs)
            assert quadratic == (n - 4) * a + s * s - 2 * b
            assert quadratic >= (n - 6) * a + s * s
            quadratic_cases += 1

    # Independent subtour-LP feasibility check for the Petersen obstruction.
    cheap = ({edge(i, (i + 1) % 5) for i in range(5)} |
             {edge(i, i + 5) for i in range(5)} |
             {edge(i + 5, (i + 2) % 5 + 5) for i in range(5)})
    assert len(cheap) == 15
    assert all(sum(v in e for e in cheap) == 3 for v in range(10))
    cuts = [sum(((mask >> a) & 1) != ((mask >> b) & 1) for a, b in cheap)
            for mask in range(1, (1 << 10) - 1)]
    assert min(cuts) == 3
    saved = json.loads((HERE / 'elimination/petersen-obstruction.json').read_text())
    # Original exhaustive tour receipt is independently checked by the DP run.
    assert saved['optimal_cost'] == 11
    matrix = saved['instance']['costs']
    covered = set()
    for witness in saved['edge_witnesses']:
        tour = witness['tour']
        assert sorted(tour) == list(range(10))
        tour_edges = {edge(tour[i], tour[(i + 1) % 10]) for i in range(10)}
        assert sum(matrix[a][b] for a, b in tour_edges) == 11
        assert tuple(witness['edge']) in tour_edges
        covered.add(tuple(witness['edge']))
    assert covered == set(combinations(range(10), 2))
    result = {
        'status': 'passed',
        'exchange_accounting': {'n_range': [3, 30], 'constraints': constraints,
                                'chord_occurrences': 2},
        'full_grid_joint_inequality': {'cases': grid_cases,
                                      'sizes_and_grids': [[4, 3], [5, 3], [6, 2]]},
        'quadratic_identity_and_lower_bound': {'cases': quadratic_cases, 'n_range': [3, 100]},
        'petersen_subtour_lp': {'proper_cuts': len(cuts), 'minimum_cheap_cut': min(cuts),
                               'lp_value': 10, 'tour_optimum': 11},
        'scope': 'finite checks support a separate mathematical review; no formal proof assistant'
    }
    (HERE / 'COUNT-CHECK-RESULTS.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    audit()
