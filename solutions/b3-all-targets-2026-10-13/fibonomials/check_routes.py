#!/usr/bin/env python3
"""Fresh finite construction and exact q-Fibonomial method obstructions."""
from pathlib import Path
from hashlib import sha256
from itertools import combinations
import runpy,json
HERE=Path(__file__).resolve().parent
r=runpy.run_path(str(HERE/'check_fibonomials.py'))
F=r['F'];uniform=r['uniform']
def shifted_uniform(a,length,stride):
    out=[0]*(len(a)+stride*(length-1))
    for k in range(length):
        for i,c in enumerate(a):out[i+k*stride]+=c
    return out
def unimodal(a):
    fall=False
    for x,y in zip(a,a[1:]):
        if y<x:fall=True
        if fall and y>x:return False
    return True
def main():
    fresh=[]
    for total in range(21,25):
        for n in range(5,(total+1)//2):
            m=total-n
            if m==n:continue
            a=r['fibonomial'](m,n)
            assert r['unimodal'](a) and min(a)>0
            fresh.append({'m':m,'n':n,'degree':len(a)-1,
                          'mass':sum(a),'central_coefficient':a[len(a)//2]})
    demand=[4,6,8,9,10];supply=list(range(11,21))
    neighbors={i:[j for j in supply if F[j]%F[i]==0] for i in demand}
    union=sorted(set().union(*(set(v) for v in neighbors.values())))
    assert union==[12,16,18,20] and len(union)<len(demand)
    # A and B have the actual degree, total mass, constant/leading
    # coefficient and symmetric unimodality of B_(3,2)=B_(2,3).
    synthetic=[1,1,1,9,1,1,1]
    actual=r['fibonomial'](3,2)
    assert sum(synthetic)==sum(actual)==15
    assert synthetic==synthetic[::-1] and unimodal(synthetic)
    out=shifted_uniform(synthetic,F[4],F[3])
    out+=[0]*max(0,6+len(synthetic)-len(out))
    for i,v in enumerate(synthetic):out[i+6]+=v
    assert out==[1,1,2,10,3,11,4,11,3,10,2,1,1]
    assert out==out[::-1] and not unimodal(out)
    # Actual path N N E E N on a 2x3 rectangle: two forced
    # vertical dominoes have q-weights q and q^2; the top row
    # has two monominoes or one horizontal domino of weight q^2.
    fiber=[0,0,0,1,0,1]
    assert not unimodal(fiber)
    assert r['unimodal'](r['fibonomial'](2,3))
    result={'status':'PASS','fresh_asymmetric_cases':fresh,
       'fresh_count':len(fresh),'fresh_actual_counterexample':None,
       'whole_q_integer_divisor_Hall_obstruction':{'m':10,'n':10,
                'demand_indices':demand,'neighbors':neighbors,'union':union},
       'constrained_recursion_obstruction':{'synthetic_predecessors':synthetic,
                'actual_predecessor':actual,'output':out},
       'actual_fixed_path_obstruction':{'m':2,'n':3,'path':'NNEEN',
                'forced_vertical_weights':[1,2],'optional_horizontal_weight':2,
                'polynomial':fiber},
       'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
       'scope':'Finite actual construction and distinct sufficient-method failures; not a counterexample to Q2751.'}
    (HERE/'ROUTE-CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='fresh_asymmetric_cases'},indent=2))
if __name__=='__main__':main()
