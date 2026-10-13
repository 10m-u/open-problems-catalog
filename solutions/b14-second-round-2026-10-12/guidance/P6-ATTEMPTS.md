# P6: five learned guidance attempts without a retained advantage

12 October 2026. These pursue the broader ambition of reducing cost to a
certified answer on held-out families. They are actual trained policies
inside the same correct solver, rather than claims that learning is
impossible. Each is unsuccessful at establishing that ambition in the
declared comparison; count awaits independent review.

The [baseline protocol](RESULT.md), [baseline receipt](EXPERIMENT.json),
and [four-model extension](VARIATIONS.json) retain training, inference,
verification and exact solving. The corrected outer query timer includes
setup and certificate construction. Every result has a checked incumbent,
strict safe elimination and an exhaustive fallback. Training uses only
four Euclidean n8/n10 inputs; 20 test inputs hold out entire families and
size 12. Forty test queries per model amortize its complete training cost.
The common nominal elimination budget is 50 milliseconds; started-call
overruns are recorded. No policy can delete an edge from its learned score.

## A1: linear prediction of the next ordinary lower-bound gain

Ridge regression on gap, gradient norm, trajectory age and last improvement
predicts the next normalized scalar bound gain. It selects roots with
periodic exploration. The corrected run retains 23.125 edges on average,
versus 23.100 for the manual policy, with 271616 versus 271602 exact-DP
transitions and 2.388295 versus 2.387643 seconds aggregate checked-answer
time. Neither a practically meaningful nor a structural gain is established.
The scalar objective also need not rank forced deletion profiles.

## A2: predict newly certifiable deletions directly

Keep the linear estimator but train on each trajectory's newly eliminated
edge fraction, using cumulative strongest forced bounds. This targets P1's
actual deletion condition, bypassing the scalar-bound proxy. The model
retains 23.175 edges and uses 271662 transitions, with 2.410370 seconds
aggregate time. It does not beat the ordinary or manual controls. This is
a distinct learning objective, not another seed of A1.

## A3: predict downstream exact-solver work saved

Generate exact residual subset-DP transition labels on training trajectories
and train on the fraction of work removed. This directly targets the
certification pipeline rather than sparsity alone. Training increases to
0.198430 seconds, fully charged across queries. The model retains 23.200
edges and uses 271694 transitions, with aggregate time 2.393802 seconds.
The changed supervision does not establish an advantage. The expensive
labels are used only on training inputs, never test optima or future work.

## A4: use a local nonlinear estimator instead of linear extrapolation

Five-nearest-neighbor regression uses the bound-gain examples, to retain
nonlinear local patterns across trajectory features. Inference must scan
the 192 retained training examples. It leaves 30.850 edges, 440956 DP
transitions and 2.550829 seconds aggregate time. The recorded maximum
started-call overrun is 1.233 milliseconds. Inference overhead and poorer
allocation erase the hoped-for transfer. No larger neighbor search is
counted as an extra attempt.

## A5: learn quadratic interactions in the state features

Ridge regression augments the gap, gradient norm, age and last gain with
their pairwise quadratic products, to model interactions that A1 misses.
It leaves 23.600 edges, 272102 transitions and 2.390592 seconds aggregate
time. The small timing difference from ordinary is unsupported by stronger
repetition, while its deterministic work and residual counts are worse.
It does not establish a useful transfer advantage.

## What the failures mean

These five routes vary the prediction target or estimator, with the same
solver, training/test identities, safety obligations and budget. The
extension was designed after inspecting the baseline; it is an iterative
research comparison with no untouched final validation set. No test
labels enter fitting, and no hyperparameters were selected by a test
search. The model blocks run sequentially, so small timing effects are
especially inconclusive. No universal impossibility or statistical
significance claim is made.

All 320 current certificate packets pass independent original-cost checks
and all exact answers agree with reference optima. The old stage-timing
receipts remain archived for the timing correction and are not extra
attempts. Under the per-problem rule, stop P6 after five reviewed failures;
the broad ambition remains unresolved. Do not deploy any of these policies
on the basis of this evidence.

Final disposition: the [main-thread route review](../BROADER-ROUTE-REVIEW.md) accepts the five-failure count. This target is stopped for this run and remains mathematically unresolved.
