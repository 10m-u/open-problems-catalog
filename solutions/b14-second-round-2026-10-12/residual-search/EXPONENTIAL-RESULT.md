# P2: an exponential, realizable reduction after certified elimination

12 October 2026. The endpoint-state equivalence in [RESULT.md](RESULT.md)
can collapse exponentially many realizable boundary partitions, not just
improve the finite control set by a few percent. This establishes the
broader existential state-reduction ambition of P2, including P1 integration.
It gives no universal polynomial algorithm or performance dominance.

For each t>=1 let n=t+6. Name endpoint pairs (0,1), (2,3), (4,5) and
interior vertices Z={6,...,n-1}. The prefix graph contains the three
pair edges, all edges within Z, and all edges from Z to 2,3,4,5.
The suffix graph contains 1--2, 3--4, 5--0 and all edges 0--z.
Process every prefix edge before every suffix edge.

For every assignment of each z to one of pairs (2,3) and (4,5), insert
the assigned vertices, in increasing order, into that pair's path.
Keep 0--1 as a third path. These are 2^t different partial path forests,
all with the same boundary degree vector: the six endpoints have degree
one and Z has degree two. Every vertex is still on the boundary:
endpoints have later connecting edges, and each z has its later 0--z edge.

The full component partition identifies to which of the two paths each
z belongs, so its 2^t keys are distinct. Endpoint compression drops
those saturated labels and retains only the three endpoint pairs; all
2^t forests become one key. Their prefix costs are t+3 if edges cost one.
Every forest completes to a Hamiltonian cycle using the same three
connecting suffix edges. Since each z is already saturated, the remaining
suffix edges 0--z are unusable. All suffix feasibility and relative costs
are identical by the state-equivalence proof, including the zero-choice
constraints on those edges.

## An actual P1 residual

Make complete-graph costs one on the prefix/suffix union H and two
elsewhere. This is a metric. The constructed tours have cost n, matching
the degree lower bound. At any root, H with that root removed is connected,
because a Hamiltonian cycle is present. Every H edge not incident to
the root therefore extends to a unit-cost spanning tree on nonroot
vertices; any H root edge extends to two unit-cost root spokes. Hence
every forced zero-potential 1-tree bound for an H edge equals n.

A forced non-H edge has cost two among n edges whose other costs are
at least one, so its forced bound is at least n+1. Strict elimination
against the known incumbent n consequently leaves **exactly H**.
Thus the exponential quotient occurs on a certified residual of the
original metric instance, rather than an abstract set of invalid states.

This is a factor 2^(n-6) within the displayed boundary class. It is a
lower bound on the number of full-partition representatives identified
by the quotient, not a factor guaranteed for total runtime or for all
reachable states. Z is saturated within a selected prefix, but each of
its vertices has residual-graph degree t+4; static degree-two graph
preprocessing does not remove it. A solver could instead suppress
selected degree-two vertices within each prefix state. The claimed
reduction compares precisely the stated full-partition representation
with endpoint compression. H has Theta(n^2) edges and the exhibited
frontier has size n; this is not a sparse or bounded-width residual family.

[check_exponential.py](check_exponential.py) checks t=1,...,5, independently
recomputes every forced bound with Kruskal, constructs every displayed
forest, and compares both ordered DPs with subset-DP optima.
[EXPONENTIAL-CHECK-RESULTS.json](EXPONENTIAL-CHECK-RESULTS.json) retains
the state and work counters. The DP now accepts a checked explicit edge
order; its default order and its earlier correctness controls are retained.
