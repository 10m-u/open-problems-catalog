#!/usr/bin/env python3
"""Independent exact subset controls for Q256 and Q257 (standard library only).

Run from any directory.  The default exhausts every unlabeled tree of orders
2 through 13; --max-n can change the finite verification boundary.
The mathematical proofs do not rely on these finite checks.
"""
import argparse
import json
from pathlib import Path
from itertools import product

from caterpillar import adjacency as caterpillar_adjacency, solve
from tree_enumeration import rooted_shapes, adjacency, canonical, exact_parameters


def leaf_word(adj):
    core = [v for v in range(len(adj)) if len(adj[v]) > 1]
    if not core:
        return None
    core_set = set(core)
    neighbors = {v: [u for u in adj[v] if u in core_set] for v in core}
    if any(len(ns) > 2 for ns in neighbors.values()):
        return None
    start = min((v for v in core if len(neighbors[v]) <= 1), default=core[0])
    order = []
    prev, v = -1, start
    while True:
        order.append(v)
        fresh = [u for u in neighbors[v] if u != prev]
        if not fresh:
            break
        prev, v = v, fresh[0]
    assert len(order) == len(core)
    return tuple(sum(len(adj[u]) == 1 for u in adj[v]) for v in order)


def general_leaf_kernel(adj):
    """Delete leaves beyond deg_H(v)+2, where H is the non-leaf core."""
    core = {v for v in range(len(adj)) if len(adj[v]) > 1}
    keep = set(core)
    for v in sorted(core):
        d = sum(u in core for u in adj[v])
        keep.update(sorted(u for u in adj[v] if u not in core)[:d + 2])
    order = sorted(keep)
    labels = {v: i for i, v in enumerate(order)}
    return [[labels[u] for u in adj[v] if u in keep] for v in order]


def check_witness(leaves, result):
    adj = caterpillar_adjacency(leaves)
    selected = set(result.vertices)
    sigma = [sum(u in selected for u in ns) for ns in adj]
    assert len(selected) == result.minimum
    assert all(sigma)
    assert all(sigma[v] != sigma[u] for v in range(len(adj)) for u in adj[v])
    assert tuple(sigma[:len(leaves)]) == result.spine_neighbor_sums


def verify(max_n):
    shapes, by_size = rooted_shapes(max_n)
    counts, pairs = {}, {}
    caterpillars = 0
    feasible = 0
    kernel_reductions = 0
    for n in range(2, max_n + 1):
        seen = set()
        n_feasible = 0
        for rid in by_size[n]:
            adj = adjacency(rid, shapes)
            key = canonical(adj)
            if key in seen:
                continue
            seen.add(key)
            a, b, aw, bw = exact_parameters(adj)
            if n >= 3:
                core_size = sum(len(ns) > 1 for ns in adj)
                assert core_size <= 2 * a - 2
                small = general_leaf_kernel(adj)
                assert len(small) <= 6 * a - 4
                if len(small) < n:
                    kernel_reductions += 1
                    ka, kb, _, _ = exact_parameters(small)
                    assert (ka, kb) == (a, b)
            leaves = leaf_word(adj)
            if leaves is not None:
                caterpillars += 1
                result = solve(leaves)
                assert (None if result is None else result.minimum) == b, (leaves, a, b, result)
                capped = tuple(min(t, 3) for t in leaves)
                capped_result = solve(capped)
                assert (None if capped_result is None else capped_result.minimum) == b
                if result is not None:
                    check_witness(leaves, result)
            if b is None:
                continue
            feasible += 1
            n_feasible += 1
            assert a + 1 <= b <= 6 * a - 4
            if a == 2:
                assert b in (3, 5)
            if a == 3:
                assert b in (6, 7)
            if (a, b) not in pairs:
                pairs[a, b] = {'n': n, 'adjacency': adj,
                               'total_witness': [v for v in range(n) if (aw >> v) & 1],
                               'proper_witness': [v for v in range(n) if (bw >> v) & 1]}
        counts[n] = {'trees': len(seen), 'proper_total_feasible': n_feasible}
        print(f'n={n}: {len(seen)} unlabeled trees checked', flush=True)

    # Exhaust every short leaf word with capacities above the proved cutoff.
    # These are separate from the unlabeled-tree pass and directly stress the cap.
    short_words = 0
    for k in range(1, 5):
        for leaves in product(range(6), repeat=k):
            if (k == 1 and leaves[0] < 2) or (k > 1 and (leaves[0] == 0 or leaves[-1] == 0)):
                continue
            if k + sum(leaves) > 14:
                continue
            adj = caterpillar_adjacency(leaves)
            _, b, _, _ = exact_parameters(adj)
            result = solve(leaves)
            assert (None if result is None else result.minimum) == b
            short_words += 1
    sharp_leaf = solve((3, 0, 0, 1))
    assert sharp_leaf.minimum == 7 and 3 in sharp_leaf.selected_leaf_counts
    assert solve((2, 0, 0, 1)) is None
    sharp_sum = solve((1, 1, 2, 1))
    assert sharp_sum.minimum == 9 and 4 in sharp_sum.spine_neighbor_sums

    # Large multiplicities affect label arithmetic but not the finite state set.
    large_word = tuple(100_000 + i for i in range(200))
    large = solve(large_word)
    capped_large = solve((3,) * len(large_word))
    assert large.minimum == capped_large.minimum
    assert len(large.vertices) == large.minimum

    # The complete a=2 and a=3 slices must all have explicit witnesses.
    assert {(2, 3), (2, 5), (3, 6), (3, 7)} <= set(pairs)
    output = {
        'status': 'passed', 'maximum_tree_order': max_n,
        'tree_count': sum(d['trees'] for d in counts.values()),
        'proper_total_feasible_trees': feasible,
        'caterpillars_checked': caterpillars,
        'leaf_kernel_reductions_checked': kernel_reductions,
        'additional_short_leaf_words_checked': short_words,
        'counts_by_order': counts,
        'large_multiplicity_check': {'spine_length': len(large_word),
                                     'full_tree_order': len(large_word) + sum(large_word),
                                     'minimum': large.minimum},
        'sharpness_examples': {
            'leaf_cap_three': {'leaf_word': [3, 0, 0, 1], 'minimum': 7,
                               'cap_two_feasible': False},
            'neighbor_sum_four': {'leaf_word': [1, 1, 2, 1], 'minimum': 9}},
        'observed_pairs': [{'a': a, 'b': b, **data} for (a, b), data in sorted(pairs.items())],
        'scope': 'Exhaustive finite controls; not a proof of assertions at unbounded order.'
    }
    Path(__file__).with_name('verification.json').write_text(json.dumps(output, indent=2) + '\n')
    print(json.dumps({k: v for k, v in output.items() if k not in ('observed_pairs', 'counts_by_order')}, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--max-n', type=int, default=13)
    args = parser.parse_args()
    if args.max_n < 7:
        parser.error('--max-n must be at least 7 to include all slice witnesses.')
    verify(args.max_n)
