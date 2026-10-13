#!/usr/bin/env python3
"""Exact Laurent-support and coefficient controls; no link enumeration."""
from collections import Counter
from itertools import product
from pathlib import Path
from hashlib import sha256
from math import factorial
from fractions import Fraction
import json
HERE=Path(__file__).resolve().parent
def shift(a,i,j):
    return tuple(v+int(k==i)-int(k==j) for k,v in enumerate(a))
def m_failure(P):
    S=set(P)
    for a in sorted(S):
        for b in sorted(S):
            for i in range(4):
                if a[i]<=b[i]:continue
                choices=[j for j in range(4) if a[j]<b[j]]
                if not any(shift(a,j,i) in S and shift(b,i,j) in S for j in choices):
                    return {'alpha':a,'beta':b,'i':i+1,'candidate_j':[j+1 for j in choices]}
def lc_failure(P):
    centers=set(P)
    for a in P:
        for i in range(4):
            for j in range(4):centers.add(shift(a,i,j))
    for a in sorted(centers):
        for i in range(4):
            for j in range(4):
                if i==j:continue
                cp=P.get(shift(a,i,j),0);cm=P.get(shift(a,j,i),0);c=P.get(a,0)
                if c*c<cp*cm:return {'alpha':a,'i':i+1,'j':j+1,'center':c,'plus':cp,'minus':cm}
def multiply(P,Q):
    out=Counter()
    for a,c in P.items():
        for b,d in Q.items():out[tuple(x+y for x,y in zip(a,b))]+=c*d
    return out
def main():
    cycles=[]
    for n in range(3,13):
        r=n-1;P={(-k,-(r-k),0,0):1 for k in range(n)}
        assert not m_failure(P) and not lc_failure(P)
        edges=set(range(n));T={k:edges-{k} for k in range(n)}
        for k in range(1,r):
            common=T[k-1]&T[k+1]
            assert k in common and not common<=T[k]
        assert not (T[0]&T[r])<=T[1]
        cycles.append({'n':n,'trees':len(P),'midpoint_pair_obstructions':r-1})
    relaxed={(-1,0,1,0):1,(0,-1,0,1):1}
    assert m_failure(relaxed)
    actual41={a:1 for a in ((0,0,0,0),(-1,0,1,0),(0,-1,1,0),(-1,0,0,1),(0,-1,0,1))}
    assert not m_failure(actual41) and not lc_failure(actual41)
    actual810=Counter()
    for a,b in ((-2,0),(-1,-1),(0,-2)):
        for z in range(5):actual810[a,b,z,4-z]+=1
    for a,b in ((-1,0),(0,-1)):
        for z,c in enumerate((1,2,2,1)):actual810[a,b,z,3-z]+=c
    assert len(actual810)==23 and sum(actual810.values())==27
    assert not m_failure(actual810) and not lc_failure(actual810)
    F={tuple(v+(2 if k<2 else 0) for k,v in enumerate(a)):c for a,c in actual810.items()}
    derivative={}
    lam=(0,2,0,2)
    for a,c in F.items():
        if any(v<l for v,l in zip(a,lam)):continue
        normalized=Fraction(c,1)
        for v in a:normalized/=factorial(v)
        for v,l in zip(a,lam):normalized*=factorial(v)//factorial(v-l)
        derivative[tuple(v-l for v,l in zip(a,lam))]=normalized
    assert derivative=={(1,0,1,0):Fraction(2),(1,0,0,1):Fraction(1),
                        (0,0,2,0):Fraction(1,2),(0,0,1,1):Fraction(1),(0,0,0,2):Fraction(1,2)}
    H=[[0,2,1],[2,1,1],[1,1,1]]
    determinant=H[0][0]*(H[1][1]*H[2][2]-H[1][2]*H[2][1])-H[0][1]*(H[1][0]*H[2][2]-H[1][2]*H[2][0])+H[0][2]*(H[1][0]*H[2][1]-H[1][1]*H[2][0])
    assert determinant==-1 and sum(H[i][i] for i in range(3))==2
    fake=Counter({(0,0,0,0):1})
    for u,v in product(range(3),repeat=2):
        c=((4,5,4),(5,4,5),(4,5,4))[u][v]
        fake[-u,-(2-u),v,2-v]=c
    assert m_failure(fake) and lc_failure(fake)
    def specialize(P,powers):
        out=Counter()
        for a,c in P.items():out[sum(v*p for v,p in zip(a,powers))]+=c
        return dict(sorted(out.items()))
    marginal1=specialize(fake,(-1,1,0,0));marginal2=specialize(fake,(0,0,-1,1))
    unsigned=specialize(fake,(-1,1,-1,1))
    assert marginal1==marginal2=={-2:13,0:15,2:13}
    assert unsigned=={-4:4,-2:10,0:13,2:10,4:4}
    assert sum(c*(-1)**(a[1]+a[3]) for a,c in fake.items())==1
    center=(-1,-1,1,1)
    assert fake[center]**2==16<fake[shift(center,2,3)]*fake[shift(center,3,2)]==25
    assert fake[(-1,0,1,0)]==0 and fake[(-2,0,2,0)]==4
    # Counter lookup above inserts a zero; exclude it from the support receipt.
    fake=+fake
    branch_sum={(-2,0,0,0):1,(0,-2,0,0):1}
    assert m_failure(branch_sum) and lc_failure(branch_sum)
    for n in range(3,13):
        contracted={(-k-1,-(n-2-k),0,0):1 for k in range(n-1)}
        contracted[(0,-(n-1),0,0)]=1
        assert contracted=={(-k,-(n-1-k),0,0):1 for k in range(n)}
    S=((0,0,0,0),(-1,0,1,0),(0,-1,1,0),(-1,-1,2,0))
    A=dict(zip(S,(4,1,1,4)));B=dict(zip(S,(1,4,4,1)))
    assert not m_failure(A) and not m_failure(B) and not lc_failure(A) and not lc_failure(B)
    C=multiply(A,B);alpha=(-1,-1,2,0)
    assert len(C)==9 and not m_failure(C) and lc_failure(C)
    assert [C[alpha],C[shift(alpha,0,2)],C[shift(alpha,2,0)]]==[16,17,17]
    cycle_products=0
    profiles=((),(2,),(3,),(4,),(2,3),(3,4))
    for positives,mirrors in product(profiles,repeat=2):
        P={(0,0,0,0):1}
        for n in positives:P=multiply(P,{(-k,-(n-1-k),0,0):1 for k in range(n)})
        for n in mirrors:P=multiply(P,{(0,0,k,n-1-k):1 for k in range(n)})
        assert not m_failure(P) and not lc_failure(P)
        cycle_products+=1
    receipt={'status':'PASS','cycle_controls':cycles,
        'relaxed_matching_M_exchange_failure':m_failure(relaxed),
        'actual_source_figure_eight_terms':len(actual41),
        'actual_source_810_terms':len(actual810),'actual_source_810_mass':sum(actual810.values()),
        'normalized_810_derivative':{' '.join(map(str,a)):str(c) for a,c in derivative.items()},
        'normalized_810_Hessian':H,'Hessian_determinant':determinant,'Hessian_positive_eigenvalues':2,
        'relaxed_marginal_polynomial_terms':len(fake),'relaxed_marginal_M_failure':m_failure(fake),
        'relaxed_filled_slice_LC_values':[4,5,5],
        'relaxed_source_marginals':marginal1,'relaxed_unsigned_Alexander':unsigned,
        'scalar_branch_union_M_failure':m_failure(branch_sum),
        'scalar_branch_sum_LC_failure':lc_failure(branch_sum),
        'weak_LC_product_inputs_support_size':4,'weak_LC_product_output_support_size':len(C),
        'weak_LC_product_failure_values':[16,17,17],'cycle_product_controls':cycle_products,
        'scope':'Exact named actual cycle family and attributed actual P41; relaxed matching is not a link counterexample.',
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (HERE/'BONINGER-CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))
if __name__=='__main__':main()
