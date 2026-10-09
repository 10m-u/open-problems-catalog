#!/usr/bin/env python3
"""Independent check for Q2598: P(A appears before B) from the absorbing Markov chain on prefix states.

States are the distinct proper prefixes of A and B (including the empty prefix). From state w, appending a
symbol c moves to the longest suffix of wc that is a prefix of A or B, or absorbs if wc ends in A or B. The
absorption probabilities into A solve (2I - M) p = r over the integers (each symbol has probability 1/2);
solved by fraction-free Bareiss elimination. Shares no code with Conway's formula in penney_flipped.py.
"""
import json
import sys
from fractions import Fraction
from multiprocessing import Pool


def prob_A_first(A, B):
    prefixes = sorted({A[:k] for k in range(len(A))} | {B[:k] for k in range(len(B))}, key=len)
    idx = {w: i for i, w in enumerate(prefixes)}
    m = len(prefixes)
    M = [[0] * (m + 1) for _ in range(m)]      # augmented integer system: 2 p_w - sum p_next = [hits A]
    for w, i in idx.items():
        M[i][i] += 2
        for c in 'HT':
            s = w + c
            if s.endswith(A):
                M[i][m] += 1
                continue
            if s.endswith(B):
                continue
            k = len(s)
            while s[len(s) - k:] not in idx:
                k -= 1
            M[i][idx[s[len(s) - k:]]] -= 1
    # Bareiss fraction-free elimination
    prev = 1
    for k in range(m):
        piv = next(r for r in range(k, m) if M[r][k] != 0)
        if piv != k:
            M[k], M[piv] = M[piv], M[k]
        for r in range(k + 1, m):
            for c in range(k + 1, m + 1):
                M[r][c] = (M[r][c] * M[k][k] - M[r][k] * M[k][c]) // prev
            M[r][k] = 0
        prev = M[k][k]
    x = [Fraction(0)] * m
    for r in range(m - 1, -1, -1):
        s = Fraction(M[r][m]) - sum(Fraction(M[r][c]) * x[c] for c in range(r + 1, m))
        x[r] = s / M[r][r]
    return x[idx['']]


def words(n):
    return [''.join('H' if (v >> (n - 1 - i)) & 1 else 'T' for i in range(n)) for v in range(1 << n)]


def check_A(args):
    A, n = args
    W = words(n)
    vals = {B: prob_A_first(A, B) for B in W if B != A}
    best = max(vals.values())
    opt = sorted(B for B, v in vals.items() if v == best)
    cands = {'H' * n, 'T' * n, A[1:] + 'H', A[1:] + 'T'} - {A}
    return A, opt, str(best), [B for B in opt if B not in cands]


if __name__ == '__main__':
    lo, hi = (int(v) for v in sys.argv[1:3])
    report = {}
    with Pool(3) as pool:
        for n in range(lo, hi + 1):
            As = [A for A in words(n) if A[0] == 'H']
            res = pool.map(check_A, [(A, n) for A in As], chunksize=4)
            report[n] = {'A_checked': len(res), 'counterexamples': [r for r in res if r[3]],
                         'optimal': {r[0]: [r[1], r[2]] for r in res}}
            print(n, len(res), 'counterexamples', len(report[n]['counterexamples']), flush=True)
    with open(f'penney_markov_n{lo}-{hi}.json', 'w') as fh:
        json.dump(report, fh)
