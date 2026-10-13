from pathlib import Path
import sys,itertools,json,time
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import lil_matrix
from test_structure import geom,closure
n=int(sys.argv[1]) if len(sys.argv)>1 else 3
P,id,mid=geom(n);N=len(P);rows=[];lbs=[];ubs=[]
def row(d,lo=-np.inf,hi=np.inf):rows.append(d);lbs.append(lo);ubs.append(hi)
for x in range(N):row({x:1,N+x:1},hi=1)
for x in range(N):
 for y in range(x+1,N):
  z=mid[x][y]
  row({x:1,y:1,N+z:1},hi=2)
  row({N+z:1,N+x:-1,x:-1,N+y:-1,y:-1},hi=0)
# R contains an affine basis.
for r in [(0,)*n]+[tuple(int(j==i)for j in range(n))for i in range(n)]:row({N+id[r]:1},lo=1,hi=1)
# A meets the complement of every affine hyperplane.
seen=set()
for u in P[1:]:
 first=next(x for x in u if x)
 if first!=1:continue
 for b in range(3):
  outside=[i for i,x in enumerate(P)if sum(a*v for a,v in zip(u,x))%3!=b]
  row({i:1 for i in outside},lo=1)
mat=lil_matrix((len(rows),2*N))
for i,d in enumerate(rows):
 for j,v in d.items():mat[i,j]=v
print('start',n,mat.shape,flush=True)
t=time.time();res=milp(np.zeros(2*N),integrality=np.ones(2*N),bounds=Bounds(0,1),constraints=LinearConstraint(mat.tocsr(),lbs,ubs),options={'time_limit':15})
print('result',res.message,'time',time.time()-t,flush=True)
out={'n':n,'status':str(res.message)}
if res.x is not None:
 A=[i for i in range(N)if res.x[i]>.5];R=[i for i in range(N)if res.x[N+i]>.5];B=sorted(set(range(N))-set(A)-set(R))
 assert len(closure(A,mid))==len(closure(R,mid))==N
 assert all(mid[x][y]not in R for C in [A,B]for x in C for y in C)
 out.update(A=[P[i]for i in A],B=[P[i]for i in B],R=[P[i]for i in R]);print(json.dumps(out),flush=True)
json.dump(out,open(Path(__file__).with_name(f'SPANNING-SEARCH-{n}.json'),'w'),indent=2)
