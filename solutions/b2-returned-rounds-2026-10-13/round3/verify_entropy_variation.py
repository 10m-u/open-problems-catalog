#!/usr/bin/env python3
"""Exact algebraic controls for the entropy first variation.

The infinite-tail asymptotics are proved in the manuscript, not inferred
from these finite tests. The finite ascent is a rational certificate.
"""
from __future__ import annotations
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json
from rational_entropy import certify, interval_record


def clean(d):
    return {k:v for k,v in d.items() if v and k!=1}


def check_identity(support, weights, target, rho):
    p={x:F(w,sum(weights)) for x,w in zip(support,weights)}
    base=support[0]
    v=defaultdict(F,{target:F(1),base:F(-1)})
    q,r,dq,dr=map(lambda _:defaultdict(F),range(4))
    for x in support:
        for y in support:
            q[x+y]+=p[x]*p[y]
            r[x-y]+=p[x]*p[y]
            dq[x+y]+=v[x]*p[y]+p[x]*v[y]
            dr[x-y]+=v[x]*p[y]+p[x]*v[y]
    assert sum(dq.values())==sum(dr.values())==0
    direct=defaultdict(F)
    for s,w in dr.items(): direct[r[s]]-=w
    for s,w in dq.items(): direct[q[s]]+=rho*w
    for x in support: direct[p[x]]-=(rho-1)*v[x]
    gradient=defaultdict(F)
    for n,sgn in [(target,1),(base,-1)]:
        for j in support:
            gradient[r[n-j]]-=sgn*2*p[j]
            gradient[q[n+j]]+=sgn*2*rho*p[j]
        gradient[p[n]]-=sgn*(rho-1)
    assert clean(direct)==clean(gradient)


def main():
    cases=0
    for m in range(2,8):
        for A in combinations(range(7),m):
            for weights in [list(range(1,m+1)),list(range(m,0,-1)),[7]+[1]*(m-1)]:
                for n in A[1:]:
                    check_identity(A,weights,n,F(7,5))
                    cases+=1
    # This law is a finite exact diagnostic, not an infinite-tail certificate
    # and not a new lower bound for the universal constant.
    weights=[2**(64-n*n) for n in range(9)]
    before=certify('finite_gaussian_diagnostic_before',weights,F(1))
    upper=F(int(before['ratio']['scaled_upper_integer']),int(before['ratio']['decimal_scale']))
    # Move epsilon=10^-12 from zero to six, leaving the support unchanged.
    denominator=10**12
    after_weights=[w*denominator for w in weights]
    after_weights[0]-=sum(weights)
    after_weights[6]+=sum(weights)
    after=certify('finite_gaussian_diagnostic_after',after_weights,upper)
    receipt={
      'status':'passed','arithmetic':'exact fractions and certified rational logarithm intervals',
      'formal_first_variation_identity_checks':cases,
      'infinite_tail_theorem_status':'written proof; not certified by truncation',
      'scope':'Gradient identities and a finite, fixed-support mass-transfer ascent. No new universal entropy bound.',
      'finite_ascent':{'epsilon':'1/1000000000000','from_atom':0,'to_atom':6,'before':before,'after':after},
      'tail_coefficient':{
         'kappa_beta':'min(1, 2**(1-beta))',
         'general':'1 + rho - 2*rho*kappa_beta',
         'gaussian_beta_2':'1',
         'stationary_beta':'log_2(4*rho/(1+rho))'
      }
    }
    path=Path(__file__).with_name('ENTROPY-VARIATION-CHECKS.json')
    path.write_text(json.dumps(receipt,indent=2)+'\n')
    print('Passed',cases,'formal first-variation identities.')
    print('Finite diagnostic ascent:',before['ratio']['lower'],'->',after['ratio']['lower'])
    print('Wrote',path.name)

if __name__=='__main__':
    main()
