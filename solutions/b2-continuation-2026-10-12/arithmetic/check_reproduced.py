#!/usr/bin/env python3
"""Standalone replay of controls originally run as inline B2 scripts."""
from collections import defaultdict
from itertools import combinations
from math import isqrt
from pathlib import Path
import json
import sympy as sp

HERE = Path(__file__).resolve().parent


def read(name):
    return json.loads((HERE / name).read_text())


def power_controls():
    old = read('POWER-EQUATION-CHECK.json')
    solutions = {}
    for sign in (1, -1):
        kernels = defaultdict(list)
        for a in range(1 if sign == 1 else 2, old['cubic_bound']+1):
            value = a**3 + sign
            factors = sp.factorint(value)
            assert sp.prod(p**e for p, e in factors.items()) == value
            kernel = int(sp.prod(p for p, e in factors.items() if e % 2))
            kernels[kernel].append(a)
        rows = []
        for kernel, values in kernels.items():
            for a, b in combinations(values, 2):
                product = (a**3+sign)*(b**3+sign)
                x = isqrt(product)
                assert x*x == product
                rows.append([a, b, x, kernel])
        solutions[str(sign)] = sorted(rows)
        assert solutions[str(sign)] == sorted(old['solutions'][str(sign)])
    a, b, x = old['quartic_minus_exception']
    assert (a**4-1)*(b**4-1) == x*x
    hits = []
    for k in range(2, 101):
        for y in range(1, 21):
            for z in range(1, 21):
                value = k**z-(2*k-1)**y
                if value > 0 and isqrt(value)**2 == value:
                    hits.append((k, isqrt(value), y, z))
    assert hits == [(k, k-1, 1, 2) for k in range(2, 101)]
    assert len(hits) == old['Terai_control']['hits']
    return {'cubic_bound': old['cubic_bound'], 'solutions': solutions,
            'quartic_minus_exception': [a,b,x], 'Terai_hits': len(hits)}


def factor_controls():
    old = read('FACTOR-CHECK.json')
    x = sp.Symbol('x')
    phis = {n: sp.Poly(sp.cyclotomic_poly(n,x),x,domain=sp.ZZ)
            for n in range(2, old['n_m_max']+1)}
    count = 0
    for n in phis:
        for m in range(n, old['n_m_max']+1):
            for h in (phis[n]+phis[m], phis[n]*phis[m]+sp.Poly(1,x)):
                content, factors = sp.factor_list(h)
                reconstructed = sp.Poly(content,x,domain=sp.ZZ)
                noncyclotomic = 0
                for factor, multiplicity in factors:
                    reconstructed *= factor**multiplicity
                    if not factor.is_cyclotomic:
                        noncyclotomic += multiplicity
                assert reconstructed == h
                assert noncyclotomic <= 1, (n,m,h)
                count += 1
    assert count == old['polynomials_checked']
    return {'n_m_max': old['n_m_max'], 'polynomials_checked': count}


def height_controls():
    old = read('CYCLOTOMIC-HEIGHT-CHECK.json')
    x = sp.Symbol('x')
    rows = []
    for expected in old['rows']:
        n = expected['n']
        phi = sp.Poly(sp.cyclotomic_poly(n,x),x,domain=sp.ZZ)
        inverse, remainder = sp.div(sp.Poly.from_dict({(n,):1,(0,):-1},x),phi)
        assert remainder.is_zero
        row = {'n': n, 'degree': phi.degree(),
               'height': int(max(abs(c) for c in phi.all_coeffs())),
               'inverse_height': int(max(abs(c) for c in inverse.all_coeffs()))}
        assert row == expected
        rows.append(row)
    return rows


def main():
    result = {'status':'passed', 'power_equations':power_controls(),
              'factorizations':factor_controls(), 'cyclotomic_heights':height_controls(),
              'scope':'Replay of declared finite controls; no expanded search or full closure.'}
    (HERE/'REPRODUCED-CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in {'power_equations','cyclotomic_heights'}}))


if __name__ == '__main__':
    main()
