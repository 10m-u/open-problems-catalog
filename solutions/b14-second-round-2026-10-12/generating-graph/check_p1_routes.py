#!/usr/bin/env python3
"""Independently verify the P1 allocation and exact-work route witnesses."""
from pathlib import Path
import json
import sys

HERE = Path(__file__).resolve().parent
FIRST = HERE.parent.parent/'b14-first-round-2026-10-12'/'elimination'
sys.path.insert(0,str(FIRST))
from one_tree import snapshot
from check_certificate import verify


def main():
    p = FIRST/'certificates/clustered-euclidean-ceil-n10-s0-four-roots.json'
    data = json.loads(p.read_text()); audit = verify(data)
    values = {}
    for idx in (3,5):
        cert = data['certificates'][idx]
        row,bounds,_ = snapshot(data['instance']['costs'],cert['root'],cert['potentials'],cert['scale'])
        values[idx] = (row['bound_numerator'],
                       sum(v>16*data['incumbent']['cost'] for v in bounds.values()))
    assert values=={3:(22652,8),5:(22966,7)}
    residual = json.loads((HERE.parent/'residual-search/CHECK-RESULTS.json').read_text())
    grouped = {}
    for row in residual['rows']:
        if row['kind']!='certified_residual': continue
        family = row['instance'].split('-n8')[0]
        before,after = grouped.get(family,(0,0))
        grouped[family] = (before+row['frontier']['transitions'],after+row['subset_dp']['transitions'])
    assert all(a>b for a,b in grouped.values())
    guidance = json.loads((HERE.parent/'guidance/EXPERIMENT.json').read_text())
    trees = [r for r in guidance['rows'] if r['family']=='tree-metric']
    assert len(trees)==48
    for row in trees:
        assert row['residual_edges']==row['n']*(row['n']-1)//2
        assert row['residual_dp']==guidance['full_dp_controls'][row['instance']]['work']
        assert row['verification_seconds']>0 and row['elimination_and_inference_seconds']>0
    result = {'status':'passed','allocation_witness':values,'original_cost_audit':audit,
              'frontier_vs_subset_transitions':grouped,'unchanged_tree_fallback_runs':len(trees),
              'scope':'specified failed sufficient routes, no universal elimination impossibility'}
    (HERE/'P1-ROUTE-CHECK-RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__': main()
