#!/usr/bin/env python3
"""Exact local controls for P4's specified failed sufficient premises."""
from pathlib import Path
from itertools import combinations
import json
import sys
from fractions import Fraction as F

HERE = Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'generating-graph'))
from check_obstruction import necklace, mincut
sys.path.insert(0,str(HERE.parent.parent/'b14-first-round-2026-10-12'/'elimination'))
from one_tree import exact_tour


def main():
    # Verify the odd-cycle matching premise exhaustively.
    cycle = [(i,(i+1)%5) for i in range(5)]
    perfect = 0
    for mask in range(1<<5):
        chosen = [e for i,e in enumerate(cycle) if mask>>i&1]
        perfect += all(sum(v in e for e in chosen)==1 for v in range(5))
    assert perfect==0
    # A minimum unit-cost star and exact parity cost.
    n = 10
    c = [[0 if a==b else 1 for b in range(n)] for a in range(n)]
    x = necklace(1)
    assert sum(x.values())==2*n and mincut(n,x)==4
    star = [(0,v) for v in range(1,n)]
    odd = [v for v in range(n) if sum(v in e for e in star)%2]
    assert len(odd)==10
    assert len(star)+len(odd)//2==14>F(4*n,3)
    optimum,_,_ = exact_tour(c)
    assert optimum==n
    # The k=3 support has the cut-feasible template used by the all-size no-path proof.
    x3 = necklace(3)
    assert len(x3)==45 and sum(x3.values())==60 and mincut(30,x3)==4
    assert all(sum(w for e,w in x3.items() if v in e)==4 for v in range(30))
    result = {'status':'passed','odd_pentagon_edge_subsets':32,'perfect_matchings':0,
        'uniform_metric_lp':10,'minimum_tree_plus_parity':14,'uniform_optimum':10,
        'three_gadget_necklace_min_cut_twice_x':4,
        'source_only_control':'non-half-integral class at n=8: primary enumeration Table 4, not locally reproduced',
        'scope':'route obstructions only; no 4/3 counterexample'}
    (HERE/'ROUTE-CHECK-RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__': main()
