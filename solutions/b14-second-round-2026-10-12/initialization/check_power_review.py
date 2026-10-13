#!/usr/bin/env python3
"""Independent exact scope/vertex controls for the main power-route audit."""
from itertools import combinations
from fractions import Fraction as F
from pathlib import Path
import json


def degrees(n, edges):
    out = [0] * n
    for u, v in edges:
        out[u] += 1; out[v] += 1
    return out


def rank(matrix):
    a = [[F(x) for x in row] for row in matrix]
    pivot = 0
    for column in range(len(a[0])):
        selected = next((r for r in range(pivot, len(a)) if a[r][column]), None)
        if selected is None:
            continue
        a[pivot], a[selected] = a[selected], a[pivot]
        divisor = a[pivot][column]
        a[pivot] = [x / divisor for x in a[pivot]]
        for r in range(len(a)):
            if r != pivot and a[r][column]:
                f = a[r][column]
                a[r] = [x - f * y for x, y in zip(a[r], a[pivot])]
        pivot += 1
        if pivot == len(a):
            break
    return pivot


def main():
    n = 20
    base = {e for e in combinations(range(n), 2)
            if min(e[1] - e[0], n - e[1] + e[0]) <= 2}
    graph = base | {(0, 3), (10, 13)}
    assert min(degrees(n, graph)) == 4
    rotations = []
    degree_obstructions = 0
    for start in range(n):
        mapping = {v: (v - start) % n for v in range(n)}
        rotated = {tuple(sorted((mapping[u], mapping[v]))) for u, v in graph}
        cut = {e for e in rotated if e[1] - e[0] <= 3}
        d = degrees(n, cut)
        assert max(d) == 5 and sum(x <= 4 for x in d) >= 16
        # Sorted matching is a necessary condition for *any* assignment of
        # these vertex degrees to the theorem's positions, even ignoring bandwidth.
        sd = sorted(d)
        for width in range(3, n):
            asym = sorted(min(i + 2, width + 2, width + n - i - 1)
                          for i in range(n))
            host_deg = [min(width, i) + min(width, n - 1 - i) for i in range(n)]
            effective = sorted(min(width + 2, x) for x in host_deg)
            assert any(x < y for x, y in zip(sd, asym))
            assert any(x < y for x, y in zip(sd, effective))
            degree_obstructions += 2
        rotations.append({"start": start, "degree5_vertices": sum(x == 5 for x in d),
                          "degree_at_most4_vertices": sum(x <= 4 for x in d)})

    spokes = {tuple(sorted((i, i + 5))) for i in range(5)}
    outer = {tuple(sorted((i, (i + 1) % 5))) for i in range(5)}
    inner = {tuple(sorted((i + 5, 5 + (i + 2) % 5))) for i in range(5)}
    support = sorted(spokes | outer | inner)
    x = {e: F(1) if e in spokes else F(1, 2) for e in support}
    assert len(support) == 15
    equations = [[int(v in e) for e in support] for v in range(10)]
    equations += [[int(e == s) for e in support] for s in sorted(spokes)]
    r = rank(equations)
    assert r == 15
    cuts = 0
    for mask in range(1, 2 ** 10 - 1):
        cut_sum = sum(value for (u, v), value in x.items()
                      if bool(mask & (1 << u)) != bool(mask & (1 << v)))
        assert cut_sum >= 2
        cuts += 1
    # Exhaust all cheap Hamilton paths rooted at 0; none can close into a cycle.
    adjacency = [set() for _ in range(10)]
    for u, v in support:
        adjacency[u].add(v); adjacency[v].add(u)
    stack = [(0, (0,))]
    cheap_hamilton_cycles = 0
    while stack:
        current, path = stack.pop()
        if len(path) == 10:
            cheap_hamilton_cycles += int(0 in adjacency[current])
        else:
            for v in adjacency[current] - set(path):
                stack.append((v, path + (v,)))
    assert cheap_hamilton_cycles == 0
    result = {"status": "passed", "arithmetic": "exact rational/integer",
              "strengthened_cycle_transfer_cuts": 20,
              "arbitrary_degree_assignment_failures": degree_obstructions,
              "petersen_supported_constraint_rank": r,
              "petersen_proper_cuts": cuts,
              "petersen_cheap_hamilton_cycles": cheap_hamilton_cycles,
              "rotations": rotations,
              "scope": "independent controls for theorem-transfer scope and fractional-vertex proof; no conjecture counterexample"}
    Path(__file__).with_name("POWER-REVIEW-CHECK-RESULTS.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "rotations"}, indent=2))


if __name__ == "__main__":
    main()
