# Combinatorics & Graph Theory (part 3 of 4)

[Subject overview](combinatorics-graph-theory.md) · Parts: [1](combinatorics-graph-theory-part-1.md) · [2](combinatorics-graph-theory-part-2.md) · [3](combinatorics-graph-theory-part-3.md) · [4](combinatorics-graph-theory-part-4.md)

<a id="q3568"></a>

## Q3568. Width-two order-polynomial positivity

**Status:** Open, partial results · **Kind:** conjecture (Conjecture 7.1) · **Collection** 36

Does every width-two finite poset P have Ω\_P(t) with nonnegative coefficients in the ordinary power basis?

**Context.** Degree: Doctoral thesis; 2021 defence listed, award unverified. Advisors: Luca Moci. Source type: Later joint paper; doctoral genealogy verified Paper: Skew shapes, Ehrhart positivity, and beyond Authors: Luis Ferroni, Alejandro H. Morales, Greta Panova Origin: Authors’ conjecture, informed by Haimu Wang’s computations; not established as thesis-originated. Setup: For a finite poset P, Ω\_P(t) counts weakly order-preserving maps P→{1,…,t}. Its width is the maximum antichain size.

**Source.** Luis Ferroni, Alejandro H. Morales, Greta Panova. *Skew shapes, Ehrhart positivity, and beyond*. 2026. [primary source](https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/plms.70204) Location: Final article §7.1, Conjecture 7.1; definitions §2.1.

**Literature check.** Status: Final August 2026 article retains this conjecture. Funding-only correction; bounded recheck 2026-10-09 found no resolution.

**Results.**

- **Partial result**: Every ordinal sum of singleton or two-element antichain layers has nonnegative ordinary order-polynomial coefficients. Its exact factorization is a rising factorial times a residual polynomial whose roots lie on a vertical line with nonpositive real part. Empty and chain cases are included. General width-two posets with incomplete cross-layer comparisons remain unresolved. Internally reviewed at this scope; no novelty or external peer-review claim. [Details](../../solutions/b3-all-targets-2026-10-13/posets/WIDTH-TWO-WEAK-ORDERS.md).
- **Partial result** (B3-ALL-TARGETS-Q3568-WEAK-LAYERS: Order-polynomial positivity for all weak orders of width two): Every ordinal sum of singleton or two-element antichain layers has nonnegative ordinary order-polynomial coefficients. Its exact factorization is a rising factorial times a residual polynomial whose roots lie on a vertical line with nonpositive real part. Empty and chain cases are included. Remaining/limits: General width-two posets with incomplete cross-layer comparisons remain unresolved. [Report](../../solutions/b3-all-targets-2026-10-13/posets/WIDTH-TWO-WEAK-ORDERS.md).
- **Investigated, unresolved** (B3-ALL-TARGETS-STOP-REGISTER: Reviewed B3 failed routes and per-target stopping decisions): 45 targets have each reached five consecutive substantive distinct full-target failures. STATUS.json records every accepted route, written analysis, evidence path and review provenance. Partial results do not reset counters. Rejected proposed attempts, source-range replays, service errors and shared mechanisms remain explicit rather than supplying extra counts. Remaining/limits: These questions remain mathematically unresolved. A failure-limit stop is an operational disposition, not a counterexample or proof. Missing historical archives remain separate evidence issues. [Report](../../solutions/b3-all-targets-2026-10-13/STATUS.json).

**Further links.** [1](https://phd.unibo.it/matematica/en/agenda/public-defense-of-the-doctoral-thesis-by-luis-rivetti-ferroni) · [2](https://arxiv.org/pdf/2503.16403v3)


<a id="q3569"></a>

## Q3569. Periodic zero-extension

**Status:** Solved here: proved · **Kind:** conjecture (Conjecture 9.1) · **Collection** 36

For p≥1, is [w∈L_U iff w0^p∈L_U for every w∈A\*] equivalent to having infinite words a_0,…,a_{p−1} with rep_U(U_{np+i}−1)=Pref_{np+i}(a_i) for all n≥0 and 0≤i&lt;p, necessarily satisfying σ^j(a_i)≤lex a_{i−j mod p} for every j≥0? Here σ deletes the first letter.

**Context.** Degree: Docteur en Sciences Advisors: Émilie Charlier. Source type: Doctoral dissertation Origin: Thesis conjecture; Rigo’s context-free question. Setup: Let U=(U_n) be strictly increasing positive integers, U_0=1, with bounded successive ratios. Write rep_U for greedy representation over alphabet A, L_U=0\*rep_U(N), and Max_U={rep_U(U_n−1):n≥0}; Pref_k means length-k prefix.

**Source.** Savinien Kreczman. *Linear numeration systems without a dominant root, alternate base numeration systems, and their links*. Université de Liège, 2026. Advisor(s): Émilie Charlier. [primary source](https://orbi.uliege.be/handle/2268/345086) Location: Conjecture 9.1, printed p.280; definitions pp.12–13.

**Literature check.** Status: No resolution located by 2026-10-09.

**Further links.** [1](https://orbi.uliege.be/bitstream/2268/345086/1/Kreczman_PhD_Thesis_JuryRemarks.pdf)

**Result (2026-10-09).** For every p>=1, validity is preserved and reflected by appending p zeroes exactly when maximal greedy words are nested along residue classes modulo p. Their unique infinite limits satisfy every stated cross-residue lexicographic shift inequality. Full Conjecture 9.1 for positional U-systems; the separate alternate-base and noncanonical-shift conjectures are not resolved.

[Proof](../../solutions/round-2026-10-09/discrete/Q3569-periodic-zero-extension.md) · [Internal review](../../solutions/round-2026-10-09/algebra/review-Q3569.md) · [Exact computational controls](../../solutions/round-2026-10-09/discrete/periodic-zero-checks.json). This is a research proposal with a separate internal AI review, not an externally peer-reviewed result.



<a id="q3570"></a>

## Q3570. Context-free Max_U

**Status:** Open · **Kind:** open problem (Problem 8) · **Collection** 36

Characterize linear-recurrence U whose minimal characteristic polynomial has unique maximal-modulus root β>1 and Max_U is context-free.

**Context.** Degree: Docteur en Sciences Advisors: Émilie Charlier. Source type: Doctoral dissertation Origin: Thesis conjecture; Rigo’s context-free question. Setup: Let U=(U_n) be strictly increasing positive integers, U_0=1, with bounded successive ratios. Write rep_U for greedy representation over alphabet A, L_U=0\*rep_U(N), and Max_U={rep_U(U_n−1):n≥0}; Pref_k means length-k prefix.

**Source.** Savinien Kreczman. *Linear numeration systems without a dominant root, alternate base numeration systems, and their links*. Université de Liège, 2026. Advisor(s): Émilie Charlier. [primary source](https://orbi.uliege.be/handle/2268/345086) Location: Problem 8, printed pp.288–290.

**Literature check.** Status: No resolution located by 2026-10-09.

**Further links.** [1](https://orbi.uliege.be/bitstream/2268/345086/1/Kreczman_PhD_Thesis_JuryRemarks.pdf)


<a id="q3573"></a>

## Q3573. Squared-outdegree extremum excluding the regular five-tournament

**Status:** Open · **Kind:** conjecture (Conjecture 3.3) · **Collection** 36

For every n≥1, does T_4(n) maximize Σ\_v d⁺(v)² among n-vertex digraphs containing no Reg_5 subdigraph?

**Context.** Degree: PhD defence verified; award unverified. Advisors: Daniel Král, Richard Montgomery. Source type: Later paper; advisor’s doctoral-student list verifies genealogy Paper: L2 Turán Problems for Small Tournaments and Stability Origin: Author’s conjecture in arXiv:2609.05042v1, 4 September 2026; no thesis-origin claim. Setup: Digraphs are loopless, with at most one arc per ordered pair; opposite arcs are allowed. Reg_5 has vertex set Z/5Z and arcs i→i+1,i+2. T_4(n) has four balanced parts, both arcs between different parts, and no arcs within parts.

**Source.** Daniel Iľkovič. *L2 Turán Problems for Small Tournaments and Stability*. 2026. [primary source](https://arxiv.org/abs/2609.05042) Location: Conjecture 3.3, printed p.4; definitions §2.

**Literature check.** Status: Only v1 listed and no later resolution located in bounded 2026-10-09 check.

**Further links.** [1](https://www.ucw.cz/~kral/cv-stud.html)


<a id="q3574"></a>

## Q3574. Cohen–Macaulay harmonic algebras of hypersimplices

**Status:** Open · **Kind:** open problem · **Collection** 36

Is H_{P_{ℓ,1,n}} Cohen–Macaulay for all integers 1≤ℓ≤n?

**Context.** Degree: PhD defence verified; award unverified. Advisors: Brendon Rhoades. Source type: Later paper; May 2025 PhD defence verified Paper: Graded Ehrhart theory for hypersimplices Authors: Nathaniel Libman, Weston Miller Origin: First question specializes Reiner–Rhoades’s earlier conjecture; second is the authors’ computationally supported proposal. Setup: For finite Z⊂Q^n, let J_Z be generated by highest-degree parts of polynomials vanishing on Z, and V_Z={h∈Q[x_1,…,x_n]:f(∂)h=0 for all f∈J_Z}. Set H_P=⊕\_{r≥0}x_0^r V_{rP∩Z^n}, with ordinary multiplication. Let P_{ℓ,m,n}={x∈[0,m]^n:Σx_i=ℓ}.

**Source.** Nathaniel Libman, Weston Miller. *Graded Ehrhart theory for hypersimplices*. 2026. [primary source](https://arxiv.org/abs/2608.27438) Location: §6, first bullet, printed pp.18–19; definitions §2.1.

**Literature check.** Status: Inspected arXiv:2608.27438v1; bounded 2026-10-09 check found no later resolution.

**Further links.** [1](https://mathweb.ucsd.edu/~bprhoades/advising.html)


<a id="q3575"></a>

## Q3575. Degree-one generation for cube-slice harmonic algebras

**Status:** Open · **Kind:** open problem · **Collection** 36

For positive integers m,n and 1≤ℓ≤⌊mn/2⌋, is H_{P_{ℓ,m,n}} generated as a Q-algebra in x_0-degree one?

**Context.** Degree: PhD defence verified; award unverified. Advisors: Brendon Rhoades. Source type: Later paper; May 2025 PhD defence verified Paper: Graded Ehrhart theory for hypersimplices Authors: Nathaniel Libman, Weston Miller Origin: First question specializes Reiner–Rhoades’s earlier conjecture; second is the authors’ computationally supported proposal. Setup: For finite Z⊂Q^n, let J_Z be generated by highest-degree parts of polynomials vanishing on Z, and V_Z={h∈Q[x_1,…,x_n]:f(∂)h=0 for all f∈J_Z}. Set H_P=⊕\_{r≥0}x_0^r V_{rP∩Z^n}, with ordinary multiplication. Let P_{ℓ,m,n}={x∈[0,m]^n:Σx_i=ℓ}.

**Source.** Nathaniel Libman, Weston Miller. *Graded Ehrhart theory for hypersimplices*. 2026. [primary source](https://arxiv.org/abs/2608.27438) Location: §6, third bullet, printed p.19.

**Literature check.** Status: Inspected arXiv:2608.27438v1; bounded 2026-10-09 check found no later resolution.

**Further links.** [1](https://mathweb.ucsd.edu/~bprhoades/advising.html)


<a id="q3576"></a>

## Q3576. Proximity under order, size and vertex-connectivity constraints

**Status:** Open · **Kind:** open problem · **Collection** 36

For admissible n,m,κ, determine the maximum π(G) among κ-connected G.

**Context.** Degree: Philosophiae Doctor in Mathematics Advisors: Peter Dankelmann, Sonwabile Mafunda. Source type: Doctoral dissertation Origin: Formalizations of the dissertation’s unnumbered future directions. Setup: For a connected simple n-vertex graph G, n≥2, with at least m edges, set a_G(v)=(n−1)^{-1}Σ\_u d_G(u,v), remoteness ρ(G)=max_v a_G(v), and proximity π(G)=min_v a_G(v). Connectivity constraints are lower bounds.

**Source.** Sufiyan Arif Mallu. *Bounds on proximity and remoteness in graphs and digraphs*. University of Johannesburg, 2025. Advisor(s): Peter Dankelmann, Sonwabile Mafunda. [primary source](https://ujcontent.uj.ac.za/esploro/outputs/doctoral/Bounds-on-proximity-and-remoteness-in/9960708807691) Location: Conclusion, p.136; proximity definition Chapter 1.

**Literature check.** Status: Later digraph/outerplanar results do not resolve these cases; checked 2026-10-09.

**Further links.** [1](https://www.uj.ac.za/members/mr-sufiyani-mallu/)


<a id="q3577"></a>

## Q3577. Contiguity of the random regular graph process

**Status:** Open · **Kind:** open problem · **Collection** 36

As n→∞ through nd even, are P_n and U_n mutually contiguous, meaning P_n(A_n)→0 iff U_n(A_n)→0 for every sequence of graph events A_n?

**Context.** Degree: PhD in Mathematics Advisors: Lutz Warnke. Source type: Doctoral dissertation restating an earlier conjecture Origin: Wormald’s 1999 Conjecture 6.3, restated in the thesis and Molloy–Surya–Warnke paper. Setup: Fix d≥2. On labeled vertices [n], repeatedly add a uniformly chosen missing edge whose endpoints both have degree below d, stopping when none is available. Let P_n be the final graph’s law conditioned on d-regularity, and U_n the uniform simple d-regular graph law.

**Source.** Erlang Surya. *Concentration and Sharp Thresholds in Random Graphs*. University of California San Diego, 2025. Advisor(s): Lutz Warnke. [primary source](https://escholarship.org/uc/item/7vt625fh) Location: Thesis Chapter 2, pp.4–5; final JCTB 176 (2026), Introduction.

**Literature check.** Status: January 2026 journal introduction explicitly retains it; irregular-degree noncontiguity theorem excludes this case. Bounded check 2026-10-09.

**Further links.** [1](https://mathweb.ucsd.edu/~lwarnke/PhD_Thesis_ErlangSurya.pdf) · [2](https://www.sciencedirect.com/science/article/pii/S0095895625000577)


<a id="q3578"></a>

## Q3578. Polynomial clique-degeneracy bounds forbidding broadleaved stars

**Status:** Open · **Kind:** open problem (Problem 6) · **Collection** 36

For every r≥3, ζ≥2 and r-broadleaved ζ-star H, is there k>0 such that degen_r(G)≤b(G)^k for every graph G with no induced H?

**Context.** Degree: PhD in Combinatorics and Optimization Advisors: Sophie Spirkl, Rowan Yeats. Source type: Doctoral dissertation Origin: Problem in ongoing joint work with LaGrange, Rundström and Spirkl, incorporated in the dissertation. Setup: An r-broadleaved ζ-star replaces each leaf of K_{1,ζ} by a nonempty clique of size at most r−1, preserving adjacency to the center. Let d_r^F(v) count a largest vertex-disjoint family of (r−1)-cliques in N_F(v), degen_r(G)=max_{∅≠F⊆G} min_v d_r^F(v), and b(G)=max{t:K_{t,t}⊆G}, with b=0 for edgeless graphs.

**Source.** Aristotelis Chaniotis. *Preserving and Generalizing χ-boundedness*. University of Waterloo, 2025. Advisor(s): Sophie Spirkl, Rowan Yeats. [primary source](https://uwspace.uwaterloo.ca/items/26df24d4-8ee7-4bab-9975-be038b27d919) Location: Problem 6, printed p.118; definitions pp.33–35.

**Literature check.** Status: Source gives only an unspecified bounding function. No polynomial-bound resolution located by 2026-10-09.

**Further links.** [1](https://uwspace.uwaterloo.ca/bitstreams/9a05e803-e0ed-4ee6-a495-2ff062ffb57b/download)


<a id="q3579"></a>

## Q3579. A general combinatorial rule for complementary-sum Chern plethysm

**Status:** Open · **Kind:** open problem (Problem 26) · **Collection** 36

Give a cancellation-free combinatorial interpretation of c_{λμ}(n) for arbitrary λ,μ,n in the stated range.

**Context.** Degree: PhD defence verified; award unverified. Advisors: Brendon Rhoades. Source type: Earlier joint paper; doctoral genealogy verified Paper: Combinatorics and Representation Theory of Special Cases of Chern Plethysm Authors: Nathaniel Libman, Gidon Orelowitz Origin: Joint-paper open problem, not verified as thesis-originated. Setup: Let s_λ be the Schur polynomial in n variables. For partitions λ,μ with length at most n and |λ|=|μ|, define c_{λμ}(n)=[s_μ]s_λ(X−x_1,…,X−x_n), where X=x_1+⋯+x_n.

**Source.** Nathaniel Libman, Gidon Orelowitz. *Combinatorics and Representation Theory of Special Cases of Chern Plethysm*. 2024. [primary source](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v31i2p20) Location: Final §7, Problem 26, p.20; definitions pp.4–5. Preprint Problem 1 is renumbered.

**Literature check.** Status: Final April 2024 article inspected; bounded 2026-10-09 author/topic checks found no general combinatorial rule.

**Results.**

- **Investigated, unresolved** (B3-ALL-TARGETS-STOP-REGISTER: Reviewed B3 failed routes and per-target stopping decisions): 45 targets have each reached five consecutive substantive distinct full-target failures. STATUS.json records every accepted route, written analysis, evidence path and review provenance. Partial results do not reset counters. Rejected proposed attempts, source-range replays, service errors and shared mechanisms remain explicit rather than supplying extra counts. Remaining/limits: These questions remain mathematically unresolved. A failure-limit stop is an operational disposition, not a counterexample or proof. Missing historical archives remain separate evidence issues. [Report](../../solutions/b3-all-targets-2026-10-13/STATUS.json).

**Further links.** [1](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v31i2p20/pdf)


<a id="q3580"></a>

## Q3580. Rigid-graph realizations in even norms

**Status:** Open · **Kind:** conjecture (Conjecture 6.1) · **Collection** 36

For even p≥4 and d≥1, if G is rigid in ℓ\_p^d, is |D_G(P)|≥c_{G,p,d}|P|^{|V|−1} for every nonempty finite P⊂R^d, for some c_{G,p,d}>0?

**Context.** Degree: PhD, awarded 13 May 2025 Advisors: Misha Rudnev. Source type: Joint paper after dissertation-first access attempt Paper: Generalised Erdős distance theory on graphs Authors: Sean Dewar, Nora Frankl, Samuel Mansfield, Anthony Nixon, Jonathan Passant, Audie Warren Origin: Authors’ May 2025 paper conjectures. Setup: Let D_G(P)={(‖p_u−p_v‖)\_{uv∈E}:p∈P^V} for G=(V,E). Generic ℓ\_p-rigidity means generic vertex placements have finitely many realizations with their edge lengths, modulo isometries.

**Source.** Sean Dewar, Nora Frankl, Samuel Mansfield, Anthony Nixon, Jonathan Passant, Audie Warren. *Generalised Erdős distance theory on graphs*. 2025. [primary source](https://arxiv.org/abs/2505.06590) Location: Conjecture 6.1, p.39; metric and rigidity definitions §§1.2–1.3.

**Literature check.** Status: Only v1; no resolution located by 2026-10-09.

**Further links.** [1](https://research-information.bris.ac.uk/en/studentTheses/geometric-and-arithmetic-structure-in-finite-point-sets/)


<a id="q3581"></a>

## Q3581. Euclidean realization counts

**Status:** Open · **Kind:** conjecture (Conjecture 6.6) · **Collection** 36

For every fixed connected simple graph G with minimum degree at least two, does |D_G(P)|≥c_G|P|^{|V|−1} hold for all nonempty finite P⊂R² in the Euclidean norm, for some c_G>0?

**Context.** Degree: PhD, awarded 13 May 2025 Advisors: Misha Rudnev. Source type: Joint paper after dissertation-first access attempt Paper: Generalised Erdős distance theory on graphs Authors: Sean Dewar, Nora Frankl, Samuel Mansfield, Anthony Nixon, Jonathan Passant, Audie Warren Origin: Authors’ May 2025 paper conjectures. Setup: Let D_G(P)={(‖p_u−p_v‖)\_{uv∈E}:p∈P^V} for G=(V,E). Generic ℓ\_p-rigidity means generic vertex placements have finitely many realizations with their edge lengths, modulo isometries.

**Source.** Sean Dewar, Nora Frankl, Samuel Mansfield, Anthony Nixon, Jonathan Passant, Audie Warren. *Generalised Erdős distance theory on graphs*. 2025. [primary source](https://arxiv.org/abs/2505.06590) Location: Conjecture 6.6, p.41.

**Literature check.** Status: Only v1; no resolution located by 2026-10-09.

**Further links.** [1](https://research-information.bris.ac.uk/en/studentTheses/geometric-and-arithmetic-structure-in-finite-point-sets/)


<a id="q3582"></a>

## Q3582. Hamilton–Waterloo decompositions with one six-cycle factor and coprime other length

**Status:** Open · **Kind:** open problem · **Collection** 36

For which integers N≥3 and v≥1 with gcd(6,N)=1 and lcm(6,N)|v can K_v−I be edge-decomposed into one C_6-factor and (v−4)/2 C_N-factors?

**Context.** Degree: PhD in Mathematical Sciences Advisors: Melissa S. Keranen. Source type: Doctoral dissertation and later accepted joint manuscript Paper: On the Hamilton-Waterloo Problem with a single factor of 6-cycles Authors: Zazil Santizo Huerta, Melissa S. Keranen Origin: Unresolved case identified in the dissertation and subsequent joint paper. Setup: A C_k-factor is a spanning disjoint union of k-cycles. For even v, write K_v−I for the complete graph with a perfect matching removed.

**Source.** Zazil Santizo Huerta. *On Graph Decompositions and Designs: Exploring the Hamilton-Waterloo Problem with a Factor of 6-Cycles and Projective Planes of Order 16*. Michigan Technological University, 2024. Advisor(s): Melissa S. Keranen. [primary source](https://digitalcommons.mtu.edu/etdr/1740/) Location: Thesis conclusion p.124; accepted paper §7, p.31; definition §1.

**Literature check.** Status: Watermarked accepted manuscript, matching AMC DOI 10.26493/1855-3974.3316.6d0, retains the gap; checked 2026-10-09. Final typeset file not inspected.

**Further links.** [1](https://digitalcommons.mtu.edu/michigantech-p2/2231/)


<a id="q3583"></a>

## Q3583. Bounded-depth minor extensions of arbitrary matroids

**Status:** Open · **Kind:** conjecture (Conjecture 1) · **Collection** 36

Is there a function f such that every finite nonempty matroid M is a minor of some matroid N with cdd(N)≤f(bd(M))?

**Context.** Degree: PhD defence verified; award unverified. Advisors: Daniel Král. Source type: Joint paper; dissertation access attempted; advisor verifies May 2025 PhD defence Paper: Branch-depth is minor closure of contraction-deletion-depth Authors: Marcin Briański, Daniel Král, Kristýna Pekárková Origin: Joint-paper conjecture. Setup: For finite nonempty matroid M with ground set E, λ(X)=r(X)+r(E−X)−r(E). For |E|≥2, bd(M) minimizes k over trees with an internal vertex and leaves bijective to E, radius≤k, and λ(X)≤k for unions X of components after deleting an internal vertex; bd(singleton)=0. Define cdd(singleton)=1; for disconnected M take the maximum cdd of its components; otherwise cdd(M)=1+min_e min(cdd(M/e),cdd(M\e)).

**Source.** Marcin Briański, Daniel Král, Kristýna Pekárková. *Branch-depth is minor closure of contraction-deletion-depth*. 2024. [primary source](https://arxiv.org/abs/2402.16215) Location: Conjecture 1, p.17; Conjecture 2 is equivalent and not counted separately.

**Literature check.** Status: Reaffirmed in Measuring Depth of Matroids v3, p.36 (2026-10-02).

**Further links.** [1](https://www.ucw.cz/~kral/cv-stud.html)


<a id="q3620"></a>

## Q3620. Parallel-hyperplane mass bisection

**Status:** Open · **Kind:** conjecture (Conjecture 2.4) · **Collection** 37

For all integers d,k≥1, can any d+k−1 absolutely continuous probability measures on R^d be simultaneously bisected by the chessboard coloring of at most k parallel hyperplanes?

**Context.** Advisor(s): Pavle Blagojević. Origin: Older Soberón–Takahashi and Tverberg–Vrećica conjectures, restated in the thesis. Setup: For parallel affine hyperplanes, their chessboard coloring alternates black and white across consecutive slabs. A bisection gives each color half the measure. All partitions below have nonempty parts.

**Source.** Nikola Sadovek. *Obstructions across geometry and topology*. Freie Universität Berlin, 2025. Advisor(s): Pavle Blagojević. [primary source](https://refubium.fu-berlin.de/bitstream/handle/fub188/51916/Sadovek%20-%20Doctoral%20dissertation.pdf?isAllowed=y&sequence=1) Location: Conjecture 2.4, printed p.18 (PDF p.30).

**Literature check.** Status: Open in thesis; bisection is reaffirmed in June 2026 v3, Conjecture 1.5. No general resolution located, 2026-10-09.

**Further links.** [1](https://arxiv.org/html/2404.14320v3) · [2](https://refubium.fu-berlin.de/handle/fub188/51916) · [3](https://www.mi.fu-berlin.de/fb/dates/disputationen/Sadovek_-Nikola---MI---Aushang.pdf)


<a id="q3621"></a>

## Q3621. Tverberg–Vrećica common affine transversal

**Status:** Open · **Kind:** conjecture (Conjecture 3.6) · **Collection** 37

Let 0≤k&lt;d and r_0,…,r_k≥1 be integers. Given A_i⊂R^d with |A_i|=(r_i−1)(d−k+1)+1, can each A_i be partitioned into r_i parts whose convex hulls all meet one common affine k-plane?

**Context.** Advisor(s): Pavle Blagojević. Origin: Older Soberón–Takahashi and Tverberg–Vrećica conjectures, restated in the thesis. Setup: For parallel affine hyperplanes, their chessboard coloring alternates black and white across consecutive slabs. A bisection gives each color half the measure. All partitions below have nonempty parts.

**Source.** Nikola Sadovek. *Obstructions across geometry and topology*. Freie Universität Berlin, 2025. Advisor(s): Pavle Blagojević. [primary source](https://refubium.fu-berlin.de/bitstream/handle/fub188/51916/Sadovek%20-%20Doctoral%20dissertation.pdf?isAllowed=y&sequence=1) Location: Conjecture 3.6, printed p.32 (PDF p.44).

**Literature check.** Status: Open in thesis; bisection is reaffirmed in June 2026 v3, Conjecture 1.5. No general resolution located, 2026-10-09.

**Further links.** [1](https://arxiv.org/html/2404.14320v3) · [2](https://refubium.fu-berlin.de/handle/fub188/51916) · [3](https://www.mi.fu-berlin.de/fb/dates/disputationen/Sadovek_-Nikola---MI---Aushang.pdf)


<a id="q3669"></a>

## Q3669. Double-star exclusions and domatic growth

**Status:** Open · **Kind:** conjecture (Conjecture 3) · **Collection** 37

For every fixed s,t≥1, is the class with no induced S_{s,t} DOM-bounded?

**Context.** Doctoral connection: Variations on the graph colouring problem; Université Paris-Saclay, 2026; advisers Nathalie Aubrun, François Pirot. Graphs are finite, nonempty and simple; δ is minimum degree. DOM(G) maximizes parts in a vertex partition each meeting every closed neighbourhood. DOM-bounded means DOM(G)≥f(δ(G)) for some unbounded f:Z_{≥0}→R_{>0}. S_{s,t} is an edge with s,t pendant leaves at its ends. Authors: Quentin Chuet, Selma Djelloul, Hoang La, François Pirot, Hossein Zaredehabadi. Remaining double-star conjecture; explicit problems.

**Source.** Quentin Chuet, Selma Djelloul, Hoang La, François Pirot and Hossein Zaredehabadi. *A Domatic Analogue of χ-Bounded Graph Classes and the Gyárfás–Sumner Conjecture*. 2026. [primary source](https://arxiv.org/abs/2606.02030) Location: Conjecture 3, p.2; stars and P4 settled.

**Literature check.** Status: v1, June 2026; no resolution found by 2026-10-09.


<a id="q3670"></a>

## Q3670. Linear domatic growth for unit disk graphs

**Status:** Open · **Kind:** open problem (Problem 1) · **Collection** 37

Does an absolute c>0 satisfy DOM(G)≥cδ(G) for every intersection graph G of equal-radius disks in the plane?

**Context.** Doctoral connection: Variations on the graph colouring problem; Université Paris-Saclay, 2026; advisers Nathalie Aubrun, François Pirot. Graphs are finite, nonempty and simple; δ is minimum degree. DOM(G) maximizes parts in a vertex partition each meeting every closed neighbourhood. DOM-bounded means DOM(G)≥f(δ(G)) for some unbounded f:Z_{≥0}→R_{>0}. S_{s,t} is an edge with s,t pendant leaves at its ends. Authors: Quentin Chuet, Selma Djelloul, Hoang La, François Pirot, Hossein Zaredehabadi. Remaining double-star conjecture; explicit problems.

**Source.** Quentin Chuet, Selma Djelloul, Hoang La, François Pirot and Hossein Zaredehabadi. *A Domatic Analogue of χ-Bounded Graph Classes and the Gyárfás–Sumner Conjecture*. 2026. [primary source](https://arxiv.org/abs/2606.02030) Location: Problem 1, p.19.

**Literature check.** Status: v1, June 2026; no resolution found by 2026-10-09.


<a id="q3671"></a>

## Q3671. Fractional domatic spectrum

**Status:** Open · **Kind:** open problem (Problem 3) · **Collection** 37

Determine {FDOM(G):G is a nonempty finite simple graph}.

**Context.** Doctoral connection: Variations on the graph colouring problem; Université Paris-Saclay, 2026; advisers Nathalie Aubrun, François Pirot. For nonempty finite simple G, δ is minimum degree and girth is shortest-cycle length. A dominating (p:q)-colouring assigns each vertex q colours from [p]={1,…,p}, with all p colours on each closed neighbourhood; p,q are positive integers. FDOM(G)=sup p/q over these colourings. Put F(g)=inf{FDOM(G):δ(G)=2,girth(G)≥g}; F_P(g) restricts this infimum to planar G. Authors: Quentin Chuet, Hugo Demaret, Hoang La, François Pirot. Explicit problems and conjecture.

**Source.** Quentin Chuet, Hugo Demaret, Hoang La and François Pirot. *Fractional domatic number and minimum degree*. 2025. [primary source](https://arxiv.org/abs/2508.19617) Location: Problem 3, p.31.

**Literature check.** Status: v1, 2025-08-27; no resolution found by 2026-10-09.


<a id="q3672"></a>

## Q3672. Sharp planar fractional domatic values

**Status:** Open · **Kind:** conjecture (Conjecture 33) · **Collection** 37

For integers k≥1 and g≥3 with 3k−1≤g≤3k+1, is F_P(g)=(3k+1)/(k+1)?

**Context.** Doctoral connection: Variations on the graph colouring problem; Université Paris-Saclay, 2026; advisers Nathalie Aubrun, François Pirot. For nonempty finite simple G, δ is minimum degree and girth is shortest-cycle length. A dominating (p:q)-colouring assigns each vertex q colours from [p]={1,…,p}, with all p colours on each closed neighbourhood; p,q are positive integers. FDOM(G)=sup p/q over these colourings. Put F(g)=inf{FDOM(G):δ(G)=2,girth(G)≥g}; F_P(g) restricts this infimum to planar G. Authors: Quentin Chuet, Hugo Demaret, Hoang La, François Pirot. Explicit problems and conjecture.

**Source.** Quentin Chuet, Hugo Demaret, Hoang La and François Pirot. *Fractional domatic number and minimum degree*. 2025. [primary source](https://arxiv.org/abs/2508.19617) Location: Conjecture 33, p.32.

**Literature check.** Status: v1, 2025-08-27; no resolution found by 2026-10-09.


<a id="q3673"></a>

## Q3673. Forbidden subgraphs reducing frugal colouring growth

**Status:** Open · **Kind:** open problem (Problem A) · **Collection** 37

For fixed β≥1, classify the bipartite graphs H satisfying χβ(Δ,H)=o(Δ^{1+1/β}) as Δ→∞.

**Context.** Doctoral connection: Variations on the graph colouring problem; Université Paris-Saclay, 2026; advisers Nathalie Aubrun, François Pirot. Graphs are finite and simple; β≥1 is integral. A β-frugal colouring is proper, with each colour used at most β times in each open neighbourhood. Let χβ(Δ,H) maximize the minimum such colour count over H-subgraph-free graphs of maximum degree at most Δ. Let χ\_{2,H}(Δ) maximize the minimum proper-colouring count avoiding bichromatic H, over all graphs of maximum degree at most Δ. Authors: Quentin Chuet. v3, 2026-10-04; Problem C has been solved.

**Source.** Quentin Chuet. *Frugal colourings of graphs via sparse hypergraph colouring*. 2026. [primary source](https://arxiv.org/abs/2603.23379) Location: Problem A, p.3.

**Literature check.** Status: Problems A–B; subsequently reaffirmed in arXiv:2609.39716.


<a id="q3674"></a>

## Q3674. Sharp avoiding-colouring exponent

**Status:** Open · **Kind:** open problem (Problem B) · **Collection** 37

For every fixed connected bipartite H with m≥2 edges, is χ\_{2,H}(Δ)=Θ(Δ^{1+1/(m−1)})?

**Context.** Doctoral connection: Variations on the graph colouring problem; Université Paris-Saclay, 2026; advisers Nathalie Aubrun, François Pirot. Graphs are finite and simple; β≥1 is integral. A β-frugal colouring is proper, with each colour used at most β times in each open neighbourhood. Let χβ(Δ,H) maximize the minimum such colour count over H-subgraph-free graphs of maximum degree at most Δ. Let χ\_{2,H}(Δ) maximize the minimum proper-colouring count avoiding bichromatic H, over all graphs of maximum degree at most Δ. Authors: Quentin Chuet. v3, 2026-10-04; Problem C has been solved.

**Source.** Quentin Chuet. *Frugal colourings of graphs via sparse hypergraph colouring*. 2026. [primary source](https://arxiv.org/abs/2603.23379) Location: Problem B, p.11.

**Literature check.** Status: Problems A–B; subsequently reaffirmed in arXiv:2609.39716.


<a id="q3675"></a>

## Q3675. Maximum degree controls inversion diameter

**Status:** Open · **Kind:** conjecture (Conjecture 1.2) · **Collection** 37

Is D(G)≤Δ(G) for every finite simple graph G?

**Context.** Doctoral connection: Variations on the graph colouring problem; Université Paris-Saclay, 2026; advisers Nathalie Aubrun, François Pirot. An inversion of X⊆V(G) reverses arcs with both endpoints in X. For finite simple labelled G, D(G) maximizes, over pairs of orientations, the minimum inversions transforming one into the other; Δ(G) is maximum degree. A subdivision replaces edges by internally vertex-disjoint paths. Authors: Carmen Arana, Thomas Bellitto, Hector Buffière, Quentin Chuet, Théo Pierron, Amadeus Reinald. Degree conjecture restates Havet–Hörsch–Rambaud; subdivision question is posed here.

**Source.** Carmen Arana, Thomas Bellitto, Hector Buffière, Quentin Chuet, Théo Pierron and Amadeus Reinald. *Inversion diameter and 2-edge-colored homomorphisms*. 2026. [primary source](https://arxiv.org/abs/2602.24171) Location: Conjecture 1.2, p.2.

**Literature check.** Status: v1, 2026-02-27; degree conjecture reaffirmed in June 2026.


<a id="q3676"></a>

## Q3676. Bounded subdivision penalty for inversions

**Status:** Open · **Kind:** open problem (Question 1.6) · **Collection** 37

Is there an absolute c such that D(H)≤D(G)+c for every subdivision H of every graph G?

**Context.** Doctoral connection: Variations on the graph colouring problem; Université Paris-Saclay, 2026; advisers Nathalie Aubrun, François Pirot. An inversion of X⊆V(G) reverses arcs with both endpoints in X. For finite simple labelled G, D(G) maximizes, over pairs of orientations, the minimum inversions transforming one into the other; Δ(G) is maximum degree. A subdivision replaces edges by internally vertex-disjoint paths. Authors: Carmen Arana, Thomas Bellitto, Hector Buffière, Quentin Chuet, Théo Pierron, Amadeus Reinald. Degree conjecture restates Havet–Hörsch–Rambaud; subdivision question is posed here.

**Source.** Carmen Arana, Thomas Bellitto, Hector Buffière, Quentin Chuet, Théo Pierron and Amadeus Reinald. *Inversion diameter and 2-edge-colored homomorphisms*. 2026. [primary source](https://arxiv.org/abs/2602.24171) Location: Question 1.6, p.3.

**Literature check.** Status: v1, 2026-02-27; degree conjecture reaffirmed in June 2026.


<a id="q3677"></a>

## Q3677. Extensions of an almost-complete graphic matroid

**Status:** Open · **Kind:** open problem · **Collection** 37

Determine an asymptotic equivalent, as n→∞, for log₂ ext(M(K_{n+1}−e)), where e is one edge.

**Context.** Doctoral connection: Enumerating matroid extensions; University of Waterloo, 2023; advisers Peter Nelson. M(G) is the cycle matroid of G: its independent sets are forests. Let ext(M) count matroids N on E(M)∪{x}, with x a fixed new element and N\x=M, retaining the labels of E(M). Authors: Shayla Redlin Hume. Formalization of the explicit unnumbered asymptotic gap.

**Source.** Shayla Redlin Hume. *Enumerating matroid extensions*. University of Waterloo, 2023. Advisor(s): Peter Nelson. [primary source](https://uwspace.uwaterloo.ca/handle/10012/19829) Location: Section 9.3, pp.124–125.

**Literature check.** Status: 2023 dissertation; no later resolution located by 2026-10-09.


<a id="q3678"></a>

## Q3678. Log-concavity for oriented-matroid circuit polytopes

**Status:** Open · **Kind:** conjecture (Conjecture 3.11) · **Collection** 37

Does h_i\*²≥h_{i−1}\*h_{i+1}\* hold for every such P and 1≤i&lt;d?

**Context.** Doctoral connection: Oriented Matroid Circuit Polytopes; Washington University in St. Louis, 2025; advisers Laura Escobar, John Shareshian. For a finite oriented matroid with nonempty signed-circuit set C⊂{0,±1}^E, put P=conv(C) and d=dim P. Define h\*(t)=Σ\_{i=0}^d h_i\*t^i by Σ\_{m≥0}|mP∩Z^E|t^m=h\*(t)/(1−t)^{d+1}. Authors: Laura Escobar, Jodi McWhirter. Conjecture present in v2, absent from v1; thesis priority unverified.

**Source.** Laura Escobar and Jodi McWhirter. *Oriented Matroid Circuit Polytopes*. 2025. [primary source](https://arxiv.org/abs/2501.00108) Location: Conjecture 3.11, p.14.

**Literature check.** Status: v2, 2026-07-14; no later resolution located by 2026-10-09.

**Results.**

- **Investigated, unresolved** (B3-ALL-TARGETS-CIRCUIT-GAUGES: Circuit-polytope lattice reductions and fractional carries): Rank-one root circuit polytopes have binomial-square Ehrhart numerators in every size. The cographic K_N-minus-one-edge family is nonreflexive for every N>=5. The exact free-sum Ehrhart correction counts pairs of nonintegral gauges with fractional parts summing to at most one. A represented uniform rank-two family has sign-circuit span and saturated lattice equal to R^N and Z^N despite its flow-kernel dimension N-2. Remaining/limits: The root family is known and rederived here. The new structural obstructions are not counterexamples to full h\* log-concavity. The complete conjecture remains unresolved. [Report](../../solutions/b3-all-targets-2026-10-13/oriented-matroids/Q3678-ATTEMPTS.md).
- **Investigated, unresolved** (B3-ALL-TARGETS-STOP-REGISTER: Reviewed B3 failed routes and per-target stopping decisions): 45 targets have each reached five consecutive substantive distinct full-target failures. STATUS.json records every accepted route, written analysis, evidence path and review provenance. Partial results do not reset counters. Rejected proposed attempts, source-range replays, service errors and shared mechanisms remain explicit rather than supplying extra counts. Remaining/limits: These questions remain mathematically unresolved. A failure-limit stop is an operational disposition, not a counterexample or proof. Missing historical archives remain separate evidence issues. [Report](../../solutions/b3-all-targets-2026-10-13/STATUS.json).


<a id="q3679"></a>

## Q3679. Maximum density of spectrally symmetric orientations

**Status:** Open · **Kind:** open problem (Problem 1) · **Collection** 37

Determine ρ=sup{2|E(G)|/|V(G)|²:G admits a spectrally symmetric orientation}.

**Context.** Doctoral connection: Graph Coverings with Few Eigenvalues or No Short Cycles; University of Waterloo, 2023; advisers Chris Godsil. For an orientation D of a finite nonempty simple graph G, define H_uv=e^{iπ/3} when u→v, H_uv=e^{−iπ/3} when v→u, and H_uv=0 otherwise. Call D spectrally symmetric when the eigenvalue multiset of H is invariant under λ↦−λ. Authors: Saieed Akbari, Jonathan Aloni, Maxwell Levit, Bojan Mohar, Steven Xia. Explicit extremal problem. v2, 2026-09-09; the bounds are now 31/36≤ρ≤10/11.

**Source.** Saieed Akbari, Jonathan Aloni, Maxwell Levit, Bojan Mohar and Steven Xia. *Spectrally symmetric orientations of graphs*. 2025. [primary source](https://arxiv.org/abs/2512.08049) Location: Problem 1, p.2.


<a id="q3680"></a>

## Q3680. Constant-degree expanders far from bipartite

**Status:** Open · **Kind:** conjecture (Conjecture 8.3) · **Collection** 37

Is there an absolute C>0 such that every d-regular γ-expander that is γ-far from bipartite and satisfies d≥(Cγ^{-1})^C is Hamiltonian?

**Context.** Doctoral connection: Extremal and Ramsey Problems; ETH Zürich, 2025; advisers Benny Sudakov. For γ>0, a finite simple n-vertex d-regular graph is a γ-expander if e(S,V\S)≥γd|S| whenever 1≤|S|≤2n/3; e counts crossing edges. It is γ-far from bipartite if at least γ|E| edge deletions are needed to make it bipartite. Hamiltonian means containing a spanning cycle. Authors: Domagoj Bradač, Oliver Janzer. Conjectures posed in the later paper.

**Source.** Domagoj Bradač and Oliver Janzer. *Hamiltonicity of regular sublinear expanders*. 2026. [primary source](https://arxiv.org/abs/2605.15043) Location: Conjecture 8.3, p.38.

**Literature check.** Status: v1, 2026-05-14; later 2026 counterexamples do not settle these degree thresholds.


<a id="q3681"></a>

## Q3681. Constant-degree bipartite expanders

**Status:** Open · **Kind:** conjecture (Conjecture 8.2) · **Collection** 37

Is there an absolute C>0 such that every bipartite d-regular γ-expander with d≥(Cγ^{-1})^C is Hamiltonian?

**Context.** Doctoral connection: Extremal and Ramsey Problems; ETH Zürich, 2025; advisers Benny Sudakov. For γ>0, a finite simple n-vertex d-regular graph is a γ-expander if e(S,V\S)≥γd|S| whenever 1≤|S|≤2n/3; e counts crossing edges. It is γ-far from bipartite if at least γ|E| edge deletions are needed to make it bipartite. Hamiltonian means containing a spanning cycle. Authors: Domagoj Bradač, Oliver Janzer. Conjectures posed in the later paper.

**Source.** Domagoj Bradač and Oliver Janzer. *Hamiltonicity of regular sublinear expanders*. 2026. [primary source](https://arxiv.org/abs/2605.15043) Location: Conjecture 8.2, p.38.

**Literature check.** Status: v1, 2026-05-14; later 2026 counterexamples do not settle these degree thresholds.


<a id="q3682"></a>

## Q3682. Remoteness under higher edge-connectivity and size constraints

**Status:** Open · **Kind:** open problem · **Collection** 37

For admissible n,m and λ≥4, determine the maximum ρ(G) among λ-edge-connected G.

**Context.** Doctoral connection: Bounds on proximity and remoteness in graphs and digraphs; University of Johannesburg, 2025; advisers Peter Dankelmann, Sonwabile Mafunda. For a connected finite simple n-vertex graph G, n≥2, with at least m edges, define ρ(G)=max_v (n−1)^{-1}Σ\_u d_G(u,v). Connectivity constraints are lower bounds. Authors: Sufiyan Arif Mallu. Formalizations of the dissertation’s unnumbered future directions.

**Source.** Sufiyan Arif Mallu. *Bounds on proximity and remoteness in graphs and digraphs*. University of Johannesburg, 2025. Advisor(s): Peter Dankelmann, Sonwabile Mafunda. [primary source](https://ujcontent.uj.ac.za/esploro/outputs/doctoral/Bounds-on-proximity-and-remoteness-in/9960708807691) Location: Conclusion, p.136; Chapter 2; (n,m)-graph definition p.5.

**Literature check.** Status: No later resolution found in checks through 2026-10-09.


<a id="q3683"></a>

## Q3683. Remoteness with minimum degree and size prescribed

**Status:** Open · **Kind:** open problem · **Collection** 37

For admissible n,m,δ, determine the maximum ρ(G) among G with minimum degree at least δ.

**Context.** Doctoral connection: Bounds on proximity and remoteness in graphs and digraphs; University of Johannesburg, 2025; advisers Peter Dankelmann, Sonwabile Mafunda. For a connected finite simple n-vertex graph G, n≥2, with at least m edges, define ρ(G)=max_v (n−1)^{-1}Σ\_u d_G(u,v). Connectivity constraints are lower bounds. Authors: Sufiyan Arif Mallu. Formalizations of the dissertation’s unnumbered future directions.

**Source.** Sufiyan Arif Mallu. *Bounds on proximity and remoteness in graphs and digraphs*. University of Johannesburg, 2025. Advisor(s): Peter Dankelmann, Sonwabile Mafunda. [primary source](https://ujcontent.uj.ac.za/esploro/outputs/doctoral/Bounds-on-proximity-and-remoteness-in/9960708807691) Location: Conclusion, p.136, final sentence.

**Literature check.** Status: No later resolution found in checks through 2026-10-09.


<a id="q3702"></a>

## Q3702. Ordinary subsum-denominator log-concavity

**Status:** Open, partial results · **Kind:** conjecture (Conjecture 4) · **Collection** 38

For n≥1, n∉{3,5,6,7}, is ∏\_{i=1}^n(1+x^i)^{⌊log_2(n/i)⌋+1} log-concave?

**Context.** Setup: A polynomial ∑\_j a_j x^j is log-concave if a_j²≥a_{j−1}a_{j+1} at each internal index.

**Source.** Ballantine, Beck, Feigon and Maurischat. *Reciprocals of subsum polynomials*. 2026. [primary source](https://doi.org/10.1007/s11139-026-01419-0) Location: Conjecture 4, PDF p.18; Proposition 3.8(a).

**Literature check.** Status: Final explicitly retains both; n≥6 is the authors’ corrected range. No later resolution located, 9 October 2026.

**Results.**

- **Partial result**: For every n>=8, the first two nontrivial log-concavity inequalities of F_n and their reflected counterparts are strict. Its normalized coefficient law has variance asymptotic to 2\*n^3/21 and converges after centering and standardization to the normal law. The finite permitted small endpoints are treated separately. A central limit does not determine exact interior curvature signs; the full conjecture remains unresolved. Internally reviewed at this scope; no novelty or external peer-review claim. [Details](../../solutions/b3-all-targets-2026-10-13/subsums/BOUNDARIES.md).
- **Partial result** (B3-ALL-TARGETS-Q3702-ENDPOINTS: First two subsum-product inequalities and a central limit): For every n>=8, the first two nontrivial log-concavity inequalities of F_n and their reflected counterparts are strict. Its normalized coefficient law has variance asymptotic to 2\*n^3/21 and converges after centering and standardization to the normal law. Remaining/limits: The finite permitted small endpoints are treated separately. A central limit does not determine exact interior curvature signs; the full conjecture remains unresolved. [Report](../../solutions/b3-all-targets-2026-10-13/subsums/BOUNDARIES.md).
- **Investigated, unresolved** (B3-ALL-TARGETS-STOP-REGISTER: Reviewed B3 failed routes and per-target stopping decisions): 45 targets have each reached five consecutive substantive distinct full-target failures. STATUS.json records every accepted route, written analysis, evidence path and review provenance. Partial results do not reset counters. Rejected proposed attempts, source-range replays, service errors and shared mechanisms remain explicit rather than supplying extra counts. Remaining/limits: These questions remain mathematically unresolved. A failure-limit stop is an operational disposition, not a counterexample or proof. Missing historical archives remain separate evidence issues. [Report](../../solutions/b3-all-targets-2026-10-13/STATUS.json).


<a id="q3703"></a>

## Q3703. Binary subsum-numerator log-concavity

**Status:** Open, partial results · **Kind:** conjecture (Conjecture 7) · **Collection** 38

Let B(n) be partitions of n into powers of 2, with multiplicities m_λ(2^i). For n≥6, is ∑\_{λ∈B(n)}∏\_{i=0}^{⌊log_2 n⌋}(1+x^{2^i})^{⌊n/2^i⌋−m_λ(2^i)} log-concave?

**Context.** Setup: A polynomial ∑\_j a_j x^j is log-concave if a_j²≥a_{j−1}a_{j+1} at each internal index.

**Source.** Ballantine, Beck, Feigon and Maurischat. *Reciprocals of subsum polynomials*. 2026. [primary source](https://doi.org/10.1007/s11139-026-01419-0) Location: Conjecture 7, PDF p.21; Section 4.

**Literature check.** Status: Final explicitly retains both; n≥6 is the authors’ corrected range. No later resolution located, 9 October 2026.

**Results.**

- **Partial result**: For every n>=4, the first and final nontrivial log-concavity inequalities of H_n are strict. Exact mixture moments also prove that H_(2^s) is not ultra-log-concave for every s>=2. Ultra-log-concavity is stronger than the frozen ordinary log-concavity question. All interior inequalities remain unresolved. Internally reviewed at this scope; no novelty or external peer-review claim. [Details](../../solutions/b3-all-targets-2026-10-13/subsums/BOUNDARIES.md).
- **Partial result** (B3-ALL-TARGETS-Q3703-ENDPOINTS: Strict binary-partition sum boundary inequalities): For every n>=4, the first and final nontrivial log-concavity inequalities of H_n are strict. Exact mixture moments also prove that H_(2^s) is not ultra-log-concave for every s>=2. Remaining/limits: Ultra-log-concavity is stronger than the frozen ordinary log-concavity question. All interior inequalities remain unresolved. [Report](../../solutions/b3-all-targets-2026-10-13/subsums/BOUNDARIES.md).
- **Investigated, unresolved** (B3-ALL-TARGETS-STOP-REGISTER: Reviewed B3 failed routes and per-target stopping decisions): 45 targets have each reached five consecutive substantive distinct full-target failures. STATUS.json records every accepted route, written analysis, evidence path and review provenance. Partial results do not reset counters. Rejected proposed attempts, source-range replays, service errors and shared mechanisms remain explicit rather than supplying extra counts. Remaining/limits: These questions remain mathematically unresolved. A failure-limit stop is an operational disposition, not a counterexample or proof. Missing historical archives remain separate evidence issues. [Report](../../solutions/b3-all-targets-2026-10-13/STATUS.json).


<a id="q3716"></a>

## Q3716. For all 0≤h,i,j≤D, is (E_h⊗E_i⊗E_j)Λ={0} equivalent to q^h_{ij}=0?

**Status:** Open · **Kind:** open problem · **Collection** 38

For all 0≤h,i,j≤D, is (E_h⊗E_i⊗E_j)Λ={0} equivalent to q^h_{ij}=0?

**Context.** Let Γ be a finite Q-polynomial distance-regular graph with vertex set X, diameter D≥1, adjacency A, and Q-polynomially ordered primitive idempotents E₀,…,E_D. On V=(ℂ^X)^{⊗3}, M^{(r)} acts as M on factor r. Define B₁(e_x⊗e_y⊗e_z)=|X|(E₁)\_{yz}(e_x⊗e_y⊗e_z), and B₂,B₃ cyclically. Let Λ be the smallest subspace containing 1^{⊗3} invariant under A^{(r)},B_r (r=1,2,3), where 1=∑\_x e_x. Define Krein parameters by E_i∘E_j=|X|⁻¹∑\_h q^h_{ij}E_h (entrywise product). Let F_r be the coordinate projection onto basis tensors whose other two vertex indices coincide.

**Source.** Paul Terwilliger. *The S₃-symmetric tridiagonal algebra*. 2025. [primary source](https://doi.org/10.1007/s10801-025-01420-8) Location: Conjectures 12.2–12.3, p.32; the latter is an equivalent dimension formulation.

**Literature check.** Status: Publisher final and later literature checked October 9, 2026; no general resolution located.


<a id="q3717"></a>

## Q3717. For every r∈{1,2,3}, are dim(F_rΛ)=dim(E₀^{(r)}Λ)=D+1?

**Status:** Open · **Kind:** open problem · **Collection** 38

For every r∈{1,2,3}, are dim(F_rΛ)=dim(E₀^{(r)}Λ)=D+1?

**Context.** Let Γ be a finite Q-polynomial distance-regular graph with vertex set X, diameter D≥1, adjacency A, and Q-polynomially ordered primitive idempotents E₀,…,E_D. On V=(ℂ^X)^{⊗3}, M^{(r)} acts as M on factor r. Define B₁(e_x⊗e_y⊗e_z)=|X|(E₁)\_{yz}(e_x⊗e_y⊗e_z), and B₂,B₃ cyclically. Let Λ be the smallest subspace containing 1^{⊗3} invariant under A^{(r)},B_r (r=1,2,3), where 1=∑\_x e_x. Define Krein parameters by E_i∘E_j=|X|⁻¹∑\_h q^h_{ij}E_h (entrywise product). Let F_r be the coordinate projection onto basis tensors whose other two vertex indices coincide.

**Source.** Paul Terwilliger. *The S₃-symmetric tridiagonal algebra*. 2025. [primary source](https://doi.org/10.1007/s10801-025-01420-8) Location: Conjectures 12.2–12.3, p.32; the latter is an equivalent dimension formulation.

**Literature check.** Status: Publisher final and later literature checked October 9, 2026; no general resolution located.


<a id="q3768"></a>

## Q3768. Full-length Ramsey chains in complete graphs

**Status:** Open · **Kind:** conjecture (Conjecture 2.6) · **Collection** 38

For every n≥3 and every red/blue edge-coloring of K_n, do there exist pairwise edge-disjoint monochromatic subgraphs G_1,…,G_{n−1}, where G_i has i edges and G_i is isomorphic to a subgraph of G_{i+1} for 1≤i&lt;n−1? The colors of different G_i may differ.

**Context.** Dissertation route: Chatterjee, Ramsey Chains in Graphs, Western Michigan University, PhD, 2026; first advisor Ping Zhang. Origin: Chartrand–Zhang’s 2023 conjecture, restated here.

**Source.** Ritabrato Chatterjee and Ping Zhang. *On Ramsey indexes of graphs*. 2026. [primary source](https://combinatorialpress.com/article/jcmcc/Volume%20129/on-ramsey-indexes-of-graphs.pdf) Location: Conjecture 2.6, journal p.5; PDF p.3.

**Literature check.** Status: Publisher final and later literature checked 9 October 2026; no resolution located. Thesis metadata verified; thesis text unavailable.

**Further links.** [1](https://scholarworks.wmich.edu/dissertations/4282/)


<a id="q3769"></a>

## Q3769. Must Pl(G)≤Δ(G)?

**Status:** Open · **Kind:** conjecture (Conjecture 2.6) · **Collection** 38

Must Pl(G)≤Δ(G)?

**Context.** Paper: Pushing Vertices to Make Graphs Irregular; Julien Bensmail, Clara Marcille, Mano Orenga. Origin: Questions introduced in this paper. Setup: For a finite simple graph G without K₂ components, let Pl(G) be the least k admitting ρ:V(G)→{0,…,k} such that σ(v)=d(v)(1+ρ(v))+Σ\_{u∈N(v)}ρ(u) differs across every edge.

**Source.** Julien Bensmail, Clara Marcille and Mano Orenga. *Pushing Vertices to Make Graphs Irregular*. 2025. [primary source](https://dmtcs.episciences.org/16418/pdf) Location: Conjecture 2.6, p.5.

**Literature check.** Status: Final DMTCS (2025); Δ-conjecture reaffirmed June 2026; recognition questions unresolved in checked sources. https://doi.org/10.61091/ars167-10

**Further links.** [1](https://doctorat.u-bordeaux.fr/soutenances/soutenances-du-24-06-2025) · [2](https://doi.org/10.61091/ars167-10)


<a id="q3770"></a>

## Q3770. Determine the computational complexity of deciding Pl(G)≤1 for bipartite G.

**Status:** Open · **Kind:** open problem · **Collection** 38

Determine the computational complexity of deciding Pl(G)≤1 for bipartite G.

**Context.** Paper: Pushing Vertices to Make Graphs Irregular; Julien Bensmail, Clara Marcille, Mano Orenga. Origin: Questions introduced in this paper. Setup: For a finite simple graph G without K₂ components, let Pl(G) be the least k admitting ρ:V(G)→{0,…,k} such that σ(v)=d(v)(1+ρ(v))+Σ\_{u∈N(v)}ρ(u) differs across every edge.

**Source.** Julien Bensmail, Clara Marcille and Mano Orenga. *Pushing Vertices to Make Graphs Irregular*. 2025. [primary source](https://dmtcs.episciences.org/16418/pdf) Location: Section 5, p.14.

**Literature check.** Status: Final DMTCS (2025); Δ-conjecture reaffirmed June 2026; recognition questions unresolved in checked sources. https://doi.org/10.61091/ars167-10

**Further links.** [1](https://doctorat.u-bordeaux.fr/soutenances/soutenances-du-24-06-2025) · [2](https://doi.org/10.61091/ars167-10)


<a id="q3771"></a>

## Q3771. For every fixed integer k≥2, is deciding Pl(G)≤k NP-complete?

**Status:** Open · **Kind:** open problem · **Collection** 38

For every fixed integer k≥2, is deciding Pl(G)≤k NP-complete?

**Context.** Paper: Pushing Vertices to Make Graphs Irregular; Julien Bensmail, Clara Marcille, Mano Orenga. Origin: Questions introduced in this paper. Setup: For a finite simple graph G without K₂ components, let Pl(G) be the least k admitting ρ:V(G)→{0,…,k} such that σ(v)=d(v)(1+ρ(v))+Σ\_{u∈N(v)}ρ(u) differs across every edge.

**Source.** Julien Bensmail, Clara Marcille and Mano Orenga. *Pushing Vertices to Make Graphs Irregular*. 2025. [primary source](https://dmtcs.episciences.org/16418/pdf) Location: Section 5, p.14.

**Literature check.** Status: Final DMTCS (2025); Δ-conjecture reaffirmed June 2026; recognition questions unresolved in checked sources. https://doi.org/10.61091/ars167-10

**Further links.** [1](https://doctorat.u-bordeaux.fr/soutenances/soutenances-du-24-06-2025) · [2](https://doi.org/10.61091/ars167-10)


<a id="q3772"></a>

## Q3772. Does every graph admit labels in {1,2} such that each subgraph induced by {v:σ(v)=x} is a forest?

**Status:** Open · **Kind:** open problem · **Collection** 38

Does every graph admit labels in {1,2} such that each subgraph induced by {v:σ(v)=x} is a forest?

**Context.** Paper: Some remarks and results on the Standard (2,2)-Conjecture; Olivier Baudon, Julien Bensmail, Lyn Vayssieres. Origin: Restated conjectures and an explicit strengthening question. Setup: Graphs are finite and simple. A proper edge-labelling makes the incident-label sums σ(v) unequal across every edge. Nice means no K₂ component; nicer additionally excludes K₃ components.

**Source.** Olivier Baudon, Julien Bensmail and Lyn Vayssieres. *Some remarks and results on the Standard (2,2)-Conjecture*. 2026. [primary source](https://www.opuscula.agh.edu.pl/vol46/2/art/opuscula_math_4606.pdf) Location: Degenerate 1-2-3 Conjecture, p.130.

**Literature check.** Status: Full final, published April 10, 2026; Strong conjecture also reaffirmed in March 2026 DAM. https://doi.org/10.1016/j.dam.2025.12.011

**Further links.** [1](https://jbensmai.fr/datas/thesis/phd.pdf) · [2](https://doi.org/10.1016/j.dam.2025.12.011)


<a id="q3773"></a>

## Q3773. Does every nice graph admit a proper {1,2,3}-edge-labelling whose edges labelled 3 form a matching?

**Status:** Open · **Kind:** open problem · **Collection** 38

Does every nice graph admit a proper {1,2,3}-edge-labelling whose edges labelled 3 form a matching?

**Context.** Paper: Some remarks and results on the Standard (2,2)-Conjecture; Olivier Baudon, Julien Bensmail, Lyn Vayssieres. Origin: Restated conjectures and an explicit strengthening question. Setup: Graphs are finite and simple. A proper edge-labelling makes the incident-label sums σ(v) unequal across every edge. Nice means no K₂ component; nicer additionally excludes K₃ components.

**Source.** Olivier Baudon, Julien Bensmail and Lyn Vayssieres. *Some remarks and results on the Standard (2,2)-Conjecture*. 2026. [primary source](https://www.opuscula.agh.edu.pl/vol46/2/art/opuscula_math_4606.pdf) Location: After Observation 1.3, p.129.

**Literature check.** Status: Full final, published April 10, 2026; Strong conjecture also reaffirmed in March 2026 DAM. https://doi.org/10.1016/j.dam.2025.12.011

**Further links.** [1](https://jbensmai.fr/datas/thesis/phd.pdf) · [2](https://doi.org/10.1016/j.dam.2025.12.011)


<a id="q3774"></a>

## Q3774. Can every nicer graph receive red or blue edge labels of value 1 or 2 so that adjacent vertices…

**Status:** Open · **Kind:** open problem · **Collection** 38

Can every nicer graph receive red or blue edge labels of value 1 or 2 so that adjacent vertices with positive red sums have different red sums, and likewise for blue sums?

**Context.** Paper: Some remarks and results on the Standard (2,2)-Conjecture; Olivier Baudon, Julien Bensmail, Lyn Vayssieres. Origin: Restated conjectures and an explicit strengthening question. Setup: Graphs are finite and simple. A proper edge-labelling makes the incident-label sums σ(v) unequal across every edge. Nice means no K₂ component; nicer additionally excludes K₃ components.

**Source.** Olivier Baudon, Julien Bensmail and Lyn Vayssieres. *Some remarks and results on the Standard (2,2)-Conjecture*. 2026. [primary source](https://www.opuscula.agh.edu.pl/vol46/2/art/opuscula_math_4606.pdf) Location: Strong (2,2)-Conjecture, p.131.

**Literature check.** Status: Full final, published April 10, 2026; Strong conjecture also reaffirmed in March 2026 DAM. https://doi.org/10.1016/j.dam.2025.12.011

**Further links.** [1](https://jbensmai.fr/datas/thesis/phd.pdf) · [2](https://doi.org/10.1016/j.dam.2025.12.011)


<a id="q3775"></a>

## Q3775. Can every oriented graph have its arcs coloured with three colours so that every arc uv has…

**Status:** Open · **Kind:** conjecture (Conjecture 75) · **Collection** 38

Can every oriented graph have its arcs coloured with three colours so that every arc uv has d⁺(u)≠d⁺(v) in its own colour class?

**Context.** Origin: First restates Bensmail–Renault; second originates jointly with Onderko and Woźniak. Setup: Digraphs are finite and loopless, with at most one arc per ordered pair; opposite arcs are allowed. An oriented graph has no opposite pair. Here d⁺ and d⁻ are outdegree and indegree, measured within each arc-colour class.

**Source.** Igor Grzelec. *Lokalna nieregularność grafów, multigrafów i digrafów*. AGH University of Krakow, 2025. Advisor(s): Mariusz Woźniak. [primary source](https://api.repo.agh.edu.pl/server/api/core/bitstreams/6ee88780-75a1-461f-858a-870bd1712e85/content) Location: Conjecture 75, p.137; paper Conjecture 2, p.4.

**Literature check.** Status: Thesis and https://arxiv.org/abs/2502.07933v1; current version unchanged, no resolution found.

**Further links.** [1](https://arxiv.org/abs/2502.07933v1)


<a id="q3776"></a>

## Q3776. Can every digraph have its arcs coloured with two colours so that every arc uv has…

**Status:** Open · **Kind:** conjecture (Conjecture 95) · **Collection** 38

Can every digraph have its arcs coloured with two colours so that every arc uv has d⁺(u)−d⁻(u)≠d⁺(v)−d⁻(v) in its own colour class?

**Context.** Origin: First restates Bensmail–Renault; second originates jointly with Onderko and Woźniak. Setup: Digraphs are finite and loopless, with at most one arc per ordered pair; opposite arcs are allowed. An oriented graph has no opposite pair. Here d⁺ and d⁻ are outdegree and indegree, measured within each arc-colour class.

**Source.** Igor Grzelec. *Lokalna nieregularność grafów, multigrafów i digrafów*. AGH University of Krakow, 2025. Advisor(s): Mariusz Woźniak. [primary source](https://api.repo.agh.edu.pl/server/api/core/bitstreams/6ee88780-75a1-461f-858a-870bd1712e85/content) Location: Conjecture 95, p.148; paper Conjecture 22, p.15.

**Literature check.** Status: Thesis and https://arxiv.org/abs/2502.07933v1; current version unchanged, no resolution found.

**Further links.** [1](https://arxiv.org/abs/2502.07933v1)


<a id="q3777"></a>

## Q3777. For a uniformly random connected partition Ψ of Gₙ, is E[max_{B∈Ψ}|B|]=Θ(n)?

**Status:** Open · **Kind:** conjecture (Conjecture 4.1.2.1) · **Collection** 38

For a uniformly random connected partition Ψ of Gₙ, is E[max_{B∈Ψ}|B|]=Θ(n)?

**Context.** Origin: Thesis conjecture; counting problem also attributed to Simon–Tittmann–Trinks and Vince. Setup: A connected partition of a finite simple graph is an unordered partition of its vertices into nonempty sets inducing connected subgraphs. The number of blocks is unrestricted. Gₙ is the n×n square grid.

**Source.** Elle Najt. *Connected graph partitions from perspectives of complexity theory, statistical physics and probability theory, with applications to ensemble analysis of political redistricting plans and other statistical models*. University of Wisconsin–Madison, 2021. Advisor(s): Jordan Ellenberg. [primary source](https://asset.library.wisc.edu/1711.dl/L3OLMTH4ESXZN8T/R/file-19c5d.pdf) Location: Conjecture 4.1.2.1, p.82.

**Literature check.** Status: 2021 thesis; bounded current search found no resolution.

**Further links.** [1](https://ifds.info/lorenzo-najt/)


<a id="q3778"></a>

## Q3778. Determine the computational complexity of computing the number of connected partitions of an…

**Status:** Solved here: proved · **Kind:** open problem (Question 4.1.2) · **Collection** 38

Determine the computational complexity of computing the number of connected partitions of an input graph.

**Context.** Origin: Thesis conjecture; counting problem also attributed to Simon–Tittmann–Trinks and Vince. Setup: A connected partition of a finite simple graph is an unordered partition of its vertices into nonempty sets inducing connected subgraphs. The number of blocks is unrestricted. Gₙ is the n×n square grid.

**Source.** Elle Najt. *Connected graph partitions from perspectives of complexity theory, statistical physics and probability theory, with applications to ensemble analysis of political redistricting plans and other statistical models*. University of Wisconsin–Madison, 2021. Advisor(s): Jordan Ellenberg. [primary source](https://asset.library.wisc.edu/1711.dl/L3OLMTH4ESXZN8T/R/file-19c5d.pdf) Location: Question 4.1.2, p.82.

**Literature check.** Status: 2021 thesis; bounded current search found no resolution.

**Results.**

- **Proved**: Exact counting is #P-complete under polynomial-time Turing reductions, already for connected bipartite simple graphs. Subdivisions satisfy C(G^(ℓ)) = P_G(2^ℓ−ℓ−1, 2^ℓ−1) for a two-variable polynomial whose value at (1,0) counts connected spanning edge subsets, a #P-hard Tutte evaluation (Jaeger–Vertigan–Welsh); polynomially many even subdivisions recover it by interpolation. Limits: no parsimonious reduction; approximate counting and sampling are not addressed. Reconstructed checkpoint without its original checkers; re-derived here by hand and spot-checked with independent exact computations on 10 October 2026. Not external peer review or a novelty certification. Filed from the public-repo research round seven-problems-2026-10-10. [Details](../../solutions/seven-problems-2026-10-10/Q3778.md).

**Further links.** [1](https://ifds.info/lorenzo-najt/)


<a id="q3779"></a>

## Q3779. For each fixed t≥3, are graphs of clique-width at most t DOM-bounded?

**Status:** Open · **Kind:** open problem (Problem 2) · **Collection** 38

For each fixed t≥3, are graphs of clique-width at most t DOM-bounded?

**Context.** Paper: A Domatic Analogue of χ-Bounded Graph Classes and the Gyárfás–Sumner Conjecture; Quentin Chuet, Selma Djelloul, Hoang La, François Pirot, Hossein Zaredehabadi. Origin: Explicit paper problems. Setup: Graphs are nonempty, finite and simple. DOM(G) maximizes the number of parts partitioning V(G), each meeting every closed neighbourhood. With δ denoting minimum degree, DOM-bounded means DOM(G)≥f(δ(G)) for a positive unbounded function f on {0,1,…}. Clique-width minimizes labels used for vertex creation, disjoint union, relabelling, and joining distinct label classes.

**Source.** Quentin Chuet, Selma Djelloul, Hoang La, François Pirot and Hossein Zaredehabadi. *A Domatic Analogue of χ-Bounded Graph Classes and the Gyárfás–Sumner Conjecture*. 2026. [primary source](https://arxiv.org/pdf/2606.02030v1) Location: Problem 2, p.19.

**Literature check.** Status: Current v1 checked October 9, 2026; no later resolution found.

**Further links.** [1](https://www.lisn.upsaclay.fr/evenements/variations-sur-le-probleme-de-coloration-de-graphes/?lang=en)


<a id="q3780"></a>

## Q3780. For n≥5, determine the least q(n) such that every n-vertex G with FDOM(G)≥5/2 has a dominating…

**Status:** Open · **Kind:** open problem (Problem 1) · **Collection** 38

For n≥5, determine the least q(n) such that every n-vertex G with FDOM(G)≥5/2 has a dominating (5q(n):2q(n))-colouring.

**Context.** Paper: Fractional domatic number and minimum degree; Quentin Chuet, Hugo Demaret, Hoang La, François Pirot. Origin: Explicit paper problems. Setup: For nonempty finite simple G, let δ be minimum degree and girth be shortest-cycle length. For positive integers p,q, a dominating (p:q)-colouring assigns every vertex a q-subset of [p]={1,…,p}, whose union on every closed neighbourhood is [p]. FDOM(G) is the supremum of p/q. Put F(g)=inf{FDOM(G):δ(G)=2, girth(G)≥g}.

**Source.** Quentin Chuet, Hugo Demaret, Hoang La and François Pirot. *Fractional domatic number and minimum degree*. 2025. [primary source](https://arxiv.org/pdf/2508.19617v1) Location: Problem 1, p.31.

**Literature check.** Status: Current v1 checked October 9, 2026; no later resolution found.

**Further links.** [1](https://www.lisn.upsaclay.fr/evenements/variations-sur-le-probleme-de-coloration-de-graphes/?lang=en)


<a id="q3781"></a>

## Q3781. Determine lim_{g→∞}F(g).

**Status:** Open · **Kind:** open problem (Problem 5) · **Collection** 38

Determine lim_{g→∞}F(g).

**Context.** Paper: Fractional domatic number and minimum degree; Quentin Chuet, Hugo Demaret, Hoang La, François Pirot. Origin: Explicit paper problems. Setup: For nonempty finite simple G, let δ be minimum degree and girth be shortest-cycle length. For positive integers p,q, a dominating (p:q)-colouring assigns every vertex a q-subset of [p]={1,…,p}, whose union on every closed neighbourhood is [p]. FDOM(G) is the supremum of p/q. Put F(g)=inf{FDOM(G):δ(G)=2, girth(G)≥g}.

**Source.** Quentin Chuet, Hugo Demaret, Hoang La and François Pirot. *Fractional domatic number and minimum degree*. 2025. [primary source](https://arxiv.org/pdf/2508.19617v1) Location: Problem 5, p.32.

**Literature check.** Status: Current v1 checked October 9, 2026; no later resolution found.

**Further links.** [1](https://www.lisn.upsaclay.fr/evenements/variations-sur-le-probleme-de-coloration-de-graphes/?lang=en)


<a id="q3786"></a>

## Q3786. For every connected G as above, must maxOne(G)≥⌈|E(G)|/2⌉−1?

**Status:** Open · **Kind:** conjecture (Conjecture 10) · **Collection** 38

For every connected G as above, must maxOne(G)≥⌈|E(G)|/2⌉−1?

**Context.** Paper: Maximising 1’s through Proper Labellings; Julien Bensmail. Origin: Conjecture and algorithmic question originate in this paper. Setup: For a finite simple graph G without K₂ components, a proper labelling assigns positive integers to edges so that adjacent vertices have different incident-label sums. Let maxOne(G) be the largest number of edges labelled 1 in any such labelling; the other labels are unrestricted.

**Source.** Julien Bensmail. *Maximising 1’s through Proper Labellings*. 2025. [primary source](https://bibliotekanauki.pl/articles/59945820.pdf) Location: Conjecture 10, p.363.

**Literature check.** Status: Final Discuss. Math. Graph Theory 45 (2025), 351–376; no later resolution located.

**Further links.** [1](https://jbensmai.fr/datas/thesis/phd.pdf)


<a id="q3787"></a>

## Q3787. Determine the computational complexity of computing maxOne(G) from G.

**Status:** Open · **Kind:** open problem · **Collection** 38

Determine the computational complexity of computing maxOne(G) from G.

**Context.** Paper: Maximising 1’s through Proper Labellings; Julien Bensmail. Origin: Conjecture and algorithmic question originate in this paper. Setup: For a finite simple graph G without K₂ components, a proper labelling assigns positive integers to edges so that adjacent vertices have different incident-label sums. Let maxOne(G) be the largest number of edges labelled 1 in any such labelling; the other labels are unrestricted.

**Source.** Julien Bensmail. *Maximising 1’s through Proper Labellings*. 2025. [primary source](https://bibliotekanauki.pl/articles/59945820.pdf) Location: Section 6, pp.374–375.

**Literature check.** Status: Final Discuss. Math. Graph Theory 45 (2025), 351–376; no later resolution located.

**Further links.** [1](https://jbensmai.fr/datas/thesis/phd.pdf)


<a id="q3825"></a>

## Q3825. Three-row character sums

**Status:** Open · **Kind:** conjecture (Conjecture 6) · **Collection** 39

Is A_1(λ)=B_1(λ) for every partition λ?

**Context.** Paper: David J. Hemmer, Armin Straub, Karlee J. Westrem, New Identities in the Character Table of Symmetric Groups involving Riordan Numbers, EJC 33(1), P1.57 (2026). For λ⊢n, Ev(λ) is the multiset from independently replacing each part a by 2a or (a,a). Write ℓ for length, μ′ for conjugation, χ^μ\_ρ for the irreducible S_{2n}-character indexed by μ at cycle type ρ, z_λ=∏\_j j^{m_j}m_j! with m_j the multiplicity of j, and g_λ(q)=∏\_i q^{λ\_i}/(1+q^{λ\_i}). Define A_N(λ)=Σ\_{ρ∈Ev(λ)}Σ\_{μ⊢2n,ℓ(μ)≤2N+1,all μ\_i even}(−1)^{ℓ(ρ)}χ^μ\_ρ, B_N(λ)=Σ\_{ρ∈Ev(λ)}Σ\_{μ⊢2n,ℓ(μ)≤2N,all μ′\_i even}χ^μ\_ρ. Origin/locators: Joint-paper Conjecture 6, p.4; Amdeberhan’s Conjecture 18, p.16. Inspected EJC final and later knapsack final. Unrestricted unweighted identities are false; these residual targets remain unresolved in bounded 10 October 2026 searches.

**Source.** David J. Hemmer, Armin Straub and Karlee J. Westrem. *New Identities in the Character Table of Symmetric Groups involving Riordan Numbers*. 2026. [primary source](https://doi.org/10.37236/14401) Location: Joint-paper Conjecture 6, p.4; Amdeberhan’s Conjecture 18, p.16.

**Literature check.** Status: Origin/locators: Joint-paper Conjecture 6, p.4; Amdeberhan’s Conjecture 18, p.16. Inspected EJC final and later knapsack final. Unrestricted unweighted identities are false; these residual targets remain unresolved in bounded 10 October 2026 searches.

**Further links.** [1](https://digitalcommons.mtu.edu/etdr/1892/) · [2](https://pages.mtu.edu/~djhemmer/papers/equalknapsackidentities.pdf)


<a id="q3826"></a>

## Q3826. Weighted character-sum series

**Status:** Open · **Kind:** conjecture (Conjecture 6) · **Collection** 39

For every N≥1, does Σ\_{n≥0}Σ\_{λ⊢n}g_λ(q)A_N(λ)/z_λ=Σ\_{n≥0}Σ\_{λ⊢n}g_λ(q)B_N(λ)/z_λ hold as formal power series?

**Context.** Paper: David J. Hemmer, Armin Straub, Karlee J. Westrem, New Identities in the Character Table of Symmetric Groups involving Riordan Numbers, EJC 33(1), P1.57 (2026). For λ⊢n, Ev(λ) is the multiset from independently replacing each part a by 2a or (a,a). Write ℓ for length, μ′ for conjugation, χ^μ\_ρ for the irreducible S_{2n}-character indexed by μ at cycle type ρ, z_λ=∏\_j j^{m_j}m_j! with m_j the multiplicity of j, and g_λ(q)=∏\_i q^{λ\_i}/(1+q^{λ\_i}). Define A_N(λ)=Σ\_{ρ∈Ev(λ)}Σ\_{μ⊢2n,ℓ(μ)≤2N+1,all μ\_i even}(−1)^{ℓ(ρ)}χ^μ\_ρ, B_N(λ)=Σ\_{ρ∈Ev(λ)}Σ\_{μ⊢2n,ℓ(μ)≤2N,all μ′\_i even}χ^μ\_ρ. Origin/locators: Joint-paper Conjecture 6, p.4; Amdeberhan’s Conjecture 18, p.16. Inspected EJC final and later knapsack final. Unrestricted unweighted identities are false; these residual targets remain unresolved in bounded 10 October 2026 searches.

**Source.** David J. Hemmer, Armin Straub and Karlee J. Westrem. *New Identities in the Character Table of Symmetric Groups involving Riordan Numbers*. 2026. [primary source](https://doi.org/10.37236/14401) Location: Joint-paper Conjecture 6, p.4; Amdeberhan’s Conjecture 18, p.16.

**Literature check.** Status: Origin/locators: Joint-paper Conjecture 6, p.4; Amdeberhan’s Conjecture 18, p.16. Inspected EJC final and later knapsack final. Unrestricted unweighted identities are false; these residual targets remain unresolved in bounded 10 October 2026 searches.

**Further links.** [1](https://digitalcommons.mtu.edu/etdr/1892/) · [2](https://pages.mtu.edu/~djhemmer/papers/equalknapsackidentities.pdf)


<a id="q3827"></a>

## Q3827. One-orbit partition growth

**Status:** Open · **Kind:** open problem · **Collection** 39

Determine the asymptotic growth of a(n) as n→∞.

**Context.** Paper: Billiard Orbits in Young Diagrams: Medial Links, Bicycle Spaces, and Domino Tilings, arXiv:2609.16533v1, 15 September 2026. For a nonempty partition λ, remove its Young diagram’s first row and column to obtain λ□. Its cell-adjacency graph joins side-sharing cells. With adjacency matrix A, put σ(λ)=1+nullity_{F₂}A(λ□), assigning empty-matrix nullity zero. This equals the number of diagonal billiard orbits. Define a(n)=#{λ⊢n:σ(λ)=1}. Origin/locators: Post-doctoral paper Problems 7.1,7.3, pp.23–24, found through Westrem’s advisor. Inspected v1; doctoral metadata from official CV, thesis unread. No later version or resolution found in bounded 10 October 2026 searches.

**Source.** David J. Hemmer. *Billiard Orbits in Young Diagrams: Medial Links, Bicycle Spaces, and Domino Tilings*. 2026. [primary source](https://arxiv.org/abs/2609.16533v1) Location: Post-doctoral paper Problems 7.1,7.3, pp.23–24, found through Westrem’s advisor.

**Literature check.** Status: Origin/locators: Post-doctoral paper Problems 7.1,7.3, pp.23–24, found through Westrem’s advisor. Inspected v1; doctoral metadata from official CV, thesis unread. No later version or resolution found in bounded 10 October 2026 searches.

**Further links.** [1](https://www.math.buffalo.edu/~dhemmer/CVFebruary2016.pdf)


<a id="q3828"></a>

## Q3828. Fat-hook billiard counts

**Status:** Open · **Kind:** open problem · **Collection** 39

Find an explicit formula in a,b,m,n for σ((a^m,b^n)) when a>b≥1 and m,n≥1 are integers.

**Context.** Paper: Billiard Orbits in Young Diagrams: Medial Links, Bicycle Spaces, and Domino Tilings, arXiv:2609.16533v1, 15 September 2026. For a nonempty partition λ, remove its Young diagram’s first row and column to obtain λ□. Its cell-adjacency graph joins side-sharing cells. With adjacency matrix A, put σ(λ)=1+nullity_{F₂}A(λ□), assigning empty-matrix nullity zero. This equals the number of diagonal billiard orbits. Define a(n)=#{λ⊢n:σ(λ)=1}. Origin/locators: Post-doctoral paper Problems 7.1,7.3, pp.23–24, found through Westrem’s advisor. Inspected v1; doctoral metadata from official CV, thesis unread. No later version or resolution found in bounded 10 October 2026 searches.

**Source.** David J. Hemmer. *Billiard Orbits in Young Diagrams: Medial Links, Bicycle Spaces, and Domino Tilings*. 2026. [primary source](https://arxiv.org/abs/2609.16533v1) Location: Post-doctoral paper Problems 7.1,7.3, pp.23–24, found through Westrem’s advisor.

**Literature check.** Status: Origin/locators: Post-doctoral paper Problems 7.1,7.3, pp.23–24, found through Westrem’s advisor. Inspected v1; doctoral metadata from official CV, thesis unread. No later version or resolution found in bounded 10 October 2026 searches.

**Further links.** [1](https://www.math.buffalo.edu/~dhemmer/CVFebruary2016.pdf)


<a id="q3829"></a>

## Q3829. Fixed points in random cycle-factors

**Status:** Open · **Kind:** open problem (Problem 4.2) · **Collection** 39

Is there a universal constant C with E[F]≤Cn/d for every such D?

**Context.** Paper authors: Micha Christoph, Nemanja Draganić, António Girão, Eoin Hurley, Lukas Michel, Alp Müyesser. Cycle-factors of regular graphs via entropy. Let D be an n-vertex digraph allowing loops and opposite arcs, without parallel arcs, with every indegree and outdegree d≥1. Choose uniformly a permutation σ of V(D) satisfying v→σ(v)∈E(D). Define F=|{v:σ(v)=v}|.

**Source.** Micha Christoph, Nemanja Draganić, António Girão, Eoin Hurley, Lukas Michel and Alp Müyesser. *Cycle-factors of regular graphs via entropy*. 2025. [primary source](https://arxiv.org/abs/2507.19417v3) Location: Joint-paper Problem 4.2, p.9.

**Literature check.** Status: Origin/locator: Joint-paper Problem 4.2, p.9. Inspected arXiv:2507.19417v3, 29 September 2026, which retains this target after acknowledging disproof of a different extremal cycle-count conjecture. No later resolution located in bounded 10 October 2026 searches. Thesis metadata verified; thesis full text inaccessible during this audit.

**Further links.** [1](https://doi.org/10.5287/ora-yqryd5jv2) · [2](https://people.math.ethz.ch/~lukmichel/)


<a id="q3839"></a>

## Q3839. For every n≥2 and every n-vertex tree T, does every zero z of Φ\_T satisfy…

**Status:** Open · **Kind:** conjecture (Conjecture 5.1) · **Collection** 39

For every n≥2 and every n-vertex tree T, does every zero z of Φ\_T satisfy 1/2≤|z+1/2|≤1/2+(n−1)^{1/(n−1)}?

**Context.** Doctoral route: Ruoyu Wang, Subtrees in Graphs: Statistics, Extrema and Asymptotics, Uppsala University doctoral dissertation, 2026; supervisor Stephan Wagner. Its scheduled defense was 27 August; degree conferral was not independently established. Origin: Jason I. Brown and Lucas Mol, On the roots of the subtree polynomial, Conjecture 4.2 (2018 preprint; 2020 article). Setup: For a finite tree T, put Φ\_T(z)=Σ\_S z^{|S|}, over nonempty vertex subsets inducing connected subgraphs.

**Source.** Xian’an Jin, Tianlong Ma and Yi Wang. *Proof of a Brown-Mol conjecture on subtree roots*. 2026. [primary source](https://arxiv.org/abs/2608.07898v2) Location: Xian’an Jin, Tianlong Ma and Yi Wang, Proof of a Brown-Mol conjecture on subtree roots, arXiv:2608.07898v2 (14 August 2026), Conjecture 5.1, p.16.

**Literature check.** Status: Current primary source: Xian’an Jin, Tianlong Ma and Yi Wang, Proof of a Brown-Mol conjecture on subtree roots, arXiv:2608.07898v2 (14 August 2026), Conjecture 5.1, p.16. The proved disk bound does not settle this translated annulus. No matching resolution located through 10 October 2026.

**Further links.** [1](https://diva-portal.org/smash/get/diva2%3A2058439/FULLTEXT01.pdf) · [2](https://arxiv.org/abs/1810.08655v1)


<a id="q3840"></a>

## Q3840. Which integer pairs n≥5 odd, m≥6, m≢3 (mod 4) make C_n□P_m admit such a set?

**Status:** Open, partial results · **Kind:** open problem (Problem 2.8) · **Collection** 39

Which integer pairs n≥5 odd, m≥6, m≢3 (mod 4) make C_n□P_m admit such a set?

**Context.** Doctoral context: Sawyer Isaac Osborn, From Total Domination to Graph Coloring, Western Michigan University, PhD, June 2026; primary advisor Ping Zhang, listed first in the institutional record. Full thesis text was not inspected. Paper formulation: Sawyer Osborn and Ping Zhang, From princes on chessboards to proper total domination in graphs, Journal of Combinatorial Mathematics and Combinatorial Computing 129 (2026), 33–48; final version, published 27 January. Its acknowledgments credit Gary Chartrand with suggesting concepts and problems. Setup: In a finite simple graph, S⊆V is proper total dominating if σ\_S(v)=|N(v)∩S|≥1 at every vertex and σ\_S(u)≠σ\_S(v) whenever uv is an edge. P_m is the m-vertex path, C_n the n-cycle, and □ the Cartesian product.

**Source.** Sawyer Osborn and Ping Zhang. *From princes on chessboards to proper total domination in graphs*. 2026. [primary source](https://doi.org/10.61091/jcmcc129-03) Location: Problem 2.8, p.39.

**Literature check.** Status: No matching resolution located through 10 October 2026.

**Literature check.** Research update, 10 October 2026: proved partial classification recorded in seven-selected-2026-10-10. The full classification at all odd circumferences n>=7 remains unresolved. Exact exhaustive certificates prove the finitely many negative cases; nonexistence is not asserted to pull back to graph covers.

**Further links.** [1](https://scholarworks.wmich.edu/dissertations/4275/)

**Result (2026-10-10).** C_5 square P_m has a proper total dominating set exactly for m in {3,5,7} or m>=9. In the catalog's requested range, the circumference-five failures are precisely m=6 and m=8. Explicit two-row insertions prove the infinite positive families, and covering pullbacks supply positive families for every odd circumference divisible by five. The full classification at all odd circumferences n>=7 remains unresolved. Exact exhaustive certificates prove the finitely many negative cases; nonexistence is not asserted to pull back to graph covers.

[Proof](../../solutions/seven-selected-2026-10-10/discrete/Q3840.md) · [Internal review](../../solutions/seven-selected-2026-10-10/probability/review-Q3840-Q3841.md) · [Computational controls](../../solutions/seven-selected-2026-10-10/discrete/verification.json) · [Source check](../../solutions/seven-selected-2026-10-10/discrete/sources.md). Separate internal AI review found no blocking defect; not external peer review, formal certification, or a novelty certification.



<a id="q3841"></a>

## Q3841. Which odd integers n,m≥5 make C_n□C_m admit such a set?

**Status:** Open, partial results · **Kind:** open problem · **Collection** 39

Which odd integers n,m≥5 make C_n□C_m admit such a set?

**Context.** Doctoral context: Sawyer Isaac Osborn, From Total Domination to Graph Coloring, Western Michigan University, PhD, June 2026; primary advisor Ping Zhang, listed first in the institutional record. Full thesis text was not inspected. Paper formulation: Sawyer Osborn and Ping Zhang, From princes on chessboards to proper total domination in graphs, Journal of Combinatorial Mathematics and Combinatorial Computing 129 (2026), 33–48; final version, published 27 January. Its acknowledgments credit Gary Chartrand with suggesting concepts and problems. Setup: In a finite simple graph, S⊆V is proper total dominating if σ\_S(v)=|N(v)∩S|≥1 at every vertex and σ\_S(u)≠σ\_S(v) whenever uv is an edge. P_m is the m-vertex path, C_n the n-cycle, and □ the Cartesian product.

**Source.** Sawyer Osborn and Ping Zhang. *From princes on chessboards to proper total domination in graphs*. 2026. [primary source](https://doi.org/10.61091/jcmcc129-03) Location: §4(II), p.46.

**Literature check.** Status: No matching resolution located through 10 October 2026.

**Literature check.** Research update, 10 October 2026: proved partial classification recorded in seven-selected-2026-10-10. The full classification when both odd circumferences are at least seven remains unresolved. The covering argument is sufficient for existence and makes no assertion that nonexistence persists under covers.

**Further links.** [1](https://scholarworks.wmich.edu/dissertations/4275/)

**Result (2026-10-10).** For odd m>=5, C_5 square C_m has a proper total dominating set if and only if m>=7. An exact exhaustive certificate excludes C_5 square C_5; explicit seeds and two-row insertions cover all positive lengths. Covering pullbacks extend the positive families to odd circumferences divisible by five. The full classification when both odd circumferences are at least seven remains unresolved. The covering argument is sufficient for existence and makes no assertion that nonexistence persists under covers.

[Proof](../../solutions/seven-selected-2026-10-10/discrete/Q3841.md) · [Internal review](../../solutions/seven-selected-2026-10-10/probability/review-Q3840-Q3841.md) · [Computational controls](../../solutions/seven-selected-2026-10-10/discrete/verification.json) · [Source check](../../solutions/seven-selected-2026-10-10/discrete/sources.md). Separate internal AI review found no blocking defect; not external peer review, formal certification, or a novelty certification.



<a id="q3842"></a>

## Q3842. Is m_{S_n}(3,0)=2(4n+1)!/((3n+2)!(n+1)!)?

**Status:** Open · **Kind:** open problem · **Collection** 39

Is m_{S_n}(3,0)=2(4n+1)!/((3n+2)!(n+1)!)?

**Context.** Doctoral context: John Lentfer, Combinatorics of Bosonic-Fermionic Coinvariant Rings, University of California, Berkeley, PhD 2026; advisors Mark D. Haiman and Sylvie Corteel. Setup: For G=S_n or B_n, where B_n is the signed-permutation group, let A=Sym((C^n)^⊕k)⊗Λ((C^n)^⊕j), with G acting identically on every variable set by its natural representation. Here Sym denotes polynomial algebra and Λ exterior algebra. Put R_G^{(k,j)}=A/⟨A^G_+⟩, where A^G_+ consists of invariants without constant term. Let m_G(k,j) be the ungraded determinant-character multiplicity. Define F_0=0,F_1=1,F_r=F_{r−1}+F_{r−2} for r≥2. For all integers n≥1:

**Source.** John Lentfer. *Combinatorics of Bosonic-Fermionic Coinvariant Rings*. University of California, Berkeley, 2026. Advisor(s): Mark D. Haiman and Sylvie Corteel. [primary source](https://escholarship.org/uc/item/2612s2ds) Location: Haiman’s conjecture; thesis 7.2.1, p.125.

**Literature check.** Status: August tables retain all four; September’s (2,1) theorem differs. No resolution located through 10 October 2026.

**Further links.** [1](https://doi.org/10.5802/alco.424) · [2](https://doi.org/10.37236/13818) · [3](https://arxiv.org/abs/2608.02881v1) · [4](https://arxiv.org/abs/2609.23297v1)


<a id="q3843"></a>

## Q3843. Is m_{S_n}(1,3)=F_{3n}/2?

**Status:** Open · **Kind:** conjecture (Conjecture 30) · **Collection** 39

Is m_{S_n}(1,3)=F_{3n}/2?

**Context.** Doctoral context: John Lentfer, Combinatorics of Bosonic-Fermionic Coinvariant Rings, University of California, Berkeley, PhD 2026; advisors Mark D. Haiman and Sylvie Corteel. Setup: For G=S_n or B_n, where B_n is the signed-permutation group, let A=Sym((C^n)^⊕k)⊗Λ((C^n)^⊕j), with G acting identically on every variable set by its natural representation. Here Sym denotes polynomial algebra and Λ exterior algebra. Put R_G^{(k,j)}=A/⟨A^G_+⟩, where A^G_+ consists of invariants without constant term. Let m_G(k,j) be the ungraded determinant-character multiplicity. Define F_0=0,F_1=1,F_r=F_{r−1}+F_{r−2} for r≥2. For all integers n≥1:

**Source.** John Lentfer. *Combinatorics of Bosonic-Fermionic Coinvariant Rings*. University of California, Berkeley, 2026. Advisor(s): Mark D. Haiman and Sylvie Corteel. [primary source](https://escholarship.org/uc/item/2612s2ds) Location: François Bergeron’s conjecture; thesis 4.8.7, p.83; Lentfer’s The Sign Character of the Triagonal Fermionic Coinvariant Ring, EJC 33(2), P2.3 (2026), Conjecture 30, p.20.

**Literature check.** Status: August tables retain all four; September’s (2,1) theorem differs. No resolution located through 10 October 2026.

**Further links.** [1](https://doi.org/10.5802/alco.424) · [2](https://doi.org/10.37236/13818) · [3](https://arxiv.org/abs/2608.02881v1) · [4](https://arxiv.org/abs/2609.23297v1)


<a id="q3844"></a>

## Q3844. Is dim R_{B_n}^{(1,2)}=4^n n!?

**Status:** Open · **Kind:** conjecture (Conjecture 9.8) · **Collection** 39

Is dim R_{B_n}^{(1,2)}=4^n n!?

**Context.** Doctoral context: John Lentfer, Combinatorics of Bosonic-Fermionic Coinvariant Rings, University of California, Berkeley, PhD 2026; advisors Mark D. Haiman and Sylvie Corteel. Setup: For G=S_n or B_n, where B_n is the signed-permutation group, let A=Sym((C^n)^⊕k)⊗Λ((C^n)^⊕j), with G acting identically on every variable set by its natural representation. Here Sym denotes polynomial algebra and Λ exterior algebra. Put R_G^{(k,j)}=A/⟨A^G_+⟩, where A^G_+ consists of invariants without constant term. Let m_G(k,j) be the ungraded determinant-character multiplicity. Define F_0=0,F_1=1,F_r=F_{r−1}+F_{r−2} for r≥2. For all integers n≥1:

**Source.** John Lentfer. *Combinatorics of Bosonic-Fermionic Coinvariant Rings*. University of California, Berkeley, 2026. Advisor(s): Mark D. Haiman and Sylvie Corteel. [primary source](https://escholarship.org/uc/item/2612s2ds) Location: Lentfer’s conjecture; thesis 3.9.8, p.54; A conjectural basis for the (1,2)-bosonic-fermionic coinvariant ring, Algebraic Combinatorics 8(3) (2025), Conjecture 9.8, p.736.

**Literature check.** Status: August tables retain all four; September’s (2,1) theorem differs. No resolution located through 10 October 2026.

**Further links.** [1](https://doi.org/10.5802/alco.424) · [2](https://doi.org/10.37236/13818) · [3](https://arxiv.org/abs/2608.02881v1) · [4](https://arxiv.org/abs/2609.23297v1)


<a id="q3845"></a>

## Q3845. Is m_{B_n}(1,3)=F_{3(n+1)}/2?

**Status:** Open · **Kind:** open problem · **Collection** 39

Is m_{B_n}(1,3)=F_{3(n+1)}/2?

**Context.** Doctoral context: John Lentfer, Combinatorics of Bosonic-Fermionic Coinvariant Rings, University of California, Berkeley, PhD 2026; advisors Mark D. Haiman and Sylvie Corteel. Setup: For G=S_n or B_n, where B_n is the signed-permutation group, let A=Sym((C^n)^⊕k)⊗Λ((C^n)^⊕j), with G acting identically on every variable set by its natural representation. Here Sym denotes polynomial algebra and Λ exterior algebra. Put R_G^{(k,j)}=A/⟨A^G_+⟩, where A^G_+ consists of invariants without constant term. Let m_G(k,j) be the ungraded determinant-character multiplicity. Define F_0=0,F_1=1,F_r=F_{r−1}+F_{r−2} for r≥2. For all integers n≥1:

**Source.** John Lentfer. *Combinatorics of Bosonic-Fermionic Coinvariant Rings*. University of California, Berkeley, 2026. Advisor(s): Mark D. Haiman and Sylvie Corteel. [primary source](https://escholarship.org/uc/item/2612s2ds) Location: Yuhan Jiang–John Lentfer, Type B fermionic coinvariant rings, arXiv:2608.02881v1, Table 4, p.4; paper-origin conjecture.

**Literature check.** Status: August tables retain all four; September’s (2,1) theorem differs. No resolution located through 10 October 2026.

**Further links.** [1](https://doi.org/10.5802/alco.424) · [2](https://doi.org/10.37236/13818) · [3](https://arxiv.org/abs/2608.02881v1) · [4](https://arxiv.org/abs/2609.23297v1)


<a id="q3846"></a>

## Q3846. Does every finite minor of (T(n,k))\_{n,k≥0} have nonnegative coefficients in a,c,d,e?

**Status:** Open, partial results · **Kind:** conjecture (Conjecture 1.3) · **Collection** 39

Does every finite minor of (T(n,k))\_{n,k≥0} have nonnegative coefficients in a,c,d,e?

**Context.** Doctoral route: Yufei Zhang, Some Combinatorial Problems Involving Total Non-Negativity and Unimodality, University of Notre Dame, PhD dissertation, April 2025; research director David Galvin. Thesis Conjecture 3.3.1, p.37, restates the weaker assertion for nonnegative numerical parameters. Paper origin: Xi Chen, Bishal Deb, Alexander Dyachenko, Tomack Gilmore and Alan D. Sokal, Coefficientwise Total Positivity of Some Matrices Defined by Linear Recurrences, Séminaire Lotharingien de Combinatoire 85B.30 (2021), Conjecture 1.3, p.3; publisher final dated 29 April 2021. Setup: Let a,c,d,e be independent indeterminates. Set T(0,k)=δ\_{k0}, T(n,k)=0 outside 0≤k≤n, and for n≥1, T(n,k)=[a(n−k)+c]T(n−1,k−1)+(dk+e)T(n−1,k).

**Source.** Xi Chen, Bishal Deb, Alexander Dyachenko, Tomack Gilmore and Alan D. Sokal. *Coefficientwise Total Positivity of Some Matrices Defined by Linear Recurrences*. 2021. [primary source](https://www.mat.univie.ac.at/~slc/wpapers/FPSAC2021/30Chen.pdf) Location: Conjecture 1.3, p.3; publisher final dated 29 April 2021.

**Literature check.** Status: No full resolution located through 10 October 2026. Mao’s August order-three result concerns numerical Eulerian triangles, not all coefficientwise minors here.

**Results.**

- **Partial result**: Every minor using only columns zero and one of the source four-parameter generalized Eulerian triangle has nonnegative coefficients in a,c,d,e, for arbitrary row gaps. The displayed formula proves this without polynomial division. Higher columns and arbitrary-order minors remain unresolved. The negative forced production entry is not a negative actual triangle minor. Internally reviewed at this scope; no novelty or external peer-review claim. [Details](../../solutions/b3-all-targets-2026-10-13/matrices/Q3846-ATTEMPTS.md#a5).
- **Partial result** (B3-ALL-TARGETS-Q3846-TWO-COLUMNS: Coefficientwise total positivity in the first two Eulerian columns): Every minor using only columns zero and one of the source four-parameter generalized Eulerian triangle has nonnegative coefficients in a,c,d,e, for arbitrary row gaps. The displayed formula proves this without polynomial division. Remaining/limits: Higher columns and arbitrary-order minors remain unresolved. The negative forced production entry is not a negative actual triangle minor. [Report](../../solutions/b3-all-targets-2026-10-13/matrices/Q3846-ATTEMPTS.md#a5).
- **Investigated, unresolved** (B3-ALL-TARGETS-STOP-REGISTER: Reviewed B3 failed routes and per-target stopping decisions): 45 targets have each reached five consecutive substantive distinct full-target failures. STATUS.json records every accepted route, written analysis, evidence path and review provenance. Partial results do not reset counters. Rejected proposed attempts, source-range replays, service errors and shared mechanisms remain explicit rather than supplying extra counts. Remaining/limits: These questions remain mathematically unresolved. A failure-limit stop is an operational disposition, not a counterexample or proof. Missing historical archives remain separate evidence issues. [Report](../../solutions/b3-all-targets-2026-10-13/STATUS.json).

**Further links.** [1](https://curate.nd.edu/articles/thesis/28786115) · [2](https://arxiv.org/abs/2608.29224v1)


<a id="q3847"></a>

## Q3847. If the underlying graph is three-edge-connected, are there at most F_{n+2}+1 paths?

**Status:** Open · **Kind:** conjecture (Conjecture 1.3) · **Collection** 39

If the underlying graph is three-edge-connected, are there at most F_{n+2}+1 paths?

**Context.** Doctoral route: Zhenyang Zhang, Combinatorial and Machine Learning Problems Motivated by the Simplex Method, University of California, Davis, PhD 2022; advisor Jesús A. De Loera. Thesis Conjecture 2.3.6, p.41, concerns linearly oriented simple three-dimensional polytopes; Q3847 extends that scope. Paper origin: François Clément and Dan Guyer, Monotone Paths on Acyclic 3-Regular Graphs, arXiv:2508.02108v1 (4 August 2025). Setup: Let D be a finite simple acyclic digraph on 2n vertices, n≥2, with unique source and sink and cubic underlying undirected graph. Count directed source-to-sink paths. Define F_0=0,F_1=1,F_r=F_{r−1}+F_{r−2} for r≥2.

**Source.** François Clément and Dan Guyer. *Monotone Paths on Acyclic 3-Regular Graphs*. 2025. [primary source](https://arxiv.org/abs/2508.02108v1) Location: Conjecture 1.3, p.2.

**Literature check.** Status: The sole posted version and author’s preprint listing were checked; no matching resolution located through 10 October 2026.

**Further links.** [1](https://escholarship.org/content/qt2nd082p3/qt2nd082p3.pdf)


<a id="q3848"></a>

## Q3848. If the underlying graph is two-vertex-connected, are there at most 3^{n/2}+1 paths?

**Status:** Open · **Kind:** conjecture (Conjecture 3.13) · **Collection** 39

If the underlying graph is two-vertex-connected, are there at most 3^{n/2}+1 paths?

**Context.** Doctoral route: Zhenyang Zhang, Combinatorial and Machine Learning Problems Motivated by the Simplex Method, University of California, Davis, PhD 2022; advisor Jesús A. De Loera. Thesis Conjecture 2.3.6, p.41, concerns linearly oriented simple three-dimensional polytopes; Q3847 extends that scope. Paper origin: François Clément and Dan Guyer, Monotone Paths on Acyclic 3-Regular Graphs, arXiv:2508.02108v1 (4 August 2025). Setup: Let D be a finite simple acyclic digraph on 2n vertices, n≥2, with unique source and sink and cubic underlying undirected graph. Count directed source-to-sink paths. Define F_0=0,F_1=1,F_r=F_{r−1}+F_{r−2} for r≥2.

**Source.** François Clément and Dan Guyer. *Monotone Paths on Acyclic 3-Regular Graphs*. 2025. [primary source](https://arxiv.org/abs/2508.02108v1) Location: Conjecture 3.13, p.14.

**Literature check.** Status: The sole posted version and author’s preprint listing were checked; no matching resolution located through 10 October 2026.

**Notes.** Two-vertex- and two-edge-connectivity coincide here.

**Further links.** [1](https://escholarship.org/content/qt2nd082p3/qt2nd082p3.pdf)


<a id="q3859"></a>

## Q3859. If η refines α by splitting its parts, must every α-accepted tableau of weight λ also be η-accepted?

**Status:** Open · **Kind:** conjecture (Conjecture 4.2.10) · **Collection** 39

If η refines α by splitting its parts, must every α-accepted tableau of weight λ also be η-accepted?

**Context.** Doctoral source: Mitsuki Hanada, Catabolism and tableau combinatorics of generalized coinvariant rings, UC Berkeley PhD, May 2026; co-advisors Mark Haiman and Sylvie Corteel. Conjecture 4.2.10(a), p.29, continues Li-Chung Chen’s 2010 thesis Conjecture 5.2.3(1). Setup: Use French semistandard tableaux: rows weakly increase rightward and columns strictly increase upward. Fix partition weight λ, with ℓ positive parts. For h≥0, h-catabolism is permitted when every occurrence of each of the h smallest letters lies in its corresponding bottom row. Delete these letters, leaving a skew tableau; split it after the original bottom h rows into south V and north U. Replace it by the Schensted insertion tableau of rw(V)rw(U), where rw reads rows left-to-right, top-to-bottom, and renumber remaining letters consecutively. The case h=0 is the identity. A composition α of ℓ, allowing zero parts, accepts T when applying these operations successively with its parts is permitted and ends empty.

**Source.** Mitsuki Hanada. *Catabolism and tableau combinatorics of generalized coinvariant rings*. University of California, Berkeley, 2026. Advisor(s): Mark Haiman and Sylvie Corteel. [primary source](https://escholarship.org/uc/item/99r1g2sm) Location: Conjecture 4.2.10(a), p.29, continues Li-Chung Chen’s 2010 thesis Conjecture 5.2.3(1).

**Literature check.** Status: No resolution found through 10 October 2026; September’s higher-Specht results address different questions.

**Further links.** [1](https://escholarship.org/uc/item/6dc2n1tj) · [2](https://arxiv.org/abs/2609.12255)


<a id="q3898"></a>

## Q3898. Is there an absolute constant c such that every arrangement’s crossings admit at most m(A)+c…

**Status:** Open · **Kind:** open problem · **Collection** 39

Is there an absolute constant c such that every arrangement’s crossings admit at most m(A)+c colors, with distinct colors at crossings on each pseudoline?

**Context.** Doctoral source: Sandro Michel Roch, Arrangements: Combinatorial and Computational Problems, TU Berlin, approved dissertation (2026); defense 15 December 2025; advisor Stefan Felsner. Conjectures 1,2,4, pp.25,31,35. Origins: Roch (2024); Björner–Las Vergnas–Sturmfels–White–Ziegler (1993; Euclidean form here); thesis, respectively. Setup: Euclidean pseudoline arrangements consist of finitely many proper embedded copies of R in R², pairwise crossing exactly once. They are simple when no three meet. Let m(A) be the maximum number of distinct crossings on one pseudoline.

**Source.** Sandro Michel Roch. *Arrangements: Combinatorial and Computational Problems*. Technische Universität Berlin, 2026. Advisor(s): Stefan Felsner. [primary source](https://doi.org/10.14279/depositonce-25298) Location: Conjectures 1,2,4, pp.25,31,35.

**Literature check.** Status: No matching resolution found through 10 October 2026.


<a id="q3899"></a>

## Q3899. In every simple arrangement of at least three pseudolines colored red and blue, both colors…

**Status:** Open · **Kind:** open problem · **Collection** 39

In every simple arrangement of at least three pseudolines colored red and blue, both colors used, is some bounded triangular cell incident to both colors?

**Context.** Doctoral source: Sandro Michel Roch, Arrangements: Combinatorial and Computational Problems, TU Berlin, approved dissertation (2026); defense 15 December 2025; advisor Stefan Felsner. Conjectures 1,2,4, pp.25,31,35. Origins: Roch (2024); Björner–Las Vergnas–Sturmfels–White–Ziegler (1993; Euclidean form here); thesis, respectively. Setup: Euclidean pseudoline arrangements consist of finitely many proper embedded copies of R in R², pairwise crossing exactly once. They are simple when no three meet. Let m(A) be the maximum number of distinct crossings on one pseudoline.

**Source.** Sandro Michel Roch. *Arrangements: Combinatorial and Computational Problems*. Technische Universität Berlin, 2026. Advisor(s): Stefan Felsner. [primary source](https://doi.org/10.14279/depositonce-25298) Location: Conjectures 1,2,4, pp.25,31,35.

**Literature check.** Status: No matching resolution found through 10 October 2026.


<a id="q3900"></a>

## Q3900. Are there simple arrangements with arbitrarily many pseudolines whose arrangement graph has odd…

**Status:** Open · **Kind:** open problem · **Collection** 39

Are there simple arrangements with arbitrarily many pseudolines whose arrangement graph has odd chromatic number three? Vertices are crossings; edges join consecutive crossings. An odd coloring is proper and gives every nonisolated vertex some color appearing oddly often among its neighbors; minimize the number of colors.

**Context.** Doctoral source: Sandro Michel Roch, Arrangements: Combinatorial and Computational Problems, TU Berlin, approved dissertation (2026); defense 15 December 2025; advisor Stefan Felsner. Conjectures 1,2,4, pp.25,31,35. Origins: Roch (2024); Björner–Las Vergnas–Sturmfels–White–Ziegler (1993; Euclidean form here); thesis, respectively. Setup: Euclidean pseudoline arrangements consist of finitely many proper embedded copies of R in R², pairwise crossing exactly once. They are simple when no three meet. Let m(A) be the maximum number of distinct crossings on one pseudoline.

**Source.** Sandro Michel Roch. *Arrangements: Combinatorial and Computational Problems*. Technische Universität Berlin, 2026. Advisor(s): Stefan Felsner. [primary source](https://doi.org/10.14279/depositonce-25298) Location: Conjectures 1,2,4, pp.25,31,35.

**Literature check.** Status: No matching resolution found through 10 October 2026.


<a id="q3901"></a>

## Q3901. If P_Δ is reflexive, must P_Γ be reflexive for every subcomplex Γ⊆Δ of the same dimension?

**Status:** Open · **Kind:** open problem · **Collection** 40

If P_Δ is reflexive, must P_Γ be reflexive for every subcomplex Γ⊆Δ of the same dimension?

**Context.** Paper origin: Torben Donzelmann, Thiago Holleben and Martina Juhnke, Symmetric (co)homology polytopes, arXiv:2602.17253v1, 19 February 2026, Questions 9.3–9.4, p.38. Setup: For a finite d-dimensional simplicial complex Δ, orient its faces and let A=∂\_d be its integral top boundary matrix. Define P_Δ=conv(±columns(A)) and P^Δ=conv(±columns(Aᵀ)). Each polytope P is considered in its real span with lattice L=span_R(P)∩Z^N. It is reflexive if its polar is a lattice polytope in the dual lattice L\*. For m=dim(P), define h\*\_P(t) by Σ\_{r≥0}|rP∩L|t^r=h\*\_P(t)/(1−t)^{m+1}.

**Source.** Torben Donzelmann, Thiago Holleben and Martina Juhnke. *Symmetric (co)homology polytopes*. 2026. [primary source](https://arxiv.org/abs/2602.17253v1) Location: Questions 9.3–9.4, p.38.

**Literature check.** Status: The authors’ current research page still lists this work as submitted. Known counterexamples concern a broader regular-matroid class; no matching boundary-polytope counterexample was found. No matching later resolution found through 10 October 2026.


<a id="q3905"></a>

## Q3905. Does a simple rotationally symmetric p-Venn diagram exist for every prime p?

**Status:** Open · **Kind:** open problem · **Collection** 40

Does a simple rotationally symmetric p-Venn diagram exist for every prime p?

**Context.** Paper source: Chris Dzoba, Simple symmetric Venn diagrams with 17, 19 and 23 curves, arXiv:2609.26546v2, 6 October 2026, §1, p.1. This is the older simple-symmetry question discussed by Grünbaum and by Ruskey, Savage and Wagon, not a thesis-origin question. Setup: An n-Venn diagram consists of n Jordan curves in the plane, intersecting only finitely often, such that each of the 2^n possible inside/outside membership patterns occurs in a nonempty connected region. It is simple if no point lies on three curves, and rotationally symmetric if rotation through 2π/n maps the family to itself.

**Source.** Chris Dzoba. *Simple symmetric Venn diagrams with 17, 19 and 23 curves*. 2026. [primary source](https://arxiv.org/abs/2609.26546v2) Location: §1, p.1.

**Literature check.** Status: The current revision reports constructions for p=17,19,23, extending previously known cases through 13; those finitely many constructions do not settle the universal question. General prime-order symmetric constructions allow multiple curves at a crossing and therefore do not answer this question. No matching resolution found through 10 October 2026.


<a id="q3906"></a>

## Q3906. For every integer n≥2, does an n-Venn diagram exist with exactly L_n crossings?

**Status:** Open · **Kind:** open problem · **Collection** 40

For every integer n≥2, does an n-Venn diagram exist with exactly L_n crossings?

**Context.** Paper source: Sofia Brenner, Petr Gregor, Torsten Mütze and Francesco Verciani, On Minimum Venn Diagrams, SoCG 2026, §1.1, p.21:4 and §6, p.21:17; published 27 May 2026. The conjecture originates with Bette Bultena and Frank Ruskey (1998). Setup: An n-Venn diagram is a family of n Jordan curves in the plane with finitely many intersection points, for which each of the 2^n inside/outside patterns occupies one nonempty connected region. Several curves may meet at a crossing; each distinct intersection location counts only once. Write L_n=⌈(2^n−2)/(n−1)⌉.

**Source.** Sofia Brenner, Petr Gregor, Torsten Mütze and Francesco Verciani. *On Minimum Venn Diagrams*. 2026. [primary source](https://doi.org/10.4230/LIPIcs.SoCG.2026.21) Location: §1.1, p.21:4 and §6, p.21:17; published 27 May 2026.

**Literature check.** Status: Cases n≤7 are known. The 2026 final proves asymptotic bounds rather than the exact conjecture. A later August preprint by John W. G. Seamons claims 39 crossings for n=8, expressly making no minimality claim; it does not attain L_8=37. No matching resolution found through 10 October 2026.

**Further links.** [1](https://zenodo.org/records/22004839)


<a id="q3907"></a>

## Q3907. If every curve is an ordinary Euclidean circle and the arrangement has no digons, must it have…

**Status:** Open · **Kind:** open problem · **Collection** 40

If every curve is an ordinary Euclidean circle and the arrangement has no digons, must it have at least 2n−4 triangular cells?

**Context.** Paper origin: Stefan Felsner and Manfred Scheucher, Arrangements of Pseudocircles: Triangles and Drawings, Discrete & Computational Geometry 65 (2021), 261–278; published online 27 January 2020. Conjectures 2.2 and 2.10, PDF pp.5,9. Related restatements by Felsner, Sandro Roch and Scheucher in Computing in Geometry and Topology 3(1), Article 11 (2024), Conjectures 6,8, pp.11:4–5; full final read. We use the original crossing-only domain. Setup: An intersecting arrangement consists of n≥3 Jordan curves in the plane, each pair crossing exactly twice, with no tangencies or triple intersections. Cells are components of the complement; a digon or triangle has respectively two or three boundary edges, including the unbounded cell when applicable.

**Source.** Stefan Felsner and Manfred Scheucher. *Arrangements of Pseudocircles: Triangles and Drawings*. 2021. [primary source](https://doi.org/10.1007/s00454-020-00173-4) Location: Conjectures 2.2 and 2.10, PDF pp.5,9.

**Literature check.** Status: The stronger 2n−4 claim for arbitrary digon-free pseudocircles is false; neither selected claim is that statement. No matching resolution found through 10 October 2026.

**Further links.** [1](https://doi.org/10.57717/cgt.v3i1.67)


<a id="q3908"></a>

## Q3908. Must every such pseudocircle arrangement, allowing digons, have at least n−1 triangular cells?

**Status:** Open · **Kind:** open problem · **Collection** 40

Must every such pseudocircle arrangement, allowing digons, have at least n−1 triangular cells?

**Context.** Paper origin: Stefan Felsner and Manfred Scheucher, Arrangements of Pseudocircles: Triangles and Drawings, Discrete & Computational Geometry 65 (2021), 261–278; published online 27 January 2020. Conjectures 2.2 and 2.10, PDF pp.5,9. Related restatements by Felsner, Sandro Roch and Scheucher in Computing in Geometry and Topology 3(1), Article 11 (2024), Conjectures 6,8, pp.11:4–5; full final read. We use the original crossing-only domain. Setup: An intersecting arrangement consists of n≥3 Jordan curves in the plane, each pair crossing exactly twice, with no tangencies or triple intersections. Cells are components of the complement; a digon or triangle has respectively two or three boundary edges, including the unbounded cell when applicable.

**Source.** Stefan Felsner and Manfred Scheucher. *Arrangements of Pseudocircles: Triangles and Drawings*. 2021. [primary source](https://doi.org/10.1007/s00454-020-00173-4) Location: Conjectures 2.2 and 2.10, PDF pp.5,9.

**Literature check.** Status: The stronger 2n−4 claim for arbitrary digon-free pseudocircles is false; neither selected claim is that statement. No matching resolution found through 10 October 2026.

**Further links.** [1](https://doi.org/10.57717/cgt.v3i1.67)


<a id="q3909"></a>

## Q3909. For every fixed 0<ε<1/6 and every sequence n^{−1/3+ε}≪p(n)≪n^{−ε}, determine χ\_c(G_{n,p}) to…

**Status:** Open · **Kind:** open problem (Problem 4.6.3) · **Collection** 40

For every fixed 0<ε<1/6 and every sequence n^{−1/3+ε}≪p(n)≪n^{−ε}, determine χ\_c(G_{n,p}) to multiplicative error 1+o(1), with probability tending to one.

**Context.** Doctoral dissertation: Manuel Fernandez V, Large-scale Phenomena in Geometry, Probability, and Combinatorics, Georgia Tech, May 2025; advisor Galyna V. Livshyts. Problem 4.6.3, p.175, restates joint work with Lutz Warnke. Setup: G_{n,p} has n labeled vertices and each edge independently present with probability p. Its clique chromatic number χ\_c is the least number of vertex colors preventing monochromatic inclusion-maximal cliques of size at least two. Write a≪b for a/b→0 as n→∞.

**Source.** Manuel Fernandez V. *Large-scale Phenomena in Geometry, Probability, and Combinatorics*. Georgia Institute of Technology, 2025. Advisor(s): Galyna V. Livshyts. [primary source](https://repository.gatech.edu/bitstreams/1f830ab2-9b1f-48bd-b215-d6bbcc126b51/download) Location: Problem 4.6.3, p.175, restates joint work with Lutz Warnke.

**Literature check.** Status: Order Θ(log(n)/p) is known, but the leading factor remains unresolved in the authors’ accepted RSA manuscript, arXiv:2403.03013v3 (2 June 2025), Problem 6.3, p.24. Final metadata match; no substantive difference or later matching resolution found through 10 October 2026.

**Further links.** [1](https://arxiv.org/abs/2403.03013v3)


<a id="q3910"></a>

## Q3910. Is S_k(n)=S_{k−ℓ}(n−ℓ) whenever 1≤ℓ&lt;k≤n?

**Status:** Open · **Kind:** open problem (Problem 1.6) · **Collection** 40

Is S_k(n)=S_{k−ℓ}(n−ℓ) whenever 1≤ℓ&lt;k≤n?

**Context.** For closed connected k-dimensional subgroups T⊆(R/Z)^n not contained in the union of coordinate hyperplanes, let D(T)=min_{x∈T}max_i|x_i−1/2|, using representatives x_i∈[0,1], and S_k(n)={D(T)}. In an abelian group G, C is solid if no D⊋C has D−D=C−C. It is a maximal supplement if some nonempty W⊆G makes the translates c+W, c∈C, pairwise disjoint, and C is inclusion-maximal with that property for W. Locators: thesis Problem 1.6, §1.9(4), Question 3.9; final spectrum paper Problem 1.6, §9(5); supplement paper Question 9.

**Source.** Noah Kravitz. *Combinatorics with a View Towards Number Theory*. Princeton University, 2025. Advisor(s): Noga Alon. [primary source](https://theses-dissertations.princeton.edu/items/3c3fa837-2c08-4f9e-af79-19786c0badf3) Location: thesis Problem 1.6, §1.9(4), Question 3.9; final spectrum paper Problem 1.6, §9(5); supplement paper Question 9.

**Literature check.** Status: No resolution found in searches through 10 October 2026; the 2026 relative-spectrum results concern restricted subtori.

**Further links.** [1](https://doi.org/10.1017/S0305004125101497) · [2](https://doi.org/10.1016/j.jnt.2020.10.009)


<a id="q3911"></a>

## Q3911. Is ⋃\_{n≥1}S_1(n) dense in [0,1/2]?

**Status:** Open · **Kind:** open problem (Problem 1.6) · **Collection** 40

Is ⋃\_{n≥1}S_1(n) dense in [0,1/2]?

**Context.** For closed connected k-dimensional subgroups T⊆(R/Z)^n not contained in the union of coordinate hyperplanes, let D(T)=min_{x∈T}max_i|x_i−1/2|, using representatives x_i∈[0,1], and S_k(n)={D(T)}. In an abelian group G, C is solid if no D⊋C has D−D=C−C. It is a maximal supplement if some nonempty W⊆G makes the translates c+W, c∈C, pairwise disjoint, and C is inclusion-maximal with that property for W. Locators: thesis Problem 1.6, §1.9(4), Question 3.9; final spectrum paper Problem 1.6, §9(5); supplement paper Question 9.

**Source.** Noah Kravitz. *Combinatorics with a View Towards Number Theory*. Princeton University, 2025. Advisor(s): Noga Alon. [primary source](https://theses-dissertations.princeton.edu/items/3c3fa837-2c08-4f9e-af79-19786c0badf3) Location: thesis Problem 1.6, §1.9(4), Question 3.9; final spectrum paper Problem 1.6, §9(5); supplement paper Question 9.

**Literature check.** Status: No resolution found in searches through 10 October 2026; the 2026 relative-spectrum results concern restricted subtori.

**Further links.** [1](https://doi.org/10.1017/S0305004125101497) · [2](https://doi.org/10.1016/j.jnt.2020.10.009)


<a id="q3912"></a>

## Q3912. Determine the asymptotic growth of the largest integer 0≤h(n)≤n such that every nonempty solid C…

**Status:** Open · **Kind:** open problem (Problem 1.6) · **Collection** 40

Determine the asymptotic growth of the largest integer 0≤h(n)≤n such that every nonempty solid C in every abelian group G of order n, with |C|≤h(n), is a maximal supplement.

**Context.** For closed connected k-dimensional subgroups T⊆(R/Z)^n not contained in the union of coordinate hyperplanes, let D(T)=min_{x∈T}max_i|x_i−1/2|, using representatives x_i∈[0,1], and S_k(n)={D(T)}. In an abelian group G, C is solid if no D⊋C has D−D=C−C. It is a maximal supplement if some nonempty W⊆G makes the translates c+W, c∈C, pairwise disjoint, and C is inclusion-maximal with that property for W. Locators: thesis Problem 1.6, §1.9(4), Question 3.9; final spectrum paper Problem 1.6, §9(5); supplement paper Question 9.

**Source.** Noah Kravitz. *Combinatorics with a View Towards Number Theory*. Princeton University, 2025. Advisor(s): Noga Alon. [primary source](https://theses-dissertations.princeton.edu/items/3c3fa837-2c08-4f9e-af79-19786c0badf3) Location: thesis Problem 1.6, §1.9(4), Question 3.9; final spectrum paper Problem 1.6, §9(5); supplement paper Question 9.

**Literature check.** Status: No resolution found in searches through 10 October 2026; the 2026 relative-spectrum results concern restricted subtori.

**Further links.** [1](https://doi.org/10.1017/S0305004125101497) · [2](https://doi.org/10.1016/j.jnt.2020.10.009)


<a id="q3922"></a>

## Q3922. Determine N(7).

**Status:** Open · **Kind:** open problem (Question 4.1) · **Collection** 40

Determine N(7).

**Context.** For a finite simple d-regular graph G, an independent exact r-cover is an independent vertex set S such that every vertex outside S has exactly r neighbors in S. Let N(d) be the minimum number of vertices of a nonempty such graph having, for every integer 1≤r≤d, an independent exact r-cover; the covers may differ with r. Origin: Robert Johnson’s 2024 question, recorded as Question 4.1; the surviving finite case is identified before Proposition 4.8, and the asymptotic question in Remark 4.9. Existence for every d is proved; known bounds give (2−o(1))d≤log N(d)≤d(log(4d)−1+o(1)); log is natural.

**Source.** Hou Tin Chau. *Graphs with Independent Exact r-Covers for All r*. 2025. [primary source](https://arxiv.org/abs/2501.05854) Location: Robert Johnson’s 2024 question, recorded as Question 4.1; the surviving finite case is identified before Proposition 4.8, and the asymptotic question in Remark 4.9.

**Literature check.** Status: No later version, published successor, resolution or matching claim found through 10 October 2026.

**Further links.** [1](https://research-information.bris.ac.uk/en/studentTheses/some-isoperimetric-type-problems-on-graphs/)


<a id="q3923"></a>

## Q3923. Determine the asymptotic growth of N(d) as d→∞.

**Status:** Open · **Kind:** open problem (Question 4.1) · **Collection** 40

Determine the asymptotic growth of N(d) as d→∞.

**Context.** For a finite simple d-regular graph G, an independent exact r-cover is an independent vertex set S such that every vertex outside S has exactly r neighbors in S. Let N(d) be the minimum number of vertices of a nonempty such graph having, for every integer 1≤r≤d, an independent exact r-cover; the covers may differ with r. Origin: Robert Johnson’s 2024 question, recorded as Question 4.1; the surviving finite case is identified before Proposition 4.8, and the asymptotic question in Remark 4.9. Existence for every d is proved; known bounds give (2−o(1))d≤log N(d)≤d(log(4d)−1+o(1)); log is natural.

**Source.** Hou Tin Chau. *Graphs with Independent Exact r-Covers for All r*. 2025. [primary source](https://arxiv.org/abs/2501.05854) Location: Robert Johnson’s 2024 question, recorded as Question 4.1; the surviving finite case is identified before Proposition 4.8, and the asymptotic question in Remark 4.9.

**Literature check.** Status: No later version, published successor, resolution or matching claim found through 10 October 2026.

**Further links.** [1](https://research-information.bris.ac.uk/en/studentTheses/some-isoperimetric-type-problems-on-graphs/)


<a id="q3928"></a>

## Q3928. Is there an absolute constant C such that c(G)≤C for every graph G of diameter two?

**Status:** Open · **Kind:** open problem · **Collection** 40

Is there an absolute constant C such that c(G)≤C for every graph G of diameter two?

**Context.** For a finite simple graph G, H(S) is obtained by repeatedly adding every vertex with at least two neighbors already present. Its P3-Carathéodory number c(G) is the least c such that every v∈H(S) belongs to H(T) for some T⊆S with |T|≤c. Origin: Joint paper-origin conjecture with his two advisers and Simone Dantas, reaffirmed in the post-publication thesis conclusion. No resolution found through 10 October 2026.

**Source.** Braully Rocha da Silva. *Aspectos Computacionais Teóricos na Convexidade P3: Número de Carathéodory e Seleção de Conjunto Alvo*. Universidade Federal de Goiás, 2026. Advisor(s): Erika Morais Martins Coelho; co-adviser Hebert Coelho da Silva. [primary source](https://repositorio.bc.ufg.br/tede/bitstreams/8ed9f1ea-ef10-4ac1-87c4-2dc38cc8d003/download) Location: Thesis §2.3, printed page 38, and Chapter 7, page 75.

**Literature check.** Status: Origin: Joint paper-origin conjecture with his two advisers and Simone Dantas, reaffirmed in the post-publication thesis conclusion. No resolution found through 10 October 2026.

**Further links.** [1](https://doi.org/10.1016/j.dam.2026.02.029)


<a id="q4009"></a>

## Q4009. Does every connected graph G on n≥3 vertices satisfy μ̃(G)≤μ̃(C_n)?

**Status:** Open · **Kind:** conjecture (Conjecture 5.1) · **Collection** 41

Does every connected graph G on n≥3 vertices satisfy μ̃(G)≤μ̃(C_n)?

**Context.** For a finite simple graph G, a perfect edge dominating set is F⊆E(G) such that every edge outside F shares an endpoint with exactly one edge of F. No analogous restriction is imposed on edges inside F. Let μ̃(G) count all such subsets, including E(G), rather than only minimum or inclusion-minimal ones. Let C_n denote the n-vertex cycle.

**Source.** Luciano N. Grippo, Min Chih Lin, Verónica Moyano and Camilo Vera. *Counting perfect edge dominating sets: extremal results and linear-time algorithms*. 2026. [primary source](https://arxiv.org/abs/2607.03894v1) Location: Conjecture 5.1, page 27, in the July 2026 paper, not the 2017 dissertation.

**Literature check.** Status: Origin and status: Conjecture 5.1, page 27, in the July 2026 paper, not the 2017 dissertation. The paper establishes the bound for trees; counting algorithms for chordal and generalized series-parallel graphs do not settle all connected graphs. No proof or disproof found through 10 October 2026.

**Further links.** [1](https://bibliotecadigital.exactas.uba.ar/collection/tesis/document/tesis_n6216_Moyano)


<a id="q4013"></a>

## Q4013. Characterize bipartite graphs having no proper {0,1}-edge-labelling.

**Status:** Open · **Kind:** open problem · **Collection** 41

Characterize bipartite graphs having no proper {0,1}-edge-labelling.

**Context.** Graphs are finite and simple. An edge-labelling is proper when the sums of labels on incident edges differ at the endpoints of every edge. Origin: Q4013 restates Lyngsie’s 2018 §4 problem, with earlier characterization work attributed there to Skowronek-Kaziów; Q4014 is the 2026 authors’ explicit strengthening question.

**Source.** Olivier Baudon, Julien Bensmail and Vayssieres. *Some remarks and results on the Standard (2,2)-Conjecture*. 2026. [primary source](https://www.opuscula.agh.edu.pl/vol46/2/art/opuscula_math_4606.pdf) Location: Baudon–Bensmail–Vayssieres, Opuscula Mathematica 46(2) (2026), p.135; restates Lyngsie’s 2018 §4 problem

**Literature check.** Status: Full final read; no later resolution found through 10 October 2026.

**Further links.** [1](https://dmtcs.episciences.org/4554/pdf) · [2](https://jbensmai.fr/datas/thesis/phd.pdf)


<a id="q4014"></a>

## Q4014. If G has no connected component isomorphic to K₂ or K₃, must there be F⊆E(G) such that adjacent…

**Status:** Open · **Kind:** open problem · **Collection** 41

If G has no connected component isomorphic to K₂ or K₃, must there be F⊆E(G) such that adjacent vertices in G[F] have different G[F]-degrees, and G−F has a proper {1,2}-edge-labelling?

**Context.** Graphs are finite and simple. An edge-labelling is proper when the sums of labels on incident edges differ at the endpoints of every edge. Origin: Q4013 restates Lyngsie’s 2018 §4 problem, with earlier characterization work attributed there to Skowronek-Kaziów; Q4014 is the 2026 authors’ explicit strengthening question.

**Source.** Olivier Baudon, Julien Bensmail and Vayssieres. *Some remarks and results on the Standard (2,2)-Conjecture*. 2026. [primary source](https://www.opuscula.agh.edu.pl/vol46/2/art/opuscula_math_4606.pdf) Location: Baudon–Bensmail–Vayssieres, Opuscula Mathematica 46(2) (2026), p.135 (the authors’ strengthening question)

**Literature check.** Status: Full final read; no later resolution found through 10 October 2026.

**Further links.** [1](https://dmtcs.episciences.org/4554/pdf) · [2](https://jbensmai.fr/datas/thesis/phd.pdf)


<a id="q4015"></a>

## Q4015. Is every finite passable game over P equivalent to the game form of such a Hex region?

**Status:** Open · **Kind:** open problem · **Collection** 41

Is every finite passable game over P equivalent to the game form of such a Hex region?

**Context.** Let P={⊥,a,b,c,⊤}, with a,b,c incomparable between bottom and top. Finite game forms are atoms [p], p∈P, or {L|R} with nonempty finite sets of earlier forms. Write Gᴸ,Gᴿ for options. Recursively, G≤H means every Gᴸ◁H, every G◁Hᴿ, and additionally G◁H if either game is atomic. Define G◁H when some Gᴿ≤H, some G≤Hᴸ, or both are atoms [p],[q] with p≤q. Equivalence means G≤H≤G. A form is passable when every follower F, including itself, satisfies F◁F. A three-terminal Hex region is a finite set of hexagonal cells completely surrounded by stones, with three black and three white boundary components. Players fill empty hexagonal cells with their own colours. Its terminal atoms record black connectivity: ⊥ no pair, a only 2–3, b only 1–3, c only 1–2, ⊤ all three. Black moves are left options; white moves are right options. Definition source: Selinger, Integers 22 (2022), #G3, Definitions 4.1, 4.3, 6.2.

**Source.** Eric Demer and Peter Selinger. *On 3-terminal positions in Hex*. 2025. [primary source](https://arxiv.org/abs/2507.08247) Location: conclusion p.42.

**Literature check.** Status: No later version, resolution or matching claim found through 10 October 2026.

**Further links.** [1](https://math.colgate.edu/~integers/wg3/wg3.pdf)


<a id="q4016"></a>

## Q4016. For maximum hyperedge size at most three, is deciding whether Client has a winning strategy…

**Status:** Open · **Kind:** conjecture (Conjecture 2.22) · **Collection** 41

For maximum hyperedge size at most three, is deciding whether Client has a winning strategy polynomial-time solvable?

**Context.** On an explicitly listed finite hypergraph, Waiter offers two unclaimed vertices; Client claims one and Waiter receives the other. An unpaired final vertex goes to Client. In Client-Waiter, Client wins by owning an entire hyperedge; otherwise Waiter wins. In Waiter-Client, instead Waiter wins by owning an entire hyperedge. For a Waiter-winning hypergraph H let t(H) be the least number of offers within which Waiter can force victory. Let os(k) be the maximum t(H) among such H with maximum hyperedge size k. Origin: Q4016 is thesis Conjecture 2.22, p.60; the final paper’s equivalent Tadpole problem remains open. Q4017 is paper Problem 1, p.89:16. Maker-Maker domination: thesis pp.102,133, restating joint work with Duchêne, Dumas, Parreau and Rémila. A cograph has no induced four-vertex path. Two players alternately claim unclaimed vertices, starting with none claimed. The first whose own set dominates the finite simple graph wins; otherwise exhaustion is a draw. A set dominates when every vertex belongs to it or has a neighbour in it.

**Source.** Nacim Oijid. *Complexity of Positional Games on Graphs*. Université Claude Bernard Lyon 1, 2024. Advisor(s): Éric Duchêne and Aline Parreau. [primary source](https://nacim-oijid.fr/PhD_thesis_Nacim_Oijid.pdf) Location: thesis Conjecture 2.22, p.60; equivalent Tadpole problem in Gledel–Oijid–Tavenas–Thomassé, ICALP 2025, §6

**Literature check.** Status: No later resolution found through 10 October 2026. The thesis retains Q4018 after the May 2024 journal publication.

**Further links.** [1](https://doi.org/10.4230/LIPIcs.ICALP.2025.89) · [2](https://doi.org/10.1016/j.dam.2024.01.023)


<a id="q4017"></a>

## Q4017. Determine os(k) for all k≥3.

**Status:** Open · **Kind:** open problem (Problem 1) · **Collection** 41

Determine os(k) for all k≥3.

**Context.** On an explicitly listed finite hypergraph, Waiter offers two unclaimed vertices; Client claims one and Waiter receives the other. An unpaired final vertex goes to Client. In Client-Waiter, Client wins by owning an entire hyperedge; otherwise Waiter wins. In Waiter-Client, instead Waiter wins by owning an entire hyperedge. For a Waiter-winning hypergraph H let t(H) be the least number of offers within which Waiter can force victory. Let os(k) be the maximum t(H) among such H with maximum hyperedge size k. Origin: Q4016 is thesis Conjecture 2.22, p.60; the final paper’s equivalent Tadpole problem remains open. Q4017 is paper Problem 1, p.89:16. Maker-Maker domination: thesis pp.102,133, restating joint work with Duchêne, Dumas, Parreau and Rémila. A cograph has no induced four-vertex path. Two players alternately claim unclaimed vertices, starting with none claimed. The first whose own set dominates the finite simple graph wins; otherwise exhaustion is a draw. A set dominates when every vertex belongs to it or has a neighbour in it.

**Source.** Nacim Oijid. *Complexity of Positional Games on Graphs*. Université Claude Bernard Lyon 1, 2024. Advisor(s): Éric Duchêne and Aline Parreau. [primary source](https://nacim-oijid.fr/PhD_thesis_Nacim_Oijid.pdf) Location: Gledel–Oijid–Tavenas–Thomassé, On the Complexity of Client-Waiter and Waiter-Client Games, ICALP 2025, Problem 1, p.89:16

**Literature check.** Status: No later resolution found through 10 October 2026. The thesis retains Q4018 after the May 2024 journal publication.

**Further links.** [1](https://doi.org/10.4230/LIPIcs.ICALP.2025.89) · [2](https://doi.org/10.1016/j.dam.2024.01.023)


<a id="q4018"></a>

## Q4018. Is there a polynomial-time algorithm deciding whether the first player can force a win on any…

**Status:** Open · **Kind:** open problem · **Collection** 41

Is there a polynomial-time algorithm deciding whether the first player can force a win on any possibly disconnected cograph?

**Context.** On an explicitly listed finite hypergraph, Waiter offers two unclaimed vertices; Client claims one and Waiter receives the other. An unpaired final vertex goes to Client. In Client-Waiter, Client wins by owning an entire hyperedge; otherwise Waiter wins. In Waiter-Client, instead Waiter wins by owning an entire hyperedge. For a Waiter-winning hypergraph H let t(H) be the least number of offers within which Waiter can force victory. Let os(k) be the maximum t(H) among such H with maximum hyperedge size k. Origin: Q4016 is thesis Conjecture 2.22, p.60; the final paper’s equivalent Tadpole problem remains open. Q4017 is paper Problem 1, p.89:16. Maker-Maker domination: thesis pp.102,133, restating joint work with Duchêne, Dumas, Parreau and Rémila. A cograph has no induced four-vertex path. Two players alternately claim unclaimed vertices, starting with none claimed. The first whose own set dominates the finite simple graph wins; otherwise exhaustion is a draw. A set dominates when every vertex belongs to it or has a neighbour in it.

**Source.** Nacim Oijid. *Complexity of Positional Games on Graphs*. Université Claude Bernard Lyon 1, 2024. Advisor(s): Éric Duchêne and Aline Parreau. [primary source](https://nacim-oijid.fr/PhD_thesis_Nacim_Oijid.pdf) Location: thesis pp.102,133 (Maker-Maker domination), restating joint work with Duchêne, Dumas, Parreau and Rémila

**Literature check.** Status: No later resolution found through 10 October 2026. The thesis retains Q4018 after the May 2024 journal publication.

**Further links.** [1](https://doi.org/10.4230/LIPIcs.ICALP.2025.89) · [2](https://doi.org/10.1016/j.dam.2024.01.023)


<a id="q4019"></a>

## Q4019. Determine this decision problem’s complexity on caterpillars, trees whose non-leaf vertices…

**Status:** Open · **Kind:** open problem · **Collection** 41

Determine this decision problem’s complexity on caterpillars, trees whose non-leaf vertices induce a path, possibly empty.

**Context.** On a finite simple graph G, Maker and Breaker alternately colour one uncoloured vertex red and blue, respectively. The input specifies who starts. At exhaustion, Maker’s score counts vertices v whose closed neighbourhood N[v] is entirely red. Maker maximizes this score; Breaker minimizes it. Given an integer s, ask whether Maker can guarantee score at least s. Neighborhood diversity w is the smallest number of vertex classes having identical neighbours outside their class, each class a clique or independent set.

**Source.** Mathieu Hilaire, Perig Montfort and Nacim Oijid. *On the Complexity of the Maker-Breaker Happy Vertex Game*. 2026. [primary source](https://doi.org/10.4230/LIPIcs.FUN.2026.24) Location: §4.3 and §5.

**Literature check.** Status: Final published 15 May 2026; no later resolution found through 10 October 2026.


<a id="q4020"></a>

## Q4020. Determine its complexity on cographs, graphs with no induced four-vertex path.

**Status:** Open · **Kind:** open problem · **Collection** 41

Determine its complexity on cographs, graphs with no induced four-vertex path.

**Context.** On a finite simple graph G, Maker and Breaker alternately colour one uncoloured vertex red and blue, respectively. The input specifies who starts. At exhaustion, Maker’s score counts vertices v whose closed neighbourhood N[v] is entirely red. Maker maximizes this score; Breaker minimizes it. Given an integer s, ask whether Maker can guarantee score at least s. Neighborhood diversity w is the smallest number of vertex classes having identical neighbours outside their class, each class a clique or independent set.

**Source.** Mathieu Hilaire, Perig Montfort and Nacim Oijid. *On the Complexity of the Maker-Breaker Happy Vertex Game*. 2026. [primary source](https://doi.org/10.4230/LIPIcs.FUN.2026.24) Location: §4.3 and §5.

**Literature check.** Status: Final published 15 May 2026; no later resolution found through 10 October 2026.


<a id="q4021"></a>

## Q4021. Does the problem have a polynomial kernel parameterized by w: a polynomial-time reduction to an…

**Status:** Open · **Kind:** open problem · **Collection** 41

Does the problem have a polynomial kernel parameterized by w: a polynomial-time reduction to an equivalent instance of encoding length w^O(1)?

**Context.** On a finite simple graph G, Maker and Breaker alternately colour one uncoloured vertex red and blue, respectively. The input specifies who starts. At exhaustion, Maker’s score counts vertices v whose closed neighbourhood N[v] is entirely red. Maker maximizes this score; Breaker minimizes it. Given an integer s, ask whether Maker can guarantee score at least s. Neighborhood diversity w is the smallest number of vertex classes having identical neighbours outside their class, each class a clique or independent set.

**Source.** Mathieu Hilaire, Perig Montfort and Nacim Oijid. *On the Complexity of the Maker-Breaker Happy Vertex Game*. 2026. [primary source](https://doi.org/10.4230/LIPIcs.FUN.2026.24) Location: §4.3 and §5.

**Literature check.** Status: Final published 15 May 2026; no later resolution found through 10 October 2026.


<a id="q4022"></a>

## Q4022. Is deciding whether Maker wins from the empty board, with positive integers a,b supplied in the…

**Status:** Open · **Kind:** open problem · **Collection** 41

Is deciding whether Maker wins from the empty board, with positive integers a,b supplied in the input, EXPTIME-complete?

**Context.** A finite hypergraph H is explicitly listed. Maker has a red tokens and Breaker b blue tokens, initially off-board. Starting with Maker, players alternate placing an unused token on an empty vertex, moving an existing own token to any empty vertex, or passing. Vacated vertices become empty. Maker wins upon covering a hyperedge with red tokens; Breaker wins by preventing this indefinitely, including repetition of a state with the same player to move. This is the token-jumping (a,b)-game.

**Source.** Guillaume Bagan, Quentin Deschamps, Florian Galliot, Mirjana Mikalački and Nacim Oijid. *Token Positional Games*. 2026. [primary source](https://doi.org/10.4230/LIPIcs.FUN.2026.5) Location: §6, p.5:20.

**Literature check.** Status: The final published 15 May 2026 leaves these questions open; the EXPTIME-completeness result there concerns token sliding from preoccupied positions. No later resolution found through 10 October 2026.


<a id="q4023"></a>

## Q4023. Give a structural characterization of the hypergraphs on which Maker wins the (3,2)-game.

**Status:** Open · **Kind:** open problem · **Collection** 41

Give a structural characterization of the hypergraphs on which Maker wins the (3,2)-game.

**Context.** A finite hypergraph H is explicitly listed. Maker has a red tokens and Breaker b blue tokens, initially off-board. Starting with Maker, players alternate placing an unused token on an empty vertex, moving an existing own token to any empty vertex, or passing. Vacated vertices become empty. Maker wins upon covering a hyperedge with red tokens; Breaker wins by preventing this indefinitely, including repetition of a state with the same player to move. This is the token-jumping (a,b)-game.

**Source.** Guillaume Bagan, Quentin Deschamps, Florian Galliot, Mirjana Mikalački and Nacim Oijid. *Token Positional Games*. 2026. [primary source](https://doi.org/10.4230/LIPIcs.FUN.2026.5) Location: §6, p.5:20.

**Literature check.** Status: The final published 15 May 2026 leaves these questions open; the EXPTIME-completeness result there concerns token sliding from preoccupied positions. No later resolution found through 10 October 2026.


<a id="q4024"></a>

## Q4024. Can the winner be decided in f(t)n^C time for a computable f and constant C?

**Status:** Open · **Kind:** open problem · **Collection** 41

Can the winner be decided in f(t)n^C time for a computable f and constant C?

**Context.** In a finite simple n-vertex graph G, Dominator and Staller alternately claim unclaimed vertices; input specifies who starts. Dominator wins by owning a set containing or adjacent to every vertex; otherwise Staller wins. Treewidth t minimizes largest-bag-size minus one over tree-indexed bags covering vertices/edges, with bags containing each vertex forming a connected subtree. Modular width w is the least w allowing G to be built from singletons by disjoint unions, complete joins and substitutions into templates of at most w vertices. Substitution replaces template vertices by graphs, adding all cross-edges exactly along template edges.

**Source.** Guillaume Bagan, Mathieu Hilaire, Nacim Oijid and Aline Parreau. *On the parameterized complexity of the Maker-Breaker domination game*. 2026. [primary source](https://arxiv.org/abs/2601.08562) Location: §7, p.24.

**Literature check.** Status: No newer version or resolution found through 10 October 2026.


<a id="q4025"></a>

## Q4025. Is there a polynomial-time reduction to an equivalent winner-decision instance of encoding…

**Status:** Open · **Kind:** open problem · **Collection** 41

Is there a polynomial-time reduction to an equivalent winner-decision instance of encoding length w^O(1)?

**Context.** In a finite simple n-vertex graph G, Dominator and Staller alternately claim unclaimed vertices; input specifies who starts. Dominator wins by owning a set containing or adjacent to every vertex; otherwise Staller wins. Treewidth t minimizes largest-bag-size minus one over tree-indexed bags covering vertices/edges, with bags containing each vertex forming a connected subtree. Modular width w is the least w allowing G to be built from singletons by disjoint unions, complete joins and substitutions into templates of at most w vertices. Substitution replaces template vertices by graphs, adding all cross-edges exactly along template edges.

**Source.** Guillaume Bagan, Mathieu Hilaire, Nacim Oijid and Aline Parreau. *On the parameterized complexity of the Maker-Breaker domination game*. 2026. [primary source](https://arxiv.org/abs/2601.08562) Location: §7, p.24.

**Literature check.** Status: No newer version or resolution found through 10 October 2026.


<a id="q4026"></a>

## Q4026. Determine winner-decision complexity for graphs of maximum degree at most three.

**Status:** Open · **Kind:** open problem · **Collection** 41

Determine winner-decision complexity for graphs of maximum degree at most three.

**Context.** In a finite simple n-vertex graph G, Dominator and Staller alternately claim unclaimed vertices; input specifies who starts. Dominator wins by owning a set containing or adjacent to every vertex; otherwise Staller wins. Treewidth t minimizes largest-bag-size minus one over tree-indexed bags covering vertices/edges, with bags containing each vertex forming a connected subtree. Modular width w is the least w allowing G to be built from singletons by disjoint unions, complete joins and substitutions into templates of at most w vertices. Substitution replaces template vertices by graphs, adding all cross-edges exactly along template edges.

**Source.** Guillaume Bagan, Mathieu Hilaire, Nacim Oijid and Aline Parreau. *On the parameterized complexity of the Maker-Breaker domination game*. 2026. [primary source](https://arxiv.org/abs/2601.08562) Location: §7, p.24.

**Literature check.** Status: No newer version or resolution found through 10 October 2026.


<a id="q4027"></a>

## Q4027. Determine the complexity of deciding whether the first player wins the Maker-Maker game on…

**Status:** Open · **Kind:** open problem · **Collection** 41

Determine the complexity of deciding whether the first player wins the Maker-Maker game on hypergraphs with nonempty edges of size at most three: players alternately claim one unclaimed vertex, the first to own an entire edge wins, and otherwise exhaustion is a draw.

**Context.** Doctoral context: Galliot, Hypergraphs and the Maker-Breaker game: a structural approach, Université Grenoble Alpes, defended 3 July 2023; supervisor Sylvain Gravier, co-supervisor Isabelle Sivignon. All hypergraphs below are finite and explicitly listed; play starts with every vertex unclaimed.

**Source.** Florian Galliot and Jonas Sénizergues. *A unified convention for achievement positional games*. 2025. [primary source](https://arxiv.org/abs/2503.18163) Location: §5, p.29.

**Literature check.** Status: Current v2 is dated 18 March 2026; no later resolution found through 10 October 2026.


<a id="q4028"></a>

## Q4028. Is Maker-Breaker winner-decision polynomial-time when the input explicitly lists both a…

**Status:** Open · **Kind:** open problem · **Collection** 41

Is Maker-Breaker winner-decision polynomial-time when the input explicitly lists both a hypergraph and all its inclusion-minimal transversals? A transversal meets every edge. Maker moves first; players alternately claim one unclaimed vertex. Maker wins by owning an edge, and Breaker wins otherwise. Running time is measured in the combined explicit input length.

**Context.** Doctoral context: Galliot, Hypergraphs and the Maker-Breaker game: a structural approach, Université Grenoble Alpes, defended 3 July 2023; supervisor Sylvain Gravier, co-supervisor Isabelle Sivignon. All hypergraphs below are finite and explicitly listed; play starts with every vertex unclaimed.

**Source.** Florian Galliot and Jonas Sénizergues. *A unified convention for achievement positional games*. 2025. [primary source](https://arxiv.org/abs/2503.18163) Location: §5, p.29.

**Literature check.** Status: Current v2 is dated 18 March 2026; no later resolution found through 10 October 2026.


<a id="q4029"></a>

## Q4029. Determine winner-decision complexity for arbitrary H whose edges have size at most three,…

**Status:** Open · **Kind:** open problem · **Collection** 41

Determine winner-decision complexity for arbitrary H whose edges have size at most three, without assuming linearity.

**Context.** Doctoral context: Gledel, Couverture de sommets sous contraintes, Université de Lyon, defended 24 September 2019; advisors Éric Duchêne and Aline Parreau. On a finite explicitly listed hypergraph H, Avoider and Enforcer alternately claim one unclaimed vertex until exhaustion. Enforcer wins if Avoider owns an entire hyperedge; otherwise Avoider wins. An empty edge makes Enforcer win. Start from an empty board, with Avoider moving last: she starts exactly when |V(H)| is odd.

**Source.** Florian Galliot, Valentin Gledel and Aline Parreau. *The Avoider-Enforcer Game in Hypergraphs of Rank 3*. 2026. [primary source](https://doi.org/10.37236/14014) Location: conclusion p.24.

**Literature check.** Status: The final, published 22 May 2026, solves the linear case with this move order. No later resolution found through 10 October 2026.


<a id="q4031"></a>

## Q4031. Is deciding whether Alice can force the closed hull game to end within k moves PSPACE-complete,…

**Status:** Open · **Kind:** open problem · **Collection** 41

Is deciding whether Alice can force the closed hull game to end within k moves PSPACE-complete, with positive integer k as input?

**Context.** Doctoral context: Nisse, Jeux des gendarmes et du voleur dans les graphes: Mineurs de graphes, stratégies connexes, et approche distribuée, Paris-Sud XI, defended 2 July 2007; advisor Pierre Fraigniaud. For a finite simple graph G, I(S) contains S and all vertices on shortest paths between vertices of S. H(S) is obtained by iterating I to a fixed point. Starting with S empty, Alice and Bob alternate adding one vertex outside I(S) in the closed interval game, or outside H(S) in the closed hull game, until none remains. Alice starts.

**Source.** Samuel N. Araújo, Fabrício Benevides, Nicolas Martins, Nicolas Nisse and Rudini Sampaio. *The Closed Hull Game and the Closed Interval Game*. 2026. [primary source](https://doi.org/10.4230/LIPIcs.FUN.2026.4) Location: pp.4:2,4:10–11.

**Literature check.** Status: No later resolution found through 10 October 2026.


<a id="q4032"></a>

## Q4032. Is the analogous closed interval decision problem NP-hard on cobipartite graphs, whose vertices…

**Status:** Open · **Kind:** open problem · **Collection** 41

Is the analogous closed interval decision problem NP-hard on cobipartite graphs, whose vertices partition into two cliques?

**Context.** Doctoral context: Nisse, Jeux des gendarmes et du voleur dans les graphes: Mineurs de graphes, stratégies connexes, et approche distribuée, Paris-Sud XI, defended 2 July 2007; advisor Pierre Fraigniaud. For a finite simple graph G, I(S) contains S and all vertices on shortest paths between vertices of S. H(S) is obtained by iterating I to a fixed point. Starting with S empty, Alice and Bob alternate adding one vertex outside I(S) in the closed interval game, or outside H(S) in the closed hull game, until none remains. Alice starts.

**Source.** Samuel N. Araújo, Fabrício Benevides, Nicolas Martins, Nicolas Nisse and Rudini Sampaio. *The Closed Hull Game and the Closed Interval Game*. 2026. [primary source](https://doi.org/10.4230/LIPIcs.FUN.2026.4) Location: pp.4:2,4:10–11.

**Literature check.** Status: No later resolution found through 10 October 2026.


<a id="q4033"></a>

## Q4033. For every finite L⊂{1,2,…}, connected graph G and vertex u, append n new path vertices to u by…

**Status:** Open · **Kind:** open problem (Question 5.6) · **Collection** 41

For every finite L⊂{1,2,…}, connected graph G and vertex u, append n new path vertices to u by one edge and call the resulting graph G_n. Must there exist integers p≥1, d≥0 and N≥0 such that g_A(G_(n+p))=g_A(G_n)+d for every n≥N, where A={1,2,…}∖L?

**Context.** For a set A of positive integers, CSG(A) is normal play on finite connected simple graphs: delete a nonempty vertex set inducing a connected subgraph, of size in A, leaving a connected graph or the empty graph. Its Grundy value g_A is the least nonnegative integer absent among values of legal followers; a terminal position has value zero. Origin: Q4033 is thesis-stated. Q4034 weakens the earlier Beaudou–Coupechoux–Dailly–Gravier–Moncel–Parreau–Sopena tree-realization conjecture.

**Source.** Antoine Dailly. *Criticalité, identification et jeux de suppression de sommets dans les graphes: Des étoiles plein les jeux*. Université de Lyon, 2018. Advisor(s): Hamamache Kheddouci; co-directors Éric Duchêne and Aline Parreau. [primary source](https://daillya.github.io/Manuscrit.pdf) Location: Question 5.6, p.105; Conjecture 5.32, p.136.

**Literature check.** Status: No later resolution found through 10 October 2026.

**Further links.** [1](https://math.colgate.edu/~integers/tg3/tg3.pdf)


<a id="q4034"></a>

## Q4034. Are the values g_{1,2}(T) unbounded over finite trees T?

**Status:** Open · **Kind:** open problem (Question 5.6) · **Collection** 41

Are the values g_{1,2}(T) unbounded over finite trees T?

**Context.** For a set A of positive integers, CSG(A) is normal play on finite connected simple graphs: delete a nonempty vertex set inducing a connected subgraph, of size in A, leaving a connected graph or the empty graph. Its Grundy value g_A is the least nonnegative integer absent among values of legal followers; a terminal position has value zero. Origin: Q4033 is thesis-stated. Q4034 weakens the earlier Beaudou–Coupechoux–Dailly–Gravier–Moncel–Parreau–Sopena tree-realization conjecture.

**Source.** Antoine Dailly. *Criticalité, identification et jeux de suppression de sommets dans les graphes: Des étoiles plein les jeux*. Université de Lyon, 2018. Advisor(s): Hamamache Kheddouci; co-directors Éric Duchêne and Aline Parreau. [primary source](https://daillya.github.io/Manuscrit.pdf) Location: Question 5.6, p.105; Conjecture 5.32, p.136.

**Literature check.** Status: No later resolution found through 10 October 2026.

**Further links.** [1](https://math.colgate.edu/~integers/tg3/tg3.pdf)


<a id="q4035"></a>

## Q4035. Determine the complexity of deciding γ≤k when the input is a cograph G, a positive integer k,…

**Status:** Open · **Kind:** open problem · **Collection** 41

Determine the complexity of deciding γ≤k when the input is a cograph G, a positive integer k, and the starting player; cographs have no induced four-vertex path.

**Context.** Initially all vertices of a finite simple graph are unclaimed. Dominator and Staller alternately claim one unclaimed vertex, starting with the specified player. Dominator wins once her vertices form a dominating set, meaning every vertex belongs to that set or has a neighbor in it. Otherwise Staller wins. Let γ be the least number of Dominator’s own moves in which she can force a win, or infinity if she cannot.

**Source.** Valentin Gledel, Vesna Iršič and Sandi Klavžar. *Maker-Breaker domination number*. 2019. [primary source](https://arxiv.org/abs/1810.04397) Location: §7(4), p.19; restated in Gledel’s thesis, p.70, and Oijid’s thesis, p.102

**Literature check.** Status: No later resolution found through 10 October 2026.

**Further links.** [1](https://doi.org/10.1007/s40840-019-00757-1)


<a id="q4036"></a>

## Q4036. Find an explicit formula for sg(Q_n) for every integer n≥1.

**Status:** Open · **Kind:** open problem · **Collection** 41

Find an explicit formula for sg(Q_n) for every integer n≥1.

**Context.** A strong geodetic set S in a connected graph permits choosing one shortest path for every unordered pair of distinct vertices of S so that the union of those paths covers every vertex. The strong geodetic number sg(G) is the smallest possible |S|. The hypercube Q_n has vertex set {0,1}^n, with adjacency when exactly one coordinate differs. Origin: Older joint-paper question, reaffirmed by the thesis after the journal version appeared.

**Source.** Valentin Gledel. *Couverture de sommets sous contraintes*. Université de Lyon, 2019. Advisor(s): Éric Duchêne and Aline Parreau. [primary source](https://vgledel.github.io/pdf/these/manuscrit.pdf) Location: thesis Chapter 4, §7, p.92; earlier joint question with Vesna Iršič in Strong geodetic number of complete bipartite graphs, crown graphs and hypercubes, concluding paragraph, arXiv:1810.04004v1, p.11.

**Literature check.** Status: No later resolution found through 10 October 2026.

**Further links.** [1](https://doi.org/10.1007/s40840-019-00833-6)


<a id="q4137"></a>

## Q4137. Does a K₂-hypohamiltonian graph of girth at most four exist?

**Status:** Open · **Kind:** open problem · **Collection** 42

Does a K₂-hypohamiltonian graph of girth at most four exist?

**Context.** Graphs are finite, simple and connected. A Hamiltonian cycle visits every vertex exactly once. A graph is K₂-hypohamiltonian if it has no Hamiltonian cycle but deleting the endpoints of any edge leaves a graph with one. Girth is the length of a shortest cycle. Origin: Older question, restated by Jan Goedgebeur, Jarne Renders, Gábor Wiener and Carol T. Zamfirescu in K₂-Hamiltonian Graphs: II; reaffirmed here. No matching resolution found through 10 October 2026. The high-girth and bipartite existence problems are different questions.

**Source.** Jarne Renders. *Studying Cycles with Computational Graph Theory*. KU Leuven, 2025. Advisor(s): Jan Goedgebeur and Carol T. Zamfirescu. [primary source](https://www.st.fmph.uniba.sk/~lukac133/thesis_Jarne_Renders.pdf) Location: Thesis §8.1, p.175.

**Literature check.** Status: Origin: Older question, restated by Jan Goedgebeur, Jarne Renders, Gábor Wiener and Carol T. Zamfirescu in K₂-Hamiltonian Graphs: II; reaffirmed here. No matching resolution found through 10 October 2026. The high-girth and bipartite existence problems are different questions.


<a id="q4138"></a>

## Q4138. If G is cyclically 4-edge-connected and is not isomorphic to the Petersen graph, must fn(G)≤2?

**Status:** Open · **Kind:** conjecture (Conjecture 1) · **Collection** 42

If G is cyclically 4-edge-connected and is not isomorphic to the Petersen graph, must fn(G)≤2?

**Context.** Graphs are finite, simple and 3-edge-connected. The Frank number fn(G) is the minimum number of orientations such that, for each edge e, deleting its oriented arc leaves a strongly connected digraph in at least one orientation. Strong connectivity requires directed paths between every ordered pair of vertices. Cyclic 4-edge-connectivity means deleting fewer than four edges cannot separate two components each containing a cycle.

**Source.** Jan Goedgebeur, Edita Máčajová and Jarne Renders. *The Frank number and nowhere-zero flows on graphs*. 2025. [primary source](https://arxiv.org/abs/2305.02133v4) Location: §1, Conjecture 1, p.2 (accepted manuscript arXiv:2305.02133v4); also thesis Conjecture 4.3

**Literature check.** Status: Origin: Joint paper conjecture, also thesis Conjecture 4.3. The institutional repository identifies v4 as the accepted manuscript for this final article; no substantive difference or later resolution found through 10 October 2026.

**Further links.** [1](https://biblio.ugent.be/publication/01JX2G236QPBTH9Q9NMWKB4GVT)


<a id="q4139"></a>

## Q4139. Does every 4-connected planar graph have a HIST?

**Status:** Open · **Kind:** open problem · **Collection** 42

Does every 4-connected planar graph have a HIST?

**Context.** Graphs are finite and simple. A HIST is a spanning tree with no vertex of degree two. A HIST-critical graph has no HIST, while deleting any vertex produces a graph having a HIST. Origin: Q4139 restates Malkevitch’s 1979 conjecture; Q4140 restates Albertson–Berman–Hutchinson–Thomassen’s question; Q4141–Q4142 are joint-paper residuals, incorporated in Renders’s thesis. No newer version, final publication or matching resolution found through 10 October 2026. The line-graph theorem settles only a subclass of Q4139.

**Source.** Jan Goedgebeur, Kenta Noguchi, Jarne Renders and Carol T. Zamfirescu. *HIST-Critical Graphs and Malkevitch’s Conjecture*. 2025. [primary source](https://arxiv.org/abs/2401.04554v2) Location: §§3.4,4,4.2, pp.9–10.

**Literature check.** Status: Origin: Q4139 restates Malkevitch’s 1979 conjecture; Q4140 restates Albertson–Berman–Hutchinson–Thomassen’s question; Q4141–Q4142 are joint-paper residuals, incorporated in Renders’s thesis. No newer version, final publication or matching resolution found through 10 October 2026. The line-graph theorem settles only a subclass of Q4139.


<a id="q4140"></a>

## Q4140. Is there a connected 6-regular graph without a HIST?

**Status:** Open · **Kind:** open problem · **Collection** 42

Is there a connected 6-regular graph without a HIST?

**Context.** Graphs are finite and simple. A HIST is a spanning tree with no vertex of degree two. A HIST-critical graph has no HIST, while deleting any vertex produces a graph having a HIST. Origin: Q4139 restates Malkevitch’s 1979 conjecture; Q4140 restates Albertson–Berman–Hutchinson–Thomassen’s question; Q4141–Q4142 are joint-paper residuals, incorporated in Renders’s thesis. No newer version, final publication or matching resolution found through 10 October 2026. The line-graph theorem settles only a subclass of Q4139.

**Source.** Jan Goedgebeur, Kenta Noguchi, Jarne Renders and Carol T. Zamfirescu. *HIST-Critical Graphs and Malkevitch’s Conjecture*. 2025. [primary source](https://arxiv.org/abs/2401.04554v2) Location: §§3.4,4,4.2, pp.9–10.

**Literature check.** Status: Origin: Q4139 restates Malkevitch’s 1979 conjecture; Q4140 restates Albertson–Berman–Hutchinson–Thomassen’s question; Q4141–Q4142 are joint-paper residuals, incorporated in Renders’s thesis. No newer version, final publication or matching resolution found through 10 October 2026. The line-graph theorem settles only a subclass of Q4139.


<a id="q4141"></a>

## Q4141. For which integers k≥4 does a k-regular HIST-critical graph exist?

**Status:** Open · **Kind:** open problem · **Collection** 42

For which integers k≥4 does a k-regular HIST-critical graph exist?

**Context.** Graphs are finite and simple. A HIST is a spanning tree with no vertex of degree two. A HIST-critical graph has no HIST, while deleting any vertex produces a graph having a HIST. Origin: Q4139 restates Malkevitch’s 1979 conjecture; Q4140 restates Albertson–Berman–Hutchinson–Thomassen’s question; Q4141–Q4142 are joint-paper residuals, incorporated in Renders’s thesis. No newer version, final publication or matching resolution found through 10 October 2026. The line-graph theorem settles only a subclass of Q4139.

**Source.** Jan Goedgebeur, Kenta Noguchi, Jarne Renders and Carol T. Zamfirescu. *HIST-Critical Graphs and Malkevitch’s Conjecture*. 2025. [primary source](https://arxiv.org/abs/2401.04554v2) Location: §§3.4,4,4.2, pp.9–10.

**Literature check.** Status: Origin: Q4139 restates Malkevitch’s 1979 conjecture; Q4140 restates Albertson–Berman–Hutchinson–Thomassen’s question; Q4141–Q4142 are joint-paper residuals, incorporated in Renders’s thesis. No newer version, final publication or matching resolution found through 10 October 2026. The line-graph theorem settles only a subclass of Q4139.


<a id="q4142"></a>

## Q4142. For which n∈{26,30,34,38,45,48,52} does an n-vertex HIST-critical graph exist?

**Status:** Open · **Kind:** open problem · **Collection** 42

For which n∈{26,30,34,38,45,48,52} does an n-vertex HIST-critical graph exist?

**Context.** Graphs are finite and simple. A HIST is a spanning tree with no vertex of degree two. A HIST-critical graph has no HIST, while deleting any vertex produces a graph having a HIST. Origin: Q4139 restates Malkevitch’s 1979 conjecture; Q4140 restates Albertson–Berman–Hutchinson–Thomassen’s question; Q4141–Q4142 are joint-paper residuals, incorporated in Renders’s thesis. No newer version, final publication or matching resolution found through 10 October 2026. The line-graph theorem settles only a subclass of Q4139.

**Source.** Jan Goedgebeur, Kenta Noguchi, Jarne Renders and Carol T. Zamfirescu. *HIST-Critical Graphs and Malkevitch’s Conjecture*. 2025. [primary source](https://arxiv.org/abs/2401.04554v2) Location: §§3.4,4,4.2, pp.9–10.

**Literature check.** Status: Origin: Q4139 restates Malkevitch’s 1979 conjecture; Q4140 restates Albertson–Berman–Hutchinson–Thomassen’s question; Q4141–Q4142 are joint-paper residuals, incorporated in Renders’s thesis. No newer version, final publication or matching resolution found through 10 October 2026. The line-graph theorem settles only a subclass of Q4139.


<a id="q4143"></a>

## Q4143. For every planar G, is χ\_i(G) at most 5 when Δ≤3, Δ+5 when 4≤Δ≤7, and ⌊3Δ/2⌋+1 when Δ≥8?

**Status:** Open · **Kind:** conjecture (Conjecture 1.2) · **Collection** 42

For every planar G, is χ\_i(G) at most 5 when Δ≤3, Δ+5 when 4≤Δ≤7, and ⌊3Δ/2⌋+1 when Δ≥8?

**Context.** For a finite simple undirected graph G, χ\_i(G) is the fewest vertex colours needed when distinct vertices sharing a neighbour must have different colours. Write Δ for maximum degree and g for girth. Origin: Earlier conjectures of Lužar–Škrekovski and La–Štorgel, respectively, explicitly retained here. No matching resolution found through 10 October 2026.

**Source.** Matias Daneels, Jan Goedgebeur and Jarne Renders. *Infinite families of planar graphs of a given injective chromatic number*. 2025. [primary source](https://amc-journal.eu/index.php/amc/article/download/3514/2225) Location: Conjecture 1.2, p.2; Conjecture 4.1, p.12.

**Literature check.** Status: Origin: Earlier conjectures of Lužar–Škrekovski and La–Štorgel, respectively, explicitly retained here. No matching resolution found through 10 October 2026.


<a id="q4144"></a>

## Q4144. For every planar G with g≥4 and Δ≥3, is χ\_i(G)≤⌊3Δ/2⌋?

**Status:** Open · **Kind:** conjecture (Conjecture 1.2) · **Collection** 42

For every planar G with g≥4 and Δ≥3, is χ\_i(G)≤⌊3Δ/2⌋?

**Context.** For a finite simple undirected graph G, χ\_i(G) is the fewest vertex colours needed when distinct vertices sharing a neighbour must have different colours. Write Δ for maximum degree and g for girth. Origin: Earlier conjectures of Lužar–Škrekovski and La–Štorgel, respectively, explicitly retained here. No matching resolution found through 10 October 2026.

**Source.** Matias Daneels, Jan Goedgebeur and Jarne Renders. *Infinite families of planar graphs of a given injective chromatic number*. 2025. [primary source](https://amc-journal.eu/index.php/amc/article/download/3514/2225) Location: Conjecture 1.2, p.2; Conjecture 4.1, p.12.

**Literature check.** Status: Origin: Earlier conjectures of Lužar–Škrekovski and La–Štorgel, respectively, explicitly retained here. No matching resolution found through 10 October 2026.


<a id="q4145"></a>

## Q4145. For every d-regular Moore graph M of order m, is c_d(n)&lt;c_d(m)=c(M) for every admissible n>m?

**Status:** Open · **Kind:** conjecture (Conjecture 2) · **Collection** 42

For every d-regular Moore graph M of order m, is c_d(n)&lt;c_d(m)=c(M) for every admissible n>m?

**Context.** For finite simple G, let N(G) count nonempty vertex sets inducing connected subgraphs and c(G)=N(G)^(1/|V(G)|). For integer d≥2, let c_d(n) maximize c(G) over d-regular n-vertex graphs, and c_d=limsup c_d(n) over orders admitting such graphs. A d-regular graph of girth g is Moore if its order equals 1+d∑\_{i=0}^{r−1}(d−1)^i for g=2r+1, or 2∑\_{i=0}^{r−1}(d−1)^i for g=2r. Origin: Joint-paper conjecture and concluding question. No matching resolution or relevant erratum found through 10 October 2026.

**Source.** Stijn Cambie, Jan Goedgebeur and Jorik Jooken. *The maximum number of connected sets in regular graphs*. 2025. [primary source](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v32i1p20/pdf/) Location: Conjecture 2, p.3; §6, p.17; definitions p.2.

**Literature check.** Status: Origin: Joint-paper conjecture and concluding question. No matching resolution or relevant erratum found through 10 October 2026.


<a id="q4146"></a>

## Q4146. As integer d→∞, is 2−c_d=Θ(2^(−d))?

**Status:** Open · **Kind:** conjecture (Conjecture 2) · **Collection** 42

As integer d→∞, is 2−c_d=Θ(2^(−d))?

**Context.** For finite simple G, let N(G) count nonempty vertex sets inducing connected subgraphs and c(G)=N(G)^(1/|V(G)|). For integer d≥2, let c_d(n) maximize c(G) over d-regular n-vertex graphs, and c_d=limsup c_d(n) over orders admitting such graphs. A d-regular graph of girth g is Moore if its order equals 1+d∑\_{i=0}^{r−1}(d−1)^i for g=2r+1, or 2∑\_{i=0}^{r−1}(d−1)^i for g=2r. Origin: Joint-paper conjecture and concluding question. No matching resolution or relevant erratum found through 10 October 2026.

**Source.** Stijn Cambie, Jan Goedgebeur and Jorik Jooken. *The maximum number of connected sets in regular graphs*. 2025. [primary source](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v32i1p20/pdf/) Location: Conjecture 2, p.3; §6, p.17; definitions p.2.

**Literature check.** Status: Origin: Joint-paper conjecture and concluding question. No matching resolution or relevant erratum found through 10 October 2026.


<a id="q4147"></a>

## Q4147. If g is even and d≤g, must every (k;g,d)-cage be bipartite?

**Status:** Open · **Kind:** open problem (Question 1) · **Collection** 42

If g is even and d≤g, must every (k;g,d)-cage be bipartite?

**Context.** Graphs are finite, simple, undirected and connected. For integers k≥2, g≥3 and d≥1, a (k;g,d)-cage is a k-regular graph having girth exactly g and diameter exactly d, with the fewest vertices among graphs satisfying all three conditions, whenever any exist. Girth is shortest-cycle length; diameter is greatest vertex distance. Origin: Joint-paper question, stronger than the classical even-girth cage conjecture. No later matching resolution found through 10 October 2026.

**Source.** Stijn Cambie, Jan Goedgebeur, Jorik Jooken and Tibo Van den Eede. *On the order-diameter ratio of girth-diameter cages*. 2026. [primary source](https://dmtcs.episciences.org/en/articles/17595/download) Location: §5, Question 1, p.16.

**Literature check.** Status: Origin: Joint-paper question, stronger than the classical even-girth cage conjecture. No later matching resolution found through 10 October 2026.


<a id="q4195"></a>

## Q4195. For each integer d≥2, determine max(S_F(d)∩{q∈Q:q&lt;d−1}), the next endpoint below d−1 in the Fine…

**Status:** Open · **Kind:** open problem (Question 3.7.11) · **Collection** 42

For each integer d≥2, determine max(S_F(d)∩{q∈Q:q&lt;d−1}), the next endpoint below d−1 in the Fine Q-codegree spectrum.

**Context.** For a full-dimensional lattice polytope P⊂Rᵈ, put h_P(a)=min_{x∈P}⟨a,x⟩ and P^F(s)={x:⟨a,x⟩≥h_P(a)+s for every nonzero integral covector a}. Define μ\_F(P)=1/sup{s>0:P^F(s)≠∅}, and let S_F(d) be the set of these values over all such P.

**Source.** Sofía Garzón Mora. *Fine Polyhedral Adjunction, Weighted Ehrhart Theory, and Tensor Network Varieties: A Combinatorial View*. Freie Universität Berlin, 2025. Advisor(s): Christian Haase. [primary source](https://doi.org/10.17169/refubium-51064) Location: Question 3.7.11, p. 55.

**Literature check.** Status checked 10 October 2026: Current v1 retains the question. Its classification of the top values and low-dimensional results do not determine this endpoint in every dimension. No later resolution was found.

**Further links.** [1](https://arxiv.org/abs/2601.03145v1)


<a id="q4236"></a>

## Q4236. Does every element of L have a unique factorisation into atoms, up to permutation?

**Status:** Open · **Kind:** open problem · **Collection** 43

Does every element of L have a unique factorisation into atoms, up to permutation?

**Context.** Games are short partizan games under misère play: a player unable to move wins. The disjunctive sum permits moving in one component. Two games are equal when adding any short game gives identical outcomes for either starting player. Let L be the monoid of Left dead ends: games having no Left option at any subposition, modulo this equality. An atom is a nonzero element not expressible as a sum of two nonzero elements; a molecule is a nonzero sum of atoms that is not an atom. T(G) is the set of lengths of option-tree paths from G to the empty game, without alternating-player restrictions. Origin and locations: Open Problems 8.1–8.2, pp.39–41; definitions pp.5–9,14. Version: 26 September 2024, v1. No matching resolution located through 10 October 2026.

**Source.** Alfie Davies. *On factorisations of Left dead ends*. 2024. [primary source](https://arxiv.org/abs/2409.17871v1) Location: Open Problems 8.1–8.2, pp.39–41; definitions pp.5–9,14.

**Literature check.** Status: Origin and locations: Open Problems 8.1–8.2, pp.39–41; definitions pp.5–9,14. Version: 26 September 2024, v1. No matching resolution located through 10 October 2026.


<a id="q4237"></a>

## Q4237. For each finite S⊆{1,2,...}, how many atoms and molecules G∈L have T(G)=S?

**Status:** Open · **Kind:** open problem · **Collection** 43

For each finite S⊆{1,2,...}, how many atoms and molecules G∈L have T(G)=S?

**Context.** Games are short partizan games under misère play: a player unable to move wins. The disjunctive sum permits moving in one component. Two games are equal when adding any short game gives identical outcomes for either starting player. Let L be the monoid of Left dead ends: games having no Left option at any subposition, modulo this equality. An atom is a nonzero element not expressible as a sum of two nonzero elements; a molecule is a nonzero sum of atoms that is not an atom. T(G) is the set of lengths of option-tree paths from G to the empty game, without alternating-player restrictions. Origin and locations: Open Problems 8.1–8.2, pp.39–41; definitions pp.5–9,14. Version: 26 September 2024, v1. No matching resolution located through 10 October 2026.

**Source.** Alfie Davies. *On factorisations of Left dead ends*. 2024. [primary source](https://arxiv.org/abs/2409.17871v1) Location: Open Problems 8.1–8.2, pp.39–41; definitions pp.5–9,14.

**Literature check.** Status: Origin and locations: Open Problems 8.1–8.2, pp.39–41; definitions pp.5–9,14. Version: 26 September 2024, v1. No matching resolution located through 10 October 2026.


<a id="q4238"></a>

## Q4238. For all G,H,J∈B, does G+J≥B H+J imply G≥B H?

**Status:** Open · **Kind:** open problem (Problem 5.3) · **Collection** 43

For all G,H,J∈B, does G+J≥B H+J imply G≥B H?

**Context.** Consider short partizan games under misère play, where inability to move wins; G+H permits a move in one component. A Left end has no Left options. Recursively, it is blocked if every Right option is either a blocked Left end or has a Left option to one; blocked Right ends are defined symmetrically. Let B consist of games whose subpositions that are ends are all blocked. Write G≥B H when, for every X∈B and either starting player, Left winning H+X implies Left winning G+X. Origin and location: Problem 5.3, p.24, following the authors' 2024 pocancellation work. The stronger comparison using every short game as a test is distinguished in the paper. Published 20 April 2026 final read; no matching later resolution located through 10 October 2026.

**Source.** Alfie Davies and Rebecca Milley. *Order and inverses in the monoid of misère blocking games*. 2026. [primary source](https://doi.org/10.5070/C66165692) Location: Problem 5.3, p.24, following the authors' 2024 pocancellation work.

**Literature check.** Status: Origin and location: Problem 5.3, p.24, following the authors' 2024 pocancellation work. The stronger comparison using every short game as a test is distinguished in the paper. Published 20 April 2026 final read; no matching later resolution located through 10 October 2026.


<a id="q4239"></a>

## Q4239. Can U× be nontrivial while U contains no U-invertible form of formal birthday 1?

**Status:** Open · **Kind:** open problem · **Collection** 43

Can U× be nontrivial while U contains no U-invertible form of formal birthday 1?

**Context.** Games are short partizan forms under misère play: inability to move wins. Addition means moving in one component. A universe U is a nonempty set closed under addition, exchanging players, options, and forming {A|B} for finite nonempty A,B⊆U. Write G≡U H if G+X and H+X have identical outcomes for either starting player for every X∈U. Let U× be the group of classes represented by G∈U admitting H∈U with G+H≡U0. Formal birthday is the height of the option tree. Origin and locations: Open Problems 22, p.13, and 46, p.22 (2024 preprint; 3 October 2025 final read). Problem 46 is reiterated in Davies–Milley (2026), Problem 5.4. No matching resolution located through 10 October 2026.

**Source.** Alfie Davies and Vishal Yadav. *Invertibility in the misère multiverse*. 2025. [primary source](https://doi.org/10.37236/13504) Location: Open Problems 22, p.13, and 46, p.22 (2024 preprint; 3 October 2025 final read).

**Literature check.** Status: Origin and locations: Open Problems 22, p.13, and 46, p.22 (2024 preprint; 3 October 2025 final read). Problem 46 is reiterated in Davies–Milley (2026), Problem 5.4. No matching resolution located through 10 October 2026.

**Further links.** [1](https://doi.org/10.5070/C66165692)


<a id="q4240"></a>

## Q4240. Determine the group structure of U× for each universe U.

**Status:** Open · **Kind:** open problem · **Collection** 43

Determine the group structure of U× for each universe U.

**Context.** Games are short partizan forms under misère play: inability to move wins. Addition means moving in one component. A universe U is a nonempty set closed under addition, exchanging players, options, and forming {A|B} for finite nonempty A,B⊆U. Write G≡U H if G+X and H+X have identical outcomes for either starting player for every X∈U. Let U× be the group of classes represented by G∈U admitting H∈U with G+H≡U0. Formal birthday is the height of the option tree. Origin and locations: Open Problems 22, p.13, and 46, p.22 (2024 preprint; 3 October 2025 final read). Problem 46 is reiterated in Davies–Milley (2026), Problem 5.4. No matching resolution located through 10 October 2026.

**Source.** Alfie Davies and Vishal Yadav. *Invertibility in the misère multiverse*. 2025. [primary source](https://doi.org/10.37236/13504) Location: Open Problems 22, p.13, and 46, p.22 (2024 preprint; 3 October 2025 final read).

**Literature check.** Status: Origin and locations: Open Problems 22, p.13, and 46, p.22 (2024 preprint; 3 October 2025 final read). Problem 46 is reiterated in Davies–Milley (2026), Problem 5.4. No matching resolution located through 10 October 2026.

**Further links.** [1](https://doi.org/10.5070/C66165692)


<a id="q4241"></a>

## Q4241. For which n can S_n\A_n be partitioned as M⊔N, where M and N are unions of entire S_n-conjugacy…

**Status:** Open · **Kind:** open problem · **Collection** 43

For which n can S_n\A_n be partitioned as M⊔N, where M and N are unions of entire S_n-conjugacy classes and |M|=|N|?

**Context.** For n≥3, let S_n be the symmetric group and A_n its subgroup of even permutations. Origin and location: thesis §3.4, p.34, following Corollary 3.4.2. The cardinalities count permutations, not the number of conjugacy classes. The source reports checks through n=10. Repository version deposited 24 September 2024; no matching resolution located through 10 October 2026.

**Source.** Mariia Sobchuk. *Algebraic Approach to Quantum Isomorphisms*. University of Waterloo, 2024. Advisor(s): Chris Godsil. [primary source](https://hdl.handle.net/10012/21079) Location: thesis §3.4, p.34, following Corollary 3.4.2.

**Literature check.** Status: Origin and location: thesis §3.4, p.34, following Corollary 3.4.2. The cardinalities count permutations, not the number of conjugacy classes. The source reports checks through n=10. Repository version deposited 24 September 2024; no matching resolution located through 10 October 2026.


<a id="q4242"></a>

## Q4242. Which 2n×2m Queen graphs are almost opposable, for positive integers n,m?

**Status:** Open · **Kind:** open problem · **Collection** 43

Which 2n×2m Queen graphs are almost opposable, for positive integers n,m?

**Context.** A finite simple graph G is opposable if it has an automorphism f of order two with f(v)∉N[v] for every vertex. It is almost opposable if G−S is opposable for some vertex u and u∈S⊆N[u]; N[u] is the closed neighborhood. The a×b Queen graph has board squares as vertices, adjacent when distinct squares share a row, column or diagonal. In Snort, players alternate coloring uncolored vertices in their own colors, never adjacent to the opponent's color; inability to move loses. Initially all vertices are uncolored. Origin and locations: Open Problems 2–3, p.25 (2025 preprint; 26 June 2026 published final read). No matching later resolution located through 10 October 2026.

**Source.** Rylo Ashmore, Beth Ann Austin, Alfie M. Davies, Danny Dyer and William Kellough. *On graph automorphisms related to Snort*. 2026. [primary source](https://math.colgate.edu/~integers/aag2/aag2.pdf) Location: Open Problems 2–3, p.25 (2025 preprint; 26 June 2026 published final read).

**Literature check.** Status: Origin and locations: Open Problems 2–3, p.25 (2025 preprint; 26 June 2026 published final read). No matching later resolution located through 10 October 2026.


<a id="q4243"></a>

## Q4243. Can the second player win Snort on any 2n×2m Queen graph, for positive integers n,m?

**Status:** Open · **Kind:** open problem · **Collection** 43

Can the second player win Snort on any 2n×2m Queen graph, for positive integers n,m?

**Context.** A finite simple graph G is opposable if it has an automorphism f of order two with f(v)∉N[v] for every vertex. It is almost opposable if G−S is opposable for some vertex u and u∈S⊆N[u]; N[u] is the closed neighborhood. The a×b Queen graph has board squares as vertices, adjacent when distinct squares share a row, column or diagonal. In Snort, players alternate coloring uncolored vertices in their own colors, never adjacent to the opponent's color; inability to move loses. Initially all vertices are uncolored. Origin and locations: Open Problems 2–3, p.25 (2025 preprint; 26 June 2026 published final read). No matching later resolution located through 10 October 2026.

**Source.** Rylo Ashmore, Beth Ann Austin, Alfie M. Davies, Danny Dyer and William Kellough. *On graph automorphisms related to Snort*. 2026. [primary source](https://math.colgate.edu/~integers/aag2/aag2.pdf) Location: Open Problems 2–3, p.25 (2025 preprint; 26 June 2026 published final read).

**Literature check.** Status: Origin and locations: Open Problems 2–3, p.25 (2025 preprint; 26 June 2026 published final read). No matching later resolution located through 10 October 2026.


<a id="q4245"></a>

## Q4245. For each integer k≥4, find a structural characterization of the graphs with cat number k.

**Status:** Open · **Kind:** open problem · **Collection** 43

For each integer k≥4, find a structural characterization of the graphs with cat number k.

**Context.** On a finite connected simple graph, the cat chooses its initial vertex. Turns then alternate, starting with the herder deleting any one edge; the cat must move along a nontrivial path to a different vertex in the remaining graph. Play ends when the cat is isolated. The score counts deleted edges. The herder minimizes this score and the cat maximizes it; their optimal value is the graph's cat number. Origin and location: §6, p.20. Version: arXiv v1, submitted 12 May 2025 (PDF dated 11 June 2025). No matching resolution located through 10 October 2026; the later infinite-tree paper addresses a different scope.

**Source.** Rylo Ashmore, Danny Dyer and Rebecca Milley. *Extremal Cat Herding*. 2025. [primary source](https://arxiv.org/abs/2505.07588v1) Location: §6, p.20.

**Literature check.** Status: Origin and location: §6, p.20. Version: arXiv v1, submitted 12 May 2025 (PDF dated 11 June 2025). No matching resolution located through 10 October 2026; the later infinite-tree paper addresses a different scope.

**Further links.** [1](https://doi.org/10.4230/LIPIcs.FSTTCS.2025.10)


<a id="q4246"></a>

## Q4246. Determine the additive quotient monoid U/≡ together with its four outcome classes (Left always…

**Status:** Open · **Kind:** open problem · **Collection** 43

Determine the additive quotient monoid U/≡ together with its four outcome classes (Left always wins, Right always wins, first player wins, second player wins).

**Context.** Use finite partizan game forms under misère play: a player unable to move wins. A dicot has, at every reachable position, either options for both players or none. Let U be the closure under finite disjunctive sums and followers of all dicot forms whose game trees have height at most two. A sum move changes exactly one component. Put G≡H when G+X and H+X have the same winner for each starting player for every X∈U. Origin and location: thesis §6, p.107; definitions §2.1, pp.8–9; related partial computations §4.3. March 2013 thesis. Later individual-form classifications do not give this arbitrary-sum monoid; no matching resolution located through 10 October 2026.

**Source.** Rebecca Milley. *Restricted Universes of Partizan Misère Games*. Dalhousie University, 2013. Advisor(s): Richard Nowakowski. [primary source](https://hdl.handle.net/10222/21441) Location: thesis §6, p.107; definitions §2.1, pp.8–9; related partial computations §4.3.

**Literature check.** Status: Origin and location: thesis §6, p.107; definitions §2.1, pp.8–9; related partial computations §4.3. March 2013 thesis. Later individual-form classifications do not give this arbitrary-sum monoid; no matching resolution located through 10 October 2026.


<a id="q4247"></a>

## Q4247. Is QP(A) a polytope for every finite simple graph?

**Status:** Open · **Kind:** open problem · **Collection** 43

Is QP(A) a polytope for every finite simple graph?

**Context.** For a finite simple graph with adjacency matrix A of order n, let C(A) be the universal unital C\*-algebra generated by projections uᵢⱼ satisfying ∑ᵢuᵢⱼ=∑ᵢuⱼᵢ=1 and uA=Au. Define QP(A)={ (ρ(uᵢⱼ))ᵢⱼ : ρ is a positive unital linear functional on C(A) }. Origin and location: §5, first open question, p.19; definitions 1–2, pp.2,5. Version: arXiv v1, 11 June 2026. The earlier 2025 proceedings note introduces quantum compactness but does not pose this question. No matching resolution located through 10 October 2026.

**Source.** Pedro Baptista, Gabriel Coutinho, Chris Godsil and Simon Schmidt. *Compact graphs and quantum automorphisms*. 2026. [primary source](https://arxiv.org/abs/2606.13928v1) Location: §5, first open question, p.19; definitions 1–2, pp.2,5.

**Literature check.** Status: Origin and location: §5, first open question, p.19; definitions 1–2, pp.2,5. Version: arXiv v1, 11 June 2026. The earlier 2025 proceedings note introduces quantum compactness but does not pose this question. No matching resolution located through 10 October 2026.


<a id="q4250"></a>

## Q4250. Is every minimal obstruction to S_a an induced subgraph of some minimal obstruction to N_a, for…

**Status:** Open · **Kind:** conjecture (Conjecture 3.17) · **Collection** 43

Is every minimal obstruction to S_a an induced subgraph of some minimal obstruction to N_a, for every a≥1?

**Source.** Rebecca Whitman. *Hereditary Subclasses and Closures of Invariant-Defined Graph Classes*. University of California, Berkeley, 2026. Advisor(s): Thomas Scanlon and Vaidyanathan Sivaraman. [primary source](https://escholarship.org/uc/item/9sg796rf) Location: thesis Conjecture 3.17, p.71; definitions pp.45–46,70.

**Literature check.** Status: Origin: thesis Conjecture 3.17, p.71; definitions pp.45–46,70. Primary: https://escholarship.org/uc/item/9sg796rf . The generalized paper remains listed in preparation; no matching resolution located by 10 October 2026.


<a id="q4251"></a>

## Q4251. For each d≥3, can all coordinate 2-colorings exist while no Borel 2^d-polychromatic coloring exists?

**Status:** Open · **Kind:** open problem (Question 5.3) · **Collection** 43

For each d≥3, can all coordinate 2-colorings exist while no Borel 2^d-polychromatic coloring exists?

**Source.** Katalin Berlow and Edward Hou. *Borel Polychromatic Number of Grids*. 2025. [primary source](https://arxiv.org/abs/2508.18559) Location: Open Question 5.3, p.12; definitions pp.1–2,9.

**Literature check.** Status: Origin: Open Question 5.3, p.12; definitions pp.1–2,9. Primary: https://arxiv.org/abs/2508.18559 (v1, 25 August 2025). No later version or matching resolution located by 10 October 2026.


<a id="q4257"></a>

## Q4257. If χB is finite, must χB≤2n+1?

**Status:** Open · **Kind:** open problem (Question 1.7) · **Collection** 43

If χB is finite, must χB≤2n+1?

**Context.** Thesis: https://escholarship.org/uc/item/1075v66x , Question 1.7, p.4. Origin: attributed there to Kechris–Solecki–Todorcevic (1999), Question 4.9; Kechris–Marks’s survey, Problem 5.8, identifies that predecessor as slightly restricted. Current exact reaffirmation: Bernshteyn–Hou–Shinko–Weilacher, Randomized Borel (2d+1)-Coloring of Digraphs, https://arxiv.org/abs/2609.21286 , Question 4, p.1. Pelayo Gómez’s https://arxiv.org/abs/2609.19038 , Remark 4, p.2, explicitly leaves the Borel question open. Checked 10 October 2026.

**Source.** Konstantinos Palamourdas. *1,2,3,...,2n+1,∞!*. University of California, Los Angeles, 2012. Advisor(s): Itay Neeman. [primary source](https://escholarship.org/uc/item/1075v66x) Location: Question 1.7, p.4.

**Literature check.** Status: Thesis: https://escholarship.org/uc/item/1075v66x , Question 1.7, p.4. Origin: attributed there to Kechris–Solecki–Todorcevic (1999), Question 4.9; Kechris–Marks’s survey, Problem 5.8, identifies that predecessor as slightly restricted. Current exact reaffirmation: Bernshteyn–Hou–Shinko–Weilacher, Randomized Borel (2d+1)-Coloring of Digraphs, https://arxiv.org/abs/2609.21286 , Question 4, p.1. Pelayo Gómez’s https://arxiv.org/abs/2609.19038 , Remark 4, p.2, explicitly leaves the Borel question open. Checked 10 October 2026.

**Further links.** [1](https://arxiv.org/abs/2609.21286) · [2](https://arxiv.org/abs/2609.19038)


<a id="q4288"></a>

## Q4288. Is p_n(2431)=p_n(3241) for every n≥1? For m≥0, let a_m count ordered pairs (P,Q) of length-m…

**Status:** Open · **Kind:** conjecture (Conjecture 5.2) · **Collection** 43

Is p_n(2431)=p_n(3241) for every n≥1? For m≥0, let a_m count ordered pairs (P,Q) of length-m Motzkin paths from (0,0) to (m,0), using steps (1,1),(1,0),(1,−1), staying above or on the horizontal axis. Require P to lie weakly below Q and their classes to agree: a path’s class records which non-down steps, indexed in occurrence order, are horizontal. Thus a_0=1; these numbers are OEIS A307786.

**Context.** For n≥1, flatten a set partition of [n]={1,…,n} by increasing entries within each block, ordering blocks by increasing minimum, then erasing separators. Let P_n contain the distinct resulting permutations, counted once each. Let p_n(τ) count members with no subsequence order-isomorphic to τ.

**Source.** Toufik Mansour, Olivia Nabawanda and Mark Shattuck. *Distinct flattened partitions avoiding a pattern of length four*. 2026. [primary source](https://arxiv.org/abs/2610.11271v1) Location: Conjecture 5.2, p.20.

**Literature check.** Status: Paper-origin. Both remain conjectures in current v1; no matching later resolution located, 11 October 2026. Sequence definition: Colin Defant’s OEIS entry https://oeis.org/A307786.

**Further links.** [1](https://oeis.org/A307786)


<a id="q4289"></a>

## Q4289. Is p_n(2341)=a_{n−1} for every n≥1?

**Status:** Open · **Kind:** conjecture (Conjecture 5.3) · **Collection** 43

Is p_n(2341)=a_{n−1} for every n≥1?

**Context.** For n≥1, flatten a set partition of [n]={1,…,n} by increasing entries within each block, ordering blocks by increasing minimum, then erasing separators. Let P_n contain the distinct resulting permutations, counted once each. Let p_n(τ) count members with no subsequence order-isomorphic to τ.

**Source.** Toufik Mansour, Olivia Nabawanda and Mark Shattuck. *Distinct flattened partitions avoiding a pattern of length four*. 2026. [primary source](https://arxiv.org/abs/2610.11271v1) Location: Conjecture 5.3, p.20.

**Literature check.** Status: Paper-origin. Both remain conjectures in current v1; no matching later resolution located, 11 October 2026. Sequence definition: Colin Defant’s OEIS entry https://oeis.org/A307786.

**Further links.** [1](https://oeis.org/A307786)


<a id="q4290"></a>

## Q4290. Determine π(C₅(r)) within a multiplicative constant as r→∞.

**Status:** Open · **Kind:** open problem (Problem 6.1) · **Collection** 43

Determine π(C₅(r)) within a multiplicative constant as r→∞.

**Context.** An r-uniform hypergraph has r-element edges. For such H, let ex(N,H) be the maximum number of edges of an H-free r-uniform hypergraph on N vertices, where H-free excludes any isomorphic subhypergraph; put π(H)=lim_{N→∞}ex(N,H)/binom(N,r). For a graph F and integer r≥2, F(r) is obtained by adjoining the same r−2 new vertices to every edge. Let C₅ be the five-vertex cycle, and let H₃ʳ be the r-uniform hypergraph on r+1 vertices with exactly three edges.

**Source.** Oleg Pikhurko, Jiabao Yang and Xiutao Zhu. *Turán densities of hypergraph augmentations*. 2026. [primary source](https://arxiv.org/abs/2610.11757v1) Location: Open Problem 6.1.

**Literature check.** Status: Paper-origin. The current paper supersedes Yang–Zhu arXiv:2608.18924; it explicitly leaves both targets open. No matching later resolution located, 11 October 2026.

**Further links.** [1](https://arxiv.org/abs/2608.18924)


<a id="q4291"></a>

## Q4291. Determine the asymptotic value of π(H₃ʳ) as r→∞. (Unnumbered open problem preceding 6.1.)

**Status:** Open · **Kind:** open problem · **Collection** 43

Determine the asymptotic value of π(H₃ʳ) as r→∞. (Unnumbered open problem preceding 6.1.)

**Context.** An r-uniform hypergraph has r-element edges. For such H, let ex(N,H) be the maximum number of edges of an H-free r-uniform hypergraph on N vertices, where H-free excludes any isomorphic subhypergraph; put π(H)=lim_{N→∞}ex(N,H)/binom(N,r). For a graph F and integer r≥2, F(r) is obtained by adjoining the same r−2 new vertices to every edge. Let C₅ be the five-vertex cycle, and let H₃ʳ be the r-uniform hypergraph on r+1 vertices with exactly three edges.

**Source.** Oleg Pikhurko, Jiabao Yang and Xiutao Zhu. *Turán densities of hypergraph augmentations*. 2026. [primary source](https://arxiv.org/abs/2610.11757v1) Location: §6, p.23.

**Literature check.** Status: Paper-origin. The current paper supersedes Yang–Zhu arXiv:2608.18924; it explicitly leaves both targets open. No matching later resolution located, 11 October 2026.

**Further links.** [1](https://arxiv.org/abs/2608.18924)


<a id="q4292"></a>

## Q4292. For each integer d≥2, are there infinitely many n admitting a symmetric abstract d-rigidity…

**Status:** Open · **Kind:** conjecture (Conjecture 4.1) · **Collection** 43

For each integer d≥2, are there infinitely many n admitting a symmetric abstract d-rigidity matroid on K_n that belongs to no such family?

**Context.** For integers n≥d≥1, an abstract d-rigidity matroid on the edges of K_n has rank dn−binom(d+1,2), with every K_{d+2} edge set a circuit (minimal dependent set). It is symmetric when every vertex permutation preserves independence. An abstract d-rigidity matroid family is a sequence (M_m)\_{m≥N} of symmetric abstract d-rigidity matroids on K_m whose restriction to every K_{m−1} is isomorphic to M_{m−1}, for m>N.

**Source.** Sean Dewar and Joannes Vermant. *Constructing pathological symmetric abstract rigidity matroids*. 2026. [primary source](https://arxiv.org/abs/2610.12036v1) Location: Conjecture 4.1, p.12.

**Literature check.** Status: Paper-origin. The paper proves the d=2 case and conjectures the full statement. Current v1 retains it; no matching later resolution located, 11 October 2026.


<a id="q4293"></a>

## Q4293. Is there a universal C with χ\_ℓ(M₁,M₂)≤χ(M₁,M₂)+C for every pair? In particular, does C=1 work?…

**Status:** Open · **Kind:** open problem (Question 3.1) · **Collection** 43

Is there a universal C with χ\_ℓ(M₁,M₂)≤χ(M₁,M₂)+C for every pair? In particular, does C=1 work? A matroid is strongly base-orderable if every pair of bases B₁,B₂ admits a bijection φ:B₁→B₂ for which (B₁∖S)∪φ(S) is a basis for every S⊆B₁.

**Context.** Let M₁,M₂ be finite loopless matroids on the same ground set E. A common coloring assigns colors to E with each color class independent in both matroids; χ(M₁,M₂) is its minimum number of colors. Define χ\_ℓ(M₁,M₂) as the least k such that every assignment of k permissible colors to each element admits a common coloring choosing from those lists.

**Source.** Bence Garami. *A note on the list chromatic number of two matroids*. 2026. [primary source](https://arxiv.org/abs/2610.07318v1) Location: Question 3.1, pp.4–5.

**Literature check.** Status: Paper-origin. The new counterexample concerns unrestricted equality; the strongly base-orderable case is proved only for two colors. Both questions remain in current v1; no matching later resolution located, 11 October 2026.


<a id="q4294"></a>

## Q4294. If both M₁ and M₂ are strongly base-orderable, must χ\_ℓ(M₁,M₂)=χ(M₁,M₂)?

**Status:** Open · **Kind:** open problem (Question 3.2) · **Collection** 43

If both M₁ and M₂ are strongly base-orderable, must χ\_ℓ(M₁,M₂)=χ(M₁,M₂)?

**Context.** Let M₁,M₂ be finite loopless matroids on the same ground set E. A common coloring assigns colors to E with each color class independent in both matroids; χ(M₁,M₂) is its minimum number of colors. Define χ\_ℓ(M₁,M₂) as the least k such that every assignment of k permissible colors to each element admits a common coloring choosing from those lists.

**Source.** Bence Garami. *A note on the list chromatic number of two matroids*. 2026. [primary source](https://arxiv.org/abs/2610.07318v1) Location: Question 3.2, pp.4–5.

**Literature check.** Status: Paper-origin. The new counterexample concerns unrestricted equality; the strongly base-orderable case is proved only for two colors. Both questions remain in current v1; no matching later resolution located, 11 October 2026.


<a id="q4295"></a>

## Q4295. As a function of positive integers N,k for which admissible partitions of [N]={1,…,N} exist,…

**Status:** Open · **Kind:** open problem (Problem 3) · **Collection** 43

As a function of positive integers N,k for which admissible partitions of [N]={1,…,N} exist, determine the minimum, over those partitions, of the largest ℓ such that {a,a+d,…,a+(ℓ−1)d}⊆R for integers a and d>0.

**Context.** Call a partition X=A₁⊔⋯⊔A_k⊔R admissible when |R|≥|X|/10 and (x+y)/2∉R for every i and x,y∈A_i. R has no assigned color. In integers the midpoint is rational; in 𝔽₃ⁿ division uses the inverse of 2.

**Source.** Tomasz Kościuszko. *Arithmetic Progressions in Midpoint Colourings*. 2026. [primary source](https://arxiv.org/abs/2610.11847v1) Location: Problem 3, p.2.

**Literature check.** Status: Paper-origin. Current v1 gives bounds with a remaining gap for each extremal target; no matching later resolution located, 11 October 2026.

**Results.**

- **Investigated, unresolved** (B2-CONTINUATION-STOP-REGISTER: Every B2 target reaches its own stopping condition): All 81 catalog questions have five reviewed substantive failed full-target routes (405 total); A-TRANSFER is solved locally. Partial proofs do not reset counters. The same retained agent completed ten catalog packets and the broader proof; root completed the other 71 catalog questions and the final filing. Remaining/limits: The catalog questions remain unresolved. Source, shell and service failures are excluded; new finite checks do not recover the original missing archive. [Report](../../solutions/b2-continuation-2026-10-12/STATUS.json).


<a id="q4296"></a>

## Q4296. As a function of positive integers n,k for which admissible partitions of 𝔽₃ⁿ exist, determine…

**Status:** Open, partial results · **Kind:** open problem (Problem 4) · **Collection** 43

As a function of positive integers n,k for which admissible partitions of 𝔽₃ⁿ exist, determine the minimum, over those partitions, of the largest dimension of an affine subspace contained in R.

**Context.** Call a partition X=A₁⊔⋯⊔A_k⊔R admissible when |R|≥|X|/10 and (x+y)/2∉R for every i and x,y∈A_i. R has no assigned color. In integers the midpoint is rational; in 𝔽₃ⁿ division uses the inverse of 2.

**Source.** Tomasz Kościuszko. *Arithmetic Progressions in Midpoint Colourings*. 2026. [primary source](https://arxiv.org/abs/2610.11847v1) Location: Problem 4, p.2.

**Literature check.** Status: Paper-origin. Current v1 gives bounds with a remaining gap for each extremal target; no matching later resolution located, 11 October 2026.

**Results.**

- **Partial result**: For every positive n, the minimum largest affine-subspace dimension of R under the source admissibility condition with k=1 is n-1. A nonempty complement is midpoint-closed and affine; a hyperplane complement attains the bound. The general sharp function for k>=2 remains unresolved. Internally reviewed at this scope; no external peer-review claim. Five failed full-target routes leave the catalog question unresolved. Later results (13 October 2026): Later external rounds prove O_p(k(log(2k)+log(1/alpha))) codimension, weighted quotient avoidance, block constructions, the two-color line-free classification, exact initial values through dimension four, maximal-flat fibre rigidity and occupied-fibre inheritance, sharp plane-free size 16 in dimension three, and the bound (5/2)2^n-4 for plane-free remainders when n>=3. The full sharp function and logarithmic gap remain open. [Details](../../solutions/b2-continuation-2026-10-12/arithmetic/UNCOLOURED-ATTEMPTS.md).
- **Partial result** (B2-CONTINUATION-ONE-COLOUR-DIMENSION: Exact one-colour finite-field remainder dimension): For every positive n, the minimum largest affine-subspace dimension of R under the source admissibility condition with k=1 is n-1. A nonempty complement is midpoint-closed and affine; a hyperplane complement attains the bound. Remaining/limits: The general sharp function for k>=2 remains unresolved. [Report](../../solutions/b2-continuation-2026-10-12/arithmetic/UNCOLOURED-ATTEMPTS.md).
- **Investigated, unresolved** (B2-CONTINUATION-STOP-REGISTER: Every B2 target reaches its own stopping condition): All 81 catalog questions have five reviewed substantive failed full-target routes (405 total); A-TRANSFER is solved locally. Partial proofs do not reset counters. The same retained agent completed ten catalog packets and the broader proof; root completed the other 71 catalog questions and the final filing. Remaining/limits: The catalog questions remain unresolved. Source, shell and service failures are excluded; new finite checks do not recover the original missing archive. [Report](../../solutions/b2-continuation-2026-10-12/STATUS.json).
- **Partial result** (B2-RETURN-R1-B2-NEW-Q4296-LOG-CODIMENSION: all-dimension theorem using established external PFR): Every admissible k-colour midpoint partition of F_3^n with remainder density at least 1/10 has an affine subspace in R of codimension O(k log(2k)). Remaining/limits: The exact extremal function and removal of the logarithmic factor are not determined. Full catalog target remains unresolved; internal review, no external peer review or worldwide-priority claim. [Report](../../solutions/b2-returned-rounds-2026-10-13/round1/RESEARCH-NOTE.tex).
- **Partial result** (B2-RETURN-R1-B2-NEW-WEIGHTED-QUOTIENT-AVOIDANCE: auxiliary general lemma): If A is covered by M cosets of H, s <= dim(W/H), and M p^(-s)<1, then an affine codimension-s subspace avoiding A exists on which any nonnegative function has average at most its ambient average divided by 1-M p^(-s). Remaining/limits: No small-doubling or midpoint hypothesis is required for this standalone lemma. Full catalog target remains unresolved; internal review, no external peer review or worldwide-priority claim. [Report](../../solutions/b2-returned-rounds-2026-10-13/round1/RESEARCH-NOTE.tex).
- **Partial result** (B2-RETURN-R1-B2-NEW-Q4296-BLOCK-CONSTRUCTION: explicit companion construction): For n>=kb, the remainder with every one of k disjoint b-dimensional blocks nonzero admits k midpoint colours on its complement and has largest affine subspace dimension exactly n-k; density is (1-p^(-b))^k. Remaining/limits: The primary source already notes linear-loss constructions; no priority claim for necessity of linear loss. Full catalog target remains unresolved; internal review, no external peer review or worldwide-priority claim. [Report](../../solutions/b2-returned-rounds-2026-10-13/round1/RESEARCH-NOTE.tex).
- **Partial result** (B2-RETURN-R2-Q4296-two-colour-cap: Q4296-two-colour-cap): For every n, line-free admissible two-colour remainders in F_3^n are exactly the empty set, a singleton, two points, or an affine parallelogram. Remaining/limits: Full catalog target remains unresolved; internal review, no external peer review or worldwide-priority claim. [Report](../../solutions/b2-returned-rounds-2026-10-13/round2/RESEARCH-NOTE.tex).
- **Partial result** (B2-RETURN-R2-Q4296-full-fibre: Q4296-full-fibre): Full fibres inherit admissibility for any k over odd prime fields. For two colours the number of complete parallel maximal flats is 1, 2, or 4, with parallelogram quotient structure for four. Remaining/limits: Full catalog target remains unresolved; internal review, no external peer review or worldwide-priority claim. [Report](../../solutions/b2-returned-rounds-2026-10-13/round2/RESEARCH-NOTE.tex).
- **Partial result** (B2-RETURN-R2-Q4296-initial-values: Q4296-initial-values): At density >=1/10, f(1,2)=f(2,2)=f(3,2)=0 and f(4,2)=1. Remaining/limits: Full catalog target remains unresolved; internal review, no external peer review or worldwide-priority claim. [Report](../../solutions/b2-returned-rounds-2026-10-13/round2/RESEARCH-NOTE.tex).
- **Partial result** (B2-RETURN-R2-Q4296-k-plus-two-obstruction: Q4296-k-plus-two-obstruction): For k>=2, n>=k ceil(log_3(10k))+2, there is an admissible density-1/10 partition with largest affine dimension exactly n-k-2. Remaining/limits: Full catalog target remains unresolved; internal review, no external peer review or worldwide-priority claim. [Report](../../solutions/b2-returned-rounds-2026-10-13/round2/RESEARCH-NOTE.tex).
- **Partial result** (B2-RETURN-R3-B2-III-M1: Maximal-flat fibre rigidity): In an admissible two-colour partition of F_3^n, quotient in the direction of a maximum-dimensional affine subspace contained in R. The full remainder fibres form a cap of size 1,2,4; all but at most one nonfull fibre have a monochromatic affine coloured complement. Remaining/limits: Full catalog target remains unresolved; internal review, no external peer review or worldwide-priority claim. [Report](../../solutions/b2-returned-rounds-2026-10-13/round3/RESEARCH-NOTE.tex).
- **Partial result** (B2-RETURN-R3-B2-III-M2: Occupied-fibre inheritance): Under the hypotheses of M1, the quotient set of fibres meeting R inherits an admissible two-colouring. Remaining/limits: Full catalog target remains unresolved; internal review, no external peer review or worldwide-priority claim. [Report](../../solutions/b2-returned-rounds-2026-10-13/round3/RESEARCH-NOTE.tex).
- **Partial result** (B2-RETURN-R3-B2-III-M3: Sharp plane-free threshold in F_3^3): The maximum cardinality of a plane-free admissible two-colour remainder in F_3^3 is exactly 16. Remaining/limits: Full catalog target remains unresolved; internal review, no external peer review or worldwide-priority claim. [Report](../../solutions/b2-returned-rounds-2026-10-13/round3/RESEARCH-NOTE.tex).
- **Partial result** (B2-RETURN-R3-B2-III-M4: All-dimension plane-free bound): For n>=3, a plane-free admissible two-colour remainder in F_3^n has cardinality at most (5/2)\*2^n-4. At density >=1/10, an affine plane is forced for n>=8. Remaining/limits: No sharpness claim beyond dimension 3; no improvement to general O(k log k) codimension. Full catalog target remains unresolved; internal review, no external peer review or worldwide-priority claim. [Report](../../solutions/b2-returned-rounds-2026-10-13/round3/RESEARCH-NOTE.tex).


<a id="q4297"></a>

## Q4297. If |α|=1 and α is algebraic but not an algebraic integer, must χ(Γ\_α)≤3?

**Status:** Open · **Kind:** open problem · **Collection** 43

If |α|=1 and α is algebraic but not an algebraic integer, must χ(Γ\_α)≤3?

**Context.** For finite A⊂{z∈ℂ:|z|=1}, let Γ\_A have vertex set ℤ[A]; two vertices are adjacent when their difference is a signed finite product of elements of A, including the empty product. Write Γ\_α=Γ\_{ {α} }. Let χ be the minimum number of colors in a proper coloring. Define χ\_c as the infimum of r≥2 admitting a map to a circle of circumference r with adjacent images at circular distance at least 1.

**Source.** Jonathan Davidson. *Coloring Monomial Cayley Graphs: The One-Parameter Case*. 2026. [primary source](https://arxiv.org/abs/2610.09474v1) Location: Conjectures 4.3/4.7 and questions pp.37,42.

**Literature check.** Status: Paper-origin. The first two conjectures have different remaining algebraic classes; ordinary four-chromaticity is proved for the sextic, not its circular value. Current v1 retains all four targets; no later resolution located, 11 October 2026.


<a id="q4298"></a>

## Q4298. For every |α|=1, must χ(Γ\_α)≤4?

**Status:** Open · **Kind:** open problem · **Collection** 43

For every |α|=1, must χ(Γ\_α)≤4?

**Context.** For finite A⊂{z∈ℂ:|z|=1}, let Γ\_A have vertex set ℤ[A]; two vertices are adjacent when their difference is a signed finite product of elements of A, including the empty product. Write Γ\_α=Γ\_{ {α} }. Let χ be the minimum number of colors in a proper coloring. Define χ\_c as the infimum of r≥2 admitting a map to a circle of circumference r with adjacent images at circular distance at least 1.

**Source.** Jonathan Davidson. *Coloring Monomial Cayley Graphs: The One-Parameter Case*. 2026. [primary source](https://arxiv.org/abs/2610.09474v1) Location: Conjectures 4.3/4.7 and questions pp.37,42.

**Literature check.** Status: Paper-origin. The first two conjectures have different remaining algebraic classes; ordinary four-chromaticity is proved for the sextic, not its circular value. Current v1 retains all four targets; no later resolution located, 11 October 2026.


<a id="q4299"></a>

## Q4299. For a unit-modulus root α of x⁶−x⁴−x³−x²+1, is χ\_c(Γ\_α)=7/2?

**Status:** Open · **Kind:** open problem · **Collection** 43

For a unit-modulus root α of x⁶−x⁴−x³−x²+1, is χ\_c(Γ\_α)=7/2?

**Context.** For finite A⊂{z∈ℂ:|z|=1}, let Γ\_A have vertex set ℤ[A]; two vertices are adjacent when their difference is a signed finite product of elements of A, including the empty product. Write Γ\_α=Γ\_{ {α} }. Let χ be the minimum number of colors in a proper coloring. Define χ\_c as the infimum of r≥2 admitting a map to a circle of circumference r with adjacent images at circular distance at least 1.

**Source.** Jonathan Davidson. *Coloring Monomial Cayley Graphs: The One-Parameter Case*. 2026. [primary source](https://arxiv.org/abs/2610.09474v1) Location: Conjectures 4.3/4.7 and questions pp.37,42.

**Literature check.** Status: Paper-origin. The first two conjectures have different remaining algebraic classes; ordinary four-chromaticity is proved for the sextic, not its circular value. Current v1 retains all four targets; no later resolution located, 11 October 2026.


<a id="q4300"></a>

## Q4300. Do unit complex numbers α,β exist with χ(Γ\_{ {α,β} })≥5?

**Status:** Open · **Kind:** open problem · **Collection** 43

Do unit complex numbers α,β exist with χ(Γ\_{ {α,β} })≥5?

**Context.** For finite A⊂{z∈ℂ:|z|=1}, let Γ\_A have vertex set ℤ[A]; two vertices are adjacent when their difference is a signed finite product of elements of A, including the empty product. Write Γ\_α=Γ\_{ {α} }. Let χ be the minimum number of colors in a proper coloring. Define χ\_c as the infimum of r≥2 admitting a map to a circle of circumference r with adjacent images at circular distance at least 1.

**Source.** Jonathan Davidson. *Coloring Monomial Cayley Graphs: The One-Parameter Case*. 2026. [primary source](https://arxiv.org/abs/2610.09474v1) Location: Conjectures 4.3/4.7 and questions pp.37,42.

**Literature check.** Status: Paper-origin. The first two conjectures have different remaining algebraic classes; ordinary four-chromaticity is proved for the sextic, not its circular value. Current v1 retains all four targets; no later resolution located, 11 October 2026.


<a id="q4301"></a>

## Q4301. Must |diam(O(P))−diam(C(P))|≤1 for every such P?

**Status:** Open · **Kind:** conjecture (Conjecture 29) · **Collection** 44

Must |diam(O(P))−diam(C(P))|≤1 for every such P?

**Context.** Let P={a₁,…,a_d} be a finite poset whose comparability graph is connected. Define O(P)={x∈[0,1]^d:x_i≥x_j whenever a_i≤\_P a_j} and C(P)={x∈ℝ\_{≥0}^d:Σ\_{a_i∈K}x_i≤1 for every chain K⊆P}. For a polytope Q, diam(Q) is the largest shortest-path distance between vertices in its vertex-edge graph.

**Source.** Jon Lee. *A refinement of the edge theorem for order and chain polytopes*. 2026. [primary source](https://arxiv.org/abs/2610.07413v1) Location: Conjecture 29, p.15.

**Literature check.** Status: Paper-origin. The source’s disconnected examples do not satisfy the connectedness hypothesis. Current v1 retains the conjecture; no matching later resolution located, 11 October 2026.


<a id="q4302"></a>

## Q4302. Is f_k(Γ)=Θ̃(n^(1/k)) as n→∞? Here Θ̃ permits multiplicative powers of log n, with constants…

**Status:** Open · **Kind:** conjecture (Conjecture 5.1) · **Collection** 44

Is f_k(Γ)=Θ̃(n^(1/k)) as n→∞? Here Θ̃ permits multiplicative powers of log n, with constants depending only on k.

**Context.** Fix k≥2. Let Γ range over finite abelian groups of sufficiently large order n with no nonzero element annihilated by k. Write kA={a₁+⋯+a_k:a_i∈A}, allowing repetitions. Let f_k(Γ) be the largest integer s such that every S⊆Γ with |S|≥n−s equals kA for some A⊆Γ.

**Source.** Jihyo Chae and Hyunwoo Lee. *Random Cayley sum hypergraphs and k-fold sumsets*. 2026. [primary source](https://arxiv.org/abs/2610.08629v1) Location: Conjecture 5.1, p.20.

**Literature check.** Status: Paper-origin. This is the source’s asymptotic conjecture. Current v1 proves the corresponding lower bound up to logarithms but leaves a larger upper bound; no matching later resolution located, 11 October 2026.

**Results.**

- **Investigated, unresolved** (B2-CONTINUATION-STOP-REGISTER: Every B2 target reaches its own stopping condition): All 81 catalog questions have five reviewed substantive failed full-target routes (405 total); A-TRANSFER is solved locally. Partial proofs do not reset counters. The same retained agent completed ten catalog packets and the broader proof; root completed the other 71 catalog questions and the final filing. Remaining/limits: The catalog questions remain unresolved. Source, shell and service failures are excluded; new finite checks do not recover the original missing archive. [Report](../../solutions/b2-continuation-2026-10-12/STATUS.json).


<a id="q4303"></a>

## Q4303. Determine explicit formulas for γ(J(n,k)) and γ\_t(J(n,k)) in terms of n,k for k≥4 and n>k.

**Status:** Open · **Kind:** open problem (Problem 29) · **Collection** 44

Determine explicit formulas for γ(J(n,k)) and γ\_t(J(n,k)) in terms of n,k for k≥4 and n>k.

**Context.** For integers n>k≥1, J(n,k) has the k-element subsets of {1,…,n} as vertices; distinct vertices are adjacent when their intersection has size k−1. A dominating set D gives every vertex outside D a neighbor in D. A total dominating set gives every vertex, including those in D, a neighbor in D. Let γ and γ\_t be the respective minimum cardinalities.

**Source.** María Gracia Cornet, Tanja Dravec and Pablo Torres. *Domination and Total Domination in Johnson graphs*. 2026. [primary source](https://arxiv.org/abs/2610.04675v1) Location: Problem 29, p.26.

**Literature check.** Status: Paper-origin, retained as one compound problem. The current paper settles k=2,3 and explicitly leaves the general target open; no matching later resolution located, 11 October 2026.


<a id="q4306"></a>

## Q4306. Classify all such G for which A has exactly three distinct eigenvalues.

**Status:** Open · **Kind:** open problem · **Collection** 44

Classify all such G for which A has exactly three distinct eigenvalues.

**Context.** For a finite simple connected graph G with vertex degrees d_i, define the real symmetric ISI matrix by A_ij=d_i d_j/(d_i+d_j) on edges and A_ij=0 elsewhere.

**Source.** Fareeha Jamal. *Problems in Extremal Graph Theory and Spectral Graph Theory*. United Arab Emirates University, 2025. Advisor(s): Nafaa Chbili. [primary source](https://scholarworks.uaeu.ac.ae/all_dissertations/346/) Location: dissertation future-work question, §7.3.1, p.92 (PDF115), extending the bipartite classification in Jamal–Imran–Rather (2023).

**Literature check.** Status checked 11 October 2026: Rather–Ganie's September 2026 v2 treats multipartite families and leaves irregular three-eigenvalue classification open; no complete resolution located.

**Further links.** [1](https://doi.org/10.1515/spma-2022-0175) · [2](https://arxiv.org/abs/2603.08895v2)


<a id="q4308"></a>

## Q4308. If G^L&lt;G for every immediate Left option and G&lt;G^R for every immediate Right option, must G be…

**Status:** Open · **Kind:** open problem · **Collection** 44

If G^L&lt;G for every immediate Left option and G&lt;G^R for every immediate Right option, must G be game-equivalent to a dyadic rational m/2^k, with m∈Z and k∈Z_{≥0}? The displayed inequalities are imposed only at G, not recursively on its followers.

**Context.** Doctoral context: Kant's IIT Bombay PhD, Bidding Combinatorial Games, defended 9 October 2025; supervisors K.S. Mallikarjuna Rao and Urban Larsson. The question's verified origin is this joint paper, not an inspected dissertation passage. Use short partizan games with alternating normal play: inability to move loses. In the disjunctive sum, a move changes one component; −H swaps players recursively. Define G>H when Left wins G+(−H) regardless of starting player, and G=H when the second player wins that difference.

**Source.** Prem Kant and Urban Larsson. *A number game reconciliation*. 2025. [primary source](https://arxiv.org/abs/2507.04717v1) Location: Problem5.21, p.28, equivalently Conjecture6.6, p.31.

**Literature check.** Status checked 11 October 2026: v1 remains current; no matching resolution located.

**Further links.** [1](https://www.ieor.iitb.ac.in/node/3955)


<a id="q4315"></a>

## Q4315. For every integer k≥1, is there an H with clique number at least k on which Alice has a winning…

**Status:** Open · **Kind:** open problem (Question 1) · **Collection** 44

For every integer k≥1, is there an H with clique number at least k on which Alice has a winning strategy when p=q=1?

**Context.** Genealogy: Malekshahian, A statistical physics approach to probabilistic combinatorics, King's College London PhD awarded 1 June 2026; supervisor Matthew Jenssen. Thesis text unavailable; deposit date unestablished. On a finite simple graph H, Alice moves first. Players alternately claim p and q unclaimed edges respectively, taking all remaining edges if fewer remain. Their clique scores ω\_A,ω\_B are the largest clique orders in their respective spanning graphs. For p≠q, the player with larger bias wins only with strictly larger score; ties go to the smaller-bias player. For p=q, Alice wins only if ω\_A>ω\_B.

**Source.** Alexandru Malekshahian and Sam Spiro. *On a Clique-Building Game of Erdős*. 2026. [primary source](https://doi.org/10.1002/jgt.70061) Location: Question 1, p.220.

**Literature check.** Status checked 11 October 2026: published final read; no matching resolution located.

**Further links.** [1](https://arxiv.org/abs/2410.18304v2) · [2](https://kclpure.kcl.ac.uk/portal/en/studentTheses/a-statistical-physics-approach-to-probabilistic-combinatorics/)


<a id="q4316"></a>

## Q4316. For every fixed pair of positive integers p,q, does the larger-bias player win on K_n for all…

**Status:** Open · **Kind:** conjecture (Conjecture 1) · **Collection** 44

For every fixed pair of positive integers p,q, does the larger-bias player win on K_n for all sufficiently large n, with Bob winning when p=q?

**Context.** Genealogy: Malekshahian, A statistical physics approach to probabilistic combinatorics, King's College London PhD awarded 1 June 2026; supervisor Matthew Jenssen. Thesis text unavailable; deposit date unestablished. On a finite simple graph H, Alice moves first. Players alternately claim p and q unclaimed edges respectively, taking all remaining edges if fewer remain. Their clique scores ω\_A,ω\_B are the largest clique orders in their respective spanning graphs. For p≠q, the player with larger bias wins only with strictly larger score; ties go to the smaller-bias player. For p=q, Alice wins only if ω\_A>ω\_B.

**Source.** Alexandru Malekshahian and Sam Spiro. *On a Clique-Building Game of Erdős*. 2026. [primary source](https://doi.org/10.1002/jgt.70061) Location: Conjecture 1, p.220.

**Literature check.** Status checked 11 October 2026: published final read; no matching resolution located.

**Further links.** [1](https://arxiv.org/abs/2410.18304v2) · [2](https://kclpure.kcl.ac.uk/portal/en/studentTheses/a-statistical-physics-approach-to-probabilistic-combinatorics/)


<a id="q4317"></a>

## Q4317. Taking the difference Δ(A)−Δ(B), is s=0 for every regular G other than K_2 and K_3, where Δ…

**Status:** Open · **Kind:** conjecture (Conjecture 7) · **Collection** 44

Taking the difference Δ(A)−Δ(B), is s=0 for every regular G other than K_2 and K_3, where Δ denotes maximum degree? For vertex capture, let a (respectively b) count vertices having strictly more than half their incident edges in A (respectively B), and use difference a−b.

**Context.** On a finite simple graph G, Alice moves first and the players alternately colour one uncoloured edge in their own colour until none remain. Let A,B be their final spanning graphs. For a specified score difference, Alice maximizes it and Bob minimizes it; s is its perfect-information minimax value. Original vertex-capture source: https://doi.org/10.1016/j.tcs.2022.04.050

**Source.** Stijn Cambie and Michiel Provoost. *On edge-colouring-games by Erdős, and Bensmail and Mc Inerney*. 2025. [primary source](https://arxiv.org/abs/2505.03497v2) Location: Conjecture 7, p.3.

**Literature check.** Status checked 11 October 2026: current version read; no newer publication or matching resolution located.

**Further links.** [1](https://doi.org/10.1016/j.tcs.2022.04.050)


<a id="q4318"></a>

## Q4318. On G=K_n for every integer n≥1, is s=2 if n=2, s=1 if n≡3 mod4, and s=0 otherwise?

**Status:** Open · **Kind:** conjecture (Conjecture 4) · **Collection** 44

On G=K_n for every integer n≥1, is s=2 if n=2, s=1 if n≡3 mod4, and s=0 otherwise?

**Context.** On a finite simple graph G, Alice moves first and the players alternately colour one uncoloured edge in their own colour until none remain. Let A,B be their final spanning graphs. For a specified score difference, Alice maximizes it and Bob minimizes it; s is its perfect-information minimax value. Original vertex-capture source: https://doi.org/10.1016/j.tcs.2022.04.050

**Source.** Stijn Cambie and Michiel Provoost. *On edge-colouring-games by Erdős, and Bensmail and Mc Inerney*. 2025. [primary source](https://arxiv.org/abs/2505.03497v2) Location: Conjecture 4, p.2.

**Literature check.** Status checked 11 October 2026: current version read; no newer publication or matching resolution located.

**Further links.** [1](https://doi.org/10.1016/j.tcs.2022.04.050)


<a id="q4319"></a>

## Q4319. Is it impossible for w, w⟨5⟩ and w⟨8⟩ all to be square-free?

**Status:** Open · **Kind:** open problem · **Collection** 44

Is it impossible for w, w⟨5⟩ and w⟨8⟩ all to be square-free?

**Context.** A word is square-free if no contiguous factor equals uu for a nonempty finite word u. For w=w_0w_1w_2⋯ over {0,1,2} and a positive integer p, write w⟨p⟩=w_0w_pw_{2p}⋯.

**Source.** Thomas Delépine, Pascal Ochem and Matthieu Rosenfeld. *Pairs of square-free arithmetic progressions in infinite words*. 2026. [primary source](https://arxiv.org/abs/2605.29853v1) Location: pp.1–2 and Question33, pp.23–24.

**Literature check.** Status checked 11 October 2026: current primary explicitly retains both; no newer publication or matching resolution located.

**Further links.** [1](https://doi.org/10.1016/j.tcs.2019.10.006)


<a id="q4320"></a>

## Q4320. Do positive integers p,k exist such that, for every strictly increasing sequence (p_i)\_{i≥0} of…

**Status:** Open · **Kind:** open problem · **Collection** 44

Do positive integers p,k exist such that, for every strictly increasing sequence (p_i)\_{i≥0} of pairwise coprime positive integers with p_0=p and p_{i+1}>kp_i, some infinite ternary word w has both w and every w⟨p_i⟩ square-free?

**Context.** A word is square-free if no contiguous factor equals uu for a nonempty finite word u. For w=w_0w_1w_2⋯ over {0,1,2} and a positive integer p, write w⟨p⟩=w_0w_pw_{2p}⋯.

**Source.** Thomas Delépine, Pascal Ochem and Matthieu Rosenfeld. *Pairs of square-free arithmetic progressions in infinite words*. 2026. [primary source](https://arxiv.org/abs/2605.29853v1) Location: pp.1–2 and Question33, pp.23–24.

**Literature check.** Status checked 11 October 2026: current primary explicitly retains both; no newer publication or matching resolution located.

**Further links.** [1](https://doi.org/10.1016/j.tcs.2019.10.006)


<a id="q4324"></a>

## Q4324. Is ultimate abelian periodicity of s decidable from f(a),f(b)?

**Status:** Open · **Kind:** open problem · **Collection** 44

Is ultimate abelian periodicity of s decidable from f(a),f(b)?

**Context.** An input specifies nonempty finite binary words f(a),f(b), with f(a)=au for a nonempty word u. Extend f to words by concatenation, and let s=f^ω(a) be the infinite word whose prefixes include every iterate f^j(a). Call s ultimately abelian periodic if s=v_0v_1v_2⋯, where v_0 is finite, possibly empty, and the nonempty blocks v_i, i≥1, all have identical counts of each letter.

**Source.** Arina Filimonova and Svetlana Puzynina. *On abelian periodicity of purely morphic words*. 2026. [primary source](https://arxiv.org/abs/2605.30306v1) Location: Theorem1 and following paragraph, p.2; definitions, p.3; §4, p.20.

**Literature check.** Status checked 11 October 2026: the current paper gives an algorithm only for the version requiring v_0 empty, and explicitly leaves the preperiod case’s algorithmic criterion open. No newer publication or matching resolution located.


<a id="q4325"></a>

## Q4325. Are e_5(n)=O(n^{1/3}) and e_6(n)=O(n^{1/4}) as n→∞? These are the matching upper bounds sought…

**Status:** Open · **Kind:** open problem · **Collection** 44

Are e_5(n)=O(n^{1/3}) and e_6(n)=O(n^{1/4}) as n→∞? These are the matching upper bounds sought in the source’s single tightness question; both are retained together.

**Context.** For a finite simple graph G, let b(G) be the least nonnegative integer b for which V(G) can be partitioned into two independent sets and b further sets, each containing only vertex pairs at graph distance at least three. Empty colour classes are allowed. For g∈{5,6}, let e_g(n)=max b(G) over n-vertex planar graphs of girth at least g; forests have infinite girth.

**Source.** Thomas Delépine. *Between proper and square coloring of planar graphs, hardness and extremal graphs*. 2026. [primary source](https://arxiv.org/abs/2602.13037v1) Location: Question34, p.28; definitions, pp.2–4,24.

**Literature check.** Status checked 11 October 2026: current version read; later maximum-degree-four results do not cover arbitrary degree. No matching resolution or newer publication located.


<a id="q4326"></a>

## Q4326. For every integer k≥3, is there n_0(k) such that, for every n≥n_0(k), the second player wins by…

**Status:** Open · **Kind:** conjecture (Conjecture 2.9) · **Collection** 44

For every integer k≥3, is there n_0(k) such that, for every n≥n_0(k), the second player wins by replying to every first-player choice p with p^r? The reply must remain legal after the preceding move; mere existence of some second-player winning strategy is weaker.

**Context.** Let S_n be all permutations of {1,…,n}. A permutation contains p∈S_k if a length-k subsequence has the same relative order as p. Starting with X=S_n, two players alternately choose a pattern p∈S_k contained in some member of X and replace X by those members avoiding p. A player with no legal move loses. Write p^r for p read backwards.

**Source.** Henning Ulfarsson. *A Permutation Avoidance Game with Reverse Replies and Monotone Traps*. 2026. [primary source](https://arxiv.org/abs/2603.16004v1) Location: Conjecture 2.9, p.5; Definition 1.1, p.1.

**Literature check.** Status checked 11 October 2026: current arXiv and author repository retain the conjecture; k=3,4 results are partial. No matching resolution or journal final located.


<a id="q4327"></a>

## Q4327. Must every nonempty losing position have even rank |λ\_1−r|?

**Status:** Open · **Kind:** conjecture (Conjecture 1) · **Collection** 44

Must every nonempty losing position have even rank |λ\_1−r|?

**Context.** Related student work: Bašić’s Column-Row Game, University of Primorska undergraduate thesis (2023), primary mentor Matjaž Krnc, co-mentor Eric Gottlieb; repository deposit 11 October 2023. It is not a doctoral dissertation; the body was not recovered. For a nonempty integer partition λ=(λ\_1≥⋯≥λ\_r>0), draw λ\_i left-justified cells in row i. A move deletes any entire row or column and closes the resulting gap, leaving a Young diagram. Players alternate; a player with no move loses. A losing position means that the next player loses under optimal play.

**Source.** Ina Bašić, Eric Gottlieb and Matjaž Krnc. *CRIM: A Natural Game on Integer Partitions*. 2026. [primary source](https://arxiv.org/abs/2606.16828v1) Location: Conjecture 1, p.17; definitions, pp.4,6,8.

**Literature check.** Status checked 11 October 2026: current paper retains the conjecture; no matching resolution or newer journal final located. Earlier thesis and conference material share this source-family capacity.

**Further links.** [1](https://repozitorij.upr.si/IzpisGradiva.php?id=19707)


<a id="q4328"></a>

## Q4328. For all finite nonempty posets P,Q, does E(P)≅E(Q) imply P≅Q, where ≅ means order-isomorphism?

**Status:** Open · **Kind:** open problem · **Collection** 44

For all finite nonempty posets P,Q, does E(P)≅E(Q) imply P≅Q, where ≅ means order-isomorphism?

**Context.** Origin: Duffus’s 1984 question, explicitly restated by Farley; this is a paper-origin entry. For a finite nonempty poset P, let E(P) consist of all maps f:P→P satisfying x≤y⇒f(x)≤f(y), with f≤g exactly when f(x)≤g(x) for every x∈P. Only this pointwise partial order is retained, without composition.

**Source.** Jonathan David Farley. *Trebled*. 2026. [primary source](https://arxiv.org/abs/2609.38532v1) Location: §1, pp.1–3; concluding discussion, p.18.

**Literature check.** Status checked 11 October 2026: the current paper settles special cases and leaves the general reconstruction question open; no active general resolution or newer final located.


<a id="q4329"></a>

## Q4329. For a=1, winning sets all triangles, and q=⌈√(2n−2)−3/2⌉, are there winning Breaker strategies…

**Status:** Open · **Kind:** open problem (Problem 5.1) · **Collection** 44

For a=1, winning sets all triangles, and q=⌈√(2n−2)−3/2⌉, are there winning Breaker strategies S_n with sup_{plays consistent with S_n}Σ\_i max(b_i−q,0)=o(n²) as n→∞, where b_i is Breaker’s edge count on turn i?

**Context.** Fix n≥3, q∈Z_{≥0}, a∈[0,1]. Players claim previously unclaimed edges of K_n, Maker first. Maker takes one edge per turn. Breaker takes any integer 0≤b≤⌊q+B⌋, where B initially equals zero. Afterward B decreases by b−q if b>q, and increases by a(q−b) otherwise. Maker wins by completing a specified winning edge-set; Breaker wins by meeting every winning set.

**Source.** Sebastian Lüderssen, Fabien Nießen and Silas Rathke. *Maker Breaker Games on a Budget*. 2026. [primary source](https://arxiv.org/abs/2609.38138v1) Location: Problem 5.1, pp.18–19.

**Literature check.** Status checked 11 October 2026: both targets remain in the current preprint; no matching resolution or newer final located.


<a id="q4330"></a>

## Q4330. When the winning sets are all Hamilton cycles, determine the threshold bias q_H(n,a), the least…

**Status:** Open · **Kind:** open problem (Problem 5.4) · **Collection** 44

When the winning sets are all Hamilton cycles, determine the threshold bias q_H(n,a), the least q for which Breaker has a winning strategy, for all a∈[0,1].

**Context.** Fix n≥3, q∈Z_{≥0}, a∈[0,1]. Players claim previously unclaimed edges of K_n, Maker first. Maker takes one edge per turn. Breaker takes any integer 0≤b≤⌊q+B⌋, where B initially equals zero. Afterward B decreases by b−q if b>q, and increases by a(q−b) otherwise. Maker wins by completing a specified winning edge-set; Breaker wins by meeting every winning set.

**Source.** Sebastian Lüderssen, Fabien Nießen and Silas Rathke. *Maker Breaker Games on a Budget*. 2026. [primary source](https://arxiv.org/abs/2609.38138v1) Location: Problem 5.4, pp.18–19.

**Literature check.** Status checked 11 October 2026: both targets remain in the current preprint; no matching resolution or newer final located.


<a id="q4331"></a>

## Q4331. Do both polynomials have ultra-log-concave coefficients for every n≥1, meaning c_i/binom(d,i) is…

**Status:** Open, partial results · **Kind:** conjecture (Conjecture 3.14) · **Collection** 44

Do both polynomials have ultra-log-concave coefficients for every n≥1, meaning c_i/binom(d,i) is log-concave, with d the polynomial’s degree? A Motzkin path of length l runs from (0,0) to (l,0), stays nonnegative, and uses (1,1),(1,0),(1,−1). Let M_l(t)=Σ\_P t^{1+maxheight(P)} over such paths, and R_l(t) the same sum restricted to paths with no horizontal step at height zero.

**Context.** Student context: Leite is a KTH doctoral student, primary supervisor Petter Brändén, co-supervisor Katharina Jochemko; no completed dissertation is claimed. Let H(n,h) count paths from (0,0) to (2n,0) with steps (1,±1), never below height zero, whose maximum height is h. Set H(0,0)=1 and other impossible counts to zero. For n≥1 put A_n(t)=Σ\_{i≥1}[H(n,2i−1)+H(n,2i)]t^i and B_n(t)=Σ\_{i≥1}[H(n−1,2i−2)+H(n−1,2i−1)]t^i.

**Source.** Per Alexandersson and Leonardo Saud Maia Leite. *Peaks and peak-nestings on unit interval graphs*. 2026. [primary source](https://arxiv.org/abs/2609.38084v1) Location: Conjecture 3.14, p.12.

**Literature check.** Status checked 11 October 2026: both conjectures remain in v1; no matching resolution or newer final located.

**Results.**

- **Partial result**: For d=ceil(n/2), A_n coefficients divided by binom(d,i) are log-concave at ceil((n+2)/4)&lt;i&lt;d; B_n has the same assertion at floor((n+2)/4)+1&lt;i&lt;d. The i=1 zero-boundary inequalities hold as well. For Motzkin and Riordan paths at every length, the final nontrivial ordinary log-concavity inequality holds. Arbitrary interior heights in all four families remain unresolved. Internally reviewed at this scope; no novelty or external peer-review claim. [Details](../../solutions/b3-all-targets-2026-10-13/paths/UPPER-TAIL.md).
- **Partial result** (B3-ALL-TARGETS-PATH-ENDPOINTS: All-length upper inequalities for path-height rows): For d=ceil(n/2), A_n coefficients divided by binom(d,i) are log-concave at ceil((n+2)/4)&lt;i&lt;d; B_n has the same assertion at floor((n+2)/4)+1&lt;i&lt;d. The i=1 zero-boundary inequalities hold as well. For Motzkin and Riordan paths at every length, the final nontrivial ordinary log-concavity inequality holds. Remaining/limits: Arbitrary interior heights in all four families remain unresolved. [Report](../../solutions/b3-all-targets-2026-10-13/paths/UPPER-TAIL.md).
- **Investigated, unresolved** (B3-ALL-TARGETS-STOP-REGISTER: Reviewed B3 failed routes and per-target stopping decisions): 45 targets have each reached five consecutive substantive distinct full-target failures. STATUS.json records every accepted route, written analysis, evidence path and review provenance. Partial results do not reset counters. Rejected proposed attempts, source-range replays, service errors and shared mechanisms remain explicit rather than supplying extra counts. Remaining/limits: These questions remain mathematically unresolved. A failure-limit stop is an operational disposition, not a counterexample or proof. Missing historical archives remain separate evidence issues. [Report](../../solutions/b3-all-targets-2026-10-13/STATUS.json).


<a id="q4332"></a>

## Q4332. For every l≥0, are the coefficients of both M_l and R_l log-concave, meaning c_i²≥c_{i−1}c_{i+1}?

**Status:** Open, partial results · **Kind:** conjecture (Conjecture 6.8) · **Collection** 44

For every l≥0, are the coefficients of both M_l and R_l log-concave, meaning c_i²≥c_{i−1}c_{i+1}?

**Context.** Student context: Leite is a KTH doctoral student, primary supervisor Petter Brändén, co-supervisor Katharina Jochemko; no completed dissertation is claimed. Let H(n,h) count paths from (0,0) to (2n,0) with steps (1,±1), never below height zero, whose maximum height is h. Set H(0,0)=1 and other impossible counts to zero. For n≥1 put A_n(t)=Σ\_{i≥1}[H(n,2i−1)+H(n,2i)]t^i and B_n(t)=Σ\_{i≥1}[H(n−1,2i−2)+H(n−1,2i−1)]t^i.

**Source.** Per Alexandersson and Leonardo Saud Maia Leite. *Peaks and peak-nestings on unit interval graphs*. 2026. [primary source](https://arxiv.org/abs/2609.38084v1) Location: Conjecture 6.8, p.31.

**Literature check.** Status checked 11 October 2026: both conjectures remain in v1; no matching resolution or newer final located.

**Results.**

- **Partial result**: For d=ceil(n/2), A_n coefficients divided by binom(d,i) are log-concave at ceil((n+2)/4)&lt;i&lt;d; B_n has the same assertion at floor((n+2)/4)+1&lt;i&lt;d. The i=1 zero-boundary inequalities hold as well. For Motzkin and Riordan paths at every length, the final nontrivial ordinary log-concavity inequality holds. Arbitrary interior heights in all four families remain unresolved. Internally reviewed at this scope; no novelty or external peer-review claim. [Details](../../solutions/b3-all-targets-2026-10-13/paths/UPPER-TAIL.md).
- **Partial result** (B3-ALL-TARGETS-PATH-ENDPOINTS: All-length upper inequalities for path-height rows): For d=ceil(n/2), A_n coefficients divided by binom(d,i) are log-concave at ceil((n+2)/4)&lt;i&lt;d; B_n has the same assertion at floor((n+2)/4)+1&lt;i&lt;d. The i=1 zero-boundary inequalities hold as well. For Motzkin and Riordan paths at every length, the final nontrivial ordinary log-concavity inequality holds. Remaining/limits: Arbitrary interior heights in all four families remain unresolved. [Report](../../solutions/b3-all-targets-2026-10-13/paths/UPPER-TAIL.md).
- **Investigated, unresolved** (B3-ALL-TARGETS-STOP-REGISTER: Reviewed B3 failed routes and per-target stopping decisions): 45 targets have each reached five consecutive substantive distinct full-target failures. STATUS.json records every accepted route, written analysis, evidence path and review provenance. Partial results do not reset counters. Rejected proposed attempts, source-range replays, service errors and shared mechanisms remain explicit rather than supplying extra counts. Remaining/limits: These questions remain mathematically unresolved. A failure-limit stop is an operational disposition, not a counterexample or proof. Missing historical archives remain separate evidence issues. [Report](../../solutions/b3-all-targets-2026-10-13/STATUS.json).


<a id="q4333"></a>

## Q4333. Does every finite square-free word over A have a square-free extension?

**Status:** Open · **Kind:** conjecture (Conjecture 12) · **Collection** 44

Does every finite square-free word over A have a square-free extension?

**Context.** Let A be an alphabet with exactly four symbols. A finite word over A is square-free when none of its contiguous factors equals XX for a nonempty word X. An extension inserts one symbol from A into any gap, including either end. Current reaffirmation: Eng Keat Hng and Silas Rathke, No extremal square-free words over alphabets of size at least 5, arXiv:2608.10591v1 (11 August 2026), Conjecture 3.1, p.18; Definition 1.1, p.1.

**Source.** Jarosław Grytczuk, Hubert Kordulewski and Artur Niewiadomski. *Extremal Square-Free Words*. 2020. [primary source](https://doi.org/10.37236/9264) Location: Conjecture 12, p.8; definitions, pp.1–2.

**Literature check.** Status checked 11 October 2026: the current paper settles alphabet sizes at least five and explicitly retains the four-symbol case; no matching resolution located.

**Further links.** [1](https://arxiv.org/abs/2608.10591v1)


<a id="q4348"></a>

## Q4348. Must G be plain?

**Status:** Open · **Kind:** conjecture (Conjecture 1) · **Collection** 44

Must G be plain?

**Context.** Fields: combinatorial group theory; computational complexity. Setup: Σ is finite and R⊂Σ\*×Σ\* is finite, with |ℓ|>|r| for every rule ℓ→r. Assume contextual rewriting has a unique irreducible normal form for every word and the quotient monoid is a group G. A plain group is a free product of finitely many finite groups and a finite-rank free group.

**Source.** Murray Elder and Adam Piggott. *On groups presented by inverse-closed finite confluent length-reducing rewriting systems*. 2023. [primary source](https://doi.org/10.1016/j.jalgebra.2023.03.022) Location: Madlener–Otto’s 1987 conjecture; Murray Elder and Adam Piggott, On groups presented by inverse-closed finite confluent length-reducing rewriting systems (2023), authenticated accepted copy, Conjecture 1, p.1.

**Literature check.** Status: Paper-origin formulations; no dissertation attribution. Status checked 11 October 2026: Σ₃^P is established; no matching general resolution found. The inverse-closed restriction belongs only to Q4349.

**Further links.** [1](https://doi.org/10.4230/LIPIcs.STACS.2022.26)


<a id="q4363"></a>

## Q4363. Let I,J be the identity and all-ones matrices of size 40, and C=I_10⊗(J_4−I_4). Does a matrix A∈{0,1}^{40×40} exist with

**Status:** Open · **Kind:** open problem (Problem 8.3) · **Collection** 44

A+Aᵀ=J−I−C, AJ=JA=18J, and A²=8(A+Aᵀ)+12C? Equivalently, seek a doubly regular tournament on ten teams of four, with no intrateam arcs, one directed arc per interteam pair, and these path-count parameters.

**Context.** Akihiro Higashitani: a forty-vertex type-2 scheme Genealogy: thesis acknowledgments p.8 and https://ir.library.osaka-u.ac.jp/repo/ouka/all/24732/

**Source.** Akihiro Higashitani and Kurihara. *Imprimitive association schemes and elimination theory*. 2026. [primary source](https://arxiv.org/abs/2603.20989) Location: Higashitani–Kurihara, Imprimitive association schemes and elimination theory, arXiv 2603.20989v2, Problem 8.3 p.43; Jørgensen, Algorithmic approach to non-symmetric 3-class association schemes, equations (1)–(4), Theorem 6, open case p.14. https://arxiv.org/abs/2603.20989 https://people.math.aau.dk/~leif/research/scheme3article.pdf

**Literature check.** Status: April 2026 v2 explicitly retains this smallest feasible case; known larger constructions do not settle it.

**Further links.** [1](https://ir.library.osaka-u.ac.jp/repo/ouka/all/24732/) · [2](https://people.math.aau.dk/~leif/research/scheme3article.pdf) · [3](https://arxiv.org/abs/2603.20989v2)


<a id="q4401"></a>

## Q4401. If every edge-colouring of G with b+1 colours contains a monochromatic copy of H, must Maker…

**Status:** Open · **Kind:** conjecture (Conjecture 6.1) · **Collection** 45

If every edge-colouring of G with b+1 colours contains a monochromatic copy of H, must Maker have a winning strategy in this game, for every finite simple G,H and every b≥1? For the unbiased game b=1, let r̂\_MB(H) be the minimum |E(G)| over all finite simple graphs G on which Maker can force a copy of H.

**Context.** On a finite simple graph G, Maker and Breaker alternately claim previously unclaimed edges, Maker first. Maker claims one per turn; Breaker claims at most b, where b≥1 is an integer. Maker wins by claiming every edge of a copy of a specified graph H; otherwise Breaker wins when the board is exhausted.

**Source.** Alexander Allin, Juri Barkey and Dennis Clemens. *Ramsey-type results for Maker-Breaker games*. 2026. [primary source](https://arxiv.org/abs/2609.02588v1) Location: Conjecture 6.1, p.23.

**Literature check.** Status checked 11 October 2026: current v1 retains both questions; no newer final or matching resolution located.


<a id="q4402"></a>

## Q4402. Determine r̂\_MB(P_n) for every positive integer n, where P_n is the n-vertex path.

**Status:** Open · **Kind:** open problem (Problem 6.10) · **Collection** 45

Determine r̂\_MB(P_n) for every positive integer n, where P_n is the n-vertex path.

**Context.** On a finite simple graph G, Maker and Breaker alternately claim previously unclaimed edges, Maker first. Maker claims one per turn; Breaker claims at most b, where b≥1 is an integer. Maker wins by claiming every edge of a copy of a specified graph H; otherwise Breaker wins when the board is exhausted.

**Source.** Alexander Allin, Juri Barkey and Dennis Clemens. *Ramsey-type results for Maker-Breaker games*. 2026. [primary source](https://arxiv.org/abs/2609.02588v1) Location: Problem 6.10, p.25.

**Literature check.** Status checked 11 October 2026: current v1 retains both questions; no newer final or matching resolution located.


<a id="q4403"></a>

## Q4403. Is there a connected n-vertex graph H with 4≤n≤121 and f(H)=n?

**Status:** Open · **Kind:** open problem (Question 1) · **Collection** 45

Is there a connected n-vertex graph H with 4≤n≤121 and f(H)=n?

**Context.** For finite simple H, Builder and Painter play on n vertices with three colours. Each round, Builder exposes a previously unexposed edge and may forbid one colour; Painter assigns that edge an allowed colour. Painter wins upon making a monochromatic H. Builder tries to delay or prevent this. Let f(H) be the least n allowing Painter to force a win, and f(n,H) the minimum number of rounds within which Painter can force a win. Doctoral route: Almási is a BME doctoral student supervised by Géza Tóth; no completed doctorate is asserted. Genealogy/status sources: https://doktori.math.bme.hu/english/phd-students.htm

**Source.** Nóra Almási and Maria Axenovich. *Online Ramsey turnaround numbers*. 2025. [primary source](https://arxiv.org/abs/2512.08053v1) Location: Question 1, p.12.

**Literature check.** Status checked 11 October 2026: current v1 still poses all three questions; no newer final or matching resolution located.

**Further links.** [1](https://doktori.math.bme.hu/english/phd-students.htm)


<a id="q4404"></a>

## Q4404. Determine f(n,K_3) for n≥6.

**Status:** Open · **Kind:** open problem (Question 2) · **Collection** 45

Determine f(n,K_3) for n≥6.

**Context.** For finite simple H, Builder and Painter play on n vertices with three colours. Each round, Builder exposes a previously unexposed edge and may forbid one colour; Painter assigns that edge an allowed colour. Painter wins upon making a monochromatic H. Builder tries to delay or prevent this. Let f(H) be the least n allowing Painter to force a win, and f(n,H) the minimum number of rounds within which Painter can force a win. Doctoral route: Almási is a BME doctoral student supervised by Géza Tóth; no completed doctorate is asserted. Genealogy/status sources: https://doktori.math.bme.hu/english/phd-students.htm

**Source.** Nóra Almási and Maria Axenovich. *Online Ramsey turnaround numbers*. 2025. [primary source](https://arxiv.org/abs/2512.08053v1) Location: Question 2, p.12.

**Literature check.** Status checked 11 October 2026: current v1 still poses all three questions; no newer final or matching resolution located.

**Further links.** [1](https://doktori.math.bme.hu/english/phd-students.htm)


<a id="q4405"></a>

## Q4405. Do connected graphs H of arbitrarily large order exist such that every three-colouring of…

**Status:** Open · **Kind:** open problem (Question 3) · **Collection** 45

Do connected graphs H of arbitrarily large order exist such that every three-colouring of E(K_|V(H)|) contains a copy of H using at most two colours?

**Context.** For finite simple H, Builder and Painter play on n vertices with three colours. Each round, Builder exposes a previously unexposed edge and may forbid one colour; Painter assigns that edge an allowed colour. Painter wins upon making a monochromatic H. Builder tries to delay or prevent this. Let f(H) be the least n allowing Painter to force a win, and f(n,H) the minimum number of rounds within which Painter can force a win. Doctoral route: Almási is a BME doctoral student supervised by Géza Tóth; no completed doctorate is asserted. Genealogy/status sources: https://doktori.math.bme.hu/english/phd-students.htm

**Source.** Nóra Almási and Maria Axenovich. *Online Ramsey turnaround numbers*. 2025. [primary source](https://arxiv.org/abs/2512.08053v1) Location: Question 3, p.12.

**Literature check.** Status checked 11 October 2026: current v1 still poses all three questions; no newer final or matching resolution located.

**Further links.** [1](https://doktori.math.bme.hu/english/phd-students.htm)


<a id="q4406"></a>

## Q4406. Characterize the outerplanar graphs H for which some N≥|V(H)| guarantees that every maximal…

**Status:** Open · **Kind:** open problem (Problem 1) · **Collection** 45

Characterize the outerplanar graphs H for which some N≥|V(H)| guarantees that every maximal outerplanar graph with at least N vertices contains H.

**Context.** Doctoral route: Baldacchino, Birmingham, advisor Anupam Das; Mifsud, Oxford, supervisors Leslie Ann Goldberg and Andreas Galanis. Both remain doctoral students. Graphs are finite and simple; containment means ordinary subgraph containment. A graph is maximal planar, respectively maximal outerplanar, if adding any missing edge destroys planarity, respectively outerplanarity. Outerplanarity means admitting a plane drawing with every vertex on the unbounded face. Genealogy/status sources: https://abaldacchino.github.io/index.html https://www.cs.ox.ac.uk/people/leslieann.goldberg/projects.html https://xmif1.github.io/

**Source.** Adriana Baldacchino, Yair Caro and Xandru Mifsud. *Ramsey properties of maximal (outer)planar graphs*. 2026. [primary source](https://arxiv.org/abs/2609.05268v1) Location: Problem 1, p.21.

**Literature check.** Status checked 11 October 2026: current v1 retains both problems; the author's publication list calls the paper submitted. No newer final or matching resolution located.

**Further links.** [1](https://abaldacchino.github.io/index.html) · [2](https://www.cs.ox.ac.uk/people/leslieann.goldberg/projects.html) · [3](https://xmif1.github.io/)


<a id="q4407"></a>

## Q4407. Characterize all pairs of graphs (H,F) for which some N guarantees that every red/blue…

**Status:** Open · **Kind:** open problem (Problem 3) · **Collection** 45

Characterize all pairs of graphs (H,F) for which some N guarantees that every red/blue edge-colouring of every maximal planar graph with at least N vertices contains a red H or a blue F.

**Context.** Doctoral route: Baldacchino, Birmingham, advisor Anupam Das; Mifsud, Oxford, supervisors Leslie Ann Goldberg and Andreas Galanis. Both remain doctoral students. Graphs are finite and simple; containment means ordinary subgraph containment. A graph is maximal planar, respectively maximal outerplanar, if adding any missing edge destroys planarity, respectively outerplanarity. Outerplanarity means admitting a plane drawing with every vertex on the unbounded face. Genealogy/status sources: https://abaldacchino.github.io/index.html https://www.cs.ox.ac.uk/people/leslieann.goldberg/projects.html https://xmif1.github.io/

**Source.** Adriana Baldacchino, Yair Caro and Xandru Mifsud. *Ramsey properties of maximal (outer)planar graphs*. 2026. [primary source](https://arxiv.org/abs/2609.05268v1) Location: Problem 3, p.21.

**Literature check.** Status checked 11 October 2026: current v1 retains both problems; the author's publication list calls the paper submitted. No newer final or matching resolution located.

**Further links.** [1](https://abaldacchino.github.io/index.html) · [2](https://www.cs.ox.ac.uk/people/leslieann.goldberg/projects.html) · [3](https://xmif1.github.io/)


<a id="q4408"></a>

## Q4408. Characterize all such G with RC(G)=C(G).

**Status:** Open · **Kind:** open problem (Problem 1) · **Collection** 45

Characterize all such G with RC(G)=C(G).

**Context.** Let G be finite, simple and connected. D⊆V(G) is dominating if every outside vertex has a neighbour in D; it is restrained dominating if every outside vertex also has an outside neighbour. For either property P, a P-coalition is two disjoint non-P sets whose union has P. A P-partition is a vertex partition whose P-parts are singletons and whose other parts each form a P-coalition with another part. Let C(G), respectively RC(G), be its maximum number of parts for domination, respectively restrained domination.

**Source.** Andrey A. Dobrynin, Aleksey N. Glebov and Hamidreza Golmohammadi. *On Restrained Coalitions in Graphs: Bounds and Exact Values*. 2026. [primary source](https://doi.org/10.47443/dml.2025.223) Location: Problem 1, p.62.

**Literature check.** Status checked 11 October 2026: published final retains both questions; no later matching resolution located.


<a id="q4409"></a>

## Q4409. Characterize all graphs obtained from a restrained-domination partition of a cycle by making its…

**Status:** Open · **Kind:** open problem (Problem 2) · **Collection** 45

Characterize all graphs obtained from a restrained-domination partition of a cycle by making its parts vertices and joining precisely the pairs that form a restrained-domination coalition.

**Context.** Let G be finite, simple and connected. D⊆V(G) is dominating if every outside vertex has a neighbour in D; it is restrained dominating if every outside vertex also has an outside neighbour. For either property P, a P-coalition is two disjoint non-P sets whose union has P. A P-partition is a vertex partition whose P-parts are singletons and whose other parts each form a P-coalition with another part. Let C(G), respectively RC(G), be its maximum number of parts for domination, respectively restrained domination.

**Source.** Andrey A. Dobrynin, Aleksey N. Glebov and Hamidreza Golmohammadi. *On Restrained Coalitions in Graphs: Bounds and Exact Values*. 2026. [primary source](https://doi.org/10.47443/dml.2025.223) Location: Problem 2, p.62.

**Literature check.** Status checked 11 October 2026: published final retains both questions; no later matching resolution located.


<a id="q4410"></a>

## Q4410. Characterize all G satisfying C_tr(G)=C(G).

**Status:** Open · **Kind:** open problem · **Collection** 45

Characterize all G satisfying C_tr(G)=C(G).

**Context.** Graphs are finite, simple and without isolated vertices. A total restrained dominating set S gives every vertex a neighbour in S and every vertex outside S a neighbour outside S. A total restrained coalition is two disjoint sets neither having this property whose union has it. Let C_tr(G) maximize the number of parts of a vertex partition in which each part forms such a coalition with another part. Let C(G) similarly use ordinary domination, allowing dominating singleton parts; ordinary domination requires every outside vertex to have a neighbour in the set.

**Source.** M. Chellali, H. Golmohammadi, N. A. Matrokhin, I. I. Takhonov and J. C. Valenzuela-Tripodoro. *Total restrained coalitions in graphs*. 2025. [primary source](https://doi.org/10.1007/s40314-025-03439-w) Location: §5, directions 1 and 4, p.13.

**Literature check.** Status checked 11 October 2026: published final retains both questions; no later matching resolution located.


<a id="q4411"></a>

## Q4411. Can C_tr(T) be computed in polynomial time for every tree T with at least two vertices?

**Status:** Open · **Kind:** open problem · **Collection** 45

Can C_tr(T) be computed in polynomial time for every tree T with at least two vertices?

**Context.** Graphs are finite, simple and without isolated vertices. A total restrained dominating set S gives every vertex a neighbour in S and every vertex outside S a neighbour outside S. A total restrained coalition is two disjoint sets neither having this property whose union has it. Let C_tr(G) maximize the number of parts of a vertex partition in which each part forms such a coalition with another part. Let C(G) similarly use ordinary domination, allowing dominating singleton parts; ordinary domination requires every outside vertex to have a neighbour in the set.

**Source.** M. Chellali, H. Golmohammadi, N. A. Matrokhin, I. I. Takhonov and J. C. Valenzuela-Tripodoro. *Total restrained coalitions in graphs*. 2025. [primary source](https://doi.org/10.1007/s40314-025-03439-w) Location: §5, directions 1 and 4, p.13.

**Literature check.** Status checked 11 October 2026: published final retains both questions; no later matching resolution located.


<a id="q4412"></a>

## Q4412. Does γ∞(G)=θ(G) hold for every planar G?

**Status:** Open · **Kind:** open problem (Problem 1.1) · **Collection** 45

Does γ∞(G)=θ(G) hold for every planar G?

**Context.** For a finite simple graph G, θ(G) is the minimum number of cliques partitioning its vertices. Let γ∞(G) be the minimum guards needed to defend forever: initially their occupied vertices dominate; after each attack at an unoccupied vertex, exactly one guard moves along an edge to it, leaving a dominating set. G is vertex-critical if θ(G−v)<θ(G) for every vertex v.

**Source.** Kenji Kimura, Naoki Matsumoto and Tsukasa Sato. *Note on the Eternal Domination Number of Planar Graphs and Vertex-Critical Graphs*. 2026. [primary source](https://doi.org/10.47443/dml.2025.208) Location: Problem 1.1, p.45.

**Literature check.** Status checked 11 October 2026: published final retains both questions; no matching later resolution located.

**Further links.** [1](https://doi.org/10.5614/ejgta.2022.10.2.19)


<a id="q4413"></a>

## Q4413. If G is triangle-free and vertex-critical, n=|V(G)| and |E(G)|≤2n−3, is γ∞(G)=θ(G) equivalent to…

**Status:** Open · **Kind:** conjecture (Conjecture 2.1) · **Collection** 45

If G is triangle-free and vertex-critical, n=|V(G)| and |E(G)|≤2n−3, is γ∞(G)=θ(G) equivalent to γ∞(G−v)=θ(G−v) for every v∈V(G)?

**Context.** For a finite simple graph G, θ(G) is the minimum number of cliques partitioning its vertices. Let γ∞(G) be the minimum guards needed to defend forever: initially their occupied vertices dominate; after each attack at an unoccupied vertex, exactly one guard moves along an edge to it, leaving a dominating set. G is vertex-critical if θ(G−v)<θ(G) for every vertex v.

**Source.** Kenji Kimura, Naoki Matsumoto and Tsukasa Sato. *Note on the Eternal Domination Number of Planar Graphs and Vertex-Critical Graphs*. 2026. [primary source](https://doi.org/10.47443/dml.2025.208) Location: Conjecture 2.1, p.47.

**Literature check.** Status checked 11 October 2026: published final retains both questions; no matching later resolution located.

**Further links.** [1](https://doi.org/10.5614/ejgta.2022.10.2.19)


<a id="q4414"></a>

## Q4414. Is R_{Γ(G)+2}(G) connected for every planar G?

**Status:** Open · **Kind:** conjecture (Conjecture 5.1) · **Collection** 45

Is R_{Γ(G)+2}(G) connected for every planar G?

**Context.** For finite simple G, a dominating set meets every closed neighbourhood. Let Γ(G) be the largest size of an inclusion-minimal dominating set. R_k(G) has dominating sets of size at most k as vertices, adjacent when one vertex is added or deleted. Treewidth tw(G), respectively pathwidth pw(G), minimizes largest bag size minus one over tree, respectively path, decompositions: bags cover vertices and edges, and bags containing each vertex form a connected subtree.

**Source.** Alice Joffard. *Graph domination and reconfiguration problems*. Université de Lyon, 2020. Advisor(s): Hamamache Kheddouci; co-director Nicolas Bousquet. [primary source](https://perso.liris.cnrs.fr/ajoffard/manuscript.pdf) Location: Origins: thesis Conjecture 5.1, p.66, and discussion, p.118; linked Bousquet–Joffard–Ouvrard ISAAC 2020 paper, pp.3–5, and Bousquet's habilitation Question 110, p.107.

**Literature check.** Status checked 11 October 2026: cited final and later habilitation checked; no matching resolution located.

**Further links.** [1](https://doi.org/10.4230/LIPIcs.ISAAC.2020.37) · [2](https://perso.liris.cnrs.fr/nbousquet/Habilitation_defense.pdf)


<a id="q4415"></a>

## Q4415. Is R_{Γ(G)+tw(G)}(G) connected for every G?

**Status:** Open · **Kind:** conjecture (Conjecture 5.1) · **Collection** 45

Is R_{Γ(G)+tw(G)}(G) connected for every G?

**Context.** For finite simple G, a dominating set meets every closed neighbourhood. Let Γ(G) be the largest size of an inclusion-minimal dominating set. R_k(G) has dominating sets of size at most k as vertices, adjacent when one vertex is added or deleted. Treewidth tw(G), respectively pathwidth pw(G), minimizes largest bag size minus one over tree, respectively path, decompositions: bags cover vertices and edges, and bags containing each vertex form a connected subtree.

**Source.** Alice Joffard. *Graph domination and reconfiguration problems*. Université de Lyon, 2020. Advisor(s): Hamamache Kheddouci; co-director Nicolas Bousquet. [primary source](https://perso.liris.cnrs.fr/ajoffard/manuscript.pdf) Location: Origins: thesis Conjecture 5.1, p.66, and discussion, p.118; linked Bousquet–Joffard–Ouvrard ISAAC 2020 paper, pp.3–5, and Bousquet's habilitation Question 110, p.107.

**Literature check.** Status checked 11 October 2026: cited final and later habilitation checked; no matching resolution located.

**Further links.** [1](https://doi.org/10.4230/LIPIcs.ISAAC.2020.37) · [2](https://perso.liris.cnrs.fr/nbousquet/Habilitation_defense.pdf)


<a id="q4416"></a>

## Q4416. Is there an absolute constant c such that R_k(G) is connected whenever k≥Γ(G)+pw(G)/2+c?

**Status:** Open · **Kind:** conjecture (Conjecture 5.1) · **Collection** 45

Is there an absolute constant c such that R_k(G) is connected whenever k≥Γ(G)+pw(G)/2+c?

**Context.** For finite simple G, a dominating set meets every closed neighbourhood. Let Γ(G) be the largest size of an inclusion-minimal dominating set. R_k(G) has dominating sets of size at most k as vertices, adjacent when one vertex is added or deleted. Treewidth tw(G), respectively pathwidth pw(G), minimizes largest bag size minus one over tree, respectively path, decompositions: bags cover vertices and edges, and bags containing each vertex form a connected subtree.

**Source.** Alice Joffard. *Graph domination and reconfiguration problems*. Université de Lyon, 2020. Advisor(s): Hamamache Kheddouci; co-director Nicolas Bousquet. [primary source](https://perso.liris.cnrs.fr/ajoffard/manuscript.pdf) Location: Origins: thesis Conjecture 5.1, p.66, and discussion, p.118; linked Bousquet–Joffard–Ouvrard ISAAC 2020 paper, pp.3–5, and Bousquet's habilitation Question 110, p.107.

**Literature check.** Status checked 11 October 2026: cited final and later habilitation checked; no matching resolution located.

**Further links.** [1](https://doi.org/10.4230/LIPIcs.ISAAC.2020.37) · [2](https://perso.liris.cnrs.fr/nbousquet/Habilitation_defense.pdf)


<a id="q4417"></a>

## Q4417. For every l-stem v with l≥1, is a_v(G)≤(4n+1)/6, with equality exactly when l=1 and G is star-like?

**Status:** Open · **Kind:** open problem · **Collection** 45

For every l-stem v with l≥1, is a_v(G)≤(4n+1)/6, with equality exactly when l=1 and G is star-like?

**Context.** Setup: G is a finite simple graph with n≥2 vertices and no isolated vertices. A dominating set contains or neighbors every vertex. Let a_v(G) be the mean cardinality of all dominating sets containing v. A leaf has degree1; an l-stem has exactly l leaf neighbors. Call G star-like if every vertex is either a leaf or a stem with one or two leaf neighbors.

**Source.** Tingyun Chen, Weihua He, Hong-Jian Lai and Jianping Li. *On the local average order of dominating sets*. 2026. [primary source](https://arxiv.org/abs/2610.11446v1) Location: Conjecture6.1, p.12; definitions pp.1–2,9.

**Literature check.** Status: The current version poses this conjecture; searches through11October2026 found no matching resolution. The paper proves strict inequality for l≥2, leaving the general1-stem case.


<a id="q4418"></a>

## Q4418. Characterize all graphs H such that, for every integer k≥1, only finitely many k-vertex-critical…

**Status:** Open · **Kind:** open problem (Problem 4.2) · **Collection** 45

Characterize all graphs H such that, for every integer k≥1, only finitely many k-vertex-critical graphs are {2P3,H}-free.

**Context.** Setup: Graphs are finite and simple; χ is chromatic number. A graph is k-vertex-critical if χ(G)=k and every proper induced subgraph is (k−1)-colorable. F-free means containing no induced copy of any graph in F. P3 is the three-vertex path; 2P3 is two disjoint copies. Finiteness counts isomorphism types.

**Source.** Iain Beaton, Ben Cameron and Adam van Omme. *Obstructions to k-colouring H-free graphs*. 2026. [primary source](https://arxiv.org/abs/2610.10737v1) Location: Problem 4.2, pp.8–9.

**Literature check.** Status: Both questions remain posed in the current version; no matching resolution located through11October2026.


<a id="q4419"></a>

## Q4419. For every fixed k≥4, does there exist a finite nonempty family F of pairwise nonisomorphic…

**Status:** Open · **Kind:** open problem (Problem 4.3) · **Collection** 45

For every fixed k≥4, does there exist a finite nonempty family F of pairwise nonisomorphic graphs, each with chromatic number less than k, and an integer m≥k, such that F-free graphs include infinitely many m-vertex-critical graphs and infinitely many (m+1)-chromatic graphs, but only finitely many (m+1)-vertex-critical graphs?

**Context.** Setup: Graphs are finite and simple; χ is chromatic number. A graph is k-vertex-critical if χ(G)=k and every proper induced subgraph is (k−1)-colorable. F-free means containing no induced copy of any graph in F. P3 is the three-vertex path; 2P3 is two disjoint copies. Finiteness counts isomorphism types.

**Source.** Iain Beaton, Ben Cameron and Adam van Omme. *Obstructions to k-colouring H-free graphs*. 2026. [primary source](https://arxiv.org/abs/2610.10737v1) Location: Problem 4.3, pp.8–9.

**Literature check.** Status: Both questions remain posed in the current version; no matching resolution located through11October2026.


<a id="q4424"></a>

## Q4424. Fractional graph coloring. Let D be a finite loopless digraph with no parallel arcs; opposite…

**Status:** Open · **Kind:** open problem · **Collection** 45

Fractional graph coloring. Let D be a finite loopless digraph with no parallel arcs; opposite arcs are allowed. Write N⁺(v) for the outneighbors of v. A vertex set S is majority-stable if |N⁺(v)∩S|≤|N⁺(v)|/2 for every v∈S. Define χ\*maj(D) as the minimum Σ\_S w_S over nonnegative real weights on majority-stable sets, subject to Σ\_{S∋v}w_S≥1 for every vertex v. A strongly connected component is terminal if no arc leaves it. If no terminal strongly connected component of D is isomorphic to the directed three-cycle, must χ\*maj(D)≤8/3?

**Context.** Primary: https://arxiv.org/abs/2610.11997 , version 1, October 8, 2026.

**Source.** Walid Ben-Ameur and Alessandro Maddaloni. *Fractional majority coloring of digraphs: bounds and inapproximability*. [primary source](https://arxiv.org/abs/2610.11997) Location: Walid Ben-Ameur and Alessandro Maddaloni, “Fractional majority coloring of digraphs: bounds and inapproximability,” §7, the second extremal question.

**Literature check.** Status checked: 2026-10-11; the current primary explicitly asks this bound and gives a sharpness example, with no later matching resolution located.


<a id="q4425"></a>

## Q4425. Does restricting the defining test for stack(G) to almost stacked configurations leave its value…

**Status:** Open · **Kind:** open problem · **Collection** 45

Does restricting the defining test for stack(G) to almost stacked configurations leave its value unchanged for every G?

**Context.** Origin: Tamás Csernák–Lajos Soukup, “The Almost Stacked Hypothesis,” Hypothesis3.2(1–2) and §6.4; paper-origin, continuing their earlier stacking/clearing work.

**Source.** Tamás Csernák and Lajos Soukup. *The Almost Stacked Hypothesis*. [primary source](https://arxiv.org/abs/2610.09650) Location: Tamás Csernák–Lajos Soukup, “The Almost Stacked Hypothesis,” Hypothesis3.2(1–2) and §6.4; paper-origin, continuing their earlier stacking/clearing work.

**Literature check.** Status checked: 2026-10-11; current versions retain these questions. No matching later resolution located.

**Further links.** [1](https://arxiv.org/abs/2604.22341)


<a id="q4426"></a>

## Q4426. Does the analogous restriction leave clear(G) unchanged for every non-bipartite G?

**Status:** Open · **Kind:** open problem · **Collection** 45

Does the analogous restriction leave clear(G) unchanged for every non-bipartite G?

**Context.** Origin: Tamás Csernák–Lajos Soukup, “The Almost Stacked Hypothesis,” Hypothesis3.2(1–2) and §6.4; paper-origin, continuing their earlier stacking/clearing work.

**Source.** Tamás Csernák and Lajos Soukup. *The Almost Stacked Hypothesis*. [primary source](https://arxiv.org/abs/2610.09650) Location: Tamás Csernák–Lajos Soukup, “The Almost Stacked Hypothesis,” Hypothesis3.2(1–2) and §6.4; paper-origin, continuing their earlier stacking/clearing work.

**Literature check.** Status checked: 2026-10-11; current versions retain these questions. No matching later resolution located.

**Further links.** [1](https://arxiv.org/abs/2604.22341)


<a id="q4427"></a>

## Q4427. Determine a threshold function for G(n,p) to be connected, non-bipartite and satisfy…

**Status:** Open · **Kind:** open problem · **Collection** 45

Determine a threshold function for G(n,p) to be connected, non-bipartite and satisfy clear(G)=n+1, as n→∞; edges of G(n,p) occur independently with probability p.

**Context.** Origin: Tamás Csernák–Lajos Soukup, “The Almost Stacked Hypothesis,” Hypothesis3.2(1–2) and §6.4; paper-origin, continuing their earlier stacking/clearing work.

**Source.** Tamás Csernák and Lajos Soukup. *The Almost Stacked Hypothesis*. [primary source](https://arxiv.org/abs/2610.09650) Location: Tamás Csernák–Lajos Soukup, “The Almost Stacked Hypothesis,” Hypothesis3.2(1–2) and §6.4; paper-origin, continuing their earlier stacking/clearing work.

**Literature check.** Status checked: 2026-10-11; current versions retain these questions. No matching later resolution located.

**Further links.** [1](https://arxiv.org/abs/2604.22341)


<a id="q4428"></a>

## Q4428. For every positive integer r and every nonempty n-vertex 2r-regular simple graph G, is…

**Status:** Open · **Kind:** conjecture (Conjecture 5.1) · **Collection** 45

For every positive integer r and every nonempty n-vertex 2r-regular simple graph G, is |F_2(G)|^{1/n} ≤ |F_2(K_{2r,2r})|^{1/(4r)}?

**Context.** DL-S22 | Extremal enumerative graph theory. Genealogy (separate author-homepage source DL-S23): Lee is in KAIST’s integrated master’s/doctoral program (2023–present), advised by Jaehoon Kim; no completed doctorate is asserted. https://sites.google.com/view/hyunwoo-lee/ Setup: For a finite simple graph H, let F_2(H) be its set of spanning 2-regular subgraphs, counted as distinct edge sets. Let K_{2r,2r} be the complete bipartite graph with both parts of size 2r.

**Source.** Hyunwoo Lee. *A counting version of Petersen’s 2-factor theorem*. 2026. [primary source](https://arxiv.org/abs/2610.10424v1) Location: Conjecture 5.1, p.14.

**Literature check.** Status checked 11 October 2026: the current primary version explicitly conjectures this exact extremal bound. Its asymptotically sharp large-degree theorem does not settle the displayed inequality; no matching later resolution was found.

**Further links.** [1](https://sites.google.com/view/hyunwoo-lee/)


<a id="q4429"></a>

## Q4429. For T=C^{(r)} with integer r≥6, or T=S^{(r)} with integer r≥7, does every integer n≥3 admit…

**Status:** Open · **Kind:** conjecture (Conjecture 5.1) · **Collection** 45

For T=C^{(r)} with integer r≥6, or T=S^{(r)} with integer r≥7, does every integer n≥3 admit integers 2≤ℓ≤u≤n−1 such that the three row segments (T_{n,k})\_{k=1}^{ℓ}, (T_{n,k})\_{k=ℓ−1}^{u+1}, and (T_{n,k})\_{k=u}^{n} are respectively strictly log-concave, strictly log-convex, and strictly log-concave?

**Context.** DL-S24 | Enumerative combinatorics. Setup: C^{(r)}\_{n,k} counts permutations of [n+(r−1)k] with k cycles, each having at least r elements. S^{(r)}\_{n,k} counts partitions of that set into k blocks, each of size at least r. A sequence (a_k) is strictly log-concave, respectively strictly log-convex, if a_k²>a_{k−1}a_{k+1}, respectively a_k²&lt;a_{k−1}a_{k+1}, at every internal index.

**Source.** William Y.C. Chen and Elena L. Wang. *The Higher-order Stirling Triangles*. 2026. [primary source](https://arxiv.org/abs/2610.09362v1) Location: Conjecture 5.1, p.36; definitions p.2.

**Literature check.** Status checked 11 October 2026: current v1 expressly leaves this overlapping three-segment pattern conjectural. Earlier triangle-total-positivity and Hankel questions are different; no matching resolution was located.

**Results.**

- **Investigated, unresolved** (B3-ALL-TARGETS-STOP-REGISTER: Reviewed B3 failed routes and per-target stopping decisions): 45 targets have each reached five consecutive substantive distinct full-target failures. STATUS.json records every accepted route, written analysis, evidence path and review provenance. Partial results do not reset counters. Rejected proposed attempts, source-range replays, service errors and shared mechanisms remain explicit rather than supplying extra counts. Remaining/limits: These questions remain mathematically unresolved. A failure-limit stop is an operational disposition, not a counterexample or proof. Missing historical archives remain separate evidence issues. [Report](../../solutions/b3-all-targets-2026-10-13/STATUS.json).


<a id="q4430"></a>

## Q4430. For every integer i≥1, does a polynomial P_i(x)∈ℤ[x] of degree exactly 3i−2 satisfy…

**Status:** Open · **Kind:** conjecture (Conjecture 15) · **Collection** 45

For every integer i≥1, does a polynomial P_i(x)∈ℤ[x] of degree exactly 3i−2 satisfy x^iS_{−i}(x)=S_0(x)C(x)^{−i}+P_i(x)/(1−x)^i as an identity of formal power series?

**Context.** DL-S25 | Enumerative combinatorics. Actual earlier origin: Claesson–Franklín–Steingrímsson, Permutations with Few Inversions, Electronic Journal of Combinatorics 30(4), P4.7 (6 October 2023), Conjecture 15. https://doi.org/10.37236/12075 Setup: Let I_n(k) count permutations π of {1,…,n} with k pairs a&lt;b satisfying π(a)>π(b), with I_0(0)=1 and other impossible counts zero. For integer j set S_j(x)=Σ\_{n≥0}I_n(n−j)x^n. Let C(x)=Σ\_{n≥0}binom(2n,n)x^n/(n+1).

**Source.** Anders Claesson, Atli Fannar Franklín and Einar Steingrímsson. *Permutations with few inversions*. 2023. [primary source](https://doi.org/10.37236/12075) Location: Paper Conjecture 15; doctoral reproduction Conjecture 15, p.55.

**Literature check.** Status checked 11 October 2026: the publisher’s final paper and doctoral reproduction retain the conjecture. Searches found no matching subsequent resolution; ordinary subdiagonal identities and pattern-restricted inversion enumerations do not settle it.


<a id="q4431"></a>

## Q4431. If a graph class C has the property that G≡\_C H implies G≅H whenever G and H have simple…

**Status:** Open · **Kind:** open problem · **Collection** 45

If a graph class C has the property that G≡\_C H implies G≅H whenever G and H have simple spectrum, must C contain, for every integer t≥1, a graph having K_t as a minor?

**Context.** DL-S26 | Algebraic graph theory / graph isomorphism. Setup: All graphs are finite, simple and undirected. Write G≡\_C H when hom(F,G)=hom(F,H) for every F∈C, where hom counts adjacency-preserving vertex maps. A graph has simple spectrum when its adjacency eigenvalues are pairwise distinct; its nullity is the dimension of the adjacency matrix’s kernel. Let D_3 consist of all graphs of maximum degree at most three.

**Source.** Takanori Maehara. *Distinguishing graphs with simple spectrum by homomorphism counts*. 2026. [primary source](https://arxiv.org/abs/2610.09042v1) Location: Remark 11, p.12.

**Literature check.** Status checked 11 October 2026: v1 explicitly leaves both questions open. Necessity of a K_7 minor and the proved nullity-at-most-one case do not settle them; nullity-three counterexamples do not refute the second question. No later matching resolution was found.


<a id="q4432"></a>

## Q4432. If G has nullity two and H is arbitrary, does G≡\_{D_3}H imply G≅H?

**Status:** Open · **Kind:** open problem · **Collection** 45

If G has nullity two and H is arbitrary, does G≡\_{D_3}H imply G≅H?

**Context.** DL-S26 | Algebraic graph theory / graph isomorphism. Setup: All graphs are finite, simple and undirected. Write G≡\_C H when hom(F,G)=hom(F,H) for every F∈C, where hom counts adjacency-preserving vertex maps. A graph has simple spectrum when its adjacency eigenvalues are pairwise distinct; its nullity is the dimension of the adjacency matrix’s kernel. Let D_3 consist of all graphs of maximum degree at most three.

**Source.** Takanori Maehara. *Distinguishing graphs with simple spectrum by homomorphism counts*. 2026. [primary source](https://arxiv.org/abs/2610.09042v1) Location: Remark 17, p.22.

**Literature check.** Status checked 11 October 2026: v1 explicitly leaves both questions open. Necessity of a K_7 minor and the proved nullity-at-most-one case do not settle them; nullity-three counterexamples do not refute the second question. No later matching resolution was found.


<a id="q4433"></a>

## Q4433. Determine inf{c∈ℝ\_{>0}: for every integer ℓ≥1, every ⌈cℓ⌉-connected G admits V(G)=S⊔T with…

**Status:** Open · **Kind:** open problem · **Collection** 45

Determine inf{c∈ℝ\_{>0}: for every integer ℓ≥1, every ⌈cℓ⌉-connected G admits V(G)=S⊔T with G[S],G[T] both ℓ-connected and every vertex of S having at least ℓ neighbors in T}.

**Context.** DL-S29 | Structural graph theory. Primary: Jia Zhou, Jin Yan, Yunshu Gao, A linear bound for a connectivity partition in graphs, arXiv:2610.09365v1 (7 October 2026), §4, p.8. Earlier directed origin: Kühn–Osthus–Townsend, arXiv:1309.7677; reproduced in Timothy Duncan Townsend’s Extremal problems on graphs, directed graphs and hypergraphs, Birmingham PhD thesis, Question 3.1.4, p.48 (submitted August 2015; repository year 2016). Advisors: Daniela Kühn, Deryk Osthus. Setup: Graphs are finite. G is simple undirected; D is loopless with no parallel arcs, allowing opposite arcs. (Strongly) k-connected means having more than k vertices and remaining (strongly) connected after deletion of fewer than k vertices.

**Source.** Jia Zhou, Jin Yan and Yunshu Gao. *A linear bound for a connectivity partition in graphs*. [primary source](https://arxiv.org/abs/2610.09365v1) Location: §4, p.8.

**Literature check.** Status checked 11 October 2026: the 641 bound leaves the optimum undetermined. The directed question is retained in Girão–Letzter’s 2025 final, Question 5.2, and the 2026 primary; the solved tournament case does not settle it.

**Further links.** [1](https://arxiv.org/abs/1309.7677)


<a id="q4434"></a>

## Q4434. Does some g:ℕ\_{≥1}→ℕ\_{≥1} ensure that every strongly g(k)-connected D admits V(D)=A⊔B with…

**Status:** Open · **Kind:** open problem · **Collection** 45

Does some g:ℕ\_{≥1}→ℕ\_{≥1} ensure that every strongly g(k)-connected D admits V(D)=A⊔B with D[A],D[B] both strongly k-connected, for every k≥1?

**Context.** DL-S29 | Structural graph theory. Primary: Jia Zhou, Jin Yan, Yunshu Gao, A linear bound for a connectivity partition in graphs, arXiv:2610.09365v1 (7 October 2026), §4, p.8. Earlier directed origin: Kühn–Osthus–Townsend, arXiv:1309.7677; reproduced in Timothy Duncan Townsend’s Extremal problems on graphs, directed graphs and hypergraphs, Birmingham PhD thesis, Question 3.1.4, p.48 (submitted August 2015; repository year 2016). Advisors: Daniela Kühn, Deryk Osthus. Setup: Graphs are finite. G is simple undirected; D is loopless with no parallel arcs, allowing opposite arcs. (Strongly) k-connected means having more than k vertices and remaining (strongly) connected after deletion of fewer than k vertices.

**Source.** Jia Zhou, Jin Yan and Yunshu Gao. *A linear bound for a connectivity partition in graphs*. [primary source](https://arxiv.org/abs/2610.09365v1) Location: §4, p.8.

**Literature check.** Status checked 11 October 2026: the 641 bound leaves the optimum undetermined. The directed question is retained in Girão–Letzter’s 2025 final, Question 5.2, and the 2026 primary; the solved tournament case does not settle it.

**Further links.** [1](https://arxiv.org/abs/1309.7677)


<a id="q4443"></a>

## Q4443. Unimodality of the shuffle eigenvalue polynomials

**Status:** Open, partial results · **Kind:** open problem (Question 5.28) · **Collection** 45

Let λ/μ be a horizontal strip (at most one box per column), with |λ|=n and |μ|=j. Label its boxes j+1,…,n row-by-row, top-to-bottom and left-to-right. Let c_ℓ be the column index minus row index of box ℓ, and [a]\_q=(1−q^a)/(1−q). For 0≤k≤n−j, set E_{λ/μ}(k)=q^{nk−binom(k,2)} ∑\_{j<ℓ\_1<⋯<ℓ\_k≤n} ∏\_{m=1}^k q^{−ℓ\_m}[ℓ\_m+1−m+c_{ℓ\_m}]\_q. Must each polynomial have unimodal coefficients, meaning they weakly increase and then weakly decrease?

**Source.** Sarah Brauner, Patricia Commins, Darij Grinberg and Franco Saliola. *The q-deformed random-to-random family in the Hecke algebra*. 2025. [primary source](https://arxiv.org/abs/2503.17580v3) Location: Question 5.28, p. 33; formula (5.8), p. 24, and definitions, pp. 18–22.

**Literature check.** Status checked 11 October 2026: the current full paper retains the question; its 2026 conference abstract supplies no resolution. The single-row case is proved.

**Results.**

- **Partial result**: For every horizontal strip and ambient size, E(1) is unimodal because its interval summands share an integer center. E(N) is a product of positive q-integers and is palindromic unimodal. Together with E(0)=1 this covers every rank when N<=2. General intermediate ranks 2<=k&lt;N remain unresolved. The fresh bounded construction beyond source size 28 supplies no full proof. Internally reviewed at this scope; no novelty or external peer-review claim. [Details](../../solutions/b3-all-targets-2026-10-13/shuffle-eigenvalues/RESULTS.md).
- **Partial result** (B3-ALL-TARGETS-Q4443-ENDPOINTS: Every horizontal-strip eigenvalue at endpoint ranks): For every horizontal strip and ambient size, E(1) is unimodal because its interval summands share an integer center. E(N) is a product of positive q-integers and is palindromic unimodal. Together with E(0)=1 this covers every rank when N<=2. Remaining/limits: General intermediate ranks 2<=k&lt;N remain unresolved. The fresh bounded construction beyond source size 28 supplies no full proof. [Report](../../solutions/b3-all-targets-2026-10-13/shuffle-eigenvalues/RESULTS.md).
- **Investigated, unresolved** (B3-ALL-TARGETS-STOP-REGISTER: Reviewed B3 failed routes and per-target stopping decisions): 45 targets have each reached five consecutive substantive distinct full-target failures. STATUS.json records every accepted route, written analysis, evidence path and review provenance. Partial results do not reset counters. Rejected proposed attempts, source-range replays, service errors and shared mechanisms remain explicit rather than supplying extra counts. Remaining/limits: These questions remain mathematically unresolved. A failure-limit stop is an operational disposition, not a counterexample or proof. Missing historical archives remain separate evidence issues. [Report](../../solutions/b3-all-targets-2026-10-13/STATUS.json).

**Further links.** [1](https://arxiv.org/abs/2503.17580)


<a id="q4511"></a>

## Q4511. For which (δ,k) is MP(n,δ,k)−c_{δ,k}n bounded, and for which is this difference eventually…

**Status:** Open · **Kind:** open problem (Problem 51) · **Collection** 46

For which (δ,k) is MP(n,δ,k)−c_{δ,k}n bounded, and for which is this difference eventually periodic in n?

**Context.** DL-S10 — Extremal graph theory Primary-paper source: Yair Caro, Riste Škrekovski and Christina Zarb, Spreads of degrees in maximal planar graphs—an exposition, arXiv:2610.11395v1 (8 October 2026), Problems 51–53, pp.61–62. Setup: Graphs are finite, simple and undirected. Let sp(G,k) be the largest number of vertices whose degrees in G lie within an interval of width k. Let MP(n,δ,k) minimize sp(G,k) over n-vertex edge-maximal planar graphs of minimum degree exactly δ∈{3,4,5}; k≥0 is integral. Write c_{δ,k}=lim_{n→∞}MP(n,δ,k)/n, whose existence and value the paper establishes. Limits and assertions use admissible orders.

**Source.** Yair Caro, Riste Škrekovski and Christina Zarb. *Spreads of degrees in maximal planar graphs—an exposition*. 2026. [primary source](https://arxiv.org/abs/2610.11395) Location: Problem 51, pp.61–62.

**Literature check.** Status checked 11 October 2026: all three remain explicit problems in current v1.

**Further links.** [1](https://arxiv.org/abs/2610.11395v1)


<a id="q4512"></a>

## Q4512. Is MP(n,3,k)≤MP(n,4,k)≤MP(n,5,k) whenever all three are defined?

**Status:** Open · **Kind:** open problem (Problem 52) · **Collection** 46

Is MP(n,3,k)≤MP(n,4,k)≤MP(n,5,k) whenever all three are defined?

**Context.** DL-S10 — Extremal graph theory Primary-paper source: Yair Caro, Riste Škrekovski and Christina Zarb, Spreads of degrees in maximal planar graphs—an exposition, arXiv:2610.11395v1 (8 October 2026), Problems 51–53, pp.61–62. Setup: Graphs are finite, simple and undirected. Let sp(G,k) be the largest number of vertices whose degrees in G lie within an interval of width k. Let MP(n,δ,k) minimize sp(G,k) over n-vertex edge-maximal planar graphs of minimum degree exactly δ∈{3,4,5}; k≥0 is integral. Write c_{δ,k}=lim_{n→∞}MP(n,δ,k)/n, whose existence and value the paper establishes. Limits and assertions use admissible orders.

**Source.** Yair Caro, Riste Škrekovski and Christina Zarb. *Spreads of degrees in maximal planar graphs—an exposition*. 2026. [primary source](https://arxiv.org/abs/2610.11395) Location: Problem 52, pp.61–62.

**Literature check.** Status checked 11 October 2026: all three remain explicit problems in current v1.

**Further links.** [1](https://arxiv.org/abs/2610.11395v1)


<a id="q4513"></a>

## Q4513. Determine an asymptotic formula, for fixed integers d≥1,k≥0, for min_G sp(G,k) over n-vertex…

**Status:** Open · **Kind:** open problem (Problem 53) · **Collection** 46

Determine an asymptotic formula, for fixed integers d≥1,k≥0, for min_G sp(G,k) over n-vertex edge-maximal d-degenerate graphs as n→∞. Here d-degenerate means every nonempty subgraph has a vertex of degree at most d.

**Context.** DL-S10 — Extremal graph theory Primary-paper source: Yair Caro, Riste Škrekovski and Christina Zarb, Spreads of degrees in maximal planar graphs—an exposition, arXiv:2610.11395v1 (8 October 2026), Problems 51–53, pp.61–62. Setup: Graphs are finite, simple and undirected. Let sp(G,k) be the largest number of vertices whose degrees in G lie within an interval of width k. Let MP(n,δ,k) minimize sp(G,k) over n-vertex edge-maximal planar graphs of minimum degree exactly δ∈{3,4,5}; k≥0 is integral. Write c_{δ,k}=lim_{n→∞}MP(n,δ,k)/n, whose existence and value the paper establishes. Limits and assertions use admissible orders.

**Source.** Yair Caro, Riste Škrekovski and Christina Zarb. *Spreads of degrees in maximal planar graphs—an exposition*. 2026. [primary source](https://arxiv.org/abs/2610.11395) Location: Problem 53, pp.61–62.

**Literature check.** Status checked 11 October 2026: all three remain explicit problems in current v1.

**Further links.** [1](https://arxiv.org/abs/2610.11395v1)


<a id="q4514"></a>

## Q4514. Must p(G)=c(G) hold for every perfect graph G?

**Status:** Open · **Kind:** open problem (Problem 1) · **Collection** 46

Must p(G)=c(G) hold for every perfect graph G?

**Context.** DL-S11 — Perfect graphs Primary-paper source: András Gyárfás, Márton Marits and Géza Tóth, Partitioning perfect graphs into comparability graphs, arXiv:2408.13523v3 (8 October 2026), Problem 1, p.13; definitions p.2. Setup: A finite simple graph is perfect if every induced subgraph has equal chromatic and clique numbers. A comparability graph joins exactly the comparable distinct elements of some partial order. For a graph G, let c(G) be the minimum number of comparability subgraphs whose edge sets cover E(G), and let p(G) be the corresponding minimum when these edge sets must be pairwise disjoint. Subgraphs need not be induced.

**Source.** András Gyárfás, Márton Marits and Géza Tóth. *Partitioning perfect graphs into comparability graphs*. 2026. [primary source](https://arxiv.org/abs/2408.13523) Location: Problem 1, p.13; definitions p.2.

**Literature check.** Status checked 11 October 2026: current v3 retains the question. Its equality for several subclasses and its almost-all-perfect-graphs theorem do not establish universal equality.

**Further links.** [1](https://arxiv.org/abs/2408.13523v3)


<a id="q4517"></a>

## Q4517. Must s_{k,F}(n)=O_{k,F}(n) as n→∞ for every such k and F?

**Status:** Open · **Kind:** conjecture (Conjecture 1.1) · **Collection** 46

Must s_{k,F}(n)=O_{k,F}(n) as n→∞ for every such k and F?

**Context.** DL-S13 — Hypergraph saturation Primary-paper source: Tianying Xie, A linear upper bound for Berge saturation numbers, arXiv:2610.11409v1 (8 October 2026), Conjecture 1.1, p.2; setup p.1. The conjecture is attributed to English–Gordon–Graber–Methuku–Sullivan, Saturation of Berge hypergraphs (2019), Conjecture 6.3. Setup: Fix k≥2 and a finite nonempty family F of finite simple graphs, each with an edge. A k-uniform hypergraph contains a Berge copy of J if J’s vertices embed injectively and its edges map injectively to hyperedges containing their embedded endpoints. Call H Berge-F-saturated if it contains no such copy for any J∈F, but adding any missing k-element hyperedge creates one. Let s_{k,F}(n) be the minimum number of hyperedges among these n-vertex hypergraphs.

**Source.** Tianying Xie. *A linear upper bound for Berge saturation numbers*. 2026. [primary source](https://arxiv.org/abs/2610.11409) Location: Conjecture 1.1, p.2; setup p.1.

**Literature check.** Status checked 11 October 2026: current v1 proves the single-forbidden-graph case and retains the finite-family conjecture.

**Further links.** [1](https://arxiv.org/abs/2610.11409v1)


<a id="q4519"></a>

## Q4519. Is there a universal integer R≥1 such that every Q_n, n>1, contains an R-dense induced cycle?

**Status:** Open · **Kind:** open problem (Problem 1.6) · **Collection** 46

Is there a universal integer R≥1 such that every Q_n, n>1, contains an R-dense induced cycle?

**Context.** Hypercube origin: the author’s MathOverflow question of 2 September 2026. https://mathoverflow.net/q/514865 Setup: Graphs are simple and undirected, with graph distance d_G. R-dense means every vertex lies within distance R. Cycles may be single vertices. A finite graph is t-tough if deleting any vertex separator S leaves at most |S|/t components. Q_n has vertex set {0,1}^n, adjacent when one coordinate differs. Checked 11 October 2026: current preprint retains these questions; no matching resolution located.

**Source.** Agelos Georgakopoulos. *Asymptotic connectivity, hamiltonicity and toughness*. 2026. [primary source](https://arxiv.org/abs/2610.09992) Location: Problem 1.6, pp.5,8.

**Literature check.** Status: Checked 11 October 2026: current preprint retains these questions; no matching resolution located.

**Further links.** [1](https://mathoverflow.net/q/514865) · [2](https://arxiv.org/abs/2610.09992v1)


<a id="q4520"></a>

## Q4520. For which t>0 does some integer R≥1 ensure an R-dense cycle in every finite t-tough graph?…

**Status:** Open · **Kind:** open problem (Problem 1.8) · **Collection** 46

For which t>0 does some integer R≥1 ensure an R-dense cycle in every finite t-tough graph? Determine the optimal dependence of R on t.

**Context.** Hypercube origin: the author’s MathOverflow question of 2 September 2026. https://mathoverflow.net/q/514865 Setup: Graphs are simple and undirected, with graph distance d_G. R-dense means every vertex lies within distance R. Cycles may be single vertices. A finite graph is t-tough if deleting any vertex separator S leaves at most |S|/t components. Q_n has vertex set {0,1}^n, adjacent when one coordinate differs. Checked 11 October 2026: current preprint retains these questions; no matching resolution located.

**Source.** Agelos Georgakopoulos. *Asymptotic connectivity, hamiltonicity and toughness*. 2026. [primary source](https://arxiv.org/abs/2610.09992) Location: Problem 1.8, pp.5,8.

**Literature check.** Status: Checked 11 October 2026: current preprint retains these questions; no matching resolution located.

**Further links.** [1](https://mathoverflow.net/q/514865) · [2](https://arxiv.org/abs/2610.09992v1)


<a id="q4521"></a>

## Q4521. For every Cayley graph G of a group with a finite symmetric generating set excluding the…

**Status:** Open · **Kind:** open problem (Problem 1.15) · **Collection** 46

For every Cayley graph G of a group with a finite symmetric generating set excluding the identity, and every integer d≥1, do integers R,D≥1 and an R-dense subtree T⊆G exist such that whenever x,y∈V(T) satisfy d_G(x,y)≤d, their T-path has diameter at most D measured in G?

**Context.** Hypercube origin: the author’s MathOverflow question of 2 September 2026. https://mathoverflow.net/q/514865 Setup: Graphs are simple and undirected, with graph distance d_G. R-dense means every vertex lies within distance R. Cycles may be single vertices. A finite graph is t-tough if deleting any vertex separator S leaves at most |S|/t components. Q_n has vertex set {0,1}^n, adjacent when one coordinate differs. Checked 11 October 2026: current preprint retains these questions; no matching resolution located.

**Source.** Agelos Georgakopoulos. *Asymptotic connectivity, hamiltonicity and toughness*. 2026. [primary source](https://arxiv.org/abs/2610.09992) Location: Problem 1.15, pp.5,8.

**Literature check.** Status: Checked 11 October 2026: current preprint retains these questions; no matching resolution located.

**Further links.** [1](https://mathoverflow.net/q/514865) · [2](https://arxiv.org/abs/2610.09992v1)


<a id="q4523"></a>

## Q4523. Does κ(D)≥α₂(D)+1 force a directed cycle through every vertex?

**Status:** Open · **Kind:** open problem · **Collection** 46

Does κ(D)≥α₂(D)+1 force a directed cycle through every vertex?

**Context.** Setup: D is a finite loopless digraph without parallel arcs; opposite arcs are allowed. Let α₂(D) be the largest size of a vertex set containing no directed 2-cycle. The digraph is k-strong if |V(D)|≥k+1 and deleting any fewer than k vertices leaves directed paths between every ordered pair of surviving vertices. Let κ(D) be the largest such k, or zero if D is not strongly connected or has at most one vertex. Checked 11 October 2026: the current paper improves the sufficient bound but retains this conjecture. Its pancyclicity counterexample concerns a different target.

**Source.** Chengli Li and Bo Ning. *A near-linear Chvátal–Erdős condition for Hamilton cycles in digraphs*. 2026. [primary source](https://arxiv.org/abs/2610.10292) Location: §1, p.2.

**Further links.** [1](https://arxiv.org/abs/2610.10292v1)


<a id="q4524"></a>

## Q4524. Characterize the connected bipartite graphs B admitting a perfect matching for which…

**Status:** Open · **Kind:** open problem (Problem 1) · **Collection** 46

Characterize the connected bipartite graphs B admitting a perfect matching for which f(B^{□k})=⌈√k⌉ for every k≥1.

**Context.** Setup: Graphs are finite and simple. Let α(G) be the maximum size of an independent vertex set and Δ(G) its maximum degree. Define f_t(G)=min{Δ(G[U]):U⊆V(G), |U|=α(G)+t} whenever 1≤t≤|V(G)|−α(G), and f=f₁. The Cartesian power B^{□k} has k-tuples as vertices, adjacent when they agree except in one coordinate containing adjacent vertices of B. Let Q_n=K₂^{□n}. Checked 11 October 2026: current preprint retains both targets; its results for matched-bridge factors and other hypercube dimensions do not settle them. No matching later resolution located.

**Source.** Zhen-Mu Hong, Zi-Yi Wu and Zheng-Jiang Xia. *Graph Sensitivity of Cartesian Products with Matched Bridges*. 2026. [primary source](https://arxiv.org/abs/2610.09483) Location: Problem 1, pp.15–16.

**Literature check.** Status: Checked 11 October 2026: current preprint retains both targets; its results for matched-bridge factors and other hypercube dimensions do not settle them. No matching later resolution located.

**Further links.** [1](https://arxiv.org/abs/2610.09483v1)


<a id="q4525"></a>

## Q4525. Is f₂(Q₉) equal to 3 or 4?

**Status:** Open · **Kind:** open problem (Problem 2) · **Collection** 46

Is f₂(Q₉) equal to 3 or 4?

**Context.** Setup: Graphs are finite and simple. Let α(G) be the maximum size of an independent vertex set and Δ(G) its maximum degree. Define f_t(G)=min{Δ(G[U]):U⊆V(G), |U|=α(G)+t} whenever 1≤t≤|V(G)|−α(G), and f=f₁. The Cartesian power B^{□k} has k-tuples as vertices, adjacent when they agree except in one coordinate containing adjacent vertices of B. Let Q_n=K₂^{□n}. Checked 11 October 2026: current preprint retains both targets; its results for matched-bridge factors and other hypercube dimensions do not settle them. No matching later resolution located.

**Source.** Zhen-Mu Hong, Zi-Yi Wu and Zheng-Jiang Xia. *Graph Sensitivity of Cartesian Products with Matched Bridges*. 2026. [primary source](https://arxiv.org/abs/2610.09483) Location: Problem 2, pp.15–16.

**Literature check.** Status: Checked 11 October 2026: current preprint retains both targets; its results for matched-bridge factors and other hypercube dimensions do not settle them. No matching later resolution located.

**Further links.** [1](https://arxiv.org/abs/2610.09483v1)


<a id="q4526"></a>

## Q4526. What is the computational complexity of computing χFAT(G) exactly?

**Status:** Open · **Kind:** open problem (Question 2) · **Collection** 46

What is the computational complexity of computing χFAT(G) exactly?

**Context.** Setup: G is a finite connected simple graph with at least two vertices. A FAT k-coloring is a partition into nonempty classes V₁,…,V_k for which constants α,β∈[0,1], β=1−(k−1)α, satisfy: every vertex v has αdeg(v) neighbors in each other class and βdeg(v) neighbors in its own class. For k=1 take α=0. Define χFAT(G) as the largest possible k. Checked 11 October 2026: current Question 2 persists; inspected subsequent structural and irreducible-coloring results do not determine this computational complexity.

**Source.** Lies Beers and Raffaella Mulas. *Fair and Tolerant (FAT) Graph Colorings*. 2026. [primary source](https://arxiv.org/abs/2510.18494) Location: Question 2, p.23.

**Further links.** [1](https://arxiv.org/abs/2510.18494v3)


<a id="q4547"></a>

## Q4547. Higher resonance linearity

**Status:** Open · **Kind:** open problem · **Collection** 46

If M is not realizable over C, must every irreducible component of R^q(M) be a linear subspace defined over Q, for every q≥2?

**Context.** For a finite simple matroid M on [n], define A=∧\_C(e₁,…,e_n)/⟨∂e_C:C a circuit⟩, where ∂ is the graded derivation with ∂e_i=1. Set R^q(M)={a∈A¹:H^q(A,a∧−)≠0}. Let μ:∧²A¹→A² be multiplication and h=Lie((A¹)\*)/⟨im μ\*⟩. Put θ\_r=dim_C(h/[h′,h′])\_r, where h′=[h,h], and let c_m count the m-dimensional irreducible components of R¹(M). Checked 11 October 2026: the final survey retains these targets; no later general resolution located.

**Source.** Alexandru Suciu. *Resonance varieties and Lie algebras of matroids and hyperplane arrangements*. 2025. [primary source](https://bulletin.ssmr.ro/pdf/68-3/articol_9.pdf) Location: Question5.6, p374.

**Literature check.** Status: Checked 11 October 2026: the final survey retains these targets; no later general resolution located.


<a id="q4548"></a>

## Q4548. Holonomy Chen ranks

**Status:** Open · **Kind:** open problem · **Collection** 46

For every M, does θ\_r=(r−1)∑\_{m≥2}c_m binom(m+r−2,r) hold for all sufficiently large r?

**Context.** For a finite simple matroid M on [n], define A=∧\_C(e₁,…,e_n)/⟨∂e_C:C a circuit⟩, where ∂ is the graded derivation with ∂e_i=1. Set R^q(M)={a∈A¹:H^q(A,a∧−)≠0}. Let μ:∧²A¹→A² be multiplication and h=Lie((A¹)\*)/⟨im μ\*⟩. Put θ\_r=dim_C(h/[h′,h′])\_r, where h′=[h,h], and let c_m count the m-dimensional irreducible components of R¹(M). Checked 11 October 2026: the final survey retains these targets; no later general resolution located.

**Source.** Alexandru Suciu. *Resonance varieties and Lie algebras of matroids and hyperplane arrangements*. 2025. [primary source](https://bulletin.ssmr.ro/pdf/68-3/articol_9.pdf) Location: Conjecture4.14, p369; Theorem4.9 identifies components with multinets.

**Literature check.** Status: Checked 11 October 2026: the final survey retains these targets; no later general resolution located.


<a id="q4591"></a>

## Q4591. Find a positive combinatorial Littlewood–Richardson rule for O_{λμ}^ν in ξ\_λξ\_μ=Σ\_ν O_{λμ}^ν ξ\_ν…

**Status:** Open · **Kind:** open problem · **Collection** 46

Find a positive combinatorial Littlewood–Richardson rule for O_{λμ}^ν in ξ\_λξ\_μ=Σ\_ν O_{λμ}^ν ξ\_ν in H_T^\*(Y;ℤ), where T is the diagonal maximal torus and ξ\_λ are equivariant Schubert classes. Positivity means nonnegative coefficients in γ\_1=t_1 and γ\_i=t_i−t_{i−1} (i>1), with H_T^\*(pt;ℤ)=ℤ[t_1,…,t_n].

**Context.** DL-S25 — Algebraic combinatorics Origin: Older Schubert-calculus problems restated on thesis p.43 and in Estupiñán-Salamanca–Pechenik, https://arxiv.org/abs/2503.14609v2, §1. Setup: Let Y=OG(n,2n+1) and Z=LG(n,2n) be complex varieties of maximal isotropic subspaces for nondegenerate symmetric and alternating forms, respectively. Schubert varieties Y_λ,Z_λ are indexed by strict partitions λ⊆(n,n−1,…,1), with codimension |λ|. Checked 12 October 2026: final thesis and latest joint preprint retain both problems; later searches found no general solution.

**Source.** Santiago Estupiñán-Salamanca. *A New Shifted Littlewood–Richardson Rule and Related Developments*. University of Waterloo, 2026. Advisor(s): Oliver Pechenik. [primary source](https://uwspace.uwaterloo.ca/items/7a57b332-02ae-4b04-9f11-b98bbdb628c3) Location: Older Schubert-calculus problems restated on thesis p.43 and in Estupiñán-Salamanca–Pechenik, §1.

**Results.**

- **Investigated, unresolved** (B3-ALL-TARGETS-STOP-REGISTER: Reviewed B3 failed routes and per-target stopping decisions): 45 targets have each reached five consecutive substantive distinct full-target failures. STATUS.json records every accepted route, written analysis, evidence path and review provenance. Partial results do not reset counters. Rejected proposed attempts, source-range replays, service errors and shared mechanisms remain explicit rather than supplying extra counts. Remaining/limits: These questions remain mathematically unresolved. A failure-limit stop is an operational disposition, not a counterexample or proof. Missing historical archives remain separate evidence issues. [Report](../../solutions/b3-all-targets-2026-10-13/STATUS.json).

**Further links.** [1](https://arxiv.org/abs/2503.14609v2)


<a id="q4592"></a>

## Q4592. Find a cancellation-free combinatorial rule for (−1)^{|ν|−|λ|−|μ|}c_{λμ}^ν, where…

**Status:** Open · **Kind:** open problem · **Collection** 46

Find a cancellation-free combinatorial rule for (−1)^{|ν|−|λ|−|μ|}c_{λμ}^ν, where [O_{Z_λ}][O_{Z_μ}]=Σ\_ν c_{λμ}^ν[O_{Z_ν}] in K^0(Z). Here O denotes the structure sheaf.

**Context.** DL-S25 — Algebraic combinatorics Origin: Older Schubert-calculus problems restated on thesis p.43 and in Estupiñán-Salamanca–Pechenik, https://arxiv.org/abs/2503.14609v2, §1. Setup: Let Y=OG(n,2n+1) and Z=LG(n,2n) be complex varieties of maximal isotropic subspaces for nondegenerate symmetric and alternating forms, respectively. Schubert varieties Y_λ,Z_λ are indexed by strict partitions λ⊆(n,n−1,…,1), with codimension |λ|. Checked 12 October 2026: final thesis and latest joint preprint retain both problems; later searches found no general solution.

**Source.** Santiago Estupiñán-Salamanca. *A New Shifted Littlewood–Richardson Rule and Related Developments*. University of Waterloo, 2026. Advisor(s): Oliver Pechenik. [primary source](https://uwspace.uwaterloo.ca/items/7a57b332-02ae-4b04-9f11-b98bbdb628c3) Location: Older Schubert-calculus problems restated on thesis p.43 and in Estupiñán-Salamanca–Pechenik, §1.

**Results.**

- **Investigated, unresolved** (B3-ALL-TARGETS-STOP-REGISTER: Reviewed B3 failed routes and per-target stopping decisions): 45 targets have each reached five consecutive substantive distinct full-target failures. STATUS.json records every accepted route, written analysis, evidence path and review provenance. Partial results do not reset counters. Rejected proposed attempts, source-range replays, service errors and shared mechanisms remain explicit rather than supplying extra counts. Remaining/limits: These questions remain mathematically unresolved. A failure-limit stop is an operational disposition, not a counterexample or proof. Missing historical archives remain separate evidence issues. [Report](../../solutions/b3-all-targets-2026-10-13/STATUS.json).

**Further links.** [1](https://arxiv.org/abs/2503.14609v2)


<a id="q4593"></a>

## Q4593. Fix d≥3. Sample n independent uniform points P⊂[0,1]^d. Join comparable points in coordinatewise…

**Status:** Open · **Kind:** open problem · **Collection** 46

Fix d≥3. Sample n independent uniform points P⊂[0,1]^d. Join comparable points in coordinatewise order when no other point lies strictly between them. Is this graph’s independence number O_d(n loglog n/(log n)^(d−1)) with probability tending to one as n→∞?

**Context.** DL-S26 — Probabilistic combinatorics Origin: Jin–Kwan–Lichev, https://arxiv.org/abs/2501.12373v1, p.2; thesis p.86. Checked 12 October 2026: latest preprints and final thesis read; no matching resolution located.

**Source.** Zhihan Jin. *Unavoidable Structures in Discrete Objects: Ramsey-Theoretic, Geometric and Probabilistic Perspectives*. ETH Zürich, 2026. Advisor(s): Benjamin Sudakov. [primary source](https://doi.org/10.3929/ethz-c-000801028) Location: p.2; thesis p.86.

**Literature check.** Status: Checked 12 October 2026: latest preprints and final thesis read; no matching resolution located.

**Further links.** [1](https://arxiv.org/abs/2501.12373v1)


<a id="q4636"></a>

## Q4636. For every integer n≥2, must every set S⊂S^{n−1}⊂R^n of 2(n+1) unit vectors, such that every…

**Status:** Open · **Kind:** open problem · **Collection** 47

For every integer n≥2, must every set S⊂S^{n−1}⊂R^n of 2(n+1) unit vectors, such that every three distinct points contain a pair with inner product −1/n, partition into two sets of n+1 points, each having pairwise inner product −1/n?

**Context.** Audited provenance and status: Subject: Discrete geometry

**Source.** Bachoc, Bram Bekker, Moustrou and de Oliveira Filho. *Obtuse almost-equiangular sets*. 2025. [primary source](https://arxiv.org/abs/2504.11086v2) Location: Bachoc–Bekker–Moustrou–de Oliveira Filho, Obtuse almost-equiangular sets (2025), §1.3 before Theorem 1.4.

**Further links.** [1](https://arxiv.org/abs/2609.34845v1)


<a id="q4638"></a>

## Q4638. Does a universal constant C exist such that, for every matroid M on [n], nonnegative weights…

**Status:** Open · **Kind:** conjecture (Conjecture 5) · **Collection** 47

Does a universal constant C exist such that, for every matroid M on [n], nonnegative weights w_i, and x in the convex hull of its basis-incidence vectors, some basis B satisfies |Σ\_{i≤t}w_i(1_{i∈B}−x_i)|≤C·max_i w_i simultaneously for every t∈[n]?

**Context.** Kristóf Bérczi, Siyue Liu, Victor Reis and Jakub Tarnawski, Weighted Equitability and Matroid-Constrained Discrepancy, arXiv:2608.13983v1 (14 August 2026), Conjecture 5 and §8. Audited provenance and status: Subject: Combinatorial optimization Mohammed Majthoub Almoghrabi, Machine learning and combinatorial methods for discrete optimization problems, TU Berlin doctoral thesis; accepted 14 November 2025, issued 2026. Advisor Martin Skutella. Current author publication list retains the Bérczi–Liu–Reis–Tarnawski paper as a preprint. Karingula–Lovett v2, §1: the constant Komlós theorem controls the final sum only; its prefix discussion does not settle matroid-constrained rounding. Kintali, ECCC TR26-242, Theorem3.1 and Corollary3.2: counterexamples have growing column sparsity; the linear sparse lower bound leaves a constant after ℓ1 normalization. No matroid-basis result or two-sparse unbounded counterexample is stated.

**Source.** Kristóf Bérczi, Siyue Liu, Victor Reis and Jakub Tarnawski. *Weighted Equitability and Matroid-Constrained Discrepancy*. 2026. [primary source](https://arxiv.org/abs/2608.13983v1) Location: Conjecture 5 and §8.

**Literature check.** Status: Theorem 14 gives O(log n) for the first question; Theorem 17 disproves factor 1 in the second. Both residuals retained in the latest version; checked 12 October 2026.


<a id="q4639"></a>

## Q4639. Let D=(V,A) be a finite acyclic digraph with source s, sink terminals t_1,…,t_n, and demands…

**Status:** Open · **Kind:** conjecture (Conjecture 5) · **Collection** 47

Let D=(V,A) be a finite acyclic digraph with source s, sink terminals t_1,…,t_n, and demands d_j>0. Let x≥0 be an arc flow with incoming flow d_j at t_j and flow conservation at all other vertices except s. Must there be one s–t_j path P_j per terminal such that y_a=Σ\_{j:a∈P_j}d_j satisfies |x_a−y_a|≤2max_j d_j for every arc a?

**Context.** Kristóf Bérczi, Siyue Liu, Victor Reis and Jakub Tarnawski, Weighted Equitability and Matroid-Constrained Discrepancy, arXiv:2608.13983v1 (14 August 2026), Conjecture 5 and §8. Audited provenance and status: Subject: Combinatorial optimization Mohammed Majthoub Almoghrabi, Machine learning and combinatorial methods for discrete optimization problems, TU Berlin doctoral thesis; accepted 14 November 2025, issued 2026. Advisor Martin Skutella. Current author publication list retains the Bérczi–Liu–Reis–Tarnawski paper as a preprint. Karingula–Lovett v2, §1: the constant Komlós theorem controls the final sum only; its prefix discussion does not settle matroid-constrained rounding. Kintali, ECCC TR26-242, Theorem3.1 and Corollary3.2: counterexamples have growing column sparsity; the linear sparse lower bound leaves a constant after ℓ1 normalization. No matroid-basis result or two-sparse unbounded counterexample is stated.

**Source.** Kristóf Bérczi, Siyue Liu, Victor Reis and Jakub Tarnawski. *Weighted Equitability and Matroid-Constrained Discrepancy*. 2026. [primary source](https://arxiv.org/abs/2608.13983v1) Location: Conjecture 5 and §8.

**Literature check.** Status: Theorem 14 gives O(log n) for the first question; Theorem 17 disproves factor 1 in the second. Both residuals retained in the latest version; checked 12 October 2026.


<a id="q4646"></a>

## Q4646. Diameter and cube dimension

**Status:** Open · **Kind:** conjecture (Conjecture 6.4) · **Collection** 47

If the Coxeter graph is triangle-free, does diam B(α) equal the least d admitting a distance-preserving embedding of B(α) into the binary d-cube?

**Context.** Algebraic combinatorics. Barnes–Breland–Ernst–Perry, Braid graphs in simply-laced triangle-free Coxeter systems are median (2024). https://arxiv.org/abs/2408.16839 Let (W,S) be a Coxeter system with S finite and m(s,t)∈{2,3} for distinct generators. For a reduced expression α, let B(α) have vertices the expressions reachable from α using only substitutions sts↔tst with m(s,t)=3; edges are single such substitutions. Commutation moves are excluded. The Coxeter graph has vertex set S and edges where m(s,t)=3. For a finite connected graph G, set I(u,v)={x:d(u,x)+d(x,v)=d(u,v)}. Call G median when every triple u,v,w has exactly one vertex in I(u,v)∩I(u,w)∩I(v,w). Locators: Conjecture6.4; §9(8),(11). These restate master’s-thesis questions, not claims of origin in Breland’s dissertation. Audited provenance and status: Subject: Algebraic combinatorics Pari2026 retains broader diameter/median conjectures; its theorem excludes triangles labelled3,3,m. Checked 12 October 2026: no matching resolution was located.

**Source.** Barnes, Jadyn V. Breland, Ernst and Perry. *Braid graphs in simply-laced triangle-free Coxeter systems are median*. 2024. [primary source](https://arxiv.org/abs/2408.16839v1) Location: Conjecture 6.4, 2024 paper.

**Literature check.** Status: Unread ProQuest route returned a technical fetch error. Research page updated August2026 lists2408.16839 as submitted; Breland–Howard ribbon-polyomino work remains in preparation, with no posted resolution claim.

**Further links.** [1](https://arxiv.org/abs/2408.16839)


<a id="q4647"></a>

## Q4647. Classifying braid graphs

**Status:** Open · **Kind:** open problem · **Collection** 47

Which finite median graphs, up to graph isomorphism, occur as B(α) in triangle-free Coxeter systems above?

**Context.** Algebraic combinatorics. Barnes–Breland–Ernst–Perry, Braid graphs in simply-laced triangle-free Coxeter systems are median (2024). https://arxiv.org/abs/2408.16839 Let (W,S) be a Coxeter system with S finite and m(s,t)∈{2,3} for distinct generators. For a reduced expression α, let B(α) have vertices the expressions reachable from α using only substitutions sts↔tst with m(s,t)=3; edges are single such substitutions. Commutation moves are excluded. The Coxeter graph has vertex set S and edges where m(s,t)=3. For a finite connected graph G, set I(u,v)={x:d(u,x)+d(x,v)=d(u,v)}. Call G median when every triple u,v,w has exactly one vertex in I(u,v)∩I(u,w)∩I(v,w). Locators: Conjecture6.4; §9(8),(11). These restate master’s-thesis questions, not claims of origin in Breland’s dissertation. Audited provenance and status: Subject: Algebraic combinatorics Pari2026 retains broader diameter/median conjectures; its theorem excludes triangles labelled3,3,m. Checked 12 October 2026: no matching resolution was located.

**Source.** Barnes, Jadyn V. Breland, Ernst and Perry. *Braid graphs in simply-laced triangle-free Coxeter systems are median*. 2024. [primary source](https://arxiv.org/abs/2408.16839v1) Location: §9(8), 2024 paper.

**Literature check.** Status: Unread ProQuest route returned a technical fetch error. Research page updated August2026 lists2408.16839 as submitted; Breland–Howard ribbon-polyomino work remains in preparation, with no posted resolution claim.

**Further links.** [1](https://arxiv.org/abs/2408.16839)


<a id="q4648"></a>

## Q4648. Removing triangle-freeness

**Status:** Open · **Kind:** open problem · **Collection** 47

Is B(α) median for every simply-laced Coxeter system above?

**Context.** Algebraic combinatorics. Barnes–Breland–Ernst–Perry, Braid graphs in simply-laced triangle-free Coxeter systems are median (2024). https://arxiv.org/abs/2408.16839 Let (W,S) be a Coxeter system with S finite and m(s,t)∈{2,3} for distinct generators. For a reduced expression α, let B(α) have vertices the expressions reachable from α using only substitutions sts↔tst with m(s,t)=3; edges are single such substitutions. Commutation moves are excluded. The Coxeter graph has vertex set S and edges where m(s,t)=3. For a finite connected graph G, set I(u,v)={x:d(u,x)+d(x,v)=d(u,v)}. Call G median when every triple u,v,w has exactly one vertex in I(u,v)∩I(u,w)∩I(v,w). Locators: Conjecture6.4; §9(8),(11). These restate master’s-thesis questions, not claims of origin in Breland’s dissertation. Audited provenance and status: Subject: Algebraic combinatorics Pari2026 retains broader diameter/median conjectures; its theorem excludes triangles labelled3,3,m. Checked 12 October 2026: no matching resolution was located.

**Source.** Barnes, Jadyn V. Breland, Ernst and Perry. *Braid graphs in simply-laced triangle-free Coxeter systems are median*. 2024. [primary source](https://arxiv.org/abs/2408.16839v1) Location: §9(11), 2024 paper.

**Literature check.** Status: Unread ProQuest route returned a technical fetch error. Research page updated August2026 lists2408.16839 as submitted; Breland–Howard ribbon-polyomino work remains in preparation, with no posted resolution claim.

**Further links.** [1](https://arxiv.org/abs/2408.16839)


<a id="q4656"></a>

## Q4656. If a+b is odd, does every x∈X_A contain every word of L_A?

**Status:** Open · **Kind:** conjecture (Conjecture 7.0.1) · **Collection** 47

If a+b is odd, does every x∈X_A contain every word of L_A?

**Context.** Setup: For integers 1≤a&lt;b, put A={a,b}. Let R list lengths of maximal constant runs. Let X_A comprise right-infinite A-sequences whose every iterated R is defined and remains a right-infinite A-sequence. Let L_A be their combined finite-factor language and p_A(n)=|L_A∩Aⁿ|. Sources: thesis Conjectures7.0.1–2, p89; Cassaigne–Henry, arXiv2603.10733v4, Conjectures1.16/1.19, pp7–8. Theorem1.31 identifies L_A with finite smooth words. DL27 extends Dekking/Sing; DL28 restates their conjecture. The lower bound and both-even case are proved; remaining upper bounds are open. Checked 12 October 2026. Audited provenance and status: Subject: Combinatorics on words Author lists EJC acceptance and an unlinked same-parity manuscript. Latest v4: 16 June2026; no published final identified. Huang’s conflicting exponent uses a wrong derivative (§1.2.5). Older publisher final unread; its exact claims and derivative mismatch are explicitly diagnosed in the current primary paper.

**Source.** Julien Cassaigne and Raphaël Henry. *The complexity of smooth words over binary alphabets*. 2026. [primary source](https://arxiv.org/abs/2603.10733v4) Location: Thesis Conjecture 7.0.1, p.89; Cassaigne–Henry Conjecture 1.16, p.7.


<a id="q4657"></a>

## Q4657. For all integers 1≤a&lt;b, is p_A(n)=Θ(n^ρ), where ρ=log(a+b)/log((a+b)/2)?

**Status:** Open · **Kind:** conjecture (Conjecture 7.0.2) · **Collection** 47

For all integers 1≤a&lt;b, is p_A(n)=Θ(n^ρ), where ρ=log(a+b)/log((a+b)/2)?

**Context.** Setup: For integers 1≤a&lt;b, put A={a,b}. Let R list lengths of maximal constant runs. Let X_A comprise right-infinite A-sequences whose every iterated R is defined and remains a right-infinite A-sequence. Let L_A be their combined finite-factor language and p_A(n)=|L_A∩Aⁿ|. Sources: thesis Conjectures7.0.1–2, p89; Cassaigne–Henry, arXiv2603.10733v4, Conjectures1.16/1.19, pp7–8. Theorem1.31 identifies L_A with finite smooth words. DL27 extends Dekking/Sing; DL28 restates their conjecture. The lower bound and both-even case are proved; remaining upper bounds are open. Checked 12 October 2026. Audited provenance and status: Subject: Combinatorics on words Author lists EJC acceptance and an unlinked same-parity manuscript. Latest v4: 16 June2026; no published final identified. Huang’s conflicting exponent uses a wrong derivative (§1.2.5). Older publisher final unread; its exact claims and derivative mismatch are explicitly diagnosed in the current primary paper.

**Source.** Julien Cassaigne and Raphaël Henry. *The complexity of smooth words over binary alphabets*. 2026. [primary source](https://arxiv.org/abs/2603.10733v4) Location: Thesis Conjecture 7.0.2, p.89; Cassaigne–Henry Conjecture 1.19, p.8.


<a id="q4665"></a>

## Q4665. Must (Σ\_λ c(λ)s_λ)(Σ\_λ d(λ)s_λ)−(Σ\_λ a(λ)s_λ)(Σ\_λ b(λ)s_λ), with all sums over P^ℓ, have…

**Status:** Open, partial results · **Kind:** open problem · **Collection** 47

Must (Σ\_λ c(λ)s_λ)(Σ\_λ d(λ)s_λ)−(Σ\_λ a(λ)s_λ)(Σ\_λ b(λ)s_λ), with all sums over P^ℓ, have nonnegative coefficients in the Schur basis?

**Context.** Setup: For an integer ℓ≥1, let P^ℓ be the partitions with at most ℓ parts, padded with zeros, and let s_λ be the usual Schur symmetric function. Let a,b,c,d:P^ℓ→R≥0 have finite support and satisfy a(λ)b(μ)≤c(⌈(λ+μ)/2⌉)d(⌊(λ+μ)/2⌋) for every λ,μ∈P^ℓ, with coordinatewise rounding. Audited provenance and status: Subject: Algebraic combinatorics Hong Chen, Rutgers PhD, May2026; advisor Siddhartha Sahi. Defense: Hypergeometric series associated with Jack and Macdonald polynomials, 10 March2026. ArXiv history: only v1, 4 June2026. PDF body dated 8 June2026; HTML body dated 24 August2026; author PDF dated 29 May2026. Conjecture11.5 agrees in all three. Pak’s current papers page lists the ADS paper as a preprint.

**Source.** Chan, Hong Chen, Igor Pak and Soskin. *Correlation inequalities for Schur positivity*. 2026. [primary source](https://arxiv.org/abs/2606.06688v1) Location: Correlation inequalities for Schur positivity, arXiv2606.06688v1, Conjecture11.5, p34.

**Literature check.** Status: Source: Correlation inequalities for Schur positivity, arXiv2606.06688v1, Conjecture11.5, p34. This is the four-function Schur-positive Klartag–Lehec conjecture. Checked 12 October2026; no matching resolution found.

**Results.**

- **Partial result**: The full weighted Schur difference is Schur-positive whenever each summed midpoint-output fiber has total input weight at most its c(u)d(v) budget. In particular the frozen pairwise weight hypothesis suffices for injective midpoint support pairs, including either singleton input support. For all legal finite supports the difference has nonnegative values on every nonnegative alphabet. Colliding midpoint fibers need additional compensation. Nonnegative evaluations alone do not imply Schur positivity; the full question remains unresolved. Internally reviewed at this scope; no novelty or external peer-review claim. [Details](../../solutions/b3-all-targets-2026-10-13/schur-midpoints/Q4665-RESULTS.md).
- **Partial result** (B3-ALL-TARGETS-Q4665-INJECTIVE: Schur midpoint positivity with injective output fibers): The full weighted Schur difference is Schur-positive whenever each summed midpoint-output fiber has total input weight at most its c(u)d(v) budget. In particular the frozen pairwise weight hypothesis suffices for injective midpoint support pairs, including either singleton input support. For all legal finite supports the difference has nonnegative values on every nonnegative alphabet. Remaining/limits: Colliding midpoint fibers need additional compensation. Nonnegative evaluations alone do not imply Schur positivity; the full question remains unresolved. [Report](../../solutions/b3-all-targets-2026-10-13/schur-midpoints/Q4665-RESULTS.md).
- **Investigated, unresolved** (B3-ALL-TARGETS-STOP-REGISTER: Reviewed B3 failed routes and per-target stopping decisions): 45 targets have each reached five consecutive substantive distinct full-target failures. STATUS.json records every accepted route, written analysis, evidence path and review provenance. Partial results do not reset counters. Rejected proposed attempts, source-range replays, service errors and shared mechanisms remain explicit rather than supplying extra counts. Remaining/limits: These questions remain mathematically unresolved. A failure-limit stop is an operational disposition, not a counterexample or proof. Missing historical archives remain separate evidence issues. [Report](../../solutions/b3-all-targets-2026-10-13/STATUS.json).


<a id="q4667"></a>

## Q4667. For every integer r≥1, is F_{r,ω} independent of ω, as a formal series in T and p with…

**Status:** Open · **Kind:** open problem · **Collection** 47

For every integer r≥1, is F_{r,ω} independent of ω, as a formal series in T and p with rational-function coefficients in u,q,t?

**Context.** Setup: For a partition λ and cell s=(i,j), put a_s=λ\_i−j, l_s=λ′\_j−i and h_s=a_s+l_s+1. The r-core core_r(λ) remains after successively removing rim r-hooks. With formal parameters u,q,t,p,T, set θ(z;p)=∏\_{j≥0}(1−zp^j)(1−p^{j+1}/z). For an r-core ω define F_{r,ω}=Σ\_{core_r(λ)=ω} T^{(|λ|−|ω|)/r}∏\_{s∈λ:r∣h_s} θ(uq^{a_s+1}t^{l_s};p)θ(u⁻¹q^{a_s}t^{l_s+1};p)/[θ(q^{a_s+1}t^{l_s};p)θ(q^{a_s}t^{l_s+1};p)]. Audited provenance and status: Subject: Algebraic combinatorics Current author PDF retains Eq4.10. FPSAC2026 final, 1 April2026, proves only nonelliptic r≥3. FPSAC final p11 explicitly retains the elliptic core-independence conjecture.

**Source.** Seamus Albion Ferlinc and Joshua Jeishing Wen. *Ext operators for wreath Macdonald polynomials*. 2025. [primary source](https://arxiv.org/abs/2508.10772v1) Location: arXiv2508.10772v1, §4.4.3, Eq4.10, p16; the authors attribute the question to Walsh–Warnaar.

**Literature check.** Status: Source: arXiv2508.10772v1, §4.4.3, Eq4.10, p16; the authors attribute the question to Walsh–Warnaar. This uses the newer paper’s explicit product convention; the older printed theta convention differs. Checked 12 October2026; no matching resolution located.


<a id="q4676"></a>

## Q4676. Is there no nonplanar such G with n≥17, c(G)>binom(n−1,2), and ceil(√n)≤Δ(G)≤(n+1)/2?

**Status:** Open · **Kind:** open problem · **Collection** 47

Is there no nonplanar such G with n≥17, c(G)>binom(n−1,2), and ceil(√n)≤Δ(G)≤(n+1)/2?

**Context.** Setup: For a finite simple C4-free graph G on n vertices, let c(G) count unordered pairs of distinct vertices having a common neighbor; Δ(G) is its maximum degree. C4-free forbids a four-cycle as a subgraph, not merely an induced cycle. Audited provenance and status: Subject: Graph theory Paper v1 dated8September2026, only arXiv version.

**Source.** Michela Ascolese, Negrini, Pagani and Pellegrini. *A Graph Reconstruction Problem Involving Common Neighbors*. 2026. [primary source](https://arxiv.org/abs/2609.08803v1) Location: Thesis §3.5.4 pp112–115 treats the earlier reconstruction problem; the precise nonplanarity target comes from the later paper.

**Literature check.** Status: Checked12October2026; no matching resolution located.


<a id="q4678"></a>

## Q4678. Maximum 2-scattered subspaces in dimension four

**Status:** Open · **Kind:** open problem · **Collection** 47

For every prime power q, does there exist an eight-dimensional F_q-linear subspace U⊆F_{q⁶}⁴ such that its F_{q⁶}-linear span is F_{q⁶}⁴ and dim_{F_q}(U∩H)≤2 for every two-dimensional F_{q⁶}-linear subspace H⊆F_{q⁶}⁴? Such a U is called maximum 2-scattered.

**Context.** Finite geometry. Relevant functions over finite fields and algebraic varieties, dissertation2025, Chapter7; Ghiandoni–Giannoni,2610.08237v1 (October6,2026). https://arxiv.org/abs/2610.08237 Earlier finite-geometry problem restated in the thesis; the current paper singles out its remaining dimension. Audited provenance and status: Subject: Finite geometry Current October paper and thesis inspected. The earlier March2025 publisher full text was not inspected; exact October residual postdates it. Checked 12 October 2026: no matching resolution was located.

**Source.** Francesco Ghiandoni and Alessandro Giannoni. *Maximum 2-scattered subspaces of V(r,q^6)*. 2026. [primary source](https://arxiv.org/abs/2610.08237v1) Location: thesis §7.1, pp111–112; current paper §1 and Remark5.4, p9.

**Literature check.** Status: Checked 12 October 2026: no matching resolution was located.

**Notes.** Constructions are known when q=2^s with s odd; the October paper settles all ambient dimensions r≥3 except r=4 for arbitrary q.

**Further links.** [1](https://arxiv.org/abs/2610.08237)


<a id="q4682"></a>

## Q4682. Is the number of intervals [u,v] in P_{m,n}, including singleton intervals, always…

**Status:** Open · **Kind:** open problem · **Collection** 47

Is the number of intervals [u,v] in P_{m,n}, including singleton intervals, always (m+1)/(n(mn+1))·binom((m+1)²n+m,n−1)?

**Context.** Setup: For integers m,n≥1, let B_n⁺ be the positive braid monoid with generators σ₁,…,σₙ₋₁, relations σᵢσⱼ=σⱼσᵢ for |i−j|≥2 and σᵢσᵢ₊₁σᵢ=σᵢ₊₁σᵢσᵢ₊₁. Put c=σ₁⋯σₙ₋₁ and Δ=(σ₁⋯σₙ₋₁)(σ₁⋯σₙ₋₂)⋯σ₁. An element is c-sortable when its lexicographically-first position sequence of c∞ representing it uses weakly decreasing sets of generators in successive c-blocks. Let P_{m,n} be the c-sortable left divisors of Δᵐ, ordered by left divisibility. Audited provenance and status: Subject: Algebraic combinatorics FPSAC2025 final p12 retains conjecture. Current project page retains interval-count goal; its proved framing result concerns linear intervals. No identifiable published long successor located. Fang’s current research page lists2504.13492 as an FPSAC2025 extended abstract, with full version in preparation. September2026 rowmotion invariance concerns alt-Tamari orbit statistics, not m-Cambrian interval enumeration.

**Source.** Clément Chenevière, Wenjie Fang and Corentin Henriet. *A new definition for m-Cambrian lattices*. 2025. [primary source](https://www.mat.univie.ac.at/~slc/wpapers/FPSAC2025/73.pdf) Location: Stump–Thomas–Williams; restated in thesis Conjecture9.3.1 and Chenevière–Fang–Henriet, Conjecture5.2.

**Literature check.** Status: Origin: Stump–Thomas–Williams; restated in thesis Conjecture9.3.1 and Chenevière–Fang–Henriet, Conjecture5.2. Checked12October2026; no matching resolution located.


<a id="q4694"></a>

## Q4694. For infinitely many integers n≥4, does an (n−2,2)-factorisation exist that is not a…

**Status:** Open · **Kind:** open problem · **Collection** 47

For infinitely many integers n≥4, does an (n−2,2)-factorisation exist that is not a hyperfactorisation?

**Context.** Setup: Let Mₙ be all perfect matchings of K₂ₙ. A nonempty D⊆Mₙ is an (n−2,2)-factorisation if every four-vertex subset contains two edges of exactly c members of D, for a fixed positive integer c. It is a hyperfactorisation if every pair of disjoint edges belongs to exactly c′ members, for some fixed c′>0. Origin: Bamberg–Klawuhn, 2025 paper; thesis §6.6, pp150–151; July 2026 final §6(1),(3), p806. Checked 12 October 2026; no matching resolution located. Audited provenance and status: Subject: Algebraic combinatorics September final concerns polynomial intersection distributions, not matching designs. https://doi.org/10.1016/j.ffa.2026.102828

**Source.** John Bamberg and Lukas Klawuhn. *On the association scheme of perfect matchings and their designs*. 2026. [primary source](https://arxiv.org/abs/2507.00813v2) Location: Bamberg–Klawuhn, 2025 paper; thesis §6.6, pp150–151; July 2026 final §6(1),(3), p806.

**Literature check.** Status: Origin: Bamberg–Klawuhn, 2025 paper; thesis §6.6, pp150–151; July 2026 final §6(1),(3), p806. Checked 12 October 2026; no matching resolution located.

**Further links.** [1](https://doi.org/10.1016/j.ffa.2026.102828)


<a id="q4695"></a>

## Q4695. Does some integer n≥4 admit ∅≠D⊊Mₙ such that every triple of pairwise disjoint edges belongs to…

**Status:** Open · **Kind:** open problem · **Collection** 47

Does some integer n≥4 admit ∅≠D⊊Mₙ such that every triple of pairwise disjoint edges belongs to exactly c members of D, for a fixed positive integer c?

**Context.** Setup: Let Mₙ be all perfect matchings of K₂ₙ. A nonempty D⊆Mₙ is an (n−2,2)-factorisation if every four-vertex subset contains two edges of exactly c members of D, for a fixed positive integer c. It is a hyperfactorisation if every pair of disjoint edges belongs to exactly c′ members, for some fixed c′>0. Origin: Bamberg–Klawuhn, 2025 paper; thesis §6.6, pp150–151; July 2026 final §6(1),(3), p806. Checked 12 October 2026; no matching resolution located. Audited provenance and status: Subject: Algebraic combinatorics September final concerns polynomial intersection distributions, not matching designs. https://doi.org/10.1016/j.ffa.2026.102828

**Source.** John Bamberg and Lukas Klawuhn. *On the association scheme of perfect matchings and their designs*. 2026. [primary source](https://arxiv.org/abs/2507.00813v2) Location: Bamberg–Klawuhn, 2025 paper; thesis §6.6, pp150–151; July 2026 final §6(1),(3), p806.

**Literature check.** Status: Origin: Bamberg–Klawuhn, 2025 paper; thesis §6.6, pp150–151; July 2026 final §6(1),(3), p806. Checked 12 October 2026; no matching resolution located.

**Further links.** [1](https://doi.org/10.1016/j.ffa.2026.102828)


<a id="q4710"></a>

## Q4710. Is K(Γ(r,n))≅(Z/nZ)^[r(n−2)−2]⊕Z/(2rn)Z for every r,n≥3?

**Status:** Open · **Kind:** open problem · **Collection** 48

Is K(Γ(r,n))≅(Z/nZ)^[r(n−2)−2]⊕Z/(2rn)Z for every r,n≥3?

**Context.** Setup: For integers r,n≥3, form Γ(r,n) from a cycle C_r by gluing one separate complete graph K_n along each cycle edge, identifying that edge and its endpoints. Different copies have no other identifications. Let L be its integer Laplacian and K(Γ)=ker(Σ:Z^V→Z)/LZ^V. Audited provenance and status: Subject: Algebraic graph theory Williams’s official supervision page confirms Tamimi’s PhD award on9August2022.

**Source.** Baha Tamimi. *The Sandpile & Smith Groups of Certain Classes of Graphs*. University of Essex, 2022. Advisor(s): David Penman; Gerald Williams. [primary source](https://repository.essex.ac.uk/33230/) Location: Thesis-origin Conjecture4.4.2 p115; edge-tiling definition p11. Checked12October2026: no matching resolution located.

**Literature check.** Status: Thesis-origin Conjecture4.4.2 p115; edge-tiling definition p11. Checked12October2026: no matching resolution located.

**Further links.** [1](https://repository.essex.ac.uk/33230/1/baha_tamimi_phd_thesis_05_08_2022.pdf)


<a id="q4739"></a>

## Q4739. Characterize exactly the pairs of integers r,c≥0 for which a nonempty finite simple undirected…

**Status:** Open · **Kind:** open problem (Question 1) · **Collection** 48

Characterize exactly the pairs of integers r,c≥0 for which a nonempty finite simple undirected graph exists in which every vertex has degree r and belongs to exactly c distinct triangles.

**Context.** Artem Hak: Kyiv-Mohyla doctoral student since2024; supervisor Sergiy Kozerenko. Paper-origin target; no completed doctorate asserted. Audited provenance and status: Subject: Graph theory Hak–Kozerenko–Lohvynov–Yarosh, Regular K₃-regular graphs, 2602.23517v2, §5 Question1 p21; definitions pp3–4. Restates Caro–Lauri–Mifsud–Yuster–Zarb, Flip colouring of graphs, GraphsCombin.40(2024)106, §7 spectrum problem. Checked12October2026: current v2 and readable original journal-final retain the full parameter classification. Sheffield–Xi2507.14473v1 p2 gives partial bounds and an abelian-Cayley conjecture, not a general classification. No matching resolution located. Hak’s self-authored education entry identifies the ongoing doctorate and supervisor; doctoral dissertation title is not given. Adjacent graph-structure classifications remain unselected.

**Source.** Artem Hak; Sergiy Kozerenko; Lohvynov; Yarosh. *Regular K₃-regular graphs*. 2026. [primary source](https://arxiv.org/abs/2602.23517v2) Location: §5, Question 1, p.21; definitions pp.3–4; original flip-colouring spectrum problem §7.

**Literature check.** Status: Checked12October2026: current v2 and readable original journal-final retain the full parameter classification. Sheffield–Xi2507.14473v1 p2 gives partial bounds and an abelian-Cayley conjecture, not a general classification. No matching resolution located.

**Further links.** [1](https://arxiv.org/abs/2602.23517) · [2](https://arxiv.org/pdf/2602.23517v2) · [3](https://link.springer.com/article/10.1007/s00373-024-02838-w) · [4](https://arxiv.org/abs/2312.08777) · [5](https://arxiv.org/abs/2507.14473) · [6](https://github.com/artikgak/artikgak)


<a id="q4758"></a>

## Q4758. For every integer n≥0, are the numbers of trees in T_n avoiding A and avoiding B equal?

**Status:** Open · **Kind:** open problem · **Collection** 48

For every integer n≥0, are the numbers of trees in T_n avoiding A and avoiding B equal?

**Context.** Namrata: Warwick PhD2024; supervisor Torsten Mütze. Setup: Let T_n be the rooted ordered binary trees with n vertices, up to order-preserving isomorphism; vertices have optional left and right children. Pattern A occurs if distinct vertices r,a,b,c,d satisfy: a lies in r's left subtree, b in a's right subtree, c is r's right child, and d lies in c's right subtree. Pattern B uses the same conditions except that a must be r's left child and c may lie anywhere in r's right subtree. Avoidance means having no occurrence. Audited provenance and status: Subject: Enumerative combinatorics Hamiltonicity in flip graphs: Set Systems, Pattern Avoidance, and Hardness, June2024; §§4.2.1–4.2.2, Theorem54 p117, §4.9 p141. Gregor–Mütze–Namrata origin: EJC122(December2024)104020 §8.3; patterns (31245,0-1-)/(31245,1-0-). Publisher-indexed final passage read; direct403, full final unread. Checked12October2026: no matching resolution located. Latest2306.08420v4 and author PDF retain target. Burstein–Han–Kitaev–Zhang, EJC32(1)2025P1.7 §§1–4: classical permutation-pattern sets and Ferrers-board shape equivalence; no matching mixed binary-tree claim. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v32i1p7/pdf/

**Source.** Namrata. *Hamiltonicity in flip graphs: Set Systems, Pattern Avoidance, and Hardness*. University of Warwick, 2024. Advisor(s): Torsten Mütze. [primary source](https://wrap.warwick.ac.uk/id/eprint/190281/) Location: Thesis §§4.2.1–4.2.2, Theorem 54 p.117, §4.9 p.141; paper §8.3.

**Literature check.** Status: Checked12October2026: no matching resolution located. Latest2306.08420v4 and author PDF retain target.

**Further links.** [1](https://wrap.warwick.ac.uk/id/eprint/190281/1/WRAP_Theses_Namrata_2024.pdf) · [2](https://sites.google.com/view/nnamrata) · [3](https://sites.google.com/view/nnamrata/publications) · [4](https://arxiv.org/abs/2306.08420) · [5](https://tmuetze.de/papers/jump6.pdf) · [6](https://doi.org/10.1016/j.ejc.2024.104020) · [7](https://www.sciencedirect.com/science/article/pii/S0195669824001057) · [8](https://arxiv.org/abs/2212.03918) · [9](https://tmuetze.de/papers/kneser.pdf) · [10](https://doi.org/10.1016/j.aim.2025.110189) · [11](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v32i1p7/pdf/)


<a id="q4764"></a>

## Q4764. For every triangular λ, is A_λ a nonnegative-integer linear combination of two-variable Schur…

**Status:** Open · **Kind:** open problem · **Collection** 48

For every triangular λ, is A_λ a nonnegative-integer linear combination of two-variable Schur polynomials s_(a,b)(q,t), a≥b≥0?

**Context.** Setup: Here λ,μ are partitions; |ν| counts cells. For a cell c of a French Ferrers diagram ν, let a_ν(c),ℓ\_ν(c) count cells rightward and upward, and h_ν(c)=a_ν(c)+ℓ\_ν(c)+1. For nonempty λ put L=max_{c∈λ}ℓ\_λ(c)/h_λ(c), U=min_{c∈λ}(ℓ\_λ(c)+1)/h_λ(c). Call λ triangular when L&lt;U, and set v=(L+U)/2. For μ⊆λ let sim_λ(μ)=#{c∈μ:ℓ\_μ(c)/h_μ(c)&lt;v≤(ℓ\_μ(c)+1)/h_μ(c)}, including sim_λ(∅)=0. Define A_λ(q,t)=Σ\_{μ⊆λ}q^{|λ|−|μ|}t^{sim_λ(μ)}. Audited provenance and status: Subject: Algebraic combinatorics Doctoral topic: qt-symmetry in triangular partitions; Pons CV2023 p8. LeMogne–Pons, Deficit and (q,t)-symmetry in triangular partitions,2604.00245v1,31March2026: Conjecture1 p8, Definitions2.5–2.8 pp5–6. Earlier exact formulation: Bergeron–Mazin final Conjecture7.1 p17, ECA3:1(2023)S2R1, published9September2022. Current endpoint inequalities follow Remark2.9. Checked12October2026: current author list retains preprint; no matching resolution located. BHMPS final Conjecture7.1.1 concerns Schur expansion in X over N[q,t]; its identification with this q,t-Schur target is unverified. https://doi.org/10.1017/fmp.2023.4 https://arxiv.org/abs/2102.07931 https://www.cambridge.org/core/journals/forum-of-mathematics-pi/article/shuffle-theorem-for-paths-under-any-line/956194CE18D7DCFF1D1BC3BE3F69659D Known for partitions with at most two parts (Theorem4.10).

**Source.** Loïc Le Mogne; Viviane Pons. *Deficit and (q,t)-symmetry in triangular partitions*. 2026. [primary source](https://arxiv.org/abs/2604.00245v1) Location: Loïc Le Mogne: Paris-Saclay doctoral student since2022; supervisors Nicolas Thiéry and Viviane Pons; degree award unverified.

**Literature check.** Status: Checked12October2026: current author list retains preprint; no matching resolution located.

**Further links.** [1](https://arxiv.org/abs/2604.00245) · [2](https://www.lri.fr/~pons/docs/cv_HDR_2023.pdf) · [3](https://www.lisn.upsaclay.fr/membres/le-mogne-loic/?lang=en) · [4](https://perso.lisn.upsaclay.fr/pons/docs/HDR.pdf) · [5](https://perso.lisn.upsaclay.fr/pons/en/pages/publications.html) · [6](https://www.mat.univie.ac.at/~slc/wpapers/FPSAC2023/21.pdf) · [7](https://ecajournal.haifa.ac.il/Volume2023/ECA2023_S2A1.pdf) · [8](https://doi.org/10.54550/ECA2023V3S1R1) · [9](https://arxiv.org/abs/2203.15942) · [10](https://doi.org/10.1017/fmp.2023.4) · [11](https://arxiv.org/abs/2102.07931) · [12](https://www.cambridge.org/core/journals/forum-of-mathematics-pi/article/shuffle-theorem-for-paths-under-any-line/956194CE18D7DCFF1D1BC3BE3F69659D)


<a id="q4766"></a>

## Q4766. Characterize the partitions μ for which Σ\_{λ≤Iμ}p_λ has nonnegative coefficients in the Schur basis.

**Status:** Open · **Kind:** open problem (Question 2.4.1) · **Collection** 48

Characterize the partitions μ for which Σ\_{λ≤Iμ}p_λ has nonnegative coefficients in the Schur basis.

**Context.** Setup: For partitions λ,μ of n, write λ≤Iμ when s_μ−s_λ has nonnegative monomial coefficients; s_λ is the Schur function. Put p_λ=∏ᵢ(Σⱼxⱼ^{λᵢ}). Audited provenance and status: Subject: Algebraic combinatorics David Kenepp: UC Davis PhD, 2025; advisor Anne Schilling. The Immersion Poset and a Crystal Analysis of Claw-Free Graphs: Question 2.4.1, p. 60; acknowledgment p. v. Earlier joint-paper origin: The immersion poset on partitions (2025), Question 4.1, p. 43. Checked 13 October 2026: both thesis copies and publisher final read; no matching later resolution located. Some lower intervals fail Schur positivity.

**Source.** David Kenepp. *The Immersion Poset and a Crystal Analysis of Claw-Free Graphs*. UC Davis, 2025. Advisor(s): Anne Schilling. [primary source](https://escholarship.org/content/qt3z0225rf/qt3z0225rf_noSplash_c8d8ccaffb181143a753620a3b6a146e.pdf) Location: The Immersion Poset and a Crystal Analysis of Claw-Free Graphs: Question 2.4.1, p. 60; acknowledgment p. v.

**Literature check.** Status: Checked 13 October 2026: both thesis copies and publisher final read; no matching later resolution located.

**Further links.** [1](https://doi.org/10.1007/s10801-025-01380-z) · [2](https://d-nb.info/1368679838/34) · [3](https://math.ucdavis.edu/~anne/graduate_students.html)


<a id="q4767"></a>

## Q4767. Can every such graph also arise from a finite extremal semidistributive lattice?

**Status:** Open · **Kind:** open problem (Question 3.102) · **Collection** 48

Can every such graph also arise from a finite extremal semidistributive lattice?

**Context.** Setup: In a finite semidistributive lattice L, label each cover x⋖y by min{j≤y:j≰x}. The canonical join graph has join-irreducibles as vertices, adjacent when labeling covers into a common element. Extremality means longest-chain length equals both join- and meet-irreducible counts. Audited provenance and status: Subject: Lattice theory / algebraic combinatorics Adrien Segovia: Étude des ordres et treillis, UQAM doctorate 2026; advisors Samuele Giraudo and Hugh Thomas. Doctoral-research question appearing in the earlier paper Extremality in semidistributive lattices. Checked 13 October 2026: later shellability and dimension papers read; no matching resolution located.

**Source.** Adrien Segovia. *Étude des ordres et treillis*. UQAM, 2026. Advisor(s): Samuele Giraudo; Hugh Thomas. [primary source](https://archipel.uqam.ca/20179/1/D5119.pdf) Location: Thesis Question 3.102, p. 110; also arXiv:2511.18540v3 Question 5.4.

**Literature check.** Status: Extremality papers checked; no matching resolution. https://www.mat.univie.ac.at/~slc/wpapers/FPSAC2026/56.html https://arxiv.org/abs/2604.20947

**Further links.** [1](https://archipel.uqam.ca/20179/) · [2](https://arxiv.org/abs/2511.18540) · [3](https://arxiv.org/abs/2608.14092) · [4](https://arxiv.org/abs/2609.07382) · [5](https://www.mat.univie.ac.at/~slc/wpapers/FPSAC2026/56.html) · [6](https://arxiv.org/abs/2604.20947) · [7](https://arxiv.org/abs/2511.18540v3)


<a id="q4769"></a>

## Q4769. For all such S₁,…,Sₘ and positive integers y₁,…,yₘ, does the Ehrhart polynomial…

**Status:** Open · **Kind:** open problem (Problem 5.4) · **Collection** 48

For all such S₁,…,Sₘ and positive integers y₁,…,yₘ, does the Ehrhart polynomial |t(ΣᵢyᵢΔ⁰\_{Sᵢ})∩ℤⁿ| have strictly positive coefficients in every degree from zero through the polytope’s dimension?

**Context.** Setup: Let e₁,…,eₙ be the standard basis of ℝⁿ, with e₋ᵢ=−eᵢ. For nonempty S⊆{±1,…,±n} containing no opposite pair, put Δ⁰\_S=conv({0}∪{eᵢ:i∈S}). Audited provenance and status: Subject: Polyhedral combinatorics Warut Thawinrak: UC Davis PhD, 2025; advisor Fu Liu. On the Faces and Ehrhart Polynomials of Polytopes, Problem 2.5.4, p. 33; definitions 2.2.2–2.2.4; acknowledgments p. vii. Checked 13 October 2026: latest paper retains question; no matching resolution located. Cross-polytope positivity (arXiv:2608.16037v1, Theorem 1.5, Remark 4.14) has different scope. v2: same scope (4.15). Negative linear coefficients exclude positive simplex sums; general-simplex counterexamples also differ.

**Source.** Warut Thawinrak. *On the Faces and Ehrhart Polynomials of Polytopes*. UC Davis, 2026. Advisor(s): Fu Liu. [primary source](https://www.math.ucdavis.edu/~webfiles/dissertations/202503_Warut_Thawinrak_Dissertation.pdf) Location: Thesis question; later author paper arXiv:2512.01332v2, Problem 5.4.

**Literature check.** Status: Checked 13 October 2026: latest paper retains question; no matching resolution located.

**Further links.** [1](https://escholarship.org/uc/item/59t710m1) · [2](https://arxiv.org/abs/2512.01332) · [3](https://arxiv.org/abs/2608.16037) · [4](https://arxiv.org/abs/2512.01332v2) · [5](https://arxiv.org/abs/2608.16037v1)

