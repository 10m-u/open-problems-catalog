# Independent audit of returned B2 continuation III

Reviewed 2026-10-13 by the same retained research subagent. The mathematical
claims remain attributed to the uploaded continuation, *Occupied-fibre
rigidity and entropy tail nonattainment*, not to this audit. This is an
internal written review and exact replay, not external peer review, a formal
proof, or a worldwide novelty assessment.

**Disposition: accept all seven result records at their stated scopes.** I
found no mathematical gap requiring a correction to the submission. Neither
Q4296 nor Q4660 is closed. The former results concern two colours, and the
entropy results require the stated one-sided full-support regular tail.
The old stopping counters are unchanged; no new full-target failure or
closure is manufactured from these partial results.

## Material and source scope

I read the complete [TeX proof](../round3/RESEARCH-NOTE.tex) before reading or
executing its scripts, checked the corresponding nine-page PDF statements,
and read README, RESULTS, AUDIT-NOTES, SOURCES and PROVENANCE. The submitted
manifest initially passed. All 19 submission files remain byte-identical;
the original scripts were copied to round3/ before execution.
Exploratory MILP code was neither executed nor treated as proof.

I independently checked the local primary texts and the current primary
pages. Kościuszko's [Problem 4 and Theorem 3](https://arxiv.org/html/2610.11847v1)
give the finite-field question, density condition and quadratic codimension
baseline. Li's [Section 8](https://arxiv.org/html/2607.29042v1) gives the
sum–difference inequality with coefficient 2 and its sharpness question;
Conjecture 1.10 concerns a different sum–product inequality. Preserve the
submission's source-location correction alongside the original catalog
label. Li's Lemma 7.5 is a prior truncation ingredient, not the source of
the new tail stationarity or prescribed-tail conclusion. The exact
hyperplane-blocking number is classical: the
[Brouwer–Schrijver primary paper](https://ir.cwi.nl/pub/9858/9858D.pdf)
also attributes the independent Jamison result. I checked that primary
paper directly; I did not independently read the whole Jamison article.

The preceding cap classification is reproved in the appendix and used as
an inherited lemma. The earlier general codimension bound and entropy
lower bound are dependencies reviewed with rounds I/II by the main agent.
They are not newly established by this round's finite diagnostic.

## Geometry: M1 and M2

The direction must come from an affine flat of **maximum dimension** in
nonempty R. An inclusion-maximal flat does not suffice. The notation in
Theorem 2.2 and AUDIT-NOTES makes this distinction correctly. Quotienting
in this direction, write S for full remainder fibres and D for occupied
remainder fibres. A line in S lifts to a larger flat in R, so S is a cap.
Selecting a coloured representative from each fibre outside S transfers
the original admissibility to S. The inherited cap classification then
gives sizes 1, 2 or 4, with a parallelogram in the last case.

Here is the key rigidity argument checked independently. For q,t outside
S whose midpoint lies in S, **every** pair of coloured points from the two
fibres has its midpoint in R. Their nonempty coloured parts therefore
use disjoint colour sets. With two colours this forces each part to be
monochromatic. A quotient point q is isolated in this conflict graph
precisely when the reflection s ↦ 2s−q preserves S. In characteristic three
this is s ↦ 2q−s. Two different reflection centres compose to a nonzero
translation, whose three-element orbits are affine lines. A nonempty cap
cannot be invariant under such a translation. Thus at most one fibre can
escape the monochromatic conclusion. The singleton centre belongs to S,
so it creates no exception outside S. For a pair or parallelogram the
unique centre is outside S.

Within a monochromatic coloured part C, admissibility keeps midpoints in
the coloured part of the same fibre, hence in C. Translating a point of C
to zero, midpoint closure gives negation and then addition. Thus C is an
affine F3-subspace, and its size is 3^j for 0≤j≤d. This proves the stated
fibre cardinalities, including d=0 and the case R is the whole ambient
space. The theorem is not asserted for empty R, which has no chosen flat.

Occupied-fibre inheritance needs more than full-fibre inheritance, and
the submission supplies the missing step. Outside D, a regular fibre is
entirely monochromatic. At most one outside-D fibre can be exceptional;
choose a colour occurring there. For two distinct same-colour quotient
points outside D, one entire fibre has that colour and the other contains
one point of it. Midpoints of that fixed point with the entire fibre fill
the midpoint fibre, so the midpoint fibre cannot meet R. The diagonal
case has midpoint q itself and is automatic. This proves M2 without
assuming partially occupied fibres are full or monochromatic in R.

## Geometry: M3 and M4

The three-dimensional bound is a proof rather than an inference from
enumeration. With |R|≥17 the coloured complement C has size≤10. Relabel
the larger colour A. If |A|≤3, then |C|≤6 and the classical affine blocking
bound produces a plane disjoint from C. The reproduced polynomial proof
is valid: after translating a blocker to contain zero, its product
polynomial represents the delta function at zero; reduction modulo
x_i^3−x_i has degree at most the original degree and unique coordinate
degrees≤2, while that delta function has degree 2m.

For |A|=4, an affine basis has sumset size 10 and a planar four-point cap
has sumset size 9; both contradict |C|≤8. The remaining type is a line
plus an off-line point. Its midpoint set puts seven points of C in one
plane, leaving at most one coloured point elsewhere; one of the other
parallel planes is in R. For |A|≥5, a three-dimensional A contains five
spanning points. Normalize an affine basis to 0,e1,e2,e3: its ten sums
are distinct. Any fifth point creates another sum, by the explicit cases
in Lemma 3.2. This contradicts |C|≤10. Otherwise A lies in a plane and
occupies more than half its points, so its midpoint set fills the plane;
again another parallel plane is uncoloured. These cases are exhaustive.

The 16-point sharp example is genuinely admissible and plane-free.
Its two block projections avoid zero. Each such affine projection lies
in a nonzero functional level set. The pulled-back functionals have
disjoint coordinate supports and are independent, limiting any contained
flat to dimension one. An explicit line attains that dimension.

For the all-n bound, a plane-free remainder containing a line has maximum
flat dimension exactly one. Each regular occupied nonfull line fibre
contains two remainder points; a full fibre contains three, and there is
at most one exception, which has at least one if occupied. If D contained
a quotient plane, its pullback would have nine occupied fibres and at
least 8·2+1=17 remainder points in a three-space. Applying the actual
restricted partition to M3 gives a plane in R, a contradiction. Thus D
is both admissible and plane-free. Consequently

\[
 M_n\le 2M_{n-1}+4,\qquad M_3=16,
 \qquad M_n\le20\,2^{n-3}-4.
\]

Line-free remainders have size≤4 by the inherited cap theorem and also
satisfy this bound. At n=8 the upper bound is 636, below 3^8/10=656.1;
its density decreases thereafter. The density corollary follows. This
does not show sharpness for n≥4, optimality of n=8, or a higher-flat
analogue. It does not solve the full general-k extremal question.

## Entropy: E1 and the infinite differentiations

For a nondegenerate finite-entropy discrete real law, Δ+=H(X+X′)−H(X)>0.
Equality would make the conditional translates of the law of X′ agree
for two distinct atoms of X, making a probability law invariant under a
nonzero translation. Its positive atom would then generate infinite
total mass. This also explains why excluding point masses from the
ratio supremum changes no universal-constant question.

Fix the submission's hypotheses p_n>0 on every n∈N0 and
−log p_n=c n^β+o(n^β), c,β>0. These imply every polynomial moment and
finite entropy. Both output laws have positive masses throughout their
specified supports. For a transfer p+t(e_n−e_0), a sufficiently small
two-sided neighbourhood satisfies p/2≤p^(t)≤3p/2. The output masses are
therefore comparable to the original masses, uniformly in that
neighbourhood. Endpoint terms give

\[
 -\log q_s^{(t)}\le K(1+s^\beta),\qquad
 -\log r_m^{(t)}\le K(1+|m|^\beta).
\]

For each fixed n, the derivatives of the output masses are finite sums
of shifted/reflected p plus finitely supported terms. Multiplying them
by these logarithmic bounds gives a summable dominating sequence.
This justifies differentiating the three infinite entropy sums, rather
than merely a finite truncation. The neighbourhood and transfer size
may depend on n; no uniform-in-n transfer size is used or promised.

Differentiating with the old ρ held fixed yields

\[
 \Delta_+\rho'(0)=G_n-G_0,\quad
 G_n=-2\sum_jp_j\log r_{n-j}
     +2\rho\sum_jp_j\log q_{n+j}
     -(\rho-1)\log p_n.
\]

The factor two in the difference term uses the equality r_m=r_−m; the
coordinate-independent entropy-derivative constants cancel between n
and zero. I rederived this and independently checked it as an identity
between rational coefficients of formal logarithms, including other
base atoms and supports with negative values. The latter controls only
check the derivative algebra, not the one-sided tail theorem.

The tail asymptotics are sound without additional smoothness of p_n.
For any ε>0 the whole mass sequence is bounded above and below by
constant multiples of exp(−(c∓ε)n^β). In the sum convolution the minimum
of j^β+(n−j)^β occurs at an endpoint for β≤1 and at the balanced pair
for β>1. A minimizing term supplies one bound and n+1 times the largest
term supplies the other; log(n+1)=o(n^β). Thus the sum tail coefficient
is κβ=min(1,2^(1−β)). In the difference convolution, the j=0 term is
a lower bound, while monotonicity of (n+j)^β bounds the whole sum above
by a constant times exp(−(c−ε)n^β). Its tail coefficient is one.

Passing these limits through the p-weighted averages is also justified:
the normalized logarithms are bounded by a constant times 1+j^β, and
that sequence is p-integrable. Therefore

\[
 \frac{G_n}{cn^\beta}\longrightarrow 1+\rho-2\rho\kappa_\beta.
\]

If the coefficient is nonzero, G_n−G_0 eventually has its sign, giving
a strict ascent with the appropriate small transfer direction. A negative
coefficient is an obstruction just as a positive one is, because each
distant atom has positive mass. Stationarity with ρ>1 excludes β≤1 and
forces β=log2(4ρ/(1+ρ)) for β>1. This proves E1, but neither sufficiency
nor existence of a stationary law.

## Entropy: E2 and E3

The prescribed-tail supremum equality is valid. I checked all three
approximation operations; entropy continuity is not being inferred from
pointwise convergence.

1. For a finite-support exhaustion, conditioning X on the exhaustion
   gives input entropy convergence by its explicit conditional-mass
   formula. For Z=(X,X′), let E mean both entries lie in the exhaustion
   and δ=P(E^c). Finite joint entropy implies
   δH(Z|E^c)→0. For W=X±X′,
   H(W)=(1−δ)H(W|E)+δH(W|E^c)+I(W;1_E), with the last two terms bounded
   by δH(Z|E^c) and h(δ). Hence both output entropies converge. Conditioning
   on E preserves the two truncated copies' independence. Δ+ stays away
   from zero for all sufficiently late truncations, so their ratios
   converge too.
2. A finite real support embeds additively in Z^r after clearing rational
   coordinates in a rational basis. An integer linear functional avoiding
   finitely many hyperplanes is injective on the union of the support,
   its sumset and its difference set. It therefore preserves exactly all
   three probability-mass collision patterns. Translation to nonnegative
   integers changes none of their entropies. Rational approximation to
   the finitely many probabilities then preserves the ratio in the limit.
3. For each fixed c,β>0, mix such a finite law with ε times the full-support
   law Q_n proportional to exp(−c(n+1)^β). Beyond the finite support the
   mixed law has precisely the desired asymptotic coefficient c and
   exponent β. Input entropy convergence follows from the two-component
   mixture bound. Each sum/difference output is a four-component mixture
   of finite-entropy laws; the component-label entropy tends to zero and
   the vanishing-weight components have fixed finite entropies. Both
   output entropies converge. The reverse supremum inequality is immediate
   because the prescribed-tail class is a subclass of the unrestricted
   class.

For β=2 the gradient coefficient is exactly one, independently of ρ.
Thus no member of a fixed Gaussian-log-tail class can maximize its ratio:
a finite-coordinate ascent stays in that same class. Together with E2
this gives the claimed supremum-without-attainment phenomenon. This part
does not depend on trusting the earlier sharp numerical witness.

For a regular-tail global attainer, E1 instead forces
β=log2(4C*/(1+C*)). The source bound C*≤2 gives the upper endpoint
log2(8/3). The displayed lower endpoint using L=1.4051810329 depends
on the unchanged round-II certificate C*>L, separately audited by the
main agent. Algebraically the dependence is correct because 4ρ/(1+ρ)
is strictly increasing. No arbitrary irregular, two-sided or sparse
extremizer is excluded, and no maximizer is asserted to exist.

## Exact replay and independent controls

The reviewed submission scripts use only the standard library. Copied
`verify_midpoint.py` and `verify_entropy_variation.py` both passed and their
regenerated JSON receipts match the submitted receipts exactly. The former
checks all 19,683 labelled plane partitions (1,371 admissible), 1,159 fibre
and occupied-quotient instances, 640 plane-free projection instances,
296,010 six-point blockers, 75,816 spanning five-point sets, and all 17,550
four-point classifications. It uses 35 selected three-dimensional product
lifts and the sharp example, not all three-dimensional partitions. The
minimum five-point sumset observed is 12; the proved weaker bound 11 is
all the threshold argument needs. The latter checks 963 formal identities
and a certified finite fixed-support ascent. It is not an infinite-tail
verification or an improved C* witness.

[independent_check.py](round3/independent_check.py) imports no submitted
code. It generates flats using direction vectors and hyperplane equations,
checks all admissible plane partitions and **all 1,371 of their three-space
product lifts**, covering 1,129 maximum-flat directions in each dimension,
and independently checks the sharp construction and 23 normalized
spanning five-point configurations. It checks 80 gradient identities with
other base atoms, and certifies the finite ascent using separately written
35-term rational logarithm intervals with no rounded logarithm cache.
The lower-after interval exceeds the upper-before interval. The one
initial audit-receipt serialization error was corrected locally; it was
not a mathematical failure or a submitted-code error.

See [independent receipt](round3/INDEPENDENT-CHECK.json),
[preservation hashes](round3/PRESERVATION.json), and
[combined review receipt](ROUND3-REVIEW.json). These controls support the
written audit; they do not replace the proofs of the general results.

## Integration disposition

Retain the seven attributed scoped results separately from baseline
records, with the source-location note for Q4660. Retain both full targets
as unresolved and all earlier counters. Do not promote the 4D MILP time
limit to infeasibility, or present either finite entropy diagnostic as
a new universal lower bound. The supplied general codimension and entropy
constant bounds remain unchanged. No canonical data, exporter, public
repository, or older research packet was modified in this audit.
