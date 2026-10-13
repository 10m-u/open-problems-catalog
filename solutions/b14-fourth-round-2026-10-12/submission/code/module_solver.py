"""Exact two-port necklace solver and completion-based edge lower bounds.

The promised family is verified by audit_instance. No floating-point arithmetic.
Arbitrary nonnegative repair excess is allowed: solve returns a lower bound and
an actual tour, which is certified optimal exactly when the two coincide.
"""
from __future__ import annotations
from dataclasses import dataclass
from itertools import combinations
from typing import Iterable

Edge = tuple[int,int]
def edge(u:int,v:int)->Edge:
    return (min(u,v),max(u,v))

def hamilton_paths(b:int, edges:Iterable[Edge], start:int)->list[tuple[int,...]]:
    """Enumerate local paths only. b is the bounded module size."""
    adj=[[] for _ in range(b)]
    for u,v in edges: adj[u].append(v);adj[v].append(u)
    out=[]
    def dfs(path:list[int],mask:int)->None:
        if len(path)==b: out.append(tuple(path));return
        for v in sorted(adj[path[-1]]):
            if not (mask>>v)&1: dfs(path+[v],mask|(1<<v))
    dfs([start],1<<start)
    return out

@dataclass
class Necklace:
    k:int
    b:int
    ports:tuple[int,int]
    local_edges:tuple[Edge,...]
    B:int
    W:int
    tolls:list[int]
    secondary:list[list[int]]
    @property
    def n(self)->int:return self.k*self.b
    def connectors(self)->tuple[Edge,...]:
        left,right=self.ports
        return tuple(edge(i*self.b+right,((i+1)%self.k)*self.b+left) for i in range(self.k))
    def cheap(self)->set[Edge]:
        return set(self.connectors())|{(i*self.b+u,i*self.b+v) for i in range(self.k) for u,v in self.local_edges}
    def cost(self,u:int,v:int)->int:
        if u==v:return 0
        a=2 if edge(u,v) in self.cheap() else 3
        return a*self.B+self.secondary[u][v]
    def as_dict(self)->dict:
        return dict(k=self.k,b=self.b,ports=self.ports,local_edges=self.local_edges,B=self.B,W=self.W,tolls=self.tolls,secondary=self.secondary)


def audit_instance(I:Necklace)->dict:
    n=I.n
    if I.k<2 or I.k%2:raise ValueError('An even number of at least two modules is required.')
    if len(set(I.ports))!=2 or any(p<0 or p>=I.b for p in I.ports):raise ValueError('Invalid ports.')
    if I.B<=n*I.W or I.W<0:raise ValueError('Require B > n W >= 0.')
    if len(I.secondary)!=n or any(len(row)!=n for row in I.secondary):raise ValueError('Wrong matrix size.')
    if len(I.tolls)!=n or any(x<0 for x in I.tolls):raise ValueError('Invalid toll vector.')
    E=I.cheap(); checks=0
    for u,v in combinations(range(n),2):
        s=I.secondary[u][v]
        if not isinstance(s,int) or s!=I.secondary[v][u] or not 0<=s<=I.W:raise ValueError('Secondary costs must be symmetric integers in [0,W].')
        if u//I.b!=v//I.b and (u,v) not in E:
            if s<I.tolls[u]+I.tolls[v]:raise ValueError('The endpoint-toll envelope is not a lower bound.')
        checks+=1
    paths={p:hamilton_paths(I.b,I.local_edges,p) for p in I.ports}
    for p in I.ports:
        if not paths[p]:raise ValueError('Each port must start some Hamiltonian path.')
        if any(P[-1] in I.ports for P in paths[p]):raise ValueError('A port-to-port Hamiltonian path invalidates the obstruction.')
    return dict(pair_checks=checks,paths_per_port={str(p):len(paths[p]) for p in I.ports},strict_metric_proved_by_range=True)


def solve(I:Necklace,check:bool=True)->dict:
    audit=audit_instance(I) if check else {}
    n=I.n;local_paths={p:hamilton_paths(I.b,I.local_edges,p) for p in I.ports}
    # Each local path is represented by its cost, endpoint, edge set and witness.
    tables={}
    for i in range(I.k):
        for p in I.ports:
            rows=[]
            for path in local_paths[p]:
                P=tuple(i*I.b+v for v in path)
                E=frozenset(edge(u,v) for u,v in zip(P,P[1:]))
                val=sum(I.secondary[u][v] for u,v in E)+I.tolls[P[-1]]
                rows.append((val,P[-1],E,P))
            tables[i,p]=sorted(rows,key=lambda x:(x[0],x[3]))
    connectors=I.connectors(); patterns=[]
    for parity in [0,1]:
        chosen=list(range(parity,I.k,2)); port={}
        for j in chosen:
            port[j]=I.ports[1];port[(j+1)%I.k]=I.ports[0]
        mates={}
        for j in chosen:mates[j]=(j+1)%I.k;mates[(j+1)%I.k]=j
        rows={i:tables[i,port[i]][0] for i in range(I.k)}
        S=sum(r[0] for r in rows.values())+sum(I.secondary[connectors[j][0]][connectors[j][1]] for j in chosen)
        # A paired component runs endpoint -> right port -> next left port -> endpoint.
        units=[]
        for j in chosen:
            units.append(tuple(reversed(rows[j][3]))+rows[(j+1)%I.k][3])
        tour=tuple(v for unit in units for v in unit)
        patterns.append(dict(parity=parity,connectors=chosen,ports=port,mates=mates,local_rows=rows,secondary_lower=S,tour=tour))
    base=I.B*(2*n+I.k//2)
    E=I.cheap()
    def tour_cost(P):return sum((2 if edge(P[j],P[(j+1)%n]) in E else 3)*I.B+I.secondary[P[j]][P[(j+1)%n]] for j in range(n))
    U,tour=min((tour_cost(P['tour']),P['tour']) for P in patterns)
    L=base+min(P['secondary_lower'] for P in patterns)
    # The constructed primary-minimal tour has at most n W secondary cost.
    assert U<I.B*(2*n+I.k//2+1)
    return dict(lower=L,upper=U,optimal=L==U,tour=tour,patterns=patterns,tables=tables,base=base,audit=audit)


def forced_bounds(I:Necklace,R:dict)->dict[Edge,int]:
    """All bounds apply to full original tours, not just a promised primary face.

    Any excluded primary-face edge gets the next-primary-level lower bound.
    Other edge bounds are capped at that level for the same reason.
    """
    base=R['base']; next_level=base+I.B; C=I.connectors(); Cindex={e:j for j,e in enumerate(C)}
    cheap=I.cheap(); out={}
    for u,v in combinations(range(I.n),2):
        e=(u,v);i,j=u//I.b,v//I.b; vals=[]
        for P in R['patterns']:
            S=P['secondary_lower']; ports=P['ports']; rows=P['local_rows']
            if e in Cindex:
                if Cindex[e] in P['connectors']:vals.append(base+S)
            elif i==j:
                if e not in cheap:continue
                eligible=[r[0] for r in R['tables'][i,ports[i]] if e in r[2]]
                if eligible:vals.append(base+S-rows[i][0]+min(eligible))
            else:
                # All nonconnector intermodule edges are repairs.
                if I.k>2 and P['mates'][i]==j:continue
                A=[r[0] for r in R['tables'][i,ports[i]] if r[1]==u]
                B=[r[0] for r in R['tables'][j,ports[j]] if r[1]==v]
                if A and B:
                    excess=I.secondary[u][v]-I.tolls[u]-I.tolls[v]
                    vals.append(base+S-rows[i][0]-rows[j][0]+min(A)+min(B)+excess)
        out[e]=min([next_level]+vals)
    return out


def fixture(kind:str='petersen')->tuple[int,tuple[int,int],tuple[Edge,...]]:
    if kind=='petersen':
        E={edge(i,(i+1)%5) for i in range(5)}|{edge(5+i,5+(i+2)%5) for i in range(5)}|{edge(i,5+i) for i in range(1,5)}
        return 10,(0,5),tuple(sorted(E))
    if kind.startswith('cycle'):
        b=int(kind[5:]);return b,(0,2),tuple(sorted({edge(i,(i+1)%b) for i in range(b)}))
    if kind=='barbell':
        E={(0,1),(1,2),(0,2),(2,3),(3,4),(4,5),(3,5)}
        return 6,(0,1),tuple(sorted(E))
    raise ValueError(kind)


def random_instance(kind:str,k:int,seed:int)->Necklace:
    import random
    rng=random.Random(seed);b,ports,E=fixture(kind);n=b*k
    toll=[rng.randrange(6) for _ in range(n)]; W=20;B=n*W+1
    I=Necklace(k,b,ports,E,B,W,toll,[[0]*n for _ in range(n)])
    cheap=I.cheap()
    for u,v in combinations(range(n),2):
        s=toll[u]+toll[v] if u//b!=v//b and (u,v) not in cheap else rng.randrange(W+1)
        I.secondary[u][v]=I.secondary[v][u]=s
    return I


def planted_separation(k:int)->Necklace:
    # The witness is first discovered from local paths, then used to define
    # a family separating the two certificate systems. Not a blind benchmark.
    b,ports,E=fixture('petersen');n=b*k
    I=Necklace(k,b,ports,E,n+1,1,[0]*n,[[0]*n for _ in range(n)])
    R=solve(I);P=R['tour'];T={edge(P[j],P[(j+1)%n]) for j in range(n)}
    for u,v in combinations(range(n),2):I.secondary[u][v]=I.secondary[v][u]=int((u,v) not in T)
    return I
