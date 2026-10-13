import numpy as np,json
from scipy.special import softmax,xlogy
from scipy.optimize import root
from pathlib import Path

def stationarity(z,output=False):
 p=softmax(np.r_[0.,z]);n=len(p);ix=np.arange(n);sm=ix[:,None]+ix[None,:];dm=ix[:,None]-ix[None,:]+n-1
 s=np.convolve(p,p);d=np.convolve(p,p[::-1]);h=-np.sum(xlogy(p,p));hs=-np.sum(xlogy(s,s));hd=-np.sum(xlogy(d,d));r=(hd-h)/(hs-h)
 gh=-np.log(p)-1;gs=-2*((np.log(s)[sm]+1)@p);gd=-2*((np.log(d)[dm]+1)@p)
 g=gd-r*gs+(r-1)*gh
 return (r,p,g-g[0])if output else g[1:]-g[0]
ps=np.array([.88162304,.10154519,.01485728,.00177393,.00018242,.00001665,.00000138,.00000011])
results=[]
for n in [5,8,10,12,16,24,40]:
 p=np.r_[ps,ps[-1]*.06**np.arange(1,max(1,n-len(ps)+1))][:n]
 z=np.log(p[1:]/p[0]);fit=root(stationarity,z,method='hybr',options={'xtol':1e-10})
 r,p,g=stationarity(fit.x,True)
 print(n,fit.success,r,'res',np.max(np.abs(g)),p,flush=True)
 results.append({'n':n,'converged':bool(fit.success),'ratio':r,'max_residual':float(np.max(np.abs(g))),'p':p.tolist()})
Path(__file__).with_name('REFINED-ENTROPY-SEARCH.json').write_text(json.dumps(results,indent=2))
