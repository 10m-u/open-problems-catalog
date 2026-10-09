#!/usr/bin/env python3
"""Mechanical check of every lemma used in PROOF-Q3188.md, against an independent AvA evaluator.

The proof is the written argument; this script checks each lemma's statement over a finite range, so
that a slip in the write-up would show up as a failure. The AvA outcome here is computed by explicit
recursion over (heap, profile) with the tie rule written straight from Definition 2. It does not share
code with subtraction.py or q3188_scan.py.
"""
import json
import sys
from functools import lru_cache

sys.setrecursionlimit(100000)


def ava_tree(a, b, H):
    """AvA outcome by memoized recursion on the explicit game tree (Definition 2, X = d(X) = AvA)."""
    @lru_cache(maxsize=None)
    def out(h):
        if h < a:
            return (0, 0)
        options = []
        for s in (a, b):
            if s <= h:
                first_next, second_next = out(h - s)   # roles swap after the move
                options.append((s + second_next, first_next))
        best_own = max(o[0] for o in options)
        tied = [o for o in options if o[0] == best_own]
        return min(tied, key=lambda o: o[1])         # antagonistic: minimize opponent's cumulation
    for h in range(H + 1):                            # fill bottom-up so recursion stays shallow
        out(h)
    return [out(h) for h in range(H + 1)]


def one_player(a, b, H):
    """G = best response of the mover against an opponent who always removes the largest legal move.
    V(y) = G(y - g(y)) is what the player to move second from y collects."""
    G = [0] * (H + 1)
    V = [0] * (H + 1)
    for y in range(a, H + 1):
        g = b if y >= b else a
        V[y] = G[y - g]
        G[y] = max(s + V[y - s] for s in (a, b) if s <= y)
    return G, V


def zero_sum_value(a, b, H):
    z = [0] * (H + 1)
    for h in range(a, H + 1):
        z[h] = max(s - z[h - s] for s in (a, b) if s <= h)
    return z


def closed_form(a, b, G, H):
    D = b - a
    theta = [e - G[e] for e in range(2 * b)]
    res = []
    for y in range(H + 1):
        N, rho = divmod(y, 2 * b)
        res.append(b * N + rho - min(theta[rho + i * D] for i in range(N + 1) if rho + i * D < 2 * b))
    return res


def check(a, b, H):
    D = b - a
    tree = ava_tree(a, b, H)
    G, V = one_player(a, b, H + 2 * b)
    z = zero_sum_value(a, b, H)
    fails = []
    for h in range(H + 1):
        if tree[h] != (G[h], V[h]):
            fails.append(('AvA=(G,V)', h))
        if z[h] != G[h] - V[h]:
            fails.append(('z=G-V', h))
    if closed_form(a, b, G, H) != G[:H + 1]:
        fails.append(('closed form', None))
    delta = [G[t + D] - G[t] for t in range(H + 1)]
    eps = [V[t + D] - V[t] for t in range(H + 1)]
    for t in range(H + 1):
        if delta[t] < 0 or eps[t] < 0:
            fails.append(('M', t))
        if t < b and eps[t] > D:
            fails.append(('eps<=Delta below b', t))
        if t >= b and eps[t] != delta[t - b]:
            fails.append(('eps=delta(t-b)', t))
        if delta[t] > D:
            if not (t < a or (t >= a + b and delta[t - a - b] > D)):
                fails.append(('chain', t))
            if 2 * a <= b:
                fails.append(('no excess when b>=2a', t))
            if t + b <= H and delta[t + b] != 0:
                fails.append(('P', t))
            if 2 * a > b and t < a and not (a - D <= t):
                fails.append(('base block', t))
    return fails


if __name__ == '__main__':
    B, H = (int(x) for x in sys.argv[1:3]) if len(sys.argv) > 2 else (40, 600)
    bad = {}
    for b in range(2, B + 1):
        for a in range(1, b):
            f = check(a, b, H)
            if f:
                bad[f'{a},{b}'] = f[:5]
    result = {'max_b': B, 'H': H, 'pairs': B * (B - 1) // 2, 'failing_pairs': len(bad), 'examples': dict(list(bad.items())[:5])}
    print(json.dumps(result, indent=2))
    with open(f'q3188_proof_check_b{B}_H{H}.json', 'w') as fh:
        json.dump(result, fh, indent=2)
