#!/usr/bin/env python3
"""Literal RYY shifted edge slides; bounded failed repairs, not a general rule."""
from itertools import permutations, product
from pathlib import Path
from hashlib import sha256
import json

HERE=Path(__file__).resolve().parent
def cells(shape):
    return {(i,j) for i,length in enumerate(shape,1) for j in range(i,i+length)}
def superstandard(shape):
    ans={};k=1
    for i,length in enumerate(shape,1):
        for j in range(i,i+length):ans[i,j]=k;k+=1
    return ans
def increasing(boxes):
    for (i,j),a in boxes.items():
        for (r,c),b in boxes.items():
            if (i==r and j<c) or (j==c and i<r):
                if a>=b:return False
    return True
def rectify(outer,inner,boxes,edges,order='row'):
    outer=cells(outer);inner=cells(inner);boxes=dict(boxes)
    edges={i:set(v) for i,v in edges.items()}
    while inner:
        corners=[p for p in inner if (p[0],p[1]+1) not in inner and
                 (p[0]+1,p[1]) not in inner]
        hole=max(corners,key=(lambda p:(p[0],p[1])) if order=='row'
                 else (lambda p:(p[1],p[0])))
        inner.remove(hole)
        while True:
            i,j=hole;right=(i,j+1);down=(i+1,j)
            a=boxes.get(right,float('inf'))
            if i==j:
                b=min(edges.get(i,set()),default=float('inf'))
                if b<a:
                    boxes[hole]=b;edges[i].remove(b)
                    break
                if a<float('inf'):
                    boxes[hole]=boxes.pop(right);hole=right;continue
            else:
                b=boxes.get(down,float('inf'))
                nxt=right if a<b else down
                if min(a,b)<float('inf'):
                    boxes[hole]=boxes.pop(nxt);hole=nxt;continue
            outer.remove(hole)
            if i==j:edges.pop(i,None)
            break
    return boxes,{i:sorted(v) for i,v in edges.items() if v}
def tableaux(outer,inner,N, fixed=None):
    skew=sorted(cells(outer)-cells(inner))
    diagonals=range(1,len(outer)+1)
    box_options=[tuple(fixed[p] for p in skew)] if fixed else permutations(range(1,N+1),len(skew))
    for vals in box_options:
        boxes=dict(zip(skew,vals))
        if not increasing(boxes):continue
        unused=sorted(set(range(1,N+1))-set(vals))
        for locations in product(diagonals,repeat=len(unused)):
            edges={i:set() for i in diagonals}
            valid=True
            for label,i in zip(unused,locations):
                if any(v>=label for (r,c),v in boxes.items() if c==i):
                    valid=False;break
                edges[i].add(label)
            if valid:yield boxes,edges
def count(outer,inner,target,order):
    want=superstandard(target);N=sum(target);total=hits=0
    for boxes,edges in tableaux(outer,inner,N):
        total+=1;b,e=rectify(outer,inner,boxes,edges,order)
        if b==want and not e:hits+=1
    return {'admissible_tableaux':total,'rectification_fibre':hits}
def main():
    outer=(4,3,2,1)
    col_ab=count(outer,(4,3),(3,2,1),'column')
    col_ba=count(outer,(3,2,1),(4,3),'column')
    assert col_ab['rectification_fibre']==20,col_ab
    assert col_ba['rectification_fibre']==16,col_ba
    row_ab=count(outer,(4,3),(3,2,1),'row')
    row_ba=count(outer,(3,2,1),(4,3),'row')
    assert row_ab['rectification_fibre']==row_ba['rectification_fibre']
    outer=(4,2,1);inner=(3,);target=(3,2,1)
    fixed={(1,4):3,(2,2):1,(2,3):2,(3,3):4}
    fibre=[]
    for boxes,edges in tableaux(outer,inner,6,fixed=fixed):
        b,e=rectify(outer,inner,boxes,edges)
        if b==superstandard(target) and not e:
            fibre.append({str(i):sorted(v) for i,v in edges.items() if v})
    assert fibre==[{'3':[5,6]}],fibre
    receipt={'status':'PASS','column_rectification':{'lambda_mu':col_ab,'mu_lambda':col_ba},
       'row_control':{'lambda_mu':row_ab,'mu_lambda':row_ba},
       'fixed_box_fibre':fibre,'fixed_box_fibre_size':len(fibre),
       'required_power_two_divisor':2,
       'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
       'scope':'Independent literal bounded repair obstructions; RYY one-parameter objects are not a proved full OG rule.'}
    (HERE/'EDGE-RECTIFICATION-CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))
if __name__=='__main__':main()

