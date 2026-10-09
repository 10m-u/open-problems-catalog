# A focused research portfolio for the Bayesian knowledge system

**Research derivations and computational checks · 5 October 2026**

## Executive result

I selected catalogue questions **413, 725, 449 and 810**. They connect directly to four implementable operations: combining dependent forecasts, certifying decisions made from learned rewards, checking a common probabilistic decoder, and auditing a dependence graph against its closest alternative.

The strongest results are:

| Target | Result obtained | Scope that remains open here |
|---|---|---|
| Q413 | A calibration-feasible empirical-profile projection algorithm with a square-root regret bound and no additive calibration-tolerance-times-horizon term; a matching square-root lower bound in an exact-calibration example. | Sharp joint dependence on alphabet size, actions and tolerance. |
| Q725 | A general lifted-geometric characterization, a witness-producing finite LP method for polyhedral lifts, and an entropy-regularized example whose safety boundary is genuinely curved. | A general efficient algorithm for arbitrary continuous regularizers. |
| Q449 | An explicit common stochastic decoder for an overlapping rank-two code, extending to an infinite block family; 27,297 exact rank-two grid comparisons. | All full-rank binary matrices and the continuum of parameters outside the proved family. |
| Q810 | A general endpoint certificate, a proof for complete multipartite graphs, and exhaustive verification for every undirected graph on at most seven vertices. | The assertion for arbitrary undirected graphs; the different DAG question Q811. |

The proofs below are derivations made in this work, not claims that the cited papers already prove these statements. They have been algebraically checked and paired with the computational tests described below, but have not received independent peer review or formal proof-assistant verification. The bibliography check was targeted, not an exhaustive priority or novelty audit.

### Input and prior-work boundary

The readable inputs were the research map and six collections, containing original IDs 401–1000. The map identifies three earlier full results (507, 724, 734) and four partial results (449, 533, 633, 812), referring to a separate solutions file. I used those claims to avoid unnecessary duplication, not as verified lemmas.

The user subsequently mentioned two additional attachments, including the solutions. Neither appeared in file search or the mounted working directory during this run. Consequently, this report does **not** claim to have inspected them or checked their proofs. The input manifest records the seven files actually available.

The selection follows the map's distinction between broad mathematical importance and immediate architectural usefulness. It does not turn the other catalogue questions into implementation prerequisites. Nor does this work establish that an existing scaffold implements the resulting operations: no scaffold code was supplied or modified.

## 1. Q413: calibration-robust learning without a linear tolerance penalty

### 1.1 Exact contract

There are finitely many known forecast profiles
\[
E=\{e_1,\ldots,e_m\},\qquad e_j\in[0,1]^n.
\]
Profiles arrive independently from one unknown, fixed distribution \(p\in\Delta_m\). There are \(d\) actions and known binary-state utilities \(u(a,y)\), with \(|u(a,y)|\le U\). The learner observes profiles but receives neither resolved states nor payoff feedback.

Fix a known tolerance \(\tau\in[0,1]\). For a horizon-dependent contract, take \(\tau=\varepsilon_T\) throughout that run. A possible conditional truth mapping \(\rho\in[0,1]^m\) must satisfy, for every expert \(i\) and report value \(v\),
\[
\left|\sum_{j:e_j^i=v}p_j(\rho_j-v)\right|
\le \tau\sum_{j:e_j^i=v}p_j.
\tag{1}
\]
The feasible set is assumed nonempty. This is the catalogue's population-calibration, common-\(\rho\) benchmark. It is not a promise that a finite realized sequence of binary labels satisfies exact empirical calibration.

A policy \(x\) assigns an action distribution to each profile. Write \(W_p(x)\) for its worst expected one-period utility over (1), and \(V(p)=\max_xW_p(x)\). The target regret is
\[
\operatorname{Reg}_T
=T V(p)-\min_{\rho\in C_\tau(p)}
\mathbb E\sum_{t=1}^T x_t(e_t)^\top v_\rho(e_t).
\tag{2}
\]
One common \(\rho\) is used in (2) across the whole horizon.

The source's Theorem 2 gives a penalized plug-in algorithm and a bound of the form
\[
O\big((U+n\gamma)\sqrt{mT}+n\gamma\varepsilon_TT\big).
\]
Here \(\gamma\) is that paper's penalty coefficient, not an MDP discount. The construction below takes a different route: it restores feasibility of the estimated profile law before optimizing. [S1, §4, Theorem 2]

### 1.2 Truth masses make the constraint matrix fixed

Use \(z_j=p_j\rho_j\), the joint mass of profile \(j\) and truth 1. This avoids division by profile probabilities and therefore includes structural zeros.

Let \(A\) be the zero-one matrix whose rows index the expert/report groups in (1), and let \(v_g\) be the report value for group \(g\). Define
\[
G=\begin{bmatrix}A\\-A\\I\\-I\end{bmatrix},\qquad
B_\tau=\begin{bmatrix}
\operatorname{diag}(v+\tau)A\\
-\operatorname{diag}(v-\tau)A\\I\\0
\end{bmatrix}.
\]
Then
\[
Z_\tau(p)=\{z:Gz\le B_\tau p\}
\tag{3}
\]
is exactly the joint calibration polytope, including \(0\le z\le p\). The left-hand matrix \(G\) depends only on the incidence of profiles in report groups. It does not change with \(p\), \(\tau\), or the numerical report values once the groups are fixed.

The admissible profile laws form a compact polytope
\[
\mathcal F_\tau=\{q\in\Delta_m:Z_\tau(q)\ne\varnothing\}.
\tag{4}
\]

### 1.3 Algorithm: project, then optimize

At period \(t\ge2\), form empirical frequencies \(\hat p_{t-1}\) and solve
\[
\tilde p_{t-1}\in
\arg\min_{q\in\mathcal F_\tau}\|q-\hat p_{t-1}\|_1.
\tag{5}
\]
Next choose
\[
x_t\in\arg\max_x W_{\tilde p_{t-1}}(x).
\tag{6}
\]
The mapping \(x_t\) is constructed from past profiles; its entry for the current profile is used after that profile arrives. At the first period, any action mapping is allowed.

Both (5) and (6) are linear programs. In (5), use variables \((q,z,t)\), the constraints in (3), and \(t_j\ge|q_j-\hat p_j|\). In (6), dualize the inner minimization over \(z\). The implementation also resolves the inner primal LP to check the returned objective and feasibility residuals.

The algorithm does not need a Hoffman constant, an estimate of truth frequencies, a lower bound on positive profile mass, or a source-independence assumption. Exact polynomial-time statements concern the explicitly enumerated finite problem with rational input. They do not imply polynomial time in the number of experts when the profile alphabet itself is exponentially large.

### 1.4 Theorem and proof

Let \(H\) be a Hoffman constant for \(G\), in the following norm convention:
\[
\operatorname{dist}_1(z,\{w:Gw\le b\})
\le H\|(Gz-b)_+\|_\infty
\tag{7}
\]
whenever the target polyhedron is nonempty. Such a finite constant exists for each fixed finite matrix. The classical error-bound theorem is also stated in the source's appendix. [S1, Appendix A]

**Theorem 1.** The projected algorithm satisfies
\[
\boxed{
\operatorname{Reg}_T\le
2U+8U(1+4H)\sqrt{(m-1)(T-1)}.
}
\tag{8}
\]
In particular, there is no additive \(\tau T\) term.

**Proof.** For two feasible laws \(p,q\),
\[
\|B_\tau(p-q)\|_\infty\le2\|p-q\|_1.
\]
Applying (7) in both directions shows that the Hausdorff distance in \(\ell_1\) between \(Z_\tau(p)\) and \(Z_\tau(q)\) is at most \(2H\|p-q\|_1\).

For a fixed policy, write its payoff as
\[
\sum_j p_j a_{0,j}(x)+z_j a_{\Delta,j}(x),
\]
where \(|a_{0,j}|\le U\) and \(|a_{\Delta,j}|\le2U\). Thus, uniformly over all policies,
\[
|W_p(x)-W_q(x)|\le K\|p-q\|_1,
\quad |V(p)-V(q)|\le K\|p-q\|_1,
\quad K=U(1+4H).
\tag{9}
\]
Because the true \(p\) belongs to (4), optimality of (5) and the triangle inequality give
\[
\|\tilde p_{t-1}-p\|_1
\le2\|\hat p_{t-1}-p\|_1.
\]
Optimality of (6), together with (9), now yields
\[
V(p)-W_p(x_t)\le4K\|\hat p_{t-1}-p\|_1.
\tag{10}
\]
For \(s\) iid observations,
\[
\mathbb E\|\hat p_s-p\|_1
\le\sum_j\sqrt{p_j(1-p_j)/s}
\le\sqrt{(m-1)/s}.
\tag{11}
\]
The last inequality follows from Cauchy–Schwarz and \(\sum p_j^2\ge1/m\).

For every one fixed feasible \(\rho\), its conditional expected payoff at period \(t\) is at least \(W_p(x_t)\). Therefore the minimum over one common \(\rho\) in (2) is at least \(\sum_t\mathbb E W_p(x_t)\). This is only an inequality used in the proof; the adversary in the problem has not been changed to a time-varying one.

The first-period gap is at most \(2U\). Summing (10), using (11) and \(\sum_{s=1}^{T-1}s^{-1/2}\le2\sqrt{T-1}\), proves (8). ∎

The geometry constant can be large. Consequently, (8) does not determine the optimal dependence on the number of profiles or experts. Although the bound has no explicit action-count factor, the LP dimensions still depend on the action count. The theorem is uniform over tolerance values in \([0,1]\) for a fixed profile-incidence matrix.

**Inexact-computation extension.** If (5) returns a feasible law whose projection objective is within \(\eta_t\) of optimum, and (6) loses at most \(\zeta_t\) in robust value, the proof adds at most \(\sum_{t\ge2}(2K\eta_t+\zeta_t)\). Feasibility remains essential; this is not a license to ignore violated calibration constraints.

### 1.5 A matching square-root lower bound at exact calibration

Consider two experts with report alphabet \(\{0,1/2,1\}\), binary prediction actions, and utility \(u(a,y)=\mathbf1\{a=y\}\). There are five supported profiles:
\[
(1/2,1/2),\ (1/2,0),\ (0,1/2),\ (1/2,1),\ (1,1/2).
\]
For \(|\delta|\le1/6\), give them probabilities
\[
p_\delta=(1/3,\ 1/6+\delta/2,\ 1/6+\delta/2,
1/6-\delta/2,\ 1/6-\delta/2).
\tag{12}
\]
Unused profiles in the full nine-element Cartesian alphabet have probability zero.

Exact calibration forces the unique truth mapping
\[
\rho_\delta=(1/2+3\delta/2,\ 0,\ 0,\ 1,\ 1).
\tag{13}
\]
The 0 and 1 reports force the last four entries; calibration conditional on either expert's report of 1/2 then gives the center entry. The robust value equals the Bayes value in this particular example:
\[
V(p_\delta)=5/6+|\delta|/2.
\]
The optimal prediction at the center profile changes with the sign of \(\delta\). An incorrect choice there incurs unconditional one-period regret \(|\delta|\).

For \(\delta>0\),
\[
D_{\rm KL}(p_\delta\|p_{-\delta})
=2\delta\log\frac{1+3\delta}{1-3\delta}
\le24\delta^2.
\tag{14}
\]
Take \(\delta=1/(12\sqrt T)\). The total variation distance between the two distributions of any pre-period history is at most \(\sqrt{1/12}<1/2\), by additivity of KL and Pinsker's inequality. The sum of the two sign-error probabilities is therefore at least 1/2. The current center profile has the same probability in both models and provides no extra information about the sign.

Averaging the regret under \(+\delta\) and \(-\delta\) gives
\[
\boxed{\inf_{\mathcal A}\sup_p\operatorname{Reg}_T\ge\sqrt T/48.}
\tag{15}
\]
This holds already for two experts and two actions. It establishes the sharp \(T\)-exponent at fixed finite alphabets under **exact** calibration. It does not assert this lower bound for every nonzero tolerance; a sufficiently permissive tolerance can change or trivialize the robust decision problem.

### 1.6 Exact integration controls

For equally likely profiles in \(\{1/3,2/3\}^2\), the complete feasible family is
\[
\rho(a)=\begin{pmatrix}a&2/3-a\\2/3-a&2/3+a\end{pmatrix},
\qquad0\le a\le1/3.
\]
Binary-prediction robust accuracy is exactly **2/3**. Following either expert's threshold guarantees that value. At \(a=1/6\), even a predictor that knows the truth mapping cannot exceed 2/3, proving optimality.

Replacing this joint family by independent coordinate intervals produces **7/12**, not 2/3. The original constraints couple the coordinates; the larger coordinatewise uncertainty set permits combinations that no jointly calibrated law allows. The implementation preserves the joint polytope.

A second control verifies that duplicating a calibrated report does not increase its robust accuracy: one expert with reports 0.2/0.8 and two identical copies both yield 0.8. A single always-observed profile (0.2,0.8) is rejected as incompatible with exact calibration rather than silently repaired. For comparison, two genuinely conditionally independent accuracy-0.8 positive signals at prior 1/2 yield posterior 16/17, whereas a perfect copy of one such signal leaves posterior 4/5. These are different observation models.

## 2. Q725: regularization changes the geometry of reward safety

The source's unregularized theorem characterizes safe coverage distributions using finitely many strict linear inequalities, and expressly asks for a regularized extension. The key result here is that a finite-facet extension works for a polyhedral lifted model, but **fails in general even for entropy regularization in a one-state MDP**. [S2, Theorem 3.5 and Appendix C.3.5]

### 2.1 A general occupancy–penalty lift

Fix a finite discounted MDP and its compact space \(\Pi\) of stationary randomized policies. Let \(d(\pi)\) be the **unnormalized** discounted occupancy vector, so
\[
J_r(\pi)=d(\pi)\cdot r.
\]
Let \(\omega:\Pi\to[0,\infty)\) be continuous and \(\lambda>0\). For the true reward \(R\), assume that policy returns are nonconstant. Fix a regret threshold \(L\in[0,1]\), and put
\[
b=J_R^{\max}-L(J_R^{\max}-J_R^{\min}).
\]
A policy is bad exactly when \(R\cdot d(\pi)\le b\), including equality.

Form the compact convex lift
\[
K=\operatorname{conv}\{(d(\pi),\omega(\pi)):\pi\in\Pi\}.
\tag{16}
\]
For a direction \(q\), let \(F_K(q)=\arg\max_{z\in K}q\cdot z\) be the exposed face. Define
\[
\mathcal B_{\lambda,L}
=\{r:F_K((r,-\lambda))\cap\{(d,w):R\cdot d\le b\}\ne\varnothing\}.
\tag{17}
\]
Equivalently, (17) is a union of slices of normal cones at bad lifted points:
\[
\exists z=(d,w)\in K:\quad R\cdot d\le b,
\quad(r,-\lambda)\in N_K(z).
\]
Here \(N_K(z)=\{q:q\cdot(z'-z)\le0\text{ for all }z'\in K\}\).

**Theorem 2.** The set in (17) is precisely the set of reward vectors admitting a regularized-optimal policy with true normalized regret at least \(L\).

**Proof.** A bad maximizing policy provides a point in the intersection immediately. Conversely, any point in the exposed face is a finite convex combination of lifted policy points. Every component with positive weight must maximize the same exposing linear functional. If every such policy had true return strictly greater than \(b\), so would the convex combination. Hence at least one component is both maximizing and bad. ∎

The set \(\mathcal B_{\lambda,L}\) is closed. To see this, take convergent bad reward vectors and select a bad maximizing policy for each. Compactness provides a convergent subsequence of policies. Continuity of occupancy, penalty and return preserves badness and optimality in the limit.

### 2.2 Exact margin and the zero-coverage distinction

For a coverage distribution \(D\), define
\[
\Delta(D)=\inf_{r\in\mathcal B_{\lambda,L}}
\sum_i D_i|r_i-R_i|,
\tag{18}
\]
with an empty infimum equal to infinity.

For strictly positive \(D\), the objective is coercive and the bad set is closed. Therefore the infimum is attained whenever finite, and
\[
\boxed{D\text{ is safe}\iff
\Delta(D)>\epsilon\,\operatorname{range}R.}
\tag{19}
\]
This preserves the source's strict regret threshold and non-strict reward-error threshold. Equality in (19) is unsafe when attained.

If some \(D_i=0\), the weighted error is a seminorm. The exact general criterion is still that **every** bad reward has weighted error strictly greater than the allowed radius. When the infimum equals the radius, one must check whether it is attained; closedness alone does not make an unbounded seminorm sublevel set compact. The finite polyhedral construction below removes this attainment ambiguity.

For every continuous penalty, the safe set remains convex: it is the intersection, over all bad rewards \(r\), of the strict affine conditions
\[
D\cdot|r-R|>\epsilon\,\operatorname{range}R
\]
with the coverage simplex. Convexity does not imply finitely many facets.

### 2.3 A finite LP characterization for polyhedral lifts

Suppose the **full** lift (16) is supplied as a polytope with vertices
\(z_j=(d_j,w_j)\), each with an actual policy witness. This includes suitable piecewise-affine penalties in occupancy coordinates; merely being piecewise-affine in policy probabilities does not automatically prove that the occupancy lift is polyhedral.

A maximizing face has a bad point if and only if it has a bad vertex. For each vertex with \(R\cdot d_j\le b\), solve
\[
\begin{aligned}
\min_{r,t}\quad&\sum_iD_it_i\\
\text{subject to}\quad&
(d_\ell-d_j)\cdot r\le\lambda(w_\ell-w_j)
\quad\text{for every }\ell,\\
&t_i\ge r_i-R_i,\quad t_i\ge R_i-r_i,\quad t_i\ge0.
\end{aligned}
\tag{20}
\]
Take the smallest feasible objective over the bad vertices. This equals \(\Delta(D)\), and a minimizing \(r\) together with vertex \(j\) certifies failure. Every feasible LP has a finite attained optimum because its objective is bounded below by zero. Thus (19) holds in this case **also at zero coverage**.

A finite matrix representation also follows. Split each reward-optimality polyhedron in (20) into the finitely many orthants of \(r-R\). In each orthant, express the nonnegative absolute-deviation vector \(v=|r-R|\). The resulting polyhedron is pointed. Any nonnegative objective \(D\cdot v\) has a vertex minimizer when feasible. Collect all these finitely many vertex deviation vectors into the rows of \(M\). Then
\[
\Delta(D)=\min_j(MD)_j,
\qquad D\text{ safe}\iff MD>\epsilon\,\operatorname{range}R\,\mathbf1.
\tag{21}
\]
The matrix may be very large. This is an exact finite characterization given the lift, not a polynomial-time method for constructing arbitrary lifts or for arbitrary continuous penalties.

### 2.4 Why randomized breakpoints must be included

Take a one-state, two-action MDP with discount \(\gamma=1/2\),
\[
R=(1,0),\quad D=(0.7,0.3),\quad
\omega(\pi)=|\pi_2-1/2|,\quad\lambda=0.4,\quad L=1/2.
\]
The full lifted polytope is generated by
\[
(d,w)=((2,0),1/2),\ ((1,1),0),\ ((0,2),1/2).
\]
Its middle point is a randomized-policy breakpoint, not a deterministic policy.

The unregularized safety margin is **0.30**. The regularized margin is **0.24**. An attaining reward is \(\hat R=(1,0.8)\): the equally mixed policy is regularized-optimal and has true regret 1/2. It ties with the pure good policy, but the contract quantifies over **every** maximizer, so this is a valid failure witness.

Consequently, error tolerance 0.239 is safe and tolerance 0.24 is unsafe. With coverage \(D=(1,0)\), the same failure has zero weighted error. Regularization here decreases the margin. No universal protective effect should be inferred from the presence of a penalty.

### 2.5 Entropy yields a genuinely curved safety boundary

Take a one-state, three-action MDP with
\[
\gamma=1/2,\qquad R=(1,1,0),\qquad\lambda=2,
\qquad\omega(\pi)=\mathrm{KL}(\pi\|\mathrm{Unif}_3).
\]
Use \(0\log0=0\), so the penalty is continuous and nonnegative on the closed policy simplex. Since unnormalized occupancy is \(2\pi\), the unique regularized optimizer for learned reward \(r\) is \(\operatorname{softmax}(r)\). True normalized regret is its third-action probability.

Set \(L=1/3\). For positive coverage weights with \(D_3\ge1/2\), write \(s=D_1+D_2\). Then
\[
\boxed{
\Delta(D)=s-D_1\log\frac{2D_1}{s}
-D_2\log\frac{2D_2}{s}.
}
\tag{22}
\]
A minimizing reward witness is
\[
\hat R=\left(\log\frac{2D_1}{s},
\log\frac{2D_2}{s},0\right),
\tag{23}
\]
which induces third-action probability exactly 1/3.

**Proof.** A learned reward is unsafe exactly when
\[
\exp(r_1-r_3)+\exp(r_2-r_3)\le2.
\]
Clipping \(r_1,r_2\) down to at most 1 and \(r_3\) up to at least 0 weakens this constraint and cannot increase weighted error. Hence restrict to those values. Put \(v_i=r_i-r_3\). The objective becomes
\[
s-D_1v_1-D_2v_2+(D_3-s)r_3.
\]
Because \(D_3\ge s\), it is bounded below by \(s\) minus the maximum of \(D_1v_1+D_2v_2\) over \(e^{v_1}+e^{v_2}\le2\). Set \(q_i=e^{v_i}\). Weighted logarithmic optimization over \(q_1+q_2\le2\) gives \(q_i=2D_i/s\). Taking \(r_3=0\) attains the bound and respects \(r_i<\log2<1\). This proves (22) and (23). ∎

For example:

| Coverage \(D\) | Exact/formula margin | Safe at \(\epsilon=0.36\)? |
|---|---:|---|
| \((0.2,0.2,0.6)\) | \(0.4\) | Yes |
| \((0.3,0.1,0.6)\) | \(0.3476751856235453\) | No |

The second witness is \((\log1.5,\log0.5,0)\), producing policy \((1/2,1/6,1/3)\).

To verify that this is not merely a nonlinear formula for a polyhedral set, compute the Hessian in \((D_1,D_2)\):
\[
\nabla^2\Delta
=-\operatorname{diag}(1/D_1,1/D_2)+\frac1s\mathbf1\mathbf1^\top.
\tag{24}
\]
Its only zero direction is radial; it is strictly negative on directions changing the ratio \(D_1:D_2\). A tangent to a positive level set cannot be radial, by positive homogeneity and Euler's identity. Thus these level curves have nonzero curvature. For example, the level \(\Delta=0.36\) has a curved arc strictly inside \(D_3>1/2\). Writing \(t=D_1/s\), this arc is
\[
s=\frac{0.36}{1-\log2+h(t)},\qquad
h(t)=-t\log t-(1-t)\log(1-t),
\]
near \(t=1/2\).

It follows that **no finite matrix of strict linear inequalities can characterize this safety region**. The same finite-matrix form as the unregularized theorem therefore cannot extend to every continuous regularizer. This does not refute the unregularized theorem: it identifies a real geometric change introduced by the regularizer.

## 3. Q449: a common decoder for an overlapping rank-two code

The source proves truncation dominance at independence and equal-magnitude opposite correlations, and conjectures it for arbitrary opposite correlations. The supplied map records earlier one-row progress. The construction here handles a genuinely overlapping two-row code. [S3, Theorem 2 and Conjecture 1]

Let
\[
G_\triangle=\begin{pmatrix}1&0&1\\0&1&1\end{pmatrix},
\qquad0\le p_0\le1/2\le p_1\le1.
\]
Under hypothesis \(h\), the noise bits \(Z_i=X_i\oplus Y_i\) are independent Bernoulli\((p_h)\). The target compressed noise is
\[
V=(Z_1\oplus Z_3,Z_2\oplus Z_3).
\]
The truncated experiment supplies two independent noise bits \(W=(Z_1,Z_2)\).

Set
\[
c=p_0+p_1-2p_0p_1,\qquad
\alpha=1-\frac{p_0p_1}{c},\qquad
\beta=1-\frac{(1-p_0)(1-p_1)}c.
\]
Since \(c\ge1/2\) and both numerator products are at most 1/2, \(\alpha,\beta\in[0,1]\). In input/output order 00, 01, 10, 11, use the channel
\[
K=\begin{pmatrix}
\alpha&(1-\alpha)/3&(1-\alpha)/3&(1-\alpha)/3\\
0&1/3&1/3&1/3\\
0&1/3&1/3&1/3\\
\beta&(1-\beta)/3&(1-\beta)/3&(1-\beta)/3
\end{pmatrix}.
\tag{25}
\]
This is one channel for the two specified hypotheses, not a decoder that knows which hypothesis generated the sample.

Under Bernoulli\((p)\) input, its probability of output 00 is
\[
\alpha(1-p)^2+\beta p^2
=1-3p+3p^2-\frac{(p-p_0)(p-p_1)}c.
\]
At both \(p=p_0\) and \(p=p_1\), this equals the target probability \(1-3p+3p^2\). The three other target outputs each have probability \(p(1-p)\); symmetry of the last three columns and normalization give them exactly.

To reconstruct the full compressed pair, draw an independent uniform \(U\in\mathbb F_2^2\) and output \((U,U\oplus V)\). Full row rank makes \(GX\) uniform and independent of \(GZ\), so this reproduces \((GX,GY)\) under either hypothesis. This is an explicit Blackwell garbling certificate.

For \(p_0=1/10,p_1=7/10\), (25) is
\[
\begin{pmatrix}
59/66&7/198&7/198&7/198\\
0&1/3&1/3&1/3\\
0&1/3&1/3&1/3\\
13/22&3/22&3/22&3/22
\end{pmatrix}.
\]

The construction tensorizes over disjoint triangle blocks and identity bits. It also survives column permutations, unused zero columns, and invertible row transformations. This proves an infinite family of full-rank codes, while leaving the unrestricted conjecture open here.

### 3.1 Exact finite search beyond the construction

A rank-two matrix, modulo invertible row transformations and column permutations, is characterized by the counts \((a,b,c)\) of nonzero column types 10, 01, 11. At least two types must occur; sorting the counts removes the row-transformation symmetry. Zero columns can be dropped.

Writing \(t=1-2p\), the output noise law is
\[
q_p(u,v)=\tfrac14\left[1+(-1)^u t^{a+c}
+(-1)^v t^{b+c}+(-1)^{u+v}t^{a+b}\right].
\]
I checked every such orbit through effective length 20: **337 orbits**. For each, I checked all 81 pairs
\[
p_0\in\{1/20,\ldots,9/20\},\quad
p_1\in\{11/20,\ldots,19/20\}.
\]
The resulting **27,297 comparisons** passed.

These comparisons use exact integer probability numerators. The finite binary-experiment Blackwell condition is checked via all likelihood-ratio breakpoints of
\[
\sum_x(P_0(x)-tP_1(x))_+
\ge\sum_y(Q_0(y)-tQ_1(y))_+,
\]
including 0 and the limiting condition at infinity. Between consecutive breakpoints the difference is affine, making the check exact for each parameter pair. This criterion is also described in the source's numerical section. [S3, §5]

The test is not an all-parameter proof. In addition, 121 rational tests verified every entry and both pushforward identities of (25), including boundary hypotheses. One of these is the redundant equal-hypothesis point \(p_0=p_1=1/2\); the construction still works there.

## 4. Q810: nearest dependence graphs

For undirected graphs on a fixed vertex set, the distance counts disagreements on all statements of whether \(u\) and \(v\) are separated by \(S\subseteq V\setminus\{u,v\}\). Equivalently, test connectivity in the induced graph after removing \(S\). The source conjectures that a globally nearest alternative always occurs by one edge addition or deletion. Its reported small-scale evidence uses five vertices. [S4, §3.2]

### 4.1 A sufficient endpoint certificate

Let
\[
r_1(G)=\min_{H:\,|E(G)\triangle E(H)|=1}d(G,H).
\]
For every nonedge \(e=uv\), let
\[
s_G(e)=\#\{S:u\perp_Gv\mid S\},\qquad
 a(G)=\min_{e\notin E(G)}s_G(e),
\]
where a minimum over no nonedges is infinity.

**Theorem 3.** If \(a(G)\ge r_1(G)\), then \(r_1(G)\) is the global minimum distance to any different graph.

**Proof.** Consider any alternative \(H\). If it adds an edge \(uv\), every separation of those endpoints in \(G\) becomes a dependence in \(H\). The direct edge survives every allowed conditioning set, regardless of other edge changes. Hence
\(d(G,H)\ge s_G(uv)\ge a(G)\ge r_1(G)\).

Otherwise \(H\) is a proper subgraph of \(G\). Choose \(e\in E(G)\setminus E(H)\). Since \(H\subseteq G-e\subseteq G\), separation indicators are monotone under these deletions. Every query changed by deleting only \(e\) is also changed in \(H\). Thus \(d(G,H)\ge d(G,G-e)\ge r_1(G)\). A one-edge minimizer achieves the lower bound. ∎

This is a sufficient certificate, not a necessary condition. Failing it does not refute the conjecture. Computing its ingredients by exhaustive separation queries is still exponential in vertex count; no general polynomial-time audit is asserted.

### 4.2 Complete multipartite graphs: a proved infinite class

**Corollary.** Q810 holds for every complete multipartite graph, including complete bipartite graphs and stars.

**Proof.** A nonedge \(uv\) lies inside one independent part \(A\). Both endpoints are adjacent to every vertex outside \(A\). If any outside vertex remains after conditioning, the induced graph's vertices in \(A\) are already connected through it. If no outside vertex remains, all surviving vertices of \(A\) are isolated, and adding \(uv\) changes only the connectivity of that pair. Therefore
\[
d(G,G+uv)=s_G(uv)=2^{|A|-2}.
\]
Taking the minimum over nonedges gives \(r_1(G)\le a(G)\), and Theorem 3 applies. If the graph is complete there are no nonedges and every alternative is a subgraph, so the deletion argument applies directly. ∎

### 4.3 Exhaustive checks through seven vertices

The C++ program builds the complete separation signature of every labelled graph. It then compares each isomorphism representative with every labelled alternative. Importantly, it independently verifies that all supplied representatives cover every labelled graph by enumerating their vertex permutations. Thus representative completeness is checked within the computation rather than assumed from the graph-atlas library.

| Vertices | Labelled graphs | Representatives | Separation queries per graph | Counterexamples |
|---:|---:|---:|---:|---:|
| 2 | 2 | 2 | 1 | 0 |
| 3 | 8 | 4 | 6 | 0 |
| 4 | 64 | 11 | 24 | 0 |
| 5 | 1,024 | 34 | 80 | 0 |
| 6 | 32,768 | 156 | 240 | 0 |
| 7 | 2,097,152 | 1,044 | 672 | 0 |

Signatures and distances use exact integer bit operations. A separate Python implementation exhaustively verified all 1,024 labelled five-vertex graphs, using an independently ordered enumeration of conditioning sets.

The endpoint certificate alone certifies **113 of the 156** six-vertex isomorphism representatives. The other 43 require another argument, even though exhaustive global comparison verifies the conjecture for them too.

This supplies exact finite evidence and a proved infinite subclass, not a proof for arbitrary graphs. The DAG version Q811 was not included in this computation.

## 5. Reproducibility and numerical qualifications

The package includes the following implementations:

- `calibrated_forecasts.py`: joint truth-mass calibration constraints, feasible-profile projection, robust aggregation, and a profile-only online learner.
- `reward_safety.py`: the lifted-polytope margin LP and the entropy example, including an independent convex-optimization cross-check.
- `garbling.py`: the exact rational common decoder and exact integer rank-two experiment comparisons.
- `graph_controls.py`, `graph_audit.py`, `graph_audit.cpp`: the endpoint certificate, independent five-vertex checker, representative generation, and exhaustive C++ audit.
- `run_checks.py`: deterministic regression checks and recorded outputs.

The mathematical proofs establish the all-parameter statements above. Floating-point optimization is used to test implementations, not to establish those theorems. The recorded checks include 50 projection/aggregation problems at five tolerance levels, 80 entropy-margin comparisons, 121 rational decoder identities, 27,297 exact experiment comparisons, and the graph audits in the table.

The largest residual in the 50 LP projection/aggregation controls was approximately \(1.11\times10^{-16}\). The maximum discrepancy between the entropy formula and the independent convex optimizer over 80 cases was approximately \(2.50\times10^{-13}\). These are numerical consistency checks, not machine-verified safety certificates for arbitrary near-boundary inputs. The exact rational examples and proofs explicitly address the strict equality cases.

The code was tested with Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0 and NetworkX 3.6.1. The graph audit requires a C++20 compiler. Its exhaustive scope is deliberately capped at seven vertices. It is a benchmark oracle, not a scalable graph-learning algorithm.

## 6. What these results change in the next prototype

**Forecast aggregation.** Store one joint feasible truth-mass polytope, reject incompatible asserted calibration, and project empirical profile laws before optimizing. Retain the profile-only information contract. This lets copied evidence remain copied evidence rather than acquire an invented independent likelihood.

**Decision safety.** Evaluate the distance to a bad regularized optimum, not just average reward-prediction error. A failed certificate should return an alternative reward and a bad optimal policy. Include randomized-policy breakpoints and equality cases. Entropy regularization calls for curved optimization geometry, not an assumed finite table of linear coverage inequalities.

**Representation changes.** Require a single stochastic channel valid under the retained hypotheses. The triangle kernel is a concrete exact regression fixture. A collection of separately fitted model-specific decoders is not the same certificate.

**Dependence repair.** Report separation-query distance and an alternative graph witness. Apply the endpoint certificate where it succeeds; label other outputs as bounded exhaustive results or unresolved. Ordinary edge-edit distance is not the metric in Q810.

These are mathematical and reference-implementation deliverables. They do not certify the truth of natural-language reports, the empirical calibration of an extractor, a causal interpretation of a learned graph, or safe deployment under an incorrect utility model. Grounded measurement and independent validation remain separate tasks.

## Sources and provenance

The source papers supply the questions, contracts and prior results identified above. All newly derived statements are proved in this report. Source versions were checked during this work; no claim is made to have exhaustively searched every subsequent or unindexed result.

**[S1]** Xinxiang Guo, Yingkai Li and Yifen Mu. *Robust Aggregation of Calibrated Forecasts*. arXiv:2606.31020v1, 30 June 2026. Especially §4, Theorem 2, and Appendix A. https://arxiv.org/html/2606.31020v1

**[S2]** Lukas Fluri, Leon Lang, Alessandro Abate, Patrick Forré, David Krueger and Joar Skalse. *The Perils of Optimizing Learned Reward Functions: Low Training Error Does Not Guarantee Low Regret*. ICML 2025; inspected arXiv:2406.15753v3. Especially Definition 2.1, Theorem 3.5 and Appendix C.3.5. https://arxiv.org/html/2406.15753v3

**[S3]** Adway Girish, Robinson D. H. Cung and Emre Telatar. *On the Suboptimality of Linear Codes for Binary Distributed Hypothesis Testing*. arXiv:2601.10526v2, 9 July 2026. Especially Theorem 2, Conjecture 1 and §5. https://arxiv.org/html/2601.10526v2

**[S4]** Juha Harviainen, Pekka Parviainen and Vidya Sagar Sharma. *Learning Bayesian and Markov Networks with an Unreliable Oracle*. UAI 2026; arXiv:2603.09563. Especially §3.2 and Conjectures 1–2. https://arxiv.org/html/2603.09563

**Supplied programme:** `03_research_map(1).md`, especially the active-portfolio discussion and the Q413, Q449, Q725 and Q810 investigation cards; Collections 5, 8 and 9 for their complete formulations. Collections 6, 7 and 10 were also available as part of the programme. The file hashes in `input_manifest.json` identify the actual seven inputs.
