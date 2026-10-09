#!/usr/bin/env python3
"""Q3259-3261 (Lin, Dartmouth thesis 2024, Ch. 2): Penney races for permutation patterns, Markov model.

Chain on S_k: X_0 uniform; P(sigma, tau) = 1/k iff st(sigma_2..sigma_k) = st(tau_1..tau_{k-1}). The chain is
doubly stochastic (each tau has exactly k predecessors), so pi is uniform. T_sigma = min{t >= 0 : X_t = sigma}.

Main method: Z = (I - P + Pi)^{-1} exactly (python-flint fmpq_mat). Then
  m(i, j) = E_i[T_j] = (Z_jj - Z_ij) / pi_j  (i != j),     E_pi[T_j] = Z_jj / pi_j - 1,
  Pr_pi(T_s < T_t) = (E_pi T_t - E_pi T_s + m(t, s)) / (m(s, t) + m(t, s)).
Check method (separate code path): direct absorbing-chain solves for hitting times / race probabilities.
"""
import itertools
import json
import random
import sys
from fractions import Fraction
import flint


def st(seq):
    order = sorted(seq)
    return tuple(order.index(x) + 1 for x in seq)


def chain(k):
    perms = list(itertools.permutations(range(1, k + 1)))
    idx = {p: i for i, p in enumerate(perms)}
    by_head = {}
    for p in perms:
        by_head.setdefault(st(p[:-1]), []).append(idx[p])
    succ = [by_head[st(p[1:])] for p in perms]
    return perms, idx, succ


def fundamental(k, perms, succ):
    n = len(perms)
    M = flint.fmpq_mat(n, n)
    inv_n = flint.fmpq(1, n)
    for i in range(n):
        for j in range(n):
            M[i, j] = inv_n
        M[i, i] += 1
        for j in succ[i]:
            M[i, j] -= flint.fmpq(1, k)
    return M.inv()


def to_frac(q):
    return Fraction(int(q.p), int(q.q))


def direct_hitting(k, succ, target):
    """E_x[T_target] for all x by solving (I - P restricted) h = 1; returns E_pi[T_target]."""
    n = len(succ)
    others = [i for i in range(n) if i != target]
    pos = {s: r for r, s in enumerate(others)}
    A = flint.fmpq_mat(n - 1, n - 1)
    b = flint.fmpq_mat(n - 1, 1)
    for r, s in enumerate(others):
        A[r, r] += 1
        b[r, 0] = 1
        for j in succ[s]:
            if j != target:
                A[r, pos[j]] -= flint.fmpq(1, k)
    h = A.solve(b)
    return sum((to_frac(h[r, 0]) for r in range(n - 1)), Fraction(0)) / n


def direct_race(k, succ, s, t):
    """Pr_pi(T_s < T_t) by solving the absorbing chain f = P f with f(s) = 1, f(t) = 0."""
    n = len(succ)
    others = [i for i in range(n) if i not in (s, t)]
    pos = {x: r for r, x in enumerate(others)}
    A = flint.fmpq_mat(n - 2, n - 2)
    b = flint.fmpq_mat(n - 2, 1)
    for r, x in enumerate(others):
        A[r, r] += 1
        for j in succ[x]:
            if j == s:
                b[r, 0] += flint.fmpq(1, k)
            elif j != t:
                A[r, pos[j]] -= flint.fmpq(1, k)
    f = A.solve(b)
    return (Fraction(1) + sum((to_frac(f[r, 0]) for r in range(n - 2)), Fraction(0))) / n


def main(k, n_check_pairs=60, seed=1):
    perms, idx, succ = chain(k)
    n = len(perms)
    Z = fundamental(k, perms, succ)
    Zd = [to_frac(Z[j, j]) for j in range(n)]
    ET = [n * Zd[j] - 1 for j in range(n)]

    def m(i, j):
        return (Zd[j] - to_frac(Z[i, j])) * n if i != j else Fraction(0)

    def race(s, t):
        return (ET[t] - ET[s] + m(t, s)) / (m(s, t) + m(t, s))

    inc, dec = idx[tuple(range(1, k + 1))], idx[tuple(range(k, 0, -1))]
    mono = {inc, dec}
    out = {'k': k, 'states': n}
    # Q3259
    worst = max(range(n), key=lambda j: ET[j])
    out['Q3259'] = {'E_T_increasing': str(ET[inc]), 'max_E_T': str(ET[worst]),
                    'argmax': [''.join(map(str, perms[j])) for j in range(n) if ET[j] == ET[worst]],
                    'violations': [''.join(map(str, perms[j])) for j in range(n) if ET[j] > ET[inc]]}
    # Q3260: one-way overlaps
    one_way = [(s, t) for s in range(n) for t in succ[s] if s != t and s not in succ[t]]
    v60, min60 = [], None
    for s, t in one_way:
        p = race(s, t)
        if min60 is None or p < min60[0]:
            min60 = (p, s, t)
        if p < Fraction(1, 2):
            v60.append((''.join(map(str, perms[s])), ''.join(map(str, perms[t])), str(p)))
    out['Q3260'] = {'pairs': len(one_way), 'violations': len(v60), 'examples': v60[:10],
                    'min_prob': str(min60[0]) if min60 else None,
                    'min_pair': [''.join(map(str, perms[min60[1]])), ''.join(map(str, perms[min60[2]]))] if min60 else None}
    # Q3261: monotone vs nonmonotone
    v61, max61 = [], None
    for s in mono:
        for t in range(n):
            if t in mono:
                continue
            p = race(s, t)
            if max61 is None or p > max61[0]:
                max61 = (p, s, t)
            if p > Fraction(1, 2):
                v61.append((''.join(map(str, perms[s])), ''.join(map(str, perms[t])), str(p)))
    out['Q3261'] = {'pairs': 2 * (n - 2), 'violations': len(v61), 'examples': v61[:10],
                    'max_prob': str(max61[0]), 'max_pair': [''.join(map(str, perms[max61[1]])), ''.join(map(str, perms[max61[2]]))]}
    # independent checks
    rng = random.Random(seed)
    hit_targets = list(range(n)) if k <= 4 else sorted({inc, dec, worst} | set(rng.sample(range(n), min(8, n))))
    hit_bad = [j for j in hit_targets if direct_hitting(k, succ, j) != ET[j]]
    pairs = [(s, t) for s in range(n) for t in range(n) if s != t] if k <= 3 else []
    if k >= 4:
        pairs = rng.sample([(s, t) for s in range(n) for t in range(n) if s != t], n_check_pairs)
        pairs += one_way[:10] + [(s, t) for s in mono for t in range(n) if t not in mono][:10]
        if min60 and (min60[0] < Fraction(1, 2) or v60):
            pairs += [(idx_s, idx_t) for (idx_s, idx_t) in [(min60[1], min60[2])]]
    race_bad = [(s, t) for s, t in pairs if direct_race(k, succ, s, t) != race(s, t)]
    out['checks'] = {'hitting_targets_checked': len(hit_targets), 'hitting_mismatches': len(hit_bad),
                     'race_pairs_checked': len(pairs), 'race_mismatches': len(race_bad)}
    return out


if __name__ == '__main__':
    results = []
    for k in (int(x) for x in sys.argv[1:]):
        r = main(k)
        results.append(r)
        print(json.dumps(r), flush=True)
        with open(f'markov_penney_k{k}.json', 'w') as fh:
            json.dump(r, fh, indent=1)
