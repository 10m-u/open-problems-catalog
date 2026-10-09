#!/usr/bin/env python3
"""Exact positivity diagnostics. Python 3.10+, standard library only.

JSON input kinds: finite-row, prefix, matrix, polynomial-matrix, polynomial,
interpolated-polynomial. Polynomial coefficients are in ascending degree order.
Unknown prefix terms are never padded by zero. Every bounded pass states its
scope; only the PF numerator theorem supplies an infinite-sequence certificate.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import comb, prod
import argparse
import json
from pathlib import Path


def rational(x):
    if isinstance(x, bool) or isinstance(x, float):
        raise ValueError('Use exact integers or rational strings, not booleans/floats')
    if not isinstance(x, (int, str, Q)):
        raise ValueError('Expected an integer or rational string')
    return Q(x)


def enc(x):
    if isinstance(x, Q):
        return x.numerator if x.denominator == 1 else str(x)
    if isinstance(x, dict):
        return {str(k): enc(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [enc(v) for v in x]
    return x


def poly(p):
    a = [rational(v) for v in p]
    if not a:
        return (Q(0),)
    while len(a)>1 and a[-1] == 0:
        a.pop()
    return tuple(a)


def padd(a,b):
    return poly([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
                 for i in range(max(len(a),len(b)))])


def pneg(a):
    return tuple(-v for v in a)


def psub(a,b):
    return padd(a,pneg(b))


def pmul(a,b):
    out=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return poly(out)


def pdivmod(a,b):
    a,b=list(poly(a)),poly(b)
    if b==(Q(0),):
        raise ZeroDivisionError('zero polynomial')
    q=[Q(0)]*max(1,len(a)-len(b)+1)
    while len(a)>=len(b) and any(a):
        k=len(a)-len(b); c=a[-1]/b[-1]; q[k]+=c
        for j in range(len(b)):
            a[j+k]-=c*b[j]
        a=list(poly(a))
    return poly(q),poly(a)


def pexactdiv(a,b):
    q,r=pdivmod(a,b)
    if any(r):
        raise ArithmeticError('non-exact polynomial division in certificate calculation')
    return q


def pderivative(a):
    return poly([i*a[i] for i in range(1,len(a))])


def pgcd(a,b):
    while any(b):
        _,r=pdivmod(a,b); a,b=b,r
    return poly([v/a[-1] for v in a])


def peval(a,x):
    v=Q(0)
    for c in reversed(a):
        v=v*x+c
    return v


def variations(signs):
    signs=[v for v in signs if v]
    return sum(a*b<0 for a,b in zip(signs,signs[1:]))


def sturm_report(coefficients):
    p=poly(coefficients)
    if not any(p):
        raise ValueError('the zero polynomial has no finite root multiset')
    degree=len(p)-1
    if degree==0:
        return {'degree':0,'real_rooted':True,'nonpositive_real_roots':True,
                'distinct_real_roots':0,'zero_multiplicity':0,
                'method':'exact rational Sturm sequence'}
    zero=0
    while p[0]==0:
        zero+=1; p=p[1:]
    if len(p)==1:
        return {'degree':degree,'real_rooted':True,'nonpositive_real_roots':True,
                'distinct_real_roots':1,'zero_multiplicity':zero,
                'method':'exact factor x^m'}
    squarefree=pexactdiv(p,pgcd(p,pderivative(p)))
    chain=[squarefree,pderivative(squarefree)]
    while True:
        _,r=pdivmod(chain[-2],chain[-1])
        if not any(r):
            break
        chain.append(pneg(r))
    signs_plus=[1 if f[-1]>0 else -1 for f in chain]
    signs_minus=[s*((-1)**(len(f)-1)) for f,s in zip(chain,signs_plus)]
    signs_zero=[(f[0]>0)-(f[0]<0) for f in chain]
    real=variations(signs_minus)-variations(signs_plus)
    positive=variations(signs_zero)-variations(signs_plus)
    allreal=real==len(squarefree)-1
    return {'degree':degree,'squarefree_nonzero_degree':len(squarefree)-1,
            'distinct_real_roots':real+int(zero>0),'positive_real_roots':positive,
            'zero_multiplicity':zero,'real_rooted':allreal,
            'nonpositive_real_roots':allreal and positive==0,
            'method':'exact rational Sturm sequence',
            'sturm_signs':{'negative_infinity':signs_minus,'zero':signs_zero,
                           'positive_infinity':signs_plus}}


def determinant(M):
    """Rational Gaussian elimination with row pivoting."""
    n=len(M)
    if any(len(r)!=n for r in M):
        raise ValueError('determinant requires a square matrix')
    a=[[rational(v) for v in row] for row in M]
    det=Q(1)
    for k in range(n):
        pivot=next((i for i in range(k,n) if a[i][k]),None)
        if pivot is None:
            return Q(0)
        if pivot!=k:
            a[k],a[pivot]=a[pivot],a[k];det=-det
        p=a[k][k];det*=p
        for i in range(k+1,n):
            t=a[i][k]/p
            for j in range(k+1,n):
                a[i][j]-=t*a[k][j]
            a[i][k]=0
    return det


def polynomial_determinant(M):
    """Bareiss determinant in Q[x], with exact division and row pivoting."""
    n=len(M)
    if any(len(r)!=n for r in M):
        raise ValueError('determinant requires a square matrix')
    if n==0:
        return (Q(1),)
    a=[[poly(v) for v in row] for row in M]
    prev=(Q(1),);sign=1
    for k in range(n-1):
        pivot=next((i for i in range(k,n) if any(a[i][k])),None)
        if pivot is None:
            return (Q(0),)
        if pivot!=k:
            a[k],a[pivot]=a[pivot],a[k];sign=-sign
        p=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                a[i][j]=pexactdiv(psub(pmul(p,a[i][j]),pmul(a[i][k],a[k][j])),prev)
            a[i][k]=(Q(0),)
        prev=p
    return a[-1][-1] if sign==1 else pneg(a[-1][-1])


def psd_report(M):
    """Exact symmetric elimination; negative result includes an original principal minor."""
    n=len(M)
    if any(len(row)!=n for row in M):
        raise ValueError('PSD requires square matrix')
    original=[[rational(v) for v in row] for row in M]
    if any(original[i][j]!=original[j][i] for i in range(n) for j in range(n)):
        raise ValueError('PSD requires symmetric matrix')
    a=[r[:] for r in original];ids=list(range(n));chosen=[];pivots=[]
    def fail(extra):
        indexes=chosen+[ids[i] for i in extra]
        entries=[[original[i][j] for j in indexes] for i in indexes]
        d=determinant(entries)
        assert d<0
        return {'positive_semidefinite':False,'method':'exact symmetric elimination',
                'witness':{'principal_indices':indexes,'entries':entries,'determinant':d}}
    while a:
        ncur=len(a)
        for i in range(ncur):
            if a[i][i]<0:
                return fail([i])
            if a[i][i]==0:
                for j in range(ncur):
                    if a[i][j]!=0:
                        return fail([i,j])
        pick=next((i for i in range(ncur) if a[i][i]>0),None)
        if pick is None:
            return {'positive_semidefinite':True,'rank':len(pivots),
                    'method':'exact symmetric elimination','positive_pivots':pivots,
                    'nullity':len(original)-len(pivots)}
        pivot=a[pick][pick]
        keep=[i for i in range(ncur) if i!=pick]
        new=[[a[i][j]-a[i][pick]*a[pick][j]/pivot for j in keep] for i in keep]
        chosen.append(ids[pick]);pivots.append(pivot)
        ids=[ids[i] for i in keep];a=new
    return {'positive_semidefinite':True,'rank':len(pivots),
            'method':'exact symmetric elimination','positive_pivots':pivots,
            'nullity':len(original)-len(pivots)}


def bounded_minors(M,max_order=3,budget=100000,polynomial=False):
    if not M or not M[0] or any(len(row)!=len(M[0]) for row in M):
        raise ValueError('nonempty rectangular matrix required')
    nr,nc=len(M),len(M[0]);max_order=min(max_order,nr,nc)
    if max_order<1 or budget<1:
        raise ValueError('positive minor order and budget required')
    planned=sum(comb(nr,k)*comb(nc,k) for k in range(1,max_order+1))
    scope={'row_indices':[0,nr-1],'column_indices':[0,nc-1],
           'minor_order_max':max_order,'planned_minor_count':planned,'budget':budget}
    if planned>budget:
        return {'verdict':'insufficient-data','reason':'declared minor budget too small',
                'checked':{**scope,'minors_checked':0}}
    tested=0
    for k in range(1,max_order+1):
        for I in combinations(range(nr),k):
            for J in combinations(range(nc),k):
                entries=[[M[i][j] for j in J] for i in I]
                d=polynomial_determinant(entries) if polynomial else determinant(entries)
                tested+=1
                negatives=[(i,v) for i,v in enumerate(d) if v<0] if polynomial else ([] if d>=0 else [(None,d)])
                if negatives:
                    deg,val=negatives[0]
                    witness={'rows':I,'columns':J,'entries':entries,'determinant':d}
                    if polynomial:
                        witness.update({'negative_coefficient_degree':deg,'negative_coefficient':val})
                    return {'verdict':'counterexample','checked':{**scope,'minors_checked':tested},'witness':witness}
    return {'verdict':'finite-support','checked':{**scope,'minors_checked':tested},'witness':None}


def row_report(values,offset=0,complete=False,order=None):
    a=[rational(v) for v in values]
    if not a:
        raise ValueError('empty row/prefix')
    sign_witness=next(({'index':offset+i,'value':v} for i,v in enumerate(a) if v<0),None)
    result={'known_indices':[offset,offset+len(a)-1],
            'nonnegative':{'holds':sign_witness is None,'witness':sign_witness}}
    down=None;unimodal=None
    for i in range(1,len(a)):
        if a[i]<a[i-1] and down is None:
            down=offset+i-1
        if down is not None and a[i]>a[i-1]:
            unimodal={'descent_at':down,'later_ascent_at':offset+i-1};break
    result['unimodality']={'holds_on_known_data':unimodal is None,'witness':unimodal}
    for label,sense in [('log_concavity',1),('log_convexity',-1)]:
        fail=None
        for i in range(1,len(a)-1):
            left=a[i]**2;right=a[i-1]*a[i+1]
            if sense*(left-right)<0:
                fail={'index':offset+i,'triple':a[i-1:i+2],
                      'center_squared':left,'neighbor_product':right};break
        result[label]={'holds_on_known_data':fail is None,'triples_checked':max(0,len(a)-2),'witness':fail}
    positive=[i for i,v in enumerate(a) if v>0]
    result['internal_zero_in_known_support']=bool(positive and any(v==0 for v in a[min(positive):max(positive)+1]))
    if order is not None:
        if not isinstance(order,int) or order<0:
            raise ValueError('ULC order must be a nonnegative integer')
        if offset!=0 or len(a)!=order+1:
            result['ultra_log_concavity']={'verdict':'insufficient-data',
                'reason':'supply all indices 0,...,N explicitly for ULC','order':order}
        else:
            fail=None
            for k in range(1,order):
                left=a[k]**2*comb(order,k-1)*comb(order,k+1)
                right=a[k-1]*a[k+1]*comb(order,k)**2
                if left<right:
                    fail={'index':k,'cross_multiplied_left':left,'cross_multiplied_right':right};break
            result['ultra_log_concavity']={'holds_on_known_data':fail is None,'order':order,'witness':fail}
    result['verdict']='certified-instance' if complete else 'finite-support'
    result['scope']='complete finite row' if complete else 'known prefix only; missing values remain unknown'
    return result


def hankel_report(values):
    a=[rational(v) for v in values];out={}
    for shift in (0,1):
        size=(len(a)+1-shift)//2
        if size<1:
            out[f'H{shift}']={'verdict':'insufficient-data'};continue
        M=[[a[i+j+shift] for j in range(size)] for i in range(size)]
        out[f'H{shift}']={'size':size,'largest_sequence_index':2*(size-1)+shift,**psd_report(M)}
    fail=any(v.get('positive_semidefinite') is False for v in out.values())
    return {'verdict':'counterexample' if fail else 'finite-support',
            'scope':'necessary finite Hankel PSD constraints; no extension or infinite moment claim',**out}


def hurwitz_report(coefficients,degree_budget=12):
    """Closed left-half-plane test via Hurwitz determinants of p(z+t), t -> 0+.

For nonzero real p with positive leading coefficient, all roots satisfy Re<=0
iff each leading Hurwitz determinant of p(z+t) has positive first nonzero
coefficient in t. This is exactly strict Hurwitz for all sufficiently small t>0.
"""
    p=poly(coefficients)
    if not any(p):
        raise ValueError('zero polynomial is not a stability instance')
    n=len(p)-1
    if n>degree_budget:
        return {'verdict':'insufficient-data','reason':'declared symbolic degree budget exceeded',
                'degree':n,'degree_budget':degree_budget}
    if p[-1]<0:
        p=pneg(p)
    if n==0:
        return {'verdict':'certified-instance','closed_left_half_plane':True,'degree':0,'certificates':[]}
    shifted=[poly([p[k+j]*comb(k+j,k) for j in range(n-k+1)]) for k in range(n+1)]
    H=[[shifted[n-1-2*j+i] if 0<=n-1-2*j+i<=n else (Q(0),)
        for j in range(n)] for i in range(n)]
    cert=[]
    for k in range(1,n+1):
        d=polynomial_determinant([row[:k] for row in H[:k]])
        first=next(((i,v) for i,v in enumerate(d) if v),None)
        cert.append({'order':k,'shift_polynomial':d,'lowest_nonzero_term':first})
        if first is None or first[1]<0:
            return {'verdict':'certified-instance','closed_left_half_plane':False,'degree':n,
                    'method':'exact shifted Hurwitz criterion','certificates':cert}
    return {'verdict':'certified-instance','closed_left_half_plane':True,'degree':n,
            'method':'exact shifted Hurwitz criterion','certificates':cert}


def gamma_report(coefficients):
    p=list(poly(coefficients));d=len(p)-1
    if d==0:
        return {'degree':0,'a':p,'b':[Q(0)],'gamma_a':p,'gamma_b':[],
                'bi_gamma_nonnegative':p[0]>=0}
    b=[];running=Q(0)
    for k in range(d):
        running+=p[d-k]-p[k];b.append(running)
    a=[p[0]]+[p[k]-b[k-1] for k in range(1,d+1)]
    def gamma(f,D):
        assert f==f[::-1]
        rem=f[:];out=[]
        for i in range(D//2+1):
            g=rem[i];out.append(g)
            for j in range(D-2*i+1):
                rem[i+j]-=g*comb(D-2*i,j)
        assert not any(rem)
        return out
    ga,gb=gamma(a,d),gamma(b,d-1)
    return {'degree':d,'a':a,'b':b,'gamma_a':ga,'gamma_b':gb,
            'bi_gamma_nonnegative':all(v>=0 for v in ga+gb),
            'scope':'exact basis conversion; no combinatorial interpretation asserted'}


def interpolated_report(coefficients):
    p=poly(coefficients)
    if not any(p):
        raise ValueError('U_n membership excludes the zero polynomial')
    n=len(p)-1
    values=[peval(p,k) for k in range(n+1)]
    numerator=poly([sum((-1)**j*comb(n+1,j)*values[k-j] for j in range(k+1))
                    for k in range(n+1)])
    roots=sturm_report(numerator)
    membership=all(v>=0 for v in numerator) and roots['nonpositive_real_roots']
    return {'verdict':'structural-certificate' if membership else 'certified-instance',
            'degree':n,'belongs_to_U_n':membership,'generating_function_numerator':numerator,
            'denominator':'(1-z)^'+str(n+1),'numerator_root_test':roots,
            'P_root_test':sturm_report(p),
            'scope':'all sampled values P(k), k>=0, by the exact PF numerator criterion'}


def analyze(data):
    kind=data.get('kind')
    out={'kind':kind,'arithmetic':'exact integers/rationals',
         'metadata':data.get('metadata',{})}
    if kind in ('finite-row','prefix'):
        out['row']=row_report(data['values'],data.get('offset',0),kind=='finite-row',data.get('ulc_order'))
        if data.get('hankel'):
            if data.get('offset',0)!=0:
                out['hankel']={'verdict':'insufficient-data','reason':'moment sequence must include index zero'}
            else:
                out['hankel']=hankel_report(data['values'])
        if 'toeplitz_size' in data:
            size=data['toeplitz_size'];offset=data.get('offset',0)
            vals=[rational(x) for x in data['values']]
            def entry(k):
                if k<0:return Q(0)
                if offset<=k<offset+len(vals):return vals[k-offset]
                if kind=='finite-row':return Q(0)
                raise IndexError('unknown prefix entry')
            try:
                M=[[entry(j-i) for j in range(size)] for i in range(size)]
                out['toeplitz']=bounded_minors(M,data.get('minor_order',3),data.get('minor_budget',100000))
            except IndexError:
                out['toeplitz']={'verdict':'insufficient-data','reason':'Toeplitz window needs unknown prefix entries'}
    elif kind in ('matrix','polynomial-matrix'):
        isp=kind=='polynomial-matrix'
        M=[[poly(x) if isp else rational(x) for x in row] for row in data['entries']]
        out['minors']=bounded_minors(M,data.get('minor_order',3),data.get('minor_budget',100000),isp)
        if data.get('psd'):
            if isp:raise ValueError('PSD specialization is not coefficientwise PSD')
            out['psd']=psd_report(M)
    elif kind=='polynomial':
        coefficients=data['coefficients']
        out['roots']=sturm_report(coefficients)
        nonneg=all(rational(x)>=0 for x in coefficients)
        out['finite_PF_infinity']=nonneg and out['roots']['nonpositive_real_roots']
        out['verdict']='certified-instance'
        if data.get('half_plane'):
            out['half_plane']=hurwitz_report(coefficients,data.get('stability_degree_budget',12))
        if data.get('gamma'):
            out['symmetric_decomposition']=gamma_report(coefficients)
    elif kind=='interpolated-polynomial':
        out.update(interpolated_report(data['coefficients']))
    else:
        raise ValueError('unknown input kind')
    return enc(out)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input',type=Path)
    parser.add_argument('--out',type=Path)
    args=parser.parse_args()
    data=json.loads(args.input.read_text())
    result=[analyze(item) for item in data] if isinstance(data,list) else analyze(data)
    rendered=json.dumps(result,indent=2)+'\n'
    if args.out:
        args.out.write_text(rendered)
    else:
        print(rendered,end='')

if __name__=='__main__':
    main()
