#!/usr/bin/env python3
"""Exact certificates for catalog Q3840/Q3841, restricted to circumference 5.

Python 3 standard library only. No solver, floating point, input data, or network.
The search enumerates every 5-bit row triple, then every compatible transition.
An independent graph-neighborhood check validates each constructive witness.
"""
from itertools import product
import json


CYLINDER_SEEDS = {
    3: ('11010', '10111', '11010'),
    5: ('11010', '01110', '01010', '01001', '10111'),
    7: ('11100', '11010', '10010', '11011', '10010', '01010', '11101'),
    10: ('10111', '01010', '01111', '10111', '01001', '11100',
         '10101', '11011', '10010', '11101'),
    12: ('11100', '11010', '10010', '11011', '10010', '11010',
         '11100', '01010', '10111', '11011', '01001', '10111'),
}
TORUS_SEEDS = {
    7: ('01010', '10111', '11011', '01001', '10111', '11000', '11100'),
    9: ('01111', '11110', '10100', '01111', '01100', '01011',
        '11010', '11000', '10010'),
    11: ('10010', '11011', '11101', '01010', '00111', '01101',
         '11110', '10100', '01111', '10000', '11101'),
    13: ('11011', '10010', '01010', '11001', '01000', '10111',
         '01001', '11011', '10111', '01010', '11100', '11010', '10010'),
}
C = '10010'
D = '11011'


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def row_vector(a, b, c):
    """Neighbor sums of middle row b; the row coordinate is cyclic."""
    n = len(b)
    return tuple(b[(i - 1) % n] + b[(i + 1) % n] + a[i] + c[i]
                 for i in range(n))


def good_row(sums):
    return all(sums[i] > 0 and sums[i] != sums[(i + 1) % len(sums)]
               for i in range(len(sums)))


def graph_check(rows, cyclic):
    """Use actual sets of neighbors, independent of transfer-state code."""
    n, m = len(rows[0]), len(rows)
    require(n >= 3 and (not cyclic or m >= 3), 'invalid graph dimensions')
    require(all(len(row) == n and set(row) <= {'0', '1'} for row in rows),
            'invalid membership rows')
    selected = {(j, i) for j in range(m) for i in range(n) if rows[j][i] == '1'}
    neighbors = {}
    for j, i in product(range(m), range(n)):
        adjacent = {(j, (i - 1) % n), (j, (i + 1) % n)}
        if cyclic:
            adjacent |= {((j - 1) % m, i), ((j + 1) % m, i)}
        else:
            if j > 0:
                adjacent.add((j - 1, i))
            if j + 1 < m:
                adjacent.add((j + 1, i))
        neighbors[j, i] = adjacent
    sums = {u: len(adjacent & selected) for u, adjacent in neighbors.items()}
    require(all(value > 0 for value in sums.values()), 'a vertex is not dominated')
    require(all(sums[u] != sums[v] for u, adjacent in neighbors.items() for v in adjacent),
            'adjacent vertices have equal neighbor sums')
    return len(selected)


def transfer_graph(n=5):
    """Return every valid triple (a,b,c), its sum vector, and all legal arcs."""
    masks = tuple(tuple((mask >> i) & 1 for i in range(n)) for mask in range(1 << n))
    states, sums, by_first_pair = [], [], {}
    for a, b, c in product(range(1 << n), repeat=3):
        s = row_vector(masks[a], masks[b], masks[c])
        if good_row(s):
            u = len(states)
            states.append((a, b, c))
            sums.append(s)
            by_first_pair.setdefault((a, b), []).append(u)
    edges = [[] for _ in states]
    for u, (_, b, c) in enumerate(states):
        for v in by_first_pair.get((b, c), ()):
            if all(x != y for x, y in zip(sums[u], sums[v])):
                edges[u].append(v)
    return states, sums, edges


def cylinder_certificate(states, edges):
    start = {u for u, (a, _, _) in enumerate(states) if a == 0}
    finish = {u for u, (_, _, c) in enumerate(states) if c == 0}
    active = start
    rows = []
    snapshots = {}
    expected = [0, 0, 10, 0, 20, 0, 50, 0, 50, 20, 50, 50, 50, 50, 50, 50]
    for m in range(1, 17):
        accepted = len(active & finish)
        require(accepted == expected[m - 1], 'unexpected cylinder reachability')
        rows.append({'m': m, 'reachable_states': len(active), 'accepting_states': accepted})
        if m in (15, 16):
            snapshots[m] = active
        active = {v for u in active for v in edges[u]}
    require(snapshots[15] == snapshots[16], 'reachability did not stabilize')
    return rows


def torus_certificate(states, edges):
    """Count states admitting a closed walk of length k, for k <= 5.

    A closed walk need not be a simple directed cycle. Repeated states and arcs
    are deliberately allowed, as required for periodic membership patterns.
    """
    counts = [0] * 6
    for source in range(len(states)):
        active = {source}
        for length in range(1, 6):
            active = {v for u in active for v in edges[u]}
            counts[length] += source in active
    require(counts[3] == counts[5] == 0, 'unexpected small odd torus witness')
    return {str(k): counts[k] for k in range(1, 6)}


def insert_pairs(rows, at, repetitions):
    require(repetitions >= 0, 'negative insertion count')
    return rows[:at + 1] + (C, D) * repetitions + rows[at + 1:]


def constructive_certificate():
    witness_sizes = {'cylinder': {}, 'torus': {}}
    for cyclic, seeds, label in ((False, CYLINDER_SEEDS, 'cylinder'),
                                 (True, TORUS_SEEDS, 'torus')):
        for m, rows in seeds.items():
            require(len(rows) == m, 'wrong seed length')
            witness_sizes[label][str(m)] = graph_check(rows, cyclic)
    c, d = tuple(map(int, C)), tuple(map(int, D))
    at_c, at_d = row_vector(d, c, d), row_vector(c, d, c)
    require(at_c == (2, 3, 1, 2, 4) and at_d == (4, 1, 2, 3, 2),
            'incorrect insertion vectors')
    require(good_row(at_c) and good_row(at_d), 'insertion row violates local condition')
    require(all(x != y for x, y in zip(at_c, at_d)), 'insertion edge violates condition')
    checked_insertions = 0
    for cyclic, base, at in ((False, CYLINDER_SEEDS[7], 3),
                             (False, CYLINDER_SEEDS[12], 3),
                             (True, TORUS_SEEDS[13], 0)):
        require(base[at] == D and base[(at - 1) % len(base)] == C
                and base[at + 1] == C, 'base lacks the insertion triple')
        for repetitions in (0, 1, 2, 20):
            graph_check(insert_pairs(base, at, repetitions), cyclic)
            checked_insertions += 1
    # Concrete sanity checks for the covering lemma; its proof covers all factors.
    for cyclic, base in ((False, CYLINDER_SEEDS[10]), (True, TORUS_SEEDS[7])):
        for factor in (3, 5):
            graph_check(tuple(row * factor for row in base), cyclic)
    return {'seed_sizes': witness_sizes, 'checked_insertions': checked_insertions,
            'insertion_sum_at_C': at_c, 'insertion_sum_at_D': at_d}


def main():
    constructive = constructive_certificate()
    states, _, edges = transfer_graph()
    require(len(states) == 4310, 'unexpected number of transfer states')
    require(sum(map(len, edges)) == 10800, 'unexpected number of transfer arcs')
    print(json.dumps({
        'scope': 'Q3840/Q3841: circumference 5 classifications and covering families; general problems remain unresolved',
        'arithmetic': 'exact integers; Python standard library only',
        'transfer_states': len(states),
        'transfer_arcs': sum(map(len, edges)),
        'cylinder_reachability': cylinder_certificate(states, edges),
        'torus_closed_walk_start_counts': torus_certificate(states, edges),
        'constructive_certificates': constructive,
    }, indent=2))


if __name__ == '__main__':
    main()
