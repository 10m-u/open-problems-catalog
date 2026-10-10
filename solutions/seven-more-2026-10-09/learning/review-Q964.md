# Independent internal review of Q964

Date: 2026-10-09. Reviewer role: probability and finite-state verification.

## Outcome

No blocking mathematical defect was found in `Q964-proof.md`. Its policy and
analysis provide a proposed complete affirmative answer to the catalog's
known-`c/T`, fixed-`K,c` existence question: the worst-case expected regret to
the full informed sequence benchmark is
`O_(K,c)(T^(4/5) (log T)^(1/5))`.

This conclusion is an internal review of the written argument and executable
controls. It is not a formal proof certificate, external peer review, or a
publication-priority determination.

## Model and source check

The primary [version-5 source](https://arxiv.org/html/2307.11655v5), Section 2,
was opened independently during this review. It gives an initial state one,
unknown arm reward/end-state pairs in `[0,1]^2`, reward observation before the
state update, hidden state, known evolution rate, and an informed optimal
sequence comparator. These agree with the proof. In particular, the proof's
benchmark is not an external-regret benchmark against a fixed arm. The source
was checked on 2026-10-09.

## Review of the arguments most likely to fail

### Pathwise expansion and the calibration identity

Subtracting the first-order state expression from the exact recurrence gives
`e_(t+1)-e_t=lambda*(1-q_t)`. The bound
`0 <= 1-q_t <= lambda*t` therefore yields the claimed nonnegative second-order
remainder for every action history. This identity is exact, and its validity
does not depend on independent or predetermined arm choices.

For a probe `j^L i^L j^L`, comparing offset `k` in the two reference blocks
crosses `(L-k)` reference actions, `L` actions of arm `i`, and another `k`
reference actions. Thus it crosses exactly `L` of each arm, including when
`i=j`. For the adjacent reference-only calibration it crosses exactly `L`
reference actions. The two differences cancel the reference effect with the
claimed sign. The use of a global remainder bound `E` at all calibration and
probe times correctly accounts for the entire earlier exploration history.

### Adaptation and concentration

The reference arm depends on the pilot observations, but each later measured
block is selected using information available before the block. Conditional
on its past, every reward minus its conditional mean has mean zero and
conditional range length one. Conditional Hoeffding concentration therefore
applies with the exponent `-2*L*eta^2`. There are exactly `3K+2` measured block
averages: `K` pilots, two calibration blocks, and two reference blocks per
probe. The union bound is valid despite reuse of the common calibration
difference in every estimator; it does not require those estimators to be
independent.

The argument bounds empirical averages against averages of their time-varying
conditional means. It does not incorrectly regard rewards from a block as
identically distributed.

### Small rewards and identifiability

An unweighted bound on every end-state estimate would fail when the reference
reward approaches zero. The proof instead bounds
`r_max * max_i |bhat_i-b_i|`, exactly the quantity needed by the reward
comparison. Projection onto `[0,1]` gives
`rhat_j*|bhat_i-b_i| <= xi+epsilon_r`; replacing the estimated reference reward
by the true reward and then by `r_max` costs the claimed additional errors.
The argument uses the fact that the end-state error is at most one, rather
than dividing a final bound by a potentially tiny true reward.

If the largest pilot estimate is zero, every pilot estimate is zero and the
same concentration event forces `r_max <= epsilon_r`. The separate zero
branch is therefore valid. Arms of reward zero may still alter future states;
the reference-arm probes retain those effects. No minimum positive reward,
reward gap, or end-state separation is required.

### The informed full-horizon comparator

The exploration uses `N` rounds and changes the actual latent state. The proof
charges both costs. The informed benchmark's discarded prefix contributes at
most `N`, and either the learner's or benchmark's state after that prefix is
within `lambda*N` of one. The comparison of an arbitrary true tail to the
estimated tail begun at one includes this discrepancy explicitly.

The one-step reward comparison is valid in the form
`epsilon_r + r_max*(lambda*N+Delta_b)`. The parameter estimates are uniformly
accurate on the event, so this bound holds simultaneously for all tail
sequences, including the selected sequence and the informed benchmark's tail.
Taking two such comparisons, plus the planning loss, proves the displayed
regret bound without resetting the physical state or reducing benchmark
reward by a multiplicative factor.

The realized sum of conditional reward means is the correct quantity to use:
its expectation is the learner's expected reward by the tower property.
Conditioning on the final selected sequence and then assuming unbiased
historical observations would have been invalid, and is not done here.

### Planner and rate

Rounding the internal state down by a grid of mesh `1/T^2` loses at most
`t/T^2` state at time `t` for any fixed sequence. Summing the corresponding
reward losses gives at most `H(H-1)/(2*T^2) <= 1/2`. The rounded dynamic program
optimizes over all sequences, and its selected sequence has continuous reward
at least its rounded reward. These facts establish its additive guarantee.
The internal grid state is calculated from estimated parameters and is never
read from the environment.

With `L` of order `T^(4/5)*(log T)^(1/5)`, the dominant errors
`eta/(lambda*L)`, `E/(lambda*L)`, and `lambda*N` are all of order
`T^(-1/5)*(log T)^(1/5)` for fixed `K,c`. The unscaled prefix cost has the
claimed order as well. The constants are independent of the unknown reward
and end-state parameters, so the conclusion also covers parameter vectors
depending on `T`. The finite-horizon fallback and the restriction
`0 < lambda <= 1` handle the remaining admissible horizons.

## Implementation and executable evidence

The implementations in `q964.py` and `check_q964.py` were read. The schedule,
reference tie rule, estimator sign, clipping branch, grid indexing, remaining
horizon, and fallback correspond to the written policy. The reference
implementation performs estimation and planning with rational arithmetic for
rational input parameters; floating point evaluation only chooses the integer
block budget. Its cubic planner is a reproducibility implementation and does
not imply practical feasibility at the enormous horizons at which this
conservative schedule first explores rather than falling back.

An independent rerun of `python3 check_q964.py` passed:

| Control | Count |
| --- | ---: |
| Exact state-remainder inequalities | 12,096 |
| Matched probe offsets | 252 |
| Estimator scenarios | 144 |
| Estimator bounds strictly below one | 96 |
| Independent clipping cases | 512 |
| Grid plans compared with exhaustive sequence optima | 108 |
| Tail initial-state comparisons | 324 |
| Callback schedule and fallback checks | 2 |

These finite controls test vulnerable identities and boundary cases. The
all-horizon regret rate rests on the mathematical inequalities reviewed above.

## Remaining scope limits

The result concerns known `lambda=c/T` with fixed positive `c` and fixed
number of arms. It does not establish an optimal exponent, constants uniform
as `c` approaches zero or infinity, a growing-arm guarantee, or unknown-rate
learning. None of these extensions is required by the catalog statement.
