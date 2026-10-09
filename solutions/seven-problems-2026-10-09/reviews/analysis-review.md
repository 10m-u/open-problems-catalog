# Independent internal review: Q3286 and Q3287

Date: 2026-10-09. Reviewer: a separate AI research agent from the author of the analysis report. This is an internal mathematical audit, not external peer review, formal verification, or a historical-priority determination.

**Verdict: the affirmative proof proposals are mathematically supported, subject to the explicitly stated dependence on Sun's fixed-parameter coefficient formula.** Both results concern fixed dimension $d\ge2$, with $n\to\infty$ before the parameter limit. They do not assert interchange of these limits or uniformity in dimension.

## Source alignment

The reviewer independently inspected the thesis text at Theorem 4.8 (printed pages 72–73), Remark 4.10 (page 73), and Remark D.6 (page 263), and visually inspected the rendered page 72. The source uses the rising factorial $a^{\overline d}$, not $a^d$. The mean coefficient and all three variance coefficients in equations (1)–(2) of the report agree after dividing by the mean coefficient. The counted variable is the number $R_n$ of records set, not the number $r_n$ of records remaining.

The full source URL is [Ao Sun, *Studies in Multivariate Pareto Records*](https://jscholarship.library.jhu.edu/server/api/core/bitstreams/7ca48c8a-5406-49b2-979f-adf49c725f4d/content). The public PDF was available in the current research workspace. One later web-reader fetch returned 403; that failure was not used as evidence about the paper's contents.

## Checks of the analytic argument

1. **The positive kernels.** Direct integration of the definitions gives both closed forms (7). Integration by parts gives
   $G_A=D^{-b}-A^{-b}+h(I_A^{\rm old}-I_A^{\rm new})$
   and the analogous expression for $G_B$. The integral differences are nonpositive; together with positivity from the definitions this proves $0\le G_A,G_B\le bcz$. The factors multiplying $h$ are bounded as $b\uparrow1$ at every fixed interior $(c,z)$.

2. **Radial and time variables.** For the region $x=t+\theta\le y=t+\eta$, the substitution $x=sy$, $t=rsy$ has Jacobian $sy^2$. The radial exponent is $d+2a-2=\delta+a-1$, and the $s$ exponent before applying the kernel is $a+p-1$. Integration in the radial variable gives $\Gamma(1+b)/\delta$. The substitution $v=uw$ gives the factor $\int_0^1u^{-b}\,du=1/(1-b)$. After normalizing by $(d-1)/\Gamma(b)$, the remaining factor is $b$. Dividing by $s^\delta$ in $G_A$ gives $s^{-q}$ exactly. The opposite ordering gives the second line of (8), with exponent $a+q-1$ and kernel $G_B$. The derivation of (9) for $J_2$ has the same radial power and gives $x^{-d}G_A$, as stated.

3. **The small-parameter estimates.** Bound (11) integrates the nonnegative majorants with exponents $\delta$ in $r$, and respectively $\delta-q$ and $a+q+\delta-1$ in $s$. Their denominators are those displayed. In (12), the inequalities $1-x^a\le a(-\log x)$ and $(1-x)^{d-1}\le1-x^{d-1}$ give an integrable majorant even when $d=2$. In (13), the linear Taylor contribution cancels the beta integral exactly to $2b$. The quadratic remainder integrates to the rising-factorial denominator $(2a+d-1)_d$. Thus $T_1,T_2,2b-T_3$ are all $O_d(a^2)$, and the claimed derivative at zero follows.

4. **Large-parameter cancellation.** The substitutions $x=e^{-t/\delta}$ give the powers $e^{-bt}$ in $T_2$ and $e^{ht}$ in $T_3$. Each normalized integrand is bounded by $t^{d-1}e^{-t/2}$ for $a\ge d-1$. Both limits are the same Fermi-type integral, so the cancellation is justified separately, without subtracting divergent quantities.

5. **The double-integral limit.** In (8), the substitutions $r=e^{-R/\delta}$ and $s=e^{-S/\delta}$ give a total factor $\delta^{-d}$. The first Jacobian-adjusted exponential is $e^{-R/\delta}e^{(q-1)S/\delta}$, while the second contains $e^{-R/\delta}e^{-(a+q)S/\delta}$. The stated polynomial times $e^{-R-S/2}$ majorants control both. The factor $P/\delta^d$ tends to one.

6. **Symmetry and constants.** Relabeling $p,q$ in the second sum is legitimate because the combinatorial coefficients are symmetric. The factor $1+e^{-S}$ then cancels exactly from the kernel. The change $x=R$, $y=R+S$ maps to the half-plane $x<y$ with unit Jacobian; symmetry of the entire weighted sum accounts for the factor of two. Direct integration in one variable gives $x/(e^x-1)$, hence $C_2=1+\pi^2/3$ and $C_3=1+12\zeta(3)$. The positive integrands give $C_d>1$, and the displayed exponential majorant proves finiteness.

## Correction made during review

The first draft omitted the plus sign preceding each $h$-weighted integral in (4). Those two typographical omissions were reported to the author and corrected. The intended additive expression was already used in the subsequent inequality, but the displayed identities needed the correction.

No unresolved mathematical gap was found in the endpoint-limit arguments after that correction. The diagnostic quadrature is not used to justify positivity, infinite-dimensional integration, or an interchange of limits. The imported fixed-$a,d$ asymptotic identity remains the explicit external dependency.
