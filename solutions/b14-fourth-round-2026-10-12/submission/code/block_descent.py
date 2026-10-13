"""Blockwise 2-opt gain decomposition and exact sign-preserving integer metrics.

SciPy locates a candidate vertex. SymPy reconstructs a basis exactly. Every
returned surrogate is checked with rational/integer arithmetic; a numerical
optimizer success alone never certifies an output.
"""
from __future__ import annotations
from itertools import combinations,product
from functools import lru_cache
from math import lcm
import networkx as nx
import numpy as np
from scipy.optimize import linprog
import sympy as sp

def floyd(n:int,edges:list[tuple[int,int,int]])->list[list[int]]:
    inf=sum(w for _,_,w in edges)+1
    d=[[0 if u==v else inf for v in range(n)] for u in range(n)]
    for u,v,w in edges:d[u][v]=d[v][u]=min(w,d[u][v])
    for k in range(n):
        for i in range(n):
            for j in range(n):d[i][j]=min(d[i][j],d[i][k]+d[k][j])
    if any(d[0][v]>=inf for v in range(n)):raise ValueError('Disconnected graph')
    return d

def blocks_and_projections(n:int,edges:list[tuple[int,int,int]])->list[dict]:
    G=nx.Graph();G.add_nodes_from(range(n));G.add_weighted_edges_from(edges)
    if not nx.is_connected(G):raise ValueError('Disconnected graph')
    out=[]
    for V0 in nx.biconnected_components(G):
        V=sorted(V0);pos={v:i for i,v in enumerate(V)}
        es=[(pos[u],pos[v],w) for u,v,w in edges if u in pos and v in pos]
        local=floyd(len(V),es)
        # Removing this block's internal edges gives its vertex fibers.
        R=G.copy();R.remove_edges_from([(u,v) for u,v in G.edges if u in pos and v in pos])
        proj=[-1]*n
        for comp in nx.connected_components(R):
            roots=set(comp)&set(V)
            if len(roots)!=1:raise AssertionError('Block fiber is not rooted at one vertex')
            r=pos[next(iter(roots))]
            for v in comp:proj[v]=r
        out.append(dict(vertices=V,d=local,projection=proj))
    return out

@lru_cache(None)
def gain_rows(b:int)->tuple[tuple[int,...],...]:
    es=list(combinations(range(b),2));ix={e:i for i,e in enumerate(es)};rows=set()
    for a,c,d,e in product(range(b),repeat=4):
        row=[0]*len(es)
        for u,v,s in [(a,c,1),(d,e,1),(a,d,-1),(c,e,-1)]:
            if u!=v:row[ix[tuple(sorted((u,v)))]]+=s
        if any(row):rows.add(tuple(row))
    return tuple(sorted(rows))

def sign(x):return (x>0)-(x<0)

def surrogate(d:list[list[int]])->dict:
    b=len(d);es=list(combinations(range(b),2));D=len(es);v=[d[u][w] for u,w in es]
    rows=gain_rows(b); ge=[];eq=[]
    for r in rows:
        s=sign(sum(a*x for a,x in zip(r,v)))
        if s:ge.append(tuple(s*a for a in r))
        else:eq.append(r)
    ge=sorted(set(ge));eq=sorted(set(eq))
    ge+= [tuple(int(i==j) for j in range(D)) for i in range(D)]
    opt=linprog(np.ones(D),A_ub=-np.array(ge,dtype=float),b_ub=-np.ones(len(ge)),A_eq=np.array(eq,dtype=float) if eq else None,b_eq=np.zeros(len(eq)) if eq else None,bounds=[(None,None)]*D,method='highs')
    if not opt.success:raise ArithmeticError(opt.message)
    # Find d independent tight integer equations; equalities have RHS zero.
    candidate=[(r,0) for r in eq]+[(r,1) for r in ge if abs(np.dot(r,opt.x)-1)<1e-7]
    basis=[];rhs=[];rank=0
    for r,y in candidate:
        trial=sp.Matrix(basis+[list(r)])
        new=trial.rank()
        if new>rank:basis.append(list(r));rhs.append(y);rank=new
        if rank==D:break
    if rank!=D:raise ArithmeticError('No exact full-rank basis recovered')
    M=sp.Matrix(basis);det=abs(int(M.det()));x=M.inv()*sp.Matrix(rhs)
    z=[int(t*det) for t in x]
    if any(t*det!=q for t,q in zip(x,z)):raise ArithmeticError('Cramer scaling failed')
    bound=D*2**(D-1)
    assert all(1<=q<=bound for q in z)
    for r in rows:assert sign(sum(a*x for a,x in zip(r,v)))==sign(sum(a*x for a,x in zip(r,z)))
    out=[[0]*b for _ in range(b)]
    for (u,w),q in zip(es,z):out[u][w]=out[w][u]=q
    for a,c,e in product(range(b),repeat=3):assert out[a][e]<=out[a][c]+out[c][e]
    return dict(d=out,vector=z,determinant=det,basis=basis,rhs=rhs,theorem_bound=bound,gain_rows=len(rows))

def gains(blocks:list[dict],a:int,b:int,c:int,d:int,key:str='d')->list[int]:
    gs=[]
    for B in blocks:
        p=B['projection'];q=B[key];A,Bb,C,D=map(lambda v:p[v],[a,b,c,d])
        gs.append(q[A][Bb]+q[C][D]-q[A][C]-q[Bb][D])
    return gs

def glued_metric(n:int,blocks:list[dict],key:str='d')->list[list[int]]:
    return [[sum(B[key][B['projection'][u]][B['projection'][v]] for B in blocks) for v in range(n)] for u in range(n)]

def descend(d:list[list[int]],tour:list[int],rule:str='first')->dict:
    n=len(tour);steps=0;evals=0;history=[tour[:]]
    while True:
        best=None
        for i in range(n):
            for j in range(i+2,n):
                if i==0 and j==n-1:continue
                a,b,c,e=tour[i],tour[(i+1)%n],tour[j],tour[(j+1)%n]
                gain=d[a][b]+d[c][e]-d[a][c]-d[b][e];evals+=1
                if gain>0 and (best is None or gain>best[0]):best=(gain,i,j)
                if rule=='first' and best is not None:break
            if rule=='first' and best is not None:break
        if best is None:return dict(tour=tour,steps=steps,evaluations=evals,history=history)
        _,i,j=best;tour=tour[:i+1]+list(reversed(tour[i+1:j+1]))+tour[j+1:];steps+=1;history.append(tour[:])
