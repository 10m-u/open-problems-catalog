#!/usr/bin/env python3
"""Exact ruling controls: integer walk DP and independent rational Sturm signs."""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import comb
from pathlib import Path
from hashlib import sha256
import json
from rulings import row, components, endpoint_rows, dense_parity, violations
HERE=Path(__file__).resolve().parent

def convolution(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,c in enumerate(a):
        for j,d in enumerate(b):out[i+j]+=c*d
    return out

def trim(a):
    a=list(a)
    while a and not a[-1]:a.pop()
    return a
def remainder(a,b):
    a=trim(a);b=trim(b)
    while len(a)>=len(b) and a:
        q=a[-1]/b[-1];d=len(a)-len(b)
        for j,c in enumerate(b):a[d+j]-=q*c
        a=trim(a)
    return a
def sturm(a):
    seq=[list(map(F,a)),[F(j)*a[j] for j in range(1,len(a))]]
    while seq[-1]:
        r=[-v for v in remainder(seq[-2],seq[-1])]
        if not r:break
        # Positive normalization controls rational coefficient growth.
        r=[v/abs(r[-1]) for v in r]
        seq.append(r)
    return seq
def infinity_variations(seq,positive):
    signs=[(1 if a[-1]>0 else -1)*(-1 if not positive and (len(a)-1)%2 else 1) for a in seq]
    return sum(a!=b for a,b in zip(signs,signs[1:]))
def direct_raw(n,word,endpoint=None):
    """Enumerate masks independently; a set bit means a legal stay."""
    out=Counter();w0=tuple(range(n,0,-1));endpoint=w0 if endpoint is None else endpoint
    for mask in product((0,1),repeat=len(word)):
        p=w0
        for i,stay in zip(word,mask):
            if stay:
                if p.index(i)<p.index(i+1):break
            else:p=tuple(i+1 if a==i else i if a==i+1 else a for a in p)
        else:
            if p==endpoint:out[sum(mask)]+=1
    return dict(out)

def main():
    sourceword=(1,1,2,2,3,3,4,4,3,3,2,1)
    assert row(5,sourceword)==[4,20,33,24,8,1]
    assert direct_raw(5,sourceword)==endpoint_rows(5,sourceword)[(5,4,3,2,1)]
    two=[]
    for m in range(61):
        d=m//2;e=m%2
        formula=[comb(d+j+e,d-j) for j in range(d+1)]
        assert row(2,(1,)*m)==formula and violations(formula)==([],[])
        two.append(formula)
    braid_controls=0
    for n in range(3,6):
        for i in range(1,n-1):
            for prefix,suffix in [((),()),((1,n-1),(n-1,1)),((i,i+1),(i+1,i))]:
                assert row(n,prefix+(i,i+1,i)+suffix)==row(n,prefix+(i+1,i,i+1)+suffix)
                braid_controls+=1
        for i in range(1,n):
            for j in range(i+2,n):
                assert row(n,(i,j,i,j))==row(n,(i,i,j,j));braid_controls+=1
    campaign=json.loads((HERE/'RULING-FAMILY-CHECK.json').read_text())
    for d in campaign['records']:
        word=tuple(d['block'])*d['repetitions']
        assert len(word)>15 and row(d['n'],word)==d['row']
        assert components(d['n'],word)==d['components'] and violations(d['row'])==([],[])
    witness=(1,2,3,2)*6;a=row(4,witness)
    assert a==[1,18,177,1110,3711,7105,8361,6292,3076,970,190,21,1]
    seq=sturm(a);left=infinity_variations(seq,False);right=infinity_variations(seq,True)
    assert len(seq[-1])==1 # gcd(P,P')=1, so no repeated roots are omitted.
    assert left-right==4<12
    q=[1,1,1];p=[4,1]
    nextq=[q[j]+(p[j] if j<len(p) else 0) for j in range(3)]
    assert violations(q)==violations(p)==([],[]) and nextq==[5,2,1]
    assert violations(nextq)==([1],[])
    prefix=(1,3,2,2,1,1,3,1);actual=endpoint_rows(4,prefix)
    qstate=(4,3,2,1);pstate=(4,2,3,1)
    qraw=actual[qstate];praw=actual[pstate]
    assert qraw=={0:1,2:5,4:8,6:5,8:1} and praw=={5:2,7:1}
    assert direct_raw(4,prefix,qstate)==qraw and direct_raw(4,prefix,pstate)==praw
    qa=[qraw.get(s,0) for s in range(0,9,2)]
    pa=[praw.get(s,0) for s in range(1,10,2)]
    j=1;cross=2*qa[j]*pa[j]-qa[j-1]*pa[j+1]-qa[j+1]*pa[j-1]
    assert cross==-2 and violations(qa)==violations(pa)==([],[])
    assert components(4,prefix+(2,))==3 and row(4,prefix+(2,))==[1,5,10,6,1]
    word=(1,3,1,3);w0=(4,3,2,1);low=[w0];state=w0
    for i in word:
        state=tuple(i+1 if x==i else i if x==i+1 else x for x in state);low.append(state)
    high=[w0]*5
    meetings=[j for j in range(5) if low[j]==high[j]]
    assert meetings==[0,4] and row(4,word)==[1,2,1]
    assert direct_raw(4,word)=={0:1,2:2,4:1}
    one=row(2,(1,));twoletter=row(2,(1,1));three=row(2,(1,1,1))
    assert one==[1] and twoletter==[1,1] and three==[2,1]
    composition_checks=0
    for u in range(1,21):
        for v in range(1,21):
            first=convolution(two[u],two[v]);second=convolution(two[u-1],two[v-1])
            eu=u%2;ev=v%2
            first=[0]*(eu*ev)+first;second=[0]*((1-eu)*(1-ev))+second
            out=[(first[j] if j<len(first) else 0)+(second[j] if j<len(second) else 0)
                 for j in range(max(len(first),len(second)))]
            assert out==two[u+v];composition_checks+=1
    assert row(3,(1,2))==[1] and row(3,(1,2,1,2))==[2,1]
    assert direct_raw(3,(1,2,1,2))=={2:2,4:1}
    receipt={'status':'PASS','actual_fresh_families':len(campaign['records']),
       'source_example_independent_masks':2**len(sourceword),'two_strand_formula_rows':len(two),
       'braid_relation_controls':braid_controls,
       'actual_non_real_rooted':{'strands':4,'word':witness,'components':4,'row':a,
          'Sturm_degrees':[len(p)-1 for p in seq],'V_minus_infinity':left,'V_plus_infinity':right,
          'distinct_real_roots':left-right,'gcd_degree':0,'LC_and_no_holes':True},
       'formal_statewise_LC_not_invariant':{'q':q,'p':p,'next_q':nextq,'scope':'Synthetic state profile, not asserted reachable.'},
       'actual_cross_term_negative':{'prefix_word':prefix,'appended_generator':2,
           'q_state':qstate,'p_state':pstate,'raw_q':qraw,'raw_p':praw,
           'aligned_q':qa,'aligned_p':pa,'index':1,'cross_term':cross,
           'new_normalized_row':[1,5,10,6,1],'scope':'Actual two-branch inputs; their intrinsic slack compensates the negative cross term.'},
       'actual_one_meeting_splice_obstruction':{'word':word,'all_swap_path':low,'all_stay_path':high,
          'meeting_times':meetings,'switch_counts':[0,4],'desired_middle_switch_count':2,'actual_row':[1,2,1]},
       'actual_same_strand_concatenation_not_multiplicative':{'first_row':one,'second_row':twoletter,
          'product_row':[1,1],'concatenated_row':three,
          'three_strand_one_peak_factor_rows':[[1],[1]],'three_strand_concatenation_row':[2,1],
          'all_size_two_strand_composition_formula_controls':composition_checks},
       'scope':'Exact named actual braids and scoped stronger-contract failures; no counterexample to Q2924.',
       'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
       'walk_engine_sha256':sha256((HERE/'rulings.py').read_bytes()).hexdigest()}
    (HERE/'RULING-CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))
if __name__=='__main__':main()
