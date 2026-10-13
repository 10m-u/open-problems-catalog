"""Exact fixed-gap enumeration and both-sign two-row Pell families."""
import json
from math import isqrt
from pathlib import Path


def square(n):
    return n>=0 and isqrt(n)**2==n


def main():
    controls=0
    for delta in range(1,101):
        exact=set()
        for d in range(1,isqrt(delta)+1):
            if delta%d:
                continue
            e=delta//d
            if (e-d)%2:
                continue
            s=(e-d)//2
            b=s*s-1
            if b>=1:
                exact.add(b)
        brute={b for b in range(1,5001) if square(b+1) and square(b+1+delta)}
        assert {b for b in exact if b<=5000}==brute
        assert all(square(b+1) and square(b+1+delta) for b in exact)
        controls+=5000
    families={}
    for epsilon,(v,u) in [(1,(1,1)),(-1,(3,2))]:
        bs=[]
        for _ in range(8):
            b=u*u-epsilon
            if b>0:
                assert b+epsilon==u*u and 2*b+epsilon==v*v
                bs.append(b)
            v,u=3*v+4*u,2*v+3*u
        families[str(epsilon)]=bs
    assert families["1"][:3]==[24,840,28560]
    assert families["-1"][:3]==[5,145,4901]
    out={"passed":True,"fixed_gap_integer_controls":controls,"gap_max":100,
         "two_row_Pell_families":families,
         "scope":"Complete fixed-gap candidate method and finite Pell identity controls; no full near-square or bipartite-size closure"}
    Path(__file__).with_name("SQUARE-BOUNDARY-CHECK.json").write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps(out))


if __name__=="__main__":
    main()
