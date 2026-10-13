"""Exact f_k on small cyclic groups, permitting repeated summands."""
import json
from math import gcd
from pathlib import Path


def rotate(mask,shift,n):
    return ((mask<<shift)|(mask>>(n-shift))) & ((1<<n)-1)


def compute(n,k):
    represented=set()
    for a in range(1<<n):
        current=a
        entries=[i for i in range(n) if a>>i&1]
        for _ in range(k-1):
            new=0
            for i in entries:
                new|=rotate(current,i,n)
            current=new
        represented.add(current)
    bad=sorted((n-s.bit_count(),s) for s in range(1<<n) if s not in represented)
    if bad:
        missing,mask=bad[0]
        result=missing-1
        example=[i for i in range(n) if not(mask>>i&1)]
    else:
        result,example=n,None
    return {"n":n,"k":k,"f":result,"represented_sets":len(represented),"first_bad_complement":example}


def main():
    rows=[compute(n,k) for k in (2,3) for n in range(3,14) if gcd(n,k)==1]
    assert next(r["f"] for r in rows if r["n"]==5 and r["k"]==2)==0
    out={"passed":True,"rows":rows,"max_order":13,
         "scope":"Complete small cyclic-group tables, no uniform asymptotic upper bound"}
    Path(__file__).with_name("SUMSET-ROOT-CHECK.json").write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps(out))


if __name__=="__main__":
    main()
