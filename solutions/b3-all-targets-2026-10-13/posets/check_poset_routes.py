#!/usr/bin/env python3
"""Actual Boolean and two-chain route controls, with explicit formal relaxations."""
from pathlib import Path
from math import comb
from itertools import combinations
from collections import Counter
from hashlib import sha256
import sympy as sp,json
from poset_tools import h_poly,closure,product2
HERE=Path(__file__).resolve().parent
t=sp.Symbol('t')
def conv(p,q):
    r=[0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):r[i+j]+=a*b
    return r

def scaled_omega(N,h):
    out=[0]*(N+1)
    for j,c in enumerate(h):
        a=[c]
        for s in range(-j,N-j):a=conv(a,[s,1])
        out=[x+y for x,y in zip(out,a)]
    return out

def extensions(N,rel):
    out=Counter()
    def walk(pre,rem):
        if not rem:
            out[tuple(sorted(a+1 for a,b in zip(pre,pre[1:]) if a>b))]+=1;return
        for v in sorted(rem):
            if any(b==v and a in rem for a,b in rel):continue
            walk(pre+(v,),rem-{v})
    walk((),set(range(N)))
    return out

def boolean_rel(n):
    nodes=sorted(range(2**n),key=lambda a:(a.bit_count(),a))
    return {(i,j) for i,a in enumerate(nodes) for j,b in enumerate(nodes) if i<j and a&b==a}

def gamma_h(g,D):
    return [sum(c*comb(D-2*j,i-j) for j,c in enumerate(g) if 0<=i-j<=D-2*j) for i in range(D+1)]

def main():
    source=json.loads((HERE/'BOOLEAN-CHECK.json').read_text())['cases']
    for n in range(5):assert h_poly(2**n,boolean_rel(n))==source[n]['hstar']
    quartic=sp.Poly(2*t**4+12*t**3+25*t**2+21*t+10,t)
    omega=sp.Poly(sum(c*t**i for i,c in enumerate(scaled_omega(8,source[3]['hstar']))),t)
    assert sp.expand(omega.as_expr()-24*t*(t+1)*(t+2)*(t+3)*quartic.as_expr())==0
    assert quartic.count_roots(-sp.oo,sp.oo)==0
    exts=extensions(8,boolean_rel(3));four=[0]*4
    for S,c in exts.items():
        if 6 in S or 7 in S:continue
        c*=(-2)**(5 in S);four[(3 in S)+2*(4 in S)]+=c
    assert four==[-1,-1,3,1] and four[1]*four[2]-four[0]*four[3]==-2
    P={(0,1),(0,2),(0,3)};Q={(0,3),(1,2)}
    hP=h_poly(4,P);hQ=h_poly(4,Q);hp=product2(4,P);hq=product2(4,Q)
    assert hP==hQ==[1,4,1]
    assert hp==[1,27,116,116,27,1] and hq==[1,27,112,112,27,1]
    g=source[4]['gamma'][:];g[2]-=300;g[3]+=1200
    formal=gamma_h(g,11);actual=source[4]['hstar'];gp=sp.Poly(sum(c*t**i for i,c in enumerate(g)),t)
    assert min(g)>0 and formal==formal[::-1] and all(c>0 for c in formal)
    assert formal[:2]==actual[:2] and sum(formal)==sum(actual)
    assert all(formal[i]**2>=formal[i-1]*formal[i+1] for i in range(1,11))
    assert gp.count_roots(-sp.oo,0)==3<gp.degree()==5
    # Actual two-chain posets outside the source's reported chain bound5.
    cases=[];seen=set()
    words=list(combinations(range(12),6))
    for j in range(0,len(words),7):
        A=set(words[j]);B=set(range(12))-A
        chains={(a,b) for S in [A,B] for a,b in combinations(sorted(S),2)}
        for mode in range(3):
            cross={(a,b) for a in range(12) for b in range(a+1,12)
                   if ((a in A)!=(b in A)) and (a*19+b*7+j*11)%(mode+3)==0}
            rel=closure(12,chains|cross);key=tuple(sorted(rel))
            if key in seen:continue
            seen.add(key);h=h_poly(12,rel);om=scaled_omega(12,h)
            assert min(om)>=0
            cases.append({'A_positions':sorted(A),'relations':[list(x) for x in key],
                          'hstar':h,'scaled_ordinary_coefficients':om})
    assert len(cases)>200
    # Weak-layer extension fails to cover an actual chain2 plus isolated element.
    rel={(0,1)};h=h_poly(3,rel);assert h==[1,2]
    assert h not in [[1],[1,1]]
    # Real-rooted descent polynomial alone does not force ordinary positivity.
    star={(0,j) for j in range(1,5)};hs=h_poly(5,star);om=scaled_omega(5,hs)
    assert hs==[1,11,11,1] and om==[0,-4,0,40,60,24]
    assert sp.Poly(sum(c*t**i for i,c in enumerate(hs)),t).count_roots(-sp.oo,0)==3
    # Same rectangle encodes distinct two-chain and cell posets.
    two={(0,1),(2,3)};cell={(0,1),(0,2),(1,3),(2,3)}
    ht=h_poly(4,two);hc=h_poly(4,cell)
    assert ht==[1,4,1] and hc==[1,1]
    ot=scaled_omega(4,ht);oc=scaled_omega(4,hc)
    assert sum(ot)*2**0==24 and sum(oc)==24
    assert sum(c*2**i for i,c in enumerate(ot))==216
    assert sum(c*2**i for i,c in enumerate(oc))==144
    # Actual comparison-order completion has a negative ordinary difference.
    difference=[0,-1,1];assert scaled_omega(2,[1,1])==[0,0,2]
    assert scaled_omega(2,[1])==[0,1,1]
    assert [a-b for a,b in zip(scaled_omega(2,[1,1]),scaled_omega(2,[1]))]==difference
    receipt={'status':'PASS','Boolean_actual_n0_through4_independent_DP':True,
        'Boolean_n3_order_quartic_real_roots':0,'Boolean_n3_Rayleigh_coefficients':four,
        'same_input_hstar':hP,'star_times_C2_hstar':hp,'two_chains_times_C2_hstar':hq,
        'formal_gamma_delta300':g,'formal_hstar_delta300':formal,
        'formal_same_B4_h0_h1_and_mass':True,'formal_hstar_log_concave':True,
        'formal_gamma_negative_real_roots':3,'formal_gamma_degree':5,
        'two_chain_6_by6_cases':cases,'two_chain_6_by6_count':len(cases),
        'actual_chain2_plus_isolated_hstar':h,'outside_width2_star_hstar':hs,
        'outside_width2_star_scaled_omega':om,'rectangle_two_chain_omega':ot,
        'rectangle_cell_omega':oc,'two_point_completion_scaled_difference':difference,
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
        'helper_sha256':sha256((HERE/'poset_tools.py').read_bytes()).hexdigest(),
        'scope':'Exact actual/family controls and labelled sufficient-method obstructions; no full conjecture counterexample.'}
    (HERE/'POSET-ROUTES-CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({k:v for k,v in receipt.items() if k!='two_chain_6_by6_cases'},indent=2))
if __name__=='__main__':main()
