# Independent Q2508 mathematical and attempt-count review

Reviewed on 2026-10-13. I accept the restricted-pairing identity, the
all-degree flat family, the all-r rank-Q family, the two geometric
propagation obstructions, and five distinct failed full-target routes.
Problem 1(i)'s complete classification remains unresolved. The source
corrections below have their literal stated scopes; no novelty, external
review or public communication is claimed.

## Source hypotheses and rank corrections

I read the frozen Q2508 statement (38ee4eff0fa06bac5bff) and the final
paper's local text, especially Definition 2.2, Lemma 2.3, Theorem 4.2
and Problem 1(i). The [authors' primary text](https://arxiv.org/html/2405.14756v1)
agrees on these hypotheses and statements. The catalog requires
characteristic zero, n>=m>=3, d>=3, independent but algebraically dependent
p_j. The definition does not restrict their span to general position.
General position used in constructing a particular example is not an
additional hypothesis of the universal minimum claim.

For e>=3 the full binary degree-e monomials and Z^e are independent;
q=e+2>3 guarantees algebraic dependence. Here m=3,n=e+1,d=e+1 and
q<=binom(e+2,2), so all numerical conditions hold. A first-order operator
killing F must have its U,V,Z part kill every p_j: the binary monomials
and Z^e force this part to vanish. Its remaining X part then vanishes
by independence. Consequently every variable is essential, including
the three U variables; these are not degenerate cone examples. The
term Z^(e+1) has degree d, is nonzero and is absorbable by X_* -> X_*+Z.

For e=3, the one-X second derivatives span U²,UV,V²,Z². The pure-U
second derivatives have four independent X-linear projections:

    6X_0U+2X_1V, 2X_1U+2X_2V,
    2X_2U+6X_3V, 6X_4Z.

The pure-U derivative of G adds no new pure form. Hence h_2=8, with
h_1=8 and symmetry giving (1,8,8,8,1). Theorem 4.2 formula (10) gives
min(10,11,12)=10 at these same invariants. This is an actual contradiction
to its universal minimum bound as printed. The proof's inference from
each block having nonzero rank to a lower bound on their combined rank
does not account for overlaps.

For the directional-derivative lemma, q=e+2<=binom(e+1,2) satisfies its
numerical hypothesis. Every direction maps the binary subspace into
binary degree-(e-1) forms (dimension e) and Z^e into at most one more
dimension. Its rank is at most e+1<q, and equals e+1 when the binary
direction and Z component are both nonzero. Thus the lemma's proof
assertion that the q transformed p_j remain independent is false for
this legal input. Adding X components to the operator changes only the
pure-U part; a lost X direction still annihilates the derivative. The
prescribed same-variable, fixed-q induction fails. This does **not**
rule out a smaller Perazzo presentation after removing cone directions;
the packet correctly distinguishes that possibility.

## Restricted-pairing identity

Write D=K[partial_U], J=Ann_D(W), r_i=dim(D_i/J_i), d=e+1.
Pure-U order-i operators map to the X-linear component with rank r_i
and kernel J_i. Operators containing one X derivative supply
V=D_(i-1)W in the pure-U component of degree d-i. Under the perfect
scalar differentiation pairing its annihilator is J_(d-i): testing all
order-(i-1) further derivatives is equivalent to the polynomial a p_j
being zero. Therefore dim(V)=r_(d-i).

The remaining pure images are aG, a in J_i, modulo V. The dual of this
quotient is J_(d-i); its pairing is exactly (a,b)->(ab)G. Their extra
dimension is its rank e_i. This proves

    h_F(i)=r_i+r_(d-i)+e_i,  0<=i<=d.

Boundary values use J_0=0, r_0=1, r_d=0, so h_0=h_d=1 and e_0=e_d=0.
Commutativity gives e_i=e_(d-i). An element of K[U]_1 W can be absorbed
by an invertible linear X shift. As the r_i are unchanged, the identity
also shows that correction ranks depend only on G modulo that space.
No generic-rank or block-independence assertion enters this proof.

For the flat family, binary order-i operators are independent on all
binary degree-e forms, contributing i+1 dimensions, while partial_Z^i
adds one. Mixed binary/Z operators kill W. Thus r_i=i+2 for 1<=i<=e,
and removable G has e_i=0. The formula proves the stated flat row for
every e>=3, independently of the finite checker.

## Quartics and parameter propagation

With W the full cubic space in r variables plus Z³, J_1=0 and
J_2 is precisely the r-dimensional span of partial_(U_j)partial_Z.
Its restricted pairing on Z²Q is a nonzero scalar multiple of Q's
symmetric matrix. Hence e_2=rank(Q), and all other e_i vanish. The
displayed h-vector follows. Its middle-minus-first difference is
rank(Q)-binom(r,3), proving the rank threshold for **every** quadratic
Q and every r>=3, over the stated field. Signature or a diagonal choice
is not a hidden restriction: the rank formula uses the full matrix.

The line Q=tU_1² is entirely legal, with unimodal row for t!=0 and
nonunimodal row at zero, so unimodality is not closed. For the independent
quintic deformation W_t=W_0+tW_1, I verified the claimed maximal ranks
at t=1. The independent receipt gives explicit nonzero square minors
at every level 1..5, not only rank summaries. Each such minor is a
polynomial in t, hence nonzero outside finitely many values. The maximum
possible ranks are (1,3,6,10,15,7,0). J_1,J_2,J_3 are zero on this generic
set; symmetry eliminates all correction terms for any G. Therefore
the generic row is (1,10,21,20,21,10,1), while the legal t=0 input has
the flat row (1,10,10,10,10,10,1).

More precisely, restrict the parameter line to the legal open subset
where W is independent and F has all variables essential. It contains
zero and all but finitely many parameters. Its unimodal locus contains
zero and misses the generic parameters, so it is not open there. No
claim about the finitely many omitted parameter values is needed. The
two examples exclude open or closed propagation alone; a full analysis
of rank strata remains possible.

The flat quartic's gamma vector is (1,4,-6). A positive reciprocal
quartic with only real nonpositive roots pairs inverse roots into
(1+z)²+c z with c>=0, including repeated roots at -1. Products of these
have nonnegative gamma vectors. The negative last entry therefore
proves that this actual unimodal row is not real-rooted. This is a
failure of a necessary-and-sufficient root classification, not a
failure of unimodality.

## Five attempt dispositions

| Route | Decision and distinct obligation |
|---|---|
| A1 | Accept: universal extrema-based classification fails because its proposed lower-bound region excludes a legal solution. The independently derived pairing identity is retained. |
| A2 | Accept: a degree-reduction induction fails to preserve the fixed q presentation. It shares A1's family but attacks closure of an operation rather than numerical bounds. |
| A3 | Accept: fixed W does not determine unimodality when G varies outside removable gauge terms. The all-r rank-Q theorem supplies a worked replacement reduction, not a full answer. |
| A4 | Accept: the actual flat row blocks real-rootedness as a necessary complete certificate. A narrower sufficient root subclass remains possible. |
| A5 | Accept: generic-stratum classification does not propagate by either openness or closedness. One witness overlaps A3, but the second independent W-deformation and nonzero generic-minor argument establish the distinct geometric failure. |

These are five failures of specified classification mechanisms. Neither
the supplied source's open Problem 1(i) nor a possibility of a different
classification is disproved. No sixth route is authorized by this review.

## Independent exact controls

[check_perazzo_review.py](check_perazzo_review.py) imports none of the
root implementation. It constructs full factorial-moment catalecticant
matrices directly from coefficients, obtains their ranks by integer
elimination, and computes annihilator kernels separately by rational
RREF. Restricted pairings then independently reproduce the full ranks.
[PERAZZO-REVIEW-CHECK.json](PERAZZO-REVIEW-CHECK.json) passes six flat
families, 24 directional maps, 15 rank-Q quartics and four actual
quintic deformations. It additionally records five exact nonzero minor
determinants at t=1 and the quartic gamma obstruction. The all-size
claims rely on the proofs above; finite controls audit arithmetic,
witnesses and the generic-stratum certificates.
