"""Exact primary-formula, literal-word, gamma, and small Ehrhart audit.

No inference from numerical roots or sampled gamma coefficients. The large
graph's h* identification uses the audited published dissection theorem;
the independent arithmetic is exact integer polynomial computation.
"""
from collections import defaultdict
from fractions import Fraction
from hashlib import sha256
from itertools import product
from math import comb
from pathlib import Path
import json


def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return out


def power(a,n):
    out=[1]
    for _ in range(n): out=mul(out,a)
    return out


def pieces_formula(k,i):
    row=[0]*k
    for r in range(i):
        for j in range(k-i+1):
            row[k-i+r-j]+=comb(r+j,r)*comb(k-1-r-j,i-1-r)
    return row


def pieces_words(k):
    plus=[[0]*k for _ in range(k+1)]
    minus=[[0]*k for _ in range(k+1)]
    for word in product([0,1],repeat=k):
        i=sum(word)
        for deleted in range(k):
            away=sum(word[:deleted])+sum(1-x for x in word[deleted+1:])
            (plus if word[deleted] else minus)[i][away]+=1
    return plus,minus


def row_from_pieces(k,m,plus,minus):
    dimension=m*(k-1)+1
    answer=[0]*(dimension+1)
    for i in range(k+1):
        for whole_path in range(m):
            # Whole path choices correspond to the two dual-arborescence blocks.
            term=mul(power(plus[i],whole_path),power(minus[i],m-1-whole_path))
            for j,value in enumerate(term):
                if value:
                    assert j+i<=dimension
                    answer[j+i]+=comb(k,i)*value
    return answer


def gamma_by_subtraction(h):
    d=len(h)-1; remaining=h[:]; gamma=[]
    for i in range(d//2+1):
        value=remaining[i]; gamma.append(value)
        for j in range(d-2*i+1): remaining[i+j]-=value*comb(d-2*i,j)
    assert remaining==[0]*(d+1)
    return gamma


def gamma_by_inverse(h):
    d=len(h)-1; answer=[]
    for j in range(d//2+1):
        value=Fraction(0)
        for i in range(j+1):
            factor=Fraction(d-2*i,d-i-j) if d-i-j else Fraction(1)
            value+=(-1)**(j-i)*factor*comb(d-i-j,j-i)*h[i]
        assert value.denominator==1
        answer.append(int(value))
    return answer


def graph(k,m):
    # Endpoints 0 and 1; all internal vertices are distinct across paths.
    paths=[[0]+[2+p*(k-1)+j for j in range(k-1)]+[1] for p in range(m)]
    edges=[(path[j],path[j+1]) for path in paths for j in range(k)]
    return paths,edges


def literal_E(k,m):
    paths,edges=graph(k,m); n=m*(k-1)+2; d=n-1
    vertices=[]
    for u,v in edges:
        a=[0]*d
        if u<d: a[u]+=1
        if v<d: a[v]-=1
        vertices += [tuple(a),tuple(-x for x in a)]
    current={tuple([0]*d)}; counts=[1]
    for _ in range(d):
        current |= {tuple(x+y for x,y in zip(a,b)) for a in current for b in vertices}
        counts.append(len(current))
    h=[sum((-1)**j*comb(d+1,j)*counts[i-j] for j in range(i+1))
       for i in range(d+1)]
    return counts,h


def main():
    pieces=[]
    for k in range(2,11):
        plus,minus=pieces_words(k)
        for i in range(k+1):
            assert plus[i]==pieces_formula(k,i)
            assert minus[i]==pieces_formula(k,i+1)
        pieces.append({'k':k,'marked_word_count':k*2**k})
    plus,minus=pieces_words(8)
    h=row_from_pieces(8,5,plus,minus)
    saved=[1,44,950,13420,139545,1139424,7611536,42797920,
           206716612,869517648,3208517832,10401251024,29530579604,
           72992503712,155919966064,285492984352,444071652750,
           581531566920,636773179140,581531566920,444071652750,
           285492984352,155919966064,72992503712,29530579604,
           10401251024,3208517832,869517648,206716612,42797920,
           7611536,1139424,139545,13420,950,44,1]
    assert h==saved and h==h[::-1]
    gamma=gamma_by_subtraction(h)
    assert gamma==gamma_by_inverse(h)
    assert gamma==[1,8,48,256,1280,6144,28672,131072,461136,
                   1373568,3438592,8290304,16487040,37120000,
                   63755264,77045760,-9799680,0,0]
    paths,edges=graph(8,5)
    assert len(set(edges))==40
    assert set(v for e in edges for v in e)==set(range(37))
    assert len(set(v for path in paths for v in path[1:-1]))==35
    seen={0}
    while True:
        expanded=seen|{v for u,v in edges if u in seen}|{u for u,v in edges if v in seen}
        if expanded==seen: break
        seen=expanded
    assert len(seen)==37
    # Choose one complete path and break every other path at its first edge.
    basis_edges=[e for p,path in enumerate(paths) for e in zip(path,path[1:])
                 if p==0 or e!=(path[0],path[1])]
    assert len(basis_edges)==36
    # A connected 37-vertex, 36-edge graph is a tree; its reduced incidence
    # matrix is unimodular. Connectivity is checked independently here.
    reached={0}
    while True:
        expanded=reached|{v for u,v in basis_edges if u in reached}|{u for u,v in basis_edges if v in reached}
        if expanded==reached: break
        reached=expanded
    assert len(reached)==37
    small=[]
    for k,m in [(2,1),(3,1),(4,1),(5,1),(2,2),(3,2),(2,3),(2,4)]:
        E,literal=literal_E(k,m)
        plus,minus=pieces_words(k)
        predicted=row_from_pieces(k,m,plus,minus)
        assert literal==predicted, (k,m,literal,predicted)
        small.append({'k':k,'m':m,'E':E,'h_star':literal})
    here=Path(__file__)
    out={'result':'PASS','attributed_source':'Luis Ferroni, arXiv:2607.02424v1, Proposition 2.1 and Corollary 2.2',
         'scope':'Full target counterexample via homology branch; source theorem plus independent exact arithmetic audit.',
         'large_graph':{'paths':paths,'edges':[list(e) for e in edges],
                        'vertices':37,'edges_count':40,'dimension':36,
                        'tree_basis_edges':[list(e) for e in basis_edges]},
         'literal_marked_word_controls':pieces,
         'independent_small_Ehrhart_controls':small,
         'h_star':h,'gamma':gamma,'gamma_16':gamma[16],
         'two_gamma_inversions_agree':True,
         'checker_sha256':sha256(here.read_bytes()).hexdigest()}
    here.with_name('FERRONI-CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'result':'PASS','gamma_16':gamma[16],
                      'marked_word_controls':sum(p['marked_word_count'] for p in pieces),
                      'literal_small_Ehrhart_cases':len(small)}))


if __name__=='__main__':main()
