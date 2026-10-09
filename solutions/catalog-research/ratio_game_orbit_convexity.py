"""Control for research/round2-harder.md section 4: curvature of closed Hamiltonian orbits of 2x2 ratio games; expect zero negative-curvature fraction, and some non-convex A or B on the swept range."""
import numpy as np
rng=np.random.default_rng(13)
M=400; g=(np.arange(M)+0.5)/M
n=0; worst=0; ex=None; worst_full=0
for trial in range(60000):
    R=rng.normal(size=(2,2)); S=rng.uniform(0.02,1,size=(2,2))
    a,b,c,d=R[0,0],R[0,1],R[1,0],R[1,1]; n0,n1,n2,n3=d,b-d,c-d,a-b-c+d
    a,b,c,d=S[0,0],S[0,1],S[1,0],S[1,1]; d0,d1,d2,d3=d,b-d,c-d,a-b-c+d
    V=d0*n2+d0*n3*g+d1*n2*g+d1*n3*g**2-d2*n0-d2*n1*g-d3*n0*g-d3*n1*g**2
    W=d0*n1+d0*n3*g-d1*n0-d1*n2*g+d2*n1*g+d2*n3*g**2-d3*n0*g-d3*n2*g**2
    dV=d0*n3+d1*n2+2*d1*n3*g-d2*n1-d3*n0-2*d3*n1*g
    dW=d0*n3-d1*n2+d2*n1+2*d2*n3*g-d3*n0-2*d3*n2*g
    ip=np.where(V[:-1]*V[1:]<0)[0]; iq=np.where(W[:-1]*W[1:]<0)[0]
    if len(ip)!=1 or len(iq)!=1: continue
    i,j=ip[0],iq[0]; s=np.sign(dV[i])
    if s*np.sign(dW[j])<=0: continue
    n+=1
    A=np.cumsum(V)/M*s; B=np.cumsum(W)/M*s
    L=i
    while L>0 and A[L-1]>=A[L]: L-=1
    Rr=i
    while Rr<M-1 and A[Rr+1]>=A[Rr]: Rr+=1
    Lq=j
    while Lq>0 and B[Lq-1]>=B[Lq]: Lq-=1
    Rq=j
    while Rq<M-1 and B[Rq+1]>=B[Rq]: Rq+=1
    hmax=min(min(A[L],A[Rr])-A[i], min(B[Lq],B[Rq])-B[j])
    Hl=(A[L:Rr+1][:,None]-A[i])+(B[Lq:Rq+1][None,:]-B[j])
    curvnum=s*(dV[L:Rr+1][:,None]*W[Lq:Rq+1][None,:]**2+dW[Lq:Rq+1][None,:]*V[L:Rr+1][:,None]**2)
    region=Hl<=hmax
    frac=np.mean(curvnum[region]<-1e-12) if region.any() else 0
    if frac>worst: worst=frac; ex=(trial,R.round(3).tolist(),S.round(3).tolist(),g[i],g[j],hmax)
print('centers',n,'max fraction of enclosed-orbit region with negative curvature',worst)
print('example',ex)

# second test: does s*V' (and s*W') keep sign on the p-range (q-range) swept by enclosed orbits?
rng=np.random.default_rng(14); n=0; viol=0; reasons={'boundary':0,'critical':0}
for trial in range(60000):
    R=rng.normal(size=(2,2)); S=rng.uniform(0.02,1,size=(2,2))
    a,b,c,d=R[0,0],R[0,1],R[1,0],R[1,1]; n0,n1,n2,n3=d,b-d,c-d,a-b-c+d
    a,b,c,d=S[0,0],S[0,1],S[1,0],S[1,1]; d0,d1,d2,d3=d,b-d,c-d,a-b-c+d
    V=d0*n2+d0*n3*g+d1*n2*g+d1*n3*g**2-d2*n0-d2*n1*g-d3*n0*g-d3*n1*g**2
    W=d0*n1+d0*n3*g-d1*n0-d1*n2*g+d2*n1*g+d2*n3*g**2-d3*n0*g-d3*n2*g**2
    dV=d0*n3+d1*n2+2*d1*n3*g-d2*n1-d3*n0-2*d3*n1*g
    dW=d0*n3-d1*n2+d2*n1+2*d2*n3*g-d3*n0-2*d3*n2*g
    ip=np.where(V[:-1]*V[1:]<0)[0]; iq=np.where(W[:-1]*W[1:]<0)[0]
    if len(ip)!=1 or len(iq)!=1: continue
    i,j=ip[0],iq[0]; s=np.sign(dV[i])
    if s*np.sign(dW[j])<=0: continue
    n+=1
    A=np.cumsum(V)/M*s; B=np.cumsum(W)/M*s
    hA=lambda k: A[k]-A[i]; hB=lambda k: B[k]-B[j]
    L=i
    while L>0 and A[L-1]>=A[L]: L-=1
    Rr=i
    while Rr<M-1 and A[Rr+1]>=A[Rr]: Rr+=1
    Lq=j
    while Lq>0 and B[Lq-1]>=B[Lq]: Lq-=1
    Rq=j
    while Rq<M-1 and B[Rq+1]>=B[Rq]: Rq+=1
    hmax=min(min(hA(L),hA(Rr)), min(hB(Lq),hB(Rq)))
    pr=[k for k in range(L,Rr+1) if hA(k)<=hmax]; qr=[k for k in range(Lq,Rq+1) if hB(k)<=hmax]
    if np.any(s*dV[pr]<-1e-12) or np.any(s*dW[qr]<-1e-12): viol+=1
print('centers',n,'cases where A or B is non-convex on the swept range',viol)
