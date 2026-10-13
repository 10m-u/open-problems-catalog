# Q2188: power saving in the full degree-four Paley SOS bound

Exact target: SOS₄(G_p)=O(p^(1/2−ε)) for some absolute ε>0, through primes p≡1 mod4. Full question remains unresolved. In particular the known Ω(p^(1/3)) lower bound only restricts a possible exponent to ε≤1/6; it does not refute this question.

Primary source: [Kunisky–Yu](https://arxiv.org/abs/2211.02713), local `texts/papers/collections-1a69b18128a88092.txt.gz`, program (13), Definition 2.7, Remark 2.8, Theorems 3.1/5.1 and §6–7. Definitions and parameter statements were reread before these routes. Original B2 one-local conditioning and exact global degree-two obstruction are preserved; below are attempted extensions and their precise failures, not replacements.

<a id="a1"></a>
## A1. Prove a power saving through the ordinary one-local theta transfer

The earlier transfer gives SOS₄(G_p)≤1+τ(L_p), L_p the neighborhood on nonzero squares, ordinary clique theta. The proposed extension was to prove τ(L_p)=o(√p), ideally a power saving. This is impossible for this intermediate quantity.

Put n=(p−1)/2, d=(p−5)/4 and let A_L be its adjacency matrix. The global adjacency has minimum eigenvalue −(√p+1)/2. Principal compression gives A_L≽−(√p+1)I/2. Consequently

    X=[I+2A_L/(√p+1)]/n

is positive semidefinite, has trace 1 and zero entries at distinct nonedges. It is also entrywise nonnegative. Its objective is

    <J,X>=1+2d/(√p+1)
          =1+(p−5)/[2(√p+1)] ∼ √p/2.

So both ordinary and nonnegative one-local theta are Ω(√p). No upper bound on either can give a power saving by this transfer alone. The full degree-four program contains additional compatibility information across anchors which the transfer discards. This explicit local feasible witness is distinct from the earlier exact global theta witness. Extending it to any fixed localization depth gives the same obstruction and would not count as a new route.

**Outcome: failed full-target route; no contradiction to Q2188.**

<a id="a2"></a>
## A2. Condition on an edge and import the stronger two-local theta bound

The natural repair for A1 is to condition the degree-four pseudoexpectation on x_i x_j and invoke ordinary degree-two theta on the common neighborhood. The required conditional second moment is defined as a degree-four polynomial, but its positivity is not guaranteed: it would be the square of a polynomial of degree three before Boolean reduction, whereas the relaxation only requires squares of degree at most two.

An exact feasible witness establishes this failure, rather than only degree bookkeeping. On the Boolean cube {0,1}³ give weight 1 to seven points and weight −1/7 to (1,1,1), then divide by 48/7. Define the linear functional by this signed measure. Every polynomial q of degree at most two has zero third Walsh coefficient, so

    ∑_{a≠(1,1,1)} (−1)^|a|q(a)=q(1,1,1)

up to an immaterial sign. Cauchy gives ∑_{a≠(1,1,1)}q(a)²≥q(1,1,1)²/7. Hence the functional is nonnegative on all degree-two squares and is a feasible degree-four clique pseudoexpectation for K₃. Its symmetric squarefree moments are

    y_∅=1, y_i=5/12, y_{ij}=1/8, y_{123}=−1/48.

Conditioning on edge {1,2} is well-defined since y_{12}>0, but its conditional expectation of x₃, and thus x₃², is −1/6. It is not a feasible degree-two pseudoexpectation. The same witness also demonstrates why conditioning on one vertex need not give entrywise nonnegative second moments: y_{123}/y_1=−1/20. Thus neither replacing ordinary theta by Schrijver theta after one anchor nor importing ordinary theta after two anchors is justified by generic degree-four conditioning.

This is a counterexample to the proposed general conditioning theorem. It is not claimed to be an optimal Paley moment assignment, and a Paley-specific conditional-positivity theorem could still repair the route.

**Outcome: failed full-target route; exact missing lemma is Paley-specific pair-conditional positivity or a different degree-four transfer.**

<a id="a3"></a>
## A3. Use affine averaging to identify the full optimum with the FK optimum

The source proves FK₄(G_p)=Θ(p^(1/3)). If averaging could put every full feasible optimum into the FK family, that would solve Q2188 with ε=1/6. Affine averaging does force equal vertex moments and equal edge moments, but not equal moments on all triangles or four-cliques.

For p=37 there are two affine orbits of triangles, represented by {0,1,4} and {0,1,11}. To check this exactly, normalize any ordered adjacent anchor pair a,b to 0,1 by the square-affine map x↦(x−a)/(b−a), then take the minimum sorted normalized set over all anchor pairs. The two representatives have different canonical keys. The image set of 4 under the six triangle cross-ratio transformations is {4,10,12,26,28,34}; that of 11 is {11,27}.

Take a uniform distribution on the square-affine images of {0,1,4}. This is a genuine distribution on Paley cliques and therefore a feasible pseudoexpectation of every degree. It is already affine invariant, has equal vertex and edge moments, but its triangle moment is positive on the first orbit and zero on the second. It is not FK. Thus the symmetry-averaging argument cannot provide the identification. FK is a restriction of the primal feasible set, so its optimum gives a **lower** bound on the full SOS value.

This does not prove that no FK optimum is globally optimal; the exact missing lemma would be an objective-preserving replacement of arbitrary orbit-dependent moments by FK moments. Averaging alone is not such a replacement.

**Outcome: failed full-target reduction; the finite witness tests a false universal symmetry implication.**

<a id="a4"></a>
## A4. Repair random graph-matrix estimates by removing the constant direction

The source's diamond matrix is M=(p−3)(I−J), because Q²=pI−J. Its norm is (p−3)(p−1), much larger than the random-graph p^(3/2) scale. A possible repair is to project away constants first: with P=I−J/p,

    PMP=(p−3)P,

which has norm p−3. That really removes the offending large eigenvalue, so simply repeating the unprojected diamond obstruction would miss this improvement.

However, projected graph-matrix bounds do not verify the full moment matrix's positivity or the dual certificate: normalization and the objective couple to the deleted direction. The exact model block

    B=[[1, t·1^T], [t·1, cI]]

has a positive projected lower block cP whenever c≥0. Its full positive-semidefiniteness instead requires c≥pt². On the constant direction its two-by-two restriction is [[1,t√p],[t√p,c]]. For c=t=1 and p>1 it is indefinite despite the perfect projected bound. Its objective-scale sum pt is restricted by pt≤√(pc), which is still a square-root scale for c of order one.

This is a counterexample to the proposed criterion that projected norm control alone completes the moment/dual argument. It is not a constructed Paley counterexample to Q2188. The repaired route still needs compatible scalar and cross-block estimates in the constant representation; those were not obtained from the projection identity. The source's full Schur-complement proof explicitly retains these blocks.

**Outcome: failed sufficient proof route with a precise remaining constant-block obligation.**

<a id="a5"></a>
## A5. Reduce all affine-invariant degree-four moments to a scalar Fourier LP

The one-local theta graph is circulant, so its invariant matrices diagonalize by Fourier modes. The attempted extension was to average the full degree-four matrix and simultaneously diagonalize its affine-invariant union-dependent coefficients by a fixed scalar transform, leaving only linear inequalities.

This fails on the actual allowed moment-coordinate family. At p=37 index the edge-edge block by its 333 edges. For each clique-orbit key U define T_U(e,f)=1 if e∪f is a clique with affine key U and 0 otherwise. These matrices are symmetric, affine invariant, satisfy the nonclique zero pattern and the union-dependence condition. Yet with

    A=T_{(0,1,4,11)}, B=T_{(0,1,4)},

one has (AB−BA)_{(0,1),(0,4)}=1. The four-clique variation affects only the edge-edge block; thus this is also a nonzero block of the commutator of the full moment-coordinate variations. Symmetric matrices admitting a common fixed scalar orthogonal diagonalization commute, so no such transform diagonalizes this family.

These coordinates are actual feasible directions, not merely unrelated elements of the invariant algebra. The genuine uniform distribution on all cliques of size at most two gives a strictly positive-definite moment matrix on the compressed indices ∅, vertices and edges: if a quadratic multilinear polynomial vanishes on the empty set, all singletons and all edges, every allowed coefficient is zero. Sufficiently small moment perturbations along any triangle- or four-clique orbit preserve positive definiteness and all equality constraints. Affine averaging therefore does not collapse these directions.

Block matrix representation theory may still reduce the SDP substantially, but that produces positive-semidefinite blocks rather than a scalar LP. This route differs from A3: A3 attempted cardinality-only moment replacement; A5 retains all orbit coordinates and tests commutativity of their permitted matrices. Neither failure proves the full problem intractable.

**Outcome: failed scalar-LP route, exact noncommuting witness.**
