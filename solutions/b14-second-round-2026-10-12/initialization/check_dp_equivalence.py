#!/usr/bin/env python3
"""Independent exact suffix-feasibility audit of the generating-graph DP."""

import importlib.util
from itertools import combinations, permutations, product
import json
from pathlib import Path
import random
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
TARGET = HERE.parent / "generating-graph" / "euler_dp.py"
spec = importlib.util.spec_from_file_location("b14_euler_dp_audit", TARGET)
target = importlib.util.module_from_spec(spec)
spec.loader.exec_module(target)


def selected_components(n, edges, q):
    adj = [set() for _ in range(n)]
    degree = [0] * n
    for (a, b, _), copies in zip(edges, q):
        if copies:
            adj[a].add(b)
            adj[b].add(a)
            degree[a] += copies
            degree[b] += copies
    components = []
    seen = set()
    for v in range(n):
        if degree[v] and v not in seen:
            component, stack = {v}, [v]
            seen.add(v)
            while stack:
                for other in adj[stack.pop()]:
                    if other not in seen:
                        seen.add(other)
                        component.add(other)
                        stack.append(other)
            components.append(component)
    return degree, components


def accepted_state(n, edges, prefix):
    i = len(prefix)
    appeared = {v for a, b, _ in edges[:i] for v in (a, b)}
    future = {v for a, b, _ in edges[i:] for v in (a, b)}
    frontier = sorted(appeared & future)
    forgotten = appeared - future
    degree, components = selected_components(n, edges[:i], prefix)
    if any(not degree[v] or degree[v] % 2 for v in forgotten):
        return None
    closed = [component for component in components if not component.intersection(frontier)]
    if closed and (i < len(edges) or len(closed) != 1):
        return None
    if i == len(edges) and len(components) != 1:
        return None
    flags = tuple(0 if degree[v] == 0 else 1 if degree[v] % 2 else 2 for v in frontier)
    labels = []
    rename = {}
    for v in frontier:
        if not degree[v]:
            labels.append(-1)
        else:
            original = next(j for j, component in enumerate(components) if v in component)
            if original not in rename:
                rename[original] = len(rename)
            labels.append(rename[original])
    return flags, tuple(labels)


def feasible(n, edges, q):
    degree, components = selected_components(n, edges, q)
    return all(d > 0 and d % 2 == 0 for d in degree) and len(components) == 1


def metric_optimum(n, edges):
    infinity = sum(w for _, _, w in edges) + 1
    d = [[0 if a == b else infinity for b in range(n)] for a in range(n)]
    for a, b, w in edges:
        d[a][b] = d[b][a] = w
    for k in range(n):
        for a in range(n):
            for b in range(n):
                d[a][b] = min(d[a][b], d[a][k] + d[k][b])
    return min(sum(d[tour[i]][tour[(i + 1) % n]] for i in range(n))
               for tail in permutations(range(1, n)) for tour in [(0,) + tail])


def main():
    rng = random.Random(1422)
    families = [
        (4, list(combinations(range(4), 2))),
        (4, [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3)]),
        (5, [(0, 1), (1, 2), (2, 3), (3, 4)]),
        (5, [(0, 1), (0, 2), (0, 3), (0, 4)]),
        (5, [(0, 1), (1, 2), (2, 3), (3, 4), (0, 4)]),
        (5, [(0, 1), (1, 2), (0, 2), (2, 3), (3, 4), (2, 4)]),
        (5, [(0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4)]),
    ]
    graph_orders = prefix_checks = collisions = suffix_checks = 0
    optimum_checks = 0
    for n, pairs in families:
        base = [(a, b, 1 + (a * 7 + b * 11) % 5) for a, b in pairs]
        shuffled = list(base)
        rng.shuffle(shuffled)
        for edges in [base, list(reversed(base)), shuffled]:
            graph_orders += 1
            m = len(edges)
            for i in range(m + 1):
                groups = {}
                for prefix in product(range(3), repeat=i):
                    key = accepted_state(n, edges, prefix)
                    if key is None:
                        continue
                    feasible_suffixes = set()
                    for suffix in product(range(3), repeat=m - i):
                        suffix_checks += 1
                        if feasible(n, edges, prefix + suffix):
                            feasible_suffixes.add(suffix)
                    if key in groups:
                        assert groups[key] == feasible_suffixes, (n, edges, i, key, prefix)
                        collisions += 1
                    else:
                        groups[key] = feasible_suffixes
                    prefix_checks += 1
            for weights in [[0] * m, [1] * m, [w for _, _, w in edges]]:
                weighted = [(a, b, w) for (a, b, _), w in zip(edges, weights)]
                brute = min(sum(w * q for (_, _, w), q in zip(weighted, copies))
                            for copies in product(range(3), repeat=m) if feasible(n, weighted, copies))
                compressed = target.solve(n, weighted)
                uncompressed = target.solve(n, weighted, compress=False)
                assert compressed["optimum"] == uncompressed["optimum"] == brute == metric_optimum(n, weighted)
                assert feasible(n, weighted, compressed["multiplicities"])
                optimum_checks += 1
    report = {
        "status": "passed", "graph_families": len(families), "graph_orders": graph_orders,
        "accepted_prefixes_examined": prefix_checks,
        "same_state_prefix_collisions_with_identical_feasible_suffixes": collisions,
        "literal_suffix_feasibility_tests": suffix_checks,
        "four_way_optimum_comparisons": optimum_checks,
        "oracles": ["literal complete multiplicity enumeration", "literal metric tour enumeration",
                    "main compressed frontier DP", "main full-degree frontier DP"],
        "weights": ["all zero", "all tied unit", "explicit unequal positive"],
        "early_close_and_forget_conditions_checked_independently": True,
    }
    output = HERE / "DP-EQUIVALENCE-CHECK-RESULTS.json"
    output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
