#!/usr/bin/env python3
"""Exact full-state insertion-operator obstruction, separate from Hankel forms."""
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


def children(beta, word):
    return [v for i in range(len(word) + 1)
            if not contains(beta, v := word[:i] + (len(word) + 1,) + word[i:])]


def verify(beta, parent, expected):
    child = children(beta, parent)
    grandchildren = [children(beta, v) for v in child]
    degrees = list(map(len, grandchildren))
    assert degrees == expected
    assert len({w for row in grandchildren for w in row}) == sum(degrees)
    assert all(tuple(x for x in w if x != len(w)) == v
               for v, row in zip(child, grandchildren) for w in row)
    reciprocal = sum(Fraction(1, d) for d in degrees)
    assert reciprocal > 1
    return child, degrees, reciprocal


def main():
    beta = (1, 3, 2, 4)
    child, degrees, reciprocal = verify(beta, (1, 2, 3, 4), [6, 3, 4, 5, 6])
    coefficients = [10, 20, 15, 12, 10]
    norm_c = sum(d * v ** 2 for d, v in zip(degrees, coefficients))
    norm_adjoint = sum(coefficients) ** 2
    assert norm_c == 4020 and norm_adjoint == 4489
    assert norm_c - norm_adjoint == -469 and reciprocal == Fraction(67, 60)
    # Exact root-level norm identity, all small levels; not a new moment test.
    frontier = {()}
    for n in range(7):
        literal = {p for p in permutations(range(1, n + 1)) if not contains(beta, p)}
        assert frontier == literal
        frontier = {q for p in frontier for q in children(beta, p)}
    known_catalan = verify((1, 2, 3), (2, 1), [4, 2, 3])
    receipt = {'status': 'PASS', 'actual_beta': beta, 'parent': [1, 2, 3, 4],
        'children': child, 'grandchild_counts': degrees,
        'reciprocal_sum': str(reciprocal), 'integer_test_vector': coefficients,
        'norm_creation_squared': norm_c, 'norm_adjoint_squared': norm_adjoint,
        'negative_full_operator_form': norm_c - norm_adjoint,
        'root_level_identity_controls_through_n': 6,
        'known_Catalan_control_not_new_attempt': {'beta': [1, 2, 3], 'parent': [2, 1],
            'grandchild_counts': known_catalan[1], 'reciprocal_sum': str(known_catalan[2])},
        'scope': 'Failure of a full-state normal-extension construction; not an actual avoidance Hankel minor.',
        'checker_sha256': sha256(Path(__file__).read_bytes()).hexdigest()}
    (HERE / 'TREE-OPERATOR-CHECK.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()
