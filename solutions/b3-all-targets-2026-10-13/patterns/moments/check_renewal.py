#!/usr/bin/env python3
"""Literal sum/skew component checks of the exact renewal reduction."""
from itertools import combinations, permutations
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


def contains(beta, word):
    return any(all((beta[i] < beta[j]) == (word[idx[i]] < word[idx[j]])
                   for i in range(len(beta)) for j in range(i))
               for idx in combinations(range(len(word)), len(beta)))


def decomposable(word, skew):
    n = len(word)
    return any(set(word[:j]) == (set(range(n - j + 1, n + 1)) if skew else set(range(1, j + 1)))
               for j in range(1, n))


def main():
    indecomposable_initial = {}
    for skew in (False, True):
        initial = [sum(not decomposable(word, skew) for word in permutations(range(1, n + 1)))
                   for n in range(1, 4)]
        assert initial == [1, 1, 3]
        indecomposable_initial['skew' if skew else 'direct'] = initial
    # A proper direct and a proper skew cut cannot coexist in one permutation.
    pattern_controls = 0
    for n in range(2, 7):
        for beta in permutations(range(1, n + 1)):
            assert not (decomposable(beta, False) and decomposable(beta, True))
            pattern_controls += 1

    beta = (1, 3, 2, 4)
    assert decomposable(beta, False) and not decomposable(beta, True)
    a, indecomp = [], [0]
    for n in range(8):
        avoiders = [word for word in permutations(range(1, n + 1)) if not contains(beta, word)]
        a.append(len(avoiders))
        if n:
            indecomp.append(sum(not decomposable(word, True) for word in avoiders))
    assert a == [1, 1, 2, 6, 23, 103, 513, 2762]
    assert indecomp[1:7] == [1, 1, 3, 12, 56, 289]
    assert all(a[n] == sum(indecomp[j] * a[n - j] for j in range(1, n + 1))
               for n in range(1, 8))

    # Enumerate the actual nonprincipal layered class rather than assume Fibonacci.
    forbidden = [(2, 3, 1), (3, 1, 2), (3, 2, 1)]
    nonprincipal, parts = [], [0]
    for n in range(8):
        avoiders = [word for word in permutations(range(1, n + 1))
                    if all(not contains(p, word) for p in forbidden)]
        nonprincipal.append(len(avoiders))
        if n:
            parts.append(sum(not decomposable(word, False) for word in avoiders))
    assert nonprincipal == [1, 1, 2, 3, 5, 8, 13, 21]
    assert parts == [0, 1, 1, 0, 0, 0, 0, 0]
    assert nonprincipal[1] * nonprincipal[3] - nonprincipal[2] ** 2 == -1
    receipt = {'status': 'PASS', 'direct_and_skew_indec_counts_n1_to3': indecomposable_initial,
        'no_pattern_both_direct_and_skew_decomposable_controls': pattern_controls,
        'actual_beta': beta, 'closed_operation': 'skew sum', 'avoidance_counts_n0_to7': a,
        'actual_indec_counts_n1_to7': indecomp[1:],
        'actual_renewal_coefficient_identities': 7,
        'nonprincipal_positive_component_control': {'basis': forbidden,
            'counts': nonprincipal, 'indec_counts': parts[1:], 'negative_shifted_Hankel_det2': -1},
        'scope': 'Exact renewal reduction/failed inductive family closure; no principal-class Hankel counterexample.',
        'checker_sha256': sha256(Path(__file__).read_bytes()).hexdigest()}
    (HERE / 'RENEWAL-CHECK.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()
