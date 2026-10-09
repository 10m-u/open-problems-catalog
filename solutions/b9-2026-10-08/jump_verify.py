#!/usr/bin/env python3
"""Independent re-check of jump-game certificates (separately written; shares no code with jump_games.py).

verify_cycle(edges, cycle, util): every consecutive pair of configurations differs by one agent moving from
an occupied vertex to an empty one, and that agent's utility strictly rises. Utilities are recomputed here
from the edge list with Fractions (diversity) or type sets (variety).
verify_no_path_to_sink(edges, start, util): brute-force forward closure from start contains no equilibrium.
"""
from fractions import Fraction


def neighbours(edges, n):
    nb = {v: set() for v in range(n)}
    for u, v in edges:
        nb[u].add(v)
        nb[v].add(u)
    return nb


def utility(config, nb, v, util):
    t = config[v]
    occupied = [config[w] for w in nb[v] if config[w] != 0]
    if util == 'variety':
        return len(set(occupied) - {t})
    if not occupied:
        return Fraction(0)
    return Fraction(sum(1 for c in occupied if c != t), len(occupied))


def single_move(a, b):
    diff = [v for v in range(len(a)) if a[v] != b[v]]
    if len(diff) != 2:
        return None
    x, y = diff
    if a[x] != 0 and a[y] == 0 and b[x] == 0 and b[y] == a[x]:
        return x, y
    if a[y] != 0 and a[x] == 0 and b[y] == 0 and b[x] == a[y]:
        return y, x
    return None


def verify_cycle(edges, cycle, util):
    n = len(cycle[0])
    nb = neighbours(edges, n)
    assert list(cycle[0]) == list(cycle[-1]), 'not closed'
    steps = []
    for a, b in zip(cycle, cycle[1:]):
        mv = single_move(a, b)
        assert mv, f'not a single jump: {a} -> {b}'
        src, dst = mv
        before, after = utility(a, nb, src, util), utility(b, nb, dst, util)
        assert after > before, f'not improving: {a} -> {b} ({before} -> {after})'
        steps.append((src, dst, str(before), str(after)))
    return steps


def successors(config, nb, util):
    out = []
    for v, t in enumerate(config):
        if t == 0:
            continue
        here = utility(config, nb, v, util)
        for u, c in enumerate(config):
            if c == 0:
                new = list(config)
                new[v], new[u] = 0, t
                if utility(new, nb, u, util) > here:
                    out.append(tuple(new))
    return out


def verify_no_path_to_sink(edges, start, util):
    nb = neighbours(edges, len(start))
    seen, todo = {tuple(start)}, [tuple(start)]
    while todo:
        s = todo.pop()
        nxt = successors(s, nb, util)
        assert nxt, f'reached an equilibrium {s}'
        for t in nxt:
            if t not in seen:
                seen.add(t)
                todo.append(t)
    return len(seen)


if __name__ == '__main__':
    import json
    import sys
    data = json.load(open(sys.argv[1]))
    ok = bad = 0
    for f in data['flagged']:
        try:
            if f['cycle']:
                verify_cycle(f['edges'], f['cycle'], f['util'])
            if f['trapped_state']:
                verify_no_path_to_sink(f['edges'], f['trapped_state'], f['util'])
            ok += 1
        except AssertionError as err:
            bad += 1
            print('FAILED', f['gid'], f['counts'], err)
    print(sys.argv[1], 'verified', ok, 'failed', bad)
