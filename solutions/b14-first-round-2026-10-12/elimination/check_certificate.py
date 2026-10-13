"""Standalone certificate checker; independent forced-edge Kruskal calculation."""
import argparse
import json
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def edge(a, b):
    return min(a, b), max(a, b)


def kruskal(w, vertices, forced=None):
    parent = {v: v for v in vertices}
    def find(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v
    total, count = 0, 0
    pairs = []
    if forced is not None:
        a, b = forced
        require(a in parent and b in parent and a != b, "invalid forced tree edge")
        parent[find(a)] = find(b)
        total, count = w[a][b], 1
    for a in vertices:
        for b in vertices:
            if a < b:
                pairs.append((w[a][b], a, b))
    for value, a, b in sorted(pairs):
        if find(a) != find(b):
            parent[find(a)] = find(b)
            total += value
            count += 1
    require(count == len(vertices) - 1, "tree disconnected")
    return total


def verify(data):
    require(data["schema"] == "b14-one-tree-certificate-v1", "wrong schema")
    c = data["instance"]["costs"]
    n = len(c)
    require(n >= 3 and all(len(row) == n for row in c), "wrong matrix size")
    require(all(type(c[a][b]) is int and c[a][b] >= 0 and c[a][b] == c[b][a]
                for a in range(n) for b in range(n)), "costs must be symmetric nonnegative integers")
    require(all(c[a][a] == 0 for a in range(n)), "nonzero diagonal")
    tour = data["incumbent"]["tour"]
    require(sorted(tour) == list(range(n)), "incumbent is not a tour")
    upper = sum(c[tour[i]][tour[(i + 1) % n]] for i in range(n))
    require(upper == data["incumbent"]["cost"], "incumbent cost wrong")
    checked = []
    for cert in data["certificates"]:
        r, p, scale = cert["root"], cert["potentials"], cert["scale"]
        require(type(r) is int and 0 <= r < n, "invalid root")
        require(type(scale) is int and scale > 0 and len(p) == n
                and all(type(x) is int for x in p), "invalid exact potentials")
        w = [[scale * c[a][b] + p[a] + p[b] for b in range(n)] for a in range(n)]
        vertices = [v for v in range(n) if v != r]
        tree = [tuple(e) for e in cert["tree_edges"]]
        require(len(tree) == n - 2 and len(set(tree)) == len(tree)
                and all(0 <= a < b < n and r not in (a, b) for a, b in tree),
                "invalid tree edges")
        # Independently verify connectedness, then compare with a separate optimizer.
        reachable = {vertices[0]}
        for _ in range(n):
            for a, b in tree:
                if a in reachable or b in reachable:
                    reachable.update((a, b))
        require(reachable == set(vertices), "certificate tree disconnected")
        minimum = kruskal(w, vertices)
        require(sum(w[a][b] for a, b in tree) == minimum, "certificate tree is not minimum")
        root_edges = [tuple(e) for e in cert["root_edges"]]
        require(len(root_edges) == 2 and len(set(root_edges)) == 2
                and all(0 <= a < b < n and r in (a, b) for a, b in root_edges),
                "invalid root edges")
        spokes = sorted(w[r][v] for v in vertices)
        root_value = sum(spokes[:2])
        require(sum(w[a][b] for a, b in root_edges) == root_value, "root pair is not minimum")
        base = minimum + root_value - 2 * sum(p)
        require(base == cert["bound_numerator"], "wrong certificate lower bound")
        require(base <= upper * scale, "bound exceeds a feasible tour")
        checked.append((r, p, scale, w, vertices, base))
    all_edges = {(a, b) for a in range(n) for b in range(a + 1, n)}
    expected_removed, seen = set(), set()
    for row in data["forced_bounds"]:
        a, b = tuple(row["edge"])
        require((a, b) in all_edges and (a, b) not in seen, "invalid/duplicate bound edge")
        seen.add((a, b))
        r, p, scale, w, vertices, _ = checked[row["certificate"]]
        require(row["scale"] == scale, "bound scale mismatch")
        if r in (a, b):
            other = a if b == r else b
            value = kruskal(w, vertices) + w[r][other] + min(
                w[r][v] for v in vertices if v != other) - 2 * sum(p)
        else:
            value = kruskal(w, vertices, (a, b)) + sum(
                sorted(w[r][v] for v in vertices)[:2]) - 2 * sum(p)
        require(value == row["numerator"], "wrong forced-edge lower bound")
        if value > upper * scale:
            expected_removed.add((a, b))
    require(seen == all_edges, "missing bound edges")
    require({tuple(e) for e in data["eliminated_edges"]} == expected_removed,
            "wrong elimination list")
    require({tuple(e) for e in data["residual_edges"]} == all_edges - expected_removed,
            "wrong residual graph")
    require(all(edge(tour[i], tour[(i + 1) % n]) not in expected_removed for i in range(n)),
            "incumbent was eliminated")
    gl = data["global_lower_bound"]
    cert = data["certificates"][gl["certificate"]]
    require(gl["numerator"] == cert["bound_numerator"] and gl["scale"] == cert["scale"],
            "wrong global bound")
    return {"instance": data["instance"]["id"], "method": data["method"],
            "certificates_checked": len(checked), "forced_bounds_checked": len(seen),
            "edges_eliminated": len(expected_removed)}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    args = parser.parse_args()
    print(json.dumps(verify(json.loads(args.certificate.read_text())), indent=2))
