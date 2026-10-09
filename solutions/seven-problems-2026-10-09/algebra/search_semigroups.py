#!/usr/bin/env python3
"""Finite model search. A SAT witness is checked separately; UNSAT is solver evidence."""
import argparse
import itertools
import json
import time
import z3


def build(order, question, variety, timeout):
    z3.set_param(proof=True)
    sort, es = z3.EnumSort('S', ['e'+str(i) for i in range(order)])
    mul = z3.Function('mul',sort,sort,sort)
    sol = z3.Solver()
    sol.set(timeout=timeout)
    for a,b,c in itertools.product(es, repeat=3):
        sol.add(mul(mul(a,b),c)==mul(a,mul(b,c)))
    if variety in ('band','normal-band'):
        for a in es: sol.add(mul(a,a)==a)
    else:
        inv=z3.Function('inv',sort,sort)
        for a in es:
            sol.add(mul(a,inv(a))==mul(inv(a),a),mul(mul(a,inv(a)),a)==a)
    if variety=='normal-band':
        for a,b,c in itertools.product(es,repeat=3):
            sol.add(mul(mul(mul(a,b),c),a)==mul(mul(mul(a,c),b),a))
    comm=lambda a,b:mul(a,b)==mul(b,a)
    nc=lambda a:z3.Or([z3.Not(comm(a,b)) for b in es])
    left=lambda a,path,d:z3.And([mul(a,b)==mul(d,b) for b in path])
    if question=='Q3102':
        a,b,c,d=es[:4]
        sol.add(*[nc(x) for x in (a,b,c,d)],comm(a,b),comm(b,c),comm(c,d),left(a,(a,b,c,d),d))
        for x,y in itertools.combinations(es,2):
            sol.add(z3.Not(z3.And(nc(x),nc(y),comm(x,y),left(x,(x,y),y))))
        for x,z in itertools.combinations(es,2):
            for y in es:
                if y in (x,z):continue
                sol.add(z3.Not(z3.And(nc(x),nc(y),nc(z),comm(x,y),comm(y,z),left(x,(x,y,z),z))))
    else:
        cycle=es[:5]
        sol.add(*[nc(x) for x in cycle])
        for i in range(5):sol.add(comm(cycle[i],cycle[(i+1)%5]))
        for a,b,c in itertools.combinations(es,3):
            sol.add(z3.Not(z3.And(nc(a),nc(b),nc(c),comm(a,b),comm(b,c),comm(c,a))))
        for subset in itertools.combinations(es,4):
            a=subset[0]
            for b,c,d in itertools.permutations(subset[1:]):
                if str(b)>str(d):continue
                sol.add(z3.Not(z3.And(nc(a),nc(b),nc(c),nc(d),comm(a,b),comm(b,c),comm(c,d),comm(d,a))))
    return sol,mul,es


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--order',type=int,required=True)
    p.add_argument('--question',choices=['Q3101','Q3102'],required=True)
    p.add_argument('--variety',choices=['band','normal-band','completely-regular'],default='band')
    p.add_argument('--timeout-ms',type=int,default=60000)
    p.add_argument('--output')
    args=p.parse_args()
    start=time.time()
    s,m,es=build(args.order,args.question,args.variety,args.timeout_ms)
    build_time=time.time()-start
    result=s.check()
    data=dict(question=args.question,order=args.order,variety=args.variety,result=str(result),build_seconds=round(build_time,3),solve_seconds=round(time.time()-start-build_time,3),z3_version=z3.get_version_string())
    if result==z3.sat:
        model=s.model()
        labels={str(e):i for i,e in enumerate(es)}
        data['multiplication_table']=[[labels[str(model.eval(m(a,b)))] for b in es] for a in es]
    elif result==z3.unknown:data['reason_unknown']=s.reason_unknown()
    if args.output:
        with open(args.output,'w') as f:json.dump(data,f,indent=2);f.write('\n')
    print(json.dumps(data))
if __name__=='__main__':main()
