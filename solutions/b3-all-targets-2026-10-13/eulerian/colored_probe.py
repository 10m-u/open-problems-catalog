#!/usr/bin/env python3
from functools import lru_cache
from math import comb,factorial,prod
from itertools import product
from pathlib import Path
import json
HERE=Path(__file__).resolve().parent
@lru_cache(None)
def factors(n):
 if n==1:return ((),)
 return tuple((a,)+v for a in range(2,n+1) if n%a==0 for v in factors(n//a))
@lru_cache(None)
def ref(s):
 if not s:return ((1,),)
 if len(s)==1:return ((1,),)+((0,1),)*(s[0]-1)
 f=ref(s[:-1]);a,b=s[-2:];D=max(map(len,f));out=[]
 for j in range(b):
  z=[0]*(D+1);cut=(j*a+b-1)//b
  for i,q in enumerate(f):
   for k,c in enumerate(q):z[k+int(i<cut)]+=c
  while len(z)>1 and not z[-1]:z.pop()
  out.append(tuple(z))
 return tuple(out)
def euler(s):
 f=ref(tuple(s));out=[0]*max(map(len,f))
 for q in f:
  for k,c in enumerate(q):out[k]+=c
 while len(out)>1 and not out[-1]:out.pop()
 return tuple(out)
def colored(m,r):
 N=sum(m);values=[prod(comb(c*t+a,a) for a,c in zip(m,r)) for t in range(N+1)]
 h=[sum((-1)**j*comb(N+1,j)*values[t-j] for j in range(t+1)) for t in range(N+1)]
 while len(h)>1 and not h[-1]:h.pop()
 return tuple(h)
def vectors(N,limit):
 for f in factors(N):
  if len(f)>limit:continue
  for units in product((0,1),repeat=len(f)-1):
   if len(f)+sum(units)>limit:continue
   s=[f[0]]
   for a,u in zip(f[1:],units):
    if u:s.append(1)
    s.append(a)
   yield tuple(s)
def main():
 cases=[]
 for m in [(1,2),(2,2),(1,3),(2,3),(1,1,2)]:
  for r in product(range(1,4),repeat=len(m)):
   if all(a==1 for a in r):continue
   h=colored(m,r);N=sum(h)
   if N>180:continue
   ss=list(vectors(N,2*(len(h)-1)-1));match=[s for s in ss if euler(s)==h]
   cases.append({'m':m,'r':r,'h':h,'volume':N,'candidate_count':len(ss),'matches':match})
   print(m,r,N,'candidates',len(ss),'matches',len(match),flush=True)
 (HERE/'COLORED-PROBE.json').write_text(json.dumps({'cases':cases,'scope':'Finite exact colored cases; structural classification unresolved.'},indent=2)+'\n')
if __name__=='__main__':main()
