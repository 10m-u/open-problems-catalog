#!/usr/bin/env python3
"""Exhaustive improving-response analysis for variety- and diversity-seeking jump games (Problem 4).

A state is a type-configuration cfg[v] in {0 = empty, 1..k}. An agent of type t at v may jump to an empty u;
the move is improving iff its utility at u (computed with v now empty) is strictly larger than at v.
For one (graph, type counts, utility) instance, analyse() builds the move digraph on all configurations
and reports: IRC (a strongly connected component with >= 2 states), sinks (equilibria), and weak
acyclicity (every bottom SCC is a single sink). Exact integer comparisons only.
"""
import sys


def multiset_perms(counts_with_empty):
    """All sequences with counts_with_empty[c] copies of symbol c (c = 0..k)."""
    total = sum(counts_with_empty)
    seq = [0] * total
    rem = list(counts_with_empty)
    out = []

    def rec(i):
        if i == total:
            out.append(tuple(seq))
            return
        for c in range(len(rem)):
            if rem[c]:
                rem[c] -= 1
                seq[i] = c
                rec(i + 1)
                rem[c] += 1
    rec(0)
    return out


def util_variety(cfg, nbrs, at, t, vacated):
    seen = set()
    for w in nbrs[at]:
        if w != vacated:
            c = cfg[w]
            if c and c != t:
                seen.add(c)
    return len(seen)


def util_diversity(cfg, nbrs, at, t, vacated):
    other = occ = 0
    for w in nbrs[at]:
        if w != vacated:
            c = cfg[w]
            if c:
                occ += 1
                if c != t:
                    other += 1
    return (other, occ)


def better(util, new, old):
    if util == 'variety':
        return new > old
    (o2, n2), (o1, n1) = new, old
    if n2 == 0:
        return False
    if n1 == 0:
        return o2 > 0
    return o2 * n1 > o1 * n2


def moves(cfg, nbrs, util):
    f = util_variety if util == 'variety' else util_diversity
    empties = [u for u, c in enumerate(cfg) if c == 0]
    out = []
    for v, t in enumerate(cfg):
        if not t:
            continue
        old = f(cfg, nbrs, v, t, None)
        for u in empties:
            new = f(cfg, nbrs, u, t, v)
            if better(util, new, old):
                nc = list(cfg)
                nc[v], nc[u] = 0, t
                out.append((tuple(nc), v, u))
    return out


def tarjan(n, adj):
    index = [None] * n
    low = [0] * n
    onstack = [False] * n
    stack, comps = [], []
    comp_of = [None] * n
    idx = 0
    for root in range(n):
        if index[root] is not None:
            continue
        work = [(root, 0)]
        index[root] = low[root] = idx
        idx += 1
        stack.append(root)
        onstack[root] = True
        while work:
            v, i = work[-1]
            if i < len(adj[v]):
                work[-1] = (v, i + 1)
                w = adj[v][i]
                if index[w] is None:
                    index[w] = low[w] = idx
                    idx += 1
                    stack.append(w)
                    onstack[w] = True
                    work.append((w, 0))
                elif onstack[w]:
                    low[v] = min(low[v], index[w])
            else:
                work.pop()
                if work:
                    low[work[-1][0]] = min(low[work[-1][0]], low[v])
                if low[v] == index[v]:
                    comp = []
                    while True:
                        w = stack.pop()
                        onstack[w] = False
                        comp_of[w] = len(comps)
                        comp.append(w)
                        if w == v:
                            break
                    comps.append(comp)
    return comps, comp_of


def find_cycle(comp, adj, states):
    """A cycle inside a strongly connected component (as a list of state tuples, first == last)."""
    inside = set(comp)
    start = comp[0]
    parent = {start: None}
    order = [start]
    for v in order:                      # BFS inside the component until we return to start
        for w in adj[v]:
            if w == start:
                path = [v]
                while parent[path[-1]] is not None:
                    path.append(parent[path[-1]])
                path.reverse()
                return [states[s] for s in path] + [states[start]]
            if w in inside and w not in parent:
                parent[w] = v
                order.append(w)
    raise AssertionError('component without cycle')


def analyse(nbrs, counts, util, want_cycle=True):
    N = len(nbrs)
    e = N - sum(counts)
    states = multiset_perms([e] + list(counts))
    pos = {s: i for i, s in enumerate(states)}
    adj = [[pos[m[0]] for m in moves(s, nbrs, util)] for s in states]
    comps, comp_of = tarjan(len(states), adj)
    big = [c for c in comps if len(c) > 1]
    sinks = [i for i in range(len(states)) if not adj[i]]
    bottom_bad = []
    for ci, c in enumerate(comps):
        if len(c) > 1 and all(comp_of[w] == ci for v in c for w in adj[v]):
            bottom_bad.append(c)
    res = {'states': len(states), 'irc': bool(big), 'sinks': len(sinks), 'weakly_acyclic': not bottom_bad}
    if big and want_cycle:
        res['cycle'] = find_cycle(min(big, key=len), adj, states)
    if bottom_bad:
        res['trapped_state'] = states[bottom_bad[0][0]]
    return res


def partitions(n, kmin=2):
    """Sorted (descending) count vectors of n into at least kmin positive parts."""
    out = []

    def rec(rem, maxp, acc):
        if rem == 0:
            if len(acc) >= kmin:
                out.append(tuple(acc))
            return
        for p in range(min(rem, maxp), 0, -1):
            rec(rem - p, p, acc + [p])
    rec(n, n, [])
    return out


if __name__ == '__main__':
    # smoke test: the variety-seeking IRC of Theorem 3.1 needs 3 empties on a 3-regular graph
    import networkx as nx
    G = nx.complete_bipartite_graph(3, 3)
    nb = [tuple(G.neighbors(v)) for v in range(6)]
    print(analyse(nb, (1, 1, 1), 'variety'))
