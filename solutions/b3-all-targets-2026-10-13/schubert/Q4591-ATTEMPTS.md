# Q4591: positive equivariant OG Littlewood–Richardson rule

Exact target: find a cancellation-free combinatorial rule for every O^nu_(lambda,mu) in H_T^*(OG(n,2n+1);Z), as a polynomial with nonnegative integer coefficients in gamma1=t1 and gamma_i=t_i-t_(i-1). Frozen statement bc3a6d517ae78c07fa91, thesis printed p.43, [joint primary paper §1](https://arxiv.org/html/2503.14609v2). The local thesis was read at texts/collections-bd8ace3842285c95.txt.gz. These attempts concern the full independent-parameter problem, rather than only ordinary cohomology or the Anderson–Fulton one-parameter quotient.

Source setup: [Robichaux–Yadav–Yong §§8–10](https://arxiv.org/pdf/1908.11224), especially Problem 8.1, Chevalley formula (23), Theorem 8.2 and specialization (34). Known positivity is not itself the requested combinatorial rule. No new general rule or originality claim is made.

## Exact rank-two algebra used below

Write a=xi_(1), b=xi_(2), c=xi_(2,1), u=gamma1, v=gamma2. Chevalley gives

    a²=u a+b,   ab=(u+v)b+c,   ac=(2u+v)c.

These imply, by associativity,

    b²=v(u+v)b+2(u+v)c,
    bc=(u+v)(2u+v)c,
    c²=u(u+v)(2u+v)c.

For example b²=(a²-u a)b=v ab+ac. Next bc=(a²-u a)c=(u+v)(2u+v)c. Finally c²=(ab-(u+v)b)c=u(u+v)(2u+v)c. Together with the unit these give all products at n=2 and reproduce the primary Table 1 (whose PDF text extraction contains a spurious alpha in the OG b² entry).

Equivalently use the Newton basis 1,x,x(x-u),x(x-u)(x-u-v) in

    Z[u,v,x] / (x(x-u)(x-u-v)(x-2u-v)).

The fourth-degree relation follows by multiplying c by a and using the last Chevalley formula. It is monic, so this is a free module with the stated four basis elements. This is an exact low-rank derivation and checker control, not a general LR construction.

<a id="q4591-a1"></a>
## A1: reweight the unchanged ordinary shifted LR objects

Attempt: start from the new ordinary shifted LR rule and assign nonnegative gamma-monomial weights to its existing tableaux, keeping the same skew shape nu/lambda, content mu and ordinary rectification constraint. If every full equivariant coefficient were such a weighted count, the ordinary machinery could be lifted without introducing extra label locations or changing the objects.

The construction cannot supply lower-size outputs. Already lambda=mu=nu=(1) has skew shape empty and content (1), hence no ordinary tableau; any weighting of that empty set gives zero. The exact rank-two product instead has O^1_(1,1)=u. At u=v=0 the term disappears, as it must. Conversely O^2_(1,1)=1 is genuinely the ordinary one-box contribution. Thus the obstruction occurs precisely in the information lost upon ordinary specialization, rather than in the known ordinary rule.

The missing step is to create new objects for equivariant excess degree while retaining positivity, not merely to reweight the old ones. Edge labels are one plausible enlargement, examined in subsequent routes. First full-target failure; the exact product is preserved. This excludes only the unchanged-object lift.

<a id="q4591-a2"></a>
## A2: reconstruct the full answer from a one-parameter edge-tableau quotient

Attempt: prove a positive rule for the Anderson–Fulton ring using shifted edge tableaux, then recover the full equivariant coefficient from the resulting one-parameter structure constants by homogeneity and the ordinary specialization. This would exploit a much smaller coefficient ring.

The primary formula (34) specializes the LG coefficients by alpha1=z and all other alpha_i=0. Theorem 8.2 makes the corresponding OG information exactly its gamma_i=0 for i>1 specialization, up to known powers of two and z=2u. Even granting every conjectural edge-tableau/ring identification, that map has a large kernel.

The actual n=2 coefficient O^2_(2,2)=v(u+v)=uv+v² is homogeneous of degree two, nonzero and coefficientwise positive. Both this coefficient and the zero polynomial have the same one-parameter image and ordinary specialization. In particular no rule restricted to the coefficients of that image can determine these two positive monomials. The shape data could support a richer reconstruction, but homogeneity and the image alone do not prove it.

The precise missing step is a positive independent-parameter refinement of the specialized objects, with a theorem identifying each gamma monomial. This differs from A1: the objects now allow excess labels, but the coefficient specialization discards directions. Second full-target failure, not a claim that the one-parameter conjectures are false.

<a id="q4591-a3"></a>
## A3: count positive fixed-point localization products directly

Attempt: use positive Schubert restrictions at torus fixed points as weights, multiply the two restrictions and divide by the restriction of the desired output class. Such a formula would avoid signed inversion of the restriction matrix and provide positive local objects.

At the fixed point indexed by (2), Chevalley or the Newton basis gives

    a|2=u+v,   b|2=v(u+v),   c|2=0.

For lambda=mu=(1),nu=(2), the proposed raw quotient is

    (a|2)²/(b|2)=(u+v)/v=1+u/v,

whereas O^2_(1,1)=1. The lower output a contributes u(a|2); the correct triangular reconstruction is

    [(u+v)²-u(u+v)]/[v(u+v)]=1.

The two numerators are individually positive, but the second must be subtracted. Thus raw localization is neither polynomial nor the requested coefficient. Merely deleting terms with negative powers does not solve arbitrary triangular reconstruction: the lower-output subtraction must be accounted for compatibly across all fixed points.

An exact computational signed formula follows from triangular localization, but no cancellation-free inverse or weight-preserving subtraction bijection is provided. Third full-target failure. A2 loses parameter information; A3 retains all parameters but cannot positively invert the basis restrictions.

<a id="q4591-a4"></a>
## A4: replace row rectification by column rectification in an edge lift

Attempt: supply a shifted edge lift by using the ordinary-looking column rectification order, so that a conventional rectification/insertion proof could establish the product rule before adding independent gamma weights. A valid full rule must remain commutative after the one-parameter specialization; this is a necessary test of the proposed repair, even without guessing its final weights.

The literal slides J1/J2/J3'/J4' were implemented with each label 1,...,N occurring once, boxes strictly increasing along rows and columns, edge labels larger than boxes in their column, and edges only south of diagonal boxes. The checker enumerates all admissible tableaux, rather than randomly sampling fillings. On nu=(4,3,2,1), lambda=(4,3), mu=(3,2,1), it gives:

| Rectification order | nu/lambda to S_mu | nu/mu to S_lambda |
| --- | ---: | ---: |
| Column, rightmost inner corner first | 20 of 558 | 16 of 1156 |
| Row, southernmost inner corner first | 16 of 558 | 16 of 1156 |

Here Delta=|lambda|+|mu|-|nu|=3, and L=ell(lambda)+ell(mu)-ell(nu)=1. The conventional factor 2^(L-Delta) is 1/4 for both orders. Thus the proposed column law produces 5z^3 in one input order and 4z^3 in the other. No commutative cohomology ring can have those as its products. This independently reproduces the primary Example 9.9; the source already identifies this obstruction, so it is not a new discovery.

The missing step is a compatible slide/order theory whose specialized counts are commutative and whose independent-parameter weights can be proved correct. The row control passes this necessary test but does not settle its associative or full-weight extension. Fourth full-target failure; this is an obstruction to the column repair, not to an arbitrary positive LR rule.

<a id="q4591-a5"></a>
## A5: remove powers-of-two fractions by forgetting edge positions

Attempt: take the row edge-tableau candidate and make its normalization manifestly integral by grouping tableaux with the same underlying box labels into free orbits of size 2^(Delta-L) when Delta>L. The resulting orbit count would furnish positive integral specialized objects, to be refined with gamma weights for the full target. This tests an actual construction of the required objects, rather than simply assuming positivity of a computed polynomial.

For lambda=(3), mu=(3,2,1), nu=(4,2,1), Delta=2 and L=1, so the required orbit size is two. Fix these four box labels of nu/lambda:

    (1,4)=3, (2,2)=1, (2,3)=2, (3,3)=4.

All distributions of the remaining labels 5,6 among the three permitted diagonal edges are enumerated, subject to the column constraints. Exactly one row-rectifies to the row superstandard S_(3,2,1): both labels lie on diagonal edge 3. The fibre obtained by forgetting edge positions therefore has size one, not a multiple of two. Its normalized contribution alone is z²/2. There can be global divisibility across different box fillings; no such divisibility follows from the proposed fixed-box equivalence. This independently reproduces the source Example 9.4.

The missing step is a global orbit/bijection or another direct integral model that mixes box configurations, and a theorem refining it to the independent gamma variables. A4 changes the slide order and fails commutativity; A5 retains row slides but fails its proposed integrality quotient. Both concern the same edge candidate and that overlap is disclosed. Neither disproves row edge-tableau conjectures or the catalog target. Fifth consecutive full-target failure: stop Q4591 unresolved.

## Receipts and scope

[OG-RANK-TWO-CHECK.json](OG-RANK-TWO-CHECK.json) verifies all rank-two products by a monic polynomial quotient. [EDGE-RECTIFICATION-CHECK.json](EDGE-RECTIFICATION-CHECK.json) records the complete bounded row/column and fixed-box computations, with [literal slide checker](check_edge_rectification.py). These are precise restricted proof-contract obstructions, not finite evidence that the open problem is impossible. Source/service errors and the checker expression-comparison repair count zero. Main-thread review of the five-count disposition remains pending.

