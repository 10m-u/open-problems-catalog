#!/usr/bin/env python3
"""Direct selected-tuple expansion independently checks shuffle recursion."""
from collections import Counter
from itertools import combinations
from pathlib import Path
from hashlib import sha256
import json,runpy
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
root=runpy.run_path(str(ROOT/'shuffle-eigenvalues/check_eigenvalues.py'))
def partitions(n, bound=None):
    if not n:yield ();return
    for a in range(1,min(n,bound or n)+1):
        for tail in partitions(n-a,a):yield (a,)+tail
def cells(shape):return {(r,c) for r,a in enumerate(shape,1) for c in range(1,a+1)}
def expanded(j,contents,k):
    n=j+len(contents);answer=Counter()
    for selected in combinations(range(len(contents)),k):
        labels=[j+i+1 for i in selected]
        shift=n*k-k*(k-1)//2-sum(labels)
        term=Counter({shift:1})
        for m,i in enumerate(selected,1):
            length=j+i+2-m+contents[i]
            assert length>=1
            out=Counter()
            for a,c in term.items():
                for b in range(length):out[a+b]+=c
            term=out
        answer.update(term)
    degree=max(answer,default=0)
    return [answer[i] for i in range(degree+1)]
def main():
    strips=polys=endpoint=0
    for n in range(9):
        allmu=[mu for j in range(n+1) for mu in partitions(j)]
        for lam in partitions(n):
            outer=cells(lam)
            for mu in allmu:
                inner=cells(mu)
                if not inner<=outer:continue
                skew=outer-inner
                if len({c for r,c in skew})!=len(skew):continue
                contents=[c-r for r,c in sorted(skew)]
                j=sum(mu);N=len(skew)
                assert all(c>=-j for c in contents)
                recurrence=root['eigenvalues'](j,contents)
                for k in range(N+1):
                    p=expanded(j,contents,k)
                    assert p==recurrence[k]
                    assert root['unimodal'](p)
                    polys+=1
                if N:
                    one=Counter()
                    for index,c in enumerate(contents,1):
                        for t in range(N-index,n+c):one[t]+=1
                    assert [one[i] for i in range(max(one)+1)]==expanded(j,contents,1)
                    full=[1]
                    for c in contents:full=root['uniform'](full,j+1+c)
                    assert full==expanded(j,contents,N)==full[::-1]
                    endpoint+=2
                strips+=1
    actual=expanded(2,[1,-2],1)
    assert actual==[1,2,1,1,1]
    terms=[]
    for selected in combinations(range(3),2):
        term=Counter({8-1-sum(2+i for i in selected):1})
        for m,i in enumerate(selected,1):
            out=Counter()
            for a,c in term.items():
                for b in range(2+i+1-m+[1,2,-1][i]):out[a+b]+=c
            term=out
        terms.append([term[i] for i in range(max(term)+1)])
    mode_sets=[set(root['modes'](p)) for p in terms]
    assert not set.intersection(*mode_sets)
    large_cases=large_polys=0
    for j in (28,41,70,100):
        for N in (3,4):
            for b in range(2,N+1):
                lam=(j+N-b-1,b,1);mu=(j-1,1)
                skew=cells(lam)-cells(mu)
                assert cells(mu)<=cells(lam)
                assert len(skew)==N==len({c for r,c in skew})
                contents=[c-r for r,c in sorted(skew)]
                rec=root['eigenvalues'](j,contents)
                for k in range(2,N):
                    p=expanded(j,contents,k)
                    assert p==rec[k] and root['unimodal'](p)
                    large_polys+=1
                large_cases+=1
    receipt={'status':'PASS','all_horizontal_strips_through_n':8,
       'strips':strips,'direct_tuple_polynomials':polys,'endpoint_controls':endpoint,
       'selected_tuple_modes':[sorted(s) for s in mode_sets],
       'actual_lc_and_symmetry_obstruction':actual,
       'fresh_three_row_direct_tuple_strips':large_cases,
       'fresh_three_row_direct_tuple_intermediate_polynomials':large_polys,
       'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
       'scope':'Independent direct tuples/deleted-column strip test versus root recursion. Bounded validation, not an additional solve attempt.'}
    (HERE/'SHUFFLE-REVIEW-CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))
if __name__=='__main__':main()

