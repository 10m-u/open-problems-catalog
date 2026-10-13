# Q2212: a multiplicity-boundary theorem

Partial result, independent review accepted; see ROOT-REVIEW.md#power-monoid-final-review. The full numerical-monoid
unimodality conjecture remains unresolved. In [Tringali, Conjecture5.4](https://arxiv.org/html/2602.15754v3),
alpha_(k,l)(H) counts k-element atoms with maximum **at most** l, not
maximum exactly l. The sole unit is {0}; a nonunit A is atomic precisely
when it is not a sumset B+C of two sets containing0 with cardinalities
at least two. Numerical monoids include0 and all sufficiently large integers.

## Every monoid, up to twice its least positive element

Let m=min(H minus{0}) and h=|H intersect[1,l]|. If l<2m, every nonunit
subset of H intersect[0,l] containing0 is atomic. For k>=2,

    alpha_(k,l)=binomial(h,k-1).

Indeed max(B+C)=max(B)+max(C)>=2m for any two nonunit factors.
Thus a decomposition within the cutoff is impossible.

At l=2m, the only decomposable set is {0,m,2m}. Equality in the maximum
bound requires max(B)=max(C)=m, and hence B=C={0,m}. Closure of H
ensures2m belongs to H. Therefore, for k>=2,

    alpha_(k,2m)=binomial(h,k-1)-1_(k=3).

In both formulas alpha_0=alpha_1=0, and out-of-range binomial coefficients
are zero. These give unimodality and even ordinary log-concavity for all
l<=2m. For the boundary row, only the log-concavity inequality at the
lowered coefficient needs a new check. For h>=3 its defect is

    (binomial(h,2)-1)^2-h*binomial(h,3)
      =h(h-1)(h(h+1)-12)/12+1>=1.

The h=2 row is (0,0,2,0,...); the other inequalities either retain a
binomial inequality or have a decreased right-hand side. There are no
internal zeros. Restricting the full row to indices0,...,l preserves
unimodality, including m=1 and the very short cutoffs. No novelty is claimed.

## Exact bounded coverage and literature qualification

[EXPLORATION.json](EXPLORATION.json) exhausts all1,655 additive-closed
restrictions through the single cutoff l=18. Every restriction extends to
an actual numerical monoid by including every integer greater than18.
It checks1,048,832 unordered nonunit factor pairs, yielding54,544 distinct
decomposable sets and1,136,236 atomic sets across the monoids. No
unimodality or ordinary log-concavity counterexample occurs at that cutoff.
This does not imply any arbitrary-cutoff theorem.

The survey describes Aggarwal–Gotti–Lu as giving full unimodality for
density-one cutoffs in H=N. However, the directly inspected
[original paper, Corollary5.3](https://arxiv.org/html/2412.05857v1)
states that most *cardinality indices* satisfy the appropriate consecutive
inequality, for each cutoff. Its abstract likewise describes an almost
unimodal row. Those are different quantifiers. We retain the original's
limited assertion as attributed background and do not promote it to
full rows at almost every cutoff. Its asymptotic estimates also do not
give the exact central inequalities needed here. This source discrepancy
counts as no failed mathematical attempt.

[check_routes.py](check_routes.py) independently enumerates ordinary finite
sets for the exact route obstructions and verifies the multiplicity formulas
on every additive-closed restriction through cutoff12. The all-size result
comes from the maximum argument and displayed defect, not the finite check.
