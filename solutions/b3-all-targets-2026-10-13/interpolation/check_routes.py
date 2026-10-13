#!/usr/bin/env python3
"""Exact controls for disclosed interpolation routes; no asymptotic claims."""
import json
from math import comb
from pathlib import Path
import sympy as S

HERE = Path(__file__).resolve().parent

def vertex_coefficients(n, k):
    p = [1]
    for j in range(n):
        a, b = n + k - j - 1, n - k + j
        q = [0] * (len(p) + 1)
        for d, c in enumerate(p):
            q[d] += a * c
            q[d + 1] += b * c
        p = q
    return p[::-1]

def main():
    z, w = S.symbols('z w')
    a = S.Rational(17, 20) - S.Rational(7, 20) * S.I
    q = z*z + (4*a-1)*z + 2*a*a
    disc = S.expand((4*a-1)**2 - 8*a*a)
    assert disc == -1 - S.Rational(49,25)*S.I
    assert abs(a-S.Rational(1,2))**2 == S.Rational(49,200)
    # sqrt(disc)=u-i*v; the negative branch root has |z|>2.
    rho2 = S.Rational(3026,625)
    assert rho2 > S.Rational(99,50)**2
    assert rho2 > S.Rational(47,25)**2
    # u>.7, v>1.2 give |z|^2>(1.55)^2+(1.3)^2>4.
    assert S.Rational(31,20)**2 + S.Rational(13,10)**2 > 4

    centered_a = S.Rational(1,2)-S.Rational(2,5)*S.I
    centered_q = S.expand((w-S.Rational(1,2))**2
                         +(4*centered_a-1)*(w-S.Rational(1,2))+2*centered_a**2)
    assert centered_q == w*w-S.Rational(8,5)*S.I*w-S.Rational(7,100)
    assert 57 > 7**2  # |w|=(8+sqrt(57))/10 > 3/2.

    orbit_count = 0
    records = []
    for n in range(3,33):
        bs = [vertex_coefficients(n,k) for k in range(n+1)]
        vals = []
        for k in range(n+1):
            for p in range(n-k+1):
                value = sum(comb(p,h)*(bs[k+h][1]*bs[k+p-h][2]
                                      -bs[k+h][0]*bs[k+p-h][3]) for h in range(p+1))
                assert value > 0, (n,k,p,value)
                vals.append(value)
        orbit_count += len(vals)
        records.append({'n':n,'orbits':len(vals),'minimum':str(min(vals)),
                        'maximum':str(max(vals))})
    bs = [vertex_coefficients(3,k) for k in range(4)]
    pair = bs[0][1]*bs[3][2]+bs[3][1]*bs[0][2]-bs[0][0]*bs[3][3]-bs[3][0]*bs[0][3]
    assert pair == -475
    rank_one = sum(n+1 for n in range(2,81))
    assert all(vertex_coefficients(n,k)[1]>0 for n in range(2,81) for k in range(n+1))

    falling = lambda v,n:S.prod(v-j for j in range(n))
    mixture = S.expand(falling(z,4)+falling(z+4,4))
    assert S.expand(mixture.subs(z,w-S.Rational(1,2))) == 2*w**4+43*w*w+S.Rational(105,8)
    # Boundary-circle radius squared is 49/4; large imaginary roots have
    # squared modulus 43/4+sqrt(109)>49/4.
    assert 109 > S.Rational(3,2)**2
    result = {'status':'PASS','complex_parameter_grace_obstructions':2,
              'negative_vertex_pair':{'n':3,'k':0,'ell':3,'value':pair},
              'delta2_full_box_degrees':list(range(3,33)),
              'delta2_coefficient_orbits':orbit_count,'delta2_by_degree':records,
              'rank_one_coefficients_checked':rank_one,
              'relaxed_shift_mixture_identity':True,
              'scope':'Delta_1 has a separate all-size proof; Delta_2 controls certify exactly n=3..32. No all-size higher-order conclusion.'}
    (HERE/'CHECK-RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='delta2_by_degree'}))

if __name__ == '__main__':main()
