#!/usr/bin/env python3
"""A fresh actual horizontal-strip counter-construction beyond n=28."""
from pathlib import Path
from hashlib import sha256
import json, runpy

HERE=Path(__file__).resolve().parent
r=runpy.run_path(str(HERE/'check_eigenvalues.py'))

def main():
    cases=[]; polynomials=0; bad=None
    # mu=(j-1,1), lambda=(j+N-b-1,b,1).  N>=b ensures
    # lambda_1>=mu_1>=lambda_2>=mu_2>=lambda_3>=0.
    for j in (28,41,70,100):
        for N in range(3,13):
            for b in range(2,N+1):
                lam=(j+N-b-1,b,1); mu=(j-1,1,0)
                assert sum(lam)==j+N and sum(mu)==j
                assert all(lam[i]>=mu[i]>=(lam[i+1] if i<2 else 0) for i in range(3))
                cs=r['contents'](lam,mu)
                E=r['eigenvalues'](j,cs)
                assert len(cs)==N
                checked=[]
                for k in range(2,N):
                    p=E[k];polynomials+=1
                    if not r['unimodal'](p):
                        bad={'lambda':lam,'mu':mu,'k':k,'coefficients':p}
                        break
                    checked.append({'k':k,'degree':len(p)-1,
                                    'modes':r['modes'](p),
                                    'mass':sum(p)})
                cases.append({'lambda':lam,'mu':mu,'n':j+N,'checks':checked})
                if bad:break
            if bad:break
        if bad:break
    receipt={'status':'ACTUAL_COUNTEREXAMPLE' if bad else 'PASS',
       'family':'mu=(j-1,1), lambda=(j+N-b-1,b,1)',
       'j_values':[28,41,70,100],'N_range':[3,12],
       'b_range':'2,...,N','strips':len(cases),
       'intermediate_polynomials':polynomials,
       'ambient_sizes':sorted({c['n'] for c in cases}),
       'counterexample':bad,'cases':cases,
       'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
       'scope':'Fresh finite actual-strip construction; no all-size or novelty claim.'}
    (HERE/'LARGE-FAMILY-CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({k:v for k,v in receipt.items() if k!='cases'},indent=2))
if __name__=='__main__': main()
