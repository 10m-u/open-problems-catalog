# B14 P2 — Exact search on the sparse generating graph

This provides a proved state-equivalence rule and a working exact solver when the input metric comes from a supplied graph on the city set. It avoids requiring the complete metric's residual graph to have low width. The equivalence with a connected spanning Eulerian multigraph is established graph-TSP mathematics; this is a reproduced and checked baseline, with no novelty claim. [Graph-TSP formulation, Takazawa](https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1826.pdf)

Let $G=(V,E)$ be connected, with $n\geq3$ cities and nonnegative rational edge weights $w$. All vertices are required cities. Its shortest-path metric defines a complete-graph TSP.

## Equivalent exact formulation

Expanding a metric tour into generating-graph shortest paths gives a connected spanning even-degree multigraph of the same cost. Conversely, an Euler walk of any connected spanning even-degree multigraph visits every city; shortcut repeated cities in its metric closure to obtain a tour of no greater cost. Therefore the two minimum costs are equal.

An optimum multigraph can use each generating edge zero, one or two times. If an edge has multiplicity at least three, reduce its multiplicity by two. Both endpoint parities remain unchanged, at least one copy remains, and connectivity is preserved. Nonnegative weights ensure that cost does not increase. Repeat as needed.

Thus the search assigns $q_e\in\{0,1,2\}$, minimizing $\sum_e w_eq_e$, subject to connectivity and positive even degree at every city. Degree two is unnecessary: this is a generating-graph walk formulation, not a Hamiltonian-cycle formulation on that graph.

## The state-equivalence rule

Fix an edge-processing order. A frontier vertex has already appeared and is still incident to an unprocessed edge. Temporarily include the next edge's endpoints while processing it.

A prefix state records:

- whether each frontier vertex is still uncovered, covered with odd degree, or covered with even degree;
- the partition of covered frontier vertices into connected components of selected prefix edges.

Reject a prefix if a forgotten vertex is uncovered or has odd degree. Reject a selected component that loses all frontier vertices before the last edge is processed. At the end require one completed component.

**Lemma.** Two accepted prefixes with the same frontier coverage/parity states and component partition have exactly the same feasible suffix assignments.

Every forgotten vertex has no remaining incident edge, so its feasibility is already decided. Every future degree constraint depends only on present parity and whether a currently degree-zero city eventually receives an edge. Future selected edges merge components according to the same boundary partition. A closed component cannot reconnect later, which is why early disappearance is rejected. The exact positive degree of a covered boundary vertex imposes no additional restriction. These facts determine both parity and eventual connectivity for every common suffix.

Suffix cost is independent of the prefix. Therefore retain only the cheapest representative of each such state. This is a proved dominance rule that compresses full positive degrees to parity while preserving coverage and connectivity.

If a processing bag has at most $b$ vertices, an upper bound on the number of states is $3^b B_b$, where $B_b$ is the Bell number. The abstract dynamic programme takes $O(|E|3^b B_b\operatorname{poly}(b))$ arithmetic operations. Bit complexity depends on weight encoding. This is a frontier/path-decomposition parameter, not the treewidth of the complete metric.

The small readable implementation retains each representative's entire winning multiplicity prefix; copying those prefixes adds an extra factor in $|E|$. A predecessor-table implementation can recover the abstract storage and update bounds. No large-size performance claim relies on the present code.

## Implementation and checks

[euler_dp.py](euler_dp.py) implements the compressed DP and a comparison mode retaining exact degrees. It reconstructs an Eulerian multigraph, checks its feasibility independently, then uses Hierholzer and first-visit shortcutting to return a metric tour.

[check_dp.py](check_dp.py) compares both modes against the previous round's independent subset DP on the full metric closure. Forty weighted path, star, cycle, ladder and triangle-chain instances at $n=6,8,10,12$ agree in optimum, feasible multigraph cost and returned tour cost. Three additional four-vertex graphs, including zero weights, agree with exhaustive enumeration of all edge multiplicities and reversed processing order.

| Family | Compressed states | Full-degree states | Generating DP transitions | Metric subset-DP transitions |
|---|---:|---:|---:|---:|
| Paths | 72 | 72 | 192 | 134,080 |
| Stars | 72 | 72 | 192 | 134,080 |
| Cycles | 312 | 312 | 912 | 134,080 |
| Ladders | 412 | 592 | 1,212 | 134,080 |
| Triangle chains | 240 | 328 | 696 | 134,080 |

Each row sums eight instances. The largest processing bag has size three. These are distinct work counters, not equal-cost wall-time operations. The ladder and triangle rows demonstrate an actual reduction from the proved degree compression. Paths and stars also solve the first round's dense tree metrics through their generating graphs.

Full instances, edge orders, multiplicities and tours are in [DP-CHECK-RESULTS.json](DP-CHECK-RESULTS.json).

## Scope

This completes a concrete P2 baseline deliverable: an explicit state rule, a proof, an implementation and an independent optimum comparison. It is partial progress toward the broader search and compression investigation. It establishes no new worst-case parameter dependence, output-sensitive certificate discovery, or polynomial-time solution for arbitrary TSP. An arbitrary sparse graph can have a large frontier.

The input must supply a connected generating graph, with all its vertices required. A complete matrix does not itself supply a compact graph representation. Unrequired Steiner vertices need modified coverage conditions and are outside this implementation.

## Reproduce

From the repository root:

    python3 solutions/b14-second-round-2026-10-12/generating-graph/check_dp.py
