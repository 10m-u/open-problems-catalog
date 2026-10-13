#!/usr/bin/env python3
"""Register reviewed B2 packets without counting partials as full solutions."""
from collections import Counter
from pathlib import Path
import json
import re

HERE = Path(__file__).resolve().parent


def main():
    status = json.loads((HERE / 'STATUS.json').read_text())
    root_packets = {}
    for file in sorted(HERE.rglob('*ATTEMPTS.md')):
        if 'paley' in file.relative_to(HERE).parts:
            continue
        for q in re.findall(r'<a id="(q\d+)-a[1-5]"', file.read_text()):
            root_packets[q.upper()] = str(file.relative_to(HERE))
    accepted_agent = {'Q2187', 'Q2188', 'Q2189', 'Q2190', 'Q2191',
                      'Q1959', 'Q1960', 'Q1961', 'Q1860', 'Q1861'}
    agent_status = json.loads((HERE / 'paley/STATUS.json').read_text())
    agent_targets = {t['target']: t for t in agent_status['targets']}
    for target in status['targets']:
        q = target['target']
        if q in root_packets:
            file = root_packets[q]
            prior = {a['attempt']:a for a in target['attempts']}
            target['attempts'] = [
                {**prior.get(n, {}), 'id': f'{q}-A{n}', 'attempt': n,
                 'outcome': 'full_target_failure',
                 'evidence': f'{file}#{q.lower()}-a{n}'} for n in range(1, 6)]
            target['evidence'] = [file]
        if q in root_packets or (target['attempts'] and q not in agent_targets
                                 and q.startswith('Q')):
            assert len(target['attempts']) == 5, q
            target['owner'] = '/root'
            target['status'] = 'failure_limit'
            target['consecutive_failures'] = 5
            target['review'] = 'ROOT-REVIEW.md#root-routes'
            for n, attempt in enumerate(target['attempts'], 1):
                attempt.update(id=f'{q}-A{n}', attempt=n, root_review_accepted=True)
        elif q in accepted_agent:
            supplied = agent_targets[q]
            assert len(supplied['attempts']) == 5, q
            target['attempts'] = [dict(a, id=f'{q}-A{n}', root_review_accepted=True)
                                  for n, a in enumerate(supplied['attempts'], 1)]
            target['evidence'] = supplied['evidence']
            target['owner'] = '/root/b14_local_optima'
            target['status'] = 'failure_limit'
            target['consecutive_failures'] = 5
            target['review'] = ('ROOT-REVIEW.md#colouring' if q in {'Q1860','Q1861'}
                                else 'ROOT-REVIEW.md#cubes' if q in {'Q1959','Q1960','Q1961'}
                                else 'ROOT-REVIEW.md#paley')
        elif q == 'A-TRANSFER':
            assert target['status'] == 'solved_locally'
            target['owner'] = '/root/b14_local_optima'
            target['review'] = 'ROOT-REVIEW.md#transfer'
        else:
            target['owner'] = '/root/b14_local_optima'
    counts = Counter(t['status'] for t in status['targets'])
    status['counts'] = dict(counts)
    # A replay must not reopen a completed, separately validated filing.
    if status.get('overall_state') != 'complete_under_stopping_rule':
        status['overall_state'] = 'research_and_review_in_progress'
    status['ownership_counts'] = dict(Counter(t['owner'] for t in status['targets']
                                              if t['target'].startswith('Q')))
    assert status['ownership_counts'] == {'/root': 71, '/root/b14_local_optima': 10}
    (HERE / 'STATUS.json').write_text(json.dumps(status, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'counts': dict(counts), 'ownership': status['ownership_counts']}))


if __name__ == '__main__':
    main()
