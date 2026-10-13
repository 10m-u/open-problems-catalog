#!/usr/bin/env python3
"""Exact local cuts and integral min-cut checks for the necklace obstruction."""
from itertools import combinations, permutations
import json
from pathlib import Path
from random import Random
import networkx as nx

HERE = Path(__file__).resolve().parent


def edge(a, b):
    return tuple(sorted((a, b)))


def necklace(k):
    weights = {}
    for i in range(k):
        base = 10 * i
        for j in range(5):
            weights[edge(base + j, base + (j + 1) % 5)] = 1
            weights[edge(base + 5 + j, base + 5 + (j + 2) % 5)] = 1
            if j != 0:
                weights[edge(base + j, base + 5 + j)] = 2
        weights[edge(base + 5, 10 * ((i + 1) % k))] = 2
    return weights


def permute_to(n, source, target):
    sigma = list(range(n))
    for origin, destination in zip(source, target):
        other = sigma.index(destination)
        sigma[origin], sigma[other] = sigma[other], sigma[origin]
    assert tuple(sigma[v] for v in source) == target
    assert sum(i != v for i, v in enumerate(sigma)) <= 4
    return sigma


def mincut(n, weights):
    graph = nx.Graph()
    graph.add_nodes_from(range(n))
    graph.add_weighted_edges_from((a, b, w) for (a, b), w in weights.items())
    return nx.stoer_wagner(graph)[0]


def main():
    # Exhaustively prove the fixed ten-vertex gadget facts.
    petersen = necklace(1)
    assert len(petersen) == 15
    local_cuts = 0
    for mask in range(1, (1 << 10) - 1):
        capacity = sum(w for (a, b), w in petersen.items()
                       if ((mask >> a) & 1) != ((mask >> b) & 1))
        assert capacity >= 4
        removed = capacity - (2 if ((mask >> 0) & 1) != ((mask >> 5) & 1) else 0)
        assert removed >= 2
        if ((mask >> 0) & 1) == ((mask >> 5) & 1):
            assert removed >= 4
        local_cuts += 1
    hamiltonian = 0
    for rest in permutations(range(1, 10)):
        if rest[0] > rest[-1]:
            continue
        tour = (0,) + rest
        if all(edge(tour[i], tour[(i + 1) % 10]) in petersen for i in range(10)):
            hamiltonian += 1
    assert hamiltonian == 0

    cases = []
    rng = Random(142)
    force_cases = 0
    for k in [2, 3, 4, 8, 17, 20]:
        n = 10 * k
        original = necklace(k)
        assert len(original) == 15 * k
        assert sum(original.values()) == 2 * n
        assert all(sum(w for e, w in original.items() if v in e) == 4 for v in range(n))
        cut_value = mincut(n, original)
        assert cut_value >= 4
        unit_edge = next(e for e, w in original.items() if w == 2)
        all_edges = list(combinations(range(n), 2))
        targets = all_edges if k == 2 else rng.sample(all_edges, 24)
        highest_cost_numerator = 0
        for target in targets:
            sigma = permute_to(n, unit_edge, target)
            relabeled = {edge(sigma[a], sigma[b]): w for (a, b), w in original.items()}
            assert relabeled[target] == 2
            assert all(sum(w for e, w in relabeled.items() if v in e) == 4 for v in range(n))
            cost_num = sum(w * (1 if e in original else 2) for e, w in relabeled.items())
            assert cost_num <= 2 * (n + 8)
            highest_cost_numerator = max(highest_cost_numerator, cost_num)
            if k == 2:
                assert mincut(n, relabeled) >= 4
            force_cases += 1
        if k >= 17:
            assert 2 * n + 9 <= 2 * n + (k + 1) // 2
        cases.append({'k': k, 'cities': n, 'global_cut_numerator': cut_value,
                      'forced_edges_checked': len(targets),
                      'max_forced_primary_cost_numerator': highest_cost_numerator,
                      'fractional_cost_scale': 2})
    result = {
        'status': 'passed', 'local_cuts_exhausted': local_cuts,
        'petersen_undirected_tours_enumerated': 181440, 'petersen_hamiltonian_tours': hamiltonian,
        'necklaces': cases, 'forced_witnesses_checked': force_cases,
        'large_binary_perturbation': 'verified symbolically in RESULT.md; not materialized',
        'scope': 'finite exact checks support the all-size proof; no exhaustive tour search on necklaces'
    }
    (HERE / 'OBSTRUCTION-CHECK-RESULTS.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
