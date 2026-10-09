"""Exploratory LP search; exact certificates are generated separately."""
from itertools import product, combinations
from fractions import Fraction
import numpy as np
from scipy.optimize import linprog

STATES = np.array(list(product([0, 1], repeat=4)))
SUBSETS = STATES.copy()
PAIRS = list(combinations(range(4), 2))

def solve(a, p):
    x = (STATES-np.array(p))*np.array(a)
    cost = (SUBSETS @ x.T)**2
    cov = np.array([x[:,i]*x[:,j] for i,j in PAIRS])
    eq = np.column_stack([np.vstack([np.ones(16), STATES.T]),np.zeros(5)])
    beq = np.r_[1,p]
    ub = np.column_stack([cost,-np.ones(16)])
    nc = np.column_stack([cov,np.zeros(6)])
    objective = np.r_[np.zeros(16),1]
    args = dict(c=objective,A_eq=eq,b_eq=beq,bounds=[(0,None)]*16+[(None,None)],method='highs')
    first = linprog(A_ub=ub,b_ub=np.zeros(16),**args)
    second = linprog(A_ub=np.vstack([ub,nc]),b_ub=np.zeros(22),**args)
    return first,second

if __name__ == '__main__':
    candidates = []
    ps = [[.5,2/3,3/5,4/7,5/9,8/15], [.5,1/3,2/5,3/7,4/9,8/17], [.25,1/3,.2], [.5,1/3,2/5,3/7,5/12]]
    for p in product(*ps):
        a = [7,3,5,7]
        first,second=solve(a,p)
        if second.fun-first.fun>1e-8:
            complexity=sum(Fraction(v).limit_denominator().denominator for v in p)
            candidates.append((complexity,second.fun-first.fun,p))
    candidates.sort(key=lambda z:(z[0],-z[1]))
    for row in candidates[:20]:print(row,flush=True)
