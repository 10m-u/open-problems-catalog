"""Independent certificate reader. Standard library only.

Does not import any research implementation and does not run an LP, a flow
optimizer, or the contracted forward-DP construction. It checks supplied
integer metrics, signed flow conservation, and every saved Bellman recurrence.
Run without Python's -O option so all assertions remain enabled.
"""
from __future__ import annotations
from itertools import combinations,product
from pathlib import Path
from math import inf
import json,time
ROOT=Path(__file__).resolve().parents[1]

def load(name):return json.loads((ROOT/name).read_text())
def edge(u,v):return (min(u,v),max(u,v))
def sign(x):return (x>0)-(x<0)

def ordinal():
    records=load('checks/ORDINAL-CERTIFICATES.json');comparisons=0
    for item in records:
        a=item['original'];q=item['surrogate']['d'];n=len(a);D=n*(n-1)//2;bound=D*2**(D-1)
        assert len(q)==n and all(len(row)==n for row in q)
        for u in range(n):assert q[u][u]==0
        for u,v in combinations(range(n),2):assert isinstance(q[u][v],int) and 1<=q[u][v]==q[v][u]<=bound
        for u,v,w in product(range(n),repeat=3):assert q[u][v]<=q[u][w]+q[w][v]
        for u,v,w,z in product(range(n),repeat=4):
            assert sign(a[u][v]+a[w][z]-a[u][w]-a[v][z])==sign(q[u][v]+q[w][z]-q[u][w]-q[v][z])
            comparisons+=1
    return dict(integer_metrics=len(records),four_label_sign_checks=comparisons)

def flows():
    x=load('checks/SUBTOUR-FLOW-CERTIFICATES.json');n=x['n'];caps={};deg=[0]*n
    for u,v,cap in x['twice_x']:
        assert 0<=u<v<n and (u,v) not in caps and cap in (1,2)
        caps[u,v]=cap;deg[u]+=cap;deg[v]+=cap
    assert deg==[4]*n
    targets=set();entries=0
    for item in x['flows']:
        t=item['target'];assert 0<t<n and t not in targets;targets.add(t)
        divergence=[0]*n;seen=set()
        for u,v,value in item['net']:
            assert (u,v) in caps and (u,v) not in seen;seen.add((u,v))
            assert isinstance(value,int) and abs(value)<=caps[u,v]
            divergence[u]+=value;divergence[v]-=value;entries+=1
        expected=[0]*n;expected[0]=4;expected[t]=-4;assert divergence==expected
    assert targets==set(range(1,n))
    return dict(vertices=n,flow_certificates=len(targets),signed_entries=entries,all_subtour_cuts_certified=True)

def instance(name):
    I=load(name);k=I['k'];b=I['b'];n=k*b;s=I['secondary'];p=I['ports'];B=I['B'];W=I['W']
    assert k>=2 and k%2==0 and B>n*W>=0 and len(set(p))==2
    assert len(s)==n and all(len(r)==n for r in s)
    E={edge(*e) for e in I['local_edges']};assert all(0<=u<v<b for u,v in E)
    cheap={edge(i*b+u,i*b+v) for i in range(k) for u,v in E}
    cheap|={edge(i*b+p[1],((i+1)%k)*b+p[0]) for i in range(k)}
    for u,v in combinations(range(n),2):assert 0<=s[u][v]==s[v][u]<=W and isinstance(s[u][v],int)
    P=I['tour'];assert sorted(P)==list(range(n))
    tour_edges={edge(P[j],P[(j+1)%n]) for j in range(n)};assert len(tour_edges)==n
    cost=sum(B*(2+int(e not in cheap))+s[e[0]][e[1]] for e in tour_edges)
    assert cost==I['optimum'] and cost<B*(2*n+k//2+1)
    # Exact weighted Hamiltonian-path tables, independently computed by subsets.
    adj=[[] for _ in range(b)]
    for u,v in E:adj[u].append(v);adj[v].append(u)
    tables={};states=0
    for i in range(k):
        for start in p:
            dp=[{} for _ in range(1<<b)];dp[1<<start][start]=0
            for mask,row in enumerate(dp):
                for last,value in row.items():
                    states+=1
                    for v in adj[last]:
                        if mask>>v&1:continue
                        new=mask|1<<v;val=value+s[i*b+last][i*b+v]
                        if val<dp[new].get(v,inf):dp[new][v]=val
            assert dp[-1] and not set(dp[-1]).intersection(p)
            tables[i,start]={i*b+v:value for v,value in dp[-1].items()}
    return I,cheap,tour_edges,tables,states

def unique():
    I,H,T,_,states=instance('instances/unique-180-city-separation.json');n=I['k']*I['b'];s=I['secondary']
    assert I['B']==n+1 and I['W']==1 and I['k']>=18
    assert all(s[u][v]==int((u,v) not in T) for u,v in combinations(range(n),2))
    assert sum(e not in H for e in T)==I['k']//2
    assert I['optimum']==I['B']*(2*n+I['k']//2)
    assert {tuple(e) for e in I['retained_edges']}==T
    return dict(optimum=I['optimum'],local_dp_states=states,unique_optimum_certificate=True)

def contracted():
    I,H,T,tables,localstates=instance('instances/nonseparable-180-city.json')
    k=I['k'];b=I['b'];m=k//2;s=I['secondary'];p=I['ports'];records=load('checks/CONTRACTED-DP-CERTIFICATE.json')
    assert sorted(r['parity'] for r in records)==[0,1]
    n=k*b;allmin=[];count=0;comparisons=0
    for record in records:
        chosen=list(range(record['parity'],k,2));units=[(j,(j+1)%k) for j in chosen]
        g={};endpoint={};exits=[];owner={};conn=[]
        for j in chosen:
            for i,port in [(j,p[1]),((j+1)%k,p[0])]:
                g.update(tables[i,port]);endpoint[i]=sorted(tables[i,port])
        for q,(a,bb) in enumerate(units):
            out=endpoint[a]+endpoint[bb];exits.append(out)
            for v in out:owner[v]=q
            conn.append(s[a*b+p[1]][bb*b+p[0]])
        transfer={}
        for x in owner:
            for q,(a,bb) in enumerate(units):
                if owner[x]==q:continue
                for v in exits[q]:
                    other=bb if v//b==a else a
                    transfer[x,v]=g[v]+conn[q]+min(s[x][u]+g[u] for u in endpoint[other])
        a,bb=units[0]
        cases=record['root_cases'];assert sorted(c['start'] for c in cases)==endpoint[a]
        for case in cases:
            start=case['start'];rows=[{} for _ in range(1<<m)]
            for mask,v,value in case['rows']:
                assert 0<=mask<1<<m and v not in rows[mask] and isinstance(value,int)
                rows[mask][v]=value;count+=1
            for mask,row in enumerate(rows):
                if mask==1:expected_keys=set(endpoint[bb])
                elif mask&1:expected_keys={v for q in range(1,m) if mask>>q&1 for v in exits[q]}
                else:expected_keys=set()
                assert set(row)==expected_keys
                for v,value in row.items():
                    if mask==1:expected=g[start]+g[v]+conn[0]
                    else:
                        previous=mask^(1<<owner[v]);comparisons+=len(rows[previous])
                        expected=min(old+transfer[x,v] for x,old in rows[previous].items())
                    assert value==expected
            minimum=min(value+s[v][start] for v,value in rows[-1].items())
            assert minimum==case['minimum'];allmin.append(minimum)
    optimum=I['B']*(2*n+k//2)+min(allmin)
    assert optimum==I['optimum'] and sum(e not in H for e in T)==k//2
    X=load('checks/SUBTOUR-FLOW-CERTIFICATES.json')
    assert X['n']==n and all((u,v) in H for u,v,cap in X['twice_x'])
    one_tree_cap=I['B']*(2*n+8)+n*I['W']
    primary_lower=I['B']*(2*n+k//2)
    assert one_tree_cap<primary_lower<=optimum
    return dict(optimum=optimum,path_units=m,certified_dp_entries=count,bellman_comparisons=comparisons,independent_local_dp_states=localstates,all_forced_fractional_analytic_upper=one_tree_cap,primary_tour_lower=primary_lower)

def main():
    if not __debug__:raise RuntimeError('Do not disable assertion checks with python -O.')
    start=time.perf_counter();out=dict(status='PASS',ordinal=ordinal(),flow=flows(),unique=unique(),contracted=contracted(),uses_third_party_libraries=False)
    out['elapsed_seconds']=time.perf_counter()-start
    (ROOT/'checks/INDEPENDENT-CERTIFICATE-RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
