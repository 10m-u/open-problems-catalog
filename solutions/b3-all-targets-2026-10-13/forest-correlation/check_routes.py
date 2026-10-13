#!/usr/bin/env python3
"""Exact finite base identities and actual switching obstruction for Q4396."""
from pathlib import Path
from collections import defaultdict
from itertools import product
from hashlib import sha256
import json,runpy
import sympy as s

HERE=Path(__file__).resolve().parent
components=runpy.run_path(str(HERE/'check_forests.py'))['components']
def base(n,pairs):
    edges=[(i,(i+1)%n) for i in range(n)];powers=[3**j for j in range(n)]
    allf=[];A=[];B=[];J=[]
    for mask in range(1<<n):
        p=components(n,edges,mask)
        if p is None:continue
        code=sum(powers[i] for i in range(n) if mask>>i&1);allf.append(code)
        a=p[pairs[0][0]]==p[pairs[0][1]];b=p[pairs[1][0]]==p[pairs[1][1]]
        if a:A.append(code)
        if b:B.append(code)
        if a and b:J.append(code)
    d=defaultdict(int)
    for a,b in product(J,allf):d[a+b]+=1
    for a,b in product(A,B):d[a+b]-=1
    assert all(v>=0 for v in d.values())
    return {str(code):v for code,v in sorted(d.items()) if v}
def main():
    identities={
      'triangle_shared_terminal':base(3,((0,1),(0,2))),
      'four_cycle_adjacent_pairs':base(4,((0,1),(2,3))),
      'four_cycle_alternating_pairs':base(4,((0,2),(1,3)))}
    edges=[(0,4),(4,1),(4,5),(5,1),(2,3)]
    first=0b00011;second=0b11100
    p1=components(6,edges,first);p2=components(6,edges,second)
    assert p1 is not None and p2 is not None
    assert p1[0]==p1[1] and p1[2]!=p1[3]
    assert p2[2]==p2[3] and p2[0]!=p2[1]
    assert components(6,edges,first|second) is None
    # Failed FKG support condition.
    tri=[(0,1),(1,2),(0,2)]
    assert components(3,tri,3) is not None and components(3,tri,4) is not None
    assert components(3,tri,7) is None
    z=s.symbols('z');L=s.Matrix([[2,-1,-1],[-1,2,-1],[-1,-1,2]])
    assert s.expand((s.eye(3)+z*L).det())==1+6*z+9*z*z
    receipt={'status':'PASS','cycle_base_identities':identities,
      'cycle_exponent_encoding':'base 3, edge i is the i to i+1 arc',
      'whole_path_switch_obstruction':'actual acyclic pair; transfer creates a triangle',
      'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
      'scope':'Exact bases for all-size cycle/cactus proof plus three distinct route obstructions.'}
    (HERE/'ROUTE-CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt,indent=2))
if __name__=='__main__':main()
