"""Exact algebra/congruence controls for the constructive linear theorem."""
import json
from math import gcd, prod
from pathlib import Path
from sympy import factorint, totient


def main():
    controls = 0
    examples = []
    for a in range(-12, 13):
        if not a:
            continue
        for b in range(-12, 13):
            g = gcd(abs(a), abs(b))
            aa, bb = a // g, b // g
            sign = 1 if a > 0 else -1
            modulus = abs(aa)
            residue = (sign * bb) % modulus
            base = residue
            while base <= 1:
                base += modulus
            assert gcd(base, modulus) == 1
            phi = int(totient(modulus))
            allowed = set(factorint(g * base))
            previous = None
            start = 1
            while base**(1 + start * phi) <= abs(bb):
                start += 1
            for k in range(start, start + 3):
                m = 1 + k * phi
                numerator = sign * base**m - bb
                assert numerator % aa == 0
                n = numerator // aa
                assert a*n+b == sign*g*base**m
                assert n > 0
                if previous is not None:
                    assert n > previous
                previous = n
                # Identity proves prime support without factoring enormous values.
                assert prod(p**e for p, e in factorint(g * base).items()) == g * base
                controls += 1
            if (a, b) in {(3, 2), (-7, 4), (6, 0)}:
                examples.append({"a": a, "b": b, "B": base, "fixed_prime_support": sorted(allowed)})
    result = {"passed": True, "exact_congruence_and_value_controls": controls,
              "examples": examples,
              "scope": "Finite controls of the all-linear proof; no verification of the all-degree conjecture"}
    Path(__file__).with_name("LINEAR-SMOOTHNESS-CHECK.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
