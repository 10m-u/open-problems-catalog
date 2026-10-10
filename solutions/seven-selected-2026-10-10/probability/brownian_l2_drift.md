# Brownian motion under an L² budget: subcritical and critical drifts

**Catalog problems:** 3982 and 3983.

**Date:** 2026-10-10.

**Result:** proposed complete proofs, submitted for mathematical review.
**Source:** Aurzada, Dutta and Wiegand, [arXiv:2610.12354v1](https://arxiv.org/html/2610.12354v1), §1.1. The source's Theorem 1 assumes a power bound on the squared drift with exponent below 1/2; §1.1 asks about the larger subcritical range and the critical square-root range. The argument below retains the squared drift in the saddle exponent. Its analytic conclusions are proved here, rather than attributed to the source.

## 1. The two conclusions

Fix a starting point $x\in\mathbb R$ and a budget parameter $\theta>0$.
For each $T$, put

$$
W_t^{(T)}=x+B_t+\mu_Tt,
\qquad
Q_T=\mathcal L\left(W^{(T)}\,\middle|\,
          \int_0^T(W_s^{(T)})^2\,ds\leq\theta T\right),
$$

where $B$ is standard Brownian motion and $\mu_T$ is deterministic.

**Theorem.** Suppose $\mu_T^2/T\longrightarrow r\in[0,\infty)$.
Let $\lambda_r$ be the unique positive solution of

$$
\boxed{\quad 2\theta\lambda_r^3-\lambda_r^2-r=0.\quad}                 \tag{1}
$$

For every finite $t$, the restrictions of $Q_T$ to $C([0,t])$ converge in
total variation to the law of

$$
dX_s=dB_s-\lambda_rX_s\,ds,\qquad X_0=x.                            \tag{2}
$$

Consequently $Q_T$ converges weakly to this law on $C([0,\infty))$ with
the topology of uniform convergence on compact intervals.

This resolves the two catalog statements as follows.

* **3982:** $\mu_T^2=o(T)$ means $r=0$, so
  $\lambda_0=1/(2\theta)$, exactly the parameter in the question.
* **3983:** $\mu_T\sim c\sqrt T$, with $c\ne0$, means $r=c^2$.
  The limit is the Ornstein–Uhlenbeck law (2), with the parameter in (1).
  In particular $\lambda_{c^2}>1/(2\theta)$. The limit depends on $c^2$,
  so changing the sign of the critical drift does not change it.

Existence and uniqueness in (1) follow directly from

$$
\theta=\frac1{2\lambda}+\frac{r}{2\lambda^3}:                         \tag{3}
$$

the right side is strictly decreasing from infinity to zero on
$(0,\infty)$. This also proves continuity of $r\mapsto\lambda_r$.

## 2. Eliminate the original drift exactly

Write $P_x$ for driftless Brownian motion started at $x$, and write $W$
for its canonical coordinate process. Set

$$
A_t=\int_0^tW_s^2\,ds.
$$

For events measurable through time $T$, the Cameron–Martin density of
drift $\mu_T$ is
$\exp\{\mu_T(W_T-x)-\mu_T^2T/2\}$.
Its deterministic factor cancels on conditioning. Therefore, for
$0\leq t<T$,

$$
\frac{d(Q_T|_{\mathcal F_t})}{d(P_x|_{\mathcal F_t})}
=\frac{F_{T-t}(W_t,\mu_T;\theta T-A_t)}
       {F_T(x,\mu_T;\theta T)},                                    \tag{4}
$$

where, for driftless Brownian motion $Y$ started at $y$,

$$
F_L(y,m;b)=E_y\!\left[e^{mY_L}
       \mathbf1_{\{\int_0^LY_s^2ds\leq b\}}\right],                 \tag{5}
$$

with $F_L=0$ for $b\leq0$. The denominator in (4) is positive: Brownian
motion has positive probability to follow a continuous path which moves
from $x$ to zero sufficiently rapidly and then remains sufficiently
close to zero. Such a path can have squared integral below $\theta T$.

Thus it suffices to obtain a ratio asymptotic for (5). The value of $m$
in the numerator remains $\mu_T$; it is not replaced by $\mu_{T-t}$.

## 3. Exact transform

For $\Re s>0$, put $g=g(s)=\sqrt{2s}$, using the branch with positive
real part. The endpoint-tilted transform is

$$
M_L(y,m;s)
=E_y\exp\left\{-s\int_0^LY_u^2du+mY_L\right\}
=\frac1{\sqrt{\cosh(gL)}}
  \exp\left\{-\frac{gy^2}{2}\tanh(gL)
       +\frac{my}{\cosh(gL)}
       +\frac{m^2}{2g}\tanh(gL)\right\}.                            \tag{6}
$$

For completeness, for real $s>0$ use the ansatz
$M=\exp\{-q(L)y^2/2+\ell(L)y+c(L)\}$ in

$$
\partial_LM=\tfrac12\partial_{yy}M-sy^2M,\qquad M_0=e^{my}.
$$

It gives

$$
q'=2s-q^2,\quad \ell'=-q\ell,\quad
c'=\tfrac12(\ell^2-q),\qquad(q(0),\ell(0),c(0))=(0,m,0).
$$

The solutions are $q=g\tanh(gL)$,
$\ell=m/\cosh(gL)$, and
$c=-\tfrac12\log\cosh(gL)+m^2\tanh(gL)/(2g)$.
Feynman–Kac proves (6) for real $s>0$; analytic continuation proves it
on the right half-plane. The expectation is analytic there by dominated
convergence on closed sub-half-planes, using
$E_y e^{mY_L}<\infty$. The square root of $\cosh$ is the analytic branch
positive on the positive real axis.

The weighted distribution in (5) has no atoms. Indeed, condition on the
Brownian bridge in $Y_u=y+(u/L)B_L+\beta_u$. Its squared integral is a
strictly convex quadratic polynomial in the independent Gaussian
variable $B_L$. A fixed value has at most two preimages.

Laplace inversion therefore gives, for $b>0$ and $s_0>0$,

$$
F_L(y,m;b)=\frac1{2\pi i}
       \int_{s_0-i\infty}^{s_0+i\infty}
          \frac{e^{bs}M_L(y,m;s)}s\,ds.                             \tag{7}
$$

Absolute integrability on the contours used below follows from the
explicit estimates in the next section. Formula (6) is also obtainable
from the source's displayed transform in §2 by cancelling the
Cameron–Martin factor.

## 4. A uniform saddle lemma

The following lemma is the needed extension beyond a perturbatively
small squared drift.

**Lemma.** Fix $\theta>0$ and $R<\infty$. Let $m_T$ be any real sequence
with $r_T=m_T^2/T\in[0,R]$. Put

$$
\lambda_T=\lambda_{r_T},\quad s_T=\lambda_T^2/2,
\quad h_T(s)=\theta s-\frac{g(s)}2+\frac{r_T}{2g(s)},
$$

and

$$
v_T=h_T''(s_T)=\frac1{2\lambda_T^3}
                   +\frac{3r_T}{2\lambda_T^5}>0,
\qquad
K_T=\frac{e^{T h_T(s_T)}}{s_T\sqrt{\pi T v_T}}.                     \tag{8}
$$

For fixed $t\geq0$, $y\in\mathbb R$ and $a\in\mathbb R$,

$$
F_{T-t}(y,m_T;\theta T-a)
=K_T\exp\left\{\frac{t\lambda_T}{2}-a s_T
                         -\frac{\lambda_Ty^2}{2}\right\}(1+o(1)).  \tag{9}
$$

The error is uniform for $r_T\in[0,R]$ and for $(t,y,a)$ in any fixed
compact set with $t\geq0$.

### Proof: the moving saddle and its whole contour

Equation (3) gives $h_T'(s_T)=0$. Because $r_T\in[0,R]$, there are
constants $0<\lambda_-\leq\lambda_+<\infty$ such that
$\lambda_-\leq\lambda_T\leq\lambda_+$. Also $v_T$ is bounded above
and away from zero.

On $s=s_T+iu$, write $g(s)=\alpha+i\beta$. Then

$$
\alpha^2-\beta^2=\lambda_T^2,\quad
\alpha\beta=u,\quad
\alpha\geq\lambda_T,\quad
|g|\leq\sqrt2\alpha,
\quad
\Re\frac1g=\frac\alpha{\alpha^2+\beta^2}
                     \leq\frac1{\lambda_T}.                       \tag{10}
$$

Consequently

$$
\Re[h_T(s_T+iu)-h_T(s_T)]
=-\frac{\alpha-\lambda_T}{2}
  +\frac{r_T}{2}\left(\frac\alpha{\alpha^2+\beta^2}
                                  -\frac1{\lambda_T}\right)
\leq-\frac{\alpha-\lambda_T}{2}.                                 \tag{11}
$$

This is a bound along the entire vertical contour, not only a local
Taylor estimate. For uniform constants $c_1,c_2>0$,

$$
\alpha-\lambda_T\geq c_1u^2\quad(|u|\leq1),\qquad
\alpha-\lambda_T\geq c_2\sqrt{|u|}\quad(|u|\geq1).                 \tag{12}
$$

To check (12), use

$$
\alpha^2=\frac{\lambda_T^2+\sqrt{\lambda_T^4+4u^2}}2,
\qquad
\alpha-\lambda_T
=\frac{2u^2}
 {(\alpha+\lambda_T)(\sqrt{\lambda_T^4+4u^2}+\lambda_T^2)}.
$$

On $|u|\leq1$ the denominator has a uniform finite upper bound. On
$|u|\geq1$ the ratio $(\alpha-\lambda_T)/\sqrt{|u|}$ is positive,
continuous for $\lambda_T\in[\lambda_-,\lambda_+]$, and tends
uniformly to one as $|u|\to\infty$.

### Proof: the exact transform has a uniformly negligible correction

Set $L=T-t$ and $q=e^{-2gL}$. Rewriting (6) gives

$$
M_L(y,m_T;s)
=\sqrt2\exp\left\{-\frac{Lg}{2}-\frac{gy^2}{2}
                               +\frac{m_T^2}{2g}\right\}E_T(s),   \tag{13}
$$

where

$$
E_T(s)=(1+q)^{-1/2}
 \exp\left\{\left(gy^2-\frac{m_T^2}{g}\right)\frac q{1+q}
                +\frac{2m_Ty e^{-gL}}{1+q}\right\}.               \tag{14}
$$

For bounded $t,y$, equations (10), $m_T^2\leq RT$, and
$|1+q|\geq1-e^{-2\lambda_-L}$ show

$$
\sup_{u\in\mathbb R}|E_T(s_T+iu)-1|
                   \leq C(1+T)e^{-cT}=:\varepsilon_T.              \tag{15}
$$

For the only apparently unbounded factor in this estimate, use
$|g|e^{-2\alpha L}\leq\sqrt2\alpha e^{-2\alpha L}$ and maximize
over $\alpha\geq\lambda_-$. Its maximum is at $\lambda_-$ once
$L\geq1/(2\lambda_-)$.

Substitution into (7) leaves the principal integral

$$
\frac{\sqrt2}{2\pi}\int_{\mathbb R}
 e^{T h_T(s_T+iu)}b_T(s_T+iu)\,du,
\qquad
b_T(s)=\frac1s
   \exp\left\{\frac{tg(s)}2-as-\frac{g(s)y^2}2\right\}.            \tag{16}
$$

For bounded $(t,y,a)$, its integrand, divided by $e^{T h_T(s_T)}$,
is in absolute value at most

$$
C\exp\left\{-\frac{T-t}{2}(\alpha-\lambda_T)\right\}.             \tag{17}
$$

Indeed $|s|^{-1}\leq s_T^{-1}$; the factor $e^{-as}$ has constant
modulus on the contour; the $y^2$ term can only improve the bound; and
$e^{t\alpha/2}$ is absorbed as displayed. By (12), the integral of
(17) is $O(T^{-1/2})$. Therefore replacing $E_T$ by one in (16) has
absolute error
$O(\varepsilon_T e^{T h_T(s_T)}T^{-1/2})$.

### Proof: local evaluation and exclusion of all other frequencies

Take $\delta_T=T^{-2/5}$. All derivatives needed for Taylor expansion
are bounded uniformly on a fixed neighborhood of the real compact
interval containing the $s_T$. Hence, uniformly for $|u|\leq\delta_T$,

$$
h_T(s_T+iu)
=h_T(s_T)-\tfrac12v_Tu^2+O(|u|^3),
\qquad b_T(s_T+iu)=b_T(s_T)(1+O(|u|)).                              \tag{18}
$$

Here $T\delta_T^3=T^{-1/5}\to0$ and
$\sqrt T\delta_T=T^{1/10}\to\infty$. The contribution of this
interval to (16) is thus

$$
\frac{\sqrt2}{2\pi}
 e^{T h_T(s_T)}b_T(s_T)
 \sqrt{\frac{2\pi}{T v_T}}(1+o(1))
=K_T e^{t\lambda_T/2-a s_T-\lambda_Ty^2/2}(1+o(1)).               \tag{19}
$$

For $\delta_T<|u|\leq1$, equations (12) and (17) bound the absolute
integral by $C e^{-cT^{1/5}}$. For $|u|\geq1$, substitution
$z=\sqrt{|u|}$ in the same bounds gives $O(e^{-cT})$.
Both estimates are after division by $e^{T h_T(s_T)}$ and both are
$o(T^{-1/2})$. Together with (15), they prove (9). All constants used
are uniform on the compact parameter sets asserted in the lemma. ∎

## 5. The path limit

Return to $m_T=\mu_T$ with $r_T\to r$. A fixed continuous sample path
has finite $W_t$ and $A_t$. Apply (9) to the numerator of (4), with
$y=W_t$ and $a=A_t$, and to its denominator with $t=0$, $y=x$, $a=0$.
The same $K_T$ cancels. Since $\lambda_T\to\lambda_r$, the density
in (4) converges $P_x$-almost surely to

$$
D_t=\exp\left\{\frac{\lambda_rt}{2}
       -\frac{\lambda_r(W_t^2-x^2)}2
       -\frac{\lambda_r^2}{2}\int_0^tW_s^2ds\right\}.              \tag{20}
$$

For all sufficiently large $T$, $\theta T-A_t>0$ on each fixed path,
so the convention for nonpositive budgets causes no issue.

The function (20) is the density of the Ornstein–Uhlenbeck law (2)
relative to Brownian motion through time $t$. One can verify that it
has expectation one without a Novikov assumption. Set
$h(y)=e^{-\lambda_ry^2/2}$ and $s_r=\lambda_r^2/2$. Direct
differentiation gives

$$
\left(\tfrac12\partial_{yy}-s_ry^2\right)h
=-\tfrac{\lambda_r}{2}h.
$$

Itô's formula then makes
$e^{\lambda_rs/2-s_r A_s}h(W_s)/h(x)$ a local martingale. On every
bounded time interval it is bounded by
$\exp\{\lambda_rt/2+\lambda_rx^2/2\}$, hence is a true martingale.
Its change of measure has generator
$\tfrac12\partial_{yy}-\lambda_ry\partial_y$, which proves the
identification and $E_xD_t=1$.

Each density in (4) is nonnegative and integrates to one. Scheffé's
lemma applied to its pointwise limit (20) proves the asserted total
variation convergence on $C([0,t])$.

To pass to $C([0,\infty))$, use the metric

$$
d(f,g)=\sum_{j\geq1}2^{-j}
             \left(1\wedge\|f-g\|_{[0,j]}\right).
$$

Let $E_jf$ agree with $f$ through time $j$ and be constant afterwards.
Then $d(f,E_jf)\leq2^{-j}$. For any bounded Lipschitz test function,
replace each path by $E_jf$, use total variation convergence on
$[0,j]$, and then send $j\to\infty$. Convergence for bounded
Lipschitz functions gives weak convergence in this metric. This proves
the theorem. ∎

## 6. Interpretation and precise scope

At critical scale the limiting stationary variance is
$1/(2\lambda_{c^2})<\theta$. Equation (3) decomposes the prescribed
budget as

$$
\theta=\frac1{2\lambda_{c^2}}
             +\frac{c^2}{2\lambda_{c^2}^3}.
$$

This identity is consistent with a terminal boundary layer consuming
part of the budget. That interpretation is not needed in the proof;
the fixed-time path limit follows from (4)–(20).

The theorem requires only convergence of $\mu_T^2/T$, not of the
signed quantity $\mu_T/\sqrt T$. It therefore also covers drifts whose
sign oscillates while their squared magnitude has a limit.

No conclusion here is asserted for $\mu_T^2/T\to\infty$, for a
time-dependent drift within a single path, or for intervals reaching
the conditioning endpoint $T$. The result uses the deterministic
threshold in the catalog questions.

## 7. Reproduction and evidence boundaries

Run from the repository root:

```sh
python solutions/seven-selected-2026-10-10/probability/verify_brownian.py
python solutions/seven-selected-2026-10-10/probability/verify_brownian.py --numeric
```

The first command uses only Python's standard library. It checks the
saddle coefficients, positivity identities and contour inequalities
using exact rational arithmetic. The second additionally requires
NumPy and SciPy; it independently compares (6) against a truncated
Karhunen–Loève Gaussian product and numerically inverts the exact
transform to check the density ratio in subcritical and critical
regimes. Numerical checks detect coefficient and implementation errors;
they do not establish the asymptotic theorem. Sections 2–5 supply the
proof for all the parameters claimed.

The bounded literature check and source locations are recorded in
[sources.json](sources.json). The source's arXiv version history and
author publication list were checked on 2026-10-10. No resolution of
these two extensions was found in that bounded check. This is not a
claim of an exhaustive literature search or of external peer review.
