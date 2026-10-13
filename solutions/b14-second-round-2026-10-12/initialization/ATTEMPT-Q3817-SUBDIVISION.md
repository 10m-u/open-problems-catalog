# Q3817 attempt 5: Gamma-concentrated subdivisions do not transfer a bad NN order

**Proposed full-target route.** Try to disprove Q3817 by realizing a deterministic bad weighted tree inside an iid-exponential sparse graph. Replace a weight-$j$ edge by a chain of $jM$ independent $\operatorname{Exp}(1)$ edges. Its total is Gamma distributed with mean $jM$ and relative standard deviation $1/\sqrt{jM}$, so large $M$ appears to reproduce the scaled macro distances and the logarithmic NN lower bound.

**Outcome.** This transfer cannot follow from concentration of macro distances. In Q3817 every generating-graph vertex is a city, including every inserted subdivision vertex. Two exact obstructions show that the added cities change NN at both deterministic and stochastic levels. The subdivided exponential family itself is not proved to have a constant or divergent expected ratio; no Q3817 counterexample is claimed.

## A near-unit weighted tree theorem

**Theorem.** On a finite tree whose positive generating-edge weights lie in $[a,b]$ with $b<2a$, nearest neighbor from every start and under every tie rule makes a depth-first traversal after shortest-path expansion. Its closed tour has cost $2W=OPT$.

Root the tree at the start. Initially, and whenever NN first visits a vertex with an unvisited adjacent child, such a child has distance at most $b$. Any nonadjacent unvisited city has distance at least $2a>b$, so NN must select an adjacent child.

Inductively assume the already completed child subtrees have been exhausted, and the currently unfinished ancestors lie on the root-to-current path, as in a DFS prefix. When the current vertex has no adjacent unvisited child, let $u$ be its closest ancestor with an unvisited child. A child of $u$ is at distance at most $d(v,u)+b$. Any boundary edge attached to a higher ancestor requires at least one additional ancestor edge and its final boundary edge, giving distance at least $d(v,u)+2a$, which is larger. A city deeper in an unvisited subtree is farther than that subtree's first child. Thus NN backtracks to $u$ and visits one of its unvisited children. No completed subtree is entered again. This proves the induction, including arbitrary ties between children of the same ancestor.

After returning to the start, every generating edge has been traversed exactly once in each direction. All metric shortcuts have equal length to their expanded tree paths. The cost is $2W$, which is optimal by the generating-edge cut lower bound. The assumption is strictly stronger than positive weights; weighted trees outside this range can have logarithmic NN ratios.

## Subdivision preserves the old metric but destroys its NN lower bound

Use the strict bad tree $T_K$ from [attempt 3](ATTEMPT-Q3817-MST-ENVELOPE.md), with connecting edges of weight $j$ and leaf spikes of weight $1+j/(4K)$. Its old-city NN ratio is at least $(K+1)/7$.

Replace each integer-weight connector $j$ by a path of $j$ unit edges and keep every spike unchanged. Distances between all original vertices are exactly preserved. Yet every generating edge of the subdivided tree now lies in $[1,5/4]$, and every inserted vertex is a city. The theorem above gives NN/OPT exactly 1 from every start and for every tie rule. Thus preserving the entire original distance matrix does not preserve NN when the city set has been enlarged.

This is a strict, all-size obstruction, rather than dependence on a special tie rule. The all-city conclusion also survives any sufficiently small perturbation retaining $b<2a$. Counting only the old vertices would instead be a different model. The source paper explicitly distinguishes restriction to a city subset as a separate proposed extension in [§6](https://doi.org/10.1007/s00453-023-01167-3); Q3817's setup uses all generating vertices.

## Persistent disagreement in the actual exponential model

Take a junction $v$ with a short arm of $M$ independent exponential edges $X_1,\ldots,X_M$ and a long arm of $2M$ independent exponential edges $Y_1,\ldots,Y_{2M}$. This graph is a path; start NN at $v$. Write

\[
A=\sum_{i=1}^M X_i,\qquad B=\sum_{i=1}^{2M}Y_i.
\]

An endpoint-only model has three cities: the junction and the two arm endpoints. Its first NN choice is the short endpoint on $A<B$. The independent Gamma totals satisfy

\[
\mathbb E[B-A]=M,\qquad\operatorname{Var}(B-A)=3M,
\qquad \Pr(A\ge B)\le\frac3M
\tag{1}
\]

by Chebyshev's inequality. Thus the intended macro choice has probability tending to 1.

The all-city NN algorithm initially compares only $X_1$ and $Y_1$. Each wins with probability $1/2$, independently of the lengths of the two arms. More strongly, there is a probability bounded away from zero that it explores the entire long arm before even entering the short one. Let $R_j=\sum_{i=1}^jY_i$, and set

\[
E=\{Y_i<R_{i-1}+X_1\text{ for }1\le i\le2M\}.
\]

On this event the nearest short-arm city remains its first vertex, at distance $R_{i-1}+X_1$, and NN takes every successive long-arm neighbor. The complete-long-arm argument in [attempt 4](ATTEMPT-Q3817-FRESH-CLOCKS.md), applied to the boundary weight $X_1$, gives

\[
\Pr(E\cap\{X_1\ge\log4\})\ge\frac18.
\tag{2}
\]

The rest of the short arm plays no role in that estimate. Combining (1)–(2) by the union bound, with no independence assertion, gives

\[
\Pr(E\cap\{X_1\ge\log4\}\cap\{A<B\})
\ge\frac18-\frac3M
\ge\frac1{16}\qquad(M\ge48).
\tag{3}
\]

On (3), the concentrated endpoint-only NN selects the short endpoint, while all-city NN reaches the long endpoint first and has visited no short-arm vertex. Therefore even the induced order of the original endpoints fails to match the macro NN order with a nonvanishing probability as subdivision lengths grow. Concentrating the macro distances does not fix the city-set mismatch.

The path theorem still bounds the actual all-city ratio by $3/2$. The claim here is about the failed transfer, rather than a lower bound on its approximation ratio.

## Checks, scope and per-problem stopping rule

[check_subdivision.py](check_subdivision.py) checks the near-unit theorem against all NN tie choices on every labelled tree through five vertices, with edge weights 1 or $3/2$: 2,140 tree weightings, 10,548 starts and 17,922 NN orders. It verifies 42,933 preserved old-city distance pairs on seven recursively subdivided bad families and optimal all-city costs for one deterministic order in each larger family. Exact rational controls check the constants in (1)–(3). Its receipt is [SUBDIVISION-CHECK-RESULTS.json](SUBDIVISION-CHECK-RESULTS.json). The general theorems come from the written proofs, not the finite controls.

This is the fifth distinct substantive failed full-target route for Q3817: packing-integral ceiling; uniform expected generating-edge charge; pointwise MST domination; uniform expected NN step cost; and subdivision/Gamma transfer of a deterministic lower bound. The named-family theorems remain partial and do not reset the full-question count. Subject to the main thread's independent review, Q3817 therefore reaches the user's five-consecutive-failures stopping rule **for this problem only**. Q3817 remains unresolved. This does not stop work on other B14 targets.
