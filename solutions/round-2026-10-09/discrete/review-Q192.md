# Independent review of Q192

Date: 2026-10-09. Reviewer: the discrete-mathematics research agent, independently of the probability author.

**Verdict:** accept the mathematical proof at the precise scope of Habermann's Conjecture 4.2.3 and catalog Q192. No substantive gap was found. This is an internal independent review, not external peer review or a priority certification.

Reviewed file: [Q192-brownian-power-conditioning.md](../probability/Q192-brownian-power-conditioning.md).

## Primary-source alignment

The reviewer separately opened [Habermann's primary thesis PDF](https://api.repository.cam.ac.uk/server/api/core/bitstreams/23395d65-5112-4485-95e9-0fb3ad75f796/content), reading printed pp. 82–84. Page 82 defines the laws $Q_N^y$ by disintegrating ordinary Wiener measure against the single stochastic integral. Page 84, Lemma 4.2.2, gives its first-marginal density, with variance $\int_0^1v_t^{2(N-1)}\,dt$. Conjecture 4.2.3 asks for weak convergence of that first marginal at $y=0$ to the zero path. There is no endpoint bridge condition in this law. The proposed substitution $m=N-1$ is correct. The review does not extend to the separate full-signature law or its comparison conjectures.

## Normalization and conditional density

Given the first Brownian path, the independent stochastic integral is Gaussian with the claimed variance. The Itô and Stratonovich versions agree because independent Brownian coordinates have zero cross-variation.

The finiteness argument for
$$
Z_m=\mathbb E\left(\int_0^1|B_t|^{2m}dt\right)^{-1/2}
$$
is valid. On a measure-one time interval, $\|B\|_{2m}\ge\|B\|_2$, so the density is bounded above by $\|B\|_2^{-m}$. Projecting onto $d>m$ orthonormal interval-indicator functions bounds this in turn by the inverse $m$-th power of a nondegenerate $d$-dimensional Gaussian norm. Its density is bounded near zero, and $\int_0^1r^{d-1-m}\,dr<\infty$; the contribution outside the unit ball is also finite. The stochastic-Fubini variance calculation correctly proves nondegeneracy.

The author also addresses the null-event issue correctly: the pathwise Gaussian density at $y$ is dominated by its integrable value at zero. Dominated convergence yields $L^1$ convergence of unnormalized densities, and the positive normalizer then yields total-variation continuity of the normalized conditional laws. Conditioning on shrinking intervals produces the same law. This is enough to identify the canonical first-marginal disintegration.

## Deterministic peak estimate

For a path starting at zero with a $1/4$-Hölder constant $K$, $\|f\|_\infty\ge\varepsilon$ implies $K\ge\varepsilon$. Around an absolute maximizer, the clipped interval of radius $\delta=(\varepsilon/(2K))^4$ has length at least $\delta$, including when the maximum occurs at time 1. On that interval $|f|\ge\varepsilon/2$. Thus
$$
\left(\int_0^1|f|^{2m}\right)^{-1/2}
\le(2/\varepsilon)^m(2K/\varepsilon)^2.
$$
All inequality directions, powers, and endpoint cases are correct.

The bound on the weighted escape numerator follows immediately on taking expectations. The lower bound on $Z_m$ uses the separate event $\{\|B\|_\infty\le a\}$; it makes no independence assumption involving the random Hölder constant.

## Hölder moment and the escape ratio

The eighth-moment maximal-increment estimate is correct:
$$
\|A_k\|_2\le\|A_k\|_8
\le105^{1/8}2^{-3k/8}.
$$
Consequently $\sum_k2^{k/4}A_k$ converges in $L^2$. For $2^{-(l+1)}<t-s\le2^{-l}$, the left dyadic approximations at level $l$ differ by at most one level-$l$ interval, and each subsequent refinement contributes at most one increment per endpoint. This proves the displayed chaining estimate and the constant $2^{5/4}$.

Taking $a=\varepsilon/4$ makes the ratio of the exponential factors exactly $2^{-m}$. The remaining constant is finite and independent of $m$. Every fixed open neighborhood of the zero path consequently receives probability tending to one. The final bounded-continuous-functional argument correctly proves weak convergence in the uniform topology without a separate tightness argument.

The asserted stronger statement, faster than any fixed exponential at each fixed positive radius, also follows: for any fixed $R>1$, use $a=\varepsilon/(2R)$. Its prefactor may depend on $R$, as the report correctly states. No uniform claim in a shrinking radius follows automatically.

## Small-ball clarification

Positivity of Brownian uniform small balls is standard and is all the proof requires. The report's proposed elementary bridge argument can be made fully explicit as follows. Partition into $N$ intervals of length $h=1/N$. The grid values have a nondegenerate finite Gaussian density, so the event that all lie in $(-a/2,a/2)$ has positive probability. Conditional on these values, the centered bridge fluctuations are independent of them and of one another. A bridge on $[0,h]$ is
$$
\beta_t=W_t-(t/h)W_h.
$$
Its supremum is at most twice the supremum of $|W|$ on that interval. By the reflection principle and a union bound, choose $h$ small enough that
$$
\mathbb P\left(\sup_{0\le t\le h}|W_t|\ge a/4\right)
\le4\mathbb P(W_h\ge a/4)<1.
$$
Each bridge then has positive probability of staying in $(-a/2,a/2)$. The finite intersection with the grid event is a positive-probability Brownian small ball. This avoids any ambiguity from using the unit-time formula $W_t-tW_1$ on a shorter interval.

## Presentation and review limits

The initial review requested only presentation corrections: restore mathematical delimiters and a missing integral symbol, and clarify the bridge scaling. A subsequent inspection on the same date confirmed that the final integral is restored and the bridge is written as $W_t-(t/h)W_h$ on $[0,h]$. These edits do not change the result.

This review independently checked the source and all analytic steps. It did not attempt to prove historical priority or inspect all later literature. The proposed finite piecewise-linear computations are appropriate consistency controls but are not part of the justification of the Brownian theorem.
