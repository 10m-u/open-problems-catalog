#!/usr/bin/env python3
"""Exact controls for the reconstructed E1/E2/E3 arguments."""
from functools import lru_cache
from itertools import combinations, product
from math import isqrt, prod
from pathlib import Path
import json


@lru_cache(None)
def refined(vector):
    state = {(0, 0): 1}
    previous = 1
    for denominator in vector:
        new = {}
        for (last, degree), count in state.items():
            for numerator in range(denominator):
                key = (numerator, degree + (last*denominator < numerator*previous))
                new[key] = new.get(key, 0) + count
        state = new
        previous = denominator
    coefficients = [0]*(len(vector)+1)
    for (_, degree), count in state.items():
        coefficients[degree] += count
    while len(coefficients)>1 and coefficients[-1] == 0:
        coefficients.pop()
    return tuple(coefficients)


def literal(vector):
    coefficients = [0]*(len(vector)+1)
    for word in product(*(range(n) for n in vector)):
        numerator, denominator, rank = 0, 1, 0
        for k, s in zip(word, vector):
            rank += numerator*s < k*denominator
            numerator, denominator = k, s
        coefficients[rank] += 1
    while len(coefficients)>1 and coefficients[-1] == 0:
        coefficients.pop()
    return tuple(coefficients)


@lru_cache(None)
def ordered_factorizations(n):
    if n == 1:
        return ((),)
    result = [(n,)]
    for first in range(2, n):
        if n % first == 0:
            result.extend((first,)+tail for tail in ordered_factorizations(n//first))
    return tuple(result)


def canonical_vectors(n):
    for factors in ordered_factorizations(n):
        for separators in product((False, True), repeat=max(0,len(factors)-1)):
            vector = []
            for i, factor in enumerate(factors):
                if i and separators[i-1]:
                    vector.append(1)
                vector.append(factor)
            yield tuple(vector)


def run():
    exact = 0
    for length in range(1, 5):
        for vector in product(range(1,6), repeat=length):
            assert refined(vector) == literal(vector), vector
            assert sum(refined(vector)) == prod(vector)
            exact += 1
    contractions = []
    for degree in range(1, 13):
        old = (2,)*(2*degree)
        new = (2,)*(2*degree-2)+(4,)
        assert refined(old) == refined(new)
        assert len(refined(old))-1 == degree
        contractions.append({'degree':degree,'old':list(old),'new':list(new)})
    triple_count = 0
    for a,b,c in product(range(2,13),repeat=3):
        polynomial = refined((a,b,c))
        assert polynomial == refined((c,b,a)), 'Reversal'
        exact_chain = any(b < a*j and c*j < b*(c-1) for j in range(1,b))
        assert (len(polynomial)==4) == exact_chain, (a,b,c)
        if len(polynomial)==3:
            assert polynomial[1]>polynomial[2]>0
            aa,cc = min(a,c),max(a,c)
            expected = ((aa==2 and (b==2 or cc==2 or (b,cc) in [(3,3),(4,3),(4,4),(6,3)]))
                        or (aa,b,cc)==(3,3,3))
            assert expected,(a,b,c)
        triple_count += 1
    exceptions = {(2,3,3):(1,10,7), (2,4,3):(1,12,11),
                  (2,4,4):(1,18,13), (2,6,3):(1,19,16), (3,3,3):(1,16,10)}
    for vector, expected in exceptions.items():
        assert literal(vector) == refined(vector) == expected
    for parameter in range(2,101):
        assert refined((2,2,parameter)) == (1,parameter+2*(parameter//2)+2,3*parameter-2*(parameter//2)-3)
        expected = (1,2*parameter,2*parameter-1) if parameter%2 else (1,2*parameter+2,2*parameter-3)
        assert refined((2,parameter,2))==expected
    multiset_controls = 0
    for b in range(1,13):
        coefficients = [0]*3
        for positions in combinations(range(b+2),2):
            word = [2]*(b+2)
            for position in positions:
                word[position]=1
            rank=sum(word[i]>word[i+1] for i in range(len(word)-1))
            coefficients[rank]+=1
        assert coefficients==[1,2*b,b*(b-1)//2]
        multiset_controls+=1
    recognition=[]
    for b in range(1,21):
        polynomial = (1,2*b,b*(b-1)//2) if b>1 else (1,2)
        volume=(b+1)*(b+2)//2
        candidates=list(canonical_vectors(volume))
        witnesses=[v for v in candidates if refined(v)==polynomial]
        triangular=b*(b+1)//2
        expected=b==2 or isqrt(triangular)**2==triangular
        assert bool(witnesses)==expected,b
        assert not witnesses or min(map(len,witnesses))<=2*(len(polynomial)-1)-1
        recognition.append({'b':b,'volume':volume,'canonical_candidate_count':len(candidates),
                            's_eulerian':expected,'witness':list(min(witnesses,key=len)) if witnesses else None})
    result={'status':'PASS','literal_vs_refined_vectors':exact,
            'all_two_contractions':contractions,'triple_degree_controls':triple_count,
            'infinite_family_formula_controls':198,'literal_multiset_controls':multiset_controls,
            'exceptional_triple_coefficients': {str(k):list(v) for k,v in exceptions.items()},
            'arbitrary_length_volume_recognition_b1_to20':recognition,
            'scope':'Finite controls for independently written E1/E2/E3 proofs; no full coloured Q1262 classification.'}
    return result


if __name__=='__main__':
    result=run()
    path=Path(__file__).with_name('eulerian_checks.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['all_two_contractions','arbitrary_length_volume_recognition_b1_to20']},indent=2))
