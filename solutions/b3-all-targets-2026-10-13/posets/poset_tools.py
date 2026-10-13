from collections import defaultdict
from itertools import combinations
from math import comb
from pathlib import Path
import json,sympy as sp
def h_poly(N,rel):
 pred=[sum(1<<a for a,b in rel if b==i) for i in range(N)];current={0:{-1:[1]}}
 for k in range(N):
  nxt={}
  for mask,lasts in current.items():
   for v in range(N):
    if mask>>v&1 or pred[v]&mask!=pred[v]:continue
    out=nxt.setdefault(mask|(1<<v),{}).setdefault(v,[0]*(k+1))
    for last,poly in lasts.items():
     for j,c in enumerate(poly):out[j+int(last>v)]+=c
  current=nxt
 h=[sum(a[j] for a in current[(1<<N)-1].values()) for j in range(N)]
 while len(h)>1 and not h[-1]:h.pop()
 return h

def closure(N,r):
 r=set(r)
 for k in range(N):
  for i in range(N):
   for j in range(N):
    if (i,k) in r and (k,j) in r:r.add((i,j))
 return r

def product2(N,r):
 # Labels first layer then second preserve the order.
 rel={(a,b) for a,b in r}|{(N+a,N+b) for a,b in r}|{(i,N+i) for i in range(N)}
 return h_poly(2*N,rel)

