#!/usr/bin/env python3
"""Exact height DP and independent ceiling-matrix controls."""
from collections import defaultdict
from math import comb, factorial
from pathlib import Path
import json
import sympy as S

HERE=Path(__file__).resolve().parent

def distributions(length,horizontal=False,riordan=False,up_weights=None):
    state={(0,0):1};out={0:[1]}
    for step in range(1,length+1):
        nxt=defaultdict(int)
        for (h,m),c in state.items():
            nxt[(h+1,max(m,h+1))]+=c*(up_weights[h] if up_weights and h<len(up_weights) else 1)
            if h:nxt[(h-1,m)]+=c
            if horizontal and (h or not riordan):nxt[(h,m)]+=c
        state=nxt
        heights=[state.get((0,m),0) for m in range(step//2+1)]
        out[step]=heights
    return out

def ceiling_count(length,cap,horizontal=False,riordan=False):
    v=[1]+[0]*cap
    for _ in range(length):
        q=[0]*(cap+1)
        for h,c in enumerate(v):
            if h<cap:q[h+1]+=c
            if h:q[h-1]+=c
            if horizontal and (h or not riordan):q[h]+=c
        v=q
    return v[0]

def lc(c):return all(c[i]**2>=c[i-1]*c[i+1] for i in range(1,len(c)-1))
def ulc(c):
    d=len(c)-1
    return all(i*(d-i)*c[i]**2 >= (i+1)*(d-i+1)*c[i-1]*c[i+1] for i in range(1,d))

def max_join(a,b,shift=0):
    out=[0]*(max(len(a)+shift,len(b)))
    for i,ai in enumerate(a):
        for j,bj in enumerate(b):out[max(i+shift,j)]+=ai*bj
    return out

def add_arrays(a,b):
    return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
            for i in range(max(len(a),len(b)))]

def grouped(H,n,kind):
    d=(n+1)//2;h=H[2*n] if kind=='A' else H[2*(n-1)]
    get=lambda k:h[k] if 0<=k<len(h) else 0
    return [0]+[get(2*i-1)+get(2*i) if kind=='A' else get(2*i-2)+get(2*i-1) for i in range(1,d+1)]

def tail_formula(n,i,kind):
    if kind=='A':
        return 4*(2*i+1)*(8*i*(i+1)-3*(n+1))*factorial(2*n+1)//(factorial(n-2*i+1)*factorial(n+2*i+3))
    return 8*i*(8*i*i*(2*n-1)-(6*n*n+n-2))*factorial(2*n-2)//(factorial(n-2*i+1)*factorial(n+2*i+1))

def main():
    H=distributions(200);M=distributions(100,True);R=distributions(100,True,True)
    assertions=0
    for n in range(0,101):
        assert sum(H[2*n])==comb(2*n,n)//(n+1)
        for kind in ['A','B'] if n else []:
            c=grouped(H,n,kind);assert ulc(c),(n,kind,c)
            threshold=(n+5)//4 if kind=='A' else (n+2)//4+1
            for i in range(threshold,len(c)):
                assert c[i]==tail_formula(n,i,kind),(n,i,kind)
                assertions+=1
        assert lc([0]+M[n]) and lc([0]+R[n]),n
    for length in range(0,17):
        for cap in range(length//2+1):
            for D,horiz,riord in [(H,False,False),(M,True,False),(R,True,True)]:
                assert sum(D[length][:cap+1])==ceiling_count(length,cap,horiz,riord)
    t=S.symbols('t');witnesses=[]
    for name,c in [('A17',grouped(H,17,'A')),('B16',grouped(H,16,'B')),
                   ('M11',[0]+M[11]),('R12',[0]+R[12])]:
        first=next(i for i,v in enumerate(c) if v)
        p=S.Poly(sum(v*t**(i-first) for i,v in enumerate(c) if v),t)
        real_count=p.count_roots(-S.oo,S.oo)
        assert real_count < p.degree()
        witnesses.append({'family':name,'coefficients':c,'nonzero_degree':p.degree(),'real_roots':int(real_count)})
    strong=[]
    for name,D in [('M',M),('R',R)]:
        first=next(n for n in range(101) if not ulc([0]+D[n]))
        strong.append({'family':name,'first_ULC_failure_length':first,'counts':[0]+D[first]})
    assert not ulc(H[14])
    first_return_controls=0
    for n in range(1,17):
        c=[]
        for j in range(n):c=add_arrays(c,max_join(H[2*j],H[2*(n-1-j)],1))
        assert c==H[2*n]
        first_return_controls+=1
    for length in range(1,13):
        cm=M[length-1][:];cr=[]
        for j in range(length-1):
            cm=add_arrays(cm,max_join(M[j],M[length-2-j],1))
            cr=add_arrays(cr,max_join(M[j],R[length-2-j],1))
        while len(cm)<len(M[length]):cm.append(0)
        while len(cr)<len(R[length]):cr.append(0)
        assert cm==M[length] and cr==R[length]
        first_return_controls+=2
    lc_f,lc_g=[1,1,1,0],[0,0,1,2]
    ulc_f,ulc_g=[1,2,1,0],[0,0,1,3]
    assert lc(lc_f) and lc(lc_g) and not lc(add_arrays(lc_f,lc_g))
    assert ulc(ulc_f) and ulc(ulc_g) and not ulc(add_arrays(ulc_f,ulc_g))
    weighted_dyck=distributions(14,up_weights=[1]*6+[10000])[14]
    weighted_A=[0]+[sum(weighted_dyck[2*i-1:2*i+1]) for i in range(1,5)]
    assert not ulc(weighted_A)
    weighted_M=[0]+distributions(6,True,up_weights=[1,1,100])[6]
    weighted_R=[0]+distributions(6,True,True,up_weights=[1,1,100])[6]
    assert not lc(weighted_M) and not lc(weighted_R)
    m,u=S.symbols('m u');C=lambda n,k:S.prod(n-j for j in range(k))/S.factorial(k)
    hh=2*m*m-7*m+3
    endpoint={
      'Meven':(S.Integer(1),2*m*m+m-3,hh+(2*m-5)*C(2*m,2)+C(2*m,4)),
      'Modd':(2*m+1,(2*m-3)*(2*m+1)+C(2*m+1,3),hh*(2*m+1)+(2*m-5)*C(2*m+1,3)+C(2*m+1,5)),
      'Reven':(S.Integer(1),m*(2*m-3),hh+(2*m-7)*C(2*m-2,2)+2*C(2*m-3,2)+C(2*m-2,4)),
      'Rodd':(2*m-1,(2*m-5)*(2*m-1)+4*m-4+C(2*m-1,3),
        (2*m-1)*(2*m*m-11*m+12)+(2*m-2)*(4*m-12)+3*(2*m-3)
        +(2*m-7)*C(2*m-1,3)+2*C(2*m-2,3)+C(2*m-1,5))}
    endpoint_receipts=[]
    for name,(a,b,c) in endpoint.items():
        f=S.Poly(S.expand((b*b-a*c).subs(m,u+5)),u)
        assert all(v>0 for v in f.all_coeffs())
        for q in range(5,50):
            length=2*q+int('odd' in name);D=M if name.startswith('M') else R
            assert [D[length][-j] for j in [1,2,3]]==[int(x.subs(m,q)) for x in [a,b,c]]
        endpoint_receipts.append({'family':name,'defect_at_m_equals_u_plus_5':str(f.as_expr())})
    for length in range(10):
        for D in [M,R]:
            c=D[length]
            if len(c)>=3:assert c[-2]**2>=c[-3]*c[-1]
    result={'status':'PASS','A_and_B_ULC_n':list(range(1,101)),
            'M_and_R_LC_lengths':list(range(101)),
            'tail_formula_assertions':assertions,'independent_ceiling_controls_through_length':16,
            'actual_nonreal_witnesses':witnesses,'actual_stronger_ULC_failures':strong,
            'finer_Dyck_ULC_failure':{'n':7,'counts':H[14]},
            'first_return_identity_controls':first_return_controls,
            'generic_sum_obstructions':{'LC':[lc_f,lc_g],'ULC_order_3':[ulc_f,ulc_g]},
            'weighted_spectral_route_obstructions':{'A7':weighted_A,'M6':weighted_M,'R6':weighted_R},
            'endpoint_formula_controls':endpoint_receipts,
            'scope':'The separate proof establishes all-size upper-tail ULC for A/B. The full finite DP controls are bounded.'}
    (HERE/'HEIGHT-CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['A_and_B_ULC_n','M_and_R_LC_lengths','actual_stronger_ULC_failures']})[:1800])

if __name__=='__main__':main()
