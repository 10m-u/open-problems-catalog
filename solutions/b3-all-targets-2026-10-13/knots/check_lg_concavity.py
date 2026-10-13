#!/usr/bin/env python3
"""Exact formal controls for specific LG proof contracts, not knot enumeration."""
from itertools import product, combinations
from collections import Counter
from pathlib import Path
from hashlib import sha256
import json
HERE=Path(__file__).resolve().parent
def add(a,d):return tuple(x+y for x,y in zip(a,d))
def mul(P,Q):
    out=Counter()
    for a,c in P.items():
        for b,d in Q.items():out[add(a,b)]+=c*d
    return {a:c for a,c in out.items() if c}
def b_candidates(P,a,b,i):
    ds=[];d=[0,0];d[i]=-1;ds.append(tuple(d))
    for j in range(2):
        if a[j]<b[j]:
            d=[0,0];d[i]=-1;d[j]+=1;ds.append(tuple(d))
        if j!=i and a[j]>b[j]:
            d=[0,0];d[i]=-1;d[j]-=1;ds.append(tuple(d))
    return [(d,P.get(add(a,d),0)*P.get(add(b,tuple(-v for v in d)),0)) for d in ds]
def main():
    P={(x,y):2**min(x,2*y) for x,y in product(range(3),repeat=2)}
    a=(2,1);b=(0,0);input_product=P[a]*P[b]
    candidates=b_candidates(P,a,b,0)
    assert input_product==4 and [v for d,v in candidates]==[2,2]
    negative={(0,0):-1,(2,2):2}
    specializations=[]
    for sign in (1,-1):
        out=Counter()
        for (x,y),c in negative.items():out[x-y]+=c*sign**y
        out={k:v for k,v in out.items() if v}
        assert out=={0:1}
        specializations.append(dict(out))
    grid=[[16,4,1],[4,8,16],[1,16,4]]
    G={(x,y):grid[x][y] for x,y in product(range(3),repeat=2)}
    midpoint_checks=0
    for aa,bb in combinations(G,2):
        if any((aa[j]+bb[j])%2 for j in range(2)):continue
        mid=tuple((aa[j]+bb[j])//2 for j in range(2))
        assert G[mid]**2>=G[aa]*G[bb]
        midpoint_checks+=1
    triangle=[(0,0),(2,1),(1,2)];center=(1,1)
    assert tuple(sum(a[j] for a in triangle)//3 for j in range(2))==center
    assert G[center]**3==512 < 4096==G[triangle[0]]*G[triangle[1]]*G[triangle[2]]
    characteristic=mul(mul({(1,0,0):1,(0,0,0):1},
                          {(1,0,0):1,(0,1,0):1}),
                          {(1,0,0):1,(0,0,1):1})
    assert characteristic=={(3,0,0):1,(2,0,0):1,(2,1,0):1,(2,0,1):1,
        (1,1,0):1,(1,0,1):1,(1,1,1):1,(0,1,1):1}
    # Sign twist h=-g still forces a negative coefficient on h.
    recurrence={a:(-1)**a[0]*c for a,c in characteristic.items() if a[0]!=3}
    assert recurrence[(1,1,0)]==recurrence[(1,0,1)]==recurrence[(1,1,1)]==-1
    A={(0,0):1,(1,1):1};B={(0,2):1,(1,1):1,(2,0):1}
    AB=mul(A,B);hole=(1,2)
    assert AB=={(0,2):1,(1,1):1,(2,0):1,(1,3):1,(2,2):1,(3,1):1}
    assert hole not in AB and (0,2) in AB and (2,2) in AB
    assert tuple(((0,2)[j]+(2,2)[j])//2 for j in range(2))==hole
    receipt={'status':'PASS','formal_concave_extendable_not_type_B':{
        'coefficient_grid':[[P[x,y] for y in range(3)] for x in range(3)],
        'extension':'min(x,2y)*log(2)','alpha':a,'beta':b,'coordinate':1,
        'input_product':input_product,'all_candidates':candidates},
        'Alexander_kernel_formal_negative_polynomial':{str(a):c for a,c in negative.items()},
        'both_Alexander_specializations':specializations,
        'all_lattice_line_LC_not_concave_extendable':{
            'coefficient_grid':grid,'all_midpoint_checks':midpoint_checks,
            'triangle':triangle,'center':center,'center_cubed':512,'vertex_product':4096,
            'scope':'Full 3x3 lattice square, symmetric positive integer coefficients; not a knot invariant.'},
        'actual_R1_sign_substitution':{'g_characteristic':{str(a):c for a,c in characteristic.items()},
            'sign_twisted_h3_recurrence':{str(a):c for a,c in recurrence.items()},
            'scope':'Algebraic identity from primary R1; no claim that its closures remain alternating knots.'},
        'formal_connected_sum_class_not_closed':{
            'factor_A':{str(a):c for a,c in A.items()},'factor_B':{str(a):c for a,c in B.items()},
            'product':{str(a):c for a,c in AB.items()},'missing_convex_hull_lattice_point':hole,
            'scope':'Both factors are symmetric, positive, hole-free and concave extendable; neither asserted an LG invariant.'},
        'scope':'Formal exact contract witnesses; named actual non-type-B knots are primary-source evidence, not recomputed here.',
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (HERE/'LG-CONCAVITY-CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))
if __name__=='__main__':main()
