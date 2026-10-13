import numpy as np,itertools,json,time
from pathlib import Path
from scipy.special import softmax
from explore_correlations import Problem
rng=np.random.default_rng(120266);t=time.time();records=[];best=1.4051810316
supports=[]
for n in [8,12,20]:supports.append(np.arange(n)[:,None])
for n in [3,4,6]:supports.append(np.array(list(itertools.product(range(n),repeat=2))))
for _ in range(30):supports.append(np.sort(rng.choice(30,rng.integers(5,13),replace=False))[:,None])
for sidx,x in enumerate(supports):
 p=Problem(x)
 for j in range(8 if sidx<6 else 2):
  z=rng.normal(0,2,len(x));z[rng.integers(len(x))]+=rng.uniform(2,7)
  fit=p.fit(z);r=-fit.fun
  if r>best+1e-10:
   best=r;rec={'support':x.tolist(),'probabilities':softmax(fit.x).tolist(),'ratio':r};records.append(rec)
   print('NEW',r,rec,flush=True)
  if time.time()-t>16:break
 if time.time()-t>16:break
print('finished',sidx,'best',best,'seconds',time.time()-t)
Path(__file__).with_name('OTHER-SUPPORT-SEARCH.json').write_text(json.dumps({'best':best,'improvements':records,'last_support_index':sidx},indent=2))
