#!/usr/bin/env python3
"""Independent small exact expansions supporting the subsum proof audit."""
from collections import defaultdict
from fractions import Fraction
from math import comb
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
HOME = HERE.parent

def convolution(a, b):
    out = defaultdict(int)
    for i, x in a.items():
        for j, y in b.items():
            out[i + j] += x * y
    return dict(out)

def factor(step, count):
    return {step * j: comb(count, j) for j in range(count + 1)}

def dense(p):
    return [p.get(i, 0) for i in range(max(p) + 1)]

def F(n):
    p = {0: 1}
    for step in range(1, n + 1):
        count = sum(1 for j in range(n.bit_length()) if step * 2**j <= n)
        p = convolution(p, factor(step, count))
    return dense(p)

def multiplicities(n):
    """Descending denomination recursion, independent of halving partitions."""
    powers = [2**j for j in range(n.bit_length())]
    def rec(j, residual, partial):
        if j == 0:
            yield (residual,) + partial
            return
        for count in range(residual // powers[j] + 1):
            yield from rec(j - 1, residual - count * powers[j],
                           (count,) + partial)
    yield from rec(len(powers) - 1, n, ())

def H(n):
    p = defaultdict(int)
    parts = list(multiplicities(n))
    for counts in parts:
        term = {0: 1}
        for j, count in enumerate(counts):
            step = 2**j
            term = convolution(term, factor(step, n // step - count))
        for k, value in term.items():
            p[k] += value
    return dense(p), parts

def lc(p):
    return all(p[i]**2 >= p[i-1]*p[i+1] for i in range(1, len(p)-1))

def variance(p):
    d = len(p)-1
    return Fraction(sum((2*i-d)**2*c for i, c in enumerate(p)),
                    4*sum(p))

def main():
    products = binaries = regroupings = 0
    for n in range(1, 17):
        p = F(n)
        L = n.bit_length()
        assert p[0] == 1 and p[1] == L
        if n >= 2:
            assert p[2] == comb(L, 2) + L - 1
        if len(p) >= 4:
            assert p[3] == comb(L, 3) + L*(L-1) + (n//3).bit_length()
        if n >= 8:
            assert p[1]**2 > p[2]
            assert p[2]**2 > p[1]*p[3]
        # Independently check both regrouping and the n-step quotient.
        regroup = {0: 1}
        for odd in range(1, n+1, 2):
            for q in range((n//odd).bit_length()):
                regroup = convolution(regroup,
                    {odd*k: 1 for k in range(2**(q+1))})
        assert dense(regroup) == p
        increment = {i:v for i,v in enumerate(F(n-1))} if n > 1 else {0:1}
        step = n
        while True:
            increment = convolution(increment, {0:1, step:1})
            if step % 2:
                break
            step //= 2
        assert dense(increment) == p
        regroupings += 2
        products += 1

        if n >= 2:
            h, parts = H(n)
            N = n//2
            b = [1] + [len(list(multiplicities(t))) for t in range(1, N+1)]
            assert h[0] == len(parts) == sum(b)
            assert h[1] == 2*sum(t*bt for t,bt in enumerate(b))
            assert h[2] == sum(comb(n-c[0],2)+N-(c[1] if len(c)>1 else 0)
                               for c in parts)
            assert h == h[::-1] and min(h) > 0
            if n >= 4:
                assert 2*h[1] >= (2*N+1)*h[0]
                assert h[1]**2 > h[0]*h[2]
            weights = [Fraction(1,2**sum(c)) for c in parts]
            square = sum(w*sum(cj*4**j for j,cj in enumerate(c))
                         for c,w in zip(parts, weights))/sum(weights)
            S = sum(4**j*(n//2**j) for j in range(n.bit_length()))
            assert variance(h) == (S-square)/4
            binaries += 1
            if n in (4,8,16):
                s = n.bit_length()-1
                support = {0:1}
                for j in range(s):
                    support = convolution(support, factor(2**j,n//2**j))
                assert min(dense(support)) > 0
                assert max(support) == s*n
                assert variance(h) >= Fraction(n*n-n,4) > Fraction(s*n,4)

    h,_ = H(6)
    altered = h[:]
    for i,v in zip(range(3,8),(1,-4,6,-4,1)):
        altered[i] += 10*v
    assert lc(h) and not lc(altered)
    assert min(altered)>0 and altered == altered[::-1]
    for power in range(3):
        assert sum(i**power*v for i,v in enumerate(h)) == \
               sum(i**power*v for i,v in enumerate(altered))
    assert variance(h) == Fraction(176,39)
    # Exact nonreal-root remainders.
    f8 = F(8)
    assert sum(c*(-1)**(i//2) for i,c in enumerate(f8) if i%2==0) == 0
    assert sum(c*(-1)**(i//2) for i,c in enumerate(f8) if i%2==1) == 0
    assert len({sum(h[i] for i in range(r,len(h),3)) for r in range(3)}) == 1
    # Generic sufficient-lemma failures with positive full support.
    assert not lc(dense(convolution({0:1,1:100,2:1},{0:1,2:1})))
    assert not lc(dense(convolution({i:1 for i in range(4)},{0:1,3:1})))
    tv_bounds = []
    for m in range(2,17):
        base = [Fraction(comb(2*m,i),4**m) for i in range(2*m+1)]
        removed = 2*base[m]/(m+1)
        modified = base[:]
        modified[m] -= removed
        modified = [x/(1-removed) for x in modified]
        tv = sum(abs(x-y) for x,y in zip(base,modified))/2
        assert not lc(modified) and tv <= Fraction(2,m+1)
        tv_bounds.append(str(tv))

    paths = ("subsums/ATTEMPTS.md", "subsums/BOUNDARIES.md",
             "subsums/check_boundaries.py", "subsums/BOUNDARY-CHECK.json")
    hashes = {p:hashlib.sha256((HOME/p).read_bytes()).hexdigest() for p in paths}
    receipt = {"status":"PASS", "independent_product_expansions":products,
               "independent_binary_partition_expansions":binaries,
               "exact_regrouping_and_increment_controls":regroupings,
               "powers_of_two_mixture_and_full_support_controls":[4,8,16],
               "same_moment_control_variance":"176/39",
               "generic_convolution_and_actual_nonreal_controls":4,
               "same_normal_limit_controls":len(tv_bounds),
               "reviewed_files_sha256":hashes,
               "scope":"Finite independent controls support algebra and obstructions; all-size claims use the written proofs."}
    (HERE/"SUBSUM-REVIEW-CHECK.json").write_text(json.dumps(receipt,indent=2)+"\n")
    print(json.dumps(receipt,indent=2))

if __name__ == "__main__":
    main()

