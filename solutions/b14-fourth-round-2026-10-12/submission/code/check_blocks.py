"""Exact tests for block noncancellation, ordinal compression, and trajectories."""
from __future__ import annotations
import json,random,time
from pathlib import Path
from itertools import combinations,permutations
import networkx as nx
from block_descent import *
ROOT=Path(__file__).resolve().parents[1]

def block_graph(seed:int):
    rng=random.Random(seed);n=1;edges=[]
    for j in range(rng.randrange(2,6)):
        b=rng.randrange(2,6);root=rng.randrange(n);V=[root]+list(range(n,n+b-1));n+=b-1
        pairs=list(combinations(V,2)) if rng.randrange(2) else list(zip(V,V[1:]+V[:1]))
        seen=set()
        for u,v in pairs:
            e=tuple(sorted((u,v)))
            if e in seen:continue
            seen.add(e)
            w=rng.choice([1,2,3,7,23])
            if seed%7==0:w*=10**rng.randrange(0,31)
            edges.append((u,v,w))
    return n,edges

def cost(d,P):return sum(d[P[i]][P[(i+1)%len(P)]] for i in range(len(P)))

def three_opt_counterexample():
    # A bounded exhaustive search on a weighted path, separate from 2-opt tests.
    n=6;edges=[(0,1,1),(1,2,1),(2,3,10),(3,4,1),(4,5,1)]
    d=floyd(n,edges)
    tours=[(0,)+P for P in permutations(range(1,n)) if P[0]<P[-1]]
    data=[]
    for P in tours:
        E={tuple(sorted((P[i],P[(i+1)%n]))) for i in range(n)}
        counts=[sum((u<=j)!=(v<=j) for u,v in E) for j in range(n-1)]
        data.append((P,E,counts,cost(d,P)))
    for P,E,C,c in data:
        for Q,F,D,v in data:
            diff=[a-b for a,b in zip(C,D)]
            if c>v and len(E-F)==3 and min(diff)<0<max(diff):
                return dict(edges=edges,old_tour=P,new_tour=Q,removed=sorted(E-F),added=sorted(F-E),old_cost=c,new_cost=v,old_cut_counts=C,new_cut_counts=D)
    raise AssertionError('No expected 3-opt counterexample found')

def main():
    t=time.perf_counter();stats=dict(graphs=0,distance_entries=0,quartet_comparisons=0,nonzero_multiblock_comparisons=0,compressed_blocks=0,compressed_gain_rows=0,global_sign_comparisons=0,first_improvement_trajectory_pairs=0,actual_strict_moves=0)
    certs=[];records=[]
    for seed in range(160):
        n,edges=block_graph(seed);Bs=blocks_and_projections(n,edges);d=floyd(n,edges)
        assert glued_metric(n,Bs)==d
        G=nx.Graph();G.add_weighted_edges_from(edges)
        for u in range(n):
            dd=nx.single_source_dijkstra_path_length(G,u,weight='weight')
            assert all(dd[v]==d[u][v] for v in range(n))
        stats['graphs']+=1;stats['distance_entries']+=n*n
        for a,b,c,e in combinations(range(n),4):
            for q in [(a,b,c,e),(a,b,e,c),(a,c,e,b)]:
                g=gains(Bs,*q)
                assert not (min(g)<0<max(g)),(seed,q,g)
                stats['quartet_comparisons']+=1
                if sum(x!=0 for x in g)>1:stats['nonzero_multiblock_comparisons']+=1
        if seed<32:
            for B in Bs:
                S=surrogate(B['d']);B['surrogate']=S['d']
                stats['compressed_blocks']+=1;stats['compressed_gain_rows']+=S['gain_rows']
                certs.append(dict(seed=seed,vertices=B['vertices'],original=B['d'],surrogate=S))
            dd=glued_metric(n,Bs,key='surrogate')
            for a,b,c,e in combinations(range(n),4):
                for q in [(a,b,c,e),(a,b,e,c),(a,c,e,b)]:
                    assert sign(sum(gains(Bs,*q)))==sign(sum(gains(Bs,*q,key='surrogate')))
                    stats['global_sign_comparisons']+=1
            rng=random.Random(987+seed)
            for r in range(3):
                P=list(range(n));rng.shuffle(P)
                R=descend(d,P,'first');S=descend(dd,P,'first')
                assert R['history']==S['history']
                stats['first_improvement_trajectory_pairs']+=1
                for rule in ['first','best']:
                    R=descend(d,P,rule)
                    phis=[cost(dd,H) for H in R['history']]
                    assert all(x>y for x,y in zip(phis,phis[1:]))
                    for X,Y in zip(R['history'],R['history'][1:]):
                        for B in Bs:
                            p=B['projection'];m=B['d']
                            f=lambda H:sum(m[p[H[i]]][p[H[(i+1)%n]]] for i in range(n))
                            assert f(X)>=f(Y)
                    assert R['steps']<=phis[0]
                    stats['actual_strict_moves']+=R['steps']
            records.append(dict(seed=seed,n=n,blocks=len(Bs),max_block=max(len(B['vertices']) for B in Bs),largest_original_edge=max(w for _,_,w in edges),largest_surrogate_block_distance=max(max(row) for B in Bs for row in B['surrogate'])))
    # Additional exact surrogates at dimensions 15 and 21 (block sizes 6,7).
    for b in [6,7]:
        rng=random.Random(b);es=[(u,v,rng.randrange(1,31)) for u,v in combinations(range(b),2)];d=floyd(b,es)
        S=surrogate(d);certs.append(dict(seed='complete-'+str(b),vertices=list(range(b)),original=d,surrogate=S));stats['compressed_blocks']+=1;stats['compressed_gain_rows']+=S['gain_rows']
    counter=three_opt_counterexample()
    (ROOT/'checks/ORDINAL-CERTIFICATES.json').write_text(json.dumps(certs,indent=2)+'\n')
    result=dict(status='PASS',**stats,records=records,three_opt_counterexample=counter,elapsed_seconds=time.perf_counter()-t)
    (ROOT/'checks/BLOCK-RESULTS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='records'},indent=2))
if __name__=='__main__':main()
