# Full-scope Q3817 attempt: the packing-integral route fails

**Target:** extend the nearest-neighbor expected-ratio bound to every sparse connected generating graph with independent $\operatorname{Exp}(1)$ edge weights.

**Attempt outcome:** this proposed proof route fails. Its universal upper-bound expression is already $\Omega(n\log n)$ on exponential paths, where the [actual NN ratio is at most $3/2$](RESULT.md). This is a precise obstruction to the estimate, not a counterexample to Q3817. No full-scope resolution or streak reset is justified by the restricted path/tree results.

## The natural general-metric estimate

Let $P_r$ be the largest number of cities with pairwise distances greater than $r$. Let $N_r$ count the nonclosing nearest-neighbor steps with distance greater than $r$.

The origins of those steps, together with the final city, form an $r$-separated set: at each such departure, every later city is still unvisited and therefore farther than $r$. Consequently

$$
N_r\leq P_r-1.
$$

By the layer-cake identity and the diameter bound on the closing edge,

$$
NN\leq D+\int_0^\infty(P_r-1)\,dr.
\tag{1}
$$

This is a valid estimate for every metric. A tempting extension of the source paper's clustering proof is to establish a uniformly integrable expected packing bound on every sparse exponential metric and apply (1). The required integrability is false, even on paths.

## Exact renewal obstruction on exponential paths

Place path vertices $0,1,\ldots,n-1$ on the line, beginning at coordinate zero, with independent $\operatorname{Exp}(1)$ successive gaps. These are the first $n-1$ arrivals of a rate-one Poisson process, together with its starting point.

Build an $r$-separated subset greedily: accept the starting point, then the first subsequent arrival more than $r$ to its right, and repeat. The number of city indices consumed between consecutive accepted points is

$$
D_j=1+\operatorname{Poisson}(r).
$$

The $D_j$ are independent: after an accepted arrival, the Poisson process has fresh independent increments; wait time $r$, count the arrivals in that interval, and accept the next arrival. All future increments after this next arrival are again fresh. This follows directly from independent exponential interarrival times and memorylessness.

Let $S_j=\sum_{i=1}^jD_i$, and $M=\min\{j:S_j\geq n\}$. The accepted indices within $0,\ldots,n-1$ are $S_0=0,S_1,\ldots,S_{M-1}$, so their number is $M$. Since each increment is at least one, $M\leq n$. In particular, all expectations below are finite.

Expanding the stopped sum proves the elementary Wald identity without a limiting argument:

$$
\mathbb E[S_M]
=\sum_{j=1}^n\mathbb E[\mathbf1\{M\geq j\}D_j]
=(r+1)\sum_{j=1}^n\Pr(M\geq j)
=(r+1)\mathbb E[M].
$$

The indicator depends only on previous increments and is independent of $D_j$. Since $S_M\geq n$ and the accepted points are an $r$-packing,

$$
\mathbb E[P_r]\geq\mathbb E[M]\geq\frac n{r+1}.
\tag{2}
$$

An explicit finite formula, if needed for a bounded numerical evaluation, is

$$
\mathbb E[M]
=1+\sum_{j=1}^{n-1}
e^{-jr}\sum_{h=0}^{n-1-j}\frac{(jr)^h}{h!}.
$$

No simulation is needed for (2).

## Why the route cannot finish Q3817

On these paths $\mathbb E[D]=n-1$. Integrating (2) only over $0\leq r\leq n-1$ already gives

$$
\mathbb E\left[D+\int_0^\infty(P_r-1)dr\right]
\geq(n-1)+\int_0^{n-1}\left(\frac n{r+1}-1\right)dr
=n\log n.
\tag{3}
$$

Thus the right side of (1) cannot provide an $O(n)$ expected-cost ceiling uniformly over sparse graphs. This contrasts with $\mathbb E[NN]\leq3(n-1)$ from the deterministic path theorem.

The failure also applies directly to the expected-ratio use of this bound. The upper-bound expression in (1) is homogeneous in the path weights. Its normalized value is independent of their total, by the [Gamma/Dirichlet factorization](RESULT.md#5-an-exact-exponential-normalization-identity-on-trees). Therefore its expected value after division by $OPT=2W$ is at least

$$
\frac{n\log n}{2(n-1)},
$$

which grows without bound. The expression is finite for each $n$: $P_r-1\leq(n-1)\mathbf1\{D>r\}$ bounds its integral by $(n-1)D$.

This shows where the proposed general proof loses the path cancellation. Large-step origins are packed, but most possible packed sets never occur as nearest-neighbor departure sets. A successful extension needs an NN-dependent estimate, such as a charge to deferred frontier edges, rather than a bound on all separated sets.

## Source and scope

The starting method is motivated by the clustering/binned-edge analysis in Klootwijk and Manthey, §§3.2 and 4.2; the arbitrary-sparse extension is posed in §6. [Original paper](https://doi.org/10.1007/s00453-023-01167-3). The obstruction above is derived here using the named path family. The source's fast-growing-cut theorem remains valid within its own scope.

**Next independent route:** analyze the conditional residual weights of deferred frontier edges, or find a cyclic generating family that makes NN-specific cancellations fail. This note records one failed full-scope solve attempt, while retaining the proved restricted baselines separately.
