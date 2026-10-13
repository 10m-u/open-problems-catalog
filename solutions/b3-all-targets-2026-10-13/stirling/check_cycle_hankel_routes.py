#!/usr/bin/env python3
"""Exact finite controls for actual cycle-Hankel proof explorations."""
from fractions import Fraction as F
from itertools import permutations
from math import factorial, comb
from pathlib import Path
import hashlib
import json
from check_hankel_tn2 import rows, mul, sub


def pdet(m):
    n=len(m); ans=[0]
    for p in permutations(range(n)):
        term=[1]
        for i in range(n):term=mul(term,m[i][p[i]])
        if sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))%2:term=[-v for v in term]
        ans=sub(ans,[-v for v in term])
    return ans


def run():
    counts=dict(compound_poisson_moment_coefficients=0, shifted_row_formulas=0,
                shifted_triple_coefficient_formulas=0, ratio_lower_bounds=0,
                coefficient_isolation_controls=0)
    # Bell moments with cumulants u*j!/(p+j), integrated over S.
    for r in range(2,13):
        p=r-1
        tab=rows(r,10,'C')
        bell=[[F(1)]]
        for n in range(1,11):
            z=[F(0)]*(n+1)
            for j in range(1,n+1):
                factor=comb(n-1,j-1)*F(factorial(j),p+j)
                for k,v in enumerate(bell[n-j]):z[k+1]+=factor*v
            bell.append(z)
        for n in range(11):
            for k,v in enumerate(bell[n]):
                assert v*F(factorial(n+p*k),factorial(n))==tab[n][k]
                counts['compound_poisson_moment_coefficients']+=1
    invfac=[[F(1,factorial(i+j))] for i in range(3) for j in range(3)]
    assert pdet([[invfac[3*i+j] for j in range(3)] for i in range(3)])==[-F(1,144)]
    assert F(1,2)-1==-F(1,2)
    # Unique third S-fraction at actual r3 in normalized variable.
    alpha=[F(1),F(12),F(24),F(-72),F(216)]
    numerator=[F(1),F(15),F(60)]
    assert mul(alpha[:4],[1,3])[:4]==numerator+[F(0)]
    for r in list(range(2,22))+[32,64,100]:
        a=factorial(r-1)
        table=rows(r,5,'C')
        f=[[F(v,a**k) for k,v in enumerate(z)] for z in table]
        B=F(factorial(2*r),2*factorial(r)**2)
        T=F(factorial(3*r),6*factorial(r)**3)
        U=F(factorial(4*r),24*factorial(r)**4)
        V=F(factorial(5*r),120*factorial(r)**5)
        f5=[0,r*(r+1)*(r+2)*(r+3),
            2*r*r*(2*r+1)*(2*r+2)*(2*r+3)*(F(1,r*(r+3))+F(1,(r+1)*(r+2)))*B,
            3*r*(3*r+1)*(3*r+2)*(F(1,r+2)+F(r,(r+1)**2))*T,
            F(4*r*(4*r+1),r+1)*U,V]
        assert f[5]==f5
        counts['shifted_row_formulas']+=1
        got=pdet([[f[i+j] for j in range(3)] for i in [1,2,3]])
        P=24*r**7+162*r**6+357*r**5+282*r**4+129*r**3+282*r*r+276*r+72
        D=r**8-r**7-48*r**6-134*r**5-135*r**4+71*r**3+330*r*r+276*r+72
        expected=[2*r*r*(r+1),F(4*r**3*(r**3+5*r*r+13*r+11),(r+2)*(r+3))*B,
                  F(r,(r+1)**2*(r+2)**2*(r+3))*(T*P-B*B*D)]
        assert got[3:6]==expected and all(v>0 for v in expected)
        counts['shifted_triple_coefficient_formulas']+=3
        assert T/B**2>=F(5*r,6)
        ratio=F(3*(3*r+1)*(3*r+2),4*(2*r+1)**2)
        assert ratio>=F(r+1,r)
        t=r-2
        assert 5*r*P-6*D == 114*t**8+2640*t**7+26265*t**6+146706*t**5+504135*t**4+1094112*t**3+1467504*t*t+1112112*t+362880
        counts['ratio_lower_bounds']+=2
        assert table[1][2:] == []
        b2=table[2][2]
        assert -b2*b2<0
        counts['coefficient_isolation_controls']+=1
    subset=rows(3,5,'S')
    witness=pdet([[subset[i+j] for j in range(3)] for i in [1,2,3]])
    assert witness==[0,0,0,0,0,-16,19110,938700,15309000,79380000]
    out=dict(schema='b3-cycle-hankel-routes-v1',date='2026-10-13',passed=True,
             counts=counts,subset_scope_control=witness,
             source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             scope='Universal partials rest on written proof; finite controls and route obstructions do not close cycle conjectures.')
    Path(__file__).with_name('CYCLE-HANKEL-CHECK-RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out))


if __name__=='__main__':run()
