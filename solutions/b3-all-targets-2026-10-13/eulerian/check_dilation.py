#!/usr/bin/env python3
"""Literal all-length exclusion controls and all-size formula checks."""
from itertools import product
from math import gcd
from pathlib import Path
from hashlib import sha256
import json
from colored_probe import colored,vectors,euler
HERE=Path(__file__).resolve().parent

def main():
    h=colored((1,1),(4,5));ss=list(vectors(sum(h),3));records=[]
    for s in ss:
        c=[0]*(len(s)+1)
        for e in product(*(range(a) for a in s)):
            k=int(e[0]>0)+sum(e[i-1]*s[i]<e[i]*s[i-1] for i in range(1,len(s)))
            c[k]+=1
        while len(c)>1 and not c[-1]:c.pop()
        assert tuple(c)==euler(s)
        records.append({'s':s,'row':c})
    assert h==(1,27,12) and len(records)==22 and all(tuple(x['row'])!=h for x in records)
    for a in range(1,41):
        for b in range(1,41):
            expected=(1,(a*b+a+b+gcd(a,b)-4)//2,((a-1)*(b-1)-gcd(a,b)+1)//2)
            while len(expected)>1 and not expected[-1]:expected=expected[:-1]
            assert euler((a,b))==expected
    controls=[]
    for t in range(1,25):
        a=8*t;b=45*t;expected=(1,180*t*t+27*t-2,180*t*t-27*t+1)
        assert colored((1,1),(12*t,15*t))==expected
        assert (1,(a*b+a+b+gcd(a,b)-4)//2,((a-1)*(b-1)-gcd(a,b)+1)//2)==expected
        if t<=3:assert euler((a,b))==expected
        controls.append({'t':t,'r':[12*t,15*t],'s':[8*t,45*t],'row':expected})
    receipt={'status':'PASS','all_length_exclusion_dependency':'Previously reviewed degree-two compression: canonical length<=3.',
        'primitive_colors':[4,5],'primitive_numerator':h,'candidate_count':len(records),
        'all_candidate_rows':records,'common_dilation':3,'two_coordinate_formula_controls':1600,
        'all_size_formula_controls':controls,'scope':'Exact named exclusion and family controls; all-size proof in DILATION-FAMILIES.md.',
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (HERE/'DILATION-CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({k:v for k,v in receipt.items() if k not in ('all_candidate_rows','all_size_formula_controls')},indent=2))
if __name__=='__main__':main()
