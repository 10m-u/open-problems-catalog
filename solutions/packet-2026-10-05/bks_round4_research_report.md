# Fourth research group: isolated moment contacts and predictive Hellinger budgets

**Bayesian Knowledge System — 5 October 2026**

## Results and scope

| Target | Result derived in this report | Scope |
|---|---|---|
| Q738: the Gaussian 3k-moment conjecture | A proof of generic rational identification of k univariate Gaussian components from moments 1 through 3k, modulo component permutation | The stated complex, generic target; not identification at every exceptional parameter and not a stable recovery algorithm |
| Q742: gamma and inverse Gaussian mixtures | The same proof gives generic rational identification from 3k moments for both families | Full stated grouped target, with the same generic and arithmetic qualifications |
| Q812 continuation: non-circular kernels and multivariate predictive resampling | An averaged Hellinger criterion; global L2 sufficiency under square-summable weights; finite-entropy sufficiency at harmonic rates; conditional KL and TV truncation bounds | Fixed positive bistochastic kernels with exact current-distribution transport and predictive resampling |
| Q615: the full-output Hellinger dictator conjecture | An affinity formulation, an exact obstruction to a stronger multiplicative inequality, and a rigorous finite-grid audit through four Boolean inputs | The full conjecture remains unresolved in this report |

The new mixture result is a written proof using an established non-weak-defectivity criterion. The infinite-time predictive results are written measure-theoretic proofs. Their computer checks are supporting finite certificates, not substitutes for the arguments. No proof assistant or independent mathematical referee has checked these proofs, and external publication priority is not established.

The programs in this package are standalone reference controls. They do not modify or certify the original knowledge-system scaffold.

## 1. Why these targets, and what was checked before pursuing them

The earlier Q418 argument used confluent interpolation to close a local identification threshold for a multiplicative latent model. Its transferable ingredient is not a theorem that local identification implies global uniqueness. It is the ability to construct exact tangent-rank witnesses using polynomial multiplicities. Here an additional isolated-contact calculation supplies the missing global geometric ingredient.

The earlier Q812 work identified the Hellinger affinity of a predictive likelihood-ratio increment as the correct convergence object for circular copulas. This round removes the equal-row-law restriction, using a distinguished-point change of measure. A second, entropy-based calculation gives a usable truncation certificate.

The Hellinger dictator conjecture is a directly connected, longstanding information-theoretic problem: it asks for the largest Hellinger information gain of a Boolean summary under noisy observations. A common mathematical functional does not establish that the predictive-density theorem proves that conjecture. The distinction is maintained below.

### 1.1 Status check

The uploaded catalogue states Q738 as generic one-to-one identification of the complexified Gaussian mixture moment map at order 3k. It explicitly excludes the known finite-fiber result at 3k−1 and rational identification at 3k+2. Q742 asks the same 3k question for gamma and inverse Gaussian mixtures.

The inspected primary sources support the following status as of this check:

- Lindberg, Améndola and Rodriguez, *Estimating Gaussian Mixtures Using Sparse Polynomial Moment Systems*, SIAM Journal on Mathematics of Data Science 7(1), 2025, prove the 3k+2 result and retain the 3k conjecture.
- Henriksson, Ranestad, Seccia and Yu, *Moment varieties of the inverse Gaussian and gamma distributions are nondefective*, Journal of Symbolic Computation 132 (2026), article 102460, explicitly retain the conjectural 3k improvement for Gaussian, gamma and inverse Gaussian mixtures. Its inspected arXiv v3 is dated 7 June 2025.
- Fong, Holmes and Walker, *Martingale posterior distributions*, JRSS B 85(5), 2023, explicitly conjecture removal of their univariate Gaussian-copula restriction for the specified approximately 2/i weights and L1 convergence of their joint multivariate autoregressive update. The univariate harmonic 1/(i+1) result without the correlation restriction is already known and is not counted as a new result here.
- Steiner, Huk and Steel, *Scalable Multivariate Martingale Posteriors*, TPM 2026, prove weak convergence for a different construction: coordinatewise marginal updates coupled through a fixed copula. Theorem 2 is not a total-variation theorem for the Fong–Holmes–Walker joint update. Its PDF was inspected, rather than treating its title as a resolution of that target.
- Durcik, Fraccaroli and Roos, *A weak Hellinger inequality for noisy Boolean channels*, arXiv:2609.28534v2, 29 September 2026, retain the full-output Hellinger conjecture and prove the version conditioning on one Boolean statistic of the output. The original full-output conjecture dates to the 2015 Simons program and the 2017 ITA paper of Anantharam, Bogdanov, Chakrabarti, Jayram and Nair.

Courtade–Kumar was considered and excluded: September 2026 primary preprints announce proofs, and the September 29 Hellinger paper explicitly acknowledges those announcements. This report does not independently audit those proofs and does not pursue Courtade–Kumar as an unsolved target.

There is one unresolved priority issue on the predictive side. Pietro Rigo's current publication list names a submitted 2026 manuscript by Dreassi, Pratelli and Rigo, *On the limit of copula based predictive distributions*. Its contents were not available in the retrieved materials. Possible overlap with this round or round three therefore remains unverified. The mathematical arguments below are explicit and self-contained; their publication priority is a separate question.

## 2. A common isolated-contact theorem for moment surfaces

### 2.1 The precise lemma

Fix k≥1 and put d=3k. The coordinate m_0=1 is normalization, not an additional observed moment. Let S be an irreducible, nondegenerate complex projective surface in P^d. Suppose a smooth, locally embedded affine chart around points (a,0), for a in a nonempty open subset of C, has moment coordinates

\[
\Phi(\mu,v)=[1:m_1(\mu,v):\cdots:m_d(\mu,v)],
\]

regular in that chart, with

\[
m_t(\mu,0)=\mu^t,\qquad
\partial_v m_t(\mu,0)=\binom t2\mu^{t-2}
\quad (0\le t\le d).
\tag{1}
\]

Zero coefficients at t=0,1 are interpreted as zero, without a singular power. Then S is k-identifiable: a generic point of its kth secant variety has one unordered decomposition into k component points.

For application to a statistical parameter map, require additionally that the chosen component parameters are generically recovered from the component moment point. This is checked explicitly for each family below.

### 2.2 Independent tangent conditions

Choose k distinct allowed points a_1,...,a_k. A hyperplane with coefficients c_0,...,c_d pulls back to

\[
F(\mu,v)=\sum_{t=0}^{d}c_t m_t(\mu,v).
\]

Write P(z)=Σ_t c_t z^t. At x_i=Φ(a_i,0), the projective tangent-plane containment equations are

\[
F(a_i,0)=F_\mu(a_i,0)=F_v(a_i,0)=0.
\]

By (1), these are exactly

\[
P(a_i)=P'(a_i)=P''(a_i)=0.
\tag{2}
\]

These 3k linear constraints are independent. Indeed, a polynomial of degree at most 3k−1 satisfying them has k distinct triple roots and must be zero. Thus the tangent vectors have the expected rank 3k, and their projective span has dimension 3k−1, strictly below the ambient dimension 3k.

An exact determinant identity makes this witness explicit. With rows t=0,...,3k−1 and column blocks

\[
\big(a_i^t,\;t a_i^{t-1},\;\tbinom t2a_i^{t-2}\big),
\]

the determinant is

\[
\boxed{\prod_{i<j}(a_j-a_i)^9.}
\tag{3}
\]

This is the confluent Vandermonde determinant with the second-derivative columns divided by two.

### 2.3 A unique tangent hyperplane with isolated contacts

Let

\[
Q(z)=\prod_{i=1}^{k}(z-a_i),\qquad P(z)=Q(z)^3.
\tag{4}
\]

Equations (2) show that this is the unique tangent hyperplane, up to scaling, for the selected k points.

Differentiate its pullback F. At every selected point,

\[
F_{\mu\mu}(a_i,0)=P''(a_i)=0,
\qquad
F_{\mu v}(a_i,0)=\tfrac12P'''(a_i)=3Q'(a_i)^3.
\]

The second v-derivative can depend on the family; it is not needed. The Hessian determinant is

\[
\boxed{
\det\nabla^2F(a_i,0)
=-\tfrac14[P'''(a_i)]^2
=-9Q'(a_i)^6\ne0.
}
\tag{5}
\]

Consequently the hyperplane section has an isolated ordinary double point at each x_i. In particular, no positive-dimensional contact component passes through a designated point.

### 2.4 Why this proves a generic, not merely special, statement

On the open set of k-tuples where the tangent-constraint matrix has rank 3k, normalize the tangent hyperplane by a nonzero coefficient. The hyperplane then depends rationally on the tuple, by solving a linear system.

Each of the k Hessian determinants is a rational function of that tuple on the chosen smooth charts. At the tuple constructed above, all are nonzero. Their simultaneous nonvanishing therefore defines a nonempty Zariski-open subset of the irreducible parameter space of tuples. For general component points, the tangent hyperplane is consequently isolated at all of them.

In the standard terminology S is not k-weakly defective. The needed external geometric implication is:

> Non-k-weak-defectivity of an irreducible nondegenerate projective variety implies generic k-identifiability in the subgeneric setting used here.

Freire, Casarotti and Massarenti state the contact-locus definition and this implication in §2, Definition 2.2 and the immediately following paragraph, attributing it to the infinitesimal Bertini theorem of Chiantini–Ciliberto. Their definition includes exactly the components of the hyperplane-section singular locus that contain at least one selected point. Thus the proof does not need to rule out unrelated singularities at projective infinity.

The expected tangent rank has already been established, and 3k−1<3k. Applying the criterion proves the lemma.

**This is the step that cannot be replaced by a Jacobian rank computation.** Rank only proves finite generic ambiguity. The isolated Hessian contacts and the geometric criterion eliminate that ambiguity.

## 3. Q738 and Q742: applying the lemma

All three families use mean μ and variance v as coordinates. For gamma and inverse Gaussian, restrict to μ≠0 when taking algebraic closures. The initial moment coordinates satisfy

\[
m_0=1,\qquad m_1=\mu,\qquad m_2=\mu^2+v.
\tag{6}
\]

Hence the component moment map is an embedded graph on this affine open set, with inverse μ=m_1, v=m_2−m_1^2. These points are smooth even at v=0.

The physical distribution at v=0 is a point mass, not a positive-variance member of the family. It nevertheless belongs to the algebraic moment surface and its regular affine chart. For gamma, the usual shape parameter diverges along this limit; that does not make the moment-surface point singular. Mean/variance coordinates resolve the apparent parameter-chart obstruction.

The surface is irreducible as the closure of an irreducible parameterized image. It is nondegenerate because its point-mass curve [1:μ:...:μ^d] spans P^d.

### 3.1 Gaussian moments

For an ordinary Gaussian with mean μ and variance v,

\[
m_t^G(\mu,v)=
\sum_{j=0}^{\lfloor t/2\rfloor}
\frac{t!}{2^j j!(t-2j)!}\mu^{t-2j}v^j.
\tag{7}
\]

The constant and linear coefficients in v are μ^t and binom(t,2)μ^(t−2), respectively. Thus (1) holds.

**Theorem G.** For every k≥2, a generic complexified k-component univariate Gaussian mixture is uniquely determined, modulo component permutation, by m_1,...,m_{3k}.

The weights are also determined: the unique component points are generically linearly independent, and the affine mixture coefficients summing to one are unique in their span. Over characteristic zero, generic degree one gives a birational map onto the image after the component-permutation quotient. This is rational identifiability in Q738's sense; it does not mean that ordered individual component labels are rational functions without choosing a labeling.

### 3.2 Gamma moments

For shape α and scale θ,

\[
\mu=\alpha\theta,\qquad v=\alpha\theta^2,
\qquad \alpha=\mu^2/v,\quad\theta=v/\mu.
\]

For t≥1,

\[
m_t^\Gamma(\mu,v)=
\prod_{j=0}^{t-1}\left(\mu+j\frac v\mu\right).
\tag{8}
\]

This is regular on μ≠0, including v=0. Its linear coefficient in v is (Σ_{j=0}^{t−1}j)μ^(t−2)=binom(t,2)μ^(t−2), so (1) holds. The change of coordinates is birational on the generic locus μv≠0.

### 3.3 Inverse Gaussian moments

For mean μ and shape λ, v=μ^3/λ. For t≥1,

\[
m_t^{IG}(\mu,v)=\mu^t
\sum_{j=0}^{t-1}
\frac{(t+j-1)!}{j!(t-j-1)!}
\left(\frac{v}{2\mu^2}\right)^j.
\tag{9}
\]

Equivalently,

\[
m_0=1,\quad m_1=\mu,\quad
m_t=(2t-3)(v/\mu)m_{t-1}+\mu^2m_{t-2}.
\tag{10}
\]

Again the constant and linear coefficients in v give (1). The chart is regular for μ≠0 and λ=μ^3/v is a rational inverse on the generic locus.

**Theorem GI.** For every k≥2, a generic complexified k-component gamma mixture, and a generic complexified k-component inverse Gaussian mixture, are rationally identifiable from their first 3k moments, modulo component permutation.

This answers both families in the grouped question Q742. Moments beyond 3k also identify a generic mixture, since the first 3k already do so.

### 3.4 What is and is not established

The statements are about generic finite-dimensional mixture models with known component count. They do not say that every parameter tuple is identifiable, that arbitrary distributions are determined by these moments, or that overfitted representations with more components are excluded. They also do not prove 3k is the smallest possible number for every k; the source question asks its sufficiency for generic rational identification.

The positive real parameter domain is Zariski dense. The nonempty algebraic open set therefore gives generic identification for positive weights and positive component variances/shapes as well. Exceptional sets, tiny weights, nearly coincident components and finite-sample moment noise remain important. Neither the proof nor the code supplies a uniform condition number, sample bound or polynomial-time stable inversion procedure.

### 3.5 Executed checks

`moment_contacts.py` verifies the first variance jet through moment order 72 for all three families, 219 identities. It checks 16 exact confluent determinants, up to dimension 48×48; 36 boundary configurations with 234 contact Hessians; and 18 strictly positive-variance configurations with 63 contact Hessians, through k=6.

The independent verifier constructs second-order bivariate Taylor jets from three distribution-specific moment recurrences rather than the producer's coefficient formulas. It checks every contact, all 18 interior tangent ranks, and rejects a perturbed hyperplane. Repeated-node and double-instead-of-triple-root controls fail in the intended ways.

These finite checks corroborate the explicit all-k proof. They are not numerical evidence being promoted to a proof of generic global uniqueness.

## 4. General predictive-density convergence beyond circular copulas

### 4.1 Update contract

Let μ_0 have a positive density f_0 on R^d. Let K(u,v)>0 be a fixed measurable bistochastic kernel on (0,1)^d×(0,1)^d:

\[
\int K(u,v)\,dv=1\quad\text{for a.e. }u,
\qquad
\int K(u,v)\,du=1\quad\text{for a.e. }v.
\tag{11}
\]

Finite positive versions off irrelevant null sets suffice. At step n let T_n be the exact current-distribution transport to the uniform cube. The Rosenblatt transform is one choice when f_n is positive: its coordinates are successive conditional CDFs. Draw V_{n+1} uniformly from the cube, equivalently draw X_{n+1} from μ_n and put V_{n+1}=T_nX_{n+1}. Update

\[
f_{n+1}(x)=f_n(x)
\left[1-r_n+r_nK(T_nx,V_{n+1})\right],
\quad 0<r_n\le1.
\tag{12}
\]

The r_n are deterministic here. Normalization follows from the column identity in (11); pointwise martingality follows from the row identity. The unknown law is not changed branch by branch, and the transport is not frozen at its initial value.

Define

\[
\bar h_K(r)=1-\iint\sqrt{1-r+rK(u,v)}\,du\,dv,
\tag{13}
\]

and, when finite,

\[
\kappa_K(r)=\iint[1-r+rK(u,v)]\log[1-r+rK(u,v)]\,du\,dv.
\tag{14}
\]

Logs are natural. Since the multiplier has mean one,

\[
\bar h_K(r)=\tfrac12\iint
\left(\sqrt{1-r+rK(u,v)}-1\right)^2du\,dv\ge0.
\tag{15}
\]

### 4.2 Averaged Hellinger theorem

**Theorem H.** If

\[
\boxed{\sum_{n=0}^\infty\bar h_K(r_n)<\infty,}
\tag{16}
\]

then μ_n converges almost surely in total variation to a probability measure absolutely continuous with respect to μ_0, and hence to Lebesgue measure. No bound on the worst copula row is required.

#### Distinguished-point proof

Let P be the law of the uniform innovation sequence and its generated densities. On the enlarged space of an entire history ω and a point x, let

\[
B(d\omega,dx)=P(d\omega)\mu_0(dx),\qquad
M_n(\omega,x)=f_n(\omega,x)/f_0(x).
\]

Let G_n contain the first n innovations and x. Construct another probability law Q by initially drawing x from μ_0 and then drawing each next innovation v with conditional density

\[
A_n(x,v)=1-r_n+r_nK(T_nx,v)
\]

relative to uniform. Its row integral is one. The usual sequential kernel construction gives Q directly; no limiting density is assumed to exist. Induction gives

\[
\frac{dQ|_{G_n}}{dB|_{G_n}}=M_n.
\tag{17}
\]

Since every f_n integrates to one, Q and P have the same marginal law for the finite history, and hence for the full history. Conditional on that history through time n, the distinguished point has density f_n under Q.

Under Q, N_n=1/M_n is a positive martingale. Put

\[
Z_n=A_n^{-1/2}-1,
\qquad h_n(u)=1-\int\sqrt{1-r_n+r_nK(u,v)}\,dv.
\]

The conditional innovation density under Q is A_n, so

\[
E_Q[Z_n\mid G_n]=-h_n(T_nx),
\quad
E_Q[Z_n^2\mid G_n]=2h_n(T_nx).
\tag{18}
\]

The crucial averaging identity is

\[
E_Qh_n(T_nx)
=E_P\int f_n(x)h_n(T_nx)dx
=\int h_n(u)du
=\bar h_K(r_n).
\tag{19}
\]

Thus Σ Z_n^2 and Σ h_n(T_nx) are finite Q-almost surely. The centered differences Z_n+h_n(T_nx) have summable expected variances, so their partial sums are an L2-bounded martingale and converge almost surely. Hence Σ Z_n converges as well.

All 1+Z_n are positive. The elementary logarithm criterion (convergent Σ Z_n and finite Σ Z_n^2) implies

\[
N_n=\prod_{j<n}(1+Z_j)^2\longrightarrow N_\infty\in(0,\infty)
\quad Q\text{-a.s.}
\tag{20}
\]

For an event E in G_m, Fatou and (17) give

\[
\int_E N_\infty\,dQ\le\liminf_{n\to\infty}\int_E N_n\,dQ=B(E).
\]

A monotone-class argument extends this domination to the full sigma-field. Since N_∞>0 Q-almost surely, Q is absolutely continuous with respect to B. Write its density as M_∞. The two laws' identical history marginals imply

\[
\int M_\infty(\omega,x)\mu_0(dx)=1\quad P\text{-a.s.}
\]

Moreover M_n=E_B[M_∞|G_n]. Martingale convergence and Fubini give pointwise convergence in x along almost every history. Both the finite and limiting densities have mass one. Scheffé's lemma proves pathwise L1, hence total-variation, convergence. This proves Theorem H.

### 4.3 Global L2 replaces a uniform row bound

Set

\[
C_K=\iint(K(u,v)-1)^2du\,dv.
\]

Since (√A−1)^2=(A−1)^2/(√A+1)^2≤(A−1)^2,

\[
\bar h_K(r)\le\tfrac12r^2C_K.
\tag{21}
\]

**Corollary L2.** Every fixed positive square-integrable bistochastic kernel preserves a density and gives almost-sure TV convergence whenever Σ r_n^2<∞.

This requires an integrated second moment, not the original supplied proposition's essential supremum of conditional row second moments. It also places no local L2 requirement on the initial Lebesgue density. The reference measure in the proof is μ_0 itself.

### 4.4 Finite entropy and harmonic-rate schedules

Let U,V be independent uniform cube points and C=K(U,V). Then EC=1 and (13) depends only on the distribution of C. For r_n=1/(n+2),

\[
\boxed{\sum_n\bar h_K(r_n)<\infty
\iff E[C\log_+C]<\infty.}
\tag{22}
\]

Here is a direct scalar proof. Put ψ(s)=(√(1+s)−1)^2. For s≥0, ψ(s)≤min(s,s^2/4). For C≤2, ψ((C−1)/j)≤j^−2 for j≥2. For C>2, split the sum at j≈C: the initial part is O(C log C), and the tail O(C). This gives the forward upper bound from finite entropy.

Conversely, when C≥4j, A=1+(C−1)/j≥C/j≥4 and (√A−1)^2≥A/4≥C/(4j). Tonelli gives

\[
\sum_{j=2}^\infty\bar h_K(1/j)
\ge\tfrac18E\left[C\sum_{2\le j\le C/4}\frac1j\right].
\]

The right side is infinite when E[C log_+ C] is infinite. This proves (22). The same splitting argument shows sufficiency for any deterministic r_n=O(1/n), with an arbitrary finite prefix.

**Corollary E.** Finite kernel entropy, ∫∫K log K<∞, guarantees density/TV convergence for every fixed-kernel harmonic-rate update in (12).

This is strictly broader than global L2: the circular kernel generated by g(t)=(1−β)t^−β, 1/2≤β<1, has finite entropy but infinite second moment.

The entropy condition is not asserted to be necessary for every individual non-circular kernel. It is sharp as a guarantee using only the distribution of K(U,V): any positive mean-one value distribution can be realized by a circular copula, and the earlier round's circular dichotomy gives a singular limit whenever the corresponding Hellinger series diverges. In particular, infinite entropy is not permission to declare every arbitrary kernel singular.

### 4.5 A conditional KL identity and computable truncation bounds

**Theorem K.** Suppose Σ κ_K(r_n)<∞. Then, for every n,

\[
\boxed{
E\left[D_{KL}(\mu_\infty\|\mu_n)\mid\mathcal F_n\right]
=\sum_{j=n}^\infty\kappa_K(r_j).
}
\tag{23}
\]

The result is also valid at a finite stopping time, with the corresponding tail sum, for this fixed kernel and deterministic schedule.

To prove it, first consider the entropy relative to μ_0. Averaging one update gives

\[
E\int f_{n+1}\log(f_{n+1}/f_0)
=E\int f_n\log(f_n/f_0)+\kappa_K(r_n).
\tag{24}
\]

The first logarithmic term uses the row integral of A; the second uses the current transport's uniform pushforward. Thus E_B[M_n log M_n]=Σ_{j<n}κ_K(r_j). Bounded entropy makes the nonnegative likelihood-ratio martingale uniformly integrable, giving a mass-one density limit as above.

Since M_n=E_B[M_∞|G_n], Jensen and Fatou applied to t log t, bounded below by −1/e, show that the final entropy is exactly the limit of the finite entropies. Restart this argument conditionally at time n with μ_n as reference measure and the remaining deterministic schedule. This proves (23). Splitting according to the values of a finite stopping time gives the stopped version.

Pinsker's inequality, in the convention TV=sup_A|P(A)−Q(A)|, yields

\[
E[TV(\mu_\infty,\mu_n)^2\mid\mathcal F_n]
\le\tfrac12\sum_{j=n}^\infty\kappa_K(r_j),
\tag{25}
\]

and consequently

\[
P\{TV(\mu_\infty,\mu_n)>\epsilon\mid\mathcal F_n\}
\le\frac{\sum_{j\ge n}\kappa_K(r_j)}{2\epsilon^2}.
\tag{26}
\]

Because log A≤A−1 and ∫∫A=1,

\[
\kappa_K(r)\le\iint(A-1)^2=r^2 C_K.
\tag{27}
\]

Therefore the exact global L2 certificate supplies computable upper bounds in (23)–(26). For losses in [0,1], TV bounds every fixed action's expected-loss discrepancy. If an action is chosen optimally under μ_n rather than μ_∞, its excess limiting Bayes loss is at most 2TV; this is a decision-loss conversion, not a claim about an unknown real-world truth law.

Finite entropy alone at harmonic rates establishes Theorem H but need not make the stronger KL sum finite. Formula (23) is not applied without its own summability condition.

## 5. The multivariate Gaussian-copula application

For a bivariate Gaussian copula c_ρ with fixed |ρ|<1,

\[
\iint c_\rho(u,v)^2du\,dv=\frac1{1-\rho^2},
\qquad
\iint c_\rho\log c_\rho=-\tfrac12\log(1-\rho^2).
\tag{28}
\]

For completeness, let Σ=[[1,ρ],[ρ,1]]. Under the independent standard-normal reference measure, the squared density ratio integrates as det(Σ)^−1 det(2Σ^−1−I)^−1/2. The latter matrix is positive definite and has determinant one, proving the L2 identity. The entropy identity is the Gaussian relative-entropy formula, or follows directly by integrating the log ratio.

The conditional row L2 integral is

\[
\int c_\rho(u,v)^2dv
=\frac{\exp(\rho^2z^2/(1+\rho^2))}{\sqrt{1-\rho^4}},
\qquad z=\Phi^{-1}(u).
\tag{29}
\]

For nonzero ρ this is unbounded as u approaches an endpoint, although its integral over u is finite. This explains exactly why a uniform-row argument misses cases handled by the new proof.

For the fixed product kernel in d dimensions,

\[
K(u,v)=\prod_{j=1}^dc_{\rho_j}(u_j,v_j),
\qquad
C_K=\prod_{j=1}^d(1-\rho_j^2)^{-1}-1<\infty.
\tag{30}
\]

**Corollary FHW.** The exact joint autoregressive predictive update of Fong–Holmes–Walker converges almost surely in L1 to a density, in every fixed finite dimension, for all fixed correlations |ρ_j|<1 and every square-summable deterministic weight schedule. This includes the paper's prescribed approximately 2/i schedule. Conditional truncation bounds follow from (25)–(27).

This addresses the exact joint update with current conditional CDFs in arXiv equation (4.10), not the separate conditional-regression construction, not a fixed marginal-CDF approximation, and not frequentist consistency for external iid observations. The latter is a different sampling law and theorem in the source.

### 5.1 A serialized bound, not a simulated convergence claim

`density_contract.py` creates an exact rational truncation contract for

\[
d=2,\quad(\rho_1,\rho_2)=(3/5,4/5),\quad r_j=2/(j+3).
\]

Here C_K=481/144. The integral test gives

\[
\sum_{j\ge n}r_j^2
\le4\left[\frac1{n+3}+\frac1{(n+3)^2}\right].
\]

The program finds 53,443 as the smallest integer meeting this particular sufficient bound for conditional probability at least 0.95 of TV error at most 0.05. It verifies the resulting rational inequality and failure of that bound one step earlier. **Those 53,443 resampling steps were not simulated.** This is a theoretical budget certificate; the bound is conservative and is not an optimality claim.

The constant grows with dimension and correlations near ±1. Qualitative convergence at every fixed parameter is not a dimension-uniform precision guarantee.

### 5.2 Finite exact implementation checks

The non-row-homogeneous three-by-three copula histogram is

\[
K=\begin{pmatrix}
3/2&1&1/2\\
1/2&7/4&3/4\\
1&1/4&7/4
\end{pmatrix}.
\]

Each entry describes one equally sized cell. Every row and column sums to three, but the row value distributions differ. Starting with a uniform density on [0,1], the program splits at each current CDF's one-third and two-thirds quantiles and executes five levels of predictive updates. There are 121 internal histories and 243 leaves.

The independent verifier checks every child likelihood ratio and density normalization, the exact conditional rank masses, the martingale identity, and all 121 finite conditional KL identities corresponding to (23). These KL checks use rational linear combinations of logarithms of primes: no floating-point logarithm is needed. Thirty-nine rational Gaussian-copula correlations also pass the exact determinant calculation behind (28).

The finite tree is a regression control for the moving-transport and change-of-measure identities, not evidence about the infinite-time tail on its own.

## 6. Q615: the full-output Hellinger conjecture

### 6.1 Exact reduction to an affinity problem

Let X be uniform on {−1,1}^n, and let Y be its noisy version with independent coordinate correlation ρ. For f taking values ±1, put p=P(f(X)=1), and let P_+,P_- be the conditional laws of Y given the two feature values. For 0<p<1,

\[
E_Y\sqrt{1-(E[f(X)\mid Y])^2}
=2\sqrt{p(1-p)}\,\operatorname{Aff}(P_+,P_-),
\tag{31}
\]

where Aff(P,Q)=∫√(dP dQ). This follows by inserting Bayes' rule pointwise; the mixture output density cancels. Constant features have zero gain and are handled separately.

The full conjecture is therefore exactly

\[
\boxed{
2\sqrt{p(1-p)}\,[1-\operatorname{Aff}(P_+,P_-)]
\le1-\sqrt{1-\rho^2}.
}
\tag{32}
\]

The output here is the entire noisy vector. Conditioning on an arbitrary Boolean g(Y) is weaker and cannot establish (32). Also, after conditioning on a nonlinear f(X), the input bits, and hence the output coordinates, need not remain independent. The product-affinity formulas used in the earlier common-decoder and circular-copula work cannot simply be substituted.

### 6.2 An exact obstruction to a tempting stronger inequality

A natural attempted route is the stronger multiplicative statement

\[
E\sqrt{1-(E[f\mid Y])^2}
\stackrel{?}{\ge}
\sqrt{1-(Ef)^2}\sqrt{1-\rho^2}.
\tag{33}
\]

It is false. Let B indicate that all n input bits are one, let f=2B−1, and set a=(1+ρ)/2. Given an output with w ones,

\[
P(B=1\mid Y)=a^w(1-a)^{n-w}.
\]

Using √(q(1−q))≤√q and summing the binomial expansion gives

\[
\frac{E\sqrt{1-(E[f\mid Y])^2}}
{\sqrt{1-(Ef)^2}}
\le
\frac{[(\sqrt a+\sqrt{1-a})/\sqrt2]^n}
{\sqrt{1-2^{-n}}}.
\tag{34}
\]

For every fixed 0<|ρ|<1, the right side tends to zero as n grows, while the claimed lower bound √(1−ρ^2) is a positive constant. Thus the failure is systematic, not a numerical anomaly.

An exact small certificate uses n=8, ρ=3/5 and a=4/5. Squaring the upper bound gives

\[
\frac{(9/10)^8}{255/256}<\frac{16}{25}=1-\rho^2.
\tag{35}
\]

This refutes (33). It does **not** refute the original conjecture (32). The original expression for this example has a strictly positive certified slack, and rare features have a small prefactor 2√(p(1−p)). Discarding that prefactor is precisely what makes the stronger route invalid.

### 6.3 Rigorous finite-grid audit

The program enumerates all Boolean functions for n=1,2,3,4, reducing by input-coordinate permutations, input sign flips and output complementation. The resulting orbit counts are 2,4,14,222, covering 65,812 truth tables in total.

For every orbit it checks ρ=j/20, j=1,...,19. There are 4,598 orbit/grid cases. Seventy-six dictator cases are verified by exact equality; all 4,522 remaining cases have strictly positive lower bounds.

Every posterior mean has an exact integer numerator. Square roots of the resulting nonnegative integer radicands are enclosed using integer square roots at 35 decimal places, producing rational interval certificates. The smallest certified non-dictator slack is about 0.000209956689364, at n=4, representative truth mask 127 and ρ=1/20.

The independent verifier rechecks all orbit sizes, disjoint coverage, the posterior calculations and interval inequalities. This is not a proof between the grid points or above four inputs. The full Hellinger conjecture remains an active unsolved target in this report. The established progress is the explicit reduction and the elimination of the multiplicative route, together with a reusable exact finite control.

## 7. Reproduction, evidence, and limitations

All programs use Python's standard library. From the package root:

```bash
python code/run_all.py
python code/verify.py
```

The verifier imports no producer module and uses no numerical optimizer. For the moment results it reconstructs local Taylor jets from recurrences, not the producer's closed-form coefficients. For the Boolean checks it recomputes the full noisy posterior. For the predictive checks it reconstructs CDF cuts and density likelihood updates and verifies conditional KL identities exactly.

Executed finite checks include:

| Check | Count |
|---|---:|
| Moment first-variance-jet identities | 219 |
| Confluent determinant identities | 16 |
| Boundary moment configurations / individual contacts | 36 / 234 |
| Positive-variance moment configurations / individual contacts | 18 / 63 |
| Exact interior tangent-rank checks | 18 |
| Boolean symmetry-orbit/grid cases | 4,598 |
| Boolean truth tables covered by the orbits | 65,812 |
| Internal predictive histories / terminal leaves | 121 / 243 |
| Exact conditional KL identities | 121 |
| Rational Gaussian L2 determinant checks | 39 |

The verifier rejects a damaged moment hyperplane and a damaged predictive density. The supplied code and proofs are not formal verification of the geometric theorem, the martingale convergence theorem, Scheffé's lemma, or Pinsker's inequality. Those mathematical dependencies are explicit.

The results change two scientific choices: which finite moment summaries generically preserve a component model, and which predictive resampling kernels and truncation budgets preserve density-based uncertainty. They do not establish grounded sensor calibration, semantic truth, real-world forecast gains, or production integration. The Hellinger conjecture remains unresolved rather than being reported as solved because a finite audit passed.

## References and status sources

URLs identify sources inspected in this run; no exhaustive bibliography or priority search is claimed.

1. Uploaded collections 5–10, `01_solutions(1).md`, `02_project_review(1).md`, `03_research_map(1).md`, and the three earlier generated reports. Exact hashes appear in `input_manifest.json`.
2. Julia Lindberg, Carlos Améndola, Jose Israel Rodriguez. *Estimating Gaussian Mixtures Using Sparse Polynomial Moment Systems*. SIAM Journal on Mathematics of Data Science 7(1), 224–252 (2025). https://doi.org/10.1137/23M1610082 ; https://arxiv.org/html/2106.15675 . The 3k target versus the proved 3k+2 result is distinguished.
3. Oskar Henriksson, Kristian Ranestad, Lisa Seccia, Teresa Yu. *Moment varieties of the inverse Gaussian and gamma distributions are nondefective*. Journal of Symbolic Computation 132 (2026), 102460. https://arxiv.org/html/2409.18421v3 ; https://doi.org/10.1016/j.jsc.2025.102460 . Introduction, future directions, and the component moment recurrences were inspected.
4. Ageu Barbosa Freire, Alex Casarotti, Alex Massarenti. *On tangential weak defectiveness and identifiability of projective varieties*. arXiv:2002.09915v3 (2022), §2. https://sfera.unife.it/retrieve/3a3cac4e-d1ae-40dd-a570-94628eca79a8/2002.09915.pdf . Printed page 3 was inspected as an image for Definition 2.2 and the implication to identifiability, attributed there to Chiantini–Ciliberto.
5. Edwin Fong, Chris Holmes, Stephen G. Walker. *Martingale posterior distributions*. JRSS B 85(5), 1357–1391 (2023). https://arxiv.org/html/2103.15671v2 ; https://academic.oup.com/jrsssb/article/85/5/1357/7597700 . The joint update, predictive resampling law and explicit convergence conjectures were checked. Frequentist consistency is a distinct section and is not the result claimed here.
6. Gregor Steiner, David Huk, Mark F. J. Steel. *Scalable Multivariate Martingale Posteriors*. TPM 2026. https://tractable-probabilistic-modeling.github.io/tpm2026/papers/CwQQV9Dpg3.pdf . This paper uses another copula-coupled marginal construction and proves weak convergence; it does not settle the exact joint-update TV target here.
7. Pietro Rigo, current publication list. https://www.unibo.it/sitoweb/pietro.rigo/pubblicazioni . The submitted Dreassi–Pratelli–Rigo 2026 title *On the limit of copula based predictive distributions* was located, but its contents were not retrieved. Overlap and priority remain unverified.
8. Polona Durcik, Marco Fraccaroli, Joris Roos. *A weak Hellinger inequality for noisy Boolean channels*. https://arxiv.org/html/2609.28534v2 (29 September 2026), equations (1.2), (1.4). It distinguishes the original full-output conjecture from its proved one-bit-output version and records the recent Courtade–Kumar proof announcements.
9. Venkat Anantharam, Andrej Bogdanov, Amit Chakrabarti, T. S. Jayram, Chandra Nair. *A conjecture regarding optimality of the dictator function under Hellinger distance*. ITA 2017. Original target as explicitly restated in source 8 and the uploaded Q615 formulation.
10. Zijie Chen, Amin Gohari, Adel Javanmard, Honghao Lin, Vahab Mirrokni, Chandra Nair, David P. Woodruff. *A proof of the most informative Boolean function conjecture*. https://arxiv.org/abs/2609.24931 . This proof announcement is a reason to exclude Courtade–Kumar as an open target; its formal artifacts were not independently run.
