# Research result and scope

The principal result of this continuation is a matching exponential upper and lower bound for Q3818/P5. Let $M_n$ count undirected Hamiltonian tours, identifying rotation and reversal, that have no strictly improving cycle-preserving two-edge exchange. When the edge costs of $K_n$ are independent uniform random variables on $[0,1]$, the result is

$$
\boxed{\lim_{n\to\infty}
\left(\frac{\mathbb E[M_n]}{\sqrt{n!}}\right)^{1/n}
=\rho=0.597586978551345\ldots.}
\tag{1}
$$

In particular, $\mathbb E[M_n]=O((3/5)^n\sqrt{n!})$. More precisely,

$$
\mathbb E[M_n]=\sqrt{n!}\,\exp\{n\log\rho+o(n)\}.
\tag{2}
$$

The exact definition of $\rho$, rather than its decimal evaluation, is given below. A rational certificate proves $\rho<3/5$ without relying on numerical quadrature.

This is stronger than the supplied handoff's all-size upper bound with exponential base $\sqrt\pi\,\operatorname{erfc}(1/2)=0.8498918\ldots$. It supplies a matching exponential lower bound, not just a smaller upper-bound constant. The handoff already claims Q3818/P5 locally proved; this continuation does not count that earlier closure as a new achievement. The new contribution relative to the handoff is the sharp rate and its extension to other independent edge-cost distributions.

The proof is developed in this continuation and supported by separate finite exact checks. It has not undergone external mathematical peer review or proof-assistant formalization. Originality beyond the supplied handoff is not established. The current primary sources consulted still present the earlier counting bound and conjecture [1]; that bounded literature check is not an exhaustive priority search.

The stable catalog statement is Q3818, ID `1ab793013b1b4b6d4773`. P5 is its programme counterpart. No live catalog, original attachment, or public repository was modified.

# Relation to the supplied programme and published work

The initial programme prioritizes certified elimination and residual-state compression, with local-optimum counting as its first theoretical companion. The complete ZIP is a later-stage handoff: it contains two research rounds, positive claims, failed routes, code, certificates, and reviews. The present work uses that later material as the starting point rather than treating the initial programme as unstarted.

The predecessor counting proof identifies a useful conditional dependency structure: after the costs on a fixed tour are given, every replacement chord occurs in exactly two exchange constraints, and the components are cycles. Its read-two inequality retains all exchanges but effectively loses a factor of two in the leading quadratic exponent. This continuation retains that structural observation and replaces the global read-two estimate with a small-threshold Janson estimate. A clipping argument makes the small-threshold estimate apply to the full integral.

The published MFCS theorem of Manthey and van Rhijn is restricted to $n=2^k+1$, despite the less-qualified abstract. Their Conjecture 17 asks for $O(\sqrt{n!})$, and their discussion suggests a possible exponential base below one [1]. Both the predecessor proof and the proof here cover all integer sizes asymptotically. The finite exceptional sizes do not affect (1).

The probabilistic ingredients used here are positive association for monotone events of independent coordinates and the general-up-set version of Janson's inequality [2]. Independence of the exchange events themselves is neither assumed nor true.

# The constant

For $a\geq0$, define

$$
J(a)=\int_0^\infty e^{-y^2/2-ay}\,dy
=\sqrt{\frac\pi2}\,e^{a^2/2}
\operatorname{erfc}\!\left(\frac a{\sqrt2}\right),
\qquad H(a)=e^{a^2/2}J(a).
\tag{3}
$$

Let $a_*$ be the unique positive solution of

$$
2a_*J(a_*)=1.
\tag{4}
$$

Then

$$
\rho=e^{-1/2}H(a_*).
\tag{5}
$$

The numerical values are

$$
\begin{aligned}
a_*&=0.612003180962480760568090301066\ldots,\\
J(a_*)&=0.816989217627371799672802587135\ldots,\\
H(a_*)&=0.985254362631023839521245490696\ldots,\\
\rho&=0.597586978551345052791857202730\ldots.
\end{aligned}
$$

\Needspace{6\baselineskip}

To justify uniqueness, let $q_a$ be the probability density

$$
q_a(y)=J(a)^{-1}e^{-y^2/2-ay},\qquad y\geq0.
$$

Differentiation under the integral gives

$$
\frac{d}{da}\log H(a)=a-\mathbb E_{q_a}Y,
\qquad
\frac{d^2}{da^2}\log H(a)=1+\operatorname{Var}_{q_a}Y>0.
\tag{6}
$$

At zero the first derivative is negative. The mean decreases with $a$ and is bounded by its value at zero, so the first derivative is positive for sufficiently large $a$. Therefore $H$ has exactly one minimizer. Integration of the derivative of $e^{-y^2/2-ay}$ gives $\mathbb E_{q_a}Y=J(a)^{-1}-a$, yielding (4). At the minimizer,

$$
\mathbb E_{q_{a_*}}Y=a_*,\qquad
\sigma^2:=\operatorname{Var}_{q_{a_*}}Y=1-2a_*^2
=0.250904212983610\ldots.
\tag{7}
$$

The variance identity follows by integrating the derivative of $y e^{-y^2/2-a_*y}$.

# Proof of the sharp exponential rate

## Fixed-tour constraints and conditional dependence

Fix the cyclic tour $0,1,\ldots,n-1,0$, with indices modulo $n$, and write $x_i$ for the cost of its edge $\{i,i+1\}$. For nonadjacent tour-edge positions $i,j$, the unique nontrivial cycle-preserving reconnection adds chords

$$
\{i,j\},\qquad\{i+1,j+1\}.
$$

The exchange is improving exactly when the sum of those chord costs is smaller than $x_i+x_j$. There are $n(n-3)/2$ such unordered pairs. Denote their collection by $\mathcal P_n$.

Condition on the entire tour-cost vector $x$. Each chord is still an independent uniform variable and belongs to exactly two exchange constraints. For $n\geq5$, two distinct constraints share at most one chord, and each constraint shares a chord with exactly two others. Thus the conditional dependency graph is a union of simple cycles. For even $n$, the diameter component has length $n/2$; the other components have length $n$. The exceptional two-variable component at $n=4$ is not used in the asymptotic argument.

Write $F_n(x)$ for the conditional probability that all exchanges are nonimproving, and put

$$
p_n=\Pr(\text{the fixed tour is 2-optimal})
=\int_{[0,1]^n}F_n(x)\,dx.
\tag{8}
$$

The exact tour-count convention gives

$$
\mathbb E[M_n]=\frac{(n-1)!}{2}\,p_n.
\tag{9}
$$

## A conditional sandwich without independence assumptions

Fix $0<\delta<1/2$ and suppose $0\leq x_i\leq\delta$ for every $i$. Every exchange threshold $t=x_i+x_j$ is then at most $2\delta<1$. A single improving-exchange event has probability

$$
p(t)=\Pr(U+V<t)=\frac{t^2}{2}.
$$

Define

$$
Q_n(x)=\sum_{\{i,j\}\in\mathcal P_n}(x_i+x_j)^2,
\qquad \mu=\frac12Q_n(x).
\tag{10}
$$

For two dependent improving events with thresholds $s,t$, their shared-chord intersection probability is

$$
\begin{aligned}
q(s,t)
&=\int_0^{\min(s,t)}(s-y)(t-y)\,dy\\
&=\frac{\min(s,t)^2\max(s,t)}2-
\frac{\min(s,t)^3}{6}.
\end{aligned}
\tag{11}
$$

In particular $q(s,t)\leq t\,p(s)$ and $q(s,t)\leq s\,p(t)$. Since both thresholds are at most $2\delta$,

$$
q(s,t)\leq2\delta\min(p(s),p(t))
\leq\delta\bigl(p(s)+p(t)\bigr).
\tag{12}
$$

Let $\Lambda$ sum these intersection probabilities over **unordered** dependent pairs. The dependency degree is two, so (12) gives $\Lambda\leq2\delta\mu$.

The improving events are decreasing events of independent chord coordinates. The general-up-set Janson inequality, applied with the coordinate order reversed, gives $F_n(x)\leq\exp(-\mu+\Lambda)$ [2]. The source uses an ordered-pair sum $\Delta=2\Lambda$, hence its exponent $-\mu+\Delta/2$ is the same. Its product-space version applies here by finite monotone discretization and convergence; the threshold boundaries have measure zero.

For the lower bound, all nonimproving events are increasing. Positive association therefore gives $F_n(x)\geq\prod_{\{i,j\}\in\mathcal P_n}(1-(x_i+x_j)^2/2)$. Since $u\leq2\delta^2$ implies $\log(1-u)\geq-u/(1-2\delta^2)$, the resulting sandwich is

$$
\boxed{
\exp\!\left[-\frac{Q_n(x)}{2(1-2\delta^2)}\right]
\ \leq\ F_n(x)\ \leq\
\exp\!\left[-\frac{1-2\delta}{2}Q_n(x)\right].}
\tag{13}
$$

The lower bound does not multiply exchange probabilities as an upper bound. Their positive dependence is essential, and its effect on the upper bound is explicitly charged in (11)–(12).

## The quadratic form

Set $A=\sum_i x_i^2$, $S=\sum_i x_i$, and $B=\sum_i x_ix_{i+1}$. Direct expansion gives

$$
Q_n(x)=(n-4)A+S^2-2B.
\tag{14}
$$

Since $0\leq B\leq A$ for nonnegative coordinates,

$$
(n-6)A+S^2\leq Q_n(x)\leq nA+S^2.
\tag{15}
$$

Both inequalities retain the $S^2$ interaction. Dropping that term would change the exponential rate.

## Upper bound: clipping controls the entire original cube

The condition $x_i\leq\delta$ cannot simply be assumed for a tour sampled from the original model. Instead, define $z_i=\min(x_i,\delta)$. Increasing a tour-edge cost can only make local optimality harder, so

$$
F_n(x)\leq F_n(z).
\tag{16}
$$

When $x_i$ is uniform on $[0,1]$, $z_i$ has Lebesgue density one below $\delta$ and an atom of mass $1-\delta$ at $\delta$. The coordinates remain independent. This atom accounts for **all** originally larger tour-edge costs.

Let $\beta=1-2\delta$, take $n\geq7$, and write $s=\sqrt{\beta(n-6)}$. For any $a\geq0$, the tangent inequality

$$
S^2\geq2a\sqrt{\frac{n-6}{\beta}}S-
\frac{a^2(n-6)}\beta
$$

combines with (13) and (15) to give

$$
p_n\leq e^{a^2(n-6)/2}
\left[
\frac1s\int_0^{s\delta}e^{-y^2/2-ay}\,dy
+(1-\delta)e^{-s^2\delta^2/2-as\delta}
\right]^n.
\tag{17}
$$

For fixed $\delta$, the atom term in brackets is exponentially small in $n$. Multiplying the bracket by $\sqrt n$ and taking the limit yields

$$
\limsup_{n\to\infty}\sqrt n\,p_n^{1/n}
\leq\frac{H(a)}{\sqrt{1-2\delta}}.
\tag{18}
$$

Choose $a=a_*$ and then let $\delta\downarrow0$. This proves an upper bound of $H(a_*)$. No unproved assertion about typical tour-edge costs or exchange independence enters this step.

## Lower bound: an exact change of probability measure

For the same fixed $\delta$, let $b=(1-2\delta^2)^{-1}$. Restricting the original integral to $[0,\delta]^n$ and using the lower bounds in (13) and (15) gives

$$
p_n\geq\int_{[0,\delta]^n}
\exp\!\left[-\frac b2(nA+S^2)\right]dx.
$$

Substitute $y_i=\sqrt{bn}\,x_i$ and $R=\delta\sqrt{bn}$. Then

$$
p_n\geq(bn)^{-n/2}I_n(R),
\quad
I_n(R)=\int_{[0,R]^n}
\exp\!\left[-\frac12\sum_i y_i^2-
\frac1{2n}\left(\sum_i y_i\right)^2\right]dy.
\tag{19}
$$

Let $Y_1,\ldots,Y_n$ be independent with density $q_{a_*}$. Completing the square in their sum gives the **exact identity**

$$
I_n(R)=H(a_*)^n\,
\mathbb E\!\left[
 e^{-(\sum_iY_i-na_*)^2/(2n)}
 \mathbf1\{\max_iY_i\leq R\}
\right].
\tag{20}
$$

By (7), the squared centered sum divided by $n$ has expectation $\sigma^2$. Jensen's inequality and the union bound therefore imply

$$
I_n(R)\geq H(a_*)^n
\left[e^{-\sigma^2/2}-n\Pr(Y_1>R)\right].
\tag{21}
$$

For fixed $\delta$, $R$ grows as $\sqrt n$. The density $q_{a_*}$ has a Gaussian tail; explicitly,

$$
\Pr(Y_1>R)\leq
\frac{e^{-R^2/2-a_*R}}{J(a_*)(R+a_*)}.
$$

Thus the bracket in (21) tends to the strictly positive constant $e^{-\sigma^2/2}$. Combining (19)–(21),

$$
\liminf_{n\to\infty}\sqrt n\,p_n^{1/n}
\geq\frac{H(a_*)}{\sqrt b}.
\tag{22}
$$

Letting $\delta\downarrow0$ proves the matching lower bound. In particular,

$$
\lim_{n\to\infty}\sqrt n\,p_n^{1/n}=H(a_*).
\tag{23}
$$

Finally, (9) and Stirling's formula give

$$
\left(\frac{\mathbb E[M_n]}{\sqrt{n!}}\right)^{1/n}
=\left(\frac{\sqrt{n!}}{2n}\right)^{1/n}p_n^{1/n}
\longrightarrow e^{-1/2}H(a_*),
$$

which proves (1).

# A rational certificate for the base $3/5$

The decimal evaluation of $a_*$ is unnecessary for the explicit upper-bound consequence. Since $H(a_*)\leq H(3/5)$,

$$
\rho\leq e^{-7/50}
\left[\sqrt{\frac\pi2}-\int_0^{3/5}e^{-u^2/2}\,du\right].
$$

Put $a=3/5$. Taylor's inequalities imply

$$
\int_0^a e^{-u^2/2}\,du
\geq a-\frac{a^3}6+\frac{a^5}{40}-\frac{a^7}{336},
\qquad
e^{-7/50}\leq1-\frac7{50}+\frac12\left(\frac7{50}\right)^2.
$$

Using $\pi<22/7$ and $\sqrt{11/7}<627/500$ gives the entirely rational estimate

$$
\rho\leq\frac{26186281431}{43750000000}
=0.598543575565714\ldots<\frac35.
\tag{24}
$$

The square comparison and final rational inequality are checked exactly by the supplied script. Equation (1) and $\rho<3/5$ imply $\mathbb E[M_n]=O((3/5)^n\sqrt{n!})$, absorbing the finitely many smaller sizes into the constant.

Equations (1)–(2) do **not** establish $\mathbb E[M_n]\sim\rho^n\sqrt{n!}$ or even $O(\rho^n\sqrt{n!})$. An $\exp(o(n))$ correction can still grow without bound. Determining that correction is a separate problem.

# Transfer theorem: universality at a regular lower endpoint

**Theorem.** Let the edge costs be independent samples from a fixed absolutely continuous distribution supported on $[\ell,\infty)$, with finite lower endpoint $\ell$ and density satisfying

$$
f(\ell+t)\longrightarrow f_0\in(0,\infty)
\quad\text{as }t\downarrow0.
\tag{25}
$$

Then (1) holds with the **same** $\rho$. No finite-moment assumption on the upper tail is needed.

Adding or subtracting $\ell$ from every edge leaves each two-edge-exchange comparison unchanged, so assume $\ell=0$. Given a small $\varepsilon>0$, choose $\delta>0$ such that on $[0,2\delta]$ the density lies between

$$
f_-=(1-\varepsilon)f_0,
\qquad f_+=(1+\varepsilon)f_0.
$$

For thresholds $t\leq2\delta$, an improving exchange has probability between $f_-^2t^2/2$ and $f_+^2t^2/2$. For two exchanges sharing a chord, conditioning on that chord gives

$$
q(s,t)\leq F(t)\,p(s)\leq2\delta f_+\,p(s),
$$

and the symmetric estimate also holds. Consequently the same unordered-pair charging gives $\Lambda\leq2\delta f_+\mu$. Janson yields an upper conditional bound with quadratic coefficient $f_-^2(1-2\delta f_+)/2$.

The clipped tour-coordinate measure now has density at most $f_+$ below $\delta$ and an atom of mass at most one at $\delta$. Repeating (17)–(18) with the corresponding scale yields

$$
\limsup_{n\to\infty}\sqrt n\,p_n^{1/n}
\leq\frac{f_+}{f_-\sqrt{1-2\delta f_+}}H(a_*).
\tag{26}
$$

For the lower bound, positive association gives the conditional coefficient $f_+^2/[2(1-2\delta^2f_+^2)]$.

The original tour density is at least $f_-^n$ on the small cube. The same Gaussian rescaling and identity (20) therefore give

$$
\liminf_{n\to\infty}\sqrt n\,p_n^{1/n}
\geq\frac{f_-}{f_+}\sqrt{1-2\delta^2f_+^2}\,H(a_*).
\tag{27}
$$

Choose $\delta$ small enough for the displayed denominators to be positive, then let $\varepsilon$ and $\delta$ tend to zero. Equations (26)–(27) prove the theorem. The density scale cancels between the $n$ tour variables and the quadratic exchange penalty.

Examples include uniform costs on any nondegenerate bounded interval and independent exponential costs assigned **directly to the edges of the complete graph**. This is not an extension to shortest-path metrics generated by exponential weights on a sparse graph: those metric distances are dependent. The theorem also does not cover a density vanishing or diverging at the lower endpoint, an atom at that endpoint, or a distribution changing with $n$.

# Finite bounds and numerical evaluation

The proof supplies finite one-dimensional bounds rather than merely an existence argument. Define

$$
T(R)=\int_R^\infty e^{-y^2/2-a_*y}\,dy,
\qquad C=e^{-\sigma^2/2}.
$$

For $n\geq7$, $0<\delta<1/2$, $s=\sqrt{(1-2\delta)(n-6)}$, and $b=(1-2\delta^2)^{-1}$,

$$
\begin{aligned}
p_n&\leq e^{a_*^2(n-6)/2}
\left[\frac{J(a_*)-T(s\delta)}s
 +(1-\delta)e^{-s^2\delta^2/2-a_*s\delta}\right]^n,\\
p_n&\geq (bn)^{-n/2}H(a_*)^n
\left[C-\frac n{J(a_*)}T(\delta\sqrt{bn})\right]_+.
\end{aligned}
\tag{28}
$$

Here $[z]_+=\max(z,0)$. The lower-bound clipping is legitimate because a negative intermediate lower bound can always be replaced by zero.

The numerical script evaluates (28) over a declared finite grid of $\delta$ values. The table reports bounds on $(\mathbb E[M_n]/\sqrt{n!})^{1/n}$, not estimates of the actual count. These are deterministic 80-digit numerical evaluations of proved formulas, not directed-rounding certificates or Monte Carlo experiments.

\Needspace{10\baselineskip}

| $n$ | Lower-bound evaluation | Upper-bound evaluation |
|---:|---:|---:|
| $1{,}000$ | 0.58839469 | 0.69450391 |
| $10{,}000$ | 0.59633470 | 0.62590169 |
| $100{,}000$ | 0.59742885 | 0.60693536 |
| $1{,}000{,}000$ | 0.59756765 | 0.60073564 |
| $100{,}000{,}000$ | 0.59758672 | 0.59794450 |

The weak finite upper bound at moderate sizes is visible. It does not contradict the asymptotic $3/5$ consequence, whose hidden finite-size threshold is not asserted to be small. No experiment enumerates tours at any of these large sizes.

# Verification and provenance

## Newly written checks

`checks/check_sharp_rate.py` imports none of the handoff's research implementations. It uses only Python's standard library and exact rational or integer arithmetic. Its completed receipt records 161,602 exchange constraints for $3\leq n\leq100$, 546 direct checks of the two possible reconnections through $n=16$, and the exact conditional cycle sizes, including even-diameter cases.

For small discrete product spaces, it enumerates 95,913 combined tour/chord assignments across 563 tour-cost assignments. It verifies the Harris lower bound, clipping monotonicity, and 2,303 individual conditional-probability inequalities underlying Janson's estimate. The discrete calculations test the dependency bookkeeping; the continuous result follows from the written probability argument, not from treating a discrete grid as the original model.

The same script checks 2,205 rational shared-chord overlap identities and inequalities, 592 quadratic identities and two-sided comparisons through $n=150$, and the exact rational certificate (24). All checks pass.

`checks/evaluate_bounds.py` evaluates the constant and finite bounds using mpmath 1.3.0 at 80 decimal digits. It cross-checks $J(a_*)$ and the tilted mean by direct quadrature rather than the complementary-error-function formula. It also checks 1,200 local probability/overlap inequalities numerically for direct independent exponential edge costs. All numerical checks pass; they are not substitutes for the transfer theorem's proof.

## Replication of the handoff

The archive contains 615 entries: 614 manifested payloads and the manifest itself. Every payload's byte count and SHA-256 digest agrees with the manifest. The original ZIP remains unchanged, with SHA-256

`8b1155feb74ec60f77e8c9b61a119a48fe8aeff06966edd33047766ce06bff50`.

Four archived checkers were rerun in a temporary extraction. All exited successfully, and their recomputed JSON receipts agree with the archived receipts as structured data. The selected domains are:

| Thread | Reproduced finite evidence |
|:---|:---|
| Q3818/P5 predecessor | 388 grid cases; 784 quadratic cases; exchange accounting through $n=30$. |
| P1 elimination | 100 snapshots and 1,280 forced-edge bounds compared with exhaustive spanning-tree calculations; negative transformed costs and ties included. |
| P2 state compression | The five $n=7,\ldots,11$ residual examples; both frontier representations agree with subset-DP optima. |
| P3 descent | 1,512 ordered quadruples; 20,376 ordinary and 20,376 normalized gain pieces. |

These are replications of finite checks, not a new independent validation of every all-size theorem in the ZIP. The P1 work establishes no fresh speed advantage, and the P2 state quotient is not a universal runtime reduction. No filing or catalog-writing script was run.

The standalone `replicate_handoff.py` validates the original ZIP and reproduces these four runs without modifying it. Source provenance records identify the copied predecessor proof and handoff overview by their original paths and hashes.

# Programme disposition and next mathematical target

Q3818/P5 receives the sharp-rate theorem, a matching exponential lower bound, the explicit $3/5$ upper-bound consequence, and the lower-endpoint transfer theorem. The contributions to P1, P2, and P3 in this continuation are finite replications, not new general theorems or comparative benchmarks. This work does not resolve Q3817, Q549, Q550, Q1852, Q1853, Q1953, Q3819, P4, or P6.

The new counting theorem concerns an expectation over instances. It does not establish concentration of $M_n$, the number of local optima in a typical instance, the cost of a local optimum returned by a search rule, attraction-basin sizes, or descent time. Direct independent costs remain distinct from metric, Euclidean, and sparse shortest-path models.

The immediate mathematical continuation is the subexponential correction in (2). The present argument pins down the exponential rate while deliberately tolerating errors below order $n$ in the logarithm. Improving the shared-chord correction beyond the cap-dependent estimate, and evaluating the resulting cyclic dependence more precisely, would address that remaining count question. Tour-cost and basin-weighted questions require additional arguments rather than reinterpretation of the count theorem.

\newpage

# References

[1] Bodo Manthey and Jesse van Rhijn. *Counting Locally Optimal Tours in the TSP*. MFCS 2025, LIPIcs 345, article 73, pp. 73:1–73:17. DOI: 10.4230/LIPIcs.MFCS.2025.73. Theorem 3, Section 4, and Conjecture 17. The publisher's HTML was checked on October 12, 2026. Related version: arXiv:2410.18650v1.

[2] Oliver Riordan and Lutz Warnke. *The Janson inequalities for general up-sets*. Random Structures & Algorithms 46(2), 2015. DOI: 10.1002/rsa.20506. Theorem 1. The arXiv:1203.1024v2 statement and its ordered-pair convention were checked, including the rendered first two pages.

[3] User-supplied B14 programme and complete handoff, dated October 12, 2026. The counting predecessor is `research/b14-first-round-2026-10-12/local-optima/RESULT.md` under `projects/thesis-catalog/`; its copied proof, review, and source hashes are in this packet's `sources/` directory. Replication receipts and original archive integrity are recorded separately.
