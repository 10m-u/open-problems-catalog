# Q3817 attempt 4: uniform expected NN step costs fail

**Proposed route.** Adapt the exponential graph-growth estimates from [Klootwijk and Manthey, §§3.1 and 4.2](https://doi.org/10.1007/s00453-023-01167-3) to each successive NN origin, using memorylessness to obtain a uniform expected cost per nonclosing step. Summing $n-1$ such ceilings would give $\mathbb E[NN]=O(n)$; a separate lower-tail estimate for $OPT$ would then be needed for the actual expected ratio.

**Outcome.** The required uniform unconditional step ceiling is false on independent-exponential paths. One fixed nonclosing step has expected length $\Omega(n)$. Conditioning on the NN history also retains frontier lower thresholds; it cannot reset the unexplored boundary to unshifted exponentials. This is an obstruction to this route, not to the $O(n)$ total expected-cost claim or Q3817.

## The conditioning that memorylessness actually permits

For a positive-weight graph and current visited set $S$, the closest unvisited city is reached by a path whose internal vertices lie in $S$. For each boundary edge $e=(u,z)$, $u\in S,z\notin S$, its candidate distance is

\[
a_e+w_e,\qquad a_e=d_{G[S]}(v,u).
\]

The next distance is the minimum of these candidates. At a decision with selected distance $t$, every still-hidden losing boundary weight satisfies the separate constraint $w_e\ge t-a_e$. Over multiple decisions its lower threshold is the maximum of all such nonnegative constraints while it remains on the boundary. Write this threshold as $L_e$.

In a deferred-revelation implementation, condition on the selected edges and their weights, internal revealed weights, and the comparison history. Every remaining hidden boundary weight has a factorized conditional law

\[
w_e=L_e+Y_e,\qquad Y_e\stackrel{\mathrm{ind}}\sim\operatorname{Exp}(1).
\tag{1}
\]

At each decision, the revealed current data determine $a_e$ and the relevant thresholds. Conditioning independent exponentials on these separate lower bounds preserves independence, with the indicated shifts. Newly exposed edges to unvisited endpoints have threshold zero. An edge that becomes internal can be revealed at its shifted law before recomputing internal distances. This sequential construction has the same decisions as full metric NN. With continuous weights, exceptional ties between genuinely different path sums have probability zero; tied shortest representations of the same city are immaterial.

The correct clocks are therefore $a_e+L_e+Y_e$, not $a_e+Y_e$. Moreover, the travel offsets $a_e$ can themselves be large. Formula (1) supplies useful exact conditional information but gives no uniform ceiling on the full NN step.

## Exact one-step illustration

Take a three-city path with center start and edge weights $X,Y\stackrel{\mathrm{ind}}\sim\operatorname{Exp}(1)$. Condition on choosing the $X$ leaf first. Then $X\sim\operatorname{Exp}(2)$, and $Y-X\sim\operatorname{Exp}(1)$ is independent of $X$; this follows directly by substituting $y=x+r$ in the conditional density $2e^{-x-y}$ on $0<x<y$.

The next step has distance $X+Y=2X+(Y-X)$ and expected value 2. Discarding the retained threshold $L_Y=X$ would instead give expected value $\mathbb E[X]+1=3/2$. This finite mismatch already rejects a fresh, unshifted boundary law after a restart. Its total tour remains optimal; the illustration concerns conditioning alone.

## A fixed step with linear unconditional expectation

Let a path have a center $v$, a right arm of $r$ edges with independent weights $X_1,\ldots,X_r$, and a single left edge with weight $Z$, independent of those weights. There are $n=r+2$ cities. Start NN at $v$ and put $S_j=\sum_{i=1}^jX_i$, $S_0=0$.

If NN has visited only the right prefix through vertex $j$, its next right choice has distance $X_{j+1}$, whereas the left leaf has distance $S_j+Z$. It follows by induction that NN visits the entire right arm before the left leaf on

\[
E_r=\{X_i<S_{i-1}+Z\text{ for every }1\le i\le r\}.
\]

Let $D_r$ be the nonclosing NN step after the $r$th newly visited city. On $E_r$, it departs from the right endpoint to the remaining left leaf and has distance $S_r+Z$.

Set $z=\log4$. For every fixed $Z\ge z$, independence and the exponential tail imply

\[
\Pr(E_r^c\mid Z)
\le\sum_{i=1}^r\mathbb E[e^{-(S_{i-1}+Z)}\mid Z]
=e^{-Z}\sum_{i=1}^r2^{-(i-1)}
<2e^{-Z}\le\frac12.
\]

No independence between the failure events is assumed. Thus

\[
\Pr(E_r\cap\{Z\ge z\})\ge\frac18.
\tag{2}
\]

Markov's inequality applied to $e^{-S_r}$ gives a separate exact bound

\[
\Pr(S_r<r/2)
\le e^{r/2}\mathbb E[e^{-S_r}]
=\left(\frac{\sqrt e}{2}\right)^r.
\tag{3}
\]

Combining (2)–(3), without conditioning a Gamma distribution on the NN event, yields

\[
\mathbb E[D_r]
\ge\frac r2\left[\frac18-\left(\frac{\sqrt e}{2}\right)^r\right]
=\Omega(r).
\tag{4}
\]

For every $r\ge32$, the bracket is at least $1/16$, so $\mathbb E[D_r]\ge r/32$. Indeed, $e<11/4$ follows from its series with a geometric upper bound on the tail, and $(11/16)^{16}<1/16$ is an exact rational comparison. This rules out a size-independent expected bound for every nonclosing step even in the actual iid exponential model, on a named sparse family and a specified start.

At the same time, the [proved deterministic path theorem](RESULT.md) gives $NN\le3W$, hence $\mathbb E[NN]\le3(r+1)$. A small number of long relocation steps is compatible with a linear total. The failed stepwise ceiling cannot be inferred from the successful total ceiling.

## Scope

[check_fresh_clocks.py](check_fresh_clocks.py) passes 3,276 exact small path controls, including 931 strict complete-right-arm orders, independently checking the NN recurrence and long-step formula. It also verifies the rational three-city moments and the finite constants establishing $r\ge32$. See [FRESH-CLOCKS-CHECK-RESULTS.json](FRESH-CLOCKS-CHECK-RESULTS.json).

This is a fourth distinct failed route for full Q3817. It rules out summing a uniform expected NN-step bound and identifies the actual retained exponential thresholds. It does not exclude charging long steps to many earlier cities, a global expected bound, or an expected-ratio bound. The source's fixed-origin growth process and fast-growing-cut theorem are unaffected. No simulation, costly enumeration, or full-question disproof is claimed.
