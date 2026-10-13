"""Numerical discovery only. Exact certificates are produced separately."""
import itertools, json, time
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
from scipy.special import xlogy, softmax

class Problem:
    def __init__(self, support):
        self.x=np.asarray(support,dtype=int)
        if self.x.ndim==1:self.x=self.x[:,None]
        n=len(self.x)
        sums=self.x[:,None,:]+self.x[None,:,:]
        diffs=self.x[:,None,:]-self.x[None,:,:]
        self.si=np.unique(sums.reshape(n*n,-1),axis=0,return_inverse=True)[1].reshape(n,n)
        self.di=np.unique(diffs.reshape(n*n,-1),axis=0,return_inverse=True)[1].reshape(n,n)
        self.ns=self.si.max()+1;self.nd=self.di.max()+1
    def evaluate(self,z):
        p=softmax(z); w=np.outer(p,p).ravel()
        s=np.bincount(self.si.ravel(),w,minlength=self.ns)
        d=np.bincount(self.di.ravel(),w,minlength=self.nd)
        h=-np.sum(xlogy(p,p));hs=-np.sum(xlogy(s,s));hd=-np.sum(xlogy(d,d))
        den=hs-h
        if den<1e-13:return 0.,np.zeros_like(z)
        r=(hd-h)/den
        gh=-np.log(np.maximum(p,1e-300))-1
        gs=-2*((np.log(np.maximum(s,1e-300))[self.si]+1)@p)
        gd=-2*((np.log(np.maximum(d,1e-300))[self.di]+1)@p)
        gr=(gd-r*gs+(r-1)*gh)/den
        return -r, -p*(gr-np.dot(p,gr))
    def fit(self,z):
        return minimize(self.evaluate,z,jac=True,method='L-BFGS-B',bounds=[(-60,20)]*len(z),options={'maxiter':1200,'ftol':1e-14,'gtol':1e-9,'maxls':40})

def main():
 rng=np.random.default_rng(46604296);t=time.time(); best=0;results=[]
 supports=[np.array(list(itertools.product(range(n),repeat=2))) for n in [2,3,4,6,8]]
 supports+=[np.array(list(itertools.product(range(n),repeat=3))) for n in [2,3,4]]
 supports +=[np.arange(n)[:,None] for n in [12,20,40,70]]
 base=np.array([.88162304,.10154519,.01485728,.00177393,.00018242,.00001665,.00000138,.00000011])
 for x in supports:
  pr=Problem(x); local=0
  for j in range(5):
   z=np.log(base[np.minimum(x,7)]).sum(axis=1)
   if j:z+=rng.normal(0,j*.8,len(x))
   fit=pr.fit(z);r=-fit.fun
   if r>local:local=r
   if r>best+1e-10:
    best=r;record={'support':x.tolist(),'p':softmax(fit.x).tolist(),'ratio':r,'status':str(fit.message),'elapsed':time.time()-t}
    results.append(record)
    Path(__file__).with_name('CORRELATION-SEARCH.json').write_text(json.dumps(results,indent=2))
    print('NEW',x.shape,r,'seconds',time.time()-t,flush=True)
  print('DONE',x.shape,local,'seconds',time.time()-t,flush=True)
if __name__=='__main__':main()
