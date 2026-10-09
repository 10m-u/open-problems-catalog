#!/usr/bin/env python3
"""Exact unlabeled-tree and subset enumeration; no third-party dependencies."""
import json
from itertools import product
from pathlib import Path


def rooted_shapes(max_n):
    shapes = [()]
    sizes = [1]
    by_size = {1: [0]}
    for n in range(2, max_n + 1):
        old_len = len(shapes)
        def combinations(rem, start):
            if rem == 0:
                yield ()
                return
            for child in range(start, old_len):
                w = sizes[child]
                if w > rem:
                    break
                for tail in combinations(rem - w, child):
                    yield (child,) + tail
        new = list(combinations(n - 1, 0))
        by_size[n] = list(range(len(shapes), len(shapes) + len(new)))
        shapes.extend(new)
        sizes.extend([n] * len(new))
    return shapes, by_size


def adjacency(shape, shapes):
    adj = []
    def add(s, parent=-1):
        v = len(adj)
        adj.append([])
        if parent >= 0:
            adj[v].append(parent)
            adj[parent].append(v)
        for child in shapes[s]:
            add(child, v)
    add(shape)
    return adj


def canonical(adj):
    n = len(adj)
    degree = list(map(len, adj))
    leaves = [v for v in range(n) if degree[v] <= 1]
    remaining = n
    while remaining > 2:
        remaining -= len(leaves)
        fresh = []
        for v in leaves:
            for u in adj[v]:
                degree[u] -= 1
                if degree[u] == 1:
                    fresh.append(u)
        leaves = fresh
    def code(v, parent):
        return '(' + ''.join(sorted(code(u, v) for u in adj[v] if u != parent)) + ')'
    return min(code(v, -1) for v in leaves)


def exact_parameters(adj):
    n = len(adj)
    masks = [sum(1 << u for u in ns) for ns in adj]
    edges = [(v, u) for v in range(n) for u in adj[v] if v < u]
    forced = 0
    for ns in adj:
        if len(ns) == 1:
            forced |= 1 << ns[0]
    options = [v for v in range(n) if not (forced >> v) & 1]
    a, b = n + 1, n + 1
    aw, bw = None, None
    for mask in range(1 << len(options)):
        size = forced.bit_count() + mask.bit_count()
        if size >= a and size >= b:
            continue
        s = forced
        for j, v in enumerate(options):
            s |= ((mask >> j) & 1) << v
        sigma = [(s & m).bit_count() for m in masks]
        if not all(sigma):
            continue
        if size < a:
            a, aw = size, s
        if size < b and all(sigma[v] != sigma[u] for v, u in edges):
            b, bw = size, s
    return a, None if b > n else b, aw, bw


def main(max_n=13):
    shapes, by_size = rooted_shapes(max_n)
    pairs = {}
    counts = {}
    for n in range(2, max_n + 1):
        seen = set()
        count_feasible = 0
        for rid in by_size[n]:
            adj = adjacency(rid, shapes)
            key = canonical(adj)
            if key in seen:
                continue
            seen.add(key)
            a, b, aw, bw = exact_parameters(adj)
            if b is None:
                continue
            count_feasible += 1
            if (a, b) not in pairs:
                pairs[a, b] = {'n': n, 'adjacency': adj,
                               'total_witness': [v for v in range(n) if (aw >> v) & 1],
                               'proper_witness': [v for v in range(n) if (bw >> v) & 1]}
        counts[n] = {'trees': len(seen), 'with_proper_total_set': count_feasible}
        print(n, counts[n], flush=True)
    output = {'maximum_order': max_n, 'counts_by_order': counts,
              'pairs': [{'a': a, 'b': b, **data} for (a, b), data in sorted(pairs.items())]}
    Path(__file__).with_name('tree-enumeration.json').write_text(json.dumps(output, indent=2) + '\n')
    print('Pairs', sorted(pairs))

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--max-n', type=int, default=13)
    main(parser.parse_args().max_n)
