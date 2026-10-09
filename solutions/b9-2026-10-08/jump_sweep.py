#!/usr/bin/env python3
"""Problem 4 sweeps (see PREREGISTRATION.md). Usage: jump_sweep.py TASK [args]

TASK atlas NMAX          all connected graphs 3..NMAX vertices, all e, all count vectors, both utilities
TASK trees NMIN NMAX     all trees, all e, all count vectors, diversity utility (spiders flagged)
TASK regular D N UTIL E  all connected D-regular graphs on N vertices, E empties, all count vectors
Each instance records IRC / sink / weak-acyclicity; certificates are kept for every IRC, no-sink and
non-weakly-acyclic instance. Output: jump_<task>_<args>.json
"""
import json
import sys
import time
from multiprocessing import Pool
import os
from math import factorial
import networkx as nx
from jump_games import analyse, partitions
from graph_families import atlas_connected, trees, is_spider, regular, nbrs_of


CAP = int(os.environ.get('JUMP_STATE_CAP', '0'))   # 0 = no cap; capped instances are counted, not run


def n_states(N, counts):
    d = factorial(N - sum(counts))
    for c in counts:
        d *= factorial(c)
    return factorial(N) // d


def job(args):
    gid, nb, counts, util, tags = args
    if CAP and n_states(len(nb), counts) > CAP:
        return {'gid': gid, 'N': len(nb), 'e': len(nb) - sum(counts), 'counts': counts, 'util': util,
                'tags': tags, 'skipped': True, 'cycle': None, 'trapped_state': None, 'sinks': None}
    r = analyse(nb, counts, util)
    keep = r['irc'] or r['sinks'] == 0 or not r['weakly_acyclic']
    return {'gid': gid, 'N': len(nb), 'e': len(nb) - sum(counts), 'counts': counts, 'util': util, 'tags': tags,
            'states': r['states'], 'irc': r['irc'], 'sinks': r['sinks'], 'weakly_acyclic': r['weakly_acyclic'],
            'cycle': r.get('cycle') if keep else None, 'trapped_state': r.get('trapped_state'),
            'edges': [(u, v) for u in range(len(nb)) for v in nb[u] if u < v] if keep else None}


def instances(task, argv):
    if task == 'atlas':
        for gi, G in enumerate(atlas_connected(3, int(argv[0]))):
            nb = nbrs_of(G)
            N = len(nb)
            reg = len({len(x) for x in nb}) == 1
            for e in range(1, N - 1):
                for counts in partitions(N - e):
                    for util in ('variety', 'diversity'):
                        yield (gi, nb, counts, util, {'regular': reg, 'tree': nx.is_tree(G)})
    elif task == 'trees':
        for N in range(int(argv[0]), int(argv[1]) + 1):
            for gi, T in enumerate(trees(N)):
                nb = nbrs_of(T)
                for e in range(1, N - 1):
                    for counts in partitions(N - e):
                        yield (f'{N}:{gi}', nb, counts, 'diversity', {'spider': is_spider(T)})
    elif task == 'regular':
        d, N, util, e = int(argv[0]), int(argv[1]), argv[2], int(argv[3])
        for gi, G in enumerate(regular(d, N)):
            nb = nbrs_of(G)
            for counts in partitions(N - e):
                yield (gi, nb, counts, util, {'regular': d})


def main():
    task, argv = sys.argv[1], sys.argv[2:]
    t0 = time.time()
    insts = list(instances(task, argv))
    with Pool(3) as pool:
        res = pool.map(job, insts, chunksize=8)
    summary = {}
    for r in res:
        key = f"{r['util']}|e={r['e']}"
        s = summary.setdefault(key, {'instances': 0, 'irc': 0, 'no_sink': 0, 'not_weakly_acyclic': 0,
                                     'skipped_over_cap': 0, 'irc_spider': 0})
        if r.get('skipped'):
            s['skipped_over_cap'] += 1
            continue
        s['instances'] += 1
        s['irc'] += r['irc']
        s['no_sink'] += r['sinks'] == 0
        s['not_weakly_acyclic'] += not r['weakly_acyclic']
        s['irc_spider'] += bool(r['irc'] and r['tags'].get('spider'))
    out = {'task': task, 'args': argv, 'state_cap': CAP, 'seconds': round(time.time() - t0, 1), 'instances': len(res),
           'summary': summary, 'flagged': [r for r in res if r['cycle'] or r['trapped_state'] or r['sinks'] == 0]}
    if CAP:
        name_suffix = f'_cap{CAP}'
    else:
        name_suffix = ''
    name = f"jump_{task}_{'_'.join(argv)}{name_suffix}.json"
    with open(name, 'w') as fh:
        json.dump(out, fh)
    print(json.dumps({k: v for k, v in out.items() if k != 'flagged'}, indent=1))
    print('flagged instances:', len(out['flagged']), '->', name)


if __name__ == '__main__':
    main()
