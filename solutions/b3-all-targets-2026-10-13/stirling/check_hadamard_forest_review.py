#!/usr/bin/env python3
"""Independent bounded arithmetic/BFS review; never writes root receipts."""
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations_with_replacement
from math import comb, factorial
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

def forest_rows(n, edges):
    rows = []
    for mask in range(1 << len(edges)):
        adj = [[] for _ in range(n)]
        for j, (u, v) in enumerate(edges):
            if mask >> j & 1:
                adj[u].append(v); adj[v].append(u)
        labels = [-1] * n; components = 0
        for start in range(n):
            if labels[start] >= 0: continue
            todo = [start]; labels[start] = components
            while todo:
                u = todo.pop()
                for v in adj[u]:
                    if labels[v] < 0:
                        labels[v] = components; todo.append(v)
            components += 1
        # A finite undirected graph is acyclic iff |E|=|V|-components.
        if mask.bit_count() == n - components:
            rows.append((tuple((mask >> j) & 1 for j in range(len(edges))), labels))
    return rows

def defect(rows, pairs):
    Z = [r[0] for r in rows]
    A = [p for p, labels in rows if labels[pairs[0][0]] == labels[pairs[0][1]]]
    B = [p for p, labels in rows if labels[pairs[1][0]] == labels[pairs[1][1]]]
    J = [p for p, labels in rows if
         labels[pairs[0][0]] == labels[pairs[0][1]] and
         labels[pairs[1][0]] == labels[pairs[1][1]]]
    d = Counter()
    for sign, X, Y in ((1, J, Z), (-1, A, B)):
        for p in X:
            for q in Y:
                d[tuple(x+y for x,y in zip(p,q))] += sign
    return {p:c for p,c in d.items() if c}

def main():
    bases = json.loads((ROOT/'forest-correlation/ROUTE-CHECK.json').read_text())['cycle_base_identities']
    controls = 0
    named = {
        'triangle_shared_terminal': (3, ((0,1),(0,2))),
        'four_cycle_adjacent_pairs': (4, ((0,1),(2,3))),
        'four_cycle_alternating_pairs': (4, ((0,2),(1,3))),
    }
    for name, (n, pairs) in named.items():
        edges = [(i,(i+1)%n) for i in range(n)]
        d = defect(forest_rows(n,edges), pairs)
        encoded = {str(sum(x*3**j for j,x in enumerate(p))):c for p,c in d.items()}
        assert encoded == bases[name]
    for n in (3,4):
        rows = forest_rows(n,[(i,(i+1)%n) for i in range(n)])
        pairs = list(combinations_with_replacement(range(n),2))
        for a in pairs:
            for b in pairs:
                assert all(c > 0 for c in defect(rows,(a,b)).values())
                controls += 1
    cactus_edges = [(0,1),(1,2),(2,0),(0,3),(3,4),(4,0)]
    cactus_rows = forest_rows(5,cactus_edges)
    for pairs in [((0,1),(3,4)), ((1,3),(2,4)), ((1,2),(2,3)),
                  ((0,0),(1,4)), ((1,4),(1,4))]:
        assert all(c > 0 for c in defect(cactus_rows,pairs).values())
        controls += 1
    # Raw coefficient convolution of shifted repeated poles versus iterated theta+h.
    pole_controls = 0
    for n in range(1,9):
        a = [F(j*j+3*j+1, j+1) for j in range(n+4)]
        for m in range(1,9):
            for l in range(4):
                p = a[l:l+n+1]
                for h in range(1,m):
                    p = [v*(j+h) for j,v in enumerate(p)]
                p = [v/factorial(m-1) for v in p]
                # Build (1-z)^(-m) by m convolutions of the geometric series.
                b = [F(1)] + [F(0)]*n
                for _ in range(m):
                    b = [sum(b[:j+1]) for j in range(n+1)]
                assert p == [a[l+j]*b[j] for j in range(n+1)]
                pole_controls += 1
    # Discriminants evaluated by integer/Fraction formulas, independent of SymPy.
    x,y,z,w = F(1,100),F(27,100),F(1),F(1)
    cubic = y*y*z*z-4*x*z**3-4*y**3*w-27*x*x*w*w+18*x*y*z*w
    assert cubic == F(17,250000)
    assert F(27,100)**2 - F(4,100) == F(329,10000)
    assert 1-4*F(101,10) == -F(197,5)
    assert 1-4*F(5,18) == -F(1,9)
    receipt = {
      'status':'PASS', 'cycle_base_identities_matched':3,
      'cycle_and_cactus_pair_controls':controls,
      'cactus_forests':len(cactus_rows),
      'shifted_repeated_pole_controls':pole_controls,
      'exact_discriminants_checked':4,
      'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
      'scope':'Independent tuple-coefficient/BFS bases and bounded cactus controls; all-size proof is analytical. No K6 replay and no full catalog closure.'
    }
    (HERE/'HADAMARD-FOREST-REVIEW-CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))
if __name__ == '__main__': main()

