# Q2508: derivative ranks and three families

Private research result, 13 October 2026. The full classification in Problem
1(i) remains unresolved. These are proofs of narrower statements, including
counterexamples to two stated auxiliary claims in the cited source. Independent review is accepted in PERAZZO-INDEPENDENT-REVIEW.md and
ROOT-REVIEW.md#perazzo-final; no priority is claimed.

## Exact contribution of G

Work over an algebraically closed field of characteristic zero. Write
F=sum_{j=1}^q X_j p_j(U)+G(U), where the p_j are linearly independent
degree-e forms, e=d-1. Set W=span(p_j), D=K[partial_U],
J=Ann_D(W), R=D/J and r_i=dim R_i (so r_0=1 and r_d=0).
For 0<=i<=d define the bilinear form

    B_i : J_i x J_(d-i) -> K,     (a,b) -> (ab)G,
    e_i = rank B_i.

Then the following exact identity holds without general-position assumptions:

    h_F(i) = r_i + r_(d-i) + e_i.                     (1)

To prove it, identify h_F(i) with the dimension of the space of order-i
derivatives of F. Operators with two X derivatives vanish. The pure-U
operators project to the X-linear component by
a -> sum X_j(ap_j), a map of rank r_i with kernel J_i. Operators with
one X derivative span the pure-U space
V=D_(i-1)W inside K[U]_(d-i), of dimension r_(d-i).
Indeed the perfect differentiation pairing between D_(d-i) and K[U]_(d-i)
identifies V's annihilator with J_(d-i): a kills every derivative
b p_j, |b|=i-1, exactly when a p_j=0. For i=0 use V=0 and r_d=0.
The remaining pure-U images are aG for a in J_i, modulo V. Pairing this
quotient with J_(d-i) gives precisely B_i, and proves (1). The endpoint
i=d follows in the same way. Commutativity makes e_i=e_(d-i).

In particular G in K[U]_1 W gives e_i=0: replace X_j by X_j+L_j
when G=sum L_j p_j. This is an invertible linear coordinate change.
The correction ranks depend only on the class of G modulo K[U]_1 W.
Formula (1) is a useful reduction to annihilator and restricted pairing
data. Listing its adjacent inequalities alone would be an algorithmic
restatement, rather than the requested structural classification.

## Flat binary-plus-pure family in every degree d>=4

For e>=3 put m=3, q=e+2, n=q-1=e+1 and

    F_e = sum_{j=0}^e X_j U^(e-j)V^j
          + X_(e+1) Z^e + Z^(e+1).

The p_j are a basis of the binary degree-e forms together with Z^e.
They are linearly independent and algebraically dependent since q>m.
They meet n>=m>=3, and all X variables and all three U,V,Z variables
are essential. One can check degree-one derivatives directly: the pure
degree-e p_j and the three X-linear U,V,Z derivatives are independent.
G has the required degree and is nonzero; it is absorbed by
X_(e+1) -> X_(e+1)+Z.

For 1<=i<=e, pure differential monomials involving Z together with U
or V annihilate W. Binary order-i operators act independently on the
full binary degree-e space, giving i+1 dimensions, and partial_Z^i
adds one independent dimension. Thus r_i=i+2. By (1),

    h(F_e) = (1, e+5, e+5, ..., e+5, 1),

with e internal entries. This all-size family is unimodal and log-concave.

**Source claim audit.** The final cited primary paper is Mezzetti and
Miró-Roig, *Perazzo n-folds and the weak Lefschetz property*,
[DOI 10.1007/s12215-024-01063-x](https://doi.org/10.1007/s12215-024-01063-x),
locally retained as texts/papers/collections-c95847ffa72383e7.txt.gz.
Definition 2.2 does not impose a genericity hypothesis on W.
Theorem 4.2, formula (10), states for n>=m>=2 a universal minimal
h_i=min{2q, binom(m+i-1,m-1)+q,
binom(m+i-1,m-1)+binom(d+m-i-1,m-1)}.
For e=3, d=4, m=3, q=5 this asserts h_2>=10, whereas F_3 has

    h(F_3)=(1,8,8,8,1).

Here the one-X second derivatives span U^2,UV,V^2,Z^2, of dimension4.
The pure-U second derivatives project to the four independent X-linear
forms 6X_0U+2X_1V, 2X_1U+2X_2V, 2X_2U+6X_3V, 6X_4Z.
The extra derivative of Z^4 lies in the existing pure-U span.
The total second-derivative dimension is exactly8. The source proof's
lower bound from the number of nonzero catalecticant blocks does not
hold when their images overlap. This is a counterexample to that stated
auxiliary bound, not a counterexample to an open classification.

Lemma 2.3 asserts the general directional derivative preserves the same
Perazzo presentation under q<=binom(d+m-3,m-1). For this family,
e+2<=binom(e+1,2) for every e>=3, but a directional derivative sends
the full binary space to binary degree e-1 forms of dimension e, and
Z^e to at most one more dimension. Its rank on W is always at most
e+1<q (exactly e+1 for generic direction). Hence the new p_j cannot
be independent. Adding X components to the differentiating linear
form changes only its pure-U term; it cannot restore that rank.
The derivative loses an essential X direction. The counterexample
addresses the source's fixed-variable presentation and stated proof,
not the possibility of treating a smaller presentation as a different
Perazzo form after eliminating cone directions.

## Fixed p_j, varying G: an exact rank classification of quartics

Let r>=3, m=r+1, with variables U_1,...,U_r,Z. Let W be the full
cubic space in the U variables, together with Z^3, and
q=binom(r+2,3)+1, n=q-1. Form

    F_Q = sum_{|alpha|=3} X_alpha U^alpha + X_* Z^3
          + Z^4 + Z^2 Q(U),

where Q is any quadratic form. All hypotheses of Q2508 hold, and the
first derivatives have rank q+m. We have r_1=m and
r_2=binom(r+1,2)+1; J_2 is spanned by partial_(U_j)partial_Z.
On this span B_2 is a nonzero scalar multiple of the matrix of Q,
so e_2=rank(Q). Consequently

    h(F_Q)=(1, q+m, 2[binom(r+1,2)+1]+rank(Q), q+m, 1).

Since q+m-2[binom(r+1,2)+1]=binom(r,3), this entire family is
unimodal if and only if rank(Q)>=binom(r,3). For r=3 the threshold
is1: Q=0 gives (1,15,14,15,1), while Q=U_1^2 gives
(1,15,15,15,1). For r=4 the threshold is4 (Q must be nonsingular).
For r>=5 the threshold exceeds r, so no Q in this family works.
Thus a classifier based only on W cannot decide the full question.

## Unimodality is neither open nor closed in these parameter families

With r=3 above, take Q=tU_1^2. All t!=0 give unimodality but t=0
does not. Thus the unimodal locus is not closed in this affine line.

For the other direction use degree6, m=3, q=7. Let W_0 be the binary
degree5 space plus Z^5. Choose seven explicit ternary quintics W_1
with the coefficient matrix in PERAZZO-CHECK.json (seeded integers,
used as exact rational coefficients). The executable checks their
annihilator quotient ranks as

    (r_0,...,r_6)=(1,3,6,10,15,7,0).

For the polynomial family W_t=W_0+tW_1 the same ranks hold on a
nonempty Zariski open set: witnessing nonzero minors at t=1 are
polynomials in t, and the stated dimensions are the maximal possible
ranks. Outside finitely many parameters those minors stay nonzero.
Choose G=Z^6. J_1,J_2,J_3=0, so all correction terms in (1) vanish
by symmetry. The generic h-vector is

    (1,10,21,20,21,10,1),

which is not unimodal, while at t=0 it is
(1,10,10,10,10,10,1), which is unimodal. Independence of W_t and
essentialness of all variables hold at t=0 and generically, and every
form under discussion is inside the Q2508 hypotheses. On an affine
line, a nonempty open set contains generic parameters; the unimodal
locus here therefore cannot be open at0.

These two examples defeat propagation from a generic parameter stratum
by either openness or closedness. They do not exclude a classification
that explicitly analyzes all restricted-rank strata.

## Verification scope

check_perazzo.py differentiates the full forms with integer coefficients
and performs exact rational sparse elimination. It uses no source rank
bound and no claimed Hilbert formula when obtaining actual ranks.
Controls include e=3,...,8, every rank-Q choice for r=3,4,5, and four
degree6 deformation values. The all-size statements above are proofs;
these finite controls verify their formulas and the explicit generic
minor witness. No general classification or publication priority follows
from the receipt.
