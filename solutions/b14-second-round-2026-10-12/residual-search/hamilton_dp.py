"""Exact frontier Hamilton-cycle DP on a certified residual graph."""


def canonical(part):
    labels = {}
    return tuple(-1 if x == -1 else labels.setdefault(x,len(labels)) for x in part)


def solve(costs, edges, *, upper=None, compress=True, drop_saturated=False, edge_order=None):
    n = len(costs)
    edges = sorted(tuple(sorted(e)) for e in edges)
    if len(set(edges)) != len(edges):
        raise ValueError('duplicate edges')
    if edge_order is not None:
        ordered = [tuple(sorted(e)) for e in edge_order]
        if len(ordered) != len(edges) or set(ordered) != set(edges):
            raise ValueError('edge order must contain every edge once')
        edges = ordered
    first, last = {}, {}
    remaining = [0]*n
    for i,(u,v) in enumerate(edges):
        if not (0 <= u < v < n):
            raise ValueError('invalid edge')
        for w in (u,v):
            first.setdefault(w,i)
            last[w] = i
            remaining[w] += 1
    if len(first) != n or min(remaining) < 2:
        return None, None, {'states':0,'transitions':0,'max_frontier':0}
    # Key: degrees, component partition, completed-cycle flag, optional full history.
    states = {((),(),False,()):(0,())}
    previous = []
    totals, transitions, max_frontier = 1,0,0
    for i,(u,v) in enumerate(edges):
        active = sorted(set(previous)|{u,v})
        index = {w:j for j,w in enumerate(active)}
        old_index = {w:j for j,w in enumerate(previous)}
        keep = [w for w in active if last[w] > i]
        max_frontier = max(max_frontier,len(active))
        remaining[u] -= 1
        remaining[v] -= 1
        following = {}
        for (old_deg,old_part,finished,_), (value,chosen) in states.items():
            if finished:
                key = ((),(),True,() if compress else chosen)
                if key not in following or value < following[key][0]:
                    following[key] = value,chosen
                transitions += 1
                continue
            degree = [old_deg[old_index[w]] if w in old_index else 0 for w in active]
            part = [old_part[old_index[w]] if w in old_index else -1 for w in active]
            for take in (0,1):
                transitions += 1
                d,p = degree[:],part[:]
                candidate = value + (costs[u][v] if take else 0)
                if upper is not None and candidate > upper:
                    continue
                cycle = False
                if take:
                    a,b = index[u],index[v]
                    if d[a] == 2 or d[b] == 2:
                        continue
                    d[a] += 1
                    d[b] += 1
                    if p[a] == -1:
                        p[a] = max(p,default=-1)+1
                    if p[b] == -1:
                        p[b] = max(p,default=-1)+1
                    if p[a] == p[b]:
                        cycle = True
                    else:
                        source,dest = p[b],p[a]
                        p = [dest if x == source else x for x in p]
                if any(d[j]+remaining[w] < 2 for j,w in enumerate(active)):
                    continue
                new_chosen = chosen + ((u,v),) if take else chosen
                if cycle:
                    # A closed cycle has no free degree for future attachment.
                    if (any(first[w] > i for w in range(n)) or
                            any(x != 2 for x in d)):
                        continue
                    key = ((),(),True,() if compress else new_chosen)
                else:
                    if drop_saturated:
                        p = [x if d[j] == 1 else -1 for j,x in enumerate(p)]
                    forgotten = [w for w in active if w not in keep]
                    if any(d[index[w]] != 2 for w in forgotten):
                        continue
                    alive = {p[index[w]] for w in keep if p[index[w]] >= 0}
                    if any(x >= 0 and x not in alive for x in p):
                        continue
                    kd = tuple(d[index[w]] for w in keep)
                    kp = canonical([p[index[w]] for w in keep])
                    key = (kd,kp,False,() if compress else new_chosen)
                if key not in following or candidate < following[key][0]:
                    following[key] = candidate,new_chosen
        states, previous = following,keep
        totals += len(states)
        if not states:
            break
    completed = [(value,chosen) for (_,_,finished,_),(value,chosen) in states.items() if finished]
    work = {'states':totals,'transitions':transitions,'max_frontier':max_frontier}
    if not completed:
        return None,None,work
    best, chosen = min(completed)
    adjacency = [set() for _ in range(n)]
    for u,v in chosen:
        adjacency[u].add(v)
        adjacency[v].add(u)
    assert len(chosen) == n and all(len(a) == 2 for a in adjacency)
    tour, parent, current = [0],None,0
    while True:
        nxt = min(adjacency[current]-({parent} if parent is not None else set()))
        if nxt == 0:
            break
        tour.append(nxt)
        parent,current = current,nxt
    assert sorted(tour) == list(range(n))
    assert sum(costs[tour[i]][tour[(i+1)%n]] for i in range(n)) == best
    return best,tour,work
