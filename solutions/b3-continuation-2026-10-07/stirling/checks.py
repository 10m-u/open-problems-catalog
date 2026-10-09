#!/usr/bin/env python3
"""Exact controls for the reconstructed Stirling continuation (standard library).

The finite ranges test the identities and catch transcription errors. They do
not prove any assertion outside those ranges; all-r proofs are in REPORT.md.
"""
from fractions import Fraction as Q
from itertools import combinations, permutations
from math import comb, factorial
from pathlib import Path
import hashlib
import json


def trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b, sign=1):
    c = [0] * max(len(a), len(b))
    for i, x in enumerate(a):
        c[i] += x
    for i, x in enumerate(b):
        c[i] += sign * x
    return trim(c)


def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return trim(c)


def determinant(a):
    """Permutation determinant, entirely separate from row formula generation."""
    n = len(a)
    result = [0]
    for sigma in permutations(range(n)):
        sign = (-1) ** sum(sigma[i] > sigma[j]
                           for i in range(n) for j in range(i + 1, n))
        product = [1]
        for i in range(n):
            product = mul(product, a[i][sigma[i]])
        result = add(result, product, sign)
    return result


def rows(r, nmax, family):
    """Lemma 1.1 recurrence; output ascending polynomial coefficients."""
    a = [[1]]
    p = r - 1
    for n in range(1, nmax + 1):
        current = [0] * (n + 1)
        for k in range(1, n + 1):
            top = n + p * k - 1
            birth = comb(top, p)
            if family == "cycle":
                birth *= factorial(p)
                stay = top
            else:
                stay = k
            current[k] = birth * a[n-1][k-1]
            if k < len(a[n-1]):
                current[k] += stay * a[n-1][k]
        a.append(current)
    return a


def egf_entry(r, n, k, family):
    """Independent labelled assembly formula for C/S(n,k)."""
    if k == 0:
        return int(n == 0)
    excess = n - k
    if excess < 0:
        return 0
    atom = [Q(1, r+j) if family == "cycle" else Q(1, factorial(r+j))
            for j in range(excess + 1)]
    power = [Q(1)]
    for _ in range(k):
        power = mul(power, atom)[:excess + 1]
    value = power[excess] * Q(factorial(n + (r-1)*k), factorial(k))
    assert value.denominator == 1
    return value.numerator


def normalized_rows(r):
    B = Q(factorial(2*r), 2*factorial(r)**2)
    T = Q(factorial(3*r), 6*factorial(r)**3)
    U = Q(factorial(4*r), 24*factorial(r)**4)
    a = factorial(r-1)
    f = [[1], [0,1], [0,r,B],
         [0,r*(r+1), Q(2*r*(2*r+1), r+1)*B,T],
         [0,r*(r+1)*(r+2),
          Q(2*r*(2*r+1)*(3*r*r+6*r+2),(r+1)*(r+2))*B,
          Q(3*r*(3*r+1),r+1)*T,U]]
    return a, B, T, U, f


def determinant_formula(r, B, T, U):
    A = 7*r**4 + 20*r**3 + 9*r**2 - 8*r - 4
    D = 4*r**4 + 6*r**3 - 14*r**2 - 16*r - 4
    E = 5*r**4 + 16*r**3 + 19*r**2 + 8*r
    return [0,0,r*r*(r+1),
            Q(r,(r+1)*(r+2))*(B*(5*r**4+8*r**3+5*r*r+8*r+4)
                                       -(r**3+5*r*r+8*r+4)),
            Q(r,(r+1)**2*(r+2))*(A*T-D*B*B-E*B),
            Q(r,r+1)*(B*B*(5*r+1)+B*T*(r-1)-T*(7*r+1)+U*(r+1)),
            B*U-T*T-B**3+2*B*T-U]


def block_minor_formulas(r, B, T, U):
    A = 7*r**4 + 20*r**3 + 9*r**2 - 8*r - 4
    D = 4*r**4 + 6*r**3 - 14*r**2 - 16*r - 4
    return {
        ((0,1),(0,1)): [0,r,B-1],
        ((0,1),(0,2)): [0,r*(r+1),Q(r,r+1)*((4*r+2)*B-r-1),T-B],
        ((0,1),(1,2)): [0,0,r,Q(2*r*r,r+1)*B,T-B*B],
        ((0,2),(0,2)): [0,r*(r+1)*(r+2),
            Q(r,(r+1)*(r+2))*(B*(12*r**3+30*r*r+20*r+4)
                                      -r**3-3*r*r-2*r),
            Q(r,r+1)*((9*r+3)*T-(2*r+2)*B),U-B*B],
        ((0,2),(1,2)): [0,0,2*r*(r+1),Q(r*(r+1)*(7*r+2),r+2)*B,
            Q(2*r,r+1)*((4*r+1)*T-(2*r+1)*B*B),U-B*T],
        ((1,2),(1,2)): [0,0,r*r*(r+1),
            Q(r,(r+1)*(r+2))*B*(5*r**4+8*r**3+5*r*r+8*r+4),
            Q(r,(r+1)**2*(r+2))*(A*T-D*B*B),
            Q(r,r+1)*(B*T*(r-1)+U*(r+1)),B*U-T*T],
    }


def run():
    result = {
        "schema": "b3-stirling-reconstructed-checks-v1",
        "date": "2026-10-07",
        "policy": "Exact finite controls support transcription checks; all-r conclusions rely on the written proof.",
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "checks": {},
    }
    count = 0
    for r in range(1,9):
        for family in ("cycle","subset"):
            table = rows(r,9,family)
            for n in range(10):
                for k in range(n+1):
                    assert table[n][k] == egf_entry(r,n,k,family)
                    count += 1
    result["checks"]["recurrence_vs_independent_assembly"] = {
        "r": [1,8], "n": [0,9], "families": ["cycle","subset"],
        "entries": count, "passed": True,
    }
    samples = []
    for r in list(range(2,33)) + [64,100]:
        a,B,T,U,f = normalized_rows(r)
        table = rows(r,4,"cycle")
        for n in range(5):
            assert f[n] == [Q(v,a**k) for k,v in enumerate(table[n])]
        det = determinant([[f[i+j] for j in range(3)] for i in range(3)])
        expected = determinant_formula(r,B,T,U)
        assert det == expected
        assert all(v > 0 for v in det[2:])
        assert B >= 3 and T >= Q(5,3)*B*B and U >= 7*T
        assert U > B*T and B*U > T*T
        for (I,J), expected_minor in block_minor_formulas(r,B,T,U).items():
            actual_minor = determinant([[f[i+j] for j in J] for i in I])
            assert actual_minor == expected_minor
            assert all(v > 0 for v in actual_minor if v)
        samples.append({"r":r,"normalized_coefficients":[str(v) for v in det]})
    result["checks"]["first_principal_hankel_formula"] = {
        "r_values": [s["r"] for s in samples], "passed": True,
        "samples": [s for s in samples if s["r"] in [2,3,4,5]],
    }
    result["checks"]["leading_block_2x2_symbolic_formulas_controls"] = {
        "r_values": [s["r"] for s in samples], "distinct_formulas":6,
        "checks":6*len(samples),"passed":True,
        "policy":"These exact substitutions check transcription; the formulas' all-r positivity is proved in REPORT.md.",
    }
    # The claim from the interrupted continuation is not recovered as a proof.
    # These are finite controls only, including arbitrary row/column gaps.
    tested = 0
    parameters = [1,2,3,4,5,6,8,11,16]
    finite_data = []
    for r in parameters:
        for family in ("cycle","subset"):
            table = rows(r,16,family)
            nmin = None
            for I in combinations(range(9),2):
                for J in combinations(range(9),2):
                    det = determinant([[table[i+j] for j in J] for i in I])
                    assert all(v >= 0 for v in det), (r,family,I,J,det)
                    tested += 1
                    nz = [v for v in det if v]
                    if nz:
                        nmin = min(nmin or min(nz),min(nz))
            finite_data.append({"r":r,"family":family,
                                "minimum_nonzero_coefficient":str(nmin)})
    result["checks"]["universal_2x2_lead_finite_controls"] = {
        "r_values": parameters,"row_column_indices": [0,8],
        "families": ["cycle","subset"],"minors":tested,
        "passed":True,"evidence_kind":"finite-only","summary":finite_data,
    }
    # A negative control guards against accidentally transferring cycle claims.
    subset = rows(3,5,"subset")
    counter = determinant([[subset[i+j] for j in range(3)] for i in range(1,4)])
    assert counter == [0,0,0,0,0,-16,19110,938700,15309000,79380000]
    result["checks"]["subset_counterexample_control"] = {
        "r":3,"I":[1,2,3],"J":[0,1,2],
        "coefficients":counter,"negative_degree":5,"passed":True,
        "scope":"Adjacent subset Hankel property, not cycle Q1160.",
    }
    result["passed"] = True
    dest = Path(__file__).with_name("checks.json")
    dest.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({"passed":True,"assembly_entries":count,
                      "first_principal_r_values":len(samples),"2x2_finite_minors":tested,
                      "output":str(dest)}))


if __name__ == "__main__":
    run()
