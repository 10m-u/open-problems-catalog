# Third research set: density preservation, learned decision certificates, and validation design

**Bayesian Knowledge System · 5 October 2026**

## Results and reading contract

This round selects **Q812**, revisiting a previously partial result, and the review's project questions **N2** and **N5**. Original identifiers and information contracts are retained. Source-derived starting points, the additional sampling contracts adopted here, mathematical derivations, and executed checks are distinguished below.

| Target | Result in this round | Scope |
|---|---|---|
| Q812 | A positive, fixed, symmetric copula and harmonic weights give an almost-surely singular weak limit. A complete Hellinger-series criterion is proved for circular copulas. | Full counterexample to the supplied universal assertion; a sharper classification within the stated circular subclass. |
| N2 | A uniform finite-sample certificate for the same common-policy deficiency as H3, valid simultaneously over all summaries of a fixed finite observation alphabet. | A finite, resolved-label sampling contract; no unlabeled-data or unrestricted semantic-learning claim. |
| N5 | A finite second-order-cone formulation, exact lower/upper certificates, an optimal symmetric allocation formula, and a validation-to-decision gate. | Explicit finite occupancy vertices; no compact-MDP polynomial-time claim. |

The Q812 argument is the principal mathematical advance. N2 and N5 deliberately use standard concentration, minimax, and convex optimization tools to complete concrete project targets. The accompanying programs are standalone controls, not a modification of the original scaffold. The proofs have not been peer-reviewed or checked by a proof assistant. Public priority is not established.

The two previous-round reports and packages are present in the supplied runtime. This round does not claim to have independently audited every earlier result. Its dependencies are the explicitly restated Q724 safety geometry and H3 deficiency contract, whose short arguments are also checked below.

---

## 1. Q812: square-summable updating does not preserve a density

### 1.1 Source question and previous progress

Collection 9, Q812 asks about

\[
 f_{n+1}(x)=f_n(x)\left[1-r_n+r_nc(F_n(x),F_n(X_{n+1}))\right],
 \qquad X_{n+1}\mid\mathcal F_n\sim f_n,
\]

where the initial density is positive, the copula density is fixed and positive, and

\[
 \sum_n r_n=\infty,\qquad \sum_n r_n^2<\infty.
\]

Must the predictive measures converge almost surely in total variation to their weak limit?

The supplied solutions establish this under a uniform conditional second-moment bound on the copula. The journal article's Section 2.3 still explicitly asks whether square-summability alone suffices for a fixed copula. Its nonconvergence example with weights bounded away from zero does not answer Q812. [S1, S2]

**Answer: no.** The counterexample below uses the ordinary harmonic schedule, a copula bounded away from zero, and a standard normal initial density.

### 1.2 A circular-copula family

Let \(g:(0,1]\to(0,\infty)\) be measurable, finite at every positive argument, and satisfy \(\int_0^1g(t)dt=1\). Let

\[
 d_{\mathbb T}(u,v)=\min\{|u-v|,1-|u-v|\},\qquad
 c_g(u,v)=g\bigl(2d_{\mathbb T}(u,v)\bigr)
\]

away from the diagonal. Define \(c_g(u,u)=1\). Values on this null set do not change any integral.

For fixed \(u\) and uniform \(V\), \(2d_{\mathbb T}(u,V)\) is uniform on \((0,1)\). Consequently every row of \(c_g\) integrates to one, as does every column. This is a positive symmetric copula density. Most importantly, the law

\[
 C\overset d=g(U),\qquad U\sim\mathrm{Unif}(0,1)
\]

is the law of \(c_g(u,V)\) for **every** fixed \(u\). It has \(EC=1\).

For a fixed spatial point \(x\), put \(M_n(x)=f_n(x)/f_0(x)\). Conditional on the past, \(V_{n+1}=F_n(X_{n+1})\) is uniform. Hence

\[
 M_{n+1}(x)=M_n(x)Z_n(x),\qquad
 Z_n(x)=1+r_n(C_n(x)-1),
\]

where, for this fixed \(x\), the \(C_n(x)\) are independent with common law \(C\). This assertion does not assert independence across different spatial points. Their dependence is immaterial to the argument.

Define

\[
 a_g(r)=E\sqrt{1+r(C-1)},\qquad
 h_g(r)=1-a_g(r).
\]

Because \(E[1+r(C-1)]=1\),

\[
 h_g(r)=\frac12E\left(\sqrt{1+r(C-1)}-1\right)^2\ge0.\tag{1}
\]

### 1.3 Exact dichotomy

**Theorem 1.** For every copula \(c_g\) above, every positive initial density, and deterministic \(r_n\in(0,1]\):

* If \(\sum_nh_g(r_n)<\infty\), the predictive measures converge almost surely in total variation to a probability measure with a density.
* If \(\sum_nh_g(r_n)=\infty\), their weak limit is almost surely purely singular with respect to Lebesgue measure. Their total-variation distance to that limit is one at every finite stage, under the convention \(\mathrm{TV}=\sup_A|P(A)-Q(A)|\).

#### Existence of the weak limit

For each Borel set \(B\), \(\mu_n(B)=\int_Bf_n\) is a bounded martingale: the copula row integral is one. To obtain almost-sure tightness, choose compact sets \(K_j\) with \(\mu_0(K_j^c)\le2^{-2j}\). Doob's inequality gives

\[
 P\{\sup_n\mu_n(K_j^c)>2^{-j}\}\le2^{-j}.
\]

Borel-Cantelli and convergence on a countable measure-determining set of continuous functions give a random probability measure \(\mu_\infty\) with \(\mu_n\Rightarrow\mu_\infty\) almost surely. Bounded martingale convergence and a monotone-class argument also give

\[
 \mu_n(B)=E[\mu_\infty(B)\mid\mathcal F_n]
\]

as a measure-valued conditional expectation.

#### Summable Hellinger series

For \(m<n\), conditional independence of the fixed-point multiplier laws yields

\[
 E\int\sqrt{f_m(x)f_n(x)}dx
 =\prod_{j=m}^{n-1}a_g(r_j).
\]

Therefore

\[
 E\int(\sqrt{f_n}-\sqrt{f_m})^2dx
 =2\left(1-\prod_{j=m}^{n-1}a_g(r_j)\right).\tag{2}
\]

When \(\sum_j(1-a_g(r_j))<\infty\), the right side tends uniformly to zero as \(m,n\to\infty\). Thus \(\sqrt{f_n}\) is Cauchy in \(L^2(P\times dx)\), and \(f_n\) converges in \(L^1(P\times dx)\).

Independently, for almost every \(x\), the nonnegative martingale \(f_n(x)\) has an almost-sure limit \(f_\infty(x)\). Fubini identifies this with the preceding product-space limit. Fatou gives \(\int f_\infty\le1\) almost surely; product-space \(L^1\) convergence gives \(E\int f_\infty=1\). The integral is therefore one almost surely. Scheffe's lemma gives pathwise \(L^1\), hence total-variation, convergence.

Equation (2) also gives the quantitative bound

\[
 E\,\mathrm{TV}(\mu_n,\mu_\infty)
 \le\sqrt{2\left(1-\prod_{j=n}^\infty a_g(r_j)\right)}
 \le\sqrt{2\sum_{j=n}^\infty h_g(r_j)}.\tag{3}
\]

This is a bound for an already specified copula and weight schedule, not an estimate of either from data.

#### Divergent Hellinger series

At every fixed spatial point,

\[
 E\sqrt{M_n(x)}=\prod_{j=0}^{n-1}a_g(r_j)\longrightarrow0.
\]

The nonnegative martingale \(M_n(x)\) converges almost surely. Fatou applied to its square root forces its limit to be zero. Fubini gives \(f_n(x)\to0\) for Lebesgue-almost every \(x\), almost surely.

To conclude **pure singularity**, rather than merely failure of \(L^1\) convergence, let \(G_\infty\) be the density of the absolutely continuous component of \(\mu_\infty\) relative to \(\mu_0\). A jointly measurable version exists on this standard Borel space. The inequality \(\mu_\infty\ge G_\infty\mu_0\), conditioned on \(\mathcal F_n\), implies

\[
 M_n(x)\ge E[G_\infty(x)\mid\mathcal F_n]
\]

for \(P\times\mu_0\)-almost every \((\omega,x)\). The right side converges to \(G_\infty(x)\), since \(\mu_\infty\), and hence its Lebesgue decomposition, is measurable with respect to the full observation history. The left side converges to zero. Therefore \(G_\infty=0\) almost everywhere.

Every finite-stage measure is absolutely continuous while the limit is singular. Their total-variation distance is consequently one. This completes the theorem.

### 1.4 Harmonic updates: entropy is the exact threshold in this family

**Theorem 2.** For \(r_n=1/(n+2)\), the circular-copula process converges in total variation to a density if and only if

\[
 \int_0^1g(t)\log_+g(t)dt<\infty.\tag{4}
\]

If the integral is infinite, the limit is purely singular. Since the negative part of \(g\log g\) is integrable, this is equivalent to finite copula relative entropy \(\int\!\int c_g\log c_g\).

**Proof.** Write \(\psi(s)=(\sqrt{1+s}-1)^2\). For \(s\ge0\),

\[
 \psi(s)\le\min\{s^2/4,s\}.
\]

For \(C\le2\) and \(n\ge2\), \(\psi((C-1)/n)\le n^{-2}\). For \(C>2\), split the sum over \(n\) at \(C\). The part \(n\le C\) is bounded by a constant times \(C\log C\); the tail is bounded by a constant times \(C\). Thus

\[
 \sum_{n=2}^\infty h_g(1/n)
 \le K\{1+E[C\log_+C]\}
\]

for a universal finite \(K\).

Conversely, on \(C\ge4n\), \(Z=1+(C-1)/n\ge C/n\ge4\), so

\[
 (\sqrt Z-1)^2\ge Z/4\ge C/(4n).
\]

By Tonelli,

\[
 \sum_{n=2}^\infty h_g(1/n)
 \ge\frac18E\left[C\sum_{2\le n\le C/4}\frac1n\right].\tag{5}
\]

This is infinite precisely when \(E[C\log_+C]\) is infinite. Apply Theorem 1. The same criterion holds for schedules bounded above and below by positive constant multiples of \(1/n\) eventually; the same splitting proof applies.

### 1.5 Explicit counterexample answering Q812

Choose

\[
 g(t)=\frac1{t(1+\log(1/t))^2},\quad 0<t\le1,
 \qquad r_n=\frac1{n+2},
 \qquad f_0=\text{standard normal density}.\tag{6}
\]

With \(s=-\log t\),

\[
 \int_0^1g(t)dt=\int_0^\infty\frac{ds}{(1+s)^2}=1.
\]

Also \(g(t)\ge e/4>0\): the minimum of \(e^s/(1+s)^2\) occurs at \(s=1\). The copula is strictly positive, including the assigned diagonal value, but unbounded. Its entropy is infinite because

\[
 \int_0^1g(t)\log g(t)dt
 =\int_0^\infty\frac{s-2\log(1+s)}{(1+s)^2}ds=\infty.
\]

For clarity, the integral truncated at \(s=L\) is exactly

\[
 \log(1+L)+\frac{2\log(1+L)+3}{1+L}-3,
\]

which diverges. The harmonic weights have divergent sum and square-summable squares. Theorem 2 therefore proves an almost-surely singular limit and total-variation distance one at every finite stage.

**This refutes the supplied universal assertion, not just a numerical conjecture.** It does not contradict the earlier conditional-second-moment theorem: that condition fails here.

### 1.6 Finite entropy alone is not enough for arbitrary square-summable schedules

Let

\[
 g_\beta(t)=(1-\beta)t^{-\beta},\qquad \tfrac12<\beta<1.
\]

Its entropy is finite:

\[
 \int g_\beta\log g_\beta
 =\log(1-\beta)+\frac{\beta}{1-\beta},
\]

but its second moment is infinite. Put \(\alpha=1/\beta\). A change of variables in (1), followed by dominated convergence, gives

\[
 h_{g_\beta}(r)\sim K_\beta r^{1/\beta},\qquad
 K_\beta=\frac{(1-\beta)^{1/\beta}}{4(1/\beta-1)}
 B\left(2-\frac1\beta,\frac1\beta-\frac12\right)>0.\tag{7}
\]

To check the constant, \(C\) has density \(\alpha(1-\beta)^\alpha c^{-\alpha-1}\) on \([1-\beta,\infty)\). The limiting integral is

\[
 \frac{\alpha(1-\beta)^\alpha}{2}
 \int_0^\infty(\sqrt{1+y}-1)^2y^{-\alpha-1}dy.
\]

Twice integrating by parts evaluates it as (7). Near zero the integrand has order \(y^{1-\alpha}\); near infinity it has order \(y^{-\alpha}\), so both ends are integrable. The negligible interval where \(r(C-1)<0\) contributes \(O(r^2)\).

For \(r_n=(n+2)^{-a}\), Theorem 1 now yields the exact boundary

\[
 \boxed{\text{density/TV convergence iff }a>\beta;
 \quad\text{pure singularity if }a\le\beta.}\tag{8}
\]

In particular, \(\beta=3/4,a=2/3\) gives another counterexample satisfying the source's two summability conditions, even though the copula entropy is finite. With the same copula and harmonic updates, the limit instead has a density. This separates the copula condition from the schedule condition.

### 1.7 No nonsummable schedule works uniformly over all fixed positive copulas

There is a further quantifier-level consequence.

**Theorem 3.** A deterministic weight schedule in \((0,1]\) guarantees density/TV convergence for every fixed positive copula and every positive initial density **if and only if** \(\sum_nr_n<\infty\).

The sufficiency direction is the source's standard telescoping argument: the expected \(L^1\) increment is at most \(2r_n\), so the total \(L^1\) path length is finite almost surely.

For necessity, suppose \(\sum_nr_n=\infty\). Define

\[
 A(t)=\sum_{n:r_nt\ge4}r_n.
\]

As \(t\to\infty\), \(A(t)\to\infty\). Choose increasing finite \(t_j\ge8\) with \(A(t_j)\ge2^{2j}\); if some \(A(t)\) is already infinite, the argument is easier. For \(j=1,2,\ldots\), give \(C\) an atom at \(t_j\) of probability \(p_j=2^{-j-1}/t_j\). Their total contribution to \(EC\) is \(1/2\). Put the remaining probability at

\[
 b=\frac{1/2}{1-\sum_jp_j}>0,
\]

so \(EC=1\). Realize this distribution as \(g(U)\), using disjoint intervals of the prescribed lengths, and form the fixed circular copula \(c_g\).

Using the same \(Z\ge4\) inequality as above,

\[
 \sum_nh_g(r_n)
 \ge\sum_j\frac{p_jt_j}{8}A(t_j)
 \ge\sum_j2^{j-4}=\infty.
\]

The limit is singular by Theorem 1. The copula is selected for the schedule once, not changed during the run.

### 1.8 Computational checks and system consequence

`copula_limits.py` checks normalization through closed-form CDF endpoints, symmetry, CDF derivatives away from singularities, fourteen high-precision Hellinger quadratures, and eight finite independent-product identities. These are arithmetic and formula checks; the infinite-horizon conclusion is proved above.

A finite cap or finite-bin approximation to this copula changes the mathematical model. Once the approximated copula is bounded, the earlier square-summability theorem can apply to the approximation even though the uncapped process is singular. Apparent stabilization of a discretized implementation is therefore not a certificate for the original recursion.

The conclusion concerns uniform total-variation preservation. It does not say that every fixed bounded payoff fails to converge, nor that a singular probability measure is invalid. It says a density-only limiting representation is not licensed by square-summability alone.

---

## 2. N2: learning a use-specific common-policy certificate

### 2.1 Source target and the additional observation contract

The review asks for a high-probability bound on H3's task-relative deficiency using estimated kernels and held-out observations, with estimation and construction costs included. H3 defines

\[
 \delta(T)=\sup_d\inf_g\max_{m\le M}
 \{R_m(g\circ T)-R_m(d)\}.\tag{9}
\]

Here \(d\) is a raw-observation rule, \(g\) a summary rule, and the replacement must be common to all models. The dual form ranges over every mixture of the models, not merely one convenient prior. [S3, S4]

**Adopted finite sampling contract.** The raw alphabet \(\mathcal Y\) has fixed size \(K\), the action alphabet has size \(d\), and the declared loss \(\ell(h,a)\) lies in \([0,1]\). For each model \(m\), obtain \(n\) independent, resolved-label pairs \((H_{mj},Y_{mj})\sim P_m\). Independence across models is not needed for the union bound; within-model sampling is required. The model labels and target resolutions are genuine parts of this contract. Synthetic draws certify the declared synthetic models, not their applicability to real evidence.

A summary \(T\) is any deterministic map on this fixed raw alphabet. Let \(\widehat R_m\) be empirical risk and \(\widehat\delta(T)\) the exact analogue of (9) with empirical risks.

### 2.2 A simultaneous certificate over every summary

**Theorem 4.** Set

\[
 \beta_n=\sqrt{\frac{K\log d+\log(2M/\alpha)}{2n}}.
\]

With probability at least \(1-\alpha\), simultaneously for every summary \(T\),

\[
 \boxed{|\widehat\delta(T)-\delta(T)|\le2\beta_n.}\tag{10}
\]

This includes a summary selected after inspecting these data, provided its raw domain and action/loss contract are the fixed ones above.

**Proof.** There are \(d^K\) deterministic raw rules. Hoeffding's inequality and a union bound over these rules and the \(M\) models give

\[
 \sup_{m,d}|\widehat R_m(d)-R_m(d)|\le\beta_n.
\]

Every randomized raw rule is a convex combination of deterministic rules, so the same event covers randomized rules. Every composed summary rule \(g\circ T\) is also a raw rule, regardless of which \(T\) produced it. Therefore every risk difference in (9) changes by at most \(2\beta_n\). Taking the same maxima, infima, and suprema preserves that bound.

The simultaneous statement does not make data-dependent unrestricted representations free. The \(K\log d\) term already pays for **all** raw rules on the fixed finite domain. When that domain is very large, a held-out analysis with a smaller predeclared rule class can be substantially cheaper, but it certifies only that smaller class.

A valid output is

\[
 \delta(T)\in\left[
 \max\{0,\widehat\delta(T)-2\beta_n\},
 \min\{1,\widehat\delta(T)+2\beta_n\}\right].\tag{11}
\]

If the numerical optimization instead supplies an exactly verified interval \([L_T,U_T]\), use \([\max(0,L_T-2\beta_n),\min(1,U_T+2\beta_n)]\).

For any raw rule, an empirical common replacement with empirical excess risk at most \(U_T\) has true model-uniform excess risk at most \(U_T+2\beta_n\). The statement still holds for a data-selected raw rule because the event is uniform.

### 2.3 Selection, computational cost, and sample cost

Let \(\kappa(T)\) be a deterministic construction/storage cost already converted into the same decision-loss units. Choosing a summary minimizing \(\kappa(T)+\widehat\delta(T)\) gives

\[
 \kappa(\widehat T)+\delta(\widehat T)
 \le\inf_T\{\kappa(T)+\delta(T)\}+4\beta_n.\tag{12}
\]

If upper optimization bounds have maximum certified width \(\eta\), minimizing their cost-adjusted upper bounds adds at most \(\eta\) to the right side. This is not a justification for conflating bytes, time, and loss without a declared conversion.

For an absolute deficiency estimation error \(\varepsilon\), (10) requires

\[
 n\ge\frac{2[K\log d+\log(2M/\alpha)]}{\varepsilon^2}
\]

per model. A one-sided certificate with overstatement at most \(\varepsilon\) uses the stronger requirement \(4\beta_n\le\varepsilon\). If labeled examples under model \(m\) cost \(c_m\), the acquisition cost is \(\sum_mc_mn\), in addition to optimization and representation construction.

The reference implementation enumerates \(d^K\) raw rules and solves one LP per raw rule and summary. Its inference cost is exponential in \(K\). The sample bound is not an efficient-computation theorem.

### 2.4 Why the confidence statement requires ground truth

There is an immediate impossibility result for unlabeled-only certification. Let \(Y\) be a fair bit and compress it to a constant. Under one law, \(H\) is an independent fair bit; under a second, \(H=Y\). Their unlabeled \(Y\)-distributions agree exactly. Under binary classification loss their deficiencies are respectively zero and \(1/2\).

No number of unlabeled raw observations distinguishes these contracts. A universally valid certificate must therefore allow \(1/2\) on data compatible with both. The missing information cannot be supplied by model naming or a normalized posterior.

Even with labels, the \(\varepsilon^{-2}\) scale is necessary. Let \(H\) be fair and let \(Y\) report it correctly with probability \(1/2+\theta\), with a constant summary. The deficiency is \(\theta\). Distinguishing \(\theta=0\) from \(\theta=2\varepsilon\), \(0<\varepsilon\le1/8\), reduces to distinguishing Bernoulli correctness probabilities. The one-sample divergence is

\[
 D(P_0\|P_{2\varepsilon})
 =-\tfrac12\log(1-16\varepsilon^2)\le16\varepsilon^2.
\]

A certificate lying in \([\delta,\delta+\varepsilon]\) with probability at least \(1-\alpha\) under both laws yields a test with both errors at most \(\alpha\). Data processing for relative entropy then requires

\[
 n\ge
 \frac{(1-2\alpha)\log((1-\alpha)/\alpha)}{16\varepsilon^2},
 \qquad 0<\alpha<1/2.\tag{13}
\]

This establishes the accuracy/confidence obstruction, not a sharp lower bound for every finite alphabet.

### 2.5 Exact LP certificates

For a deterministic raw rule \(d\), the replacement LP minimizes \(v\) subject to

\[
 R_m(g\circ T)-R_m(d)\le v\quad(m\le M),
 \qquad g(\cdot\mid z)\in\Delta(\mathcal A).
\]

Its dual supplies a model mixture \(\lambda\). For any feasible replacement and any mixture, respectively, the following are an upper and a lower bound on the fixed-raw-rule value:

\[
 \max_m\{R_m(g\circ T)-R_m(d)\},
\]

\[
 \sum_z\min_a\sum_m\lambda_m
 E_m[\mathbf1\{T(Y)=z\}\ell(H,a)]
 -\sum_m\lambda_mR_m(d).\tag{14}
\]

All coefficients in the controls are rational. The solver only proposes policies and mixtures; they are reconstructed as nonnegative rational probability vectors, and (14) is recomputed exactly. A feasible upper replacement for every deterministic raw rule covers every randomized raw rule by mixing the replacements. The maximum lower witness and maximum upper bound therefore enclose the full deficiency. No numerical optimizer status is treated as an exact certificate.

### 2.6 Executed h2 experiment

Use the supplied h2 model

\[
 Y=2(2H-1)+E,\quad P(H=1)=p,
\]

where \(E\in\{-2,0,2\}\) has probabilities \(r/2,1-r,r/2\). The four models use \(p,r\in\{1/4,3/4\}\). Actions are predict zero, predict one, and abstain; abstention costs \(3/10\), incorrect prediction one, and correct prediction zero. [S4]

Compare sign, magnitude, and constant summaries. The exact deficiencies are

\[
 \delta(\operatorname{sign}Y)=0,
 \qquad \delta(|Y|)=\delta(\text{constant})=\frac{21}{80}.
\]

For sign, every nonzero observation reveals \(H\) exactly; at zero, raw and summary information coincide. A summary rule can match any raw rule at zero and choose a loss-minimizing action for the known target otherwise. This establishes zero deficiency for **any finite loss family depending only on this immediate target**, not just the displayed classification loss. It does not cover future queries about the noise mechanism.

For the constant summary, write \(\bar p=E_\lambda p\). Its Bayes risk is \(\min(\bar p,1-\bar p,3/10)\). The raw Bayes risk arises only at \(Y=0\) and is

\[
 \min\{E_\lambda[pr/2],E_\lambda[(1-p)r/2],(3/10)E_\lambda[r/2]\}.
\]

Since \(r\ge1/4\), the latter is at least one eighth of the constant-summary Bayes risk. Thus the gap is at most \((7/8)(3/10)=21/80\). Mix the two \(p\)-values equally while fixing \(r=1/4\); this attains the bound. Under that same mixture, magnitude is independent of the fair target, so magnitude also attains the same lower bound. Because magnitude retains more information than the constant summary, its deficiency cannot be larger. This proves both values.

The earlier full joint reconstruction error of sign is \(1/6\). There is no contradiction: reconstructing the joint raw observation law is stronger than preserving losses about \(H\). [S4]

The run uses **20,000 resolved-label synthetic samples from each of four models**, 80,000 total. One 95% simultaneous event covers all three comparisons. The computed deficiency radius is \(2\beta_n=0.0325088223\).

| Summary | True deficiency | Empirical deficiency | 95% simultaneous interval |
|---|---:|---:|---:|
| Sign | 0 | 0 | [0, 0.032509] |
| Magnitude | 0.262500 | 0.261966 | [0.229457, 0.294475] |
| Constant | 0.262500 | 0.261968 | [0.229459, 0.294477] |

At a declared maximum excess-loss budget of 0.04, sign is certified; magnitude and constant are rejected. This is an executed synthetic result, not an empirical claim about semantic sensors.

Two additional exact controls protect the quantifiers. In a model-tag example, each model individually has no value for the tag, while a mixture has deficiency \(1/2\). In an opposed-signal example, raw and compressed minimax risks both equal \(1/2\), but deficiency is still \(1/2\). Neither model-specific fitting nor equality of one minimax value substitutes for (9).

---

## 3. N5: choose coverage by dangerous policy boundaries

### 3.1 Source target and exact objective

The review proposes maximizing the minimum Q724 distance to a bad policy's normal cone under a costed validation design. The reference reward and explicit policy/occupancy class are known in this first control. This is an **oracle design benchmark**, not a claim that an unknown true reward is available for free. [S3, S4]

Let \(V\subset\mathbb R^q\) be the finite vertices of the normalized discounted occupancy polytope. Let \(R\) have nonconstant policy returns and reward range \(c>0\). Define

\[
 V_L=\{v\in V:(\max_wR\cdot w-R\cdot v)/(\max_wR\cdot w-\min_wR\cdot w)\ge L\}.
\]

For each bad vertex \(v\), let \(A_v\) have rows \(v-w\), and put \(b_v=-A_vR\). The cone-distance margin is

\[
 \delta_v(D)=\frac1{c^2}\min_{e:A_ve\ge b_v}\sum_iD_ie_i^2,
 \qquad \Delta(D)=\min_{v\in V_L}\delta_v(D).\tag{15}
\]

Every learned reward with squared validation error at most \(\varepsilon\) has only policies of regret strictly less than \(L\) among its maximizers **if and only if** \(\varepsilon<\Delta(D)\).

For necessity, a nearest reward in a bad cone gives an unsafe maximizing policy. For sufficiency, a bad optimal randomized occupancy decomposes into optimal vertices, at least one of which has bad true return. The polyhedral projection argument gives attainment even when some design weights are zero. This rechecks the Q724 dependency and preserves its strict boundary and tie convention.

Let the feasible design set be a nonempty compact polytope \(\mathcal D\subseteq\Delta_q\), for example

\[
 \mathcal D=\{D\ge0:\mathbf1^TD=1,\ k^TD\le B\}.
\]

The design target is \(\max_{D\in\mathcal D}\Delta(D)\).

### 3.2 A finite convex conic formulation

For every bad vertex, introduce multipliers \(\lambda_v\ge0\) and nonnegative slacks \(z_{vi}\). Then the exact finite reformulation is

\[
 \begin{aligned}
 \max\quad&t\\
 \text{subject to}\quad&D\in\mathcal D,\\
 &(A_v^T\lambda_v)_i^2\le4D_iz_{vi}
 &&\text{for every bad }v\text{ and coordinate }i,\\
 &b_v^T\lambda_v-\sum_i z_{vi}\ge c^2t
 &&\text{for every bad }v.
 \end{aligned}\tag{16}
\]

Each quadratic inequality is a rotated second-order-cone constraint. For example it is equivalent to

\[
 \|( (A_v^T\lambda_v)_i, D_i-z_{vi})\|_2\le D_i+z_{vi}.
\]

**Proof of equivalence.** The QP dual for fixed \(D\) is

\[
 \sup_{\lambda\ge0}\left[
 b_v^T\lambda-\sum_{i:D_i>0}\frac{(A_v^T\lambda)_i^2}{4D_i}
 \right],\tag{17}
\]

with \((A_v^T\lambda)_i=0\) wherever \(D_i=0\).

The primal is feasible, because learned reward zero is in every normal cone, and its minimum is attained. First-order optimality over a polyhedron supplies nonnegative KKT multipliers, including for zero-weight coordinates. Thus there is no duality gap. The cone inequalities in (16) are exactly the quadratic-over-linear epigraphs, with the correct zero-denominator closure. Enforcing the dual lower bound for every bad vertex is therefore equivalent to \(t\le\Delta(D)\).

### 3.3 Exact certificates without trusting the optimizer

The implementation uses a cutting-plane master LP and exact small cone projections rather than an installed conic solver. It proves a lower and an upper bound separately.

**Lower bound.** Supply a feasible rational \(D\). For each bad vertex, supply \(e_v,\lambda_v\) satisfying

\[
 A_ve_v\ge b_v,\quad\lambda_v\ge0,\quad
 2\operatorname{diag}(D)e_v=A_v^T\lambda_v,
\]

and complementarity. These rational equalities and inequalities certify the exact projection objective. Their minimum certifies \(\Delta(D)\).

**Upper bound.** Supply finitely many feasible unsafe rewards with coordinatewise squared errors \(q^j_i=e_{ji}^2/c^2\), and rational mixture weights \(w_j\ge0\), \(\sum_jw_j=1\). Put \(\bar q=\sum_jw_jq^j\). For every design,

\[
 \Delta(D)\le D\cdot\bar q.
\]

On the simplex this yields the global upper bound \(\max_i\bar q_i\). Under one cost constraint, any rational \(\zeta\ge0\) gives

\[
 \boxed{\max_{D\in\mathcal D}\Delta(D)
 \le\max_i(\bar q_i-\zeta k_i)+\zeta B.}\tag{18}
\]

SciPy proposes master designs, cut-mixture weights, and cost multipliers. The implementation reconstructs feasible rational quantities and verifies all certificates in the original problem. The exact lower/upper bracket, not the floating-point solver status, licenses its accuracy claim.

The inner active-set oracle enumerates independent active constraints and solves their KKT system over rational numbers. It requires positive design weights and is intentionally limited to small explicit instances. The master uses a small positive floor to obtain such candidates, but the upper certificate (18) is over the **original** simplex/cost set, including zero coverage. Thus a successfully closed bracket certifies the original design optimum despite the computational floor. Failure to close the bracket would be reported rather than excused as convergence.

General SOCP optima need not be rational. “Exact finite formulation” and “exact rational enclosing certificate” do not mean every optimum is represented by a rational point.

### 3.4 Closed-form optimal allocation for one best action and K bad actions

For one state, rewards \(R=(1,0,\ldots,0)\), and \(K\) bad actions, every bad action has normalized regret one. For \(0<L\le1\),

\[
 \Delta(D)=\min_{j=1}^K\frac{D_0D_j}{D_0+D_j},\tag{19}
\]

with zero when a required weight vanishes. The nearest unsafe reward ties action zero and action \(j\) at \(D_0/(D_0+D_j)\), leaving the others at zero.

Permutation symmetry and concavity allow equal bad-action weights. Write \(D_0=x\), \(D_j=(1-x)/K\). Maximizing

\[
 \frac{x(1-x)}{1+(K-1)x}
\]

gives

\[
 \boxed{D_0^*=\frac1{1+\sqrt K},\qquad
 D_j^*=\frac1{\sqrt K(1+\sqrt K)},\qquad
 \Delta^*=\frac1{(1+\sqrt K)^2}.}\tag{20}
\]

There is also a direct upper certificate. For each bad action use the tie reward \(\sqrt K/(1+\sqrt K)\), and mix these \(K\) unsafe rewards uniformly. The mean squared error in **every** coordinate is \(1/(1+\sqrt K)^2\). Equation (18) with no costs proves that no design can do better.

Uniform coverage has radius \(1/[2(K+1)]\); on-policy-only coverage has radius zero. The designed-to-uniform ratio is

\[
 \frac{2(K+1)}{(1+\sqrt K)^2},
\]

which approaches two. For \(K=9\), the exact allocation is \(D_0=1/4,D_j=1/12\), and the radius increases from \(1/20\) to \(1/16\), a 25% improvement.

The one-state Gaussian-information interpretation is closely related to established optimal best-arm allocation; this formula is not presented as a new bandit result. Its role here is an exact reward-validation control and a dual witness that can be checked without implementing a bandit algorithm. [S5]

### 3.5 A costed exact control

For \(K=4\), give the best-action validation coordinate cost five and each other coordinate cost one. Require mean cost at most two. Thus \(D_0\le1/4\), while the unconstrained optimum has \(D_0=1/3\).

The constrained optimum is

\[
 D^*=(1/4,3/16,3/16,3/16,3/16),\qquad
 \Delta^*=3/28.
\]

The unsafe ties occur at \(4/7\). Their uniform mixture has mean squared-error vector

\[
 \bar q=(9/49,4/49,4/49,4/49,4/49).
\]

Using \(\zeta=5/196\) in (18) gives exactly \(3/28\), matching the achieved radius. Uniform coverage is feasible but has radius \(1/10\). All of these certificates are rational.

### 3.6 A nontrivial two-state MDP

The main general control has two states, two actions, initial probabilities \((1/2,1/2)\), discount \(1/2\), and transitions

\[
 P(\cdot\mid0,0)=(3/4,1/4),\quad
 P(\cdot\mid0,1)=(1/4,3/4),
\]

\[
 P(\cdot\mid1,0)=(1/3,2/3),\quad
 P(\cdot\mid1,1)=(2/3,1/3).
\]

Rewards in coordinate order \((0,0),(0,1),(1,0),(1,1)\) are \((1,1/5,3/4,0)\). The bad-policy regret threshold is \(L=2/5\). Deterministic-policy occupancies are computed from the exact discounted flow equations.

The certificate gives

\[
 0.10980874\le\max_D\Delta(D)
 \le0.10981737.
\]

The achieved design, shown rounded, is

\[
 (0.49246014,\ 0.37621640,\ 0.11572322,\ 0.01560023).
\]

Uniform coverage has radius \(0.06822162426614481\). The exact lower certificate already improves it by approximately 61%. The stored design and certificate endpoints are rational; the displayed outer bracket is rounded outward, and the design is rounded for readability.

Six further rational two-state cases, including cost constraints, also achieved their requested certified bracket widths. This is finite experimental evidence about the implementation, not a scalability theorem.

### 3.7 From independent validation samples to a decision certificate

For a frozen learned reward \(\widehat R\), suppose independently sampled validation coordinates follow \(D\), reference rewards at those coordinates are resolved correctly, and

\[
 0\le (\widehat R_i-R_i)^2/c^2\le1.
\]

A one-sided Hoeffding bound gives

\[
 E_D[(\widehat R-R)^2]/c^2
 \le\widehat\varepsilon+\sqrt{\frac{\log(1/\alpha)}{2n}}
\]

with probability at least \(1-\alpha\). If this upper bound is strictly below a certified lower bound on \(\Delta(D)\), all learned-reward-optimal policies satisfy the true regret requirement. A data-dependent learned reward trained on the same validation records needs a separate uniform or held-out argument.

The executed ten-action control freezes \(\widehat R=(1,1/5,\ldots,1/5)\), uses 5,000 samples per design, and assigns error probability 0.025 to each stream, giving a joint 95% comparison.

| Design | Empirical squared error | Error upper bound | Safety radius | Certificate |
|---|---:|---:|---:|---|
| Boundary-designed | 0.029840 | 0.04904646 | 0.062500 | Pass |
| Uniform | 0.035824 | 0.05503046 | 0.050000 | Insufficient evidence |

The uniform result is **not** a conclusion that the learned reward is unsafe. It fails this sufficient confidence gate. The known true errors are 0.030 and 0.036 under the respective sampling distributions, and this frozen reward in fact selects the true best action. The experiment measures certificate power at a fixed sample budget, not realized-policy superiority.

A separate boundary test rejects equality between the allowed error and the safety margin, as required by the source's strict all-maximizers contract.

---

## 4. Verification ledger, integration, and limits

Run `python src/audit.py` from the package directory. It regenerates the certificate and result files. Run `python src/verify_saved.py` to check the saved rational N2 and N5 witnesses without re-solving their optimization problems. This independent verifier uses only the Python standard library and reimplements the certificate checks without importing either optimization module.

| Executed check | Result |
|---|---:|
| Copula CDF endpoint/normalization cases | 200 |
| Copula high-precision Hellinger quadratures | 14 |
| Finite product likelihood/root identities | 8 |
| Resolved-label synthetic N2 samples | 80,000 |
| Rational common-replacement certificates | 1,466 |
| Symmetric validation-family parameter checks | 20 |
| General MDP design brackets | 7 |
| General brackets meeting requested tolerance | 7 |
| Validation coordinates sampled in gate comparison | 10,000 |
| Deliberately corrupted certificates rejected | 2 |

Q812's asymptotic assertions come from the proof, not these tests. Its quadrature and CDF checks are numerical. N2/N5 optimization witnesses and brackets are verified with rational arithmetic. Confidence-radius evaluation uses floating-point logarithms and square roots; all reported gate margins are far from rounding ambiguity. No acquired real-world dataset is used.

### Integration changes justified by this round

The predictive-model registry should record a **density-preservation condition**, not infer it from square-summable weights. For a circular kernel, the Hellinger-series or harmonic finite-entropy criterion is an explicit usable condition. A bounded numerical approximation must be versioned as a different kernel.

A learned representation certificate should identify the raw alphabet, target labels, loss/action family, modeled populations, sample counts, confidence allocation, optimization interval, and model-common replacement witnesses. The h2 experiment gives an example where task preservation is zero even though full reconstruction error is positive.

A reward-validation certificate should identify the occupancy polytope, reference reward, regret threshold, design feasibility constraints, lower projection witnesses, upper adversarial mixture, validation cutoff, and frozen learned-reward version. It should distinguish safe, witnessed unsafe, and insufficiently validated.

These controls complement the preceding round's persisted D10 job. They do not alter that job or certify the original scaffold's code. No theorem here grants source fidelity, causal identification, or correctness of a chosen model class merely because its numerical certificate is valid.

### External status and priority

The journal source inspected for Q812 explicitly retains the fixed-copula square-summability question. However, an author-maintained publication list also lists a submitted 2026 manuscript, **Dreassi, Pratelli, and Rigo, “On the limit of copula based predictive distributions.”** Its contents were not available in the retrieved materials. A related accessible 2026 note, *Some cautionary tales about Bayesian predictive inference*, concerns distinct data-generating and asymptotic-exchangeability issues. Consequently this report supplies a self-contained mathematical answer but does **not** claim publication priority or an exhaustive novelty audit. [S1, S6, S7]

## Source notes

[S1] Garelli, Leisen, Pratelli, Rigo, *Asymptotics of predictive distributions driven by sample means and variances*, Journal of Applied Probability (2026), Section 2.3, Theorems 3–4 and the question following equation (6). Inspected full HTML: https://www.cambridge.org/core/journals/journal-of-applied-probability/article/asymptotics-of-predictive-distributions-driven-by-sample-means-and-variances/491E3396D1B3AEFB86ACEF1B54D0CCFA . Earlier arXiv text: https://arxiv.org/html/2403.16828v3 .

[S2] Supplied `Open_Problems_for_the_Bayesian_Knowledge_System_Collection_9(2).txt`, Q812; supplied `01_solutions(1).md`, Section 8. These supply the precise question and previous restricted second-moment argument.

[S3] Supplied `02_project_review(1).md`, N2 and N5. These supply the new project targets and the requirement to charge estimation/construction and protect common-policy semantics.

[S4] Supplied `01_solutions(1).md`, Q724 and H1/H3. These supply the squared-error safety contract, h2 experiment, and deficiency quantifiers. Established feature-learning precedent: van Rooyen and Williamson, *Le Cam meets LeCun: Deficiency and Generic Feature Learning* (2014), https://arxiv.org/abs/1402.4884 .

[S5] Garivier and Kaufmann, *Optimal Best Arm Identification with Fixed Confidence* (COLT 2016), https://proceedings.mlr.press/v49/garivier16a.html . Cited as an established allocation/alternative-model precedent, not as a source for the full N5 occupancy formulation. Reward-safety starting point: Fluri et al. (ICML 2025), https://proceedings.mlr.press/v267/fluri25a.html .

[S6] Pietro Rigo, author-maintained publication list, Submitted section, retrieved 5 October 2026: https://www.unibo.it/sitoweb/pietro.rigo/publications . The named copula-limit manuscript is listed but its theorem content is not supplied there.

[S7] Dreassi, Leisen, Pratelli, Rigo, *Some cautionary tales about Bayesian predictive inference* (2026), inspected HTML: https://arxiv.org/html/2607.19206v1 .
