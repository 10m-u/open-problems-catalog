#!/usr/bin/env python3
"""Exact auxiliary witnesses and symbolic all-n first-three Hurwitz controls."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import hashlib
import json
import sympy as sp
from check_hankel_tn2 import rows, mul


def det(a):
    a = [[F(v) for v in row] for row in a]
    ans = F(1)
    for i in range(len(a)):
        j = next((j for j in range(i, len(a)) if a[j][i]), None)
        if j is None:
            return F(0)
        if j != i:
            a[i], a[j] = a[j], a[i]
            ans = -ans
        pivot = a[i][i]
        ans *= pivot
        for j in range(i+1, len(a)):
            ratio = a[j][i]/pivot
            for k in range(i+1, len(a)):
                a[j][k] -= ratio*a[i][k]
    return ans


def hurwitz(ascending, j):
    desc = list(reversed(ascending))
    at = lambda k: desc[k] if 0 <= k < len(desc) else 0
    return det([[at(2*v-u+1) for v in range(j)] for u in range(j)])


def update(g, n, fam):
    out = [F(0)]*(len(g)+1)
    for j, v in enumerate(g):
        if fam == 'C':
            out[j] += (n+1+2*j)*v
            out[j+1] += (4*j*(j-1)+(4*n+14)*j+(n+2)*(n+3))*v
        else:
            out[j] += (j+1)*v
            out[j+1] += (2*j*(j-1)+(2*n+7)*j+F((n+2)*(n+3), 2))*v
    return out


def partition_counts(total):
    def go(j, rem, cur):
        if j > total:
            if rem == 0:
                yield cur
            return
        for k in range(rem//j+1):
            yield from go(j+1, rem-j*k, cur+[k])
    yield from go(1, total, [])


def fall(n, k):
    z = 1
    for j in range(k):
        z *= n-j
    return z


def excess(n, t, fam):
    h = 3 if fam == 'C' else 6
    b = [None]+[sp.Rational(3, 3+j) if fam == 'C'
                else sp.Rational(6, factorial(3+j)) for j in range(1, t+1)]
    ans = 0
    for counts in partition_counts(t):
        term = fall(n-t, sum(counts))
        for j, k in enumerate(counts, 1):
            term *= b[j]**k/factorial(k)
        ans += term
    return sp.cancel(fall(n, t)*h**t*ans/fall(3*n, 2*t))


def run():
    counts = dict(operator_transcriptions=0, strict_LC_controls=0,
                  instability_witnesses=0, hypergeometric_fit_controls=0,
                  symbolic_all_n_identities=0, excess_recurrence_comparisons=0,
                  actual_first_three_hurwitz=0)
    g = mul([F(1,100), F(1,5), F(1)],
            [F(1,100), F(1,10000), F(1)])
    assert g == [F(1,10000),F(2001,10**6),F(1001,50000),F(2001,10000),1]
    for i in range(1, len(g)-1):
        assert g[i]**2 > g[i-1]*g[i+1]
        counts['strict_LC_controls'] += 1
    out = update(g, 6, 'C')
    assert out == [F(7,10000),F(25209,10**6),F(44033,100000),
                   F(286221,50000),F(57021,1000),F(272)]
    assert hurwitz(out, 4) == -F(111702506308959257,1250000000000000000)
    counts['instability_witnesses'] += 1
    h = [1,F(11,10),F(6,5),F(11,10),1]
    for i in range(1,4):
        assert h[i]**2 > h[i-1]*h[i+1]
        counts['strict_LC_controls'] += 1
    assert hurwitz(h,2)==F(11,50) and hurwitz(h,3)==-F(121,125)
    counts['instability_witnesses'] += 1
    kapp = [None]+[1-F(1,10**6)+F(100**j,10**6) for j in range(1,5)]
    bell4 = [kapp[4],4*kapp[1]*kapp[3]+3*kapp[2]**2,
             6*kapp[1]**2*kapp[2],kapp[1]**4]
    assert hurwitz(bell4,2)==-F(33996638137056125099281531049641,10**30)
    counts['instability_witnesses'] += 1

    tabs = {fam: rows(3,24,fam) for fam in ['C','S']}
    expected_fit = {'C':(F(15463,2537),F(2537,1410),F(11500720,47)),
                    'S':(F(-1183,283),F(-283,39),F(431900,39))}
    for fam, tab in tabs.items():
        for n in range(2,25):
            assert update(tab[n-1][1:],n,fam)==tab[n][1:]
            counts['operator_transcriptions'] += 1
        b = list(map(F,tab[4][1:]))
        R,V = b[1]/(3*b[0]),b[2]/(3*b[0])
        A = R**2/(V-R**2)
        t = R/A
        last = b[0]*A*(A+1)*(A+2)*t**3
        assert (A,t,last)==expected_fit[fam] and last != b[3]
        counts['hypergeometric_fit_controls'] += 1
        for n in range(2,25):
            z = tab[n][1:]
            for i in range(1,len(z)-1):
                assert z[i]**2 > z[i-1]*z[i+1]
                counts['strict_LC_controls'] += 1
            for j in range(1,min(3,n-1)+1):
                assert hurwitz(z,j)>0
                counts['actual_first_three_hurwitz'] += 1

    N = sp.Symbol('N')
    D = (3*N-8)*(3*N-7)*(3*N-5)**2*(3*N-4)**2*(3*N-2)**2*(3*N-1)**3
    Q = {
      'C':[688905,33526710,741338325,9828735210,86793244335,535881269178,
           2360037326679,7411985227710,16264270861596,23741850863592,
           20743904820672,8215758210240],
      'S':[945,45990,1013565,13348370,116677223,710430074,3073175215,
           9439360358,20163334460,28511038824,24005911168,9114445760]}
    den = {'C':716800,'S':11200}
    for fam in ['C','S']:
        a = [sp.Integer(1)]+[excess(N,t,fam) for t in range(1,6)]
        delta = a[1]*a[2]*a[3]-a[1]**2*a[4]-a[3]**2+a[1]*a[5]
        q = sum(v*(N-6)**(11-i) for i,v in enumerate(Q[fam]))
        assert sp.cancel(delta-q/(den[fam]*D))==0
        assert all(v>0 for v in Q[fam])
        counts['symbolic_all_n_identities'] += 1
        for n in range(6,25):
            tab = tabs[fam]
            for t in range(1,6):
                assert a[t].subs(N,n)==sp.Rational(tab[n][n-t],tab[n][n])
                counts['excess_recurrence_comparisons'] += 1
            expected = F(int(q.subs(N,n)),int(den[fam]*D.subs(N,n)))
            assert hurwitz(tab[n][1:],3)/F(tab[n][n]**3)==expected
    assert [hurwitz(tabs['C'][n][1:],3) for n in [4,5]] == [
        20329344000,184019656672051200]
    assert [hurwitz(tabs['S'][n][1:],3) for n in [4,5]] == [175700,335144810000]
    receipt = dict(schema='b3-stability-routes-v1',date='2026-10-13',passed=True,
                   counts=counts,
                   scope='Exact auxiliary obstructions and symbolic all-n first-three determinants; no actual-row instability or all-order closure claimed.',
                   checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    Path(__file__).with_name('STABILITY-CHECK-RESULTS.json').write_text(
        json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt))


if __name__=='__main__':
    run()

