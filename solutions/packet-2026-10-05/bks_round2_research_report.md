# New targets: identification, calibrated feedback, and fixed-model acquisition

**Bayesian Knowledge System — research continuation — 5 October 2026**

## Results and selection

This round addresses **Q418**, **Q414**, and the review's **N3/D10** project target, with **N1 consumed-information checks** integrated into the executable demonstration. It does not repeat Q413, Q725, Q449, or Q810 from the preceding round.

| Target | Result | Scope |
|---|---|---|
| Q418 | The exact generic finite-to-one identification threshold is **n = 2ℓ+1**. A rare-component Jacobian argument proves sufficiency and matches the dimension lower bound. | Full stated binary-latent identification target. Not global uniqueness, stable estimation, or an efficient fitting algorithm. |
| Q414 | Regret at most **2√2 U√(mT)** without a log(action-count) factor. An exactly calibrated two-expert construction gives a matching **Ω(U√(mT))** lower bound on explicit alphabet families. | Worst-case order over the demonstrated families; not an instance-by-instance classification of fixed alphabets or utilities. Exact calibration can still eliminate regret in favorable cases. |
| N3 / generated D10 | A finite model-aware state contract, a coarsest exact predictive quotient under that contract, and a fixed-model common-policy minimax solver. | Exact finite-horizon control, not an unrestricted approximation theorem for the catalogue's acquisition problems. |
| N1 integration | A stored job whose consumed observations, conditional updates, action costs, reference-prior forecast, and scores are reconstructed after closing and reopening its database. | New standalone control; existing source-fidelity or production-scaffold claims are not assumed. |

Q414 and D10 change the immediate aggregation/acquisition interface. Q418 is a deliberately conditional branch: the threshold matters only after adopting its multiplicative latent model. Its value is an exact identification control rather than a justification for adopting that representation.

The supplied review's priority is an integrated, reconstructible decision demonstration [F2, §8]. The new D10 execution supplies that demonstration and records a null result as well as failures: the best fixed query order ties the adaptive optimum on this two-acquisition instance.

All mathematical claims below rest on the written arguments. Computation checks the formulas and implementations; it is not a substitute for the all-dimension arguments. The work has not received independent peer review or proof-assistant verification. The targeted external check establishes no exhaustive novelty or publication-priority claim.

## 1. Q418: the sharp product-of-experts identification threshold

### 1.1 Contract and observable information

There are ℓ independent latent bits

\[
U_j\sim\operatorname{Bernoulli}(\pi_j),\qquad 0<\pi_j<1.
\]

Given U, the n binary observables are conditionally independent and identically distributed, with

\[
\Pr(X_i=1\mid U)=Z(U)=\prod_{j=1}^{\ell}\alpha_{j,U_j},
\qquad 0<\alpha_{jb}<1.
\]

The target is generic finite-to-one identification modulo the declared continuous rescalings and finite latent-label/permutation symmetries. This is the supplied question's meaning of local identification [F4, Q418]. The originating paper supplies a sufficient observable count of 4ℓ+1 for general priors [P1].

Define the quotient coordinates

\[
A=\prod_j\alpha_{j0},\qquad b_j=\alpha_{j1}/\alpha_{j0}.
\]

The continuous rescaling symmetry is removed by retaining A and the b_j. The quotient has the **2ℓ+1** coordinates

\[
(A,\pi_1,b_1,\ldots,\pi_\ell,b_\ell).
\]

Its physical domain is an open semialgebraic set. For fixed positive b_j, the feasible A form the interval

\[
0<A<\prod_j\min(1,1/b_j).
\]

The observable joint law is equivalent to its first n success moments

\[
\mu_t=\Pr(X_1=\cdots=X_t=1)
=A^t\prod_{j=1}^{\ell}\left[1+\pi_j(b_j^t-1)\right],
\quad 1\le t\le n,
\tag{1}
\]

with μ_0=1. Indeed, the probability of any specified output pattern containing k ones is

\[
\mathbb E[Z^k(1-Z)^{n-k}]
=\sum_{r=0}^{n-k}(-1)^r\binom{n-k}{r}\mu_{k+r}.
\tag{2}
\]

Thus n coordinates of observable information are available. When n<2ℓ+1, the maximum-rank theorem applied on the open quotient domain gives positive-dimensional generic fibers. Such fibers cannot be eliminated by the remaining finite symmetries.

**Necessity:** n≥2ℓ+1.

### 1.2 Sufficiency by a rare-component limit

**Theorem 1.** For every ℓ≥1, the first **2ℓ+1 consecutive moments** generically identify the quotient parameters up to a finite ambiguity. Consequently,

\[
\boxed{n_{\mathrm{loc}}(\ell)=2\ell+1.}
\tag{3}
\]

**Proof.** Work locally with a=log A and log moments L_t=log μ_t. Both coordinate changes are nonsingular on the physical domain. Write

\[
q_{jt}=1+\pi_j(b_j^t-1).
\]

The Jacobian entries are

\[
\partial_a L_t=t,\qquad
\partial_{\pi_j}L_t=\frac{b_j^t-1}{q_{jt}},\qquad
\partial_{b_j}L_t=\frac{\pi_j t b_j^{t-1}}{q_{jt}}.
\tag{4}
\]

Choose pairwise distinct b_j>0 with b_j≠1. Set every π_j=ε>0 and divide each b_j derivative column by ε. As ε decreases to zero, the resulting matrix tends to the square matrix M, whose rows are indexed by t=1,…,2ℓ+1:

\[
M_{t,0}=t,\quad
M_{t,2j-1}=b_j^t-1,\quad
M_{t,2j}=t b_j^{t-1}.
\tag{5}
\]

This matrix is nonsingular. To prove it, suppose c=(c_1,…,c_{2ℓ+1}) is in its left kernel and set

\[
P(x)=\sum_{t=1}^{2\ell+1}c_t x^t.
\]

The kernel equations give

\[
P'(1)=0,\qquad P(b_j)=P(1),\qquad P'(b_j)=0.
\]

Therefore Q(x)=P(x)−P(1) has a double zero at each of the ℓ+1 distinct points

\[
1,b_1,\ldots,b_\ell.
\]

But deg Q≤2ℓ+1, whereas the zeros have total multiplicity 2ℓ+2. Hence Q is identically zero. P is constant, and P(0)=0 forces P≡0. Thus c=0.

Continuity now implies nonsingularity of the original Jacobian for sufficiently small **positive** ε. The argument does not claim identification at the degenerate boundary ε=0. A physical choice of A always exists; for b_j=j+1, one can take α_j0=1/(ℓ+2) and α_j1=(j+1)/(ℓ+2).

The moment map (1), in coordinates (A,π,b), is polynomial. A nonzero Jacobian at one physical point proves that its determinant is not the zero polynomial. It therefore has full rank generically. Generic fibers are zero-dimensional semialgebraic sets and hence finite. Equivalently, the polynomial map is generically finite onto its image. This proves sufficiency and, with the dimension lower bound, (3). ∎

An exact determinant identity strengthens the certificate:

\[
\det M
=\prod_{j=1}^{\ell}(b_j-1)^4
\prod_{1\le i<j\le\ell}(b_j-b_i)^4.
\tag{6}
\]

It follows by taking the confluent Vandermonde matrix with value and first-derivative columns at 1,b_1,…,b_ℓ, subtracting the value-at-1 column from the other value columns, and expanding along its degree-zero row. The polynomial-kernel proof above does not depend on remembering the determinant's sign convention.

### 1.3 Categorical-latent extension

The same argument extends beyond the catalogue's binary case.

Suppose independent latent variable j has r_j known categories, all probabilities unknown and positive, and the conditional success probability is again the product of one factor per latent variable. Use one category per factor as the baseline and put

\[
K=\sum_j(r_j-1).
\]

After removing the same baseline-factor rescalings, there are 2K+1 parameters. The moments are

\[
\mu_t=A^t\prod_j\left[1+
\sum_{b=1}^{r_j-1}\pi_{jb}(\beta_{jb}^t-1)\right].
\]

Set every nonbaseline probability to ε and choose all K ratios β_jb distinct and different from 1. The scaled limiting Jacobian is precisely (5) with K ratios. The physical simplex constraints hold for sufficiently small ε. Therefore the sharp generic finite-to-one threshold in this extension is

\[
\boxed{n=2\sum_j(r_j-1)+1.}
\tag{7}
\]

This corollary is a derivation of the present argument, not a result attributed to [P1].

### 1.4 What this does not establish

A finite fiber can contain multiple inequivalent parameter points. The theorem is not global uniqueness modulo the advertised symmetries. It also gives no polynomial-time reconstruction algorithm and no uniform conditioning or sample-complexity guarantee.

The difference between observable coordinates and independent training jobs is important. Fix a latent component of probability ε and change only that component's emission factor. Couple two models using the same latent draw and the same conditional observations whenever that component is absent. The n-observable laws then satisfy

\[
\operatorname{TV}(P_n,Q_n)\le\varepsilon
\]

for **every n**. For J independent jobs,

\[
\operatorname{TV}(P_n^{\otimes J},Q_n^{\otimes J})\le J\varepsilon.
\]

Distinguishing the two parameter points with both error probabilities at most 1/3 requires TV≥1/3, hence J≥1/(3ε). This is only a simple lower bound, not a sharp statistical rate. It is enough to show why (3) must not be advertised as a uniform data-efficiency guarantee.

### 1.5 Executed controls

`src/identifiability.py` uses exact rational derivatives, not finite differences. The audit checks:

- 48 exact rational instances of determinant identity (6), through ℓ=6.
- 40 physical interior full-rank witnesses, through ℓ=40, by nonzero modular determinants of rational Jacobians. A denominator is checked to be invertible modulo the reported prime before reduction. The largest matrix is 81×81.
- 12 singular-boundary controls, including zero latent probabilities and a unit emission ratio.
- Nine exact count-law TV controls for the rare-component coupling.

The all-ℓ proof is §1.2. The finite checks are recorded in `results/q418_checks.json`.

## 2. Q414: the worst-case state-feedback rate, including exact calibration

### 2.1 Scope and theorem

At time t, the learner sees a forecast profile e_t from a known finite set E, |E|=m, chooses an action, and then observes the binary state y_t. Utilities u(a,y) are known and satisfy |u(a,y)|≤U. The comparator chooses one fixed action per profile in hindsight.

The calibration promise is **empirical marginal calibration at the horizon**, as in the supplied Q414 [F4]. It is not the one-shot truthful-Bayesian-posterior assumption of Q407/Q408, and it is not Q413's iid profile law. The lower-bound sequences below need not have iid profiles.

The source's contextual Hedge bound has an additional √log d factor [P2, Theorem 3]. Binary outcomes allow a smaller optimization space.

**Theorem 2 (upper bound).** For every fixed input sequence and every finite action set,

\[
\boxed{\mathbb E\operatorname{Reg}'_T
\le 2\sqrt2\,U\sqrt{mT}.}
\tag{8}
\]

Calibration is not required for (8). The trivial 2UT bound can be used when it is smaller.

**Theorem 3 (exact-calibration lower bound).** For every k,N≥1 there is a fixed pair of forecast alphabets with

\[
m=(k+2)^2,\qquad T=5k^2N,
\]

and a distribution over **exactly empirically calibrated** deterministic input sequences, such that every learner has worst-case expected regret at least

\[
\boxed{2Uk^2\,\mathbb E\left|\operatorname{Bin}(N,1/2)-N/2\right|
\ge Uk^2\sqrt{N/3}.}
\tag{9}
\]

The utilities need only two actions. More actions can be added without changing their convex hull. Since k/(k+2)≥1/3,

\[
Uk^2\sqrt{N/3}
=\frac{Uk}{\sqrt{15}}\sqrt T
\ge\frac{U}{3\sqrt{15}}\sqrt{mT}.
\tag{10}
\]

Thus the √(mT) worst-case order is attained, including at calibration tolerance zero, on these explicit alphabet families. Any positive tolerance also admits this lower-bound family.

This is not a claim that every fixed alphabet geometry, utility table, or single-expert problem has that minimax value. Section 2.4 gives a contrary favorable case.

### 2.2 Proof of the upper bound: optimize utility pairs, not action weights

Associate action a with

\[
v_a=(u(a,0),u(a,1))\in[-U,U]^2,
\quad C=\operatorname{conv}\{v_a:a\in\mathcal A\}.
\]

An element x of C is the expected utility pair of a randomized action. The diameter of C is at most D=2√2 U. A point in C can be implemented using at most three hull vertices by a planar triangulation.

Maintain a separate vector x_e∈C for each profile. After observing state y on a visit to e, perform projected gradient ascent

\[
x_e\leftarrow\Pi_C(x_e+\eta e_y),\qquad
\eta=D\sqrt{m/T},
\tag{11}
\]

where e_0=(1,0), e_1=(0,1). If all actions have the same utility vector, regret is zero and no update is needed.

For a comparator x*∈C, projection nonexpansiveness gives

\[
e_y\cdot(x^*-x)
\le\frac{\|x-x^*\|^2-\|x^+-x^*\|^2}{2\eta}
+\frac\eta2\|e_y\|^2.
\]

Sum this inequality over visits to each profile, then over profiles. The comparator is allowed a different x*_e in each context. At most m initial squared-distance terms occur, each at most D², and each gradient has norm one. Therefore

\[
\operatorname{Reg}'_T\le\frac{mD^2}{2\eta}+\frac{\eta T}{2}
=D\sqrt{mT}.
\]

Randomizing among actions that realize x gives this expected payoff, proving (8). This is a specialization of projected online convex optimization, not a claim that the optimization method itself is new. The application removes the action-count dependence because the payoff geometry is two-dimensional.

The guarantee is for fixed sequences, and more generally the usual nonanticipating feedback setting. It does not allow an adversary to observe the learner's current private action sample before selecting its outcome.

### 2.3 Proof of the lower bound: defer calibration compensation to other profiles

Fix k,N. Give both experts the fixed alphabet

\[
\{0,1,v_0,\ldots,v_{k-1}\},\qquad
v_i=\frac{k+i}{3k}\in[1/3,2/3).
\tag{12}
\]

These alphabets depend on k, **not on N**.

First present each central profile (v_i,v_j) exactly N times, in a predetermined order. Generate all k²N central labels as independent fair bits. Let K_i be the number of ones in central row i and L_j the number in central column j. Thus 0≤K_i,L_j≤kN.

After **all** central observations, append row anchors. For each i, set

\[
b_i=3kNv_i-K_i=N(k+i)-K_i,\qquad
 a_i=2kN-b_i.
\]

Append a_i occurrences of profile (v_i,0) with label zero and b_i occurrences of (v_i,1) with label one. Both counts are nonnegative. In the first expert's report-v_i group, the total count is 3kN and the positive count is

\[
K_i+b_i=3kNv_i.
\]

That group is therefore exactly calibrated.

Do the analogous construction for each column j:

\[
d_j=3kNv_j-L_j,\qquad c_j=2kN-d_j,
\]

using c_j zero-labelled profiles (0,v_j) and d_j one-labelled profiles (1,v_j). These make the second expert's report-v_j groups exactly calibrated. Every report 0 is attached only to zero labels, and every report 1 only to one labels, so the remaining groups are calibrated too.

The horizon is deterministic:

\[
T=k^2N+2k^2N+2k^2N=5k^2N.
\]

Take two actions that predict zero or one, with utility +U for a correct prediction and −U otherwise. During every central phase, the current outcome is independent of the learner's history, forecast profile, and action randomization. The learner's expected central utility is zero.

For a central profile containing K ones, the best fixed prediction has utility U|2K−N|. All anchor profiles have deterministic labels, so the hindsight comparator earns U on every anchor; no learner can do better there and recover its central regret.

Hence expected regret is at least

\[
2Uk^2\,\mathbb E|\operatorname{Bin}(N,1/2)-N/2|.
\]

This is a distribution over sequences that can be completely generated before play. Averaging implies a worst deterministic sequence for each learner; no action-reactive adversary is needed.

For the explicit constant, write S_N as a sum of N independent fair signs. Then

\[
\mathbb E S_N^2=N,\qquad
\mathbb E S_N^4=3N^2-2N.
\]

Hölder interpolation gives

\[
\mathbb E|S_N|
\ge\frac{(\mathbb E S_N^2)^{3/2}}{(\mathbb E S_N^4)^{1/2}}
\ge\sqrt{N/3}.
\]

Since |Bin(N,1/2)−N/2|=|S_N|/2, this proves (9). ∎

The construction identifies the obstruction: **marginal calibration can be repaired by reports arriving after the decisions that incur regret, in contexts where the outcome is deterministic**. Marginal calibration therefore does not create profile-wise predictability.

### 2.4 Calibration can still be decisive in a favorable contract

With one expert, a profile is just a reported value v. Under exact empirical calibration, its empirical outcome frequency is exactly v. Choosing

\[
a^*(v)\in\arg\max_a\{(1-v)u(a,0)+vu(a,1)\}
\]

on every occurrence attains the profile's hindsight value exactly. No state feedback is needed, and regret is zero.

If each report group's empirical error is at most ε, the same policy incurs regret at most

\[
4U\varepsilon T.
\tag{13}
\]

To see this, compare the utility lines of the hindsight-optimal and report-optimal actions at the actual empirical frequency r and at v. Their slope difference is at most 4U, and the comparison at v is nonpositive. The group regret is therefore at most 4U|r−v| times its size.

Thus a full answer to the *instance-specific* question must retain the geometry of the forecast alphabets and calibration groups. The worst-case result does not erase useful favorable structure.

### 2.5 Executed controls

The audit constructs and exactly verifies **1,294** lower-bound sequences exhaustively over their central bits, plus **100** larger generated sequences. It verifies the binomial lower-bound inequality with rational arithmetic for N=1,…,128.

The numerical OGD implementation works over a two-dimensional convex hull and constructs an action mixture of support at most three. Its two-action and 1,000-action duplicate-hull runs have identical regret. Twenty additional utility-hull runs check mixture reconstruction and the regret bound. Sixty one-expert controls verify the zero-regret favorable case.

The calibration equalities and binomial checks are exact. Projection and OGD payoffs use floating-point arithmetic. None of these generated runs estimates real-world forecast value.

## 3. N3: exact model-aware continuation states

### 3.1 Why the model must remain in the state

The supplied solutions already show that a scalar posterior for the immediate target can lose information needed for the next query [F3, H2]. That counterexample is a starting control, not a new result of this round.

A second distinction matters for implementation: even equality of every model's *conditional* future kernel need not preserve the information a history supplies about **which model holds**. A reusable state must also retain the likelihood ratios between models, unless a stronger task-specific argument makes them irrelevant.

Let the fixed episode model be m∈{1,…,M} and let ω range over a finite latent world. All queried outputs are deterministic functions of the once-drawn world in the D10 control. More general finite kernels can be represented by including their pre-drawn randomness in ω.

Choose a full-support reference prior q_m, used only for representation. Define

\[
Q(m,\omega)=q_mP_m(\omega),\qquad
b_h(m,\omega)=Q(m,\omega\mid h).
\tag{14}
\]

The actual control objective remains minimax over fixed models; q is not substituted for that objective. The state includes b_h, remaining horizon, and the resource/access contract. For any prior λ on models,

\[
P_\lambda(m,\omega\mid h)
\propto\frac{\lambda_m}{q_m}b_h(m,\omega).
\tag{15}
\]

Thus one full-support reference belief can serve every later declared prior without manufacturing independence or resetting the episode model.

### 3.2 Exact vector recursion and the fixed-model quantifiers

Let L be total query cost plus terminal loss. For a common policy π,

\[
R_m(\pi)=\mathbb E_m L
=\mathbb E_Q\left[\frac{\mathbf1\{M=m\}}{q_m}L\right].
\tag{16}
\]

At reference belief b, define a vector immediate cost for querying q by

\[
g_m(b,q)=\frac{b(M=m)}{q_m}\,c_q,
\]

and a vector terminal cost for stopping with a by

\[
g_m(b,a)=\frac1{q_m}\sum_\omega b(m,\omega)\ell(H(\omega),a).
\]

Let K(b,q,z) be the reference-prior probability of the next output z and B(b,q,z) the posterior update. The attainable continuation risk-vector set satisfies

\[
\mathcal C_t(b)=\operatorname{conv}\left(
\{g(b,a):a\text{ terminal}\}\ \cup\
\bigcup_{q\text{ feasible}}
\left\{g(b,q)+\sum_zK(b,q,z)v_z:
 v_z\in\mathcal C_{t-1}(B(b,q,z))\right\}
\right).
\tag{17}
\]

Budget and access variables are suppressed in the notation but are part of each successor state. At the root,

\[
\boxed{V^*=\min_{v\in\mathcal C_H(b_0)}\max_m v_m.}
\tag{18}
\]

Equation (17) follows from the tower property under Q: choose one initial randomized action, then one continuation policy for each observed branch. Conversely, any choices in (17) can be implemented by one common policy. Induction on the remaining horizon proves equality.

The component for model m is retained all the way to the root. Replacing every continuation vector by its coordinatewise worst scalar before combining branches is not generally equivalent to (18). The review's fixed-model-versus-branch-switching example is retained as a regression control [F2, §1, Change 3].

The sets in (17) can have many vertices. This is an exact finite specification, not a compact-model polynomial-time complexity claim.

### 3.3 The coarsest exact quotient for a declared predictive contract

The implemented finite contract preserves:

1. Remaining horizon and the exact remaining budget, including their reporting values.
2. The reference-prior posterior over episode models.
3. Every available terminal action's conditional expected loss in every still-possible model.
4. Every allowed query's labeled outcome probabilities in each model and the successor class for each outcome.

Zero-probability model/history pairs are explicitly marked as impossible rather than smoothed.

Two terminal histories have the same signature when items 1–3 agree. At a nonterminal history, add the query signatures in item 4, referring recursively to already assigned child classes. Assign equal class identifiers exactly when signatures agree.

**Proposition 4.** This backward construction is a deterministic updateable state representation preserving the declared contract. Among deterministic representations required to preserve that same contract, its equivalence relation is the coarsest one.

**Proof.** Equal signatures give identical current outputs, available actions, and query probabilities, and each common observed outcome leads to the same child class. Induction therefore preserves the law of every permitted future labeled interaction and all declared terminal losses. The retained model posterior converts these per-model laws into the same reference-prior transitions and vector costs in (17), so common-policy optimization is preserved.

For minimality under the contract, any two histories assigned the same state must have identical required current outputs. Their identical input query and output value must lead to the same next state. If their backward signatures first differ at depth r, this is either an immediate required-output difference or, after a positive-probability common output, a depth-(r−1) difference. Induction rules out their merger. ∎

This is not a minimum-memory theorem for one fixed utility, an approximate posterior, or the entire software system. A weaker decision-only contract can admit more merging. The exact remaining budget and returned output labels are deliberately preserved here because the control also audits accounting and consumed information.

### 3.4 An explicit approximation transfer bound

A bounded extension follows once a **common causal policy transfer** is actually certified. Suppose, for every fixed model, a transferred policy's joint terminal-state/priced-transcript law is within TV distance ε of the original, with terminal loss in [0,1] and total query cost at most B. Then

\[
|R_m(\pi)-R_m(\widetilde\pi)|\le(1+B)\varepsilon.
\tag{19}
\]

This follows directly by integrating a [0,1+B]-valued loss against the two laws. If transfers in both directions have this guarantee, using an optimal abstract policy in the original problem loses at most

\[
2(1+B)\varepsilon
\]

relative to the original minimax optimum. A common stepwise coupling whose failure probability is at most η per acquisition, and which also protects the terminal decision variables, gives ε≤Hη by the union bound.

The policy transfer must be common across models. Merely fitting model-specific decoders or comparing target posteriors is insufficient. This bound prices an existing approximation certificate; it does not learn one, find a smallest approximate state, or optimize refresh costs. Those portions of N3 remain outside the completed result.

## 4. Executed D10: from latent draw to a persisted score

### 4.1 Source-derived and newly chosen parts

The generator, twelve models, query meanings, target, and terminal losses are from the supplied review [F2, §4]. The rational query costs and budget below are **new choices for this run**, not values attributed to an unattached protocol file.

Each job draws a fair H, an independent uniform three-bit nuisance A, a source S of accuracy p, a fresh verifier W of accuracy q, and an independent copying switch C with probability ρ. S and W are conditionally independent given H. Put V=S when C=1 and V=W otherwise. The raw source is (A,S).

The fixed model alternatives are

\[
p\in\{2/3,4/5\},\quad q\in\{3/5,3/4\},\quad
\rho\in\{0,1/2,1\}.
\]

A model is fixed for the whole job. All report values are drawn once. Querying a report again does not redraw it.

| Query | Output | Cost |
|---|---|---:|
| A | Nuisance feature | 1/1000 |
| S | Source answer | 1/200 |
| S_repeat | Exact same source answer | 1/200 |
| V | Partially copied verifier | 1/500 |
| W | Fresh verifier | 1/100 |
| RAW | Full (A,S) source record | 1/125 |

At most two acquisitions are permitted; total query cost is at most 3/100. Terminal actions predict 0, predict 1, or abstain. Wrong classification costs one, correct classification zero, and abstention 3/10. The complete machine-readable contract is `protocol.json`.

### 4.2 Common-policy sequence-form program

The implementation explicitly builds each reachable history. A variable x_(h,a) is the product of the policy's action probabilities along its own action sequence through h and a; it does **not** include the chance probability of the history.

At the root, the outgoing variables sum to one. At a later node, their sum equals the realization variable of its parent query, identically for every possible returned output. For each model,

\[
R_m(x)=
\sum_{h,q} P_m(h)c_qx_{h,q}
+\sum_{h,a\text{ terminal}}
\mathbb E_m[\mathbf1_h\ell(H,a)]x_{h,a}.
\tag{20}
\]

The minimax LP minimizes v subject to the realization equalities, x≥0, and R_m(x)≤v for all twelve models. One x is used under every model. This prevents the policy from using the true hidden model or the adversary from changing it after an answer.

There are **461 history nodes** and **1,581 realization variables**, plus the scalar objective variable. SciPy discovers a numerical solution. Its policy, equality dual, and least-favorable prior are rationally reconstructed and verified against the original Fraction coefficients.

For the minimax certificate, the verifier checks primal feasibility, nonnegative model weights λ summing to one, and

\[
E^Ty\le\sum_m\lambda_mR_m
\]

on every free nonnegative realization variable. Equality of the primal value with y_0 proves zero duality gap. The reported optimum is therefore backed by exact primal and dual witnesses, not an LP solver status alone.

A separate latent-world evaluator computes policy risks directly. An independent rational scalar dynamic program is used only for known-model or declared-prior Bayesian comparisons, where that recursion is legitimate.

### 4.3 Exact optimum and a short analytic proof

A common optimal policy buys S and W, predicts their common value on agreement, and abstains on disagreement. The query order can be reversed.

For this policy,

\[
R_{p,q,\rho}=rac3{200}+(1-p)(1-q)
+\frac3{10}\left[p(1-q)+(1-p)q\right].
\tag{21}
\]

The risk does not depend on ρ and decreases in both p and q. At p=2/3,q=3/5,

\[
(1-p)(1-q)=2/15,\quad
\Pr(S\ne W)=7/15.
\]

Hence

\[
\boxed{V^*=rac3{200}+\frac2{15}+\frac3{10}\frac7{15}
=\frac{173}{600}=0.288333\ldots.}
\tag{22}
\]

For an independent analytic lower bound, take the single fixed model p=2/3,q=3/5,ρ=1/2. No individual answer has enough accuracy to beat abstention. After the pair (S,V), the smaller posterior error is 7/23 on agreement and 3/7 on disagreement. After (W,V), it is 8/23 on agreement and 3/7 on disagreement. All exceed 3/10, so neither pair changes the optimal terminal action from abstention. Repeats add no information, A is independent nuisance, and RAW is a more expensive route to S for this target. The only beneficial pair is S,W, giving (22). Thus even a known-model oracle cannot beat (22) in this particular model, while the common policy attains it in the worst case.

Under the **uniform declared prior** on models, the same terminal rule and the same pair are Bayes-optimal. Their average risk is

\[
\boxed{1363/6000=0.227166\ldots.}
\]

This equality of deployed policies is an observed feature of this control, not a general equivalence of Bayesian and minimax planning.

### 4.4 Comparison results, including the null result

| Policy / comparison | Uniform-prior average loss | Worst-model loss |
|---|---:|---:|
| No query; abstain | 3/10 = 0.300000 | 3/10 = 0.300000 |
| Fixed-model common-policy minimax | 1363/6000 = 0.227167 | 173/600 = 0.288333 |
| Uniform-prior Bayes-optimal | 1363/6000 = 0.227167 | 173/600 = 0.288333 |
| Best fixed query order, S then W | Same S,W rule attains 1363/6000 | 173/600 = 0.288333 |
| Target-entropy-per-cost greedy | 2957/12000 = 0.246417 | 1021/3000 = 0.340333 |
| Full-latent-entropy-per-cost greedy | 1793/6000 = 0.298833 | 403/1000 = 0.403000 |
| True-model oracle, not a common deployable policy | 82/375 = 0.218667 | 173/600 = 0.288333 |

Both entropy heuristics use the uniform reference prior, acquire while positive information gain remains within the two-query contract, and use the Bayes-optimal terminal action at their resulting history. They differ in their information target. This definition is recorded to avoid equating entropy with monetary loss reduction.

The target-entropy heuristic buys V and then the source feature; a complete copy can masquerade as corroboration in its terminal decision. The full-latent-entropy heuristic buys the three-bit nuisance A and then V. Its first query has no information about H. Both are nevertheless evaluated using the correct conditional model; these failures do not rely on deliberately multiplying independent likelihoods.

All 43 deterministic query schedules of length zero, one, or two were optimized with observation-dependent stopping and common terminal rules. The best schedule ties the unrestricted adaptive minimax LP. **There is no demonstrated adaptivity advantage at this horizon and cost schedule.** The result should not be replaced by a more favorable claim.

The 45 exact primal-dual certificates consist of the unrestricted minimax solve, one uniform-prior solve, and those 43 schedule-restricted solves. Twelve additional known-model oracle values come from the exact independent DP.

### 4.5 State quotient and memory accounting

The declared signature construction reduces **461** reachable history nodes to **70** continuation classes. A second exact Bayesian dynamic program on the quotient returns the same root value 1363/6000.

A class identifier fits in seven bits rather than the nine bits needed to index 461 explicit nodes. This comparison prices only the identifier. Model definitions, rational constants, the transition table, action rules, and the evidence archive remain additional storage. It is not a claim of a seven-bit Bayesian system or globally minimum decision-only memory.

The quotient includes the model-posterior likelihood vector. Dropping that vector simply because model-conditional kernels look the same would not be licensed by Proposition 4.

### 4.6 Consumed-information controls and a persisted job

The exact regression controls are:

\[
P(H=1)=P(H=1\mid A=5)=1/2,
\]

\[
P(H=1\mid A=5,S=1)=11/15,
\]

\[
P(H=1\mid S=1,S_{\mathrm{repeat}}=1)=11/15,
\]

and, for the partially copied verifier under the uniform model prior,

\[
P(H=1\mid S=1,V=1)=737/949.
\]

The first three implement the distinction in the supplied H2 result: shared ancestry is not full information consumption, but a true deterministic repeat is neutral. They are regression integrations of that existing result, not another claimed solution of it.

`results/d10_replay.sqlite` stores an actual synthetic job with seven append-only, hash-chained events. A raw record (A=5,S=1) is stored without being automatically consumed by inference. The common policy observes W=1 and then S=1, pays 3/200, and predicts one. Under the explicitly declared uniform reference prior,

\[
P(H=1\mid W=1,S=1)=297/349,
\]

while the model-conditional probabilities range from 3/4 to 12/13. The reference probability is a separately identified scoring forecast, not an assertion that the evidence uniquely determines one posterior across the model class.

The synthetic resolution is H=1. The stored and recomputed scores are

\[
\text{Brier}=\left(1-\frac{297}{349}\right)^2
=\frac{2704}{121801},
\]

\[
\text{log loss}=-\log(297/349)=0.1613397833997276\ldots,
\]

and total realized decision loss is 3/200, entirely query cost. The database is closed and reopened before replay. Conditional likelihood ratios, posterior vectors, spent budget, forecast, and score are reconstructed from the protocol and **consumed observations**, rather than from the stored raw bytes or the later resolution.

A test update to an existing event is rejected by an append-only trigger. Hash chaining checks the stored sequence against its retained hashes; it is not a substitute for externally trusted signing or an adversarial storage-security proof. No semantic source-fidelity guarantee is inferred from a hash.

## 5. Verification ledger, deliverables, and limits

### 5.1 Executed verification

| Check | Outcome |
|---|---:|
| Q418 exact limiting-determinant identities | 48 |
| Q418 rational interior full-rank witnesses | 40, through ℓ=40 |
| Q418 singular controls | 12 |
| Q418 exact rare-component TV examples | 9 |
| Q414 exhaustive exactly calibrated sequences | 1,294 |
| Q414 additional generated exactly calibrated sequences | 100 |
| Q414 exact binomial lower-bound checks | 128 |
| Q414 one-expert zero-regret controls | 60 |
| Q414 extra numerical utility-hull checks | 20 |
| D10 rational primal-dual optimality certificates | 45 |
| D10 known-model exact DP oracles | 12 |
| D10 reachable histories / exact continuation classes | 461 / 70 |
| Persisted D10 event records | 7 |
| Reopened forecast / cost / score reconstruction | Passed |

### 5.2 Reproduction

From the extracted package root:

```bash
python -m pip install -r requirements.txt
python src/audit.py
```

The verification run used Python 3.13.5, NumPy 2.3.5, and SciPy 1.17.0. The exact mathematical routines use Python's rational arithmetic. NumPy is used for numerical utility-hull OGD; SciPy discovers LP candidates whose advertised exact optimality is subsequently checked rationally.

`results/audit_stdout.txt` and `results/summary.json` record the executed checks. `results/d10_minimax_certificate.json` contains the primal realization, equality dual, least-favorable prior, per-model risks, and policy. `results/d10_state_quotient.json` records every history-to-class assignment. The source files are self-contained and do not call a model API or access an external dataset.

### 5.3 Scope remaining

Q418's sharp population identification threshold is proved; global uniqueness, fitting complexity, and robust statistical estimation remain separate targets.

Q414's action-count dependence and worst-case square-root rate are addressed. Exact minimax constants and a complete classification for each fixed forecast alphabet/utility geometry are not claimed.

N3 is answered here for a finite exact predictive contract and a generated two-acquisition control. A learned approximate state certificate, minimum total storage, refresh optimization, or scalable acquisition guarantee in compact model representations is not supplied. The general catalogue questions surrounding decision trees and latent-mixture search are not relabeled as solved.

The new programs are standalone reference controls. They do not modify, rerun, or certify the original scaffold's reported tests. No real-world calibration, forecasting advantage, sensor fidelity, or economic benefit has been established by these synthetic experiments.

## Source register

**[F1]** `03_research_map(1).md`, especially the active portfolio and the distinction between project relevance and mathematical scope.

**[F2]** `02_project_review(1).md`, §4 (generated D10), §7 N1/N3, and §8 (integrated milestone).

**[F3]** `01_solutions(1).md`, §9 H2 (consumed information and model-aware query choice), §10 H3 (common-policy task comparison). These are earlier supplied results, not this round's discoveries.

**[F4]** `Open_Problems_for_the_Bayesian_Knowledge_System_Collection_5(2).txt`, Q414 and Q418, including their shared contracts and qualifications.

**[P1]** Gordon, Kant, Ma, Schulman, and Staicu. *Identifiability of Product of Experts Models*. AISTATS 2024, PMLR 238, pp. 4492–4500; arXiv:2310.09397. The source supplies the model and previous general-prior sufficient observable count. The first-consecutive-moments threshold proof in §1 is a derivation of this round.

**[P2]** Guo, Li, and Mu. *Robust Aggregation of Calibrated Forecasts*. arXiv:2606.31020, 2026, §5 and Theorem 3. The source supplies the state-feedback benchmark and contextual-Hedge upper bound. The utility-hull specialization and exact-calibration lower-bound construction in §2 are derived here.

Source addresses and the targeted verification scope are recorded in `sources.json`. The input manifest hashes all nine supplied programme files and the preceding round's report/package. Original uploads are not duplicated in this output package.
