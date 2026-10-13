#!/usr/bin/env python3
"""Exact small-tree and preserved-metric checks of the subdivision obstruction."""
import sys
sys.dont_write_bytecode = True
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path
from check_mst_envelope import family, distances


def prufer_edges(n, code):
    degree = [1] * n
    for v in code:
        degree[v] += 1
    edges = []
    for v in code:
        leaf = min(i for i, x in enumerate(degree) if x == 1)
        edges.append((leaf, v))
        degree[leaf] -= 1
        degree[v] -= 1
    a, b = [i for i, x in enumerate(degree) if x == 1]
    return edges + [(a, b)]


def all_nn_costs(d, start):
    n = len(d)
    stack = [(start, frozenset(range(n)) - {start}, F(0))]
    while stack:
        current, remaining, cost = stack.pop()
        if not remaining:
            yield cost + d[current][start]
            continue
        nearest = min(d[current][v] for v in remaining)
        for v in remaining:
            if d[current][v] == nearest:
                stack.append((v, remaining - {v}, cost + nearest))


def main():
    tree_weightings = start_cases = orders = 0
    for n in range(3, 6):
        for code in product(range(n), repeat=n - 2):
            es = prufer_edges(n, code)
            for weights in product((F(1), F(3, 2)), repeat=n - 1):
                a = [[] for _ in range(n)]
                for (u, v), w in zip(es, weights):
                    a[u].append((v, w)); a[v].append((u, w))
                d = distances(a)
                opt = 2 * sum(weights)
                tree_weightings += 1
                for start in range(n):
                    start_cases += 1
                    for cost in all_nn_costs(d, start):
                        orders += 1
                        assert cost == opt

    retained_pairs = 0
    recursive_receipts = []
    for k in range(1, 8):
        a, left, _, _, _ = family(k, F(1, 4 * k))
        old_n = len(a)
        original_d = distances(a)
        subdivided = [[] for _ in a]
        for u, row in enumerate(a):
            for v, w in row:
                if u >= v:
                    continue
                if w.denominator == 1:
                    previous = u
                    for _ in range(int(w) - 1):
                        next_v = len(subdivided)
                        subdivided.append([])
                        subdivided[previous].append((next_v, F(1)))
                        subdivided[next_v].append((previous, F(1)))
                        previous = next_v
                    subdivided[previous].append((v, F(1)))
                    subdivided[v].append((previous, F(1)))
                else:
                    subdivided[u].append((v, w)); subdivided[v].append((u, w))
        ds = distances(subdivided)
        for u in range(old_n):
            for v in range(u + 1, old_n):
                retained_pairs += 1
                assert ds[u][v] == original_d[u][v]
        # A single deterministic NN order on larger controls; all ties were
        # exhaustively checked above only at n<=5.
        remaining = set(range(len(subdivided))) - {left}
        current = left
        cost = F(0)
        while remaining:
            target = min(remaining, key=lambda v: (ds[current][v], v))
            cost += ds[current][target]
            current = target
            remaining.remove(target)
        cost += ds[current][left]
        weight = sum(w for u, row in enumerate(subdivided) for v, w in row if u < v)
        assert cost == 2 * weight
        recursive_receipts.append({"k": k, "old_cities": old_n,
                                   "all_cities": len(subdivided), "nn_ratio": "1"})

    gamma_controls = []
    for m in (48, 64, 96, 128, 256):
        # Sum M Exp(1) minus sum 2M Exp(1): mean -M, variance 3M.
        chebyshev = F(3 * m, m * m)
        joint_lower = F(1, 8) - chebyshev
        assert joint_lower >= F(1, 16)
        gamma_controls.append({"M": m, "order_disagreement_lower": str(joint_lower)})
    result = {"status": "passed", "arithmetic": "exact rational",
              "near_unit_tree_weightings": tree_weightings,
              "near_unit_start_cases": start_cases,
              "all_tied_nn_orders": orders,
              "retained_original_distance_pairs": retained_pairs,
              "subdivided_families": recursive_receipts,
              "gamma_controls": gamma_controls,
              "scope": "finite controls support the independent all-size proof; not an exponential-tree expected-ratio resolution"}
    Path(__file__).with_name("SUBDIVISION-CHECK-RESULTS.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k not in ("subdivided_families", "gamma_controls")}, indent=2))


if __name__ == "__main__":
    main()
