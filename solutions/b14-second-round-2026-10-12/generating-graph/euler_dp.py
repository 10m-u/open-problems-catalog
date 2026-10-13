"""Exact graphical TSP using covered/parity/connectivity frontier states."""
from collections import defaultdict


def canonical(labels):
    rename = {}
    out = []
    for value in labels:
        if value < 0:
            out.append(-1)
        else:
            if value not in rename:
                rename[value] = len(rename)
            out.append(rename[value])
    return tuple(out)


def solve(n, edges, compress=True):
    """Edges are (u,v,nonnegative integer weight), in a declared processing order."""
    assert n >= 3 and edges
    assert all(0 <= u < v < n and w >= 0 for u, v, w in edges)
    assert len({(u, v) for u, v, _ in edges}) == len(edges)
    last = {v: i for i, e in enumerate(edges) for v in e[:2]}
    assert set(last) == set(range(n))
    states = {((), ()): (0, ())}
    frontier = []
    total_states, transitions, max_states, max_width = 1, 0, 1, 0
    for i, (a, b, weight) in enumerate(edges):
        introduced = [v for v in (a, b) if v not in frontier]
        current = frontier + introduced
        positions = {v: j for j, v in enumerate(current)}
        pa, pb = positions[a], positions[b]
        forget = [j for j, v in enumerate(current) if last[v] == i]
        retain = [j for j, v in enumerate(current) if last[v] > i]
        next_states = {}
        max_width = max(max_width, len(current))
        for (old_degrees, old_labels), (cost, choices) in states.items():
            for multiplicity in (0, 1, 2):
                transitions += 1
                degrees = list(old_degrees) + [0] * len(introduced)
                labels = list(old_labels) + [-1] * len(introduced)
                if multiplicity:
                    for j in (pa, pb):
                        if compress:
                            degrees[j] = (multiplicity if degrees[j] == 0 else
                                          degrees[j] if multiplicity == 2 else 3 - degrees[j])
                        else:
                            degrees[j] += multiplicity
                        if labels[j] < 0:
                            labels[j] = max(labels, default=-1) + 1
                    old, new = labels[pb], labels[pa]
                    labels = [new if label == old else label for label in labels]
                if any(degrees[j] == 0 or degrees[j] % 2 for j in forget):
                    continue
                remaining = {labels[j] for j in retain if labels[j] >= 0}
                closed = {label for label in labels if label >= 0} - remaining
                if closed and (i != len(edges) - 1 or len(closed) != 1):
                    continue
                key = (tuple(degrees[j] for j in retain),
                       canonical(labels[j] for j in retain))
                value = cost + multiplicity * weight
                if key not in next_states or value < next_states[key][0]:
                    next_states[key] = value, choices + (multiplicity,)
        states = next_states
        frontier = [current[j] for j in retain]
        total_states += len(states)
        max_states = max(max_states, len(states))
    assert ((), ()) in states
    optimum, multiplicities = states[(), ()]
    return {'optimum': optimum, 'multiplicities': list(multiplicities),
            'states': total_states, 'transitions': transitions,
            'max_layer_states': max_states, 'max_frontier': max_width,
            'state_mode': 'covered-parity-partition' if compress else 'degree-partition'}


def check_walk(n, edges, multiplicities):
    """Independent feasibility and cost check for the returned multigraph."""
    assert len(edges) == len(multiplicities)
    adjacency = defaultdict(list)
    for (a, b, _), q in zip(edges, multiplicities):
        assert q in (0, 1, 2)
        if q:
            adjacency[a].append(b)
            adjacency[b].append(a)
    degree = [sum(q for (a, b, _), q in zip(edges, multiplicities) if v in (a, b))
              for v in range(n)]
    assert all(d > 0 and d % 2 == 0 for d in degree)
    seen, stack = {0}, [0]
    while stack:
        for v in adjacency[stack.pop()]:
            if v not in seen:
                seen.add(v)
                stack.append(v)
    assert len(seen) == n
    return sum(w * q for (_, _, w), q in zip(edges, multiplicities))


def shortcut(n, edges, multiplicities):
    """Hierholzer followed by first-visit shortcutting in the metric closure."""
    adjacency = defaultdict(list)
    used = set()
    token = 0
    for (a, b, _), q in zip(edges, multiplicities):
        for _ in range(q):
            adjacency[a].append((b, token))
            adjacency[b].append((a, token))
            token += 1
    stack, circuit = [0], []
    while stack:
        v = stack[-1]
        while adjacency[v] and adjacency[v][-1][1] in used:
            adjacency[v].pop()
        if adjacency[v]:
            w, index = adjacency[v].pop()
            used.add(index)
            stack.append(w)
        else:
            circuit.append(stack.pop())
    assert len(used) == token
    tour, seen = [], set()
    for v in reversed(circuit):
        if v not in seen:
            seen.add(v)
            tour.append(v)
    assert len(tour) == n
    return tour
