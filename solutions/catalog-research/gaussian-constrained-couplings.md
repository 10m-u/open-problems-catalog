# Prescribed Gaussian marginals on affine manifolds

**Result.** Prescribed univariate Gaussian marginals admit a joint law supported on an affine subspace exactly when a finite covariance feasibility problem succeeds. Any successful coupling can be replaced by a Gaussian coupling with a compact sampler. When the subspace has dimension at most two, exact rational feasibility reduces to linear equations and at most one quadratic inequality. For two overlapping sum constraints, there is also a closed formula for the smallest possible squared violation while preserving every marginal.

These are **restricted answers** to Jayanti's Open Problem 5.1, connected to the catalog's shared-separator work. Gaussian mixability and covariance methods have established antecedents. The arbitrary-marginal, arbitrary-manifold question remains unresolved here, and these Gaussian marginals do not provide the nonnegative bids needed for a Blotto equilibrium.

## Source and exact model

Siddhartha Jayanti, *On computing Nash equilibria of Borel's Colonel Blotto Game for multiple players including in arbitrary measure spaces* (2020), Open Problem 5.1, printed p. 62, asks when one-dimensional marginal distributions can be coupled on a specified manifold and how to construct those couplings efficiently. Exact extraction ID: `41b1c7792350f621ca27`; local thesis text; [MIT record](https://dspace.mit.edu/handle/1721.1/127347). The question is broader than finding compatible unconstrained marginals.

Here D_i = N(μ_i,σ_i²), with zero variances permitted, and the specified manifold is M = {x in Rⁿ : Ax = b}. “Supported on” means contained in M, so a singular coupling on a smaller subspace is allowed. Marginals remain exact. We either enforce all support constraints or minimize a declared residual; we do not silently change the input laws.

## Exact existence and construction

**Affine Gaussian coupling theorem.** A coupling of the prescribed D_i supported on M exists if and only if

\[
A\mu=b,\qquad C\succeq0,\quad C_{ii}=\sigma_i^2,\quad AC=0
\]

for some symmetric matrix C. The coupling need not initially be jointly Gaussian for necessity to hold. Whenever C exists, X = μ + F G is a valid coupling, where FFᵀ = C and G is a vector of independent standard Gaussians. F may have only rank(C) columns.

**Proof.** Every coupling has finite second moments and a positive semidefinite covariance C with the required diagonal. Ax = b almost surely implies Aμ = b and Cov(AX,X) = AC = 0. Conversely, factor a feasible C = FFᵀ. Then A C Aᵀ = (AF)(AF)ᵀ = 0, so AF = 0. Thus X has the given univariate Gaussian marginals and AX = Aμ + AF G = b identically. ∎

Let N have columns forming a basis of ker(A). Equivalent covariance variables are C = NQNᵀ, Q positive semidefinite, with

\[
\operatorname{diag}(NQN^\top)=s,\qquad s=(\sigma_1^2,\ldots,\sigma_n^2).
\]

This is a semidefinite feasibility problem on the dimension of the allowed subspace. It replaces a search over probability laws by a finite matrix problem. General numerical SDP solvers need feasibility tolerances and care at singular boundaries; the reduction alone is not an unconditional claim of an exact polynomial-time bit algorithm for arbitrary SDP input.

There is an exact dual rejection certificate: if some y satisfies Nᵀ diag(y) N positive semidefinite but y·s < 0, no coupling exists. For any feasible Q, y·s = tr(Q Nᵀ diag(y) N) ≥ 0. Such a certificate exists whenever covariance feasibility fails: the cone of attainable variance vectors is closed. To see closedness, work with C positive semidefinite and range(C) contained in ker(A). A convergent sequence of diagonals bounds tr(C), which bounds the matrices; a convergent subsequence yields a feasible limiting C. Cone separation then supplies y. A failed mean constraint is a separate elementary certificate.

## An exact solver for subspaces of dimension at most two

The [solver](gaussian_affine_coupling.py) handles rational A,b,μ,s with dim ker(A) ≤ 2, including zero variances, redundant constraint rows and singular covariances. It returns an exact covariance and sampling factor when feasible.

- For dimension zero, all variances must vanish.
- For dimension one, Q is one nonnegative scalar, so all diagonal equations must agree on that scalar.
- For dimension two, write Q = [[u,v],[v,w]]. Each marginal supplies a linear equation N_i1² u + 2 N_i1 N_i2 v + N_i2² w = s_i. Because N has two independent rows, these equations have rank at least two: the outer products of two independent row vectors are linearly independent. Hence a consistent solution is either one point or one affine line. Positive semidefiniteness is exactly u ≥ 0, w ≥ 0 and uw−v² ≥ 0. On a line this is a system of univariate linear and quadratic inequalities, solved exactly by SymPy. Feasible algebraic endpoints are retained rather than rounded away.

Factor Q = BBᵀ and use F = NB in the sampler. Thus the implementation constructs a law, rather than merely reporting that a feasibility test passed. Higher-dimensional subspaces are explicitly outside this exact solver's implementation; the general matrix theorem still applies.

## Shared separators: two feasible constraints can conflict

Consider centred normals with standard deviations (1,2,2,2), and require

\[
X_1+X_2+X_3=0,\qquad X_2+X_3+X_4=0.
\]

Each equation separately permits a Gaussian coupling. For the first, the standard deviations (1,2,2) satisfy the closed-triangle condition; for the second they are (2,2,2). Their simultaneous enforcement, however, implies X_1 = X_4 almost surely, contradicting their unequal variances. A dual certificate is y = (1,0,0,−1): on ker(A), x_1 = x_4, so its restricted quadratic form is zero, while y·s = 1−4 = −3.

This is the general issue for larger shared interfaces. Each local constraint specifies a permissible joint law, but its shared separator (X_2,X_3) must agree across contexts. The first constraint requires Var(X_2+X_3) = 1; the second requires it to be 4. Agreement of the singleton laws of X_2 and X_3 does not ensure agreement of their joint separator law. Choosing these context couplings independently defeats global realization.

## A sharp bound when the marginals are protected

For arbitrary nonnegative standard deviations (a,b,c,d), retain centred Gaussian marginals and minimize

\[
\mathcal R=\mathbb E[(X_1+X_2+X_3)^2+(X_2+X_3+X_4)^2]
\]

over **all** couplings. Let I = [|b−c|,b+c], m = (a+d)/2, and let s* be m clipped to I. Then

\[
\boxed{\min\mathcal R=(s^*-a)^2+(s^*-d)^2
=\tfrac12(a-d)^2+2\operatorname{dist}(m,I)^2.}
\]

In particular, an exactly supported coupling for both equations exists precisely when a = d and a belongs to I. Both local triangle inequalities alone omit the equality a = d.

**Lower bound.** Work in the Hilbert space of centred square-integrable random variables. Put S = X_2+X_3 and s = ||S||₂. Triangle and reverse-triangle inequalities give |b−c| ≤ s ≤ b+c. They also give ||X_1+S||₂ ≥ |a−s| and ||X_4+S||₂ ≥ |d−s|. Hence every coupling has residual at least (a−s)²+(d−s)². This convex quadratic minimizes at the clipped value s*.

**Attainment and sampler.** Take independent standard normals Z,W. If s* > 0, set α = ((s*)²+b²−c²)/(2s*) and h = sqrt(b²−α²). The interval condition ensures h is real. Define

\[
X_1=aZ,\quad X_4=dZ,\quad
X_2=-\alpha Z+hW,\quad X_3=(\alpha-s^*)Z-hW.
\]

Their variances are exactly a²,b²,c²,d² and their shared sum is −s*Z, so the residual attains the bound. If s* = 0, necessarily b = c; use X_2 = bW and X_3 = −bW while keeping X_1 = aZ and X_4 = dZ. This also covers fully degenerate cases. ∎

For the incompatible (1,2,2,2) example, s* = 3/2 and the exact minimum residual is **1/2**. An optimal protected-marginal sampler is

\[
X_1=Z,\quad X_2=-\tfrac34 Z+\tfrac{\sqrt{55}}4W,\quad
X_3=-\tfrac34 Z-\tfrac{\sqrt{55}}4W,\quad X_4=2Z.
\]

The two sum residuals are −Z/2 and Z/2. This gives a quantitative, attainable obstruction. It differs from 54f's TV repair problem: here input marginals stay fixed and support constraints incur a squared violation; in 54f the allowed changes are distributional corrections to context laws. Their numeric budgets are not interchangeable.

The function `shared_separator_optimum` returns the optimal value and exact sampler for rational standard deviations. Its lower bound is valid for any finite-variance marginals; attainment as written relies on the Gaussian family, so the formula is not asserted for arbitrary marginal shapes.

## Prior work, executed controls and remaining scope

[Wang–Wang, *Joint Mixability* (2016), Example 2.2 and Theorem 3.7](https://sas.uwaterloo.ca/~wang/papers/2015Wang-Wang-MOR.pdf), supplies the established Gaussian/elliptical constant-sum framework and scale conditions. [Dandapanthula et al., *Optimal Transportation and Alignment Between Gaussian Measures*, §4.2 and Appendix A.6](https://arxiv.org/html/2512.03579v1), uses covariance-based semidefinite reductions for multimarginal quadratic transport. Its objective is different from enforcing a prescribed affine support, but its Gaussian replacement argument is a close antecedent. The local existence theorem, low-dimensional elimination, and overlap residual calculation are specializations of established covariance geometry; novelty of the particular overlap formula has not been established.

Run:

```sh
python3 solutions/catalog-research/gaussian_affine_checks.py
```

The [results](gaussian-affine-checks.json) record 189 cases checked against the independently known weighted normal polygon criterion, 168 seeded exact primal cases generated from one- or two-dimensional Gaussian factors, and all 625 standard-deviation quadruples in {0,…,4}⁴ for the overlap residual. The audits check exact marginal variances, annihilation by A, sampling-factor identities, attained residuals, scalar optimality conditions and agreement between zero residual and support feasibility. They also verify the explicit dual obstruction, a rank-one boundary covariance, fixed coordinates, and a failed mean constraint. No Monte Carlo estimate is used as a feasibility certificate.

For the solver CLI, put A,b,means,variances in JSON and pass its path:

```json
{"A": 1,1,1, "b": [0], "means": [0,0,0], "variances": [1,1,4]}
```

```sh
python3 solutions/catalog-research/gaussian_affine_coupling.py /tmp/coupling-input.json
```

The three inputs above admit the singular sampler (Z,Z,−2Z). Fractions can be JSON strings to preserve exact rational input.

**Remaining work:** identify a particular bounded, nonnegative family and budget manifold from the actual Blotto model before extending this result toward equilibria. Ordinary covariance feasibility is generally only necessary for non-Gaussian marginals, and nonlinear manifolds add higher-order support constraints. The broad thesis extraction keeps a **partial** mark and remains eligible for review.
