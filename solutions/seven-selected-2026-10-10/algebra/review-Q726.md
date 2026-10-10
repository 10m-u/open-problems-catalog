# Independent review of Q726

**Reviewer role:** algebra agent, separate from the author of the Q726 note.
**Reviewed on:** 2026-10-10.
**Verdict:** the proof establishes the stated regret rate under its explicitly
retained bounded-estimator/source-projection convention. No mathematical
correction to the argument was identified. This is an internal proof review,
not external peer review.

The reviewed file is [learning/Q726.md](../learning/Q726.md).

## Source scope

The [primary source](https://arxiv.org/html/2406.16745v3), Section 5.2,
raises the removal of the plausible-maximizer restriction after Theorem 6.
Section 4 explicitly assumes the fitted RKHS norm bound in its main-text
analysis. Appendix A, Equation (8), supplies a constrained gradient-space
projection, and its Theorem 10 gives the corresponding formal confidence
statement. Section C.1 applies the confidence result to the dueling kernel.

The Q726 note correctly retains that theoretical convention and explicitly
excludes an unprojected fitted function whose norm exceeds the stated bound.
Its mention of projection should be read as the source's Equation (8),
not an arbitrary Euclidean or radial projection.

## Independent reconstruction

1. **Difference structure and pseudometric.** The dueling feature map is
   $\psi(x,y)=\phi(x)-\phi(y)$. With $a_0>0$ and
   $V=a_0I+\sum\psi_j\otimes\psi_j$, the inverse identity gives
   $d(x,y)^2=a_0\langle\psi(x,y),V^{-1}\psi(x,y)\rangle$.
   Thus $d$ is the norm distance between transformed features. Its symmetry,
   zero diagonal, and triangle inequality follow without a finite-dimensional
   feature assumption. A norm-bounded member of the dueling RKHS remains a
   scalar difference after projection, and evaluation gives
   $|h(x,y)|\le B\|\psi(x,y)\|\le2B$.

2. **Leader improvement.** For a selected leader $x$, follower $y$, and
   $D=g(y)-g(x)>0$, the difference between the two objectives against any
   opponent $z$ is at least $m_BD-\beta d(x,y)$. The logistic derivative is
   bounded below by $m_B$ on the entire relevant interval, and the negative
   uncertainty term is controlled by the triangle inequality with the
   correct sign. Taking infima and then using the leader's global
   optimality yields $D\le\beta d(x,y)/m_B$. This argument allows ties and
   does not rely on the plausible-maximizer restriction.

3. **Selected value.** The follower may match the leader, giving $v\le1/2$.
   Writing $u=\beta d(x,y)$ and $w=1/2-v$ gives
   $w=s(D)-1/2+u$. The derivative upper bound $1/4$ and the preceding
   inequality yield $0\le w\le C_Bu$. The case $D\le0$ obeys the same
   inequality without a mean-value lower bound.

4. **Two queried regrets.** The optimal true action is in the unrestricted
   follower domain, so the leader's logistic regret $a$ is at most $w$ on
   the uniform confidence event. If the follower has at least the leader's
   true utility, its regret $b$ is at most $a$. In the other case, logistic
   centered regret is subadditive on nonnegative arguments, and confidence
   on the selected pair gives the additional true preference gap at most
   $2u-w$. Hence $b\le2u$. As $C_B\ge2$, both terms are at most $C_Bu$.
   The proof also covers $u=0$ without division.

5. **Information gain.** The posterior covariance is bounded above by
   the prior covariance, so $0\le d_t^2\le4$. Sequential determinant
   factorization gives the sum of $\log(1+d_t^2/a_0)$. The chord bound
   for the concave logarithm on $[0,4]$ has the direction used in the
   note and yields the factor $8/\log(1+4/a_0)$ after the definition of
   information gain. Cauchy--Schwarz and monotonicity of the original
   exploration coefficient give exactly the displayed cumulative
   constant. The pre-round covariance indexing is consistent with this
   factorization. A single uniform confidence event suffices for every
   horizon.

## Executed controls

The command

    python solutions/seven-selected-2026-10-10/learning/check_q726.py

completed successfully. Its exact rational controls covered 4,617 finite
games and 6,726 optimizing leader/follower pairs, including ties and zero
widths. The nonmetric negative control was detected. The feature/kernel
posterior comparisons and sequential determinant identities also passed.
These checks support the calculations; the written proof supplies the
general-domain and anytime assertions.

## Presentation note

The initially reviewed draft contained some lost inline mathematics
delimiters, including a mixed parenthesis/dollar delimiter around the
optimal action. These were repaired in the final formatting audit. They
do not affect the mathematical verdict above.
