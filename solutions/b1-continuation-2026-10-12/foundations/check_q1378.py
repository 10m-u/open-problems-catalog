"""Independent exact controls for finite-QE routes."""
from itertools import product
import json
from pathlib import Path


def value(t, x):
    if t == 'x':
        return x
    if isinstance(t, int):
        return t
    op = t[0]
    if op == '+':
        return value(t[1], x) + value(t[2], x)
    if op == 'v':
        a = value(t[1], x)
        return 0 if a == 0 else a & -a
    return value(t[2], x) // t[1]


def ord2(a):
    return (a & -a).bit_length() - 1


class Refine(Exception):
    def __init__(self, modulus, residue):
        self.modulus, self.residue = modulus, residue


def affine(t, slope, offset):
    if t == 'x':
        return slope, offset
    if isinstance(t, int):
        return 0, t
    if t[0] == '+':
        a,b = affine(t[1], slope, offset)
        c,d = affine(t[2], slope, offset)
        return a+c,b+d
    if t[0] == 'v':
        a,b = affine(t[1], slope, offset)
        if a == 0:
            return 0, (0 if b == 0 else b & -b)
        if b and ord2(a) > ord2(b):
            return 0, b & -b
        # Force n == 1 mod 2^L, preserving previously frozen nodes.
        exponent = max(1, ord2(a+b) - ord2(a) + 1)
        raise Refine(1 << exponent, 1)
    q = t[1]
    a,b = affine(t[2], slope, offset)
    if a % q:
        raise Refine(q, 0)
    return a//q,b//q


def carry_generators(q=3, k=2):
    maps = []
    for x,y in product(range(k), repeat=2):
        image = []
        for c in range(q):
            numerator = q*y+c-x
            image.append(numerator//k if numerator % k == 0 and 0 <= numerator//k < q else -1)
        maps.append(tuple(image))
    return maps


def compose(left, right):
    return tuple(-1 if right[x] == -1 else left[right[x]] for x in range(len(left)))


def quotient_graph(x, y):
    states = {0,1,2}
    length = max(1, x.bit_length(), y.bit_length())
    for j in range(length):
        xb,yb = (x>>j)&1,(y>>j)&1
        states = {(3*yb+c-xb)//2 for c in states
                  if (3*yb+c-xb)%2 == 0 and 0 <= (3*yb+c-xb)//2 < 3}
    return 0 in states


def in_k(x):
    if x == 0:
        return True
    s = bin(x)[2:]
    if len(s)%2:
        s = '0'+s
    return all(s[j:j+2] in ['01','10'] for j in range(0,len(s),2))


def main():
    terms = ['x',0,1,3,15, ('+','x',1),('+','x',3),('+','x',15),
             ('v','x'),('v',('+','x',1)),('v',('+','x',15)),
             ('+',('v','x'),'x'), ('v',('+',('v','x'),'x')),
             ('f',3,'x'), ('f',5,('+','x',1)),
             ('v',('f',3,'x')), ('f',5,('v',('+','x',3))),
             ('f',3,('+',('f',5,'x'),('v','x'))),
             ('v',('+',('f',3,'x'),('f',5,('+','x',1))))]
    slope,offset = 1,0
    refinements = 0
    while True:
        try:
            forms = [affine(t,slope,offset) for t in terms]
            break
        except Refine as refine:
            offset += slope * refine.residue
            slope *= refine.modulus
            refinements += 1
            assert refinements < 100
    remaining = slope
    for p in [2,3,5]:
        while remaining % p == 0:
            remaining //= p
    assert remaining == 1 and slope % 7 != 0
    term_controls = 0
    for n in range(151):
        for t,(a,b) in zip(terms,forms):
            assert value(t,slope*n+offset) == a*n+b
            term_controls += 1
    assert {((slope*n+offset)%7 == 0) for n in range(7)} == {False,True}

    generators = carry_generators()
    identity = tuple(range(3))
    monoid = {identity}
    frontier = [identity]
    while frontier:
        old = frontier.pop()
        for g in generators:
            new = compose(g,old)
            if new not in monoid:
                monoid.add(new)
                frontier.append(new)
    for g in monoid:
        h = identity
        for _ in range(3):
            h = compose(g,h)
        assert compose(g,h) == h, (g,h)
        for subset in range(8):
            image = lambda mask: sum(1<<g[x] for x in range(3)
                                    if mask&(1<<x) and g[x] >= 0)
            # Use a set, since two carry states can merge.
            def apply(mask):
                return sum(1<<y for y in {g[x] for x in range(3)
                           if mask&(1<<x) and g[x] >= 0})
            a = subset
            for _ in range(3):
                a = apply(a)
            assert apply(a) == a
    graph_controls = 0
    for x in range(256):
        for y in range(100):
            assert quotient_graph(x,y) == (y == x//3)
            graph_controls += 1
    cyclic_map = tuple((4*r+1)%3 for r in range(3))
    assert cyclic_map == (1,2,0)
    assert compose(cyclic_map,cyclic_map) != cyclic_map
    assert compose(cyclic_map,compose(cyclic_map,cyclic_map)) == identity
    for j in range(1,50):
        word_value = 2*(4**j-1)//3
        assert (word_value%3 == 0) == (j%3 == 0)

    sparse_counts = []
    for length in range(1,17):
        n = 1<<length
        actual = sum(in_k(x) for x in range(n))
        expected = 2**((length+1)//2)+2**(length//2)-1
        assert actual == expected
        sparse_counts.append(actual)
    receipt = dict(status="passed", term_controls=term_controls,
                   terms=len(terms), refinements=refinements,
                   progression_slope=slope, progression_offset=offset,
                   graph_controls=graph_controls,
                   quotient_graph_monoid_size=len(monoid),
                   nontrivial_residue_cycle=list(cyclic_map),
                   sparse_count_lengths=16, sparse_counts=sparse_counts,
                   scope="finite route controls; no unrestricted finite-QE decision")
    Path(__file__).with_name("Q1378-CHECK-RESULTS.json").write_text(json.dumps(receipt,indent=2)+"\n")
    print(json.dumps(receipt))


if __name__ == "__main__":
    main()
