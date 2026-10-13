"""Independent exact Q3892 controls; no import of the submitted checker."""
from collections import defaultdict
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
from math import comb, factorial
from pathlib import Path
import json


def rank(rows):
    basis = {}
    for source in rows:
        row = {k: Fraction(v) for k, v in source.items() if v}
        while row:
            pivot = min(row)
            if pivot not in basis:
                a = row[pivot]
                basis[pivot] = {k: v/a for k, v in row.items()}
                break
            a = row[pivot]
            for k, v in basis[pivot].items():
                row[k] = row.get(k, 0)-a*v
                if row[k] == 0:
                    del row[k]
    return len(basis)


def squarefree_apolar_row(monomials):
    """Literal constant-coefficient derivative matrices of a squarefree F."""
    d = len(monomials[0])
    answer = []
    for degree in range(d+1):
        operators = defaultdict(lambda: defaultdict(int))
        for mon in monomials:
            for op in combinations(mon, degree):
                remaining = tuple(x for x in mon if x not in op)
                operators[op][remaining] += 1
        answer.append(rank(operators.values()))
    return answer


def multiply(a, b):
    out = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def main():
    joins = []
    for q, s in product(range(2, 5), range(1, 4)):
        facets = list(product(range(s), repeat=q))
        mons = [tuple(sorted([q*s+a]+[i*s+x for i, x in enumerate(f)]))
                for a, f in enumerate(facets)]
        actual = squarefree_apolar_row(mons)
        d = q+1
        expected = [1]+[comb(q, i)*s**i+comb(q, i-1)*s**(d-i)
                        for i in range(1, d)]+[1]
        assert actual == expected
        joins.append({'q': q, 's': s, 'literal_derivative_ranks': actual})

    cm_controls = 0
    for q in range(10, 41):
        k = (q+1)//2
        j = k+1
        coefficients = [(-1)**(j-i)*comb(q-i, j-i) for i in range(j+1)]
        error = sum(abs(x) for x in coefficients[1:])
        for u, v in product(range(k, q+1), repeat=2):
            if u == v:
                continue
            targets = [1]+[comb(q, i) for i in range(1, k)]
            targets += [3**q+u*comb(q, j), 3**q+v*comb(q, j)]
            # f0/T <= 2, epsilon <= 1. Choose the worst empty-face sign.
            bound = sum(coefficients[i]*targets[i] for i in range(1, j+1))
            bound += max(0, 2*coefficients[0])+error
            assert bound < 0
            cm_controls += 1

    padding = []
    seed = [1, 234, 216, 234, 1]
    h = seed
    for r in range(1, 51):
        h = multiply(h, [1, 1])
        assert all(h[i+1] > h[i] for i in range((r+4)//2))
        padding.append(r)
    for d in range(12, 101):
        assert (d-1)*comb(d//2, 2)+1 < factorial(d//2)

    # Clear the reciprocal identity as an exact polynomial equation.
    hm = [1]
    for factor in [[1,-1,1], [1,-1,1], [1,-1], [1,-1], [1,-1]]:
        hm = multiply(hm, factor)
    numerator = [1]
    for factor in [[1,1], [1,1], [1,1,1], [1,1,1], [1,1,1], [1,0,0,1]]:
        numerator = multiply(numerator, factor)
    denominator = multiply(multiply([1,0,0,0,0,0,-1],
                                     [1,0,0,0,0,0,-1]),
                            [1,0,0,0,0,0,-1])
    assert multiply(hm, numerator) == denominator
    assert all(x >= 0 for x in numerator)

    connected = []
    for d in range(3, 9):
        mons = [tuple(range(d)), tuple(range(d, 2*d))]
        actual = squarefree_apolar_row(mons)
        expected = [1]+[2*comb(d, i) for i in range(1, d)]+[1]
        assert actual == expected
        connected.append({'d': d, 'literal_derivative_ranks': actual,
                          'quadratic_quotient_degree_d_dimension': 2})
    here = Path(__file__)
    out = {'result': 'PASS', 'independent_of': 'check_koszul_routes.py',
           'join_apolar_matrices': joins,
           'CM_template_pair_maximizations': cm_controls,
           'padding_rows': len(padding), 'order_bound_degrees': 89,
           'reciprocal_polynomial_identity': True,
           'connected_sum_apolar_matrices': connected,
           'scope': 'Exact finite controls supplement the reviewed all-size arguments.',
           'checker_sha256': sha256(here.read_bytes()).hexdigest()}
    here.with_name('KOSZUL-REVIEW-CHECK.json').write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps({k: out[k] for k in ['result', 'CM_template_pair_maximizations',
                                        'padding_rows', 'order_bound_degrees']}))


if __name__ == '__main__':
    main()
