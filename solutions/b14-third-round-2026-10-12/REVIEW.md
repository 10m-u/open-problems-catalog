# Review of the B14 third return

13 October 2026. Review by the main thread against the actual first-round proof, its review, and the submitted report and code. This is an intake review independent of the submitted derivation, without a new subagent or a new research search. All mathematical results below are accepted at their stated scopes.

## Advance over the handoff

The predecessor retained every exchange using a read-two inequality. It proved an all-size upper bound with base $c=\sqrt\pi\,\operatorname{erfc}(1/2)<6/7$. It explicitly left a sharp rate and matching lower bound open. The return proves

$$
\mathbb E M_n=\sqrt{n!}\exp(n\log\rho+o(n)),\qquad
\rho=e^{-1/2}\min_{a\ge0}e^{a^2/2}J(a),
$$

where $J(a)=\int_0^\infty e^{-y^2/2-ay}\,dy$. The evaluated rate is approximately 0.597586978551345; an exact rational estimate proves $\rho<3/5$. This supplies a smaller upper base and a matching exponential lower rate. It is stronger than an alternative proof of Q3818's existing closure. The independent-law endpoint extension is also new relative to the handoff. The replication section is an audit of existing finite evidence.

## Conditional probability argument

For a fixed cyclic tour, each replacement chord appears in exactly two exchange constraints. For $n\ge5$ the conditional dependency graph has degree two; distinct dependent constraints share exactly one chord. The even diameter component has $n/2$ constraints. The exceptional $n=4$ component is excluded from the asymptotic argument.

For tour coordinates bounded by $\delta<1/2$, a bad exchange of threshold $t$ has probability $t^2/2$. Two thresholds $s,t$ sharing a chord have joint probability $\min(s,t)^2\max(s,t)/2-\min(s,t)^3/6$. It is at most $\delta(p(s)+p(t))$. Summing over unordered dependency edges gives $\Lambda\le2\delta\mu$ because each exchange has two neighbors.

[Riordan and Warnke, Theorem 1](https://arxiv.org/pdf/1203.1024), was checked directly: its ordered-pair $\Delta$ is $2\Lambda$, and the no-event bound is $\exp(-\mu+\Delta/2)$. Its hypotheses admit general monotone events, not just intersections of coordinate events. Reversing the coordinate order handles bad exchanges. Harris association and closure under unions/intersections hold in this product space. Finite monotone discretization with null threshold boundaries justifies the continuous version. Positive association of the complementary events gives the lower product bound. Together these yield report equation (13), with the directions and factors as written.

The exact expansion $Q=(n-4)A+S^2-2B$ and $0\le B\le A$ give $(n-6)A+S^2\le Q\le nA+S^2$. Retaining $S^2$ matters to the rate.

## Whole integral and matching lower rate

Clipping each tour coordinate to $\delta$ can only increase the conditional probability of local optimality. The clipped measure has density one below $\delta$ and atom $1-\delta$ at the cap. Thus equation (17) bounds the whole original integral, including coordinates above the cap. The tangent to $S^2$, with scale $\sqrt{(1-2\delta)(n-6)}$, has the displayed constant and linear terms. For fixed $\delta$ the cap atom vanishes exponentially compared with the $n^{-1/2}$ integral. This proves the upper root limit before sending $\delta$ to zero.

For the lower bound, using the upper quadratic estimate in the negative exponent and restricting to the small cube are both valid lower bounds. Rescaling by $\sqrt{bn}$ gives equation (19). The tilted product density gives the exact identity (20); it is not an approximate saddle-point calculation. Strict convexity of $\log H$ establishes the unique minimizer, with mean $a_*$ and variance $1-2a_*^2$. Jensen applied to the nonnegative squared centered sum gives the constant lower expectation. Subtracting the union-bound Gaussian tail outside the cube preserves a positive constant for large $n$. This proves the matching lower root limit.

The tour count $(n-1)!/2$ and Stirling's formula give the factor $e^{-1/2}$ in $\rho$. The rational upper estimate in equation (24) follows from Taylor bounds and $\pi<22/7$; its value is $26186281431/43750000000<3/5$. A root limit strictly below $3/5$ implies the stated big-O bound, absorbing finite exceptional sizes. It does not imply a bounded correction at base $\rho$.

## Endpoint extension

A common finite lower endpoint cancels in every exchange. Density bounds $f_-,f_+$ on the small interval bound both single-event probabilities and shared-chord intersections. The upper clipped measure has density at most $f_+$ and an atom at most one. The lower small-cube density is at least $f_-^n$. Equations (26)-(27) correctly cancel the local density scale. Sending the density tolerance and cap to zero proves the same rate for the specified fixed absolutely continuous laws; no upper-tail moment is needed. Atoms, irregular endpoint densities, size-dependent laws and dependent metric distances are excluded from the accepted scope.

## Replay and preservation

All 28 manifested payload hashes and the manifest itself were checked. All three predecessor copies exactly match their live catalog sources. The supplied exact checker was inspected and rerun, preserving the original receipt. It passes 161,602 exchange constraints, 546 reconnection tests, 95,913 discrete assignments, 2,303 conditional-chain inequalities, 2,205 overlap checks and 592 quadratic checks. The numerical evaluator was rerun at 80 digits; its structured output matches the submission. Neither checker is a formal proof of the all-size theorem.

[Replay validation](verification/REPLAY-VALIDATION.json) records equality except elapsed times. The earlier four-check replication remains clearly identified as submitted replication evidence; it was not counted as fresh mathematical progress. The 12 October handoff stays a dated, immutable snapshot. The private result routes point to this review and submitted proof, retaining Q3818's existing proved mark and every previous result.
