"""Exact controls for the finite-state coefficient reduction, not its uniform conjecture."""
import itertools
import json
import random
from pathlib import Path


def multiply(a, b, p):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % p
    return out


def polynomial(m, p):
    a = [1]
    for r, exponent in enumerate(m, 1):
        for _ in range(exponent):
            a = multiply(a, [-r % p, 1], p)
    return a


def coefficient(m, n, p):
    state = [1] + [0] * (p - 1)
    while any(m) or n:
        block = polynomial([x % p for x in m], p)
        digit = n % p
        new = [0] * p
        for c, weight in enumerate(state):
            for target in range(p):
                j = digit + p * target - c
                if 0 <= j < len(block):
                    new[target] += weight * block[j]
        state = [x % p for x in new]
        m = [x // p for x in m]
        n //= p
    # Remaining zero digits with identity blocks discard positive carries.
    while any(state[1:]):
        state = [sum(state[c] for c in range(p) if c == p*t) % p
                 for t in range(p)]
    return state[0]


def main():
    rng = random.Random(1613)
    checks = 0
    admissible = {}
    for p in [2, 3, 5, 7]:
        examples = list(itertools.product(range(5), repeat=p-1)) if p <= 3 else [tuple(rng.randrange(21) for _ in range(p-1)) for _ in range(80)]
        degrees = set()
        for exponents in examples:
            direct = polynomial(exponents, p)
            for n, value in enumerate(direct):
                assert coefficient(list(exponents), n, p) == value
                checks += 1
            if all(direct):
                degrees.add(sum(exponents))
        admissible[str(p)] = sorted(degrees)
    out = {"status": "passed", "exact_coefficient_comparisons": checks,
           "bounded_admissible_degrees": admissible,
           "scope": "Tests finite carry transition against direct polynomial multiplication; not uniform digit boundedness"}
    Path(__file__).with_name("DIGIT-CARRY-CHECK.json").write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(out))


if __name__ == '__main__':
    main()
