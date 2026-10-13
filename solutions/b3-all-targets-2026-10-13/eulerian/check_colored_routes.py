#!/usr/bin/env python3
from pathlib import Path
from itertools import product,permutations
from math import prod
from hashlib import sha256
import json,sympy as sp
from colored_probe import euler,colored,vectors
HERE=Path(__file__).resolve().parent;x=sp.Symbol('x')
def words(m,r):
    labels=tuple(i for i,a in enumerate(m) for _ in range(a))
    out=[]
    for w in sorted(set(permutations(labels))):
        for c in product(*(range(1,r[i]+1) for i in w)):
            v=tuple(zip(c,w));sent=(1,len(m));d=sum(a>b for a,b in zip(v,v[1:]+(sent,)))
            out.append((w,c,d))
    return out

def row(wordlist,D):
    h=[0]*(D+1)
    for w,c,d in wordlist:h[d]+=1
    return h

def decompose(h):
    D=len(h)-1;a=[0]*(D+1);b=[0]*D
    for i in range(D+1):a[i]=h[i]-(h[D+1-i] if i else 0)+(a[i-1] if i else 0)
    for i in range(D):b[i]=h[D-i]-h[i]+(b[i-1] if i else 0)
    assert a==a[::-1] and b==b[::-1]
    return a,b

def gamma(h):
    from math import comb
    D=len(h)-1;rem=h[:];g=[]
    for i in range(D//2+1):
        c=rem[i];g.append(c)
        for j in range(D-2*i+1):rem[i+j]-=c*comb(D-2*i,j)
    assert not any(rem);return g

def main():
    packet=json.loads((HERE/'COLORED-PROBE.json').read_text());controls=0
    for case in packet['cases']:
        m=tuple(case['m']);r=tuple(case['r']);h=tuple(case['h']);N=case['volume']
        assert colored(m,r)==h
        literal=row(words(m,r),sum(m))
        while len(literal)>1 and not literal[-1]:literal.pop()
        assert literal==list(h);controls+=1
        candidates=list(vectors(N,2*(len(h)-1)-1))
        assert len(candidates)==case['candidate_count']
        assert [list(v) for v in candidates if euler(v)==h]==case['matches']
    bad=colored((1,2),(3,2));assert bad==(1,20,15)
    assert 20**2-4*15>0 and not any(euler(v)==bad for v in vectors(36,3))
    assert euler((3,1,2,2))==(1,5,6) and euler((3,2,2))!=bad
    assert euler((1,1,6,4))==(1,16,7) != colored((2,2),(1,2))==(1,13,10)
    base=colored((1,1),(3,2));assert base==(1,9,2)==euler((2,6))
    P=sum(c*x**i for i,c in enumerate(base));new=sp.expand((1+2*x)*P+x*(1-x)*sp.diff(P,x))
    assert new==1+20*x+15*x*x and euler((2,6,3))==(1,19,16)
    W=words((1,1),(3,3));h=colored((1,1),(3,3));a,b=decompose(list(h));g=gamma(a);eta=gamma(b)
    frozen=[w for w in W if w[1]==(1,1)];assert row(frozen,2)==[1,1,0]
    bylast=[row([w for w in W if w[1][-1]==c],2) for c in [1,2,3]]
    byorder=[row([w for w in W if w[0]==o],2) for o in [(0,1),(1,0)]]
    assert h==(1,13,4) and a==[1,10,1] and b==[3,3] and g==[1,8] and eta==[3]
    assert byorder==[[1,7,1],[0,6,3]] and bylast[0]==[1,5,0]
    assert prod((3,3))==9 and colored((1,1),(1,1))==(1,1)
    B4=colored((1,)*4,(2,)*4);aa,bb=decompose(list(B4));gg=gamma(aa)
    assert B4==(1,76,230,76,1) and gg==[1,72,80] and all(v==0 for v in bb)
    assert 72**2-4*80==256*19
    formal=(1+x)**2;c=sp.Rational(3,2)
    ff=sp.Poly(sp.expand((1+(3*c-1)*x)*formal+c*x*(1-x)*sp.diff(formal,x)),x)
    hh=[ff.nth(i) for i in range(4)];aaa,bbb=decompose(hh)
    assert bbb==[-sp.Rational(1,2),-1,-sp.Rational(1,2)]
    after=colored((2,1),(3,3));av,bv=decompose(list(after));assert gamma(av)==[1,32] and gamma(bv)==[1,5]
    endpoint_controls=0;two_letter_controls=0
    for N in range(1,5):
        for R in range(2,6):
            ww=words((1,)*N,(R,)*N);hh=list(colored((1,)*N,(R,)*N));a0,b0=decompose(hh)
            aa0=row([w for w in ww if w[1][-1] in (1,R)],N)
            bb0=row([w for w in ww if 1<w[1][-1]<R],N)
            assert aa0==a0 and bb0==[0]+b0;endpoint_controls+=1
            if N==2:
                special=[w for w in ww if w[1] in [(1,1),(R,R)]]
                rest=[w for w in ww if w[1][-1] in (1,R) and w not in special]
                assert row(special,2)==[1,2,1]
                assert len(rest)==4*(R-1) and all(w[2]==1 for w in rest)
                assert gamma(a0)==[1,4*(R-1)] and gamma(b0)==[R*(R-2)];two_letter_controls+=1
    repeated=words((2,1),(3,3))
    repeated_endpoint=row([w for w in repeated if w[1][-1] in (1,3)],3)
    assert repeated_endpoint==[1,31,22,0]!=av
    receipt={'status':'PASS','colored_cases_literal_word_and_exact_recognizer':controls,
      'known_uniform_color_cases_are_controls_not_new_attempts':True,
      'new_colored_RR_exclusion':{'m':[1,2],'r':[3,2],'h':bad,'all_length_candidates':27},
      'separated_single_component_rows':[1,5,6],'heterogeneous_scaled_known_vector_row':[1,16,7],
      'multiplicity_operator_actual_input':base,'multiplicity_operator_actual_output':bad,
      'append_volume_denominator_actual_output':[1,19,16],
      'gamma_actual_colored_two_letter':{'h':h,'a':a,'b':b,'gamma':g,'eta':eta,
           'frozen_classical_pair_row':[1,1,0],'last_color_rows':bylast,'underlying_order_rows':byorder},
      'root_factor_integer_decoration_obstruction':{'actual_B4_h':B4,'gamma':gg,'discriminant':256*19},
      'formal_gamma_growth_negative_eta':list(map(str,bbb)),
      'actual_gamma_growth_positive':{'after':after,'gamma':gamma(av),'eta':gamma(bv)},
      'endpoint_partition_exact_controls':endpoint_controls,'two_letter_gamma_orbit_controls':two_letter_controls,
      'actual_repeated_letter_endpoint_failure':repeated_endpoint,
      'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
      'probe_sha256':sha256((HERE/'colored_probe.py').read_bytes()).hexdigest(),
      'scope':'Finite exact decisions/actual method obstructions and a labelled formal gamma transition; no full structural classification or interpretation.'}
    (HERE/'COLORED-ROUTES-CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt,indent=2))
if __name__=='__main__':main()
