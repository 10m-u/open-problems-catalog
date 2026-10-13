#!/usr/bin/env python3
"""Exact controls for two split-direction and matching-proof obstructions."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import gcd
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


def matching_proof(n, edges, deficiency):
    """Half-integral LP oracle, exhaustive optimal variable proof synthesis."""
    edges = tuple(edges)
    m = len(edges)
    threshold = F(n-deficiency+1, 2)
    feasible = []
    for doubled in product(range(3), repeat=m):
        degree = [0]*n
        for (u,v), x in zip(edges,doubled):
            degree[u] += x
            degree[v] += x
        if max(degree) <= 2:
            feasible.append((doubled, sum(doubled)))
    integer_max = max(F(total,2) for x,total in feasible if all(v != 1 for v in x))
    assert integer_max < threshold

    @lru_cache(None)
    def lp(state):
        candidates = [total for x,total in feasible
                      if all(y == -1 or x[i] == 2*y for i,y in enumerate(state))]
        return F(max(candidates),2) if candidates else None

    @lru_cache(None)
    def solve(state):
        value = lp(state)
        if value is None or value < threshold:
            return (1,None)
        best = (10**9,None)
        for i,x in enumerate(state):
            if x == -1:
                zero = state[:i]+(0,)+state[i+1:]
                one = state[:i]+(1,)+state[i+1:]
                candidate = solve(zero)[0]+solve(one)[0]
                if candidate < best[0]:
                    best = (candidate,i)
        assert best[1] is not None
        return best

    initial = (-1,)*m
    leaves, branch = solve(initial)
    @lru_cache(None)
    def depth(state):
        value = lp(state)
        if value is None or value < threshold:
            return 0
        return 1+min(max(depth(state[:i]+(0,)+state[i+1:]),
                         depth(state[:i]+(1,)+state[i+1:]))
                     for i,x in enumerate(state) if x == -1)
    return {'vertices':n, 'edges':[list(e) for e in edges],
            'deficiency_parameter':deficiency, 'integer_matching_max':str(integer_max),
            'fractional_matching_max':str(lp(initial)), 'minimum_variable_leaves':leaves,
            'minimum_possible_depth':depth(initial),
            'optimal_root_edge':list(edges[branch]) if branch is not None else None,
            'states_examined':solve.cache_info().currsize,
            'root_child_lp':[
                {'edge':list(edges[i]),
                 'zero':str(lp(initial[:i]+(0,)+initial[i+1:])),
                 'one':str(lp(initial[:i]+(1,)+initial[i+1:]))}
                for i in range(m)]}


def main():
    split_checks = 0
    for N in (4,8,16,32):
        witnesses = [(F(N*j)+F(1,2),F(j)) for j in range(N+1)]
        M = N-2
        for a,b in product(range(-M,M+1), repeat=2):
            if (a,b) == (0,0):
                continue
            values = [a*x+b*y for x,y in witnesses]
            # Values in one open unit gap can remove at most one witness.
            bins = {}
            for v in values:
                if v.denominator != 1:
                    floor = v.numerator//v.denominator
                    bins[floor] = bins.get(floor,0)+1
            assert all(c <= 1 for c in bins.values())
            split_checks += 1
        normal_values = [x-N*y for x,y in witnesses]
        assert normal_values == [F(1,2)]*(N+1)
    facet_checks = []
    for N in (1,2,5,16):
        z = (F(0),F(1,2))
        normals = [(1,0),(1,-6*N),(1,6*N)]
        values = [a*z[0]+b*z[1] for a,b in normals]
        assert all(v.denominator == 1 for v in values)
        vertices = [(F(0),F(1,3)),(F(N),F(1,2)),(F(0),F(2,3))]
        assert all(F(1,3) <= y <= F(2,3) for x,y in vertices)
        facet_checks.append({'N':N, 'surviving_fractional_point':list(map(str,z)),
                             'primitive_facet_normals':normals,
                             'integer_normal_values':list(map(str,values)),
                             'general_refuting_direction':[0,1]})
    triangle = matching_proof(3,[(0,1),(0,2),(1,2)],1)
    cycle5 = matching_proof(5,[(i,(i+1)%5) for i in range(5)],1)
    bowtie = matching_proof(5,[(0,1),(0,2),(1,2),(0,3),(0,4),(3,4)],1)
    assert triangle['minimum_variable_leaves'] == 2
    assert cycle5['minimum_variable_leaves'] == 2
    assert bowtie['minimum_variable_leaves'] == 3
    assert cycle5['integer_matching_max'] == bowtie['integer_matching_max'] == '2'
    assert cycle5['fractional_matching_max'] == bowtie['fractional_matching_max'] == '5/2'
    enumeration = []
    for N in (4,8,16,32,64):
        checked = 0
        answer = None
        for M in range(1,N+1):
            for a in range(M+1):
                for b in range(-M,M+1):
                    if max(a,abs(b)) != M or gcd(a,b) != 1 or (a == 0 and b != 1):
                        continue
                    checked += 1
                    lo = min(0,N*(a*N+b))+F(a,3)
                    hi = max(0,N*(a*N+b))+F(2*a,3)
                    threshold = lo.numerator//lo.denominator
                    if lo > threshold and hi < threshold+1:
                        answer = (a,b,threshold,M)
                        break
                if answer:
                    break
            if answer:
                break
        assert answer == (1,-N,0,N) and checked >= N-1
        enumeration.append({'N':N,'directions_examined':checked,
                            'first_two_leaf_certificate':answer})
    friends = []
    disjoint = []
    for q in range(1,4):
        edges = [(0,2*i+1) for i in range(q)]+[(0,2*i+2) for i in range(q)]
        edges += [(2*i+1,2*i+2) for i in range(q)]
        row = matching_proof(2*q+1,edges,1)
        assert row['minimum_variable_leaves'] == q+1
        assert row['minimum_possible_depth'] == q
        friends.append(row)
        separate = [(3*i,3*i+1) for i in range(q)]
        separate += [(3*i,3*i+2) for i in range(q)]+[(3*i+1,3*i+2) for i in range(q)]
        loose = matching_proof(3*q,separate,1)
        tight = matching_proof(3*q,separate,q)
        assert loose['minimum_variable_leaves'] == 2
        assert tight['minimum_variable_leaves'] == 2**q
        if q >= 2:
            cutoff = F(2*q+1,2)
            assert all(F(v) >= cutoff for row in tight['root_child_lp']
                       for v in (row['zero'],row['one']))
        disjoint.append({'q':q,'deficiency1':loose,'deficiency_q':tight})
    receipt = {'status':'passed','restricted_normal_checks':split_checks,
               'facet_invariant_checks':facet_checks,
               'unrestricted_direction_enumeration':enumeration,
               'friendship_proofs':friends,'disjoint_triangle_proofs':disjoint,
               'matching_proofs':[triangle,cycle5,bowtie],
               'scope':'Proposed discovery routes fail; Q549 and Q550 remain unresolved.'}
    (HERE/'ROUTE-CHECK-RESULTS.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({'status':'passed','normal_checks':split_checks,
                      'matching_minimum_leaves':[2,2,3],
                      'friendship_leaf_depth':[[r['minimum_variable_leaves'],r['minimum_possible_depth']] for r in friends],
                      'enumeration_counts':[r['directions_examined'] for r in enumeration]}))


if __name__ == '__main__':
    main()
