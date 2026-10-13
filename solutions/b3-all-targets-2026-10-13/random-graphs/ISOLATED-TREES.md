# Isolated-tree obstructions to stronger Q2400 certificates

These are failures of stronger sufficient conditions, not counterexamples
to log-concavity of the full random-graph row. Fix d>0 and let G=G(n,d/n).
For each fixed finite tree T on h vertices, there is an isolated component
isomorphic to T with probability1-O_(T,d)(1/n). Here is an elementary
second-moment proof, retaining explicit constants instead of treating
local tree structure as evidence for a full coefficient theorem.

Let A be the automorphism count of T, p=d/n,q=1-p, and n>max(d,2h).
For each injection of T's vertices into [n], identify maps differing by
an automorphism and count the event that its image is the entire isolated
component. The number of such distinct specified labeled edge sets is
(n)_h/A. The event fixes h-1 present edges and

    B=h(n-h)+binom(h,2)-(h-1)

absent edges: all external incidences and the internal nonedges. Thus

    E X_T=(n)_h/A * p^(h-1) q^B
         ~ n d^(h-1)e^(-dh)/A.

For disjoint images, the joint-event probability is the product times
q^(-h^2): the h^2 cross edges were each counted absent twice. Distinct
events with overlapping images are mutually exclusive, since an isolated
connected component cannot partially overlap another or have a different
edge set. Ignoring these negative covariances gives

    Var X_T <= E X_T +(E X_T)^2[q^(-h^2)-1],
    P(X_T=0) <=1/E X_T+q^(-h^2)-1=O_(T,d)(1/n).    (1)

The asymptotic holds for fixed d, even when d is a very large fixed
constant. No uniform-in-d rate or practicality at moderate n is asserted.

## Real-rootedness fails with high probability

Take T=K_(1,3), h=4,A=6. Its independence polynomial is

    I_T(x)=(1+x)^3+x=1+4x+3x^2+x^3.

The cubic discriminant is -31, hence there are two nonreal roots.
The independence polynomial factors over connected components. Therefore
an isolated claw makes the entire I_G non-real-rooted. Formula(1) proves

    P(I_G has only real roots)=O_d(1/n)->0.

Its actual coefficient row [1,4,3,1] is log-concave. This defeats a
uniform Newton/real-rootedness strengthening while preserving the exact
catalog question.

## The multivariate matroid/Lorentzian route also fails

Homogenize the multiaffine independent-set generating polynomial to
degree n with a slack variable y. For the three vertices of an induced
path with center c and leaves a,b, two legal exponent vectors correspond
to independent sets {c} and {a,b}. Their slack exponents are n-1 and n-2.
In the M-convex symmetric-exchange requirement, choose the center
coordinate where the first exceeds the second. The only deficient
coordinates in the first vector are a,b; exchanging either would require
the illegal independent pair {c,a} or {c,b} in the second vector.
Thus the support is not M-convex. A Lorentzian polynomial requires
M-convex support, so that stronger multivariate certificate cannot apply
to any graph containing such an induced path, including every isolated
claw event above. This is a support/exchange obstruction, distinct from
the scalar nonreal roots, although the same frequent component witnesses
both.

There is an additional exact obstruction to proving the unweighted
question through a theorem for **every** nonnegative vertex weighting.
On the claw give each leaf weight1 and the center weight10. Its row is
[1,13,3,1], failing 3^2>=13. If G contains an induced claw, set every
other vertex weight to epsilon>0. At epsilon=0 its weighted polynomial
equals this claw polynomial. The violated coefficient inequality is
strict, so it stays violated for sufficiently small positive epsilon
by continuity. The resulting weights are all positive. This excludes
only the proposed all-weight certificate; the unweighted graph remains
the exact target.

## Componentwise log-concavity is not a high-probability reduction

Convolution preserves log-concavity for nonnegative rows with interval
support. One might try to apply that fact to every component of the random
graph, replacing the complete-row problem with componentwise proofs.
That stronger component condition fails with probability tending to one.

Use the known26-vertex tree T1 of
[Kadrawi--Levit, Section2](https://arxiv.org/html/2305.01784).
It has a central vertex connected to three branch roots, whose numbers
of pendant length-two arms are3,4,4. This fixes the tree without using
an unavailable figure. For a branch with k arms, deletion of the branch
root gives (1+2x)^k; choosing it gives x(1+x)^k. Deleting or choosing
the central vertex therefore proves the complete polynomial identity

    I_T(x)=product_(k in {3,4,4})[(1+2x)^k+x(1+x)^k]
             +x(1+2x)^11.

In particular [x^14]I_T=1, [x^13]I_T=51 and [x^12]I_T=2979;
51^2-2979=-378<0. These values are independently reconstructed from
the actual edge list by deletion/closed-neighborhood recursion. The
tree counterexample is already published; it is not a new resolution
or a newly invented random-graph witness.

The automorphism count is2*(3!)*(4!)^2=6912: the center has degree3,
the unequal branch has degree4, the two equal branches have degree5,
and pendant arm permutations are independent. Formula(1), with h=26,
shows an isolated copy of this **fixed** non-log-concave tree occurs
with probability1-O_d(1/n). Consequently

    P(every component of G has a log-concave row)=O_d(1/n)->0.

The failure of that structural reduction is a new inference about its
random-model scope, not a recount of the published deterministic tree
calibration. A non-log-concave factor does not force its convolution
with the other components to fail. Thus this result neither disproves
Q2400 nor proves that small components explain its tail. A full proof
must control compensation in the combined row, rather than assume
each factor separately has the desired property.
