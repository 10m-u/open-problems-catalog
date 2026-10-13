"""Independent Jacobi--Trudi/Pieri audit of the saved LR products.

Only the final comparison calls lr.product. All independent expansions
use horizontal-strip interlacing and the determinant permutation formula.
"""
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from itertools import permutations, product as cartesian
from pathlib import Path
import json

import lr


@lru_cache(None)
def pieri(shape, r):
    if r < 0:
        return ()
    if not shape:
        return ((r,),) if r else ((),)
    old = shape+(0,)
    answer = []

    def extend(i, remaining, lower_increments):
        if i == 0:
            out = (old[0]+remaining,)+tuple(old[j]+lower_increments[j]
                                          for j in range(1, len(old)))
            answer.append(tuple(x for x in out if x))
            return
        for delta in range(min(old[i-1]-old[i], remaining)+1):
            lower_increments[i] = delta
            extend(i-1, remaining-delta, lower_increments)
    extend(len(old)-1, r, {})
    return tuple(answer)


@lru_cache(None)
def jt_product(a, b):
    # Expand the shorter Jacobi--Trudi determinant, without using LR symmetry
    # as an algorithmic identity beyond commutativity of multiplication.
    if len(a) < len(b):
        a, b = b, a
    out = defaultdict(int)
    for perm in permutations(range(len(b))):
        indices = [b[i]-i+perm[i] for i in range(len(b))]
        if min(indices, default=0) < 0:
            continue
        sign = (-1)**sum(perm[i] > perm[j] for i in range(len(b))
                         for j in range(i+1, len(b)))
        current = {a: 1}
        for r in sorted(indices):
            nxt = defaultdict(int)
            for shape, count in current.items():
                for bigger in pieri(shape, r):
                    nxt[bigger] += count
            current = nxt
        for shape, count in current.items():
            out[shape] += sign*count
    result = {k: v for k, v in out.items() if v}
    assert all(v > 0 for v in result.values())
    return result


def decode(rows):
    return {tuple(row['partition']): Fraction(row['weight']) for row in rows}


def midpoint(a, b):
    sums = [x+y for x,y in zip(a+(0,)*max(0,len(b)-len(a)),
                               b+(0,)*max(0,len(a)-len(b)))]
    return tuple((x+1)//2 for x in sums if x), tuple(x//2 for x in sums if x//2)


def expansion(A, B):
    out = defaultdict(Fraction)
    for a, x in A.items():
        for b, y in B.items():
            for shape, count in jt_product(a, b).items():
                out[shape] += x*y*count
    return {k:v for k,v in out.items() if v}


def main():
    here = Path(__file__)
    saved_path = here.with_name('SCHUR-ROUTES-CHECK.json')
    saved = json.loads(saved_path.read_text())
    pairs = {((1,), (1,)), ((2,), (1,)), ((1,1), (1,1))}
    control_a = {():Fraction(1), (2,):Fraction(1)}
    control_c = {():Fraction(1), (1,):Fraction(1), (2,):Fraction(1)}
    pairs.update(cartesian(control_a, repeat=2))
    pairs.update(cartesian(control_c, repeat=2))
    pairs.add(((1,), (1,)))
    weighted = []
    for record in saved['fresh_weighted_records']:
        a,b,c,d = [decode(record[key]) for key in ['a','b','c','d']]
        pairs.update(cartesian(a,b))
        pairs.update(cartesian(c,d))
        for x,u in a.items():
            for y,v in b.items():
                up, down = midpoint(x,y)
                assert u*v <= c.get(up,0)*d.get(down,0)
        cd, ab = expansion(c,d), expansion(a,b)
        actual = {k:cd.get(k,0)-ab.get(k,0) for k in cd.keys()|ab.keys()}
        actual = {k:v for k,v in actual.items() if v}
        assert actual == decode(record['Schur_difference'])
        assert all(v >= 0 for v in actual.values())
        weighted.append(record['index'])
    comparison = []
    for a,b in sorted(pairs):
        actual = jt_product(a,b)
        assert actual == lr.product(a,b), (a,b,actual,lr.product(a,b))
        comparison.append({'a':list(a),'b':list(b), 'output_shapes':len(actual)})
    # Saved cache has 233 products; require coverage instead of assuming it.
    assert len(pairs) == 233, len(pairs)
    cd, ab = expansion(control_c,control_c), expansion(control_a,control_a)
    actual = {k:cd.get(k,0)-ab.get(k,0) for k in cd.keys()|ab.keys()}
    actual = {k:v for k,v in actual.items() if v}
    assert actual == decode(saved['actual_fiber_budget_failure']['actual_difference'])
    pushed = defaultdict(Fraction)
    for x,y in cartesian(control_a, repeat=2):
        up,down = midpoint(x,y)
        for nu,k in jt_product(up,down).items():
            pushed[nu] += k
    assert cd.get((1,1),0)-pushed.get((1,1),0) == -1
    for N in range(2, 21):
        assert jt_product((),(N,)).get((N,)) == 1
        assert jt_product((1,),(N-1,)).get((N,)) == 1
        assert jt_product((1,),(N,)).get((N,),0) == 0
        assert jt_product((),(N-1,)).get((N,),0) == 0
    out = {'result':'PASS', 'method':'Jacobi--Trudi determinant with independent Pieri interlacing',
           'independent_of':'LR tableau enumeration; lr.product used only for comparison',
           'compared_products':comparison, 'product_count':len(pairs),
           'recomputed_weighted_differences':len(weighted),
           'actual_fiber_budget_negative_coefficient':-1,
           'fixed_output_degree_controls_N':[2,20],
           'checker_sha256':sha256(here.read_bytes()).hexdigest(),
           'submitted_receipt_sha256':sha256(saved_path.read_bytes()).hexdigest()}
    here.with_name('SCHUR-REVIEW-CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'result':'PASS','products':len(pairs),'weighted_cases':len(weighted)}))


if __name__ == '__main__':
    main()
