# Q3819 — Attempts on short improving clustering paths

The target asks for the existence of a polynomial-length improving path from every partition into nonempty clusters. A slow pivot rule does not disprove it. The stopping count belongs to Q3819 separately.

## Q3819-A1: an integer potential counting ordered inversions

**Proposed route.** Order clusters by their means and count pairs x>y with x in an earlier cluster than y. This integer is at most n(n-1)/2. Try to find an improving transfer lowering it whenever the state is not locally optimal; that would give a polynomial improving path.

**Exact obstruction.** Let

    A={-6,0,1/1000,2/1000,3/1000,4/1000}, B={8/5}.

The initial means are -599/600 and 8/5; the partition is contiguous and has zero inversions. For a transfer of x from a source of size p>1 and mean a to a destination of size q and mean b, recomputing means changes squared error by

$$
\Delta=\frac{q}{q+1}(x-b)^2-\frac{p}{p-1}(x-a)^2.
$$

The checker uses exact rational arithmetic for every permitted transfer. Only transferring -6 from A to B strictly improves. Afterwards A has mean 1/500 and B has mean -11/5. In centroid order, B is first but contains 8/5, greater than all five A points. The inversion count rises from zero to five. Every improving path is forced to take that first step.

Thus neither sorted partitions nor the nonnegativity of this inversion count guarantee local optimality; the desired decreasing-potential lemma is false. Transfers may improve even when the destination mean is farther from the transferred point, because removal and addition have different size factors.

**Outcome:** unsuccessful full-target attempt, streak 1. The catalog question is not refuted. There is a two-move improving path to a local optimum: after the forced transfer, move 8/5 into A. An exact breadth-first search and all 126 nonempty labeled two-cluster partitions verify this qualification.

**Evidence:** [checker](check_initial_routes.py), [receipt](INITIAL-ROUTE-CHECK-RESULTS.json), [independent review](../initialization/FINAL-ROUTE-REVIEW.md). [Primary source, concluding section](https://doi.org/10.4230/LIPIcs.STACS.2024.52). No new originality claim.
