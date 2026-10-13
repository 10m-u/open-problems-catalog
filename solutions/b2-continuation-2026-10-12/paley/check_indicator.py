"""Bounded numerical basis controls plus exact coefficient-cap fractions."""
import cmath
from fractions import Fraction
from itertools import accumulate
import json
from pathlib import Path


def primitive_root(p):
    for g in range(2, p):
        if len({pow(g, j, p) for j in range(p-1)}) == p-1:
            return g
    raise AssertionError(p)


def main():
    count = prefixes = exception_controls = 0
    max_error = 0.0
    for p in [3, 5, 7, 11, 13]:
        g = primitive_root(p)
        log = {pow(g, j, p): j for j in range(p-1)}
        add = [[cmath.exp(-2j*cmath.pi*a*x/p) for x in range(p)] for a in range(1, p)]
        mul = [[0j if x == 0 else cmath.exp(-2j*cmath.pi*j*log[x]/(p-1))
                for x in range(p)] for j in range(1, p-1)]
        for mask in range(1, (1 << p)-1):
            s = [x for x in range(p) if mask >> x & 1]
            k, e = len(s), int(mask & 1 != 0)
            a = Fraction(min(k, p-k)**2, k*(p-k))
            b = Fraction((p*e-k)**2, (p-1)*k*(p-k))
            h = min(k-e, p-1-(k-e))
            q = Fraction(p*h*h, (p-1)*k*(p-k))
            energies_a = [abs(sum(row[x] for x in s))**2/(k*(p-k)) for row in add]
            energies_m = [p*abs(sum(row[x] for x in s))**2/((p-1)*k*(p-k)) for row in mul]
            err = max(abs(sum(energies_a)-1), abs(sum(energies_m)+float(b)-1))
            max_error = max(max_error, err)
            assert err < 2e-12
            for r, val in enumerate(accumulate(sorted(energies_a, reverse=True)), 1):
                assert val <= float(r*a)+2e-12
                prefixes += 1
            for z, val in enumerate(accumulate(sorted(energies_m, reverse=True)), 1):
                assert val <= float(z*q)+2e-12
                assert val+float(b) <= float(z*q+b)+2e-12
                prefixes += 2
            if e == 0:
                cap_a = Fraction(k, p-k)
                cap_m = Fraction(p*k, (p-1)*(p-k))
                assert a <= cap_a and b <= cap_m and q <= cap_m
            if s == [0] or s == list(range(1, p)):
                assert b == 1 and q == 0
                exception_controls += 1
            count += 1
    receipt = {'passed': True, 'all_nonconstant_indicators': count,
               'projection_prefix_controls': prefixes,
               'zero_completion_exceptions': exception_controls,
               'largest_basis_energy_error': max_error,
               'arithmetic': 'Exact rational coefficient caps; double-precision character coefficients with 2e-12 tolerance.',
               'scope': 'Finite controls of the all-prime algebraic proof, not an asymptotic empirical claim.'}
    Path(__file__).with_name('INDICATOR-CHECK-RESULTS.json').write_text(json.dumps(receipt, indent=2)+'\n')
    print(json.dumps(receipt))


if __name__ == '__main__':
    main()
