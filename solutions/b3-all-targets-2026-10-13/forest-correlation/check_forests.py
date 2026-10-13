#!/usr/bin/env python3
"""Exact multivariate connectivity-correlation controls on complete graphs."""
from itertools import combinations
from collections import defaultdict
from pathlib import Path
from hashlib import sha256
import json

HERE=Path(__file__).resolve().parent
def components(n,edges,mask):
    p=list(range(n))
    def find(i):
        while p[i]!=i:i=p[i]
        return i
    for j,(a,b) in enumerate(edges):
        if mask>>j&1:
            a,b=find(a),find(b)
            if a==b:return None
            p[a]=b
    return tuple(find(i) for i in range(n))
def check(n):
    edges=list(combinations(range(n),2));powers=[3**j for j in range(len(edges))]
    rows=[]
    for mask in range(1<<len(edges)):
        if mask.bit_count()>=n:continue
        p=components(n,edges,mask)
        if p is None:continue
        rows.append((sum(powers[j] for j in range(len(edges)) if mask>>j&1),
                    p[0]==p[1],p[2]==p[3]))
    allf=[r[0] for r in rows];ab=[r[0] for r in rows if r[1]]
    cd=[r[0] for r in rows if r[2]];both=[r[0] for r in rows if r[1] and r[2]]
    d=defaultdict(int)
    for a in both:
        for b in allf:d[a+b]+=1
    for a in ab:
        for b in cd:d[a+b]-=1
    bad={k:v for k,v in d.items() if v<0}
    return {'vertices':n,'edges':len(edges),'forests':len(rows),
            'ordered_forest_pairs':len(both)*len(allf)+len(ab)*len(cd),
            'nonzero_coefficients':sum(v!=0 for v in d.values()),
            'negative_coefficients':bad,
            'scope':'Exact ternary exponent arithmetic. Deletion of edge variables proves all simple subgraphs on this vertex set.'}
def main():
    results=[check(n) for n in [4,5,6]]
    receipt={'status':'PASS' if all(not r['negative_coefficients'] for r in results) else 'COUNTEREXAMPLE',
       'graphs':results,'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
       'scope':'Exact bounded graph control, not an arbitrary-order proof.'}
    (HERE/'FOREST-CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt,indent=2))
if __name__=='__main__':main()
