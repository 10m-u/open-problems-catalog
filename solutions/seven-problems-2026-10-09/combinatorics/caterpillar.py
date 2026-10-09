#!/usr/bin/env python3
"""Exact 16-state characterization for Q256; Python standard library only.

The input is the pendant-leaf count at each vertex of the non-leaf spine.
A one-vertex spine requires at least two leaves; longer spines require at
least one leaf at each end.  The algorithm returns a minimum proper total
dominating set or None.  Labels 0,...,k-1 denote spine vertices; successive
blocks of labels, beginning at k, denote pendant leaves.
"""
from dataclasses import asdict, dataclass
from itertools import product
import argparse
import json


@dataclass(frozen=True)
class Solution:
    minimum: int
    spine_membership: tuple
    selected_leaf_counts: tuple
    spine_neighbor_sums: tuple
    vertices: tuple


def validate_leaf_word(leaves):
    if not leaves or any(type(t) is not int or t < 0 for t in leaves):
        raise ValueError('The leaf word must be a nonempty sequence of nonnegative integers.')
    if len(leaves) == 1:
        if leaves[0] < 2:
            raise ValueError('A one-vertex non-leaf spine must have at least two leaves.')
    elif leaves[0] < 1 or leaves[-1] < 1:
        raise ValueError('Each endpoint of a nontrivial non-leaf spine must have a leaf.')


def local(leaf_count, left, center, right, neighbor_sum):
    """The local predicate in Theorem 2 of Q0256-caterpillars.md."""
    if not 1 <= neighbor_sum <= 4:
        return False
    y = neighbor_sum - left - right
    if leaf_count == 0:
        return y == 0
    return center == 1 and neighbor_sum >= 2 and 0 <= y <= min(leaf_count, 3)


def solve(leaves):
    """Return an optimal witness, or None when no proper total set exists."""
    leaves = tuple(leaves)
    validate_leaf_word(leaves)
    k = len(leaves)
    # State (a,b,q) after i records (x_i,x_{i+1},sigma_i).
    layers = []
    costs = {}
    first = {}
    for a, b, q in product(range(2), range(2), range(1, 5)):
        if local(leaves[0], 0, a, b, q):
            state = (a, b, q)
            costs[state] = a + q - b
            first[state] = None
    layers.append(first)
    for i in range(1, k):
        next_costs, previous = {}, {}
        for (a, b, q), cost in costs.items():
            for d, r in product(range(2), range(1, 5)):
                if q != r and local(leaves[i], a, b, d, r):
                    state = (b, d, r)
                    proposal = cost + b + r - a - d
                    if state not in next_costs or proposal < next_costs[state]:
                        next_costs[state] = proposal
                        previous[state] = (a, b, q)
        costs = next_costs
        layers.append(previous)
    accepted = [(cost, state) for state, cost in costs.items() if state[1] == 0]
    if not accepted:
        return None
    minimum, state = min(accepted)
    states = []
    for i in range(k - 1, -1, -1):
        states.append(state)
        state = layers[i][state]
    states.reverse()
    x = tuple(st[0] for st in states)
    q = tuple(st[2] for st in states)
    y = tuple(q[i] - (x[i - 1] if i else 0) - (x[i + 1] if i + 1 < k else 0)
              for i in range(k))
    chosen = [i for i, value in enumerate(x) if value]
    start = k
    for available, selected in zip(leaves, y):
        chosen.extend(range(start, start + selected))
        start += available
    assert len(chosen) == minimum
    return Solution(minimum, x, y, q, tuple(chosen))


def adjacency(leaves):
    validate_leaf_word(leaves)
    k = len(leaves)
    adj = [[] for _ in range(k + sum(leaves))]
    for i in range(k - 1):
        adj[i].append(i + 1)
        adj[i + 1].append(i)
    nxt = k
    for i, count in enumerate(leaves):
        for leaf in range(nxt, nxt + count):
            adj[i].append(leaf)
            adj[leaf].append(i)
        nxt += count
    return adj


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('leaf_counts', type=int, nargs='+')
    args = parser.parse_args()
    try:
        result = solve(args.leaf_counts)
    except ValueError as exc:
        parser.error(str(exc))
    print(json.dumps(None if result is None else asdict(result), indent=2))
