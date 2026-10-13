#!/usr/bin/env python3
"""Exact finite controls for the four Ramsey proof/construction routes."""
from itertools import combinations
from pathlib import Path
import json
import sympy as sp

HERE = Path(__file__).resolve().parent


def valuation(n,p):
    e = 0
    while n%p == 0:
        n //= p
        e += 1
    return e


def distinct_schur_free(mask,p):
    points = [x for x in range(p) if mask>>x&1]
    for x,y in combinations(points,2):
        z = (x+y)%p
        if z not in (x,y) and mask>>z&1:
            return False
    return True


def main():
    ratio_controls = 0
    for a in range(1,21):
        for b in range(1,21):
            if a == b:
                continue
            fa,fb = sp.factorint(a),sp.factorint(b)
            prime = next(p for p in sorted(set(fa)|set(fb)) if fa.get(p,0)!=fb.get(p,0))
            d = abs(fa.get(prime,0)-fb.get(prime,0))
            for x in range(1,301):
                if a*x%b:
                    continue
                y = a*x//b
                assert (valuation(x,prime)//d)%2 != (valuation(y,prime)//d)%2
                ratio_controls += 1
    assert 2*1+3*11 == 7*5
    assert all(valuation(x,2)==0 for x in [1,11,5])
    P = 2*3*5*7*11
    coefficients = [P,2*P,-3*P+1]
    subset_sums = [sum(c for i,c in enumerate(coefficients) if mask>>i&1)
                   for mask in range(1,8)]
    assert all(s!=0 for s in subset_sums)
    assert all(any(s%q==0 for s in subset_sums) for q in [2,3,5,7,11])
    assert P*(P-1)+2*P*P-(3*P-1)*P == 0
    schur_rows = []
    for p in [2,3,5,7,11,13,17]:
        total,maximum = 0,0
        for mask in range(1<<p):
            if distinct_schur_free(mask,p):
                total += 1
                maximum = max(maximum,mask.bit_count())
                B = mask&~1
                assert 3*B.bit_count() <= p+3
        schur_rows.append({'p':p,'sets_checked':1<<p,'weakly_schur_free_sets':total,
                           'maximum_size':maximum})
    p,A = 13,{1,3,9}
    assert all((x+y)%p not in A for x in A for y in A)
    triangle = [0,1,4]
    assert all((x-y)%p in A or (y-x)%p in A for x,y in combinations(triangle,2))
    interval_controls = 0
    for p in list(sp.primerange(5,102)):
        for lo in range(1,p):
            for hi in range(lo,p):
                free = True
                for z in range(lo,hi+1):
                    for x in range(lo,hi+1):
                        y = (3*z-x)%p
                        if lo<=y<=hi and len({x,y,z})==3:
                            free = False
                            break
                    if not free:
                        break
                if free:
                    independent_size = min(lo,p-hi)
                    assert independent_size >= 2*(hi-lo+1)-10
                    interval_controls += 1
    greedy_controls = 0
    for n in range(2,51):
        for b in range(1,n):
            colours = []
            for x in range(n):
                earlier = [y for y in {(x+b)%n,(x-b)%n} if y<x]
                colours.append(next(c for c in range(3) if all(colours[y]!=c for y in earlier)))
            assert all(colours[x]!=colours[(x+b)%n] for x in range(n))
            greedy_controls += n
    colour = lambda x: 0 if x in {0,1,2,4} else 1
    assert all(colour(x)!=colour(x^7) for x in range(8))
    assert colour(3)==colour(5)==1 and colour(3&5)==0
    result = {'status':'passed','two_variable_valuation_controls':ratio_controls,
              'bounded_prime_counter_coefficients':coefficients,'subset_sums':subset_sums,
              'weak_schur_complete_tables':schur_rows,'strong_sum_free_triangle':[13,sorted(A),triangle],
              'mixed_coefficient_interval_controls':interval_controls,
              'greedy_three_colour_vertices_checked':greedy_controls,
              'Boolean_filter_counterexample_checked':True,
              'scope':'Finite controls of explicit obstructions and boundary proofs, not full-target closures.'}
    (HERE/'RAMSEY-CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
