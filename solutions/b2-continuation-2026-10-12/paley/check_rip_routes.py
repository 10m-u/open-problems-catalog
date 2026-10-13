"""Exact compressed-matrix controls and random-support fourth moments."""
from fractions import Fraction
from itertools import combinations
from math import comb
import json
from pathlib import Path


def matrix(p):
    sq = {x*x % p for x in range(1, p)}
    return [[0 if x == y else 1 if x == p or y == p or (x-y) % p in sq else -1
             for y in range(p+1)] for x in range(p+1)]


def squared(a):
    return [[sum(x*z for x, z in zip(row, col)) for col in zip(*a)] for row in a]


def determinant(a):
    a = [[Fraction(x) for x in row] for row in a]
    out = Fraction(1)
    for i in range(len(a)):
        if not a[i][i]:
            j = next((j for j in range(i+1, len(a)) if a[j][i]), None)
            if j is None:
                return Fraction(0)
            a[i], a[j] = a[j], a[i]
            out = -out
        pivot = a[i][i]
        out *= pivot
        for j in range(i+1, len(a)):
            factor = a[j][i]/pivot
            for k in range(i+1, len(a)):
                a[j][k] -= factor*a[i][k]
            a[j][i] = 0
    return out


def main():
    subsets = leakage_entries = positive_integer_norms = 0
    fourth_moment_groups = []
    for p, limit in [(5, 3), (13, 4), (17, 3)]:
        s = matrix(p)
        assert squared(s) == [[p if i == j else 0 for j in range(p+1)] for i in range(p+1)]
        for k in range(1, limit+1):
            total = 0
            for ix in combinations(range(p+1), k):
                a = [[s[i][j] for j in ix] for i in ix]
                a2 = squared(a)
                outside = [j for j in range(p+1) if j not in ix]
                for i, x in enumerate(ix):
                    for j, y in enumerate(ix):
                        leakage = sum(s[x][z]*s[y][z] for z in outside)
                        assert a2[i][j]+leakage == (p if i == j else 0)
                        leakage_entries += 1
                norm_matrix = [[(p if i == j else 0)-a2[i][j] for j in range(k)] for i in range(k)]
                value = determinant(norm_matrix)
                assert value.denominator == 1 and value >= 1
                positive_integer_norms += 1
                trace4 = sum(x*x for row in a2 for x in row)
                assert trace4 <= p*k*(k-1)
                total += trace4
                subsets += 1
            expected = Fraction(total, comb(p+1, k))
            formula = Fraction(k*(k-1)*(2*k-3))-Fraction(k*(k-1)*(k-2)*(k-3), p-2)
            assert expected == formula
            fourth_moment_groups.append({'p': p, 'k': k, 'exact_expectation': str(expected)})
    assert all(comb(p, (p+1)//2) > p*(p-1) for p in [13, 17, 29, 61])
    receipt = {'passed': True, 'exact_supports': subsets,
               'exact_leakage_entries': leakage_entries,
               'positive_integer_norm_determinants': positive_integer_norms,
               'random_support_fourth_moments': fourth_moment_groups,
               'scope': 'Exact finite algebraic identities and determinant controls; no uniform asymptotic RIP certification.'}
    Path(__file__).with_name('RIP-CHECK-RESULTS.json').write_text(json.dumps(receipt, indent=2)+'\n')
    print(json.dumps(receipt))


if __name__ == '__main__':
    main()
