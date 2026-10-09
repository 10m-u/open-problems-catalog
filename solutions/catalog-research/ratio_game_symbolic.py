"""Control for research/round2-harder.md section 4: symbolic factorisation K = -(n3 D - d3 N) * Q of the Green integrand."""
import sympy as sp
p,q=sp.symbols('p q')
n0,n1,n2,n3,d0,d1,d2,d3=sp.symbols('n0 n1 n2 n3 d0 d1 d2 d3')
N=n0+n1*p+n2*q+n3*p*q; D=d0+d1*p+d2*q+d3*p*q
W=sp.expand(sp.diff(N,p)*D-N*sp.diff(D,p)); V=sp.expand(sp.diff(N,q)*D-N*sp.diff(D,q))
print('W depends on p?',sp.diff(W,p)==0,' V depends on q?',sp.diff(V,q)==0)
print('W =',sp.factor(W)); print('V =',sp.factor(V))
K=sp.expand(sp.diff(V,p)*sp.diff(W,q)*D-sp.diff(W,q)*V*sp.diff(D,p)-sp.diff(V,p)*W*sp.diff(D,q))
print('K factor:',sp.factor(K))
# relation to Hessian-like quantities: compare K with D^? * something in terms of f
