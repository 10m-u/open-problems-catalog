import itertools,json,sys,time
from pathlib import Path
import numpy as np
from scipy.sparse import lil_matrix
from scipy.optimize import milp,Bounds,LinearConstraint
n=int(sys.argv[1]) if len(sys.argv)>1 else 4
P=list(itertools.product(range(3),repeat=n)); ix={x:i for i,x in enumerate(P)}; N=len(P)
add=lambda x,y:tuple((a+b)%3 for a,b in zip(x,y))
sc=lambda c,x:tuple(c*a%3 for a in x)
mid=[[ix[sc(2,add(x,y))]for y in P]for x in P]
planes=set()
for i,u in enumerate(P[1:],1):
 if next(c for c in u if c)!=1:continue
 for v in P[i+1:]:
  if v in [u,sc(2,u)]:continue
  plane=frozenset(ix[add(sc(a,u),sc(b,v))]for a in range(3)for b in range(3))
  planes.add(plane)
allplanes=set()
for H in planes:
 for a in P:
  allplanes.add(tuple(sorted(ix[add(a,P[j])]for j in H)))
rows=[];lo=[];hi=[]
def row(d,l=-np.inf,h=np.inf):rows.append(d);lo.append(l);hi.append(h)
# first variables A, second R; B=1-A-R
for x in range(N):row({x:1,N+x:1},h=1)
for x in range(N):
 for y in range(x+1,N):
  z=mid[x][y]
  row({x:1,y:1,N+z:1},h=2)
  row({N+z:1,N+x:-1,x:-1,N+y:-1,y:-1},h=0)
for pl in allplanes:row({N+x:1 for x in pl},h=8)
# affinely spanning remainder
for x in [(0,)*n]+[tuple(int(i==j)for i in range(n))for j in range(n)]:row({N+ix[x]:1},l=1,h=1)
M=lil_matrix((len(rows),2*N))
for i,d in enumerate(rows):
 for j,c in d.items():M[i,j]=c
c=np.r_[np.zeros(N),-np.ones(N)]
print('constraints',len(rows),'planes',len(allplanes),flush=True)
t=time.time();r=milp(c,integrality=np.ones(2*N),bounds=Bounds(0,1),constraints=LinearConstraint(M.tocsr(),lo,hi),options={'time_limit':25})
out={'n':n,'status':str(r.message),'seconds':time.time()-t,'objective':r.fun}
if r.x is not None:
 A={x for x in range(N)if r.x[x]>.5};R={x for x in range(N)if r.x[N+x]>.5};B=set(range(N))-A-R
 assert all(mid[x][y]not in R for S in [A,B]for x in S for y in S)
 assert all(not set(pl)<=R for pl in allplanes)
 out.update(A=[P[x]for x in A],B=[P[x]for x in B],R=[P[x]for x in R])
print(out,flush=True)
Path(__file__).with_name(f'SPANNING-PLANE-FREE-{n}.json').write_text(json.dumps(out,indent=2))
