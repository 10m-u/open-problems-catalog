"""Independent certificate audit, including explicit subtour-feasibility flows.

Does not import module_solver. Integer flow certificates establish every
subtour inequality of the original fractional point. Relabeling certifies the
forced points. The all-root/all-potential conclusion uses the written lemma.
"""
import json,time,hashlib
from pathlib import Path
from itertools import combinations
import networkx as nx
ROOT=Path(__file__).resolve().parents[1]

def e(u,v):return (min(u,v),max(u,v))

def main():
    ts=time.perf_counter();I=json.loads((ROOT/'instances/unique-180-city-separation.json').read_text())
    k=I['k'];b=I['b'];n=k*b;B=I['B'];s=I['secondary'];T=I['tour'];U=I['optimum'];assert b==10 and k%2==0 and k>=18
    E=set();x={}
    for j in range(k):
        z=10*j
        for a in range(5):
            for u,v in [(z+a,z+(a+1)%5),(z+5+a,z+5+(a+2)%5)]:E.add(e(u,v));x[e(u,v)]=1
        for a in range(1,5):E.add((z+a,z+5+a));x[z+a,z+5+a]=2
        q=e(z+5,10*((j+1)%k));E.add(q);x[q]=2
    assert all(sum(w for (u,v),w in x.items() if t in (u,v))==4 for t in range(n))
    assert sum(x.values())==2*n
    # Independently check the fixed-size forbidden Hamiltonian path by masks.
    E0={q for q in E if q[0]<10 and q[1]<10};adj=[[] for _ in range(10)]
    for u,v in E0:adj[u].append(v);adj[v].append(u)
    reachable={(1,0)}
    for mask in range(1<<10):
        for v in range(10):
            if (mask,v) not in reachable:continue
            for u in adj[v]:
                if not(mask>>u&1):reachable.add((mask|1<<u,u))
    assert ((1<<10)-1,5) not in reachable
    # Check the cost identity and a matching primal certificate.
    assert len(T)==n and set(T)==set(range(n));tour_edges={e(T[j],T[(j+1)%n]) for j in range(n)}
    assert len(tour_edges)==n
    assert len(tour_edges-E)==k//2
    assert all(s[u][v]==int((u,v) not in tour_edges) for u,v in combinations(range(n),2))
    assert U==B*(2*n+k//2)
    assert sum((2 if q in E else 3)*B+s[q[0]][q[1]] for q in tour_edges)==U
    assert B==n+1 and 3*B+1<4*B
    # Produce s--t flow witnesses for every t. Only the flows are trusted below.
    G=nx.DiGraph()
    for (u,v),cap in x.items():G.add_edge(u,v,capacity=cap);G.add_edge(v,u,capacity=cap)
    flows=[];flow_entries=0
    for target in range(1,n):
        value,f=nx.maximum_flow(G,0,target,flow_func=nx.algorithms.flow.edmonds_karp)
        net=[];balance=[0]*n
        for (u,v),cap in x.items():
            a=f[u][v]-f[v][u]
            assert isinstance(a,int) and abs(a)<=cap
            balance[u]+=a;balance[v]-=a
            if a:net.append([u,v,a])
        assert balance==[4 if v==0 else -4 if v==target else 0 for v in range(n)]
        flows.append(dict(target=target,net=net));flow_entries+=len(net)
    (ROOT/'checks/SUBTOUR-FLOW-CERTIFICATES.json').write_text(json.dumps(dict(n=n,twice_x=[[u,v,c] for (u,v),c in sorted(x.items())],flows=flows),indent=2)+'\n')
    # All fixed-edge points are permutations of x mapping a unit edge to e.
    maximum=-1;minimum=10**100;counts=0;digest=hashlib.sha256()
    for a,b in combinations(range(n),2):
        perm=list(range(n))
        # First label transposition sends 1 to a.
        perm=[a if v==1 else 1 if v==a else v for v in perm]
        at=perm[6]
        # Second label transposition sends the current image of 6 to b,
        # while leaving a fixed.
        perm=[b if v==at else at if v==b else v for v in perm]
        assert e(perm[1],perm[6])==(a,b)
        val=0
        for (u,v),w in x.items():
            q=e(perm[u],perm[v]);val+=w*((2 if q in E else 3)*B+s[q[0]][q[1]])
        assert val<2*U
        maximum=max(maximum,val);minimum=min(minimum,val);counts+=1;digest.update(f'{a},{b},{val}\n'.encode())
    result=dict(status='PASS',n=n,k=k,primary_minimum_repairs=k//2,unique_optimum=U,cost_levels=[2*B,2*B+1,3*B,3*B+1],forbidden_local_path_dp_states=len(reachable),flow_certificates=len(flows),integer_flow_entries=flow_entries,forced_fractional_witnesses=counts,maximum_twice_witness_cost=maximum,minimum_twice_witness_cost=minimum,twice_unique_optimum=2*U,witness_results_sha256=digest.hexdigest(),universally_blind_forced_1tree_edges=counts,completion_certifiably_deleted=counts-n,retained_edges=n,elapsed_seconds=time.perf_counter()-ts)
    (ROOT/'checks/SEPARATION-RESULTS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
