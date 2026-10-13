# P1: five unsuccessful broader elimination routes

12 October 2026. P1's equal-budget baseline is complete, but the user
asked for its broader ambition. These are specified routes toward a
generally beneficial certified-elimination solver, not assertions that
every possible method fails. Count is subject to independent review.

## A1: uniqueness makes forced-1-tree elimination uniformly sparse

The [unique-optimum necklace theorem](RESULT.md), independently reviewed,
refutes this route even with all roots and real potentials available.
For n=10k, k>=17, every forced lower bound lies below the unique optimum,
and hence below every incumbent. No edge can be eliminated.
This was the first continuation P1 failure recorded in CONTROL.md.

## A2: preserve every optimum and bound the residual width

The [first-round tree-metric theorem](../../b14-first-round-2026-10-12/elimination/RESULT.md)
already blocks this route: every complete metric edge occurs in an optimum
of cost twice the generating-tree weight. Any method preserving all optima
retains K_n and width n-1. This earlier failed universal-width route is
included in P1's full-target sequence, rather than counted again for each
tree example. It differs from A1: tied-optimum feasibility versus a
relaxation gap below a unique optimum. Preserving a chosen optimum or
working on the generating tree remains possible.

## A3: maximize the ordinary bound to select the best elimination check

Try to allocate checks by the scalar unforced 1-tree bound, assuming
that a stronger scalar bound dominates the forced-edge deletion profile.
The independently checked clustered Euclidean n10, seed0, four-root packet
has two retained snapshots:

| Snapshot index | Global bound numerator, scale 16 | Deleted edges against U=1494 |
|---|---:|---:|
| 5 | 22966 | 7 |
| 3 | 22652 | 8 |

Thus even the higher unforced bound can remove fewer edges. The proposed
dominance lemma is false; a ranking may still be useful empirically.
This is not a second run of the universal density obstruction. It concerns
how to spend a finite check budget on heterogeneous forced profiles.

## A4: switch residual exact search to the frontier solver for a general work gain

The [integrated residual experiment](../residual-search/RESULT.md) verifies
both solvers, but the exact frontier transition totals exceed subset DP
on all four tested n8 families: clustered 7671 versus 2673, Euclidean
101 versus 88, random metric 2512 versus 1222, and tree metric 19268
versus 5376. These are the full-partition baseline counters, not a claim
that endpoint compression never helps. The verified quotient subsequently
reduces states, even exponentially on one family, without supplying
uniform superiority over subset DP.

The attempt to infer an end-to-end gain merely from using an edge-frontier
solver after elimination is unsuccessful. A better order, width-adaptive
solver selection or alternative implementation remains possible.

## A5: amortize a fixed elimination budget on every metric query

Try the stronger operational claim that a fixed positive elimination
budget before the same exact fallback always reduces total proof work.
The held-out tree metrics retain every edge under every tested policy.
Their residual and full subset-DP work are identical. The positive
50-millisecond elimination cost and original-cost verification therefore
add work while giving this fallback no reduction. This is an operational
failure distinct from A2's structural width claim: it includes the actual
production/checking/fallback pipeline and matched-budget comparison.
An adaptive bypass based on recognizing a tree generating graph would
avoid the overhead; that is an additional solver decision, not this
fixed-budget algorithm.

## Disposition and retained evidence

These five failed sufficient routes do not close P1 by proving a universal
impossibility. They exhaust the user's per-problem attempt allowance if
accepted by review. The positive certificates, useful reductions on the
geometric and random families, and P2's representation theorem remain.
The question of the best combination per unit computation remains
unresolved beyond the bounded comparison.

[check_p1_routes.py](check_p1_routes.py) rechecks A3's original-cost
snapshots and the A4/A5 receipt counters; A1/A2 have existing proof reviews.

Final disposition: the [main-thread route review](../BROADER-ROUTE-REVIEW.md) accepts the five-failure count. This target is stopped for this run and remains mathematically unresolved.
