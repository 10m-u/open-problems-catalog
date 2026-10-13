#!/usr/bin/env python3
"""Independent poset review via multichains of ideals and Newton differences."""
from pathlib import Path
from math import comb, factorial
from itertools import combinations, permutations
from collections import Counter
from hashlib import sha256
import json
from check_poset_review import sturm_negative, conv
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent/'posets'

def ideal(mask,rel):return all(not(mask>>b&1) or mask>>a&1 for a,b in rel)
def maps_and_polys(N,rel,ideals=None):
    if ideals is None:ideals=[s for s in range(1<<N) if ideal(s,rel)]
    ideals=sorted(ideals);end=ideals.index((1<<N)-1)
    predecessors=[[i for i,I in enumerate(ideals) if I&J==I] for J in ideals]
    cur=[0]*len(ideals);cur[ideals.index(0)]=1;vals=[int(N==0)]
    for k in range(N+1):
        cur=[sum(cur[i] for i in pre) for pre in predecessors];vals.append(cur[end])
    h=[sum((-1)**j*comb(N+1,j)*vals[i-j+1] for j in range(i+1)) for i in range(N+1)]
    while len(h)>1 and not h[-1]:h.pop()
    ordinary=[0]*(N+1);falling=[1]
    for k in range(N+1):
        difference=sum((-1)**(k-j)*comb(k,j)*vals[j] for j in range(k+1))
        scale=difference*factorial(N)//factorial(k)
        for i,c in enumerate(falling):ordinary[i]+=scale*c
        falling=conv(falling,[-k,1])
    return vals,h,ordinary

def brute_extensions(N,rel):
    out=Counter()
    for p in permutations(range(N)):
        pos=[p.index(j) for j in range(N)]
        if all(pos[a]<pos[b] for a,b in rel):
            out[tuple(sorted(a+1 for a,b in zip(p,p[1:]) if a>b))]+=1
    return out

def main():
    receipt=json.loads((ROOT/'POSET-ROUTES-CHECK.json').read_text())
    source=json.loads((ROOT/'BOOLEAN-CHECK.json').read_text())['cases']
    boolean=[]
    for n in range(5):
        nodes=sorted(range(2**n),key=lambda a:(a.bit_count(),a));N=len(nodes)
        rel={(i,j) for i,a in enumerate(nodes) for j,b in enumerate(nodes) if a!=b and a&b==a}
        vals,h,ordinary=maps_and_polys(N,rel)
        assert h==source[n]['hstar']
        boolean.append({'n':n,'ideal_multichain_hstar_agrees':True,'Omega2':vals[2]})
        if n==3:
            exts=brute_extensions(N,rel);four=[0]*4
            for S,c in exts.items():
                if 6 in S or 7 in S:continue
                four[(3 in S)+2*(4 in S)]+=c*(-2)**(5 in S)
            assert four==[-1,-1,3,1]
            quartic=[10,21,25,12,2]
            factor=[1]
            for k in range(4):factor=conv(factor,[k,1])
            assert [24*c for c in conv(factor,quartic)]==ordinary
            assert sturm_negative(quartic)==0
    gamma_checks=[]
    for case in source:
        g=case['gamma'];roots=sturm_negative(g)
        assert roots==len(g)-1==case['negative_gamma_roots']
        D=len(case['hstar'])-1
        h=[sum(c*comb(D-2*j,i-j) for j,c in enumerate(g) if 0<=i-j<=D-2*j) for i in range(D+1)]
        assert h==case['hstar']
        gamma_checks.append({'n':case['n'],'negative_gamma_roots':roots})
    P={(0,1),(0,2),(0,3)};Q={(0,3),(1,2)}
    outputs=[]
    for rel,expected in [(P,[1,27,116,116,27,1]),(Q,[1,27,112,112,27,1])]:
        assert maps_and_polys(4,rel)[1]==[1,4,1]
        prod=rel|{(4+a,4+b) for a,b in rel}|{(i,4+i) for i in range(4)}
        h=maps_and_polys(8,prod)[1];assert h==expected;outputs.append(h)
    g=receipt['formal_gamma_delta300'];h=receipt['formal_hstar_delta300']
    assert g==[1,140,3246,25412,43648,14400] and sturm_negative(g)==3
    assert h==h[::-1] and all(c>0 for c in h)
    assert all(h[j]**2>=h[j-1]*h[j+1] for j in range(1,len(h)-1))
    assert h[:2]==source[4]['hstar'][:2] and sum(h)==sum(source[4]['hstar'])
    keys=set();case_checks=0;minimum=0
    for case in receipt['two_chain_6_by6_cases']:
        rel=set(map(tuple,case['relations']));key=tuple(sorted(rel));assert key not in keys;keys.add(key)
        A=case['A_positions'];B=sorted(set(range(12))-set(A))
        assert len(A)==len(B)==6 and all(a<b for a,b in rel)
        assert all((a,b) in rel for S in (A,B) for a,b in combinations(S,2))
        masks=set()
        for a in range(7):
            for b in range(7):
                mask=sum(1<<i for i in A[:a]+B[:b])
                if ideal(mask,rel):masks.add(mask)
        vals,hh,ordinary=maps_and_polys(12,rel,sorted(masks))
        assert hh==case['hstar'] and ordinary==case['scaled_ordinary_coefficients'] and min(ordinary)>=0
        case_checks+=1
    assert case_checks==394
    rel={(0,1)};v,hh,om=maps_and_polys(3,rel)
    assert hh==[1,2] and om==[0,0,3,3]
    star={(0,j) for j in range(1,5)};_,hh,om=maps_and_polys(5,star)
    assert hh==[1,11,11,1] and om==[0,-4,0,40,60,24]
    rectangle=[]
    for rel,expected in [({(0,1),(2,3)},[0,0,6,12,6]),
                         ({(0,1),(0,2),(1,3),(2,3)},[0,4,10,8,2])]:
        v,hh,om=maps_and_polys(4,rel);assert om==expected;rectangle.append(v[2])
    assert rectangle==[9,6]
    anti=maps_and_polys(2,set())[2];chain=maps_and_polys(2,{(0,1)})[2]
    assert [a-b for a,b in zip(anti,chain)]==[0,-1,1]
    result={'status':'PASS','independent_Boolean_ideal_multichains':boolean,
        'independent_Boolean_gamma_Sturm':gamma_checks,'actual_B3_brute_refinement':four,
        'actual_same_input_doubling_outputs':outputs,'formal_gamma_negative_roots':3,
        'two_chain_cases_independent_ideal_multichain_and_Newton_reconstruction':case_checks,
        'rectangle_weak_maps_at2':rectangle,'counts_accepted':{'Q3500':5,'Q3568':5},
        'scope':'Independent exact scope/contract review; neither full conjecture is resolved.',
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (HERE/'POSET-ROUTE-REVIEW-CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
