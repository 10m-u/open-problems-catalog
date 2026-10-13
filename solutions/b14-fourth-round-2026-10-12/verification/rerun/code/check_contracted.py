"""Check contracted exact solving against unstructured Held--Karp instances."""
from __future__ import annotations
import json,random,time
from itertools import combinations
from pathlib import Path
from module_solver import random_instance,solve
from contracted_solver import exact_contract
from check_modules import exact
ROOT=Path(__file__).resolve().parents[1]

def nonseparable(kind,k,seed):
    I=random_instance(kind,k,seed);rng=random.Random(10000+seed);cheap=I.cheap()
    for u,v in combinations(range(I.n),2):
        if u//I.b!=v//I.b and (u,v) not in cheap:
            I.secondary[u][v]+=rng.randrange(11);I.secondary[v][u]=I.secondary[u][v]
    return I

def main():
    ts=time.perf_counter();records=[]
    for kind,k,seeds in [('cycle4',2,range(12)),('cycle5',2,range(6)),('barbell',2,range(6)),('cycle4',4,range(2))]:
        for seed in seeds:
            for excess in [False,True]:
                I=nonseparable(kind,k,seed) if excess else random_instance(kind,k,seed)
                R=solve(I);A=exact_contract(I,R);OPT,_=exact(I)
                assert A['optimum']==OPT
                records.append(dict(kind=kind,k=k,seed=seed,nonseparable=excess,lower=R['lower'],exact_optimum=OPT,old_upper=R['upper'],states=A['dp_states']))
    scales=[]
    for k in [4,8,12,18]:
        I=nonseparable('petersen',k,29);R=solve(I);t=time.perf_counter()
        A=exact_contract(I,R,certificate=(k==18));elapsed=time.perf_counter()-t
        if k==18:
            packet=I.as_dict();packet['tour']=A['tour'];packet['optimum']=A['optimum']
            (ROOT/'instances/nonseparable-180-city.json').write_text(json.dumps(packet,indent=2)+'\n')
            (ROOT/'checks/CONTRACTED-DP-CERTIFICATE.json').write_text(json.dumps(A['certificate'],separators=(',',':'))+'\n')
        scales.append(dict(n=I.n,k=k,seed=29,path_units=A['path_units'],lower=R['lower'],optimum=A['optimum'],previous_constructed_upper=R['upper'],secondary_optimum=A['secondary_optimum'],dp_states=A['dp_states'],transitions=A['transition_evaluations'],seconds=elapsed))
    out=dict(status='PASS',full_city_oracle_cases=len(records),all_nonseparable_oracle_cases_exact=True,records=records,scales=scales,elapsed_seconds=time.perf_counter()-ts)
    (ROOT/'checks/CONTRACTED-RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))
if __name__=='__main__':main()
