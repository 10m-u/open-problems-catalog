#!/usr/bin/env python3
"""Side finding: Lemma 9 of arXiv:2510.24280v2 (AvA -> unilateral friendly deviation) fails as stated.

Lemma 9 claims, for S = {s2 < s1}: o1_AvA = o1_FvA, o2_AvA <= o2_FvA, o1_AvA <= o1_AvF, o2_AvA = o2_AvF.
The equalities fail; the smallest instance is S = {4, 7}, h = 34 (AvA = (18, 14), AvF = (19, 15)). The script
checks the stated lemma, the weakened version with every '=' replaced by '<=', and the paper's Theorem 3
(o_FvF >= o_AvA coordinatewise), using both subtraction.outcomes and an independent tree evaluator.
"""
import json
import sys
from functools import lru_cache
from subtraction import outcomes


def tree_outcomes(S, H):
    S = tuple(sorted(S))

    @lru_cache(maxsize=None)
    def t(h, me, other):
        if h < S[0]:
            return (0, 0)
        opts = []
        for s in S:
            if s <= h:
                nxt = t(h - s, other, me)
                opts.append((s + nxt[1], nxt[0]))
        m = max(x[0] for x in opts)
        tied = [x for x in opts if x[0] == m]
        return (min if me == 'A' else max)(tied, key=lambda x: x[1])
    for h in range(H + 1):
        for X in ('FvF', 'FvA', 'AvF', 'AvA'):
            t(h, X[0], X[2])
    return {X: [t(h, X[0], X[2]) for h in range(H + 1)] for X in ('FvF', 'FvA', 'AvF', 'AvA')}


def main(B=60, H=2000, tree_B=25, tree_H=400):
    stated, weak, thm3, pairs = 0, 0, 0, set()
    first = None
    for b in range(2, B + 1):
        for a in range(1, b):
            o = outcomes((a, b), H)
            if b <= tree_B:
                tr = tree_outcomes((a, b), tree_H)
                assert all(tr[X][h] == o[X][h] for X in tr for h in range(tree_H + 1)), (a, b)
            for h in range(H + 1):
                A, FA, AF, F = o['AvA'][h], o['FvA'][h], o['AvF'][h], o['FvF'][h]
                if A[0] != FA[0] or A[1] != AF[1] or A[1] > FA[1] or A[0] > AF[0]:
                    stated += 1
                    pairs.add((a, b))
                    if first is None or (b, h) < (first[0][1], first[1]):
                        first = ((a, b), h, {'AvA': A, 'FvA': FA, 'AvF': AF, 'FvF': F})
                if not (A[0] <= FA[0] and A[1] <= FA[1] and A[0] <= AF[0] and A[1] <= AF[1]):
                    weak += 1
                if not (F[0] >= A[0] and F[1] >= A[1]):
                    thm3 += 1
    out = {'B': B, 'H': H, 'tree_cross_check': f'b<={tree_B}, h<={tree_H}, all four profiles agree',
           'heaps_violating_stated_lemma9': stated, 'pairs_violating': len(pairs),
           'pairs_violating_in_dominant_regime': sum(1 for a, b in pairs if b >= 2 * a),
           'smallest_violation': first, 'weak_lemma9_failures': weak, 'theorem3_failures': thm3,
           'smallest_violating_pairs': sorted(pairs, key=lambda p: (p[1], p[0]))[:12]}
    print(json.dumps(out, indent=1))
    with open(f'lemma9_check_b{B}_H{H}.json', 'w') as fh:
        json.dump(out, fh, indent=1)


if __name__ == '__main__':
    main(*(int(x) for x in sys.argv[1:]))
