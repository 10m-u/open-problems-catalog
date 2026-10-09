#!/usr/bin/env python3
"""Finite controls for the graph-testing proofs; Python standard library only.

Enumerate all interval menus cheaper than the proposed nonadaptive optima
through n=6; compute exact adaptive one-defect costs through n=8; check all
binary targets through n=7. The proofs, not these bounds, establish all n.
Run from any directory; pass --write to save the checked results alongside it.
"""
import argparse
from functools import lru_cache
from itertools import combinations
import json
from pathlib import Path


def intervals(n):
    return [(left, right) for left in range(1, n + 1)
            for right in range(left, n + 1)]


def reading(pool, defects):
    left, right = pool
    return int(any(left <= v <= right for v in defects))


def signature(menu, defects):
    return tuple(reading(pool, defects) for pool in menu)


def separating_bits(pool, worlds, labels):
    outcomes = [reading(pool, w) for w in worlds]
    return sum(1 << i for i, (a, b) in enumerate(
        (a, b) for a in range(len(worlds)) for b in range(a + 1, len(worlds))
        if labels[a] != labels[b]) if outcomes[a] != outcomes[b])


def certify_optimum(n, worlds, labels, construction):
    """Reject EVERY cheaper menu, then directly check the proposed menu."""
    pair_count = sum(labels[a] != labels[b] for a in range(len(worlds))
                     for b in range(a + 1, len(worlds)))
    required = (1 << pair_count) - 1
    covers = [separating_bits(pool, worlds, labels) for pool in intervals(n)]
    cheaper_menus = 0
    for k in range(len(construction)):
        for chosen in combinations(covers, k):
            covered = 0
            for bits in chosen:
                covered |= bits
            assert covered != required, (n, k, construction)
            cheaper_menus += 1
    joint = {}
    for world, label in zip(worlds, labels):
        code = signature(construction, world)
        assert code not in joint or joint[code] == label
        joint[code] = label
    return cheaper_menus


def adaptive_cost(n, include_empty):
    worlds = [(v,) for v in range(1, n + 1)]
    if include_empty:
        worlds.append(())
    tests = [sum(reading(pool, w) << i for i, w in enumerate(worlds))
             for pool in intervals(n)]

    @lru_cache(None)
    def cost(states):
        if states.bit_count() <= 1:
            return 0
        choices = []
        for test in tests:
            yes = states & test
            no = states ^ yes
            if yes and no:
                choices.append(1 + max(cost(yes), cost(no)))
        assert choices
        return min(choices)

    return cost((1 << len(worlds)) - 1)


def run():
    recovery = []
    for n in range(1, 7):
        one = [(v,) for v in range(1, n + 1)]
        m = 0 if n == 1 else (n + 1) // 2
        exact_menu = [(j, j + m - 1) for j in range(1, m + 1)]
        exact_checked = certify_optimum(n, one, list(range(n)), exact_menu)
        at_most = [()] + one
        m0 = (n + 2) // 2
        at_most_menu = [(j, min(j + m0 - 1, n)) for j in range(1, m0 + 1)]
        at_most_checked = certify_optimum(n, at_most, list(range(n + 1)), at_most_menu)
        two = [tuple(c) for k in range(min(2, n) + 1)
               for c in combinations(range(1, n + 1), k)]
        singleton_menu = [(v, v) for v in range(1, n + 1)]
        two_checked = certify_optimum(n, two, list(range(len(two))), singleton_menu)
        recovery.append({"n": n, "exactly_one": m, "at_most_one": m0,
                         "at_most_two": n,
                         "all_cheaper_menus_rejected": {
                             "exactly_one": exact_checked, "at_most_one": at_most_checked,
                             "at_most_two": two_checked},
                         "attaining_menus": {"exactly_one": exact_menu,
                                             "at_most_one": at_most_menu,
                                             "at_most_two": singleton_menu}})
    adaptive = []
    for n in range(1, 9):
        exact, at_most = adaptive_cost(n, False), adaptive_cost(n, True)
        assert exact == (n - 1).bit_length()
        assert at_most == n.bit_length()
        adaptive.append({"n": n, "exactly_one": exact, "at_most_one": at_most})
    binary = []
    target_count = 0
    for n in range(1, 8):
        checked = 0
        for pattern in range(1 << n):
            labels = [(pattern >> v) & 1 for v in range(n)]
            runs = []
            left = 1
            for v in range(2, n + 1):
                if labels[v - 1] != labels[v - 2]:
                    runs.append((left, v - 1, labels[v - 2]))
                    left = v
            runs.append((left, n, labels[-1]))
            selected_label = 1 - runs[0][2] if len(runs) % 2 else 0
            menu = [(a, b) for a, b, label in runs if label == selected_label]
            assert len(menu) == len(runs) // 2
            checked += certify_optimum(n, [(v,) for v in range(1, n + 1)], labels, menu)
            target_count += 1
        binary.append({"n": n, "labelings_checked": 1 << n,
                       "all_cheaper_menus_rejected": checked})
    # Controls on the connected-pool masking lemma: all simple graphs <=4 nodes.
    masking = {"graphs": 0, "low_degree_vertex_checks": 0}
    for n in range(1, 5):
        edges = list(combinations(range(n), 2))
        for edge_mask in range(1 << len(edges)):
            adj = [set() for _ in range(n)]
            for i, (a, b) in enumerate(edges):
                if edge_mask >> i & 1:
                    adj[a].add(b); adj[b].add(a)
            connected = []
            for pool_mask in range(1, 1 << n):
                pool = {v for v in range(n) if pool_mask >> v & 1}
                reached = {min(pool)}
                while True:
                    expanded = reached | {u for v in reached for u in adj[v] if u in pool}
                    if expanded == reached:
                        break
                    reached = expanded
                if reached == pool:
                    connected.append(pool)
            for d in range(1, n + 1):
                for v in range(n):
                    if len(adj[v]) <= d - 1:
                        for pool in connected:
                            separates = bool(pool & adj[v]) != bool(pool & (adj[v] | {v}))
                            assert separates == (pool == {v})
                        masking["low_degree_vertex_checks"] += 1
            masking["graphs"] += 1
    return {"checked_on": "2026-09-30", "statement_id": "a89c4a7fea1f6a2b1d26",
            "nonadaptive_recovery": recovery, "adaptive_recovery": adaptive,
            "binary_targets": binary, "total_binary_targets": target_count,
            "connected_pool_masking": masking, "scope": "finite controls; see hand proofs for all sizes"}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = run()
    if args.write:
        Path(__file__).with_name("graph-testing-checks.json").write_text(
            json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print("PASS: all cheaper interval menus rejected through n=6; "
          "adaptive optima through n=8; 254 binary targets through n=7; "
          "connected-pool masking on 75 graphs.")
