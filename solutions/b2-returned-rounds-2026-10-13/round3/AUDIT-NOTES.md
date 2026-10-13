# Proof-sensitive points and exclusions

## Midpoint results

The quotient direction must be the direction of a **maximum-dimensional**
affine subspace contained in R. Otherwise the full-fibre set need not be a
cap and the reflection-centre argument does not give at most one exceptional
fibre. “Maximal” in informal descriptions always means maximum dimension,
not merely inclusion-maximal.

The relation 2s−q = 2q−s uses characteristic three. Two colours are essential:
a complete bipartite conflict forces monochromatic fibre complements only
when there are two available labels.

The occupied quotient is coloured only outside its occupied set. Of two
same-colour quotient points, at least one whole fibre is monochromatic;
midpoints with a single appropriately coloured point in the other fill the
midpoint fibre. This is why partially occupied remainder fibres do not
invalidate the proof.

For the plane-free induction, all regular occupied line fibres contain at
least two remainder points; the single possible exception contains at least
one. Thus nine occupied fibres give at least seventeen points in a
three-space. The sharp three-dimensional theorem is applied to the actual
restricted partition on that three-space.

The all-dimension bound is an upper bound only. No claimed equality for n>=4,
sharpness of the n>=8 density threshold, or extension to higher-flat-free
remainders is supported by the current proof.

The appendix's cap incidence exclusions are checked with exact fractions.
For section sizes 3,5,7,11, n4 is nonintegral; for 6,8,9, n1 is negative;
for 10,12, n0 is negative. This arithmetic is included in the receipt.

## Entropy results

The tail theorem assumes p_n>0 for every nonnegative integer n, with no
negative support, and -log p_n = c n^beta+o(n^beta), c,beta>0. It does not
apply to two-sided tails: their difference-convolution asymptotics differ.

The proof does not assume termwise differentiability without justification.
Finite-coordinate perturbations keep the law componentwise comparable to
its starting law. Logarithms of input and output masses have polynomial
bounds, and the tail assumption supplies every needed polynomial moment.
These facts justify dominated differentiation and the later expectation
limits.

A negative asymptotic gradient is also an ascent obstruction: positive
mass at the distant atom can be transferred back to zero. Only positivity
of a sufficiently small transfer, not a uniform transfer size in n, is used.

Supremum equality for a prescribed tail class is an approximation theorem.
It does not assert that a member of the class maximizes the ratio. The
nonattainment theorem combines this approximation with an obstruction to
stationarity. No existence of a global extremizer, or necessity that an
extremizer have regular tails or full support, is asserted.

The finite Gaussian-shaped diagnostic has ratio approximately 1.2167 and is
not a better universal witness. It tests the differential calculation using
an exact finite ascent; the infinite tail proof does not rely on this test.

## Exploratory route

`exploratory/SPANNING-PLANE-FREE-4.json` records a four-dimensional MILP run
that hit a time limit with no primal solution. This is not infeasibility,
not a proof that all examples lie in a three-space, and not an exact value
of the extremal function. No result depends on that solver run.
