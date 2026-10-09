"""Control for research/round2-harder.md section 4: orbit-averaged extragradient drift on random 2x2 ratio games (Green form I(h)); expect cands=0."""
import numpy as np
rng=np.random.default_rng(11)
M=600; g=(np.arange(M)+0.5)/M
def coeffs(R,S):
    # N = n0 + n1 p + n2 q + n3 pq with x=(p,1-p), y=(q,1-q)
    a,b,c,d=R[0,0],R[0,1],R[1,0],R[1,1]
    n=(d, b-d, c-d, a-b-c+d)
    a,b,c,d=S[0,0],S[0,1],S[1,0],S[1,1]
    m=(d, b-d, c-d, a-b-c+d)
    return n,m
cands=0; tested=0; centers=0
for trial in range(200000):
    R=rng.normal(size=(2,2)); S=rng.uniform(0.02,1,size=(2,2))
    (n0,n1,n2,n3),(d0,d1,d2,d3)=coeffs(R,S)
    Wq=lambda q: d0*n1+d0*n3*q-d1*n0-d1*n2*q+d2*n1*q+d2*n3*q**2-d3*n0*q-d3*n2*q**2
    Vp=lambda p: d0*n2+d0*n3*p+d1*n2*p+d1*n3*p**2-d2*n0-d2*n1*p-d3*n0*p-d3*n1*p**2
    V=Vp(g); W=Wq(g)
    ip=np.where(V[:-1]*V[1:]<0)[0]; iq=np.where(W[:-1]*W[1:]<0)[0]
    if len(ip)==0 or len(iq)==0: continue
    tested+=1
    A=np.concatenate([[0],np.cumsum(V)/M]); A=0.5*(A[1:]+A[:-1])   # antiderivatives on grid
    B=np.concatenate([[0],np.cumsum(W)/M]); B=0.5*(B[1:]+B[:-1])
    dV=np.gradient(V,1/M); dW=np.gradient(W,1/M)
    for i in ip:
        for j in iq:
            sa=np.sign(dV[i]); sb=np.sign(dW[j])
            if sa*sb<=0: continue          # saddle
            centers+=1
            s=sa
            # monotone box around center: extend while s*A increasing away from i
            Ap=s*A; Bq=s*B
            L=i
            while L>0 and Ap[L-1]>=Ap[L]: L-=1
            Rr=i
            while Rr<M-1 and Ap[Rr+1]>=Ap[Rr]: Rr+=1
            Lq=j
            while Lq>0 and Bq[Lq-1]>=Bq[Lq]: Lq-=1
            Rq=j
            while Rq<M-1 and Bq[Rq+1]>=Bq[Rq]: Rq+=1
            # max level fully enclosed: min of boundary values of the box (relative to center)
            h0=Ap[i]+Bq[j]
            hmax=min(Ap[L],Ap[Rr])-Ap[i]+min(Bq[Lq],Bq[Rq])-Bq[j]
            hmax=min(min(Ap[L],Ap[Rr])-Ap[i], min(Bq[Lq],Bq[Rq])-Bq[j])  # conservative: level set stays in box
            if hmax<=1e-9: continue
            P,Q=np.meshgrid(g[L:Rr+1],g[Lq:Rq+1],indexing='ij')
            Hloc=(Ap[L:Rr+1][:,None]+Bq[Lq:Rq+1][None,:])-h0
            Dg=d0+d1*P+d2*Q+d3*P*Q; Ng=n0+n1*P+n2*Q+n3*P*Q
            Qb=(-d0**2*n3+d0*d1*n2-d0*d1*n3*P+d0*d2*n1-d0*d2*n3*Q+d0*d3*n0+2*d0*d3*n1*P+2*d0*d3*n2*Q+d0*d3*n3*P*Q+d1**2*n2*P-2*d1*d2*n0-d1*d2*n1*P-d1*d2*n2*Q-2*d1*d2*n3*P*Q-d1*d3*n0*P+d1*d3*n2*P*Q+d2**2*n1*Q-d2*d3*n0*Q+d2*d3*n1*P*Q-d3**2*n0*P*Q)
            K=-(n3*Dg-d3*Ng)*Qb
            dens=(2*K/Dg**3).ravel(); hv=Hloc.ravel()
            o=np.argsort(hv); hv=hv[o]; cum=np.cumsum(dens[o])/M**2
            sel=hv<=hmax
            if sel.sum()<50: continue
            c=cum[sel]
            # stabilizing sign is the sign near the center (first ~ 2% of cells)
            k0=max(10,int(0.02*len(c))); s0=np.sign(np.median(c[:k0]))
            if s0==0: continue
            frac_bad=np.mean(np.sign(c[k0:])==-s0) if len(c)>k0 else 0
            if frac_bad>0.02 and np.min(s0*c[k0:])< -1e-6*np.max(np.abs(c)):
                cands+=1
                if cands<=8: print('CAND',trial,'R',R.round(3).tolist(),'S',S.round(3).tolist(),'center',round(g[i],3),round(g[j],3),'s0',s0,'min s0*I',float(np.min(s0*c[k0:])),'max|I|',float(np.max(np.abs(c))),flush=True)
    if trial%20000==0: print('progress',trial,'tested',tested,'centers',centers,'cands',cands,flush=True)
print('done tested',tested,'centers',centers,'cands',cands)
