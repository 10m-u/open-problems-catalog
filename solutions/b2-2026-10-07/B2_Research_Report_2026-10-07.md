# B2 research report: addition and multiplication over integers and finite fields

**7 October 2026 · Exact-scope research return for the attached 48-question programme**

## Principal outcomes

The strongest quantitative construction obtained here is

\[
\boxed{\liminf_{n\to\infty}\Lambda_{n,4}\ge\frac{50368}{90905}
=0.5540729332819977\ldots.}
\]

An explicit nine-interval colouring has an exact integer count at every scale. This improves the four-colour lower bound 10/21 supplied by the cited September 2026 source. It does not determine the optimum or prove convergence of the extremal densities.

Other substantial deductions are:

- For **provisional Q2462, stable ID `ab65e680b82754944885`**, every equal-coefficient equation c(x₁+⋯+x_k)=0, k≥3 and c≠0, has d(L,ε)=1/k for every fixed ε>0. The proof includes the restricted-sum polynomial coefficient argument and an interval construction with independence number at most k−1.
- For **provisional Q2469, stable ID `d4554ad68bb1d9e77596`**, WKL₀ proves the retained ring-colouring assertion over RCA₀, with at most [3(n−1)]^(n−1) colours for n≥2. An explicit finite-presentation argument removes a hidden quotient-range comprehension step. A matching reversal is not established.
- For Q2215, any decomposition of a set differing from the squares by o(√X) elements must introduce at least X^(1/3−o(1)) nonsquares. In particular perturbations O(X^(1/3−δ)), δ>0, cannot decompose.
- For Q2315 and Q2316, integral points exist over every p-adic field, and real points exist. Q2316 additionally has the exact rational point (−13/20,−79/20,21/5). Neither equation can be ruled out by any finite modulus, but the requested global integer points remain missing.
- The Paley work proves an exact degree-two obstruction, a justified localization-to-SOS₄ transfer, and a sharp characterization of coherence saturation. It includes exact clique certificates and rational relaxation certificates for every eligible prime through 300.
- The squarefree work proves the finite-product transfer required to assess family 020 correctly. Factor degrees at most 3 are unconditional using the classical input; a cutoff 4 remains conditional on the imported quartic theorem. The linked comparator has a `by sorry` stub and is not a completed proof receipt.
- Exact cubic square-product searches through b≤10⁷ reproduce precisely the retained lists; all 65,536 finite sets containing0 in[0,16] were exhausted for factorization lengths; cyclotomic powers-of-two subfamilies and several algebraic restrictions are proved.

**No one of the 48 full retained questions is marked solved or disproved.** The report records proved auxiliary theorems separately from the exact-scope status of the question they advance. Some elementary consequences reproduce known results or specialize established methods; no blanket novelty claim is made. No theorem was compiled in a proof assistant.

The accompanying JSON ledger preserves all 48 exact retained statements and stable IDs. The verification archive contains the complete input packet, scripts, exact certificates, raw outputs, and a hash manifest. Full proofs are included below; the report is not merely an index of files.

## Programme decision and tool-to-target map

B2 is productive as a coordinated collection of precisely specified arithmetic problems. Its strongest connection to the original inverse programme is the Paley setting, where additive differences are tested by multiplicative characters and multiplication by squares creates an exact cyclic symmetry after localization. The remaining families need their own reductions; membership in B2 is not a common mathematical reduction.

| Target | Domain and operations | Degeneracy or obstruction | Justified consequence here | What is still required |
|---|---|---|---|---|
| Q2187–Q2191, Paley | Addition on F_p; multiplicative characters on F_p*; additive differences tested for quadratic-residue membership | Group orders p and p−1 differ; constants and the missing multiplicative-basis direction must be handled | A flat basis pair on the common mean-zero space; exact support and robust uncertainty | For indicators, exact additive support is full; useful concentration or higher correlations are needed |
| Q2187–Q2190, relaxations | PSD matrices built from χ(x−y); square multiplication acts on a localized vertex set | The global degree-two feasible point attains √p exactly | SOS₄(G_p)≤1+τ(L_p), with rational finite certificates | Uniform character-sum or dual-certificate estimates across large primes |
| Provisional Q2462 (`ab65e680b82754944885`) | Linear equations and Cayley graphs on the additive group F_p | Fixed integer coefficients are repeated addition, not a separate multiplicative group law | Exact d(L,ε)=1/k for common coefficients | Mixed coefficient vectors and their extremal constructions |
| Provisional Q2468 (`3529c68ac8a3205e8a47`) | Schur-free sets and Cayley chromatic number | Large chromatic number does not imply the small independence number required by the Ramsey–Turán parameter | A precise nontransfer between the two graph parameters | An exact density threshold, not only a qualitative classification |
| Q1509–Q1510 | Polynomial addition/multiplication over Z; divisibility modulo p² | Reducibility, degree, and integer-versus-prime arguments alter the hypotheses | Finite-product transfer, including fixed-prime normalization | Squarefree asymptotics for the remaining irreducible factors at the correct argument type |
| Q49, Q1609, Q1611 | Integer polynomial values and multiplication of squarefree kernels | Bounded collision searches do not bound the smallest index globally | Effective reductions and exact bounded classifications | Uniform control of the unbounded kernel/curve family |
| Q2314–Q2316 | Polynomial equations over Z,Q,R,Z_p | Zariski density and local solubility do not give a finite integer parametrization or an integer point | An explicit dense family; rational/local witnesses; exact model limitations | Global arithmetic analysis rather than searching for a forbidden modulus |
| Q2215 | Additive sumsets versus multiplicatively defined squares | Shifted square intersections are finite; moving differences can have many divisors | Error exponent at least1/3−o(1) from the square-sum graph | A stronger uniform incidence estimate to reach the allowed o(√X) scale |
| Q2210, Q2217 | Minkowski addition of finite sets in ordered monoids | Set cardinality is not factorization length; accumulation at0 removes naive descent | Exact length witnesses and exclusions of group/positive-gap counterexamples | General finite length sets; accumulation-at-zero monoids |
| Provisional Q2414 (`fbf539f5a7f03f1da075`), Q2415 (`a06b211ca02e3eb359fa`) | Addition/multiplication in Z[x]; complex root moduli | Cyclotomic factors must be removed with the source convention | Powers-of-two irreducibility subfamilies | Arbitrary cyclotomic indices |
| Provisional Q2469 (`d4554ad68bb1d9e77596`) | Countable rings; additive finite presentations; matrix multiplication | The range sR need not be available in RCA₀ | A finite integer-matrix construction and one WKL step | A reversal or a weaker-system proof |

The theorem label “proved” below means a written argument, sometimes with exact finite arithmetic certificates. A source comparison is labelled separately. Family 020 is not promoted from an imported claim to a verified theorem.

## Contents

- Part A: interval, density, character, and resonance results.
- Part B: Paley proofs, exact cliques, rational certificates, and source-scope audit.
- Part C: squarefree transfer, near-squares, factorization, and cyclotomic subfamilies.
- Part D: Diophantine local proofs, rational witness, searches, and repaired subcase.
- Part E: the WKL₀ upper bound and the explicit finite algorithm.
- Part F: experiment register and reproducibility.
- Part G: complete 48-question exact-statement ledger.
- Part H: remaining decisive targets and evidence boundaries.


## Part A. Interval, character, and density results

Date: 7 October 2026. The arguments in this part are written proofs. Exact arithmetic computations support the constructions; no proof-assistant compilation is claimed. The full retained questions remain unresolved unless a restriction is explicitly stated. The purpose of this report is to establish mathematical consequences and their scope; it makes no claim of priority over all literature.

### 1. Q1861: a four-colour lower bound with an exact count at every scale

**Programme B2; Q1861; stable statement ID `17b96fc493616f6da52c`.**

**Exact retained statement:** Determine liminf_(n→∞) Λ_(n,4) and limsup_(n→∞) Λ_(n,4), including whether they coincide.

For a colouring c:[n]→[4], let R_n(c) count **ordered** pairs (x,y) of positive integers with x+y≤n and c(x), c(y), c(x+y) pairwise distinct. The denominator is binom(n,2)=n(n−1)/2, the total number of these ordered pairs. In particular pairs with x=y are present in the underlying triangle but cannot be rainbow.

**Theorem B2-R1.**

\[
\boxed{\liminf_{n\to\infty}\Lambda_{n,4}\ge
\frac{50368}{90905}=0.5540729332819977\ldots.}
\]

This improves the explicit four-colour lower bound 10/21 obtained from Theorem 1.3 of Hegde–Kumar–Pratibha, [arXiv:2609.18474v1](https://arxiv.org/html/2609.18474v1), dated 16 September 2026. The source gives the general lower bound (k−2)(k+1)/((k−1)(k+3)) and upper bound 1−1/k. Thus the certified interval now is

\[
\frac{50368}{90905}\le\liminf\Lambda_{n,4}
\le\limsup\Lambda_{n,4}\le\frac34.
\]

The upper bound and the possible gap between the two limits are not improved here. No optimality of the construction is asserted.

#### 1.1 The explicit colouring

Set D=90905 and

\[
(b_0,\ldots,b_9)=
(0,22268,29113,38882,48505,56585,60430,73462,82414,90905).
\]

For every integer t≥1, colour the block {tb_i+1,…,tb_(i+1)} as follows:

| i | b_i | b_(i+1) | Colour |
|---:|---:|---:|---:|
| 0 | 0 | 22268 | 1 |
| 1 | 22268 | 29113 | 2 |
| 2 | 29113 | 38882 | 3 |
| 3 | 38882 | 48505 | 4 |
| 4 | 48505 | 56585 | 2 |
| 5 | 56585 | 60430 | 4 |
| 6 | 60430 | 73462 | 3 |
| 7 | 73462 | 82414 | 2 |
| 8 | 82414 | 90905 | 4 |

The exact count is

\[
\boxed{R_{tD}=2289351520t^2+25184t
=25184t(90905t+1).}
\]

In particular its normalized density at n=tD is exactly

\[
\frac{R_{tD}}{\binom{tD}{2}}
=\frac{50368}{90905}\frac{90905t+1}{90905t-1}.
\]

#### 1.2 A symbolic integer certificate, not a fitted polynomial

For an integer s define T(s)=(s+1)(s+2)/2 if s≥0 and T(s)=0 otherwise. For inclusive integer intervals [a,b] and [c,d], the number of pairs with x+y≤h is

\[
T(h-a-c)-T(h-b-1-c)-T(h-a-d-1)+T(h-b-d-2).
\]

This follows by translating to nonnegative x,y, counting the unrestricted triangle, and applying inclusion–exclusion to its two upper bounds. To restrict x+y to a third block, subtract its value at the lower endpoint minus one from its value at the upper endpoint.

For the blocks above, every term has the form T(tH−2), where H is an integer signed sum of endpoint numerators. Write H_+=max(H,0). For **every** integer t≥1,

\[
T(tH-2)=\frac{H_+^2t^2-H_+t}{2}.
\]

If H≤0 both sides vanish. If H≥1 this is the usual triangle formula, including the boundary tH=1 where both sides still vanish. Therefore every interval-triple count is a polynomial in t valid at all positive integer scales.

Sum over all **ordered** interval triples (i,j,k) whose three colours are distinct. Aggregating the coefficients by the colour of x+y gives this compact exact certificate:

| Colour of x+y | Coefficient of t² | Coefficient of t |
|---:|---:|---:|
| 1 | 0 | 0 |
| 2 | 709173547 | 9259 |
| 3 | 658245872 | 8156 |
| 4 | 921932101 | 7769 |
| **Total** | **2289351520** | **25184** |

The short finite sum is implemented verbatim using rational arithmetic in `research/root/rainbow_exact.py`. An independent rectangle counter in `research/squarefree_algebra/verify_rainbow_interval.py` uses direct integer inclusion–exclusion. Its rectangle formula agreed with 2,548 small brute-force cases, and its complete nonzero interval contributions are preserved for t=1,2,3,10,100. The first three total counts are 2289376704, 9157456448, and 20604239232. These checks corroborate the all-t proof; they do not replace it.

For arbitrary n, let t=floor(n/D), colour [tD] as above, and colour the remaining fewer than D integers arbitrarily. Every counted pair on [tD] survives. Since tD/n→1, dividing by binom(n,2) proves the stated **liminf**, rather than merely a subsequence bound.

#### 1.3 Discovery, a simpler construction, and scope

The exploratory search used interval/residue colourings and local improvement of their rainbow-triple area objective. Its floating-point output only suggested a colour pattern and an active cell of a piecewise quadratic function. Exact rational differentiation of that cell produced the displayed endpoints. The proof of the bound depends only on those endpoints and the exact count, not on convergence or completeness of the search.

A short-denominator alternative uses the same nine colours and endpoints

\[
(0,245,320,428,534,622,665,808,907,1000)/1000,
\]

giving 34629/62500=0.554064. A simpler parity construction gives 9/17: colour all even integers 4, and colour odd integers by intervals with normalized endpoints 0,4/17,7/17,13/17,16/17,1 and colours 1,2,3,2,1. At n=34t its exact count is 306t²+6t. Both alternatives are archived as checks and simpler examples.

**Changed assumptions:** none for the stated lower-bound theorem; the conclusion is only one inequality from the retained determination problem. **Evidence:** written argument; primary-source comparison; exact finite computation. **Retained-question status:** partial. Q1860, stable ID `1bbd790f1e916985ec31`, remains unresolved; exploratory three-colour searches did not beat 9/22.

### 2. Provisional Q2462: exact density for every equal-coefficient equation

**Programme B2; provisional Q2462; stable statement ID `ab65e680b82754944885`.**

**Exact retained statement:** If no nonempty subset of the coefficients sums to zero, determine lim_(ε↓0)d(L,ε).

The handoff fixes L:Σ_(i=1)^k c_i x_i=0 with k≥3 and nonzero integer coefficients. A⊆F_p∖{0} is L-free if it has no solution with pairwise distinct coordinates. Cay_p(A) joins distinct u,v when u−v or v−u belongs to A. The density is

\[
d(L,\varepsilon)=\limsup_{p\to\infty\text{ prime}}
\frac1p\max\{|A|: A\text{ is L-free},\ 
\alpha(\operatorname{Cay}_p(A))\le\varepsilon p\}.
\]

**Theorem B2-R2.** Fix k≥3 and a nonzero integer c. For

\[
L:\quad c(x_1+\cdots+x_k)=0,
\]

one has, for every fixed ε>0,

\[
\boxed{d(L,\varepsilon)=1/k.}
\]

Consequently the ε↓0 limit is 1/k for this infinite family. These coefficients satisfy the retained nondegeneracy condition: every nonempty subsum is a nonzero multiple of c. Finitely many primes dividing c or at most k do not affect the limsup.

#### 2.1 Lower bound with bounded independence number

For p>k with p∤c let m=floor((p−1)/k) and A={1,…,m}⊂F_p. Any sum of k elements, even with repetition, lies between k and km≤p−1. Hence A is L-free.

Let I be an independent set of Cay_p(A). If |I|≥2, list its elements in circular order around F_p. Every consecutive cyclic gap is at least m+1, since differences 1,…,m give edges. Thus

\[
|I|\le\left\lfloor\frac{p}{m+1}\right\rfloor\le k-1.
\]

The last inequality follows from p<k(m+1): equality could occur only if k divided p, which is impossible for a prime p>k. Singleton independent sets satisfy the same bound. Therefore α≤k−1≤εp for all sufficiently large p. Since |A|/p→1/k, the lower bound follows.

#### 2.2 Upper bound from restricted sums

Here the independence-number restriction is not needed. Let A have m elements and contain no k pairwise distinct elements summing to zero. The case m<k is harmless. Suppose, for a contradiction, that

\[
k(m-k)\ge p-1.
\]

Put D_0=k(k−1)/2 and write p−1=kq+r with 0≤r<k. Choose

\[
t_i=(i-1)+q+\mathbf 1_{i>k-r},\qquad 1\le i\le k.
\]

These are distinct integers in [0,m−1], and Σt_i=p−1+D_0. The upper endpoint is valid because m−k≥ceil((p−1)/k). Consider the polynomial over F_p

\[
P(X_1,\ldots,X_k)=
\bigl((X_1+\cdots+X_k)^{p-1}-1\bigr)
\prod_{i<j}(X_j-X_i).
\]

It vanishes on A^k: repeated coordinates make the Vandermonde factor zero, and pairwise distinct coordinates have nonzero sum, making the first factor zero by Fermat's theorem.

On the other hand, the coefficient of X_1^(t_1)⋯X_k^(t_k), whose total degree equals deg P, is

\[
\frac{(p-1)!}{\prod_i t_i!}
\prod_{i<j}(t_j-t_i),
\]

up to the irrelevant sign from the orientation of the Vandermonde. To derive it, expand the Vandermonde as det(X_i^(j−1)). After the multinomial expansion, the determinant of the falling factorials (t_i)_(j−1) remains. These are monic polynomials of respective degrees 0,…,k−1, so their determinant is the ordinary Vandermonde in the t_i. A falling factorial with j−1>t_i is zero, matching the missing multinomial term. Every t_i<p and every nonzero difference t_j−t_i has magnitude less than p; thus this coefficient is nonzero in F_p.

**Interpolation dependency lemma.** If a polynomial P has total degree at most Σt_i and vanishes on ∏A_i with |A_i|=t_i+1, then its coefficient at ∏X_i^(t_i) is zero. Indeed, apply in coordinate i the functional

\[
\ell_i(f)=\sum_{a\in A_i}
\frac{f(a)}{\prod_{b\in A_i\setminus\{a\}}(a-b)}.
\]

Lagrange interpolation shows ℓ_i(X_i^j)=0 for j<t_i and 1 for j=t_i. In the tensor product, every monomial of total degree at most Σt_i except the target has some exponent below its t_i and is killed. The resulting coefficient functional is zero when P vanishes on the grid. Notice that a bound on each individual degree is unnecessary.

Choose A_i⊂A of size t_i+1. The lemma contradicts the nonzero coefficient. Therefore k(m−k)≤p−2, and

\[
|A|\le\frac{p+k^2-2}{k}.
\]

After division by p this gives the upper limit 1/k, completing the proof.

#### 2.3 What transfers, and what remains

The conclusion determines the entire ε-profile for this equal-coefficient family. It does not determine the value for arbitrary nondegenerate coefficient tuples. In general ε↦d(L,ε) is nondecreasing and bounded; therefore its right limit at zero exists as its infimum. The difficult part of the retained question is the value.

The source question is in Bucić–Christoph–Kim–Lee–Sivashankar, [arXiv:2507.22831v1, Problem 5.2](https://arxiv.org/html/2507.22831v1), with the handoff's retained journal scope controlling the definition. This report does not import other preprint conjectures as current results.

**Changed assumptions:** c_1=⋯=c_k=c≠0 for the exact value. **Evidence:** written argument; primary-source comparison. **Retained-question status:** partial. No formal theorem was compiled.

### 3. A precise additive/multiplicative character transfer, and its limitation

**Programme B2; relevant targets Q2187–Q2191.** The exact retained statements and stable IDs are in the Paley part and the consolidated ledger. This is an auxiliary theorem, not a solution of an asymptotic Paley question.

#### 3.1 Removing the common constant component

Let p be prime and give C^(F_p) the inner product Σ_x f(x)overline(g(x)). The mean-zero subspace

\[
H_0=\{f:\mathbb F_p\to\mathbb C:\sum_x f(x)=0\}
\]

has dimension p−1. It has the additive-character orthonormal basis

\[
e_a(x)=p^{-1/2}\exp(2\pi i ax/p),\qquad a\in\mathbb F_p^*.
\]

Extend every nontrivial multiplicative character χ of F_p* to zero at 0. A second orthonormal basis of the same space is

\[
v=\frac{p\delta_0-\mathbf1}{\sqrt{p(p-1)}},
\qquad m_\chi=\frac{\chi}{\sqrt{p-1}}
\quad(\chi\ne1).
\]

The vector v is essential: deleting the multiplicative trivial character leaves only p−2 vectors. The displayed extra vector completes the correct dimension. All vectors are mean-zero; multiplicative character orthogonality and Σχ=0 prove orthonormality.

**Theorem B2-R3.** Every overlap between these two bases has magnitude 1/sqrt(p−1). Consequently, if a nonzero f∈H_0 has r nonzero additive coordinates and s nonzero coordinates in the completed multiplicative basis, then

\[
\boxed{rs\ge p-1.}
\]

For v, the overlap is immediate. For m_χ it follows from the Gauss-sum identity |G(χ)|=sqrt(p). Here is the needed proof. For a nontrivial χ and a nontrivial additive character ψ, let G=Σ_(x≠0)χ(x)ψ(x). Substitute x=ty into its squared modulus:

\[
|G|^2=\sum_{t\ne0}\chi(t)
\sum_{y\ne0}\psi((t-1)y)
=(p-1)-\sum_{t\ne1}\chi(t)=p.
\]

All nonzero additive frequencies merely multiply G by a character phase. Dividing by sqrt(p(p−1)) proves the common overlap magnitude. This classical Gauss-sum dependency is also stated and proved in Keith Conrad, [Gauss and Jacobi sums, Theorem 2.2](https://kconrad.math.uconn.edu/blurbs/gradnumthy/Gauss-Jacobi-sums.pdf).

If a transition matrix has all entries of magnitude (p−1)^(−1/2), Cauchy–Schwarz bounds each additive coefficient by sqrt(s/(p−1))‖f‖_2. Summing over its r nonzero coefficients proves the support inequality.

There is also a robust version. For unit f, suppose projections onto r additive coordinates and s completed multiplicative coordinates leave errors at most ε and η respectively. The norm of the corresponding r×s transition submatrix is at most sqrt(rs/(p−1)), while

\[
\|P_rQ_sf\|\ge\|P_rf\|-\|f-Q_sf\|
\ge\sqrt{1-\varepsilon^2}-\eta.
\]

Thus

\[
rs\ge(p-1)\bigl(\sqrt{1-\varepsilon^2}-\eta\bigr)_+^2.
\]

This uses a genuinely different pair of bases on a common, correctly normalized space; it does not equate the additive group of order p with the multiplicative group of order p−1.

#### 3.2 Exact support is vacuous for nontrivial indicators

The transfer has a severe limitation for the desired combinatorial applications. If f:F_p→Q is not constant, then **every nonzero additive Fourier coefficient is nonzero**. Indeed, a vanishing coefficient would give

\[
\sum_{x=0}^{p-1} f(x)\zeta^{ax}=0,
\]

where a≠0 and ζ is a primitive pth root of unity. After permuting coefficients by multiplication by a, this is a rational polynomial of degree at most p−1 vanishing at ζ. The minimal polynomial is Φ_p(X)=1+X+⋯+X^(p−1), so all coefficients are equal, contrary to the hypothesis.

For any nonempty proper set A⊂F_p, the centered indicator 1_A−|A|/p is rational, mean-zero, and nonconstant. Its additive support therefore has size r=p−1. The exact support inequality gives only s≥1. To constrain such sets, one needs approximate concentration, higher correlations, or additional combinatorial constraints. Flat change-of-basis entries alone do not yield a small Paley clique bound.

The same basis construction works over every finite field F_q with q replacing p. In square-order fields, the subfield F_s⊂F_(s²) is a Paley clique of size s: every nonzero subfield element is a square in the larger field. Thus flat character overlaps are compatible with a sqrt(q)-sized clique. Any prime-field improvement must use information beyond this flatness.

The Paley part supplies a second, sharper nontransfer certificate: global degree-two theta remains exactly sqrt(p), even after entrywise nonnegativity. It also supplies a valid positive transfer, SOS_4(G_p)≤1+τ(L_p), which identifies a relaxation that could support a stronger result.

**Evidence:** written argument, with a classical primary-source dependency. **Auxiliary-theorem status:** proved. **Retained asymptotic targets:** partial, not closed.

### 4. Q49: squarefree-kernel reduction and a bounded exact search

**Programme B2; Q49; stable statement ID `d0a8503718ca529daf5a`.**

**Exact retained statement:** Set F(n)=n(n−1)(n+2). Are there only finitely many integer triples n_(1),n_(2),n_(3)≥2 satisfying [F(n_(1))+F(n_(2))−F(n_(3))]^(2)=4F(n_(1))F(n_(2))?

Expanding the squared equation shows it is symmetric in its three F-values. Since F is positive and strictly increasing on integers at least two, sort the indices as 2≤a≤b<c. The equation is then exactly

\[
\sqrt{F(a)}+\sqrt{F(b)}=\sqrt{F(c)}.
\]

The squared product F(a)F(b) is a square, so F(a)=du² and F(b)=dv² for one squarefree d>0 and positive integers u,v. The equation forces F(c)=d(u+v)². Conversely these identities imply the original equation, and all permutations recover the unsorted solutions.

This is the common-squarefree-kernel reduction already used in Shao, [arXiv:2301.00115v2, Proposition 2.3](https://arxiv.org/pdf/2301.00115). It is not claimed as a new reduction. The following elementary inequalities additionally make every bounded-minimum search effective:

\[
\boxed{b<\frac49F(a),\qquad c<a+b.}
\]

Write λ(t)=sqrt(F(t)). For t≥2,

\[
(F'(t))^2-9tF(t)=3t^3+10t^2-8t+4>0,
\]

so λ′(t)>(3/2)sqrt(t). Therefore

\[
\lambda(a)=\lambda(c)-\lambda(b)
>\tfrac32(c-b)\sqrt b\ge\tfrac32\sqrt b,
\]

proving the bound on b. Also λ(t)/t=sqrt(t+1−2/t) is strictly increasing, so λ(a+b)>λ(a)+λ(b)=λ(c), proving the bound on c. The source's Runge-based O(a²) bound is stronger than the displayed elementary O(a³) bound; no improvement on that source theorem is claimed.

#### Exact finite certificate

The deterministic script `research/root/q49_search.py` factors all F(n) for 2≤n≤1,000,000, groups them by squarefree kernel, and tests u+v=w inside each group, allowing a=b. It verifies every reported triple directly in the original integer equation. There are 999955 distinct kernel groups, largest group size five, and 135 candidate pairs in nonsingleton groups. The only sorted solutions in this box are

| (a,b,c) | d | (u,v,u+v) | (F(a),F(b),F(c)) |
|---|---:|---|---|
| (5,5,8) | 35 | (2,2,4) | (140,140,560) |
| (10,10,16) | 30 | (6,6,12) | (1080,1080,4320) |

The search ran in approximately 2.27 seconds. The source already proves there are no other resonances with minimum index at most 10^4, with no box bound on the other two indices. A box with **all** indices at most 10^6 does not contain that entire published domain. It supplies independent bounded verification and a different finite region, not a replacement for the source's unbounded-in-the-other-indices result.

**Changed assumptions:** all three indices at most 10^6 for the computed exhaustion; bounded minimum for the elementary effective inequalities. **Evidence:** written argument, primary-source comparison, exact finite computation. **Retained-question status:** partial. The possibility of resonances with unbounded minimum index remains unresolved.

### 5. Provisional Q2468: distinguish two different graph obstructions

**Programme B2; provisional Q2468; stable statement ID `3529c68ac8a3205e8a47`.**

**Exact retained statement:** What is the exact value of δχ?

The handoff defines δχ using Schur-free A⊆F_p and a uniform upper bound on χ(Cay_p(A)) once |A|≥dp. The source [Liu–Wu–Yang–Zhang, arXiv:2603.05490v1](https://arxiv.org/html/2603.05490v1), Theorem 1.4 and Problem 6.1, supplies a qualitative classification and explicitly retains the exact Schur value as a problem. No new value is obtained here.

The parameter α(Cay_p(A))≤εp in provisional Q2462, stable ID `ab65e680b82754944885`, is stronger information of a different kind than χ(Cay_p(A)) being unbounded. The inequality χ≥p/α converts small independence number into large chromatic number, but large chromatic number alone does not give a comparably small independence number. Thus the Ramsey–Turán density and chromatic threshold cannot simply be substituted for one another.

Fixed integer coefficients c_i act by iterated addition. Both the linear equation and its Cayley graph can be formulated on an abelian group without a separate multiplicative group structure. This observation does not diminish the finite-field results; it specifies that they do not themselves establish a two-operation inverse theorem.

**Evidence:** primary-source comparison and elementary logical comparison. **Retained-question status:** unresolved. The exact threshold is not computed or disproved.


## Part B. Paley structures: exact transfers and certificates

Date: 7 October 2026. Targets: Q2187–Q2191. This report supplies written proofs and exact finite certificates. It does not close any of the five asymptotic retained questions. The elementary results below are not claimed to be novel.

### 1. Exact targets and status

|Q|Stable statement ID|Exact retained statement|Result at retained scope|
|---|---|---|---|
|Q2187|`6a0c75d8af9af7e1c137`|Do absolute C,K>0 satisfy ω(G_p)≤C(log p)^K for every prime p≡1 mod 4?|Unresolved; exact clique numbers for every eligible p≤300; exact obstruction to the global degree-two relaxation.|
|Q2188|`277f454289360bbd69ef`|Does some ε>0 satisfy SOS₄(G_p)=O(p^{1/2−ε}) as p→∞ through primes p≡1 mod 4?|Unresolved; a proved transfer from one-local ordinary theta bounds to degree-four SOS, with certified finite upper bounds.|
|Q2189|`b7cebb91447185f8bc65`|Are there infinitely many such p with 1+τ₊(H_p)<⌊(1+√(2p−1))/2⌋?|Unresolved; the strict inequality is certified exactly for p=61,281, and certified false for the other 27 eligible primes p≤300.|
|Q2190|`858e236a2a78c67c9b1f`|Does there exist ε>0 such that θ(H_p)≤(1/√2−ε)√p for all sufficiently large primes p≡1 mod 4?|Unresolved; rational positive-semidefinite dual certificates for all eligible p≤300.|
|Q2191|`68bd7a5a8c3e1ff55f95`|Do absolute C,α>0 and 0<δ<√2−1 exist such that (1−δ)‖x‖₂²≤‖Φ_px‖₂²≤(1+δ)‖x‖₂² for every x supported on at most Cp/(log p)^α coordinates and all sufficiently large such p?|Unresolved; a sharp characterization of coherence saturation, a quantitative first gap, and a source-scope correction.|

The two graphs both called H_p in the handoff are different. Here L_p denotes the one-local graph induced on nonzero quadratic residues; T_p denotes the graph induced on `{x: χ(x)=χ(x−1)=1}`. The Q2190 graph H_p, defined using common nonneighbors of `{0,g}` for a primitive root g, is isomorphic to the complement of T_p by x↦gx. Thus τ₊ in Q2189 is a clique relaxation of L_p, whereas θ in Q2190 is the ordinary independence relaxation of the complement of T_p. These conventions matter for every bound below.

### 2. An exact obstruction: the global degree-two relaxation stops at √p

Let p≡1 mod4 be prime, χ(0)=0, and χ the quadratic character on F_p. Put

\[
Q_{xy}=\chi(x-y),\qquad A=(J-I+Q)/2.
\]

Here A is the adjacency matrix of G_p. Let

\[
\tau(G_p)=\max\{\langle J,X\rangle:X\succeq0,\operatorname{Tr}X=1,
X_{xy}=0\text{ for distinct nonadjacent }x,y\}.
\]

Let τ₊ add entrywise nonnegativity. Then, for every such prime,

\[
\boxed{\tau(G_p)=\tau_+(G_p)=\mathrm{SOS}_2(G_p)=\sqrt p.}
\]

#### Dependency lemma: the character matrix

The character sums give Q1=0 and Q²=pI−J. The off-diagonal correlation is elementary: for x≠y, an affine change of variable reduces it to Σ_t χ(t(t−1))=−1. To see this last identity, count pairs (t,s) with s²=t(t−1). The substitution

\[
u=2t-1-2s,\quad v=2t-1+2s
\]

is a bijection to uv=1, giving p−1 pairs. Counting the same pairs as p+Σ_tχ(t(t−1)) proves the identity. The diagonal correlation is p−1. Consequently Q is zero on constants and has eigenvalues ±√p on their orthogonal complement. In particular

\[
Q\preceq\sqrt p(I-J/p).
\]

#### Upper certificate

For any feasible X, let t=〈J,X〉. The diagonal of Q is zero, its entries are +1 on edges, and the nonedge entries of X vanish. Hence 〈Q,X〉=t−1. Taking the inner product of the preceding matrix inequality with X≽0 gives

\[
t-1\le\sqrt p(1-t/p),
\]

which rearranges to t≤√p. This proof permits arbitrary signs in X.

#### Matching primal certificate

Set

\[
X_*={1\over p}\left(I+{2A\over1+\sqrt p}\right).
\]

It has trace one, the prescribed nonedge zeros, and nonnegative entries. Since A has eigenvalue (p−1)/2 on constants and eigenvalues (−1±√p)/2 off constants, X_* is positive semidefinite. Its objective is

\[
1+{p-1\over1+\sqrt p}=\sqrt p.
\]

Thus even entrywise nonnegativity cannot improve the global theta bound.

For completeness, the degree-two pseudoexpectation has means y=p^{−1/2}1 and second moments B=√p X_*. Its moment matrix is `[[1,yᵀ],[y,B]]`; the Schur complement B−yyᵀ is positive semidefinite by the same eigenvalue calculation. Its diagonal equals y and its nonedge entries vanish, so it is feasible for SOS₂. Conversely, if B and y come from a feasible degree-two pseudoexpectation and t=Σy_i>0, then B/t is theta-feasible and 〈J,B〉≥t², proving t≤τ. The t=0 case is immediate.

This is an exact model obstruction, not a lower bound on the actual clique number. The adjacency definition and the character-matrix identity genuinely combine additive differences with multiplicative quadratic characters. Better overlap or uncertainty statements do not alter the exhibited feasible point. A successful upper-bound method must add constraints that exclude it.

### 3. A justified transfer to Q2188: one localization bounds SOS₄

Write τ(L_p)=θ(complement(L_p)), without Schrijver nonnegativity. Then

\[
\boxed{\mathrm{SOS}_4(G_p)\le1+\tau(L_p).}
\]

This statement holds more generally for any finite vertex-transitive graph G, with its neighborhood graph in place of L_p.

Let L be a feasible degree-four pseudoexpectation and S=Σ_j x_j. Put a_i=L(x_i), t=L(S). Positivity and Boolean reduction imply a_i=L(x_i²)≥0. For a_i>0, define a conditional degree-two functional on the neighbors of i by

\[
L_i(f)=L(x_i f)/a_i.
\]

For every linear q,

\[
L_i(q^2)=L((x_iq)^2)/a_i\ge0,
\]

because L vanishes on `(x_i²−x_i)q²`, a polynomial of degree at most four. The other degree-two Boolean and nonedge constraints descend in the same way. Therefore L_i is a degree-two feasible pseudoexpectation for the neighborhood graph.

To bound its objective without invoking any equivalence theorem, let b be its vector of means, B its second-moment matrix, and σ=Σb_j=TrB. If σ>0, then B/σ is theta-feasible. Positivity applied to the sum of its variables gives 〈J,B〉≥σ², so σ≤τ(L_p). If σ=0, the conclusion is automatic.

The anchor has conditional value one, and nonneighbors have conditional value zero. It follows that

\[
L(x_iS)\le a_i(1+\tau(L_p)).
\]

If a_i=0, Cauchy–Schwarz for L gives L(x_iS)=0, so the inequality still holds. Sum over i and use L((S−t)²)≥0:

\[
t^2\le L(S^2)=\sum_iL(x_iS)
\le(1+\tau(L_p))t.
\]

This proves the assertion.

The nonnegative one-local relaxation τ₊(L_p) is not substituted in this argument. Conditional third moments need not be nonnegative under degree-four positivity. Likewise, the two-local theta certificates below are not asserted to be degree-four SOS certificates. The separate ordinary-theta certificates are included specifically to make the displayed SOS₄ transfer valid.

#### Why one localization becomes a Fourier linear program

Let g generate F_p*, n=(p−1)/2, and label the vertices of L_p by g^{2j}, j∈Z_n. Its adjacency rule is translation-invariant in j, because multiplying an additive difference by a square preserves χ. Averaging any feasible matrix over these cyclic shifts preserves feasibility and objective, so the optimum is attained by a real symmetric circulant matrix. Such a matrix is positive semidefinite exactly when every discrete Fourier eigenvalue is nonnegative.

There are two explicit certificate forms used in the archive. If f(0)=1, f is symmetric, f vanishes on nonedges, and all its Fourier coefficients are nonnegative, then `circ(f)/n` is an ordinary-theta feasible point of value Σf(j). For τ₊ one additionally requires f≥0. If d is symmetric, all its Fourier coefficients are nonnegative, and d(j)=−1 on edges, then `circ(d)` certifies τ(L_p)≤1+d(0). The same certificate works for τ₊ with the weaker inequalities d(j)≤−1 on edges. Indeed, for every feasible X, positivity gives 0≤〈circ(d),X〉≤1+d(0)−〈J,X〉.

### 4. A sharp coherence threshold for the Paley frame

Let δ_k be the least restricted-isometry constant for all supports of size at most k, with Φ_p exactly as defined in the handoff. For every prime p≡1 mod4 and every integer 1≤k≤p+1,

\[
\boxed{\delta_k=(k-1)/\sqrt p
\quad\Longleftrightarrow\quad k\le\omega(G_p)+1.}
\]

Moreover, whenever k≥ω(G_p)+2,

\[
\boxed{\delta_k\le
\min\left\{1,{k-4+\sqrt{k^2+4k-12}\over2\sqrt p}\right\}
<{k-1\over\sqrt p}.}
\]

The forward construction is the Paley specialization of Bandeira–Fickus–Mixon–Wong, Theorem 20. The converse and quantitative gap are proved here to specify exactly where the coherence argument ceases to be sharp; no priority claim is made.

#### Gram matrix and the easy direction

The standard quadratic Gauss-sum identity gives

\[
\Phi_p^*\Phi_p=I+p^{-1/2}\mathcal S,
\]

where S has zero diagonal, S_xy=χ(x−y) for x,y∈F_p, and S_{∞x}=S_{x∞}=1. Every off-diagonal entry has absolute value one. The elementary row-sum norm bound therefore gives δ_k≤(k−1)/√p. If C is a clique of size k−1, the principal matrix on C∪{∞} is J−I, which attains that norm. This proves equality through k=ω+1.

The bound δ_k≤1 follows independently from tightness: the displayed frame has Φ_pΦ_p*=2I by additive-character orthogonality. Hence its full Gram matrix has eigenvalues 0 and 2, so all principal Gram matrices have eigenvalues in [0,2].

#### Equality for a signed complete matrix

Let M be any real symmetric k×k matrix with zero diagonal and all other entries ±1. If ‖M‖=k−1, choose an eigenvector v for an eigenvalue σ(k−1), σ∈{±1}, and an index at which |v_i| is maximal. Equality in

\[
(k-1)|v_i|=\left|\sum_{j\ne i}M_{ij}v_j\right|
\le\sum_{j\ne i}|v_j|\le(k-1)|v_i|
\]

forces every |v_j| to equal |v_i|, and then all rowwise triangle inequalities force M_ij=σε_iε_j, where ε_i is the sign of v_i. Thus M is diagonally sign-conjugate to either J−I or −(J−I). Conversely, these two forms attain the norm k−1.

#### Inversion removes the switching ambiguity

For a∈F_p, define a permutation of the projective line by

\[
F_a(a)=\infty,\quad F_a(\infty)=0,\quad
F_a(x)=(x-a)^{-1}\quad(x\ne a,\infty).
\]

Set d_a=d_∞=1 and d_x=χ(x−a) otherwise. A direct calculation, including entries involving a and ∞, shows

\[
\mathcal S_{F_a(x),F_a(y)}=d_xd_y\mathcal S_{xy}.
\]

For finite x,y distinct from a, this follows from `F_a(x)−F_a(y)=(y−x)/((x−a)(y−a))` and χ(−1)=1. Thus inversion is a switching symmetry of the extended Paley sign matrix.

Suppose a k-subset attains the coherence norm. If it does not already contain ∞, apply an inversion taking one of its vertices to ∞. Its sign matrix is still sign-conjugate to σ(J−I). Since every entry in the infinity row is +1, the conjugating signs on the remaining vertices must all be equal. Their pairwise signs are therefore all σ. For σ=+1 they form a clique of size k−1; for σ=−1 they form an independent set of that size. Multiplication by any nonsquare interchanges cliques and independent sets in G_p, so both possibilities require k−1≤ω(G_p). This proves the converse.

#### A quantitative first gap

Assume k≥ω+2, so no k-submatrix is sign-conjugate to either constant-sign form. Let λ be an eigenvalue of a k-submatrix M, set σ=sign(λ), and conjugate σM by the signs of an associated eigenvector to obtain an eigenvector w≥0 with eigenvalue |λ|. The conjugated matrix has at least one negative off-diagonal edge. Replace every other negative edge by +1. Because w≥0, this replacement can only increase its quadratic form. Therefore

\[
|\lambda|\le\lambda_{\max}(M_k),
\]

where M_k has all off-diagonal entries +1 except one symmetric pair −1. On the two exceptional vertices and the other k−2 vertices, its quotient matrix is

\[
\begin{pmatrix}-1&k-2\\2&k-3\end{pmatrix}.
\]

The remaining eigenvalues are +1 and −1. For k≥4 its largest eigenvalue is `(k−4+sqrt(k²+4k−12))/2`. This is strictly below k−1 because `k²+4k−12=(k+2)²−16`. Dividing by √p and taking the maximum over supports proves the stated gap.

This gap is of order 1/(k√p) relative to the coherence upper bound. It describes a finite structural threshold but is much too weak at k comparable to p/(log p)^α. It supplies no solution to Q2191.

#### Source-scope correction for Q2191

The downloaded original arXiv:1202.1234v2, Conjecture 25, printed page 20, states the fixed-δ, near-linear-sparsity assertion retained in the handoff. Satake arXiv:2405.08608v2, Conjecture 29, printed page 8, presents a stronger quantitative profile for δ_K and attributes it to that conjecture. Satake's Theorem 18 instead assumes a polynomially decaying RIP constant p^{−τ}. Neither stronger hypothesis follows merely by replacing the retained statement with its wording. This is a scope mismatch, not a disproof of any implication by some additional argument.

One consequence directly justified from retained Q2191 is ω(G_p)≤δ√p for all sufficiently large p. Indeed, the elementary spectral bound ensures ω+1≤√p+1, eventually below Cp/(log p)^α, and the exact equality δω+1=ω/√p then applies. This improves the leading constant if Q2191 holds, but this argument gives no polynomial or polylogarithmic exponent improvement.

### 5. Exact finite experiment

#### Declared computation

The domain is all 29 primes p≤300 with p≡1 mod4. There is no random seed because the search and certificate generation are deterministic. The largest normalized two-local graph has 72 vertices. Maximum-clique search uses greedy independent-set colorings for branch-and-bound, and a separate certificate tree proves exclusion of the next clique size. Floating linear programming and smooth spectral minimization only propose rational certificates; no floating sign decision establishes any reported bound.

The one-local primal and dual certificates have denominator 10^9. Their Fourier eigenvalues are verified using exact rational cosine intervals. Those intervals are derived from Machin's identity for π, alternating arctangent sums, Taylor's theorem, and the Lipschitz bound for cosine. The resulting verification uses only integer arithmetic and Python's Fraction type.

For two-local theta, a candidate dual has the form `D=tI+Y−J`, where Y is supported on edges of H_p. The entries of t and Y have denominator 10^6. A lower-triangular rational factor R has denominator 10^8. The verifier checks, with integers, that `E=D−RRᵀ` is symmetric diagonally dominant with nonnegative diagonal. Such an E is positive semidefinite: each off-diagonal term contributes a nonnegative multiple of `(e_i±e_j)(e_i±e_j)ᵀ`, with nonnegative diagonal slack left over. Thus D≽0 exactly, and θ(H_p)≤t follows by weak duality.

Every feasible dual is useful even if numerical optimization has not converged to the optimum. The reported two-local numbers are certified upper bounds, not asserted optimal SDP values. The resource cap was four smooth optimization stages, at most 250 iterations per stage, for each finite graph. A complete generation took about seven seconds and verification about two seconds in this workspace; exact recorded timings and software versions are in the JSON outputs.

#### Results

All decimal entries in the following table are exact rational certificate bounds as printed, not rounded floating estimates. The SOS₄ column comes from the proved ordinary one-local transfer. The final column is a clique upper bound, not an SOS₄ upper bound.

|p|ω(G_p), exact|HP floor|1+τ₊(L_p), upper|SOS₄(G_p), upper|2+θ(H_p), upper|
|---:|---:|---:|---:|---:|---:|
|5|2|2|2.000020000|2.000020000|2.000000|
|13|3|3|3.000020000|3.000020000|3.001000|
|17|3|3|3.343165751|3.343165751|3.001000|
|29|4|4|4.317687207|4.317687207|4.001749|
|37|4|4|4.759905298|4.759905298|4.001942|
|41|5|5|5.472155955|5.472155955|5.001870|
|53|5|5|5.678290247|5.678290247|5.002402|
|61|5|6|5.888668557|5.900879819|5.119424|
|73|5|6|6.377212643|6.377212643|5.468387|
|89|5|7|7.060043967|7.155358309|5.804775|
|97|6|7|7.945153245|7.948278655|6.878530|
|101|5|7|7.289150921|7.290275997|5.929592|
|109|6|7|8.001799380|8.007014117|7.028225|
|113|7|8|8.330481542|8.330502189|7.189639|
|137|7|8|8.826160613|8.829045958|7.619533|
|149|7|9|9.188375905|9.188375905|7.605060|
|157|7|9|9.670495349|9.694896941|8.033569|
|173|8|9|10.233907752|10.316505769|8.617414|
|181|7|10|10.320738168|10.324107760|8.293455|
|193|7|10|10.437919339|10.505781408|8.330590|
|197|8|10|10.651714422|10.651714422|8.667043|
|229|9|11|11.620198883|11.658699631|9.697391|
|233|7|11|11.238223635|11.238223635|9.066342|
|241|7|11|11.441080511|11.595513060|9.179928|
|257|7|11|11.537270540|11.557777546|9.123805|
|269|8|12|12.304789700|12.306734826|9.782203|
|277|8|12|12.298772237|12.469257700|9.759899|
|281|7|12|11.891614776|11.902285080|9.390241|
|293|8|12|13.114505994|13.127043941|10.224079|

The comparator HP floor is `floor((1+sqrt(2p−1))/2)`. The independent spectral bound is √p for every row; it is retained at full precision in the CSV. Hanson–Petridis is used only as a cited comparator, not as an ingredient in the exact clique computation.

At p=61, the exact Schrijver enclosure is

\[
5.888609672\le1+\tau_+(L_{61})\le5.888668557<6.
\]

At p=281 it is

\[
11.891495862\le1+\tau_+(L_{281})\le11.891614776<12.
\]

For every other eligible p≤300, either an exact clique witness or the rational Schrijver primal certificate proves `1+τ₊≥HP floor`. Thus the classification as exactly two strict improvements on this declared range is certified in both directions. The two primes already occur in the 2019 source's numerical table; the present contribution is a locally reproducible exact verification, not a new family of improving primes.

The two-local certificates, after adding two and taking the floor, equal the exact clique number in 18 of the 29 cases. They strictly beat the HP integer bound in 21 cases. These are finite computations and imply no assertion about infinitely many primes or a uniform asymptotic constant.

Some explicit maximum cliques are

- p=61: `{0,1,42,57,58}`;
- p=229: `{0,1,57,71,135,154,203,215,218}`;
- p=281: `{0,1,156,163,219,272,277}`;
- p=293: `{0,1,225,229,235,268,278,284}`.

The verifier checks every pairwise difference by Euler's criterion. Upper certificates apply to every clique: any edge `{a,b}` can be mapped to `{0,1}` by `(x−a)/(b−a)`, whose scale factor is a square. The remainder lies in T_p. Hence `ω(G_p)=2+ω(T_p)`, including the p=5 empty-graph case.

#### Files and verification status

- `paley_experiment.py`: all generator, optimization, and search code; it ran successfully.
- `verify_paley.py`: independent standard-library-only verifier; it ran successfully.
- `certificates/p5.json` through `certificates/p293.json`: the complete witnesses, branching certificates, Fourier primal/dual rows, and rational SDP decompositions for the declared 29 primes.
- `results.csv`, `results.json`, `run.log`: raw generated bounds, software versions, search statistics, timing, and optimizer logs within each certificate.
- `verification.json`, `verification.log`: exact check outcomes, including rational lower bounds on Fourier eigenvalues and diagonal-dominance margins.
- `paley_statement_ledger.json`: exact retained-scope decisions and separate auxiliary theorem records.
- `source_notes.json`: source URLs, versions, locations, and scope findings.
- `source_1202.1234v2.pdf` and its text extraction: the primary text used for the Q2191 scope comparison.

No proof-assistant theorem was compiled. Exact arithmetic checks are executable certificates plus the written correctness arguments above; they are not a Lean kernel receipt.

### 6. Source comparison and residual targets

1. Kunisky and Yu, [A degree 4 sum-of-squares lower bound for the clique number of the Paley graph](https://arxiv.org/html/2211.02713v2), v2, 25 April 2024. Conjecture 1.1 is Q2187; Theorem 1.2 gives SOS₄≥cp^{1/3}; §6 motivates Q2188. Consequently any exponent improvement in Q2188 has ε≤1/6. This lower bound concerns the relaxation, not the clique number. Its proof was not independently audited here.
2. Magsino, Mixon, and Parshall, [Linear programming bounds for cliques in Paley graphs](https://arxiv.org/html/1907.05971v1), 12 July 2019. Propositions 2–4 give the circulant primal/dual formulations; Conjecture 6 is Q2189; Table 1 includes the numerical p=61,281 improvements reproduced here. The LP reduction and certificates used here also have the independent arguments in §3 and §5.
3. Kunisky, [Spectral pseudorandomness and the road to improved clique number bounds for Paley graphs](https://arxiv.org/html/2303.16475v1), 29 March 2023. Appendix A, Conjecture A.1, is Q2190. Theorem 1.19 explains why a conjectural two-local minimum-eigenvalue law alone yields leading constant √3/2, above the Hanson–Petridis constant; the full theta dual can be stronger. This report proves no uniform spectral-edge estimate.
4. Bandeira et al., [Randomstrasse101: Open Problems of 2025](https://arxiv.org/html/2603.29571v1), 31 March 2026. Entry 12 retains the polylogarithmic clique and polynomial SOS-improvement questions and discusses both localizations. This is a dated problem source, not a resolution or a proof of absence of later work.
5. Bandeira, Fickus, Mixon, and Wong, [The road to deterministic matrices with the restricted isometry property](https://arxiv.org/abs/1202.1234), arXiv v2, 23 February 2012; journal version 2013. Theorem 20 gives the initial coherence-saturation interval; Conjecture 25, printed p.20, is the fixed-δ question retained here.
6. Satake, [On the Paley RIP and Paley graph extractor](https://arxiv.org/pdf/2405.08608v2), v2, 15 May 2024. Definition 11 and Lemma 12 match the frame and its Gram matrix. Theorem 18, p.6, requires polynomial decay of the RIP constant. Conjecture 29, p.8, supplies a stronger quantitative profile; it must be distinguished from the retained fixed-δ statement.
7. Hanson and Petridis, [Refined estimates concerning sumsets contained in the roots of unity](https://arxiv.org/abs/1905.09134), source of the comparator `ω≤(1+sqrt(2p−1))/2` cited in items 1–3. This proof was not rederived for the experiment.

The remaining mathematical obstacles are specific. Q2187 needs constraints or character-sum cancellation beyond the exact global degree-two feasible point. Q2188 needs a uniform upper analysis improving the exponent, and finite local bounds supply no such rate. Q2189 needs a constructible infinite family of strict dual certificates or another infinitude argument. Q2190 needs a dual construction with a controlled leading constant across all sufficiently large primes. Q2191 needs uniform sparse spectral control far beyond the first coherence-saturation gap; the fixed-δ hypothesis must not be silently replaced with a stronger decay profile.


## Part C. Squarefree values, near-squares, and algebra

Date: 2026-10-07. These are research notes for consolidation, not an update to the authoritative catalog. No exact universal question in this lane is claimed closed. All proofs below are written arguments; no Lean theorem was compiled. Claims imported from family 020 remain conditional on that imported theorem being valid.

### 1. Q1509: exact transfer from irreducible factors

Stable ID `ffda628de2bac43d0ec3`. Retained statement: for every separable integer polynomial of degree at least four with no fixed prime-square divisor, its squarefree values have density equal to the product of local densities.

**Proposition 1 (finite-product transfer).** Let

\[
f=c\prod_{i=1}^r g_i\in\mathbb Z[x],\qquad c\ne0,
\]

where the nonconstant separable polynomials \(g_i\) are pairwise coprime over \(\mathbb Q\). Suppose no prime square divides every value of \(f\). For every \(i\), assume

\[
S_{g_i}(X):=\#\{1\le n\le X:g_i(n)\text{ is squarefree}\}
=C_{g_i}X+o(X),
\quad C_g=\prod_p\left(1-\frac{\rho_g(p^2)}{p^2}\right).
\]

Then \(S_f(X)=C_fX+o(X)\), and \(C_f>0\).

**Proof.** Include in a finite set \(B\) every prime dividing \(c\) or any nonzero resultant \(\operatorname{Res}(g_i,g_j)\). The Bézout identity for a resultant shows that, outside \(B\), a prime cannot divide two distinct values \(g_i(n),g_j(n)\). Consequently, outside \(B\), if \(p^2\mid f(n)\), then \(p^2\mid g_i(n)\) for some \(i\).

For fixed \(Y\), write \(T_h(X,Y)\) for the number of \(1\le n\le X\) with \(p^2\nmid h(n)\) for every prime \(p\le Y\), and write

\[
C_h(Y)=\prod_{p\le Y}\left(1-\frac{\rho_h(p^2)}{p^2}\right).
\]

The Chinese remainder theorem gives \(T_h(X,Y)=C_h(Y)X+O_{h,Y}(1)\). All the Euler products converge: outside finitely many primes the polynomial has at most its degree many simple roots modulo \(p\), each lifting uniquely modulo \(p^2\). Thus \(\rho_h(p^2)=O_h(1)\) there. The local hypothesis for \(f\) makes each factor positive, so its product is positive. It also implies local admissibility for each \(g_i\).

Take \(Y\) larger than all primes of \(B\). Every integer counted by \(T_f(X,Y)\) but not by \(S_f(X)\) is counted by at least one of

\[
T_{g_i}(X,Y)-S_{g_i}(X).
\]

Indeed, its offending square divisor has prime larger than \(Y\); the resultant observation assigns it to one factor, and passing the small-prime sieve for \(f\) implies passing that sieve for every factor. Hence

\[
T_f(X,Y)-\sum_i\bigl(T_{g_i}(X,Y)-S_{g_i}(X)\bigr)
\le S_f(X)\le T_f(X,Y).
\]

Divide by \(X\), let \(X\to\infty\), then \(Y\to\infty\). Both limiting bounds become \(C_f\). This proves the proposition. Zeros cause no difficulty: once \(Y\ge2\), zero values fail the small-prime sieve.

**Why the precise argument matters.** An individual Euler-product asymptotic directly controls the number that pass its small-prime sieve but fail to be squarefree. It does not, by itself, give a bound for *every* integer with any large square divisor. The proof uses precisely the former count, so an unproved stronger tail estimate is unnecessary. Neither independence of factor values nor an asymptotic uniform over arithmetic progressions is assumed.

**Consequence for the packet.** Classical squarefree asymptotics through irreducible degree three, together with Proposition 1, cover separable polynomials whose irreducible factors all have degree at most three, however large their total degree. Every reducible separable quartic is already in this class. If family 020's irreducible quartic theorem is accepted, the factor-degree cutoff improves from three to four, again with no bound on total degree. Polynomials containing an irreducible factor of degree at least five remain outside this consequence. The higher-degree \((d-2)\)-free conclusion in family 020 does not imply squarefreeness.

Booker–Browning's primary paper, *Square-free values of reducible polynomials*, arXiv:1511.00601v3, Theorem 1.2, p. 4, explicitly states the asymptotic for factor degrees at most three. Its introduction uses a no-fixed-prime-divisor convention. The following elementary normalization removes that stronger condition and justifies using the theorem here.

**Fixed-prime removal lemma.** Let \(B\) be the finite set of primes dividing every value of a nonzero polynomial \(f\), and put \(M=\prod_{p\in B}p\), with \(M=1\) if \(B\) is empty. Finiteness follows by evaluating at any fixed argument having nonzero value. Assume no prime square divides every value. Partition the arguments into classes \(a\pmod{M^2}\). Discard a class if \(p^2\mid f(a)\) for some \(p\in B\). In every remaining class define

\[
h_a(t)=\frac{f(a+M^2t)}{M}\in\mathbb Z[t].
\]

For \(p\in B\), the constant coefficient is nonzero modulo \(p\), while every nonconstant coefficient is divisible by \(p\). Thus \(p\nmid h_a(t)\) for all \(t\). For \(q\notin B\), multiplication by \(M\) and the affine change of argument are invertible modulo \(q\), so \(q\) is not a fixed divisor of \(h_a\). Therefore \(h_a\) has no fixed prime divisor; separability and irreducible-factor degrees are preserved. Since \(M\) is squarefree and coprime to every value of \(h_a\), squarefreeness of \(f(a+M^2t)\) is equivalent to squarefreeness of \(h_a(t)\).

For \(q\notin B\), root counts modulo \(q^2\) are unchanged; for \(p\in B\), \(h_a\) has no roots even modulo \(p\). Hence the density constant of every retained \(h_a\) is \(\prod_{q\notin B}(1-\rho_f(q^2)/q^2)\). The retained residue classes have density \(\prod_{p\in B}(1-\rho_f(p^2)/p^2)\). Summing their asymptotics recovers exactly \(C_f\). This proves that the cited no-fixed-prime theorem supplies the packet's weaker local hypothesis without a gap.

An entirely self-contained unconditional subcase of Proposition 1 is obtained with linear factors: for \(an+b\), primes with a square divisor are at most \(O(\sqrt X)\), and away from fixed coefficient primes each contributes at most \(X/p^2+1\). This gives a large-prime tail \(O(X/Y)+O(\sqrt X)\) and hence the asymptotic.

#### Family 020 evidence audit

The exact pinned scope document was opened. It declares irreducibility over \(\mathbb Q\), degree \(d\ge4\), exponent \(k=d-2\), the local \(k\)-power condition, and an Euler-product asymptotic. The linked comparator was also opened. Its theorem `OAI.QuarticPowerFree.allDegrees` ends with `by sorry`. This is a comparator statement stub, not evidence of a completed proof. That observation does not inspect or disprove a separate proof elsewhere in the repository. The underlying PDF could not be retrieved as text through the attempted raw URL. No build, axiom audit, or independent proof audit of the manuscript was performed.

Sources:

- https://arxiv.org/pdf/1511.00601 — Theorem 1.2; v3, 18 January 2017.
- https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/020.md
- https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/PowerFreeValues.lean

### 2. Q1510: prime-argument transfer and exact obstruction example

Stable ID `88eed316b86c7cab6b69`. Retained statement: for every separable integer polynomial of degree at least four with prime local constant \(c_f>0\), \(N_f(X)\sim c_fX/\log X\).

Proposition 1 has an exact prime-argument analogue: if each factor has its correct prime-argument squarefree asymptotic, then their product does too. Replace the integer CRT count by the prime number theorem in each fixed reduced residue class modulo \(\prod_{p\le Y}p^2\), and normalize by \(\pi(X)\). The finitely many input primes dividing this modulus contribute \(O_Y(1)\). The same resultant inclusion and two limiting operations prove the result, with

\[
c_h(Y)=\prod_{p\le Y}\left(1-\frac{r_h(p^2)}{p(p-1)}\right).
\]

This covers any total degree when all irreducible factors belong to a known prime-argument class. Pasten's source states that degrees at most three are known, and its Theorem 1.1 gives the general assertion under number-field abc for the root fields. Its integer-argument counterpart does not supply the missing prime-argument input: an \(o(X)\) exceptional set can contain every prime, because \(\pi(X)=o(X)\).

**Exact nontransfer example.** Let \(f(x)=x(x+1)(x^2+1)\). This separable quartic has no fixed square divisor, since \(f(2)=30\) is squarefree. Nevertheless every odd prime argument produces a multiple of four: both \(p+1\) and \(p^2+1\) are even. Thus the only squarefree prime argument is \(p=2\). Its prime local factor at two is zero. Its integer local factor at two is \(1/4\), since precisely the residue \(2\pmod4\) survives. For odd primes,

\[
\rho_f(p^2)=\begin{cases}4,&p\equiv1\pmod4,\\2,&p\equiv3\pmod4.\end{cases}
\]

The roots from the three factors are distinct away from two. This example proves that integer local admissibility cannot replace prime local admissibility. It is not a counterexample to Q1510, whose hypothesis explicitly excludes it.

Source: https://people.math.harvard.edu/~hpasten/preprints/SqfPrimIJNT.pdf — introduction and Theorem 1.1, pp. 1–2; manuscript date 3 August 2014.

### 3. Q2215: a quantitative necessary error rate

Stable ID `235fbd589621177ad36d`. Let \(Q\) be the positive squares and suppose the retained hypotheses hold: \(R=A+B\), both summands have at least two positive integers, and \(|(R\triangle Q)\cap[1,X]|=o(\sqrt X)\). Put \(E(X)=|(R\setminus Q)\cap[1,X]|\).

**Proposition 2 (necessary error exponent at least one third).** Both summands must be infinite, \(A(X),B(X)=o(\sqrt X)\), and for every \(\eta>0\) there is a positive constant \(c_\eta\) such that

\[
E(X)\ge c_\eta X^{1/3-\eta}
\]

for all sufficiently large \(X\). Consequently, the asserted irreducibility is proved whenever the perturbation is \(O(X^{1/3-\delta})\) for some fixed \(\delta>0\). An elementary intermediate estimate is

\[
\liminf_{X\to\infty}\frac{E(X)}{X^{1/4}}\ge1,
\]

which the proof first establishes before improving the exponent by counting square-sum graph edges.

**Proof.** Fix distinct \(a_1,\ldots,a_k\in A\), with \(k\ge2\). For each pair \(i\ne j\), the equation \(u^2-v^2=a_i-a_j\) has only finitely many integer solutions, because \((u-v)(u+v)\) is a fixed nonzero integer. Consequently, for all sufficiently large \(b\), at most one of \(a_i+b\), \(1\le i\le k\), is a square. Each such \(b\in B\cap[1,X]\) therefore produces at least \(k-1\) nonsquare pairs \((i,b)\). Any value is represented by at most \(k\) such pairs, giving

\[
(k-1)B(X)\le kE(X+\max_i a_i)+O_k(1)=kE(X)+O_{A,k}(1).
\]

The final equality follows because an interval of fixed length contains only boundedly many integers. Using \(k=2\) proves \(B(X)=o(\sqrt X)\), and the symmetric argument proves the same for \(A\). If either summand were finite, \(R(X)\le A(X)B(X)\) would contradict \(R(X)\sim\sqrt X\). Both are therefore infinite, so arbitrary fixed \(k\) is permitted in both estimates. Since

\[
\sqrt X(1+o(1))=R(X)\le A(X)B(X)
\le\left(\frac{k}{k-1}E(X)+O_k(1)\right)^2,
\]

the lower limit in the claim is at least \((k-1)/k\). Let \(k\to\infty\).

For the stronger exponent, form a bipartite graph with vertex sets \(A\cap[1,X]\) and \(B\cap[1,X]\), putting an edge at \((a,b)\) if \(a+b\le X\) is square. Write its vertex counts as \(a_X,b_X\) and its edge count as \(m_X\). Every represented square at most \(X\) supplies an edge, so \(m_X\ge(1-o(1))\sqrt X\). Two distinct vertices \(a,a'\) on the first side have at most

\[
D(X)=\max_{1\le d\le X}\tau(d)
\]

common neighbors: each neighbor gives a solution \(u^2-v^2=|a-a'|\), and hence a factor pair of that positive integer. Let \(d_b\) be the degree of \(b\). Double-counting pairs of neighbors, followed by Cauchy–Schwarz, gives

\[
\sum_b\binom{d_b}{2}\le D(X)\binom{a_X}{2},
\qquad
\frac{m_X^2}{b_X}-m_X\le D(X)a_X^2.
\]

Thus \(m_X\le b_X+\sqrt{D(X)}a_X\sqrt{b_X}\). The already proved two-shift bounds imply \(a_X,b_X\le2E(X)+O(1)\), and \(E(X)\to\infty\). Hence

\[
\sqrt X\ll E(X)+\sqrt{D(X)}E(X)^{3/2},
\qquad E(X)\gg X^{1/3}D(X)^{-1/3}.
\]

For completeness, \(D(X)\ll_\epsilon X^\epsilon\) is elementary. In \(\tau(d)=\prod_{p^e\parallel d}(e+1)\), large primes satisfy \(e+1\le2^e\le p^{\epsilon e}\); for each of the finitely many smaller primes, the ratio \((e+1)/p^{\epsilon e}\) has a finite supremum. Multiplying proves the bound uniformly in \(d\). Use \(\epsilon=3\eta\) to obtain the asserted exponent. If an error bound \(O(X^{1/3-\delta})\) held, choosing \(\eta<\delta\) would contradict it.

The gap between the necessary exponent \(1/3-o(1)\) and the retained allowed error \(o(X^{1/2})\) is not closed. In particular, this does not treat every \(o(X^{1/3})\) perturbation. This proof does not claim novelty relative to all literature on perturbations of squares.

### 4. Q2414 and Q2415: infinite elementary subfamilies

These numbers remain provisional and are always paired here with stable IDs.

**Q2414, `fbf539f5a7f03f1da075`.** For \(n=2^r,m=2^s\), \(r,s\ge1\), the conjecture holds. If \(r=s\), the sum is \(2\Phi_{2^r}\) and its noncyclotomic part is two. Otherwise assume \(r<s\), put \(a=2^{r-1},b=2^{s-1}\), and consider \(F=x^b+x^a+2\). A root with modulus below one would give \(|x^b+x^a|<2\), a contradiction. A root on the unit circle would force \(x^a=x^b=-1\), again impossible because \(b/a\) is even. Thus every root has modulus strictly greater than one. If \(F\) had two nonconstant monic integer factors, each factor's constant term would have absolute value greater than one and therefore at least two. Their product could not be the constant term two of \(F\). Gauss's lemma proves irreducibility over \(\mathbb Q\). Here the entire sum is irreducible.

**Q2415, `a06b211ca02e3eb359fa`.** For \(n=m=2^r\), \(r\ge1\), the product plus one is

\[
(x^{2^{r-1}}+1)^2+1=x^{2^r}+2x^{2^{r-1}}+2.
\]

This is Eisenstein at two, hence irreducible. It has no cyclotomic factor: its constant term two prevents it from being cyclotomic, and it is already irreducible.

Direct source comparison confirms these are restrictions of exactly Conjectures 1.2 and 1.5 in https://arxiv.org/html/2610.05568v1. Arbitrary indices remain unresolved.

### 5. Q2210: singleton length sets and exact finite witnesses

Stable ID `be959fff2c1da528a958`. In the monoid of finite subsets of \(\mathbb N_0\) containing zero, every singleton length set \(\{k\}\), \(k\ge2\), occurs.

**Construction.** Let \(A_k=\{\sum_{j=0}^{k-1}\epsilon_j3^j:\epsilon_j\in\{0,1\}\}\). It equals the sum of the \(k\) atoms \(\{0,3^j\}\). To classify all decompositions \(A_k=B+C\), note that \(B,C\subseteq A_k\). Adding two base-three vectors with digits zero or one makes no carries. No coordinate can occur in both factors, since their sum would have digit two. Each vector \(3^j\in A_k\) must occur in exactly one factor. All combinations of its assigned coordinates must occur in that factor, since all combinations occur in \(A_k\) and the other factor cannot supply those coordinates. Thus each factor is the full cube on a block of coordinates. Recursing shows the only atoms in any factorization are the \(k\) displayed two-point sets, and \(L(A_k)=\{k\}\).

The deterministic program `power_monoid_search.py` exhausts all 65,536 sets containing zero in \([0,16]\). It examines 229,504 unordered nonunit factor pairs and computes every length set by increasing maximum. For a decomposition, \(\max(B+C)=\max B+\max C\), so all factors are earlier layers. If no decomposition exists, the set is an atom. Otherwise take the union of sums of previously computed length sets. This establishes the algorithm's exhaustiveness.

Selected smallest-maximum witnesses from this exhaustion are:

| Length set | Witness |
|---|---|
| \(\{2\}\) | \(\{0,1,2\}\) |
| \(\{3\}\) | \(\{0,1,2,4,5,6\}\) |
| \(\{2,3\}\) | \(\{0,1,2,3\}\) |
| \(\{4\}\) | \(\{0,1,2,4,5,6,8,9,10\}\) |
| \(\{2,4\}\) | \(\{0,1,2,4,5,6,10,11,12,14,15,16\}\) |
| \(\{2,3,4\}\) | \(\{0,1,2,3,4\}\) |
| \(\{2,3,4,5\}\) | \(\{0,1,2,3,4,5\}\) |

An independent recursive verifier uses ordinary sets and enumerates possible divisors as subsets of each target. It reproduced all seven length sets. The full dynamic-programming table is preserved in `power_monoid_lengths_u32le.bin`; complete immediate decompositions of the witnesses are in `power_monoid_output.json`. For example, no \(\{3,4\}\) witness appears within this declared bound. This says nothing about existence outside that bound, and the general finite-set realization question remains open.

### 6. Additional precise reductions

#### Q1613 (`75f7fe19d171998305b3`)

The retained question is exactly equivalent to the finite-field assertion for polynomials over \(\mathbb F_p\) that split into nonzero linear factors and have every coefficient nonzero. In one direction, numerator and denominator of each reduced rational root are coprime to \(p\), because they divide the integer constant and leading coefficients. Reduce all roots modulo \(p\). Conversely, choose integer representatives \(1,\ldots,p-1\) of all finite-field roots and form the product of their integer linear factors; it has the same degree and the required coefficient reductions.

If all roots have a single residue class modulo \(p\), the reduced polynomial is a scalar multiple of \((x-a)^n\). Lucas's theorem implies all its coefficients are nonzero precisely when every base-\(p\) digit of \(n\) below its highest digit is \(p-1\). Therefore \(n+1\) has exactly one nonzero digit. This proves that restricted subfamily for every prime and proves the entire \(p=2\) case.

Primary checks: Hajdu–Tijdeman–Varga, Theorem 1.2 and Problems 2–3, https://dea.lib.unideb.hu/bitstreams/b0c2409b-44fa-47f4-9edc-ed6df4b24ac8/download ; Bosma et al., §3 and Figure 3, https://cs.uwaterloo.ca/journals/JIS/VOL28/Fokkink/fokkink9.pdf . The latter reports the prime-five bound via Walnut; that computation was not rerun here. The first theorem gives \(\deg f\le3\) for Q1612 (`4211038b2f8f58510864`) whenever \(2,3\notin S\). These are primary-source comparisons, not new universal solutions.

#### Q2011 (`910e657e85689a64c8c1`)

A unit clique injects into every residue field after translating one vertex to zero: distinct vertices have unit differences and therefore distinct reductions. Hence \(M(K)\le\#(\mathcal O_K/\mathfrak p)\) for every prime ideal \(\mathfrak p\). If \(M(K)>7\), every prime over two has residue degree at least three. Since \(\sum e_if_i=[K:\mathbb Q]\), in degree six the only possible pairs \((e_i,f_i)\) over two are \([(1,6)]\), \([(1,3),(1,3)]\), or \([(2,3)]\). In degree seven they are \([(1,7)]\) or \([(1,3),(1,4)]\); in particular two is unramified. Over each of three, five, and seven, all residue degrees must be at least two. These are necessary local restrictions; they do not prove finiteness of the fields.

#### Q2213 (`ca6484e601099abf0ee7`)

The inequality \(E(G)\ge d(G)+|G|\) holds for every finite group. Append \(|G|-1\) identities to a product-one-free sequence of length \(d(G)\). Any subsequence of length \(|G|\) must contain a nonempty part of the original sequence; if its terms could be ordered to product one, deleting identities would contradict product-one-freeness. Thus only the reverse inequality is a remaining universal target.

#### Q2217 (`19c8d772d81df73beca8`)

A counterexample must, after embedding its Grothendieck group into \(\mathbb Q\) and possibly changing signs, be a nonnegative rational monoid with positive elements accumulating at zero. Indeed, a rational monoid containing both a positive and a negative element is a group: a positive rational multiple relation supplies the inverse of either element, and then of every element. For a subgroup of \(\mathbb Q\), normalize a finite set by its minimum. Every normalized factor is a subset of that fixed finite normalized target. Its positive width is at least the least positive element of that target, so factorization length is bounded by the target width divided by that positive minimum. Repeated splitting terminates, proving that the power monoid is atomic. For a nonnegative monoid with all positive elements at least \(\delta>0\), every nonunit factor has maximum at least \(\delta\); the same argument using maxima proves atomicity of the power monoid. In particular no finitely generated rank-one monoid can answer Q2217. The accumulation-at-zero case remains open here.

The primary source explicitly retains Question 5.6 and locates its counterexample in rank two: https://arxiv.org/html/2501.03407v1 . This was checked against the exact retained scope.



## Part D. Exact Diophantine research

Date: 7 October 2026. All arithmetic programs below actually ran. No proof assistant was run. The full retained questions remain unresolved; the results below are partial theorems, exact local witnesses, a source-proof repair, and bounded exhaustive computations. No novelty claim is made for the derived elementary identities or local-solubility results.

### 1. Source scope and status audit

The source setup is part of each question, even when absent from its short wording.

| Question | Stable ID | Exact retained target and scope | Outcome in this lane |
|---|---|---|---|
| Q1511 | `0f88e5baee08af4d6f4f` | For every integer k>1, is (x,y,z)=(k−1,1,2) the only positive-integer solution of x²+(2k−1)^y=k^z? | Corrected, computationally certified proof of the known y∈{3,5} exclusion when z is even or k is a square. General uniqueness remains unresolved. |
| Q1608 | `a2149a20f47eba9e27ee` | Is (a^n+1)(b^n+1)=x² impossible for every n≥4, with positive integers and 1≤a<b? | Source comparison only; the 4|n subcase is already proved in the source. |
| Q1609 | `56c577fc2add1efcbecd` | Are the only positive solutions of (a³+1)(b³+1)=x², 1≤a<b, the triples (1,23,156), (6,26,1953), (20,362,616077)? | Exact exhaustive verification through b≤10,000,000; no additional solutions. |
| Q1610 | `746ff7ed37b5c6eff82f` | Is (a^n−1)(b^n−1)=x² impossible for every n≥5, with positive integers and 1<a<b? | Source comparison only; general target remains unresolved. |
| Q1611 | `77f199e22acb02c0e966` | Are the only positive solutions of (a³−1)(b³−1)=x², 1<a<b, the triples (2,4,21), (2,22,273), (3,313,28236), (4,22,819)? | Exact exhaustive verification through b≤10,000,000; no additional solutions. |
| Q2314 | `5a4ccc40e698f43e2bbe` | Is {(x,y,z,t)∈Z⁴:xyz+t²+1=0} a finite union of images of integer-coefficient polynomial maps Z^r→Z⁴? | Explicit dense three-parameter polynomial family and an exact point outside that family and all its sign/permutation copies. Finite-cover target remains unresolved. |
| Q2315 | `fe5ce4fae3105179737a` | Does x⁴+x³y−y⁴+y³z+z⁴=0 have a nonzero integer solution? | Proved solubility over R and primitive solubility over every Z_p. Thus every modulus admits a primitive local solution. Global existence remains unresolved. |
| Q2316 | `210ee10d0d0097b4ee16` | Does x³+x+y³+y+z³+z=xyz+1 have an integer solution? | Explicit rational point, proved solubility over every Z_p, and exclusion of coordinates 0,±1. Integer existence remains unresolved. |

Primary source comparisons, retrieved in this session:

* Bogdan Grechuk, *A systematic approach to Diophantine equations: open problems*, arXiv:2404.08518v10, 1 October 2026: https://arxiv.org/html/2404.08518v10 . Definition 1 and Table 1 give the polynomial-family scope; equation (24), Problem 5 gives Q2315; equation (28), Problem 6 gives Q2316. All three are retained as open. The arXiv abstract confirms v10 is the 1 October revision: https://arxiv.org/abs/2404.08518 .
* Paulius Virbalas, arXiv:2606.31223v1, 30 June 2026: https://arxiv.org/html/2606.31223v1 . Equations (1.1)/(1.2) require 1<a<b for minus and 1≤a<b for plus. Section 6 explicitly retains the two Cohn targets and Conjectures 6.2–6.3. Immediately before Conjecture 6.3, the author reports a plus-cubic search through b≤10^6. The present 10^7 bound extends that stated bound; it is not a claim of the world's largest search.
* Elif Kızıldere Mutlu, Maohua Le, Gökhan Soydan, arXiv:2301.05431v1, 13 January 2023: https://arxiv.org/pdf/2301.05431 . Page 1 states the same unrestricted k>1 uniqueness conjecture. Lemma 2.3 and its proof are on pp.4–5, Lemma 2.4 on pp.5–6, Theorem 1.2 on p.2. A repairable threshold error is documented below.
* Maohua Le and Anitha Srinivasan, arXiv:2210.04758v2, 2 December 2023: https://arxiv.org/pdf/2210.04758 . Theorem 1.3 assumes **4 exactly divides k**, 4≤k≤1000, and 2k−1 a prime power. It must not be expanded to all multiples of 4. Its introduction also identifies a y=1 coverage gap in an earlier cited result. These are scope statements, not independent validation of that paper's full proof.
* Grechuk's author-maintained MathOverflow question and answer: https://mathoverflow.net/questions/400714/can-you-solve-the-listed-smallest-open-diophantine-equations . In his 19 February 2022 comment below the first answer, the author reports no Q2316 solution with |y+z|≤5,000,000. Therefore the much smaller scratch search used here to find a rational point is not represented as an integer-search advance.

For Q1608, the source's 4|n theorem has the familiar squarefree-core reduction: a^n+1=du² and b^n+1=dv². If n=4ℓ, this gives two positive solutions to X⁴−dY²=−1, contrary to the Ljunggren uniqueness theorem cited as Lemma 2.5. The cited deep dependency was not independently reproved here. Diagonal a=b examples violate the retained source setup and do not disprove either higher-exponent conjecture.

### 2. Q2315: an exact proof of everywhere local solubility

Let

F(x,y,z)=x⁴+x³y−y⁴+y³z+z⁴,

and let C be the projective plane curve F=0.

#### 2.1 Smooth reduction outside three explicitly identified primes

The partial derivatives are

F_x=x²(4x+3y),
F_y=x³−4y³+3y²z,
F_z=y³+4z³.

Over a field of characteristic other than 2 or 3, a singular projective point cannot have y=0: F_z=0 would then force z=0 and F_x=0 would force x=0. Scale y=1. Then F_x=0 implies either x=0 or x=−3/4, while the other two derivative equations imply

z³=−1/4,   z=(4−x³)/3.

If x=0, then z=4/3 and the compatibility condition is 283=0 in the field. If x=−3/4, then z=283/192 and the compatibility condition is

283³+192³/4 = 24,434,659 = 149·163,991 = 0.

Thus a singular reduction is possible only for p∈{149,283,163991}. The same calculation over Q proves C is smooth over Q. In characteristic 2, F_z=y³=0 forces y=0, F_y=x³=0 forces x=0, and then F=0 forces z=0. In characteristic 3, F_x=x³=0 and F_y=−y³=0 force x=y=0, and F_z=z³=0 forces z=0. Hence these characteristics are smooth too.

A smooth plane quartic is geometrically irreducible and has genus (4−1)(4−2)/2=3. For good primes p≥37, Hasse–Weil yields

#C(F_p) ≥ p+1−6√p > 0.

The genus formula and Hasse–Weil statement can be checked in Bjorn Poonen, *Lectures on rational points on curves*, 5 March 2006 version, §2.9.2, printed p.39 (PDF p.45), and §3.3, printed p.52 (PDF p.58): https://math.mit.edu/~poonen/papers/curves.pdf . Smoothness guarantees that any such point is nonsingular.

#### 2.2 Certificates for the remaining primes

Each row below satisfies F(P)≡0 mod p and has the indicated nonzero derivative. The complete F values and full derivative triples are in `q2315_local.json`.

| p | P=(x,y,z) | A nonzero derivative mod p |
|---:|---|---|
| 2 | (1,0,1) | F_y=1 |
| 3 | (1,1,1) | F_x=1 |
| 5 | (1,1,3) | F_x=2 |
| 7 | (0,1,4) | F_y=1 |
| 11 | (0,1,8) | F_y=9 |
| 13 | (0,1,11) | F_y=3 |
| 17 | (0,1,2) | F_y=2 |
| 19 | (1,1,2) | F_x=7 |
| 23 | (0,1,11) | F_y=6 |
| 29 | (0,1,7) | F_y=17 |
| 31 | (2,1,21) | F_x=13 |
| 149 | (1,1,63) | F_x=7 |
| 283 | (0,1,18) | F_y=50 |
| 163991 | (−19,19,−5) | F_x≠0 |

The last certificate is particularly small: F(−19,19,−5)=−163991. Its x-derivative is −6859, which is nonzero modulo 163991.

Fix two coordinates and use a coordinate with nonzero derivative as the one-variable Hensel variable. The point lifts to a zero of F in Z_p³ that remains nonzero modulo p. Therefore, for every prime p, C has a primitive Z_p point. The intermediate value theorem applied to F(0,1,z)=z⁴+z−1 at z=0 and z=1 gives a real point.

For any positive integer m, take the lifted points modulo each prime power dividing m and combine coordinates by the Chinese remainder theorem. The resulting congruence solution satisfies gcd(x,y,z,m)=1. Consequently **no modulus can obstruct a primitive solution**, and searching for a contradictory modulus cannot settle Q2315 negatively. Existence of a rational/projective point, equivalently a nonzero integer point after clearing denominators, is still unresolved.

An elementary necessary condition for a primitive integer point is y≡2 mod4 with x,z odd. Modulo 2, y odd makes F odd; y even forces x,z to have the same parity, and primitivity then forces both odd. Modulo 4, 4|y would give F≡2, so v₂(y)=1. These restrictions are compatible with the local points and do not give a contradiction.

### 3. Q2316: a rational point and integral points over every local field

Write

G(x,y,z)=x³+x+y³+y+z³+z−xyz−1.

The exact rational point is

P=(−13/20,−79/20,21/5).

Its common-denominator check is

(−13)³+(−79)³+84³−(−13)(−79)(84)
 +(−13−79+84)·20²−20³ = 0.

The first four cubic terms total 11200 and the remaining terms total −11200. Thus G(P)=0 over Q. For each prime p not dividing 20, all three coordinates lie in Z_p.

At p=2, use (1,1,1): G=4 and G_x=3 is odd. More explicitly, G(x,1,1)=x³+3, which has a simple root x=1 modulo 2 and hence a root in Z₂. At p=5, use (1,1,3): G=30 and G_x=1 modulo 5. Here G(x,1,3)=x³−2x+31, again with a simple root x=1 modulo 5. Hensel's lemma supplies integral local points at the remaining primes. The rational point also supplies a real point.

This proves

{(x,y,z)∈Z_p³:G(x,y,z)=0}≠∅ for every prime p,

and hence solvability modulo every positive integer. **Pure congruence obstruction is unavailable for Q2316 as well.** The rational point does not answer the question about integer points.

#### 3.1 An exact divisor reduction

For integer solutions, reduction modulo 2 gives xyz odd, so all coordinates are odd. Put

a=(x+y)/2, b=(x−y)/2, d=3(x+y)+z.

Then x=a+b, y=a−b, z=d−6a, and direct expansion gives the identity

G(a+b,a−b,d−6a)
 =d[b²+(d−9a)²+26a²+1]−(208a³+4a+1).

Consequently every integer solution satisfies

d | 208a³+4a+1,

b²=(208a³+4a+1)/d−(d−9a)²−26a²−1≥0,

where a,b have opposite parity and d is odd. Conversely any integers a,b,d satisfying the identity reconstruct an integer solution. The right-hand cubic is odd and cannot vanish for integer a, so d=0 does not create a missing case. This is an exact divisor-search reformulation, not a new proof of nonexistence.

For the rational point, the homogeneous analogue with denominator w is

d[b²+(d−9a)²+26a²+w²]=208a³+4aw²+w³.

The tuple (a,b,d,w)=(−46,33,−192,20) gives the displayed rational point. The discovery search considered w in increasing order from 2 with cap 30 and −100≤a≤100 by exact divisor enumeration; it stopped after finding a point at w=20. It was a witness search, not an exhaustive integer-height claim. The complete script and output are q2316_rational_search.py/.json.

#### 3.2 No coordinate can be 0 or ±1

Zero is excluded by parity. For a fixed coordinate c=±1, put s=y+z and p=yz. Then s is even and

(3s+c)p=s³+s+c³+c−1.

Since

27(s³+s+c³+c−1)
 =(3s+c)(9s²−3cs+c²+9)+(26c³+18c−27),

d=3s+c divides R(c)=26c³+18c−27. For c=1, R=17 and d≡1 mod6; the only possibilities are (d,s)=(1,0),(−17,−6). Their quadratic discriminants s²−4p are −4 and −16. For c=−1, R=−71 and d≡−1 mod6; the only possibilities are (d,s)=(−1,0),(71,24), with discriminants −12 and −204. All are negative. Symmetry completes the exclusion of any coordinate 0,±1.

### 4. Q2314: dense polynomial families do not provide a finite cover

For any solution xyz+t²+1=0 and any u∈Z, the transformation

(x,y,z,t) ↦ (x,y,z−2tu−xyu²,t+xyu)

preserves the equation, by direct cancellation. Permuting x,y,z gives analogous transformations. Thus each fixed solution lies on an explicit one-parameter polynomial family; this fact alone would provide only a countable union.

A useful three-parameter family is obtained as follows. For arbitrary integers a,b,c, set

A=a²+1,  B=1−2ab+Ab²,  T=a−Ab,

(x,y,z,t)=(−1−2Tc−ABc², B, A, T+ABc).

Since AB=T²+1, substitution gives xyz+t²+1=0 identically. Moreover B=(ab−1)²+b²>0, and A>0. The Jacobian of (z,y,t) with respect to (a,b,c), at (1,0,0), is

[[2,0,0],[0,−2,0],[1,−2,2]],

with determinant −8. These three coordinates are algebraically independent; the polynomial image is Zariski dense in the three-dimensional irreducible hypersurface xyz+t²+1=0.

Nevertheless this family always has z=a²+1. Any coordinate permutation or allowable sign change of it still has some coordinate whose absolute value is one more than a square. The exact solution

(x,y,z,t)=(−13,13,29,70)

satisfies xyz=−4901 and t²+1=4901, while neither 13 nor 29 is one more than a square. It lies outside every such copy of this particular family. This proves a precise limitation of the constructed dense family. It does **not** rule out a different finite collection of polynomial families.

### 5. Q1609 and Q1611: exact exhaustive cubic search through ten million

For a positive integer n, let sf(n) be the product of the primes whose exponents in n are odd. Then UV is a square if and only if sf(U)=sf(V). This elementary equivalence removes the quadratic pair enumeration.

The code factors a³+1=(a+1)(a²−a+1), and a³−1=(a−1)(a²+a+1). A smallest-prime-factor sieve handles a±1. The quadratic factors are sieved at their roots modulo every prime p≤N. Except for p=3, such roots exist precisely for p≡1 mod3, where the quadratic formula uses a square root of −3. Repeated division records exponent parity. Each remaining quadratic cofactor is either 1 or a prime greater than N: a quadratic value is less than (N+1)², so two unsieved prime factors are impossible. Combining the two squarefree cores cancels their common factors twice. Sorting these exact cores produces every admissible collision.

The program uses unsigned 128-bit integers for cubes, cores, packed sort entries, and reported square roots. It verifies at every input a that (a³±1)/sf(a³±1) is an exact square. Each reported pair is checked again by arbitrary-precision Python substitution. The full b≤1000 search was independently compared with direct integer-square-root testing of every product, without using the sieve.

Declared domain: N=10,000,000; plus 1≤a<b≤N; minus 2≤a<b≤N. Exhaustive and deterministic; no seed. The intended resource ceiling was approximately 0.5 GiB memory and one minute. The completed C++ run reported 9.22701 seconds. The experiment is a search for exact square products; there is no fitted model or empirical loss function.

| Sign | Number of eligible a-values | Number of represented ordered-by-size pairs | All collisions (a,b,x) |
|---|---:|---:|---|
| + | 10,000,000 | 49,999,995,000,000 | (1,23,156), (6,26,1953), (20,362,616077) |
| − | 9,999,999 | 49,999,985,000,001 | (2,4,21), (2,22,273), (4,22,819), (3,313,28236) |

The plus cores are 2,217,889 respectively. The minus triples involving 2,4,22 have core 7; the (3,313) pair has core 26. No extra solution appeared. This establishes the bounded statements only. Every possible b>10^7 remains outside the computation.

Files: `cubic_squarecore.cpp`, `cubic_squarecore_10000000.json`, `validate_cubic_search.py`, `cubic_search_validation.json`. An earlier N=2,000,000 run is also archived. The C++ executable is reproducible with

    g++ -O3 -std=c++17 cubic_squarecore.cpp -o cubic_squarecore
    ./cubic_squarecore 10000000
    python validate_cubic_search.py

### 6. Q1511: repair and verification of a known partial argument

This section proves the following partial statement:

**For every integer k>1, no positive-integer solution to x²+(2k−1)^y=k^z exists when y∈{3,5} and either z is even or k is a square.**

These are subcases already claimed in the cited 2023 paper. The value of the present work is an explicit correction and executable verification, not a claim to have resolved Terai's conjecture.

#### 6.1 Corrected gap lemma and certificates

Suppose F,G,R∈Z[T] satisfy F=G²+R. If G(n)>0, R(n)>0, and 2G(n)−R(n)>0, then

G(n)²<F(n)<(G(n)+1)².

If G(n)>0, R(n)<0, and 2G(n)+R(n)−1>0, then

(G(n)−1)²<F(n)<G(n)².

Either case excludes F(n) being a positive square.

For equation (2.16), the source sets G(T)=T³−4 and R(T)=12T²−6T−15. Its asserted eventual positivity threshold m(2G−R)=1 is false: (2G−R)(2)=−13. Threshold 6 works, since

2G(T)−R(T)=2T²(T−6)+6T+7>0 for T≥6.

The program `q1511_corrected_subcase.py` verifies all eight identities F=G²+R in Lemma 2.3 by integer polynomial arithmetic and supplies valid thresholds:

| Source equation | Safe threshold T |
|---|---:|
| (2.15) | 16 |
| (2.16) | 6 |
| (2.17) | 27050 |
| (2.18) | 43 |
| (2.19) | 6 |
| (2.20) | 40 |
| (2.21) | 168 |
| (2.22) | 40 |

For each case, the JSON certificate contains the exact coefficient lists for F,G,R, and the coefficient lists of G(T+u), |R(T+u)|, and the required gap polynomial at T+u. Every listed coefficient is nonnegative and every constant coefficient is positive. This proves all required signs for every real u≥0, not just a tested range. For each integer 1≤n<T, exact integer-square-root tests exclude positive squares. In total 27,361 finite tests ran. The full input polynomials, shifted positivity certificates, test ranges, and SHA-256 digests of the finite test streams are in `q1511_corrected_subcase.json`.


The complete input polynomials for that finite certificate are listed here; coefficients are exact. In every row F=G²+R.

| Source equation | F(T) | G(T) | R(T) | Safe threshold |
|---|---|---|---|---:|
| 2.15 | $T^4-(2T-1)^3$ | $T^{2}-4T-2$ | $-22T-3$ | 16 |
| 2.16 | $T^6-(2T-1)^3$ | $T^{3}-4$ | $12T^{2}-6T-15$ | 6 |
| 2.17 | $T^6-(2T-1)^5$ | $T^{3}-16T^{2}-88T-1448$ | $-54040T^{2}-254858T-2096703$ | 27050 |
| 2.18 | $T^8-(2T-1)^5$ | $T^{4}-16T+40$ | $-80T^{3}-216T^{2}+1270T-1599$ | 43 |
| 2.19 | $T^{10}-(2T^2-1)^3$ | $T^{5}-4T$ | $12T^{4}-22T^{2}+1$ | 6 |
| 2.20 | $T^{10}-(2T-1)^5$ | $T^{5}-16$ | $80T^{4}-80T^{3}+40T^{2}-10T-255$ | 40 |
| 2.21 | $T^{14}-(2T^2-1)^5$ | $T^{7}-16T^{3}+40T$ | $-336T^{6}+1320T^{4}-1610T^{2}+1$ | 168 |
| 2.22 | $T^{18}-(2T^2-1)^5$ | $T^{9}-16T$ | $80T^{8}-80T^{6}+40T^{4}-266T^{2}+1$ | 40 |

#### 6.2 Deduction for even z

Assume z=2m. Because gcd(k,2k−1)=1, the original equation implies gcd(x,k)=1. The two positive factors

k^m−x, k^m+x

are odd, coprime, and have product (2k−1)^y. Since y is 3 or 5, they equal g^y and f^y for coprime odd positive integers f>g with fg=2k−1. Therefore

2k^m=f^y+g^y≤(2k−1)^y+1<2^y k^y.

The first inequality follows by maximizing U+V among positive integers UV=(2k−1)^y. Also z>y, because (2k−1)^y>k^y.

For y=3 and k≥4, these inequalities force m∈{2,3}, so x² equals the polynomial in (2.15) or (2.16). For y=5 and k≥16, they force m∈{3,4,5}, so x² equals (2.17), (2.18), or (2.20). The corrected gap certificates exclude all these possibilities. For y=3,k∈{2,3}, and y=5,2≤k≤15, the program enumerates all coprime factorizations fg=2k−1 and verifies that (f^y+g^y)/2 is not a power of k. Eighteen exact factor cases were checked. Thus the even-z statement holds for every k>1.

These small-k checks also avoid an implicit small-base problem in the source's inference from 2k^m<2^y k^y: a bound on m valid for large k cannot be used without treating small k separately.

#### 6.3 Deduction when k is a square

Let k=t² with t≥2. The even-z case is already excluded. For odd z, the same coprime factorization now gives

2t^z=f^y+g^y≤(2t²−1)^y+1<2^y t^{2y},

with fg=2t²−1 and z>y. For y=3,t≥4, this forces odd z=5; the square equation is (2.19). For y=5,t≥16, it forces odd z∈{7,9}; the square equations are (2.21) and (2.22). The same corrected gap certificates apply. The remaining t values were checked by all coprime factorizations of 2t²−1, nineteen cases total, with no mean (f^y+g^y)/2 equal to a power of t. This completes the stated partial theorem.

Residual Q1511 scope includes all other y values, and y=3 or 5 with nonsquare k and odd z. The full uniqueness conjecture is not closed by this argument.

### 7. Artifact inventory and evidence boundaries

* `q2315_local.py`, `q2315_local.json`, `q2315_local_run.txt`: complete finite local certificates plus the written all-prime proof above.
* `q2316_checks.py`, `q2316_checks.json`: rational witness and exceptional-prime Hensel checks. The transformation grid is a regression check; the written expansion is the proof of the polynomial identity.
* `q2314_checks.py`, `q2314_checks.json`: regression checks for the written identities and exact excluded-family point.
* `cubic_squarecore.cpp`, compiled `cubic_squarecore`, full JSON outputs at 2m and 10m, independent validation script and JSON.
* `q1511_corrected_subcase.py`, `q1511_corrected_subcase.json`: all exact polynomial and finite certificates for the repaired partial theorem.
* `ledger_fragment.json`: statement-level status, assumptions, dependencies, source links and evidence classes.

No script result here is a compiled formal theorem. The all-prime conclusions combine written proofs with the finite certificates, Hensel lifting, and, only for Q2315, the standard Hasse–Weil theorem. Finite cubic searches establish exactly the declared bounded regions. Neither local solubility theorem supplies the missing global integral point.


## Part E. A WKL₀ upper bound for ring colouring

Programme B2; provisional Q2469; stable statement ID `d4554ad68bb1d9e77596`.

Exact retained question: What is the reverse-mathematical strength over RCA₀ of the assertion that, for every countable commutative ring R, finite m×n matrix A over R, and nonzero b∈R^m, if Ax=b has no constant solution then some finite coloring of R has no monochromatic solution?

### Conclusion

The proposed ACA₀ proof is correct. The use of arithmetical comprehension to form the range of r↦(Σ_i a_i)r can be avoided. The finite-presentation construction below gives the stronger upper bound

\[
\boxed{\mathrm{WKL}_0\ \Longrightarrow\ \text{the retained ring-coloring assertion}.}
\]

For n≥2, the number of colors can be bounded uniformly by

\[
\boxed{q(n)=[3(n-1)]^{n-1}.}
\]

For n≤1 the assertion is trivial with one color. This is an upper bound only. No reversal to WKL₀ is proved, so the exact reverse-mathematical strength remains unresolved. The proof below is a written mathematical argument; no proof-assistant formalization has run. Its finitary algebra uses explicit integer matrices and the Euclidean algorithm, not a basis theorem for an arbitrary subgroup of a finitely generated group.

### 1. Review of the ACA₀ quotient argument

Write the columns of A as a₁,…,a_n∈R^m and put s=Σ_i a_i. A constant solution exists exactly when b=sr for some r∈R. In ACA₀ the set H={sr:r∈R} exists; it is an additive subgroup of R^m. Equality modulo H is decidable relative to this set, and least representatives give a coded quotient abelian group G=R^m/H. The class of b is nonzero.

Let ℓ=n−1. Laboska's Theorem 4.2 supplies a coloring c of G with at most 3ℓ colors that forbids every solution

\[
\sum_{i=1}^{\ell}(u_i-v_i)=\bar b
\]

in which c(u_i)=c(v_i) separately for every i. Color r∈R by the ℓ-tuple `(c(a_i r+H))_{i≤ℓ}`. If x₁,…,x_n had the same tuple-color and Ax=b, then

\[
\sum_{i=1}^{\ell}(a_i x_i-a_i x_n)=b-sx_n\equiv b\pmod H,
\]

contradicting the defining property of c. The color count is at most (3ℓ)^ℓ. The endpoint n=1 has no solution at all under the hypothesis, since every one-variable solution is constant.

The arithmetic is correct. The quotient-range step is an avoidable use of ACA₀, not evidence of an ACA₀ lower bound.

### 2. Finitary integer-separation lemma

**Lemma.** Fix a finite list of relation vectors r₁,…,r_t∈Z^d and z∈Z^d. Suppose z is not an integer linear combination of the r_j. Then one can find an integer N≥2 and a homomorphism

\[
h:\mathbb Z^d\longrightarrow\mathbb Z/N\mathbb Z
\]

such that h(r_j)=0 for all j and the least residue β of h(z) satisfies

\[
N/3\le\beta\le2N/3.
\]

All input and output objects are finite integer arrays. The lemma is available in RCA₀.

**Proof and computational content.** Apply integer row and column operations to the finite matrix whose rows are r_j, retaining the unimodular transformations. The Euclidean algorithm diagonalizes it: in transformed coordinates the row lattice is generated by `d₁e₁,…,d_re_r`, with d_i>0. The divisibility chain of a full Smith normal form is unnecessary. Explicit finite diagonalization is performed by swaps, sign changes, integer row/column additions, and Euclidean remainder reductions. Nonzero pivot reductions strictly decrease a positive integer; completed pivots reduce the remaining matrix dimension. The primitive-recursive termination bound is supplied in the appendix below, to distinguish this step from nonuniform subgroup-basis existence. No comprehension of the range of a homomorphism of countable structures is used.

Let z′ be the transformed z. If z′_j≠0 for some j>r, project to that free coordinate modulo N=2|z′_j|. Its image is N/2, and every relation maps to zero.

Otherwise, for some j≤r the integer d=d_j fails to divide z′_j. Let t be the residue of z′_j modulo d, let g=gcd(t,d), and q=d/g≥2. The integer t/g is invertible modulo q. Choose an integer a with

\[
a(t/g)\equiv\lfloor q/2\rfloor\pmod q.
\]

The homomorphism given by a times the j-th transformed coordinate modulo N=d annihilates every relation and sends z to the residue

\[
\beta=g\lfloor q/2\rfloor.
\]

For every integer q≥2, q/3≤floor(q/2)≤2q/3, so β lies in the required interval. This completes the proof.

**Coloring consequence.** For any ℓ≥1, put K=3ℓ. Color w∈Z^d by

\[
c(w)=\left\lfloor K\,\frac{\operatorname{res}_N h(w)}N\right\rfloor\in\{0,\dots,K-1\}.
\]

This factors through the relations. Whenever c(u_i)=c(v_i), the difference of their least residues has absolute value strictly less than N/K. Therefore a sum of ℓ such differences has absolute value strictly less than N/3. It cannot be congruent modulo N to β∈[N/3,2N/3]. Hence c excludes pairwise monochromatic solutions to `Σ_i(u_i−v_i)=z` modulo the relations. This proves the particular finite-presentation version of Straus' lemma needed below inside RCA₀; it does not invoke an infinite quotient or an infinite coloring theorem.

### 3. Every finite part of the ring has a uniformly bounded good coloring

Assume n≥2, put ℓ=n−1, and let F be any finite set of elements of R. Form the free abelian group on the finite formal symbols

\[
B,\qquad E_{i,r}\quad(1\le i\le\ell,\ r\in F).
\]

These are formal symbols: equalities such as a_i r=a_j u in R^m need not be identified. This avoids constructing any actual subgroup or quotient of R^m.

For every actual tuple x=(x₁,…,x_n)∈F^n satisfying Ax=b, include the finite relation vector

\[
\rho_x=\sum_{i=1}^{\ell}(E_{i,x_i}-E_{i,x_n})-B.
\]

There are only finitely many such tuples, and they are recognized by evaluating the given ring operations. The distinguished basis vector B is not in the integer span of these relation vectors. To prove this, evaluate the formal symbols additively by

\[
B\mapsto b,\qquad E_{i,r}\mapsto a_i r\in R^m.
\]

For every listed solution x,

\[
\rho_x\longmapsto
\sum_{i=1}^{\ell}(a_i x_i-a_i x_n)-b
=-sx_n.
\]

If B=Σ_x c_xρ_x with integers c_x, evaluation would give

\[
b=-\sum_x c_xs x_n
=s\left(-\sum_x c_x x_n\right).
\]

The parenthesized expression is an explicitly formed element of R, yielding a constant solution and contradicting the hypothesis. This reasoning uses no set H={sr:r∈R}.

Apply the finitary lemma to these relation vectors and z=B. Its K=3ℓ coloring c now gives a coloring of F by

\[
C_F(r)=\big(c(E_{1,r}),\dots,c(E_{\ell,r})\big).
\]

There are at most K^ℓ=q(n) tuple colors. If an actual solution x∈F^n were monochromatic for C_F, then c(E_{i,x_i})=c(E_{i,x_n}) for every i. But its included relation says

\[
\sum_{i=1}^{\ell}(E_{i,x_i}-E_{i,x_n})=B
\]

modulo the finite relation list, contradicting the finitary coloring lemma. Thus every finite F has a q(n)-coloring avoiding all its monochromatic solutions. This whole finite-feasibility argument is carried out in RCA₀.

### 4. One application of weak König's lemma

Represent the countable ring by its coded domain D⊆N and its given operations. Fix q=q(n). Let T be the tree of finite strings σ∈q^{<N} such that there is no monochromatic solution Ax=b whose coordinates lie in D below |σ|. Elements outside D may be colored arbitrarily.

Membership in T is computable relative to the coded ring and finite matrix: there are only |σ|^n tuples to inspect, and their products and sums are computed using the given operations. Therefore T exists by Δ₁ comprehension in RCA₀. It is closed under initial segments. Section 3 shows that T has a node at every height, so it is infinite.

WKL₀, in its equivalent finite-branching form, gives an infinite path C through T. Restrict C to D. A monochromatic solution in R would have all of its finitely many coordinate codes below some height, contradicting the defining condition on the corresponding initial segment of C. This completes the WKL₀ upper-bound proof with the explicit color bound q(n).

### 5. Evidence boundaries and computability consequence

The construction shows more than the original ACA₀ quotient argument: the q(n)-branching solution tree is uniformly computable relative to the ring presentation and matrix, and its infinitude follows from finitary integer algebra. Thus every PA degree relative to a computable input can compute a witnessing coloring, by the standard path characterization of PA degrees. No lower bound or optimality of q(n) is asserted.

The reverse direction requires an independent construction. In particular, taking an equation x−y=b does not immediately yield a WKL₀ reversal when arbitrarily many colors are allowed: its graph has maximum degree two and admits a straightforward computable three-coloring. Optimal two-coloring statements must not be confused with the retained existence of some finite coloring.

Primary comparison: Gabriela Laboska, [On the Effectiveness of Partition Regularity over Algebraic Structures](https://arxiv.org/html/2504.09235v1), Theorem 4.2 and Open Question 3 (also Open Question 40 in §5.3). Her theorem supplies the Straus upper bound used in the initial ACA₀ argument. The finite-presentation proof here independently supplies exactly the finite feasibility needed for WKL, and avoids applying her theorem to an uncoded range quotient.

### Appendix: a primitive-recursive bound for the required diagonalization

Only diagonal form is needed, not the Smith divisibility conditions. Here is a bounded algorithm for an r×d integer matrix, retaining its elementary-operation list. Treating that list as a finite certificate also avoids any implicit choice of transformations.

At the current active block, move a nonzero entry to its top-left corner and make the pivot a positive. For each entry y below it in its column, write y=qa+t with 0≤t<a and subtract q times the pivot row. If t>0, swap that row into the pivot position and restart the phase; the new positive pivot is strictly smaller. If the column clears, treat every other entry in the pivot row by the analogous column division. A nonzero remainder again produces a strictly smaller pivot and a restarted phase. If no such remainder occurs, both the pivot row and column clear, leaving a smaller active block. Zero blocks terminate immediately.

Suppose C≥1 bounds the entries in absolute value at the start of one active-block step. The initial positive pivot is at most C and every restarted phase strictly decreases it. Thus there are at most C restarted or completed phases. Each phase contains at most r+d Euclidean reductions, and each reduction uses at most a bounded number of elementary additions, swaps, and sign changes. The generous bound

\[
N=4(C+1)(r+d+1)
\]

therefore bounds the elementary operations needed to isolate that pivot. If M≥1 bounds the absolute entries of the current matrix and the accumulated row/column transformation matrices, then a quotient in one reduction has absolute value at most 2M. Consequently the function

\[
F(M)=4(M+1)^2
\]

bounds every updated entry, including entries in the transformation matrices. Iterating F exactly N times supplies a primitive-recursive bound on all entries after that active-block step. Repeat this bound at most min(r,d) times, once for each completed pivot. This is still primitive recursion on finite integers. Euclidean division and all checks on the resulting finite matrices are available in RCA₀, and Σ₁ induction proves the stated termination and correctness bounds.

Each operation is explicitly unimodular and its inverse is another elementary integer operation. The resulting diagonal matrix therefore describes exactly the original row lattice after the recorded change of coordinates. The lattice-membership alternatives used in the finitary separation lemma are merely coordinate divisibility tests on this explicit diagonal matrix. No statement that an arbitrary subgroup of Z^d has a finite basis is invoked.


## Part F. Experiment register and reproducibility

The finite computations have the domains below. The numerical searches propose objects; the exact checks establish the bounded claims. Runtime numbers are observations from this workspace and are not performance guarantees.

### four_color_discovery

- **Purpose:** Find an explicit high-density coloring; no upper-bound or optimality claim.
- **Domain:** Piecewise constant colorings with interval and residue classes; exact final family has nine intervals.
- **Generator:** Seeded local improvement in rainbow_search.py and rainbow_grid_search.cpp; rational stationary calculation in rainbow_exact.py.
- **Permitted observations:** Color assignments and exact or numerical counts of rainbow triples.
- **Loss:** Negative ordered rainbow-triple density.
- **Seed:** 20261007; C++ uses20261007+number_of_colors
- **Resource budget:** Initial parity grid240 with30 restarts and100 sweeps; saved C++ grid runs use120 or500 restarts,180 sweeps, and25-second per-run cap.
- **Controls:** Exact Fraction integration; symbolic integer all-t coefficients; independent integer rectangle enumeration and2548 brute-force cases.
- **Uncertainty:** Heuristic search is incomplete; the displayed coloring is rigorously certified without assuming the search was optimal.

Artifacts: `research/root/rainbow_search.py`, `research/root/rainbow_search_output.json`, `research/root/rainbow_grid_search.cpp`, `research/root/rainbow_grid_k3.json`, `research/root/rainbow_grid_k4.json`, `research/root/rainbow_grid_k4_m240.json`, `research/root/rainbow_exact.py`, `research/root/rainbow_exact_output.json`, `research/squarefree_algebra/rainbow_interval_verification.json`.

### paley

- **Purpose:** Certify finite cliques and justified relaxation bounds.
- **Domain:** All29 primes p<=300 with p=1mod4.
- **Generator:** paley_experiment.py
- **Permitted observations:** Explicit adjacency, clique witnesses, optimization candidates and certificate residuals.
- **Loss:** Negative clique size for search; theta primal/dual objectives for candidate optimization.
- **Seed:** Deterministic; no random seed.
- **Resource budget:** At most4 smooth optimization stages,250 iterations per stage per finite graph; actual generator6.635s and verifier1.682s recorded.
- **Controls:** Independent integer clique trees, rational Fourier interval primal/dual checks, rational Gram plus diagonal-dominance PSD certificates.
- **Uncertainty:** Finite prime range; two-local SDP certificates need not be optimal; no asymptotic inference.

Artifacts: `research/paley/results.csv`, `research/paley/results.json`, `research/paley/certificates/`, `research/paley/verification.json`.

### cubic_square_products

- **Purpose:** Exhaustively test the two retained cubic solution lists.
- **Domain:** 1<=a<b<=10^7 for plus;2<=a<b<=10^7 for minus.
- **Generator:** cubic_squarecore.cpp
- **Permitted observations:** Exact squarefree-core collisions and integer-square checks.
- **Loss:** None: exact decision enumeration.
- **Seed:** Deterministic; no random seed.
- **Resource budget:** Approximately0.5GiB and one minute; actual10^7 run9.22701s.
- **Controls:** Every core quotient is checked square; independent direct product testing for all b<=1000; arbitrary-precision substitution of every witness.
- **Uncertainty:** No assertion about b>10^7.

Artifacts: `research/diophantine/cubic_squarecore.cpp`, `research/diophantine/cubic_squarecore_10000000.json`, `research/diophantine/cubic_search_validation.json`.

### q49

- **Purpose:** Exact resonance box verification.
- **Domain:** Every index2..1000000.
- **Generator:** q49_search.py
- **Permitted observations:** Squarefree kernel and exact root-sum comparisons.
- **Loss:** None: exact decision enumeration.
- **Seed:** Deterministic; no random seed.
- **Resource budget:** Fixed one-million endpoint; completed2.266855406s.
- **Controls:** Integer kernel factorization and direct original-equation substitution.
- **Uncertainty:** Box scope does not include all triples with bounded minimum index.

Artifacts: `research/root/q49_search.py`, `research/root/q49_search.json`.

### power_monoid

- **Purpose:** Exact bounded factorization-length classification.
- **Domain:** All65536 subsets of[0,16] containing0.
- **Generator:** power_monoid_search.py
- **Permitted observations:** All Minkowski decompositions within the maximum bound.
- **Loss:** None: exact dynamic programming.
- **Seed:** Deterministic; no random seed.
- **Resource budget:** Maximum16;229504 nonunit unordered factor pairs.
- **Controls:** Independent recursive ordinary-set verifier for seven displayed witnesses.
- **Uncertainty:** No exclusion of other length sets at larger maximum.

Artifacts: `research/squarefree_algebra/power_monoid_lengths_u32le.bin`, `research/squarefree_algebra/power_monoid_output.json`, `research/squarefree_algebra/verification_output.json`.

### q2316_rational

- **Purpose:** Find a rational witness and verify it exactly.
- **Domain:** Denominator2..30 and-100<=a<=100; stopped at first witness, denominator20.
- **Generator:** q2316_rational_search.py
- **Permitted observations:** Exact divisor identities and square checks.
- **Loss:** None: witness search.
- **Seed:** Deterministic; no random seed.
- **Resource budget:** Fixed small parameter caps.
- **Controls:** Separate Fraction substitution and Hensel residue witnesses at2 and5.
- **Uncertainty:** Not an exhaustive integer-point height search; not an integer witness.

Artifacts: `research/diophantine/q2316_rational_search.py`, `research/diophantine/q2316_rational_search.json`, `research/diophantine/q2316_checks.json`.

### q1511_repair

- **Purpose:** Verify the repaired infinite subcase via polynomial positivity plus exhaustive finite remainders.
- **Domain:** Eight specified gap polynomials with certified eventual thresholds and all smaller positive integer arguments.
- **Generator:** q1511_corrected_subcase.py
- **Permitted observations:** Exact coefficients, shifted sign certificates, square tests, factor power checks.
- **Loss:** None: exact certificate verification.
- **Seed:** Deterministic; no random seed.
- **Resource budget:** 27361 finite square tests,18 small-k and19 square-base cases.
- **Controls:** Exact polynomial identity and nonnegative shifted coefficients with positive constant terms.
- **Uncertainty:** Only y=3,5 with even z or square k; no full uniqueness theorem.

Artifacts: `research/diophantine/q1511_corrected_subcase.py`, `research/diophantine/q1511_corrected_subcase.json`.

The archive README gives the reproduction commands. The Paley certificate verifier uses only the Python standard library; candidate generation additionally uses NumPy and SciPy. The cubic search uses a C++17 compiler and unsigned128-bit arithmetic, with a separate arbitrary-precision Python control. The other verification scripts use standard Python. All displayed verification scripts ran successfully. The proof reviews and final check results are recorded in `research/root/review_record.json` and `research/root/verification_summary.json`.

The preserved exploratory C++ grid source is the final500-restart version. The two earlier120-restart output files remain raw observations from its earlier restart setting; their exact setting is declared in the experiment register. Heuristic rediscovery can depend on runtime and does not certify optimality. Reproducing the final mathematical lower bound requires only `rainbow_exact.py` and the independent integer checker.


## Part G. Complete exact-statement ledger

The retained statements below are copied byte-for-byte from the parsed attachment register. Source setup clarifies omitted domains without rewriting the retained wording. “Partial” records a specified consequence; **all48 exact-scope closure flags remain false**. Source-only subcases are identifiable by their evidence labels.

### Q49 — `d0a8503718ca529daf5a`

**Programme:** B2. **Title:** Retained statement.

**Exact retained statement:** Set F(n)=n(n−1)(n+2). Are there only finitely many integer triples n_(1),n_(2),n_(3)≥2 satisfying [F(n_(1))+F(n_(2))−F(n_(3))]^(2)=4F(n_(1))F(n_(2))?

**Status:** partial. **Exact-scope status:** unresolved. **Compiled formal theorem:** no.

**Results:** Common-squarefree-kernel reduction and elementary effective inequalities b<4F(a)/9 and c<a+b for sorted resonances. Exact exhaustion with all three indices in [2,1000000] gives only sorted triples (5,5,8) and (10,10,16). The cited source already treats minimum index<=10000 with other indices unbounded; the new box is a different domain.

**Changed assumptions / conclusion restriction:** All three indices<=1000000 for the finite exhaustion.

**Evidence:** written_argument, finite_computation, primary_source_comparison.

**Residual:** No argument bounds the minimum index of every resonance; global finiteness is unresolved.

**Auxiliary result IDs:** B2-R4.

### Q1312 — `7e21e2d207cc4fd014a3`

**Programme:** B2. **Title:** An abc bound sensitive to the number of prime factors.

**Exact retained statement:** For every ε>0, does some C_ε>0 satisfy c<C_ε H(abc)^{1+ε} for all coprime positive integers a, b, c with a+b=c?

**Status:** unresolved. **Exact-scope status:** unresolved. **Compiled formal theorem:** no.

**Results:** No new argument or computation at this exact scope was established in this work.

**Changed assumptions / conclusion restriction:** No replacement of the retained question is claimed; see any explicitly bounded or one-sided result above.

**Evidence:** No additional evidence beyond the supplied statement packet..

**Residual:** No exact closure established in this session.

### Q1509 — `ffda628de2bac43d0ec3`

**Programme:** B2. **Title:** Squarefree polynomial values.

**Exact retained statement:** For every separable f∈Z[x] of degree≥4 with no fixed prime-square divisor, is #{1≤n≤X:f(n) squarefree}∼X∏_{p prime}(1−ρ_f(p²)/p²)?

**Status:** partial. **Exact-scope status:** unresolved. **Compiled formal theorem:** no.

**Results:** Correct Euler-product squarefree asymptotics transfer to finite products of pairwise coprime separable factors. Unconditional factor-degree≤3 class; conditional imported quartic theorem expands cutoff to4.

**Changed assumptions / conclusion restriction:** Constituent factor asymptotics required; irreducible factors of degree≥5 remain unresolved.

**Evidence:** written_argument, primary_source_comparison.

**Residual:** A product-transfer theorem is proved. Factor degrees<=3 are unconditional using classical input. Factor degrees<=4 are conditional on the unverified imported quartic theorem; irreducible factors of degree>=5 remain outside this consequence.

**Auxiliary result IDs:** B2-A1, B2-SCOPE-020.

### Q1510 — `88eed316b86c7cab6b69`

**Programme:** B2. **Title:** Squarefree values at primes.

**Exact retained statement:** For every separable f∈Z[x] of degree≥4 with c_f>0, is N_f(X)∼c_f X/log X?

**Status:** partial. **Exact-scope status:** unresolved. **Compiled formal theorem:** no.

**Results:** Prime-argument constituent asymptotics transfer to finite products. Integer-argument asymptotic does not supply this hypothesis. Explicit f=x(x+1)(x²+1) is integer-admissible but has only prime argument2 yielding a squarefree value.

**Changed assumptions / conclusion restriction:** Constituent asymptotics must hold at prime arguments; the explicit example has prime local constant0 and is not a counterexample to retained statement.

**Evidence:** written_argument, primary_source_comparison, finite_computation.

**Residual:** Constituent prime-argument asymptotics are still required. Integer-argument statements do not supply them; general higher irreducible degrees remain unresolved.

**Auxiliary result IDs:** B2-A2.

### Q1511 — `0f88e5baee08af4d6f4f`

**Programme:** B2. **Title:** Terai’s Ramanujan–Nagell conjecture.

**Exact retained statement:** For every integer k>1, is (x,y,z)=(k−1,1,2) the only positive-integer solution of x²+(2k−1)^y=k^z?

**Source setup:** k>1 and x,y,z positive integers.

**Status:** partial. **Exact-scope status:** unresolved. **Compiled formal theorem:** no.

**Results:** No positive-integer solution exists when y is 3 or 5 and either z is even or k is a square. Repaired a false eventual-positivity threshold in source Lemma 2.3; verified all eight polynomial gap arguments and necessary small-base cases.

**Changed assumptions / conclusion restriction:** Proved subcase y in {3,5} and (z even or k a square); the full uniqueness conclusion is not asserted.

**Evidence:** written_argument, finite_computation, primary_source_comparison.

**Residual:** All other y, and y=3 or 5 with nonsquare k and odd z, remain outside the repaired partial theorem.

**Auxiliary result IDs:** B2-D5.

### Q1608 — `a2149a20f47eba9e27ee`

**Programme:** B2. **Title:** Higher-exponent plus equation.

**Exact retained statement:** Is (a^n+1)(b^n+1)=x² impossible for every n≥4?

**Source setup:** All variables positive integers; 1<=a<b.

**Status:** unresolved. **Exact-scope status:** unresolved. **Compiled formal theorem:** no.

**Results:** Primary source retains the full conjecture; its 4-divides-n theorem is correctly scoped. Diagonal a=b examples are inadmissible.

**Changed assumptions / conclusion restriction:** No replacement of the retained question is claimed; see any explicitly bounded or one-sided result above.

**Evidence:** primary_source_comparison.

**Residual:** No exact closure established in this session.

### Q1609 — `56c577fc2add1efcbecd`

**Programme:** B2. **Title:** Cubic plus equation.

**Exact retained statement:** Are the only solutions of (a³+1)(b³+1)=x² the triples (1,23,156), (6,26, 1953), and (20,362,616077)?

**Source setup:** All variables positive integers; 1<=a<b.

**Status:** partial. **Exact-scope status:** unresolved. **Compiled formal theorem:** no.

**Results:** The listed three triples are exactly all admissible solutions with b<=10000000.

**Changed assumptions / conclusion restriction:** Retained source setup 1<=a<b and positive x; additional finite bound b<=10000000.

**Evidence:** finite_computation, written_argument, primary_source_comparison.

**Residual:** All b>10000000 remain outside the exact search.

**Auxiliary result IDs:** B2-D4.

### Q1610 — `746ff7ed37b5c6eff82f`

**Programme:** B2. **Title:** Higher-exponent Cohn equation.

**Exact retained statement:** Is (a^n−1)(b^n−1)=x² impossible for every n≥5?

**Source setup:** All variables positive integers; 1<a<b.

**Status:** unresolved. **Exact-scope status:** unresolved. **Compiled formal theorem:** no.

**Results:** Primary source retains the full conjecture. Diagonal or a=1 examples are inadmissible.

**Changed assumptions / conclusion restriction:** No replacement of the retained question is claimed; see any explicitly bounded or one-sided result above.

**Evidence:** primary_source_comparison.

**Residual:** No exact closure established in this session.

### Q1611 — `77f199e22acb02c0e966`

**Programme:** B2. **Title:** Cubic Cohn equation.

**Exact retained statement:** Are the only solutions of (a³−1)(b³−1)=x² the triples (2,4,21), (2,22,273), (3,313,28236), and (4,22,819)?

**Source setup:** All variables positive integers; 1<a<b.

**Status:** partial. **Exact-scope status:** unresolved. **Compiled formal theorem:** no.

**Results:** The listed four triples are exactly all admissible solutions with b<=10000000.

**Changed assumptions / conclusion restriction:** Retained source setup 1<a<b and positive x; additional finite bound b<=10000000.

**Evidence:** finite_computation, written_argument, primary_source_comparison.

**Residual:** All b>10000000 remain outside the exact search.

**Auxiliary result IDs:** B2-D4.

### Q1612 — `4211038b2f8f58510864`

**Programme:** B2. **Title:** Bounded degree of split S-polynomials.

**Exact retained statement:** For every finite S, is there N(S) such that every S-polynomial f∈ℤ[x] splitting over ℚ has deg f≤N(S)?

**Status:** partial. **Exact-scope status:** unresolved. **Compiled formal theorem:** no.

**Results:** The checked primary source gives degree≤3 whenever2,3 are both absent from S.

**Changed assumptions / conclusion restriction:** Restrict S to finite prime sets excluding2 and3; this is a known source theorem, not a new proof.

**Evidence:** primary_source_comparison.

**Residual:** General finite S, especially those containing 2 or 3, remains unresolved. The reported degree<=3 subcase is a source result.

### Q1613 — `75f7fe19d171998305b3`

**Programme:** B2. **Title:** Prime-digit bound for split polynomials.

**Exact retained statement:** For every prime p, does a constant c(p) bound the number of nonzero base-p digits of deg(f)+1 whenever f∈ℤ[x] splits over ℚ and no coefficient is divisible by p? Can c(p)=p−1 always be used?

**Status:** partial. **Exact-scope status:** unresolved. **Compiled formal theorem:** no.

**Results:** Exact equivalence to split finite-field polynomials with all coefficients nonzero. If all roots reduce to the same nonzero class, deg(f)+1 has one nonzero digit; entire p=2 case follows. Primary-source comparison confirms reported p=3,5 cases.

**Changed assumptions / conclusion restriction:** One-root-class restriction for arbitrary primes; p=3,5 computations/proofs were not rerun locally.

**Evidence:** written_argument, primary_source_comparison.

**Residual:** General primes with more than one nonzero root residue class, and the proposed universal p-1 digit bound, are not proved.

**Auxiliary result IDs:** B2-A7.

### Q1860 — `1bbd790f1e916985ec31`

**Programme:** B2. **Title:** Settle the rainbow Schur density.

**Exact retained statement:** Is lim_(n→∞) Λ_(n,3)=9/22?

**Status:** unresolved. **Exact-scope status:** unresolved. **Compiled formal theorem:** no.

**Results:** Exploratory three-color interval/residue searches did not beat 9/22; no certificate of optimality was produced.

**Changed assumptions / conclusion restriction:** No replacement of the retained question is claimed; see any explicitly bounded or one-sided result above.

**Evidence:** finite_computation, primary_source_comparison.

**Residual:** The claimed limiting value 9/22 is neither proved nor disproved.

### Q1861 — `17b96fc493616f6da52c`

**Programme:** B2. **Title:** Find the four-colour Schur density.

**Exact retained statement:** Determine liminf_(n→∞) Λ_(n,4) and limsup_(n→∞) Λ_(n,4), including whether they coincide.

**Status:** partial. **Exact-scope status:** unresolved. **Compiled formal theorem:** no.

**Results:** Independently verified root-agent construction giving density50368/90905 by exact integer lattice counts at n=t·90905 for t=1,2,3,10,100; checked rectangle counting formula in2548 small cases. Proved liminf Lambda_(n,4)>=50368/90905 with an explicit nine-interval coloring. For all integers t>=1, R_(90905t)=2289351520t^2+25184t; an integer inclusion-exclusion identity certifies every scale.

**Changed assumptions / conclusion restriction:** No hypothesis restriction for the lower-bound theorem; only a one-sided conclusion from the retained determination problem is proved.

**Evidence:** finite_computation, written_argument, primary_source_comparison.

**Residual:** The exact liminf, limsup, and their equality remain unresolved; the cited upper bound 3/4 remains.

**Auxiliary result IDs:** B2-R1.

### Q1903 — `6f77af6017250e8f5f73`

**Programme:** B2. **Title:** Rational septuples.

**Exact retained statement:** Does a rational Diophantine septuple exist?

**Status:** unresolved. **Exact-scope status:** unresolved. **Compiled formal theorem:** no.

**Results:** Checked against Dujella's dated open-problem source; no construction or proof at the retained scope was established.

**Changed assumptions / conclusion restriction:** No replacement of the retained question is claimed; see any explicitly bounded or one-sided result above.

**Evidence:** primary_source_comparison.

**Residual:** No exact closure established in this session.

### Q1904 — `ffe6233da22c4944b875`

**Programme:** B2. **Title:** Two integral entries.

**Exact retained statement:** Does a rational Diophantine sextuple with at least two integer elements exist?

**Status:** unresolved. **Exact-scope status:** unresolved. **Compiled formal theorem:** no.

**Results:** Checked against Dujella's dated open-problem source; no construction or proof at the retained scope was established.

**Changed assumptions / conclusion restriction:** No replacement of the retained question is claimed; see any explicitly bounded or one-sided result above.

**Evidence:** primary_source_comparison.

**Residual:** No exact closure established in this session.

### Q1905 — `993c5519c53ce33a2045`

**Programme:** B2. **Title:** Strong rational quadruples.

**Exact retained statement:** Do four distinct nonzero rationals a₁,…,a₄ exist with a_i a_j+1 a rational square for every 1≤i,j≤4?

**Status:** unresolved. **Exact-scope status:** unresolved. **Compiled formal theorem:** no.

**Results:** Checked against Dujella's dated open-problem source; no construction or proof at the retained scope was established.

**Changed assumptions / conclusion restriction:** No replacement of the retained question is claimed; see any explicitly bounded or one-sided result above.

**Evidence:** primary_source_comparison.

**Residual:** No exact closure established in this session.

### Q1906 — `ecfc3848aae38321043a`

**Programme:** B2. **Title:** A Diophantine K₃,₃.

**Exact retained statement:** Do six distinct positive integers a₁,a₂,a₃,b₁,b₂,b₃ exist with a_i b_j+1 square for every i,j?

**Status:** unresolved. **Exact-scope status:** unresolved. **Compiled formal theorem:** no.

**Results:** Checked against Dujella's dated open-problem source; no construction or proof at the retained scope was established.

**Changed assumptions / conclusion restriction:** No replacement of the retained question is claimed; see any explicitly bounded or one-sided result above.

**Evidence:** primary_source_comparison.

**Residual:** No exact closure established in this session.

### Q1907 — `ef826ba72180d89f7c12`

**Programme:** B2. **Title:** Six positive integral solutions.

**Exact retained statement:** Do distinct positive integers a₁,a₂,a₃ exist such that ∏_{i=1}³(a_i x+1) is square for at least six positive integers x?

**Status:** unresolved. **Exact-scope status:** unresolved. **Compiled formal theorem:** no.

**Results:** Checked against Dujella's dated open-problem source; no construction or proof at the retained scope was established.

**Changed assumptions / conclusion restriction:** No replacement of the retained question is claimed; see any explicitly bounded or one-sided result above.

**Evidence:** primary_source_comparison.

**Residual:** No exact closure established in this session.

### Q1908 — `86bfeed53339e892c665`

**Programme:** B2. **Title:** Mixed-sign extension identity.

**Exact retained statement:** For every D(−1)-triple {a,b,c} and positive integer d with ad+1,bd+1,cd+1 squares, must (d+a+b−c)²=4(ab−1)(cd+1)?

**Status:** unresolved. **Exact-scope status:** unresolved. **Compiled formal theorem:** no.

**Results:** Checked against Dujella's dated open-problem source; no construction or proof at the retained scope was established.

**Changed assumptions / conclusion restriction:** No replacement of the retained question is claimed; see any explicitly bounded or one-sided result above.

**Evidence:** primary_source_comparison.

**Residual:** No exact closure established in this session.

### Q1959 — `65d0b4c5a86887c26fd5`

**Programme:** B2. **Title:** Bound projective-cube-free integer sets.

**Exact retained statement:** Is the maximum size of a 3-cube-free subset of {1,…,N} at most (2/3+o(1))N as N→∞?

**Status:** unresolved. **Exact-scope status:** unresolved. **Compiled formal theorem:** no.

**Results:** No new argument or computation at this exact scope was established in this work.

**Changed assumptions / conclusion restriction:** No replacement of the retained question is claimed; see any explicitly bounded or one-sided result above.

**Evidence:** No additional evidence beyond the supplied statement packet..

**Residual:** No exact closure established in this session.

### Q1960 — `5bcb37e9988a37da8cc3`

**Programme:** B2. **Title:** Bound projective-cube-free cyclic sets.

**Exact retained statement:** For all integers d≥2 and N divisible by d, must every d-cube-free A⊆Z/NZ satisfy |A|≤(d−1)N/d?

**Status:** unresolved. **Exact-scope status:** unresolved. **Compiled formal theorem:** no.

**Results:** No new argument or computation at this exact scope was established in this work.

**Changed assumptions / conclusion restriction:** No replacement of the retained question is claimed; see any explicitly bounded or one-sided result above.

**Evidence:** No additional evidence beyond the supplied statement packet..

**Residual:** No exact closure established in this session.

### Q1961 — `dfe8135fbdbcd3117dc4`

**Programme:** B2. **Title:** Prove the five-eighths projective-cube bound.

**Exact retained statement:** For every integer n≥3, must a projective-3-cube-free subset of Z/(2^n)Z have at most 5·2^(n−3) elements?

**Status:** unresolved. **Exact-scope status:** unresolved. **Compiled formal theorem:** no.

**Results:** No new argument or computation at this exact scope was established in this work.

**Changed assumptions / conclusion restriction:** No replacement of the retained question is claimed; see any explicitly bounded or one-sided result above.

**Evidence:** No additional evidence beyond the supplied statement packet..

**Residual:** No exact closure established in this session.

### Q2008 — `36753dcad26060a463f6`

**Programme:** B2. **Title:** Half-factorial class groups.

**Exact retained statement:** Is every abelian group isomorphic to the ideal class group of a half-factorial Dedekind domain?

**Status:** unresolved. **Exact-scope status:** unresolved. **Compiled formal theorem:** no.

**Results:** No new result in this lane.

**Changed assumptions / conclusion restriction:** None.

**Evidence:** scope_review.

**Residual:** No exact closure established in this session.

### Q2010 — `9413185b6a31098502e0`

**Programme:** B2. **Title:** Torsion forces exceptional units.

**Exact retained statement:** For prime N≥29, if E/K has a K-rational point of order N and N∤c(E/K), must M(K)≥(N−1)/2?

**Status:** unresolved. **Exact-scope status:** unresolved. **Compiled formal theorem:** no.

**Results:** No new result in this lane.

**Changed assumptions / conclusion restriction:** None.

**Evidence:** scope_review.

**Residual:** No exact closure established in this session.

### Q2011 — `910e657e85689a64c8c1`

**Programme:** B2. **Title:** Large sextic and septic unit cliques.

**Exact retained statement:** Are there only finitely many Q-isomorphism classes of fields K with [K:Q]∈{6,7} and M(K)>7?

**Status:** partial. **Exact-scope status:** unresolved. **Compiled formal theorem:** no.

**Results:** M(K)>7 forces no residue field of order≤7. Exact possible factorization types of2 are classified for degree6 and7; in degree7,2 must be unramified.

**Changed assumptions / conclusion restriction:** Necessary local restrictions only; no finiteness proof.

**Evidence:** written_argument.

**Residual:** Necessary residue-degree restrictions do not establish finiteness of the field isomorphism classes.

**Auxiliary result IDs:** B2-A8.

### Q2187 — `6a0c75d8af9af7e1c137`

**Programme:** B2. **Title:** Polylogarithmic Paley clique size.

**Exact retained statement:** Do absolute C,K>0 satisfy ω(G_p)≤C(log p)^K for every prime p≡1 mod 4?

**Status:** partial. **Exact-scope status:** unresolved. **Compiled formal theorem:** no.

**Results:** Global degree-two clique theta, even with entrywise nonnegativity, equals sqrt(p). All 29 eligible prime clique numbers p<=300 exactly certified. On the mean-zero space, the completed multiplicative-character basis is flat relative to nontrivial additive characters; exact-support uncertainty is vacuous for nonconstant rational functions, including centered indicators.

**Changed assumptions / conclusion restriction:** Finite computations restrict p to all primes <=300 congruent to 1 modulo 4.

**Evidence:** written_argument, finite_computation, primary_source_comparison.

**Residual:** The original asymptotic quantifiers are not established.

**Auxiliary result IDs:** B2-PAL-1, B2-PAL-4, B2-R3.

### Q2188 — `277f454289360bbd69ef`

**Programme:** B2. **Title:** Polynomial gain from degree-four SOS.

**Exact retained statement:** Does some ε>0 satisfy SOS₄(G_p)=O(p^{1/2−ε}) as p→∞ through primes p≡1 mod 4?

**Status:** partial. **Exact-scope status:** unresolved. **Compiled formal theorem:** no.

**Results:** Proved SOS4(G_p)<=1+theta(complement(L_p)), where L_p is the one-local residue graph. Ordinary one-local rational Fourier duals give certified finite SOS4 upper bounds for every eligible p<=300. On the mean-zero space, the completed multiplicative-character basis is flat relative to nontrivial additive characters; exact-support uncertainty is vacuous for nonconstant rational functions, including centered indicators.

**Changed assumptions / conclusion restriction:** Finite computations restrict p to all primes <=300 congruent to 1 modulo 4.

**Evidence:** written_argument, finite_computation, primary_source_comparison.

**Residual:** The original asymptotic quantifiers are not established.

**Auxiliary result IDs:** B2-PAL-2, B2-PAL-4, B2-R3.

### Q2189 — `b7cebb91447185f8bc65`

**Programme:** B2. **Title:** Infinitely many strict Schrijver improvements.

**Exact retained statement:** Are there infinitely many such p with 1+τ₊(H_p)<⌊(1+√(2p−1))/2⌋?

**Status:** partial. **Exact-scope status:** unresolved. **Compiled formal theorem:** no.

**Results:** Exactly p=61 and p=281 satisfy the strict inequality among eligible primes p<=300, with both directions certified. The two examples are already present numerically in the source and are not claimed new. On the mean-zero space, the completed multiplicative-character basis is flat relative to nontrivial additive characters; exact-support uncertainty is vacuous for nonconstant rational functions, including centered indicators.

**Changed assumptions / conclusion restriction:** Finite computations restrict p to all primes <=300 congruent to 1 modulo 4.

**Evidence:** written_argument, finite_computation, primary_source_comparison.

**Residual:** The original asymptotic quantifiers are not established.

**Auxiliary result IDs:** B2-PAL-4, B2-R3.

### Q2190 — `858e236a2a78c67c9b1f`

**Programme:** B2. **Title:** Two-localization beats the leading constant.

**Exact retained statement:** Does there exist ε>0 such that θ(H_p)≤(1/√2−ε)√p for all sufficiently large primes p≡1 mod 4?

**Status:** partial. **Exact-scope status:** unresolved. **Compiled formal theorem:** no.

**Results:** Rational theta dual upper bounds certified on all 29 eligible primes p<=300. After adding two and taking floors, 18/29 match the exact clique number and 21/29 improve the HP floor. On the mean-zero space, the completed multiplicative-character basis is flat relative to nontrivial additive characters; exact-support uncertainty is vacuous for nonconstant rational functions, including centered indicators.

**Changed assumptions / conclusion restriction:** Finite computations restrict p to all primes <=300 congruent to 1 modulo 4.

**Evidence:** written_argument, finite_computation, primary_source_comparison.

**Residual:** The original asymptotic quantifiers are not established.

**Auxiliary result IDs:** B2-PAL-4, B2-R3.

### Q2191 — `68bd7a5a8c3e1ff55f95`

**Programme:** B2. **Title:** Near-linear sparsity for the Paley frame.

**Exact retained statement:** Do absolute C,α>0 and 0<δ<√2−1 exist such that (1−δ)||x||₂²≤||Φ_px||₂²≤(1+δ)||x||₂² for every x supported on at most Cp/(log p)^α coordinates and all sufficiently large such p?

**Status:** partial. **Exact-scope status:** unresolved. **Compiled formal theorem:** no.

**Results:** Proved delta_k=(k-1)/sqrt(p) if and only if k<=omega(G_p)+1. For k>=omega+2, proved delta_k<=min(1,(k-4+sqrt(k^2+4k-12))/(2sqrt(p))). Fixed-delta Q2191 must be distinguished from polynomially decaying RIP and stronger quantitative profiles in Satake. On the mean-zero space, the completed multiplicative-character basis is flat relative to nontrivial additive characters; exact-support uncertainty is vacuous for nonconstant rational functions, including centered indicators.

**Changed assumptions / conclusion restriction:** The coherence-saturation and first-gap theorems hold for every eligible prime and finite support size. Computations restrict p<=300. No near-linear sparsity estimate is proved.

**Evidence:** written_argument, finite_computation, primary_source_comparison.

**Residual:** The original asymptotic quantifiers are not established.

**Auxiliary result IDs:** B2-PAL-3, B2-PAL-5, B2-R3.

### Q2203 — `f44a7194398e19780ec5`

**Programme:** B2. **Title:** Uniform color bounds for linear equations.

**Exact retained statement:** For every m≥1, does an integer r(m) exist such that every r(m)-regular E in m variables is regular?

**Status:** unresolved. **Exact-scope status:** unresolved. **Compiled formal theorem:** no.

**Results:** No new argument or computation at this exact scope was established in this work.

**Changed assumptions / conclusion restriction:** No replacement of the retained question is claimed; see any explicitly bounded or one-sided result above.

**Evidence:** No additional evidence beyond the supplied statement packet..

**Residual:** No exact closure established in this session.

### Q2210 — `be959fff2c1da528a958`

**Programme:** B2. **Title:** Realizing all finite factorization-length sets.

**Exact retained statement:** For every finite nonempty L⊆{2,3,…}, does some A∈P satisfy L(A)=L?

**Status:** partial. **Exact-scope status:** unresolved. **Compiled formal theorem:** no.

**Results:** Every singleton length set{k} realized by a base-three Boolean cube. Exact exhaustive search of all65536 sets containing0 in[0,16] gives seven displayed length-set witnesses, independently checked.

**Changed assumptions / conclusion restriction:** Universal claim restricted to singleton L; bounded computation does not rule out witnesses beyond maximum16.

**Evidence:** written_argument, finite_computation.

**Residual:** Arbitrary finite nonempty length sets remain unresolved; the exhaustive computation is restricted to sets in [0,16].

**Auxiliary result IDs:** B2-A6.

### Q2213 — `ca6484e601099abf0ee7`

**Programme:** B2. **Title:** Prescribed product-one subsequence threshold.

**Exact retained statement:** Is E(G)=d(G)+|G| for every finite nonabelian group G?

**Status:** partial. **Exact-scope status:** unresolved. **Compiled formal theorem:** no.

**Results:** Universal lower bound E(G)≥d(G)+|G| proved by adding |G|−1 identities to a product-one-free sequence.

**Changed assumptions / conclusion restriction:** Remaining universal direction is E(G)≤d(G)+|G|. This is a standard necessary bound.

**Evidence:** written_argument.

**Residual:** The reverse inequality E(G)<=d(G)+|G| remains the substantive universal target.

**Auxiliary result IDs:** B2-A9.

### Q2215 — `235fbd589621177ad36d`

**Programme:** B2. **Title:** Additive irreducibility near the squares.

**Exact retained statement:** If R⊆N satisfies |(R△Q)∩[1,X]|=o(√X) as X→∞, is it impossible to have R=A+B with A,B⊆N and |A|,|B|≥2?

**Status:** partial. **Exact-scope status:** unresolved. **Compiled formal theorem:** no.

**Results:** Any decomposition under the retained hypotheses has both summands infinite, A(X),B(X)=o(√X), liminf |(R\Q)∩[1,X]|/X^(1/4)≥1, and the stronger bound E(X)≫_η X^(1/3−η) for every η>0. Thus irreducibility holds for perturbations O(X^(1/3−δ)) for any fixed δ>0.

**Changed assumptions / conclusion restriction:** The full o(√X) perturbation class remains unresolved.

**Evidence:** written_argument.

**Residual:** The necessary error lower bound is X^(1/3-o(1)); it does not exclude every o(sqrt(X)) perturbation, nor every o(X^(1/3)) perturbation.

**Auxiliary result IDs:** B2-A3.

### Q2216 — `df34eaaa5ab7e530f259`

**Programme:** B2. **Title:** Uniform bipartite square-tuple bound.

**Exact retained statement:** Does an absolute C exist such that min(|A|,|B|)≤C for every ε∈{−1,1} and every pair with BD₂(ε)?

**Status:** unresolved. **Exact-scope status:** unresolved. **Compiled formal theorem:** no.

**Results:** No new result in this lane.

**Changed assumptions / conclusion restriction:** None.

**Evidence:** scope_review.

**Residual:** No exact closure established in this session.

### Q2217 — `19c8d772d81df73beca8`

**Programme:** B2. **Title:** Failure of almost atomicity in rank one.

**Exact retained statement:** Does a cancellative torsion-free commutative monoid M with rank-one Grothendieck group exist such that M is almost atomic but P_fin(M) is not?

**Status:** partial. **Exact-scope status:** unresolved. **Compiled formal theorem:** no.

**Results:** Any counterexample must be a proper Puiseux monoid with positive elements accumulating at0. Groups and monoids with positive lower gap have atomic power monoids.

**Changed assumptions / conclusion restriction:** Necessary restriction; no rank-one counterexample or ascent theorem for accumulating Puiseux monoids.

**Evidence:** written_argument, primary_source_comparison.

**Residual:** The case of a proper nonnegative rational monoid with positive elements accumulating at zero remains unresolved.

**Auxiliary result IDs:** B2-A10.

### Q2306 — `c8a9d6037b292fdf3b04`

**Programme:** B2. **Title:** Imaginary quadratic Diophantine quintuple.

**Exact retained statement:** Does some imaginary quadratic field K have a D(1)-quintuple in its ring of integers O_K?

**Status:** unresolved. **Exact-scope status:** unresolved. **Compiled formal theorem:** no.

**Results:** Checked against Dujella's dated open-problem source; no construction or proof at the retained scope was established.

**Changed assumptions / conclusion restriction:** No replacement of the retained question is claimed; see any explicitly bounded or one-sided result above.

**Evidence:** primary_source_comparison.

**Residual:** No exact closure established in this session.

### Q2307 — `388e074f811c33b3c869`

**Programme:** B2. **Title:** Rank four with maximal rational two-power torsion.

**Exact retained statement:** Does an elliptic curve E/Q exist with E(Q)_tors≅C₂×C₈ and rank E(Q)=4?

**Status:** unresolved. **Exact-scope status:** unresolved. **Compiled formal theorem:** no.

**Results:** Checked against Dujella's dated open-problem source; no construction or proof at the retained scope was established.

**Changed assumptions / conclusion restriction:** No replacement of the retained question is claimed; see any explicitly bounded or one-sided result above.

**Evidence:** primary_source_comparison.

**Residual:** No exact closure established in this session.

### Q2308 — `b97d79c1f4837f05055a`

**Programme:** B2. **Title:** Infinitely many rank-two C₂×C₈ curves.

**Exact retained statement:** Are there infinitely many elliptic curves E/Q with E(Q)_tors≅C₂×C₈ and rank E(Q)≥2?

**Status:** unresolved. **Exact-scope status:** unresolved. **Compiled formal theorem:** no.

**Results:** Checked against Dujella's dated open-problem source; no construction or proof at the retained scope was established.

**Changed assumptions / conclusion restriction:** No replacement of the retained question is claimed; see any explicitly bounded or one-sided result above.

**Evidence:** primary_source_comparison.

**Residual:** No exact closure established in this session.

### Q2309 — `c2919a57f718e86ebf52`

**Programme:** B2. **Title:** Six-torsion from an integral Diophantine triple.

**Exact retained statement:** Does a Diophantine triple {a,b,c} exist whose curve y²=(ax+1)(bx+1)(cx+1) has rational torsion group C₂×C₆?

**Status:** unresolved. **Exact-scope status:** unresolved. **Compiled formal theorem:** no.

**Results:** Checked against Dujella's dated open-problem source; no construction or proof at the retained scope was established.

**Changed assumptions / conclusion restriction:** No replacement of the retained question is claimed; see any explicitly bounded or one-sided result above.

**Evidence:** primary_source_comparison.

**Residual:** No exact closure established in this session.

### Q2314 — `5a4ccc40e698f43e2bbe`

**Programme:** B2. **Title:** Polynomial families for a cubic product equation.

**Exact retained statement:** Is {(x,y,z,t):xyz+t²+1=0} a finite union of polynomial families?

**Source setup:** All variables integers; each polynomial family is the image of Z^r under integer-coefficient polynomials, with finite r>=0.

**Status:** partial. **Exact-scope status:** unresolved. **Compiled formal theorem:** no.

**Results:** Constructed a Zariski-dense integer polynomial family with three parameters; gave an exact integer solution outside it and every sign/permutation copy. This is a limitation of that family, not a disproof of finite polynomial parametrization.

**Changed assumptions / conclusion restriction:** One explicit polynomial family and its sign/permutation copies are studied, not every possible finite union.

**Evidence:** written_argument, finite_computation, primary_source_comparison.

**Residual:** The displayed dense family and its symmetries are incomplete; a different finite union of polynomial families is neither constructed nor excluded.

**Auxiliary result IDs:** B2-D3.

### Q2315 — `fe5ce4fae3105179737a`

**Programme:** B2. **Title:** A nonzero point on a small ternary quartic.

**Exact retained statement:** Does x⁴+x³y−y⁴+y³z+z⁴=0 have a solution (x,y,z)≠(0,0,0)?

**Source setup:** All variables integers.

**Status:** partial. **Exact-scope status:** unresolved. **Compiled formal theorem:** no.

**Results:** The projective quartic is smooth of genus 3 over Q and has a real point and a primitive Z_p point for every prime p. Therefore no finite modulus supplies a primitive local obstruction. Global nonzero integer existence remains unresolved.

**Changed assumptions / conclusion restriction:** The proved solvability statement is over R and every Z_p, not over Z or Q.

**Evidence:** written_argument, finite_computation, primary_source_comparison.

**Residual:** Everywhere local solubility is proved; a nonzero rational/projective point, equivalently nonzero integer point, is not supplied.

**Auxiliary result IDs:** B2-D1.

### Q2316 — `210ee10d0d0097b4ee16`

**Programme:** B2. **Title:** Integral solvability of a symmetric cubic.

**Exact retained statement:** Does x³+x+y³+y+z³+z=xyz+1 have an integer solution?

**Source setup:** All variables integers.

**Status:** partial. **Exact-scope status:** unresolved. **Compiled formal theorem:** no.

**Results:** Found exact rational point (-13/20,-79/20,21/5), proved Z_p-solubility for every prime, and ruled out any integer coordinate 0 or +/-1. Integer existence remains unresolved.

**Changed assumptions / conclusion restriction:** The explicit global point is rational; the proved integral solvability is over each Z_p separately.

**Evidence:** written_argument, finite_computation, primary_source_comparison.

**Residual:** The rational point and every-p-adic integral points do not supply an integer point.

**Auxiliary result IDs:** B2-D2.

### Q2414 (provisional) — `fbf539f5a7f03f1da075`

**Programme:** B2. **Title:** Nicol’s cyclotomic-sum irreducibility.

**Exact retained statement:** For every n,m>1, is the non-cyclotomic part of Φ_n(x)+Φ_m(x) either 2 or irreducible?

**Status:** partial. **Exact-scope status:** unresolved. **Compiled formal theorem:** no.

**Results:** For n=2^r,m=2^s with r,s≥1, equal indices leave2 and unequal indices give an irreducible entire sum.

**Changed assumptions / conclusion restriction:** Both indices restricted to powers of2; numbering provisional.

**Evidence:** written_argument, primary_source_comparison, finite_computation.

**Residual:** Indices not both powers of two remain outside the proved subfamily.

**Auxiliary result IDs:** B2-A4.

### Q2415 (provisional) — `a06b211ca02e3eb359fa`

**Programme:** B2. **Title:** Cyclotomic product plus one.

**Exact retained statement:** For every n,m>1, is the non-cyclotomic part of Φ_n(x)Φ_m(x)+1 irreducible?

**Status:** partial. **Exact-scope status:** unresolved. **Compiled formal theorem:** no.

**Results:** For n=m=2^r, r≥1, the polynomial is Eisenstein at2 and therefore irreducible.

**Changed assumptions / conclusion restriction:** Equal indices restricted to powers of2; numbering provisional.

**Evidence:** written_argument, primary_source_comparison, finite_computation.

**Residual:** Pairs other than equal powers of two remain outside the proved subfamily.

**Auxiliary result IDs:** B2-A5.

### Q2462 (provisional) — `ab65e680b82754944885`

**Programme:** B2. **Title:** Evaluate nondegenerate limiting densities.

**Exact retained statement:** If no nonempty subset of the coefficients sums to zero, determine lim_(ε↓0)d(L,ε).

**Status:** partial. **Exact-scope status:** unresolved. **Compiled formal theorem:** no.

**Results:** For every fixed k>=3 and nonzero integer c, the equation c(x1+...+xk)=0 satisfies d(L,epsilon)=1/k for every fixed epsilon>0. The general epsilon-down-to-zero limit exists by monotonicity; its value for arbitrary nondegenerate coefficients remains unresolved.

**Changed assumptions / conclusion restriction:** All coefficients equal one fixed nonzero integer c for the evaluated density.

**Evidence:** written_argument, primary_source_comparison.

**Residual:** Arbitrary nondegenerate integer coefficient tuples are not evaluated.

**Auxiliary result IDs:** B2-R2.

### Q2468 (provisional) — `3529c68ac8a3205e8a47`

**Programme:** B2. **Title:** Determine the Schur chromatic threshold.

**Exact retained statement:** What is the exact value of δχ?

**Status:** unresolved. **Exact-scope status:** unresolved. **Compiled formal theorem:** no.

**Results:** Primary-source qualitative threshold classification does not give the exact Schur threshold. Small Cayley independence number and unbounded Cayley chromatic number are distinct constraints; fixed integer scalar multiplication alone does not introduce a second independent group law.

**Changed assumptions / conclusion restriction:** No replacement of the retained question is claimed; see any explicitly bounded or one-sided result above.

**Evidence:** written_argument, primary_source_comparison.

**Residual:** No new exact value or quantitative bound for the retained Schur chromatic threshold is established.

### Q2469 (provisional) — `d4554ad68bb1d9e77596`

**Programme:** B2. **Title:** Strength of inhomogeneous ring regularity.

**Exact retained statement:** What is the reverse-mathematical strength over RCA₀ of the assertion: for every commutative ring R, finite m×n matrix A over R and nonzero b∈R^m, if Ax=b has no constant solution, some finite coloring of R has no monochromatic solution?

**Status:** partial. **Exact-scope status:** unresolved. **Compiled formal theorem:** no.

**Results:** WKL0 proves the retained ring-coloring assertion over RCA0, with at most [3(n-1)]^(n-1) colors for n>=2 and one color for n<=1. A finite-presentation construction avoids comprehension of the range sR; supplied finite integer matrices are diagonalized by an explicit primitive-recursive algorithm. Every PA degree relative to the input can compute a witnessing coloring.

**Changed assumptions / conclusion restriction:** Countable coded commutative rings, as required for the retained second-order arithmetic statement; no additional ring hypothesis. Only an upper bound on logical strength is proved.

**Evidence:** written_argument, primary_source_comparison.

**Residual:** No WKL0 reversal, lower bound on the optimal color count, or exact reverse-mathematical classification is proved.

**Auxiliary result IDs:** B2-R5.


## Part H. Remaining decisive targets and evidence boundaries

The report establishes more than the packet's requested minimum of one justified transfer or precise nontransfer. It does not support treating the48 questions as one reducible problem. The following are the most concrete remaining mathematical targets suggested by the completed work.

1. **Four-colour Schur density:** improve or bound the explicit interval construction with an upper certificate for a clearly specified class, then identify whether residue dependence can beat that class. The exact nine-interval count supplies a reproducible benchmark. A heuristic stationary point is not an upper certificate, and an interval-class optimum would not by itself be the full extremal theorem.
2. **Provisional Q2462, stable ID `ab65e680b82754944885`:** treat a first genuinely unequal coefficient family. The equal-coefficient upper proof depends on symmetry of the restricted sum; arbitrary coefficients destroy that Vandermonde coefficient simplification. The construction side must keep Cayley independence sublinear while avoiding the weighted equation.
3. **Provisional Q2469, stable ID `d4554ad68bb1d9e77596`:** build a reversal respecting the permission to use any finite number of colours, or prove the assertion in a weaker system. Optimal two-colouring or an added monochromatic-cyclic-subgroup condition would be a different statement. The finite-presentation construction already handles the upper bound, so a quotient-range argument requiring ACA₀ is no longer the right obstacle.
4. **Paley:** use constraints that exclude the explicit global degree-two feasible point. The one-local ordinary theta inequality is a valid route to SOS₄, but Schrijver positivity and two-local theta cannot be silently substituted. Infinite families and uniform rates remain the required next step after the certified finite table.
5. **Q2215:** improve the square-sum incidence estimate beyond the divisor-controlled pairwise common-neighbor bound. The current exponent1/3 follows transparently from m≈√X and m≲E^(3/2)X^o(1). Reaching the retained o(√X) regime needs additional structure.
6. **Q2315 and Q2316:** investigate global arithmetic. No finite modulus can settle nonexistence, because every modulus is already proved soluble. For the cubic, the divisor reformulation gives a structured exact search; for the quartic, the local proof identifies the smooth projective genus-three setting. A rational point for the quartic or an integer point for the cubic would be decisive.
7. **Q1509–Q1510:** audit an actual proof of the imported quartic theorem before treating the conditional factor-degree4 class as unconditional. The comparator statement stub is insufficient. Integer and prime arguments remain distinct; their product transfers require the corresponding constituent theorem.

### Evidence and authority

The input packet's historical collector notes, the present exact-ID conclusions, and the unverified imported result claims remain separate. Every formula reported as a finite classification has a stated domain. The report does not infer global nonexistence from a negative search, infinitude from a prime table, or a compiled formal theorem from a successful arithmetic script.

No authoritative catalog or prior programme record was edited. The five recovery-draft question numbers remain provisional and retain their stable IDs. The accompanying ledger is a research return for reconciliation, not an assertion that the original register has been updated.

**Input SHA-256:** `1b2874d545cb8c4a89d721dc5a86353a2f7d3263919a10d8fe3585741166a307`.
