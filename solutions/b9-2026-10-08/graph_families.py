#!/usr/bin/env python3
"""Graph families for Problem 4, each with an exhaustiveness check.

- connected graphs on N <= 7 vertices: networkx atlas (complete by construction);
- trees: networkx nonisomorphic_trees (complete); spiders = trees with at most one vertex of degree > 2;
- connected d-regular graphs: random sampling with isomorphism dedupe until the count matches OEIS
  (A002851 cubic, A006820 quartic, values read from the local OEIS mirror on 8 October 2026).
"""
import random
import networkx as nx

CUBIC = {4: 1, 6: 2, 8: 5, 10: 19, 12: 85, 14: 509}          # A002851, connected, N = 2n
QUARTIC = {5: 1, 6: 1, 7: 2, 8: 6, 9: 16, 10: 59, 11: 265}   # A006820, connected


def atlas_connected(nmin=3, nmax=7):
    return [G for G in nx.graph_atlas_g() if nmin <= G.number_of_nodes() <= nmax and nx.is_connected(G)]


def trees(N):
    return list(nx.nonisomorphic_trees(N))


def is_spider(T):
    return sum(1 for _, d in T.degree() if d > 2) <= 1


def regular(d, N, seed=0, max_tries=2_000_000):
    target = (CUBIC if d == 3 else QUARTIC)[N]
    rng = random.Random(seed)
    found, buckets = [], {}
    tries = 0
    while len(found) < target:
        tries += 1
        if tries > max_tries:
            raise RuntimeError(f'only {len(found)}/{target} {d}-regular graphs on {N} vertices found')
        G = nx.random_regular_graph(d, N, seed=rng.randrange(1 << 30))
        if not nx.is_connected(G):
            continue
        h = nx.weisfeiler_lehman_graph_hash(G)
        if any(nx.is_isomorphic(G, H) for H in buckets.get(h, [])):
            continue
        buckets.setdefault(h, []).append(G)
        found.append(G)
    return found


def nbrs_of(G):
    G = nx.convert_node_labels_to_integers(G)
    return [tuple(sorted(G.neighbors(v))) for v in range(G.number_of_nodes())]


if __name__ == '__main__':
    for N in (8, 10, 12):
        print('cubic', N, len(regular(3, N)))
    for N in (8, 9, 10):
        print('quartic', N, len(regular(4, N)))
    print('atlas connected 3..7:', len(atlas_connected()))
    print('trees 11:', len(trees(11)), 'spiders 11:', sum(map(is_spider, trees(11))))
