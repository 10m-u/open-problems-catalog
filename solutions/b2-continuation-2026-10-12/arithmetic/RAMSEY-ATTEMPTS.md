# Four remaining Ramsey targets

The main thread took Q2203/Q2462/Q2468/Q2469 while the retained agent's handle
was awaiting initialization. That interruption counts as no attempt.
Exact statements, provisional flags and prior partials remain in the snapshot.
Primary readings: Wesley's cached thesis introduction and §3;
[Fox–Kleitman's primary paper](https://math.mit.edu/~fox/paper-FoxKleitman.pdf);
[Bucić et al. preprint](https://arxiv.org/html/2507.22831v1), definitions and §5;
[Liu et al. v2](https://arxiv.org/html/2603.05490v2), Theorem 1.4 and §6;
Laboska's cached final journal text, Theorems 3.1, 4.1–4.4, Proposition 3.8
and Open Question 3. The final Bucić journal numbering has not been independently
recovered here; the provisional catalog flag remains unchanged.

## Two exact elementary boundary results

For Q2203, r(1)=1 and r(2)=2 suffice. A one-variable equation has no positive
solution. In two variables, equal-sign coefficients likewise have none. For
opposite signs write the solution ratio q=−a/b>0. If q=1, all constant tuples
solve the equation. Otherwise choose a prime ℓ with d=v_ℓ(q)≠0 and colour x by
floor(v_ℓ(x)/|d|) modulo 2. Multiplying by q shifts this integer by ±1 whenever
both numbers are positive integers, so every solution uses both colours.
The three-variable bound24 is an established primary-source input, not a new
proof here. No bound for arbitrary m follows from these cases.

For Q2469's equation x−y=b, b≠0, RCA₀ itself proves a three-colouring for every
countable coded ring, indeed every coded abelian group. On the enumerated
domain, join x to x+b and x−b. The graph has degree at most two and no loops.
At each vertex choose the least of three colours unused by its previously
enumerated neighbours. Bounded recursion relative to the coded operations
defines the colouring, and induction proves every edge is properly coloured.
This uses no path-selection principle. The optimal two-colour version in the
source can have WKL₀ strength; the question permits any finite palette.

<a id="q2203-a1"></a>
## Q2203 A1 — Extend the two-variable valuation parity colouring

The proof above supplies a uniform two-colour obstruction to each nonregular
two-variable equation. In three or more variables several terms at the least
valuation can cancel. The equation2x+3y=7z has no zero-sum coefficient subset,
but its solution(x,y,z)=(1,11,5) is monochromatic under v₂(x) mod2.
Thus that proposed fixed parity rule does not generalize. A multi-term
valuation invariant would be needed. **Failed direct uniform-colouring extension.**

<a id="q2203-a2"></a>
## Q2203 A2 — Bound the palette in Rado's least-nonzero-digit proof

The usual proof chooses a prime p dividing no nonempty coefficient subset
sum, then colours by the least nonzero base-p digit, using p−1 colours.
There is no bounded list of suitable primes even with fixed m=3. Put
P=product of all primes in a proposed finite list and take coefficients
(P,2P,−3P+1), P≥2. All seven subset sums are nonzero, and their gcd is1,
but every listed prime divides the first coefficient. The proof's required
prime therefore escapes the list. This refutes that uniform prime-selection
criterion, not Rado's boundedness conjecture (the three-variable case has a
different proof). **Failed bounded-prime palette proof.**

<a id="q2203-a3"></a>
## Q2203 A3 — Merge variable blocks to invoke the three-variable theorem

Identifying several variables imposes equality on a solution that regularity
does not promise. For example x₁+x₂+x₃−2x₄=0 is regular because1+1−2=0.
Merging its first three variables produces3x−2y=0, which the two-variable
colouring above shows is nonregular. Thus variable identification does not
preserve regularity in the direction required by this reduction. No adaptive
block-partition lemma preserving r-regularity for all coefficient vectors
has been established. **Failed dimension-reduction proof.**

<a id="q2203-a4"></a>
## Q2203 A4 — Compactify the normalized coefficient vectors

One might seek a finite cover of the normalized nonregular parameter space
by neighbourhoods admitting a bounded avoiding palette. The vectors
(1,2,−3+1/P), P→∞, are nonregular after clearing denominators but converge
to the regular zero-sum vector(1,2,−3). The nonregular locus excludes
zero-subset-sum hyperplanes and is not compact. A finite subcover is therefore
not supplied by the projective compactification; behaviour near those
hyperplanes needs a uniform additional argument. **Failed compact-parameter proof.**

<a id="q2203-a5"></a>
## Q2203 A5 — Certify a universal colour threshold with bounded SAT instances

Enumerating coefficient heights and colourings of[N] is exact at each bound.
It has no universal height or witness-size bound. For P>N the primitive
equation P x+2P y−(3P−1)z=0 has no solution in[N] at all, since reduction
modulo P requires P|z. Yet(P−1,P,P) is a positive solution on the full
domain. Thus even one-colour existence can evade every fixed test interval
as coefficient height grows. A finite SAT table cannot close the all-height
regularity claim without a separate compactness bound. **Failed finite-certificate completion.**

<a id="q2462-a1"></a>
## Q2462 A1 — Reduce arbitrary coefficients to the equal-coefficient theorem

The prior full equal-coefficient subcase d(L,ε)=1/k remains preserved.
Multiplying the equation by a nonzero scalar, permuting variables, or dilating
the common set does not change the relative coefficient ratios. Substituting
y_i=c_i x_i instead makes the variables belong to different sets c_i A,
rather than one common set with its prescribed Cayley graph. In particular
(1,1,−3) has no zero-sum subset and cannot become an equal-coefficient problem
by those common transformations. **Failed uniform coefficient reduction.**

<a id="q2462-a2"></a>
## Q2462 A2 — Use one interval with a small Cayley independence number

For L:x+y=3z, a fixed interval A/p→[a,b] of width w=b−a>0 cannot produce
the required positive density with independence o(p). If2b>3a, the real
solution region x+y=3z inside this interval has nonempty relative interior;
integer-grid approximation supplies pairwise distinct solutions for large p.
Thus solution-freeness requires2b≤3a, or a≥2w. Replacing each coordinate
by1−x preserves the equation modulo p and gives1−b≥2w as well.
The interval[0,min(a,1−b)) is independent in Cay(A), so

    α(Cay(A)) ≥ 2w p−O(1).

The same conclusion holds after a common nonzero dilation. A positive-width
single-interval template therefore retains a positive independent fraction;
to meet ε→0 its width must tend to zero. This is a concrete obstruction for
one admissible coefficient vector, not an evaluation of the full limit.
**Failed single-interval extremizer; scoped obstruction proved.**

<a id="q2462-a3"></a>
## Q2462 A3 — Build a dense Fourier-uniform solution-free set

For L:x+y=3z let F(r)=Σ_{x∈A}e(rx/p). The ordered solution count is
p⁻¹Σ_r F(r)²F(−3r). Its zero-frequency term is |A|³/p. Parseval bounds
the absolute remaining sum by max_{r≠0}|F(r)|·|A|. Hence at fixed positive
density, max_{r≠0}|F(r)|=o(p) forces Θ(p²) solutions. Repeated-coordinate
solutions contribute onlyO(p) for p>3, so distinct solutions remain.
Uniform random/Fourier-flat positive-density generators cannot be L-free.
Small Cayley independence does not itself imply this Fourier flatness;
structured constructions escape the attempted argument. **Failed pseudorandom generator construction.**

<a id="q2462-a4"></a>
## Q2462 A4 — Read the exact limit off the zero/nonzero classification

The primary classification guarantees a positive limiting obstruction when
no subset sum vanishes. It does not give its optimal value. The newer chromatic
threshold concerns bounded χ, while this question concerns α=o(p).
The implication α small⇒χ large follows from χ≥p/α; the reverse implication
does not follow. Covering by random translates of an independent set of
sizeδp gives only O_δ(log p) colours, not a bound independent of p.
Neither qualitative threshold classification evaluates d(L,0+).
**Failed qualitative-to-sharp and chromatic substitution.**

<a id="q2462-a5"></a>
## Q2462 A5 — Exchange the prime and ε limits in finite optimization

For a fixed p every Cayley graph has an independent vertex. Once ε<1/p
there are no feasible sets, giving zero under the usual empty-maximum
convention. Taking ε→0 before p→∞ therefore loses every positive limiting
construction, including the preserved equal-coefficient value1/k.
Exhausting all subsets at finitely many primes cannot justify exchanging
these limits or produce a uniform extremal theorem for arbitrary coefficients.
The monotonicity guaranteeing existence of the stated limit is preserved;
its value remains unknown. **Failed finite-table/limit-exchange proof.**

<a id="q2468-a1"></a>
## Q2468 A1 — Identify positivity with the exact Schur threshold

The source's classification shows δχ(x+y=z)>0 because no subcollection
of at least three coefficients sums to zero. An elementary upper bound is
δχ≤1/3: remove0 from a weakly Schur-free A, obtaining B. The restricted
sumset2^∧B is disjoint from B, and the restricted-sumset inequality gives
|2^∧B|≥min(p,2|B|−3). Thus |A|≤(p+6)/3. At any fixed d>1/3 only
bounded p admit |A|≥dp, so their chromatic numbers are uniformly bounded.
These bounds leave an interval of possible thresholds. No matching positive
lower value or bounded-colouring theorem below1/3 follows.
**Failed exact determination from the known dichotomy and extremal size.**

<a id="q2468-a2"></a>
## Q2468 A2 — Import the triangle-free graph chromatic threshold

The underlying undirected Cayley graph need not be triangle-free. In F₁₃,
A={1,3,9} is even strongly sum-free, but0,1,4 form a triangle, with directed
differences1,3,9 summing to0. Schur-freeness prohibits a+b=c, not a+b+c=0.
The edge symmetrization therefore permits a different triangle orientation.
The ordinary triangle-free threshold theorem cannot apply unchanged.
**Failed forbidden-graph transfer.**

<a id="q2468-a3"></a>
## Q2468 A3 — Cover by translates of one independent set

The Ramsey–Turán theorem supplies a positive-density independent set at each
fixed generator density for Schur's equation. Greedily or randomly translating
that independent set covers p vertices in O_δ(log p) steps. Removing overlaps
gives a valid colouring, but its palette still grows with p. A bounded-cover
lemma is the missing step; large α alone is insufficient. The newer source's
positive Schur threshold is itself evidence that this qualitative route
cannot establish δχ=0. **Failed translate-cover upper bound.**

<a id="q2468-a4"></a>
## Q2468 A4 — Get a dense high-chromatic witness by independent sampling

An independent random subset of density q has Θ(q³p²) distinct Schur triples
in expectation, whereas it has only qp vertices. The crude delete-one-vertex
per-triple alteration bound becomes useful only when q is of order p⁻¹/²,
which gives density tending to zero. It cannot supply a fixed positive-density
Schur-free witness needed to lower-bound the threshold sharply. Correlated
structured generators, such as the primary's high-dimensional construction,
are needed; the independent alteration does not replace them.
**Failed positive-density random witness.**

<a id="q2468-a5"></a>
## Q2468 A5 — Decide the asymptotic threshold by finite exact enumeration

The checker exhausts weakly Schur-free subsets at declared small primes and
their maximum sizes, and checks the explicit triangle counterexample.
One can also compute χ exactly in any chosen finite Cayley graph. None of
these finitely many p determines whether a palette bound holds for every
prime above a candidate density. There is no monotone prime-size reduction
or finite universal bound on a first high-chromatic witness.
**Failed bounded extremal classification.**

<a id="q2469-a1"></a>
## Q2469 A1 — Force the optimal two-colour Straus reversal

The source can encode WKL₀ into optimal two-colour avoidance of x−y=b.
The catalog ring assertion permits an arbitrary finite palette, and the
three-colour greedy construction above is already provable in RCA₀ for this
entire single-difference subcase. Passing a coded abelian group to the
square-zero ring Z⊕G does not force the extracted palette back to two.
Thus that direct reversal loses its required colour restriction.
**Failed optimal-palette reversal; full single-difference subcase proved.**

<a id="q2469-a2"></a>
## Q2469 A2 — Compute the principal-image quotient used by a classical proof

Writing s for the vector of row sums, no constant solution says b∉sR.
The map r↦sr is computable, but a procedure finding an element in its range
does not decide nonmembership or choose canonical representatives of every
quotient class. The single promise b∉sR supplies no such global decision.
An RCA₀ proof cannot silently comprehend this arbitrary range. The original
B2 upper proof's finite-presentation workaround avoids this problem but
still uses WKL₀. No quotient algorithm eliminating that use is constructed.
**Failed effective-quotient reduction.**

<a id="q2469-a3"></a>
## Q2469 A3 — Rationalize the ring and use linear algebra over a field

Tensoring with Q kills additive torsion. For R=F₂, b=1 and equation x−y=1,
the hypothesis has no constant solution. Rationalization gives the zero
ring and kills b, turning the equation into a constant-soluble one. Thus
the obstruction does not survive this reduction, and a field calculation
cannot settle every coded ring. **Failed rational linear-algebra proof.**

<a id="q2469-a4"></a>
## Q2469 A4 — Turn the safe-colouring tree upper proof into a classification

For a fixed sufficient palette K, finite safe colourings form a finitely
branching tree; an infinite path is a witnessing colouring. The preserved
B2 argument supplies such a tree and uses WKL₀ for its path. Building a
computable tree does not provide a computable path, and the fixed tree alone
does not prove that every possible palette must encode WKL₀. The two needed
directions are distinct: an effective path-selection argument for RCA₀, or
a ring encoding that constrains all palettes for a reversal. Neither is
obtained from this tree construction. **Failed upper-to-exact-strength inference.**

<a id="q2469-a5"></a>
## Q2469 A5 — Encode a tree in a Boolean ring and read a path from a colour class

The equation x+y=1 in a Boolean ring forces complementary elements to receive
different colours. It does not force a colour class to be an ultrafilter or
the colouring to be a homomorphism to F₂. In F₂³ colour {000,100,010,001}
with0 and the complementary four elements with1. This valid two-colouring
has colour1 at011 and101 but colour0 at their product001. Thus the proposed
colour1 branch-choice filter is not closed under intersection. Boolean-ring
tree/path encodings need multiplicative consistency that this linear
avoidance condition has not enforced. **Failed Boolean-path reversal.**

Each exact target has five failed full-target routes. Their constructive
boundary proofs, interval obstruction and finite controls retain their
scopes. No exact reverse-mathematical classification, coefficient-uniform
Ramsey bound, density limit or Schur chromatic threshold is claimed.
