# Eulerian reconstruction: degree bound and the quadratic (2,b) classification

These arguments independently reconstruct leads L10 and L11 in
PROGRESS-LEADS.md. They concern partial scope of Q1262,
statement `b1ba78271e207b25e0d3`; the general coloured classification remains
open. No novelty or proof-assistant claim is made.

For a positive integer vector s=(s₁,…,sL), put

`E_s(x)=Σ_e x^asc(e)`, with `0≤eᵢ<sᵢ`, `e₀=0`, `s₀=1`, and
`asc(e)=#{i: eᵢ/sᵢ<eᵢ₊₁/sᵢ₊₁}`.

The source convention is the inversion-sequence/lecture-hall definition used in
[Deligeorgaki–Han–Solus, §4.1 and Proposition 25](https://arxiv.org/abs/2407.12076).
Its factor-volume and unit-removal observations were already used in the initial
packet. The new proofs here do not require a claim of simple roots for arbitrary
nonunit blocks.

## A degree-dependent finite representation bound

**Theorem E1.** Every nonconstant s-Eulerian polynomial of degree d has a
representing positive integer vector of length at most **2d−1**.

Leading/trailing unit entries can be deleted. Adjacent unit entries can be
replaced by a single unit. A remaining unit separates two independent ascent
statistics, so `E_(s,1,t)=E_s E_t`. It suffices to treat each contiguous block
whose entries are at least two, and then reinsert one separator between blocks.

Let a block have length L and polynomial degree D. Choose positive inversion
coordinates in odd positions and zeros in even positions. This gives
`ceil(L/2)` ascents, hence `L≤2D`.

Suppose `L=2D`. If some odd pair `(s₂ⱼ₋₁,s₂ⱼ)` differs from `(2,2)`, choose
positive coordinates in that pair with strictly increasing normalized values.
Such a pair exists: for integers A,B≥2,
`1/A < (B−1)/B` unless A=B=2. Before the chosen pair use the odd-positive,
even-zero pattern; after it use zero,positive pairs. This constructs D+1
ascents, a contradiction. Thus a block of length 2D must be all twos.

For an all-two block, its last pair of twos can be replaced by one entry four
without changing the total ascent polynomial. If the preceding ratio is zero,
the two final binary coordinates contribute `1+3x`; if it is one half they
contribute `3+x`. A single final coordinate with denominator four contributes
the same polynomials in the respective cases. For a block of length two the
preceding ratio is the initial zero, so the identity still holds. The new block
length is 2D−1. All other blocks already have length at most 2D−1.

If the block degrees are D₁,…,Db, their sum is d. The resulting length is at
most `Σ(2Dᵢ−1)+(b−1)=2d−1`. This proves the theorem.

This also gives a stronger finite recognizer than the initial volume bound:
the canonical ordered factorization/separator enumeration may be capped at
length `2d−1`, as well as volume `E_s(1)`. The theorem is existential; it does
not say every original representing vector already satisfies the bound.

## Connected quadratics have a larger linear coefficient

**Lemma E2.** If s has no unit entries and `deg E_s=2`, write
`E_s=1+h₁x+h₂x²`. Then `h₁>h₂>0`.

The preceding ascent argument restricts its length to at most four. Length four
forces the all-two vector; it has polynomial `1+10x+5x²` and can be replaced by
`(2,2,4)`. A length-two vector `(A,B)` has

`h₂=((A−1)(B−1)−gcd(A,B)+1)/2`,
`h₁=AB−1−h₂`,

so `h₁−h₂=A+B+gcd(A,B)−3>0`. The top coefficient counts strictly increasing
positive normalized pairs. Counting the lattice points on either side of the
diagonal gives the formula.

For length three, reversal preserves E_s. One proof uses the lecture-hall
simplex: `yᵢ ↦ s_(L+1−i)−y_(L+1−i)` is an affine integral bijection to the
reversed simplex, preserving its Ehrhart numerator. Write s=(A,B,C) with A≤C.
Degree three occurs exactly when there is an integer j with
`B/A < j < B(C−1)/C`. If A,C≥3, the only degree-two exception is `(3,3,3)`:
for B=2 use j=1; for B=3 and C>3 use j=2; for A>3 use j=1; and for B≥4 choose
a j strictly between B/3 and 2B/3.

If A=2, the degree-two triples are exactly

- `(2,2,C)` for arbitrary C≥2;
- `(2,B,2)` for arbitrary B≥2;
- `(2,3,3)`, `(2,4,3)`, `(2,4,4)` and `(2,6,3)`;
- and their reversals, together with `(3,3,3)` above.

To see completeness when C≥3, the smallest j strictly above B/2 is below
`B(C−1)/C` unless B=2; B=3,C=3; B=4,C≤4; or B=6,C=3. For B=5 or B≥7 that
j is strictly below 2B/3, giving degree three for every C≥3.

The two infinite families have

`E_(2,2,C)=1+(C+2 floor(C/2)+2)x+(3C−2 floor(C/2)−3)x²`,

and

`E_(2,B,2)=1+2B x+(2B−1)x²` for odd B,

`E_(2,B,2)=1+(2B+2)x+(2B−3)x²` for even B.

These formulas follow by conditioning on the ratio in the adjacent binary
coordinate(s). Their linear-minus-quadratic gaps are respectively 3 or 5, and
1 or 5. The five remaining triples give coefficient pairs
`(10,7),(12,11),(18,13),(19,16),(16,10)`. Every gap is positive, proving E2.

The `(2,6,3)` pair was corrected after the independent review: its exact
polynomial is `1+19x+16x²`. See [the review](eulerian-independent-review.md)
for the hand count; the correction does not change E2 or E3.

## Exact (2,b) classification

**Theorem E3.** For every positive integer b, the uncoloured two-symbol multiset
Eulerian polynomial

`A_(2,b)(x)=1+2b x+binom(b,2)x²`

is s-Eulerian for some positive integer vector of arbitrary length **if and only
if b=2 or b(b+1)/2 is an integer square**.

For b=1 the polynomial is `1+2x=E_(3)` and its triangular number is one.
For b≥2 its degree is two. Split a canonical vector into nonunit blocks.
There are either two degree-one blocks or one degree-two block.

In the two-block case the polynomial is `(1+ux)(1+vx)` for positive integers
u,v. Matching coefficients gives `u+v=2b`, `uv=b(b−1)/2`; therefore
`(u−v)²=2b(b+1)`, equivalent to `b(b+1)/2=t²` with integer t. Conversely the
vector `(b−t+1,1,b+t+1)` realizes the polynomial whenever this square condition
holds. For b≥2, t<b, so both nonunit entries are at least two.

In the one-block case E2 requires `2b>binom(b,2)`, hence b≤4. Its volume is
`(b+1)(b+2)/2`. For b=2 volume six admits `(2,3)` and gives `1+4x+x²`.
For b=3 volume ten permits only `(2,5)` or its reversal (a single coordinate
has degree one); these give `1+7x+2x²`, not `1+6x+3x²`. For b=4 volume fifteen
permits only `(3,5)` or its reversal; these give `1+10x+4x²`, not
`1+8x+6x²`. Length-three nonunit vectors have at least three prime factors
in their volume, so cannot occur at volumes six, ten or fifteen. This exhausts
the connected case and proves E3.

## Remaining recovery leads and checks

The claimed all-degree sharpness of E1 for `(1+ux)^d` and simple-root theorem
for every nonunit block are **not assumed or recovered in this note**. E3 has
its own elementary classification proof. The full coloured Q1262 and the
combinatorial interpretation in Q1263 remain open.

[eulerian_checks.py](eulerian_checks.py) supplies independent literal and refined
inversion-sequence comparisons, the elementary contraction, degree-two
classification controls and bounded exhaustive volume recognition. Its finite
controls support the written arguments; they do not replace their quantifiers.
