#!/usr/bin/env python3
"""Compare graphical frontier DP with independent metric subset DP."""
import importlib.util
from itertools import product
import json
from pathlib import Path
from random import Random
from time import perf_counter
from euler_dp import solve, check_walk, shortcut

HERE = Path(__file__).resolve().parent
BASE = HERE.parents[1] / 'b14-first-round-2026-10-12/elimination/one_tree.py'
spec = importlib.util.spec_from_file_location('b14_reference', BASE)
reference = importlib.util.module_from_spec(spec)
spec.loader.exec_module(reference)


def closure(n, edges):
    infinity = sum(w for _, _, w in edges) + 1
    c = [[0 if i == j else infinity for j in range(n)] for i in range(n)]
    for a, b, w in edges:
        c[a][b] = c[b][a] = w
    for k in range(n):
        for i in range(n):
            for j in range(n):
                c[i][j] = min(c[i][j], c[i][k] + c[k][j])
    return c


def instance(n, family, seed):
    rng = Random(seed + 14200)
    pairs = {(i, i + 1) for i in range(n - 1)}
    if family == 'star':
        pairs = {(0, i) for i in range(1, n)}
    elif family == 'cycle':
        pairs.add((0, n - 1))
    elif family == 'ladder':
        pairs = {(i, i + 1) for i in range(n - 1) if i % 2 == 0}
        pairs.update((i, i + 2) for i in range(n - 2))
    elif family == 'triangles':
        pairs.update((i, i + 2) for i in range(0, n - 2, 2))
    return [(a, b, rng.randrange(1, 10)) for a, b in sorted(pairs)]


def main():
    started = perf_counter()
    rows = []
    for family in ['path', 'star', 'cycle', 'ladder', 'triangles']:
        for n in [6, 8, 10, 12]:
            for seed in [0, 1]:
                edges = instance(n, family, seed)
                compressed = solve(n, edges)
                raw = solve(n, edges, compress=False)
                c = closure(n, edges)
                optimum, _, subset_work = reference.exact_tour(c)
                assert compressed['optimum'] == raw['optimum'] == optimum
                assert check_walk(n, edges, compressed['multiplicities']) == optimum
                tour = shortcut(n, edges, compressed['multiplicities'])
                assert reference.cost(c, tour) == optimum
                assert compressed['states'] <= raw['states']
                rows.append({'family': family, 'n': n, 'seed': seed, 'edges': edges,
                             'metric_optimum': optimum, 'tour': tour, 'compressed': compressed,
                             'raw_degrees': raw, 'metric_subset_work': subset_work})

    # All multiplicity assignments are a second exact oracle on small graphs.
    exhaustive = 0
    for weights in [(0, 0, 0, 0, 0), (1, 2, 3, 4, 5), (2, 2, 1, 1, 2)]:
        edges = [(a, b, w) for (a, b), w in zip([(0,1),(0,2),(1,2),(1,3),(2,3)], weights)]
        valid_costs = []
        for q in product(range(3), repeat=5):
            try:
                value = check_walk(4, edges, q)
            except AssertionError:
                continue
            valid_costs.append(value)
        assert solve(4, edges)['optimum'] == min(valid_costs)
        # Reverse processing order tests that the frontier, not labels, controls correctness.
        assert solve(4, list(reversed(edges)))['optimum'] == min(valid_costs)
        exhaustive += 1

    totals = {}
    for family in ['path', 'star', 'cycle', 'ladder', 'triangles']:
        subset = [r for r in rows if r['family'] == family]
        totals[family] = {
            'instances': len(subset),
            'compressed_states': sum(r['compressed']['states'] for r in subset),
            'raw_degree_states': sum(r['raw_degrees']['states'] for r in subset),
            'compressed_transitions': sum(r['compressed']['transitions'] for r in subset),
            'metric_subset_transitions': sum(r['metric_subset_work']['transitions'] for r in subset),
            'max_frontier': max(r['compressed']['max_frontier'] for r in subset)}
    result = {'status': 'passed', 'instances_checked': len(rows), 'exhaustive_small_graphs': exhaustive,
              'all_three_optimum_methods_agree': True, 'totals': totals,
              'elapsed_seconds': perf_counter() - started, 'instances': rows}
    (HERE / 'DP-CHECK-RESULTS.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'instances'}, indent=2))


if __name__ == '__main__':
    main()
