# B7 — Invariant completeness: research return

Research date: **7 October 2026**. This return follows the attached 48-question B7 handoff and its exact-statement evidence policy.

## 1. Outcomes and decision summary

This work supplies complete written proofs for **three previously unclosed retained statements: Q17, Q739 and Q1749**. It also supplies precisely scoped partial results for eleven other questions, a stability obstruction attached to the two previously accepted mixture-identification results, and a verified failure of one proposed spectral-to-homometric encoding.

The proposed exact-statement ledger now has **5 proved entries, including the 2 accepted in the input; 11 partial entries; and 32 unresolved entries**. “Proved” for the three new results means a complete mathematical argument with its dependencies and relevant exact certificates supplied here. It does not mean external peer review, publication priority, a proof-assistant kernel pass, or that the original catalog has already accepted this return. No external catalog was modified.

| Question | Principal result in this return | Exact-statement decision |
|---|---|---|
| Q17 | The stronger divisor \((n-1)(2^{k-1}-1)\) works for every tree and every integer \(k\ge2\). | Proved, new written proof |
| Q739 | Every bivariate Gaussian secant has the expected dimension, for all \(d\ge2,k\ge1\). | Proved, new written proof |
| Q1749 | Unique Gaussian Gabor signals are comeagre for \(ab<1\), nonempty nowhere dense for \(ab=1\), and absent for \(ab>1\). At critical density an exact coefficient criterion is proved. | Proved, new written proof |
| Q1766 | \(13\le\operatorname{edim}_m(Q_6)\le15\), combining an elementary bound and complete finite exclusions. | Partial |
| Q740 | The conjectured defect is a universal lower bound; equality is certified at \(n=8,k=11\); an explicit positive real ambiguity family is given. | Partial |
| Q741 | Generic Gauss finiteness in every degree \(d\ge5\), plus all-fiber finiteness on the smooth coprime parameter image. | Partial: exceptional smooth loci remain |
| Q1001–Q1002 | A real diagonal-tensor uniqueness criterion; finite determination for each fixed cumulant sequence; no uniform cumulant cutoff. | Partial for both classifications |
| Q1156–Q1157 | Complete constructive one-dimensional subcases. | Partial |
| Q608–Q609, Q611 | Calibration and thinning, a hard-pair embedding theorem, and interior-grid lower-bound transfer. | Partial: Family 122 premises remain unverified |
| Q613 | An exact retention-independent Bayes rule and full average-case enumeration through \(n=8\). | Partial: asymptotic and worst-case targets remain |
| Q738, Q742 | Accepted identifiability decisions retained; a new near-collision stability obstruction covers all three families. | Proved as imported; no re-audit |
| Spectral transfer | A classical isospectral lens pair has nonhomometric signed weight sets, with a full-spectrum certificate. | Disproves this encoding implication; no original spectral question closed |

The strongest results concern three different meanings of completeness. Q17 is an integral resultant statement; Q739 is a dimension statement and does not imply uniqueness; Q1749 is global uniqueness modulo phase and a norm-topological category classification. The ledger preserves those distinctions rather than treating them as one generic notion of identifiability.

### Evidence labels

**Written argument** means the all-parameter proof appears in this report and in its working source. **Primary-source comparison** identifies the precise definitions or published theorem used. **Finite computation** means exact inputs, code, outputs, and declared domains are in the archive. **Compiled formal theorem** is false throughout this return. The accessible Family 122 comparator contains theorem placeholders; that observation neither validates nor refutes the separate underlying theorem.

### How to use the deliverables

The report contains the mathematical arguments and all 48 exact retained statements. The JSON ledger contains one structured entry per stable statement, result-to-question links, changed assumptions, remaining work, and evidence types. The verification ZIP contains this report, the ledger, the supplied handoff, all working proof notes, every cited script, exact certificates, raw computation logs, the source comparison catalog, a replay entry point, and a SHA-256 file manifest.

Run the default exact checks after extracting the archive:

~~~bash
python b7_work/reproduce.py
~~~

To additionally rebuild and repeat every complete six-cube exclusion:

~~~bash
python b7_work/reproduce.py --full-cube
~~~

The default run rechecks exact finite certificates and audits the archived completed cube logs; it does not redo the billions of cube candidates. The complete option does. Python 3.10 or newer and NumPy suffice for the default computations; the complete cube replay also requires a C++17 compiler named g++. Time limits are explicit and a timeout is treated as a failure. See the archive README for further details.

## 2. All 48 exact-statement decisions

“Unresolved” means this return supplies no full solution. For unworked entries it is not a new claim about the entire literature as of the research date. The two accepted results retain the authority and scope assigned by the supplied handoff.

| Question | Stable statement ID | Decision | Result or remaining issue |
|---|---|---|---|
| Q17 | `3e7e1834fd713fe73a83` | proved — new written proof | Stronger divisor for every tree and every order k>=2. |
| Q20 | `9ba5075d118c04918d6d` | unresolved | No new analysis or status promotion in this return. |
| Q101 | `06c3626cd7abe261f06c` | unresolved | No new analysis or status promotion in this return. |
| Q169 | `2db69aae8c225ff910dd` | unresolved | No new analysis or status promotion in this return. |
| Q337 | `3f57476cd8727d99a539` | unresolved | No new analysis or status promotion in this return. |
| Q400 | `c406d4b9e0c3a2b80408` | unresolved | No new analysis or status promotion in this return. |
| Q607 | `2ebcfe72585b1be70fc9` | unresolved | Exact-model comparator audited; underlying Family 122 proof remains unverified. |
| Q608 | `16cdc05113faa8ab347d` | partial | Rational-to-real retention reduction, now with constant-factor sample overhead. |
| Q609 | `9144c2582d1e2c9c3b3a` | partial | Hard-pair embedding proves a conditional negative consequence; premise unverified. |
| Q610 | `8a00508df67e6fbcd058` | unresolved | No new result for insertion/deletion accuracy and runtime. |
| Q611 | `472e43724c08d9837feb` | partial | Two-point emission reduction, including an interior grid pair; minimax rate remains. |
| Q612 | `4c25b9b7f68a9602ba33` | unresolved | No new result for unlabeled population recovery. |
| Q613 | `c302289d6bd6215ff58d` | partial | Exact Bayes formula and complete finite computation through n=8; asymptotics remain. |
| Q738 | `2f577a87fee1b2c95e2d` | proved — imported accepted | Imported accepted generic identification; new collision-stability obstruction. |
| Q739 | `3e3c622525036c1e9a43` | proved — new written proof | Full nondefectivity formula for every d>=2,k>=1. |
| Q740 | `b69755d99b945371b6be` | partial | Universal defect lower bound, exact n=8,k=11 dimension, positive real ambiguity family. |
| Q741 | `f344e3bf779aac637144` | partial | Generic Gauss finiteness in every degree; full smooth-locus fibers remain. |
| Q742 | `c069b7ff6ff08382c685` | proved — imported accepted | Imported accepted result for both families; new collision-stability obstruction. |
| Q997 | `8bdda54c021f80a96ef9` | unresolved | No new analysis or status promotion in this return. |
| Q1001 | `93986607a1f5ccc79b75` | partial | Explicit sufficient criterion for real even-order diagonal tensors. |
| Q1002 | `ddcccae3e3f4fb404ca2` | partial | Finite cutoff for each fixed source; no uniform cutoff, with exact examples. |
| Q1156 | `48ec50411ade2c1537dd` | partial | Complete constructive line subcase. |
| Q1157 | `cc68108ee4fc5b3d3ebc` | partial | Complete line criterion via rational linear feasibility. |
| Q1324 | `b17e6d3142710d3c0f68` | unresolved | No new analysis or status promotion in this return. |
| Q1456 | `2dd40c2f94424a87477d` | unresolved | No new analysis or status promotion in this return. |
| Q1457 | `b40e30bbf175d35162cb` | unresolved | No new analysis or status promotion in this return. |
| Q1458 | `d7fe39dcb9bb210db7fa` | unresolved | No new analysis or status promotion in this return. |
| Q1498 | `01c8355b5e7fc5532a9c` | unresolved | No new analysis or status promotion in this return. |
| Q1593 | `ec5863144b957427d69c` | unresolved | No new analysis or status promotion in this return. |
| Q1749 | `0c0478553c79951846b2` | proved — new written proof | Full category trichotomy and exact critical uniqueness criterion. |
| Q1766 | `84f1767e6fac27a1ca5e` | partial | Computer-assisted interval narrowed to 13–15; exact value remains. |
| Q2025 | `35437229265179fdf70c` | unresolved | Lens-to-homometry experiment has dimension five: scope-nonmatch. |
| Q2032 | `d54894e53caf916054e2` | unresolved | Experiment uses isomorphic cyclic groups: scope-nonmatch. |
| Q2033 | `73618fc79466096402ed` | unresolved | No new analysis or status promotion in this return. |
| Q2034 | `53728349aebd91e7cfc3` | unresolved | No new analysis or status promotion in this return. |
| Q2092 | `c78457588025ba2dcd4d` | unresolved | No new analysis or status promotion in this return. |
| Q2105 | `ed3c15822967f6534d5b` | unresolved | No new analysis or status promotion in this return. |
| Q2106 | `790cf230288fb810afad` | unresolved | No new analysis or status promotion in this return. |
| Q2107 | `91432fe0cb2d0ad759e1` | unresolved | No new analysis or status promotion in this return. |
| Q2108 | `9e1bb75af8f94aaea2d7` | unresolved | No new analysis or status promotion in this return. |
| Q2109 | `783798519c45eea8a7ab` | unresolved | No new analysis or status promotion in this return. |
| Q2123 | `7ecf710a682d6bfc2410` | unresolved | No new analysis or status promotion in this return. |
| Q2134 | `d7d72638df3bb1201dc2` | unresolved | Experiment gives no all-dimensional maximum-volume result: scope-nonmatch. |
| Q2159 | `253959e9e3fc2bc95cf7` | unresolved | No new analysis or status promotion in this return. |
| Q2211 | `a0c7ab5838fac12c9329` | unresolved | No new analysis or status promotion in this return. |
| Q2350 | `1cd1a29825c43e7714d6` | unresolved | No new analysis or status promotion in this return. |
| Q2364 | `6f31e42a6bb668cb8904` | unresolved | No new analysis or status promotion in this return. |
| Q2483 (provisional) | `952a31b8ef8e3b9b0e60` | unresolved | Provisional number, stable ID 952a31b8ef8e3b9b0e60; no new result. |


## 3. Q17 — the integral tree-resultant proof

**B7 / Q17 / stable ID `3e7e1834fd713fe73a83`.** Exact retained statement:

> For a tree T and even k≥2, form D_(k)(T) with entry indexed by (v_(1),…,v_(k)) equal to the edge-count of the smallest subtree containing those vertices. Does 2^(k−1)−1 always divide its symmetric hyperdeterminant?

Stable statement ID: `3e7e1834fd713fe73a83`.

Exact retained statement: For a tree T and even k≥2, form D_(k)(T) with entry indexed by (v_(1),…,v_(k)) equal to the edge-count of the smallest subtree containing those vertices. Does 2^(k−1)−1 always divide its symmetric hyperdeterminant?

**Result: proved by a written argument.** The stronger integer
\((n-1)(2^{k-1}-1)\) divides the hyperdeterminant for every tree on \(n\ge2\) vertices and every integer \(k\ge2\), including odd orders. The one-vertex tensor has determinant zero, so the retained question holds there too. No tree-independence theorem is needed.

### Convention and primary-source comparison

Use the normalized homogeneous resultant convention
\[
\det D_{(k)}(T)=\operatorname{Res}(F_1,\ldots,F_n),\qquad
F_v(x)=\sum_{i_2,\ldots,i_k}D_{v,i_2,\ldots,i_k}x_{i_2}\cdots x_{i_k}.
\]
The resultant of \(x_1^d,\ldots,x_n^d\) is one, with \(d=k-1\). This is exactly the convention in Ya-Nan Zheng, *On the Hyperdeterminants of Steiner Distance Hypermatrices*, Electronic Journal of Combinatorics 32(2), P2.30 (2025), Theorem 2 and the paragraph following it, printed pp. 2–3; equation (1), p. 4. Its Theorem 4 supplies the resultant composition law. Source: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v32i2p30/pdf/ ; DOI https://doi.org/10.37236/13741.

Cooper–Du, *Determinants of Steiner Distance Hypermatrices*, arXiv:2505.10501v1, §1, uses the same tensor equations. Its tree-independence result is compatible with, but not a dependency of, the proof below. Source: https://arxiv.org/html/2505.10501v1 . The dissertation's exact Conjecture 4 wording is supplied by the handoff; its full PDF was not retrievable in this run.

### Lemma 1: an integral resultant divisibility certificate

Let \(F_1,\ldots,F_n\in\mathbb Z[x_1,\ldots,x_n]\) be homogeneous of the same positive degree \(d\). Let \(a\in\mathbb Z^n\) have a coordinate equal to 1. If an integer \(c\) divides every \(F_i(a)\), then
\[
c\mid\operatorname{Res}(F_1,\ldots,F_n).
\]
For \(c=0\), interpret the assertion as: all \(F_i(a)=0\) imply the resultant is zero.

**Proof.** Relabel coordinates so \(a_n=1\), and let \(U\in\operatorname{GL}_n(\mathbb Z)\) have its first \(n-1\) columns equal to the corresponding standard basis vectors and its last column equal to \(a\). Its determinant is one. Set \(G_i(y)=F_i(Uy)\). The coefficient of \(y_n^d\) in \(G_i\) equals \(F_i(a)\).

In the universal integral coefficient ring, put every coefficient of \(y_n^d\) equal to zero. All resulting forms vanish at \(e_n\), so their universal resultant specializes to the zero polynomial. To justify this integrally, evaluate all remaining coefficients arbitrarily over \(\mathbb C\); the common root \(e_n\) forces the specialized polynomial to vanish for every such evaluation. A polynomial over \(\mathbb Z\) which vanishes identically over \(\mathbb C\) has all coefficients zero. Thus the universal resultant belongs to the ideal generated by those \(n\) distinguished coefficients. After substituting the actual coefficients of \(G_i\), its value is a multiple of \(c\). Finally,
\[
\operatorname{Res}(F_1\circ U,\ldots,F_n\circ U)
=\det(U)^{d^n}\operatorname{Res}(F_1,\ldots,F_n)
=\operatorname{Res}(F_1,\ldots,F_n).
\]
Coordinate relabeling can introduce only a sign. This proves divisibility by the full integer \(c\), including its prime powers; merely exhibiting roots modulo each prime would not suffice. ∎

### Lemma 2: the tree charge has unit mass on either side of every edge

Put \(a_v=2-\deg_T(v)\). Then
\[
\sum_{v\in V(T)}a_v=2.
\]
If deleting an edge gives vertex sets \(A,B\), then
\[
\sum_{v\in A}a_v=\sum_{v\in B}a_v=1.
\]

**Proof.** The full degree sum is \(2(n-1)\). Inside a component \(A\) of the edge-deleted tree, there are \(|A|-1\) internal edges and exactly one edge leaving \(A\). Consequently \(\sum_{v\in A}\deg_T(v)=2(|A|-1)+1=2|A|-1\). Subtracting this from \(2|A|\) gives one. ∎

### Lemma 3: direct evaluation of the tensor equations

For an edge \(e\) and a vertex \(v\), write \(C_e(v)\) for the component of \(T-e\) containing \(v\), and write \(S(x)=\sum_vx_v\). Then
\[
F_v(x)=\sum_{e\in E(T)}\left[S(x)^d-
\left(\sum_{u\in C_e(v)}x_u\right)^d\right].
\]

**Proof.** An edge \(e\) belongs to the minimal subtree spanning \(v,i_2,\ldots,i_k\) precisely when at least one of \(i_2,\ldots,i_k\) lies outside \(C_e(v)\). Summing the corresponding monomial over all ordered \(d\)-tuples gives the displayed difference. Summing over edges counts exactly the subtree's edge number. ∎

At the integer vector of Lemma 2, every bracket equals \(2^d-1\). Therefore
\[
F_v(a)=(n-1)(2^d-1)\quad\text{for every }v.
\]
Every tree with at least two vertices has a leaf, and its coordinate in \(a\) is one. Lemma 1 now proves the theorem. ∎

### Weighted extension

If each edge has an integer weight \(w_e\) and tensor entries are the sums of weights on the unique spanning subtree, the same proof gives
\[
\left(2^{k-1}-1\right)\sum_e w_e\ \mid\ \det D_{(k),w}(T).
\]
If the sum of weights is zero, the tensor equations have the nonzero common root \(a\), so the determinant is zero. This extension changes the model and is supplementary to Q17.

### Evidence boundary

The all-tree, all-order conclusion follows from the written proof. Exact finite checks of the tree-charge identity and tensor contraction, and small exact resultant controls, are supporting computations only. No proof-assistant theorem has been compiled. No claim of first publication is made.


## 4. Q739 — every bivariate Gaussian secant has expected dimension

**B7 / Q739 / stable ID `3e3c622525036c1e9a43`.** Exact retained statement:

> For every d≥2,k≥1, is dim Sec_k(G_{2,d})=min{binom(d+2,2)−1,6k−1}?

Date: 2026-10-07. Stable statement ID: `3e3c622525036c1e9a43`.

### Theorem

For every integer `d>=2` and `k>=1`, over the complex numbers,

\[
\boxed{\dim\operatorname{Sec}_k(G_{2,d})
=\min\!\left\{\binom{d+2}{2}-1,\ 6k-1\right\}.}
\tag{Q739}
\]

The proof reduces the general case to the established interpolation theorem for triple points in the projective plane. Three exceptional interpolation cases are repaired by explicit integer Gaussian tangent matrices with nonzero maximal minors. The exact code, matrices, parameters, selected minors, and determinants are supplied in this folder.

This is a full proof of the **dimension** target. It establishes generic finite fibers when parameter dimension is at most the ambient moment dimension. It does not assert generic uniqueness, characterize every exceptional mixture, or give a stable statistical recovery procedure.

### 1. Conventions and smoothness of the affine Gaussian chart

Write a bivariate Gaussian parameter as

\[
(u,v,a,b,c),\qquad
\mu=(u,v),\qquad
\Sigma=\begin{pmatrix}a&b\\b&c\end{pmatrix}.
\]

Let `m_ij=E[X^i Y^j]` be the ordinary, unscaled moments, including `m_00=1`. The moment-generating series is

\[
\exp\!\left(ux+vy+\tfrac12a x^2+bxy+\tfrac12c y^2\right)
=\sum_{i,j\ge0}\frac{m_{ij}}{i!j!}x^iy^j.
\tag{1}
\]

The point of `G_{2,d}` is `[m_ij]_{i+j<=d}`. The first five nonconstant coordinates recover the five component parameters polynomially:

\[
u=m_{10},\quad v=m_{01},\quad
a=m_{20}-u^2,\quad b=m_{11}-uv,\quad c=m_{02}-v^2.
\tag{2}
\]

Every higher moment is polynomial in these five parameters. Hence the chart `m_00=1` is a closed polynomial graph isomorphic to `A^5`, so every finite Gaussian parameter point, including zero covariance, is smooth. The affine cone chart with nonzero `m_00` is correspondingly smooth of dimension 6.

For `d=2`, (2) proves `G_{2,2}=P^5`, so the assertion is immediate for every `k`.

### 2. The tangent matrix equals triple-point interpolation at zero covariance

Differentiating (1) gives

\[
\begin{aligned}
\partial_u m_{ij}&=i m_{i-1,j},&
\partial_v m_{ij}&=j m_{i,j-1},\\
\partial_a m_{ij}&=\binom i2 m_{i-2,j},&
\partial_b m_{ij}&=ij m_{i-1,j-1},&
\partial_c m_{ij}&=\binom j2 m_{i,j-2}.
\end{aligned}
\tag{3}
\]

Terms with negative subscripts are zero. The six tangent columns of the affine cone at a component are the moment vector itself and its five parameter derivatives. At covariance zero, `m_ij=u^i v^j`; consequently those six columns are the transpose of evaluation of

\[
P,\ P_x,\ P_y,\ \tfrac12P_{xx},\ P_{xy},\ \tfrac12P_{yy}
\tag{4}
\]

at `(u,v)`, for polynomials `P(x,y)` of total degree at most `d`.

For `k` distinct general means, the kernel of the transpose tangent matrix therefore consists exactly of degree-at-most-`d` polynomials vanishing to multiplicity at least 3 at the means. Homogenization identifies this space with degree-`d` plane curves through `k` general triple points. Taking means in the affine chart is harmless: the chart is dense, and maximal rank is an open condition.

Thus, whenever general triple points have their expected postulation, the tangent matrix has rank

\[
\min\left\{\binom{d+2}{2},6k\right\}.
\tag{5}
\]

A full-rank tangent matrix at these special smooth Gaussian points supplies a nonzero polynomial minor. That minor remains nonzero at general Gaussian parameters. Terracini's lemma then gives the projective secant dimension (5) minus 1. The opposite dimension inequality follows from the ambient dimension and the `6k` affine cone parameters, so this proves equality.

### 3. The precise external interpolation theorem and its complete exception list

Use Ciro Ciliberto and Rick Miranda, *Linear Systems of Plane Curves with Base Points of Equal Multiplicity*, Transactions of the AMS 352 (2000), 4037–4050; primary preprint:

https://arxiv.org/pdf/math/9804018

Their Main Conjecture 2.2 says that every special system is `(-1)`-special. Their Theorem 5.2 proves this for **every** homogeneous system `L_d(m^n)` with `m<=12`. Their Theorem 2.4 gives the complete list of `(-1)`-special homogeneous systems. Set their multiplicity `m=3` and their number of points `n=k`. The only nonempty integer intervals in that list are

\[
k=2,\quad 3\le d\le4;
\qquad
k=5,\quad 6\le d\le 13/2.
\]

Thus the complete exceptional list for our interpolation reduction is

\[
\boxed{(d,k)=(3,2),(4,2),(6,5).}
\tag{6}
\]

Every other `(d,k)` is covered by Section 2. The required statements are on PDF pages 4–5 (Main Conjecture 2.2 and Theorem 2.4) and PDF page 13 (Theorem 5.2); the document's printed page numbers are 3–4 and 12.

The following substitution table makes the classification check explicit:

| Number of points `k` | Theorem 2.4 interval after `m=3` | Integer degrees |
|---:|---|---|
| 2 | `3 <= d <= 4` | 3, 4 |
| 3 | `9/2 <= d <= 4` | none |
| 5 | `6 <= d <= 13/2` | 6 |
| 6 | `36/5 <= d <= 13/2` | none |
| 7 | `63/8 <= d <= 22/3` | none |
| 8 | `144/17 <= d <= 49/6` | none |

No other number of points occurs in their complete list.

### 4. Exact Gaussian certificates for the three exceptions

Rows are moments `m_(i,j)` in increasing total degree, and, within a total degree, increasing `i`. Each component contributes six columns in the order

`(weight, mean_x, mean_y, cov_xx, cov_xy, cov_yy)`.

The weight column is the moment vector itself; all component weights are set to 1 for the affine cone sum. This is a convenient unnormalized cone chart, not an alteration of the projective mixture variety. Dividing all component weights by `k` puts the same projective point into the usual weights-summing-to-one chart and only rescales derivative columns.

All input parameters below are integer tuples `(u,v,a,b,c)`. Positive definiteness is unnecessary for a complex algebraic rank witness.

| `(d,k)` | Component parameter tuples | Matrix rank | Exact nonzero minor determinant |
|---|---|---:|---:|
| `(3,2)` | `(0,1,2,0,0)`, `(-1,-1,2,2,0)` | 10 | `768` |
| `(4,2)` | `(0,2,1,1,1)`, `(-1,-1,1,2,1)` | 12 | `-157464` |
| `(6,5)` | `(2,-1,1,-1,2)`, `(0,1,1,0,0)`, `(1,1,2,0,2)`, `(0,1,1,-1,0)`, `(-1,-1,0,0,-1)` | 28 | `-1899345045033739139102539776` |

The selected row indices (zero based, in determinant order) are:

* `(3,2)`: `[0,2,1,5,4,3,6,7,8,9]`; columns `0,...,9`.
* `(4,2)`: `[0,2,1,5,4,3,6,7,8,9,10,11]`; columns `0,...,11`.
* `(6,5)`: `[0,2,1,5,4,3,6,7,8,10,11,12,9,13,14,15,16,17,18,19,20,21,24,23,22,25,26,27]`; columns `0,...,27`.

The determinants reduce to `61,96,37` respectively modulo 101. Each determinant is nonzero over the integers, so the corresponding complex tangent matrix reaches its maximal possible rank.

The moment values used to construct the matrices satisfy the exact recurrence

\[
m_{ij}=u m_{i-1,j}+(i-1)a m_{i-2,j}+jb m_{i-1,j-1}\quad(i>0),
\tag{7}
\]

with `m_0j=v m_0,j-1+(j-1)c m_0,j-2` and `m_00=1`. Equations (3) and (7) uniquely reproduce every entry.

Each witness reaches precisely the rank in (5). Together with (6), the proof covers every `d>=2,k>=1`, completing Q739.

### 5. Verification files

* `verify_q739.py` — standard-library Python, deterministic seed 739; reconstructs the integer tangent matrices, selects nonsingular minors modulo 101, and computes their exact integer determinants by Bareiss elimination. The modulus is only a search aid; the stored proof witnesses are exact integer determinants.
* `q739_certificates.json` — all input parameters, all row monomials, every matrix entry, the selected row and column indices, and exact determinants.
* `independent_verify_q739.py` — an independent moment calculation from the explicit exponential-series coefficient formula and a separate rational Gaussian-elimination determinant check.
* `q739_verification_output.txt` — recorded successful output from both verifiers.

No inference from a finite list to all degrees is made. The infinite portion is the cited plane triple-point theorem; computation is confined to its three explicitly classified exceptional cases.

### Source-scope caution

The primary version of Dumitrescu, *Plane curves with prescribed triple points: a toric approach*, arXiv:1104.1755v1, states Theorem 5.3 as expected dimension for all `d>=5`. Read literally, this omits `(d,k)=(6,5)`: the cube of the conic through five points is a nonzero degree-6 curve with five triple points, while the expected linear-system dimension is -1. The proof here therefore uses Ciliberto–Miranda's complete classification, which explicitly retains this case, rather than that broader literal wording.


## 5. Q1749 — complete Gabor category classification

**B7 / Q1749 / stable ID `0c0478553c79951846b2`.** Exact retained statement:

> For fixed a,b>0, is E_Λ meagre or nonmeagre in L²(R) with its norm topology?

Stable statement ID: `0c0478553c79951846b2`.

Exact retained statement: For fixed a,b>0, is E_Λ meagre or nonmeagre in L²(R) with its norm topology?

The handoff fixes complex \(L^2(\mathbb R)\), Gaussian \(\phi(t)=2^{1/4}e^{-\pi t^2}\), lattice \(\Lambda=a\mathbb Z\times b\mathbb Z\), and equivalence under multiplication by a constant of modulus one.

**Result: written proof of the full retained classification.**

| Lattice cell area | Category of \(E_\Lambda\) |
|---|---|
| \(ab<1\) | Dense \(G_\delta\), hence comeagre and nonmeagre |
| \(ab=1\) | Nonempty and nowhere dense, hence meagre |
| \(ab>1\) | Empty |

This result combines a general frame lemma, Wellershoff's 2026 density theorem, the classical Gaussian Gabor frame/completeness threshold, and a direct critical-density perturbation argument. The critical case is proved separately; the frame lemma cannot be applied there.

### 1. A general frame lemma

Let \((\psi_j)_{j\ge1}\) be a countable frame for a separable complex Hilbert space \(H\). Let \(A:H\to\ell^2\) be its analysis operator. Thus for constants \(0<c\le C<\infty\),
\[
c\|f\|^2\le\|Af\|_2^2\le C\|f\|^2.
\]
Put \(\Phi(f)=|Af|\) coordinatewise and
\[
E=\{f:\Phi(g)=\Phi(f)\Longrightarrow g\in\mathbb T f\},\quad
d_{\mathbb T}(f,g)=\inf_{|z|=1}\|f-zg\|.
\]
Then \(E\) is a \(G_\delta\) subset of \(H\).

**Compactness lemma.** If \(f_r\to f\) and \(\Phi(g_r)=\Phi(f_r)\), then some subsequence of \((g_r)\) converges strongly in \(H\).

**Proof.** The magnitudes \(|Ag_r|=|Af_r|\) converge in \(\ell^2\), since the modulus map is 1-Lipschitz. They therefore have uniformly small squared-sum tails. Each individual coefficient of \(Ag_r\) is bounded. Diagonal subsequence selection gives convergence of every coefficient along a subsequence, and uniform tail control upgrades this to convergence in \(\ell^2\). The lower frame bound makes the corresponding \(g_r\) a Cauchy sequence in \(H\); completeness gives strong convergence. ∎

For each positive integer \(m\), define
\[
B_m=\{f:\exists g,\ \Phi(g)=\Phi(f),\ d_{\mathbb T}(f,g)\ge1/m\}.
\]
If \(f_r\in B_m\) converges to \(f\), choose witnesses \(g_r\). The compactness lemma supplies a convergent subsequence. Continuity of \(\Phi\) and of \(d_{\mathbb T}\) preserves both conditions in the limit. Thus \(B_m\) is closed. Since the phase orbit \(\mathbb T f\) is compact, a point outside it has strictly positive distance from it. Consequently
\[
H\setminus E=\bigcup_{m\ge1}B_m,
\]
which proves that \(E\) is \(G_\delta\). If \(E\) is dense, each closed \(B_m\) has empty interior, so its complement is comeagre. No uniform Lipschitz stability is claimed or needed.

### 2. The oversampled case \(ab<1\)

The Gaussian system \((M_{nb}T_{ma}\phi)_{m,n\in\mathbb Z}\) is a frame when \(ab<1\). The lattice is uniformly discrete with lower Beurling density \(1/(ab)>1\). Wellershoff, *On a dense set of functions determined by sampled Gabor magnitude*, arXiv:2507.14556v2 (17 April 2026), Corollary 3, proves that every finite linear combination of Hermite functions is uniquely recoverable, among all of \(L^2\), from these magnitudes. These finite combinations form a dense subspace. Applying §1 proves the first line of the classification.

Primary density source: https://arxiv.org/html/2507.14556v2 , §2.3, Corollary 3. Published version: https://doi.org/10.1016/j.acha.2026.101884 . The general Gaussian frame result is the Lyubarskii–Seip–Wallstén theorem. The precise version for arbitrary lattices is stated as Theorem A, printed p. 2, in Borichev–Gröchenig–Lyubarskii, *Frame Constants of Gabor Frames near the Critical Density*, arXiv:0909.4937v1: https://arxiv.org/pdf/0909.4937 .

### 3. The critical case \(ab=1\)

Here \(b=1/a\). Define the unitary Zak transform on the unit square by
\[
(U_af)(x,\omega)=\sqrt a\sum_{k\in\mathbb Z} f(a(x-k))e^{2\pi ik\omega}.
\]
For arbitrary \(L^2\) functions the sum and the unitary map are understood in \(L^2([0,1]^2)\). Unitarity follows by Fourier-series Parseval in \(\omega\), followed by the change of variables \(t=a(x-k)\). Every square-integrable function on the square is an admissible Zak transform, extended quasiperiodically outside it.

Write \(z=U_a\phi\) and \(F=U_af\). The time-frequency shifts obey
\[
U_a(M_{n/a}T_{ma}\phi)(x,\omega)
=e^{2\pi i(nx-m\omega)}z(x,\omega).
\]
Therefore the Gabor coefficients are the two-dimensional Fourier coefficients of
\[
h(x,\omega)=F(x,\omega)\overline{z(x,\omega)}.
\]
The function \(z\) is bounded, so \(h\in L^2\).

#### 3.1 The Gaussian Zak zero and a division lemma

The Gaussian Zak transform has precisely one zero in the fundamental square, at \((1/2,1/2)\), and its modulus is comparable to Euclidean distance from that point locally.

For completeness this follows directly from the Jacobi triple product (NIST DLMF, equation 20.5.9, https://dlmf.nist.gov/20.5.E9). Set \(q=e^{-\pi a^2}\) and \(w=e^{2\pi a^2x+2\pi i\omega}\). Then
\[
z(x,\omega)=2^{1/4}\sqrt a\,e^{-\pi a^2x^2}
\prod_{r=1}^\infty(1-q^{2r})(1+q^{2r-1}w)(1+q^{2r-1}w^{-1}).
\]
On \(0\le x,\omega<1\), only the factor \(1+qw\) can vanish, and it does so exactly at \((1/2,1/2)\). All other factors are locally nonzero. With \(u=x-1/2\), \(v=\omega-1/2\), that factor is
\[
1-e^{2\pi a^2u+2\pi iv}
=-2\pi(a^2u+iv)+O(u^2+v^2).
\]
The real-linear map \((u,v)\mapsto a^2u+iv\) is invertible. This proves the stated comparison. Uniform convergence of the product and its derivatives on compact sets justifies the local factorization. Away from the zero, continuity and compactness give a positive lower bound for \(|z|\).

It follows that whenever a trigonometric polynomial \(P(x)\) satisfies \(P(1/2)=0\),
\[
P(x)/\overline{z(x,\omega)}\in L^2([0,1]^2),
\]
indeed the quotient is essentially bounded. Near the zero the numerator is \(O(|u|)\), while the denominator has size at least a constant times \(\sqrt{u^2+v^2}\).

#### 3.2 An open dense set of ambiguous signals

For \(j=0,1,2,3\), put
\[
c_j(f)=\mathcal Gf(0,j/a).
\]
Consider the open set
\[
\mathcal U=\{f:\operatorname{Im}(c_0\overline{c_1})\ne0,\quad c_2\ne0,\quad c_3\ne0\}.
\]
It is dense. To see this, the four functions \(M_{j/a}\phi\) are linearly independent: divide a linear relation by the everywhere nonzero Gaussian and use independence of distinct exponentials. Hence the continuous coefficient map \(H\to\mathbb C^4\) is onto and admits a continuous right inverse. The indicated condition is open dense in \(\mathbb C^4\), so its preimage is open dense in \(H\).

Fix \(f\in\mathcal U\). The smooth map
\[
\Psi:\mathbb R^3\to\mathbb C,\qquad
\Psi(\theta)=\sum_{j=0}^2(-1)^j c_j(e^{i\theta_j}-1)
\]
has real derivative of rank two at zero: the first two derivative columns are \(ic_0\) and \(-ic_1\), which are independent over \(\mathbb R\). By the real implicit function theorem, the level set \(\Psi^{-1}(0)\) is a one-dimensional smooth manifold near zero. In particular it contains nonzero arbitrarily small \(\theta\), with at least one \(e^{i\theta_j}\ne1\).

Choose such a \(\theta\), and define
\[
P(x)=\sum_{j=0}^2 c_j(e^{i\theta_j}-1)e^{2\pi ijx}.
\]
Then \(P(1/2)=\Psi(\theta)=0\), so
\[
F'=F+P/\overline z\in L^2([0,1]^2).
\]
Let \(g=U_a^{-1}F'\). The Fourier coefficients of \(F'\overline z=h+P\) differ from those of \(h\) only at indices \((j,0)\), \(j=0,1,2\), where \(c_j\) is replaced by \(e^{i\theta_j}c_j\). All Gabor magnitudes are therefore unchanged. The nonzero coefficient \(c_3\) is unchanged, so any global phase relating \(g\) to \(f\) would have to be one. At least one of \(c_0,c_1,c_2\) changed, so \(g\ne f\). Thus \(g\not\sim f\).

Every \(f\in\mathcal U\) is ambiguous. Therefore
\[
E_\Lambda\subseteq H\setminus\mathcal U,
\]
where the right side is closed nowhere dense. This proves that \(E_\Lambda\) is nowhere dense at critical density. ∎

#### 3.3 An explicit nonzero uniquely recoverable critical signal

The critical uniqueness set is not empty. Define
\[
F_*(x,\omega)=\frac{1+e^{2\pi ix}}{\overline{z(x,\omega)}},\qquad f_*=U_a^{-1}F_*.
\]
The division lemma proves \(F_*\in L^2\), and it is nonzero. Its Gabor coefficient sequence consists of exactly two nonzero entries, both one, at \((m,n)=(0,0),(0,1)\). If \(g\) has the same magnitudes, completeness of Fourier series implies
\[
(U_ag)\overline z=u+v e^{2\pi ix},\qquad |u|=|v|=1.
\]
If \(u-v\ne0\), the numerator stays bounded away from zero near \((1/2,1/2)\), while the squared reciprocal of the denominator has a nonintegrable \(1/(u_0^2+v_0^2)\) singularity in local real coordinates \((u_0,v_0)\). Thus \(U_ag\notin L^2\), a contradiction. Necessarily \(u=v\), and then \(g=u f_*\). This proves \(f_*\in E_\Lambda\).

An exact ambiguous critical pair is also archived: use numerators
\[
H(t)=1+it+(1+i)t^2+2t^3,\qquad
H'(t)=-i-t+(1+i)t^2+2t^3,
\]
with \(t=e^{2\pi ix}\), and divide by \(\overline z\). Both polynomials vanish at \(-1\); their coefficient squared magnitudes are \((1,1,2,4)\). Their last coefficient is unchanged and nonzero, but the polynomials differ, so the signals are not global-phase multiples. These exact identities are checked by `verify_q1749_control.py`.

### 4. The undersampled case \(ab>1\)

The Gaussian Gabor system is incomplete for lattice cell area greater than one, so its linear analysis operator has a nonzero kernel vector \(u\). The needed incompleteness theorem is stated for every window on a rectangular lattice in Benedetto–Heil–Walnut, *Differentiation and the Balian–Low Theorem*, Journal of Fourier Analysis and Applications 1(4) (1995), Theorem 2.2(b), printed p. 363: https://heil.math.gatech.edu/papers/blt.pdf . If \(Af\ne0\), then \(f+u\) has exactly the same coefficients as \(f\), and cannot be a global-phase multiple of \(f\): applying \(A\) would force that phase to be one. If \(Af=0\) and \(f\ne0\), compare \(f\) with zero. If \(f=0\), compare with \(u\). Consequently no signal is uniquely recoverable and \(E_\Lambda=\varnothing\).

### 5. Scope and evidence

The category classification is for the norm topology on complex \(L^2\) and the exact infinite lattice observation specified in the handoff. It does not assert finite-sample recovery or a uniform modulus of continuity. The frame compactness proof does additionally give pointwise continuity of inversion at each uniquely recoverable signal in the \(\ell^2\) magnitude norm: if \(|Ag_r|\to|Af|\) and \(f\in E\), every convergent subsequence supplied by the same tail argument limits into \(\mathbb T f\), hence \(d_{\mathbb T}(g_r,f)\to0\). This has no quantitative uniform rate. For \(ab<1\), a dense set of ambiguous signals can coexist with the comeagre set of uniquely recoverable ones.

The proof is mathematical, not a finite computation or a compiled formal theorem. The finite critical-density control, when cited in the final report, checks the perturbation identities but does not establish the category theorem. The new argument has not been subjected to external peer review; no literature-priority claim is made. The retained source question is Phasebook, arXiv:2505.15351, Question 8.8, printed p. 33: https://arxiv.org/pdf/2505.15351 .


## 6. Q1749 — exact uniqueness criterion at critical density

**B7 / Q1749 / stable ID `0c0478553c79951846b2`.** Exact retained statement:

> For fixed a,b>0, is E_Λ meagre or nonmeagre in L²(R) with its norm topology?

Date: 2026-10-07. Additional written theorem for Q1749 (`0c0478553c79951846b2`), beyond the category classification. This is a mathematical derivation, without a literature-priority claim or formal compilation.

### Theorem

Fix `a>0`, let `b=1/a`, and use the Gaussian window and complex L² convention of `q1749_proof.md`. Write the entire lattice coefficient sequence as

`c_(m,n) = Gf(ma,n/a)`.

Then f is uniquely recoverable up to one global phase from these magnitudes if and only if

`c in l¹(Z²)` and `sum_(m,n)|c_(m,n)| = 2 max_(m,n)|c_(m,n)|`.

The zero signal satisfies the condition and is unique because the critical Gaussian Gabor system is complete. The criterion includes the explicit two-coefficient example in `q1749_audit.md`.

The proof uses the preceding Q1749 proof's unitary Zak representation and simple Gaussian Zak zero. The additional steps are supplied below.

### 1. Reduction to Fourier coefficients and a single singular point

Put `F=U_af`, `z=U_a phi`, and `h=F bar(z)`. On the two-dimensional torus represented by the unit square, h belongs to L². Its Fourier coefficients are the Gabor coefficients, with an index reflection that does not change any magnitude. The function z vanishes only at `z0=(1/2,1/2)` and has modulus comparable to distance from z0 there.

Translate the torus coordinates to move z0 to the origin, and write `H(u)=h(z0+u)`. Let its Fourier coefficients be d_j. They differ from the c_j only by unit scalars. The source condition implies

`integral_(|u|<rho0) |H(u)|²/|u|² du < infinity`.

Every trigonometric polynomial P with `P(0)=0` gives an admissible perturbation: after translating back, P divided by `bar(z)` is bounded near the zero and belongs to L² globally.

If the coefficient sequence has finite support or belongs to l¹, then H is continuous. The displayed integrability condition forces `H(0)=0`; otherwise its squared magnitude is bounded below near zero, and integration of `|u|^(-2)` diverges in two dimensions.

### 2. A necessary vanishing condition detected by positive Fourier kernels

Choose a smooth, nonnegative, even bump psi on R², supported in the unit ball and with integral one. For small t, periodize `psi_t(u)=t^(-2)psi(u/t)` on the torus, and let

`K_t=psi_t * psi_t`.

Then K_t is smooth and even, is supported within distance 2t of zero, has integral one, and its Fourier coefficients satisfy

`w_t(j)=|hat(psi_t)(j)|²`, so `0<=w_t(j)<=1` and `w_t(j)->1` for each fixed j.

Scaling gives `integral |u|² |K_t(u)|² du <= C`, independently of sufficiently small t. Weighted Cauchy–Schwarz therefore yields

`|(H*K_t)(0)| <= C^(1/2) (integral_(|u|<=2t) |H(u)|²/|u|² du)^(1/2) -> 0`.

Because K_t is smooth and H belongs to L², their Fourier pairing converges absolutely and

`(H*K_t)(0)=sum_j d_j w_t(j)`.

Two consequences follow.

**(a) A nonzero admissible H cannot have all its Fourier coefficients on one ray.** After a global rotation they would be nonnegative real. The sum is then at least `d_j w_t(j)` for any fixed positive coefficient; this has a positive limit, contradicting the preceding vanishing.

**(b) If exactly one coefficient is negative real and all the others are nonnegative real, then their sum is absolutely convergent and zero.** Write the exceptional coefficient as `-A`. For every finite set J of the nonnegative coefficients,

`sum_(j in J) d_j w_t(j) <= A w_t(j0)+(H*K_t)(0)`.

Sending t to zero gives `sum_(j in J)d_j <= A`. Taking the supremum over finite J gives `sum_(j!=j0)d_j <= A`, so the whole coefficient sequence is in l¹. Dominated convergence, using `w_t(j)<=1`, now gives `sum_(j!=j0)d_j=A`.

### 3. Noncollinear coefficient phases force ambiguity

Assume that two nonzero d-coefficients are linearly independent over the reals.

If at least four coefficients are nonzero, select those two, one further nonzero coefficient, and an unchanged nonzero anchor. Rotating the first three coefficient phases preserves magnitudes. The map from their three phase angles to the complex change in their sum has real derivative of rank two at zero. The implicit-function theorem produces a nontrivial local phase change for which that sum change is zero. The resulting finite trigonometric perturbation vanishes at the origin, so it gives an admissible competitor. The unchanged anchor excludes a nontrivial global phase, and at least one coefficient changes.

If precisely three coefficients are nonzero, admissibility and continuity imply their sum is zero. Replace all three by their complex conjugates. Their magnitudes and zero-sum condition are preserved, hence this is admissible. It is not a global-phase multiple: if `bar(d_j)=lambda d_j` for all j, all d_j would lie on one real line after one common rotation, contrary to the assumption.

Support sizes one and two cannot produce a noncollinear admissible sequence, because their finite sum must vanish. Thus every nonzero unique signal has all translated Fourier coefficients on one real line. After a global phase rotation, all d_j are real.

### 4. Two positive and two negative coefficients force ambiguity

Suppose there are at least two positive coefficients p1,p2 and at least two negative coefficients `-q1,-q2`, where all four magnitudes are positive. Keep all other coefficients unchanged.

The two vectors of lengths p1,p2 can have any resultant length between `|p1-p2|` and `p1+p2`. For a sufficiently small s>0, rotate their phases so their resultant is the positive real number `p1+p2-s`; the two resulting vectors can be chosen noncollinear. Likewise rotate the two negative coefficients so that their resultant is the negative real number `-(q1+q2-s)`.

The total sum of the four coefficients remains unchanged, because the two reductions by s cancel. This finite perturbation vanishes at the origin and is admissible. It is not a global-phase multiple of the original all-collinear configuration, because the first pair is now noncollinear.

Combining this observation with Section 2(a), a unique nonzero signal must have exactly one coefficient of one sign and every other nonzero coefficient of the opposite sign. After possibly multiplying by minus one, Section 2(b) applies. Hence the coefficient sequence is in l¹ and the magnitude of its exceptional coefficient equals the sum of all other magnitudes. This proves necessity of the theorem's condition.

### 5. Sufficiency by equality in the triangle inequality

Suppose an admissible nonzero f has absolutely summable coefficients and one coefficient, at j0, has magnitude equal to the sum of all other magnitudes. Let g have the same Gabor magnitudes, and write d and d' for the translated Fourier coefficient sequences of their corresponding H and H'. Both sequences are absolutely summable, both define continuous functions, and admissibility forces

`sum_j d_j=0` and `sum_j d'_j=0`.

For either sequence,

`|d_(j0)| = |sum_(j!=j0) d_j| = sum_(j!=j0)|d_j|`.

Equality in the (possibly infinite, absolutely convergent) triangle inequality forces all nonzero coefficients other than j0 to have a common phase, opposite to that of the j0 coefficient. The same is true for d'. Since their magnitudes agree term by term, the two sequences differ by a single global phase. Fourier uniqueness gives `H'=lambda H`, and division by the nonzero-a.e. Zak factor then gives `g=lambda f`.

This proves sufficiency and completes the characterization.

### Interpretation and scope

The criterion depends only on the observed critical-lattice magnitudes. It gives an explicit characterization of the exceptional uniquely recoverable set, in addition to proving its nowhere density. It does not give a finite-data decision procedure: absolute summability and equality of an infinite sum are infinite-measurement conditions. It also provides no uniform stability estimate near the equality boundary.

All analytic facts about the Gaussian Zak transform used here are proved in the preceding Q1749 argument. The only functional-analysis inputs added are Fourier Parseval, an approximate identity constructed explicitly above, Cauchy–Schwarz, the finite-dimensional implicit-function theorem, and equality in the triangle inequality.


## 7. Q1766 — the verified six-cube interval

**B7 / Q1766 / stable ID `84f1767e6fac27a1ca5e`.** Exact retained statement:

> What is the edge multiset dimension of Q₆, the graph on {0,1}⁶ with adjacency at Hamming distance one?

Research date: 2026-10-07. Stable statement ID: `84f1767e6fac27a1ca5e`.

### Result and scope

The completed computations give the computer-assisted bound

\[
\boxed{13\leq \operatorname{edim}_m(Q_6)\leq15.}
\]

An elementary argument below independently proves the weaker lower bound **8**. Complete finite searches exclude each of the cardinalities 8, 9, 10, 11, and 12. The upper bound is the published 15-landmark set, independently verified here using breadth-first graph distances. The exact value remains one of **13, 14, or 15**. This does not close Q1766.

These are finite exhaustive computations with explicit coverage arguments and archived source code and outputs. They have not been checked by a proof-assistant kernel. A second independently written exhaustive engine reran cardinality 8. The higher-cardinality exclusions were checked through a separate exhaustive audit of the symmetry rules on five-landmark prefixes, a positive resolving-set control, and replay-log checks; their entire search spaces were not rerun with a second independent engine.

The original question asks for the least nonempty subset S of the 64 vertices such that all 192 edges have distinct **unordered** distance multisets. The object being identified is an edge of the fixed graph Q6. The equivalence during search is the action of cube automorphisms on a landmark set and its edges. Distances and comparisons are exact integers; no genericity, probability of correctness, approximate recovery, or noisy observations enter the result.

### Primary-source comparison

Jaan Allikvere, *The edge multiset dimension of hypercubes*, arXiv:2608.09983v1, dated August 2026, states `6 <= edim_m(Q6) <= 15` in Proposition 10 and asks for the exact value in §10, Open problem 1. Its Table 1 supplies the 15-set. The PDF was retrieved and inspected during this run. The narrower interval above is an improvement relative to that stated bound; no blanket claim of priority over all later literature is made.

- Primary PDF: https://arxiv.org/pdf/2608.09983
- Abstract and version record: https://arxiv.org/abs/2608.09983

### Definitions

Vertices are integers 0 through 63, interpreted as six-bit words. There is an edge between u and v precisely when `(u xor v)` has one nonzero bit. For an edge e={u,v} and a vertex s,

\[
d(e,s)=\min\{d_H(u,s),d_H(v,s)\}.
\]

For a landmark set S, write

\[
H_e=(h_0,h_1,h_2,h_3,h_4,h_5),\qquad
h_j=\#\{s\in S:d(e,s)=j\}.
\]

Equality of these histograms is equivalent to equality of distance multisets. Because an edge has only two endpoints, h0 is at most 2; because its antipodal edge also has two endpoints, h5 is at most 2.

The antipodal edge \(\bar e=\{u\oplus63,v\oplus63\}\) satisfies \(d(\bar e,s)=5-d(e,s)\). Thus its histogram is the reverse of He. The 192 edges form 96 antipodal pairs. If S resolves every edge, its 96 unordered histogram-reversal pairs are distinct, and none of the histograms is palindromic.

For each fixed landmark s, the number of edges at distance j from s is

\[
6\binom5j=(6,30,60,60,30,6)_j.
\]

One proof chooses the direction of the edge, then chooses j of the remaining five coordinates where its fixed coordinates differ from s.

### Elementary proof of the lower bound 8

#### Cardinalities at most 6

At most 6m edges meet a landmark set of size m. At most another 6m edges meet its antipodal image. Therefore at least `192 - 12m` edges have both h0=0 and h5=0. Their remaining histogram entries are four nonnegative integers summing to m, giving at most \(\binom{m+3}{3}\) possibilities.

For every m at most 6, the first quantity is at least 120 and the second is at most 84. Two edges must share a histogram. This excludes every positive cardinality at most 6.

#### Cardinality 7

Assume that a 7-set resolves. For an unordered reversal pair of histograms, put

\[
a=h_0+h_5,\qquad b=h_1+h_4,\qquad w=3a+b.
\]

The totals over the 96 antipodal edge pairs must be

\[
\sum a=6\cdot7=42,\qquad \sum b=30\cdot7=210,
\]

and hence \(\sum w=336\).

There are too few distinct histogram pairs with low weight to achieve this. The exact numbers at weights 0 through 5 are:

| Weight w | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|---:|
| Possible unordered histogram-reversal pairs | 4 | 7 | 9 | 17 | 22 | 24 |

Here is a direct derivation. If a=0 and b=w, the ordered histograms number `(w+1)(8-w)`, so the unordered pairs number `(w+1)(8-w)/2`. Because the total landmark count is odd, no histogram equals its reversal. If a=1, then w=3+b, and the unordered pair count is `(b+1)(7-b)`. For w below 6, a cannot be at least 2. These formulas give the table without relying on the LP that suggested the argument.

Only 83 possible pairs have weight below 6. Thus any collection of 96 distinct pairs has total weight at least

\[
0\cdot4+1\cdot7+2\cdot9+3\cdot17+4\cdot22+5\cdot24
+6\cdot13=362.
\]

This contradicts the required total 336. Consequently no 7-set resolves, proving the lower bound 8.

`verify_certificate.py` independently enumerates the histogram possibilities and writes `capacity7_certificate.json`. The proof above does not require that program or an LP solver.

### Exhaustive exclusions through cardinality 12

#### Coverage of the normalized domain

Let S have cardinality m at least 2, and let r be the minimum Hamming distance between two distinct members of S. Choose a pair attaining r. A translation sends one endpoint to 0; a coordinate permutation sends the other endpoint to

\[
v_r=2^r-1.
\]

All other landmarks lie in the explicitly enumerated candidate set

\[
C_r=\{x\in\{1,\ldots,63\}:x\ne v_r,\ d_H(x,0)\ge r,\ d_H(x,v_r)\ge r\}.
\]

The remaining m-2 landmarks are selected in increasing order, with every selected pair at distance at least r. Conversely, the enumeration imposes precisely these necessary distance restrictions. Running r=1 through 6 therefore covers a normalized image of every m-set, without assuming uniqueness of that image.

The cardinalities of Cr for r=1,...,6 are 62, 52, 26, 6, 0, 0.

#### Coordinate symmetry and its coverage proof

The optimized searches retain at least one lexicographically least landmark set under the group of coordinate permutations fixing 0 and vr. This group permutes the first r coordinates among themselves and the remaining 6-r coordinates among themselves.

Two pruning rules are used.

1. **Pointwise stabilizer of a selected prefix.** Coordinates are partitioned into blocks having identical bits across every selected landmark. A permutation fixes that prefix pointwise exactly when it permutes coordinates within these blocks. The next selected vertex is retained only when, within each block, its one-bits occupy the lowest coordinate positions. This is its least integer image under the pointwise stabilizer.
2. **Setwise prefix comparison.** For selected prefix lengths 4 through a fixed cutoff (6 or 8, depending on the recorded program), compare the prefix to all images under the group fixing 0 and vr. Reject it if an image is lexicographically smaller.

To prove that these rules preserve coverage, choose a full landmark set that is lexicographically least in its group orbit. Every initial segment of its sorted landmark list is also lexicographically least among its group images. If an image of a prefix were smaller, its first newly introduced smaller vertex would be absent from the full original set, since that vertex occurs before the last prefix element. The same image of the full set would then be smaller, a contradiction. This proves rule 2. Rule 1 follows by restricting to permutations that fix the preceding prefix pointwise: moving the next vertex to a smaller value would again make the full set lexicographically smaller.

Only 203 coordinate partitions can occur. The code generates all of them and their refinements exactly. The number 203 is a control count, not an assumption used to prune.

The searches may retain multiple members of one automorphism orbit. Their leaf counts are counts of examined normalized candidates, **not** claimed orbit counts.

#### Histogram representation and comparison

For fixed m, an edge histogram is encoded as

\[
K_e=\sum_{j=0}^5 h_j(m+1)^j.
\]

Every digit is at most m, so this encoding is injective. All values and sums fit within the explicitly used unsigned integer types for the cardinalities searched. A timestamped direct-address table detects an equal key. The search stops examining a candidate as soon as a collision is found; all 192 keys must be distinct to accept a resolving set. Histogram sums for a prefix are maintained exactly and only additions and subtractions are performed.

#### Completed results

| Cardinality excluded | Engine and exact recorded outputs | Examined normalized candidates | Resolving sets found |
|---:|---|---:|---:|
| 8 | `exhaust.cpp`, `exhaust8.log` | 65,442,355 | 0 |
| 9 | `exhaust.cpp`, `exhaust9.log` | 505,191,560 | 0 |
| 10 | `exhaust_sym.cpp`, `exhaust_sym10.log` | 513,890,101 | 0 |
| 11 | `exhaust_prefix.cpp`, `exhaust_prefix11.log` | 947,908,463 | 0 |
| 12 | `exhaust_sharded.cpp`, 16 `exhaust12_shard*.log` files | 2,110,540,594 | 0 |

For cardinality 12, the disjoint shard label is `(S[2]*64 + S[3]) mod 16`, using zero-based indexing in the sorted selected list. Every surviving prefix of length 4 belongs to exactly one shard. All 16 shards ran to completion for all six values of r. Their aggregate counts are 2,105,648,364 candidates for r=1 and 4,892,230 for r=2; the other values contribute zero leaves. The summed measured job runtimes were 64.57 seconds, and the longest shard took 15.55 seconds on this execution environment. Runtime depends on the machine.

A preliminary unsharded cardinality-12 search stopped at its declared 50-second cap. Its output `exhaust_prefix8_12.log` explicitly has `timedout=1`; it contributes **no exclusion claim**. The completed shard results supply the exclusion instead.

The resolving property is not monotone under adding landmarks. Consequently none of these exclusions is inferred from another cardinality: m at most 7 is excluded analytically, and each of 8 through 12 has a separate complete search.

### Independent checks and their limits

1. **Positive upper-bound control.** `verify_certificate.py` computes all vertex distances by BFS, identifies the 192 edges from those distances, and computes distance multisets directly. It also cross-checks the coordinate-projection distance formula. All 192 published-witness histograms are distinct.
2. **Independent full cardinality-8 census.** `independent8.cpp` builds BFS distance spheres as 64-bit sets, enumerates combinations in Gosper order, and obtains histogram counts by set intersections and population counts. It does not reuse recursive histogram sums, the main search order, or coordinate-symmetry pruning. It independently excludes the same 61,474,519, 3,967,830, and 6 candidates at r=1,2,3. Its measured runtime was 3.10 seconds.
3. **Exact symmetry audit.** `audit_pruning.py` enumerates every admissible five-landmark prefix directly in Python, compares all relevant coordinate-permutation images, and compares the resulting sets of canonical prefixes with the C++ pruning engine. The counts agree exactly: 864 canonical prefixes out of 37,820 distance-valid prefixes at r=1; 635 out of 16,076 at r=2; and 14 out of 336 at r=3. These cover all 54,232 valid prefixes and all 1,513 canonical prefixes.
4. **Resolving witness through the pruned search.** A normalized image of the published 15-set passes every symmetry rule and reaches a successful leaf of the same search machinery. The output records one accepted candidate and all 192 histogram checks. This guards against a search that incorrectly rejects every set.
5. **Log and coverage audit.** `replay_bound.py --check-existing` requires all six distance classes for every searched cardinality and all 16 size-12 shards, rejects timeouts and positive `found` values, and compares exact counts to the recorded complete runs. It also requires the independent checks above.

These checks substantiate the computational lower bound but are not a second independent full enumeration at each higher cardinality or a formal kernel pass. The scripts, domain proof, and complete output record make those additional verifications possible.

### Verified 15-landmark set

The published hexadecimal mask is `0x02283022a042a00a`. In integer vertex labels the set is

\[
\{1,3,13,15,17,22,29,31,33,37,44,45,51,53,57\}.
\]

`source15_histograms.csv` gives every edge and its six histogram entries, and `source15_verification.json` records 15 landmarks, 192 edges, and 192 distinct histograms. A normalization used for the pruning positive control is

\[
\{0,1,2,4,7,10,14,22,24,25,26,28,29,45,58\}.
\]

### Unsuccessful constructive searches

A 45-second, fixed-seed annealing run for cardinality 14 evaluated 9,267,000 swaps and reached two unresolved antipodal edge pairs. A 30-second run for cardinality 13 evaluated 6,420,000 swaps and did not find a resolving set. Exhausting 540,240 nearby cardinality-14 candidates obtained by removing at most three vertices from the published 15-set and adding the necessary replacements also found none. These outputs are archived as `search14_seed1.log`, `search13_seed2.log`, and `neighborhood.log`. They are heuristic or restricted-domain negative results and have no force toward excluding sizes 13 or 14.

### Reproduction

Only Python3 and a C++17 compiler are required for the proof and exhaustive replay. The LP-discovery script additionally uses NumPy and SciPy, but neither library is required for the delivered bound.

Audit the existing outputs:

```bash
python replay_bound.py --check-existing
```

Recompile and rerun the complete proof computation in a fresh directory:

```bash
python replay_bound.py --replay --out ./cube_replay
```

The script uses an internal per-job cap of 50 seconds. A timeout or missing output fails verification; it is never interpreted as nonexistence. On slower hardware, set a larger cap with `--seconds-per-job`. The optional `-mpopcnt` compilation flag used for the independent8 run is an optimization for the execution machine and does not change the mathematical test.

The next finite target is a complete size-13 exclusion or a 13-landmark witness. If size 13 is excluded, the same alternative remains at size 14. Until those are resolved, the appropriate catalog update is **partial progress: certified computational interval 13–15**, with the elementary interval 8–15 available separately.


## 8. Q740 — covariance rotations, exact base case and positive real ambiguity

**B7 / Q740 / stable ID `b69755d99b945371b6be`.** Exact retained statement:

> For n≥8,r≥3,k=n+r and P=k n(n+3)/2+k−1≤binom(n+4,4)−1, is dim Sec_k(G_{n,4})=P−binom(r−1,2)?

Date: 2026-10-07. Stable statement ID: `b69755d99b945371b6be`.

### Results and scope

For the full target range `n>=8`, `r>=3`, `k=n+r`, and

\[
P=k\left(\frac{n(n+3)}2+1\right)-1\le\binom{n+4}{4}-1,
\]

the following inequality is proved:

\[
\boxed{\dim\operatorname{Sec}_{n+r}(G_{n,4})
\le P-\binom{r-1}{2}.}
\tag{1}
\]

The missing direction for the universal Q740 equality is the corresponding lower bound. The inequality follows from an explicit orthogonal family of covariance changes that fixes the means, weights, and every moment of order at most four.

For `n=8,k=11` the lower bound is additionally certified by a maximal integer Jacobian minor nonzero modulo 101. Thus

\[
\boxed{\dim\operatorname{Sec}_{11}(G_{8,4})=493.}
\tag{2}
\]

This covers every Q740 case with `n=8`, because the parameter-count inequality then forces `k=11`. It agrees with the earlier numerical Example 19 in the source paper and supplies a written upper-bound mechanism and an exact, reproducible rank certificate.

There is also a fully explicit rational one-parameter family of eleven real, positive definite Gaussians in eight dimensions, with eleven distinct fixed means and fixed weights, whose mixed moments through order four are all identical. A fifth moment distinguishes members of the family.

### 1. Rewriting the low moments

For a Gaussian component, write

\[
\ell_i(x)=\mu_i^Tx,\qquad
q_i(x)=x^T\Sigma_i x,\qquad
Q_i=q_i+\ell_i^2.
\]

The ordinary homogeneous moment forms of degrees zero through four are

\[
1,\quad \ell_i,\quad Q_i,\quad
3\ell_iQ_i-2\ell_i^3,\quad
3Q_i^2-2\ell_i^4.
\tag{3}
\]

These formulas follow by expanding `exp(ell_i+q_i/2)` and multiplying each homogeneous degree by its factorial. Equality of a homogeneous moment form is equivalent to equality of all mixed moments in that degree.

### 2. The exact covariance-rotation symmetry

Fix nonzero weights `w_i` summing to 1 and means `mu_i`. Choose square roots of the weights and form the vectors in component-index space `C^k`

\[
v_0=(\sqrt{w_i})_i,\qquad
v_a=(\sqrt{w_i}\mu_{ia})_i\quad(1\le a\le n),
\]

and put `W=span(v_0,...,v_n)`. For positive real weights and affinely spanning real means, `W` has dimension `n+1` and its standard bilinear form is nondegenerate. These conditions also hold generically over `C`.

Let `O` be an orthogonal transformation of `C^k` that fixes `W` pointwise. Regard

\[
R=(\sqrt{w_1}Q_1,\ldots,\sqrt{w_k}Q_k)^T
\]

as a vector with entries in the space of quadratic forms. Define

\[
R'=OR,\qquad Q'_i=R'_i/\sqrt{w_i},\qquad
q'_i=Q'_i-\ell_i^2.
\tag{4}
\]

Means and weights remain fixed. The degree-two mixture moment is `v_0^T R` and is unchanged because `O` fixes `v_0`. In the degree-three expression, the only varying part is

\[
\sum_i w_i\ell_iQ_i
=\sum_{a=1}^n x_a v_a^T R,
\]

which is unchanged because every `v_a` is fixed. Finally,

\[
\sum_i w_i(Q'_i)^2=(R')^TR'=R^TR=\sum_iw_iQ_i^2.
\]

The fixed means preserve the remaining fourth-degree term. Thus (4) preserves all moments in (3), and therefore every moment of order at most four. Over the reals, sufficiently small rotations preserve positive definiteness whenever the initial covariances are positive definite.

### 3. Generic orbit dimension and the universal upper bound

The pointwise stabilizer of `W` in the orthogonal group is isomorphic to

\[
O(K),\qquad K=W^\perp,\qquad \dim K=k-n-1=r-1.
\]

Write `m=r-1` and `D=dim S^2(C^n)=n(n+1)/2`. The projection of `R` onto `K` is an `m`-tuple of quadratic forms. Because the component covariance matrices are independently arbitrary, these projected forms are generic in `K tensor S^2(C^n)` and are linearly independent whenever `m<=D`.

This inequality holds throughout the target parameter range. Indeed,

\[
k\le\frac{\binom{n+4}{4}}{(n+1)(n+2)/2}
=\frac{(n+3)(n+4)}{12},
\]

so

\[
m=k-n-1\le\frac{n(n-5)}{12}<\frac{n(n+1)}2=D.
\]

An orthogonal transformation fixing a full-row-rank `m`-tuple of quadratics is the identity: writing the tuple as an `m by D` coefficient matrix `C`, the equality `OC=C` and a right inverse of `C` force `O=I`. Consequently the generic covariance-rotation orbit has dimension

\[
\dim O(m)=\frac{m(m-1)}2=\binom{r-1}{2}.
\tag{5}
\]

This orbit is contained in the fiber of the complete moment map through degree four, with the means and weights held fixed. The normalized parameter domain has dimension `P`; the dimension theorem for a dominant map onto its image therefore proves (1). Over `C`, adjoining weight square roots is a finite algebraic cover and does not change dimensions. The argument concerns generic fibers and does not assume the formula being proved.

Equivalently, infinitesimal ambiguity directions are

\[
\delta R=AR,\qquad A^T=-A,\qquad Av_a=0\quad(0\le a\le n).
\tag{6}
\]

The orbit gives exactly `binom(r-1,2)` independent directions generically. Additional kernel directions have not been excluded in every dimension, which is precisely the unresolved part of Q740.

### 4. An explicit real family at n=8,k=11

Let `e_1,...,e_8` be the standard basis of `R^8`. Take all weights equal to `1/11`, and means, in this order,

\[
0,\ e_1,\ 2e_1,\ e_2,\ e_2+e_3,\ e_2+2e_3,
\ e_4,\ e_5,\ e_6,\ e_7,\ e_8.
\tag{7}
\]

These eleven means are distinct and affinely span `R^8`. In `R^11` put

\[
v=(1,-2,1,0,0,0,0,0,0,0,0)^T,
\qquad
w=(0,0,0,1,-2,1,0,0,0,0,0)^T.
\]

They have squared norm 6, are orthogonal, and span the orthogonal complement of the weight-and-mean space `W` above.

For any real parameter `t`, define

\[
c(t)=\frac{1-t^2}{1+t^2},\qquad
s(t)=\frac{2t}{1+t^2}.
\]

Let `E_aa=e_a e_a^T`. The covariance family is

\[
\boxed{\Sigma_i(t)=I_8
+\frac{(c(t)-1)v_i+s(t)w_i}{3}E_{11}
+\frac{(c(t)-1)w_i-s(t)v_i}{3}E_{33}.}
\tag{8}
\]

At `t=0`, all eleven covariances are the identity. Formula (8) is rational in `t`, so every rational `t` gives rational component parameters.

#### Derivation from an orthogonal rotation

Define

\[
O(t)=I_{11}
+\frac{c(t)-1}{6}(vv^T+ww^T)
+\frac{s(t)}6(wv^T-vw^T).
\tag{9}
\]

Since `c(t)^2+s(t)^2=1`, this acts as a planar rotation on `span(v,w)` and as the identity on its orthogonal complement. For initial `q_i(x)=x^Tx`, the two relevant quadratic combinations are

\[
\sum_i v_iQ_i=2x_1^2,\qquad
\sum_i w_iQ_i=2x_3^2.
\]

Substitution into `Q'(t)=O(t)Q` gives exactly (8), so Section 2 proves the equality of all moments through order four for **every** real `t`.

#### Positive definiteness for the entire family

Only the first and third diagonal entries vary. For the entries with `v_i=1` they are `(2+c)/3` and `1-s/3`; for `v_i=-2` they are `(5-2c)/3` and `1+2s/3`. For `w_i=1` they are `1+s/3` and `(2+c)/3`; for `w_i=-2` they are `1-2s/3` and `(5-2c)/3`. Since `-1<=c,s<=1`, every one of these entries is at least `1/3`. The other six entries are 1. Therefore

\[
\Sigma_i(t)\succeq \tfrac13 I_8\quad\text{for every real }t\text{ and every }i.
\tag{10}
\]

Thus the continuous ambiguity persists among ordinary nonsingular real Gaussian distributions with positive mixture weights.

#### A fifth moment detects the lost information

For a one-dimensional Gaussian with mean `mu` and variance `z`,

\[
E[X^5]=\mu^5+10\mu^3z+15\mu z^2.
\]

In (7), only the components with first-coordinate means 1 and 2 contribute to the fifth first-coordinate moment. Substitution of (8) gives

\[
\boxed{E_t[X_1^5]=\frac{168}{11}-\frac{10}{11}s(t)^2.}
\tag{11}
\]

In particular the mixtures at `t=0` and `t=1` have respective fifth moments `168/11` and `158/11`, while all 495 moments of total order at most four coincide. They are different probability distributions with the same retained fourth-order summaries.

### 5. Exact dimension certificate for the base case

For `n=8,k=11`, the normalized parameter count is `P=494`; (1) gives dimension at most 493. To prove the reverse inequality, use the unnormalized affine cone parametrization with all eleven weights set to 1. It has 495 tangent columns: per component, one weight, eight mean, and thirty-six covariance directions. There are 495 moment rows of total order at most four.

The supplied integer input produces a `495 by 495` tangent matrix with a `494 by 494` minor whose determinant is

\[
\boxed{90\pmod{101}.}
\tag{12}
\]

A nonzero residue proves that the integer determinant, and hence the complex determinant, is nonzero. Thus the affine cone has dimension at least 494 and the projective secant has dimension at least 493. Combined with the upper bound, this proves (2).

The finite-field calculation supplies a characteristic-zero lower bound only. A low rank modulo a prime would not prove an upper bound; that upper bound comes exclusively from Sections 2–3.

### 6. Reproducibility and verification

* `verify_q740.py` constructs the rational family and verifies all 495 moments through degree four at seven rational parameters, using exact fractions and independent-coordinate Gaussian formulas. With `--rank`, it builds the generic integer tangent witness and computes the maximal minor modulo 101.
* `q740_family_checks.json` records the seven parameter checks, minimum covariance eigenvalues, and fifth moments.
* `q740_n8_k11_rank_certificate.json` contains all eleven mean vectors, all eleven covariance matrices, every moment-row multi-index, every entry of the 495-by-495 integer Jacobian, the complete selected row and column indices, and the residue in (12).
* `independent_verify_q740_rank.py` recomputes every matrix entry using direct Wick formulas through degree four and verifies the selected determinant using a separate modular LU implementation. It confirms the value 90 modulo 101.
* `q740_verification_output.txt` records the successful outputs.

The exact universal family proof uses (3)–(9); the seven sample parameters are implementation controls, not evidence extrapolated to all real parameters. All code uses only the Python standard library.

### 7. Primary-source comparison

Améndola–Ranestad–Sturmfels, *Algebraic Identifiability of Gaussian Mixtures*, arXiv:1612.01129v2, Example 19 (printed p. 13), Table 2 and Conjecture 21 (printed p. 14), supplies the target dimension pattern and the previously computed base case. The present derivation explains the entire proposed defect as an explicit covariance-rotation orbit; it does not infer the general equality from the table.

Blomenhofer, arXiv:2307.03850, Section 4.1 (printed pp. 17–18), discusses Koszul syzygies of the shifted quadratic forms for a **single homogeneous fourth-order tensor**. Preserving all lower degrees adds the pointwise-fixing conditions `Av_0=...=Av_n=0` in (6), reducing the rotation dimension from `binom(k,2)` to `binom(k-n-1,2)`. The two moment models must be kept distinct.

No first-publication claim is made. The full Q740 equality for arbitrary `n,r` remains unresolved by this report.


## 9. Q741 — the all-degree generic Gauss theorem

**B7 / Q741 / stable ID `f344e3bf779aac637144`.** Exact retained statement:

> For all d≥5 and n≥2, does V=GM_d(C^n)=closure{[exp(ℓ+q/2)]_d:ℓ∈S¹(C^n),q∈S²(C^n)} have a nondegenerate tangent map? Precisely, must T:P(V_reg)→Gr(dimV,S^d(C^n)), [v]↦T_vV, have finite fibers? The unresolved extension is beyond the proved degrees 5,…,9; [·]_d means the homogeneous degree-d part.

Date: 2026-10-07. Stable statement ID: `f344e3bf779aac637144`.

### Result and status

**Theorem.** For every integer `d >= 5` and `n >= 2`, the projective Gaussian homogeneous moment variety `P(GM_d(C^n))` is not 1-tangentially weakly defective. Its Gauss map is generically finite. More strongly, every Gauss fiber contains only finitely many smooth points which admit a Gaussian representation `(ell,q)` with `gcd(ell,q)=1`.

This is an all-degree proof, without a bounded-degree computer calculation. It establishes the generic geometric condition needed for the Massarenti–Mella identifiability theorem. It does **not** yet establish that **every** fiber on the **entire** smooth locus is finite, which is the stronger exact quantifier in the attached Q741. Smooth points outside the coprime parameter image still need treatment. Therefore the stable statement must remain open under its literal all-fibers wording, while the generic version and the identifiability consequence below can be recorded as proved by the present argument.

### 1. Moment polynomials and tangent spaces

Put `R=C[x_1,...,x_n]` and denote its degree-j homogeneous part by `R_j`. Use the exponential normalization

\[
M_j(\ell,q)=[\exp(\ell+q/2)]_j
=\sum_{a=0}^{\lfloor j/2\rfloor}
\frac{\ell^{j-2a}q^a}{(j-2a)!\,2^a a!}.
\]

Set `M_j=0` for `j<0`. Direct differentiation and the generating-series identity give

\[
jM_j=\ell M_{j-1}+qM_{j-2},\qquad
D M_j(h,p)=M_{j-1}h+\tfrac12 M_{j-2}p.
\tag{1}
\]

Thus, at a smooth point where the parametrization has full rank, its affine cone tangent space is

\[
T=M_{d-1}R_1+M_{d-2}R_2.
\tag{2}
\]

The factor `1/2` does not affect the subspace. The tangent formula also appears in Blomenhofer, *Gaussian Mixture Identifiability from degree 6 Moments*, arXiv:2307.03850, Proposition 2.8, printed pp. 8–9. Its Proposition 2.13 on printed p. 11 establishes the earlier bounded-degree generic contact result. The derivation (1) supplies everything from that source used here.

### 2. Coprimeness in every degree

Suppose `gcd(ell,q)=1`. For every `j>=1`, `gcd(M_j,q)=1`, because modulo `q` the polynomial `M_j` equals `ell^j/j!`. If an irreducible polynomial divides `M_j` and `M_{j-1}`, equation (1) forces it to divide `q M_{j-2}`. It cannot divide `q`, so it divides `M_{j-2}`. Repeating forces it to divide `M_0=1`, a contradiction. Consequently

\[
\gcd(M_j,M_{j-1})=1\quad(j\ge1).
\tag{3}
\]

For every `s>=4`, the differential of `(ell,q) -> M_s` is injective on this parameter locus. Indeed, if

\[
M_{s-1}h+\tfrac12M_{s-2}p=0,
\]

then (3) implies `M_{s-2} | h`. The left divisor has degree `s-2>=2`, while `h` is linear; hence `h=0`, followed by `p=0`. In particular the affine Gaussian variety has dimension

\[
N=n+\binom{n+1}{2}=\frac{n(n+3)}2
\tag{4}
\]

for `s>=4`.

The weighted scaling `(ell,q)->(t ell,t^2 q)` sends `M_s` to `t^s M_s`. On a local slice to this scaling, the corresponding projective moment map has injective differential. To see this, if `D M_s(h,p)=c M_s`, subtract `c/s` times the weighted Euler direction `(ell,2q)` and use differential injectivity. Thus its fibers within the coprime parameter locus are zero-dimensional, and are finite because they are schemes of finite type. One can formulate the parameter quotient using weighted projective space, or simply fix a nonzero coefficient of `ell` to 1 in finitely many local charts; the residual root ambiguities are finite.

### 3. An elementary intrinsic tangent-space recovery lemma

**Lemma.** Let `a in R_{t+1}`, `b in R_t`, where `t>=3` and `gcd(a,b)=1`. Set `T=a R_1+b R_2`. Then

\[
\{g\in R_t:gR_2\subseteq T\}=\mathbb Cb,
\tag{5}
\]

and

\[
\{f\in R_{t+1}:fR_1\subseteq T\}=\mathbb Ca+bR_1.
\tag{6}
\]

**Proof of (5).** Choose two linearly independent coordinate forms `x,y`. Membership gives

\[
gx^2=aL_{xx}+bQ_{xx},\quad
gxy=aL_{xy}+bQ_{xy},\quad
gy^2=aL_{yy}+bQ_{yy},
\]

where the L's are linear and the Q's quadratic. Comparing `x(gxy)` with `y(gx^2)` gives

\[
b\mid xL_{xy}-yL_{xx}.
\]

The right side has degree 2, while `deg b>=3`, so it is zero. Comparing `x(gy^2)` with `y(gxy)` similarly gives `xL_yy=yL_xy`. The first relation implies `L_xx=cx` and `L_xy=cy` for a scalar `c`. The second implies `xL_yy=cy^2`, forcing `c=0`. All three L's vanish. Thus `b` divides both `gx^2` and `gy^2`, whence `b|g`; equal degrees give `g in Cb`. The reverse inclusion is immediate.

**Proof of (6).** Write `fx=aL_x+bQ_x` and `fy=aL_y+bQ_y`. Comparing gives `b | xL_y-yL_x`, hence `xL_y=yL_x` by the same degree argument. Therefore `L_x=cx,L_y=cy`, and `b` divides both `(f-ca)x` and `(f-ca)y`. Thus `f-ca in b R_1`, as claimed. The reverse inclusion is immediate. This proof works for every `n>=2` and uses only unique factorization.

Applied with `a=M_{d-1}`, `b=M_{d-2}`, `t=d-2`, equation (5) recovers the projective polynomial `[M_{d-2}]` from the tangent space alone. Equation (6) additionally recovers the line generated by `M_{d-1}` in `R_{d-1}/M_{d-2}R_1`.

### 4. Finite fibers on the coprime parameter image for d>=6

Fix any tangent space arising at a smooth point represented by a coprime pair. Its intrinsic kernel (5) is a single line `[b]`. Every other coprime Gaussian representation with the same tangent space must satisfy

\[
[M_{d-2}(\ell',q')]=[b].
\]

Since `d-2>=4`, Section 2 shows that there are only finitely many such parameter classes. Therefore there are only finitely many Gaussian moment points with the prescribed tangent space within the coprime image.

Alternatively, (5) defines a rational map on the Gauss image, and the degree-`d-2` projective moment map factors through the Gauss map on a dense open set. Its generic finiteness forces the Gauss map's generic finiteness. This is a function-field argument and requires no assertion about special fibers or points at infinity.

### 5. The remaining degree d=5

Here `M_3` alone has positive-dimensional parameter fibers, so also use (6). Set

\[
r=q+\ell^2/3.
\]

Then

\[
M_3=\ell r/2,
\qquad
M_4=r^2/8+\ell^2r/6-\ell^4/36.
\tag{7}
\]

For a fixed nonzero `[M_3]`, the possible projective linear forms `[ell]` are among the finitely many linear factors of `M_3`. Fix one such factor and normalize it. Then all possible `r` have the form `r'=c r`, with nonzero scalar `c`.

Modulo `M_3 R_1`, the second formula in (7) becomes

\[
[M_4]=[r^2/8-\ell^4/36].
\]

Because `gcd(ell,r)=1`, the classes of `r^2` and `ell^4` are linearly independent modulo `ell r R_1`: a relation reduces modulo `ell` to force the coefficient of `r^2` to vanish, and then modulo `r` to force the other coefficient to vanish. Thus, once the line in (6) is fixed, comparison of

\[
c^2r^2/8-\ell^4/36
\]

with its value for an existing representation forces `c^2=1`. There are at most two normalized possibilities per linear factor. Hence the Gauss fibers on the coprime image are finite also for `d=5`. This argument works for binary forms even though their quadratic factors split.

### 6. Generic identifiability consequence in all degrees

The Gaussian cone is irreducible, being the closure of the image of an affine space. It is nondegenerate because setting `q=0` supplies all degree-d powers of linear forms, which span `R_d`. The coprime parameter locus is dense and nonempty (for example `ell=x_1,q=x_2^2`), so its image is dense in the Gaussian cone. Thus the results above verify the required generic Gauss condition on this irreducible, nondegenerate variety.

Let `L=binom(n+d-1,d)` and `N=n(n+3)/2`. For every `d>=5,n>=2`, if

\[
(h+1)N\le L
\tag{8}
\]

and `GM_d(C^n)` is `(h+1)`-nondefective, then it is `h`-identifiable as an affine cone. This follows from Massarenti–Mella, *Bronowski's conjecture and the identifiability of projective varieties*, arXiv:2210.13524v3, Theorem 1.5, printed p. 3, with projective dimensions `N-1,L-1`. Their Definition 2.2 and Remark 2.3, printed p. 5, explicitly equate Gauss degeneracy with positive-dimensional contact at **general** points; the theorem needs the generic condition proved above.

Combining with Blomenhofer–Casarotti, *Nondefectivity of invariant secant varieties*, arXiv:2312.12335v2, Theorem 4.10(1), gives the explicit range

\[
h+1\le \frac{L}{N}-N.
\tag{9}
\]

In this range condition (8) follows automatically. Thus the identifiability conclusion associated with their Theorem 4.10(3) extends to every degree `d>=5`, with the necessary dimension qualification in (8). This concerns decomposition into cone points, and does not by itself separate unknown statistical weights from the scaling of means and covariances using just one homogeneous degree.

### 7. Exact remaining issue for Q741

The attached question asks that **all** fibers on `P(V_reg)` be finite. The proof covers all points represented by `gcd(ell,q)=1` and proves the generic Gauss property in all degrees. It does not classify smooth points with every representation satisfying `gcd(ell,q)!=1`, nor smooth points on the closure boundary not in the finite parameter image. A positive-dimensional Gauss fiber, if one exists, must be confined to those exceptional loci. Generic finiteness cannot be upgraded to universal finiteness by semicontinuity; special fibers can grow.

There is a wording distinction in the sources: arXiv:2312.12335v2 Theorem 3.6 writes the all-fibers condition, while its cited verification in arXiv:2307.03850 Proposition 2.13 and the original Massarenti–Mella criterion are generic contact statements. The present result deliberately preserves the stricter handoff quantifier instead of silently replacing it.

### Sources inspected

1. https://arxiv.org/html/2312.12335v2 — Definitions 4.9, Theorem 4.10, Remark 4.11; Theorem 3.6.
2. https://arxiv.org/pdf/2307.03850 — Proposition 2.8 pp. 8–9; Proposition 2.13 p. 11; Theorem 2.6 p. 7.
3. https://arxiv.org/pdf/2210.13524 — v3, Theorem 1.5 p. 3; Definition 2.2 and Remark 2.3 p. 5.

The proof above is symbolic and all-degree. No finite experiment is used to infer a universal degree statement. Q738 and Q742 remain closed as accepted in the handoff and are not re-audited here.


## 10. Q738 and Q742 — a residual stability obstruction

**B7 / Q738 / stable ID `2f577a87fee1b2c95e2d`.** Exact retained statement:

> For arbitrary k, is the complexified moment map of k-component univariate Gaussian mixtures, with unknown means, variances and weights summing to 1, generically one-to-one modulo component permutation from moments m_1,…,m_{3k}? Equivalently, is the model rationally identifiable at order 3k? Algebraic finite-fiber identification at 3k−1 and rational identification at 3k+2 are established; these are not the target.

**B7 / Q742 / stable ID `c069b7ff6ff08382c685`.** Exact retained statement:

> For each k≥2, are k-mixtures of gamma distributions and k-mixtures of inverse Gaussian distributions rationally identifiable from their first 3k moments, modulo component permutations? Component parameters and mixture weights are unknown. Rational identifiability refers to generic one-to-one fibers of the complexified moment parameterization; the two positive-support families are one source-conjectured target, not two counts.

Date: 2026-10-07. Residual stability result for accepted Q738 and Q742, stable IDs `2f577a87fee1b2c95e2d` and `c069b7ff6ff08382c685`.

The accepted generic rational-identifiability conclusions remain unchanged. The result below concerns uniform recovery from perturbed moments on positive real parameter classes whose components may approach one another. The distance is Wasserstein distance between **mixing measures on component mean–variance parameter space**, not Wasserstein distance between the resulting distributions on the observed real variable.

### Theorem

Fix `k>=2`, let `m=2k-1`, and choose one of the Gaussian, gamma, or inverse Gaussian families parameterized by component mean `mu>0` and component variance `v>0`. Let

`F_d(nu)=(integral M_1 dnu,...,integral M_d dnu)`

be the first d raw moments of the resulting mixture, where `M_r(mu,v)` is the rth raw moment of one component. For every fixed finite d, and in particular for `d=3k`, there are pairs of mixing measures `nu_even(epsilon)` and `nu_odd(epsilon)`, each with exactly k distinct components and strictly positive fixed weights, such that

`W1(nu_even(epsilon),nu_odd(epsilon)) = epsilon`,

`||F_d(nu_even(epsilon))-F_d(nu_odd(epsilon))||_infinity <= C epsilon^(2k-1)`.

All component means lie in a fixed positive bounded interval, all component variances equal a fixed positive `v0`, and the component weights have a positive lower bound depending only on k. The constant C is independent of sufficiently small epsilon.

Consequently no uniform inverse estimate

`W1(nu,nu') <= L ||F_(3k)(nu)-F_(3k)(nu')||_infinity^alpha`

can hold on such a class for any `alpha>1/(2k-1)` and finite L. This does not assert that exponent `1/(2k-1)` is achievable; the construction gives an obstruction only.

### 1. The three moment curves

Write v for the component variance. The Gaussian raw moments satisfy

`M_0=1, M_1=mu, M_r=mu M_(r-1)+(r-1)v M_(r-2)`.

They are polynomials in mu and v; this recurrence follows directly by Gaussian integration by parts.

For gamma distributions, shape and scale are respectively `mu²/v` and `v/mu`. Thus

`M_r(mu,v) = product_(j=0)^(r-1)(mu+jv/mu)`.

For inverse Gaussian distributions, the usual shape parameter is `lambda=mu³/v`. Their raw moments satisfy

`M_0=1, M_1=mu, M_r=(2r-3)(v/mu)M_(r-1)+mu²M_(r-2)`.

These formulas show that, with v fixed positive, all the moment coordinates are real analytic for mu>0. They are finite Laurent polynomials in mu. On every fixed compact positive mean interval, every derivative used below is bounded.

Primary source for the gamma product and inverse Gaussian recurrence: Henriksson, Ranestad, Seccia, and Yu, [*Moment varieties of the inverse Gaussian and gamma distributions are nondefective*, arXiv:2409.18421v3](https://arxiv.org/html/2409.18421v3), Section 3 equation (3.1), and the beginning of Section 4.

### 2. Positive mixtures from an alternating finite difference

For `j=0,...,m`, let `theta_j=(mu0+j epsilon,v0)` and define

`nu_even = 2^(1-m) sum_(j even) C(m,j) delta_(theta_j)`,

`nu_odd = 2^(1-m) sum_(j odd) C(m,j) delta_(theta_j)`.

There are k indices of each parity because m is odd. The two parity sums of binomial coefficients are both `2^(m-1)`, so these are probability measures. Every component weight is at least `2^(1-m)`, and every component is distinct when epsilon>0. For `0<epsilon<=1/m`, the choice `mu0=v0=1` keeps all means in `[1,2]` and all variances equal to one.

For any moment coordinate g(mu)=M_r(mu,v0),

`integral g d(nu_even-nu_odd) = 2^(1-m) sum_(j=0)^m (-1)^j C(m,j) g(mu0+j epsilon)`.

The forward finite-difference identity, proved by applying the fundamental theorem of calculus repeatedly, is

`Delta_epsilon^m g(mu0) = integral_[0,epsilon]^m g^(m)(mu0+t1+...+tm) dt1...dtm`.

The preceding alternating sum equals `(-1)^m Delta_epsilon^m g(mu0)`. Hence

`|integral g d(nu_even-nu_odd)| <= 2^(1-m) epsilon^m sup_(mu in [mu0,mu0+m epsilon]) |g^(m)(mu)|`.

Taking the maximum over `r=1,...,d` proves the moment estimate, with

`C=2^(1-m) max_(1<=r<=d) sup_(mu in I) |partial_mu^m M_r(mu,v0)|`

for a fixed compact interval I containing all the means.

For Gaussian components, moments of order below m agree exactly, since their mean polynomials have degree below m. For gamma and inverse Gaussian components, finite differences cancel the Taylor expansion in mean to order m-1; this is **not** a claim that their first m-1 moment coordinates agree exactly.

### 3. Exact mixing-measure Wasserstein distance

Use Euclidean distance on `(mu,v)` space. Any even-indexed support point and any odd-indexed support point differ in mean by at least epsilon and have the same variance. Every transport plan moves unit total mass by distance at least epsilon, so `W1>=epsilon`.

An explicit transport achieves this lower bound. For each adjacent index pair `(j,j+1)`, move mass

`tau_j=C(m-1,j)/2^(m-1)`

from the even index to the odd index. At every even index i, the total outgoing mass is

`[C(m-1,i-1)+C(m-1,i)]/2^(m-1)=C(m,i)/2^(m-1)`;

the same identity verifies every odd-index incoming mass. Boundary binomial coefficients are interpreted as zero. The total edge mass is one, and each edge has length epsilon. The cost is exactly epsilon. Therefore `W1=epsilon`.

This calculation is invariant under permutation of component labels and is genuinely a distance between mixing measures. It is not a coordinatewise distance between arbitrarily labeled parameter arrays.

### 4. Failure of a uniform inverse Hölder exponent above 1/(2k-1)

Suppose the displayed inverse estimate held with fixed L and alpha on a class containing all these pairs. Then

`epsilon <= L C^alpha epsilon^(m alpha)`.

Dividing by epsilon and sending epsilon to zero gives a contradiction whenever `m alpha>1`. All components remain distinct at every positive epsilon, and all weights remain bounded below. The degeneration is approach to a collision, not vanishing mixture weights or zero component variances.

One can choose an ambient compact mean–variance rectangle such as `[1/2,5/2] x [1/2,3/2]` and a weight lower bound `2^(-m)`. Every constructed parameter vector lies in its interior relative to the admissible k-component parameter space. If desired, the obstruction persists after restricting to any dense subset of this admissible space, including a dense identifiable generic subset: for each epsilon perturb the two labeled mixtures into that subset by `O(epsilon^(m+1))`. On a common compact parameter neighborhood, the moment map is Lipschitz and mixing-measure W1 changes by at most a constant times that parameter perturbation. Thus the perturbed W1 remains at least epsilon/2 and the moment gap remains `O(epsilon^m)`.

This density argument requires the indicated subset to be dense in the positive real parameter region; it is not a statement that every exceptional complex point is identifiable. The conclusion also leaves intact pointwise local inverse estimates and uniform estimates on classes with a fixed positive separation from collision and other singular sets.

### 5. A deterministic moment-noise consequence

Let a reconstruction procedure receive a vector whose coordinate errors relative to the true `F_(3k)(nu)` are at most eta. Set `epsilon=(2 eta/C)^(1/m)` for eta small enough that the preceding construction applies, and present the midpoint of the two constructed moment vectors. It is within eta of either true moment vector. By the triangle inequality, any returned mixing measure is at W1 distance at least epsilon/2 from at least one of the two possible truths.

Thus the worst-case deterministic-noise recovery error is at least a positive constant times `eta^(1/(2k-1))` on the stated class. This is not a finite-sample statistical lower bound and does not by itself give a trace or sampling requirement.

### 6. Explicit two-component Gaussian control

Take k=2, m=3, and component variance one. The two mixing measures are

`nu_even = (1/4)delta_(1,1)+(3/4)delta_(1+2epsilon,1)`,

`nu_odd = (3/4)delta_(1+epsilon,1)+(1/4)delta_(1+3epsilon,1)`.

Their W1 distance is exactly epsilon. In the order `r=1,...,6`, the exact even-minus-odd raw moment differences are

`0`,

`0`,

`-(3/2)epsilon³`,

`-6epsilon³-9epsilon⁴`,

`-30epsilon³-45epsilon⁴-(75/2)epsilon⁵`,

`-120epsilon³-270epsilon⁴-225epsilon⁵-135epsilon⁶`.

For `0<epsilon<=1/3`, the sixth coordinate has the largest absolute value, so

`||F_6(nu_even)-F_6(nu_odd)||_infinity = epsilon³(120+270epsilon+225epsilon²+135epsilon³) <= 240epsilon³`.

The mixture moment vectors are distinct for every positive epsilon; the example concerns conditioning of an inverse, not identical moment data.

| epsilon | Mixing-measure W1 | Maximum six-moment error |
| --- | --- | --- |
| 1/10 | 1/10 | 0.149385 |
| 1/100 | 1/100 | 0.000122722635 |
| 1/1000 | 1/1000 | 0.000000120270225135 |

The ratio of W1 to the moment error grows on the order of epsilon^(-2), demonstrating the failure of a uniform Lipschitz inverse even in this small positive-variance example.

### 7. Exact reproduction

`moment_collision_check.py` uses only Python's standard library and exact fractions. It verifies normalization and the adjacent-edge transport marginals for k=2,...,8, verifies the finite binomial cancellation identities at these k, and checks certified derivative bounds for all three families through moment order 3k for k=2,3,4 at two rational epsilon values. It also independently constructs and checks the six displayed Gaussian difference polynomials by exact coefficient arithmetic. The output is `moment_collision_results.json`.

These finite checks supplement the general proof; they are not used as a substitute for its all-k argument. No literature-priority claim is made for the finite-difference construction.


## 11. Q1001 and Q1002 — tensor criteria and cumulant cutoffs

**B7 / Q1001 / stable ID `93986607a1f5ccc79b75`.** Exact retained statement:

> For n≥2,d≥3, characterize T∈V_pmi with a unique orthogonal eigenvector basis up to signs/order; equivalently {Q∈O(n):Q·T∈V_pmi}=SP(n), the signed permutations.

**B7 / Q1002 / stable ID `ddcccae3e3f4fb404ca2`.** Exact retained statement:

> Which PMI source distributions are identifiable from all cumulants jointly, rather than from one generic order? Give the distributional analogue of ICA’s at-most-one-Gaussian rule.

Research date: 2026-10-07.

- Q1001 stable statement ID: `93986607a1f5ccc79b75`.
- Q1002 stable statement ID: `ddcccae3e3f4fb404ca2`.

### Scope and source alignment

Three partial results are valid:

1. An explicit sufficient criterion for a real diagonal tensor of every even order to have only the standard orthogonal eigenvector basis.
2. For a fixed PMI source distribution with analytic cumulant-generating function, the rotations satisfying all PMI cumulant restrictions already satisfy a finite initial collection of those restrictions.
3. There is no finite cutoff uniform over all such distributions, even in a fixed dimension n at least 2 and even among independent, centered, variance-one sources. More precisely, every even order at least 4 occurs as the smallest sufficient cumulant cutoff for an explicit family below.

These results do not characterize all exceptional tensors in V_pmi or all identifiable PMI distributions. They do not close Q1001 or Q1002. The diagonal sufficient criterion specializes the source paper's generic eigenvector argument to explicit coefficients; no claim that this entire idea is absent from the literature is made.

The primary source is Ribot–Seigal–Zwiernik, *Beyond independent component analysis: identifiability and algorithms*, arXiv:2510.07525v1:

https://arxiv.org/html/2510.07525v1

The paper defines O(n) as **real** orthogonal matrices in §3, gives the real tensor eigenvector definition there, and identifies orthogonal eigenvector bases with the orbit of V_pmi. Theorem 2.3 gives the equivalence between all PMI cumulant zero restrictions and the distributional PMI condition when the cumulant-generating function is finite near zero. Lemma 3.3 gives the generic diagonal-tensor argument. Our real criterion therefore matches the statistical model exactly. The paper also discusses a stronger complex generic statement in Remark 3.4; that must not be silently substituted for the real criterion.

### 1. Explicit diagonal sufficient criterion at every even order

Let d be even with d at least 4, and let

\[
T=\sum_{i=1}^n\lambda_i e_i^{\otimes d},
\]

where the real numbers lambda_i are nonzero and all have the same sign. Put

\[
w_i=|\lambda_i|^{-2/(d-2)}.
\]

**Proposition.** Suppose that no nonempty signed subset sum vanishes:

\[
\sum_{i\in I}\varepsilon_i w_i\ne0
\quad\text{for every nonempty }I\subseteq[n]
\text{ and every }\varepsilon_i\in\{-1,1\}.
\]

Then every real orthonormal eigenvector basis of T is a signed permutation of the coordinate basis. Equivalently,

\[
\{Q\in O(n):Q\bullet T\in V_{\mathrm{pmi}}\}=\mathrm{SP}(n).
\]

**Proof.** If v is a unit eigenvector with eigenvalue mu, its coordinates satisfy

\[
\lambda_i v_i^{d-1}=\mu v_i.
\]

The eigenvalue is nonzero: any nonzero coordinate would otherwise force lambda_i=0. On the support of v,

\[
v_i^{d-2}=\mu/\lambda_i.
\]

Because d-2 is even and the entries are real, the right-hand side is positive. Hence

\[
|v_i|=|\mu|^{1/(d-2)}|\lambda_i|^{-1/(d-2)}.
\]

For two real eigenvectors v and u with eigenvalues mu and eta, if their supports overlap in I, then

\[
\langle v,u\rangle
=|\mu\eta|^{1/(d-2)}
\sum_{i\in I}\operatorname{sgn}(v_i u_i)w_i.
\]

The assumed signed-sum condition makes this nonzero. Orthogonal eigenvectors therefore have disjoint supports. An orthonormal basis has n nonempty disjoint supports inside n coordinates, so every support is a singleton. This proves the first claim.

For the equivalence, write the rows of Q as q_1,...,q_n. The conditions `(Q·T)_{ij...j}=0` for i not equal to j say that `T(·,q_j,...,q_j)` is orthogonal to every q_i with i not equal to j. It is therefore parallel to q_j. Thus these conditions mean precisely that the rows of Q are an orthonormal eigenvector basis. ∎

An immediately checkable choice is

\[
w_i=C\,3^i,\qquad C>0.
\]

For a nonempty signed sum, its largest-index term is larger in absolute value than the sum of all smaller-index terms. It cannot cancel. This gives explicit tensors at all even orders, in every finite dimension.

The displayed signed-sum criterion is **sufficient**, not asserted necessary. It concerns the diagonal subspace of V_pmi, not arbitrary PMI tensors. It is a real criterion. For this particular geometric choice of weights, the stronger triangle inequality also rules out cancellation by arbitrary complex unit phases, but that strengthening is not needed for the statistical conclusions.

### 2. Every fixed all-cumulant rotation condition has a finite cutoff

Let s be a fixed centered random vector in R^n with identity covariance and all cumulants. For D at least 3 define

\[
\mathcal R_D(s)=\{Q\in O(n):
Q\bullet\kappa_r(s)\in V_{\mathrm{pmi}}^{r,n}
\text{ for every }3\le r\le D\}.
\]

Write R_infty for the intersection over all D.

**Proposition.** For every fixed cumulant sequence, there exists a finite D(s) such that

\[
\mathcal R_{D(s)}(s)=\mathcal R_\infty(s).
\]

**Proof.** Work in the polynomial ring

\[
A=\mathbb R[q_{11},\ldots,q_{nn}].
\]

For each D let I_D be the ideal generated by the entries of `Q^T Q-I` and the finitely many polynomials

\[
[Q\bullet\kappa_r(s)]_{ij\ldots j},
\qquad i\ne j,\quad3\le r\le D.
\]

The tensor entries of the fixed cumulant sequence are real coefficients. Hence `I_3 <= I_4 <= ...` is an ascending chain of ideals in a Noetherian polynomial ring. Hilbert's basis theorem implies eventual stabilization, so I_D equals the ideal generated by all orders for some finite D. Taking real zero sets gives the claimed equality. No Nullstellensatz, complexification, or compactness approximation is needed. ∎

The algebraic statement does not require an analytic moment-generating function. Analyticity is needed for its statistical interpretation: by source Theorem 2.3, if the cumulant-generating function is finite near zero, then R_infty(s) is exactly the set of orthogonal Q for which Qs is PMI. Orthogonal transformations preserve finiteness of that function near zero.

Consequently, a fixed analytic PMI source identifiable from all cumulants is identifiable from a finite initial cumulant segment. This is an existence theorem for a distribution-dependent cutoff. It does not provide an algorithm that recognizes stabilization from a truncated oracle: equality of two consecutive stage ideals need not imply that later cumulants impose no new restrictions.

### 3. No uniform finite cutoff, with exact delayed-identification examples

Fix n at least 2 and an integer m at least 2. Let gamma be N(0,1). Let He_m be the monic probabilists' Hermite polynomial of degree m. Let nu_m be the probability distribution given by m-point Gauss–Hermite quadrature for gamma.

It has positive weights at the m real roots of He_m, and its moments satisfy

\[
\int x^k\,d\nu_m=\int x^k\,d\gamma,
\qquad0\le k\le2m-1.
\]

Its first differing moment obeys the exact identity

\[
\int x^{2m}\,d\nu_m-\int x^{2m}\,d\gamma=-m!.
\]

#### Quadrature justification and the exact deficit

The standard Gaussian Hermite polynomials are monic and orthogonal, with

\[
\int\mathrm{He}_m(x)^2\,d\gamma(x)=m!.
\]

The normalization follows by comparing coefficients in

\[
\mathbb E\big[e^{tZ-t^2/2}e^{uZ-u^2/2}\big]=e^{tu},
\qquad Z\sim N(0,1).
\]

For completeness, the quadrature rule can be constructed from the real simple roots x_1,...,x_m of He_m. Let ell_j be the degree-(m-1) Lagrange polynomial that is one at x_j and zero at the other nodes, and set `a_j=∫ell_j dgamma`. For every polynomial f of degree at most 2m-1, divide it as `f=q He_m+r`, where q and r have degree at most m-1. Orthogonality gives `∫f dgamma=∫r dgamma`, and interpolation gives `∑a_j f(x_j)=∫r dgamma`. The rule is therefore exact through degree 2m-1. Applying it to ell_j squared gives `a_j=∫ell_j² dgamma>0`; applying it to 1 gives `∑a_j=1`.

Now He_m squared vanishes on the support of nu_m and has leading term x^(2m). Every lower-degree term integrates equally under nu_m and gamma. Thus the degree-2m moment deficit is exactly `-∫He_m² dgamma=-m!`.

The roots, quadrature exactness, positive weights, and Hermite normalization are standard orthogonal-polynomial facts. Authoritative references are NIST DLMF §3.5(v), §18.3, and §18.12:

- https://dlmf.nist.gov/3.5
- https://dlmf.nist.gov/18.3
- https://dlmf.nist.gov/18.12

#### Source distributions

Choose independent coordinates s_1,...,s_n with distributions

\[
\mathcal L(s_i)=(1-\theta_i)\gamma+\theta_i\nu_m,
\qquad
\theta_i=3^{-i(m-1)}.
\]

Each coordinate is centered, has variance one, and has a moment-generating function finite for every real argument. The coordinates are independent and hence PMI. All cumulants of orders 3 through 2m-1 vanish.

Cumulants are not generally linear under mixtures. Here the relevant identity is valid because all moments below order 2m already agree with the Gaussian. In the cumulant-moment polynomial, the highest moment has coefficient one and the remaining terms depend only on lower moments. It follows that

\[
\kappa_{2m}(s_i)=-m!\,\theta_i.
\]

Independence makes the full order-2m tensor diagonal:

\[
\kappa_{2m}(s)
=-m!\sum_{i=1}^n3^{-i(m-1)}e_i^{\otimes2m}.
\]

Its coefficients have the same nonzero sign. The weights in Proposition 1 are

\[
|\kappa_{2m}(s_i)|^{-1/(m-1)}
=(m!)^{-1/(m-1)}3^i.
\]

They have no vanishing signed subset sums. Thus

\[
\mathcal R_{2m}(s)=\mathrm{SP}(n).
\]

On the other hand, the mean, covariance, and cumulants through order 2m-1 are exactly those of a standard Gaussian vector. Every orthogonal rotation preserves them, so

\[
\mathcal R_D(s)=O(n)\qquad\text{for every }D<2m
\]

(with mean and covariance included). Since n is at least 2, O(n) is strictly larger than SP(n). Therefore **the smallest sufficient cumulant cutoff for this source distribution is exactly 2m**.

Given any proposed uniform cutoff D, choose m with 2m greater than D. The resulting analytic, standardized, independent source is identifiable in the PMI model from cumulants, but its cumulants through order D contain no information about the whitening rotation. No finite cutoff depending only on n can suffice for all identifiable analytic PMI sources.

This concerns exact identifiability from cumulants. It provides no numerical stability bound, sample complexity, or general distributional classification.

### Concrete sixth-order example

For m=3, nu_3 assigns masses 1/6, 2/3, and 1/6 to `-sqrt(3), 0, sqrt(3)`. In dimension two choose theta_1=1/9 and theta_2=1/81. Then both coordinates have mean zero and variance one, cumulants of orders 3, 4, and 5 vanish, and

\[
\kappa_6(s_1)=-2/3,\qquad
\kappa_6(s_2)=-2/27.
\]

The weights are in the ratio 1:3, so the sixth cumulant identifies the orthogonal source axes in the PMI model. Every summary through order five remains invariant under all rotations.

### Verification and status

`verify_quadrature.py` supplies exact rational checks for m=2,3,4,5,8,10, with four differently weighted independent coordinates in each case. It computes quadrature moments without approximate roots: the moment of x^k under nu_m is the Gaussian expectation of the remainder of x^k modulo He_m. It verifies moment matching, the deficit -m!, vanishing lower cumulants, and the displayed first nonzero cumulants. The outputs are `exact_controls.json` and `exact_controls.log`. These are finite checks of the construction; the arguments above prove it for every m and n.

For the Noetherian input, see the Stacks Project's definition and Hilbert basis theorem in §10.31:

https://stacks.math.columbia.edu/tag/00FM

Suggested ledger entries are **Q1001: explicit all-even-order sufficient criterion on diagonal tensors** and **Q1002: distribution-dependent finite determination, with an explicit proof that no uniform cutoff exists**. Both original classification questions remain open at their exact statement scopes.


## 12. Q1156 and Q1157 — complete line-realization subcases

**B7 / Q1156 / stable ID `48ec50411ade2c1537dd`.** Exact retained statement:

> For each fixed k≥1, characterize exactly the finite maps f that admit such a nearest-neighbor realization in Euclidean R^k.

**B7 / Q1157 / stable ID `cc68108ee4fc5b3d3ebc`.** Exact retained statement:

> For each fixed k≥1, characterize the pairs (f,g) realizable in some metric space that admit a simultaneous realization in Euclidean R^k.

Date: 2026-10-07.

Q1156 stable statement ID: `48ec50411ade2c1537dd`.

Exact retained statement: For each fixed k≥1, characterize exactly the finite maps f that admit such a nearest-neighbor realization in Euclidean R^k.

Q1157 stable statement ID: `cc68108ee4fc5b3d3ebc`.

Exact retained statement: For each fixed k≥1, characterize the pairs (f,g) realizable in some metric space that admit a simultaneous realization in Euclidean R^k.

**Status: partial for both full questions.** The results below settle the dimension-one subcase constructively. They retain the source's strict requirement that every distance between distinct unordered pairs be different. Dimensions two and higher remain unresolved by this argument.

Primary source for definitions and question scope: Žarko Ranđelović, *Minimal and Maximal Distances in Metric Spaces*, arXiv:2409.14648v3, 5 July 2025, Introduction and final section: https://arxiv.org/pdf/2409.14648 . The source treats general metric realizability and fixed-dimensional Euclidean questions; no claim of priority for the elementary one-dimensional observations below is made.

### 1. Nearest-neighbor maps on the line

Let \(f:[n]\to[n]\) have no fixed points, and form the undirected graph
\[
H_f=([n],\{\{i,f(i)\}:i\in[n]\}).
\]

**Theorem L1.** The following are equivalent:

1. \(f\) is realizable by distinct points on \(\mathbb R\), with all unordered pair distances different.
2. Every connected component of \(H_f\) is a path.

If realizable, there is an integer realization with every coordinate in
\([0,2^{n-1}-1]\). Thus the certificate uses \(O(n)\) bits per coordinate. The graph criterion and the construction run in polynomial time.

**Necessity.** Order the realized points from left to right. A point's nearest neighbor must be one of its immediate neighbors in this order. Hence \(H_f\) is a subgraph of the spanning path through the ordered points and is a disjoint union of paths.

**Sufficiency.** Every component has at least two vertices because \(f\) has no fixed point. A finite functional digraph has exactly one directed cycle in each weak component. A path has no undirected cycle, so this directed cycle must be one mutually nearest pair. Every other arrow points along the path toward this pair; following arrows must reach its sole cycle.

Choose an orientation of each component path and concatenate the component lists. Assign a positive gap to every adjacent pair in this total order. Inside each component, give the central mutual-pair edge the smallest gap, then make gaps strictly increase as one moves away from it in either direction. Give every intercomponent gap a value larger than every within-component gap.

These requirements form an acyclic ordering of the \(n-1\) gaps. Choose a total order extending it and assign the distinct numbers \(2^0,2^1,\ldots,2^{n-2}\) as gap sizes in that order. Each vertex now prefers exactly the neighbor prescribed by \(f\). A nonadjacent point is farther than an adjacent point in its direction. At component ends the intercomponent gap exceeds the within-component choice.

Set the leftmost coordinate to zero and obtain all others by partial sums of these gaps. Each pair distance is the sum of a nonempty interval of gaps. Distinct unordered pairs yield distinct subsets of the distinct powers of two, hence distinct sums by uniqueness of binary expansion. The total diameter is \(2^{n-1}-1\). ∎

This gives an exact certificate procedure rather than a numerical embedding test.

#### A strict dimension obstruction missed by indegree alone

With zero-based labels, let
\[
f=(1,0,1,2,2).
\]
Every vertex has indegree at most two and the only directed cycle is \(0\leftrightarrow1\), but \(H_f\) has degree three at vertex 2. Theorem L1 excludes a line realization.

The same map is realized in \(\mathbb R^2\) by
\[
(0,0),\quad(10,0),\quad(22,0),\quad(34,2),\quad(22,13).
\]
Its ten squared pair distances, in lexicographic pair order, are
\[
100,\ 484,\ 1160,\ 653,\ 144,\ 580,\ 313,\ 148,\ 169,\ 265.
\]
They are all different and give exactly the displayed nearest-neighbor map. Thus the indegree bound alone is not sufficient even in the line subcase.

### 2. Simultaneous nearest and farthest maps on the line

Here is a complete finite criterion using only a vertex order and linear inequalities. It is more explicit than the original Euclidean realization condition, and is an exact decision algorithm for the one-dimensional subcase.

For each permutation \(\pi=(\pi_1,\ldots,\pi_n)\), introduce adjacent gaps \(d_1,\ldots,d_{n-1}\). Put
\[
x_{\pi_1}=0,\qquad x_{\pi_j}=\sum_{h<j}d_h,\qquad L=\sum_{h=1}^{n-1}d_h.
\]
Discard the permutation unless every \(f(\pi_j)\) is an immediate neighbor of \(\pi_j\) in this order and every \(g(\pi_j)\) is one of the endpoints \(\pi_1,\pi_n\), distinct from \(\pi_j\).

For a retained order, impose the following rational linear inequalities:

- \(d_h\ge1\) for every \(h\).
- At each interior point with \(f(\pi_j)=\pi_{j-1}\), impose \(d_j-d_{j-1}\ge1\); if \(f(\pi_j)=\pi_{j+1}\), impose \(d_{j-1}-d_j\ge1\).
- If \(g(\pi_j)=\pi_n\), impose \(L-2\sum_{h<j}d_h\ge1\).
- If \(g(\pi_j)=\pi_1\), impose \(2\sum_{h<j}d_h-L\ge1\).

**Theorem L2.** A simultaneous line realization exists if and only if one of these \(n!\) systems is feasible over \(\mathbb Q\) (equivalently, over \(\mathbb R\)).

**Proof.** In any ordered line realization the nearest point is adjacent, the farthest point is an endpoint, and the side of the midpoint determines which endpoint is farther. These are exactly the strict homogeneous inequalities underlying the displayed system. Finitely many strict positive margins can be scaled so that all are at least one. This proves necessity.

Conversely, any feasible solution yields the desired nearest and farthest choices with positive margins. Its feasible region has an open neighborhood on which all underlying strict inequalities remain true. Equality of two different pair distances is one proper rational hyperplane in the gap variables: the corresponding two interval sums have different coefficient vectors. Finitely many proper hyperplanes cannot cover this open neighborhood, and rational points are dense there. Choose a rational point outside all of them. This gives all pair distances different while preserving the two maps. Scaling clears denominators if integer coordinates are desired. Rational linear feasibility is equivalent to real feasibility for these rational systems, for example by the existence of rational basic solutions or rational points in the underlying open cone. ∎

The enumeration takes \(n!\) rational linear feasibility checks of polynomial input size; compatible path orders and endpoint restrictions can reduce it. This does not imply a polynomial algorithm in \(n\), and no such complexity claim is made. It also does not solve the fixed-dimensional questions for \(k\ge2\).

### 3. Computation scope

`verify_metric_line.py` enumerates every fixed-point-free map on \(n=3,4,5,6\) labeled vertices. Every map satisfying the path criterion is supplied with the explicit binary-gap integer construction and checked by direct pair-distance comparisons. The planar obstruction above is checked using exact squared distances. The proof of Theorem L1 supplies necessity, so the finite computation is a constructor check, not an exhaustive Euclidean nonrealizability solver. Theorem L2 is a written algorithmic equivalence; no large linear-program census is claimed.


## 13. Q607–Q613 — trace reductions, exact decisions and source audit

**B7 / Q607 / stable ID `2ebcfe72585b1be70fc9`.** Exact retained statement:

> For each fixed retention probability p∈(0,1), is there C_p<∞ such that every unknown x∈{0,1}^n can be recovered exactly with probability at least 2/3 from n^{C_p} deletion traces? There is no computational-time restriction in this sample-complexity question.

**B7 / Q608 / stable ID `16cdc05113faa8ab347d`.** Exact retained statement:

> For fixed p∈(0,1), can worst-case exact deletion-trace reconstruction achieve quasipolynomial sample size and runtime, succeeding with probability≥2/3 for every n-bit source? Full reconstruction is required, not pairwise distinguishing.

**B7 / Q609 / stable ID `9144c2582d1e2c9c3b3a`.** Exact retained statement:

> For every fixed deletion probability δ∈(0,1), can a uniformly random unknown X∈{0,1}^n be reconstructed exactly from (log n)^{Oδ(1)} independent deletion traces, with success probability 1−o_n(1) over X and the channel? No polynomial-time condition is added.

**B7 / Q610 / stable ID `8a00508df67e6fbcd058`.** Exact retained statement:

> In the source’s insertion–deletion channel R_p, at each step copy the current input bit with probability 1−p, delete it with probability p/2, or insert a uniform random bit with probability p/2 without advancing. For fixed sufficiently small p>0 and uniform S∈{0,1}^n, can its near-linear-time reconstruction theorem be extended to edit error O(εpn), for arbitrary ε>0, using poly(1/ε) traces and success probability at least 1−1/n? Runtime is near-linear in n for fixed p,ε.

**B7 / Q611 / stable ID `472e43724c08d9837feb`.** Exact retained statement:

> In generalized trace reconstruction, a hidden vector p∈[0,1]^n first emits independent Bernoulli(p_i) bits, then each bit is deleted with fixed probability δ∈(0,1). If all p_i lie in {0,1/k,…,1}, what is the minimax number of traces for recovering p to ℓ∞ error below 1/(2k), with probability at least 2/3? In particular, can superpolynomial-in-n lower bounds persist for a fixed k≥2?

**B7 / Q612 / stable ID `4c25b9b7f68a9602ba33`.** Exact retained statement:

> For fixed retention p∈(0,1) and fixed TV accuracy ε∈(0,1/2), can a distribution D supported on at most ℓ unknown n-bit strings be learned to TV error ε, with success at least 2/3, using both exp(~O(n^(1/5) poly(ℓ))) traces and time? A trace first samples x∼D and then independently deletes bits of x; component labels and repeat observations of a chosen component are unavailable.

**B7 / Q613 / stable ID `c302289d6bd6215ff58d`.** Exact retained statement:

> Let A receive n and one δ-deletion trace of x, and output an n-bit estimate. Determine the sharp asymptotic values of L_worst(δ,n)/n and L_avg(δ,n)/n, where L_worst(δ,n)=sup_A inf_x E[LCS(A(trace,n),x)] and L_avg(δ,n)=sup_A E_{X uniform}[LCS(A(trace,n),X)] for fixed δ, already at δ=0.1 or 0.9. Here LCS denotes longest-common-subsequence length, and A is deterministic, as in the source definitions.

Date: 2026-10-07. Scope: Q607–Q613 from the supplied B7 handoff. The results below were derived in this session; novelty relative to all literature is not asserted. No theorem about Q738 or Q742 is changed.

### Executive findings

Three rigorous transfer statements substantially sharpen the handoff's scope accounting.

1. **Rational retention is not an essential barrier in Q608.** A full reconstruction algorithm with quasipolynomial samples and runtime for each fixed rational retention yields one with the same complexity class for every fixed real retention. Independent trace-length calibration followed by rational thinning proves this without an oracle for the real retention. The source decoder still needs independent validation.
2. **The claimed Family 122 one-trace lower bound would also refute Q609.** A worst-case hard pair can be embedded as rare blocks in a uniform source. An exact genie argument proves that a superpolynomial one-trace indistinguishability bound forces every polylogarithmic-trace average-case exact decoder to have success tending to zero. Thus the handoff's direct-statement nonmatch should not be mistaken for a logical nonimplication.
3. **The Q611 lower-bound transfer holds on every two-point emission alphabet.** It is not confined to vectors with deterministic 0/1 emissions. In particular, an eventual validated binary lower bound transfers to the interior grid `{1/k,2/k}` for every fixed `k >= 3`.

There is also a complete finite-dimensional solution of the average-case part of Q613: the Bayes-optimal deterministic decoder is independent of the retention probability, and its value is an explicit Bernstein polynomial whose coefficients are exact integer LCS optimizations. Exhaustive computations through length eight are included. These are finite exact values, not asymptotic constants.

The underlying Family 122 lower bound and rational decoder have **not** been independently proved or compiled here. Public source access reached the comparator statements and formalization documentation but not the actual companion proof bodies or PDF text. The results above therefore establish new rigorous implications, not unconditional closures of Q607–Q609 or the superpolynomial part of Q611.

### Question and status mapping

| Question | Stable statement ID | Session result |
| --- | --- | --- |
| Q607 | `2ebcfe72585b1be70fc9` | Full-trace formal statement semantics audited; actual lower-bound proof unverified. |
| Q608 | `16cdc05113faa8ab347d` | Proved rational-to-all-real retention transfer. A validated full rational decoder would settle the stated fixed-real-retention question. |
| Q609 | `9144c2582d1e2c9c3b3a` | Proved hard-pair-to-uniform-source bound. Family 122's stated one-trace theorem, if valid, implies a negative answer. |
| Q610 | `8a00508df67e6fbcd058` | No solution produced; the insertion/deletion accuracy and near-linear runtime target remains separate. |
| Q611 | `472e43724c08d9837feb` | Proved two-point emission reduction, including interior grid points. A simple unconditional exponential upper bound is recorded. Full minimax rate remains unresolved. |
| Q612 | `4c25b9b7f68a9602ba33` | No solution produced; unlabeled population recovery is not supplied by a single-string decoder. |
| Q613 | `c302289d6bd6215ff58d` | Exact Bayes formula and universal-in-retention deterministic decoder; exhaustive average-case values for n=1,...,8. Fixed-noise asymptotic frontier remains unresolved. |

### 1. Formal-source audit

The handoff pins Family 122 to commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. The accessible live `main` comparator has the following semantics:

- A source is a function from `Fin n` to Boolean values.
- A deletion mask independently retains or removes each source position, and the observation is only the ordered list of retained bits.
- The one-trace probability sums over all masks producing a particular complete output. Its total variation includes every output length.
- An estimator receives all complete traces and may randomize arbitrarily over all source words. No runtime restriction is imposed.
- The asymptotic sample lower-bound statement applies to every fixed real deletion probability in `(0,1)`, every fixed positive target success probability, and every positive polynomial exponent.
- The one-trace statement asserts that the minimum TV distance over distinct words of length n is smaller than every inverse polynomial asymptotically.

This is an exact model match for Q607; it is not a mean-only or bounded-statistic formulation. However, all three theorem bodies in the accessible comparator file are placeholders. A comparator statement is not the corresponding proof certificate. The repository supplies separate comparator-checking instructions; those checks were not run. The scope document and comparator are same-origin evidence. The fixed-commit source, actual proof configuration, source manuscript, and rational-decoder proof remain unaudited.

Primary pages inspected:

- [TraceReconstruction comparator](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/TraceReconstruction.lean), declarations `quantitative_sample_lower_bound`, `superpolynomial_one_trace`, and `superpolynomial_sample_complexity`.
- [Family 122 scope](https://github.com/openai/math/blob/main/lean/docs/122.md).
- [Comparator instructions](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/README.md).
- [Generalized trace reconstruction](https://arxiv.org/html/2412.00674v1), Definition 1, Theorem 2, and Section 1.1. This source explicitly asks about discrete probability sets. Its continuous lower bound does not itself establish a fixed-grid theorem.

These `main` observations are not a verification that their contents match the handoff's pinned commit. Failed retrieval is an access limitation, not evidence that a mathematical claim is false.

### 2. Rational-to-real retention theorem for Q608

Write `D_p(x)` for the deletion-trace law of a fixed length-n word with retention probability p.

#### Theorem T1: calibration and thinning

Fix a rational `r in (0,1/2)`. Suppose a finite randomized algorithm `B_r` reconstructs every length-n word from at most `M(n)` independent r-retention traces with error at most `epsilon/3`, and takes at most `T(n)` bit operations, where `0 < epsilon < 1` is fixed. Suppose the sample budget is a known computable bound; unused samples may be discarded.

There is an algorithm using only ordinary p-retention traces, with no input or oracle for p, which works simultaneously for all real `p in [2r,1)`, succeeds with error at most epsilon, and uses

`M + O((n M^2 / epsilon^2 + 1/(n r^2)) log(1/epsilon))`

traces. Its preprocessing bit complexity is polynomial in `n`, `M`, `1/r`, `1/epsilon`, and the logarithms of the numerical counters. Its complete runtime is this polynomial plus `T(n)`.

Consequently, quasipolynomial sample and bit-time bounds at every fixed rational r imply such bounds for every fixed real p. Standard constant amplification changes success 2/3 to `1-epsilon/3` with a constant-factor sample and runtime overhead.

#### Proof

Let

`eta = min(r/2, epsilon/(6 n M))`.

Take an independent calibration batch of

`K = ceil(log(6/epsilon)/(2 n eta^2))`

traces. Let S be their total observed length and let `p_hat=S/(nK)`. The observed lengths are sums of independent Bernoulli(p) deletion-mask indicators, even though the positions of those indicators are not observed. Thus `S ~ Binomial(nK,p)`, independently of the later reconstruction batch. Hoeffding's inequality gives

`Pr(|p_hat-p| > eta) <= 2 exp(-2nK eta^2) <= epsilon/3`.

Choose an integer B with `2^(-B) <= epsilon/(6nM)`. On calibration outcomes with `p_hat <= r`, output an arbitrary word. Otherwise set

`t = 2^(-B) floor(2^B r/p_hat)`.

This is an exactly representable rational in `[0,1]`; each independent t-coin uses B fair random bits. Independently delete each bit of each of M fresh p-retention traces with probability `1-t`. Conditional on the calibration batch, the transformed traces are independent samples from `D_(pt)(x)`.

On the good calibration event, `p_hat >= p-r/2 >= 3r/2`, so the arbitrary-output branch is not taken. Moreover,

`|pt-r| <= p |t-r/p_hat| + r |p-p_hat|/p_hat <= 2^(-B)+eta <= epsilon/(3nM)`.

Couple masks at retentions `pt` and r by common independent uniform random variables at every source position. Each position differs with probability `|pt-r|`. A union bound over all nM positions gives

`TV(D_(pt)(x)^M, D_r(x)^M) <= nM |pt-r| <= epsilon/3`.

Run `B_r` on the transformed traces. The three error contributions are at most epsilon/3 each: calibration failure, deviation from the ideal r-retention input law, and the base decoder's failure under that ideal law. The total error is at most epsilon.

Since `eta^(-2)=max(4/r^2,36 n^2 M^2/epsilon^2)`, the displayed sample bound follows. Counting all input bits costs at most O(nK); thinning costs O(nMB) bit operations plus rational arithmetic on O(B+log(nK)+encoding(r)) bits. All of these are quasipolynomial when M and T are quasipolynomial and r,epsilon are fixed. For an arbitrary fixed p>0, choose and hardcode a rational `r<p/2`. The algorithm need not know p. This proves the claimed quantifier extension. QED.

**Scope limits.** This reduction requires a full reconstruction base algorithm. Pairwise distinguishers do not suffice. It also requires a computationally usable sample and time bound for that base algorithm. The reduction establishes neither ingredient of the Family 122 decoder itself. The squared sample overhead changes constants in the exponent but preserves the quasipolynomial complexity class.

#### Refinement T1.1: only a constant-factor sample overhead for fixed retention and error

The preceding elementary coupling bound is conservative. The same construction actually needs `O_r,epsilon(M)` total traces and `T(n)+O_r,epsilon(nM polylog(nM))` bit operations when r and epsilon are fixed.

For retentions r and s, the one-bit Hellinger affinity is

`a=sqrt(rs)+sqrt((1-r)(1-s))`.

The identities for differences of square roots give

`1-a = [(sqrt(r)-sqrt(s))²+(sqrt(1-r)-sqrt(1-s))²]/2 <= (r-s)²/[2r(1-r)]`.

For any two discrete probability laws P,Q with affinity A, Cauchy–Schwarz gives `TV(P,Q)<=sqrt(1-A²)`. The affinity of N independent masks is `a^N`, so

`TV(Bernoulli(r)^N,Bernoulli(s)^N) <= sqrt(1-a^(2N)) <= sqrt(N)|r-s|/sqrt(r(1-r))`.

Passing from masks to the observed traces cannot increase TV. Apply this with `N=nM`.

Choose a dyadic `eta=2^(-B)` satisfying

`eta <= min(r/2, epsilon sqrt(r(1-r))/(6 sqrt(nM)))`,

with B the smallest nonnegative integer satisfying the inequalities. It is computable by rational comparisons after squaring the second inequality. Use `K=ceil(log(6/epsilon)/(2n eta²))` independent calibration traces and thin the fresh data with `t=2^(-B)floor(2^B r/p_hat)` as before. On good calibration, `|pt-r|<=2eta`, and the last TV bound is at most epsilon/3. Calibration and base-decoder errors are still each at most epsilon/3.

The minimal dyadic choice differs from the displayed minimum by at most a factor two. Hence

`K = O((M/[epsilon² r(1-r)] + 1/(nr²)) log(1/epsilon))`.

For fixed r and epsilon this is O(M). The thinning uses `B=O_r,epsilon(log(nM))` fair random bits per observed bit; the remainder of the arithmetic has polynomial bit complexity in those counter lengths. This proves the sharper bound. In particular, extending the rational decoder to fixed real retention does not require increasing the quasipolynomial exponent even by the earlier quadratic-sample reduction.

### 3. Hard-pair embedding into the uniform prior for Q609

Fix retention p. Let `P_u=D_p(u)` and `P_v=D_p(v)` for two distinct m-bit words. Let `R_avg(n,t)` be the maximum exact-recovery success probability for a uniformly random n-bit source from t traces, with arbitrary computation and with randomized estimators allowed.

#### Theorem T2: an explicit uniform-source upper bound on success

For every `1 <= m <= n`, put `K=floor(n/m)` and

`beta = TV(P_u^t,P_v^t)`.

Then

`R_avg(n,t) <= [1 - 2^(-m)(1-beta)]^K`.

In particular, with `alpha=TV(P_u,P_v)`,

`R_avg(n,t) <= exp(-K 2^(-m) (1-min(1,t alpha)))`.

#### Proof

Partition the first Km source bits into K consecutive blocks of length m. Give a decoder extra observations:

1. all block boundaries in each deletion trace, equivalently the separately labeled deletion trace of every block in every repetition;
2. for each block, whether its value lies in `{u,v}`;
3. the true contents of every block outside `{u,v}`, and the remaining `n-Km` source bits.

Concatenating the per-block traces recreates the original traces, so this enhanced experiment is at least as informative as the original experiment. The original uniform source has independent blocks. The number H of blocks in `{u,v}` has distribution `Binomial(K,2^(1-m))`. Conditional on their identities and all the revealed information, these H blocks remain independent fair choices between u and v. Their t-trace observations are also independent across blocks.

For one such fair binary hypothesis, the optimal probability of exact identification is `s=(1+beta)/2`. For H independent instances, exact reconstruction of all H choices has optimal Bayes success `s^H`. To see this without a heuristic independence assertion, factor the posterior over the H labels; the largest posterior mass of a label vector is the product of the H largest marginal posterior masses, and averaging over the independent data yields the product of their expected maxima.

Therefore the best success in the enhanced experiment is

`E[s^H] = (1-2^(1-m)+2^(1-m)s)^K = [1-2^(-m)(1-beta)]^K`.

The original experiment cannot do better. The usual product coupling gives `beta <= min(1,t alpha)`, and `1-z <= exp(-z)` gives the second inequality. QED.

#### Corollary T2.1: conditional negative answer to Q609

Suppose that for this fixed p, the minimum one-trace TV distance `alpha_m` among distinct m-bit words satisfies

`m^C alpha_m -> 0` for every fixed `C>0`.

For every fixed d and every trace budget `t(n)=O((log n)^d)`,

`R_avg(n,t(n)) -> 0`.

Indeed, take `m=floor((1/2)log_2 n)` and choose a pair attaining `alpha_m`. Then `t(n) alpha_m -> 0`, while `floor(n/m) 2^(-m) -> infinity`. Theorem T2 gives the result. Existence of a minimizing pair is automatic because the set of m-bit word pairs is finite.

The imported Family 122 one-trace theorem has exactly the premise of this corollary for every fixed deletion probability. **If that theorem is validated, Q609 has a negative answer, with success tending to zero for every polylogarithmic budget.** This is stronger than merely ruling out success `1-o(1)`. It is a proved consequence of the claimed premise, not an independent validation of that premise.

### 4. Two-point generalized emission alphabets for Q611

#### Theorem T3: data-processing reduction

Fix `0 <= a < b <= 1`. For a binary source `x`, define the generalized probability vector

`theta_i = a+(b-a)x_i`.

A generalized deletion trace of theta is obtained by taking an ordinary deletion trace of x and independently replacing every retained 0 by a Bernoulli(a) bit, and every retained 1 by a Bernoulli(b) bit.

The claim follows by coupling the same source-position deletion mask and the same independent emission randomness. Emitting before deleting and deleting before emitting have the same observed distribution because the mask is independent of all emissions. Therefore, for every pair x,y,

`TV(G_theta(x),G_theta(y)) <= TV(D_p(x),D_p(y))`,

and the same inequality holds for the joint laws of any fixed number of traces. Any estimator recovering theta with coordinate error strictly below `(b-a)/2` identifies x by nearest-point rounding. Applying the estimator after the described randomization converts it into an ordinary binary reconstruction algorithm with the same sample count and success probability.

For the grid `{0,1/k,...,1}`, any two distinct grid points have separation at least `1/k`; the target error `<1/(2k)` therefore gives the needed rounding. The binary lower bound transfers to every fixed k. For `k>=3`, the two values `a=1/k`, `b=2/k` lie strictly inside `(0,1)`, so deterministic emissions are unnecessary for the transfer. For `k=2`, there is only one interior grid point, so that particular interior-only strengthening is unavailable.

This proves a reduction, not a full minimax formula. In particular, Family 122 would imply a superpolynomial lower bound even on these interior two-point submodels if its ordinary binary lower bound is validated.

#### An unconditional finite-grid upper bound

Keep only traces of length exactly n. The retention event has probability `p^n` and is independent of the Bernoulli emissions. Conditional on being retained, each such trace is a complete independent Bernoulli sample from the unknown grid vector.

With `r0=ceil(2 k^2 log(4n/eta))` complete traces, coordinate means differ from their true probabilities by less than `1/(2k)` simultaneously with probability at least `1-eta/2`, using a harmless strict-inequality adjustment of r0 if needed. Nearest-grid rounding then recovers the vector exactly. Drawing `O(p^(-n)(k^2 log(n/eta)+log(1/eta)))` original traces supplies r0 complete traces with failure at most eta/2 by a binomial concentration bound. The runtime is O(n) times the number of input traces plus rounding work. This is an exponential upper bound, included to make finiteness and the recovery criterion explicit; it does not meet the open minimax target.

### 5. Exact average-case one-trace decision rule for Q613

For a trace y of length m, let `e(y,x)` denote the number of increasing m-position embeddings of y into x. The likelihood of y from a fixed n-bit source x is

`Pr(Y=y | X=x) = e(y,x) p^m (1-p)^(n-m)`.

#### Theorem T4: the optimal Bayes decoder does not depend on retention

For **any fixed prior on length-n sources**, and any fixed decision loss or utility, the posterior given y is independent of `p in (0,1)`: the factor `p^m(1-p)^(n-m)` cancels from Bayes' formula. Thus a deterministic Bayes-optimal decoder, with a fixed tie rule, is simultaneously optimal for all interior retention probabilities. This is a Bayes statement, not a claim about the worst-case minimax decoder.

For the uniform prior,

`Pr(X=x | Y=y) = e(y,x)/(C(n,m) 2^(n-m))`.

The denominator follows by summing over all choices of m retained positions and all `2^(n-m)` assignments to the remaining positions. The average-case LCS optimizer is therefore

`A_n(y) in argmax_(a in {0,1}^n) sum_(x in {0,1}^n) e(y,x) LCS(a,x)`.

Use lexicographic tie-breaking to obtain a deterministic rule, as Q613 requires. Put

`A_(n,m) = sum_(y in {0,1}^m) max_a sum_x e(y,x) LCS(a,x)`

and

`B_(n,m) = A_(n,m)/(C(n,m) 2^n)`.

Then the exact average optimum is

`L_avg(1-p,n) = 2^(-n) sum_(m=0)^n A_(n,m) p^m(1-p)^(n-m)`

`= sum_(m=0)^n C(n,m) B_(n,m) p^m(1-p)^(n-m)`.

All A coefficients are integers and all B coefficients are rational. Moreover, `B_(n,m)` is nondecreasing in m: deleting a uniformly selected symbol from a uniform `(m+1)`-subsequence produces a uniform m-subsequence, so the latter observation is a randomization of the former. A decoder with more information can implement that randomization, and a deterministic Bayes rule is at least as good as the resulting randomized rule. Consequently the average optimal value is nondecreasing in retention p.

#### Exact finite values

The table gives `L_avg(delta,n)/n`. Values are shown in decimal for readability; exact fractions and polynomial coefficients are in `exact_results.json`.

| n | deletion delta=0.1 | deletion delta=0.5 | deletion delta=0.9 |
| --- | ---: | ---: | ---: |
| 1 | 0.9500000000 | 0.7500000000 | 0.5500000000 |
| 2 | 0.9512500000 | 0.7812500000 | 0.6512500000 |
| 3 | 0.9449166667 | 0.7812500000 | 0.6842500000 |
| 4 | 0.9425375000 | 0.7890625000 | 0.7037875000 |
| 5 | 0.9409075000 | 0.7953125000 | 0.7153975000 |
| 6 | 0.9399918411 | 0.8022054036 | 0.7312553828 |
| 7 | 0.9393630670 | 0.8032226563 | 0.7337812455 |
| 8 | 0.9389144101 | 0.8064079285 | 0.7441196812 |

For example, n=2 has Bernstein coefficients `(5/4,3/2,2)`. Hence its expected optimum is `(5/4)(1-p)^2+3p(1-p)+2p^2`. These finite values establish neither existence nor a value for an n-to-infinity limit. No asymptotic numerical extrapolation is asserted.

### 6. Exact computation receipts

The included `exact_trace_checks.py` uses integer embedding multiplicities, exact rational probabilities, and integer LCS utility matrices. It enumerates all sources, all possible traces, and all n-bit output decisions for n up to eight. It has no Monte Carlo component.

Checks completed:

- 62 exact thinning-composition identities, covering all words of lengths 1 through 5 at retentions `3/5` and `2/3`.
- 62 exact commutations of stochastic emission and deletion, using emission probabilities `1/3,2/3`.
- 651 exact pairwise TV contraction comparisons on those generalized-emission laws.
- All posterior-normalization identities for every possible trace through length eight.
- Exhaustive Bayes LCS maximizations and deterministic decoder tables through length eight.
- Exhaustive minimum one-trace TV values for all distinct word pairs through length eight at retention 1/2.

The last minima are respectively `1/2, 1/4, 1/4, 3/16, 3/16, 5/32, 5/32, 35/256`. The output records witness pairs and enumeration counts. These small-n minima do not test a superpolynomial asymptotic theorem.

Artifacts:

- `exact_trace_checks.py`: standalone reproduction script; requires Python and NumPy.
- `exact_results.json`: exact rational results and all polynomial coefficients.
- `bayes_decoders_n1_to_n8.tsv`: an optimal deterministic decision for every trace of every source length from one through eight.

### 7. Next decisive proof work

The most valuable remaining source check is the actual Family 122 lower-bound proof and its formal comparison configuration at the pinned commit. A successful independent validation would simultaneously settle Q607 negatively, imply a negative Q609 by Theorem T2, and establish the fixed-grid superpolynomial lower-bound subquestion in Q611 by Theorem T3.

For Q608, a successful audit of the claimed rational full decoder plus Theorem T1 would settle the stated all-real fixed-retention question. An oracle for noncomputable p is unnecessary. The base algorithm must genuinely output the source, use the original complete-trace model, and satisfy a bit-time bound; efficient pairwise testing does not meet that requirement.

For Q613, the exact posterior and finite optimization provide a reproducible starting point for analytic upper/lower bounds on the Bernstein coefficients. A small-n numerical trend alone cannot settle the requested asymptotic frontier, and the worst-case deterministic minimax objective remains a separate problem.


## 14. A failed isospectral-to-homometric encoding

**B7 / Q2025 / stable ID `35437229265179fdf70c`.** Exact retained statement:

> Do nonisometric isospectral spherical orbifolds exist in any dimension 2≤d≤4?

**B7 / Q2032 / stable ID `d54894e53caf916054e2`.** Exact retained statement:

> Do isospectral spherical space forms with nonisomorphic fundamental groups exist in any dimension d≡1 (mod 4)?

**B7 / Q2134 / stable ID `d7d72638df3bb1201dc2`.** Exact retained statement:

> For every odd d≥5, must each maximum-volume pair of nonisometric isospectral spherical space forms consist of lens spaces?

Date: 2026-10-07. This is a method-level result requested by the handoff's proposed continuation, not a new closure of a registered spectral-geometry question.

**Result: the specific signed-weight transfer fails.** The nonisometric, function-isospectral lens spaces
\[
L(11;1,2,3),\qquad L(11;1,2,4)
\]
have associated signed weight sets in \(\mathbb Z/11\mathbb Z\)
\[
A=\{1,2,3,8,9,10\},\qquad B=\{1,2,4,7,9,10\}
\]
which are not homometric. No change of generator of the cyclic group repairs this failure.

### 1. Exact objects

Let \(\zeta=e^{2\pi i/11}\). The cyclic group generated by
\[
\operatorname{diag}(\zeta,\zeta^2,\zeta^3)
\quad\text{or}\quad
\operatorname{diag}(\zeta,\zeta^2,\zeta^4)
\]
acts on the unit sphere \(S^5\subset\mathbb C^3\). Every nonidentity power has no eigenvalue one because 11 is prime and the weights are nonzero. Thus both actions are free, and the quotients are smooth spherical space forms with fundamental group \(\mathbb Z/11\mathbb Z\).

The pair is classical: Ikeda, *On lens spaces which are isospectral but not isometric*, Annales scientifiques de l'École Normale Supérieure 13 (1980), 303–315, §4(I)(i), printed p. 313, lists \(L(11;1,2,4)\) and \(L(11;1,2,8)\). His Theorem 2.1, p. 309, permits independent sign changes; \(8\equiv-3\pmod{11}\) gives the displayed pair. Primary source: https://www.numdam.org/item/10.24033/asens.1384.pdf . The calculations below independently verify the relevant spectra and weight invariants rather than relying only on that identification.

### 2. A finite certificate of equality of the entire function spectrum

Complexifying the six-dimensional real representation gives weights \(A\), respectively \(B\). An invariant monomial with exponent vector \(\alpha\in\mathbb N^6\) satisfies
\[
\sum_j w_j\alpha_j\equiv0\pmod{11}.
\]
Let \(a_m(w)\) count such monomials of total degree \(m\). Write each exponent uniquely as \(\alpha_j=11\beta_j+r_j\), with \(0\le r_j\le10\). This proves the exact rational generating-function identity
\[
\sum_{m\ge0}a_m(w)z^m
=\frac{P_w(z)}{(1-z^{11})^6},
\quad
P_w(z)=\sum_{\substack{r\in\{0,\ldots,10\}^6\\w\cdot r\equiv0\pmod{11}}}z^{\sum r_j}.
\]
The numerator has degree at most 60. `verify_lens_homometry.py` computes all 61 coefficients of both numerators using two independent exact algorithms: a residue dynamic program, and direct enumeration of five residues with the sixth solved by a modular inverse. Each direct computation examines exactly \(11^5=161051\) solutions. Both methods give
\[
P_A(z)=P_B(z).
\]
The complete coefficient arrays are in `lens_homometry_certificate.json`. This is a certificate for every degree, since the entire common denominator is known; it is not a truncated eigenvalue comparison.

The ordinary polynomial space decomposes as harmonic polynomials plus the invariant squared-radius times lower-degree polynomials. Therefore the multiplicity generating function of spherical harmonics on each quotient is
\[
(1-z^2)\frac{P_w(z)}{(1-z^{11})^6}.
\]
Degree-\(m\) harmonics give the eigenvalue \(m(m+4)\) on \(S^5\). Equality of these rational functions proves equality of every function-Laplacian eigenvalue multiplicity. This agrees with Ikeda's spectral generating-function criterion, equations (2.1)–(2.3), printed pp. 309–310.

### 3. Nonisometry and failure of homometry

An isometry between these spherical quotients lifts to an orthogonal map on their simply connected universal cover \(S^5\). It conjugates the two cyclic actions, possibly changing the cyclic generator by a unit \(u\in(\mathbb Z/11\mathbb Z)^\times\). Hence isometry would require the signed weight multiset equality \(uA=B\). All ten unit images are recorded in the certificate, and none equals \(B\). This proves nonisometry.

The cyclic difference counts \(C_A(t)=\#\{(a,a')\in A^2:a-a'=t\}\) and \(C_B(t)\), for \(t=0,\ldots,10\), are

| Set | Exact difference-count vector |
|---|---|
| \(A\) | \((6,4,3,2,3,3,3,3,2,3,4)\) |
| \(B\) | \((6,2,3,5,1,4,4,1,5,3,2)\) |

They already disagree at \(t=1\), with values four and two. More strongly, the multiset of offzero values for \(B\) contains one and five, while that for \(A\) contains neither. Multiplication by a unit permutes the nonzero shifts; translation preserves the counts and inversion reverses them. Thus no unit change, translation, or reflection can make the two signed weight sets homometric.

### 4. Exact question boundaries

- **Q2025**, stable ID `35437229265179fdf70c`, asks: “Do nonisometric isospectral spherical orbifolds exist in any dimension 2≤d≤4?” This experiment has dimension five, so it is a **scope-nonmatch** for that exact target.
- **Q2032**, stable ID `d54894e53caf916054e2`, asks: “Do isospectral spherical space forms with nonisomorphic fundamental groups exist in any dimension d≡1 (mod 4)?” Both groups here are cyclic of order eleven, so it is a **scope-nonmatch**.
- **Q2134**, stable ID `d7d72638df3bb1201dc2`, asks: “For every odd d≥5, must each maximum-volume pair of nonisometric isospectral spherical space forms consist of lens spaces?” The pair supplies no maximum-volume comparison in every dimension, so it is a **scope-nonmatch**.

The precise conclusion concerns this specific signed-eigenweight encoding. It does not rule out every possible construction from isospectral geometry to cyclic homometry, and it does not establish a reduction between the registered questions.

### 5. Evidence

Written arguments identify the full Hilbert numerator as a finite certificate of the infinite spectrum, and explain the isometry test. Exact computations supply every numerator coefficient, every unit image, and both difference vectors. A separate implementation of the difference-count test is in `trace/lens_autocorrelation_check.py`. A repeated-weight control \((1,-1,1,-1,1,-1)\) fails the numerator equality first at degree two. No stochastic search or proof-assistant compilation is involved.


## 15. Verification record, reproducibility and limitations

The exact finite computations described above actually ran. A final integrated replay of fourteen certificate-producing or certificate-checking jobs passed; its complete commands, exit codes, durations and output paths are preserved in the receipt. It independently reconstructed the bivariate exceptional minors, verified the 494-dimensional modular minor from separate Wick formulas, regenerated the real Gaussian family controls, checked the critical Gabor polynomial examples, regenerated all trace tables and collision controls, checked the quadrature construction, reconstructed line embeddings, and checked the lens Hilbert numerators and cyclic difference arrays. The cube portion of this integrated replay rechecked the BFS witness and capacity certificate and audited the archived complete search logs.

The original six-cube computations exhaustively excluded every cardinality 8 through 12. A distinct exhaustive engine repeated size 8. For sizes 9–12, the entire search space was not repeated with another independent engine: the independent controls are the full five-prefix symmetry census, the known positive resolving path through the pruning code, the integer histogram checks and the complete-log audit. This limitation accompanies the proposed lower bound. The ZIP includes the source and a complete replay path so the higher-cardinality census can be repeated.

Written theorems are not inferred from bounded experiments. The tree argument uses an integral resultant ideal certificate; the bivariate moment proof uses a published complete triple-point theorem and exact exceptions; the generic Gauss proof is symbolic in every degree; the Gabor classification and critical criterion use functional analysis and explicit Zak calculations; the cumulant and collision results have all-order proofs. Finite checks support those arguments.

The verification archive preserves failed controls and exploratory non-evidence where relevant. In particular, the timed-out unsharded size-12 run is not used to exclude anything; the sixteen completed shards supply that exclusion. Unsuccessful heuristic searches at sizes 13 and 14 do not prove nonexistence. The repeated-weight lens control fails equality as intended. Incorrect tree charges, failed critical division, and exact independent formula comparisons are recorded in their respective outputs.

Every reported phase-retrieval result uses the infinite rectangular lattice and complex \(L^2(\mathbb R)\), with global phase as the equivalence. Every moment-variety result distinguishes dimension, finite fibers and one-to-one fibers. The stability lower bound concerns Wasserstein distance of mixing measures on component parameter space, and deterministic moment perturbations. It is not a finite-sample statistical lower bound. The trace reductions use complete deletion traces, while the Bayes calculation uses a fixed prior and does not settle deterministic worst-case minimax recovery.

### What was not available or not performed

The original catalog and previous private proof packets were not accessible. Their accepted decisions were taken only from the supplied handoff. The Family 122 manuscript and actual formal proof at the pinned commit were not independently verified, and no Lean theorem was compiled. Public source pages describing that work are same-origin evidence. The untouched questions did not receive comprehensive fresh literature searches. No claim of publication priority is made for any derivation or elementary subcase.

## 16. Most decisive next mathematical steps

1. **Q740:** establish the reverse dimension inequality throughout the target range. The orthogonal action now explains the entire proposed defect; what remains is to rule out additional generic tangent dependencies.
2. **Q741:** classify smooth points outside the coprime finite-parameter image and their Gauss fibers. The generic hypothesis needed for the identifiability application is already proved, but this exceptional-locus step is essential for the literal all-fibers question.
3. **Q1766:** complete sizes 13 and 14, or construct a resolving set of one of those sizes. The archive provides exact histogram machinery, symmetry coverage and a positive 15-set control. A failed heuristic is insufficient.
4. **Trace lane:** validate the actual Family 122 proof and full rational decoder. A valid one-trace lower bound would feed the proved rare-block and emission reductions, while a valid full rational decoder would feed the calibration theorem. These are mathematical implications, not assumed resolutions.
5. **Q1001–Q1002:** move from explicit diagonal criteria to necessary and sufficient conditions on general PMI tensors and dependent source laws. A universal fixed cumulant cutoff is now excluded; a distribution-sensitive criterion or effective stopping rule is the appropriate remaining target.
6. **Accepted mixture results:** study optimal stability exponents and constructive inversion under explicit separation conditions. The collision construction supplies a necessary exponent restriction without proving an attainable rate.

The other registered problems remain distinct research lanes. In particular, the proposed numbering Q2483, stable ID 952a31b8ef8e3b9b0e60, is preserved as provisional and was not folded into the finite-dimensional algebraic work.

## 17. Primary-source comparison catalog

The following catalog records the precise dependencies used, not a complete bibliography or an exhaustive priority search. Published sources are linked rather than redistributed. The supplied handoff is included verbatim, with its SHA-256 recorded. Source versions and theorem locations are also in the JSON ledger and source_catalog.json.


### S01. Supplied B7 handoff

2026-10-07. **Location:** Exact statement register, historical accepted decisions, Family 122 lead, return contract. **Use and comparison:** Supplied input; historical decisions preserved, not re-audited.

### S02. Ya-Nan Zheng, On the Hyperdeterminants of Steiner Distance Hypermatrices

[EJCombin 32(2), P2.30 (2025)](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v32i2p30/pdf/). **Location:** Theorems 2 and 4, printed pp. 2–3; equation (1), p. 4. **Use and comparison:** Raw homogeneous-resultant normalization and composition law checked.

### S03. Cooper–Du, Determinants of Steiner Distance Hypermatrices

[v1, 2025](https://arxiv.org/html/2505.10501v1). **Location:** Section 1, tensor equations. **Use and comparison:** Compatible convention; tree independence is not used in our Q17 proof.

### S04. Ciliberto–Miranda, Linear Systems of Plane Curves with Base Points of Equal Multiplicity

[Trans. AMS 352 (2000), 4037–4050; arXiv text](https://arxiv.org/pdf/math/9804018). **Location:** Conjecture 2.2, Theorems 2.4 and 5.2; PDF pp. 4, 5 and 13. **Use and comparison:** Multiplicity-three classification yields only (d,k)=(3,2),(4,2),(6,5).

### S05. Améndola–Ranestad–Sturmfels, Algebraic Identifiability of Gaussian Mixtures

[v2](https://arxiv.org/pdf/1612.01129v2). **Location:** Example 19, p. 13; Table 2 and Conjecture 21, p. 14. **Use and comparison:** Fourth-order defect target and earlier numerical n=8,k=11 result.

### S06. Blomenhofer–Casarotti, Nondefectivity of invariant secant varieties

[v2](https://arxiv.org/html/2312.12335v2). **Location:** Theorem 3.6; Definition 4.9, Theorem 4.10 and Remark 4.11. **Use and comparison:** Nondefectivity range and the strict/generic Gauss-map wording distinction.

### S07. Blomenhofer, Gaussian Mixture Identifiability from degree 6 Moments

[arXiv PDF inspected 2026-10-07](https://arxiv.org/pdf/2307.03850). **Location:** Proposition 2.8, pp. 8–9; Proposition 2.13, p. 11. **Use and comparison:** Tangent formula and earlier finite-degree contact calculation; our all-degree proof is separate.

### S08. Massarenti–Mella, Bronowski's conjecture and the identifiability of projective varieties

[v3](https://arxiv.org/pdf/2210.13524). **Location:** Theorem 1.5, printed p. 3; Definition 2.2 and Remark 2.3, p. 5. **Use and comparison:** The identifiability criterion requires the generic Gauss condition.

### S09. Wellershoff, On a dense set of functions determined by sampled Gabor magnitude

[v2, 17 April 2026](https://arxiv.org/html/2507.14556v2). **Location:** Section 2.3, Corollary 3. **Use and comparison:** Finite Hermite combinations are unique among all complex L2 competitors at lower density greater than one.

### S10. Phasebook

[arXiv PDF inspected 2026-10-07](https://arxiv.org/pdf/2505.15351). **Location:** Question 8.8, printed p. 33. **Use and comparison:** Q1749 norm-category target.

### S11. Borichev–Gröchenig–Lyubarskii, Gaussian Gabor frame bounds

[arXiv PDF inspected 2026-10-07](https://arxiv.org/pdf/0909.4937). **Location:** Theorem A, printed p. 2. **Use and comparison:** The Gaussian rectangular-lattice frame condition ab<1.

### S12. Benedetto–Heil–Walnut, Differentiation and the Balian–Low theorem

[Primary PDF inspected 2026-10-07](https://heil.math.gatech.edu/papers/blt.pdf). **Location:** Theorem 2.2(b), printed p. 363. **Use and comparison:** Gabor incompleteness when ab>1.

### S13. NIST DLMF, Jacobi triple product

[Live reference inspected 2026-10-07](https://dlmf.nist.gov/20.5.E9). **Location:** Section 20.5, equation 20.5.9. **Use and comparison:** Product identity used to locate the unique simple Gaussian Zak zero.

### S14. Allikvere, The edge multiset dimension of hypercubes

[v1, August 2026](https://arxiv.org/pdf/2608.09983). **Location:** Table 1, Proposition 10; Section 10, Open problem 1. **Use and comparison:** Published six-cube interval 6–15 and exact 15-landmark witness.

### S15. Ribot–Seigal–Zwiernik, Beyond independent component analysis: identifiability and algorithms

[v1](https://arxiv.org/html/2510.07525v1). **Location:** Theorem 2.3; Section 3, eigenvector/action definitions; Lemma 3.3 and Remark 3.4. **Use and comparison:** Real O(n) matches the statistical model; analytic all-cumulant PMI equivalence.

### S16. NIST DLMF, Gaussian quadrature and Hermite polynomials

[Live reference inspected 2026-10-07](https://dlmf.nist.gov/3.5). **Location:** Section 3.5(v); also https://dlmf.nist.gov/18.3 and https://dlmf.nist.gov/18.12. **Use and comparison:** Quadrature facts; the report also supplies the exactness, positivity and deficit proofs.

### S17. Stacks Project, Noetherian rings

[Live reference](https://stacks.math.columbia.edu/tag/00FM). **Location:** Section 10.31, Hilbert basis theorem. **Use and comparison:** Finite-variable polynomial rings over R are Noetherian.

### S18. Ranđelović, Minimal and Maximal Distances in Metric Spaces

[v3, 5 July 2025](https://arxiv.org/pdf/2409.14648v3). **Location:** Introduction and final section. **Use and comparison:** Strict pair-distance convention and fixed-dimensional targets.

### S19. Ikeda, On lens spaces which are isospectral but not isometric

[Ann. ENS 13 (1980), 303–315](https://www.numdam.org/item/10.24033/asens.1384.pdf). **Location:** Theorem 2.1, p. 309; equations (2.1)–(2.3), pp. 309–310; Section 4(I)(i), p. 313. **Use and comparison:** Classical lens pair, sign equivalence and full harmonic generating-function criterion.

### S20. OpenAI Family 122 trace comparator

[Live main inspected 2026-10-07](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/TraceReconstruction.lean). **Location:** quantitative_sample_lower_bound, superpolynomial_one_trace, superpolynomial_sample_complexity. **Use and comparison:** Exact model match; comparator contains theorem placeholders. Actual proof and pinned commit not validated.

### S21. OpenAI Family 122 scope note

[Live main inspected 2026-10-07](https://github.com/openai/math/blob/main/lean/docs/122.md). **Location:** Scope. **Use and comparison:** Same-origin claim of superpolynomial lower bound, not independent proof evidence.

### S22. OpenAI comparator instructions

[Live main inspected 2026-10-07](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/README.md). **Location:** Comparator verification workflow. **Use and comparison:** No Lean compilation or comparator proof check was run in this return.

### S23. Rivkin–Valiant–Valiant, A Generalized Trace Reconstruction Problem

[v1](https://arxiv.org/html/2412.00674v1). **Location:** Definition 1, Theorem 2 and Section 1.1. **Use and comparison:** Generalized emission model and finite-grid question.

### S24. Henriksson–Ranestad–Seccia–Yu, Moment varieties of the inverse Gaussian and gamma distributions are nondefective

[v3; J. Symbolic Computation 132 (2026), 102460](https://arxiv.org/html/2409.18421v3). **Location:** Section 3, equation (3.1); beginning of Section 4. **Use and comparison:** Gamma and inverse Gaussian moment formulas, not a new audit of accepted Q742.


## Appendix A. Complete exact statements and scope profiles

These are the exact retained texts from the supplied register. Contextual definitions, observation models and quantifiers are preserved separately rather than silently expanded into the statement text.


### Q17

**B7 / Q17 / stable ID `3e7e1834fd713fe73a83`.** Exact retained statement:

> For a tree T and even k≥2, form D_(k)(T) with entry indexed by (v_(1),…,v_(k)) equal to the edge-count of the smallest subtree containing those vertices. Does 2^(k−1)−1 always divide its symmetric hyperdeterminant?

**Return decision:** proved. Stronger divisor for every tree and every order k>=2.

**Object class:** Finite trees T and even tensor orders k≥2.

**Invariant or observation map:** Steiner-distance tensor D_(k)(T): each ordered k-tuple maps to the edge count of its spanning subtree; take its symmetric hyperdeterminant.

**Target equivalence:** Integer divisibility by 2^(k−1)−1; no object-reconstruction equivalence is imposed.

**Generic or uniform scope:** Uniform over every finite tree and every even k≥2.

**Noise and loss:** Exact integer data; divisibility, with no stochastic noise or approximation loss.

**Measurement count:** The full |V(T)|^k-entry tensor, followed by one symmetric hyperdeterminant; no sampling budget.

**Source status from handoff:** catalog disposition: No exact closure in catalog ledger; collector status verbatim: Search-qualified status: Cooper–Du (2025) resolves tree-independence of the determinant, not this divisibility statement. No proof/disproof found in targeted searches.

### Q20

**B7 / Q20 / stable ID `9ba5075d118c04918d6d`.** Exact retained statement:

> Are K_(1),K_(2),K_(3), two isolated vertices, and the three-vertex path the only graphs H for which a graph G’s adjacency spectrum always determines whether G contains an induced H?

**Return decision:** unresolved. No new analysis or status promotion in this return.

**Object class:** Finite graphs G and candidate finite induced subgraphs H.

**Invariant or observation map:** Complete adjacency eigenvalue multiset of G maps to the truth value of containing an induced H.

**Target equivalence:** Equality of adjacency spectra must preserve induced-H containment; classify H up to graph isomorphism.

**Generic or uniform scope:** Uniform over all G for each H; classify all H with this property.

**Noise and loss:** Exact spectra and exact Boolean containment; no noise.

**Measurement count:** All adjacency eigenvalues with multiplicity; no truncated-spectrum or sample budget.

**Source status from handoff:** catalog disposition: No exact closure in catalog ledger; collector status verbatim: Search-qualified status: Author’s March 2025 CV lists the relevant manuscript in preparation. The June 2025 Barranca–Barrus paper treats double stars, not this classification. No resolving later work found.

### Q101

**B7 / Q101 / stable ID `06c3626cd7abe261f06c`.** Exact retained statement:

> Do identical forced-minor sets imply that two finite graphs have homeomorphic geometric realizations?

**Return decision:** unresolved. No new analysis or status promotion in this return.

**Object class:** Geometric realizations of finite graphs, using finite cozero covers and their intersection graphs.

**Invariant or observation map:** Set of forced graph minors: H is forced when some finite cozero cover has every refinement intersection graph containing H as a minor.

**Target equivalence:** Homeomorphism of geometric realizations.

**Generic or uniform scope:** Uniform implication for every pair of finite graphs with identical forced-minor sets.

**Noise and loss:** Exact equality of the whole forced-minor set; no noise or approximate loss.

**Measurement count:** Complete forced-minor set, allowing all finite cozero covers and refinements; no finite cutoff.

**Source status from handoff:** catalog disposition: No exact closure in catalog ledger; collector status verbatim: Status evidence for this section, checked 5 October 2026: The dissertation explicitly leaves this unresolved. Searches by author, thesis title, and the specialized forced-minor/topological-invariant terminology found no later proof or counterexample. No independent recent openness declaration was located; current-status confidence is therefore moderate.

### Q169

**B7 / Q169 / stable ID `2db69aae8c225ff910dd`.** Exact retained statement:

> For fixed k≥2 and sufficiently large n=kq+1, is the maximum kth adjacency eigenvalue among connected outerplanar n-vertex graphs the spectral radius of the fan K₁ joined to a (q−1)-vertex path? Must every extremizer have a cut vertex leaving k disjoint such fans?

**Return decision:** unresolved. No new analysis or status promotion in this return.

**Object class:** Connected outerplanar graphs on n=kq+1 vertices.

**Invariant or observation map:** The kth largest adjacency eigenvalue, maximized over the graph class; compare with the spectral radius of K₁ joined to a (q−1)-vertex path.

**Target equivalence:** Exact extremal value and structural characterization of every extremizer by a cut vertex and k fan components.

**Generic or uniform scope:** For every fixed k≥2 and all sufficiently large admissible n=kq+1; structural conclusion for all extremizers.

**Noise and loss:** Exact spectral optimization; no noise or approximation loss.

**Measurement count:** One specified adjacency eigenvalue per graph, with full graph structure for the extremizer clause; no sample budget.

**Source status from handoff:** catalog disposition: No exact closure in catalog ledger; collector status verbatim: Status evidence, checked 5 October 2026: The 2025 associated paper proves the leading asymptotic and the k=2 cases; its general exact description remains conjectural. Targeted later searches found no general resolution.

### Q337

**B7 / Q337 / stable ID `3f57476cd8727d99a539`.** Exact retained statement:

> For a finite simple graph $G$, a degree-associated card is the pair $(G-v,d_G(v))$, with $G-v$ unlabeled. Let $\operatorname{drn}(G)$ be the smallest size of a submultiset of these cards that occurs in no nonisomorphic graph’s degree-associated deck. Are there only finitely many isomorphism classes of trees $T$ with $\operatorname{drn}(T)=3$?

**Return decision:** unresolved. No new analysis or status promotion in this return.

**Object class:** Finite trees, with degree-associated cards defined for finite simple graphs.

**Invariant or observation map:** Degree-associated deck: the multiset of pairs (unlabeled G−v,d_G(v)); drn(G) is the minimum size of a card submultiset excluding all nonisomorphic graphs.

**Target equivalence:** Graph isomorphism; finiteness of tree isomorphism classes having drn(T)=3.

**Generic or uniform scope:** All finite trees; card consistency is tested against nonisomorphic finite simple graphs.

**Noise and loss:** Exact unlabeled vertex-deleted cards with original vertex degrees; no noise.

**Measurement count:** Three cards for the target drn(T)=3, with minimality requiring failure of every smaller identifying submultiset.

**Source status from handoff:** catalog disposition: No exact closure in catalog ledger; collector status verbatim: Status, checked 5 October 2026: Borzooei–Shadravan, Transactions on Combinatorics 14(1) (2025), pp. 31–43 (online February 2024), explicitly recalls the Barrus–West conjecture and proves the unicentroidal case (Theorems 1.3–1.4). Its conclusion is restricted to unicentroidal trees, leaving the bicentroidal case of this conjecture untreated. Targeted searches through the check date found no full proof or counterexample. Edge-reconstruction and adversary reconstruction results concern different parameters and were not treated as resolutions. The latest direct supporting primary source is this 2025 partial result, not a claim of exhaustive literature coverage.

### Q400

**B7 / Q400 / stable ID `c406d4b9e0c3a2b80408`.** Exact retained statement:

> Does every such pair (α,β) admit a constant C=C(α,β)>0, independent of m, such that E_m(α,β)≤C exp(−2π√((α−β)m)) for every integer m≥1?

**Return decision:** unresolved. No new analysis or status promotion in this return.

**Contextual definition:** For fixed −1≤β<α<0, let E_m(α,β)=inf_{p,q} sup_{0<x≤1} |x^α−p(x)/q(x)|/x^β, where p and q are real polynomials of degree at most m and p/q has no pole in (0,1].

**Object class:** Negative powers x^α on (0,1] with fixed −1≤β<α<0, approximated by real rational functions p/q of numerator and denominator degree at most m.

**Invariant or observation map:** Weighted best rational-approximation error E_m(α,β)=inf_(p,q) sup_(0<x≤1) |x^α−p(x)/q(x)|/x^β, excluding poles in (0,1].

**Target equivalence:** Uniform root-exponential upper bound in approximation degree; no reconstruction equivalence.

**Generic or uniform scope:** Every fixed pair −1≤β<α<0 admits its own C(α,β)>0, uniformly for all integers m≥1.

**Noise and loss:** Weighted uniform error on (0,1]; target C exp(−2π√((α−β)m)); no observation noise.

**Measurement count:** Degree bounds deg p,deg q≤m; error is over the entire interval, not a finite set of measurements.

**Source status from handoff:** catalog disposition: No exact closure in catalog ledger; collector status verbatim: Status, checked 5 October 2026: The primary joint preprint labels this exact estimate Conjecture 2, and arXiv still lists only its May 2023 submission. Searches for the authors, paper identifier, weighted negative-power approximation and conjecture found no proof or counterexample through 2026-10-05. A later quantum-relative-entropy algorithm paper cites this work but was not used as an independent assertion of openness. The classic unweighted positive-power asymptotic quoted in the thesis is a different statement. Current openness is supported by the explicit source and a negative resolution search, not an independent recent open-status affirmation.

### Q607

**B7 / Q607 / stable ID `2ebcfe72585b1be70fc9`.** Exact retained statement:

> For each fixed retention probability p∈(0,1), is there C_p<∞ such that every unknown x∈{0,1}^n can be recovered exactly with probability at least 2/3 from n^{C_p} deletion traces? There is no computational-time restriction in this sample-complexity question.

**Return decision:** unresolved. Exact-model comparator audited; underlying Family 122 proof remains unverified.

**Object class:** Unknown deterministic binary strings of length n.

**Invariant or observation map:** Independent deletion traces: each bit is retained with fixed known probability p∈(0,1), preserving order.

**Target equivalence:** Exact equality of the source string.

**Generic or uniform scope:** Worst case over every n-bit string, for each fixed retention p; success at least 2/3; unrestricted computational time.

**Noise and loss:** Deletion-channel randomness; exact-recovery error probability at most 1/3.

**Measurement count:** At most n^{C_p} independent traces for some finite exponent depending only on p.

**Source status from handoff:** catalog disposition: No exact closure in catalog ledger; unverified candidate answer; collector status verbatim: Status for question 607, checked 5 October 2026: July 2026 gives exp(p^(−7/3)(log₂ n)^c) samples, improving the obsolete exp(Õ(n^(1/5))) bound but remaining superpolynomial; it reports an Ω̃(n^(3/2)) lower bound. No polynomial solution or superpolynomial lower bound located.; recorded lead: OpenAI 122: candidate negative answer. Superpolynomial exact worst-case sample lower bound; selected Lean lower-bound scope.

### Q608

**B7 / Q608 / stable ID `16cdc05113faa8ab347d`.** Exact retained statement:

> For fixed p∈(0,1), can worst-case exact deletion-trace reconstruction achieve quasipolynomial sample size and runtime, succeeding with probability≥2/3 for every n-bit source? Full reconstruction is required, not pairwise distinguishing.

**Return decision:** partial. Rational-to-real retention reduction, now with constant-factor sample overhead.

**Object class:** Unknown deterministic binary strings of length n.

**Invariant or observation map:** Independent deletion traces with fixed known retention p∈(0,1).

**Target equivalence:** Exact full reconstruction of the source string.

**Generic or uniform scope:** Worst case over all source strings for each fixed p; success at least 2/3; both sample count and runtime quasipolynomial.

**Noise and loss:** Deletion-channel randomness; exact-recovery error probability at most 1/3.

**Measurement count:** Quasipolynomially many traces and quasipolynomial runtime in n; pairwise distinguishing alone does not meet the target.

**Source status from handoff:** catalog disposition: No exact closure in catalog ledger; collector status verbatim: Status for question 608, checked 5 October 2026: July 2026 version checked; no later revision or runtime solution located. Efficient pairwise tests and restricted-string results do not solve full reconstruction.; recorded lead: OpenAI 122: candidate subcase. Full decoder with sample and bit-time bounds for fixed known rational retention; align unrestricted question parameter model before promotion.

### Q609

**B7 / Q609 / stable ID `9144c2582d1e2c9c3b3a`.** Exact retained statement:

> For every fixed deletion probability δ∈(0,1), can a uniformly random unknown X∈{0,1}^n be reconstructed exactly from (log n)^{Oδ(1)} independent deletion traces, with success probability 1−o_n(1) over X and the channel? No polynomial-time condition is added.

**Return decision:** partial. Hard-pair embedding proves a conditional negative consequence; premise unverified.

**Object class:** Uniformly random binary source X∈{0,1}^n.

**Invariant or observation map:** Independent deletion traces with fixed deletion probability δ∈(0,1), conditional on the same source X.

**Target equivalence:** Exact equality of the reconstructed and sampled source strings.

**Generic or uniform scope:** Every fixed δ; average over uniform X and channel randomness; success 1−o_n(1); no polynomial-time condition.

**Noise and loss:** Deletion-channel randomness; vanishing average exact-recovery error.

**Measurement count:** (log n)^{O_δ(1)} independent traces.

**Source status from handoff:** catalog disposition: No exact closure in catalog ledger; collector status verbatim: Status for question 609, checked 5 October 2026: July 2026 still reports exp(Õ((log n)^(1/5))) versus Ω̃((log n)^(5/2)). Its worst-case improvement is not established for the shifted oracle. No polylogarithmic solution located.; recorded lead: OpenAI 122: scope nonmatch. Average-case, insertion–deletion, unlabeled-mixture and one-trace LCS targets differ from the inspected deterministic-word statements.

### Q610

**B7 / Q610 / stable ID `8a00508df67e6fbcd058`.** Exact retained statement:

> In the source’s insertion–deletion channel R_p, at each step copy the current input bit with probability 1−p, delete it with probability p/2, or insert a uniform random bit with probability p/2 without advancing. For fixed sufficiently small p>0 and uniform S∈{0,1}^n, can its near-linear-time reconstruction theorem be extended to edit error O(εpn), for arbitrary ε>0, using poly(1/ε) traces and success probability at least 1−1/n? Runtime is near-linear in n for fixed p,ε.

**Return decision:** unresolved. No new result for insertion/deletion accuracy and runtime.

**Object class:** Uniformly random binary source S∈{0,1}^n under the source channel R_p.

**Invariant or observation map:** At each step R_p copies the current input bit with probability 1−p, deletes it with p/2, or inserts a uniform bit with p/2 without advancing.

**Target equivalence:** Approximate reconstruction measured by edit distance to S.

**Generic or uniform scope:** Fixed sufficiently small p>0, arbitrary ε>0, and uniform S; success at least 1−1/n; runtime near-linear in n for fixed p,ε.

**Noise and loss:** Insertion/deletion and inserted-bit randomness; edit error O(εpn).

**Measurement count:** poly(1/ε) independent traces; near-linear runtime in n for fixed p,ε.

**Source status from handoff:** catalog disposition: No exact closure in catalog ledger; collector status verbatim: Status for question 610, checked 5 October 2026: No resolution located. Later deletion-only few-trace/one-trace results and the Chase–Peres constant-trace existence theorem do not supply this accuracy and runtime guarantee.; recorded lead: OpenAI 122: scope nonmatch. Average-case, insertion–deletion, unlabeled-mixture and one-trace LCS targets differ from the inspected deterministic-word statements.

### Q611

**B7 / Q611 / stable ID `472e43724c08d9837feb`.** Exact retained statement:

> In generalized trace reconstruction, a hidden vector p∈[0,1]^n first emits independent Bernoulli(p_i) bits, then each bit is deleted with fixed probability δ∈(0,1). If all p_i lie in {0,1/k,…,1}, what is the minimax number of traces for recovering p to ℓ∞ error below 1/(2k), with probability at least 2/3? In particular, can superpolynomial-in-n lower bounds persist for a fixed k≥2?

**Return decision:** partial. Two-point emission reduction, including an interior grid pair; minimax rate remains.

**Object class:** Probability vectors p∈{0,1/k,…,1}^n, with particular interest in fixed k≥2.

**Invariant or observation map:** Each trace independently emits Bernoulli(p_i) bits at all positions and then deletes each emitted bit with fixed probability δ∈(0,1).

**Target equivalence:** Recovery of the ordered probability vector; ℓ∞ error below half the grid spacing permits exact coordinatewise rounding.

**Generic or uniform scope:** Minimax over all grid vectors, success at least 2/3; ask whether superpolynomial-in-n lower bounds persist at fixed k.

**Noise and loss:** Fresh Bernoulli-emission and deletion randomness; ℓ∞ error strictly below 1/(2k).

**Measurement count:** Determine the minimax number of traces as a function of n,k,δ; no runtime target is specified.

**Source status from handoff:** catalog disposition: No exact closure in catalog ledger; collector status verbatim: Status for question 611, checked 5 October 2026: No finite-grid resolution located. The July 2026 theorem covers deterministic strings, not fixed k≥2 stochastic emission grids.; recorded lead: OpenAI 122: conditional consequence. Grid includes 0/1 vectors. Sup-norm accuracy <1/(2k) rounds to the deterministic word. Source lower bound thus persists for every fixed k≥2 if valid; full minimax rate not supplied.

### Q612

**B7 / Q612 / stable ID `4c25b9b7f68a9602ba33`.** Exact retained statement:

> For fixed retention p∈(0,1) and fixed TV accuracy ε∈(0,1/2), can a distribution D supported on at most ℓ unknown n-bit strings be learned to TV error ε, with success at least 2/3, using both exp(~O(n^(1/5) poly(ℓ))) traces and time? A trace first samples x∼D and then independently deletes bits of x; component labels and repeat observations of a chosen component are unavailable.

**Return decision:** unresolved. No new result for unlabeled population recovery.

**Object class:** Distributions D supported on at most ℓ unknown binary strings of length n.

**Invariant or observation map:** Each trace draws a fresh latent x∼D and applies independent deletions with fixed retention p; latent component labels and chosen-component repeat access are unavailable.

**Target equivalence:** Recovery of D as a distribution on strings, measured in total variation; component-list order is irrelevant.

**Generic or uniform scope:** Uniform over all such D for fixed p∈(0,1) and fixed ε∈(0,1/2); success at least 2/3.

**Noise and loss:** Latent sampling plus deletion randomness; total-variation error at most ε.

**Measurement count:** Both traces and runtime bounded by exp(~O(n^(1/5) poly(ℓ))).

**Source status from handoff:** catalog disposition: No exact closure in catalog ledger; collector status verbatim: Status for question 612, checked 5 October 2026: No solution located. July 2026 solves a single-string sample obstacle, not mixture recovery. Probability-string models differ; known n^{Ω(ℓ)} lower bounds preclude a casual poly(n,ℓ) replacement.; recorded lead: OpenAI 122: scope nonmatch. Average-case, insertion–deletion, unlabeled-mixture and one-trace LCS targets differ from the inspected deterministic-word statements.

### Q613

**B7 / Q613 / stable ID `c302289d6bd6215ff58d`.** Exact retained statement:

> Let A receive n and one δ-deletion trace of x, and output an n-bit estimate. Determine the sharp asymptotic values of L_worst(δ,n)/n and L_avg(δ,n)/n, where L_worst(δ,n)=sup_A inf_x E[LCS(A(trace,n),x)] and L_avg(δ,n)=sup_A E_{X uniform}[LCS(A(trace,n),X)] for fixed δ, already at δ=0.1 or 0.9. Here LCS denotes longest-common-subsequence length, and A is deterministic, as in the source definitions.

**Return decision:** partial. Exact Bayes formula and complete finite computation through n=8; asymptotics remain.

**Object class:** Length-n binary strings under either worst-case or uniform-source evaluation.

**Invariant or observation map:** One δ-deletion trace and n are given to a deterministic algorithm returning an n-bit estimate.

**Target equivalence:** Decision fidelity given by longest-common-subsequence length between estimate and source.

**Generic or uniform scope:** Sharp asymptotic normalized optimum for each fixed δ, both supremum-over-algorithms worst-case and uniform-average criteria; already δ=0.1 or 0.9.

**Noise and loss:** One deletion trace; expected LCS utility, normalized by n; algorithms are deterministic in the retained definitions.

**Measurement count:** Exactly one trace; no computational-time restriction is added.

**Source status from handoff:** catalog disposition: No exact closure in catalog ledger; collector status verbatim: Status for question 613, checked 5 October 2026: No sharp fixed-noise frontier located. High-noise and small-noise asymptotics do not settle the stated constants; multiple-trace reconstruction has a different observation budget.; recorded lead: OpenAI 122: scope nonmatch. Average-case, insertion–deletion, unlabeled-mixture and one-trace LCS targets differ from the inspected deterministic-word statements.

### Q738

**B7 / Q738 / stable ID `2f577a87fee1b2c95e2d`.** Exact retained statement:

> For arbitrary k, is the complexified moment map of k-component univariate Gaussian mixtures, with unknown means, variances and weights summing to 1, generically one-to-one modulo component permutation from moments m_1,…,m_{3k}? Equivalently, is the model rationally identifiable at order 3k? Algebraic finite-fiber identification at 3k−1 and rational identification at 3k+2 are established; these are not the target.

**Return decision:** proved. Imported accepted generic identification; new collision-stability obstruction.

**Object class:** Complexified k-component univariate Gaussian mixtures with unknown means, variances, and weights summing to 1.

**Invariant or observation map:** Moment parameterization to raw moments m_1,…,m_{3k}.

**Target equivalence:** Mixture parameter tuples modulo component permutation; generic one-to-one fibers, equivalently rational identifiability.

**Generic or uniform scope:** Arbitrary k; algebraic generic identifiability in the complexified model, rather than a statement about every exceptional tuple.

**Noise and loss:** Exact moments; no stability, statistical noise, or finite-sample loss in the retained target.

**Measurement count:** First 3k moments; m_0=1 is normalization. Orders 3k−1 and 3k+2 are context, not the target budget.

**Source status from handoff:** catalog disposition: Ledger closed: proved; collector status verbatim: Status for question 738, checked 5 October 2026: Reaffirmed by Henriksson et al.(2025); the general 3k threshold remains unresolved in checked sources.; exact ledger decision: proved; scope statement; checked 2026-10-06.; recorded lead: BKS ledger: proved. Generic rational identification of k univariate Gaussian components from moments 1..3k, modulo permutation, via an isolated-contact lemma and a non-weak-defectivity criterion. Scope: The stated complex generic target; not every exceptional parameter and not a stable recovery algorithm.

### Q739

**B7 / Q739 / stable ID `3e3c622525036c1e9a43`.** Exact retained statement:

> For every d≥2,k≥1, is dim Sec_k(G_{2,d})=min{binom(d+2,2)−1,6k−1}?

**Return decision:** proved. Full nondefectivity formula for every d>=2,k>=1.

**Object class:** The complex projective variety G_{2,d} of bivariate Gaussian moments through degree d and its kth secant variety; component covariance matrices vary separately.

**Invariant or observation map:** Mixture moment parameterization and the dimension of Sec_k(G_{2,d}).

**Target equivalence:** Equality with the specified expected dimension min{binom(d+2,2)−1,6k−1}; no uniqueness quotient is asserted.

**Generic or uniform scope:** Every d≥2 and k≥1; dimension is an algebraic generic-rank property of the whole secant variety.

**Noise and loss:** Exact algebraic moment coordinates; no noise or approximate loss.

**Measurement count:** binom(d+2,2) projective moment coordinates including the constant coordinate, through total degree d; no sample budget.

**Source status from handoff:** catalog disposition: No exact closure in catalog ledger; collector status verbatim: Status for questions 739, 740, checked 5 October 2026: No resolution found in bounded follow-up searches through 2026-10-05.

### Q740

**B7 / Q740 / stable ID `b69755d99b945371b6be`.** Exact retained statement:

> For n≥8,r≥3,k=n+r and P=k n(n+3)/2+k−1≤binom(n+4,4)−1, is dim Sec_k(G_{n,4})=P−binom(r−1,2)?

**Return decision:** partial. Universal defect lower bound, exact n=8,k=11 dimension, positive real ambiguity family.

**Object class:** The complex projective variety G_{n,4} of n-variate Gaussian moments through degree 4 and its kth secant, with separately unknown component covariances.

**Invariant or observation map:** Fourth-order mixture moment parameterization and dimension of Sec_k(G_{n,4}).

**Target equivalence:** The precise secant dimension P−binom(r−1,2), rather than parameter identifiability.

**Generic or uniform scope:** All n≥8,r≥3,k=n+r satisfying P=k n(n+3)/2+k−1≤binom(n+4,4)−1.

**Noise and loss:** Exact algebraic moment data; no noise or numerical-stability claim.

**Measurement count:** All binom(n+4,4) projective moment coordinates through degree 4, including the constant coordinate.

**Source status from handoff:** catalog disposition: No exact closure in catalog ledger; collector status verbatim: Status for questions 739, 740, checked 5 October 2026: No resolution found in bounded follow-up searches through 2026-10-05.

### Q741

**B7 / Q741 / stable ID `f344e3bf779aac637144`.** Exact retained statement:

> For all d≥5 and n≥2, does V=GM_d(C^n)=closure{[exp(ℓ+q/2)]_d:ℓ∈S¹(C^n),q∈S²(C^n)} have a nondegenerate tangent map? Precisely, must T:P(V_reg)→Gr(dimV,S^d(C^n)), [v]↦T_vV, have finite fibers? The unresolved extension is beyond the proved degrees 5,…,9; [·]_d means the homogeneous degree-d part.

**Return decision:** partial. Generic Gauss finiteness in every degree; full smooth-locus fibers remain.

**Object class:** Homogeneous Gaussian moment cone GM_d(C^n)=closure{[exp(ℓ+q/2)]_d}, with ℓ linear and q quadratic.

**Invariant or observation map:** Projective tangent map [v]↦T_vV on the regular locus, into the stated Grassmannian.

**Target equivalence:** Every tangent-map fiber finite; this is nondegeneracy, without requiring singleton fibers.

**Generic or uniform scope:** All d≥5,n≥2, with the retained unresolved extension beyond degrees 5,…,9; finite fibers on the specified regular projective locus.

**Noise and loss:** Exact algebraic tangent spaces; no observation noise or loss.

**Measurement count:** Homogeneous degree-d coordinates in S^d(C^n), followed by the tangent space; no finite-sample recovery budget.

**Source status from handoff:** catalog disposition: No exact closure in catalog ledger; collector status verbatim: Status for question 741, checked 5 October 2026: No resolution found in bounded follow-up searches through 2026-10-05.

### Q742

**B7 / Q742 / stable ID `c069b7ff6ff08382c685`.** Exact retained statement:

> For each k≥2, are k-mixtures of gamma distributions and k-mixtures of inverse Gaussian distributions rationally identifiable from their first 3k moments, modulo component permutations? Component parameters and mixture weights are unknown. Rational identifiability refers to generic one-to-one fibers of the complexified moment parameterization; the two positive-support families are one source-conjectured target, not two counts.

**Return decision:** proved. Imported accepted result for both families; new collision-stability obstruction.

**Object class:** For each k≥2, complexified k-component gamma mixtures and k-component inverse Gaussian mixtures with unknown component parameters and weights.

**Invariant or observation map:** First 3k raw moments of the mixture for each of the two families.

**Target equivalence:** Generic one-to-one moment fibers modulo component permutations, equivalently rational identifiability.

**Generic or uniform scope:** Every k≥2 in both families, as one grouped target; algebraic generic scope, not all exceptional or real-positive parameter tuples.

**Noise and loss:** Exact moments; no numerical stability or finite-sample recovery guarantee is included.

**Measurement count:** First 3k moments for each family; the two families constitute one source-conjectured question.

**Source status from handoff:** catalog disposition: Ledger closed: proved; collector status verbatim: Status for question 742, checked 5 October 2026: Explicitly open in v3(2025), published 2026; no later resolution located.; exact ledger decision: proved; scope statement; checked 2026-10-06.; recorded lead: BKS ledger: proved. The same isolated-contact proof gives generic rational identification from 3k moments for gamma and inverse Gaussian mixtures. Scope: Full stated grouped target with the same generic and arithmetic qualifications.

### Q997

**B7 / Q997 / stable ID `8bdda54c021f80a96ef9`.** Exact retained statement:

> For all n, r≥1, d≥3, is dimσ_r(M_{n, d})=max(∑ᵢc_i−1), over integer 0≤c_i≤nr satisfying ∑_{i∈S}c_i≤∑_{λ⊢d, lenλ≤n,λ∩S≠∅}|N_λ| for every S⊆[d]?

**Return decision:** unresolved. No new analysis or status promotion in this return.

**Object class:** Complex projective product moment variety M_{n,d}, with m_α=∏_j μ_(j,α_j), |α|=d, μ_(j,0)=1, and its rth secant.

**Invariant or observation map:** Dimension of σ_r(M_{n,d}) compared with an integer optimization using partition-indexed exponent sets N_λ.

**Target equivalence:** Exact equality with the stated combinatorial maximum; no parameter-reconstruction equivalence.

**Generic or uniform scope:** All n,r≥1 and d≥3; maximum over integer 0≤c_i≤nr satisfying every subset constraint S⊆[d].

**Noise and loss:** Exact algebraic moment coordinates and combinatorial ranks; no noise or approximation loss.

**Measurement count:** All total-degree-d moment coordinates m_α, |α|=d; the formula uses every subset S⊆[d], with no sampling budget.

**Source status from handoff:** catalog disposition: No exact closure in catalog ledger; collector status verbatim: Status for question 997, checked 5 October 2026: No general resolution found through 2026-10-05. Generator-degree questions are separate.

### Q1001

**B7 / Q1001 / stable ID `93986607a1f5ccc79b75`.** Exact retained statement:

> For n≥2,d≥3, characterize T∈V_pmi with a unique orthogonal eigenvector basis up to signs/order; equivalently {Q∈O(n):Q·T∈V_pmi}=SP(n), the signed permutations.

**Return decision:** partial. Explicit sufficient criterion for real even-order diagonal tensors.

**Object class:** Symmetric order-d tensors T∈V_pmi={T:T_(ij…j)=0 for i≠j}, n≥2,d≥3.

**Invariant or observation map:** Orthogonal tensor orbit and its intersection with V_pmi, equivalently orthogonal eigenvector bases.

**Target equivalence:** Signed permutations SP(n): {Q∈O(n):Q·T∈V_pmi}=SP(n).

**Generic or uniform scope:** Exact characterization of all tensors with this uniqueness property, including exceptional cases, for every n≥2,d≥3.

**Noise and loss:** Exact tensor data; no measurement noise or estimation loss.

**Measurement count:** One full symmetric order-d tensor; no finite-sample or truncated-coordinate budget.

**Source status from handoff:** catalog disposition: No exact closure in catalog ledger; collector status verbatim: Status for questions 1001, 1002, checked 6 October 2026: 2026-10-06: no resolution located in bounded searches.

### Q1002

**B7 / Q1002 / stable ID `ddcccae3e3f4fb404ca2`.** Exact retained statement:

> Which PMI source distributions are identifiable from all cumulants jointly, rather than from one generic order? Give the distributional analogue of ICA’s at-most-one-Gaussian rule.

**Return decision:** partial. Finite cutoff for each fixed source; no uniform cutoff, with exact examples.

**Object class:** Centered PMI source distributions satisfying E[s_i|s_j]=0 for i≠j, observed through x=As with A invertible; cumulant-generating function finite near zero.

**Invariant or observation map:** All cumulant tensors jointly; whitening reduces the mixing transformation to an orthogonal one.

**Target equivalence:** Identification of source/mixing representation modulo ICA scaling and permutation, or signed permutation after whitening.

**Generic or uniform scope:** Distributional characterization across PMI sources; an all-orders analogue of ICA’s at-most-one-Gaussian criterion, without imposing a single generic cumulant order.

**Noise and loss:** Exact cumulants of all orders; no sample noise or finite-order estimation guarantee.

**Measurement count:** The full cumulant sequence, with no finite-order cutoff or finite-sample budget.

**Source status from handoff:** catalog disposition: No exact closure in catalog ledger; collector status verbatim: Status for questions 1001, 1002, checked 6 October 2026: 2026-10-06: no resolution located in bounded searches.

### Q1156

**B7 / Q1156 / stable ID `48ec50411ade2c1537dd`.** Exact retained statement:

> For each fixed k≥1, characterize exactly the finite maps f that admit such a nearest-neighbor realization in Euclidean R^k.

**Return decision:** partial. Complete constructive line subcase.

**Object class:** Finite fixed-point-free maps f:[n]→[n], n≥3, and distinct labeled Euclidean points with all distinct-pair distances mutually different.

**Invariant or observation map:** Point configuration maps each label i to the label of its unique nearest other point.

**Target equivalence:** Existence of a realization in R^k; uniqueness of the realizing configuration is not requested.

**Generic or uniform scope:** For each fixed k≥1, exact characterization of all finite maps admitting a realization.

**Noise and loss:** Exact strict distance comparisons with no equal pair distances; no noise or approximate realization.

**Measurement count:** One nearest-neighbor label per vertex; ambient dimension k fixed, with no numerical distance observations.

**Source status from handoff:** catalog disposition: No exact closure in catalog ledger; collector status verbatim: Status for questions 1156, 1157, checked 6 October 2026: Checked 2026-10-06: no resolution located in bounded searches.

### Q1157

**B7 / Q1157 / stable ID `cc68108ee4fc5b3d3ebc`.** Exact retained statement:

> For each fixed k≥1, characterize the pairs (f,g) realizable in some metric space that admit a simultaneous realization in Euclidean R^k.

**Return decision:** partial. Complete line criterion via rational linear feasibility.

**Object class:** Pairs of fixed-point-free maps (f,g) on [n], n≥3, already simultaneously realizable in some metric space with distinct labeled points and mutually distinct pair distances.

**Invariant or observation map:** A configuration records each vertex’s unique nearest and unique farthest other-point labels.

**Target equivalence:** Existence of a simultaneous realization in Euclidean R^k.

**Generic or uniform scope:** For every fixed k≥1, classify all metric-realizable pairs that admit such a Euclidean realization.

**Noise and loss:** Exact strict nearest/farthest relations and mutually distinct pair distances; no noise.

**Measurement count:** Two neighbor labels per vertex, one nearest and one farthest; no finite-distance-value sample budget.

**Source status from handoff:** catalog disposition: No exact closure in catalog ledger; collector status verbatim: Status for questions 1156, 1157, checked 6 October 2026: Checked 2026-10-06: no resolution located in bounded searches.

### Q1324

**B7 / Q1324 / stable ID `b17e6d3142710d3c0f68`.** Exact retained statement:

> If two AL structures are exact symplectomorphic after completion, must the underlying Anosov flows be orbit equivalent? Exact means λ₁=φ*λ₀+df with f constant near infinity; orbit equivalence is a homeomorphism preserving oriented trajectories.

**Return decision:** unresolved. No new analysis or status promotion in this return.

**Object class:** AL structures λ=e^(−s)α₋+e^sα₊ supporting smooth oriented Anosov flows on closed connected oriented 3-manifolds.

**Invariant or observation map:** Associate the completed exact symplectic/Liouville structure to the flow; compare λ₁=φ*λ₀+df with f constant near infinity.

**Target equivalence:** Oriented orbit equivalence: a homeomorphism preserving oriented flow trajectories.

**Generic or uniform scope:** Uniform implication for all pairs of such completed exact-symplectomorphic AL structures.

**Noise and loss:** Exact symplectic equivalence and exact oriented topological orbit equivalence; no noise or metric loss.

**Measurement count:** The whole completed AL structure; no finite measurement or sampling budget.

**Source status from handoff:** catalog disposition: No exact closure in catalog ledger; collector status verbatim: Status for question 1324, checked 6 October 2026: 2026-10-06: retained in July 2026 v2; skewed R-covered case proved.

### Q1456

**B7 / Q1456 / stable ID `2dd40c2f94424a87477d`.** Exact retained statement:

> Must every finite tree T with mdim(T)<∞ satisfy mdim(T)≤|V(T)|−diam(T)+1?

**Return decision:** unresolved. No new analysis or status promotion in this return.

**Object class:** Finite trees T with finite multiset metric dimension.

**Invariant or observation map:** For landmark set S, each vertex v maps to the unordered multiset {d(v,s):s∈S}; mdim(T) is the smallest |S| making all vertices distinct.

**Target equivalence:** Distinct vertices must have distinct distance multisets; target upper bound on the minimum resolving-set size.

**Generic or uniform scope:** Every finite tree with mdim(T)<∞; bound |V(T)|−diam(T)+1.

**Noise and loss:** Exact unweighted graph distances, with landmark labels discarded within each observation multiset; no noise.

**Measurement count:** Optimize the number |S| of landmark distances per vertex; conjectured upper bound |V(T)|−diam(T)+1.

**Source status from handoff:** catalog disposition: No exact closure in catalog ledger; collector status verbatim: Status for question 1456, checked 6 October 2026: Checked 2026-10-06: retained as Problem 3 of the July 2026 survey. Allikvere’s general-graph counterexamples do not settle this tree bound.

### Q1457

**B7 / Q1457 / stable ID `b40e30bbf175d35162cb`.** Exact retained statement:

> What is the computational complexity of deciding, given a finite tree T and an integer k, whether T has an outer multiset resolving set of size at most k?

**Return decision:** unresolved. No new analysis or status promotion in this return.

**Object class:** Finite trees T with an input integer k.

**Invariant or observation map:** Given landmark set S, compare distance multisets {d(v,s):s∈S} only for vertices v outside S.

**Target equivalence:** Decision whether all distinct vertices outside S can be distinguished with |S|≤k; classify computational complexity.

**Generic or uniform scope:** Worst-case decision complexity over arbitrary finite input trees and integers k.

**Noise and loss:** Exact distances and exact decision; no noise.

**Measurement count:** At most k landmarks; resolving requirements apply only to vertices outside the landmark set.

**Source status from handoff:** catalog disposition: No exact closure in catalog ledger; collector status verbatim: Status for question 1457, checked 6 October 2026: Checked 2026-10-06: no tree-case classification located. Later king-grid, toroidal-grid and hypercube resolutions address other questions.

### Q1458

**B7 / Q1458 / stable ID `d7fe39dcb9bb210db7fa`.** Exact retained statement:

> For fixed 1/8<x≤1/2 and (n−1)p=nˣ, is mdim(G(n,p)) finite with probability tending to one as n→∞, where each possible edge is independently present with probability p?

**Return decision:** unresolved. No new analysis or status promotion in this return.

**Object class:** Binomial random graphs G(n,p) with independent edges and (n−1)p=n^x.

**Invariant or observation map:** Multiset metric dimension from unordered distances to landmark sets, using all vertices as the distinguishing target.

**Target equivalence:** Finiteness of the multiset metric dimension, equivalently existence of a resolving landmark set.

**Generic or uniform scope:** For each fixed 1/8<x≤1/2, probability of finiteness tends to one as n→∞.

**Noise and loss:** Randomness is in the graph; conditional on the graph, distances and resolvability are exact.

**Measurement count:** Existence of some finite landmark subset of the n vertices; no fixed cardinality bound requested.

**Source status from handoff:** catalog disposition: No exact closure in catalog ledger; collector status verbatim: Status for question 1458, checked 6 October 2026: Checked 2026-10-06: September 2, 2026 v2 still states the question. Finiteness proved for 0<x≤1/8; infinitude for x>1/2.

### Q1498

**B7 / Q1498 / stable ID `01c8355b5e7fc5532a9c`.** Exact retained statement:

> Is the rate T^(−2/3) as T→∞ optimal, up to logarithms, for the worst-case Hausdorff error in recovering the entire barrier union from these fixed-frequency data when only the stated geometric and process controls are available?

**Return decision:** unresolved. No new analysis or status promotion in this return.

**Object class:** Bounded smooth planar domains with finitely many disjoint smooth closed semipermeable barriers, observed through stationary reflected Brownian motion with positive side-dependent crossing rates.

**Invariant or observation map:** Sampled process X_0,X_t,…,X_(⌊T/t⌋t), with fixed sufficiently small t under the handoff’s geometric, permeability, area, mixing, stationary-density, and connectedness controls.

**Target equivalence:** Recovery of the entire barrier union up to Hausdorff error.

**Generic or uniform scope:** Worst case under only the stated geometric/process bounds, as T→∞ with fixed admissible sampling interval t.

**Noise and loss:** Stochastic diffusion and crossing noise; worst-case Hausdorff error, asking optimality of T^(−2/3) up to logarithmic factors.

**Measurement count:** ⌊T/t⌋+1 fixed-frequency trajectory observations over duration T.

**Source status from handoff:** catalog disposition: No exact closure in catalog ledger; collector status verbatim: Status for question 1498, checked 6 October 2026: Checked 6 October 2026: current preprint and author’s publication list give no matching lower-bound result.

### Q1593

**B7 / Q1593 / stable ID `ec5863144b957427d69c`.** Exact retained statement:

> Do universal C>0 and 0<β<1 exist such that ω(A)≤C(max_i||A_i||_2)β^M for every M>1 and every such A?

**Return decision:** unresolved. No new analysis or status promotion in this return.

**Object class:** Real full-spark matrices A∈R^((2M−1)×M), M>1: every M-row submatrix is nonsingular.

**Invariant or observation map:** ω(A)=min_(|S|=M) σ_min(A_S), normalized against the largest Euclidean row norm.

**Target equivalence:** A uniform exponential upper bound on this scalar stability quantity; no object-reconstruction quotient is imposed.

**Generic or uniform scope:** Universal constants C>0 and 0<β<1 independent of every M and every eligible A.

**Noise and loss:** Exact matrix data; the target is a worst-submatrix singular-value/stability bound, not a noisy recovery risk.

**Measurement count:** 2M−1 rows; ω ranges over all M-row submatrices.

**Source status from handoff:** catalog disposition: No exact closure in catalog ledger; collector status verbatim: Status for question 1593, checked 6 October 2026: general deterministic bound unresolved; Gaussian special case was solved in 2026.

### Q1749

**B7 / Q1749 / stable ID `0c0478553c79951846b2`.** Exact retained statement:

> For fixed a,b>0, is E_Λ meagre or nonmeagre in L²(R) with its norm topology?

**Return decision:** proved. Full category trichotomy and exact critical uniqueness criterion.

**Object class:** Complex signals in L²(R) and a fixed rectangular lattice Λ=aZ×bZ, a,b>0.

**Invariant or observation map:** Magnitudes of the Gaussian-window Gabor transform Gf(x,ω)=2^(1/4)∫f(t)e^(−π(t−x)²)e^(−2πitω)dt on every lattice point.

**Target equivalence:** Signal equality modulo a global unit complex phase; E_Λ is the set whose magnitude fiber is exactly its phase orbit.

**Generic or uniform scope:** For each fixed a,b>0, determine the Baire category of E_Λ in the L² norm topology.

**Noise and loss:** Exact magnitudes, no noise; target meagreness versus nonmeagreness, rather than a numerical recovery loss.

**Measurement count:** The full countably infinite lattice of Gabor magnitudes; no finite truncation.

**Source status from handoff:** catalog disposition: No exact closure in catalog ledger; collector status verbatim: Status for question 1749, checked 6 October 2026: density has substantial positive results (Wellershoff, April 2026 revision); the separate category clause remains unanswered in checked sources.

### Q1766

**B7 / Q1766 / stable ID `84f1767e6fac27a1ca5e`.** Exact retained statement:

> What is the edge multiset dimension of Q₆, the graph on {0,1}⁶ with adjacency at Hamming distance one?

**Return decision:** partial. Computer-assisted interval narrowed to 13–15; exact value remains.

**Object class:** The six-dimensional hypercube Q₆ with vertex set {0,1}⁶ and Hamming-distance-one adjacency.

**Invariant or observation map:** For landmarks S⊆V(Q₆), edge uv maps to the multiset {min(d(u,s),d(v,s)):s∈S}.

**Target equivalence:** Distinguish every pair of edges by their distance multisets; determine the least |S|.

**Generic or uniform scope:** Exact finite value for this one graph, with all edges to be resolved.

**Noise and loss:** Exact graph distances; landmark identities discarded inside each multiset; no noise.

**Measurement count:** Optimize the landmark count |S| among the 64 vertices; each edge supplies |S| distance entries.

**Source status from handoff:** catalog disposition: No exact closure in catalog ledger; collector status verbatim: Status for question 1766, checked 6 October 2026: currently 6≤edim_m(Q₆)≤15.

### Q2025

**B7 / Q2025 / stable ID `35437229265179fdf70c`.** Exact retained statement:

> Do nonisometric isospectral spherical orbifolds exist in any dimension 2≤d≤4?

**Return decision:** unresolved. Lens-to-homometry experiment has dimension five: scope-nonmatch.

**Object class:** Spherical orbifolds S^d/Γ with Γ≤O(d+1) finite and 2≤d≤4, allowing nonfree actions.

**Invariant or observation map:** Full scalar Laplace spectrum, including multiplicities.

**Target equivalence:** Riemannian orbifold isometry; seek a pair sharing the invariant without being isometric.

**Generic or uniform scope:** Existence of such a pair in any of the dimensions 2,3,4.

**Noise and loss:** Exact isospectrality; no noise or spectral approximation.

**Measurement count:** The entire Laplace eigenvalue sequence with multiplicities; no finite spectral cutoff.

**Source status from handoff:** catalog disposition: No exact closure in catalog ledger; collector status verbatim: Status for question 2025, checked 6 October 2026: no low-dimensional resolution located; September space-form examples have different scope.

### Q2032

**B7 / Q2032 / stable ID `d54894e53caf916054e2`.** Exact retained statement:

> Do isospectral spherical space forms with nonisomorphic fundamental groups exist in any dimension d≡1 (mod 4)?

**Return decision:** unresolved. Experiment uses isomorphic cyclic groups: scope-nonmatch.

**Object class:** Curvature-one spherical space forms S^d/Γ with finite free group actions and d≡1 (mod 4).

**Invariant or observation map:** Full scalar Laplace spectrum, with multiplicities.

**Target equivalence:** Fundamental-group isomorphism; seek an isospectral pair whose fundamental groups are nonisomorphic.

**Generic or uniform scope:** Existence in any dimension congruent to 1 modulo 4.

**Noise and loss:** Exact isospectrality and exact group isomorphism distinction; no noise.

**Measurement count:** The complete Laplace spectrum with multiplicities.

**Source status from handoff:** catalog disposition: No exact closure in catalog ledger; collector status verbatim: Status for question 2032, checked 6 October 2026: September nonstrong-isospectral examples have isomorphic groups; no answer to this dimension-restricted question located.

### Q2033

**B7 / Q2033 / stable ID `73618fc79466096402ed`.** Exact retained statement:

> Can two Steklov-isospectral Ω have boundaries with different Laplace–Beltrami spectra?

**Return decision:** unresolved. No new analysis or status promotion in this return.

**Object class:** Compact connected smooth Riemannian manifolds Ω of dimension at least 2 with nonempty smooth boundary.

**Invariant or observation map:** Steklov spectrum from Δu=0 in Ω and ∂νu=σu on ∂Ω; compare the intrinsic Laplace–Beltrami spectra of the boundaries.

**Target equivalence:** Equality of Steklov spectra together with inequality of boundary Laplace–Beltrami spectra, both counted with multiplicity.

**Generic or uniform scope:** Existence of a pair of such manifolds; no genericity or restricted finite family is imposed.

**Noise and loss:** Exact spectral equalities/inequalities; no noise.

**Measurement count:** Complete Steklov and boundary Laplace–Beltrami spectra, with multiplicities.

**Source status from handoff:** catalog disposition: No exact closure in catalog ledger; collector status verbatim: Status for questions 2033, 2034, checked 6 October 2026: no resolutions located; August planar examples and 2026 nodal estimates have different scope.

### Q2034

**B7 / Q2034 / stable ID `53728349aebd91e7cfc3`.** Exact retained statement:

> For each Ω^{d+1}, do c,C>0 exist such that cσ≤H^d(Z(u)∩Ω)≤Cσ for every nonzero real Steklov eigenfunction u with eigenvalue σ>0?

**Return decision:** unresolved. No new analysis or status promotion in this return.

**Object class:** Compact connected smooth Riemannian manifolds Ω^(d+1) with nonempty smooth boundary and nonzero real Steklov eigenfunctions u.

**Invariant or observation map:** Steklov eigenvalue σ and d-dimensional Hausdorff measure of the interior nodal set Z(u)∩Ω.

**Target equivalence:** Two-sided linear nodal-size bound cσ≤H^d(Z(u)∩Ω)≤Cσ; no object-reconstruction equivalence.

**Generic or uniform scope:** For each fixed Ω, constants c,C>0 uniform over every nonzero real eigenfunction with σ>0.

**Noise and loss:** Exact nodal measure and eigenvalue; no stochastic noise or approximation loss.

**Measurement count:** Whole interior nodal set for each eigenfunction, across all positive Steklov eigenvalues; no finite sampling budget.

**Source status from handoff:** catalog disposition: No exact closure in catalog ledger; collector status verbatim: Status for questions 2033, 2034, checked 6 October 2026: no resolutions located; August planar examples and 2026 nodal estimates have different scope.

### Q2092

**B7 / Q2092 / stable ID `c78457588025ba2dcd4d`.** Exact retained statement:

> Is lim_{M→∞} p_M=0?

**Return decision:** unresolved. No new analysis or status promotion in this return.

**Object class:** Random complex matrices A∈C^((4M−5)×M), M≥2, with independent standard complex Gaussian entries.

**Invariant or observation map:** Phaseless linear map x↦|Ax|; p_M is the probability over A that this map is globally injective modulo unit complex scalars.

**Target equivalence:** Global signal equality modulo a unit complex scalar.

**Generic or uniform scope:** Asymptotic probability over the random sensing matrix as M→∞; each injectivity event quantifies over all signals.

**Noise and loss:** Matrix randomness; measurements themselves exact; target lim p_M=0.

**Measurement count:** 4M−5 complex linear measurements followed by magnitudes for dimension M.

**Source status from handoff:** catalog disposition: No exact closure in catalog ledger; collector status verbatim: Status for question 2092, checked 6 October 2026: Li proves p_M<1, leaving the asymptotic part.

### Q2105

**B7 / Q2105 / stable ID `ed3c15822967f6534d5b`.** Exact retained statement:

> For every odd prime p, field k of characteristic p, and finite p-groups G,H, does kG≅kH imply G≅H?

**Return decision:** unresolved. No new analysis or status promotion in this return.

**Object class:** Finite p-groups G,H, every odd prime p, and every coefficient field k of characteristic p.

**Invariant or observation map:** Group algebra G↦kG, with isomorphisms preserving the coefficient field and identity.

**Target equivalence:** Group isomorphism G≅H.

**Generic or uniform scope:** Uniform over all odd primes, characteristic-p fields, and pairs of finite p-groups.

**Noise and loss:** Exact algebra isomorphism; no noise or approximate loss.

**Measurement count:** The whole group algebra, not a truncated augmentation quotient or selected numerical invariants.

**Source status from handoff:** catalog disposition: No exact closure in catalog ledger; collector status verbatim: Status for questions 2105, 2106, 2107, checked 6 October 2026: 2024–2026 work settles specified group classes; bounded searches found no resolutions of these three assertions.

### Q2106

**B7 / Q2106 / stable ID `790cf230288fb810afad`.** Exact retained statement:

> For every prime p, field k of characteristic p, and finite p-groups G,H with kG≅kH, must cl(G)=cl(H)?

**Return decision:** unresolved. No new analysis or status promotion in this return.

**Object class:** Finite p-groups G,H, every prime p, and every field k of characteristic p.

**Invariant or observation map:** Group algebra G↦kG under coefficient-preserving unital isomorphism.

**Target equivalence:** Equality of nilpotency classes, defined by lower central series length.

**Generic or uniform scope:** Uniform over all primes, all characteristic-p fields, and all finite p-group pairs with isomorphic algebras.

**Noise and loss:** Exact algebra isomorphism and exact integer class comparison; no noise.

**Measurement count:** The full group algebra; no finite list of derived invariants is substituted.

**Source status from handoff:** catalog disposition: No exact closure in catalog ledger; collector status verbatim: Status for questions 2105, 2106, 2107, checked 6 October 2026: 2024–2026 work settles specified group classes; bounded searches found no resolutions of these three assertions.

### Q2107

**B7 / Q2107 / stable ID `91432fe0cb2d0ad759e1`.** Exact retained statement:

> For finite groups G,H of odd order, does ZG≅ZH imply G≅H?

**Return decision:** unresolved. No new analysis or status promotion in this return.

**Object class:** Finite groups G,H of odd order.

**Invariant or observation map:** Integral group ring G↦ZG, with coefficient-preserving unital ring isomorphism.

**Target equivalence:** Group isomorphism G≅H.

**Generic or uniform scope:** Uniform over all finite odd-order group pairs.

**Noise and loss:** Exact integral group-ring isomorphism; no noise or approximation loss.

**Measurement count:** The entire integral group ring, with no reduction to selected representations or coefficients.

**Source status from handoff:** catalog disposition: No exact closure in catalog ledger; collector status verbatim: Status for questions 2105, 2106, 2107, checked 6 October 2026: 2024–2026 work settles specified group classes; bounded searches found no resolutions of these three assertions.

### Q2108

**B7 / Q2108 / stable ID `9e1bb75af8f94aaea2d7`.** Exact retained statement:

> Let G be a finite p-group such that F_pG≅F_pH forces G≅H for every finite p-group H. Must FG≅FH force G≅H for every characteristic-p field F and finite p-group H?

**Return decision:** unresolved. No new analysis or status promotion in this return.

**Object class:** Finite p-groups G determined among finite p-groups by their group algebra over F_p.

**Invariant or observation map:** Compare determination by F_pG with determination by FG for an arbitrary characteristic-p field F.

**Target equivalence:** Group isomorphism G≅H among finite p-groups H.

**Generic or uniform scope:** For every G satisfying the prime-field determination hypothesis, every characteristic-p field F, and every finite p-group H.

**Noise and loss:** Exact coefficient-preserving unital algebra isomorphism; no noise.

**Measurement count:** Full group algebra over each field; the field extension is unrestricted in the retained target.

**Source status from handoff:** catalog disposition: No exact closure in catalog ledger; collector status verbatim: Status for question 2108, checked 6 October 2026: September 2026 descent result requires restricted extension degrees; unrestricted determination remains open.

### Q2109

**B7 / Q2109 / stable ID `783798519c45eea8a7ab`.** Exact retained statement:

> If S is a finite nonabelian simple group and G any finite group with cd(G)=cd(S), must G≅S×B for some abelian group B?

**Return decision:** unresolved. No new analysis or status promotion in this return.

**Object class:** Finite nonabelian simple groups S and arbitrary finite groups G.

**Invariant or observation map:** Character-degree set cd(G)={χ(1):χ∈Irr_C(G)}, retaining degrees without multiplicity.

**Target equivalence:** G≅S×B for some finite abelian group B; the abelian factor is not determined by this invariant.

**Generic or uniform scope:** Uniform over every finite nonabelian simple S and every finite G with cd(G)=cd(S).

**Noise and loss:** Exact equality of degree sets; no noise.

**Measurement count:** The full set of complex irreducible-character degrees, without degree multiplicities.

**Source status from handoff:** catalog disposition: No exact closure in catalog ledger; collector status verbatim: Status for question 2109, checked 6 October 2026: Exceptional groups are proved; general classical groups remain. September’s codegree theorem concerns a different invariant.

### Q2123

**B7 / Q2123 / stable ID `7ecf710a682d6bfc2410`.** Exact retained statement:

> For each n≥2, must two finite-volume hyperbolic n-manifolds with identical length spectra be commensurable?

**Return decision:** unresolved. No new analysis or status promotion in this return.

**Object class:** Connected complete boundaryless finite-volume hyperbolic n-manifolds of curvature −1.

**Invariant or observation map:** Full length spectrum with multiplicities.

**Target equivalence:** Commensurability: existence of a common finite-sheeted Riemannian cover.

**Generic or uniform scope:** For every n≥2 and every pair with identical length spectra.

**Noise and loss:** Exact equality of length spectra; no noise or finite precision.

**Measurement count:** The complete length spectrum with multiplicities; no finite length cutoff.

**Source status from handoff:** catalog disposition: No exact closure in catalog ledger; collector status verbatim: Status for questions 2121, 2122, 2123, checked 6 October 2026: no resolutions located for retained targets; August solutions exclude Problem 3.16.

### Q2134

**B7 / Q2134 / stable ID `d7d72638df3bb1201dc2`.** Exact retained statement:

> For every odd d≥5, must each maximum-volume pair of nonisometric isospectral spherical space forms consist of lens spaces?

**Return decision:** unresolved. Experiment gives no all-dimensional maximum-volume result: scope-nonmatch.

**Object class:** Pairs of nonisometric isospectral curvature-one spherical space forms S^d/Γ in a fixed odd dimension d≥5.

**Invariant or observation map:** Full scalar Laplace spectrum with multiplicities, together with maximization of the common volume among eligible pairs.

**Target equivalence:** Both members being lens spaces, equivalently both free acting groups being cyclic.

**Generic or uniform scope:** For every odd d≥5 and every maximum-volume eligible pair.

**Noise and loss:** Exact isospectrality and exact volume optimization; no noise or approximate optimality.

**Measurement count:** The full Laplace spectrum and volume; no finite spectral or sample cutoff.

**Source status from handoff:** catalog disposition: No exact closure in catalog ledger; collector status verbatim: Status for question 2134, checked 6 October 2026: fresh final-journal read retains the conjecture; September nonstrong-isospectral examples do not optimize volume. No resolution located.

### Q2159

**B7 / Q2159 / stable ID `253959e9e3fc2bc95cf7`.** Exact retained statement:

> Determine the asymptotic order of max{χ_st(G): G is planar and |V(G)|=n} as n→∞.

**Return decision:** unresolved. No new analysis or status promotion in this return.

**Object class:** Finite planar graphs with n vertices and arbitrary strict vertex rankings of the available k colors.

**Invariant or observation map:** χ_st(G): least k such that every ranking profile admits a proper coloring whose preference digraph is acyclic; u→v records preference for the adjacent vertex’s color.

**Target equivalence:** Asymptotic extremal order of max χ_st(G) on n-vertex planar graphs; no invariant-reconstruction equivalence.

**Generic or uniform scope:** Worst case over planar graphs and, within χ_st, every vertex ranking profile; n→∞.

**Noise and loss:** Exact combinatorial preference and stability conditions; no noise.

**Measurement count:** Entire graph and ranking profile; optimize the number of colors, with n the asymptotic size parameter.

**Source status from handoff:** catalog disposition: No exact closure in catalog ledger; collector status verbatim: Status for question 2159, checked 6 October 2026: source leaves this open; later searches found no resolution.

### Q2211

**B7 / Q2211 / stable ID `a0c7ab5838fac12c9329`.** Exact retained statement:

> For finite semigroups H,K, does P(H)≅P(K) imply H≅K?

**Return decision:** unresolved. No new analysis or status promotion in this return.

**Object class:** Finite semigroups H,K.

**Invariant or observation map:** Power semigroup P(H) of nonempty subsets with setwise multiplication AB={ab:a∈A,b∈B}.

**Target equivalence:** Semigroup isomorphism H≅K.

**Generic or uniform scope:** Uniform over all finite semigroup pairs whose power semigroups are isomorphic.

**Noise and loss:** Exact power-semigroup structure; no noise.

**Measurement count:** All nonempty subsets and their setwise multiplication; 2^{|H|}−1 subset elements for H.

**Source status from handoff:** catalog disposition: No exact closure in catalog ledger; collector status verbatim: Status for questions 2211, 2212, checked 6 October 2026: May revision retains both. Later reconstruction results cover other classes; atom-count results establish only almost-unimodality for H=N₀.

### Q2350

**B7 / Q2350 / stable ID `1cd1a29825c43e7714d6`.** Exact retained statement:

> For finite trees T and U, does X_T=X_U force T≅U?

**Return decision:** unresolved. No new analysis or status promotion in this return.

**Object class:** Finite trees T,U.

**Invariant or observation map:** Chromatic symmetric function X_G=∑_(proper colorings κ:V→N) ∏_(v∈V) x_(κ(v)).

**Target equivalence:** Graph isomorphism T≅U.

**Generic or uniform scope:** Uniform over every pair of finite trees with equal chromatic symmetric functions.

**Noise and loss:** Exact symmetric-function equality; no noise.

**Measurement count:** The full chromatic symmetric function, with no coefficient truncation or sampled-coloring substitute.

**Source status from handoff:** catalog disposition: No exact closure in catalog ledger; collector status verbatim: Status for question 2350, checked 6 October 2026: September papers still leave general tree reconstruction open.

### Q2364

**B7 / Q2364 / stable ID `6f31e42a6bb668cb8904`.** Exact retained statement:

> Must every finite tree with a vertex of degree at least4 fail to be e-positive?

**Return decision:** unresolved. No new analysis or status promotion in this return.

**Object class:** Finite trees with at least one vertex of degree at least 4.

**Invariant or observation map:** Coefficients of the chromatic symmetric function X_T in the elementary symmetric-function basis e_λ.

**Target equivalence:** Failure of e-positivity, meaning at least one negative elementary-basis coefficient; no reconstruction equivalence.

**Generic or uniform scope:** Every finite tree satisfying the degree condition.

**Noise and loss:** Exact coefficient signs; no noise or approximate positivity.

**Measurement count:** The entire elementary-basis expansion of X_T; no selected coefficient or finite-tree census suffices for the uniform assertion.

**Source status from handoff:** catalog disposition: No exact closure in catalog ledger; collector status verbatim: Status for question 2364, checked 6 October 2026: latest source retains these targets; bounded later searches found no resolution.

### Q2483 (provisional)

**B7 / Q2483 (provisional) / stable ID `952a31b8ef8e3b9b0e60`.** Exact retained statement:

> Is there a complete countable-language theory T with =_R<_B ≅↾Mod_ω(T)<_B =⁺, where =⁺ identifies real sequences enumerating the same set?

**Return decision:** unresolved. Provisional number, stable ID 952a31b8ef8e3b9b0e60; no new result.

**Object class:** Complete theories T in countable languages and their spaces Mod_ω(T) of countable models.

**Invariant or observation map:** The isomorphism equivalence relation on Mod_ω(T), compared by Borel reducibility with equality on R and =⁺ on sequences enumerating the same countable set of reals.

**Target equivalence:** Strict Borel-reducibility position =_R<_B ≅↾Mod_ω(T)<_B =⁺; each strict inequality excludes a reduction in the reverse direction.

**Generic or uniform scope:** Existence of one such complete theory; countable-model classification scope. Question number and import remain provisional in the handoff.

**Noise and loss:** Exact equivalence relations and Borel reductions; no statistical noise or numerical loss.

**Measurement count:** Whole countable structures and their isomorphism relation; no finite observation budget or finite-census substitute.

**Source status from handoff:** catalog disposition: No exact closure in catalog ledger; provisional numbering; collector status verbatim: Status for questions 2481, 2482, 2483, checked 7 October 2026: Checked 7 October 2026: question retained in the reviewed source; targeted searches found no matching resolution.; import status: `provisional-recovery-draft`; `proposed` numbering. Use the stable ID when returning results.


## Appendix B. Result ledger and evidence navigation

Every result below has its full statement, changed assumptions, source dependencies and exact question links in the machine-readable ledger. Paths are relative to the extracted archive root.

| Result ID | Questions | Status of this result | Written proof |
|---|---|---|---|

| B7-R01 | Q17 | proved | `b7_work/q17_proof.md` |

| B7-R02 | Q739 | proved | `b7_work/moments/q739_proof.md` |

| B7-R03 | Q1749 | proved | `b7_work/q1749_proof.md` |

| B7-R04 | Q1749 | proved | `b7_work/trace/q1749_critical_characterization.md` |

| B7-R05 | Q1766 | proved | `b7_work/cube/REPORT.md` |

| B7-R06 | Q740 | proved | `b7_work/moments/q740_rotation_proof.md` |

| B7-R07 | Q740 | proved | `b7_work/moments/q740_rotation_proof.md` |

| B7-R08 | Q740 | proved | `b7_work/moments/q740_rotation_proof.md` |

| B7-R09 | Q741 | proved | `b7_work/moments/q741_generic_gauss_proof.md` |

| B7-R10 | Q738, Q742 | proved | `b7_work/trace/moment_collision_stability.md` |

| B7-R11 | Q1001 | proved | `b7_work/pmi_audit/REPORT.md` |

| B7-R12 | Q1002 | proved | `b7_work/pmi_audit/REPORT.md` |

| B7-R13 | Q1002 | proved | `b7_work/pmi_audit/REPORT.md` |

| B7-R14 | Q1156 | proved | `b7_work/metric_line_results.md` |

| B7-R15 | Q1157 | proved | `b7_work/metric_line_results.md` |

| B7-R16 | Q608 | proved | `b7_work/trace/TRACE_REPORT.md` |

| B7-R17 | Q609 | proved | `b7_work/trace/TRACE_REPORT.md` |

| B7-R18 | Q611 | proved | `b7_work/trace/TRACE_REPORT.md` |

| B7-R19 | Q613 | proved | `b7_work/trace/TRACE_REPORT.md` |

| B7-R20 | Q2025, Q2032, Q2134 | disproved | `b7_work/lens_homometry_result.md` |

| B7-R21 | Q607 | unresolved | `b7_work/trace/TRACE_REPORT.md` |
