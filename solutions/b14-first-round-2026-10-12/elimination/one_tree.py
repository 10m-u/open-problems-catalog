"""Exact batch forced-edge bounds from rooted minimum 1-trees.

Costs, potentials and certificate numerators are integers. No solver package needed.
The search uses valid bounds throughout; tuning changes strength, not validity.
"""
from itertools import permutations
from math import isqrt
import random


def edge(a, b):
    return (min(a, b), max(a, b))


def cost(c, tour):
    return sum(c[tour[i]][tour[(i + 1) % len(tour)]] for i in range(len(tour)))


def prim(c, vertices):
    seen = {vertices[0]}
    tree = []
    while len(seen) < len(vertices):
        _, a, b = min((c[a][b], a, b) for a in seen for b in vertices if b not in seen)
        tree.append(edge(a, b))
        seen.add(b)
    return tree


def path_maxima(c, vertices, tree):
    adj = {v: [] for v in vertices}
    for a, b in tree:
        adj[a].append(b)
        adj[b].append(a)
    out = {}
    for a in vertices:
        stack = [(a, None, None)]
        while stack:
            v, parent, highest = stack.pop()
            if v != a:
                out[a, v] = highest
            for w in adj[v]:
                if w != parent:
                    value = c[v][w] if highest is None else max(highest, c[v][w])
                    stack.append((w, v, value))
    return out


def snapshot(c, root, potentials, scale=16):
    n = len(c)
    w = [[scale * c[a][b] + potentials[a] + potentials[b] for b in range(n)]
         for a in range(n)]
    vertices = [v for v in range(n) if v != root]
    tree = prim(w, vertices)
    spokes = sorted((w[root][v], v) for v in vertices)
    root_edges = [edge(root, v) for _, v in spokes[:2]]
    value = sum(w[a][b] for a, b in tree + root_edges) - 2 * sum(potentials)
    maximum = path_maxima(w, vertices, tree)
    forced = {}
    for a in range(n):
        for b in range(a + 1, n):
            if root in (a, b):
                other = b if a == root else a
                partner = min(w[root][v] for v in vertices if v != other)
                delta = w[root][other] + partner - spokes[0][0] - spokes[1][0]
            else:
                delta = w[a][b] - maximum[a, b]
            assert delta >= 0
            forced[a, b] = value + delta
    degree = [0] * n
    for a, b in tree + root_edges:
        degree[a] += 1
        degree[b] += 1
    return {
        "root": root, "potentials": list(potentials), "scale": scale,
        "tree_edges": tree, "root_edges": root_edges, "bound_numerator": value,
    }, forced, [d - 2 for d in degree]


def incumbent(c):
    """Every nearest-neighbor start, followed by deterministic best 2-opt."""
    n = len(c)
    candidates = []
    for start in range(n):
        tour = [start]
        remaining = set(range(n)) - {start}
        while remaining:
            nxt = min(remaining, key=lambda v: (c[tour[-1]][v], v))
            remaining.remove(nxt)
            tour.append(nxt)
        while True:
            moves = []
            for i in range(n):
                for j in range(i + 2, n):
                    if i == 0 and j == n - 1:
                        continue
                    a, b = tour[i], tour[(i + 1) % n]
                    d, e = tour[j], tour[(j + 1) % n]
                    gain = c[a][b] + c[d][e] - c[a][d] - c[b][e]
                    if gain > 0:
                        moves.append((-gain, i, j))
            if not moves:
                break
            _, i, j = min(moves)
            tour[i + 1:j + 1] = reversed(tour[i + 1:j + 1])
        candidates.append((cost(c, tour), tour))
    value, tour = min(candidates)
    return tour, value


def exact_tour(c, allowed=None):
    """Independent subset-DP reference with work counters."""
    n = len(c)
    dp, prev = {}, {}
    transitions = 0
    for v in range(1, n):
        if allowed is None or edge(0, v) in allowed:
            dp[1 << (v - 1), v] = c[0][v]
            prev[1 << (v - 1), v] = 0
    for mask in range(1, 1 << (n - 1)):
        for last in range(1, n):
            key = (mask, last)
            if key not in dp:
                continue
            for nxt in range(1, n):
                bit = 1 << (nxt - 1)
                if mask & bit or (allowed is not None and edge(last, nxt) not in allowed):
                    continue
                transitions += 1
                dest = (mask | bit, nxt)
                value = dp[key] + c[last][nxt]
                if dest not in dp or value < dp[dest]:
                    dp[dest], prev[dest] = value, last
    full = (1 << (n - 1)) - 1
    value, last = min((dp[full, v] + c[v][0], v) for v in range(1, n)
                      if (full, v) in dp and (allowed is None or edge(v, 0) in allowed))
    mask, reverse = full, []
    while last:
        reverse.append(last)
        nxt = prev[mask, last]
        mask ^= 1 << (last - 1)
        last = nxt
    return value, [0] + list(reversed(reverse)), {
        "states": len(dp), "transitions": transitions,
    }


def width_upper_bound(n, edges):
    """Greedy minimum-fill elimination width; upper bound, not exact treewidth."""
    adj = {v: set() for v in range(n)}
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    order, width = [], 0
    while adj:
        def key(v):
            neighbors = adj[v]
            missing = sum(b not in adj[a] for a in neighbors for b in neighbors if a < b)
            return missing, len(neighbors), v
        v = min(adj, key=key)
        neighbors = list(adj[v])
        width = max(width, len(neighbors))
        for a in neighbors:
            adj[a].discard(v)
            adj[a].update(b for b in neighbors if b != a)
        del adj[v]
        order.append(v)
    return width, order


def produce(instance, mode):
    c = instance["costs"]
    n, scale = len(c), 16
    tour, upper = incumbent(c)
    roots = [0] if mode != "four-roots" else sorted({0, n // 4, n // 2, 3 * n // 4})
    per_root = 1 if mode == "zero" else 48 // len(roots)
    snapshots, best, global_best = [], {}, None
    for root in roots:
        p = [0] * n
        for iteration in range(per_root):
            cert, bounds, gradient = snapshot(c, root, p, scale)
            idx = len(snapshots)
            snapshots.append(cert)
            if global_best is None or cert["bound_numerator"] > global_best[0]:
                global_best = cert["bound_numerator"], idx
            for e, numerator in bounds.items():
                if e not in best or numerator > best[e][0]:
                    best[e] = numerator, idx
            norm = sum(g * g for g in gradient)
            # Integer subgradient schedule; repeat terminal states to keep the same call budget.
            if mode != "zero" and norm and cert["bound_numerator"] < scale * upper:
                factor = 2 if iteration < per_root // 2 else 1
                step = max(1, factor * (scale * upper - cert["bound_numerator"]) // norm)
                p = [a + step * g for a, g in zip(p, gradient)]
    used = sorted({owner for _, owner in best.values()} | {global_best[1]})
    remap = {old: new for new, old in enumerate(used)}
    eliminated = sorted(e for e, (value, _) in best.items() if value > upper * scale)
    allowed = {e for e in best if e not in eliminated}
    width, order = width_upper_bound(n, allowed)
    optimum, exact, full_work = exact_tour(c)
    residual_optimum, _, residual_work = exact_tour(c, allowed)
    assert optimum == residual_optimum
    assert all(edge(exact[i], exact[(i + 1) % n]) in allowed for i in range(n))
    return {
        "schema": "b14-one-tree-certificate-v1", "instance": instance, "method": mode,
        "incumbent": {"tour": tour, "cost": upper},
        "certificates": [snapshots[i] for i in used],
        "global_lower_bound": {"numerator": global_best[0], "scale": scale,
                               "certificate": remap[global_best[1]]},
        "forced_bounds": [{"edge": e, "numerator": value, "scale": scale,
                           "certificate": remap[owner]} for e, (value, owner) in sorted(best.items())],
        "eliminated_edges": eliminated, "residual_edges": sorted(allowed),
        "measurements": {"snapshot_calls": len(snapshots), "retained_certificates": len(used),
                         "min_fill_width_upper_bound": width, "min_fill_order": order,
                         "optimal_cost": optimum, "optimal_tour": exact,
                         "full_dp": full_work, "residual_dp": residual_work},
    }


def matrix(n, weight):
    c = [[0] * n for _ in range(n)]
    for a in range(n):
        for b in range(a + 1, n):
            c[a][b] = c[b][a] = weight(a, b)
    return c


def petersen_instance():
    cheap = {edge(i, (i + 1) % 5) for i in range(5)}
    cheap |= {edge(i, i + 5) for i in range(5)}
    cheap |= {edge(5 + i, 5 + (i + 2) % 5) for i in range(5)}
    return {"id": "petersen-1-2", "family": "petersen-1-2", "seed": None,
            "costs": matrix(10, lambda a, b: 1 if (a, b) in cheap else 2)}


def instances():
    result = []
    for n in [8, 10, 12]:
        for seed in range(4):
            for family in ["euclidean-ceil", "clustered-euclidean-ceil", "random-shortest-path", "tree-metric"]:
                rng = random.Random(10000 * n + 100 * seed + {
                    "euclidean-ceil": 1, "clustered-euclidean-ceil": 2,
                    "random-shortest-path": 3, "tree-metric": 4}[family])
                if "euclidean" in family:
                    points = [(rng.randrange(101), rng.randrange(101)) for _ in range(n)]
                    if family.startswith("clustered"):
                        points = [(x + 300 * (i % 3), y) for i, (x, y) in enumerate(points)]
                    def distance(a, b):
                        d = sum((x - y) ** 2 for x, y in zip(points[a], points[b]))
                        q = isqrt(d)
                        return q + (q * q != d)
                    c = matrix(n, distance)
                elif family == "random-shortest-path":
                    c = matrix(n, lambda a, b: rng.randrange(1, 101))
                else:
                    c = matrix(n, lambda a, b: 10 ** 9)
                    for v in range(1, n):
                        parent = rng.randrange(v)
                        c[v][parent] = c[parent][v] = rng.randrange(1, 31)
                if family in ["random-shortest-path", "tree-metric"]:
                    for k in range(n):
                        for a in range(n):
                            for b in range(n):
                                c[a][b] = min(c[a][b], c[a][k] + c[k][b])
                result.append({"id": f"{family}-n{n}-s{seed}", "family": family, "seed": seed,
                               "costs": c})
    result.append(petersen_instance())
    return result


def enumerate_tours(c):
    """Exhaustive independent reference, identifying reversals."""
    for tail in permutations(range(1, len(c))):
        if tail[0] < tail[-1]:
            tour = (0,) + tail
            yield tour, cost(c, tour)
