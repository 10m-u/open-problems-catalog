"""Complete zero-sum-free sequence state searches on declared finite groups."""
import itertools
import json
from math import gcd
from pathlib import Path


def solve(moduli):
    elements=list(itertools.product(*(range(m) for m in moduli)))
    index={v:i for i,v in enumerate(elements)}
    n=len(elements)
    add=[[index[tuple((a+b)%m for a,b,m in zip(x,y,moduli))] for y in elements] for x in elements]
    neg=[index[tuple((-a)%m for a,m in zip(x,moduli))] for x in elements]
    cache={}
    def translated(mask,g):
        key=mask,g
        if key not in cache:
            cache[key]=sum(1<<add[x][g] for x in range(n) if mask>>x&1)
        return cache[key]
    values=[0]*n
    states={(1,0):0}
    buckets=[set() for _ in range(n+1)]
    buckets[1].add((1,0))
    for size in range(1,n+1):
        for mask,total in buckets[size]:
            length=states[mask,total]
            values[total]=max(values[total],length)
            for g in range(1,n):
                if mask>>neg[g]&1:
                    continue
                new=mask|translated(mask,g)
                assert new.bit_count()>size
                nt=add[total][g]
                key=new,nt
                if states.get(key,-1)<length+1:
                    states[key]=length+1
                    buckets[new.bit_count()].add(key)
    assert values[0]==0
    if len(moduli)==1:
        assert values==[n-gcd(n,g) for g in range(n)]
    subgroups={frozenset({0})}
    queue=list(subgroups)
    while queue:
        h=queue.pop()
        for g in range(n):
            generated=set(h)
            z=g
            while z:
                generated.update(add[x][z] for x in h)
                z=add[z][g]
            new=frozenset(generated)
            if new not in subgroups:
                subgroups.add(new);queue.append(new)
    controls=0
    for h in subgroups:
        for g in range(n):
            alpha={add[g][x] for x in h}
            da=max(values[x] for x in alpha)
            z=0
            for _ in range(n):
                beta={add[z][x] for x in h}
                assert da>=max(values[x] for x in beta)
                controls+=1
                z=add[z][g]
    return {"moduli":moduli,"order":n,"singleton_values":values,
            "exact_states":len(states),"coset_monotonicity_controls":controls}


def main():
    groups=[(n,) for n in range(2,13)]+[(2,2),(2,4),(3,3),(2,2,2)]
    rows=[solve(m) for m in groups]
    out={"passed":True,"groups":rows,"max_order":12,
         "scope":"Complete sequences and cosets in the named finite groups, not all-group monotonicity"}
    Path(__file__).with_name("DAVENPORT-CHECK.json").write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps({"passed":True,"groups":len(rows),"states":sum(r["exact_states"] for r in rows)}))


if __name__=="__main__":
    main()
