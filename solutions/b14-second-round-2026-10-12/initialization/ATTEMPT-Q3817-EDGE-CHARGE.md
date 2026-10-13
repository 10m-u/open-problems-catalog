# Full-scope Q3817 attempt: a uniform expected edge charge fails

**Target route:** for each generating edge, uniformly bound the expected traversal charge made by nearest neighbor, then sum over the sparse edge set. This would establish a linear expected NN cost, and might combine with a denominator argument to settle Q3817.

**Outcome:** the uniform edgewise estimate is false even for independent-exponential tree metrics. A double-star has a central edge whose expected charge is $\Theta(\log n)$, while its total expected NN ratio tends to one. This is a failed full-scope proof route, not a counterexample to Q3817. The construction is separate from the packing obstruction in [the first attempt](ATTEMPT-Q3817-PACKING.md).

## The exponential double-star

There are two hub cities, $A,B$, joined by an edge of weight $L$. Attach $m$ leaf cities to each hub. All $2m+1$ generating-edge weights are independent $\operatorname{Exp}(1)$; all $n=2m+2$ vertices are cities. Start nearest neighbor at $A$.

Let $C$ count traversals of the bridge cut by the completed metric tour, and let $M$ be the largest of the $2m$ leaf-edge weights. Every leaf cut is a singleton and is crossed exactly twice by any tour. Thus

$$
NN=2\sum_{\text{leaf edges}}w_e+LC,\qquad
OPT=2\sum_{\text{leaf edges}}w_e+2L.
\tag{1}
$$

The only extra traversal charge is at the bridge.

## Nearest-neighbor phases

Once both hubs are visited, every unvisited city is a leaf. If the current city is on side $A$, the common cost of reaching hub $A$ cancels from its comparisons: it chooses an $A$ leaf of next weight $a$ rather than a $B$ leaf of next weight $b$ exactly when $a<L+b$. Leaf weights on each side are therefore consumed in increasing order.

A phase is a maximal consecutive run of leaf selections on one side. During it the opposite side's smallest unvisited weight, $r$, stays fixed, and the current side consumes its remaining leaf weights up to threshold $L+r$. If it does not exhaust that side, its next weight is greater than $L+r$, and it then crosses the bridge. The initial $A$ phase fits the same description with $r=0$, treating the still-unvisited hub $B$ as the opposite candidate. Ties have probability zero.

Let $r_j$ be the finite smallest remaining weight on the side just left after phase $j$. Successive finite phase endings satisfy

$$
r_j>L+r_{j-1},\qquad r_0=0.
\tag{2}
$$

Since $r_j\leq M$, the number of finite phase endings is at most $M/L$. There can be at most one additional open bridge crossing after a side is exhausted, because all remaining unvisited leaves then lie on the other side. The closing tour edge contributes at most one more bridge traversal. Consequently

$$
LC\leq M+2L.
\tag{3}
$$

The same non-strict upper bound permits ties under any nearest choice. Since $\mathbb E[M]=H_{2m}$ and $\mathbb E[L]=1$,

$$
\mathbb E[LC]\leq H_{2m}+2=O(\log m).
\tag{4}
$$

For completeness, integrating $\Pr(M>t)=1-(1-e^{-t})^{2m}$ and substituting $u=e^{-t}$ gives $\mathbb E[M]=\int_0^1[1-(1-u)^{2m}]du/u=H_{2m}$.

## A probability-backed lower bound

Set $\delta=1/4$, $J=\lfloor2\log m\rfloor$, and $T=J/4$. Let $E_m$ be the event that on each side at least one leaf weight lies in every bin

$$
[j\delta,(j+1)\delta),\qquad0\leq j\leq J.
$$

Any one bin has probability at least $(1-e^{-1/4})e^{-T}\geq(1-e^{-1/4})m^{-1/2}$ for a leaf. A union bound over both sides gives

$$
\Pr(E_m)\geq
1-2(J+1)\exp[-(1-e^{-1/4})\sqrt m]
=1-o(1).
\tag{5}
$$

On $E_m$, after any phase with threshold $t\leq T$, the side cannot be exhausted: there is a leaf in $(t,t+2\delta]$. That leaf is still unvisited, because leaves previously consumed on that side have weights at most the current phase threshold. Thus its next weight is at most $t+2\delta$.

Now also condition on $1/2\leq L\leq1$. As long as phase thresholds are at most $T$,

$$
r_j\leq L+r_{j-1}+2\delta\leq\tfrac32j.
\tag{6}
$$

The process cannot finish while all phase thresholds are at most $T$, by the occupied-bin property. Let phase $j$ be the first with threshold $L+r_{j-1}>T$. Then $r_{j-1}>T-L\geq T-1$, so (6) implies $j-1>\frac23(T-1)$. The preceding $j-1$ nonexhausting phases have already crossed the bridge. Hence

$$
LC\geq\frac{T-1}{3}
\qquad\text{on }E_m\cap\{1/2\leq L\leq1\}.
\tag{7}
$$

The bridge is independent of the leaf event, and $\Pr(1/2\leq L\leq1)=e^{-1/2}-e^{-1}>0$. Therefore, for all sufficiently large $m$,

$$
\mathbb E[LC]
\geq(e^{-1/2}-e^{-1})\Pr(E_m)\frac{T-1}{3}
=\Omega(\log m).
\tag{8}
$$

Combining (4) and (8) proves $\mathbb E[LC]=\Theta(\log m)$ for this named sparse exponential family. No rare-event conditioning on all weights being near one is used; the occupied-bin event has probability tending to one, and the bridge event has a fixed positive probability.

## This family satisfies the desired total-ratio behavior

The [tree normalization identity](RESULT.md#5-an-exact-exponential-normalization-identity-on-trees) gives the equality between expected ratio and ratio of expectations for this model. From (1),

$$
\mathbb E[NN/OPT]
=\frac{4m+\mathbb E[LC]}{4m+2}
=1+\Theta\!\left(\frac{\log m}{m}\right).
\tag{9}
$$

Thus Q3817 is not refuted. What fails is the proposed uniform bound $\mathbb E[w_e C_e]\leq C_0$ for every generating edge, even though the entire sum remains linear on these double-stars. A successful charging proof must allow exceptional high-load edges and account for their surrounding city mass; it cannot assign a fixed constant budget to every edge separately.

## Bounded check and source scope

[check_double_star.py](check_double_star.py) checks phase/cost identities and (3) on exhaustive small positive-integer double-stars with ties, plus explicit occupied-bin instances for (7). Its receipt is [DOUBLE-STAR-CHECK-RESULTS.json](DOUBLE-STAR-CHECK-RESULTS.json). The asymptotic probability bound follows from (5), rather than from a simulation.

The target and exponential sparse-graph model are from Klootwijk and Manthey, §§2, 4.2 and 6. [Original paper](https://doi.org/10.1007/s00453-023-01167-3). This note establishes a restricted stochastic obstruction to a full-scope proof strategy; no full Q3817 resolution, originality claim, or streak reset is made.
