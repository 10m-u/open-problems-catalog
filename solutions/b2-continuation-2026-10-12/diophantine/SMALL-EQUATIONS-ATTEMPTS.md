# The small Diophantine equations: full targets and failed constructions

Exact source: Grechuk's [current retained list](https://arxiv.org/html/2404.08518v10),
local text texts/papers/collections-6232c246a1510285.txt.gz. The original
B2 report's Part D was reread before constructing these extensions.
The five routes per question concern their full integer scope.

## Q2314 — a finite union of integer polynomial families


<a id="q2314-a1"></a>

1. **Generate all solutions by the original polynomial orbit.** The
   transformation z↦z−2tu−xyu², t↦t+xyu preserves xyz+t²+1=0.
   Starting from one point gives a polynomial family for each fixed number
   of steps. But no uniform word-length bound or finite seed set was
   obtained; a countable union of such families is not the required
   finite union. The earlier dense family's counterexample remains.

<a id="q2314-a2"></a>

2. **Clear denominators in a rational parametrization.** Solve
   z=−(t²+1)/(xy). This describes every integer point only with
   the variable divisibility condition xy|(t²+1). Writing the quotient
   as a new parameter leaves the original equation. Denominator clearing
   changes the equation's constant1 and does not create polynomial
   maps whose every integer input is a solution.

<a id="q2314-a3"></a>

3. **Use Gaussian factorization.** Factor t+i in Z[i] and distribute
   Gaussian prime factors among x,y,z through their norms, treating
   the ramified prime2 separately. This can describe divisors, but
   the chosen Gaussian factors must have product with imaginary part1.
   That variable trilinear constraint was not eliminated into unrestricted
   integer polynomial parameters. Unique factorization alone is not
   the requested finite parametrization.

<a id="q2314-a4"></a>

4. **Infer completeness from Zariski density.** The original family has
   a nonzero Jacobian determinant and hence a dense image. Density
   controls vanishing polynomials, not membership of individual integer
   points; (−13,13,29,70) misses every sign/permutation copy.
   Adding finitely many missing points does not prove no further
   exceptional fibres. The necessary integral coverage argument is absent.

<a id="q2314-a5"></a>

5. **Rule out all polynomial families by a sign constraint.** Since
   xyz=−(t²+1), no coordinate vanishes and their product is negative.
   But integer polynomials can avoid zero (u²+1), and the original
   nonconstant dense family already satisfies all signs.
   This proposed obstruction does not forbid polynomial families or
   prove that finitely many cannot cover; it needs a stronger invariant
   beyond pointwise signs and nonvanishing.

## Q2315 — a nonzero point on the projective quartic


<a id="q2315-a1"></a>

1. **Construct a point on coordinate and diagonal lines.** At y=0,
   x⁴+z⁴=0 gives only the zero point. On x=0 or x=−y,
   z/y would solve v⁴+v−1=0, which has no rational root by the
   rational-root theorem. At z=0, x/y solves u⁴+u³−1=0 with
   the same obstruction. These easy lines supply no nonzero point;
   they do not exclude the full plane curve.

<a id="q2315-a2"></a>

2. **Use an ordinary height search as a decision.** Enumerating primitive
   triples inside a fixed height box would semidecide a positive answer
   if a witness appeared. Genus3 finiteness supplies no effective height
   bound for the entire rational point set. The proposed terminating
   negative search has no justified last height.

<a id="q2315-a3"></a>

3. **Turn local points into a rational point.** The prior report's smooth
   local points at every prime and real solubility were preserved.
   A local-to-global theorem for this genus-three curve is not supplied,
   and no such principle holds for arbitrary smooth curves of that genus.
   Failure to find an obstructing modulus cannot provide the global point.

<a id="q2315-a4"></a>

4. **Use Jacobian Chabauty immediately.** Embed the curve in its Jacobian
   after choosing a rational base divisor and seek a rank less than3.
   This needs an audited Mordell–Weil rank bound, a finite-index subgroup,
   and effective residue calculations for this Jacobian. None follows
   from the smoothness/genus proof. The attempted reduction stops at
   those concrete arithmetic inputs, rather than claiming Chabauty ran.

<a id="q2315-a5"></a>

5. **Parametrize by tangent lines from a local point.** A tangent at a
   p-adic point has p-adic coefficients and can produce p-adic residual
   intersections. It does not yield a rational line or a rational
   intersection; even a rational line meets the quartic in a degree-four
   divisor whose individual points need not be rational. No rational
   seed or splitting certificate was found.

## Q2316 — an integer point on the symmetric cubic


<a id="q2316-a1"></a>

1. **Complete every small-coordinate fibre.** The divisor reduction
   in [Q2316-FIBERS.md](Q2316-FIBERS.md) is exhaustive in y,z for
   each fixed x. Its exact certificate excludes every |x|≤5000,
   and symmetry excludes a small coordinate anywhere. It gives a
   new restricted theorem, but x is unbounded; no full coordinate
   height bound or global solution was obtained.

<a id="q2316-a2"></a>

2. **Scale the existing rational witness.** Clearing the denominator20
   in (−13/20,−79/20,21/5) scales cubic terms by20³, linear terms
   by20 and the constant by1. It therefore does not preserve the
   affine equation. The homogeneous rational witness cannot be
   promoted to an integer one by uniform scaling.

<a id="q2316-a3"></a>

3. **Use a Vieta integer descent.** As a monic cubic in z, the equation
   factors at an integer solution as
   (Z−z)(Z²+zZ+z²+1−xy).
   The discriminant of the remaining quadratic is4xy−3z²−4.
   There is no general second integer root and no involutive Vieta
   replacement comparable to a quadratic Markov equation.
   A descent must prove both rational square discriminant and height
   decrease; the factorization establishes neither.

<a id="q2316-a4"></a>

4. **Make the fibre discriminant uniformly negative.** With x=2,D=−1,
   the necessary divisor data give s=−1,t=−7,Δ=29.
   Thus the proposed blanket negative-discriminant lemma is false,
   even before imposing all parity conditions. What excludes this
   row is nonsquareness, not sign. A uniform square-avoidance theorem
   for the divisors of R(x) remains missing.

<a id="q2316-a5"></a>

5. **Use the everywhere-local integral proof.** The existing real,
   rational and every-prime integral points remain available.
   Local integrality at separately chosen primes does not make the
   displayed rational point globally integral, and no integral Hasse
   principle for this surface was proved. This final route supplies
   no global height or patching theorem.

All three full questions remain unresolved after their five failed routes.
The Q2316 coordinate certificate is filed separately at its exact scope.
