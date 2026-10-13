"""Exact secondary optimization on the proved minimum-repair face.

No separability assumption is used. Subset states index paired path units,
not cities. Local Hamiltonian paths are supplied by module_solver's tables.
An optional complete DP certificate is independently verifiable.
"""
from __future__ import annotations
from math import inf
from module_solver import Necklace, solve


def exact_contract(I:Necklace, R:dict|None=None, *, certificate:bool=False,
                   max_units:int=20)->dict:
    R=solve(I) if R is None else R
    m=I.k//2
    if m>max_units:
        raise ValueError(f'{m} path units exceeds explicit implementation guard {max_units}.')
    best=inf; best_tour=None; total_states=0; transitions=0; records=[]
    for P in R['patterns']:
        units=[(j,(j+1)%I.k) for j in P['connectors']]
        endcost={}; witness={}; endpoints={}; owner={}
        for j in range(I.k):
            p=P['ports'][j]
            for val,v,_,path in R['tables'][j,p]:
                internal=val-I.tolls[v]
                if v not in endcost or internal<endcost[v]:
                    endcost[v]=internal;witness[v]=path
            endpoints[j]=sorted(v for v in endcost if v//I.b==j)
        exits=[]; connector_cost=[]
        for q,(a,b) in enumerate(units):
            vv=endpoints[a]+endpoints[b];exits.append(vv)
            for v in vv:owner[v]=q
            connector_cost.append(I.secondary[a*I.b+P['ports'][a]][b*I.b+P['ports'][b]])
        # The minimum over the entrance to a unit can be eliminated before DP.
        transfer={}; entrance={}
        for x in owner:
            for q,(a,b) in enumerate(units):
                if owner[x]==q:continue
                for v in exits[q]:
                    other=b if v//I.b==a else a
                    z,u=min((I.secondary[x][u]+endcost[u],u) for u in endpoints[other])
                    transfer[x,v]=z+endcost[v]+connector_cost[q];entrance[x,v]=u
        def segment(u:int,v:int)->tuple[int,...]:
            return tuple(reversed(witness[u]))+witness[v]
        a,b=units[0]
        pattern_records=[]
        for start in endpoints[a]:
            dp=[{} for _ in range(1<<m)]; parents={}
            for v in endpoints[b]:
                dp[1][v]=endcost[start]+endcost[v]+connector_cost[0]
            for mask in range(1,1<<m,2):
                for x,value in dp[mask].items():
                    for q in range(1,m):
                        if mask>>q&1:continue
                        newmask=mask|1<<q
                        for v in exits[q]:
                            transitions+=1;z=value+transfer[x,v]
                            if z<dp[newmask].get(v,inf):
                                dp[newmask][v]=z;parents[newmask,v]=(x,entrance[x,v])
            final_value,last=min((val+I.secondary[x][start],x) for x,val in dp[-1].items())
            total_states+=sum(len(row) for row in dp)
            if final_value<best:
                best=final_value;segments=[];mask=(1<<m)-1;v=last
                while mask!=1:
                    x,u=parents[mask,v];segments.append(segment(u,v))
                    mask^=1<<owner[v];v=x
                segments.append(segment(start,v));segments.reverse()
                best_tour=tuple(v for seg in segments for v in seg)
            if certificate:
                pattern_records.append(dict(start=start,minimum=final_value,
                    rows=[[mask,v,value] for mask,row in enumerate(dp) for v,value in sorted(row.items())]))
        if certificate:records.append(dict(parity=P['parity'],root_cases=pattern_records))
    assert best_tour is not None
    E=I.cheap();actual=sum(I.B*(2+int(tuple(sorted((best_tour[j],best_tour[(j+1)%I.n]))) not in E))+I.secondary[best_tour[j]][best_tour[(j+1)%I.n]] for j in range(I.n))
    assert sorted(best_tour)==list(range(I.n)) and actual==R['base']+best
    assert R['lower']<=actual<=R['upper']
    out=dict(optimum=actual,secondary_optimum=best,tour=best_tour,
             path_units=m,dp_states=total_states,transition_evaluations=transitions)
    if certificate:out['certificate']=records
    return out
