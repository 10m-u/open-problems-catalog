#!/usr/bin/env python3
"""Exact controls for proposed Haar and 1D clustering proof routes."""
from collections import deque
from fractions import Fraction as F
from itertools import combinations
from math import gcd
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


def haar_components(m, offsets):
    adjacency = [set() for _ in range(2*m)]
    for i in range(m):
        for s in offsets:
            j = m + (i+s) % m
            adjacency[i].add(j)
            adjacency[j].add(i)
    unseen = set(range(2*m))
    components = []
    while unseen:
        queue = [unseen.pop()]
        component = []
        while queue:
            v = queue.pop()
            component.append(v)
            for u in adjacency[v] & unseen:
                unseen.remove(u)
                queue.append(u)
        components.append(len(component))
    return sorted(components)


POINTS = tuple(map(F, ['-6', '0', '.001', '.002', '.003', '.004', '1.6']))


def groups(mask):
    return ([i for i in range(7) if mask >> i & 1],
            [i for i in range(7) if not mask >> i & 1])


def mean(indices):
    return sum((POINTS[i] for i in indices), F()) / len(indices)


def sse(mask):
    return sum((sum((POINTS[i] - mean(g))**2 for i in g)
                for g in groups(mask)), F())


def inversions(mask):
    left, right = groups(mask)
    if mean(left) > mean(right):
        left, right = right, left
    return sum(POINTS[a] > POINTS[b] for a in left for b in right)


def improving(mask):
    result = []
    for i in range(7):
        nxt = mask ^ (1 << i)
        if nxt not in (0, 127) and sse(nxt) < sse(mask):
            result.append((i, nxt))
    return result


def main():
    haar = []
    for p,q,r in [(3,5,7), (3,5,11), (3,7,11), (5,7,11)]:
        m = p*q*r
        offsets = [0,p*q,p*r,q*r]
        collective = m
        pairs = []
        assert haar_components(m, offsets) == [2*m]
        for a,b in combinations(offsets, 2):
            g = gcd(m, b-a)
            collective = gcd(collective, b-a)
            comp = haar_components(m, [a,b])
            assert g > 1 and comp == [2*m//g]*g
            pairs.append({'offsets':[a,b], 'gcd':g,
                          'components':len(comp), 'cycle_length':2*m//g})
        assert collective == 1
        haar.append({'m':m, 'offsets':offsets, 'connected':True, 'pairs':pairs})
    initial = 63
    moves = improving(initial)
    assert moves == [(0, 62)]
    assert inversions(initial) == 0 and inversions(62) == 5
    queue = deque([(initial, [])])
    seen = {initial}
    path = None
    while queue:
        state, history = queue.popleft()
        successors = improving(state)
        if not successors:
            path = history
            final = state
            break
        for i,nxt in successors:
            if nxt not in seen:
                seen.add(nxt)
                queue.append((nxt, history + [str(POINTS[i])]))
    assert path is not None and len(path) == 2
    graph_edges = 0
    for mask in range(1,127):
        before = sse(mask)
        for i,nxt in improving(mask):
            assert sse(nxt) < before
            graph_edges += 1
    receipt = {
        'status':'passed', 'haar':haar,
        'clustering':{
            'points':list(map(str,POINTS)), 'initial_sse':str(sse(initial)),
            'initial_centroids':list(map(lambda g:str(mean(g)), groups(initial))),
            'transfer_deltas':{str(POINTS[i]): str(sse(initial ^ (1<<i))-sse(initial))
                              for i in range(6)},
            'only_initial_improving_transfer':'-6',
            'initial_inversions':0, 'next_inversions':5,
            'next_centroids':list(map(lambda g:str(mean(g)), groups(62))),
            'shortest_improving_path':path, 'path_length':len(path),
            'final_sse':str(sse(final)),
            'all_nonempty_labeled_partitions':126,
            'strict_improvement_arcs':graph_edges},
        'scope':'Obstructions to proposed proof routes; neither catalog question is refuted.'}
    (HERE/'INITIAL-ROUTE-CHECK-RESULTS.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({'status':'passed','connected_haar_examples':len(haar),
                      'pair_unions':24,'only_initial_transfer':'-6',
                      'shortest_clustering_path_length':len(path)}))


if __name__ == '__main__':
    main()
