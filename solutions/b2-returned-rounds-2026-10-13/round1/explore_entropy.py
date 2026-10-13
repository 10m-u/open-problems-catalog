import numpy as np
from scipy.optimize import minimize, minimize_scalar
from scipy.special import xlogy

def ent(p):
    return -float(np.sum(xlogy(p,p)))
def ratio(p):
    p=np.asarray(p,dtype=float)
    p=p/p.sum()
    h=ent(p); s=ent(np.convolve(p,p)); d=ent(np.convolve(p,p[::-1]))
    return (d-h)/(s-h) if s-h>1e-12 else 0.
for n in [3,4,5,8,12,20,40]:
    def softmax(z):
        z=np.r_[0,z]; z=z-z.max(); p=np.exp(z); return p/p.sum()
    best=None
    for q in [.025,.08,.2,.5]:
        fit=minimize(lambda z:-ratio(softmax(z)),np.arange(1,n)*np.log(q),method='L-BFGS-B',bounds=[(-40,10)]*(n-1),options={'maxiter':700,'ftol':1e-13,'gtol':1e-8})
        if best is None or fit.fun<best.fun: best=fit
    print(n,-best.fun,softmax(best.x)[:12],flush=True)
opt=minimize_scalar(lambda q:-ratio((1-q)*q**np.arange(100)),bounds=(.001,.9),method='bounded',options={'xatol':1e-14})
print('geometric',opt.x,-opt.fun,flush=True)
