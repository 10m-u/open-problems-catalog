# Q2731: positivity, hole-free support and concave extension of LG

The exact full target is [SETUP](SETUP.md): every alternating **knot**, p=LG(-t1,-t2), all three conclusions, and every convex relation for log concavity. Current full-target failure count: 5, accepted by root review. A stronger-condition obstruction or a formal polynomial is not a target counterexample. Stop solve work on this target unless root rejects a route count.

<a id="q2731-a1"></a>
## A1 — a uniform type-B exchange certificate

Try to certify log coefficients by the type-B exchange inequality in source Definition 3.4, which implies concave extendability by Theorem 3.6 and supplies hole-free support. The intended general construction would find, for each x,y and surplus coordinate, a one-step exchange satisfying the product inequality. This stronger uniform route cannot cover all actual target instances: the primary reports actual alternating knots 13a4593 and the seven listed 15-crossing knots as non-type-B, while their coefficients still satisfy the target (Theorem 1.2 and list (6)). We do not independently recompute those large knot invariants or claim a fresh range beyond 19 crossings.

Here is an exact worked model showing what the missing weakening must permit. On the complete square A={0,1,2}² put

    c_(u,v)=2^min(u,2v).

The support is hole-free. The explicit concave extension h(u,v)=min(u,2v) log 2 proves log concavity at **every convex relation**, because it is the minimum of two affine functions. Nevertheless, at x=(2,1), y=(0,0), i=1, the input product is 4. The type-B exchange candidates are x-e1,y+e1, or x-e1-e2,y+e1+e2; both output products are 2. There is no deficit coordinate to supply the third kind of move. Thus the stronger exchange test fails despite a valid concave extension. Its non-type-B ridge is u=2v, a slope 1/2 edge rather than a type-B root direction.

The obstacle is therefore not positivity or domain holes in this model, but restricting all exchanges to the type-B root system. A general certificate may need longer directions or larger rational convex combinations, whose coefficients depend on the actual concave subdivision. No construction guaranteeing them for all alternating knots was found. This is a failed uniform exchange-proof route with a worked exact distinction; the named actual exceptions are attributed primary evidence, and the model is explicitly not asserted to be a knot invariant. Source lookup and replay are zero attempts; the attempted stronger full proof and its analyzed obstruction count once.

[Checker](check_lg_concavity.py) reconstructs every type-B candidate using integer products and verifies this witness. It does not pretend to rerun the source's 51-million-knot computation.

<a id="q2731-a2"></a>
## A2 — reconstruct the joint polynomial from both Alexander specializations

Try to recover LG from the two exact primary identities L(t,t^-1)=Delta(t)² and L(t,-t^-1)=Delta(t²), then transfer alternating Alexander coefficient properties. The information loss can be computed completely. In the Laurent ring R=Z[t1^±1,t2^±1], change variables to u=t1t2, v=t1. The two specialization kernels are (u-1) and (u+1). Their intersection is

    ker(phi_+) intersect ker(phi_-) = (u²-1).                  (3)

Indeed, divisibility by the two distinct prime linear factors implies divisibility by their product in the Laurent polynomial UFD; the reverse inclusion is immediate. Equivalently, any fixed pair of Alexander specialization values leaves **every** deformation (u²-1)H(u,v) invisible, with arbitrary Laurent H. This is an infinite-dimensional loss, not a small normalization ambiguity.

For an explicit knot-normalization-compatible formal example, L=-1+2t1²t2² has both specialized values 1, just as the unknot does. It is symmetric under t1<->t2. After the required sign substitution, p=-1+2t1²t2² still has a negative coefficient. Hence even perfect knowledge of both Alexander identities and variable symmetry cannot force the first conclusion of Q2731, let alone the full joint concave extension. The formal L is not asserted to be any knot invariant; the source's complete quantum/skein data would distinguish it from the unknot.

The worked reduction supplies the exact missing information: control of the coefficients in the principal kernel (3) by the alternating diagram or quantum representation. No such control follows from those one-dimensional identities. This is a failed reconstruction/transfer route, distinct from A1's stronger discrete exchange certificate. The checker verifies both specializations term by term, including their signs, and preserves the formal nature of the example.

<a id="q2731-a3"></a>
## A3 — reconstruct the concave surface from all lattice-line inequalities

Try to prove the earlier two-dimensional log-concavity inequalities for LG and then infer the complete concave extension. The needed local-to-global lemma would say: positive coefficients on a hole-free lattice polygon, log-concave on every lattice line, imply concave extendability. This reduces the full target to pairwise restrictions, but the lemma is false even with variable symmetry and a complete square support.

Take the coefficient array, with x indexing rows and y columns,

    [[16, 4, 1],
     [ 4, 8,16],
     [ 1,16, 4]].

Every line contains at most three of the nine support points. A line containing three must have primitive direction (1,0), (0,1), (1,1) or (1,-1), up to sign: the coordinate span is at most 2, so three distinct integer points force consecutive primitive steps with each coordinate of the direction at most 1. On the three horizontal lines the middle squares are 16,64,256 and endpoint products 16,64,4; the vertical checks coincide by symmetry. On the two diagonals the middle square is 64, and endpoint products are 64 and 1. All line restrictions thus have a piecewise-linear concave interpolation. The checker also exhausts every integer-midpoint pair, including nonprimitive directions.

However, (1,1) is the centroid of (0,0),(2,1),(1,2). Concave extendability would require

    c_(1,1)^3 >= c_(0,0)c_(2,1)c_(1,2),

where the two sides are 512 and 4096. The triangle has determinant 3 and primitive edges, so it is precisely a two-dimensional almost-empty simplex in the primary Section 4 algorithm. Pairwise tests miss the single interior point of this triangle.

This is a worked failure of a weaker-to-full local reconstruction, whereas A1 attempted a stronger exchange certificate. The exact missing obligation is the **triangular** inequalities for actual LG coefficients; proving every lattice-line inequality does not discharge them. The array is formal, not an alternating-knot polynomial. We retain the source's exact segment-and-triangle criterion rather than substituting line log-concavity for the catalog statement. The source already establishes that criterion; no novelty is claimed.

<a id="q2731-a4"></a>
## A4 — termwise positive induction in the actual cubic skein basis

Try to construct the full coefficient proof by reducing positive powers of a braid generator in the complete LG skein theory, assembling the smaller closures with nonnegative coefficient multipliers after the target sign substitution. [Garoufalidis et al., Lemma 1.2, R1](https://arxiv.org/html/2505.19251v3#S1.SS3) gives, for g=s_i,

    g²+(1-t0-t1)g+(t0t1-t0-t1)1+t0t1 g^-1=0.

Multiplication by g and t0=-x,t1=-y give the factored characteristic identity

    (g+1)(g+x)(g+y)=0,
    g³=-(1+x+y)g²-(x+y+xy)g-xy.                     (4)

Thus the raw word-power reduction has negative multipliers in all three branches. Give the route its strongest uniform sign correction: put h=-g, corresponding to a parity sign on each word power. Then

    h³=(1+x+y)h²-(x+y+xy)h+xy.                       (5)

The middle branch is still negative. A positive monomial rescaling of the generator changes exponents in these multipliers, not their signs. The exact checker expands both products and records the negative coefficients. This calculation rules out the prescribed **termwise nonnegative raw-power induction**, including its uniform sign twist. It does not rule out a different basis, grouped cancellations, diagram-dependent signs or a positive state model. Applying this braid relation inside a knot can also produce links or nonalternating closures, so induction on the catalog class would need a separate admissibility argument.

The source's complete algorithm supplies computability; (4)–(5) show why that computability alone is not a positive coefficient construction. A successful replacement must both control the negative branch by other terms and preserve the joint coefficient inequalities after cancellation. No such cross-branch estimate was obtained. This is distinct from A2's incomplete Alexander data and A3's insufficient local convex tests: it uses the actual multivariable skein relation and analyzes the algebraic induction mechanism.

<a id="q2731-a5"></a>
## A5 — closure under connected sum using only the conjectured coefficient class

The actual invariant is multiplicative under connected sum ([Harper–Kohli–Song–Tahar, Proposition 2.9(4)](https://arxiv.org/html/2509.16868#S2.SS3)). Try to propagate the three desired properties from prime factors through this formula, using only positivity, hole-free support and concave extendability. The needed general product-closure lemma fails already at the support level, even with symmetry in x and y.

Consider the formal factors

    A=1+xy,       B=x²+xy+y².

Each has positive integer coefficients. Each support is the full set of integer points on its primitive lattice segment, and the logarithm of every coefficient is zero, with a constant concave extension on that segment. Both factors are invariant under x<->y. Their product has coefficient 1 at exactly

    (0,2),(1,1),(2,0),(1,3),(2,2),(3,1).

The lattice point (1,2), the midpoint of the occupied points (0,2) and (2,2), is missing. The product's support is therefore not hole-free. Geometrically the two primitive segment directions (1,1) and (1,-1) span an index-2 sublattice; Minkowski addition creates integer points outside the attainable sums. No coefficient sign or cancellation causes this obstruction.

Consequently one cannot induct over connected-sum factors in the unrestricted class described by the three conclusions. Neither A nor B is asserted to be LG of a knot, and this is not a counterexample to multiplicativity or Q2731. The precise residual obligation is an **additional support/concavity structure satisfied by actual LG factors** that rules out this index obstruction and proves product closure. Moreover, decomposition into prime knots would still leave the full prime-knot theorem to prove. This multiplicative structural route is separate from A4's additive signed skein reduction. We retain the exact formal obstruction and stop the question unresolved after five routes, without an impossibility or novelty claim.
