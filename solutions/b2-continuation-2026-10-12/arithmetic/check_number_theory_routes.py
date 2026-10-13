#!/usr/bin/env python3
"""Finite powerful-number, unit-index and shifted-prime controls."""
from bisect import bisect_left, bisect_right
from itertools import product
from math import gcd, isqrt, lcm, log
from pathlib import Path
import json
import sympy as sp

HERE = Path(__file__).resolve().parent


def squarefree(n):
    return all(e==1 for e in sp.factorint(n).values())


def powerful_table(bound):
    values = set()
    a = 1
    while a**3 <= bound:
        if squarefree(a):
            for b in range(1,isqrt(bound//a**3)+1):
                values.add(a**3*b*b)
        a += 1
    return sorted(values)


def main():
    bound = 10**9
    values = powerful_table(bound)
    prefix = {n for n in range(1,100001) if all(e>=2 for e in sp.factorint(n).values())}
    assert prefix == {n for n in values if n<=100000}
    triples = {str(i):[] for i in range(3)}
    for a,b,c in zip(values,values[1:],values[2:]):
        if a+c == 2*b:
            squares = sum(isqrt(x)**2==x for x in (a,b,c))
            assert squares in (0,1,2)
            triples[str(squares)].append([a,b,c])
    x,y = 11427,617
    assert x*x-343*y*y == 2
    seed = [(x-2)**2,(x-1)**2,x*x-2]
    assert seed[0]+seed[2]==2*seed[1]
    assert all(t in values for t in seed)
    intruders = [n for n in values[bisect_left(values,seed[0]):bisect_right(values,seed[2])]
                 if n not in seed]
    assert intruders
    scaled = [9*n for n in [1728,1764,1800]]
    assert scaled[0]<125**2<scaled[1] and 125**2 in values
    pell_rows=[]
    a,b=1,0
    for m in range(1,31):
        a,b = a+2*b,a+b
        assert a*a-2*b*b == (-1)**m
        v=2*b
        factors=sp.factorint(v)
        assert sp.prod(p**e for p,e in factors.items())==v
        inert=[int(p) for p in factors if p%8 in (3,5)]
        pell_rows.append({'m':m,'v_m':v,'factors':{str(p):e for p,e in factors.items()},
                          'inert_factors':inert})
    assert pell_rows[6]['v_m']==338 and pell_rows[6]['factors']=={'2':1,'13':2}
    index_rows=[]
    for p in list(sp.primerange(3,101)):
        if p%8 not in (3,5):continue
        a,b=1,0
        for m in range(1,p+2):
            a,b=(a+2*b)%p,(a+b)%p
            if b==0:
                index_rows.append([int(p),m])
                break
        else:raise AssertionError(p)
    moment_bound=100000
    primes=[int(p) for p in sp.primerange(2,moment_bound+2)]
    omega=[0]*(moment_bound+1)
    for p in primes:
        for n in range(p-1,moment_bound+1,p-1):omega[n]+=1
    assert all(omega[n]==1 for n in range(1,moment_bound+1,2))
    moments=[]
    for X in [100,1000,10000,100000]:
        row={'X':X}
        for k in [2,3,4]:
            total=sum(w**k for w in omega[1:X+1])
            row[str(k)]={'exact_sum':total,'normalized_log_power':total/X/log(X)**(2**k-k-1)}
        moments.append(row)
    tuple_controls=[]
    for X,k in [(100,2),(1000,2),(100,3),(30,4)]:
        shifted=[p-1 for p in primes if p<=X+1]
        total=sum(X//lcm(*xs) for xs in product(shifted,repeat=k))
        assert total == sum(w**k for w in omega[1:X+1])
        tuple_controls.append([X,k,len(shifted)**k,total])
    powers_two=[]
    for exponent in range(1,61):
        hits=[j for j in range(exponent+1) if sp.isprime(2**j+1)]
        assert all(j==0 or j&(j-1)==0 for j in hits)
        assert len(hits)<=2+exponent.bit_length()-1
        powers_two.append([exponent,len(hits)])
    result={'status':'passed','powerful_last_term_bound':bound,'powerful_values':len(values),
            'independent_powerful_prefix':100000,'consecutive_AP_triples':triples,
            'Pell_seed':seed,'Pell_seed_intervening_powerful_values':intruders,
            'square_scaling_counterexample':{'triple':scaled,'intruder':125**2},
            'Pell_coefficient_factor_controls':pell_rows,'inert_unit_index_controls':index_rows,
            'shifted_prime_moment_bound':moment_bound,'moment_tables':moments,
            'independent_prime_tuple_identity_controls':tuple_controls,
            'power_of_two_shifted_prime_controls':powers_two,
            'scope':'Exact finite identities, rejected constructions and moment tables; no asymptotic extrapolation.'}
    (HERE/'NUMBER-THEORY-CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in {
        'Pell_coefficient_factor_controls','inert_unit_index_controls','power_of_two_shifted_prime_controls'}}))


if __name__=='__main__':main()
