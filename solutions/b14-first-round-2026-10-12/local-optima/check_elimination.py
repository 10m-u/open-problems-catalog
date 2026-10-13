#!/usr/bin/env python3
"""Independent bounded audit of the main thread's forced 1-tree formulas.

Pruefer sequences enumerate every spanning tree without using Prim/Kruskal or
path maxima. Direct tour enumeration checks the lower-bound direction and the
strict deletion rule. The target modules are read without writing bytecode.
"""

import importlib.util
from itertools import combinations, permutations, product
import json
from pathlib import Path
import random
import sys

sys.dont_write_bytecode = True
BASE = Path(__file__).resolve().parent.parent / "elimination"


def load(name):
    spec = importlib.util.spec_from_file_location(name, BASE / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


one_tree = load("one_tree")
checker = load("check_certificate")


def edge(a, b):
    return tuple(sorted((a, b)))


def all_trees(vertices):
    m = len(vertices)
    for sequence in product(vertices, repeat=m - 2):
        degree = {v: 1 for v in vertices}
        for v in sequence:
            degree[v] += 1
        tree = set()
        for v in sequence:
            leaf = min(u for u in vertices if degree[u] == 1)
            tree.add(edge(leaf, v))
            degree[leaf] -= 1
            degree[v] -= 1
        last = [u for u in vertices if degree[u] == 1]
        assert len(last) == 2
        tree.add(edge(*last))
        yield tree


def all_tours(c):
    n = len(c)
    for tail in permutations(range(1, n)):
        if tail[0] < tail[-1]:
            tour = (0,) + tail
            edges = {edge(tour[i], tour[(i + 1) % n]) for i in range(n)}
            yield tour, edges, sum(c[a][b] for a, b in edges)


def main():
    rng = random.Random(14549)
    snapshots_checked = forced_checked = checker_calls = 0
    signed_snapshots = tie_snapshots = 0
    rows = []
    for n in range(3, 8):
        for case in range(4):
            c = [[0] * n for _ in range(n)]
            for a, b in combinations(range(n), 2):
                c[a][b] = c[b][a] = 1 if case == 0 else rng.randrange(5)
            if case == 0:
                potentials, scale = [0] * n, 1
            elif case == 1:
                potentials, scale = [rng.randrange(-8, 9) for _ in range(n)], 3
            elif case == 2:
                potentials, scale = [rng.randrange(-200, -19) for _ in range(n)], 1
            else:
                potentials, scale = [40 * (-1) ** v for v in range(n)], 2
            tours = list(all_tours(c))
            upper = min(value for _, _, value in tours)
            incumbent = next(tour for tour, _, value in tours if value == upper)
            all_edges = set(combinations(range(n), 2))
            forced_tour_optima = {
                e: min(value for _, edges, value in tours if e in edges) for e in all_edges
            }
            for root in range(n):
                cert, forced, _ = one_tree.snapshot(c, root, potentials, scale)
                vertices = [v for v in range(n) if v != root]
                w = [[scale * c[a][b] + potentials[a] + potentials[b]
                      for b in range(n)] for a in range(n)]
                trees = [(tree, sum(w[a][b] for a, b in tree)) for tree in all_trees(vertices)]
                assert len(trees) == len(vertices) ** (len(vertices) - 2)
                minimum = min(value for _, value in trees)
                spokes = [(set((edge(root, a), edge(root, b))), w[root][a] + w[root][b])
                          for a, b in combinations(vertices, 2)]
                minimum_spokes = min(value for _, value in spokes)
                base = minimum + minimum_spokes - 2 * sum(potentials)
                assert cert["bound_numerator"] == base
                for e, bound in forced.items():
                    if root in e:
                        exact = minimum + min(value for es, value in spokes if e in es)
                    else:
                        exact = min(value for es, value in trees if e in es) + minimum_spokes
                    exact -= 2 * sum(potentials)
                    assert bound == exact, (n, case, root, e, bound, exact)
                    assert bound <= scale * forced_tour_optima[e]
                    forced_checked += 1
                removed = {e for e, bound in forced.items() if bound > scale * upper}
                assert all(not (es & removed) for _, es, value in tours if value == upper)
                data = {
                    "schema": "b14-one-tree-certificate-v1",
                    "instance": {"id": f"independent-audit-n{n}-case{case}-root{root}", "costs": c},
                    "method": "independent-pruefer-audit",
                    "incumbent": {"tour": list(incumbent), "cost": upper},
                    "certificates": [cert],
                    "forced_bounds": [{"edge": list(e), "numerator": forced[e],
                                       "scale": scale, "certificate": 0} for e in sorted(all_edges)],
                    "eliminated_edges": sorted(removed),
                    "residual_edges": sorted(all_edges - removed),
                    "global_lower_bound": {"numerator": base, "scale": scale, "certificate": 0},
                }
                checker.verify(data)
                checker_calls += 1
                snapshots_checked += 1
                signed = any(w[a][b] < 0 for a, b in all_edges)
                ties = len({w[a][b] for a, b in all_edges}) < len(all_edges)
                signed_snapshots += signed
                tie_snapshots += ties
                rows.append({"n": n, "case": case, "root": root,
                             "negative_transformed_edges": signed, "tied_transformed_edges": ties,
                             "deleted_edges": len(removed)})
    report = {"status": "passed", "random_seed": 14549,
              "n_range": [3, 7], "snapshots_checked": snapshots_checked,
              "forced_bounds_checked_against_exhaustive_trees": forced_checked,
              "standalone_checker_calls": checker_calls,
              "snapshots_with_negative_transformed_edges": signed_snapshots,
              "snapshots_with_tied_transformed_weights": tie_snapshots,
              "checks": ["all forced minimum 1-tree values agree with exhaustive Pruefer trees",
                         "all forced bounds are at most minimum cost of a forced-edge tour",
                         "strict deletion preserves every optimum tour",
                         "independent certificate checker accepts recomputed exact certificates"],
              "cases": rows}
    output = Path(__file__).with_name("ELIMINATION-CHECK-RESULTS.json")
    output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({k: v for k, v in report.items() if k != "cases"}, indent=2))


if __name__ == "__main__":
    main()
