# Q549 — General-disjunction proof discovery

The target is a deterministic discovery algorithm polynomial in the input encoding and the **minimum general-disjunction leaf count**. A short certificate with polynomial-size binary coefficients does not supply such an algorithm.

## Q549-A1: enumerate directions of polynomial magnitude

**Attempt.** Restrict split coefficients to a polynomial in the input bit length, enumerate directions, and search their trees. This could be polynomial for a fixed number of dimensions if a short general proof always had such directions.

**Obstruction.** For integer N≥4, take

$$
P_N=\{(x,y):0\le y\le N,\quad 1/3\le x-Ny\le2/3\}.
$$

It is a bounded rational integer-free parallelogram with encoding O(log N). Splitting on x-Ny≤0 versus x-Ny≥1 gives two empty leaves. Its minimum leaf count is exactly two, since the root is nonempty.

For j=0,...,N, consider z_j=(Nj+1/2,j). For a split with integer normal (a,b), |a|,|b|≤N−2, either a=0 and every normal value at z_j is integral, or |aN+b|≥2. In the latter case a single open unit split gap can contain at most one of the z_j. Each witness follows a child until a split gap removes it; an empty leaf cannot retain it. Thus any refutation with these restricted normals needs at least N+1 internal nodes and N+2 leaves, or is unable to refute. In particular, coordinate-only branching has exponential overhead in input bits relative to the two-leaf general certificate.

This blocks the proposed coefficient-magnitude cutoff. It does not block polynomial **bit length**: (1,-N) has logarithmic encoding. For any fixed polynomial cutoff in input bits, large N satisfies that cutoff≤N−2.

**Outcome:** unsuccessful full-target attempt; streak 1. The direction search may instead use binary encoding and geometric/lattice information, but naïve bounded-magnitude enumeration cannot establish Q549.

## Q549-A2: branch only in primitive facet directions

**Attempt.** Avoid enumerating all normals by extracting the primitive integer normals of the input facets, then searching only splits in those directions.

**Obstruction.** Let

$$
T_N=\{(x,y):x\ge0,\quad x-6Ny\le-2N,\quad x+6Ny\le4N\}.
$$

Its vertices are (0,1/3),(N,1/2),(0,2/3). It is integer-free, and splitting on y≤0 versus y≥1 gives two empty leaves. Its primitive facet directions are (1,0),(1,-6N),(1,6N), up to signs. At z=(0,1/2) every such normal has an integer value. No integer-threshold split in any of these directions can remove z. Along every finite facet-only tree z therefore reaches a nonempty leaf. This calculus cannot refute T_N at all.

**Outcome:** unsuccessful full-target attempt; streak 2. Combining and saturating input rows can recover new integer normals such as (0,1); selecting the useful combination efficiently remains a different problem.

**Checks and source boundary.** [check_routes.py](check_routes.py) uses exact fractions on four parallelograms and four triangles; [receipt](ROUTE-CHECK-RESULTS.json). These elementary constructions obstruct proposed restricted discovery algorithms, not the full conjecture. General proof coefficient recompilation is a background theorem of [Dadush–Tiwari](https://arxiv.org/abs/2006.04124), not an automatization theorem. Target source: Gläser dissertation §§5–6, retained at ../../../texts/collections-f76a80f301f33456.txt.gz. No novelty claim.

## Q549-A3: complete binary-bounded direction enumeration

**Attempt.** Remove A1's incomplete coefficient cutoff. Use the known polynomial-bit recompilation theorem to enumerate every permitted normal and candidate proof tree, hoping a short minimum proof pays for the enumeration.

**Failure of the runtime argument.** On P_N above, the width in direction (a,b) is N|aN+b|+|a|/3. For a primitive integer direction to give two empty children its range must lie in an open unit slab. Therefore aN+b=0; primitiveness forces (a,b)=±(1,-N). A complete enumeration in increasing coefficient magnitude must reach N even though the optimal proof has two leaves and input length O(log N). It examines at least N−1 distinct primitive directions (1,-j), j<N, before the certificate. Exact enumeration on N=4,8,16,32,64 confirms the first normal.

This attempt differs from A1: it is complete, has no small-magnitude restriction, and fails its polynomial runtime goal rather than correctness. The proof-bit theorem gives a finite search and short encodings, not a polynomial number of labels. **Outcome:** unsuccessful; streak 3.

## Q549-A4: find split labels with one continuous LP

**Attempt.** For a two-leaf proof, introduce variables for its normal a and threshold b, constrain b<a·v<b+1 on all input vertices, and solve the resulting linear feasibility problem after dropping integrality.

**Obstruction.** The continuous problem admits a=0,b=-1/2 for every nonempty polytope. It provides no integer split. On promised P_N, two genuine labels ((1,-N),0) and ((-1,N),-1) are valid; their midpoint is that invalid zero-normal label. The set of real labels represented by convex relaxation therefore includes spurious certificates. Rounding that midpoint to an integer threshold leaves one child containing the whole nonempty root.

Keeping a and b integral produces another integer feasibility problem; no polynomial-time algorithm for it has been derived. This rejects the proposed lossless continuous relaxation, not every encoding of proof search or an integer-hull formulation. **Outcome:** unsuccessful; streak 4.

## Q549-A5: transfer variable-system non-automatizability by polynomial simulation

**Attempt.** Use the source's conditional non-automatizability of variable branching to disprove general-disjunction automatizability, by converting every short general proof into a variable proof with polynomial overhead in input bits and general proof size.

**Obstruction to the required simulation.** P_N has general leaf count two but variable leaf count at least N+2, with input length O(log N). A universal polynomial-overhead simulation of this kind is impossible. Thus the known restricted-system result cannot be transferred by that proposed conversion. Source-specific hardness constructions might still compare the two systems tightly; the obstruction does not rule those out or prove that Q549 has a positive answer.

This is a negative-answer route, separate from the discovery algorithms in A1–A4, although it reuses A1's separation family. It produces no new lower-bound theorem beyond that separation. **Outcome:** unsuccessful; streak 5.

Five specified full-target routes have failed to settle Q549. Subject to independent review, this reaches its per-problem stop limit. The exact catalog question remains unresolved, and B14 continues on its other targets.
