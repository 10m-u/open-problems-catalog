"""Exact Bernoulli inequalities and declared finite numerical-law controls."""
import json
import math
import random
from collections import defaultdict
from pathlib import Path


def entropy(p):
    return -sum(v*math.log2(v) for v in p.values() if v)


def output(p, operation):
    q=defaultdict(float)
    for x,px in p.items():
        for y,py in p.items():
            q[operation(x,y)] += px*py
    return q


def ratio(p):
    h=entropy(p)
    s=entropy(output(p,lambda x,y:x+y))
    d=entropy(output(p,lambda x,y:x-y))
    return (d-h)/(s-h) if s-h>1e-9 else None


def main():
    assert 10**100 > 3**180 * 2**18
    assert 3**1152 * 2**72 > 10**100 * 82**246
    bernoulli=ratio({0:.9,1:.1})
    controls=0
    for n in range(2,65):
        p={i:1/n for i in range(1,n+1)}
        assert abs(ratio(p)-1)<1e-10
        geometric={2**i:1/n for i in range(n)}
        s=entropy(output(geometric,lambda x,y:x+y))
        assert abs(s-(2*math.log2(n)-1+1/n))<1e-10
        controls+=2
    rng=random.Random(20261012)
    best={"ratio":bernoulli,"law":[[0,.9],[1,.1]]}
    searches=12000
    for _ in range(searches):
        support=sorted(rng.sample(range(-12,13),rng.randrange(2,8)))
        weights=[rng.expovariate(1)**rng.choice([1,2,3]) for x in support]
        total=sum(weights)
        p={x:w/total for x,w in zip(support,weights)}
        r=ratio(p)
        if r is not None and r>best["ratio"]:
            best={"ratio":r,"law":list(p.items())}
    out={"passed":True,"bernoulli_ratio":bernoulli,
         "exact_integer_comparison_proves_ratio_above":"4/3",
         "uniform_interval_and_power_progression_controls":controls,
         "weighted_laws_tested":searches,"best_numerical_witness":best,
         "scope":"Exact analytic Bernoulli lower bound plus finite floating-point controls; no global numerical optimum or sharp constant"}
    Path(__file__).with_name("ENTROPY-CHECK.json").write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps(out))


if __name__=="__main__":
    main()
