# Q4665 full-target attempts

Five proposed distinct full-target failures, pending independent review.
The complete conjecture remains unresolved. Evidence is
[Q4665-RESULTS.md](Q4665-RESULTS.md), lr.py,
check_schur_routes.py and SCHUR-ROUTES-CHECK.json. Source old-range
computations, source reads and calibration replays count zero.

<a id="q4665-a1"></a>
## A1 — termwise midpoint domination followed by output fiber budgeting

Sum the proved pairwise Schur midpoint inequalities, then dominate each
summed output by its c(u)d(v) budget. The actual legal l1 support example
has two input weights sharing one unit output budget. CD minus the pushed
sum has a negative s_(1,1) coefficient, although the full target passes.
The route therefore fails at its required budget inference. Retained:
an all-size summed-fiber criterion, hence the exact conjecture for injective
midpoint support pairs and either singleton input support.

<a id="q4665-a2"></a>
## A2 — direct or relabeled use of the proved meet/join ADS theorem

The actual singleton0,2 example satisfies midpoint weights but violates
the ADS meet/join weight condition. A common injective relabeling cannot
conjugate midpoint operations to meet/join because two distinct input
labels can have coincident midpoint outputs. This worked closure/transport
contract fails. A lifted auxiliary-lattice theorem remains possible.

<a id="q4665-a3"></a>
## A3 — scalar KL evaluations followed by recovery of Schur signs

Derive the actual all-size nonnegative-alphabet evaluation inequality
using scalar KL and the established pairwise midpoint theorem. The final
certificate implication fails: formal s2-s11=sum x_i^2 passes even
monomial positivity but has a negative Schur coefficient. This formal
control is not a legal conjecture counterexample. A proof about the
special family of actual differences is still needed; evaluations
alone do not complete the full target.

<a id="q4665-a4"></a>
## A4 — scalar midpoint KL within each fixed-output LR fiber

Keep output nu fixed, use joint (lambda,mu,tableau) indices and try
coordinatewise uniform rounding. Actual row-output LR pairs(0,N) and
(1,N-1), every N>=2, round to total degrees N+1 and N-1. Both leave
the fixed-output domain, independently of interior coordinates. The
needed domain-closure hypothesis fails. Balanced rounding could be
a different route, but this direct coefficient lifting is invalid.

<a id="q4665-a5"></a>
## A5 — fresh nonunit weighted exact Schur counter-construction

Construct32 actual rational-weight instances with size>10 a-inputs and
length4 shapes, enforcing all midpoint inequalities through exact maximum
output ratios. Compute every Schur coefficient by literal LR tableaux.
All pass, so this bounded attempt supplies neither a counterexample nor
the all-size positivity proof. It is one new construction attempt beyond
the stated prior coverage, not a count per instance or a source replay.

## Pending stopping disposition

Five specified routes have failed at the full target; narrower support
and evaluation theorems are retained. Distinct obligations are summed
fiber budgets, ADS operation transport, a numerical-to-Schur inference,
fixed-output LR-domain closure, and an actual fresh weighted construction.
No sixth solving route is begun while honest review is pending.
