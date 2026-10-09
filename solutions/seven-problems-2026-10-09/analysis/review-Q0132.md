# Independent internal review of Q132

Date: 2026-10-09. Reviewed file: [`../dynamics/Q0132.md`](../dynamics/Q0132.md).

**Disposition: accept both sufficient-condition theorems as written; retain Q132 as partial.** This is an independent derivation and source-scope review by a second AI research agent, not external peer review or a novelty certification. No unresolved proof defect was found.

## Source and scope check

The [primary paper, arXiv:2305.10286v3](https://arxiv.org/html/2305.10286v3), was opened independently, particularly Section 6.1 and Appendix D.1. Its Theorem 3 assumes bounded waiting, and the adjacent discussion separately establishes the binary-weight conclusion for every fair schedule. Its Remark 4 distinguishes aggregate convergence from individual-allocation convergence. The report preserves all three distinctions: Theorem A is a schedule extension for general weights; Theorem B is a profile restriction permitting all fair schedules; only Theorem B asserts convergence of each row. The binary case is correctly acknowledged as pre-existing.

Zero-budget agents can be deleted, consistently with the source model. After the finite initialization prefix, all rows have their fixed budgets and are supported on their donors' valued projects. Thus every external aggregate compared in the nonexpansiveness argument has the same total. No total-mass assumption is used before it becomes valid.

## Independent checks of Theorem A

1. **Best-response uniqueness.** At a proposed utility level, the positive-part vector is coordinatewise the least expenditure that attains the level. At the largest affordable level the positive parts exhaust the budget, leaving no slack to spend outside the support or on noncritical coordinates. The scalar function is strictly increasing once it becomes positive; hence the positive-budget solution is unique.

2. **Nonexpansiveness.** If the two water levels satisfy $\lambda\le\lambda'$, every coordinate with $z_x>z'_x$ satisfies $z_x-z'_x\le b'_x-b_x$. Summing on those coordinates uses the equal totals of $z,z'$; bounding by all positive differences of $b'-b$ uses the equal totals of $b,b'$. Reversing the two states covers the other ordering. This gives the stated total-variation coefficient exactly $1$, including zero coordinates.

3. **Residual movement bound.** For a nonupdating donor, only the best-response target changes, and nonexpansiveness gives a residual change at most the aggregate moved mass. For the updating donor, the prior residual equals that moved mass and the new residual is zero. Thus a complete interval must move at least the initial largest residual: choose the donor attaining that residual and sum the one-step bounds through her first update in the interval.

4. **Entropy maximization.** The derivative on positive aggregate coordinates is $\log v_{ix}-\log\delta_x-1$. The water-filling solution equalizes this derivative on positive row coordinates and makes it no larger on zero row coordinates. Every equilibrium has positive aggregate on every valued project, because any donor can independently secure positive utility. At such a state, rowwise first-order conditions combine into the global condition on the product of simplices. This verifies the equivalence of global maximizers and zero residuals; it is not merely coordinatewise stationarity for an arbitrary nonconcave function.

5. **Quadratic improvement.** Every post-initialization aggregate coordinate lies in $[0,B]$. Subtracting $s^2/(2B)$ from $s\log s$ leaves a convex function, including the endpoint zero by continuity. Therefore each row block of the potential is $1/B$-strongly concave. The improvement of an exact block maximizer is at least the squared Euclidean movement divided by $2B$. Since the row's $\ell^1$ movement is $2c_t$ and has at most $m$ coordinates, the claimed coefficient $2/(Bm)$ follows. The segment argument covers an old state with zero aggregate coordinates.

6. **Complete-interval argument.** Cauchy–Schwarz gives $\sum c_t^2\ge(\sum c_t)^2/L_k$, not an unweighted lower bound on each interval. If the limiting potential were below its maximum, compactness and the equivalence in item 4 would make every late initial residual at least a fixed $\eta>0$. Summation over the intervals contradicts bounded potential precisely when $\sum_k1/L_k=\infty$. This proves the theorem's stated sufficient condition without silently replacing it by fairness.

7. **Aggregate convergence.** Every accumulation point maximizes the potential. Strict concavity of the aggregate entropy term makes the aggregate common to all maximizers; the other term is linear in the rows. Compactness consequently yields convergence of the aggregates, even if the rows themselves have multiple accumulation points. The report does not claim individual convergence from this argument.

## Independent checks of Theorem B

Canceling each donor's factor $a_i$ leaves common project weights. For an order-preserving transfer from $x$ to $y$, the pair $(x,y)$ in the weighted Gini function loses exactly $(w_x+w_y)\varepsilon$. For each third project $z$, the derivative of the sum of the two relevant terms is

$$
w_z\left(\operatorname{sgn}\left(\frac{\delta_y+s}{w_y}-\frac{\delta_z}{w_z}\right)
-\operatorname{sgn}\left(\frac{\delta_x-s}{w_x}-\frac{\delta_z}{w_z}\right)\right)\le0.
$$

The inequality follows from the preserved order, and piecewise linearity handles ties and breakpoints. There is no missing project-dependent factor in this derivative.

The proposed transfer decomposition is valid. Coordinates whose donor allocation increases finish at the common normalized water level. Coordinates whose allocation decreases finish at or above that level. While matching source supplies to recipient demands, each source remains at least its final level and each recipient at most its final level. Every transfer therefore preserves the required order and exhausts at least one unfinished change. The sum of its amounts is exactly the total-variation movement of that row.

The linear decrease implies finite total moved mass because the Gini function is nonnegative. Summing the rowwise $\ell^1$ changes proves convergence of the entire state. Each donor's infinitely many post-update states then has zero residual and converges to the same limit; continuity makes that limit an equilibrium. This use of fairness is sound even with arbitrarily long waits.

Finally, taking logarithms turns the factorization condition into a potential assignment on a bipartite graph. Its cycle sums vanish exactly when the stated alternating products agree. Propagation along a spanning tree proves sufficiency, and forests have no remaining conditions. The forest corollary therefore applies to arbitrary positive edge weights, as claimed.

## Remaining boundary

Theorem A's proof does not cover fair schedules with a convergent reciprocal-length sum. Theorem B's proof requires consistent project weights around every incidence cycle. Square-summability from the entropy estimate cannot be promoted to summability without an additional argument. These gaps are explicitly stated in the report, so neither theorem is presented as a solution of the full catalog question.
