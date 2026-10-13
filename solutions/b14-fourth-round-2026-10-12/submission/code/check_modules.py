"""Reproduce module theorem checks with an independent C++ exact TSP oracle."""
from __future__ import annotations
import json,subprocess,time,random
from pathlib import Path
from itertools import combinations
from module_solver import *
ROOT=Path(__file__).resolve().parents[1]

def exact(I):
    n=I.n;cheap=I.cheap();c=[[0 if u==v else (2 if edge(u,v) in cheap else 3)*I.B+I.secondary[u][v] for v in range(n)] for u in range(n)]
    inp=str(n)+'\n'+'\n'.join(' '.join(map(str,row)) for row in c)+'\n'
    run=subprocess.run([str(ROOT/'code/subset_oracle')],input=inp,text=True,capture_output=True,check=True)
    lines=run.stdout.splitlines(); opt=int(lines[0]);forced=[list(map(int,line.split())) for line in lines[1:]]
    return opt,forced

def local_dp(b,E,start,require=None):
    adj=[[] for _ in range(b)]
    for u,v in E:adj[u].append(v);adj[v].append(u)
    dp={(1<<start,start,require is None):0}; counts=0
    for mask in range(1<<b):
        for v in range(b):
            for flag in (False,True):
                key=mask,v,flag
                if key not in dp:continue
                counts+=1
                for u in adj[v]:
                    if mask>>u&1:continue
                    dp[mask|1<<u,u,flag or edge(u,v)==require]=1
    return {v for v in range(b) if ((1<<b)-1,v,True) in dp},counts

def main():
    start=time.perf_counter();records=[];forced_checks=0;localstates=0
    for kind in ['cycle4','cycle5','barbell','petersen']:
        b,ports,E=fixture(kind)
        for p in ports:
            paths=hamilton_paths(b,E,p)
            ends,count=local_dp(b,E,p);localstates+=count
            assert ends=={P[-1] for P in paths} and not ends.intersection(ports)
            for e in E:
                ends,count=local_dp(b,E,p,e);localstates+=count
                assert ends=={P[-1] for P in paths if e in {edge(u,v) for u,v in zip(P,P[1:])}}
    for kind,k,seeds in [('cycle4',2,range(12)),('cycle5',2,range(6)),('barbell',2,range(6)),('cycle4',4,range(2))]:
        for seed in seeds:
            for excess in [False,True]:
                I=random_instance(kind,k,seed)
                if excess:
                    rng=random.Random(10000+seed);cheap=I.cheap()
                    for u,v in combinations(range(I.n),2):
                        if u//I.b!=v//I.b and (u,v) not in cheap:
                            I.secondary[u][v]+=rng.randrange(11);I.secondary[v][u]=I.secondary[u][v]
                R=solve(I);F=forced_bounds(I,R);OPT,oracle=exact(I)
                assert R['lower']<=OPT<=R['upper']
                if not excess:assert R['optimal'] and R['lower']==OPT
                for (u,v),lb in F.items():assert lb<=oracle[u][v];forced_checks+=1
                deleted=[e for e,lb in F.items() if lb>R['upper']]
                assert all(oracle[u][v]>OPT for u,v in deleted)
                records.append(dict(kind=kind,k=k,n=I.n,seed=seed,nonseparable_excess=excess,lower=R['lower'],optimum=OPT,upper=R['upper'],deleted=len(deleted),exact_certified=R['optimal']))
    scales=[]
    for k in [2,4,18,40,100]:
        I=random_instance('petersen',k,17);ts=time.perf_counter();R=solve(I);solve_time=time.perf_counter()-ts
        ts=time.perf_counter();F=forced_bounds(I,R);bound_time=time.perf_counter()-ts
        assert R['optimal']
        scales.append(dict(k=k,n=I.n,seed=17,lower=R['lower'],upper=R['upper'],retained=sum(v<=R['upper'] for v in F.values()),solve_seconds=solve_time,forced_bounds_seconds=bound_time))
    I=planted_separation(18);R=solve(I);F=forced_bounds(I,R);T={edge(R['tour'][j],R['tour'][(j+1)%I.n]) for j in range(I.n)}
    kept={e for e,lb in F.items() if lb<=R['upper']};assert kept==T
    packet=I.as_dict();packet['tour']=R['tour'];packet['optimum']=R['upper'];packet['retained_edges']=sorted(kept)
    (ROOT/'instances/unique-180-city-separation.json').write_text(json.dumps(packet,indent=2)+'\n')
    cheap=I.cheap()
    result=dict(status='PASS',oracle_cases=len(records),forced_edge_oracle_checks=forced_checks,local_dp_states=localstates,nonseparable_cases_not_exactly_certified=sum(r['nonseparable_excess'] and not r['exact_certified'] for r in records),records=records,scale_runs=scales,separation=dict(n=I.n,k=I.k,B=I.B,cost_levels=sorted({(2 if (u,v) in cheap else 3)*I.B+I.secondary[u][v] for u,v in combinations(range(I.n),2)}),optimum=R['upper'],complete_edges=len(F),deleted=len(F)-len(kept),retained=len(kept)),elapsed_seconds=time.perf_counter()-start)
    (ROOT/'checks/MODULE-RESULTS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='records'},indent=2))
if __name__=='__main__':main()
