# Interpolation continuation: structural routes and exact boundaries

13 October 2026. The full target definitions are in the frozen register.
The [October 7 report](../../b3-continuation-2026-10-07/interpolation/REPORT.md)
was read in full. The primary paper's [open problems](https://arxiv.org/html/2607.06207v1#S6)
and the later [Pochhammer generalization](https://arxiv.org/html/2608.03723v1)
were consulted. The latter's root statements retain their stated sufficient
hypotheses; they do not establish the current all-parameter bounds.

## I01: polarization over the parameter disk

Targets: Q1442 and B3C-Q05. Outcome: failed full-target proof route.

The inverse Newton transform is symmetric and multi-affine in the independent
parameters a_i. A Grace–Walsh polarization proof would follow if the diagonal
polynomial were nonzero for every common complex parameter in the disk
|a-1/2|<=1/2 whenever z was outside the required root region. I tested that
stronger symbol condition, which would make the all-size reduction concrete.

It fails already in degree two. The monic diagonal polynomial is
q(z)=z^2+(4a-1)z+2a^2. Put a=17/20-7i/20. This lies strictly inside that
parameter disk. Its discriminant is -1-49i/25. Write its square root u-iv,
u,v>0; u>.7 and v>1.2, by squaring the rational inequalities in the checker.
The negative-branch root has real part -6/5-u/2 and imaginary part 7/10+v/2.
Its squared modulus exceeds (31/20)^2+(13/10)^2>4. Thus this symbol fails even
for the weaker uncentered radius-two region. The separate exact choice
a=1/2-2i/5 gives a centered root w=i(8+sqrt(57))/10, outside radius 3/2.

These complex-parameter examples are obstructions to this polarization
architecture. The actual questions have real parameters in [0,1], so neither
is a counterexample to their statements. A proof would need a region adapted
to the interval, or extra structure beyond the circular coincidence theorem.

## I02: pairwise positive vertex expansion of Hurwitz minors

Target: B3C-Q04. Outcome: failed full-target positive-expansion route, with
new exact finite order-two certificates.

Let b_i(k) be the coefficient of t^(n-i) in
F_k(t)=product_(j=0)^(n-1)[(n+k-j-1)+(n-k+j)t]. The proposed expansion pairs
two Bernstein vertices to make every contribution to Delta_2=b_1*b_2-b_0*b_3
nonnegative before summing over assignments of the independent parameters.
The symmetric mixed contribution for vertices k,ell is

    b_1(k)b_2(ell)+b_1(ell)b_2(k)-b_0(k)b_3(ell)-b_0(ell)b_3(k).

At n=3,k=0,ell=3 it equals -475. Hence even the first nontrivial determinant
cannot have this termwise positive vertex-pair proof. This is a precise
architecture obstruction, not a negative coefficient of Delta_2 itself.

The independence constraint aggregates these negative terms with others.
For an odds monomial whose exponents contain k twos and p ones, the actual
coefficient is exactly

    sum_(h=0)^p binom(p,h)
       [b_1(k+h)b_2(k+p-h)-b_0(k+h)b_3(k+p-h)].

This follows by assigning each degree-one variable to either of the two
elementary-symmetric factors; degree-two variables occur in both. Thus this
formula exhausts the entire exponent box, using permutation symmetry without
assuming positivity. The [checker](check_routes.py) proves every such
coefficient strictly positive for each n=3,...,32. These are full exact
finite-degree order-two certificates, rather than a numerical parameter screen.
An all-size inequality for this binomial sum is still needed, followed by an
argument for every higher determinant order. The bounded certificates do not
reset this failed full-target attempt.

## An all-size order-one result

For every n>=2, Delta_1=b_1 has all 2^n odds monomials with strictly positive
coefficients. The coefficient at a subset of cardinality k is b_1(k).
For 0<k<n every factor of F_k has strictly positive constant and linear
coefficients, so its t^(n-1) coefficient is positive. At k=0 only the final
constant coefficient is zero; select its linear term and select one of the
other n-1 strictly positive constants to obtain a positive t^(n-1) term.
At k=n only the first linear coefficient is zero; select its positive
constant and the remaining positive linear coefficients. Multi-affinity
gives precisely the full exponent box and no other monomials. This closes
the determinant-order-one scope in every degree, not B3C-Q04 as a whole.

The [exact receipt](CHECK-RESULTS.json) also controls the rank-one formula
through degree 80 and re-derives the older degree-four relaxed-mixture
identity. That identity retains its original scope; it is not counted as a
new attempted solution merely because it was checked again.

## I03: all-size staircase corner coefficients

Auxiliary proof, not an additional failure count. The complete derivation is
[HURWITZ-CORNERS.md](HURWITZ-CORNERS.md). It proves every coefficient with
each odds exponent zero or r, for every n>=2 and 1<=r<n, using an exact
staircase Schur identity at each vertex. Mixed exponents remain outside
that theorem. This extends the order-one proof to all determinant orders
at all exponent-box corners. It does not itself complete B3C-Q04.

## I04: induction from a previous disk or Hurwitz certificate

Targets: Q1442, B3C-Q05 and B3C-Q04. Outcome: failed full-target route for
each, counted once per target. The shared mechanism is explicitly recorded.

Appending a parameter a has an exact inverse-Newton action: if
p(z)=sum_j c_j binom(z,j), then

    p_new(z)=sum_j c_j [binom(z,j+1)+a binom(z,j)].

Equivalently Delta p_new=p+a Delta p, with p_new(0)=a p(0).
I tried to induct using only nonnegative Newton coefficients and the
previous degree's disk certificate (or its equivalent numeric Hurwitz
certificate), so the target radius grows by one on appending each parameter.
This enlarged induction class is not preserved.

Take the **artificial previous polynomial** p(z)=(z+7/4)^2.
Its Newton coefficients are (49/16,9/2,2), all positive. Its repeated root
lies strictly inside the degree-two centered disk of radius3/2. Its
Cayley-transformed polynomial is (t+11)^2/16, strictly Hurwitz stable with
positive coefficients. Appending a=1 produces

    p_new(z)=(z+1)[z^2/3+(23/12)z+49/16].

The two nonreal roots are (-23 +/- i sqrt59)/8. Their squared moduli
are147/16>9, and their squared centered moduli are105/16>25/4. Thus both
degree-three disk targets fail in this enlarged class. The new Cayley
polynomial is

    (5/8)t^3+(25/48)t^2+(95/6)t+395/16,

whose Delta_2=-8275/1152<0 despite all four coefficients being positive.
So prior numeric Hurwitz stability also cannot be the entire n-induction
invariant for B3C-Q04. The artificial input is explicitly outside the TP
class: 2u^2+(9/2)u+49/16 has negative discriminant. None of these failures
is a counterexample on the independent real-parameter cube. An induction
must retain additional information about that cube or its PF transform.

## I05: a Toeplitz certificate for the coefficient row

Target: B3C-Q04. Outcome: failed full-target sufficient-class route.

A coefficientwise TN Toeplitz certificate for the b_i would imply the
negative-real-root sufficient class after numerical specialization and
therefore all Hurwitz determinants would be nonnegative. I tested this
stronger row certificate at an actual allowed specialization, rather than
assuming it follows from the positive vertex factors.

For n=2 and x1=x2=1, the exact transformed polynomial is
10t^2+16t+10. Its coefficient Toeplitz matrix has the minor

    det [[16,10,0,0], [10,16,10,0],
         [0,10,16,10], [0,0,10,16]] = -1264.

The tridiagonal determinant recurrence gives this integer directly. Hence
the proposed all-order Toeplitz certificate fails on the actual class.
Its discriminant -144 also shows why ordinary real-rootedness cannot
supply this stronger certificate. The actual polynomial is Hurwitz stable;
its positive leading Hurwitz minors are consistent with the target. This
route differs from I02's signed mixed-vertex expansion: it imposes a
different global sufficient matrix class on the resulting coefficient row.

## I06: log-concavity and the first Routh conditions

Target: B3C-Q04. Outcome: failed full-target truncation route.

The positive coefficient rows of the vertex products suggest using a
log-concavity invariant, together with Delta_1 and Delta_2, to force the
remaining Routh conditions. I worked out the required implication and
tested it against a full-positive-support coefficient row.

The artificial reciprocal degree-six polynomial with descending coefficients
(10,11,12,13,12,11,10) is strictly log-concave at every internal position.
Its first determinants are Delta_1=11, Delta_2=2 and Delta_3=-216.
Thus those necessary shape and low-order conditions do not force even the
next Hurwitz determinant. This is a generic failure of the proposed
completion theorem, not an actual F_n specialization. An induction must
control every higher order, rather than use the proved order-one result
and the finite order-two certificates as a complete Routh invariant.

## I07: numerical stability to coefficientwise positivity

Target: B3C-Q04. Outcome: failed full-target transfer route; fifth failure.

I tested whether numerical Hurwitz stability on the positive odds orthant,
plus nonnegative multi-affine coefficient polynomials, can supply the
coefficientwise claim. This would permit a numerical disk proof to close
the broader algebraic ambition without controlling determinant coefficients.

The artificial one-parameter cubic

    2t^3+(4+2x)t^2+(2+2x)t+(1+10x)

has strictly positive coefficient values for every x>=0, with nonnegative
coefficients in each multi-affine entry. Delta_1=4+2x,
Delta_2=4x^2-8x+6=4(x-1)^2+2, and
Delta_3=(1+10x)Delta_2 are strictly positive for every x>=0.
It is therefore strictly Hurwitz stable everywhere on that orthant, but
Delta_2 has a negative coefficient. This proves the generic transfer false
even with the stated structural restrictions. It is not the actual
independent-parameter vertex kernel. It does not negate B3C-Q04 itself.

The five counted B3C-Q04 routes are I02, I04, I05, I06 and I07. I03 is an
additional all-size partial proof and is not counted twice. The question
stops unresolved at five proposed full-target failures, pending independent
scope/count review. The first two Hurwitz orders and the exponent-box
corners retain exactly their separately proved scopes.

## I08: a norm bound for the Newton companion matrix

Targets: Q1442 and B3C-Q05. Outcome: failed full-target matrix-bound route.

Normalize q_n=n!P and write q_n=(z)_n+sum_(j<n)c_j(z)_j,
c_j=(n!/j!)e_(n-j)(a). Multiplication by z in the quotient algebra has the
Newton companion matrix: diagonal0,1,...,n-1 and subdiagonal1 before the
last column, whose entries subtract c_j. Its characteristic polynomial
is q_n. I tried to establish the root disks by bounding the numerical
radius after positive diagonal changes of basis.

At a1=...=an=1, its final diagonal entry is n-1-n^2. For n>=2 this has
absolute value greater than n, and after centering its absolute value is
n^2-n+1/2>n-1/2. Every diagonal similarity leaves that entry unchanged.
The numerical radius of a matrix is at least the modulus of each diagonal
entry, so no such weighted Newton companion can establish either target
radius. In degree two it is [[0,-2],[1,-3]], whose eigenvalues -1,-2 do
belong to the target disks. The obstruction is to this concrete norm
encoding; the earlier equal-parameter Jacobi representation remains valid.

## I09: weakening the shift law to ordinary log-concavity

Targets: Q1442 and B3C-Q05. Outcome: failed full-target shift-law route.

The independent Bernoulli sum in n!P(z)=E[(z+K)_n] has a log-concave
probability row. I tested whether this weaker property, retaining full
consecutive support, suffices for the root-radius argument. This is a
stricter relaxation than the old two-point SNN example, which lacked LC.

Let n=6 and make K uniform on{0,...,6}; its probability row is log-concave
and positive throughout. Up to a positive scalar, telescoping the binomial
sum gives in w=z+1/2

    Q(w)=49w^6+(10045/4)w^4+(177331/16)w^2+135135/64.

Put g(u)=Q(i sqrt u). The exact values are
g(36)=36579375/64>0 and g(49)=-17680285/64<0.
Hence it has a root u in(36,49), giving an imaginary w-root with |w|>6.
Its corresponding |z|^2=u+1/4>36. Both degree-six disk targets fail for
this LC shift law. Its probability numerator 1+t+...+t^6 has nonreal
roots, so the law is not a Bernoulli sum and the polynomial is not in U_6.
Log-concavity alone cannot replace the full PF/independence constraint.
This control is new and is not counted by replaying the older sparse SNN
counterexample.

## I10: a termwise Rouché estimate in the Newton basis

Targets: Q1442 and B3C-Q05. Outcome: failed full-target majorant route;
fifth failure for each.

I tried to isolate binom(z,n) as the dominant term outside each target
disk, using |e_k(a)|<=binom(n,k) and the product formula for binom(z,j).
Such dominance would immediately make P nonzero there. Even an actual
degree-two endpoint prevents the required termwise estimate.

At a1=a2=1, P(z)=1+2z+binom(z,2). For z=-5/2, which lies outside both
radius-two and centered-radius3/2 disks, the leading term has modulus35/8,
while the sum of the other term moduli is6. Thus the proposed triangle
majorant cannot give a strict Rouché inequality throughout the exterior.
The actual value P(-5/2)=3/8 is nonzero; cancellations are essential.
Changing the independent-parameter or Newton structure could still permit
a different analytic estimate, but this particular termwise certificate
fails at its necessary exterior-point contract.

The five counted routes for each of Q1442 and B3C-Q05 are I01, I04,
I08, I09 and I10. Their overlap is explicit: the same concrete attempts
target both nested disk assertions, without promoting a failure on one
automatically to a failure on the other. Every displayed obstruction was
checked separately against both radii. Both targets stop unresolved after
five proposed failures, pending independent count review. The equal-parameter
all-degree theorem and the degree<=5 cube certificate retain their scopes.

## Q1441 N01: powered quadratic nearest roots

Outcome: failed full-target construction of unbounded nearest-root radii,
with an improved all-size lower bound. I replaced the earlier real shifted
powers by nonreal quadratic powers (z^2+z+c)^m, whose nearest-root modulus
is sqrt(c) when c>1/4. Increasing c would refute the boundedness question
if a sequence of admissible powers survived. The exact sample-window
calculation in [NEAREST-RESULTS.md](NEAREST-RESULTS.md) forces c<2 for
every m, including an explicit negative3-by-3 minor at c=2. Hence this
family cannot furnish unbounded radii.

It does give exact TP bases at c=19/10, m=128 and129. Product closure
extends r_n>=sqrt(19/10) to every even n>=32512. Those proofs remain
partial on Q1441 and do not reset this failed full-target attempt.

## Q1441 N02: endpoint product and Viete upper bound

Outcome: failed full-target degree-independent upper-bound route, with
an explicit degree-dependent theorem. I used both P(0) and P(-1), rather
than just the constant term, to exploit a_i(1-a_i)<=1/4 for every parameter.
The complete calculation in NEAREST-RESULTS gives

    r_n <= 1/2+sqrt(1/4+(n!)^(2/n)/4).

The exact endpoint-product certificate is valid, but its right side grows
linearly in n. It does not bound sup_n r_n. A cancellation-free product
estimate loses the information that would be required for a uniform result.

## Q1441 N03: reduce to a uniformly near real zero

Outcome: failed full-target real-zero reduction. The source's odd-degree
sign argument gives a real root in[-1,0]. I attempted a parity-independent
extension using the real-rooted Newton transform and positivity of sampled
values to secure a similarly bounded real witness before bounding its
modulus. That reduction is false on the actual class already in degree2:

    P(z)=z^2+z+1/2,
    L(P)(u)=2(u+1/2)^2.

The transform roots lie in[-1,0], so P is admissible, but its discriminant
is-1 and it has no real roots. The new certified q^128 family likewise
has no real roots. Thus the full even-degree nearest-root problem needs
complex-root control. Reading the known odd-degree result is not itself
the failure count; the counted attempt is the proposed extension's false
universal real-witness obligation.

## Q1441 N04: finite-difference parity induction

Outcome: failed full-target operator-closure route. I tried to pass from
even degree to odd degree via Delta P, apply the odd-degree TP real-root
bound, and transfer that nearby zero back to P. The necessary TP closure
fails on an actual admissible polynomial.

For the inverse Newton transform,

    L(Delta P)(u)=[L(P)(u)-L(P)(0)]/u.

Take P(z)=binom(z+2,2), so L(P)=(u+1)^2. Then Delta P=z+2 and
L(Delta P)=u+2, whose zero-2 lies outside[-1,0]. The odd-degree theorem
therefore cannot be used on the difference without an enlarged class
and a new uniform bound for that class. The exact append induction I04
also needs more than prior disk data; that is a different operator and
target, not an extra failure on Q1441 here.

## Q1441 N05: finite-degree generators and product closure

Outcome: failed full-target factorization proof; fifth failure.

A decomposition of every admissible P into admissible factors of degrees
at most a fixed cutoff would prove a uniform nearest-root bound: fixed-
degree compactness gives a finite maximum for those factors, and the
nearest root of a product is the minimum of their nearest-root moduli.
I tested this constructive route at cutoff6, using the exact real-factor
structure of the new q^128 witness.

NEAREST-RESULTS proves that no nonconstant factor of that polynomial of
degree<=6 is admissible. The powers q and q^2 have negative numerator
coefficients, and q^3 has a reciprocal-reduction coefficient obstruction.
Thus the proposed finite-generator decomposition fails at the tested cutoff.
A theorem with some larger cutoff, or a different nonmultiplicative
decomposition, remains unproved; no claim of arbitrary cutoff failure is
made. This differs from N01, which tries to refute boundedness by varying
c, and from N03, which asks for a real zero of the whole polynomial.

Q1441 has five proposed failed full-target routes and stops unresolved,
pending independent count/proof review. The exact new lower family and
degree-dependent upper bound remain useful partial results. No omitted
historical archive has been recovered, and no finite experiment is promoted
to a uniform upper bound.
