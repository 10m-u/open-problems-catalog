#!/usr/bin/env python3
"""Exact checks of the strict recursive-tree NN obstruction, at bounded sizes."""
from fractions import Fraction
import json
from pathlib import Path


def family(k, epsilon):
    adjacency = []

    def vertex():
        adjacency.append([])
        return len(adjacency) - 1

    def edge(a, b, w):
        adjacency[a].append((b, w))
        adjacency[b].append((a, w))

    def build(j):
        if j == 0:
            v = vertex()
            return v, v, v, [v]
        left_l, left_r, _, left_order = build(j - 1)
        right_l, right_r, _, right_order = build(j - 1)
        middle = vertex()
        edge(left_r, right_l, Fraction(j))
        edge(right_l, middle, 1 + epsilon * j)
        return left_l, right_r, middle, left_order + right_order + [middle]

    left, right, middle, order = build(k)
    return adjacency, left, right, middle, order


def distances(adjacency):
    n = len(adjacency)
    out = []
    for root in range(n):
        row = [None] * n
        row[root] = Fraction(0)
        todo = [(root, -1)]
        while todo:
            u, parent = todo.pop()
            for v, w in adjacency[u]:
                if v == parent:
                    continue
                assert row[v] is None, "not a tree"
                row[v] = row[u] + w
                todo.append((v, u))
        assert all(x is not None for x in row)
        out.append(row)
    return out


def main():
    receipts = []
    comparisons = 0
    for k in range(1, 9):
        eps = Fraction(1, 4 * k)
        a, left, right, middle, order = family(k, eps)
        d = distances(a)
        n = len(a)
        assert n == 2 ** (k + 1) - 1
        assert len(set(order)) == n and order[0] == left and order[-1] == middle
        margins = []
        open_cost = Fraction(0)
        for i, (u, v) in enumerate(zip(order, order[1:])):
            selected = d[u][v]
            open_cost += selected
            for other in order[i + 2:]:
                comparisons += 1
                margin = d[u][other] - selected
                assert margin > 0, (k, i, u, v, other, margin)
                margins.append(margin)
        weight = sum(w for u, row in enumerate(a) for v, w in row if u < v)
        leaf_increment = eps * (2 ** (k + 1) - k - 2)
        expected_weight = 3 * 2 ** k - k - 3 + leaf_increment
        expected_nn = (k + 2) * 2 ** k - 2 + 2 * leaf_increment
        nn = open_cost + d[middle][left]
        assert weight == expected_weight
        assert nn == expected_nn
        assert d[left][right] == 2 ** (k + 1) - k - 2
        min_margin = min(margins)
        delta = min_margin / (4 * (n - 1))
        # This radius guarantees all comparisons remain strict throughout
        # the full product box: each path has at most n-1 edges.
        assert 2 * (n - 1) * delta < min_margin
        assert delta < min(w for row in a for _, w in row)
        receipts.append({
            "k": k, "vertices": n, "epsilon": str(eps),
            "weight": str(weight), "nn": str(nn), "opt": str(2 * weight),
            "ratio": str(nn / (2 * weight)),
            "smallest_strict_margin": str(min_margin),
            "positive_open_box_radius": str(delta),
        })
    result = {
        "status": "passed", "arithmetic": "exact rational",
        "families": len(receipts), "strict_nn_comparisons": comparisons,
        "maximum_vertices": max(r["vertices"] for r in receipts),
        "scope": "finite checks of the stated recursive formulas and strict NN order; not an expected-ratio counterexample",
        "receipts": receipts,
    }
    Path(__file__).with_name("MST-ENVELOPE-CHECK-RESULTS.json").write_text(
        json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "receipts"}, indent=2))


if __name__ == "__main__":
    main()
