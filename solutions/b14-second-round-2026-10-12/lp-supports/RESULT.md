# P4: exact gaps and rounding for one-spoke Petersen subdivisions

12 October 2026. This is a named, restricted support family, with a direct
certificate and a constructive all-size lemma. It completes P4's first
deliverable, not the unrestricted 4/3 conjecture. Originality is not claimed.

Let H_l replace spoke u_0 v_0 of the Petersen graph G(5,2) by a path of l>=1
unit edges, with all new vertices treated as cities. Thus n=l+9. Use the
shortest-path metric of the unweighted support graph. Give the ten edges in
its two pentagons weight x_e=1/2, and every other support edge weight x_e=1;
give all other complete-graph edges x_e=0.

**Theorem.** This x is a half-integral extreme subtour-LP point. Its metric
instance has LP=n and OPT=n+1 for every l>=1.

Degree sums are two. For l=1, all 1022 proper Petersen cuts have capacity at
least two, as checked exhaustively in the earlier obstruction certificate.
This finite fact is the base of the proof, rather than an unverified appeal
to connectivity. Subdividing a unit-x edge preserves that inequality: when
its endpoints lie on different sides, the replacement path contributes at
least one; when they are on the same side but a cut separates internal
vertices, it contributes at least two. A cut with a nontrivial restriction
to the original vertices also inherits their cut capacity. These cases
include cuts containing no original vertex and their complements.

To prove extremality, fix zero coordinates at their lower bounds and
unit coordinates at their upper bounds. The remaining variables are the
edges of the two odd pentagons. The degree equations uniquely fix them to
one half: successive equations alternate the value, and closure of an odd
cycle forces twice that value to equal one. These active constraints fix
every coordinate, so x is a vertex. This argument also covers every new
degree-two vertex and its unit path edges.

Every distance between different cities is at least one. Consequently
one-half of every degree equation, summed, gives the dual lower bound n.
The displayed x has cost n, proving LP=n exactly.

A tour of cost n would use only support edges. Every inserted vertex has
degree two in H_l, so such a Hamiltonian cycle would contract to a
Hamiltonian Petersen cycle containing the original spoke. The earlier
181440-tour exact enumeration excludes all Petersen Hamiltonian cycles.
Integer distances therefore give OPT>=n+1.

The checker supplies a Petersen Hamiltonian path containing the chosen
spoke, whose endpoints have a two-edge connecting path avoiding that spoke.
Replace the spoke within the Hamiltonian path by the subdivided path.
It remains Hamiltonian, costs n-1, and closes at distance two. This proves
the upper bound n+1 constructively for all l. The certificate records the
original path and the two-hop midpoint, so extending it needs no new search.

## A scoped rounding lemma

Suppose a metric on n cities has all nonzero distances at least a>0,
has a feasible subtour-LP point of cost na, and is supplied with a
Hamiltonian path whose n-1 edges each cost a. If its endpoints are at
distance at most beta*a, closing that path gives a tour of cost at most
(n-1+beta)*a, and ratio at most 1+(beta-1)/n relative to the LP.
These conclusions follow by summing the path costs and the degree-equation
lower bound na. The construction takes linear time given the path; this
lemma does not provide a Hamiltonian-path algorithm on an arbitrary support.
For H_l, beta=2 and the construction is optimal.

## Exact bounded controls and parity

[check.py](check.py) checks l=1,...,5 (n=10,...,14), all cuts up to
complement, degree feasibility, independent subset-DP optima and the
constructed tours. It retains a minimum spanning tree, its odd vertices,
an exact minimum perfect matching on those vertices, and the Euler
shortcut tour. [CHECK-RESULTS.json](CHECK-RESULTS.json) records original
cost matrices, fractional points, tight-cut counts and correction costs.
Degree-two subdivisions create additional tight cuts; the pentagons
remain the fractional part. The construction costs n+1 independently of
the odd set of a particular minimum spanning tree.

The gap (n+1)/n tends to one. These supports illustrate persistent
fractionality and Hamiltonicity obstruction, not asymptotically difficult
gap instances. Their exhibited metric gap is also distinct from the
maximum gap optimized over all metrics for the same fractional point.

The programme's [published enumeration paper](https://arxiv.org/html/2603.12995v5)
and [dataset landing link](https://doi.org/10.60507/FK2/JK95PC) were consulted;
the latter did not open through the web tool. No representative was
downloaded, and this family is generated independently, rather than
claimed to reproduce a particular dataset record.
