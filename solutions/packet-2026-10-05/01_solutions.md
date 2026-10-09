# Solutions and scoped mathematical progress

**Bayesian Knowledge System · 5 October 2026**

## Reading contract

The supplied corpus contains **600 questions, numbered 401–1000**, not questions 1–600. Original identifiers are preserved throughout this packet. This document distinguishes a solution of the stated question, an exact reformulation using established mathematics, a restricted result, and a project-specific result. The written arguments are the basis of the mathematical claims. Finite calculations are checks, not substitutes for proofs. None of these arguments has been independently peer-reviewed or checked by a formal proof assistant; external novelty is not established.

The original scaffold's source code was not supplied. The accompanying programs are new, standalone reference controls, not a modification or rerun of its reported 24 tests.

| Identifier | Result in this analysis | Scope |
|---|---|---|
| **507** | Constructive proof that both displayed PNS(k) endpoints are sharp; exact rational witness algorithms | Full stated target under unrestricted SCM consistency and the supplied observational/single-intervention laws |
| **734** | Seven-atom counterexample to universal optimality of an exchangeable joint mix | Full refutation of the stated universal claim |
| **724** | Necessary-and-sufficient finite normal-cone/weighted-distance characterization | Full finite geometric characterization; no claim of a compact-MDP polynomial-time algorithm or novel convex-analysis technique |
| **449** | Explicit common decoder for every one-row binary linear summary | Restricted result; the general multirow question remains unresolved here |
| **533** | An explicit, loose finite-time sublinear regret bound for the specified exact-projection lobTS rule | Partial answer; sharp dependence on gaps and order structure remains unresolved here |
| **633** | Decision-class testing certificate for a finite declared class | Standard restricted control, not closure of the general minimax gap |
| **812** | Almost-sure total-variation convergence under a uniform conditional second-moment bound on the copula | Restricted result; the unrestricted positive copula case remains unresolved here |
| **H1: handoff 47f** | Exact common reconstruction error for h2 is **1/6** | Closes the explicitly stated [1/8,1/6] gap in that finite sensor model |
| **H2: information semantics** | Shared-root counterexample and a precise update contract | Repairs a stated architectural limitation rather than a catalogued conjecture |
| **H3: task-specific comparison** | Finite decision-relative deficiency formula | Established minimax machinery specialized to the project's common-policy requirement |

Thus three catalogue entries receive complete answers in the senses stated above, four receive restricted progress, and **593 receive no mathematical resolution in this packet**. All 600 have entries in the research map. “Unresolved here” does not assert that an exhaustive literature search has certified continued openness.

---

## 1. Question 507 — sharp multivalued causal-response bounds

### 1.1 Statement and information contract

Relabel the treatments as 1,…,n. For i=1,…,k, let

\[
B_i=\mathbf 1\{Y_i=y_i\},\quad
p_i=P(X=i),\quad q_i=P(B_i=1),\quad
 a_i=P(X=i,B_i=1).
\]

Consistency identifies the last quantity with the observed cell P(X=i,Y=y_i). We seek the sharp range of

\[
z=P(B_1=\cdots=B_k=1).
\]

The full observational table and **every supplied single-intervention outcome table** must be retained, not merely these selected scalar cells. We assume these tables are compatible. There is no additional supplied causal graph, ignorability restriction, monotonicity restriction, or cross-world independence restriction. Such additional assumptions could shrink the answer.

The source's proposed bounds are

\[
L=\max\left\{0,\sum_{i=1}^kq_i-k+1,
\max_{i\le k}\left[a_i+\sum_{j\ne i}(q_j+p_j-a_j)-k+1\right]\right\},
\]

\[
U=\min\left\{\sum_{i\le k}a_i+\sum_{i>k}p_i,
\min_{i\le k}q_i,
\min_{T\subseteq[k],\ |T|\ge2}
\frac{\sum_{i\in T}(q_i-a_i)}{|T|-1}\right\}.
\]

**Theorem. Both endpoints are attainable. Every point of [L,U] is attainable.**

The primary source is Shu, Wang and Li, *Identification of Probabilities of Causation: from Recursive to Closed-Form Bounds*, Theorem 2. Its August 2026 arXiv revision states soundness in general dimension and leaves general tightness conjectural. This section supplies an argument for the specific PNS(k) question, not every other bound in that paper.

### 1.2 Failure notation

Write F_i={B_i=0}, and define

\[
d_i=p_i-a_i=P(X=i,F_i),\qquad
 e_i=1-q_i-d_i=P(X\ne i,F_i),\qquad
 b_i=q_i-a_i=P(X\ne i,B_i).
\]

Compatibility gives nonnegativity and the obvious row-capacity inequalities. We first construct a joint law of X and the k indicators. Section 1.5 then completes it to all outcome categories.

### 1.3 Upper endpoint: reserve an all-success block

Suppose an all-success event of mass z is reserved, with mass z_i inside stratum X=i. It must satisfy

\[
\sum_{i=1}^n z_i=z,
\quad 0\le z_i\le a_i\ (i\le k),
\quad 0\le z_i\le p_i\ (i>k),
\quad z-z_i\le b_i\ (i\le k).
\tag{1}
\]

Conversely, these conditions suffice to construct a law with all-success probability **at least** z. After reserving the blocks, the residual capacity of row j is t_j=p_j−z_j. The diagonal failure mass d_i fits in row i because z_i≤a_i. Its off-diagonal failure mass e_i fits outside row i because

\[
e_i\le\sum_{j\ne i}t_j
\iff z-z_i\le q_i-a_i=b_i.
\]

Place each coordinate's failures independently as measurable subsets of these residual row intervals. Failures belonging to different coordinates may overlap. This yields all required indicator marginals and diagonal cells, while the reserved blocks remain all-success.

Eliminating the z_i from (1) gives

\[
z\le\sum_{i\le k}a_i+\sum_{i>k}p_i,\qquad
z\le q_i\quad(i\le k),\qquad
\sum_{i\le k}(z-b_i)_+\le z.
\tag{2}
\]

For completeness, the first inequality is the total upper capacity. The lower capacities are z_i≥(z−b_i)_+; each fits its upper capacity precisely when z≤q_i. The final inequality says their sum does not exceed z. Remaining mass can then be allocated up to the upper capacities.

The identity

\[
\sum_i(z-b_i)_+=\max_{T\subseteq[k]}
\left(|T|z-\sum_{i\in T}b_i\right)
\]

shows that the last condition in (2) is equivalent to the subset inequalities in U; empty and singleton subsets add no constraint. Hence the largest reservable mass is U. The constructed law has all-success mass at least U, and the necessary upper bound prohibits anything larger. It therefore attains U.

**Computational simplification.** Sort b_i increasingly. For each cardinality j≥2, the smallest subset sum is the prefix sum of the j smallest b_i. Consequently the apparently exponential subset minimum is evaluated in O(k log k) exact arithmetic operations.

### 1.4 Lower endpoint: maximize the union of failures by a flow

We want to maximize P(∪F_i). Make the following capacitated network:

- A source s and sink t.
- One row node R_j for each X=j, with R_j→t capacity p_j.
- A direct arc s→R_i of capacity d_i for each i≤k.
- One off-diagonal node O_i, with s→O_i capacity e_i and O_i→R_j for every j≠i of capacity infinity. Capacity one suffices in the implementation.

A flow assigns disjoint covered mass in each row to a failure coordinate responsible for covering it. Direct flow corresponds to a diagonal failure; off-diagonal flow to that coordinate's failures in other rows.

Let a maximum flow have value F and covered row masses c_j. Two consequences of maximality are

\[
c_i\ge d_i,\qquad \sum_{j\ne i}c_j\ge e_i.
\tag{3}
\]

If the first failed, unused direct supply and unused row capacity would give an augmenting path. If the second failed, unused off-diagonal supply and an outside row with unused capacity would give one. The original compatibility inequalities guarantee enough total outside capacity.

Inside each row, arrange the flow-assigned pieces as disjoint intervals. They cover exactly c_j. For each failure F_i, keep its assigned pieces and enlarge them **only within the already covered region**, until its diagonal mass is d_i and its outside mass is e_i. Conditions (3) make these enlargements possible. Different failures may overlap. The union of all failures is exactly the covered region, of mass F. The rest is all-success.

It remains to calculate F. By the max-flow/min-cut theorem, the only potentially minimal cuts have values

\[
1,\qquad \sum_i(d_i+e_i),\qquad
1-a_i+\sum_{j\ne i}e_j\quad(i\le k).
\tag{4}
\]

Here is a direct cut check. Let K be the row nodes placed on the sink side. If K is empty, the row-to-sink arcs cost one. If K={i} for a target row, all off-diagonal supplies except e_i must be cut, giving the third expression. If K is a singleton non-target row, its cut is no smaller than the total failure supply. If |K|≥2, every off-diagonal supply must be cut; adding the remaining direct/row capacities gives at least the total failure supply. This exhausts the cuts.

Therefore

\[
1-F=\max\left\{0,\sum_iq_i-k+1,
\max_i\left(a_i-\sum_{j\ne i}e_j\right)\right\}=L.
\]

The interval construction attains this value. This is an all-dimension argument, not extrapolation from a finite search.

### 1.5 Completing the indicators without losing other outcome cells

This step is essential: optimizing only the selected indicators would not by itself settle the question.

For each targeted intervention i, write the full experimental and observed cells as

\[
q_i^y=P(Y_i=y),\qquad a_i^y=P(X=i,Y=y).
\]

On B_i=1, put Y_i=y_i. On X=i,B_i=0, assign each y≠y_i with probabilities

\[
\frac{a_i^y}{p_i-a_i}.
\]

On X≠i,B_i=0, use

\[
\frac{q_i^y-a_i^y}{1-q_i-p_i+a_i}.
\]

Each numerator is nonnegative under compatibility, and each list sums to one on a positive-mass conditioning event. When the denominator is zero, that event has no mass and its kernel can be arbitrary. For untargeted interventions i>k, assign Y_i conditional on X=i using a_i^y/p_i and conditional on X≠i using (q_i^y−a_i^y)/(1−p_i), with the same zero-mass convention.

These assignments can be made conditionally independently across potential outcomes, given the constructed X and indicator vector. They preserve every experimental outcome marginal and every observational cell. The resulting finite joint law of (X,Y_1,…,Y_n) has a structural realization: an exogenous variable carries this vector, X reads its treatment coordinate, and Y reads the potential-outcome coordinate selected by the actual or intervened treatment.

Thus no non-target outcome constraint has been discarded. Convex mixing of the lower and upper constructions preserves the input tables and attains every intermediate z.

### 1.6 Implementation and boundaries

`code/causal_bounds.py` provides exact `Fraction` implementations of the bounds, an upper witness, a lower max-flow witness, and witness verification. The indicator certificate is compact; explicitly expanding every potential-outcome tuple need not be. The scalar bound uses O(n+k log k) arithmetic operations. The rational flow and interval construction are polynomial-size operations; arithmetic bit costs remain part of the runtime.

`code/audit_causal.py` checks 900 generated compatible indicator instances, producing 1,800 exact endpoint witnesses. Independent floating-point LPs check 120 indicator instances and 48 full categorical instances. The largest LP discrepancy was approximately 2.22×10⁻¹⁶. Those LPs are numerical corroboration; the witness checks are exact for the generated inputs.

**Project use.** Add a partial-identification control that records both endpoint witnesses rather than choosing a prior and presenting its posterior mean as an evidence-identified effect. This can become a genuine decision gate: act only when the same action is acceptable throughout the identified set, otherwise acquire a discriminating observation or report the ambiguity.

**Extension.** The proof does not use distinctness of the selected outcome labels across different treatments. Distinct labels are therefore unnecessary under this same unconstrained information contract. Restrictions on the causal graph or on joint counterfactual behavior are not covered.

---

## 2. Question 734 — a counterexample to universally optimal balancing

### 2.1 Construction

Take n=3 and the common marginal F uniform on {0,1,2}. It is 3-completely mixable: randomly permuting (0,1,2) gives a constant sum of three.

Let the uncertainty set consist of **all distributions on the three two-element subsets** of {1,2,3}. It is nonempty and permutation-invariant. Its worst-case objective is

\[
\max_{|K|=2} E\left[f\left(\sum_{i\in K}X_i\right)\right],
\qquad f(s)=(s-2)_+.
\]

The loss is convex, nonnegative, and finite.

For **every** joint mix with these marginals, X_1+X_2+X_3=3 almost surely. Every two-coordinate sum is therefore 3−X_j, which is uniform on {1,2,3}. Each pair has expected loss 1/3. This conclusion does not require exchangeability.

Now construct another exchangeable coupling. Choose one of

\[
(0,0,2),\qquad(0,2,2),\qquad(1,1,1)
\]

with probability 1/3 each, and uniformly permute its coordinates. Each coordinate has probability 1/3 of each of 0,1,2. For a uniformly chosen pair, the conditional expected losses are respectively

\[
0,\qquad 2/3,\qquad 0.
\]

Exchangeability makes the value the same for each fixed pair. Its worst-pair loss is therefore **2/9**, strictly smaller than **1/3**.

### 2.2 Conclusion

No joint mix, exchangeable or otherwise, is optimal in this example. The universal claim in question 734 is false. The strict gap is 1/9. The same example also works when the uncertainty set is just the uniform distribution on pairs.

This does not refute the source's quadratic-cost theorem. It refutes its proposed extension to every convex cost. It also does not settle question 733 about negative association and symmetrization.

`code/audit_additional.py` verifies all marginal probabilities, exchangeability, and each pair's objective using rational arithmetic. The alternative has seven atoms. The value 2/9 is the exhibited coupling's value; a proof that it is the unrestricted optimum is not needed for the counterexample and is not claimed here.

**The failure is not limited to nonsmooth or non-strictly-convex losses.** Replace the hinge by

\[
f_\delta(s)=\frac{s-2+\sqrt{(s-2)^2+\delta^2}}2.
\]

This is smooth, increasing and strictly convex, and 0≤f_δ(s)−(s−2)_+≤δ/2 everywhere. Therefore the gap remains positive for 0<δ<2/9: the alternative's cost increases by at most δ/2, while a joint mix's cost cannot decrease. This is an analytic extension, not an additional numerical experiment.

### 2.3 Consequence for the knowledge system

Preserving a total, a covariance, or a balancing property is not a loss-independent certificate of safe compression. A representation that is optimal when every component is used can be inferior when only a subset is available. Store the **participation/observation menu and loss** with a representation certificate.

Primary source: Koike, Lin and Wang, *Joint mixability and notions of negative dependence*, equation (8), Theorem 4 and conclusion item 4. The inspected arXiv version states the general-convex question explicitly.

---

## 3. Question 724 — exact squared-error reward safety geometry

### 3.1 Occupancy representation

Fix the finite discounted MDP in the question. Use normalized discounted state-action occupancies d. They form the polytope

\[
\mathcal O=\left\{d\ge0:
\sum_a d(s,a)=(1-\gamma)\mu_0(s)+
\gamma\sum_{s',a'}P(s\mid s',a')d(s',a')\right\}.
\]

Every stationary randomized policy induces a point of this polytope, and every point induces such a policy by normalizing its action masses at each state. Reward ranking is ranking of R·d; the common factor 1/(1−γ) does not affect optimality or normalized regret.

Let V be its finite set of vertices. Put

\[
J_+=\max_{v\in V}R\cdot v,\quad
J_-=\min_{v\in V}R\cdot v,\quad \Delta=J_+-J_->0,
\]

and define the bad vertices

\[
V_L=\{v\in V:(J_+-R\cdot v)/\Delta\ge L\}.
\]

Let c=range(R)>0, exactly the reward-range normalization in the supplied question. For each vertex define its maximization normal cone

\[
N(v)=\{r:r\cdot(v-w)\ge0\text{ for every }w\in V\}.
\]

These are exactly the reward vectors making v optimal, including ties.

### 3.2 Necessary and sufficient condition

For a validation distribution D on state-action coordinates, set

\[
\delta_D(v)=\frac1{c^2}\min_{r\in N(v)}
\sum_iD_i(r_i-R_i)^2.
\tag{5}
\]

**Theorem.** The safety requirement in question 724 holds if and only if

\[
\boxed{\delta_D(v)>\varepsilon\quad\text{for every }v\in V_L.}
\tag{6}
\]

**Necessity.** If a bad vertex has distance at most ε, a minimizing learned reward vector satisfies the validation constraint and makes that bad vertex optimal. This violates the requirement that every maximizing policy have regret strictly below L.

**Sufficiency.** Suppose a learned reward satisfying the error bound has a bad optimal policy with occupancy d. Decompose d into vertices. Since d maximizes a linear learned reward, every vertex used with positive weight is also optimal for that reward. Since true normalized regret is affine in d, at least one of those vertices has regret at least L. Its normal cone is within squared D-distance ε of R, contradicting (6).

The minimum is attained, even when some D_i=0. Project the polyhedral cone onto the coordinates with positive D_i. Its image is a closed polyhedron. Weighted Euclidean distance to that image is attained, and a preimage exists by the definition of the image.

Learned reward vectors here are unrestricted except for the error budget stated in the question. An additional reward box or other constraint must be intersected with each normal cone; it must not be silently omitted.

This gives a finite structural characterization, not merely a sufficient bound. **Strictness matters:** equality δ_D(v)=ε is unsafe because ties are included and every optimal policy must be safe.

### 3.3 Computation and dual certificates

Let A have rows v−w for w∈V, and let b=−AR. Ignoring the factor c², the distance is the convex quadratic program

\[
\min_e e^T\operatorname{diag}(D)e\quad\text{subject to }Ae\ge b.
\]

When D_i>0, its dual is

\[
\max_{\lambda\ge0}
\left[b^T\lambda-rac14\lambda^TA\operatorname{diag}(D)^{-1}A^T\lambda\right].
\]

A primal witness is an unsafe learned reward; a dual witness certifies separation from a bad action cone. With zero D_i, replace the inverse by the pseudoinverse and impose (A^Tλ)_i=0 on those coordinates.

This is finite and constructive once the vertices are supplied. Enumerating deterministic policies can be exponential in the compact MDP description. No polynomial-time claim in that representation is made.

### 3.4 A small exact control and a design consequence

For a one-state two-action problem with R=(1,0) and D=(η,1−η), the bad action becomes optimal when its learned reward reaches or exceeds the good action's. The nearest boundary is a tie at learned reward (η,η), with squared error

\[
\eta(\eta-1)^2+(1-\eta)\eta^2=\eta(1-\eta).
\]

For 0<L≤1, safety is exactly ε<η(1−η). If either action has zero validation coverage, the safety radius is zero. The exact control is included in `audit_additional.py`.

For a fixed v, δ_D(v) is the infimum of functions linear in D, hence concave in D. Its strict superlevel set is convex. Intersecting over bad vertices shows that the set of safe validation distributions in (6) is convex. This suggests a useful experimental-design objective: choose validation coverage to maximize the distance to unsafe decision cones, rather than minimize a generic average prediction error.

**Classification.** This answers the requested finite geometric characterization using standard occupancy and normal-cone reasoning. It does not establish external novelty or solve the efficient representation problem. It also does not settle question 725: a general continuous policy penalty need not reduce to the same finite collection of vertex cones.

---

## 4. H1 — the handoff's h2 reconstruction gap is exactly 1/6

### 4.1 Model

Use the handoff's illumination-cancelled h2 readout

\[
Y=2(2U-1)+E,
\quad P(U=1)=p\in[1/4,3/4],
\]

with independent disturbance E taking −2,0,2 with probabilities r/2,1−r,r/2, where r∈[1/4,3/4]. Let S=sign(Y). A single decoder D(Y|S), independent of p and r, must reconstruct the **joint** law with U. We claim

\[
\inf_D\sup_{p,r}
\operatorname{TV}\big(P_{p,r}(U,Y),P_{p,r}(U,S)D(Y\mid S)\big)=\frac16.
\tag{7}
\]

### 4.2 Upper certificate

Use

| Input S | Decoder output distribution |
|---|---|
| −1 | −4 with probability 1/3; −2 with probability 2/3 |
| 0 | 0 with probability one |
| +1 | +2 with probability 2/3; +4 with probability 1/3 |

Direct subtraction gives

\[
\operatorname{TV}(P_{p,r},P_{p,r}(U,S)D)=\frac{|1-2r|}{3}\le\frac16,
\]

independently of p.

### 4.3 Lower certificate allowing every decoder

It is enough to use p=1/2 and the two noise endpoints r_0=1/4,r_1=3/4. Define bounded signed functions s_0,s_1 on (U,Y):

- Both are zero at Y=0.
- Both are +1 when nonzero Y has the wrong sign for 2U−1.
- On the correct sign, s_0 is +1 at |Y|=4 and −1 at |Y|=2; s_1 reverses those two signs.

For the two true laws,

\[
E_{P_0}s_0=-5/8,\qquad E_{P_1}s_1=-1/8.
\]

Write Q_i=P_i(U,S)D. For **any** decoder,

\[
\frac5{12}E_{Q_0}s_0+\frac7{12}E_{Q_1}s_1\ge0.
\tag{8}
\]

To check this without a hidden restriction on D, expand the left side as a linear function of its 15 entries D(y|s). Every coefficient is nonnegative. For s=±1, coefficients on correct-sign outputs cancel because 5·7/16=7·5/16; wrong-sign outputs have nonnegative coefficients; zero outputs have coefficient zero. For s=0, the coefficients on |y|=4 are 5/96, on |y|=2 are 7/32, and on y=0 are zero.

Since |s_i|≤1,

\[
\operatorname{TV}(P_i,Q_i)\ge\tfrac12(E_{Q_i}s_i-E_{P_i}s_i).
\]

Taking the indicated convex combination, (8) implies

\[
\sup_i\operatorname{TV}(P_i,Q_i)
\ge\frac12\left(\frac5{12}\frac58+\frac7{12}\frac18\right)=\frac16.
\]

Together with the upper certificate this proves (7). No symmetry, sign preservation, or restriction on how zero is decoded was assumed for the lower bound.

### 4.4 Why this is useful

The handoff reports identical robust squared-error risk for full h2 and its ternary summary, but an unresolved reconstruction interval [1/8,1/6]. The reconstruction optimum is the upper endpoint. Thus preserving the specified minimax estimation risk does **not** imply approximate reconstruction with arbitrarily small error. Full reconstruction is a sufficient certificate for many tasks, not a necessary certificate for this one.

The accompanying exact check verifies all 15 dual coefficients and 441 rational parameter pairs for the upper decoder. The continuum proof is the displayed formula and dual argument, not the grid.

---

## 5. Question 449 — a common decoder for one linear parity

This is a restricted result, not a solution of arbitrary-rank binary linear compression.

Consider the two doubly symmetric binary source hypotheses with noise correlations t_0=u≥0 and t_1=−v≤0, u,v∈[0,1]. A single raw pair yields a fair bit and an independent noise sign Z with mean t_i. A nonzero one-row binary linear map, of Hamming weight w≥1, yields a fair parity bit and a noise parity of mean t_i^w.

For u+v>0 define

\[
A=\frac{vu^w+u(-v)^w}{u+v},\qquad
B=\frac{u^w-(-v)^w}{u+v}.
\]

Use the binary channel

\[
P(Z'=+1\mid Z=z)=\frac{1+A+Bz}{2}.
\tag{9}
\]

The two required means follow directly:

\[
A+Bu=u^w,\qquad A-Bv=(-v)^w.
\]

It remains to check that (9) is stochastic, equivalently |A|+|B|≤1. By symmetry assume u≥v. If w is even, A,B≥0 and

\[
A+B=\frac{(1+v)u^w-(1-u)v^w}{u+v}
\le\frac{(1+v)u}{u+v}\le1.
\]

If w is odd, again A,B≥0 and

\[
A+B=\frac{(1+v)u^w+(1-u)v^w}{u+v}
\le\frac{(1+v)u+(1-u)v}{u+v}=1.
\]

The u<v case gives the same bound after exchanging u and v and accounting for the sign of A or B. When u=v=0, generate a fair output noise sign directly. Finally generate an independent fair parity bit and combine it with Z'. This is one decoder that produces the correct compressed pair law under both hypotheses.

The proof includes unequal opposite-sign correlations, not just the symmetric equal-magnitude case. For multiple overlapping parity rows, the desired output noise coordinates need not be independent; applying this scalar construction independently does not produce their joint law. That is the remaining gap.

The rational audit checks 2,688 combinations of correlations and row weights. Source: *On the suboptimality of linear codes for binary distributed hypothesis testing*, arXiv:2601.10526, and the supplied question 449.

---

## 6. Question 533 — sublinear regret for exact-projection lobTS

### 6.1 Scope

Use exactly the supplied Gaussian rule. There are k≥2 arms with means μ_a, known common variance σ²>0, and a unique best arm *. Let C_a=M_a∩Σ_a be the set onto which the algorithm projects. Assume μ∈C_* and C_a⊆{v:v_a≥v_b for all b}; these hold in the well-specified order model. At every round, compute

\[
d_a(t)=\inf_{v\in C_a}\sum_bN_b(t)(v_b-\widehat\mu_b(t))^2,
\qquad
p_a(t)=\frac{e^{-d_a(t)/(2\sigma^2)}}{\sum_b e^{-d_b(t)/(2\sigma^2)}}.
\]

Empty sets have zero weight. Projections are exact **every round**. The source's engineering variant that reuses projections for several rounds is not covered.

Let Δ_a=μ_*−μ_a, Δ_min=min_{a≠*}Δ_a, and Δ_max=max_aΔ_a. The following bound is deliberately loose; its purpose is to settle sublinearity for this rule without replacing it by UCB or assuming a Bayesian posterior identity it does not have.

### 6.2 Explicit finite-time bound

For T≥2 and 0<η<1, put

\[
J=\lceil\log_2T\rceil,\quad
H=2\log\frac{2k(J+1)}\eta,\quad
r=\frac{e^{-kH}}k,
\]

\[
K_0=32\sigma^2[(k+1)H+3\log T],\quad
n_0=\left\lceil\frac{K_0}{\Delta_{\min}^2}\right\rceil,
\quad n_a=\left\lceil\frac{K_0}{\Delta_a^2}\right\rceil,
\]

\[
t_0=\left\lceil\frac{2n_0+8\log(1/\eta)}r\right\rceil.
\]

Then a valid expected regret bound, allowing harmless endpoint-round slack, is

\[
R_T\le\min\left\{\Delta_{\max}T,
\Delta_{\max}(t_0+1+2\eta T)
+\sum_{a\ne *}\Delta_a(n_a+T^{-2})\right\}.
\tag{10}
\]

In particular, with η=T^{-1/(2k+1)}, for each fixed well-specified instance,

\[
R_T=O_{k,\sigma,\Delta}\!
\left(T^{2k/(2k+1)}(\log T)^{2k+1}\right)=o(T).
\tag{11}
\]

η is an analysis parameter, not an additional input or modification of the algorithm. The constants can be very poor. The result does not claim that the order information improves this rate.

### 6.3 Proof

Pre-generate independent Gaussian reward sequences for each arm. A dyadic-block maximal Gaussian inequality and a union bound over k arms and J+1 blocks give an event E of probability at least 1−η on which

\[
\frac{n(\widehat\mu_{a,n}-\mu_a)^2}{2\sigma^2}\le H
\quad\text{for every }a\text{ and }1\le n\le T.
\tag{12}
\]

To see the constants, in a block n∈[2^j,2^{j+1}), crossing the normalized boundary requires the partial Gaussian sum to exceed σ√(2·2^jH) in absolute value before time 2^{j+1}. Its probability is at most 2e^{-H/2}. Summing these probabilities yields η.

On E, μ is a feasible comparator in the best arm's projection, so d_*/(2σ²)≤kH and p_*≥r. Couple each categorical draw using an independent uniform variable so that the best arm is selected whenever that variable is at most p_*. Consequently, on E, its count by t_0 dominates the count of uniforms at most r. A binomial lower-tail bound gives N_*(t_0)≥n_0 except on another event of probability at most η. If t_0≥T, the trivial first term in (10) suffices.

After that time, consider a suboptimal arm with N_a≥n_a. Equation (12) gives estimation errors at most Δ_a/4 for both it and the best arm. Thus their empirical gap is at least Δ_a/2. Projection onto the larger halfspace v_a≥v_* already costs

\[
d_a\ge
\frac{N_aN_*}{N_a+N_*}
(\widehat\mu_*-\widehat\mu_a)^2
\ge\frac{\Delta_a^2}{8}\min(N_a,N_*).
\]

The chosen thresholds imply d_a/(2σ²)≥kH+3log T. Comparing its weight to the best arm's gives p_a≤T^{-3}.

There are at most n_a selections while its count is below n_a. For later rounds in the good states just described, conditional selection probability is at most T^{-3}, giving at most T^{-2} expected additional selections over T rounds. Charge the first t_0+1 rounds at Δ_max per round and the exceptional probability at 2ηTΔ_max. This proves (10). Substitution yields (11).

### 6.4 Remaining question and practical value

The dependence on k and Δ_min arises from a crude lower bound on best-arm sampling. It ignores most order structure and is not a candidate sharp analysis. A better result should exploit the geometry of C_a, identify the active misleading orders, and certify inexact/cached projections. Thus the broad rate question is still open here, but the explicit “is it o(T)?” subquestion has a positive answer under the stated exact rule.

The inspected source, Carlsson, Mwai and Johansson, *Latent Order Bandits*, August 2026 revision, explicitly lacks a regret analysis for lobTS. This argument is not a code audit or a validation of its empirical results.

---

## 7. Question 633 — a finite, task-relevant diagnostic control

Let F={f_1,…,f_M} be a **fixed before validation** collection of Boolean queries on observations. They might record failure events of the actual actions the system uses. Let P_0 be a known reference law and let X_1,…,X_n be independent observations from P. Define

\[
\widehat D_F=\max_{f\in F}
\left|\frac1n\sum_{j=1}^nf(X_j)-E_{P_0}f\right|.
\]

Hoeffding's inequality and a union bound give, with probability at least 1−α,

\[
\left|\widehat D_F-
\sup_{f\in F}|E_Pf-E_{P_0}f|\right|
\le\sqrt{\frac{\log(2M/\alpha)}{2n}}.
\]

Thus rejecting at ε/2 distinguishes P=P_0 from F-discrepancy greater than ε with error probability at most α when

\[
n\ge\frac{2\log(2M/\alpha)}{\varepsilon^2}.
\]

This is a standard sufficient bound. It does **not** solve the general instance-dependent minimax problem, show necessity for every F, test unobservable causal effects, or certify that P=P_0 following non-rejection. Reusing validation data to choose F needs a separate adaptive-analysis guarantee.

**Project use:** make model diagnostics target-sensitive. A full-law discrepancy in an irrelevant nuisance can trigger needless rebuilding; a small discrepancy concentrated at a decision boundary can matter greatly. Declare the diagnostic class and its loss interpretation in the benchmark contract.

---

## 8. Question 812 — density preservation under a second-moment condition

The original recursion is

\[
f_{n+1}(x)=f_n(x)[1-r_n+r_nc(F_n(x),F_n(X_{n+1}))],
\quad X_{n+1}\mid\mathcal F_n\sim f_n.
\]

Keep the question's assumptions and add

\[
\sup_{u\in(0,1)}\int_0^1(c(u,v)-1)^2\,dv\le C<\infty.
\tag{13}
\]

An essential supremum and almost-everywhere formulation suffice. In particular, a copula density bounded above by M satisfies (13) with C≤M−1.

**Proposition.** If ∑r_n²<∞, the predictive measures converge almost surely in total variation to a measure with a density. The divergence of ∑r_n is not needed for this restricted proposition.

**Proof.** Put h_n=f_n/f_0 in the Hilbert space L²(f_0(x)dx). Conditional on the past, V=F_n(X_{n+1}) is uniform. The copula row integrates to one, so E[h_{n+1}|𝔽_n]=h_n. Moreover,

\[
E[\|h_{n+1}\|_2^2\mid\mathcal F_n]
\le(1+Cr_n^2)\|h_n\|_2^2.
\]

Hence E||h_n||² is bounded by ∏_j(1+Cr_j²)≤exp(C∑r_j²). The square-integrable Hilbert-valued martingale converges almost surely and in mean square to h_∞. Nonnegativity and unit integral pass to the limit. Finally,

\[
\operatorname{TV}(f_n dx,f_0h_\infty dx)
\le\tfrac12\|h_n-h_\infty\|_{L^2(f_0dx)}\longrightarrow0.
\]

The general question deliberately does not assume (13). This proof therefore gives a usable sufficient contract and identifies uniform integrability as the missing bridge; it does not resolve the unrestricted copula case.

---

## 9. H2 — provenance roots are not consumed information

Let H be fair. Let a raw record contain X=(A,B), where A is a fair nuisance independent of H and B reports H with accuracy 3/4. First consume only Z_1=A. Then

\[
P(H=1\mid Z_1)=1/2.
\]

Next consume Z_2=B, derived from the **same raw record**. For B=1,

\[
P(H=1\mid Z_1,B=1)=3/4,
\qquad \mathrm{LR}(B=1\mid Z_1)=3.
\]

It is incorrect to force the second likelihood ratio to one merely because both summaries share a raw ancestor. By contrast, once B itself or the full X has been conditioned on, a deterministic repeat of B is neutral.

The exact neutral-output criterion is measurability with respect to the information actually conditioned on: if Z is determined by the current information state I under the declared procedure, then P(H|I,Z)=P(H|I). Root reachability alone does not establish that condition.

**Implementation repair:** retain the lineage DAG, but add an information-state record identifying consumed variables/projections and values, their versions, and the model under which a conditional likelihood was calculated. A derivation record says where a feature came from. A conditioning record says what inference used. An independence certificate says which factorization is licensed. These are three different records.

The handoff already identifies this limitation. The new contribution here is an explicit regression test and an operational contract, not discovery of the limitation itself.

**A posterior over the immediate target can also be insufficient for the next query.** Let H be fair and let an observed tag M, independent of H, say whether an available test is perfect or is an independent fair bit. The test costs 1/10. Wrong classification costs one and abstention costs 3/10. After either tag value the target posterior is P(H=1)=1/2. Nevertheless, with the perfect-test tag the optimal choice is to buy it, for total loss 1/10; with the useless-test tag the optimal choice is to abstain without buying, for loss 3/10. Compressing both histories to the same scalar target posterior destroys the optimal query choice. A joint belief/state retaining the relevant test mechanism avoids the problem; this is not a failure of Bayesian filtering itself.


---

## 10. H3 — a target-specific common-policy certificate

Full reconstruction is often too strong. Here is a precise finite replacement when only a declared action/loss family matters.

Let m range over finitely many models, Y be the raw observation, Z=T(Y), and A be a finite action set. For raw randomized rule d and summary rule g, let R_m(d),R_m(g) denote their expected losses. Define

\[
\delta_A=\sup_d\inf_g\max_m\{R_m(g)-R_m(d)\}.
\tag{14}
\]

The quantifiers say: every raw rule has one summary replacement whose excess risk is at most δ_A in every model. The replacement may depend on the raw rule, but not on the true model.

Finite minimax duality gives

\[
\boxed{\delta_A=\max_{\lambda\in\Delta(\mathcal M)}
\left[\min_g\sum_m\lambda_mR_m(g)
-\min_d\sum_m\lambda_mR_m(d)\right].}
\tag{15}
\]

To derive it, express max_m as max_λ, interchange min_g and max_λ for each fixed d using bilinearity and compact convex rule sets, and then commute the two maxima over d and λ. The maximization over d of the negative raw risk is minus its minimum. Because summary rules can be run on raw observations, every bracket is nonnegative.

A δ_A certificate bounds the increase in common-rule minimax risk: start with a minimax raw rule and use its summary replacement. It is generally weaker than requiring a common decoder that reconstructs the full joint law. A finite implementation can enumerate deterministic raw rules and solve the remaining LPs, but the enumeration may be exponential. This is an exact baseline, not a claim of scalable general computation.

**Important distinction:** equality of just one raw and compressed minimax value need not imply δ_A=0. Formula (15) ranges over all mixtures of models. Likewise δ_A=0 for one action/loss family does not mean all future objectives are preserved.

This is a specialization of comparison-of-experiments and deficiency ideas, not a novelty claim. Its role is to replace the ambiguous instruction “preserve what matters” with a testable contract.

---

## 11. Verification ledger and reproduction

Run from the `code` directory:

```bash
python audit_causal.py       # Requires NumPy and SciPy for independent LP checks.
python audit_additional.py   # Python standard library only.
```

The first file's exact constructors use only the standard library; SciPy is used only by its independent audit script. Audits use synthetic, compatible laws with a fixed seed. There is no acquired real-world dataset or empirical forecasting-benefit claim.

| Check | Outcome |
|---|---:|
| Exact Q507 compatible instances | 900 |
| Exact Q507 endpoint witnesses | 1,800 |
| Independent indicator LP instances | 120 |
| Independent full-categorical LP instances | 48 |
| Maximum observed numerical LP discrepancy | 2.22×10⁻¹⁶ |
| Q734 alternative atoms | 7 |
| H1 nonnegative decoder-dual coefficients checked | 15 |
| H1 exact rational upper-decoder grid cases | 441 |
| Q449 exact rational scalar-channel checks | 2,688 |
| Q724 exact two-action checks | 21 |

The Q533, Q633, Q812 and H3 arguments are written proofs/specializations; they are not accompanied by formal verification. No result should be promoted to a publication claim until another reader checks assumptions, quantifiers, and nearest prior work. Q507 and Q734 are the strongest candidates for that independent review.

## Sources and scope of external checking

Original question formulations and project status come from the seven uploaded files. Individual source files and line locators are preserved in the machine-readable catalogue. Primary sources inspected selectively include:

- Shu, Wang and Li, **Identification of Probabilities of Causation: from Recursive to Closed-Form Bounds**, arXiv:2505.15274, inspected HTML revision dated August 2026: https://arxiv.org/html/2505.15274 . Theorem 2 and the stated general tightness gap were checked. The inaccessible proceedings PDF was not independently inspected.
- Koike, Lin and Wang, **Joint mixability and notions of negative dependence**, arXiv:2204.11438v4: https://arxiv.org/html/2204.11438 . Equation (8), the quadratic theorem and conclusion item 4 were checked.
- Fluri et al., **The Perils of Optimizing Learned Reward Functions**, ICML 2025: https://proceedings.mlr.press/v267/fluri25a.html . The publication page and abstract were checked; the detailed Q724/Q725 formulation used here is the supplied collection's formulation.
- Carlsson, Mwai and Johansson, **Latent Order Bandits**, arXiv:2605.07304v2: https://arxiv.org/html/2605.07304v2 . The likelihood-projection rule and absence of a formal regret analysis were checked.
- **On the suboptimality of linear codes for binary distributed hypothesis testing**, arXiv:2601.10526: https://arxiv.org/abs/2601.10526 . The publication identity was checked; the exact Q449 formulation is from the supplied collection.
- van Rooyen and Williamson, **Le Cam meets LeCun: Deficiency and Generic Feature Learning**, arXiv:1402.4884: https://arxiv.org/abs/1402.4884 . This is an established conceptual precedent for H3, not evidence that H3 is novel.

For Q633 and Q812, the restricted propositions above are derived from the supplied problem statements. Their full originating manuscripts and all subsequent literature were not independently audited. The collected “checked 5 October 2026” labels are source metadata, not a claim that this analysis repeated all 600 literature searches.
