# Q550 — Matching proof discovery with a treewidth parameter

The target bounds runtime by f(tw(G)) poly(|G|,δ,T_var), in the **original variable-branch calculus**. Computing maximum matchings or refuting a presolved formulation does not by itself produce such a proof.

## Q550-A1: transfer a minimum presolved proof unchanged

**Attempt.** Apply the source's Nemhauser–Trotter-style presolving, solve the remaining disjoint odd cycles, and treat the returned tree as an equally small original variable proof.

**Exact obstruction to that transfer.** The bowtie graph has two triangles 012 and 034 meeting only at vertex 0. With δ=1 the cutoff is 5/2; the integer matching maximum is 2 and the fractional maximum 5/2. An optimum fractional matching sets edge 12 to one and the three edges of triangle 034 to one half. Fixing the integral optimum edge 12 to one leaves a triangle requiring two variable leaves.

The original problem has minimum **three** leaves. For every candidate root edge, one child still has a fractional matching of size 5/2; no root yields two empty LP leaves. Conversely branching on 12 gives an empty zero child and a triangle in the one child, for three leaves. The exact synthesizer enumerates all half-integral feasible vectors and recursively minimizes leaf count, confirming both claims.

**Outcome:** unsuccessful full-target attempt; streak 1. This disproves unchanged/minimum-size proof transfer, not polynomial-overhead lifting. A lifting algorithm could still settle Q550; none has been proved here. The source explicitly treats presolving as a stronger system (§5.6).

## Q550-A2: collapse proof-search states to matching-value profiles

**Attempt.** Use the ordinary bounded-treewidth matching DP, retaining only the maximum integral and fractional matching value at an empty boundary, to synthesize minimum variable proof trees.

**Exact obstruction.** C_5 and the bowtie both have n=5, treewidth 2, integral matching maximum 2, fractional maximum 5/2, and δ=1. Their minimum leaf counts are respectively 2 and 3. Thus those value profiles do not determine the required proof behavior even without a boundary. A DP that identifies them loses the certificate objective. The source's signatures instead retain possible branch precursors and every leaf's boundary coverage.

**Outcome:** unsuccessful full-target attempt; streak 2. This blocks that particular compression rule. It does not exclude richer states with polynomial T_var dependence.

**Evidence:** [exact synthesizer](check_routes.py), [receipt](ROUTE-CHECK-RESULTS.json). The LP oracle is exact because fractional matching optima are half-integral, also under consistent edge fixings: forced-one edges remove their endpoints and forced-zero edges remove their edges. The checker enumerates all feasible half-integral vectors, so its maximum includes an optimum. The recursive search considers every remaining edge at every state.

Target and stronger-system distinction: Gläser dissertation Question 5.26, Proposition 5.27 and §5.6, retained at ../../../texts/collections-f76a80f301f33456.txt.gz. No unrestricted resolution or novelty claim.

## Q550-A3: search only balanced short proof trees

**Attempt.** A proof with T leaves is supposed to admit a balanced variable proof of depth O(log T). If true, bounded-treewidth signatures would only have to describe short levels rather than long sequential histories.

**All-size obstruction.** Let F_q be q triangles sharing one hub, with distinct outer pairs. It has 2q+1 vertices, treewidth two, integer maximum matching q, fractional maximum q+1/2, and cutoff q+1/2 for δ=1. There are q feasible fractional witnesses: put halves on triangle j and ones on all other outer-pair edges.

A variable in triangle i is fractional in only witness i; its value is the same integer in all other witnesses. At every branch, all surviving witnesses except at most one follow the same child. Thus every refutation has a path with at least q internal nodes, regardless of its total size.

Conversely branch on each outer-pair edge successively. The zero child is empty under the cutoff. For that missing pair i, put z_i=x_(hub,u_i)+x_(hub,v_i); other triangles contribute at most 1+z_j/2, and sum_j z_j≤1. Total matching value is at most q−1+z_i+(1−z_i)/2≤q. The one child forces that triangle's spokes to zero and reduces to F_(q−1), subtracting one from the cutoff. This gives q+1 leaves and depth q.

Hence T_var=q+1 but **every** variable proof has depth at least q, not O(log T_var). Exact synthesis checks q=1,2,3; the witness argument proves all q. Balancing cannot cure this without altering the allowed branching system. **Outcome:** unsuccessful; streak 3.

## Q550-A4: use one representative of each original edge orbit

**Attempt.** Exploit automorphisms to choose one branching variable per original edge orbit, avoiding a large candidate set throughout the search.

**Obstruction.** In a disjoint union of q≥2 triangles all edges form one automorphism orbit. With δ=q the cutoff is q+1/2 and the polytope is integer-free. Branching only on a single representative edge fixes at most one triangle. Both children still have fractional maximum 1+3(q−1)/2≥q+1/2, so neither is a leaf. No additional allowed unfixed representative remains. The restricted search is incomplete.

Correct symmetry reduction must recompute the stabilizer of the current fixed assignments; original orbits cease to be interchangeable. This failure is unrelated to matching-value compression at an empty boundary. **Outcome:** unsuccessful; streak 4.

## Q550-A5: compose full component refutations by a product

**Attempt.** Discover a refutation for every connected component and substitute each tree at all leaves of the previous one, obtaining an original variable proof with the product of component leaf counts.

**Runtime obstruction.** For q disjoint triangles at δ=1, the cutoff is 3q/2. Branching on any one triangle edge reduces its fractional maximum from 3/2 to one in both children, so the entire LP is empty in both children and T_var=2. Fully certifying all q triangles independently uses 2^q leaves. Treewidth is two and δ=1 throughout, so this product work cannot be absorbed into f(treewidth) poly(input,δ,T_var).

This is a valid but excessively strong proof construction: it establishes all component integer bounds even though the global threshold needs only one component's loss. The failure requires a threshold-aware composition rule, rather than proving every component fully. **Outcome:** unsuccessful; streak 5.

Five specified sufficient routes have failed to settle Q550. Subject to independent review, the problem reaches its per-problem stop limit; it is not disproved. The exact synthesis controls, including friendship depth and both cutoffs on disjoint triangles, are in the updated [receipt](ROUTE-CHECK-RESULTS.json).
