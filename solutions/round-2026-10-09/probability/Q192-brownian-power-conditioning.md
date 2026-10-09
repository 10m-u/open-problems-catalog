# Q192: concentration under a single high-order Brownian constraint

**Status:** complete proof of the statement recorded as Q192, subject to independent mathematical review. This is a proof submitted in this research round, not a claim of publication or established novelty. It does not settle the full-signature conjecture Q191 or the comparison conjecture Q193.

## Exact source and scope

Karen Habermann, *Geometry of sub-Riemannian diffusion processes*, Cambridge PhD thesis (listed as 2018; cover dated August 2017), printed page 84, Lemma 4.2.2 and Conjecture 4.2.3:

- [Primary thesis, PDF](https://api.repository.cam.ac.uk/server/api/core/bitstreams/23395d65-5112-4485-95e9-0fb3ad75f796/content).
- [Author's publication list](https://warwick.ac.uk/fac/sci/statistics/staff/academic-research/habermann/publications/), checked 9 October 2026; the page includes work through September 2026.
- [The 2021 iterated-Kolmogorov-loop paper](https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/jlms.12384), especially Theorem 1.4 and the subsequent discussion. Its Gaussian time-integral constraints differ from the single power-integral constraint here, and it reiterates the separate full-signature conjecture.

The exact thesis page was checked in both extracted text and its page image. Its reference law is ordinary one-dimensional Brownian motion starting at zero, **not** a Brownian bridge. Lemma 4.2.2 gives the reweighting used below. Searches for the conjecture number, author, and power/signature-conditioning terminology located no resolution of this precise statement. That search is not a proof of novelty. No prior proof for Q192 was found in the repository's existing solution reports at base commit `8967f4f70776856b3dfc0b2494ed73167b15ee0c`.

Let $B,W$ be independent standard real Brownian motions on $[0,1]$. For an integer $m\geq1$, put

$$
Y_m=\int_0^1 B_t^m\circ dW_t,
\qquad V_m(B)=\int_0^1|B_t|^{2m}\,dt,
\qquad w_m(B)=V_m(B)^{-1/2}.
$$

Let $\mu_m$ be the canonical conditional law of $B$ given $Y_m=0$. The catalog uses $m=N-1$. The assertion is

$$
\mu_m\Longrightarrow\delta_0
\quad\text{on }C_0([0,1],\mathbb R)
\quad(m\longrightarrow\infty),
$$

where the topology is the uniform topology.

## Theorem and proof

Write $M=\|B\|_\infty$. There is a random variable $K\geq0$ with $\mathbb E K^2<\infty$ such that

$$
|B_t-B_s|\leq K|t-s|^{1/4}\quad(0\leq s,t\leq1).
\tag{1}
$$

For every $\varepsilon>0$, the conditional laws satisfy the explicit bound

$$
\mu_m\{M\geq\varepsilon\}
\leq
\frac{4\mathbb E K^2}
{\varepsilon^2\,\mathbb P(M\leq\varepsilon/4)}\,2^{-m}.
\tag{2}
$$

The denominator in (2) is positive and independent of $m$; hence the desired weak convergence follows.

### 1. The conditional density is well-defined

Since $B$ and $W$ are independent, the quadratic covariation of (B^m) and $W$ is zero. Thus the Stratonovich integral equals the Itô integral. Conditional on the whole path of $B$, $Y_m$ is centered Gaussian with variance $V_m(B)$. Consequently the canonical conditional law at zero is

$$
\mu_m(dB)=\frac{w_m(B)}{Z_m}\,\mathbb P(dB),
\qquad Z_m=\mathbb E w_m(B).
\tag{3}
$$

Here $0<Z_m<\infty$. Positivity is immediate because Brownian motion is not the zero path almost surely. For finiteness, monotonicity of Lebesgue norms on the unit interval gives

$$
w_m(B)=\|B\|_{2m}^{-m}\leq\|B\|_2^{-m}.
$$

Choose an integer $d>m$, partition $[0,1]$ into $d$ equal intervals $I_j$, and put $G_j=\sqrt d\int_{I_j}B_t\,dt$. The functions $\sqrt d\mathbf1_{I_j}$ are orthonormal in (L^2[0,1]), so Bessel's inequality gives

$$
\|B\|_2^2\geq\sum_{j=1}^{d}G_j^2.
$$

The Gaussian vector $G$ is nondegenerate. Indeed, for a nonzero step function $f=\sqrt d\sum c_j\mathbf1_{I_j}$, stochastic Fubini gives

$$
\operatorname{Var}\left(\int_0^1f(t)B_t\,dt\right)
=\int_0^1\left(\int_s^1f(t)\,dt\right)^2ds>0.
$$

If this integral vanished, the continuous primitive would vanish everywhere, and its almost-everywhere derivative would force $f=0$, a contradiction. A nondegenerate $d$-dimensional Gaussian density is bounded. Integrating $\|x\|^{-m}$ over the unit ball is finite when $d>m$, and outside that ball the integrand is at most one. Therefore $\mathbb E\|G\|^{-m}<\infty$, proving $Z_m<\infty$.

This also resolves the conditioning-at-a-null-event issue. Conditional Gaussian densities at $y$ are bounded by $(2\pi)^{-1/2}w_m(B)$. Dominated convergence therefore makes the normalized disintegration continuous in total variation at $y=0$, and conditioning on shrinking intervals around zero yields (3). No arbitrary version of a regular conditional distribution is being chosen.

### 2. A deterministic peak bound

Let $f(0)=0$ be continuous and satisfy $|f(t)-f(s)|\leq K|t-s|^{1/4}$. Suppose $\|f\|_\infty\geq\varepsilon>0$. Then $K\geq\varepsilon$. At a point $t_0$ where the absolute maximum is attained, set

$$
\delta=\left(\frac{\varepsilon}{2K}\right)^4\leq1.
$$

The interval $J=[t_0-\delta,t_0+\delta]\cap[0,1]$ has length at least $\delta$. For $t\in J$,

$$
|f(t)|\geq|f(t_0)|-K\delta^{1/4}\geq\varepsilon/2.
$$

Thus

$$
\left(\int_0^1|f(t)|^{2m}dt\right)^{-1/2}
\leq
\left(\frac2\varepsilon\right)^m
\left(\frac{2K}\varepsilon\right)^2.
\tag{4}
$$

Applying (4) pathwise gives the numerator estimate

$$
\mathbb E\bigl[w_m(B)\mathbf1_{\{M\geq\varepsilon\}}\bigr]
\leq\frac{4\mathbb E K^2}{\varepsilon^2}
\left(\frac2\varepsilon\right)^m.
\tag{5}
$$

### 3. A fixed small ball bounds the normalizer from below

For any $a>0$, on $\{M\leq a\}$ we have $V_m(B)\leq a^{2m}$. Hence

$$
Z_m\geq a^{-m}\mathbb P(M\leq a).
\tag{6}
$$

Every Brownian uniform small ball has positive probability. One elementary justification uses the orthogonal decomposition of Brownian motion into its values on a finite grid and the independent Brownian bridges between grid points. A sufficiently fine grid has positive probability of lying inside $(-a/2,a/2)$; each intervening bridge has positive probability of staying within distance $a/2$ of zero. The latter follows, for example, by writing a bridge on $[0,h]$ as $W_t-(t/h)W_h$ and applying the Brownian reflection bound on a sufficiently short interval. There are finitely many grid intervals, so the intersection has positive probability.

Dividing (5) by (6), with $a=\varepsilon/4$, proves (2). For a bounded continuous functional $F$, continuity at zero bounds $|F(B)-F(0)|$ on a sufficiently small uniform ball; its complement contributes at most $2\|F\|_\infty\mu_m(M\geq\varepsilon)$. Therefore $\int F\,d\mu_m\to F(0)$. This directly proves weak convergence; a separate tightness argument is unnecessary. ∎

## Elementary justification of the Hölder moment

The standard Brownian Hölder estimate in (1) can also be obtained without appealing to a qualitative version of Kolmogorov's theorem. Let

$$
A_k=\max_{0\leq j<2^k}
|B_{(j+1)2^{-k}}-B_{j2^{-k}}|,
\qquad S=\sum_{k\geq0}2^{k/4}A_k.
$$

Since a standard normal has eighth moment 105,

$$
\|A_k\|_2\leq\|A_k\|_8
\leq\left(2^k\cdot105\cdot2^{-4k}\right)^{1/8}
=105^{1/8}2^{-3k/8}.
$$

Minkowski's inequality implies $\|S\|_2\leq105^{1/8}\sum_{k\geq0}2^{-k/8}<\infty$. Dyadic approximation of two points with $2^{-(l+1)}<|t-s|\leq2^{-l}$ gives

$$
|B_t-B_s|\leq A_l+2\sum_{k>l}A_k
\leq2S\,2^{-l/4}
\leq 2^{5/4}S|t-s|^{1/4}.
$$

Thus $K=2^{5/4}S$ satisfies (1) and has finite second moment. This also covers points at grid boundaries by continuity.

## Strength and limitations

The choice $a=\varepsilon/4$ is convenient, not optimal. For every fixed $R>1$, taking $a=\varepsilon/(2R)$ gives

$$
\mu_m(M\geq\varepsilon)
\leq \frac{4\mathbb E K^2}
{\varepsilon^2\mathbb P(M\leq\varepsilon/(2R))}R^{-m}.
$$

Thus every fixed-radius escape probability decays faster than any prescribed exponential in $m$. No claim about the sharp shrinking-radius scale or limiting rescaled process is needed for Q192.

The proof uses the single-constraint density in (3). It does **not** assert that conditioning on additional signature coordinates can only increase concentration. That is precisely the distinct comparison issue separating this result from Q191.

## Reproducible verification

`verify_probability.py` checks the deterministic peak inequality on exact rational piecewise-linear paths, using exact integration of their even powers. These checks catch sign, exponent, endpoint, and normalization mistakes in the crucial inequality; they are not a substitute for the all-path proof or a simulation of conditional Brownian motion.
