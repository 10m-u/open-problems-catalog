#!/usr/bin/env python3
"""Independent row/column subset rook enumeration and exact order witnesses."""
from itertools import combinations
from fractions import Fraction
from pathlib import Path
from hashlib import sha256
import json

HERE=Path(__file__).resolve().parent
HOME=HERE.parent

def coefficients(r):
    out=[Fraction(1)]
    for a in r:
        new=[Fraction(0)]*(len(out)+1)
        for k,b in enumerate(out):new[k]+=b;new[k+1]+=a*b
        out=new
    return out

def compatible(a,b):
    return (a[0]-b[0])*(a[1]-b[1])<0

def cubic_discriminant(a,b,c,d):
    return b*b*c*c-4*a*c*c*c-4*b*b*b*d-27*a*a*d*d+18*a*b*c*d

def main():
    lam=(6,6,6,3,3,3);selected={1,2,3,10,11,12}
    plain=[0]*7;source=[0]*7;dual=[0]*7;bases=[]
    # Choose row and column subsets, then the only decreasing matching.
    for k in range(7):
        for rows in combinations(range(1,7),k):
            for cols in combinations(range(1,7),k):
                placement=list(zip(rows,reversed(cols)))
                if not all(c<=lam[r-1] for r,c in placement):continue
                plain[k]+=1
                basis={r for r in range(1,7) if r not in rows}|{6+c for c in cols}
                assert len(basis)==6
                complement=set(range(1,13))-basis
                source[len(basis&selected)]+=1
                dual[len(complement&selected)]+=1
                bases.append(basis)
    assert len(bases)==662 and len({tuple(sorted(b)) for b in bases})==662
    assert plain==[1,27,162,282,162,27,1]
    assert source==[1,36,225,400,0,0,0]
    assert dual==[0,0,0,400,225,36,1]==source[::-1]
    assert cubic_discriminant(400,225,36,1)==-602100
    assert cubic_discriminant(1,36,225,400)==-602100
    center=(1,1);leaves=[(1,3),(2,2),(3,1)]
    assert all(not compatible(center,b) for b in leaves)
    assert all(compatible(a,b) for a,b in combinations(leaves,2))
    assert cubic_discriminant(1,9,8,1)==1489
    assert cubic_discriminant(1,9,9,1)==2160
    assert cubic_discriminant(1,9,109,1)==-4203040
    # All 3x3 boards with no compatible triple give the quadratic bound.
    cells=[(r,c) for r in range(1,4) for c in range(1,4)]
    rank_two_controls=0
    for mask in range(512):
        board=[cell for i,cell in enumerate(cells) if mask>>i&1]
        pairs=sum(compatible(a,b) for a,b in combinations(board,2))
        triple=any(all(compatible(a,b) for a,b in combinations(t,2))
                   for t in combinations(board,3))
        if not triple:
            assert len(board)**2>=4*pairs
            rank_two_controls+=1
    data=json.loads((HOME/"coefficient-orders/BOUNDED-ORDERS.json").read_text())
    expected={"012345","012354","012534","015234","015243","051243","051423",
              "051432","054123","054132","501423","501432","504123","504132"}
    seen=set()
    for row in data["witnesses"]["5"]:
        c=coefficients(row["r"]);pi=row["permutation"]
        assert c==row["coefficients"] and all(c[i]<=c[j] for i,j in zip(pi,pi[1:]))
        seen.add("".join(map(str,pi)))
    assert seen==expected
    receipt={"status":"PASS","rook_enumeration":"row/column subsets with unique decreasing matching",
       "source_convention_bases":662,"source_weighted_coefficients":source,
       "dual_weighted_coefficients":dual,"ordinary_rook_coefficients":plain,
       "source_and_dual_cubic_discriminant":-602100,
       "rank_two_3x3_board_controls":rank_two_controls,
       "degree_five_exact_order_witnesses":len(seen),
       "checker_sha256":sha256(Path(__file__).read_bytes()).hexdigest(),
       "scope":"Exact independent controls; all-size rank-two and degree-five exhaustion reviewed in companion notes."}
    (HERE/"ROOK-ORDER-REVIEW-CHECK.json").write_text(json.dumps(receipt,indent=2)+"\n")
    print(json.dumps(receipt,indent=2))
if __name__=="__main__":main()

