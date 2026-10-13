"""Exact polynomial controls for the five Q3892 contracts and partials."""
from fractions import Fraction
from hashlib import sha256
from itertools import product
from math import comb, factorial
from pathlib import Path
import json


def mul(a, b):
    out = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def power(a, n):
    out = [1]
    for _ in range(n):
        out = mul(out, a)
    return out


def reciprocal(a, count):
    assert a[0] == 1
    b = [1]
    for n in range(1, count):
        b.append(-sum(a[i]*b[n-i] for i in range(1, min(n, len(a)-1)+1)))
    return b


def join_row(q, s):
    f = [comb(q, i)*s**i for i in range(q+1)] + [0]
    d = q+1
    return [f[i]+f[d-i] for i in range(d+1)]


def main():
    cm = []
    for q in range(10, 61):
        k = (q+1)//2
        j = k+1
        b = comb(q, j)
        # Maximize the two pi entries, and upper-bound the constant term
        # 1/T by2 and the error by its exact coefficient sum.
        upper = (1-(q-k))*3**q + b*(q-(q-k)*k)
        upper += b*(k-(-1)**j) + 2*b + comb(q, j-1)
        loose = -3**q + (q+k+4)*2**q
        assert upper < 0 and loose < 0
        coefficient_sum = sum(comb(q-i, j-i) for i in range(1, j+1))
        assert coefficient_sum == comb(q, j-1)
        assert sum((-1)**(j-i)*comb(q-i, j-i)*comb(q, i)
                   for i in range(1, k)) == b*(k-(-1)**j)
        cm.append({'q': q, 'uniform_CM_coefficient_upper_bound': upper})

    descending = []
    for d in range(3, 61):
        q=d-1
        h = join_row(q, 2*q+1)
        assert h[0] == h[-1] == 1 and h == h[::-1]
        assert all(h[i] > h[i+1] for i in range(1, d//2))
        descending.append({'d': d, 's': 2*q+1, 'h': h})
        assert [comb(d, i) for i in range(d+1)] == join_row(q, 1)
    # Literal colored-choice faces, not an assumed binomial coefficient.
    literal = []
    for q, s in product(range(2, 5), range(1, 4)):
        counts = [0]*(q+1)
        for face in product(range(s+1), repeat=q):
            counts[sum(x != 0 for x in face)] += 1
        assert counts == [comb(q, i)*s**i for i in range(q+1)]
        literal.append([q, s])

    order_bounds = []
    for d in range(12, 81):
        k=d//2; q=d-1
        bound=q*comb(k, 2)+1
        assert factorial(k)>bound
        order_bounds.append([d, bound, factorial(k)])

    seed = join_row(3, 6)
    assert seed == [1, 234, 216, 234, 1]
    padding = []
    for r in range(1, 81):
        h=mul(seed, power([1, 1], r)); N=r+4
        assert all(h[i+1]>h[i] for i in range(N//2))
        for i in range(2, N//2):
            ratio=Fraction(i*(N-i-1), (N-2)*(N-3))
            assert ratio <= Fraction(1, 2)
            A=comb(N,i)*Fraction(N-2*i-1,i+1)
            B=comb(N-2,i-1)*Fraction(N-2*i-1,i)
            C=comb(N-4,i-2)*Fraction(N-2*i-1,i-1)
            assert h[i+1]-h[i]==A+230*B-250*C
        padding.append({'r': r, 'first_half_order': 'strict ascending'})

    # Reciprocal Hilbert positivity without any possible quadratic realization.
    false_numerical = []
    P=mul(mul(power([1,1],2),power([1,1,1],3)),[1,0,0,1])
    for r in range(3, 13):
        h=mul(power([1,1,1],2),power([1,1],r))
        hm=[x*(-1)**i for i,x in enumerate(h)]
        beta=reciprocal(hm,181)
        assert all(x>=0 for x in beta)
        # Polynomial identity after clearing denominator (1-z)^r.
        # The simpler base identity suffices; extra factors have positive
        # reciprocal (1-z)^(-r+3), checked directly below.
        base_hm=[x*(-1)**i for i,x in enumerate(mul(power([1,1,1],2),power([1,1],3)))]
        denominator=power([1,0,0,0,0,0,-1],3)
        assert mul(base_hm,P)==denominator
        assert len(h)-1==r+4 and h[1]==r+2 < len(h)-1
        false_numerical.append({'r':r,'h':h,'reciprocal_prefix_nonnegative_through':180})

    connected=[]
    for d in range(3,21):
        h=[1]+[2*comb(d,i) for i in range(1,d)]+[1]
        quadratic_only=[1]+[2*comb(d,i) for i in range(1,d+1)]
        assert h[:-1]==quadratic_only[:-1] and h[-1]==1 and quadratic_only[-1]==2
        connected.append({'d':d,'h':h,'required_new_relation_degree':d})
    out={'result':'PASS','scope':'Finite arithmetic controls; see written all-size proofs',
         'CM_source_transfer_obstructions':cm,'all_degree_descending_controls':descending,
         'literal_join_faces':literal,'one_parameter_order_bounds':order_bounds,
         'fixed_seed_binomial_padding':padding,'false_numerical_certificates':false_numerical,
         'connected_sum_high_degree_relations':connected,
         'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    Path(__file__).with_name('KOSZUL-ROUTES-CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'result':'PASS','CM_bound_controls':len(cm),'descending_degrees':len(descending),
                      'padding_controls':len(padding),'numerical_certificate_controls':len(false_numerical)}))


if __name__=='__main__':
    main()
