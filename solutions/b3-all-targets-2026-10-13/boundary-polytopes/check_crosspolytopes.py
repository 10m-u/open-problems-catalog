"""Exact coset enumeration and actual simplicial boundary controls for Q3902."""
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
from math import comb
from pathlib import Path
import json


def multiply(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return out


def determinant(a):
    a=[row[:] for row in a]; sign=1; previous=1; n=len(a)
    for i in range(n-1):
        pivot=next((j for j in range(i,n) if a[j][i]),None)
        if pivot is None: return 0
        if pivot != i: a[i],a[pivot]=a[pivot],a[i]; sign=-sign
        value=a[i][i]
        for j in range(i+1,n):
            for k in range(i+1,n):
                numerator=a[j][k]*value-a[j][i]*a[i][k]
                assert numerator % previous == 0
                a[j][k]=numerator//previous
            a[j][i]=0
        previous=value
    return sign*a[-1][-1]


def rank_mod_two(a):
    rows=[sum((x%2)<<i for i,x in enumerate(row)) for row in a]
    basis={}
    for x in rows:
        while x:
            pivot=x.bit_length()-1
            if pivot not in basis: basis[pivot]=x; break
            x ^= basis[pivot]
    return len(basis)


def coset_counts(code,m):
    cap=2*m; shells=[0]*(cap+1)
    for c in code:
        row=[1]
        for i in range(m):
            literal=[0]*(cap+1)
            for z in range(-cap,cap+1):
                if z%2 == ((c>>i)&1): literal[abs(z)] += 1
            row=multiply(row,literal)[:cap+1]
        for j,count in enumerate(row): shells[j]+=count
    assert all(shells[j]==0 for j in range(1,cap+1,2))
    E=[]; total=0
    for k in range(m+1): total+=shells[2*k]; E.append(total)
    h=[sum((-1)**j*comb(m+1,j)*E[k-j] for j in range(k+1))
       for k in range(m+1)]
    formula=[0]*(m+1)
    for c in code:
        w=c.bit_count(); assert w%2==0
        for j in range(m-w+1): formula[w//2+j]+=2**w*comb(m-w,j)
    assert h==formula
    return E,h


def main():
    controls=[]
    for m in range(1,9):
        # The full even code, nested generated subcodes, and the trivial code.
        codes={frozenset([0]),frozenset(c for c in range(1<<m) if c.bit_count()%2==0)}
        generated={0}
        for i in range(1,m):
            generator=1|(1<<i)
            generated |= {c^generator for c in generated.copy()}
            codes.add(frozenset(generated))
        for code in sorted(codes,key=lambda x:(len(x),sorted(x))):
            E,h=coset_counts(code,m)
            assert sum(h)==2**m*len(code)
            controls.append({'dimension':m,'code_size':len(code),'h_star':h,'E':E})

    triangles=[tuple(map(int,t)) for t in ['125','126','134','136','145','234','235','246','356','456']]
    edges=sorted(set(e for tri in triangles for e in combinations(tri,2)))
    A=[[sum((-1)**i for i in range(3) if tuple(x for j,x in enumerate(tri) if i!=j)==edge)
        for tri in triangles] for edge in edges]
    assert rank_mod_two(A)==9
    witness=None
    for rows in combinations(range(len(A)),10):
        det=determinant([A[i] for i in rows])
        if abs(det)==2: witness={'rows':list(rows),'determinant':det}; break
    assert witness is not None
    code=[c for c in range(1<<10)
          if all(sum(row[i]*((c>>i)&1) for i in range(10))%2==0 for row in A)]
    assert code==[0,(1<<10)-1]
    E,h=coset_counts(code,10)
    assert h==[comb(10,i)+(1024 if i==5 else 0) for i in range(11)]

    cycle=[]
    for k in range(9):
        literal=sum(abs(x-y)<=k for x,y in product(range(-k,k+1),repeat=2))
        assert literal==3*k*(k+1)+1
        cycle.append(literal)
    assert [cycle[0],cycle[1]-3*cycle[0],cycle[2]-3*cycle[1]+3*cycle[0]]==[1,4,1]
    bases=[[[1,0],[0,1]],[[1,1],[0,1]],[[0,1],[1,1]]]
    assert all(abs(determinant(B))==1 for B in bases)
    here=Path(__file__)
    out={'result':'PASS','scope':'Finite exact controls of the all-size binary-code proof and one forest-assembly obstruction',
         'code_controls':controls,'RP2_boundary':{'edges':[list(e) for e in edges],
             'matrix':A,'rank_mod_2':9,'maximal_minor_witness':witness,
             'nonzero_binary_kernel_weight':10,'h_star':h,'E':E},
         'triangle_graph_counts':cycle,'triangle_h_star':[1,4,1],
         'forest_h_star':[1,2,1],
         'checker_sha256':sha256(here.read_bytes()).hexdigest()}
    here.with_name('CROSSPOLYTOPE-CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'result':'PASS','code_controls':len(controls),'RP2_minor':witness}))


if __name__=='__main__': main()
