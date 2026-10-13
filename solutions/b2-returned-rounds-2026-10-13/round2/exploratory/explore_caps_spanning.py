from pathlib import Path
import sys,itertools,time,json
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import lil_matrix
from test_structure import geom
n=int(sys.argv[1])if len(sys.argv)>1 else 3;k=int(sys.argv[2])if len(sys.argv)>2 else 3
P,id,mid=geom(n);N=len(P);rows=[];lo=[];hi=[]
def row(d,l=-np.inf,h=np.inf):rows.append(d);lo.append(l);hi.append(h)
for x in range(N):row({c*N+x:1 for c in range(k+1)},1,1)
ls=set()
for x in range(N):
 for y in range(x+1,N):
  z=mid[x][y];ls.add(tuple(sorted([x,y,z])))
  for c in range(k):row({c*N+x:1,c*N+y:1,k*N+z:1},h=2)
for L in ls:row({k*N+x:1 for x in L},h=2)

for point in [(0,)*n]+[tuple(int(j==i)for j in range(n))for i in range(n)]:row({k*N+id[point]:1},1,1)
mat=lil_matrix((len(rows),(k+1)*N))
for i,d in enumerate(rows):
 for j,v in d.items():mat[i,j]=v
obj=np.r_[np.zeros(k*N),-np.ones(N)]
print('start',n,k,mat.shape,flush=True)
t=time.time();r=milp(obj,integrality=np.ones((k+1)*N),bounds=Bounds(0,1),constraints=LinearConstraint(mat.tocsr(),lo,hi),options={'time_limit':15})
print('result',r.message,'objective',r.fun,'bound',getattr(r,'mip_dual_bound',None),'sec',time.time()-t,flush=True)
out={'n':n,'k':k,'solver_status':str(r.message),'objective':None if r.fun is None else float(r.fun),'dual':getattr(r,'mip_dual_bound',None)}
if r.x is not None:
 cs=[[i for i in range(N)if r.x[c*N+i]>.5]for c in range(k+1)];R=cs[-1]
 assert all(mid[x][y]not in R for C in cs[:-1]for x in C for y in C)
 assert all(not set(L)<=set(R)for L in ls)
 out['classes']=[[P[i]for i in C]for C in cs];print(out['classes'],flush=True)
json.dump(out,open(Path(__file__).with_name(f'CAP-SPANNING-MILP-{n}-{k}.json'),'w'),indent=2)
