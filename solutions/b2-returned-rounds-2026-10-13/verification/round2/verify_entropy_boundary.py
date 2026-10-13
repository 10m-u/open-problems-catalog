#!/usr/bin/env python3
"""Exact controls for the support-boundary perturbation formula.

Checks new-output first-order masses without floating point, verifies the
endpoint identities, and certifies a concrete support-extension ascent.
Requires only the standard library and the adjacent certify_entropy.py.
"""
from __future__ import annotations
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json
from certify_entropy import certify, interval_record


def escape_masses(support: list[int], weights: list[int], z: int) -> tuple[F,F]:
    assert len(support) == len(weights) and len(set(support)) == len(support)
    assert z not in support and min(weights) > 0
    total = sum(weights)
    sums = {x+y for x in support for y in support}
    diffs = {x-y for x in support for y in support}
    up = sum((F(w,total) for x,w in zip(support,weights) if z+x not in sums),F(0))
    um = sum((F(w,total) for x,w in zip(support,weights) if z-x not in diffs),F(0))
    # Independently aggregate output collisions in the first-order cross terms.
    cross_sum, cross_diff = defaultdict(F), defaultdict(F)
    for x,w in zip(support,weights):
        cross_sum[z+x] += 2*F(w,total)
        cross_diff[z-x] += F(w,total)
        cross_diff[x-z] += F(w,total)
    assert sum((v for y,v in cross_sum.items() if y not in sums),F(0)) == 2*up
    assert sum((v for y,v in cross_diff.items() if y not in diffs),F(0)) == 2*um
    triple_set = {a+b-c for a in support for b in support for c in support}
    if z not in triple_set:
        assert up == 1 == um
    return up,um


def boundary_report(support: list[int], weights: list[int]) -> dict:
    """Certify rho>1, then enclose L at every candidate new integer atom.

    A strictly positive lower endpoint proves eventual ascent. Intervals
    containing zero are reported as undetermined, never rounded to a sign.
    Absence of a positive coefficient is NOT an optimality certificate.
    """
    cert = certify('boundary_screen_input',weights,F(1),support=support)
    interval = cert['ratio']
    rl = F(int(interval['scaled_lower_integer']), int(interval['decimal_scale']))
    ru = F(int(interval['scaled_upper_integer']), int(interval['decimal_scale']))
    candidates = sorted({a+b-c for a in support for b in support for c in support}-set(support))
    rows = []
    for z in candidates:
        up,um = escape_masses(support,weights,z)
        a,b = 2*um-1, 1-2*up
        low,high = a+min(b*rl,b*ru), a+max(b*rl,b*ru)
        sign = 'positive' if low > 0 else 'negative' if high < 0 else 'undetermined'
        rows.append({'new_atom':z,'u_plus':str(up),'u_minus':str(um),
                     'L_interval':interval_record((low,high)),'sign':sign})
    return {'support':support,'weights':weights,'ratio':interval,
            'outside_candidate_set':'strictly negative',
            'positive_directions':sum(row['sign']=='positive' for row in rows),
            'candidate_count':len(rows),'rows':rows,
            'warning':'Necessary test only; passing is not a global optimality certificate.'}


def main() -> None:
    cases = 0
    for size in range(2,8):
        for support_tuple in combinations(range(7),size):
            support = list(support_tuple)
            for weights in [list(range(1,size+1)), list(range(size,0,-1))]:
                for z in range(-3,10):
                    if z not in support:
                        escape_masses(support,weights,z)
                        cases += 1
    endpoint_cases = 0
    r = F(7,5)
    for n in range(1,9):
        for weights in [list(range(1,n+2)),list(range(n+1,0,-1))]:
            p0,pn = F(weights[0],sum(weights)),F(weights[-1],sum(weights))
            up,um = escape_masses(list(range(n+1)),weights,n+1)
            vp,vm = escape_masses(list(range(n+1)),weights,-1)
            right = 2*um-1-r*(2*up-1)
            left = 2*vm-1-r*(2*vp-1)
            assert up == pn and um == p0 and vp == p0 and vm == pn
            assert right+left == 2*(r-1)*(1-p0-pn)
            assert max(right,left) > 0
            endpoint_cases += 1
    heavy_cases = 0
    for size in range(2,8):
        for support in combinations(range(7),size):
            weights = [size-1]+[1]*(size-1)  # Exactly half the mass at the minimum.
            if size == 2:                  # Fair two-point law has ratio one.
                weights[0] += 1
            up,um = escape_masses(list(support),weights,2*support[-1]-support[0])
            pa,pb = F(weights[0],sum(weights)),F(weights[-1],sum(weights))
            assert up == 1-pa and um == 1-pb
            assert 2*um-1-r*(2*up-1) > 0
            heavy_cases += 1
    # A necessary-only negative control: uniform {0,1,4} passes every
    # leading boundary test despite a ratio strictly between 1 and 6/5.
    sidon = [0,1,4]
    candidates = sorted({a+b-c for a in sidon for b in sidon for c in sidon}-set(sidon))
    assert candidates == [-4,-3,-2,-1,2,3,5,7,8]
    for z in candidates:
        up,um = escape_masses(sidon,[1,1,1],z)
        assert 1-up == F(1,3) and 1-um in (F(1,3),F(2,3))
    # A concrete exact instance of the ascent mechanism; numerical searches
    # are neither called nor required for this certificate.
    old = [8830,1009,143,16,2]
    old_result = certify('five_point_before_extension',old,F(281,200))
    upper = F(int(old_result['ratio']['scaled_upper_integer']),
              int(old_result['ratio']['decimal_scale']))
    e = 10**6
    extended = [w*(e-1) for w in old]+[sum(old)]
    extension_result = certify('six_point_after_epsilon_1e_minus6',extended,upper)
    twelve = [88162313713840,10154514342618,1485728499913,177389643984,
              18240191721,1665031585,137417507,10383619,725058,47123,2867,165]
    full_report = boundary_report(list(range(12)),twelve)
    negative_report = boundary_report([0,1,4],[1,1,1])
    assert full_report['positive_directions'] == 11
    assert negative_report['positive_directions'] == 0
    assert all(row['sign']=='negative' for row in negative_report['rows'])
    out = {'status':'passed','arithmetic':'exact fractions only',
           'scope':'Finite controls plus one exact ascent; general nonattainment uses the proof.',
           'complete_boundary_reports':[full_report,negative_report],
           'new_output_mass_cases':cases,'AP_endpoint_identity_cases':endpoint_cases,
           'heavy_endpoint_cases':heavy_cases,
           'finite_candidate_negative_control':{'support':sidon,'new_atom_candidates':candidates,'status':'passed'},
           'concrete_ascent':{'epsilon':'1/1000000','before':old_result,'after':extension_result}}
    path = Path(__file__).with_name('BOUNDARY-CHECKS.json')
    path.write_text(json.dumps(out,indent=2)+'\n')
    print('Passed',cases,'new-output mass checks,',endpoint_cases,'endpoint identities,',heavy_cases,'heavy-endpoint cases.')
    print('Concrete ascent:',old_result['ratio']['lower'],'->',extension_result['ratio']['lower'])
    print('Wrote',path.name)

if __name__ == '__main__':
    main()
