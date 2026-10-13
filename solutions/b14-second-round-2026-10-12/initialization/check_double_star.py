#!/usr/bin/env python3
"""Exact finite double-star phase checks; no probabilistic estimate."""

from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path


def instance(left, right, bridge):
    m = len(left)
    assert len(right) == m
    n = 2 * m + 2
    sides = [0, 1] + [0] * m + [1] * m
    spokes = [0, 0] + list(left) + list(right)
    d = [[0] * n for _ in range(n)]
    for a in range(n):
        for b in range(n):
            if a != b:
                d[a][b] = spokes[a] + spokes[b] + (bridge if sides[a] != sides[b] else 0)
    return sides, d


def run(left, right, bridge):
    sides, d = instance(left, right, bridge)
    n = len(d)
    remaining, tour = set(range(1, n)), [0]
    while remaining:
        chosen = min(remaining, key=lambda v: (d[tour[-1]][v], v))
        remaining.remove(chosen)
        tour.append(chosen)
    bridge_count = sum(sides[tour[i]] != sides[tour[(i + 1) % n]] for i in range(n))
    cost = sum(d[tour[i]][tour[(i + 1) % n]] for i in range(n))
    assert cost == 2 * sum(left + right) + bridge * bridge_count
    assert bridge_count % 2 == 0 and bridge_count >= 2
    assert bridge * bridge_count <= max(left + right) + 2 * bridge
    return bridge_count


def main():
    exhaustive = 0
    maximum_count = 0
    for m in [1, 2, 3]:
        for weights in product(range(1, 5), repeat=2 * m):
            for bridge in [1, 2, 3]:
                count = run(list(weights[:m]), list(weights[m:]), bridge)
                maximum_count = max(maximum_count, count)
                exhaustive += 1
    occupied = []
    for j in [8, 16, 32, 64]:
        leaf_weights = [F(2 * i + 1, 8) for i in range(j + 1)]
        for bridge in [F(1, 2), F(3, 4), F(1)]:
            count = run(leaf_weights, leaf_weights, bridge)
            t = F(j, 4)
            assert bridge * count >= (t - 1) / 3
            occupied.append({"bins_each_side": j + 1, "T": str(t), "bridge": str(bridge),
                             "bridge_crossings": count, "weighted_charge": str(bridge * count),
                             "proved_lower_bound": str((t - 1) / 3)})
    report = {"status": "passed", "exhaustive_positive_integer_instances": exhaustive,
              "leaves_per_side_checked": [1, 2, 3], "leaf_weights": [1, 2, 3, 4],
              "bridge_weights": [1, 2, 3], "all_ties_use_vertex_order": True,
              "maximum_crossings_in_exhaustive_small_set": maximum_count,
              "checks": ["exact NN tree-cut cost identity", "LC <= maximum_leaf_weight + 2L",
                         "occupied-bin deterministic lower bound"],
              "occupied_bin_cases": occupied,
              "asymptotic_probability_claim": "proved in accompanying note; no simulation"}
    output = Path(__file__).with_name("DOUBLE-STAR-CHECK-RESULTS.json")
    output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({k: v for k, v in report.items() if k != "occupied_bin_cases"}, indent=2))


if __name__ == "__main__":
    main()
