Gheysens Problem 8: negative answer by homogenization

Review date: 2026-10-13. Stable candidate: 5fcdf9fb9b2aa325605f.
Held source: Q102744007, physical PDF p.130, printed p.118.
Disposition: solved-source-reduction, independently checked by the coordinator.

Problem 8 asks whether a group of continuous linear transformations of a locally
convex space that leaves a bounded nonempty subset invariant must have a fixed
point in its closed convex hull. Theorem 5.2.21 of the same source supplies, for
a nonamenable countable group G, a continuous affine Hilbert action
alpha_g(v) = pi_g(v) + b_g with a bounded orbit and no common fixed point.
Translate the origin to a point on that bounded orbit, so {b_g : g in G} is
bounded. The pi_g are bounded invertible linear operators; their uniform
boundedness is unnecessary for the counterexample.

On the Hilbert space R direct-sum H define
T_g(t,v) = (t, pi_g(v) + t b_g).
The affine cocycle identity implies T_g T_h = T_gh. Each T_g is a bounded,
invertible linear operator, with inverse T_(g^-1). Thus the image of G is
literally a group of continuous linear transformations. Every T_g fixes 0.
The set A = {(1,b_g) : g in G} is nonempty and bounded, and T_h(A) = A.
Its closed convex hull is contained in the closed affine hyperplane t = 1.
If (1,v) in that hull were fixed by every T_g, then pi_g(v) + b_g = v for every
g, contradicting the absence of a common fixed point for the original action.
Consequently the requested fixed point in the closed convex hull need not exist.

The ambient fixed vector 0 is outside that hull. This distinction is essential:
the argument addresses the actual convex-hull conclusion rather than a stronger
claim that the linear action has no fixed vector.
