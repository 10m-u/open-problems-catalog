#!/usr/bin/env python3
"""Exact bounded controls for arithmetic sequence/prime construction routes."""
from pathlib import Path
from itertools import combinations
from math import comb, gcd, lcm
from sympy import divisors, factorint, isprime, primerange
import json

HERE = Path(__file__).resolve().parent


def main():
    partitions = [1]
    fac = 1
    hits = []
    for n in range(1, 2001):
        total = 0
        k = 1
        while k * (3*k-1)//2 <= n:
            sign = 1 if k % 2 else -1
            for step in (k*(3*k-1)//2, k*(3*k+1)//2):
                if step <= n:
                    total += sign * partitions[n-step]
            k += 1
        partitions.append(total)
        fac *= n
        if fac % total == 0:
            hits.append(n)
    assert hits[-1] == 39
    assert partitions[40] == 37338
    assert factorint(partitions[40]) == {2: 1, 3: 1, 7: 2, 127: 1}
    catalan_exceptions = []
    for k in range(1, 5001):
        n = (1 << k) - 1
        value = n
        while value and value % 5 <= 2:
            value //= 5
        no_carry = value == 0
        if no_carry:
            catalan_exceptions.append(k)
        if k <= 12:
            c = comb(2*n, n) // (n+1)
            assert c % 2 == 1
            assert (c % 5 != 0) == no_carry
    assert catalan_exceptions == [1, 3, 5, 7, 8]
    for n in range(201):
        c = comb(2*n, n)//(n+1)
        v = 0
        while c % 2 == 0:
            v += 1
            c //= 2
        assert v == (n+1).bit_count()-1
    for j in range(1, 9):
        k = 4*5**(j-1)
        assert pow(2, k, 5**j) == 1
    primes = list(primerange(2, 52))
    signed = primes + [-p for p in primes]
    tested = 0
    for size in range(2, 6):
        for xs in combinations(signed, size):
            num = den = 1
            for x in xs:
                num *= x
                den *= x-1
            num -= 1
            assert not (num % den == 0 and num//den >= 2), xs
            tested += 1
    assert 2*(-8)*2*2 == (-7)*3*3-1
    cycles = [
        [7,43,13,157], [13,157,7,43],
        [19,7,43,139,19183],
        [31,7,43,13,157,3499,36319,2503,22129],
        [37,43,13,157,3499,36319,5791,424429,151,22651,619],
        [43,13,157,7],
        [61,7,43,13,157,3499,36319,5791,424429,449671,109],
        [157,7,43,13],
    ]
    for cycle in cycles:
        assert len(cycle) == len(set(cycle))
        assert all(isprime(p) and p % 6 == 1 for p in cycle)
        for a,b in zip(cycle, cycle[1:] + cycle[:1]):
            assert (a*a-a+1) % b == 0
    least = [19,7,43,13,157,7]
    for a,b in zip(least, least[1:]):
        assert b == min(factorint(a*a-a+1))
    n,s = 245784,65
    ds = [d for d in divisors(n) if d % s == 1]
    assert ds == [1,66,196,456,2926,12936]
    assert gcd(n,s) == 1 and s**3 > n
    assert min(lcm(n,d) for d in range(1,s**3,s) if d not in ds) == 983136
    assert gcd(*[d-1 for d in ds[1:]]) == s
    tetrahedral_controls = 0
    for v in range(-100,101):
        t = lambda u: u*(u+1)*(u+2)//6
        assert t(v)+t(-v-1) == v*(v+1)//2
        for y in range(-100,101):
            assert t(v-1)+t(y-1)+t(-v-y-1) == -v*y*(v+y)//2
            tetrahedral_controls += 1
    assert not any(-a*b*(a+b)//2 == 2
                   for a in range(-4,5) for b in range(-4,5))
    wilson = []
    for p in primerange(3,200):
        modulus = p*p
        h = (p-1)//2
        half = full = 1
        for a in range(1,h+1):
            half = half*a % modulus
        for a in range(1,p):
            full = full*a % modulus
        harmonic = sum(pow(a,-1,p) for a in range(1,h+1)) % p
        assert full == (-1)**h * half**2 * (1-p*harmonic) % modulus
        wilson.append({"p":p,"w_p":((full+1)//p) % p})
    result = {"status":"passed","partition_range":2000,
              "partition_factorial_divisions":hits,
              "catalan_exponent_range":5000,
              "carry_free_exponents":catalan_exceptions,
              "direct_catalan_parity_cases":201,
              "signed_prime_subsets":tested,"prime_cycles":cycles,
              "six_divisor_seed":ds,"minimum_augmented_lcm":983136,
              "tetrahedral_identities":tetrahedral_controls,
              "wilson_pair_controls":wilson,
              "scope":"Exact finite controls and algebraic identities; no unbounded classification"}
    (HERE/"SEQUENCE-CHECK.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({k:v for k,v in result.items()
                      if k not in {"wilson_pair_controls","prime_cycles"}}))


if __name__ == "__main__":
    main()
