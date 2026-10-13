#!/usr/bin/env python3
"""Exact controls for I03--I10; finite checks do not imply all-size closure."""
from hashlib import sha256
import json
from pathlib import Path
from flint import fmpz_mat
import sympy as S

HERE = Path(__file__).resolve().parent

def vertex(n,k):
    p=[1]
    for j in range(n):
        a,b=n+k-j-1,n-k+j
        q=[0]*(len(p)+1)
        for i,c in enumerate(p):q[i]+=a*c;q[i+1]+=b*c
        p=q
    return p[::-1]

def hurwitz(b,r):
    entry=lambda i:b[i] if 0<=i<len(b) else 0
    return fmpz_mat([[entry(2*j-i+1) for j in range(r)]
                    for i in range(r)])

def main():
    z,t,u,x=S.symbols('z t u x')
    # I04: exact append, both root radii, and actual Hurwitz defect.
    old=(z+S.Rational(7,4))**2
    cs=[S.Rational(49,16),S.Rational(9,2),S.Integer(2)]
    binomial=lambda j:S.prod(z-k for k in range(j))/S.factorial(j)
    assert S.expand(sum(c*binomial(j) for j,c in enumerate(cs))-old)==0
    new=S.expand(sum(c*(binomial(j+1)+binomial(j))
                     for j,c in enumerate(cs)))
    assert S.expand(new-(z+1)*(z*z/3+S.Rational(23,12)*z+S.Rational(49,16)))==0
    assert S.expand(new.subs(z,z+1)-new-old-(old.subs(z,z+1)-old))==0
    assert new.subs(z,0)==old.subs(z,0)
    oldF=S.cancel((1-t)**2*old.subs(z,-S.Rational(1,2)+S.Rational(3,2)*(1+t)/(1-t)))
    assert S.expand(oldF-(t+11)**2/16)==0
    newF=S.Poly(S.cancel((1-t)**3*new.subs(z,-S.Rational(1,2)+S.Rational(5,2)*(1+t)/(1-t))),t)
    b=newF.all_coeffs()
    assert b==[S.Rational(5,8),S.Rational(25,48),S.Rational(95,6),S.Rational(395,16)]
    assert b[1]*b[2]-b[0]*b[3]==-S.Rational(8275,1152)
    assert S.Rational(147,16)>9 and S.Rational(105,16)>S.Rational(25,4)
    assert cs[1]**2-4*cs[0]*cs[2]<0

    # I05 actual row: coefficient Toeplitz certificate fails.
    actual=[vertex(2,k) for k in range(3)]
    row=[sum([1,2,1][k]*actual[k][j] for k in range(3)) for j in range(3)]
    assert row==[10,16,10]
    toeplitz=fmpz_mat([[16,10,0,0],[10,16,10,0],[0,10,16,10],[0,0,10,16]])
    assert int(toeplitz.det())==-1264

    # I06 strict LC and first two positive Hurwitz minors are insufficient.
    coefficients=[10,11,12,13,12,11,10]
    assert all(coefficients[i]**2>coefficients[i-1]*coefficients[i+1]
               for i in range(1,6))
    defects=[int(hurwitz(coefficients,r).det()) for r in range(1,4)]
    assert defects==[11,2,-216]

    # I07 positive multi-affine entries and numerical stability lack coefficient positivity.
    bb=[2,4+2*x,2+2*x,1+10*x]
    delta2=S.expand(bb[1]*bb[2]-bb[0]*bb[3])
    assert delta2==4*x*x-8*x+6
    assert S.expand(delta2-(4*(x-1)**2+2))==0
    matrix=S.Matrix(3,3,lambda i,j:bb[2*j-i+1] if 0<=2*j-i+1<4 else 0)
    assert S.expand(matrix.det()-bb[3]*delta2)==0

    # I08 concrete Newton companion, whose eigenvalues remain correct.
    C=S.Matrix([[0,-2],[1,-3]])
    assert C.charpoly(z).as_expr()==S.expand((z+1)*(z+2))
    assert abs(C[1,1])>2 and abs(C[1,1]+S.Rational(1,2))>S.Rational(3,2)
    for n in range(2,101):
        assert n*n-n+1>n and n*n-n+S.Rational(1,2)>n-S.Rational(1,2)

    # I09 full-support LC shift-law counterexample with exact IVT exterior root.
    w=S.symbols('w');n=6
    uniform=S.expand(S.prod(w+S.Rational(2*j+1,2) for j in range(n+1))-
                     S.prod(w-S.Rational(2*j+1,2) for j in range(n+1)))
    expected=49*w**6+S.Rational(10045,4)*w**4+S.Rational(177331,16)*w*w+S.Rational(135135,64)
    assert uniform==expected
    g=-49*u**3+S.Rational(10045,4)*u*u-S.Rational(177331,16)*u+S.Rational(135135,64)
    assert g.subs(u,36)==S.Rational(36579375,64)>0
    assert g.subs(u,49)==-S.Rational(17680285,64)<0
    sampled=S.expand(sum(S.prod(z+k-j for j in range(n)) for k in range(n+1)))
    assert S.expand(7*sampled.subs(z,w-S.Rational(1,2))-uniform)==0

    # I10 actual termwise Rouché failure.
    exterior=-S.Rational(5,2)
    lead=binomial(2).subs(z,exterior)
    assert abs(lead)==S.Rational(35,8)<1+abs(2*exterior)==6
    assert 1+2*exterior+lead==S.Rational(3,8)

    # I03 exact integer determinants and staircase reindexing at all bounded corners.
    corner_checks=endpoint_checks=0
    for n in range(2,13):
        for k in range(n+1):
            v=vertex(n,k)
            for r in range(1,n):
                matrix=hurwitz(v,r)
                determinant=int(matrix.det())
                assert determinant>0
                entry=lambda i:v[i] if 0<=i<len(v) else 0
                # Dual Jacobi--Trudi at staircase, with each e_i scaled by B.
                schur=fmpz_mat([[entry(r-2*i+j) for j in range(r)] for i in range(r)])
                assert determinant==int(schur.det())
                if k==n:
                    small=int(hurwitz(v[1:],r-1).det()) if r>1 else 1
                    assert determinant==v[1]*small
                    endpoint_checks+=1
                corner_checks+=1

    files=['ATTEMPTS.md','HURWITZ-CORNERS.md','check_completions.py']
    receipt={'status':'PASS','all_order_corner_determinants_checked':corner_checks,
             'corner_degrees':list(range(2,13)),'zero_leading_endpoint_expansions':endpoint_checks,
             'append_control_hurwitz_delta2':'-8275/1152',
             'actual_toeplitz_minor':-1264,'strict_LC_control_hurwitz':defects,
             'numeric_stability_negative_coefficient_control':'4x^2-8x+6',
             'uniform_LC_shift_law_exterior_signs':['36579375/64','-17680285/64'],
             'exact_disk_and_rouche_controls':True,
             'files_sha256':{f:sha256((HERE/f).read_bytes()).hexdigest() for f in files},
             'scope':'Exact finite controls support written proof routes and obstructions. Only the separate corner theorem is asserted for all n/r; the three full targets remain unresolved.'}
    (HERE/'COMPLETION-CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))

if __name__=='__main__':main()
