#!/usr/bin/env python3
"""Original-cost and protocol audit of the four additional learned policies."""
from pathlib import Path
import json
import math
import sys

HERE = Path(__file__).resolve().parent
FIRST = HERE.parent.parent/'b14-first-round-2026-10-12'/'elimination'
sys.path.insert(0,str(FIRST))
from check_certificate import verify


def main():
    baseline = json.loads((HERE/'EXPERIMENT.json').read_text())
    extension = json.loads((HERE/'VARIATIONS.json').read_text())
    assert extension['training_instances']==baseline['training_instances']
    assert extension['testing_instances']==baseline['test_instances']
    assert not set(extension['training_instances'])&set(extension['testing_instances'])
    assert len(extension['rows'])==160
    baseline_identities = {(r['instance'],r['repeat']) for r in baseline['rows']}
    snapshots,bounds = 0,0
    for mode,data in extension['models'].items():
        rows = [r for r in extension['rows'] if r['policy']=='learned-'+mode]
        assert len(rows)==40 and {(r['instance'],r['repeat']) for r in rows}==baseline_identities
        assert math.isclose(sum(r['training_debit_seconds'] for r in rows),data['training_seconds'])
        assert all(r['budget_seconds']==baseline['budget_seconds'] for r in rows)
        for row in rows:
            packet = json.loads((HERE/'certificates'/f"{row['instance']}-{row['policy']}-r{row['repeat']}.json").read_text())
            assert packet['measurements']==row
            audit = verify(packet)
            assert audit==row['independent_bound_audit']
            c=packet['instance']['costs'];n=len(c);tour=row['certified_tour']
            assert sorted(tour)==list(range(n))
            assert sum(c[tour[i]][tour[(i+1)%n]] for i in range(n))==row['optimal_cost']
            assert row['optimal_cost']==baseline['full_dp_controls'][row['instance']]['optimum']
            assert math.isclose(row['total_proof_seconds'],
                                row['query_wall_seconds']+row['training_debit_seconds'])
            assert row['query_wall_seconds']+row['training_debit_seconds']>=row['summed_timed_stages_seconds']
            assert math.isclose(row['overrun_seconds'],max(0,
                row['elimination_and_inference_seconds']+row['training_debit_seconds']-row['budget_seconds']))
            assert row['post_exact_gap']==0
            snapshots+=audit['certificates_checked'];bounds+=audit['forced_bounds_checked']
    result={'status':'passed','additional_packets':160,'additional_certificates':snapshots,
            'additional_forced_bounds':bounds,'matched_queries_per_policy':40,
            'scope':'certification/protocol checks, not wall-time replication or learning impossibility'}
    (HERE/'VARIATION-AUDIT.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
