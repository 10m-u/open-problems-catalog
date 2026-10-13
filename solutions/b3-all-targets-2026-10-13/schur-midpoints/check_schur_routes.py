from collections import defaultdict
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json
import random

from lr import midpoint, product, lr_coefficient

HERE=Path(__file__).resolve().parent


def difference(a,b,c,d):
    out=defaultdict(F)
    for sign,A,B in [(1,c,d),(-1,a,b)]:
        for x,u in A.items():
            for y,v in B.items():
                for nu,k in product(x,y).items():
                    out[nu]+=sign*u*v*k
    return {nu:v for nu,v in out.items() if v}


def encode(A):
    return [{'partition':list(p),'weight':str(v)} for p,v in sorted(A.items())]


def main():
    assert product((1,),(1,))=={(2,):1,(1,1):1}
    assert product((2,),(1,))=={(3,):1,(2,1):1}
    assert product((1,1),(1,1))=={(2,2):1,(2,1,1):1,(1,1,1,1):1}
    # A1: all local hypotheses, but the summed fiber contract overspends.
    a=b={():F(1),(2,):F(1)}
    c=d={():F(1),(1,):F(1),(2,):F(1)}
    for x,u in a.items():
        for y,v in b.items():
            up,down=midpoint(x,y)
            assert u*v<=c.get(up,0)*d.get(down,0)
    actual=difference(a,b,c,d)
    assert actual=={(1,):F(2),(2,):F(1),(1,1):F(1),(3,):F(2),(2,1):F(2)}
    push=defaultdict(F)
    for x,u in a.items():
        for y,v in b.items():
            up,down=midpoint(x,y)
            for nu,k in product(up,down).items():push[nu]+=u*v*k
    cd=difference({}, {}, c,d)
    residual={nu:cd.get(nu,0)-push.get(nu,0) for nu in cd.keys()|push.keys()}
    assert residual[(1,1)]==-1
    # A2 singleton actual midpoint hypothesis versus min/max condition.
    assert midpoint((),(2,))==((1,),(1,))
    assert difference({():F(1)},{(2,):F(1)},{(1,):F(1)},{(1,):F(1)})=={(1,1):F(1)}
    # A4 actual same-output LR pairs; uniform ceil leaves that output degree.
    assert lr_coefficient((),(2,),(2,))==1
    assert lr_coefficient((1,),(1,),(2,))==1
    assert lr_coefficient((1,),(2,),(2,))==0
    assert lr_coefficient((),(1,),(2,))==0

    big=[(11,),(12,),(8,2,1),(7,3,1),(7,2,1,1),(6,3,2,1)]
    small=[(),(1,),(2,),(1,1),(2,1),(2,1,1),(2,2,1),(3,1,1,1),(3,2,1)]
    rng=random.Random(4665)
    records=[]
    for ix in range(32):
        A=rng.sample(big,2);B=rng.sample(small,2)
        a={x:F(rng.randrange(1,6)) for x in A}
        b={x:F(rng.randrange(1,6)) for x in B}
        ups={midpoint(x,y)[0] for x in A for y in B}
        c={x:F(rng.randrange(1,6)) for x in sorted(ups)}
        d={}
        for x,u in a.items():
            for y,v in b.items():
                up,down=midpoint(x,y)
                d[down]=max(d.get(down,F(0)),u*v/c[up])
        assert all(a[x]*b[y]<=c[midpoint(x,y)[0]]*d[midpoint(x,y)[1]] for x in A for y in B)
        row=difference(a,b,c,d)
        assert all(v>=0 for v in row.values())
        assert all(sum(x)>10 for x in A)
        records.append({'index':ix,'a':encode(a),'b':encode(b),'c':encode(c),'d':encode(d),
                        'Schur_difference':encode(row),'negative_coefficients':0})
    out={'status':'PASS','scope':'One bounded fresh weighted counter-construction; no all-size conjecture conclusion',
         'actual_fiber_budget_failure':{'a':encode({():F(1),(2,):F(1)}),
            'fiber_at_1_1_input_weight':2,'output_budget':1,
            'actual_difference':encode(actual),'CD_minus_pushed_negative_s11':-1},
         'same_output_uniform_rounding_failure':{'nu':[2],'inputs':[[[],[2]],[[1],[1]]],
                                               'rounded_degrees':[3,1]},
         'fresh_weighted_records':records,
         'pair_product_cache':str(product.cache_info()),
         'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
         'lr_sha256':sha256((HERE/'lr.py').read_bytes()).hexdigest()}
    (HERE/'SCHUR-ROUTES-CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':'PASS','fresh_cases':len(records),'products':product.cache_info().currsize}))


if __name__=='__main__':main()
