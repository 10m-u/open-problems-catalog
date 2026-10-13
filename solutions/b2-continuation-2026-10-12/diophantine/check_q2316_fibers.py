#!/usr/bin/env python3
"""Complete finite-coordinate fibres, with unrestricted other coordinates."""
from pathlib import Path
from math import isqrt
from sympy import factorint, isprime
import json

HERE = Path(__file__).resolve().parent


def signed_divisors(factors):
    values = [1]
    for p,e in factors:
        values = [d*p**j for d in values for j in range(e+1)]
    assert len(values) == len(set(values))
    return sorted(values + [-d for d in values])


def packet(a):
    r = 26*a**3+18*a-27
    factors = sorted(factorint(abs(r)).items())
    rows = []
    for d in signed_divisors(factors):
        if (d-a) % 6:
            continue
        s = (d-a)//3
        num = s**3+s+a**3+a-1
        if num % d:
            continue
        t = num//d
        rows.append([d,s,t,s*s-4*t])
    return {"a":a,"R":r,"factors":factors,"candidates":rows}


def verify(p):
    a = p["a"]
    r = 26*a**3+18*a-27
    assert a % 2 and p["R"] == r and r != 0
    product = 1
    assert len({q for q,e in p["factors"]}) == len(p["factors"])
    for q,e in p["factors"]:
        assert q < 2**64 and isprime(q) and e > 0
        product *= q**e
    assert product == abs(r)
    expected = []
    for d in signed_divisors(p["factors"]):
        if (d-a) % 6:
            continue
        s = (d-a)//3
        num = s**3+s+a**3+a-1
        assert 27*num == d*(9*s*s-3*a*s+a*a+9)+r
        if num % d:
            continue
        t = num//d
        expected.append([d,s,t,s*s-4*t])
    assert p["candidates"] == expected
    hits = []
    for d,s,t,delta in expected:
        if delta < 0:
            continue
        u = isqrt(delta)
        if u*u != delta or (s+u) % 2:
            continue
        y,z = (s+u)//2,(s-u)//2
        if not y % 2 or not z % 2:
            continue
        assert a**3+a+y**3+y+z**3+z == a*y*z+1
        hits.append([a,y,z])
    return hits


def main():
    packets = json.loads(json.dumps([packet(a) for a in range(-5000,5001) if a % 2]))
    assert [p["a"] for p in packets] == list(range(-4999,5000,2))
    hits = [v for p in packets for v in verify(p)]
    assert not hits
    (HERE/"FIBER-CERTIFICATES.json").write_text(json.dumps(packets,indent=2)+"\n")
    receipt = {"status":"passed","coordinate_bound":5000,
               "odd_fixed_coordinates":len(packets),
               "complete_fibre_candidates":sum(len(p["candidates"]) for p in packets),
               "integer_solutions":hits,"other_coordinates":"unrestricted",
               "scope":"Every solution has all coordinates odd and absolute value >5000"}
    (HERE/"FIBER-CHECK.json").write_text(json.dumps(receipt,indent=2)+"\n")
    print(json.dumps(receipt))


if __name__ == "__main__":
    main()
