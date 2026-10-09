#!/usr/bin/env python3
"""Q2598 (Phillips–Hildebrand, Conjecture 7.3): best responses in the flipped Penney-Ante game.

Flipped game: the owner of the string that appears first loses, so II (string B) wins iff A appears first.
By Conway's formula (Prop. 2.3 of the source), P(A first) = X / (X + Y) with X = C(B,B) - C(B,A) and
Y = C(A,A) - C(A,B). Strings are ints with bit (n - i) = 1 iff the i-th symbol is H.

For each A with a1 = H (complementing both strings preserves every probability and maps the candidate set
onto itself), the best of the four candidates {H^n, T^n, a2..anH, a2..anT} \\ {A} is compared with the bound
U(A) = (3*2^(n-2) - 1) / (2^(n-1) + AA), which caps P(A first) for every non-candidate B (see the method
note in PREREGISTRATION.md). If the bound does not separate, every B is evaluated. Exact integer arithmetic.
"""
import json
import sys
import time
import numpy as np


def corr_vec(X, Y, n):
    """C(X, Y) elementwise for int arrays (or scalars broadcast)."""
    out = np.zeros(np.broadcast(X, Y).shape, dtype=np.int64)
    for L in range(1, n + 1):
        out += (((X & ((1 << L) - 1)) == (Y >> (n - L))).astype(np.int64)) << (L - 1)
    return out


def corr(x, y, n):
    return sum(1 << (L - 1) for L in range(1, n + 1) if (x & ((1 << L) - 1)) == (y >> (n - L)))


def exact_argmax(Xv, Yv):
    """Indices maximizing X/Y exactly (X, Y > 0)."""
    m = int(np.argmax(Xv / Yv))
    while True:
        worse = Xv * Yv[m] > Xv[m] * Yv
        if not worse.any():
            break
        m = int(np.flatnonzero(worse)[0])
    return np.flatnonzero(Xv * Yv[m] == Xv[m] * Yv), m


def run(n):
    N = 1 << n
    allB = np.arange(N, dtype=np.int64)
    BB = corr_vec(allB, allB, n)
    full = (1 << n) - 1
    capX = 3 * (1 << (n - 2)) - 1
    stats = {'n': n, 'A_checked': 0, 'full_scans': 0, 'counterexamples': [], 'optimal_set_sizes': {},
             'optimal_types': {}}
    for A in range(1 << (n - 1), N):            # a1 = H
        AA = corr(A, A, n)
        tail = (A << 1) & full
        cands = {full: 'H^n', 0: 'T^n', tail | 1: 'tail+H', tail: 'tail+T'}
        cands.pop(A, None)
        vals = {}
        for B in cands:
            vals[B] = (corr(B, B, n) - corr(B, A, n), AA - corr(A, B, n))
        best = max(vals.values(), key=lambda xy: xy[0] / xy[1])
        bx, by = best
        for xy in vals.values():                # exact max among candidates
            if xy[0] * by > bx * xy[1]:
                bx, by = xy
        opt_c = sorted(B for B, (x, y) in vals.items() if x * by == bx * y)
        stats['A_checked'] += 1
        if bx * (2 ** (n - 1) + AA) > capX * (bx + by):
            opt = opt_c
        else:
            stats['full_scans'] += 1
            AB = corr_vec(np.int64(A), allB, n)
            BA = corr_vec(allB, np.int64(A), n)
            Xv = BB - BA
            Yv = AA - AB
            mask = allB != A
            idx = np.flatnonzero(mask)
            sel, _ = exact_argmax(Xv[idx], Yv[idx])
            opt = sorted(int(idx[i]) for i in sel)
            outside = [B for B in opt if B not in cands]
            if outside:
                stats['counterexamples'].append({'A': fmt(A, n), 'optimal': [fmt(B, n) for B in opt],
                                                 'outside_set': [fmt(B, n) for B in outside]})
        k = str(len(opt))
        stats['optimal_set_sizes'][k] = stats['optimal_set_sizes'].get(k, 0) + 1
        t = '+'.join(sorted(cands.get(B, 'OTHER') for B in opt))
        stats['optimal_types'][t] = stats['optimal_types'].get(t, 0) + 1
    return stats


def fmt(x, n):
    return ''.join('H' if (x >> (n - 1 - i)) & 1 else 'T' for i in range(n))


if __name__ == '__main__':
    lo, hi = (int(v) for v in sys.argv[1:3])
    allstats = []
    for n in range(lo, hi + 1):
        t0 = time.time()
        s = run(n)
        s['seconds'] = round(time.time() - t0, 1)
        allstats.append(s)
        print(json.dumps({k: v for k, v in s.items() if k != 'counterexamples'}),
              'counterexamples:', len(s['counterexamples']), flush=True)
        with open(f'penney_flipped_n{n}.json', 'w') as fh:
            json.dump(s, fh, indent=1)
