"""Exact valuation-rank controls for the stated examples and a small complete box."""
import itertools
import json
from pathlib import Path
from sympy import factorint, Matrix


def kind(values):
    fs=[factorint(v) for v in values]
    primes=sorted(set().union(*(set(f) for f in fs)))
    cols=[[f.get(p,0) for p in primes] for f in fs]
    rank=Matrix(len(primes),len(values),lambda i,j:cols[j][i]).rank()
    if rank==3:return 'independent'
    if any(Matrix(len(primes),2,lambda r,c:cols[pair[c]][r]).rank()<2 for pair in itertools.combinations(range(3),2)):
        return '2-dependent'
    return '3-dependent'


def main():
    examples=[(2,4,14),(3,6,48),(6,8,48),(6,18,48),(6,30,216),(7,15,49),(7,49,79),(8,32,98)]
    rows=[{'triple':t,'shifts':[kind([v+j for v in t]) for j in range(3)]} for t in examples]
    assert all(all(k!='independent' for k in row['shifts']) for row in rows)
    assert not any(row['shifts']==['3-dependent']*3 for row in rows)
    family=[]
    for e in range(3,9):
        t=(2,2**e-2,2**(2*e)-2**(e+1))
        ks=[kind([v+j for v in t]) for j in range(3)]
        assert all(k!='independent' for k in ks)
        assert ks[2]=='2-dependent'
        family.append({'exponent':e,'triple':t,'shifts':ks})
    rejected={'triple':(2,6,16),'shifts':[kind([v+j for v in (2,6,16)]) for j in range(3)]}
    assert rejected['shifts'][1]=='independent'
    out={'status':'passed','exact_examples':rows,'rejected_source_case':rejected,'excluded_family_controls':family,
         'scope':'Exact example rank classification; no infinite family outside exclusions and no all-three-minimal witness'}
    Path(__file__).with_name('SHIFT-CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out))


if __name__=='__main__':main()
