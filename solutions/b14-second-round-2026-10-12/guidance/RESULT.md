# P1/P6: a controlled elimination-policy comparison

12 October 2026. The bounded first deliverables are complete. There is no
measured practically meaningful advantage for the learned policy in this
comparison. This experiment does not identify a universally best elimination
method or establish a scalable solver improvement.

All four policies choose which rooted integer-potential 1-tree trajectory
to advance inside the same certified elimination and exact subset-DP solver.
The ordinary policy rotates among four roots, random chooses a root using
retained seeds, and the manual score favors remaining bound gap relative
to gradient norm and iterations. A ridge regression predicts the next
normalized bound improvement from current gap, gradient norm, iteration
and last improvement. Learned selection has periodic ordinary exploration.
All policies initialize each root before selecting further work.

Training used four Euclidean instances at sizes 8 and 10, seeds 0 and 1,
and 192 transition examples. It took 0.026798 seconds, including incumbent
generation, example generation and fitting. Tests used seeds 2 and 3,
held out the entire clustered Euclidean, random shortest-path and tree
metric families, and included size 12, absent from training. Twenty test
instances with two repetitions give 40 queries per policy. Execution order
rotates to reduce simple order effects. There is no validation-set tuning
or claim of statistical significance from two repetitions.

Each query allocates 50 milliseconds to elimination and guidance. Learned
queries debit total training time divided by 40, so their aggregate charge
includes all training exactly once; inference executes inside the clock.
The final started snapshot can overrun. Recorded maximum overruns range
from 0.168 to 1.206 milliseconds. These are common nominal time budgets
with disclosed granularity, not perfectly identical actual wall times.
Timing uses Python perf_counter on the same Linux container; it is a
single-machine measurement with scheduling and noise limits.

| Policy | Mean residual edges | Mean width upper bound | Total residual DP transitions | Total time to checked exact answer |
|---|---:|---:|---:|---:|
| Ordinary | 23.150 | 4.6 | 271630 | 2.391272 s |
| Random | 23.150 | 4.6 | 271636 | 2.392747 s |
| Manual | 23.100 | 4.6 | 271602 | 2.387643 s |
| Learned | 23.125 | 4.6 | 271616 | 2.388295 s |

The learned policy is slightly slower than the manual score and retains slightly more edges in this corrected run. Millisecond-scale aggregate differences do not support a robust speed claim. A negative comparison still completes the stated first deliverable; the [five broader attempts](P6-ATTEMPTS.md) record the additional models and their outcomes.

## Certification and residual structure

Strict forced-edge bounds L_e>U alone justify deletions. Each retained
packet is checked by the separate Kruskal-based original-cost verifier.
The outer query timer includes root/state setup, certificate packet construction, verification, exact solving and the residual-structure measurements before that timer closes; training is added as its explicit debit. A separate sum of timed stages is retained for diagnosis. Earlier receipts named STAGE-TIMING exclude setup and packet-construction overhead and are historical controls, not the reported total proof time. Subsequent file serialization and the independent full-DP control campaign are outside the proof timer.

The exact fallback solves the certified residual graph; all 160 answers
match full complete-graph subset-DP controls. The experiment checked 2270
retained 1-tree certificates and 7728 forced-edge bounds. The heuristic
incumbent is feasible on every run, independently recosted; final gap is
zero. Pre-exact gaps, costs, degree distributions, minimum-fill width
upper bounds, verification times and exact-work counters are all retained.
Minimum-fill width is an upper bound, not the exact treewidth.

Ordinary-policy family totals show where elimination helps:

| Family | Runs | Mean residual edges | Mean width upper bound | Residual / full DP transitions |
|---|---:|---:|---:|---:|
| Clustered Euclidean | 12 | 10.500 | 2.167 | 260 / 267520 |
| Euclidean, held-out size 12 | 4 | 12.000 | 2.000 | 80 / 225280 |
| Random shortest-path | 12 | 16.333 | 3.500 | 3770 / 267520 |
| Tree metric | 12 | 46.333 | 9.000 | 267520 / 267520 |

Tree metrics reproduce the all-optima preservation obstruction. All four
policies use the same lower-bound family; the comparison addresses
allocation of these checks rather than comparing every local-exchange or
commercial solver method.

[experiment.py](experiment.py) generates the experiment and certificate
packets. [EXPERIMENT.json](EXPERIMENT.json) retains every measurement,
model weight, training/test identity and hardware/software context;
the certificates directory retains every original-cost packet.
Training cost is amortized over this batch; a single-query deployment
would instead charge it in full. No test optimum, future bound or
reference-DP work is used as a policy feature.
