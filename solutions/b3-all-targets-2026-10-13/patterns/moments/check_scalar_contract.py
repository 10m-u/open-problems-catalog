#!/usr/bin/env python3
"""Formal all-n scalar-criterion obstruction with exact principal-prefix control."""
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, permutations
from math import factorial
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
PREFIX = (1, 1, 2, 6, 23, 103)


def b(n):
    return PREFIX[n] if n < 6 else 512 * 8 ** (n - 6)


def contains(beta, word):
    return any(all((beta[i] < beta[j]) == (word[idx[i]] < word[idx[j]])
                   for i in range(len(beta)) for j in range(i))
               for idx in combinations(range(len(word)), len(beta)))


def determinant(matrix):
    A = [list(map(Fraction, row)) for row in matrix]
    result = Fraction(1)
    for col in range(len(A)):
        pivot = next((i for i in range(col, len(A)) if A[i][col]), None)
        if pivot is None:
            return 0
        if pivot != col:
            A[pivot], A[col] = A[col], A[pivot]
            result = -result
        p = A[col][col]
        result *= p
        for i in range(col + 1, len(A)):
            ratio = A[i][col] / p
            for j in range(col + 1, len(A)):
                A[i][j] -= ratio * A[col][j]
    assert result.denominator == 1
    return result.numerator


def main():
    beta = (1, 3, 4, 2)
    actual = [sum(not contains(beta, word) for word in permutations(range(1, n + 1)))
              for n in range(7)]
    assert actual == [b(n) for n in range(7)]
    defects = [b(n - 1) * b(n + 1) - b(n) ** 2 for n in range(1, 7)]
    assert defects == [1, 2, 10, 89, 1167, 159744]
    assert all(b(n) <= factorial(n) for n in range(9))
    assert all(b(i) <= 8 ** i for i in range(6))
    finite_super = [(m, n) for m in range(6) for n in range(6)]
    assert all(b(m) * b(n) <= b(m + n) for m, n in finite_super)
    # These controls accompany the all-n induction/case split in the proof.
    assert all(b(n + 1) == 8 * b(n) for n in range(6, 31))
    assert all(b(n) <= b(n + 1) for n in range(31))
    assert all(b(n - 1) * b(n + 1) >= b(n) ** 2 for n in range(1, 31))
    assert all(b(m) * b(n) <= b(m + n) for m in range(31) for n in range(31))
    coeff = [0, 1, 0, -8, 1]
    value = sum(ci * cj * b(i + j) for i, ci in enumerate(coeff) for j, cj in enumerate(coeff))
    assert value == -160
    H = [[b(i + j) for j in range(5)] for i in range(5)]
    assert determinant(H) == -5959888
    receipt = {'status': 'PASS', 'formal_sequence_not_actual_avoidance': True,
        'known_1342_prefix_used_as_calibration_only': actual,
        'adjacent_logconvexity_defects_before_geometric_tail': defects,
        'finite_pairs_sufficient_for_all_n_supermultiplicativity_proof': len(finite_super),
        'negative_polynomial_coefficients': coeff, 'negative_quadratic_form': value,
        'H0_size5_determinant': determinant(H),
        'scope': 'Exact obstruction to the stated scalar sufficient criterion; Q1454 not refuted.',
        'checker_sha256': sha256(Path(__file__).read_bytes()).hexdigest()}
    (HERE / 'SCALAR-CONTRACT-CHECK.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()
