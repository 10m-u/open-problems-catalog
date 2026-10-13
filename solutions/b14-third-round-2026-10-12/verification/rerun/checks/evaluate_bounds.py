#!/usr/bin/env python3
"""Numerically evaluate proved 1D bounds; these are not interval certificates.

Requires mpmath. No random sampling is used. The exact 3/5 certificate is in
check_sharp_rate.py and does not depend on this numerical computation.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import mpmath as mp

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name('NUMERICAL-RESULTS.json'))
    args = parser.parse_args()
    mp.mp.dps = 80
    def J(a):
        return mp.sqrt(mp.pi/2)*mp.exp(a*a/2)*mp.erfc(a/mp.sqrt(2))
    a = mp.findroot(lambda x: 2*x*J(x)-1, (mp.mpf('0.6'), mp.mpf('0.63')))
    ja = J(a)
    H = mp.exp(a*a/2)*ja
    rho = H/mp.sqrt(mp.e)
    variance = 1-2*a*a
    # A second route uses direct numerical integration rather than erfc.
    ja_quad = mp.quad(lambda y: mp.exp(-y*y/2-a*y), [0, 1, 3, 8, mp.inf])
    assert abs(ja-ja_quad) < mp.mpf('1e-65')
    mean_quad = mp.quad(lambda y: y*mp.exp(-y*y/2-a*y)/ja, [0,1,3,8,mp.inf])
    assert abs(mean_quad-a) < mp.mpf('1e-65')
    def tail(t):
        return mp.sqrt(mp.pi/2)*mp.exp(a*a/2)*mp.erfc((a+t)/mp.sqrt(2))
    def upper_log_p(n, delta):
        beta = 1-2*delta
        s = mp.sqrt(beta*(n-6))
        t = s*delta
        one = (ja-tail(t))/s + (1-delta)*mp.exp(-t*t/2-a*t)
        return (n-6)*a*a/2+n*mp.log(one)
    def lower_log_p(n, delta):
        b = 1/(1-2*delta*delta)
        R = delta*mp.sqrt(b*n)
        correction = mp.exp(-variance/2)-n*tail(R)/ja
        if correction <= 0:
            return mp.ninf
        return n*mp.log(H)-n*mp.log(b*n)/2+mp.log(correction)
    rows = []
    for n in [10, 100, 1000, 10000, 100000, 1000000, 100000000]:
        deltas = {mp.mpf(k)/1000 for k in range(1, 491, 5)}
        scale = mp.sqrt(mp.log(n)/n)
        deltas.update(mp.mpf(k)*scale/20 for k in range(1, 121))
        deltas = sorted(d for d in deltas if 0 < d < mp.mpf('0.5'))
        u, du = min((upper_log_p(n, d), d) for d in deltas)
        l, dl = max((lower_log_p(n, d), d) for d in deltas)
        logprefactor = mp.loggamma(n+1)/2-mp.log(2*n)
        lo = mp.exp((logprefactor+l)/n)
        up = mp.exp((logprefactor+u)/n)
        assert lo <= up
        rows.append({'n': n, 'normalized_nth_root_lower': float(lo),
                     'normalized_nth_root_upper': float(up),
                     'chosen_lower_delta': float(dl), 'chosen_upper_delta': float(du),
                     'delta_candidates': len(deltas)})
    exp_cases = 0
    for delta in [mp.mpf('0.01'), mp.mpf('0.1'), mp.mpf('0.3')]:
        fm, fp = mp.exp(-2*delta), mp.mpf(1)
        for i in range(1, 21):
            for j in range(1, 21):
                s, t = 2*delta*i/20, 2*delta*j/20
                m = min(s,t)
                ps, pt = 1-mp.exp(-s)*(1+s), 1-mp.exp(-t)*(1+t)
                overlap = 1-mp.exp(-m)-m*(mp.exp(-s)+mp.exp(-t)) + mp.exp(-s-t)*(mp.exp(m)-1)
                assert fm*fm*s*s/2 <= ps <= fp*fp*s*s/2
                assert overlap <= delta*fp*(ps+pt)
                exp_cases += 1
    result = {'status': 'passed', 'arithmetic': 'mpmath, 80 decimal digits; no directed rounding',
              'mpmath_version': mp.__version__, 'a_star': mp.nstr(a, 65), 'J_a_star': mp.nstr(ja,65),
              'H': mp.nstr(H,65), 'rho': mp.nstr(rho,65), 'tilted_variance': mp.nstr(variance,65),
              'independent_integral_checks': 2, 'exponential_distribution_local_checks': exp_cases,
              'finite_bounds': rows,
              'scope': 'Deterministic numerical evaluation of proved bounds, not estimates of the actual count; no simulation.'}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    main()
