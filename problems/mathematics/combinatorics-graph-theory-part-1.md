# Combinatorics & Graph Theory (part 1 of 3)

[Subject overview](combinatorics-graph-theory.md) · Parts: [1](combinatorics-graph-theory-part-1.md) · [2](combinatorics-graph-theory-part-2.md) · [3](combinatorics-graph-theory-part-3.md)

<a id="q17"></a>

## Q17. For a tree T and even k≥2, form D_(k)(T) with entry indexed by (v_(1),…,v_(k)) e…

**Status:** Solved here: proved · **Kind:** conjecture (Conjecture 4) · **Collection** 1

For a tree T and even k≥2, form D_(k)(T) with entry indexed by (v_(1),…,v_(k)) equal to the edge-count of the smallest subtree containing those vertices. Does 2^(k−1)−1 always divide its symmetric hyperdeterminant?

**Context.** Origin: The thesis proposes these questions from its computations and graph constructions; the distance-critical graph work is joint with Joshua Cooper.

**Source.** Gabrielle Anne Tauscheck. *Generalizations of the Graham-Pollak Tree Theorem*. University of South Carolina, 2024. Advisor(s): Joshua Cooper. [primary source](https://scholarcommons.sc.edu/cgi/viewcontent.cgi?article=8719&context=etd) · [record](https://scholarcommons.sc.edu/etd/7811/) Location: Conjecture 4, printed p.69. Search-qualified status: Cooper–Du (2025) resolves tree-independence of the determinant, not this divisibility statement. No proof/disproof found in targeted searches.

**Results.**

- **Proved**: Stronger divisor for every tree and every order k>=2. Remaining: None at the retained scope. Recorded from the external B7 return  (backfilled 2026-10-08); selected local controls in the intake; external archive not uploaded; not independently re-derived here. [Details](../../solutions/b7-2026-10-07/B7_Research_Report_2026-10-07.md).
- **Related result** (B7-R01: submitted proved): For every n-vertex tree, n>=2, and every integer k>=2, (n-1)(2^(k-1)-1) divides the raw symmetric tensor resultant; the n=1 determinant is zero. Remaining/limits: None for the retained statement. [Report](../../solutions/b7-2026-10-07/README.md).

**Further links.** [1](https://arxiv.org/abs/2505.10501) · [2](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v32i2p30/pdf/)


<a id="q18"></a>

## Q18. What is the least order of a connected distance-critical graph whose complement …

**Status:** Open · **Kind:** open problem (Question 6.5) · **Collection** 1

What is the least order of a connected distance-critical graph whose complement has no Hamiltonian cycle? Distance-critical means deleting any vertex changes the distance between some remaining pair.

**Context.** Origin: The thesis proposes these questions from its computations and graph constructions; the distance-critical graph work is joint with Joshua Cooper.

**Source.** Gabrielle Anne Tauscheck. *Generalizations of the Graham-Pollak Tree Theorem*. University of South Carolina, 2024. Advisor(s): Joshua Cooper. [primary source](https://scholarcommons.sc.edu/cgi/viewcontent.cgi?article=8719&context=etd) · [record](https://scholarcommons.sc.edu/etd/7811/) Location: Question 6.5, printed pp.70–71. Search-qualified status: Thesis places the answer between 12 and 27. The 2025 joint paper on distance-critical graphs and targeted later searches supplied no resolution of this minimum-order question.

**Further links.** [1](https://link.springer.com/article/10.1007/s00373-025-02943-4)


<a id="q19"></a>

## Q19. Determine the asymptotic proportion of labeled n-vertex graphs that are connecte…

**Status:** Open · **Kind:** open problem (Question 6.6) · **Collection** 1

Determine the asymptotic proportion of labeled n-vertex graphs that are connected and distance-critical (each vertex’s deletion changes a remaining pair’s distance). What is the sharp enumeration beyond the known exponential lower bound?

**Context.** Origin: The thesis proposes these questions from its computations and graph constructions; the distance-critical graph work is joint with Joshua Cooper.

**Source.** Gabrielle Anne Tauscheck. *Generalizations of the Graham-Pollak Tree Theorem*. University of South Carolina, 2024. Advisor(s): Joshua Cooper. [primary source](https://scholarcommons.sc.edu/cgi/viewcontent.cgi?article=8719&context=etd) · [record](https://scholarcommons.sc.edu/etd/7811/) Location: Question 6.6, printed p.71. Follow-on evidence: Cooper–Tauscheck’s July 2025 journal paper §6, Question 1, retains the enumeration/proportion problem, extending distance-criticality componentwise to disconnected graphs. Later targeted searches found no resolution of either enumeration.

**Further links.** [1](https://link.springer.com/article/10.1007/s00373-025-02943-4)


<a id="q20"></a>

## Q20. Are K_(1),K_(2),K_(3), two isolated vertices, and the three-vertex path the only…

**Status:** Open · **Kind:** conjecture (Conjecture 2.1.2) · **Collection** 1

Are K_(1),K_(2),K_(3), two isolated vertices, and the three-vertex path the only graphs H for which a graph G’s adjacency spectrum always determines whether G contains an induced H?

**Context.** Origin: Barranca proposes this classification after introducing spectral recognizability.

**Source.** Emily Barranca. *Recognizing Induced Subgraph and Tree Structure from the Adjacency Spectrum of a Graph*. University of Rhode Island, 2024. Advisor(s): Michael D. Barrus, Jr.. [primary source](https://digitalcommons.uri.edu/cgi/viewcontent.cgi?article=2701&context=oa_diss) · [record](https://digitalcommons.uri.edu/oa_diss/1678/) Location: Conjecture 2.1.2, printed p.26. Search-qualified status: Author’s March 2025 CV lists the relevant manuscript in preparation. The June 2025 Barranca–Barrus paper treats double stars, not this classification. No resolving later work found.

**Results.**

- **Investigated, unresolved** (B7: submitted unresolved): No new analysis or status promotion in this return. Remaining/limits: not_attempted Intake: Scope and identity checked; no independent proof or renewed literature audit of this question. [Report](../../solutions/b7-2026-10-07/README.md).

**Further links.** [1](https://inside.smcm.edu/sites/default/files/2025-03/CV.pdf) · [2](https://arxiv.org/abs/2506.06934)


<a id="q21"></a>

## Q21. Fix a connected simple H on at least three vertices. Independently 2-color each …

**Status:** Open · **Kind:** conjecture (Conjecture 2.3.7) · **Collection** 1

Fix a connected simple H on at least three vertices. Independently 2-color each G_(n) uniformly; T_(n) counts monochromatic non-induced H-copies and σ\_(n)^(2)=Var(T_(n)). If limsup_(n→∞)max_(u≠v)D_(uv)(H,G_(n))/σ\_(n)>0, where D_(uv) counts non-induced H-copies containing u,v, must (T_(n)−𝔼T_(n))/σ\_(n) fail to converge to N(0,1)?

**Context.** Origin: The coloring questions are joint with Dan Mikulincer; code counting with Dong and Zhao; and the unit-distance question with Cohen.

**Source.** Nitya Mani. *A probabilistic perspective on graph coloring*. Massachusetts Institute of Technology, 2025. Advisor(s): Pablo Parrilo; Yufei Zhao. [primary source](https://dspace.mit.edu/server/api/core/bitstreams/e66d55e0-26d8-4b82-8d6f-0c5fd49e5aa6/content) · [record](https://dspace.mit.edu/server/api/core/bitstreams/e66d55e0-26d8-4b82-8d6f-0c5fd49e5aa6/content#page=1) Location: Conjecture 2.3.7, printed p.32; Definition 2.2.4. Follow-on evidence: Available Mani–Mikulincer preprint Conjecture 1.5 retains the general claim. Its publication is Annals of Applied Probability 36(1) (2026), 744–775; search found no later resolution.

**Further links.** [1](https://arxiv.org/abs/2403.14068) · [2](https://www.imstat.org/publications/aap/aap_36_1/aap_36_1.pdf)


<a id="q22"></a>

## Q22. For fixed connected simple H on at least three vertices and graph sequence G_(n)…

**Status:** Open · **Kind:** open problem (Question 2.3.8) · **Collection** 1

For fixed connected simple H on at least three vertices and graph sequence G_(n), let Z_(c) be the centered, variance-one count of monochromatic non-induced H-copies under independent uniform c-coloring. If Z_(c)⇒N(0,1), must Z_(c^(′))⇒N(0,1) for every fixed integer c^(′)>c≥2?

**Context.** Origin: The coloring questions are joint with Dan Mikulincer; code counting with Dong and Zhao; and the unit-distance question with Cohen.

**Source.** Nitya Mani. *A probabilistic perspective on graph coloring*. Massachusetts Institute of Technology, 2025. Advisor(s): Pablo Parrilo; Yufei Zhao. [primary source](https://dspace.mit.edu/server/api/core/bitstreams/e66d55e0-26d8-4b82-8d6f-0c5fd49e5aa6/content) · [record](https://dspace.mit.edu/server/api/core/bitstreams/e66d55e0-26d8-4b82-8d6f-0c5fd49e5aa6/content#page=1) Location: Question 2.3.8, printed p.33. Follow-on evidence: Retained as Question 1.6 in the available author preprint; its 2026 journal publication was located. No subsequent solution found.

**Further links.** [1](https://arxiv.org/abs/2403.14068) · [2](https://www.imstat.org/publications/aap/aap_36_1/aap_36_1.pdf)


<a id="q23"></a>

## Q23. Fix q≥2 and c>0. If A_(q)(n,d) is the maximum size of a subset of [q]^(n) with p…

**Status:** Open · **Kind:** conjecture (Conjecture 4.2.2) · **Collection** 1

Fix q≥2 and c>0. If A_(q)(n,d) is the maximum size of a subset of [q]^(n) with pairwise Hamming distance at least d, is the number of all such subsets at most 2^(O(A_(q)(n,d))) whenever d<(1−q^(−1)−c)n?

**Context.** Origin: The coloring questions are joint with Dan Mikulincer; code counting with Dong and Zhao; and the unit-distance question with Cohen.

**Source.** Nitya Mani. *A probabilistic perspective on graph coloring*. Massachusetts Institute of Technology, 2025. Advisor(s): Pablo Parrilo; Yufei Zhao. [primary source](https://dspace.mit.edu/server/api/core/bitstreams/e66d55e0-26d8-4b82-8d6f-0c5fd49e5aa6/content) · [record](https://dspace.mit.edu/server/api/core/bitstreams/e66d55e0-26d8-4b82-8d6f-0c5fd49e5aa6/content#page=1) Location: Conjecture 4.2.2, printed p.169. Search-qualified status: Available paper Conjecture 1.2 retains this stronger claim. The solved Balogh–Treglown–Wagner conjecture in its abstract is a different Hamming-bound statement. No later resolution found.

**Further links.** [1](https://arxiv.org/abs/2205.12363) · [2](https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/abs/on-the-number-of-error-correcting-codes/7BDE7E79815F0145DC142CC108756FBF)


<a id="q24"></a>

## Q24. Is the supremal upper density m_(1) of measurable unit-distance-avoiding subsets…

**Status:** Open · **Kind:** open problem (Question 4.3.18) · **Collection** 1

Is the supremal upper density m_(1) of measurable unit-distance-avoiding subsets of ℝ^(2) attained by A=⋃\_(j)A_(j) with distances within each block <1 and distances between distinct blocks >1?

**Context.** Origin: The coloring questions are joint with Dan Mikulincer; code counting with Dong and Zhao; and the unit-distance question with Cohen.

**Source.** Nitya Mani. *A probabilistic perspective on graph coloring*. Massachusetts Institute of Technology, 2025. Advisor(s): Pablo Parrilo; Yufei Zhao. [primary source](https://dspace.mit.edu/server/api/core/bitstreams/e66d55e0-26d8-4b82-8d6f-0c5fd49e5aa6/content) · [record](https://dspace.mit.edu/server/api/core/bitstreams/e66d55e0-26d8-4b82-8d6f-0c5fd49e5aa6/content#page=1) Location: Question 4.3.18, printed p.200; §4.3.8. Search-qualified status: Available preprint Question 5.1 asks this explicitly. September 2025 journal version establishes clustering, a weaker property; searches found no full block-structure theorem.

**Further links.** [1](https://arxiv.org/abs/2407.05071) · [2](https://link.springer.com/article/10.1007/s10474-025-01556-w)


<a id="q25"></a>

## Q25. Suppose n unit simplices in nΔ\_(d−1) are spread out: any k have smallest contain…

**Status:** Open · **Kind:** conjecture (Conjecture 2.6.1) · **Collection** 1

Suppose n unit simplices in nΔ\_(d−1) are spread out: any k have smallest containing translated standard simplex of side ≥k. If repeatedly merging two simplices meeting at one point into their smallest containing standard simplex eventually yields nΔ\_(d−1), must the arrangement extend to a fine mixed subdivision?

**Context.** Origin: These are new extension conjectures in Yao’s chapter based on joint work with Fedir Yudin and Derek Liu.

**Source.** Yuan Yao. *The Combinatorics of Triangulations of Products of Two Simplices*. Massachusetts Institute of Technology, 2026. Advisor(s): Alexander Postnikov. [primary source](https://dspace.mit.edu/server/api/core/bitstreams/db558298-7433-42a4-89f5-7045101fbf9f/content) · [record](https://dspace.mit.edu/entities/publication/5d9989d2-5270-441d-912b-4a8d0478974c) Location: Conjecture 2.6.1, printed p.38; Definitions 2.1.2, 2.2.5. Search-qualified status: May 2026 thesis treats this as conjectural beyond established low-dimensional cases. Searches of exact title, author and touching-simplex condition found no later resolution.


<a id="q26"></a>

## Q26. Given a fine mixed subdivision C of nΔ\_(d−1) and a lattice vertex v of C, must t…

**Status:** Open · **Kind:** conjecture (Conjecture 2.6.2) · **Collection** 1

Given a fine mixed subdivision C of nΔ\_(d−1) and a lattice vertex v of C, must there be a subdivision C^(′) of (n+1)Δ\_(d−1) whose new unmixed cell is v+Δ\_(d−1), and whose deletion of the new summand recovers C?

**Context.** Origin: These are new extension conjectures in Yao’s chapter based on joint work with Fedir Yudin and Derek Liu.

**Source.** Yuan Yao. *The Combinatorics of Triangulations of Products of Two Simplices*. Massachusetts Institute of Technology, 2026. Advisor(s): Alexander Postnikov. [primary source](https://dspace.mit.edu/server/api/core/bitstreams/db558298-7433-42a4-89f5-7045101fbf9f/content) · [record](https://dspace.mit.edu/entities/publication/5d9989d2-5270-441d-912b-4a8d0478974c) Location: Conjecture 2.6.2, printed p.38; deletion defined in §1.5, p.22. Search-qualified status: Thesis proves the planar case and leaves the higher-dimensional assertion conjectural. Targeted post-thesis searches found no resolution.


<a id="q27"></a>

## Q27. An arrangement of n unit simplices in nΔ\_(d−1) projects along an edge to a sprea…

**Status:** Open · **Kind:** conjecture (Conjecture 2.7.7) · **Collection** 1

An arrangement of n unit simplices in nΔ\_(d−1) projects along an edge to a spread-out arrangement admitting fine mixed subdivision C in nΔ\_(d−2). Must there be a fine mixed subdivision upstairs containing the prescribed simplices and projecting to C?

**Context.** Origin: These are new extension conjectures in Yao’s chapter based on joint work with Fedir Yudin and Derek Liu.

**Source.** Yuan Yao. *The Combinatorics of Triangulations of Products of Two Simplices*. Massachusetts Institute of Technology, 2026. Advisor(s): Alexander Postnikov. [primary source](https://dspace.mit.edu/server/api/core/bitstreams/db558298-7433-42a4-89f5-7045101fbf9f/content) · [record](https://dspace.mit.edu/entities/publication/5d9989d2-5270-441d-912b-4a8d0478974c) Location: Conjecture 2.7.7, printed p.46. Search-qualified status: Open in the May 2026 thesis beyond its proved lower-dimensional case. No later resolution was located in author, title and projection searches.


<a id="q28"></a>

## Q28. For any finite Weyl group W and non-singleton geodesically convex C in its left …

**Status:** Open · **Kind:** conjecture (Conjecture 3.2.1) · **Collection** 1

For any finite Weyl group W and non-singleton geodesically convex C in its left simple-generator Cayley graph, put δ\_(C)(t)=|{w∈C:ℓ(wt)<ℓ(w)}|/|C| for reflections t. Must max_(t)min(δ\_(C)(t),1−δ\_(C)(t))≥1/3?

**Context.** Origin: These formulations arise from joint work with Christian Gaetz. The Weyl-group balance question extends the classical poset conjecture.

**Source.** Yibo Gao. *Symmetric structures in the weak and strong Bruhat orders*. Massachusetts Institute of Technology, 2022. Advisor(s): Alexander Postnikov. [primary source](https://dspace.mit.edu/server/api/core/bitstreams/f0e7b418-e3ee-4b38-b6f6-f444087e8483/content) · [record](https://dspace.mit.edu/server/api/core/bitstreams/f0e7b418-e3ee-4b38-b6f6-f444087e8483/content#page=1) Location: Conjecture 3.2.1, printed p.20 (also 1.1.1). Follow-on evidence: Gaetz–Gao’s 2023 Transactions version retains the conjecture and proves special cases/uniform weaker lower bounds. Targeted searches through 2026 found no full resolution.

**Further links.** [1](https://arxiv.org/abs/2005.09719) · [2](https://doi.org/10.1090/tran/9040)


<a id="q29"></a>

## Q29. For every Coxeter system (W,S) and u,v,w∈W, must |Conv(u,v)| |Conv(v,w)|≥|Conv(u…

**Status:** Open · **Kind:** conjecture (Conjecture 1.2.1) · **Collection** 1

For every Coxeter system (W,S) and u,v,w∈W, must |Conv(u,v)| |Conv(v,w)|≥|Conv(u,v,w)|, with Conv denoting geodesic convex hull in the undirected Cayley graph for S?

**Context.** Origin: These formulations arise from joint work with Christian Gaetz. The Weyl-group balance question extends the classical poset conjecture.

**Source.** Yibo Gao. *Symmetric structures in the weak and strong Bruhat orders*. Massachusetts Institute of Technology, 2022. Advisor(s): Alexander Postnikov. [primary source](https://dspace.mit.edu/server/api/core/bitstreams/f0e7b418-e3ee-4b38-b6f6-f444087e8483/content) · [record](https://dspace.mit.edu/server/api/core/bitstreams/f0e7b418-e3ee-4b38-b6f6-f444087e8483/content#page=1) Location: Conjecture 1.2.1, printed p.9; §4.1. Follow-on evidence: Liu (May 2025) proves the affine irreducible rank-three cases and explicitly retains the general conjecture. No general resolution was located.

**Further links.** [1](https://arxiv.org/abs/2505.15871) · [2](https://arxiv.org/abs/2012.06841)


<a id="q30"></a>

## Q30. Across finite Weyl groups, can the elements w whose strong-Bruhat interval [e,w]…

**Status:** Open · **Kind:** open problem (Question 5.3.1) · **Collection** 1

Across finite Weyl groups, can the elements w whose strong-Bruhat interval [e,w] is self-dual be characterized by root-subsystem pattern avoidance in the Billey–Postnikov sense?

**Context.** Origin: These formulations arise from joint work with Christian Gaetz. The Weyl-group balance question extends the classical poset conjecture.

**Source.** Yibo Gao. *Symmetric structures in the weak and strong Bruhat orders*. Massachusetts Institute of Technology, 2022. Advisor(s): Alexander Postnikov. [primary source](https://dspace.mit.edu/server/api/core/bitstreams/f0e7b418-e3ee-4b38-b6f6-f444087e8483/content) · [record](https://dspace.mit.edu/server/api/core/bitstreams/f0e7b418-e3ee-4b38-b6f6-f444087e8483/content#page=1) Location: Question 5.3.1, printed p.69. Search-qualified status: Thesis and associated paper establish type A and ask about the other types. Targeted later searches found no general pattern-avoidance characterization.

**Further links.** [1](https://arxiv.org/abs/2003.06710)


<a id="q31"></a>

## Q31. Write sat(F,H) for the fewest edges in an H-free spanning subgraph of F where ad…

**Status:** Open · **Kind:** open problem (Question 4.1) · **Collection** 1

Write sat(F,H) for the fewest edges in an H-free spanning subgraph of F where adding any missing edge creates H. For fixed m≥2, does sat(Q_(d),Q_(m))/2^(d) converge as d→∞? Here Q_(d) is the d-dimensional hypercube.

**Context.** Origin: The saturation questions are joint with Noel and Scott; the bootstrap-percolation question is joint with Noel.

**Source.** Natasha Morrison. *Problems in Extremal and Probabilistic Combinatorics*. University of Oxford, 2017. Advisor(s): Alex Scott. [primary source](https://ora.ox.ac.uk/objects/uuid:83970d50-71d0-4511-9545-5358c3073343/files/mf97a866736e804d7a76d8cb77d47575e) · [record](https://ora.ox.ac.uk/objects/uuid:83970d50-71d0-4511-9545-5358c3073343/files/mf97a866736e804d7a76d8cb77d47575e#page=6) Location: Chapter 3, Question 4.1, printed p.77. Follow-on evidence: Explicitly retained in the 2021 saturation survey, Question 5; coauthor Noel’s public problem page also records it. Searches through 2026 found no convergence theorem.

**Further links.** [1](https://www.combinatorics.org/ojs/index.php/eljc/article/download/DS19/pdf/) · [2](https://garden.irmacs.sfu.ca/op/saturation_in_the_hypercube)

*Also among the automatically extracted thesis statements: `c7b833e7cef6d5bf67f5`.*


<a id="q32"></a>

## Q32. Let c_(m)=liminf_(d→∞)sat(Q_(d),Q_(m))/2^(d), with ordinary subgraph saturation …

**Status:** Open · **Kind:** open problem (Question 4.2) · **Collection** 1

Let c_(m)=liminf_(d→∞)sat(Q_(d),Q_(m))/2^(d), with ordinary subgraph saturation and Q_(d) the d-cube. Is c_(m)/m→∞ as m→∞?

**Context.** Origin: The saturation questions are joint with Noel and Scott; the bootstrap-percolation question is joint with Noel.

**Source.** Natasha Morrison. *Problems in Extremal and Probabilistic Combinatorics*. University of Oxford, 2017. Advisor(s): Alex Scott. [primary source](https://ora.ox.ac.uk/objects/uuid:83970d50-71d0-4511-9545-5358c3073343/files/mf97a866736e804d7a76d8cb77d47575e) · [record](https://ora.ox.ac.uk/objects/uuid:83970d50-71d0-4511-9545-5358c3073343/files/mf97a866736e804d7a76d8cb77d47575e#page=6) Location: Chapter 3, Question 4.2, printed p.77. Search-qualified status: The author’s saturation paper asks this explicitly. Searches for later hypercube saturation bounds found no superlinear lower-bound resolution.

**Further links.** [1](https://arxiv.org/abs/1408.5488) · [2](https://garden.irmacs.sfu.ca/op/saturation_in_the_hypercube)

*Also among the automatically extracted thesis statements: `6b7631ec9c984bce1be1`.*


<a id="q33"></a>

## Q33. Determine sat(Q_(d),C_(2ℓ)) for integers ℓ≥2 and d≥⌈log_(2)(2ℓ)⌉: the minimum ed…

**Status:** Open · **Kind:** open problem (Problem 4.5) · **Collection** 1

Determine sat(Q_(d),C_(2ℓ)) for integers ℓ≥2 and d≥⌈log_(2)(2ℓ)⌉: the minimum edge count of a spanning C_(2ℓ)-free subgraph of the d-cube made non-free by any additional cube edge.

**Context.** Origin: The saturation questions are joint with Noel and Scott; the bootstrap-percolation question is joint with Noel.

**Source.** Natasha Morrison. *Problems in Extremal and Probabilistic Combinatorics*. University of Oxford, 2017. Advisor(s): Alex Scott. [primary source](https://ora.ox.ac.uk/objects/uuid:83970d50-71d0-4511-9545-5358c3073343/files/mf97a866736e804d7a76d8cb77d47575e) · [record](https://ora.ox.ac.uk/objects/uuid:83970d50-71d0-4511-9545-5358c3073343/files/mf97a866736e804d7a76d8cb77d47575e#page=6) Location: Chapter 3, Problem 4.5, printed p.78. Follow-on evidence: The 2021 survey retains it as Problem 21, and coauthor Noel’s problem page identifies it as open. Targeted 2024–2026 searches found no general solution.

**Further links.** [1](https://www.combinatorics.org/ojs/index.php/eljc/article/download/DS19/pdf/) · [2](https://garden.irmacs.sfu.ca/op/saturation_in_the_hypercube)

*Also among the automatically extracted thesis statements: `ef8efaf3625f4d7791c1`.*


<a id="q34"></a>

## Q34. What is m(Q_(d),4) for every d≥4, where m(G,r) is the fewest initially infected …

**Status:** Open, partial results · **Kind:** open problem (Problem 7.2) · **Collection** 1

What is m(Q_(d),4) for every d≥4, where m(G,r) is the fewest initially infected vertices that infect all of G when each uninfected vertex becomes infected upon acquiring r infected neighbors?

**Context.** Origin: The saturation questions are joint with Noel and Scott; the bootstrap-percolation question is joint with Noel.

**Source.** Natasha Morrison. *Problems in Extremal and Probabilistic Combinatorics*. University of Oxford, 2017. Advisor(s): Alex Scott. [primary source](https://ora.ox.ac.uk/objects/uuid:83970d50-71d0-4511-9545-5358c3073343/files/mf97a866736e804d7a76d8cb77d47575e) · [record](https://ora.ox.ac.uk/objects/uuid:83970d50-71d0-4511-9545-5358c3073343/files/mf97a866736e804d7a76d8cb77d47575e#page=6) Location: Chapter 4, Problem 7.2, printed p.103 (PDF page 123). Follow-on evidence: Noel’s April 2026 paper attains the lower bound for infinitely many dimensions and obtains additive-O(d) bounds generally; it does not determine every dimension. This is a partially solved problem, retained only in its remaining all-d scope.

**Results.**

- **Partial result**: m(Q_d;4) = d(d^2+3d+14)/24 + 1 (the Morrison-Noel lower bound) for infinitely many d, and within O(d) of it for all d. Consequently, for r = 4, (m(Q_d,4) - d^3/24)/d^2 -> 1/8. The exact value for every d and all r >= 5 remain open. [Details](../../solutions/catalog-research/round2-harder.md). Related: [Noel: Optimal and Near-Optimal Constructions for Bootstrap Percolation in Hypercubes](https://arxiv.org/abs/2604.15534).

**Further links.** [1](https://arxiv.org/abs/2604.15534) · [2](https://arxiv.org/abs/1506.04686)

*Also among the automatically extracted thesis statements: `43e10d10544b09bd3194`.*


<a id="q35"></a>

## Q35. Place chips labeled 1,…,2m+1 at 0∈ℤ. A move sends the smaller of two co-located …

**Status:** Open · **Kind:** conjecture (Conjecture 2.3.1) · **Collection** 1

Place chips labeled 1,…,2m+1 at 0∈ℤ. A move sends the smaller of two co-located chips one step left and the larger one step right. Among all terminal left-to-right permutations, is the largest inversion count exactly m?

**Context.** Origin: Both conjectures arise from joint work with Thomas McConville and James Propp, incorporated into the thesis.

**Source.** Samuel Francis Hopkins. *Root System Chip-Firing*. Massachusetts Institute of Technology, 2018. Advisor(s): Alexander Postnikov. [primary source](https://dspace.mit.edu/server/api/core/bitstreams/8aa6c8bb-6452-4944-9edc-d3e954ca0e83/content) · [record](https://dspace.mit.edu/server/api/core/bitstreams/8aa6c8bb-6452-4944-9edc-d3e954ca0e83/content#page=1) Location: Conjecture 2.3.1, printed p.51. Search-qualified status: The author/coauthor’s OEIS entry A282901 still lists the conjecture. Later Klivans–Liscio work solves other confluence conjectures; its odd-line discussion does not prove this bound. No further resolution found.

**Further links.** [1](https://oeis.org/A282901) · [2](https://www.dam.brown.edu/people/cklivans/Confluence.pdf) · [3](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v24i3p13/pdf/)

*Also among the automatically extracted thesis statements: `95321f3cf4a0e8d9567c`.*


<a id="q36"></a>

## Q36. In labeled chip-firing from 2m+1 distinct chips at the origin, does the probabil…

**Status:** Open · **Kind:** conjecture (Conjecture 2.3.2) · **Collection** 1

In labeled chip-firing from 2m+1 distinct chips at the origin, does the probability of a sorted terminal state approach 1/3 under each protocol: uniform legal move; uniform unstable vertex then uniform chip pair; or uniform complete labeled stabilization sequence? Each move sends the smaller of two co-located chips left and the larger right by one step.

**Context.** Origin: Both conjectures arise from joint work with Thomas McConville and James Propp, incorporated into the thesis.

**Source.** Samuel Francis Hopkins. *Root System Chip-Firing*. Massachusetts Institute of Technology, 2018. Advisor(s): Alexander Postnikov. [primary source](https://dspace.mit.edu/server/api/core/bitstreams/8aa6c8bb-6452-4944-9edc-d3e954ca0e83/content) · [record](https://dspace.mit.edu/server/api/core/bitstreams/8aa6c8bb-6452-4944-9edc-d3e954ca0e83/content#page=1) Location: Conjecture 2.3.2, printed p.51. Follow-on evidence: Ayyer et al. (Combinatorial Theory, 2022) describe it as a conjecture motivating subsequent work. The inspected confluence results address other variants. Targeted searches found no proof/disproof through the check date.

**Further links.** [1](https://escholarship.org/content/qt08z5b229/qt08z5b229_noSplash_7a675eca02878394c02566983be533a7.pdf) · [2](https://www.dam.brown.edu/people/cklivans/Confluence.pdf) · [3](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v24i3p13/pdf/)

*Also among the automatically extracted thesis statements: `b434a0aa4bef620d6c41`.*


<a id="q164"></a>

## Q164. For every path or cycle G on n vertices and integer ℓ ≥ 1, is the sequence γₖ(G^…

**Status:** Open, partial results · **Kind:** conjecture (Conjecture 4.1.8) · **Collection** 2

For every path or cycle G on n vertices and integer ℓ ≥ 1, is the sequence γₖ(G^ℓ)/binomial(n,k), for k = 0,…,n, log-concave? The graph G^ℓ joins vertices at distance at most ℓ, and γₖ counts k-vertex sets meeting every closed neighborhood.

**Context.** Origin: The first conjecture is joint with David Galvin; the remaining three are new thesis formulations.

**Source.** Yufei Zhang. *Some Combinatorial Problems Involving Total Non-Negativity and Unimodality*. University of Notre Dame, 2025. Advisor(s): David Galvin. [primary source](https://ndownloader.figshare.com/files/54098216) · [record](https://curate.nd.edu/articles/thesis/Some_Combinatorial_Problems_Involving_Total_Non-Negativity_and_Unimodality/28786115) Location: Conjecture 4.1.8, printed p.57; path case repeated as Conjecture 5.1.1, pp.72–73. Status evidence, checked 5 October 2026: Author’s available paper retains this as Conjecture 1.8. Searches for domination-polynomial ultra-log-concavity found no subsequent proof.

**Results.**

- **Partial result**: For every power of a path, domination counts are log-concave, including arbitrary nonnegative multiplicative vertex weights; more generally for interval-neighborhood graphs. Remaining: Binomial-normalized ultra-log-concavity and the full cycle assertion remain unresolved. B3 continuation (7 Oct): B3C-01 Weighted interval ULC through nine variables; B3C-02 All-dimensional endpoint inequalities; B3C-03 Laminar interval ULC; B3C-10 One-bit inclusion matching fails; B3C-11 Coefficientwise ULC fails; none closes the question. Recorded from the external B3 return  (backfilled 2026-10-08); initial argument review and bounded independent controls in the intake; not independently re-derived here. [Details](../../solutions/b3-2026-10-06/README.md).
- **Related result** (B3C-01: Weighted interval ULC through nine variables): For every integer 0<=m<=9, every binary family on m positions defined by arbitrary integer lower/upper bounds on sums over linear intervals, and all nonnegative real position weights, its weighted rank sequence is ultra-log-concave of order m. Limits: All dimensions and cycle domination remain open; numerical ULC is not coefficientwise ULC. [Report](../../solutions/b3-continuation-2026-10-07/README.md).
- **Related result** (B3C-02: All-dimensional endpoint inequalities): For every such linear interval family in every integer dimension m>=0 and every nonnegative weight vector, k(m-k)f_k^2 >= (k+1)(m-k+1)f_(k-1)f_(k+1) at k in {1,2,3,4,m-4,m-3,m-2,m-1} intersect {1,...,m-1}. Limits: Middle inequalities in dimensions >=10 are not established. Uses Kahn-Neiman Theorem 9. [Report](../../solutions/b3-continuation-2026-10-07/README.md).
- **Related result** (B3C-03: Laminar interval ULC): For every integer m>=0, every laminar family of integer-bounded linear intervals on m binary positions, and all nonnegative position weights, the weighted feasible-word ranks are ULC of order m. Limits: Typical overlapping path neighborhoods are not laminar. Convolution closure is published, not claimed new. [Report](../../solutions/b3-continuation-2026-10-07/README.md).
- **Counterexample (to a stronger or nearby claim)** (B3C-10: One-bit inclusion matching fails): In dimension six, equations x1+x2=x2+x3=x4+x5=x5+x6=1 give rank counts (0,0,1,2,1,0,0). The unique rank-two word 010010 has no feasible rank-three superset. Limits: Refutes the stated stronger matching route, not APP or ULC. The stalled agent matching definition was not supplied. [Report](../../solutions/b3-continuation-2026-10-07/README.md).
- **Counterexample (to a stronger or nearby claim)** (B3C-11: Coefficientwise ULC fails): The unrestricted two-variable family has central normalized ULC defect w1^2-2\*w1\*w2+w2^2, whose mixed coefficient is -2. Limits: Numerical nonnegativity survives, since the defect is (w1-w2)^2. [Report](../../solutions/b3-continuation-2026-10-07/README.md).

**Further links.** [1](https://arxiv.org/abs/2408.12731) · [2](https://www3.nd.edu/~dgalvin1/pdf/journal/domination-arxiv.pdf)


<a id="q165"></a>

## Q165. Let γₖ(Pₙ) count dominating k-sets in the n-vertex path. For each ε = 0 or 1, mu…

**Status:** Solved here: proved · **Kind:** conjecture (Conjecture 5.1.4) · **Collection** 2

Let γₖ(Pₙ) count dominating k-sets in the n-vertex path. For each ε = 0 or 1, must the polynomial obtained by summing γₖ(Pₙ)x^((k−ε)/2) over k congruent to ε modulo 2 have only real roots, for every n?

**Context.** Origin: The first conjecture is joint with David Galvin; the remaining three are new thesis formulations.

**Source.** Yufei Zhang. *Some Combinatorial Problems Involving Total Non-Negativity and Unimodality*. University of Notre Dame, 2025. Advisor(s): David Galvin. [primary source](https://ndownloader.figshare.com/files/54098216) · [record](https://curate.nd.edu/articles/thesis/Some_Combinatorial_Problems_Involving_Total_Non-Negativity_and_Unimodality/28786115) Location: Conjecture 5.1.4, printed p.83. Status evidence, checked 5 October 2026: Exact-topic and author searches found no subsequent resolution; available Galvin–Zhang paper establishes the weaker unimodality results.

**Results.**

- **Proved**: For every n>=1 both parity polynomials have only real nonpositive roots. Stronger: D_Pn(x)/x^ceil(n/3) is strictly Hurwitz stable. An all-length positive generating-function recurrence proves coefficientwise nonnegativity of Re(D_n(iy)D_(n-1)(-iy)) as a polynomial in y^2. Remaining: The zero polynomial component at n=1 is interpreted in the standard degenerate convention. Publication priority is unclaimed. Recorded from the external B3 return  (backfilled 2026-10-08); initial argument review and bounded independent controls in the intake; not independently re-derived here. [Details](../../solutions/b3-2026-10-06/README.md).

**Further links.** [1](https://arxiv.org/abs/2408.12731)


<a id="q166"></a>

## Q166. For positive n and ℓ ≥ 2, let Aℓ(n,k) count compositions of n into k positive pa…

**Status:** Solved here: proved · **Kind:** conjecture (Conjecture 5.1.7) · **Collection** 2

For positive n and ℓ ≥ 2, let Aℓ(n,k) count compositions of n into k positive parts with no run of ℓ consecutive parts equal to 1. Is the sequence Aℓ(n,k), indexed by k ≥ 0, always log-concave?

**Context.** Origin: The first conjecture is joint with David Galvin; the remaining three are new thesis formulations.

**Source.** Yufei Zhang. *Some Combinatorial Problems Involving Total Non-Negativity and Unimodality*. University of Notre Dame, 2025. Advisor(s): David Galvin. [primary source](https://ndownloader.figshare.com/files/54098216) · [record](https://curate.nd.edu/articles/thesis/Some_Combinatorial_Problems_Involving_Total_Non-Negativity_and_Unimodality/28786115) Location: Conjecture 5.1.7, printed p.86. Status evidence, checked 5 October 2026: Thesis reports extensive finite verification. Searches for restricted compositions, consecutive ones, log-concavity, and the author found no proof/disproof.

**Results.**

- **Proved**: For every n>0 and ell>=2, compositions avoiding ell consecutive unit parts have log-concave counts by number of parts. The proof covers any interval-sum constraints on binary words and all fixed nonnegative position weights. Remaining: Weighted conclusion is numerical for each weight choice, not coefficientwise log-concavity. Publication priority is unclaimed. B3 continuation (7 Oct): B3C-01 Weighted interval ULC through nine variables; B3C-03 Laminar interval ULC; none closes the question. Recorded from the external B3 return  (backfilled 2026-10-08); initial argument review and bounded independent controls in the intake; not independently re-derived here. [Details](../../solutions/b3-2026-10-06/README.md).
- **Related result** (B3C-01: Weighted interval ULC through nine variables): For every integer 0<=m<=9, every binary family on m positions defined by arbitrary integer lower/upper bounds on sums over linear intervals, and all nonnegative real position weights, its weighted rank sequence is ultra-log-concave of order m. Limits: All dimensions and cycle domination remain open; numerical ULC is not coefficientwise ULC. [Report](../../solutions/b3-continuation-2026-10-07/README.md).
- **Related result** (B3C-03: Laminar interval ULC): For every integer m>=0, every laminar family of integer-bounded linear intervals on m binary positions, and all nonnegative position weights, the weighted feasible-word ranks are ULC of order m. Limits: Typical overlapping path neighborhoods are not laminar. Convolution closure is published, not claimed new. [Report](../../solutions/b3-continuation-2026-10-07/README.md).


<a id="q167"></a>

## Q167. Which permutations π of {0,…,n} satisfy c[π(0)] ≤ ⋯ ≤ c[π(n)] for the coefficien…

**Status:** Open, partial results · **Kind:** open problem (Question 5.2.6) · **Collection** 2

Which permutations π of {0,…,n} satisfy c[π(0)] ≤ ⋯ ≤ c[π(n)] for the coefficients of the polynomial product (1+r₁x)⋯(1+rₙx), where every rᵢ is a positive integer? Ties permit every compatible ordering.

**Context.** Origin: The first conjecture is joint with David Galvin; the remaining three are new thesis formulations.

**Source.** Yufei Zhang. *Some Combinatorial Problems Involving Total Non-Negativity and Unimodality*. University of Notre Dame, 2025. Advisor(s): David Galvin. [primary source](https://ndownloader.figshare.com/files/54098216) · [record](https://curate.nd.edu/articles/thesis/Some_Combinatorial_Problems_Involving_Total_Non-Negativity_and_Unimodality/28786115) Location: Question 5.2.6, printed pp.97–98. Status evidence, checked 5 October 2026: The thesis leaves the integer restriction open. Searches for integer-root matching-polynomial order patterns and the author found no classification.

**Results.**

- **Partial result**: Complete all-integer classification, including every ordering compatible with ties, for n=1,2,3,4. Counts are 2,3,6,8; all orders have exact witnesses and exhaustiveness proofs. Remaining: General degree n remains unresolved. Recorded from the external B3 return  (backfilled 2026-10-08); initial argument review and bounded independent controls in the intake; not independently re-derived here. [Details](../../solutions/b3-2026-10-06/README.md).


<a id="q168"></a>

## Q168. Is s(1,j)=(j+2)/(2j+3) for every integer j≥1?

**Status:** Open · **Kind:** conjecture (Conjecture 2.4.1) · **Collection** 2

Is s(1,j)=(j+2)/(2j+3) for every integer j≥1?

**Context.** Origin: Joint thesis research with Linz and Lu (gaps), Gu, Hyatt, Linz, and Lu (outerplanar graphs), and Linz (codegrees). Shared notation: For simple n-vertex graphs, order adjacency eigenvalues λ₁≥⋯≥λₙ and define s(i,j)=lim_(n→∞) max_G (λ\_(i+1)(G)−λ\_(n−j)(G))/n.

**Source.** George Henry Brooks. *Explorations in Extremal Combinatorics: Graph Spectra, Codegree Squared Sum of Hypergraphs and Lin-Lu-Yau Ricci Curvature*. University of South Carolina, 2025. Advisor(s): Linyuan Lu. [primary source](https://scholarcommons.sc.edu/cgi/viewcontent.cgi?article=9363&context=etd) · [record](https://scholarcommons.sc.edu/etd/8458/) Location: Conjecture 2.4.1, printed p.23; definition pp.4–5. Status evidence, checked 5 October 2026: July 2026 follow-on paper updates the spectral-gap bounds and still shows gaps at these conjectured values; its table gives, e.g., 0.6000≤s_1,1≤0.6124. No full resolution found.

**Further links.** [1](https://arxiv.org/html/2607.15941v1) · [2](https://doi.org/10.1016/j.laa.2025.10.024)


<a id="q169"></a>

## Q169. For fixed k≥2 and sufficiently large n=kq+1, is the maximum kth adjacency eigenv…

**Status:** Open · **Kind:** conjecture (Conjecture 3.1.1) · **Collection** 2

For fixed k≥2 and sufficiently large n=kq+1, is the maximum kth adjacency eigenvalue among connected outerplanar n-vertex graphs the spectral radius of the fan K₁ joined to a (q−1)-vertex path? Must every extremizer have a cut vertex leaving k disjoint such fans?

**Context.** Origin: Joint thesis research with Linz and Lu (gaps), Gu, Hyatt, Linz, and Lu (outerplanar graphs), and Linz (codegrees). Shared notation: For simple n-vertex graphs, order adjacency eigenvalues λ₁≥⋯≥λₙ and define s(i,j)=lim_(n→∞) max_G (λ\_(i+1)(G)−λ\_(n−j)(G))/n.

**Source.** George Henry Brooks. *Explorations in Extremal Combinatorics: Graph Spectra, Codegree Squared Sum of Hypergraphs and Lin-Lu-Yau Ricci Curvature*. University of South Carolina, 2025. Advisor(s): Linyuan Lu. [primary source](https://scholarcommons.sc.edu/cgi/viewcontent.cgi?article=9363&context=etd) · [record](https://scholarcommons.sc.edu/etd/8458/) Location: Conjecture 3.1.1, printed p.26. Status evidence, checked 5 October 2026: The 2025 associated paper proves the leading asymptotic and the k=2 cases; its general exact description remains conjectural. Targeted later searches found no general resolution.

**Results.**

- **Investigated, unresolved** (B7: submitted unresolved): No new analysis or status promotion in this return. Remaining/limits: not_attempted Intake: Scope and identity checked; no independent proof or renewed literature audit of this question. [Report](../../solutions/b7-2026-10-07/README.md).

**Further links.** [1](https://arxiv.org/abs/2309.08548) · [2](https://doi.org/10.1016/j.disc.2025.114416)


<a id="q170"></a>

## Q170. For k≥4, n>2k, and an intersecting family F of k-subsets of {1,…,n} with empty t…

**Status:** Open · **Kind:** conjecture (Conjecture 4.4.2) · **Collection** 2

For k≥4, n>2k, and an intersecting family F of k-subsets of {1,…,n} with empty total intersection, is ∑\_(|E|=k−1)|{A∈F:E⊆A}|² uniquely maximized, up to relabeling, by {A:|A|=k, 1∈A, A∩{2,…,k+1}≠∅}∪{{2,…,k+1}}?

**Context.** Origin: Joint thesis research with Linz and Lu (gaps), Gu, Hyatt, Linz, and Lu (outerplanar graphs), and Linz (codegrees). Shared notation: For simple n-vertex graphs, order adjacency eigenvalues λ₁≥⋯≥λₙ and define s(i,j)=lim_(n→∞) max_G (λ\_(i+1)(G)−λ\_(n−j)(G))/n.

**Source.** George Henry Brooks. *Explorations in Extremal Combinatorics: Graph Spectra, Codegree Squared Sum of Hypergraphs and Lin-Lu-Yau Ricci Curvature*. University of South Carolina, 2025. Advisor(s): Linyuan Lu. [primary source](https://scholarcommons.sc.edu/cgi/viewcontent.cgi?article=9363&context=etd) · [record](https://scholarcommons.sc.edu/etd/8458/) Location: Conjecture 4.4.2, printed pp.83–84; H defined earlier in Chapter 4. Status evidence, checked 5 October 2026: Wu–Zhang (2025), §6 Conjecture 6.1, explicitly retain the claim and state that their method establishes n≥2.5k. The remaining range 2k&lt;n<2.5k is not resolved by that paper or later searches.

**Further links.** [1](https://arxiv.org/html/2505.08279v1#S6) · [2](https://arxiv.org/abs/2310.09379)


<a id="q171"></a>

## Q171. Let I_N be the maximum order of isomorphic induced subgraphs in two independent …

**Status:** Open · **Kind:** open problem (Problem 1) · **Collection** 2

Let I_N be the maximum order of isomorphic induced subgraphs in two independent G(N,p) graphs. For fixed ε > 0, p tending to zero, and p/N^(−2/3+ε) tending to infinity, is I_N concentrated on two consecutive integers with probability tending to one?

**Context.** Origin: Specific sparse-case question posed jointly by Surya, Warnke, and Zhu after their dense theorem. Joint Surya–Warnke–Zhu generalization proposed after their principal theorems. Joint Surya–Warnke–Zhu question strengthening their two-point concentration result; their theorem gives one-point concentration on a density-one set of N.

**Source.** Erlang Surya. *Concentration and Sharp Thresholds in Random Graphs*. University of California San Diego, 2025. Advisor(s): Lutz Warnke. [primary source](https://mathweb.ucsd.edu/~lwarnke/PhD_Thesis_ErlangSurya.pdf) · [record](https://escholarship.org/uc/item/7vt625fh) Location: Chapter 3, Problem 1 discussion, printed p.128. Status evidence, checked 5 October 2026: January 2025 author revision still poses it. Later related isomorphism work treats constant probabilities/equal sizes rather than this sparse two-point statement; no resolution found.

**Further links.** [1](https://mathweb.ucsd.edu/~lwarnke/GraphIsomorphism_draft.pdf) · [2](https://arxiv.org/abs/2410.00214)


<a id="q172"></a>

## Q172. Fix p₁,p₂ in (0,1). Determine the typical maximum order of a common induced subg…

**Status:** Open · **Kind:** open problem (Problem 2) · **Collection** 2

Fix p₁,p₂ in (0,1). Determine the typical maximum order of a common induced subgraph of independent G(N₁,p₁) and G(N₂,p₂), as both vertex counts tend to infinity, including intermediate size ratios between the known embedding and equal-size regimes.

**Context.** Origin: Specific sparse-case question posed jointly by Surya, Warnke, and Zhu after their dense theorem. Joint Surya–Warnke–Zhu generalization proposed after their principal theorems. Joint Surya–Warnke–Zhu question strengthening their two-point concentration result; their theorem gives one-point concentration on a density-one set of N.

**Source.** Erlang Surya. *Concentration and Sharp Thresholds in Random Graphs*. University of California San Diego, 2025. Advisor(s): Lutz Warnke. [primary source](https://mathweb.ucsd.edu/~lwarnke/PhD_Thesis_ErlangSurya.pdf) · [record](https://escholarship.org/uc/item/7vt625fh) Location: Chapter 3, Problem 2, printed p.128. Status evidence, checked 5 October 2026: The 2025 revised source retains it. Diamantidis–Konstantopoulos–Yuan’s later revision treats the embedding case and equal graph orders for the common-subgraph theorem, not the arbitrary two-size regime.

**Further links.** [1](https://mathweb.ucsd.edu/~lwarnke/GraphIsomorphism_draft.pdf) · [2](https://arxiv.org/abs/2410.00214)


<a id="q173"></a>

## Q173. Fix p₁,p₂ in (0,1), and let I_N be the maximum common induced-subgraph order of …

**Status:** Open · **Kind:** open problem · **Collection** 2

Fix p₁,p₂ in (0,1), and let I_N be the maximum common induced-subgraph order of independent G(N,p₁) and G(N,p₂). Do there exist c > 0, infinitely many N, and integers a_N such that both P(I_N = a_N) ≥ c and P(I_N = a_N+1) ≥ c?

**Context.** Origin: Specific sparse-case question posed jointly by Surya, Warnke, and Zhu after their dense theorem. Joint Surya–Warnke–Zhu generalization proposed after their principal theorems. Joint Surya–Warnke–Zhu question strengthening their two-point concentration result; their theorem gives one-point concentration on a density-one set of N.

**Source.** Erlang Surya. *Concentration and Sharp Thresholds in Random Graphs*. University of California San Diego, 2025. Advisor(s): Lutz Warnke. [primary source](https://mathweb.ucsd.edu/~lwarnke/PhD_Thesis_ErlangSurya.pdf) · [record](https://escholarship.org/uc/item/7vt625fh) Location: Chapter 3, Remark 32, printed p.116. Status evidence, checked 5 October 2026: Retained in the 2025 author revision. Searches for common-induced-subgraph fluctuation and two-point results found no later nondegeneracy proof.

**Further links.** [1](https://mathweb.ucsd.edu/~lwarnke/GraphIsomorphism_draft.pdf) · [2](https://doi.org/10.1007/s00493-025-00157-z)


<a id="q174"></a>

## Q174. For every k ≥ 1, does every k-tree admit a proper coloring with k+2 colors in wh…

**Status:** Open · **Kind:** conjecture (Conjecture 6.6) · **Collection** 2

For every k ≥ 1, does every k-tree admit a proper coloring with k+2 colors in which each non-isolated vertex has some color occurring an odd number of times among its neighbors? A k-tree starts from the complete graph on k+1 vertices and repeatedly adds a vertex adjacent to an existing k-clique.

**Context.** Origin: Author’s joint conjecture with Kenta Ozeki, stated after proving k=2,3. Joint Kashima–Škrekovski–Xu conjecture arising from their new degree-choosability variant. Author’s proposed component bound, strengthening his proved 2-factor existence theorem.

**Source.** Masaki Kashima. *Colorings of Graphs and Vertex Partitions of Graphs with Degree Conditions*. Keio University, 2025. Advisor(s): Katsuhiro Ota. [primary source](https://koara.lib.keio.ac.jp/xoonips/modules/xoonips/download.php/KO50002002-20246410-0003.pdf?file_id=187950) · [record](https://www.math.keio.ac.jp/academic/thesis/thesis2024/) Location: Conjecture 6.6, printed p.53. Status evidence, checked 5 October 2026: Their April 2025 paper still proposes the general bound and gives the weaker k+2 floor(log2 k)+3 theorem. Targeted later searches found no full resolution.

**Further links.** [1](https://arxiv.org/abs/2504.20573)


<a id="q175"></a>

## Q175. Does every connected graph other than the 5-cycle admit a proper coloring from e…

**Status:** Open · **Kind:** conjecture (Conjecture 7.7) · **Collection** 2

Does every connected graph other than the 5-cycle admit a proper coloring from every vertex-list assignment with at least d(v)+2 available colors at v, such that each non-isolated vertex sees some color exactly once among its neighbors?

**Context.** Origin: Author’s joint conjecture with Kenta Ozeki, stated after proving k=2,3. Joint Kashima–Škrekovski–Xu conjecture arising from their new degree-choosability variant. Author’s proposed component bound, strengthening his proved 2-factor existence theorem.

**Source.** Masaki Kashima. *Colorings of Graphs and Vertex Partitions of Graphs with Degree Conditions*. Keio University, 2025. Advisor(s): Katsuhiro Ota. [primary source](https://koara.lib.keio.ac.jp/xoonips/modules/xoonips/download.php/KO50002002-20246410-0003.pdf?file_id=187950) · [record](https://www.math.keio.ac.jp/academic/thesis/thesis2024/) Location: Conjecture 7.7, printed p.74. Status evidence, checked 5 October 2026: January and September 2026 papers prove sparse-graph cases only, leaving the general assertion open; September’s result improves the planar-girth sufficient condition to eight.

**Further links.** [1](https://arxiv.org/abs/2601.15611) · [2](https://arxiv.org/abs/2609.11249)


<a id="q176"></a>

## Q176. Let G have n vertices, and suppose every nonempty independent set I satisfies |I…

**Status:** Open · **Kind:** conjecture (Conjecture 10.7) · **Collection** 2

Let G have n vertices, and suppose every nonempty independent set I satisfies |I| < min{d(v): v in I}. Define α\*(G) as the largest |I| among independent sets whose vertex-degree sum is less than n. Must G have a spanning disjoint union of at most α\*(G) cycles?

**Context.** Origin: Author’s joint conjecture with Kenta Ozeki, stated after proving k=2,3. Joint Kashima–Škrekovski–Xu conjecture arising from their new degree-choosability variant. Author’s proposed component bound, strengthening his proved 2-factor existence theorem.

**Source.** Masaki Kashima. *Colorings of Graphs and Vertex Partitions of Graphs with Degree Conditions*. Keio University, 2025. Advisor(s): Katsuhiro Ota. [primary source](https://koara.lib.keio.ac.jp/xoonips/modules/xoonips/download.php/KO50002002-20246410-0003.pdf?file_id=187950) · [record](https://www.math.keio.ac.jp/academic/thesis/thesis2024/) Location: Conjecture 10.7, printed p.114; invariants defined in Chapter 8. Status evidence, checked 5 October 2026: Kashima’s April 2025 paper retains the equivalent degree-sum formulation as Conjecture 6, and proves it only for claw-free graphs. No general resolution found.

**Further links.** [1](https://arxiv.org/html/2504.08268v1)


<a id="q177"></a>

## Q177. For a finite Weyl group W with Coxeter length ℓ, let U be the interval [e,u] in …

**Status:** Open · **Kind:** conjecture (Conjecture 5.4.6) · **Collection** 2

For a finite Weyl group W with Coxeter length ℓ, let U be the interval [e,u] in right weak order and define W/U = {w in W: ℓ(wx) = ℓ(w)+ℓ(x) for every x in U}. Is the multiplication map from (W/U) × U to W always surjective?

**Context.** Origin: Gaetz–Gao joint conjecture; thesis §5.4.3 proposes the extension beyond type A.

**Source.** Christian Gaetz. *New combinatorics of the weak and strong Bruhat orders*. Massachusetts Institute of Technology, 2021. Advisor(s): Alexander Postnikov. [primary source](https://dspace.mit.edu/server/api/core/bitstreams/a114c8e7-9da4-4d12-8bc5-d9705f71ee78/content) · [record](https://dspace.mit.edu/server/api/core/bitstreams/a114c8e7-9da4-4d12-8bc5-d9705f71ee78/content) Location: Conjecture 5.4.6, printed p.103; Theorem 5.4.1, p.94; quotient definition, §5.3. Status evidence, checked 5 October 2026: The original Gaetz–Gao paper proves surjectivity in type A only. Searches through the current date located no proof for arbitrary finite Weyl groups; the later type-B splitting paper does not settle this general assertion.

**Further links.** [1](https://arxiv.org/abs/1911.11172) · [2](https://arxiv.org/abs/2309.02932)


<a id="q178"></a>

## Q178. For a finite Weyl group W, let U be the interval [e,u] in right weak order and d…

**Status:** Open · **Kind:** conjecture (Conjecture 5.4.7) · **Collection** 2

For a finite Weyl group W, let U be the interval [e,u] in right weak order and define W/U = {w: ℓ(wx) = ℓ(w)+ℓ(x) for every x in U}, where ℓ is Coxeter length. Is multiplication from (W/U) × U to W bijective exactly when u is separable? Separability is recursive: rank-one elements qualify; reducible systems qualify componentwise; otherwise some simple root α has all positive roots containing α either inverted by u or all uninverted, and the restriction obtained by deleting α is separable. Restriction intersects the inversion set with the parabolic root subsystem.

**Context.** Origin: Gaetz–Gao joint conjecture; thesis §5.4.3 proposes the extension beyond type A.

**Source.** Christian Gaetz. *New combinatorics of the weak and strong Bruhat orders*. Massachusetts Institute of Technology, 2021. Advisor(s): Alexander Postnikov. [primary source](https://dspace.mit.edu/server/api/core/bitstreams/a114c8e7-9da4-4d12-8bc5-d9705f71ee78/content) · [record](https://dspace.mit.edu/server/api/core/bitstreams/a114c8e7-9da4-4d12-8bc5-d9705f71ee78/content) Location: Conjecture 5.4.7, printed p.103; Definition 5.1.1, p.66. Status evidence, checked 5 October 2026: Yu–Liu, published in Journal of Combinatorial Theory A in 2025, establishes the conjecture for type B, beyond the original type-A case. The general finite-Weyl-group assertion remains posed; no all-types resolution was located.

**Further links.** [1](https://arxiv.org/abs/2309.02932) · [2](https://doi.org/10.1016/j.jcta.2025.106021)


<a id="q179"></a>

## Q179. For a k-by-n matrix whose ordered maximal minors Δ\_I are positive, let M index t…

**Status:** Open · **Kind:** conjecture (Conjecture 1.5.7) · **Collection** 2

For a k-by-n matrix whose ordered maximal minors Δ\_I are positive, let M index the minimum-valued minors. Must |M| ≤ k(n−k)+1, with equality only for weakly separated M? Weak separation forbids cyclically interleaving a,b,c,d with a,c in I minus J and b,d in J minus I, for every I,J in M.

**Context.** Origin: Farber–Postnikov joint conjecture, refined after their counterexamples to a stronger earlier formulation. Farber–Mandelshtam joint formulation, developed in thesis Chapter 2 and their 2015 preprint.

**Source.** Miriam Farber. *Arrangement of minors in the positive Grassmannian*. Massachusetts Institute of Technology, 2017. Advisor(s): Alexander Postnikov. [primary source](https://dspace.mit.edu/server/api/core/bitstreams/8b53470f-403b-49f9-8a4d-527233b00d49/content) · [record](https://dspace.mit.edu/entities/publication/40720e53-9bb4-46c1-b62b-2ad52fd369c6) Location: Conjecture 1.5.7, printed p.32 (equivalent reformulation: Conjecture 1.7.3, p.38). Status evidence, checked 5 October 2026: The published Farber–Postnikov work and thesis retain this extremal-size conjecture. Targeted searches found no later full resolution. Their disproved assertion that every smallest-minor arrangement is weakly separated is deliberately excluded.

**Further links.** [1](https://arxiv.org/abs/1502.01434)

*Also among the automatically extracted thesis statements: `5f938b66c6e4f1df100b`.*


<a id="q180"></a>

## Q180. Let J be a maximal largest-minor arrangement in the positive Grassmannian Gr⁺(k,…

**Status:** Open · **Kind:** conjecture (Conjecture 2.4.3) · **Collection** 2

Let J be a maximal largest-minor arrangement in the positive Grassmannian Gr⁺(k,n). In the dual graph of Sturmfels’ hypersimplex triangulation, define cubical distance by charging one step to cross any cube. Let d(W,J) be the minimum distance from J to a maximal arrangement containing W. If d(W,J) = t, must every realization of J have at least t distinct minor values greater than Δ[W]?

**Context.** Origin: Farber–Postnikov joint conjecture, refined after their counterexamples to a stronger earlier formulation. Farber–Mandelshtam joint formulation, developed in thesis Chapter 2 and their 2015 preprint.

**Source.** Miriam Farber. *Arrangement of minors in the positive Grassmannian*. Massachusetts Institute of Technology, 2017. Advisor(s): Alexander Postnikov. [primary source](https://dspace.mit.edu/server/api/core/bitstreams/8b53470f-403b-49f9-8a4d-527233b00d49/content) · [record](https://dspace.mit.edu/entities/publication/40720e53-9bb4-46c1-b62b-2ad52fd369c6) Location: Conjecture 2.4.3 and Definitions 2.4.1–2.4.2, printed pp.86–87. Status evidence, checked 5 October 2026: Andriets–Holikov’s July 2023 research paper, mentored by Mandelshtam, still treats the general conjecture as unresolved and proposes approaches. Searches through October 2026 found no general proof.

**Further links.** [1](https://arxiv.org/abs/1509.02600) · [2](https://math.mit.edu/research/highschool/primes/materials/2023/YD/Andriets-Holikov.pdf)

*Also among the automatically extracted thesis statements: `91a0715497710291ba5e`.*


<a id="q181"></a>

## Q181. Fix a prime p and k ≥ p+2. Do constants c,C > 0, depending only on p,k, permit f…

**Status:** Open · **Kind:** conjecture (Conjecture 5.0.3) · **Collection** 2

Fix a prime p and k ≥ p+2. Do constants c,C > 0, depending only on p,k, permit for every n a complex-valued function f on the n-dimensional vector space over Fₚ such that |f| ≤ 1, its Gowers Uᵏ norm is at least c, and |Eₓ f(x) exp(−2πiP(x)/p)| ≤ exp(−Cn) for every classical polynomial P of degree at most k−1? Field elements in the exponential use integer representatives.

**Context.** Origin: Chapter 5 is based on Tidor’s joint paper with Aaron Berger, Ashwin Sah and Mehtaab Sawhney; their Conjecture 1.3 is reproduced as 5.0.3.

**Source.** Jonathan Tidor. *Higher-order Fourier analysis with applications to additive combinatorics and theoretical computer science*. Massachusetts Institute of Technology, 2022. Advisor(s): Yufei Zhao. [primary source](https://dspace.mit.edu/server/api/core/bitstreams/62e9e3c0-d29a-4651-8ad2-434e3e48af27/content) · [record](https://math.mit.edu/documents/integral/integral_2023.pdf) Location: Conjecture 5.0.3, printed p.179. Status evidence, checked 5 October 2026: The 2022 published paper retains exponential decay as a conjecture, proving only a vanishing bound involving iterated logarithms. Exact-name and correlation-bound searches located no general resolution through October 2026.

**Further links.** [1](https://arxiv.org/abs/2107.07495) · [2](https://doi.org/10.1017/S0305004121000682)


<a id="q182"></a>

## Q182. Let Q arise from the product of chains {1,…,m} × {1,…,n} by deleting any chosen …

**Status:** Open · **Kind:** conjecture (Conjecture 4.5) · **Collection** 2

Let Q arise from the product of chains {1,…,m} × {1,…,n} by deleting any chosen horizontal cover relations (i,j) < (i,j+1) with i < m, then taking transitive closure. For each permutation σ of {1,…,n}, label (i,j) by i+m(σ(j)−1). Sum x^(des(w)) over all labeled linear extensions w and all σ, obtaining C_Q(x); des counts adjacent decreases. In the expansion C_Q(x) = Σᵣ γᵣ xʳ(1+x)^(m(n−1)−2r), must every γᵣ be nonnegative?

**Context.** Origin: Joint Beck–Deligeorgaki research; the thesis describes the proposed gamma-positivity and identifies the constituent paper. Candidate-contribution statement, p.52, credits her initiation and proofs.

**Source.** Danai Deligeorgaki. *Combinatorics and Algebraic Statistics through Polyhedra*. KTH Royal Institute of Technology, 2025. Advisor(s): Liam Solus (main advisor); Katharina Jochemko (coadvisor); Johan Håstad (coadvisor). [primary source](https://diva-portal.org/smash/get/diva2%3A1961783/FULLTEXT01.pdf) · [record](https://www.kth.se/profile/danaide?l=sv) Location: Summary §2.3, printed p.51, Paper Γ′ (Canon permutation posets); precise conjecture in constituent paper, Conjecture 4.5, p.13. Status evidence, checked 5 October 2026: The September 13, 2026 revision of the constituent paper still labels the assertion Conjecture 4.5. It proves the two endpoint classes and finite computed cases, but not all intermediate dissonant classes.

**Further links.** [1](https://arxiv.org/html/2410.03245v3) · [2](https://arxiv.org/abs/2410.03245)


<a id="q183"></a>

## Q183. For a skew Ferrers board λ/μ, let rₖ count placements of k rooks with distinct r…

**Status:** Open · **Kind:** open problem (Question 3.1.2) · **Collection** 2

For a skew Ferrers board λ/μ, let rₖ count placements of k rooks with distinct rows and columns and no rook southeast of another. If deleting rows and columns can never produce the shape (3,3,2)/(1), must the polynomial Σₖ rₖtᵏ have only real zeros?

**Context.** Origin: The thesis’s Outlook introduces this restriction using the author’s skew-shape correspondence and computations. Jal–Jochemko joint question generalizing their proved two-dimensional and special-norm cases; Paper A is explicitly included in the doctoral dissertation.

**Source.** Aryaman Jal. *Enumerative and matroidal aspects of rook placements*. KTH Royal Institute of Technology, 2025. Advisor(s): Katharina Jochemko (main advisor); Petter Brändén (coadvisor). [primary source](https://www.diva-portal.org/smash/get/diva2%3A1958137/FULLTEXT01.pdf) · [record](https://www.kth.se/profile/aryaman?l=sv) Location: Question 3.1.2, printed p.52; non-nesting definition 2.10, p.41. Status evidence, checked 5 October 2026: The full skew-shape class is not real-rooted. Jal’s July 2026 joint paper proves a generalized-snake subclass; neither that result nor the updated rook-matroid paper resolves the full pattern-avoiding class. No full resolution located.

**Results.**

- **Investigated, unresolved** (B3: submitted unresolved): Every board with at most two rows or at most two columns has a real-rooted non-nesting rook polynomial, by a quadratic discriminant bound. Remaining/limits: Only an elementary control subclass. The entire forbidden-board avoidance class is unresolved. [Report](../../solutions/b3-2026-10-06/README.md).

**Further links.** [1](https://arxiv.org/abs/2607.00922) · [2](https://arxiv.org/abs/2410.00127)


<a id="q184"></a>

## Q184. For every full-dimensional centrally symmetric polytope P in Rᵈ, centered at 0, …

**Status:** Open · **Kind:** open problem (Question 2) · **Collection** 2

For every full-dimensional centrally symmetric polytope P in Rᵈ, centered at 0, does its norm admit a bisection fan? For each ordered facet pair F,G, let B(F,G) be the cone generated by all differences v−u, where v is a vertex of F and u is a vertex of G. Must some complete polyhedral fan have the property that two generic points lie in the same open maximal cone exactly when they belong to identical collections of these B(F,G)? Generic means these membership patterns are locally constant.

**Context.** Origin: The thesis’s Outlook introduces this restriction using the author’s skew-shape correspondence and computations. Jal–Jochemko joint question generalizing their proved two-dimensional and special-norm cases; Paper A is explicitly included in the doctoral dissertation.

**Source.** Aryaman Jal. *Enumerative and matroidal aspects of rook placements*. KTH Royal Institute of Technology, 2025. Advisor(s): Katharina Jochemko (main advisor); Petter Brändén (coadvisor). [primary source](https://www.diva-portal.org/smash/get/diva2%3A1958137/FULLTEXT01.pdf) · [record](https://www.kth.se/profile/aryaman?l=sv) Location: Constituent Paper A, Polyhedral combinatorics of bisectors, §9 Question 2, p.29; thesis §2.1 pp.37–41 establishes the setting. Status evidence, checked 5 October 2026: The 2025 journal article retains Question 2, with proofs for polygons and several particular norm families. Exact bisection-fan searches through October 2026 located no general resolution.

**Further links.** [1](https://kth.diva-portal.org/smash/get/diva2%3A1957242/FULLTEXT01.pdf) · [2](https://doi.org/10.1515/advgeom-2025-0003)


<a id="q185"></a>

## Q185. Fix ε > 0 and let n tend to infinity through n congruent to 1 or 3 modulo 6. Doe…

**Status:** Open · **Kind:** conjecture (Conjecture 3.1.7) · **Collection** 2

Fix ε > 0 and let n tend to infinity through n congruent to 1 or 3 modulo 6. Does the random 3-uniform hypergraph, with each triple independently present with probability (2+ε) log(n)/n, contain a Steiner triple system with probability tending to one? Such a system selects triples so that every vertex pair occurs exactly once.

**Context.** Origin: Sah–Sawhney–Simkin joint conjecture, explicitly introduced in their Further directions and incorporated in thesis §3.1.4; sharper than the older constant-factor threshold question. Status evidence for this section, checked 5 October 2026: Later work establishes the threshold only up to a constant factor. Kang–Kelly–Kühn–Methuku–Osthus explicitly retain both the constant-2 and hitting-time conjectures; a June 2026 threshold survey in Delcourt–Kelly–Postle reports the known order of magnitude, not these sharper assertions. No full resolution found. Status source 1: https://pure-oai.bham.ac.uk/ws/portalfiles/portal/188579563/LSthreshold20230314.pdf
Status source 2: https://doi.org/10.1017/S0305004126102059

**Source.** Ashwin Sah. *Random and exact structures in combinatorics*. Massachusetts Institute of Technology, 2024. Advisor(s): Yufei Zhao. [primary source](https://dspace.mit.edu/server/api/core/bitstreams/b25f0f66-7126-4a1b-a9d0-7ab4363da07e/content) · [record](https://dspace.mit.edu/entities/publication/1e05c0fc-1380-4594-ad3c-4147e448b1a1) Location: Conjecture 3.1.7, printed p.79. Status: see the section-wide dated evidence above.

**Further links.** [1](https://pure-oai.bham.ac.uk/ws/portalfiles/portal/188579563/LSthreshold20230314.pdf) · [2](https://doi.org/10.1017/S0305004126102059)


<a id="q186"></a>

## Q186. Reveal all triples of {1,…,n} in uniformly random order, where n is congruent to…

**Status:** Open · **Kind:** conjecture (Conjecture 3.1.8) · **Collection** 2

Reveal all triples of {1,…,n} in uniformly random order, where n is congruent to 1 or 3 modulo 6. Let τ be the first time every vertex pair belongs to a revealed triple. Does the hypergraph at time τ already contain a Steiner triple system with probability tending to one as n tends to infinity?

**Context.** Origin: Sah–Sawhney–Simkin joint conjecture, explicitly introduced in their Further directions and incorporated in thesis §3.1.4; sharper than the older constant-factor threshold question. Status evidence for this section, checked 5 October 2026: Later work establishes the threshold only up to a constant factor. Kang–Kelly–Kühn–Methuku–Osthus explicitly retain both the constant-2 and hitting-time conjectures; a June 2026 threshold survey in Delcourt–Kelly–Postle reports the known order of magnitude, not these sharper assertions. No full resolution found. Status source 1: https://pure-oai.bham.ac.uk/ws/portalfiles/portal/188579563/LSthreshold20230314.pdf
Status source 2: https://doi.org/10.1017/S0305004126102059

**Source.** Ashwin Sah. *Random and exact structures in combinatorics*. Massachusetts Institute of Technology, 2024. Advisor(s): Yufei Zhao. [primary source](https://dspace.mit.edu/server/api/core/bitstreams/b25f0f66-7126-4a1b-a9d0-7ab4363da07e/content) · [record](https://dspace.mit.edu/entities/publication/1e05c0fc-1380-4594-ad3c-4147e448b1a1) Location: Conjecture 3.1.8, printed p.79. Status: see the section-wide dated evidence above.

**Further links.** [1](https://pure-oai.bham.ac.uk/ws/portalfiles/portal/188579563/LSthreshold20230314.pdf) · [2](https://doi.org/10.1017/S0305004126102059)


<a id="q187"></a>

## Q187. Fix a partition λ=(λ₁,…,λₙ) with n=λ₁≥⋯≥λₙ>0 with λᵢ ≥ n+1−i. Replace every cell…

**Status:** Solved here: proved · **Kind:** conjecture (Conjecture 3.4.9) · **Collection** 2

Fix a partition λ=(λ₁,…,λₙ) with n=λ₁≥⋯≥λₙ>0 with λᵢ ≥ n+1−i. Replace every cell of its French Young diagram by an N-by-N block and choose uniformly a placement with one rook in each row and column. Let X_N(t) be the fraction of rooks at positions (i,j) with i+j ≤ nNt, indexing matrix rows from the top. The thesis proves that mλ(t) = lim E[X_N(t)] exists. Must sup{ |X_N(t)−mλ(t)| : 0 ≤ t ≤ 2 } tend to zero in probability as N tends to infinity?

**Context.** Origin: Author’s own conjecture from his solo paper Large-scale Rook Placements, Conjecture 5.9, reproduced in the thesis; not an earlier third-party conjecture despite the citation label.

**Source.** Pakawut Jiradilok. *Inequalities and Asymptotic Formulas in Algebraic Combinatorics*. Massachusetts Institute of Technology, 2022. Advisor(s): Alexander Postnikov. [primary source](https://dspace.mit.edu/server/api/core/bitstreams/b1d4131f-6b27-4242-af21-637d52fb7e79/content) · [record](https://math.mit.edu/documents/integral/integral_2023.pdf) Location: Conjecture 3.4.9, printed pp.79–80; Proposition 3.4.8 and equation (3.22), pp.78–79. Status evidence, checked 5 October 2026: The source proves convergence for unrestricted random permutations (square diagrams), and convergence of expectations generally. Searches by author, title and limit-shape terminology located no full resolution of the fixed general-shape conjecture.

**Results.**

- **Proved**: Yes. Revealing rows in nested order, a swap coupling changes each antidiagonal count by at most one, so a martingale bound gives P(sup_t |X_N(t) − E X_N(t)| ≥ u) ≤ 2(2nN+1)exp(−nNu²/2). The source's marginal dilation identity (confirmed here by exact enumeration on small dilated boards) puts E X_N within 2/N of m_λ uniformly. This gives convergence in probability and, by Borel–Cantelli, almost surely. Reconstructed checkpoint without its original checkers; re-derived here by hand and spot-checked with independent exact computations on 10 October 2026. Not external peer review or a novelty certification. Filed from the public-repo research round seven-problems-2026-10-10. [Details](../../solutions/seven-problems-2026-10-10/Q187.md).

**Further links.** [1](https://arxiv.org/abs/2204.00615) · [2](https://sites.google.com/view/pjcombin/research)


<a id="q200"></a>

## Q200. If X is a finite 3-connected planar graph, must its quantum automorphism group Q…

**Status:** Open · **Kind:** open problem · **Collection** 2

If X is a finite 3-connected planar graph, must its quantum automorphism group Qut(X) be a closed quantum subgroup of the free orthogonal quantum group O₃⁺? The algebra C(Qut(X)) is generated by a magic unitary commuting with the adjacency matrix: a matrix of projections whose rows and columns sum to 1. The group O₃⁺ is defined by a 3-by-3 orthogonal matrix of self-adjoint generators. Subgroup inclusion means a surjective, coproduct-preserving \*-homomorphism from C(O₃⁺) to C(Qut(X)).

**Context.** Origin: The author explicitly proposes this conjecture in the concluding discussion, following his joint development of free inhomogeneous wreath products. The assertion is not attributed to an earlier source.

**Source.** Prem Nigam Kar. *Quantum Graph Theory: Graph Based Nonlocal Games and Quantum Automorphism Groups of Graphs*. Technical University of Denmark, 2025. Advisor(s): David E. Roberson (main supervisor); Carsten Thomassen (supervisor). [primary source](https://backend.orbit.dtu.dk/ws/portalfiles/portal/432894668/PhD_Thesis_2_.pdf) · [record](https://orbit.dtu.dk/en/publications/quantum-graph-theory-graph-based-nonlocal-games-and-quantum-autom/) Location: Unnumbered conjecture in Chapter 10 Discussion, printed p.153. Status evidence, checked 5 October 2026: The related 2025 joint paper treats outerplanar and block graphs, not arbitrary 3-connected planar graphs. Searches on the exact graph class and free-orthogonal-group formulation located no resolution through October 2026.

**Further links.** [1](https://arxiv.org/abs/2504.13826) · [2](https://zemanpeter.github.io/publications/)


<a id="q253"></a>

## Q253. Fix \$m\ge2\$ and \$n\ge r\ge2\$. Must \$\operatorname{sat}(P_n^d,P_r^m)\$ and its axi…

**Status:** Open · **Kind:** open problem · **Collection** 3

Fix \$m\ge2\$ and \$n\ge r\ge2\$. Must \$\operatorname{sat}(P_n^d,P_r^m)\$ and its axis-aligned variant both be \$O(n^d)\$ as \$d\to\infty\$? Powers here are Cartesian products. Saturation minimizes the edges of a spanning subgraph avoiding the specified pattern but creating one after any missing edge is added. Axis alignment restricts patterns to products of \$m\$ contiguous \$r\$-vertex intervals with other coordinates fixed.

**Context.** Origin: Grid and chain-saturation questions are joint with Morrison and Scott. The cube weak-saturation question is explicitly posed by Noel.

**Source.** Jonathan Andrew Noel. *Extremal combinatorics, graph limits and computational complexity*. University of Oxford, 2016. Advisor(s): Alex Scott. [primary source](https://ora.ox.ac.uk/objects/uuid:8743ff27-b5e9-403a-a52a-3d6299792c7b/files/m5c81b1ebbadf0d73a5e367a33505f0ad) · [record](https://ora.ox.ac.uk/objects/uuid%3A8743ff27-b5e9-403a-a52a-3d6299792c7b) Location: Questions 2.30–2.31, printed p.26.

**Further links.** [1](https://people.maths.ox.ac.uk/scott/Papers/cubesat.pdf) · [2](https://sites.miamioh.edu/millerz/files/2025/03/a-saturaion-problem-on-meshes-revision.pdf)

*Also among the automatically extracted thesis statements: `49f4843f04374a567625`, `5792ee3699c47020dff4`.*


<a id="q254"></a>

## Q254. Let \$s(k)\$ be the eventual minimum size of a maximal family of subsets of \$[n]\$ …

**Status:** Open · **Kind:** open problem (Problem 3.19) · **Collection** 3

Let \$s(k)\$ be the eventual minimum size of a maximal family of subsets of \$[n]\$ containing no inclusion chain of \$k+1\$ sets, for \$n\$ sufficiently large. Determine \$c\$ satisfying \$s(k)=2^{(c+o(1))k}\$ as \$k\to\infty\$.

**Context.** Origin: Grid and chain-saturation questions are joint with Morrison and Scott. The cube weak-saturation question is explicitly posed by Noel.

**Source.** Jonathan Andrew Noel. *Extremal combinatorics, graph limits and computational complexity*. University of Oxford, 2016. Advisor(s): Alex Scott. [primary source](https://ora.ox.ac.uk/objects/uuid:8743ff27-b5e9-403a-a52a-3d6299792c7b/files/m5c81b1ebbadf0d73a5e367a33505f0ad) · [record](https://ora.ox.ac.uk/objects/uuid%3A8743ff27-b5e9-403a-a52a-3d6299792c7b) Location: Problem 3.19, printed p.38; definitions and existence of c, pp.3–4.

**Further links.** [1](https://arxiv.org/abs/2402.14113) · [2](https://people.maths.ox.ac.uk/scott/Papers/saturatedsperner.pdf)

*Also among the automatically extracted thesis statements: `5d4697715681617aa7ef`.*


<a id="q255"></a>

## Q255. Determine \$\operatorname{wsat}(K_n,Q_d)\$ for fixed \$d\ge3\$ and \$n\ge2^d\$. This i…

**Status:** Open · **Kind:** open problem (Problem 4.8) · **Collection** 3

Determine \$\operatorname{wsat}(K_n,Q_d)\$ for fixed \$d\ge3\$ and \$n\ge2^d\$. This is the minimum number of initial edges from which \$K_n\$ can be completed one edge at a time, every added edge completing a new \$d\$-dimensional cube \$Q_d\$.

**Context.** Origin: Grid and chain-saturation questions are joint with Morrison and Scott. The cube weak-saturation question is explicitly posed by Noel.

**Source.** Jonathan Andrew Noel. *Extremal combinatorics, graph limits and computational complexity*. University of Oxford, 2016. Advisor(s): Alex Scott. [primary source](https://ora.ox.ac.uk/objects/uuid:8743ff27-b5e9-403a-a52a-3d6299792c7b/files/m5c81b1ebbadf0d73a5e367a33505f0ad) · [record](https://ora.ox.ac.uk/objects/uuid%3A8743ff27-b5e9-403a-a52a-3d6299792c7b) Location: Unnumbered question following Problem 4.8, printed pp.48–49; Conjecture 4.9 proposes an asymptotic answer.

**Further links.** [1](https://www.openproblemgarden.org/op/weak_saturation_of_the_cube_in_the_clique) · [2](https://www.ias.edu/sites/default/files/Trakulthongchai_Xu_Zhu.pdf)

*Also among the automatically extracted thesis statements: `249dba66ca19dd92bd89`.*


<a id="q256"></a>

## Q256. Characterize the caterpillars admitting a proper total dominating set. A caterpi…

**Status:** Solved here: proved · **Kind:** open problem (Problem 4.3.8) · **Collection** 3

Characterize the caterpillars admitting a proper total dominating set. A caterpillar is a tree whose non-leaf vertices induce a path.

**Context.** Origin: New domination and coloring questions from research with Ping Zhang, retained in the 2026 dissertation. Shared setup for questions 256, 257, 258: A set \$S\$ is total dominating if \$\sigma(v)=|N(v)\cap S|>0\$ for every vertex; it is proper total dominating if adjacent vertices also have different \$\sigma\$-values.

**Source.** Sawyer Isaac Osborn. *From Total Domination to Graph Coloring*. Western Michigan University, 2026. Advisor(s): Ping Zhang. [primary source](https://scholarworks.wmich.edu/cgi/viewcontent.cgi?article=5284&context=dissertations) · [record](https://scholarworks.wmich.edu/dissertations/4275/) Location: Problem 4.3.8, printed p.75.

**Further links.** [1](https://www.mdpi.com/2073-8994/17/9/1429) · [2](https://www.math.fau.edu/combinatorics/abstracts/osborn-57.pdf)

**Result (2026-10-09).** A 16-state weighted automaton characterizes exactly the caterpillars admitting a proper total dominating set and computes a minimum witness. At most three selected leaves per spine vertex and four selected neighbors per spine vertex suffice; both bounds are sharp. The minimum-witness algorithm uses O(k) arithmetic operations for a k-vertex spine; input bit costs are separate. No mathematical gap identified at the stated algorithmic characterization scope; external peer review and historical priority are not certified.

[Proof](../../solutions/seven-problems-2026-10-09/combinatorics/Q0256-caterpillars.md) · [Internal review](../../solutions/seven-problems-2026-10-09/reviews/combinatorics-review.md) · [Computational controls](../../solutions/seven-problems-2026-10-09/combinatorics/verification.json). This research proposal has a separate internal AI review; it is not externally peer reviewed.


<a id="q257"></a>

## Q257. Which integer pairs \$2\le a\le b\$ occur as the minimum size \$a\$ of a total domin…

**Status:** Open, partial results · **Kind:** open problem (Problem 4.3.10) · **Collection** 3

Which integer pairs \$2\le a\le b\$ occur as the minimum size \$a\$ of a total dominating set and the minimum size \$b\$ of a proper total dominating set in one tree?

**Context.** Origin: New domination and coloring questions from research with Ping Zhang, retained in the 2026 dissertation. Shared setup for questions 256, 257, 258: A set \$S\$ is total dominating if \$\sigma(v)=|N(v)\cap S|>0\$ for every vertex; it is proper total dominating if adjacent vertices also have different \$\sigma\$-values.

**Source.** Sawyer Isaac Osborn. *From Total Domination to Graph Coloring*. Western Michigan University, 2026. Advisor(s): Ping Zhang. [primary source](https://scholarworks.wmich.edu/cgi/viewcontent.cgi?article=5284&context=dissertations) · [record](https://scholarworks.wmich.edu/dissertations/4275/) Location: Problem 4.3.10, printed p.76.

**Further links.** [1](https://www.mdpi.com/2073-8994/17/9/1429)

**Result (2026-10-09).** Every realizable tree pair (a,b) = (gamma_t,gamma_pt) satisfies a+1 <= b <= 6a-4 and has a representative on at most 6a-4 vertices. The complete a=2 slice is b in {3,5}; the complete a=3 slice is b in {6,7}. A general characterization of the realizable pairs for a >= 4 remains unresolved; no sharpness claim is made for the upper bound.

[Proof](../../solutions/seven-problems-2026-10-09/combinatorics/Q0257-tree-pairs.md) · [Internal review](../../solutions/seven-problems-2026-10-09/reviews/combinatorics-review.md) · [Computational controls](../../solutions/seven-problems-2026-10-09/combinatorics/verification.json). This research proposal has a separate internal AI review; it is not externally peer reviewed.


<a id="q258"></a>

## Q258. Let \$\chi_{pt}(G)\$ minimize the number of distinct \$\sigma\$-values over proper t…

**Status:** Open · **Kind:** open problem (Problem 5.3.2) · **Collection** 3

Let \$\chi_{pt}(G)\$ minimize the number of distinct \$\sigma\$-values over proper total dominating sets. Which positive integers \$a\le b\le c\le d\$ occur for a connected graph \$G\$ as \$(\omega(G),\chi(G),\chi_{pt}(G),\Delta(G))=(a,b,c,d)\$, where \$\omega\$ is clique number, \$\chi\$ chromatic number and \$\Delta\$ maximum degree?

**Context.** Origin: New domination and coloring questions from research with Ping Zhang, retained in the 2026 dissertation. Shared setup for questions 256, 257, 258: A set \$S\$ is total dominating if \$\sigma(v)=|N(v)\cap S|>0\$ for every vertex; it is proper total dominating if adjacent vertices also have different \$\sigma\$-values.

**Source.** Sawyer Isaac Osborn. *From Total Domination to Graph Coloring*. Western Michigan University, 2026. Advisor(s): Ping Zhang. [primary source](https://scholarworks.wmich.edu/cgi/viewcontent.cgi?article=5284&context=dissertations) · [record](https://scholarworks.wmich.edu/dissertations/4275/) Location: Problem 5.3.2, printed p.88.

**Further links.** [1](https://shahindp.com/Contrib_Math/v10/CM24_v10_pp40-47.pdf)


<a id="q259"></a>

## Q259. For k ≥ 2, is the maximum size of an intersecting temperate family on {1,…,2k} e…

**Status:** Open · **Kind:** conjecture (Conjecture 1.2.7) · **Collection** 3

For k ≥ 2, is the maximum size of an intersecting temperate family on {1,…,2k} equal to binom(2k,k)/2 + binom(2k,k+1) + binom(2k−1,k+2)? Temperate means that every member A contains at most |A| other members as proper subsets; intersecting means all pairs of members meet.

**Context.** Origin: Joint Petr–Turek conjectures: temperate families and a reflection-compatible strengthening of the older wreath conjecture.

**Source.** Jan Petr. *Colourings, dominating sets and wreaths*. University of Cambridge, 2025. Advisor(s): Béla Bollobás. [primary source](https://www.repository.cam.ac.uk/bitstreams/6cb328d0-6f50-4e7b-9c7e-25c7f12d4d57/download) · [record](https://www.repository.cam.ac.uk/items/09faf321-7438-442a-9ed1-6487b62ab783) Location: Conjecture 1.2.7, printed p.14; definitions p.13.

**Further links.** [1](https://arxiv.org/abs/2406.18437) · [2](https://doi.org/10.1016/j.jcta.2025.106133) · [3](https://arxiv.org/html/2609.24747v1)


<a id="q260"></a>

## Q260. For every \$k\ge1\$, assign distinct permutations \$\pi_D\$ of \$\mathbb Z/(2k+1)\mat…

**Status:** Open · **Kind:** conjecture (Conjecture 1.5.10) · **Collection** 3

For every \$k\ge1\$, assign distinct permutations \$\pi_D\$ of \$\mathbb Z/(2k+1)\mathbb Z\$ fixing \$0\$ to the Dyck paths \$D\$ of semilength \$k\$. Can their cyclic length-\$k\$ blocks partition all \$k\$-subsets, with \$\pi_D(j)\in\\{1,\ldots,k\\}\$ exactly when step \$j\$ is a rise (\$1\le j\le2k\$), and \$\pi_D(j)+\pi_{R(D)}(-j)=0\$ modulo \$2k+1\$? Here \$R\$ reflects in \$x=k\$; Dyck paths have steps \$(1,\pm1)\$, stay above \$y=0\$, and run from \$(0,0)\$ to \$(2k,0)\$.

**Context.** Origin: Joint Petr–Turek conjectures: temperate families and a reflection-compatible strengthening of the older wreath conjecture.

**Source.** Jan Petr. *Colourings, dominating sets and wreaths*. University of Cambridge, 2025. Advisor(s): Béla Bollobás. [primary source](https://www.repository.cam.ac.uk/bitstreams/6cb328d0-6f50-4e7b-9c7e-25c7f12d4d57/download) · [record](https://www.repository.cam.ac.uk/items/09faf321-7438-442a-9ed1-6487b62ab783) Location: Conjecture 1.5.10, printed p.24; weaker Conjecture 1.5.8, p.23.

**Further links.** [1](https://arxiv.org/html/2501.07277v2) · [2](https://doi.org/10.37236/13812) · [3](https://janpetrscience.github.io/publications/)


<a id="q261"></a>

## Q261. For all sufficiently large m, does every graph with m(m+1)/2 edges admit an edge…

**Status:** Open · **Kind:** open problem (Problem 2.5.2) · **Collection** 3

For all sufficiently large m, does every graph with m(m+1)/2 edges admit an edge partition H₁,…,Hₘ where Hᵢ has i edges, embeds as a subgraph of Hᵢ₊₁ for i&lt;m, and is a vertex-disjoint union of one star and a matching?

**Context.** Metadata note: Repository award year 2026; submitted July 2025. The repository title begins “Topics in”; the PDF title begins “Problems in”. Origin: Ascending decomposition is joint with Letzter, Pokrovskiy and Sudakov; the cycle-threshold conjecture extends the author’s random-Ramsey work.

**Source.** Kyriakos Katsamaktsis. *Problems in extremal and probabilistic combinatorics*. University College London, 2026. Advisor(s): Shoham Letzter (primary); John Talbot (secondary). [primary source](https://discovery.ucl.ac.uk/id/eprint/10220866/1/Kyriakos_Katsamaktsis_FINAL_THESIS.pdf) · [record](https://discovery.ucl.ac.uk/id/eprint/10220866/) Location: Problem 2.5.2, p.60 of 179.

**Further links.** [1](https://people.math.ethz.ch/~sudakovb/ascending-subgraph-decomposition.pdf) · [2](https://doi.org/10.1016/j.jctb.2025.01.003)


<a id="q262"></a>

## Q262. Fix ℓ ≥ 4 and set p₀ = n^(−(ℓ−2)/(ℓ−1−1/ℓ)). Is there C > 0 such that, whenever …

**Status:** Open · **Kind:** conjecture (Conjecture 4.3) · **Collection** 3

Fix ℓ ≥ 4 and set p₀ = n^(−(ℓ−2)/(ℓ−1−1/ℓ)). Is there C > 0 such that, whenever C p₀ ≤ p = o(n^(−1+1/(ℓ−1))), the two-round Cℓ-Ramsey completion threshold is q̂ = n^(−ℓ²+ℓ) p^(−ℓ²+1)? First color G(n,p) red/blue before an independent G(n,q) is revealed, then extend the coloring. Threshold means monochromatic Cℓ can be avoided with high probability for q = o(q̂), but cannot for q/q̂ → ∞.

**Context.** Metadata note: Repository award year 2026; submitted July 2025. The repository title begins “Topics in”; the PDF title begins “Problems in”. Origin: Ascending decomposition is joint with Letzter, Pokrovskiy and Sudakov; the cycle-threshold conjecture extends the author’s random-Ramsey work.

**Source.** Kyriakos Katsamaktsis. *Problems in extremal and probabilistic combinatorics*. University College London, 2026. Advisor(s): Shoham Letzter (primary); John Talbot (secondary). [primary source](https://discovery.ucl.ac.uk/id/eprint/10220866/1/Kyriakos_Katsamaktsis_FINAL_THESIS.pdf) · [record](https://discovery.ucl.ac.uk/id/eprint/10220866/) Location: Upper-regime assertion of Conjecture 4.3, p.95 of 179; game and threshold definitions pp.91–95.

**Further links.** [1](https://kyriakosk.github.io/files/random_ramsey-3.pdf) · [2](https://kyriakosk.github.io/) · [3](https://doi.org/10.1002/rsa.70066)


<a id="q263"></a>

## Q263. Can every finite simple 2-degenerate graph of maximum degree 4 have its edges pa…

**Status:** Open · **Kind:** conjecture (Conjecture 2) · **Collection** 3

Can every finite simple 2-degenerate graph of maximum degree 4 have its edges partitioned into two linear forests? A graph is 2-degenerate if every nonempty subgraph has a vertex of degree at most 2; a linear forest is a disjoint union of paths.

**Context.** Origin: New strengthening for 2-degenerate graphs, jointly formulated with Basavaraju, Bishnu and Francis before thesis submission.

**Source.** Drimit Pattanayak. *Variants of vertex and edge colorings of graphs*. Indian Statistical Institute, 2024. Advisor(s): Mathew C. Francis. [primary source](https://digitalcommons.isical.ac.in/doctoral-theses/474/) · [record](https://digitalcommons.isical.ac.in/doctoral-theses/474/) Location: Official dissertation abstract; full-text pagination unavailable. Companion paper arXiv:2007.06066v3, Section 4, Conjecture 2, p.12.

**Further links.** [1](https://arxiv.org/html/2007.06066v3) · [2](https://doi.org/10.1016/j.disc.2021.112434) · [3](https://arxiv.org/abs/2302.01638)


<a id="q264"></a>

## Q264. Fix a vertex-ordered graph H with an edge. Let τ(H) be the infimum d such that, …

**Status:** Open · **Kind:** conjecture (Conjecture 3.15.1) · **Collection** 3

Fix a vertex-ordered graph H with an edge. Let τ(H) be the infimum d such that, for every ε > 0 and all sufficiently large n, every n-vertex ordered graph of minimum degree at least (d+ε)n has vertex-disjoint order-preserving copies of H covering at least (1−ε)n vertices. Does a constant C(H) ensure coverage of all but C(H) vertices already at minimum degree τ(H)n?

**Context.** Origin: Joint Freschi–Treglown questions from their 2022 ordered-tiling paper, incorporated into the dissertation.

**Source.** Andrea Freschi. *Extremal and probabilistic problems for discrete structures*. University of Birmingham, 2025. Advisor(s): Andrew Treglown; Richard Mycroft. [primary source](https://etheses.bham.ac.uk/id/eprint/15965/1/Freschi2025PhD.pdf) · [record](https://etheses.bham.ac.uk/id/eprint/15965/) Location: Conjecture 3.15.1, printed p.104; threshold equivalence from Theorems 3.1.4 and 3.12.1.

**Further links.** [1](https://doi.org/10.1017/fms.2022.92) · [2](https://web.mat.bham.ac.uk/A.Treglown/pubat.html)


<a id="q265"></a>

## Q265. Fix a vertex-ordered graph H with an edge. For 0 < x < 1, let f_H(x) be the infi…

**Status:** Open · **Kind:** open problem · **Collection** 3

Fix a vertex-ordered graph H with an edge. For 0 < x < 1, let f_H(x) be the infimum d such that, for every η > 0 and all sufficiently large n, minimum degree at least (d+η)n forces an n-vertex ordered graph to have vertex-disjoint order-preserving copies of H covering at least xn vertices. Is f_H piecewise linear?

**Context.** Origin: Joint Freschi–Treglown questions from their 2022 ordered-tiling paper, incorporated into the dissertation.

**Source.** Andrea Freschi. *Extremal and probabilistic problems for discrete structures*. University of Birmingham, 2025. Advisor(s): Andrew Treglown; Richard Mycroft. [primary source](https://etheses.bham.ac.uk/id/eprint/15965/1/Freschi2025PhD.pdf) · [record](https://etheses.bham.ac.uk/id/eprint/15965/) Location: Unnumbered final question of Section 3.15, printed p.104; threshold definition and sharpness, Theorem 3.1.14, pp.38–39.

**Further links.** [1](https://doi.org/10.1017/fms.2022.92) · [2](https://web.mat.bham.ac.uk/A.Treglown/ordereddirac2.pdf)


<a id="q271"></a>

## Q271. Fix \$c>0\$ and an integer \$r\ge3\$. Let \$G\sim G(n,c/n)\$, and join two distinct ve…

**Status:** Open · **Kind:** open problem · **Collection** 3

Fix \$c>0\$ and an integer \$r\ge3\$. Let \$G\sim G(n,c/n)\$, and join two distinct vertices in \$G^r\$ whenever their \$G\$-distance is at most \$r\$. Is \$\chi_\ell(G^r)/\chi(G^r)\to1\$ in probability as \$n\to\infty\$? Here \$\chi_\ell\$ is the least \$k\$ such that every assignment of \$k\$ permitted colors to each vertex admits a proper coloring from those lists.

**Context.** Origin: The author’s conjecture extending his square-graph coloring result to higher powers.

**Source.** Aditya Raut. *Topics in Random Graph Theory*. Carnegie Mellon University, 2025. Advisor(s): Alan Frieze. [primary source](https://ndownloader.figshare.com/files/60518081) · [record](https://doi.org/10.1184/R1/30776093) Location: §4.3 Conclusions, printed p.28; graph model and power definition in §4.1, p.25.

**Further links.** [1](https://arxiv.org/html/2604.14006v1)


<a id="q272"></a>

## Q272. Fix \$k\ge2\$. Choose uniformly an unordered minimal \$k\$-DNF formula on \$n\$ labell…

**Status:** Open · **Kind:** open problem (Question 2.1.19) · **Collection** 3

Fix \$k\ge2\$. Choose uniformly an unordered minimal \$k\$-DNF formula on \$n\$ labelled Boolean variables with exactly \$m=m(n)\$ clauses, each using \$k\$ distinct variables. For which feasible \$m\$-regimes is it unate with probability tending to one? Minimal means deleting any clause changes the function; unate means no variable occurs with both signs.

**Context.** Origin: Minimal-formula and directed-hypergraph questions are joint with Balogh, Lidický, Mani and Zhao; linear-system exceptions with Li and Zhao.

**Source.** Dingding Dong. *Several Problems in Extremal Combinatorics*. Harvard University, 2025. Advisor(s): Yufei Zhao. [primary source](https://dash.harvard.edu/server/api/core/bitstreams/fcc8fc04-74db-48fc-b94e-509f6ed54381/content) · [record](https://dash.harvard.edu/entities/publication/84e1e974-6469-4dbc-be04-b0237c5ac712) Location: Question 2.1.19, printed p.16; definitions pp.4–7.

**Further links.** [1](https://arxiv.org/html/2209.04894v2#S1.SS5) · [2](https://ems.press/content/serial-article-files/46994)


<a id="q273"></a>

## Q273. Fix \$k\ge3\$. In a simple \$k\$-uniform hypergraph, edges are either undirected or …

**Status:** Open · **Kind:** conjecture (Conjecture 2.2.8) · **Collection** 3

Fix \$k\ge3\$. In a simple \$k\$-uniform hypergraph, edges are either undirected or point to one of their vertices. Let \$T\$ have edges \$S\cup\\{a,b\\}\$, \$S\cup\\{a,c\\}\$, \$S\cup\\{b,c\\}\$, where \$|S|=k-2\$, \$a,b,c\$ are distinct outside \$S\$, and only \$S\cup\\{a,c\\}\$ points to \$c\$. Does every \$n\$-vertex \$T\$-free such hypergraph satisfy \$e_u+(1-1/k)^{1-k}e_d\le(1+o(1))\binom nk\$? Here \$e_u,e_d\$ count the two edge types, and containment permits erasing directions.

**Context.** Origin: Minimal-formula and directed-hypergraph questions are joint with Balogh, Lidický, Mani and Zhao; linear-system exceptions with Li and Zhao.

**Source.** Dingding Dong. *Several Problems in Extremal Combinatorics*. Harvard University, 2025. Advisor(s): Yufei Zhao. [primary source](https://dash.harvard.edu/server/api/core/bitstreams/fcc8fc04-74db-48fc-b94e-509f6ed54381/content) · [record](https://dash.harvard.edu/entities/publication/84e1e974-6469-4dbc-be04-b0237c5ac712) Location: Conjecture 2.2.8 and Problem 2.2.7, printed p.24; Definitions 2.1.9–14, pp.12–14.

**Further links.** [1](https://arxiv.org/html/2209.04894v2#S2) · [2](https://arxiv.org/abs/2107.09233)


<a id="q274"></a>

## Q274. For \$a\in\\{1,2\\}\$, is the matrix with rows \$(1,1,-1,-1,0)\$ and \$(a,-a,3,0,-3)\$ c…

**Status:** Open · **Kind:** open problem (Question 4.1.11) · **Collection** 3

For \$a\in\\{1,2\\}\$, is the matrix with rows \$(1,1,-1,-1,0)\$ and \$(a,-a,3,0,-3)\$ common over \$\mathbb F_p\$ for all sufficiently large primes \$p\$? Common means that, for every \$n\$ and \$f:\mathbb F_p^n\to[0,1]\$, \$t_L(f)+t_L(1-f)\ge1/16\$, where \$t_L(f)\$ averages \$\prod_{i=1}^5f(x_i)\$ over all solutions \$Lx=0\$, \$x_i\in\mathbb F_p^n\$.

**Context.** Origin: Minimal-formula and directed-hypergraph questions are joint with Balogh, Lidický, Mani and Zhao; linear-system exceptions with Li and Zhao.

**Source.** Dingding Dong. *Several Problems in Extremal Combinatorics*. Harvard University, 2025. Advisor(s): Yufei Zhao. [primary source](https://dash.harvard.edu/server/api/core/bitstreams/fcc8fc04-74db-48fc-b94e-509f6ed54381/content) · [record](https://dash.harvard.edu/entities/publication/84e1e974-6469-4dbc-be04-b0237c5ac712) Location: Question 4.1.11, printed p.112; exceptional matrices in Theorem 4.1.10, p.111; Definition 4.1.3, p.108.

**Further links.** [1](https://arxiv.org/html/2404.17005v2#S1) · [2](https://math.duke.edu/events/uncommon-linear-systems-two-equations) · [3](https://aqlithium.github.io/anqili/)


<a id="q317"></a>

## Q317. For every integer \$k\ge3\$, does every finite simple \$n\$-vertex bipartite graph \$…

**Status:** Open · **Kind:** conjecture (Conjecture 1.3) · **Collection** 4

For every integer \$k\ge3\$, does every finite simple \$n\$-vertex bipartite graph \$G=(X,Y)\$ of girth at least \$4k\$ admit \$k\$ pairwise edge-disjoint copies in some complete bipartite graph on \$n+k-1\$ vertices, with each copy mapping \$X\$ into the same host side and \$Y\$ into the other? Forests have infinite girth; the host’s two part sizes may be chosen.

**Context.** Discovery: Independent dissertation lead already under review before the advisor-lineage search; no genealogy-derived route is claimed. Origin: The dissertation abstract explicitly proposes the generalized k-packing conjecture jointly with Hong Wang. Their 2026 paper distinguishes it from Wang’s earlier tree-packing and two-copy conjectures.

**Source.** Jiayu Yang. *On embedding, packing and special structures in graphs*. University of Idaho, 2026. Advisor(s): Hong Wang. [primary source](https://verso.uidaho.edu/esploro/outputs/doctoral/On-embedding-packing-and-special-structures/996942733901851) · [record](https://verso.uidaho.edu/esploro/outputs/doctoral/On-embedding-packing-and-special-structures/996942733901851) Location: Official dissertation abstract; full-text pagination unavailable (embargoed until May 26, 2028). Joint paper Conjecture 1.3, journal p. 317.

**Further links.** [1](https://ajc.maths.uq.edu.au/pdf/94/ajc_v94_p316.pdf)


<a id="q318"></a>

## Q318. For \$n\ge5\$, let \$QH^\*(Fl_n;\mathbb Z)\$ be the small quantum cohomology ring of …

**Status:** Open · **Kind:** conjecture (Conjecture 2.5.8) · **Collection** 4

For \$n\ge5\$, let \$QH^\*(Fl_n;\mathbb Z)\$ be the small quantum cohomology ring of complete flags in \$\mathbb C^n\$, over \$\mathbb Z[q_1,\ldots,q_{n-1}]\$. Suppose \$\\{b_w:w\in S_n\\}\$ is a homogeneous basis of degrees \$\ell(w)\$, with \$\deg(q_i)=2\$, reducing at \$q=0\$ to the classical Schubert basis. If all multiplication constants in this basis are polynomials in \$q\$ with nonnegative integer coefficients, must \$b_w=\sigma_w\$ for every \$w\$?

**Context.** Discovery path (advisor ascent; student → supervisor):
Samuel Hopkins → Alexander Postnikov: https://dspace.mit.edu/server/api/core/bitstreams/8aa6c8bb-6452-4944-9edc-d3e954ca0e83/content#page=1
Alexander Postnikov → Richard P. Stanley: https://math.mit.edu/~apost/vita.html Origin: The thesis explicitly proposes the three-axiom strengthening and cites the author’s joint Fomin–Gelfand–Postnikov 1997 paper, Conjecture 9.3. It is the student’s own joint conjecture, not a later borrowed problem.

**Source.** Alexander Postnikov. *Enumeration in Algebra and Geometry*. Massachusetts Institute of Technology, 1997. Advisor(s): Richard P. Stanley. [primary source](https://math.mit.edu/~apost/papers/thesis.pdf) · [record](https://math.mit.edu/~apost/vita.html) Location: Conjecture 2.5.8, p. 76; Theorem 2.5.7, pp. 74–75.

**Further links.** [1](https://dspace.mit.edu/server/api/core/bitstreams/8aa6c8bb-6452-4944-9edc-d3e954ca0e83/content#page=1) · [2](https://www.researchwithrutgers.org/en/publications/positivity-determines-the-quantum-cohomology-of-grassmannians-2/) · [3](https://doi.org/10.2140/ant.2021.15.1505) · [4](https://arxiv.org/abs/2307.02418) · [5](https://math.mit.edu/~apost/papers/qschub_journal.pdf)

*Also among the automatically extracted thesis statements: `72bba1a84dc6bad78290`.*


<a id="q319"></a>

## Q319. Let \$P\$ be a finite poset and \$\omega:P\to\\{1,\ldots,|P|\\}\$ a bijection. Sum the…

**Status:** Open · **Kind:** open problem · **Collection** 4

Let \$P\$ be a finite poset and \$\omega:P\to\\{1,\ldots,|P|\\}\$ a bijection. Sum the monomials \$\prod_{u\in P}x_{f(u)}\$ over order-preserving maps \$f:P\to\mathbb Z_{>0}\$, requiring \$f(u)&lt;f(v)\$ whenever \$u&lt;v\$ and \$\omega(u)>\omega(v)\$. If this generating function is symmetric, must \$P\$ be isomorphic, preserving strict versus weak cover relations, to a skew Young diagram ordered by right/down steps, with weak horizontal and strict vertical covers?

**Context.** Metadata note: The inspected source is the 1972 published revision; the original 1971 manuscript was not retrieved. Primary scholarly testimony explicitly traces this conjecture to the thesis. Discovery path (advisor ascent; student → supervisor):
Samuel Hopkins → Alexander Postnikov: https://dspace.mit.edu/server/api/core/bitstreams/8aa6c8bb-6452-4944-9edc-d3e954ca0e83/content#page=1
Alexander Postnikov → Richard P. Stanley: https://math.mit.edu/~apost/vita.html
Richard P. Stanley → Gian-Carlo Rota: https://math.mit.edu/~rstan/pubs/pubfiles/9.pdf#page=1 Origin: The 1972 revision states the conjecture as the author’s own. MIT’s 2002 McNamara seminar abstract explicitly identifies this exact symmetry/skew-shape conjecture as originating in Stanley’s PhD thesis; Billey–McNamara 2015 describes the memoir as a subset of the thesis. Origin source: https://math.mit.edu/spams/2002fa.html
Origin source: https://sites.math.washington.edu/~billey/papers/fabric.pdf

**Source.** Richard P. Stanley. *Ordered Structures and Partitions*. Harvard University, 1971. Advisor(s): Gian-Carlo Rota. [primary source](https://math.mit.edu/~rstan/pubs/pubfiles/9.pdf) · [record](https://abel.math.harvard.edu/dissertations/index.html) Location: Unnumbered Conjecture after Proposition 21.1, printed p. 81 (PDF p. 85) in the 1972 published dissertation revision; 1971 thesis pagination unavailable.

**Further links.** [1](https://people.reed.edu/~davidp/372/resources/stanley.pdf) · [2](https://dspace.mit.edu/server/api/core/bitstreams/8aa6c8bb-6452-4944-9edc-d3e954ca0e83/content#page=1) · [3](https://math.mit.edu/~apost/vita.html) · [4](https://math.mit.edu/~rstan/pubs/pubfiles/9.pdf#page=1) · [5](https://math.mit.edu/spams/2002fa.html) · [6](https://sites.math.washington.edu/~billey/papers/fabric.pdf) · [7](https://doi.org/10.1017/fms.2024.116) · [8](https://www.mat.univie.ac.at/~slc/wpapers/FPSAC2024/27.pdf)


<a id="q320"></a>

## Q320. Fix \$\ell\ge2\$ and a size rule \$R\$. Starting with the empty graph on \$n\$ vertice…

**Status:** Open · **Kind:** conjecture (Conjecture 5.1.2) · **Collection** 4

Fix \$\ell\ge2\$ and a size rule \$R\$. Starting with the empty graph on \$n\$ vertices, each step samples \$\ell\$ vertices independently and uniformly; \$R\$ adds a nonempty set of pairs among them, determined solely by their component sizes, independent of \$n\$ and time. Write \$S(G)=n^{-1}\sum_C|C|^2\$ and \$L_1(G)=\max_C|C|\$. Let \$t_b\$ be the supremum of times \$t\$ for which \$S(G_{\lfloor tn\rfloor})\$ is bounded in probability, and \$t_c\$ the supremum for which \$L_1(G_{\lfloor tn\rfloor})/n\to0\$ in probability. Must \$t_b=t_c\$? More precisely, does every \$t>t_b\$ and \$\varepsilon>0\$ admit \$\delta>0\$ such that \$\Pr(L_1(G_{\lfloor tn\rfloor})\ge\delta n)\ge1-\varepsilon\$ for all sufficiently large \$n\$?

**Context.** Discovery path (advisor ascent; student → supervisor):
Erlang Surya → Lutz Warnke: https://mathweb.ucsd.edu/~lwarnke/PhD_Thesis_ErlangSurya.pdf
Lutz Warnke → Oliver Riordan: https://mathweb.ucsd.edu/~lwarnke/ Origin: The thesis proposes the unrestricted size-rule assertion and distinguishes earlier bounded-size cases. It is the author’s joint conjecture with Oliver Riordan, also formulated as Conjecture 2 in their April 2012 preprint The evolution of subcritical Achlioptas processes (later Random Structures & Algorithms 47 (2015), 174–203). Origin source: https://arxiv.org/abs/1204.5068
Origin source: https://www.math.cmu.edu/users/af1p/Teaching/ATIRS/Papers/ACH/subcritical.pdf

**Source.** Lutz Peter Warnke. *Random Graph Processes with Dependencies*. University of Oxford, 2012. Advisor(s): Oliver Riordan. [primary source](https://ora.ox.ac.uk/objects/uuid:71b48e5f-a192-4684-a864-ea9059a25d74/files/m108d6ed9ccb9ef25fe381ff65be80b29) · [record](https://ora.ox.ac.uk/objects/uuid:71b48e5f-a192-4684-a864-ea9059a25d74) Location: Conjecture 5.1.2, printed p. 70; size-rule definition §5.2, p. 71.

**Further links.** [1](https://mathweb.ucsd.edu/~lwarnke/) · [2](https://mathweb.ucsd.edu/~lwarnke/PhD_Thesis_ErlangSurya.pdf) · [3](https://arxiv.org/abs/1204.5068) · [4](https://www.math.cmu.edu/users/af1p/Teaching/ATIRS/Papers/ACH/subcritical.pdf) · [5](https://arxiv.org/abs/1704.08714) · [6](https://arxiv.org/html/2605.09466v1)


<a id="q321"></a>

## Q321. For \$n\ge3\$ and \$1\le r\le\lfloor n/2\rfloor\$, let \$P=\operatorname{conv}\\{e_i+e…

**Status:** Open · **Kind:** conjecture (Conjecture 3.4.5) · **Collection** 4

For \$n\ge3\$ and \$1\le r\le\lfloor n/2\rfloor\$, let \$P=\operatorname{conv}\\{e_i+e_j: i\ne j,\ \min(|i-j|,n-|i-j|)\ge r\\}\$. Define \$h^\*(P;t)\$ by \$\sum_{m\ge0}|mP\cap\mathbb Z^n|t^m=h^\*(P;t)/(1-t)^{\dim P+1}\$. Must its coefficient sequence be unimodal, meaning nondecreasing up to some index and nonincreasing afterward?

**Context.** Discovery path (advisor ascent; student → supervisor):
Danai Deligeorgaki → Liam Solus: https://diva-portal.org/smash/get/diva2%3A1961783/FULLTEXT01.pdf
Liam Solus → Benjamin Braun and Carl W. Lee: https://uknowledge.uky.edu/cgi/viewcontent.cgi?article=1030&context=math_etds Origin: Doctoral joint work: the stable-hypersimplex conjecture with Benjamin Braun (2014 preprint), and the cut-facet question with Caroline Uhler and Ruriko Yoshida (2015 preprint). Both preceded filing. Origin source: https://arxiv.org/abs/1408.4713
Origin source: https://arxiv.org/abs/1506.06702
Origin source: https://calhoun.nps.edu/server/api/core/bitstreams/048beccf-3fea-40fc-8b04-7f28de01f255/content

**Source.** Liam Solus. *Polyhedral Problems in Combinatorial Convex Geometry*. University of Kentucky, 2015. Advisor(s): Benjamin Braun; Carl W. Lee. [primary source](https://uknowledge.uky.edu/cgi/viewcontent.cgi?article=1030&context=math_etds) · [record](https://uknowledge.uky.edu/math_etds/32/) Location: Conjecture 3.4.5, printed p. 73; stable hypersimplex definition in Chapter 2.

**Further links.** [1](https://diva-portal.org/smash/get/diva2%3A1961783/FULLTEXT01.pdf) · [2](https://arxiv.org/abs/1408.4713) · [3](https://arxiv.org/abs/1506.06702) · [4](https://calhoun.nps.edu/server/api/core/bitstreams/048beccf-3fea-40fc-8b04-7f28de01f255/content) · [5](https://www.sciencedirect.com/science/article/pii/S0097316518300293) · [6](https://arxiv.org/abs/1408.5932) · [7](https://www.kth.se/profile/solus?l=en)


<a id="q322"></a>

## Q322. For a finite simple graph \$G\$ on \$p\$ vertices, let \$S_+(G)=\\{M\in\mathbb R^{p\ti…

**Status:** Open · **Kind:** open problem (Problem 5.5.5) · **Collection** 4

For a finite simple graph \$G\$ on \$p\$ vertices, let \$S_+(G)=\\{M\in\mathbb R^{p\times p}:M=M^\top,\ M\succeq0,\ M_{ij}=0\text{ for }i\ne j,\ ij\notin E(G)\\}\$. Its cut polytope is the convex hull of edge-vectors with coordinate \$-1\$ on a cut and \$+1\$ elsewhere. A facet normal \$\alpha\$ identifies an extreme ray when some nonzero matrix on an extreme ray of \$S_+(G)\$ has edge entries \$\alpha\$ or \$-\alpha\$. Characterize the graphs for which every facet normal identifies an extreme ray and the ranks of all extreme rays occur among matrices identified in this way.

**Context.** Discovery path (advisor ascent; student → supervisor):
Danai Deligeorgaki → Liam Solus: https://diva-portal.org/smash/get/diva2%3A1961783/FULLTEXT01.pdf
Liam Solus → Benjamin Braun and Carl W. Lee: https://uknowledge.uky.edu/cgi/viewcontent.cgi?article=1030&context=math_etds Origin: Doctoral joint work: the stable-hypersimplex conjecture with Benjamin Braun (2014 preprint), and the cut-facet question with Caroline Uhler and Ruriko Yoshida (2015 preprint). Both preceded filing. Origin source: https://arxiv.org/abs/1408.4713
Origin source: https://arxiv.org/abs/1506.06702
Origin source: https://calhoun.nps.edu/server/api/core/bitstreams/048beccf-3fea-40fc-8b04-7f28de01f255/content

**Source.** Liam Solus. *Polyhedral Problems in Combinatorial Convex Geometry*. University of Kentucky, 2015. Advisor(s): Benjamin Braun; Carl W. Lee. [primary source](https://uknowledge.uky.edu/cgi/viewcontent.cgi?article=1030&context=math_etds) · [record](https://uknowledge.uky.edu/math_etds/32/) Location: Problem 5.5.5, printed p. 103; Definition 5.1.2, p. 82.

**Further links.** [1](https://diva-portal.org/smash/get/diva2%3A1961783/FULLTEXT01.pdf) · [2](https://arxiv.org/abs/1408.4713) · [3](https://arxiv.org/abs/1506.06702) · [4](https://calhoun.nps.edu/server/api/core/bitstreams/048beccf-3fea-40fc-8b04-7f28de01f255/content) · [5](https://www.kth.se/profile/solus?l=en)


<a id="q323"></a>

## Q323. Let \$P\$ be a finite poset and \$A\subseteq P\$ an induced subposet containing \$\mi…

**Status:** Open · **Kind:** open problem (Question 1) · **Collection** 4

Let \$P\$ be a finite poset and \$A\subseteq P\$ an induced subposet containing \$\min(P)\cup\max(P)\$. For an integer-valued order-preserving marking \$\lambda:A\to\mathbb Z\$, let \$\Omega_{P,A}(\lambda)\$ count its integer-valued order-preserving extensions to \$P\$. This is piecewise polynomial on the cone \$\mathcal L(A)\$ of real order-preserving markings. Determine its coarsest subdivision into polynomiality regions. In particular, give a combinatorial criterion for adjacent chambers obtained by totally ordering the marked values to carry the same polynomial.

**Context.** Discovery path (advisor ascent; student → supervisor):
Aryaman Jal → Katharina Jochemko: https://www.diva-portal.org/smash/get/diva2%3A1958137/FULLTEXT01.pdf
Katharina Jochemko → Raman Sanyal: https://people.kth.se/~jochemko/CVJochemko.pdf Origin: Joint questions with Raman Sanyal, in their 2012 preprint, 2014 SIAM journal paper, and dissertation Chapter 4.

**Source.** Katharina Victoria Jochemko. *On the Combinatorics of Valuations. Freie Universität Berlin, 2014 defense; 2015 publication.*. 2015. Advisor(s): Raman Sanyal. [primary source](https://refubium.fu-berlin.de/bitstream/handle/fub188/11166/Thesis_Jochemko.pdf?isAllowed=y&sequence=1) · [record](https://refubium.fu-berlin.de/handle/fub188/11166?locale-attribute=en&show=full) Location: Chapter 4, §4.2, Question 1, printed p. 70 and continuation p. 71; joint paper Question 1, pp. 5–6 of arXiv version.

**Further links.** [1](https://people.kth.se/~jochemko/CVJochemko.pdf) · [2](https://www.diva-portal.org/smash/get/diva2%3A1958137/FULLTEXT01.pdf) · [3](https://arxiv.org/abs/1206.4066) · [4](https://arxiv.org/html/2604.08394v2)


<a id="q324"></a>

## Q324. Let \$P\$ be a finite poset and \$A\subseteq P\$ contain \$\min(P)\cup\max(P)\$. Count…

**Status:** Open · **Kind:** open problem (Question 2) · **Collection** 4

Let \$P\$ be a finite poset and \$A\subseteq P\$ contain \$\min(P)\cup\max(P)\$. Count integer-valued order-preserving extensions of \$\lambda:A\to\mathbb Z\$ by \$\Omega_{P,A}(\lambda)\$. On a chamber fixing a total order \$\lambda(a_0)\le\cdots\le\lambda(a_k)\$ compatible with the order on \$A\$, this count agrees with a multivariate polynomial. Find a combinatorial formula for its degree in each original coordinate \$\lambda(a_i)\$, in terms of \$P,A\$, and the chamber order. Degrees in the successive differences \$\lambda(a_i)-\lambda(a_{i-1})\$ are known; the question concerns the original marking coordinates.

**Context.** Discovery path (advisor ascent; student → supervisor):
Aryaman Jal → Katharina Jochemko: https://www.diva-portal.org/smash/get/diva2%3A1958137/FULLTEXT01.pdf
Katharina Jochemko → Raman Sanyal: https://people.kth.se/~jochemko/CVJochemko.pdf Origin: Joint questions with Raman Sanyal, in their 2012 preprint, 2014 SIAM journal paper, and dissertation Chapter 4.

**Source.** Katharina Victoria Jochemko. *On the Combinatorics of Valuations. Freie Universität Berlin, 2014 defense; 2015 publication.*. 2015. Advisor(s): Raman Sanyal. [primary source](https://refubium.fu-berlin.de/bitstream/handle/fub188/11166/Thesis_Jochemko.pdf?isAllowed=y&sequence=1) · [record](https://refubium.fu-berlin.de/handle/fub188/11166?locale-attribute=en&show=full) Location: Chapter 4, §4.2.4, Question 2, printed p. 73; joint paper Question 2, p. 7 of arXiv version.

**Further links.** [1](https://people.kth.se/~jochemko/CVJochemko.pdf) · [2](https://www.diva-portal.org/smash/get/diva2%3A1958137/FULLTEXT01.pdf) · [3](https://arxiv.org/abs/1206.4066) · [4](https://arxiv.org/html/2604.08394v2)


<a id="q325"></a>

## Q325. For an integer \$d\ge1\$, let \$\mathcal S_d\$ consist of the nonzero polynomials \$f…

**Status:** Solved here: proved · **Kind:** conjecture (Conjecture 3.11) · **Collection** 4

For an integer \$d\ge1\$, let \$\mathcal S_d\$ consist of the nonzero polynomials \$f(z)=\sum_{j=0}^d a_j\binom{z+d-j}{d}\$ with real \$a_j\ge0\$. Put \$M_d(z)=\binom{z+d}{d}+\binom{z}{d}\$ and \$B_d=\max\\{|\operatorname{Im}\zeta|:M_d(\zeta)=0\\}\$. Is \$|\operatorname{Im}\zeta|\le B_d\$ for every zero \$\zeta\$ of every \$f\in\mathcal S_d\$? Here \$\binom zd=z(z-1)\cdots(z-d+1)/d!\$.

**Context.** Discovery path (advisor ascent; student → supervisor):
Danai Deligeorgaki → Liam Solus: https://diva-portal.org/smash/get/diva2%3A1961783/FULLTEXT01.pdf
Liam Solus → Benjamin Braun: https://uknowledge.uky.edu/cgi/viewcontent.cgi?article=1030&context=math_etds#page=4
Benjamin Braun → John Shareshian: https://sites.google.com/view/braunmath/short-cv Origin: The dissertation attributes Conjecture 3.11 to Braun and Mike Develin, adapting their own joint preprint. Its earlier formulation is Conjecture 2.4, p. 4, of their October 2006 paper, published in Contemporary Mathematics 452 (2008), pp. 67–78. Thus this is an author-coformulated question already circulating before filing, rather than sole thesis-first authorship. The thesis acknowledgments and the author CV identify Shareshian as advisor; the official department PhD list confirms the 2007 degree.

**Source.** Benjamin James Braun. *Ehrhart Theory for Lattice Polytopes. Washington University in St*. Louis, 2007. Advisor(s): John Shareshian. [primary source](https://drive.google.com/file/d/1m8y5Gra3v5g7P9_EnOFpiY0o8Yvw1e_P/view) · [record](https://sites.google.com/view/braunmath/short-cv) Location: Conjecture 3.11, printed p. 35; Definition 3.5, p. 29; Theorem 3.10, pp. 32–33. Actual 62-page author-posted dissertation read.

**Results.**

- **Proved**: All roots of every degree-d Stanley-nonnegative polynomial satisfy |Im z|<=B_d. For d>=2 equality forces real part -1/2 and a positive scalar multiple of M_d. Also a complete description of the attainable nonreal root locus by an explicit phase-span inequality. Remaining: No canonical-line hypothesis. Publication priority is unclaimed. Recorded from the external B3 return  (backfilled 2026-10-08); initial argument review and bounded independent controls in the intake; not independently re-derived here. [Details](../../solutions/b3-2026-10-06/README.md).

**Further links.** [1](https://sites.google.com/view/braunmath/mathematical-work) · [2](https://math.washu.edu/phd-recipients) · [3](https://blogs.ams.org/matheducation/2018/01/08/advice-for-new-doctoral-advisors/) · [4](https://diva-portal.org/smash/get/diva2%3A1961783/FULLTEXT01.pdf) · [5](https://uknowledge.uky.edu/cgi/viewcontent.cgi?article=1030&context=math_etds#page=4) · [6](https://math.colgate.edu/~integers/z68/z68.pdf) · [7](https://arxiv.org/abs/2207.08011) · [8](https://arxiv.org/abs/math/0610399)


<a id="q328"></a>

## Q328. For fixed \$k\ge4\$ and \$k\mid n\$, determine the least integer \$d\$ such that every…

**Status:** Open · **Kind:** open problem (Question 1) · **Collection** 4

For fixed \$k\ge4\$ and \$k\mid n\$, determine the least integer \$d\$ such that every \$n\$-vertex oriented graph \$G\$ with \$\delta^0(G)\ge d\$ has a perfect \$T_k\$-packing. Here \$\delta^0(G)=\min_{v\in V(G)}\min\\{d^+(v),d^-(v)\\}\$, \$T_k\$ is the acyclic tournament on \$k\$ vertices, and a perfect packing partitions \$V(G)\$ into copies of \$T_k\$. Oriented graphs are loopless and have no opposite pair of arcs.

**Context.** Discovery path (advisor ascent; student → supervisor):
Andrea Freschi → Andrew Treglown: https://etheses.bham.ac.uk/id/eprint/15965/1/Freschi2025PhD.pdf
Andrew Clark Treglown → Daniela Kühn and Deryk Osthus: https://etheses.bham.ac.uk/id/eprint/1345/1/Treglown11PhD.pdf#page=4 Origin: Two distinct questions from Treglown’s own 2010 preprint, later published in 2012: perfect transitive-tournament packings and forcing a single copy.

**Source.** Andrew Clark Treglown. *Embedding problems in graphs and hypergraphs*. University of Birmingham, 2011. Advisor(s): Daniela Kühn; Deryk Osthus. [primary source](https://etheses.bham.ac.uk/id/eprint/1345/1/Treglown11PhD.pdf) · [record](https://etheses.bham.ac.uk/id/eprint/1345/) Location: Section 6.3, Question 1, printed p. 90. Title page: submitted September 2010; repository dates doctorate 2011.

**Further links.** [1](https://etheses.bham.ac.uk/id/eprint/15965/1/Freschi2025PhD.pdf) · [2](https://etheses.bham.ac.uk/id/eprint/1345/1/Treglown11PhD.pdf#page=4) · [3](https://web.mat.bham.ac.uk/A.Treglown/orientednote.pdf) · [4](https://web.mat.bham.ac.uk/A.Treglown/transitive_SIAM.pdf) · [5](https://pure-oai.bham.ac.uk/ws/portalfiles/portal/38084629/1401.0460v2.pdf) · [6](https://arxiv.org/abs/2608.10445)


<a id="q329"></a>

## Q329. For fixed \$k\ge4\$ and \$n\ge k\$, determine \$\max\\{\delta^0(G): |V(G)|=n,\ G\text{…

**Status:** Open · **Kind:** open problem (Question 2) · **Collection** 4

For fixed \$k\ge4\$ and \$n\ge k\$, determine \$\max\\{\delta^0(G): |V(G)|=n,\ G\text{ is oriented and }T_k\not\subseteq G\\}\$. Here \$T_k\$ is the transitive tournament, and \$\delta^0(G)=\min_v\min\\{d^+(v),d^-(v)\\}\$. Equivalently, find the sharp minimum-semidegree threshold forcing one \$T_k\$.

**Context.** Discovery path (advisor ascent; student → supervisor):
Andrea Freschi → Andrew Treglown: https://etheses.bham.ac.uk/id/eprint/15965/1/Freschi2025PhD.pdf
Andrew Clark Treglown → Daniela Kühn and Deryk Osthus: https://etheses.bham.ac.uk/id/eprint/1345/1/Treglown11PhD.pdf#page=4 Origin: Two distinct questions from Treglown’s own 2010 preprint, later published in 2012: perfect transitive-tournament packings and forcing a single copy.

**Source.** Andrew Clark Treglown. *Embedding problems in graphs and hypergraphs*. University of Birmingham, 2011. Advisor(s): Daniela Kühn; Deryk Osthus. [primary source](https://etheses.bham.ac.uk/id/eprint/1345/1/Treglown11PhD.pdf) · [record](https://etheses.bham.ac.uk/id/eprint/1345/) Location: Section 6.3, Question 2, printed p. 90; the immediately following paragraph settles k=3.

**Further links.** [1](https://etheses.bham.ac.uk/id/eprint/15965/1/Freschi2025PhD.pdf) · [2](https://etheses.bham.ac.uk/id/eprint/1345/1/Treglown11PhD.pdf#page=4) · [3](https://web.mat.bham.ac.uk/A.Treglown/orientednote.pdf) · [4](https://web.mat.bham.ac.uk/A.Treglown/transitive_SIAM.pdf) · [5](https://web.mat.bham.ac.uk/A.Treglown/pubat.html)


<a id="q330"></a>

## Q330. Does every locally finite \$4\$-connected planar graph \$G\$ have a Hamilton circle,…

**Status:** Open · **Kind:** conjecture (Conjecture 6.2) · **Collection** 4

Does every locally finite \$4\$-connected planar graph \$G\$ have a Hamilton circle, meaning a subspace of its Freudenthal compactification \$|G|\$ homeomorphic to \$S^1\$ that contains every vertex (and hence every end) of \$G\$? Ends are equivalence classes of rays not separable by finite vertex sets; their number is unrestricted.

**Context.** Discovery path (lateral/sibling branch; student → supervisor):
Andrea Freschi → Andrew Treglown: https://etheses.bham.ac.uk/id/eprint/15965/1/Freschi2025PhD.pdf
Andrew Clark Treglown → Daniela Kühn: https://etheses.bham.ac.uk/id/eprint/1345/1/Treglown11PhD.pdf#page=4
Daniela Kühn → Reinhard Diestel: https://www.math.uni-hamburg.de/spag/dm/papers/Kuehn.diss.pdf#page=9
Henning Bruhn → Reinhard Diestel: https://ediss.sub.uni-hamburg.de/handle/ediss/1011 Origin: The Hamilton-circle conjecture is Bruhn’s, already reported as his personal communication in 2005. The weak-evenness question is joint with Maya Stein, later published in 2007.

**Source.** Henning Bruhn. *Infinite circuits in locally finite graphs*. Universität Hamburg, 2005. Advisor(s): Reinhard Diestel. [primary source](https://www.uni-ulm.de/fileadmin/website_uni_ulm/mawi.inst.081/Henning/Dissertation.pdf) · [record](https://ediss.sub.uni-hamburg.de/handle/ediss/1011) Location: Conjecture 6.2, printed p. 74; explicit first-person formulation immediately before it on p. 73.

**Further links.** [1](https://etheses.bham.ac.uk/id/eprint/15965/1/Freschi2025PhD.pdf) · [2](https://etheses.bham.ac.uk/id/eprint/1345/1/Treglown11PhD.pdf#page=4) · [3](https://www.math.uni-hamburg.de/spag/dm/papers/Kuehn.diss.pdf#page=9) · [4](https://yu.math.gatech.edu/Papers/infHamilton.pdf) · [5](https://yu.math.gatech.edu/Papers/circle20.pdf) · [6](https://www.math.uni-hamburg.de/home/diestel/papers/TopSurvey.pdf) · [7](https://agelos.neocities.org/asymptCHT.pdf)


<a id="q331"></a>

## Q331. Let \$G\$ be locally finite with every vertex of even degree. For an end \$\omega\$ …

**Status:** Open · **Kind:** open problem (Problem 5.21) · **Collection** 4

Let \$G\$ be locally finite with every vertex of even degree. For an end \$\omega\$ and finite \$S\subseteq V(G)\$, let \$\lambda_\omega(S)\$ be the maximum number of pairwise edge-disjoint \$\omega\$-rays starting in \$S\$. Suppose every end is weakly even: \$\forall S\text{ finite}\ \exists S'\supseteq S\text{ finite}\$ with \$\lambda_\omega(S')\$ even. Must \$E(G)\in\mathcal C(G)\$? Here \$\mathcal C(G)\$ comprises thin symmetric differences of edge sets of circles in the Freudenthal compactification, with each edge in only finitely many summands.

**Context.** Discovery path (lateral/sibling branch; student → supervisor):
Andrea Freschi → Andrew Treglown: https://etheses.bham.ac.uk/id/eprint/15965/1/Freschi2025PhD.pdf
Andrew Clark Treglown → Daniela Kühn: https://etheses.bham.ac.uk/id/eprint/1345/1/Treglown11PhD.pdf#page=4
Daniela Kühn → Reinhard Diestel: https://www.math.uni-hamburg.de/spag/dm/papers/Kuehn.diss.pdf#page=9
Henning Bruhn → Reinhard Diestel: https://ediss.sub.uni-hamburg.de/handle/ediss/1011 Origin: The Hamilton-circle conjecture is Bruhn’s, already reported as his personal communication in 2005. The weak-evenness question is joint with Maya Stein, later published in 2007.

**Source.** Henning Bruhn. *Infinite circuits in locally finite graphs*. Universität Hamburg, 2005. Advisor(s): Reinhard Diestel. [primary source](https://www.uni-ulm.de/fileadmin/website_uni_ulm/mawi.inst.081/Henning/Dissertation.pdf) · [record](https://ediss.sub.uni-hamburg.de/handle/ediss/1011) Location: Problem 5.21, printed p. 71; Definition 5.20 on p. 70; Theorem 5.4 on p. 52; ray/arc equivalence Proposition 5.6 on p. 55.

**Further links.** [1](https://etheses.bham.ac.uk/id/eprint/15965/1/Freschi2025PhD.pdf) · [2](https://etheses.bham.ac.uk/id/eprint/1345/1/Treglown11PhD.pdf#page=4) · [3](https://www.math.uni-hamburg.de/spag/dm/papers/Kuehn.diss.pdf#page=9) · [4](https://www.uni-ulm.de/fileadmin/website_uni_ulm/mawi.inst.081/Henning/degree.pdf) · [5](https://www.uni-ulm.de/fileadmin/website_uni_ulm/mawi.inst.081/Henning/newdeg.pdf) · [6](https://onlinelibrary.wiley.com/doi/full/10.1002/jgt.22558) · [7](https://arxiv.org/abs/1609.00933)


<a id="q332"></a>

## Q332. Does every weakly connected digraph \$D\$ admit a family \$\mathcal B\$ of pairwise …

**Status:** Open · **Kind:** conjecture (Conjecture F) · **Collection** 4

Does every weakly connected digraph \$D\$ admit a family \$\mathcal B\$ of pairwise edge-disjoint nonempty finite directed cuts and \$F\subseteq\bigcup\mathcal B\$ such that \$|F\cap B|=1\$ for each \$B\in\mathcal B\$, while \$F\$ intersects every nonempty finite directed cut of \$D\$? A directed cut consists of all edges across a nontrivial vertex bipartition, all oriented toward one side. No countability or local-finiteness assumption is made.

**Context.** Discovery path (lateral/sibling branch; student → supervisor):
Andrea Freschi → Andrew Treglown: https://etheses.bham.ac.uk/id/eprint/15965/1/Freschi2025PhD.pdf
Andrew Clark Treglown → Daniela Kühn: https://etheses.bham.ac.uk/id/eprint/1345/1/Treglown11PhD.pdf#page=4
Daniela Kühn → Reinhard Diestel: https://www.math.uni-hamburg.de/spag/dm/papers/Kuehn.diss.pdf#page=9
Karl Heuer → Reinhard Diestel: https://ediss.sub.uni-hamburg.de/handle/ediss/7858 Origin: The thesis’s contribution declaration explicitly states that Heuer formulated F.1.5 before pursuing it jointly with J. Pascal Gollin. Their 2021 paper again credits Heuer. It also discloses Aharoni’s independently posed, more general infinite-hypergraph problem from 1991; this record is an independently formulated dissertation question, not a claim that all related formulations first appeared in 2018. The finite Lucchesi–Younger theorem is established background.

**Source.** Karl Heuer. *Connectivity in directed and undirected infinite graphs*. Universität Hamburg, 2018. Advisor(s): Reinhard Diestel. [primary source](https://ediss.sub.uni-hamburg.de/bitstream/ediss/7858/1/Dissertation.pdf) · [record](https://ediss.sub.uni-hamburg.de/handle/ediss/7858) Location: Conjecture F.1.5, printed p. 151; optimal-pair definition on pp. 149–151; explicit authorship declaration p. 181.

**Further links.** [1](https://etheses.bham.ac.uk/id/eprint/15965/1/Freschi2025PhD.pdf) · [2](https://etheses.bham.ac.uk/id/eprint/1345/1/Treglown11PhD.pdf#page=4) · [3](https://www.math.uni-hamburg.de/spag/dm/papers/Kuehn.diss.pdf#page=9) · [4](https://onlinelibrary.wiley.com/doi/full/10.1002/jgt.22680) · [5](https://arxiv.org/abs/1909.08373) · [6](https://arxiv.org/abs/2109.03518) · [7](https://pascal-gollin.github.io/)


<a id="q333"></a>

## Q333. Must every infinitely edge-connected graph with at least two vertices contain ei…

**Status:** Open · **Kind:** open problem (Problem 12.7.1) · **Collection** 4

Must every infinitely edge-connected graph with at least two vertices contain either the Farey graph \$F\$ or \$T_{\aleph_0}\*t\$ as a minor with all branch sets finite? Deletion of any finite edge set must leave the graph connected. \$T_{\aleph_0}\$ is the countable tree all of whose degrees are \$\aleph_0\$, and \$\*t\$ adds a vertex adjacent to all its vertices. The Farey graph has vertex set \$\mathbb Q\cup\\{\infty\\}\$, with reduced fractions \$a/b,c/d\$ adjacent iff \$|ad-bc|=1\$ (taking \$\infty=1/0\$).

**Context.** Discovery path (lateral/sibling branch; student → supervisor):
Andrea Freschi → Andrew Treglown: https://etheses.bham.ac.uk/id/eprint/15965/1/Freschi2025PhD.pdf
Andrew Clark Treglown → Daniela Kühn: https://etheses.bham.ac.uk/id/eprint/1345/1/Treglown11PhD.pdf#page=4
Daniela Kühn → Reinhard Diestel: https://www.math.uni-hamburg.de/spag/dm/papers/Kuehn.diss.pdf#page=9
Jan Kurkofka → Reinhard Diestel: https://www.math.uni-hamburg.de/spag/dm/papers/DissertationKurkofka.pdf#page=2 Origin: The thesis explicitly introduces this as one of the author’s own outlook problems. It accompanies his sole-authored 2020 preprint, later Mathematische Annalen 382 (2022), 1881–1900, Problem 7.1. The examination page identifies Diestel as first reviewer and supervisor.

**Source.** Jan Kurkofka. *Ends and tangles, stars and combs, minors and the Farey graph*. Universität Hamburg, 2020. Advisor(s): Reinhard Diestel. [primary source](https://www.math.uni-hamburg.de/spag/dm/papers/DissertationKurkofka.pdf) · [record](https://ediss.sub.uni-hamburg.de/handle/ediss/8491) Location: Problem 12.7.1, printed p. 218; Theorem 12.1; definitions in §12.2.

**Further links.** [1](https://etheses.bham.ac.uk/id/eprint/15965/1/Freschi2025PhD.pdf) · [2](https://etheses.bham.ac.uk/id/eprint/1345/1/Treglown11PhD.pdf#page=4) · [3](https://www.math.uni-hamburg.de/spag/dm/papers/Kuehn.diss.pdf#page=9) · [4](https://www.math.uni-hamburg.de/spag/dm/papers/DissertationKurkofka.pdf#page=2) · [5](https://link.springer.com/article/10.1007/s00208-021-02259-7) · [6](https://arxiv.org/abs/2207.08459) · [7](https://www.jan-kurkofka.eu/) · [8](https://arxiv.org/html/2207.08459v2)


<a id="q334"></a>

## Q334. Let \$\mathcal F\$ be a nonempty finite family of finite sets with \$A\cup B\in\mat…

**Status:** Open · **Kind:** open problem (Problem 9.1) · **Collection** 4

Let \$\mathcal F\$ be a nonempty finite family of finite sets with \$A\cup B\in\mathcal F\$ or \$A\cap B\in\mathcal F\$ for all \$A,B\in\mathcal F\$. Must some \$C\in\mathcal F\$ satisfy the same condition for \$\mathcal F\setminus\\{C\\}\$? Equivalently, can every such family be reduced to \$\varnothing\$ by successive single-member deletions preserving this property?

**Context.** Discovery path (lateral/sibling branch; student → supervisor):
Andrea Freschi → Andrew Treglown: https://etheses.bham.ac.uk/id/eprint/15965/1/Freschi2025PhD.pdf
Andrew Clark Treglown → Daniela Kühn: https://etheses.bham.ac.uk/id/eprint/1345/1/Treglown11PhD.pdf#page=4
Daniela Kühn → Reinhard Diestel: https://www.math.uni-hamburg.de/spag/dm/papers/Kuehn.diss.pdf#page=9
Jean Maximilian Teegen → Reinhard Diestel: https://ediss.sub.uni-hamburg.de/handle/ediss/9205?mode=full Origin: Joint original Elbracht–Kneip–Teegen question, also Problem 1 of The Unravelling Problem, arXiv: 2103.12565 (March 2021). The dissertation explains how it arose in their own study of structural submodularity. Equivalent set-family, distributive-lattice and stepwise-deletion forms count only once; the official repository gives the student’s full name and Diestel as advisor.

**Source.** Jean Maximilian Teegen. *Tangles, Trees of Tangles, and Submodularity*. Universität Hamburg, 2021. Advisor(s): Reinhard Diestel. [primary source](https://ediss.sub.uni-hamburg.de/bitstream/ediss/9205/1/TeegenDissertation.pdf) · [record](https://ediss.sub.uni-hamburg.de/handle/ediss/9205?mode=full) Location: Problem 9.1, printed p. 189; also introductory p. 7. Equivalent occurrence: Elbracht 2021, Problem 22, §5.2.1, p. 209.

**Further links.** [1](https://etheses.bham.ac.uk/id/eprint/15965/1/Freschi2025PhD.pdf) · [2](https://etheses.bham.ac.uk/id/eprint/1345/1/Treglown11PhD.pdf#page=4) · [3](https://www.math.uni-hamburg.de/spag/dm/papers/Kuehn.diss.pdf#page=9) · [4](https://arxiv.org/abs/2103.12565) · [5](https://arxiv.org/html/2103.12565v1) · [6](https://www.math.uni-hamburg.de/spag/dm/allpapersgroup.html)


<a id="q335"></a>

## Q335. Can a finite lattice \$L\$ contain \$P\subseteq L\$ with \$a\vee b\in P\$ or \$a\wedge …

**Status:** Open · **Kind:** open problem (Question 5.1.6) · **Collection** 4

Can a finite lattice \$L\$ contain \$P\subseteq L\$ with \$a\vee b\in P\$ or \$a\wedge b\in P\$ for all \$a,b\in P\$, whose dependency digraph is acyclic, but for which no \$f:L\to\mathbb R_{\ge0}\$ and \$k\in\mathbb R_{\ge0}\$ satisfy \$P=\\{x:f(x)&lt;k\\}\$ and \$f(a\vee b)+f(a\wedge b)\le f(a)+f(b)\$ for all \$a,b\in L\$? The dependency digraph has vertex set \$L\$ and arcs \$a\to b\$ exactly when: \$a\notin P,b\in P\$; or \$a,b\$ have the same membership in \$P\$ and some \$c\in P\$ satisfies \$b=a\vee c,\ a\wedge c\notin P\$, or \$b=a\wedge c,\ a\vee c\notin P\$.

**Context.** Discovery path (lateral/sibling branch; student → supervisor):
Andrea Freschi → Andrew Treglown: https://etheses.bham.ac.uk/id/eprint/15965/1/Freschi2025PhD.pdf
Andrew Clark Treglown → Daniela Kühn: https://etheses.bham.ac.uk/id/eprint/1345/1/Treglown11PhD.pdf#page=4
Daniela Kühn → Reinhard Diestel: https://www.math.uni-hamburg.de/spag/dm/papers/Kuehn.diss.pdf#page=9
Christian Elbracht → Reinhard Diestel: https://ediss.sub.uni-hamburg.de/handle/ediss/9229?mode=full Origin: Own joint questions: dependency digraphs with Teegen and Kneip (2021), and submodular-profile deciders with Diestel and Jacobs (later 2023 revision).

**Source.** Christian Elbracht. *Distinguishing and witnessing dense structures in graphs and abstract separation systems*. Universität Hamburg, 2021. Advisor(s): Reinhard Diestel. [primary source](https://ediss.sub.uni-hamburg.de/bitstream/ediss/9229/1/Dissertation_Christian_Elbracht.pdf) · [record](https://ediss.sub.uni-hamburg.de/handle/ediss/9229?mode=full) Location: Question 5.1.6, printed p. 199; equivalent separation-system Question 5.1.5, p. 198; definitions pp. 195–196.

**Further links.** [1](https://etheses.bham.ac.uk/id/eprint/15965/1/Freschi2025PhD.pdf) · [2](https://etheses.bham.ac.uk/id/eprint/1345/1/Treglown11PhD.pdf#page=4) · [3](https://www.math.uni-hamburg.de/spag/dm/papers/Kuehn.diss.pdf#page=9) · [4](https://arxiv.org/abs/2103.13162) · [5](https://arxiv.org/html/2103.13162v2)


<a id="q336"></a>

## Q336. Let \$V\$ be finite and \$U=\\{(A,B):A\cup B=V\\}\$, ordered by \$(A,B)\le(C,D)\$ iff \$A…

**Status:** Open · **Kind:** open problem (Problem 3.2.5) · **Collection** 4

Let \$V\$ be finite and \$U=\\{(A,B):A\cup B=V\\}\$, ordered by \$(A,B)\le(C,D)\$ iff \$A\subseteq C\$ and \$B\supseteq D\$. Set \$(A,B)^\*=(B,A)\$, \$(A,B)\vee(C,D)=(A\cup C,B\cap D)\$, and \$(A,B)\wedge(C,D)=(A\cap C,B\cup D)\$. Let \$f:U\to\mathbb R_{\ge0}\$ satisfy \$f(s)=f(s^\*)\$ and \$f(r\vee s)+f(r\wedge s)\le f(r)+f(s)\$, and let \$S_k=\\{s:f(s)&lt;k\\}\$. A \$k\$-profile chooses one orientation of each separation in \$S_k\$, is downward closed there, and has \$(r\vee s)^\*\notin\tau\$ whenever \$r,s\in\tau\$; it is regular if no \$(V,A)\$ belongs to it. For \$k\in\mathbb N\$, if a \$k\$-profile \$\tau'\$ extends to a regular \$2k\$-profile, must some \$X\subseteq V\$ satisfy \$|A\cap X|<|B\cap X|\$ for every \$(A,B)\in\tau'\$?

**Context.** Discovery path (lateral/sibling branch; student → supervisor):
Andrea Freschi → Andrew Treglown: https://etheses.bham.ac.uk/id/eprint/15965/1/Freschi2025PhD.pdf
Andrew Clark Treglown → Daniela Kühn: https://etheses.bham.ac.uk/id/eprint/1345/1/Treglown11PhD.pdf#page=4
Daniela Kühn → Reinhard Diestel: https://www.math.uni-hamburg.de/spag/dm/papers/Kuehn.diss.pdf#page=9
Christian Elbracht → Reinhard Diestel: https://ediss.sub.uni-hamburg.de/handle/ediss/9229?mode=full Origin: Own joint questions: dependency digraphs with Teegen and Kneip (2021), and submodular-profile deciders with Diestel and Jacobs (later 2023 revision).

**Source.** Christian Elbracht. *Distinguishing and witnessing dense structures in graphs and abstract separation systems*. Universität Hamburg, 2021. Advisor(s): Reinhard Diestel. [primary source](https://ediss.sub.uni-hamburg.de/bitstream/ediss/9229/1/Dissertation_Christian_Elbracht.pdf) · [record](https://ediss.sub.uni-hamburg.de/handle/ediss/9229?mode=full) Location: Problem 3.2.5, printed p. 44; definitions and Theorem 4 in §§3.2.3–3.2.4. The intended profile to be decided is the lower-order τ′, clarified in the later paper.

**Further links.** [1](https://etheses.bham.ac.uk/id/eprint/15965/1/Freschi2025PhD.pdf) · [2](https://etheses.bham.ac.uk/id/eprint/1345/1/Treglown11PhD.pdf#page=4) · [3](https://www.math.uni-hamburg.de/spag/dm/papers/Kuehn.diss.pdf#page=9) · [4](https://arxiv.org/html/2107.01087v3) · [5](https://arxiv.org/abs/2107.01087) · [6](https://doi.org/10.4310/joc.240907010505)


<a id="q337"></a>

## Q337. For a finite simple graph \$G\$, a degree-associated card is the pair \$(G-v,d_G(v)…

**Status:** Open · **Kind:** conjecture (Conjecture 1.2) · **Collection** 4

For a finite simple graph \$G\$, a degree-associated card is the pair \$(G-v,d_G(v))\$, with \$G-v\$ unlabeled. Let \$\operatorname{drn}(G)\$ be the smallest size of a submultiset of these cards that occurs in no nonisomorphic graph’s degree-associated deck. Are there only finitely many isomorphism classes of trees \$T\$ with \$\operatorname{drn}(T)=3\$?

**Context.** Discovery path (advisor ascent; student → supervisor):
Emily Barranca → Michael David Barrus: https://digitalcommons.uri.edu/cgi/viewcontent.cgi?article=2701&context=oa_diss
Michael David Barrus → Douglas B. West: https://www.math.uri.edu/wp-content/uploads/2021/10/CV_Barrus_Oct2021.pdf Origin: Thesis p. 28 proposes the conjecture after the author’s analysis of two exceptional trees. Chapter 1 identifies Chapter 2 as joint work with West, subsequently published as Degree-associated reconstruction number of graphs (Discrete Mathematics 310 (2010), 2600–2612). The author’s institutional CV explicitly identifies West as dissertation advisor; the indexed title page calls him Director of Research. Kostochka was committee chair, not the research advisor.

**Source.** Michael David Barrus. *On Induced Subgraphs, Degree Sequences, and Graph Structure*. University of Illinois at Urbana-Champaign, 2009. Advisor(s): Douglas B. West. [primary source](https://math.uri.edu/~barrus/papers/Dissertation.pdf) · [record](https://www.ideals.illinois.edu/items/88202) Location: Unnumbered conjecture, printed p. 28; chapter provenance on p. 1. Exact author-hosted thesis pages and title page were read through the search index; the live author PDF now redirects, so full-file retrieval was unavailable. Joint Barrus–West paper, Conjecture 1.2, author version p. 2, supplies the equivalent formulation and definitions.

**Results.**

- **Investigated, unresolved** (B7: submitted unresolved): No new analysis or status promotion in this return. Remaining/limits: not_attempted Intake: Scope and identity checked; no independent proof or renewed literature audit of this question. [Report](../../solutions/b7-2026-10-07/README.md).

**Further links.** [1](https://digitalcommons.uri.edu/cgi/viewcontent.cgi?article=2701&context=oa_diss) · [2](https://www.math.uri.edu/wp-content/uploads/2021/10/CV_Barrus_Oct2021.pdf) · [3](https://dwest.web.illinois.edu/pubs/drn.pdf) · [4](https://toc.ui.ac.ir/article_28135_1bd687e1d71802a0126d74bcfab76380.pdf) · [5](https://doi.org/10.22108/toc.2024.131563.1938)


<a id="q359"></a>

## Q359. For two groups of sizes a and b sharing indivisible goods, determine the largest…

**Status:** Open · **Kind:** open problem · **Collection** 4

For two groups of sizes a and b sharing indivisible goods, determine the largest α(a,b) such that every nonnegative additive utility profile admits a partition (G₁,G₂) giving each agent i utility at least α(a,b)μ\_i. Here μ\_i = max_{S⊆G} min{u_i(S),u_i(G\S)}. In particular, determine the asymptotic order of α(a,1) as a grows.

**Context.** Discovery path (advisor ascent; student → supervisor):
Sheung Man Yuen → Warut Suksompong: https://www.comp.nus.edu.sg/~warut/
Warut Suksompong → Tim Roughgarden: https://stacks.stanford.edu/file/vw246vj2286/dissertation-augmented.pdf Origin: Suksompong’s own 2017 preprint and 2018 journal article introduce group MMS approximation; the thesis explicitly asks for these optimal ratios. Suksompong defines this scheduling invariant in his own 2016 paper; his thesis explicitly asks whether bound one is attainable for even n.

**Source.** Warut Suksompong. *Resource Allocation and Decision Making for Groups*. Stanford University, 2018. Advisor(s): Tim Roughgarden. [primary source](https://stacks.stanford.edu/file/vw246vj2286/dissertation-augmented.pdf) · [record](https://purl.stanford.edu/vw246vj2286) Location: §5.5, printed p. 65 (PDF p. 77); Table 5.1, p. 56; definitions §2.1.

**Further links.** [1](https://www.comp.nus.edu.sg/~warut/) · [2](https://arxiv.org/abs/1706.09869) · [3](https://arxiv.org/html/2404.11543v1) · [4](https://doi.org/10.1016/j.tcs.2025.115151)


<a id="q360"></a>

## Q360. For every even n ≥ 4, can the edges of K_n be ordered as one match per time slot…

**Status:** Open · **Kind:** open problem · **Collection** 4

For every even n ≥ 4, can the edges of K_n be ordered as one match per time slot so that every pair of opponents has rest times differing by at most one? Rest time counts intervening matches since that player’s preceding match; before the first slot, all players are assigned a common fictitious match at slot zero.

**Context.** Discovery path (advisor ascent; student → supervisor):
Sheung Man Yuen → Warut Suksompong: https://www.comp.nus.edu.sg/~warut/
Warut Suksompong → Tim Roughgarden: https://stacks.stanford.edu/file/vw246vj2286/dissertation-augmented.pdf Origin: Suksompong’s own 2017 preprint and 2018 journal article introduce group MMS approximation; the thesis explicitly asks for these optimal ratios. Suksompong defines this scheduling invariant in his own 2016 paper; his thesis explicitly asks whether bound one is attainable for even n.

**Source.** Warut Suksompong. *Resource Allocation and Decision Making for Groups*. Stanford University, 2018. Advisor(s): Tim Roughgarden. [primary source](https://stacks.stanford.edu/file/vw246vj2286/dissertation-augmented.pdf) · [record](https://purl.stanford.edu/vw246vj2286) Location: §9.5, printed p. 124 (PDF p. 136); Definition 9.2.3, p. 117.

**Further links.** [1](https://www.comp.nus.edu.sg/~warut/) · [2](https://arxiv.org/abs/1804.04504) · [3](https://pmc.ncbi.nlm.nih.gov/articles/PMC9468531/) · [4](https://pypi.org/project/asyroro/)


<a id="q1152"></a>

## Q1152. Closedness of the projection-volume region

**Status:** Open · **Kind:** conjecture (Conjecture 13) · **Collection** 12

Is ψ\_n closed for every n?

**Context.** Doctoral context for question 1152: Žarko Ranđelović. Some Results in Combinatorics and Combinatorial Geometry. PhD, University of Cambridge, 2024. Advisor: Imre Leader. Origin for questions 1152, 1153: Joint doctoral work; Ranđelović, Cambridge PhD 2024, supervisor Imre Leader; thesis Conjectures 22–23. Setup for questions 1152, 1153: For n≥1, let ψ\_n⊂R^(2^n−1) consist of vectors (log vol_|A|(π\_A T)) indexed by nonempty A⊆[n], where T⊂R^n is compact with positive n-volume and π\_A is coordinate projection.

**Source.** Imre Leader; Žarko Ranđelović; Eero Räty. *Inequalities on Projected Volumes*. 2021. [primary source](https://doi.org/10.1137/19M1296306) Location: Conjecture 13.

**Literature check.** Status for questions 1152, 1153, checked 6 October 2026: Checked 2026-10-06: no resolution located in bounded searches.

**Further links.** [1](https://arxiv.org/abs/1909.12858) · [2](https://doi.org/10.1137/19M1300078) · [3](https://api.repository.cam.ac.uk/server/api/core/bitstreams/834c439d-aab8-405d-a636-4db2d49e600b/content) · [4](https://www.mi.sanu.ac.rs/novi_sajt/members/fulltime/cv/zrandjelovic.pdf)


<a id="q1153"></a>

## Q1153. Dilation closure of realizable log-projections

**Status:** Open · **Kind:** conjecture (Conjecture 14) · **Collection** 12

For every n, v∈ψ\_n and λ>1, must λv∈ψ\_n?

**Context.** Origin for questions 1152, 1153: Joint doctoral work; Ranđelović, Cambridge PhD 2024, supervisor Imre Leader; thesis Conjectures 22–23. Setup for questions 1152, 1153: For n≥1, let ψ\_n⊂R^(2^n−1) consist of vectors (log vol_|A|(π\_A T)) indexed by nonempty A⊆[n], where T⊂R^n is compact with positive n-volume and π\_A is coordinate projection.

**Source.** Imre Leader; Žarko Ranđelović; Eero Räty. *Inequalities on Projected Volumes*. 2021. [primary source](https://doi.org/10.1137/19M1296306) Location: Conjecture 14.

**Literature check.** Status for questions 1152, 1153, checked 6 October 2026: Checked 2026-10-06: no resolution located in bounded searches.

**Further links.** [1](https://arxiv.org/abs/1909.12858) · [2](https://doi.org/10.1137/19M1300078) · [3](https://api.repository.cam.ac.uk/server/api/core/bitstreams/834c439d-aab8-405d-a636-4db2d49e600b/content) · [4](https://www.mi.sanu.ac.rs/novi_sajt/members/fulltime/cv/zrandjelovic.pdf)


<a id="q1154"></a>

## Q1154. Exponentially small winning transversal families

**Status:** Open · **Kind:** conjecture (Conjecture 5) · **Collection** 12

Let f(n) be the minimum |F| for which the first player can force a win. Is there a constant c>1 such that f(n)&lt;c^n for all sufficiently large n?

**Context.** Doctoral context for question 1154: see question 1152. Origin for questions 1154, 1155: Ranđelović’s Cambridge PhD (2024, supervisor Imre Leader), Ch.6; follow-on conjectures in July 2025 revision (the thesis uses a different g). Setup for questions 1154, 1155: On an n×n board, n≥4, players alternately claim one empty cell; the first to fill a member of a prescribed family F of transversals wins. Each transversal has one cell per row and column.

**Source.** Žarko Ranđelović. *The transversal game*. 2024. [primary source](https://arxiv.org/abs/2401.16768) Location: Conjecture 5.

**Literature check.** Status for questions 1154, 1155, checked 6 October 2026: Guan (August 2026), §7, expressly leaves both targets unresolved.

**Further links.** [1](https://arxiv.org/abs/2401.16768v2) · [2](https://arxiv.org/abs/2608.13501) · [3](https://api.repository.cam.ac.uk/server/api/core/bitstreams/834c439d-aab8-405d-a636-4db2d49e600b/content) · [4](https://www.mi.sanu.ac.rs/novi_sajt/members/fulltime/cv/zrandjelovic.pdf)


<a id="q1155"></a>

## Q1155. Vanishing-density threshold for forced wins

**Status:** Open · **Kind:** conjecture (Conjecture 7) · **Collection** 12

Let g(n) be the least integer such that every family F with |F|≥g(n) gives the first player a winning strategy. Is g(n)=o(n!)?

**Context.** Doctoral context for question 1155: see question 1152. Origin for questions 1154, 1155: Ranđelović’s Cambridge PhD (2024, supervisor Imre Leader), Ch.6; follow-on conjectures in July 2025 revision (the thesis uses a different g). Setup for questions 1154, 1155: On an n×n board, n≥4, players alternately claim one empty cell; the first to fill a member of a prescribed family F of transversals wins. Each transversal has one cell per row and column.

**Source.** Žarko Ranđelović. *The transversal game*. 2024. [primary source](https://arxiv.org/abs/2401.16768) Location: Conjecture 7.

**Literature check.** Status for questions 1154, 1155, checked 6 October 2026: Guan (August 2026), §7, expressly leaves both targets unresolved.

**Further links.** [1](https://arxiv.org/abs/2401.16768v2) · [2](https://arxiv.org/abs/2608.13501) · [3](https://api.repository.cam.ac.uk/server/api/core/bitstreams/834c439d-aab8-405d-a636-4db2d49e600b/content) · [4](https://www.mi.sanu.ac.rs/novi_sajt/members/fulltime/cv/zrandjelovic.pdf)


<a id="q1156"></a>

## Q1156. Which nearest-neighbor maps embed in fixed dimension?

**Status:** Open, partial results · **Kind:** open problem (Problem 20) · **Collection** 12

For each fixed k≥1, characterize exactly the finite maps f that admit such a nearest-neighbor realization in Euclidean R^k.

**Context.** Doctoral context for question 1156: see question 1152. Origin for questions 1156, 1157: Ranđelović, Cambridge PhD 2024, supervisor Imre Leader; Ch.7. Current paper: July 2025 v3. Setup for questions 1156, 1157: For n≥3, realizations use distinct labeled points A_1,…,A_n with all distances between distinct unordered pairs mutually different. Maps f,g:[n]→[n] have no fixed points; f(i),g(i) designate the unique nearest and farthest other points.

**Source.** Žarko Ranđelović. *Minimal and Maximal Distances in Metric Spaces*. 2024. [primary source](https://arxiv.org/abs/2409.14648) Location: Problem 20.

**Literature check.** Status for questions 1156, 1157, checked 6 October 2026: Checked 2026-10-06: no resolution located in bounded searches.

**Results.**

- **Partial result**: Complete constructive line subcase. Remaining: partial Recorded from the external B7 return  (backfilled 2026-10-08); selected local controls in the intake; external archive not uploaded; not independently re-derived here. [Details](../../solutions/b7-2026-10-07/B7_Research_Report_2026-10-07.md).
- **Related result** (B7-R14: submitted proved): A fixed-point-free nearest-neighbor map is realizable on the line with all pair distances distinct iff its undirected edge graph is a disjoint union of paths; integer coordinates in [0,2^(n-1)-1] suffice. Remaining/limits: Fixed Euclidean dimensions at least two remain. [Report](../../solutions/b7-2026-10-07/README.md).

**Further links.** [1](https://arxiv.org/abs/2409.14648v3) · [2](https://api.repository.cam.ac.uk/server/api/core/bitstreams/834c439d-aab8-405d-a636-4db2d49e600b/content) · [3](https://www.mi.sanu.ac.rs/novi_sajt/members/fulltime/cv/zrandjelovic.pdf)


<a id="q1157"></a>

## Q1157. Joint nearest and farthest maps in fixed dimension

**Status:** Open, partial results · **Kind:** open problem (Problem 21) · **Collection** 12

For each fixed k≥1, characterize the pairs (f,g) realizable in some metric space that admit a simultaneous realization in Euclidean R^k.

**Context.** Doctoral context for question 1157: see question 1152. Origin for questions 1156, 1157: Ranđelović, Cambridge PhD 2024, supervisor Imre Leader; Ch.7. Current paper: July 2025 v3. Setup for questions 1156, 1157: For n≥3, realizations use distinct labeled points A_1,…,A_n with all distances between distinct unordered pairs mutually different. Maps f,g:[n]→[n] have no fixed points; f(i),g(i) designate the unique nearest and farthest other points.

**Source.** Žarko Ranđelović. *Minimal and Maximal Distances in Metric Spaces*. 2024. [primary source](https://arxiv.org/abs/2409.14648) Location: Problem 21.

**Literature check.** Status for questions 1156, 1157, checked 6 October 2026: Checked 2026-10-06: no resolution located in bounded searches.

**Results.**

- **Partial result**: Complete line criterion via rational linear feasibility. Remaining: partial Recorded from the external B7 return  (backfilled 2026-10-08); selected local controls in the intake; external archive not uploaded; not independently re-derived here. [Details](../../solutions/b7-2026-10-07/B7_Research_Report_2026-10-07.md).
- **Related result** (B7-R15: submitted proved): Simultaneous nearest/farthest line realizability is equivalent to feasibility of one of the n! explicitly given rational linear systems, with strict pair-distance uniqueness attainable by rational perturbation. Remaining/limits: Higher dimensions and a polynomial-time bound are not proved. [Report](../../solutions/b7-2026-10-07/README.md).

**Further links.** [1](https://arxiv.org/abs/2409.14648v3) · [2](https://api.repository.cam.ac.uk/server/api/core/bitstreams/834c439d-aab8-405d-a636-4db2d49e600b/content) · [3](https://www.mi.sanu.ac.rs/novi_sajt/members/fulltime/cv/zrandjelovic.pdf)


<a id="q1158"></a>

## Q1158. Total positivity of higher-order cycle triangles

**Status:** Open, partial results · **Kind:** open problem · **Collection** 12

Is C^(r) totally positive for every integer r≥2?

**Context.** Doctoral context for question 1158: Bishal Deb. Enumerative combinatorics, continued fractions and total positivity. PhD, University College London, 2023. Advisor: Alan D. Sokal. Origin for questions 1158, 1159, 1160, 1161: Deb, UCL PhD 2023, Enumerative combinatorics, continued fractions and total positivity; supervisor Alan D. Sokal, Ch.6. Setup for questions 1158, 1159, 1160, 1161: C^(r)\_(n,k) and S^(r)\_(n,k) count, respectively, permutations and set partitions of [n+(r−1)k] with k cycles/blocks, each of size≥r. Put c_(r,n)(x)=Σ\_k C^(r)\_(n,k)x^k and s_(r,n)(x)=Σ\_k S^(r)\_(n,k)x^k; n,k≥0, r≥1. “Totally positive” means all minors are nonnegative.

**Source.** Bishal Deb; Alan D. Sokal. *Higher-order Stirling cycle and subset triangles: Total positivity, continued fractions and real-rootedness*. 2025. [primary source](https://arxiv.org/abs/2507.18959) Location: 1.3(a).

**Literature check.** Status for questions 1158, 1159, 1160, 1161, checked 6 October 2026: 2026-10-06: retained conjectures; later log-concavity claim does not settle these targets.

**Results.**

- **Partial result**: Every cycle-triangle minor of order at most two is nonnegative for every r>=1. Exact Neville factors certify all minors of the 25x25 blocks for r=2,3,11,12,16,32. Remaining: Infinite minors of order at least three remain unresolved. Source already reports larger finite blocks for r<=10. Recorded from the external B3 return  (backfilled 2026-10-08); initial argument review and bounded independent controls in the intake; not independently re-derived here. [Details](../../solutions/b3-2026-10-06/README.md).

**Further links.** [1](https://bishaldeb.com/research.html) · [2](https://discovery.ucl.ac.uk/10179955/1/BishalDeb_PhDThesis_Final.pdf) · [3](https://github.com/Carptopus/MathExplore-Notes/blob/master/research/higher-order-stirling-cycle-logconcavity/higher-order-stirling-cycle-logconcavity.tex) · [4](https://bishaldeb.com/CV.pdf)


<a id="q1159"></a>

## Q1159. Total positivity of higher-order subset triangles

**Status:** Open, partial results · **Kind:** open problem · **Collection** 12

Is S^(r) totally positive for every integer r≥2?

**Context.** Origin for questions 1158, 1159, 1160, 1161: Deb, UCL PhD 2023, Enumerative combinatorics, continued fractions and total positivity; supervisor Alan D. Sokal, Ch.6. Setup for questions 1158, 1159, 1160, 1161: C^(r)\_(n,k) and S^(r)\_(n,k) count, respectively, permutations and set partitions of [n+(r−1)k] with k cycles/blocks, each of size≥r. Put c_(r,n)(x)=Σ\_k C^(r)\_(n,k)x^k and s_(r,n)(x)=Σ\_k S^(r)\_(n,k)x^k; n,k≥0, r≥1. “Totally positive” means all minors are nonnegative.

**Source.** Bishal Deb; Alan D. Sokal. *Higher-order Stirling cycle and subset triangles: Total positivity, continued fractions and real-rootedness*. 2025. [primary source](https://arxiv.org/abs/2507.18959) Location: 1.4(a).

**Literature check.** Status for questions 1158, 1159, 1160, 1161, checked 6 October 2026: 2026-10-06: retained conjectures; later log-concavity claim does not settle these targets.

**Results.**

- **Partial result**: Every subset-triangle minor of order at most two is nonnegative for every r>=1. Exact Neville factors certify all minors of the 25x25 blocks for r=2,3,11,12,16,32. Remaining: Infinite minors of order at least three remain unresolved. Source already reports larger finite blocks for r<=10. Recorded from the external B3 return  (backfilled 2026-10-08); initial argument review and bounded independent controls in the intake; not independently re-derived here. [Details](../../solutions/b3-2026-10-06/README.md).

**Further links.** [1](https://bishaldeb.com/research.html) · [2](https://discovery.ucl.ac.uk/10179955/1/BishalDeb_PhDThesis_Final.pdf) · [3](https://github.com/Carptopus/MathExplore-Notes/blob/master/research/higher-order-stirling-cycle-logconcavity/higher-order-stirling-cycle-logconcavity.tex) · [4](https://bishaldeb.com/CV.pdf)


<a id="q1160"></a>

## Q1160. Hankel positivity for higher-order cycle polynomials

**Status:** Open, partial results · **Kind:** open problem · **Collection** 12

For every integer r≥3, does every minor of (c_(r,i+j)(x))\_(i,j≥0) have nonnegative coefficients?

**Context.** Origin for questions 1158, 1159, 1160, 1161: Deb, UCL PhD 2023, Enumerative combinatorics, continued fractions and total positivity; supervisor Alan D. Sokal, Ch.6. Setup for questions 1158, 1159, 1160, 1161: C^(r)\_(n,k) and S^(r)\_(n,k) count, respectively, permutations and set partitions of [n+(r−1)k] with k cycles/blocks, each of size≥r. Put c_(r,n)(x)=Σ\_k C^(r)\_(n,k)x^k and s_(r,n)(x)=Σ\_k S^(r)\_(n,k)x^k; n,k≥0, r≥1. “Totally positive” means all minors are nonnegative.

**Source.** Bishal Deb; Alan D. Sokal. *Higher-order Stirling cycle and subset triangles: Total positivity, continued fractions and real-rootedness*. 2025. [primary source](https://arxiv.org/abs/2507.18959) Location: 1.3(d).

**Literature check.** Status for questions 1158, 1159, 1160, 1161, checked 6 October 2026: 2026-10-06: retained conjectures; later log-concavity claim does not settle these targets.

**Results.**

- **Partial result**: For every r>=2 and every cycle Hankel minor on increasing nonnegative index sets I,J, the degree is sum(I)+sum(J), the vanishing order is |I|-1_{0 in I and 0 in J}, and both extreme coefficients are strictly positive. Remaining: Interior coefficient positivity remains unresolved. A negative coefficient in a related subset Hankel minor is not a counterexample to this cycle question. B3 continuation (7 Oct): B3C-04 Leading cycle Hankel block; none closes the question. Recorded from the external B3 return  (backfilled 2026-10-08); initial argument review and bounded independent controls in the intake; not independently re-derived here. [Details](../../solutions/b3-2026-10-06/README.md).
- **Related result** (B3C-04: Leading cycle Hankel block): For every integer r>=2, all nonempty minors of (c_(r,i+j)(x))\_(i,j=0)^2 are coefficientwise nonnegative, with positive coefficients throughout each stated nonzero support. The 3x3 determinant has support exactly degrees 2 through 6. Limits: Only row and column indices 0,1,2. Universal Hankel TN2 for either family and arbitrary cycle order-three minors remain unproved here. [Report](../../solutions/b3-continuation-2026-10-07/README.md).

**Further links.** [1](https://bishaldeb.com/research.html) · [2](https://discovery.ucl.ac.uk/10179955/1/BishalDeb_PhDThesis_Final.pdf) · [3](https://github.com/Carptopus/MathExplore-Notes/blob/master/research/higher-order-stirling-cycle-logconcavity/higher-order-stirling-cycle-logconcavity.tex) · [4](https://bishaldeb.com/CV.pdf)


<a id="q1161"></a>

## Q1161. Half-plane stability at order three

**Status:** Open · **Kind:** open problem · **Collection** 12

For every n≥1, do all zeros of c_(3,n)(x) and s_(3,n)(x) satisfy Re z≤0?

**Context.** Origin for questions 1158, 1159, 1160, 1161: Deb, UCL PhD 2023, Enumerative combinatorics, continued fractions and total positivity; supervisor Alan D. Sokal, Ch.6. Setup for questions 1158, 1159, 1160, 1161: C^(r)\_(n,k) and S^(r)\_(n,k) count, respectively, permutations and set partitions of [n+(r−1)k] with k cycles/blocks, each of size≥r. Put c_(r,n)(x)=Σ\_k C^(r)\_(n,k)x^k and s_(r,n)(x)=Σ\_k S^(r)\_(n,k)x^k; n,k≥0, r≥1. “Totally positive” means all minors are nonnegative.

**Source.** Bishal Deb; Alan D. Sokal. *Higher-order Stirling cycle and subset triangles: Total positivity, continued fractions and real-rootedness*. 2025. [primary source](https://arxiv.org/abs/2507.18959) Location: 7.5, 7.7.

**Literature check.** Status for questions 1158, 1159, 1160, 1161, checked 6 October 2026: 2026-10-06: retained conjectures; later log-concavity claim does not settle these targets.

**Results.**

- **Investigated, unresolved** (B3: submitted unresolved): Both third-order row families, for each n=1,...,80, have a simple zero at 0 and all other roots strictly in the left half-plane, certified by exact rational Routh pivots. Remaining/limits: No all-n stability proof. Failure of generic differential-operator stability preservation does not refute stability of the actual rows. [Report](../../solutions/b3-2026-10-06/README.md).

**Further links.** [1](https://bishaldeb.com/research.html) · [2](https://discovery.ucl.ac.uk/10179955/1/BishalDeb_PhDThesis_Final.pdf) · [3](https://github.com/Carptopus/MathExplore-Notes/blob/master/research/higher-order-stirling-cycle-logconcavity/higher-order-stirling-cycle-logconcavity.tex) · [4](https://bishaldeb.com/CV.pdf)


<a id="q1162"></a>

## Q1162. Connectivity versus disjoint perfect matchings

**Status:** Open · **Kind:** conjecture (Conjecture 3.6) · **Collection** 12

For all integers ℓ≥3 and r≥2ℓ, is there a 2ℓ-edge-connected r-graph with at most ℓ−1 pairwise edge-disjoint perfect matchings?

**Context.** Doctoral context for question 1162: Isaak H. Wolf. Factors in graphs. PhD, Universität Paderborn, 2024. Advisor: Eckhard Steffen. Origin for question 1162: Joint doctoral work; Wolf, Factors in graphs, Paderborn PhD 2024, supervisor Eckhard Steffen; Conjecture 7.4.3. Setup for question 1162: An r-graph is a finite loopless r-regular multigraph such that every odd vertex set has at least r edges to its complement.

**Source.** Yulai Ma; Davide Mattiolo; Eckhard Steffen; Isaak H. Wolf. *Edge-connectivity and pairwise disjoint perfect matchings in regular graphs*. 2024. [primary source](https://doi.org/10.1007/s00493-023-00078-9) Location: Conjecture 3.6, p.11; thesis Conjecture 7.4.3, p.114.

**Literature check.** Status for question 1162, checked 6 October 2026: Checked 2026-10-06: no resolution located in bounded searches.

**Further links.** [1](https://arxiv.org/abs/2208.14835v2) · [2](https://digital.ub.uni-paderborn.de/hs/download/pdf/7647599) · [3](https://digital.ub.uni-paderborn.de/hs/content/titleinfo/7647599)


<a id="q1163"></a>

## Q1163. Monotonic minimum order for exact matching packing

**Status:** Open · **Kind:** conjecture (Conjecture 5.3) · **Collection** 12

For all r≥4 and 2≤k≤r−2, is o(r,k−1)≥o(r,k)?

**Context.** Doctoral context for question 1163: see question 1162. Origin for question 1163: Joint doctoral work; Wolf, Factors in graphs, Paderborn PhD 2024, supervisor Eckhard Steffen, Conjecture 8.4.3. Setup for question 1163: An r-graph is a finite loopless r-regular multigraph such that every odd vertex set has at least r edges to its complement. Let π(G) be the maximum number of pairwise edge-disjoint perfect matchings and o(r,k)=min{|V(G)|:G is an r-graph, π(G)=k}.

**Source.** Yulai Ma; Davide Mattiolo; Eckhard Steffen; Isaak H. Wolf. *Sets of r-Graphs that Color All r-Graphs*. 2025. [primary source](https://doi.org/10.1007/s00493-025-00144-4) Location: Conjecture 5.3.

**Literature check.** Status for question 1163, checked 6 October 2026: Checked 2026-10-06: no resolution located in bounded searches.

**Further links.** [1](https://link.springer.com/article/10.1007/s00493-025-00144-4) · [2](https://arxiv.org/abs/2305.08619) · [3](https://digital.ub.uni-paderborn.de/hs/download/pdf/7647599) · [4](https://digital.ub.uni-paderborn.de/hs/content/titleinfo/7647599)


<a id="q1164"></a>

## Q1164. Perfect matchings needed to remove all odd cycles

**Status:** Open · **Kind:** open problem · **Collection** 12

For each r≥4, determine the least t such that every r-graph has t perfect matchings whose union can be deleted to leave a bipartite graph.

**Context.** Doctoral context for question 1164: see question 1162. Origin for question 1164: Thesis-origin question, §5.5. Setup for question 1164: An r-graph is a finite loopless r-regular multigraph such that every odd vertex set has at least r edges to its complement.

**Source.** Isaak H. Wolf. *Factors in graphs*. 2024. Advisor(s): Eckhard Steffen. [primary source](https://digital.ub.uni-paderborn.de/hs/download/pdf/7647599) Location: §5.5, p.67, final paragraph.

**Literature check.** Status for question 1164, checked 6 October 2026: Checked 2026-10-06: no resolution located in bounded searches.

**Further links.** [1](https://digital.ub.uni-paderborn.de/hs/content/titleinfo/7647599)


<a id="q1165"></a>

## Q1165. The missing five-regular class-two graph

**Status:** Open · **Kind:** open problem (Problem 1.6) · **Collection** 12

Does a finite loopless 5-regular multigraph exist that is 5-edge-connected and has edge-chromatic number greater than 5?

**Context.** Doctoral context for question 1165: see question 1162. Origin for question 1165: Joint doctoral work; Wolf, Factors in graphs, Paderborn PhD 2024, supervisor Eckhard Steffen; Problem 7.0.2.

**Source.** Yulai Ma; Davide Mattiolo; Eckhard Steffen; Isaak H. Wolf. *Pairwise disjoint perfect matchings in r-edge-connected r-regular graphs*. 2023. [primary source](https://doi.org/10.1137/22M1500654) Location: Problem 1.6, p.3; thesis Problem 7.0.2, p.79.

**Literature check.** Status for question 1165, checked 6 October 2026: Checked 2026-10-06: no resolution located in bounded searches.

**Further links.** [1](https://arxiv.org/abs/2206.10975v2) · [2](https://arxiv.org/abs/2411.10046) · [3](https://digital.ub.uni-paderborn.de/hs/download/pdf/7647599) · [4](https://digital.ub.uni-paderborn.de/hs/content/titleinfo/7647599)


<a id="q1166"></a>

## Q1166. Force unequal complete tripartite graphs at the smallest exponent

**Status:** Open · **Kind:** conjecture (Conjecture 6.2) · **Collection** 12

For every fixed triple of positive integers t≤s≤r, is there K>0 such that, for every n, any simple tripartite graph with three parts of size n and minimum degree at least n+K n^(1−1/t) contains K_(t,s,r)?

**Context.** Origin for question 1166: Authors’ Conjecture 6.2; paper-only origin. The balanced t=t=t case is proved, not selected.

**Source.** Francesco Di Braccio; Freddie Illingworth. *The Zarankiewicz problem on tripartite graphs*. 2026. [primary source](https://doi.org/10.1112/jlms.70621) Location: §6, Conjecture 6.2.

**Literature check.** Status for question 1166, checked 6 October 2026: July 2026 journal version retains the conjecture; no later resolution located.

**Further links.** [1](https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/jlms.70621) · [2](https://arxiv.org/abs/2412.03505)


<a id="q1167"></a>

## Q1167. Odd-partite independent-transversal blowups

**Status:** Open · **Kind:** conjecture (Conjecture 6.3) · **Collection** 12

For each odd r≥5 and integer s≥2, do C>0 and n₀ exist such that every such graph with n≥n₀ and Δ(G)≤((r−1)/(2r−4))n−C n^(1−1/s) has an independent set containing exactly s vertices from every part?

**Context.** Origin for questions 1167, 1168: Paper-origin questions, §6. Setup for questions 1167, 1168: Graphs are simple r-partite graphs with specified independent parts, each of size n. An independent transversal selects exactly one vertex from each part.

**Source.** Yantao Tang; Yi Zhao. *Number of independent transversals in multipartite graphs*. 2025. [primary source](https://arxiv.org/abs/2504.03950) Location: Conjecture 6.3.

**Literature check.** Status for questions 1167, 1168, checked 6 October 2026: 2026-10-06: both remain stated open; no matching resolution located.

**Further links.** [1](https://math.gsu.edu/yzhao6/numofIT_arXiv.pdf) · [2](https://math.gsu.edu/yzhao6/pub.html)


<a id="q1168"></a>

## Q1168. Uniformly many independent transversals at half-degree

**Status:** Open · **Kind:** open problem · **Collection** 12

For all positive integers r,n, does Δ(G)≤n/2 guarantee at least (n/2)^r independent transversals?

**Context.** Origin for questions 1167, 1168: Paper-origin questions, §6. Setup for questions 1167, 1168: Graphs are simple r-partite graphs with specified independent parts, each of size n. An independent transversal selects exactly one vertex from each part.

**Source.** Yantao Tang; Yi Zhao. *Number of independent transversals in multipartite graphs*. 2025. [primary source](https://arxiv.org/abs/2504.03950) Location: After Corollary 6.2.

**Literature check.** Status for questions 1167, 1168, checked 6 October 2026: 2026-10-06: both remain stated open; no matching resolution located.

**Further links.** [1](https://math.gsu.edu/yzhao6/numofIT_arXiv.pdf) · [2](https://math.gsu.edu/yzhao6/pub.html)


<a id="q1252"></a>

## Q1252. Infinitely many ternary Barba orders

**Status:** Open · **Kind:** open problem (Problem 17) · **Collection** 13

Are there infinitely many orders n for which an n×n matrix B over μ\_3 satisfies BB\*=(n−1)I_n+J_n?

**Context.** Origin for questions 1252, 1253, 1254: Advisor: Padraig Ó Catháin. Thesis research; BH cases continue de Launey–Dawson. Setup for questions 1252, 1253, 1254: Write μ\_m={exp(2πij/m):0≤j&lt;m}; M\* is conjugate transpose, I_n the identity and J_n the all-ones matrix.

**Source.** Guillermo Núñez Ponasso. *Combinatorics of Complex Maximal Determinant Matrices*. 2023. [primary source](https://arxiv.org/abs/2404.09040) Location: Research Problem 17, p.142.

**Literature check.** Status for questions 1252, 1253, 1254, checked 6 October 2026: Checked 2026-10-06: retained in February 2026 thesis; 2025 determinant follow-on does not settle these targets.

**Further links.** [1](https://arxiv.org/abs/2503.11114) · [2](https://doi.org/10.1016/j.laa.2025.05.024) · [3](https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/1872-05.pdf) · [4](https://arxiv.org/pdf/2404.09040v2)


<a id="q1253"></a>

## Q1253. The ternary determinant maximum at order fifteen

**Status:** Open · **Kind:** open problem (Problem 20) · **Collection** 13

Determine max{|det M|:M∈μ\_3^(15×15)}.

**Context.** Origin for questions 1252, 1253, 1254: Advisor: Padraig Ó Catháin. Thesis research; BH cases continue de Launey–Dawson. Setup for questions 1252, 1253, 1254: Write μ\_m={exp(2πij/m):0≤j&lt;m}; M\* is conjugate transpose, I_n the identity and J_n the all-ones matrix.

**Source.** Guillermo Núñez Ponasso. *Combinatorics of Complex Maximal Determinant Matrices*. 2023. [primary source](https://arxiv.org/abs/2404.09040) Location: Research Problem 20, p.152.

**Literature check.** Status for questions 1252, 1253, 1254, checked 6 October 2026: Checked 2026-10-06: retained in February 2026 thesis; 2025 determinant follow-on does not settle these targets.

**Further links.** [1](https://arxiv.org/abs/2503.11114) · [2](https://doi.org/10.1016/j.laa.2025.05.024) · [3](https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/1872-05.pdf) · [4](https://arxiv.org/pdf/2404.09040v2)


<a id="q1254"></a>

## Q1254. Two remaining small quaternary determinant maxima

**Status:** Open · **Kind:** open problem (Problem 21) · **Collection** 13

Determine max{|det M|:M∈μ\_4^(n×n)} for n=11 and n=17.

**Context.** Origin for questions 1252, 1253, 1254: Advisor: Padraig Ó Catháin. Thesis research; BH cases continue de Launey–Dawson. Setup for questions 1252, 1253, 1254: Write μ\_m={exp(2πij/m):0≤j&lt;m}; M\* is conjugate transpose, I_n the identity and J_n the all-ones matrix.

**Source.** Guillermo Núñez Ponasso. *Combinatorics of Complex Maximal Determinant Matrices*. 2023. [primary source](https://arxiv.org/abs/2404.09040) Location: Research Problem 21, p.159.

**Literature check.** Status for questions 1252, 1253, 1254, checked 6 October 2026: Checked 2026-10-06: retained in February 2026 thesis; 2025 determinant follow-on does not settle these targets.

**Further links.** [1](https://arxiv.org/abs/2503.11114) · [2](https://doi.org/10.1016/j.laa.2025.05.024) · [3](https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/1872-05.pdf) · [4](https://arxiv.org/pdf/2404.09040v2)


<a id="q1255"></a>

## Q1255. Can positive graph inertia grow faster than every polynomial?

**Status:** Open · **Kind:** open problem (Problem 4.1) · **Collection** 13

Does there exist a polynomial f such that n^+(G)≤f(n^−(G)) for every finite simple graph G?

**Context.** Origin for question 1255: Earlier Akbari–Elphick–Kumar–Pragada–Tang problem, explicitly retained after refuting quadratic bounds. Setup for question 1255: For a finite simple graph G, n^+(G),n^−(G) count positive and negative adjacency eigenvalues with multiplicity.

**Source.** Clive Elphick; Hitesh Kumar; Shivaramakrishna Pragada; Thomás Jung Spier. *Resolution of a problem of Mohar on non-positive inertia*. 2026. [primary source](https://arxiv.org/abs/2609.06319) Location: Problem 4.1, §4.

**Literature check.** Status for question 1255, checked 6 October 2026: Checked 2026-10-06: explicitly open in September 2026; no later resolution located.

**Further links.** [1](https://arxiv.org/abs/2508.01163) · [2](https://doi.org/10.1016/j.disc.2025.114953) · [3](https://arxiv.org/abs/2605.07196)


<a id="q1256"></a>

## Q1256. Prescribed transversal two-factors at the El-Zahar threshold

**Status:** Open · **Kind:** open problem (Problem 6.0.4) · **Collection** 13

For all sufficiently large n, let H be an n-vertex 2-factor with r odd cycles. Must every collection G_1,…,G_n on a common n-vertex set, with δ(G_i)≥(n+r)/2 for every i, contain a transversal H?

**Context.** Origin for questions 1256, 1257: Advisor: Peter Keevash. Thesis-proposed transversal versions of older uncolored targets. Setup for questions 1256, 1257: All graphs are finite and simple. A transversal H in G_1,…,G_e(H) is a copy of H with a bijection φ:E(H)→[e(H)] satisfying e∈E(G_φ(e)).

**Source.** Yangyang Cheng. *Absorptions in Combinatorics*. 2024. [primary source](https://ora.ox.ac.uk/objects/uuid%3A81d1d1e1-e022-473f-b39d-ccf0bd07ec94/files/d9z903052s) Location: Problem 6.0.4, p.156.

**Literature check.** Status for questions 1256, 1257, checked 6 October 2026: Checked 2026-10-06: later approximate and separable embedding results do not settle these exact thresholds.

**Further links.** [1](https://doi.org/10.1016/j.jctb.2025.10.004) · [2](https://oro.open.ac.uk/106690/8/106690.pdf) · [3](https://arxiv.org/abs/2409.20535)


<a id="q1257"></a>

## Q1257. The transversal bounded-degree embedding threshold

**Status:** Open · **Kind:** open problem (Problem 6.0.5) · **Collection** 13

For every fixed integer r≥1 and all sufficiently large n, if H has n vertices and Δ(H)≤r, must every collection G_1,…,G_e(H) on a common n-vertex set with δ(G_i)≥(rn−1)/(r+1) contain a transversal H?

**Context.** Origin for questions 1256, 1257: Advisor: Peter Keevash. Thesis-proposed transversal versions of older uncolored targets. Setup for questions 1256, 1257: All graphs are finite and simple. A transversal H in G_1,…,G_e(H) is a copy of H with a bijection φ:E(H)→[e(H)] satisfying e∈E(G_φ(e)).

**Source.** Yangyang Cheng. *Absorptions in Combinatorics*. 2024. [primary source](https://ora.ox.ac.uk/objects/uuid%3A81d1d1e1-e022-473f-b39d-ccf0bd07ec94/files/d9z903052s) Location: Problem 6.0.5, p.156.

**Literature check.** Status for questions 1256, 1257, checked 6 October 2026: Checked 2026-10-06: later approximate and separable embedding results do not settle these exact thresholds.

**Further links.** [1](https://doi.org/10.1016/j.jctb.2025.10.004) · [2](https://oro.open.ac.uk/106690/8/106690.pdf) · [3](https://arxiv.org/abs/2409.20535)


<a id="q1258"></a>

## Q1258. No infinite uniquely-Wilf class contains every three-pattern

**Status:** Open · **Kind:** conjecture (Conjecture 8) · **Collection** 13

Is there no infinite permutation class C containing all six length-three permutations such that π∼\_Cτ whenever |π|=|τ|?

**Context.** Doctoral context for question 1258: Jinge Li. Enumerative coincidences in permutation classes. PhD, University of Otago, 2024. Advisor: Michael Albert. Origin for question 1258: Li: Enumerative coincidences in permutation classes, Otago PhD repository 2024 (manuscript 2023), advisor Michael Albert; thesis Conjecture 1. Setup for question 1258: A permutation class C is closed under taking patterns. For π,τ∈C, write π∼\_Cτ if, for every N, equally many length-N members of C avoid π and avoid τ.

**Source.** Michael Albert; Jinge Li. *Uniquely-Wilf classes*. 2019. [primary source](https://arxiv.org/abs/1904.05500) Location: Paper Conjecture 8; thesis Conjecture 1, p.66.

**Literature check.** Status for question 1258, checked 6 October 2026: Checked through 2026-10-06; bounded literature searches found no matching resolution.

**Further links.** [1](https://ourarchive.otago.ac.nz/view/pdfCoverPage?download=true&filePid=13407317960001891&instCode=64OTAGO_INST) · [2](https://dmtcs.episciences.org/5859/pdf) · [3](https://ourarchive.otago.ac.nz/esploro/outputs/doctoral/Enumerative-coincidences-in-permutation-classes/9926541979501891)


<a id="q1259"></a>

## Q1259. Sharp clustering for a bounded-treewidth graph times a path

**Status:** Open · **Kind:** conjecture (Conjecture 7) · **Collection** 13

For every fixed integer c≥2, is there t≥1 such that infinitely many pairs of a treewidth-t graph H and a path P require clustering Ω(|V(H⊠P)|^(c/(c²−c+1))) in every c-coloring?

**Context.** Origin for questions 1259, 1260, 1261: Paper-origin conjectures; no doctoral origin claimed. Setup for questions 1259, 1260, 1261: Clustering is the largest monochromatic connected-component order. ⊠ denotes strong product; N=|V(H_1⊠H_2)|. Each Ω constant may depend on fixed parameters, never N.

**Source.** Rutger Campbell; J. Pascal Gollin; Kevin Hendrey; Thomas Lesgourgues; Bojan Mohar; Youri Tamitegama; Jane Tan; David R. Wood. *Clustered Colouring of Graph Products*. 2025. [primary source](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v32i3p15/pdf/) Location: Conjecture 7, p.4.

**Literature check.** Status for questions 1259, 1260, 1261, checked 6 October 2026: Checked through 2026-10-06; bounded literature searches found no matching resolution.

**Further links.** [1](https://arxiv.org/abs/2407.21360)


<a id="q1260"></a>

## Q1260. The four-sevenths clustering lower bound

**Status:** Open · **Kind:** conjecture (Conjecture 8) · **Collection** 13

Is there t≥1 and infinitely many pairs H_1,H_2 of treewidth t such that every 3-coloring of H_1⊠H_2 has clustering Ω(N^(4/7))?

**Context.** Origin for questions 1259, 1260, 1261: Paper-origin conjectures; no doctoral origin claimed. Setup for questions 1259, 1260, 1261: Clustering is the largest monochromatic connected-component order. ⊠ denotes strong product; N=|V(H_1⊠H_2)|. Each Ω constant may depend on fixed parameters, never N.

**Source.** Rutger Campbell; J. Pascal Gollin; Kevin Hendrey; Thomas Lesgourgues; Bojan Mohar; Youri Tamitegama; Jane Tan; David R. Wood. *Clustered Colouring of Graph Products*. 2025. [primary source](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v32i3p15/pdf/) Location: Conjecture 8, p.4.

**Literature check.** Status for questions 1259, 1260, 1261, checked 6 October 2026: Checked through 2026-10-06; bounded literature searches found no matching resolution.

**Further links.** [1](https://arxiv.org/abs/2407.21360)


<a id="q1261"></a>

## Q1261. Sharp large-color clustering exponent for graph products

**Status:** Open · **Kind:** conjecture (Conjecture 9) · **Collection** 13

For every fixed integer c≥4, do some k and infinitely many treewidth-k pairs H_1,H_2 force clustering Ω(N^(1/((1+o_c(1))√c))) in every c-coloring, with o_c(1)→0 as c→∞?

**Context.** Origin for questions 1259, 1260, 1261: Paper-origin conjectures; no doctoral origin claimed. Setup for questions 1259, 1260, 1261: Clustering is the largest monochromatic connected-component order. ⊠ denotes strong product; N=|V(H_1⊠H_2)|. Each Ω constant may depend on fixed parameters, never N.

**Source.** Rutger Campbell; J. Pascal Gollin; Kevin Hendrey; Thomas Lesgourgues; Bojan Mohar; Youri Tamitegama; Jane Tan; David R. Wood. *Clustered Colouring of Graph Products*. 2025. [primary source](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v32i3p15/pdf/) Location: Conjecture 9, p.4.

**Literature check.** Status for questions 1259, 1260, 1261, checked 6 October 2026: Checked through 2026-10-06; bounded literature searches found no matching resolution.

**Further links.** [1](https://arxiv.org/abs/2407.21360)


<a id="q1262"></a>

## Q1262. Which colored multiset polynomials are s-Eulerian?

**Status:** Open, partial results · **Kind:** open problem (Question 4.1) · **Collection** 13

Characterize all positive integer vectors m,r for which A_m^r equals an s-Eulerian polynomial for some positive integer sequence s of any length.

**Context.** Doctoral context for question 1262: Danai Deligeorgaki. Combinatorics and Algebraic Statistics through Polyhedra. PhD, KTH Royal Institute of Technology, 2025. Advisor: Liam Solus. Origin for questions 1262, 1263: Deligeorgaki: Combinatorics and Algebraic Statistics through Polyhedra, KTH PhD 2025, Paper B′; advisor Liam Solus, coadvisors Katharina Jochemko and Johan Håstad. Setup for questions 1262, 1263: For same-length positive integer vectors m,r, set M=Σm_i and A_m^r(x)=(1−x)^(M+1)Σ\_(t≥0)[∏\_i binom(r_i t+m_i,m_i)]x^t. An s-Eulerian polynomial is the Ehrhart h\*-polynomial of {y:0≤y_1/s_1≤…≤y_l/s_l≤1}, s∈Z_(>0)^l.

**Source.** Danai Deligeorgaki; Bin Han; Liam Solus. *Colored multiset Eulerian polynomials*. 2026. [primary source](https://doi.org/10.5070/C66165697) Location: Final Question 4.1, p.21; preprint Question 22.

**Literature check.** Status for questions 1262, 1263, checked 6 October 2026: Checked 2026-10-06: final paper retains both; Yan’s August 2026 real-rootedness theorem does not resolve them.

**Results.**

- **Partial result**: Finite recognition for arbitrary allowed vector length: enumerate ordered factorizations of N=p(1) with optional unit separators; length at most 2\*Omega(N)-1 suffices. Complete exclusion for multiplicities (2,3). Infinite Pell family: A_(2,b)=E_(b-t+1,1,b+t+1) whenever b(b+1)/2=t^2. Exactly decided 28 bounded-volume uncolored two-symbol cases. Remaining: A general structural classification of colored multiplicity pairs remains unresolved. The source already uses unit-removal and volume factorization in Proposition 25. B3 continuation (7 Oct): B3C-07 Degree-dependent s-Eulerian representation bound; B3C-08 Connected quadratic s-Eulerian inequality; B3C-09 Exact uncoloured multiplicity (2,b) classification; none closes the question. Recorded from the external B3 return  (backfilled 2026-10-08); initial argument review and bounded independent controls in the intake; not independently re-derived here. [Details](../../solutions/b3-2026-10-06/README.md).
- **Related result** (B3C-07: Degree-dependent s-Eulerian representation bound): Every nonconstant s-Eulerian polynomial of integer degree d>=1 has a representing positive integer vector of length at most 2d-1. Limits: Existential bound after deleting units and contracting all-two blocks; all-degree sharpness for (1+ux)^d is not recovered. [Report](../../solutions/b3-continuation-2026-10-07/README.md).
- **Related result** (B3C-08: Connected quadratic s-Eulerian inequality): For every positive integer vector s with all entries >=2, if E_s(x)=1+h_1 x+h_2 x^2 has degree exactly two, then h_1>h_2>0. Limits: Degree-two blocks only; does not establish simple roots for every nonunit block. Exceptional (2,6,3) coefficients corrected to (1,19,16). [Report](../../solutions/b3-continuation-2026-10-07/README.md).
- **Related result** (B3C-09: Exact uncoloured multiplicity (2,b) classification): For every positive integer b, A_(2,b)(x)=1+2b x+binom(b,2)x^2 is s-Eulerian for some positive integer vector of arbitrary length iff b=2 or b(b+1)/2 is an integer square. Limits: Exact subfamily of general coloured multiset question Q1262; not full classification. [Report](../../solutions/b3-continuation-2026-10-07/README.md).

**Further links.** [1](https://arxiv.org/abs/2407.12076) · [2](https://escholarship.org/content/qt135937h5/qt135937h5_noSplash_af6056425c67947c0d921d43ba376183.pdf) · [3](https://arxiv.org/abs/2608.15682) · [4](https://diva-portal.org/smash/get/diva2%3A1961783/FULLTEXT01.pdf) · [5](https://www.kth.se/files/view/danaide/672b8fdbd5a5635b8db995c5/cv-nov-2024.pdf)


<a id="q1263"></a>

## Q1263. Interpret the two gamma vectors of colored multiset polynomials

**Status:** Open · **Kind:** open problem (Question 4.7) · **Collection** 13

When A_m^r=a+xb is bi-γ-positive, give combinatorial interpretations of both γ-vectors: a=Σγ\_i x^i(1+x)^(d−2i), b=Ση\_i x^i(1+x)^(d−1−2i), where d=deg A_m^r and all γ\_i,η\_i≥0.

**Context.** Origin for questions 1262, 1263: Deligeorgaki: Combinatorics and Algebraic Statistics through Polyhedra, KTH PhD 2025, Paper B′; advisor Liam Solus, coadvisors Katharina Jochemko and Johan Håstad. Setup for questions 1262, 1263: For same-length positive integer vectors m,r, set M=Σm_i and A_m^r(x)=(1−x)^(M+1)Σ\_(t≥0)[∏\_i binom(r_i t+m_i,m_i)]x^t. An s-Eulerian polynomial is the Ehrhart h\*-polynomial of {y:0≤y_1/s_1≤…≤y_l/s_l≤1}, s∈Z_(>0)^l.

**Source.** Danai Deligeorgaki; Bin Han; Liam Solus. *Colored multiset Eulerian polynomials*. 2026. [primary source](https://doi.org/10.5070/C66165697) Location: Final Question 4.7, p.23; preprint Question 26.

**Literature check.** Status for questions 1262, 1263, checked 6 October 2026: Checked 2026-10-06: final paper retains both; Yan’s August 2026 real-rootedness theorem does not resolve them.

**Results.**

- **Investigated, unresolved** (B3: submitted unresolved): Exact symmetric decomposition and gamma conversion implemented. Closed gamma formulas for two singleton symbols with color counts u,v>=2. Remaining/limits: No general combinatorial interpretation of both gamma vectors. [Report](../../solutions/b3-2026-10-06/README.md).

**Further links.** [1](https://arxiv.org/abs/2407.12076) · [2](https://escholarship.org/content/qt135937h5/qt135937h5_noSplash_af6056425c67947c0d921d43ba376183.pdf) · [3](https://arxiv.org/abs/2608.15682) · [4](https://diva-portal.org/smash/get/diva2%3A1961783/FULLTEXT01.pdf) · [5](https://www.kth.se/files/view/danaide/672b8fdbd5a5635b8db995c5/cv-nov-2024.pdf)


<a id="q1264"></a>

## Q1264. Optimal three-color clustering for planar graphs

**Status:** Open · **Kind:** open problem · **Collection** 13

Determine the asymptotic order of f_3(n), the least k such that every n-vertex planar graph admits a vertex 3-coloring whose monochromatic connected components each have at most k vertices.

**Context.** Origin for question 1264: Older clustered-coloring question, sharpened by this paper; no doctoral origin claimed.

**Source.** Vida Dujmović; Pat Morin; Sergey Norin; David R. Wood. *3-Colouring Planar Graphs*. 2025. [primary source](https://arxiv.org/abs/2507.03163) Location: §1, definition and open c=3 case; Theorem 1.

**Literature check.** Status for question 1264, checked 6 October 2026: Checked 2026-10-06: July 2026 revision leaves Ω(n^(1/3)) versus O(n^(4/9)); later minor-free extension does not close the gap.

**Further links.** [1](https://arxiv.org/html/2507.03163v2) · [2](https://arxiv.org/abs/2607.02159)


<a id="q1265"></a>

## Q1265. Max-lex minimizes generated unions

**Status:** Open · **Kind:** conjecture (Conjecture 11) · **Collection** 13

Order k-subsets of positive integers by A&lt;B when max A&lt;max B, or when their maxima agree and min(A△B)∈A. For every k≥1 and finite family A of k-sets, does the equal-size initial segment B minimize the number of distinct nonempty unions, so |〈A〉|≥|〈B〉|?

**Context.** Doctoral context for question 1265: Žarko Ranđelović. Some Results in Combinatorics and Combinatorial Geometry. PhD, University of Cambridge, 2024. Advisor: Imre Leader. Origin for question 1265: Roberts’s 1999 conjecture, restated in Ranđelović’s Cambridge PhD (2024, supervisor Imre Leader), §2.3.

**Source.** Žarko Ranđelović. *Minimizing the Number of Unions*. 2026. [primary source](https://doi.org/10.37236/13702) Location: Conjecture 11, p.14.

**Literature check.** Status for question 1265, checked 6 October 2026: March 2026 journal version retains the general conjecture; no later resolution located.

**Further links.** [1](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v33i1p47/pdf/) · [2](https://arxiv.org/abs/2306.04115) · [3](https://api.repository.cam.ac.uk/server/api/core/bitstreams/834c439d-aab8-405d-a636-4db2d49e600b/content) · [4](https://www.mi.sanu.ac.rs/novi_sajt/members/fulltime/cv/zrandjelovic.pdf)


<a id="q1266"></a>

## Q1266. Optimal duration of the transversal achievement game

**Status:** Open · **Kind:** conjecture (Conjecture 14) · **Collection** 13

Two players alternately claim empty cells of an n×n board; the first to own a set of n cells, one in each row and column, wins. For every n≥4, can the second player prevent a first-player win before ply 2n+3, regardless of the first player’s strategy?

**Context.** Origin for question 1266: Paper-origin Conjecture 14; no doctoral origin claimed.

**Source.** Kevin Guan. *The transversal achievement game on a square grid*. 2026. [primary source](https://arxiv.org/abs/2608.13501) Location: §7, Conjecture 14, p.14.

**Literature check.** Status for question 1266, checked 6 October 2026: August 2026 paper leaves optimality open; no later resolution located.


<a id="q1267"></a>

## Q1267. Finish Erickson’s exact-color spectrum conjecture

**Status:** Open · **Kind:** open problem · **Collection** 13

For every pair of integers c>m≥3, is there an edge-coloring of the countably infinite complete graph using exactly c colors such that no induced complete subgraph on an infinite vertex set uses exactly m colors?

**Context.** Origin for question 1267: Erickson’s conjecture; finite unresolved remainder after this paper.

**Source.** Žarko Ranđelović. *Exactly Colored Complete Subgraphs of Infinite Graphs*. 2025. [primary source](https://arxiv.org/abs/2512.04233) Location: §1, p.1, statement of P(c,m); final paragraph p.8.

**Literature check.** Status for question 1267, checked 6 October 2026: Checked 2026-10-06: no resolution located in bounded searches.


<a id="q1268"></a>

## Q1268. Classify polynomial classes with uniformly bounded Wilf complexity

**Status:** Open · **Kind:** open problem · **Collection** 13

Classify the permutation classes C of polynomial growth |C∩S_n|=O(n^d) for some d, for which some constant K bounds the number of ∼\_C-equivalence classes in C∩S_n for every n.

**Context.** Doctoral context for question 1268: see question 1258. Origin for question 1268: Advisor: Michael Albert. Thesis §4.8 future-work target. Setup for question 1268: A permutation class C is closed under taking patterns. For π,τ∈C, write π∼\_Cτ if, for every N, equally many length-N members of C avoid π and avoid τ.

**Source.** Jinge Li. *Enumerative coincidences in permutation classes*. 2024. [primary source](https://ourarchive.otago.ac.nz/view/pdfCoverPage?download=true&filePid=13407317960001891&instCode=64OTAGO_INST) Location: §4.8, p.120; definitions §4.2, pp.69–71.

**Literature check.** Status for question 1268, checked 6 October 2026: Checked through 2026-10-06; bounded literature searches found no matching resolution.

**Further links.** [1](https://ourarchive.otago.ac.nz/esploro/outputs/doctoral/Enumerative-coincidences-in-permutation-classes/9926541979501891)


<a id="q1351"></a>

## Q1351. Well-quasi-order finite-bag graphs

**Status:** Open · **Kind:** conjecture (Conjecture 1.5) · **Collection** 14

In every infinite sequence G₁,G₂,… of graphs admitting tree-decompositions into finite bags, must some G_i be a minor of G_j with i&lt;j?

**Context.** Doctoral context for question 1351: Paul Knappe. Graph-decompositions: Trees, Tangles and Locality. PhD, University of Hamburg, 2025. Advisor: Reinhard Diestel. Origin for question 1351: Authors’ conjecture strengthening Thomas’s problem; thesis Conjecture 7.1.5. Setup for question 1351: A tree-decomposition covers all vertices and edges by bags indexed by a tree, with the bags containing each vertex forming a connected subtree. Bags below are finite but need not have uniformly bounded size.

**Source.** Sandra Albrechtsen; Raphael W. Jacobs; Paul Knappe; Max Pitz. *Linked tree-decompositions into finite parts*. 2024. [primary source](https://arxiv.org/abs/2405.06753) Location: Conjecture 1.5, p. 7.

**Literature check.** Status for question 1351, checked 6 October 2026: Checked 2026-10-06: retained in 2025 thesis; no matching resolution located.

**Further links.** [1](https://ediss.sub.uni-hamburg.de/bitstream/ediss/11927/1/Dissertation.pdf) · [2](https://www.paulknappe.de/summaries/linked-lean-tds) · [3](https://www.paulknappe.de/)


<a id="q1352"></a>

## Q1352. Induce tangles by vertex sets

**Status:** Open · **Kind:** open problem (Problem 1.1) · **Collection** 14

For every finite graph G, positive integer k and k-tangle τ, is there X⊆V(G) with |X∩A|<|X∩B| for every (A,B)∈τ?

**Context.** Doctoral context for question 1352: see question 1351. Origin for question 1352: Origin: Diestel–Hundertmark–Lemanczyk; thesis Problem 10.1.1. Setup for question 1352: For finite G, a k-tangle τ orients every vertex separation {A,B} of order |A∩B|&lt;k, with A∪B=V(G) and no edge between A\B and B\A, so that no three small-side induced subgraphs G[A] cover G.

**Source.** Sandra Albrechtsen; Hanno von Bergen; Raphael W. Jacobs; Paul Knappe; Paul Wollan. *On vertex sets inducing tangles*. 2024. [primary source](https://arxiv.org/abs/2411.13656) Location: Problem 1.1, p. 1.

**Literature check.** Status for question 1352, checked 6 October 2026: Checked 2026-10-06: weighted and small-order cases established; general set version unresolved in sources.

**Further links.** [1](https://ediss.sub.uni-hamburg.de/bitstream/ediss/11927/1/Dissertation.pdf) · [2](https://doi.org/10.19086/aic.13691) · [3](https://www.paulknappe.de/)


<a id="q1353"></a>

## Q1353. Decompose every odd-regular orientation

**Status:** Open · **Kind:** conjecture (Conjecture 1.2) · **Collection** 14

For every odd positive integer d and every orientation D of a d-regular graph, can E(D) be partitioned into exactly ex(D) directed paths?

**Context.** Doctoral context for question 1353: Mehmet Akif Yıldız. Cycle partitions and path decompositions in directed graphs. PhD, University of Amsterdam, 2025. Advisor: Joanna A. Ellis-Monaghan. Origin for question 1353: Origin: Pullman, through Reid–Wayland (1987); thesis Conjecture 2.1.2. Setup for question 1353: Graphs are finite/simple. For an orientation D, ex(D)=½Σ\_v|d⁺(v)−d⁻(v)|. A path decomposition partitions its directed edges into directed paths.

**Source.** Viresh Patel; Mehmet Akif Yıldız. *Path decompositions of oriented graphs*. 2026. [primary source](https://doi.org/10.1016/j.ejc.2026.104346) Location: Conjecture 1.2.

**Literature check.** Status for question 1353, checked 6 October 2026: Checked 2026-10-06: final paper resolves random/high-girth cases, not all regular graphs.

**Further links.** [1](https://ir.cwi.nl/pub/36262/36262.pdf) · [2](https://pure.uva.nl/ws/files/234210831/Thesis.pdf) · [3](https://www.dare.uva.nl/id/d749e03d-5127-4544-b659-4ecad57ae856) · [4](https://www.uva.nl/shared-content/uva/en/events/2025/06/cycle-partitions-and-path-decompositions-in-directed-graphs.html)


<a id="q1354"></a>

## Q1354. Partition regular digraphs into paths

**Status:** Open · **Kind:** conjecture (Conjecture 1.6) · **Collection** 14

For every d-regular n-vertex digraph G, is π(G)≤n/(d+1), with the stronger π(G)≤n/(2d+1) whenever G is oriented?

**Context.** Doctoral context for question 1354: see question 1353. Origin for question 1354: Authors’ extension of Magnant–Martin; thesis Conjecture 5.1.6. Setup for question 1354: Digraphs are finite and loopless with no repeated arcs. d-regular means every indegree and outdegree equals d; oriented means no pair of opposite arcs. π(G) is the minimum number of vertex-disjoint directed paths partitioning V(G), allowing singleton paths.

**Source.** Allan Lo; Viresh Patel; Mehmet Akif Yıldız. *Cycle Partitions in Dense Regular Digraphs and Oriented Graphs*. 2025. [primary source](https://doi.org/10.1017/fms.2025.28) Location: Conjecture 1.6.

**Literature check.** Status for question 1354, checked 6 October 2026: Checked 2026-10-06: dense and small-degree cases known; full conjecture retained.

**Further links.** [1](https://arxiv.org/abs/2309.11677) · [2](https://math.gatech.edu/seminars-colloquia/series/combinatorics-seminar/akif-yildiz-20260424) · [3](https://pure.uva.nl/ws/files/234210831/Thesis.pdf) · [4](https://www.dare.uva.nl/id/d749e03d-5127-4544-b659-4ecad57ae856) · [5](https://www.uva.nl/shared-content/uva/en/events/2025/06/cycle-partitions-and-path-decompositions-in-directed-graphs.html)


<a id="q1355"></a>

## Q1355. Bound periodic chromatic cost

**Status:** Open · **Kind:** open problem (Problem 4.9) · **Collection** 14

Does some function f:N→N guarantee that every locally finite graph G admitting a periodic proper vertex-coloring admits one using at most f(χ(G)) colors?

**Context.** Origin for questions 1355, 1356, 1357: Authors’ questions; equivalent edge-coloring formulations merged. Setup for questions 1355, 1356, 1357: A graph is quasi-transitive if its automorphism group has finitely many vertex orbits. A coloring or spanning subgraph is periodic if its preserving automorphisms have finitely many vertex orbits. All graphs here are locally finite.

**Source.** Tara Abrishami; Louis Esperet; Ugo Giocanti; Matthias Hamann; Paul Knappe; Rögnvaldur G. Möller. *Periodic colorings and orientations in infinite graphs*. 2025. [primary source](https://doi.org/10.5070/C65465671) Location: Problem 4.9.

**Literature check.** Status for questions 1355, 1356, 1357, checked 6 October 2026: Checked 2026-10-06: these survive the 2026 solution of separate planar Problem 6.6.

**Further links.** [1](https://arxiv.org/abs/2411.01951) · [2](https://arxiv.org/abs/2604.22705) · [3](https://iris.hi.is/en/publications/periodic-colorings-and-orientations-in-infinite-graphs/)


<a id="q1356"></a>

## Q1356. Find nontrivial periodic edge colorings

**Status:** Open · **Kind:** open problem (Problem 6.2) · **Collection** 14

Must every locally finite quasi-transitive graph having a component with at least two edges admit a periodic two-edge-coloring that is nonconstant on some component?

**Context.** Origin for questions 1355, 1356, 1357: Authors’ questions; equivalent edge-coloring formulations merged. Setup for questions 1355, 1356, 1357: A graph is quasi-transitive if its automorphism group has finitely many vertex orbits. A coloring or spanning subgraph is periodic if its preserving automorphisms have finitely many vertex orbits. All graphs here are locally finite.

**Source.** Tara Abrishami; Louis Esperet; Ugo Giocanti; Matthias Hamann; Paul Knappe; Rögnvaldur G. Möller. *Periodic colorings and orientations in infinite graphs*. 2025. [primary source](https://doi.org/10.5070/C65465671) Location: Problem 6.2 (equivalently 6.1/6.3).

**Literature check.** Status for questions 1355, 1356, 1357, checked 6 October 2026: Checked 2026-10-06: these survive the 2026 solution of separate planar Problem 6.6.

**Further links.** [1](https://arxiv.org/abs/2411.01951) · [2](https://arxiv.org/abs/2604.22705) · [3](https://iris.hi.is/en/publications/periodic-colorings-and-orientations-in-infinite-graphs/)


<a id="q1357"></a>

## Q1357. Find periodic two-factors

**Status:** Open · **Kind:** open problem (Problem 6.5) · **Collection** 14

Does every infinite 4-regular vertex-transitive graph have a periodic spanning subgraph in which every vertex has degree 2?

**Context.** Origin for questions 1355, 1356, 1357: Authors’ questions; equivalent edge-coloring formulations merged. Setup for questions 1355, 1356, 1357: A graph is quasi-transitive if its automorphism group has finitely many vertex orbits. A coloring or spanning subgraph is periodic if its preserving automorphisms have finitely many vertex orbits. All graphs here are locally finite.

**Source.** Tara Abrishami; Louis Esperet; Ugo Giocanti; Matthias Hamann; Paul Knappe; Rögnvaldur G. Möller. *Periodic colorings and orientations in infinite graphs*. 2025. [primary source](https://doi.org/10.5070/C65465671) Location: Problem 6.5.

**Literature check.** Status for questions 1355, 1356, 1357, checked 6 October 2026: Checked 2026-10-06: these survive the 2026 solution of separate planar Problem 6.6.

**Further links.** [1](https://arxiv.org/abs/2411.01951) · [2](https://arxiv.org/abs/2604.22705) · [3](https://iris.hi.is/en/publications/periodic-colorings-and-orientations-in-infinite-graphs/)


<a id="q1358"></a>

## Q1358. Recognize defective queue layouts

**Status:** Open · **Kind:** open problem · **Collection** 14

For fixed k,h≥1, determine the complexity of recognizing graphs admitting k-defective h-queue layouts, with the vertex order to be chosen.

**Context.** Origin for question 1358: Authors’ OP4. Setup for question 1358: A k-defective h-stack/queue layout orders a finite simple graph’s vertices and partitions edges into h pages. Each edge crosses/nests with at most k independent same-page edges, respectively; crossings have alternating endpoints, nesting means strict interval containment.

**Source.** Michael A. Bekos; Carla Binucci; Emilio Di Giacomo; Walter Didimo; Luca Grilli; Maria Eleni Pavlidi; Alessandra Tappini; Alexandra Weinberger. *Stack and Queue Layouts with Defects*. 2026. [primary source](https://arxiv.org/abs/2607.19968) Location: OP4.

**Literature check.** Status for question 1358, checked 6 October 2026: Checked 2026-10-06: retained in July full paper; no later resolution located.

**Further links.** [1](https://www.fernuni-hagen.de/ti/forschung/publikationen/bbdgdgpw26.shtml)


<a id="q1359"></a>

## Q1359. Linear pathwidth from edge covers

**Status:** Open · **Kind:** open problem (Question 37) · **Collection** 14

If G is edge-covered by k shortest paths, must pw(G)=O(k)? Does the sharper bound pw(G)≤k always hold?

**Context.** Origin for questions 1359, 1360, 1361: Sharp edge target: authors; other two continue Dumas et al. (2024). Setup for questions 1359, 1360, 1361: Graphs are finite, simple and unweighted. Covers may overlap. Shortest means shortest between the path’s own endpoints. pw(G) denotes pathwidth.

**Source.** Julien Baste; Lucas De Meyer; Ugo Giocanti; Etienne Objois; Timothé Picavet. *A Polynomial Bound on the Pathwidth of Graphs Edge-Coverable by k Shortest Paths*. 2026. [primary source](https://doi.org/10.4230/LIPIcs.STACS.2026.10) Location: Question 37; full-version Question 6.1.

**Literature check.** Status for questions 1359, 1360, 1361, checked 6 October 2026: Checked 2026-10-06: current final/version 2 retains these; isometric-tree variants separately resolved.

**Further links.** [1](https://arxiv.org/abs/2510.02901) · [2](https://arxiv.org/abs/2511.03524) · [3](https://doi.org/10.1016/j.tcs.2026.115910)


<a id="q1360"></a>

## Q1360. Polynomial pathwidth from vertex covers

**Status:** Open · **Kind:** open problem (Question 37) · **Collection** 14

Does some polynomial p satisfy pw(G)≤p(k) for every graph whose vertices are covered by k shortest paths?

**Context.** Origin for questions 1359, 1360, 1361: Sharp edge target: authors; other two continue Dumas et al. (2024). Setup for questions 1359, 1360, 1361: Graphs are finite, simple and unweighted. Covers may overlap. Shortest means shortest between the path’s own endpoints. pw(G) denotes pathwidth.

**Source.** Julien Baste; Lucas De Meyer; Ugo Giocanti; Etienne Objois; Timothé Picavet. *A Polynomial Bound on the Pathwidth of Graphs Edge-Coverable by k Shortest Paths*. 2026. [primary source](https://doi.org/10.4230/LIPIcs.STACS.2026.10) Location: §6, paragraph after Question 37.

**Literature check.** Status for questions 1359, 1360, 1361, checked 6 October 2026: Checked 2026-10-06: current final/version 2 retains these; isometric-tree variants separately resolved.

**Further links.** [1](https://arxiv.org/abs/2510.02901) · [2](https://arxiv.org/abs/2511.03524) · [3](https://doi.org/10.1016/j.tcs.2026.115910)


<a id="q1361"></a>

## Q1361. Fixed-parameter isometric path cover

**Status:** Open · **Kind:** open problem · **Collection** 14

Can deciding whether an n-vertex graph is vertex-covered by at most k shortest paths, without prescribed endpoints, be solved in f(k)n^O(1) time?

**Context.** Origin for questions 1359, 1360, 1361: Sharp edge target: authors; other two continue Dumas et al. (2024). Setup for questions 1359, 1360, 1361: Graphs are finite, simple and unweighted. Covers may overlap. Shortest means shortest between the path’s own endpoints. pw(G) denotes pathwidth.

**Source.** Julien Baste; Lucas De Meyer; Ugo Giocanti; Etienne Objois; Timothé Picavet. *A Polynomial Bound on the Pathwidth of Graphs Edge-Coverable by k Shortest Paths*. 2026. [primary source](https://doi.org/10.4230/LIPIcs.STACS.2026.10) Location: §1, Algorithmic motivations.

**Literature check.** Status for questions 1359, 1360, 1361, checked 6 October 2026: Checked 2026-10-06: current final/version 2 retains these; isometric-tree variants separately resolved.

**Further links.** [1](https://arxiv.org/abs/2510.02901) · [2](https://arxiv.org/abs/2511.03524) · [3](https://doi.org/10.1016/j.tcs.2026.115910)


<a id="q1362"></a>

## Q1362. Bound basis number by clique-width

**Status:** Open · **Kind:** open problem · **Collection** 14

Does a function f exist with bn(G)≤f(cw(G)) for every finite graph G, where cw denotes clique-width?

**Context.** Origin for questions 1362, 1363: Authors’ §8.2 questions. Setup for questions 1362, 1363: For finite simple G, bn(G) is the least maximum edge multiplicity in a cycle family generating its F₂-cycle space. Adhesion bounds adjacent-bag intersections; a torso completes each adjacent-bag intersection to a clique. Hereditary means closed under induced subgraphs.

**Source.** Colin Geniet; Ugo Giocanti. *Basis Number of Graphs Excluding Minors*. 2026. [primary source](https://arxiv.org/abs/2601.05195) Location: §8.2, Hereditary classes.

**Literature check.** Status for questions 1362, 1363, checked 6 October 2026: Checked 2026-10-06: February version 3 retains these; polynomial bounds already incorporated.

**Further links.** [1](https://colingeniet.com/publications.html) · [2](https://arxiv.org/abs/2601.14095)


<a id="q1363"></a>

## Q1363. Glue hereditary bounded-basis torsos

**Status:** Open · **Kind:** open problem · **Collection** 14

Is there f(b,k) such that bn(G)≤f(b,k) whenever G has a tree-decomposition of adhesion≤k whose torsos belong to a hereditary class all of whose members have basis number≤b?

**Context.** Origin for questions 1362, 1363: Authors’ §8.2 questions. Setup for questions 1362, 1363: For finite simple G, bn(G) is the least maximum edge multiplicity in a cycle family generating its F₂-cycle space. Adhesion bounds adjacent-bag intersections; a torso completes each adjacent-bag intersection to a clique. Hereditary means closed under induced subgraphs.

**Source.** Colin Geniet; Ugo Giocanti. *Basis Number of Graphs Excluding Minors*. 2026. [primary source](https://arxiv.org/abs/2601.05195) Location: §8.2; modification of Theorem 1.6.

**Literature check.** Status for questions 1362, 1363, checked 6 October 2026: Checked 2026-10-06: February version 3 retains these; polynomial bounds already incorporated.

**Further links.** [1](https://colingeniet.com/publications.html) · [2](https://arxiv.org/abs/2601.14095)


<a id="q1364"></a>

## Q1364. Count monotone-triple-avoiding kings

**Status:** Open · **Kind:** open problem (Problem 1) · **Collection** 14

Determine the enumeration, by length n≥0, of king permutations avoiding 123 (equivalently, avoiding 321).

**Context.** Origin for questions 1364, 1365: Authors’ separate enumeration problems. Setup for questions 1364, 1365: A king permutation σ∈S_n satisfies |σ\_(i+1)−σ\_i|>1 for every adjacent pair. Classical pattern occurrence means a subsequence with the specified relative order. Baxter permutations avoid 2-41-3 and 3-14-2, with the undashed middle entries adjacent.

**Source.** Dan Li; Sergey Kitaev. *King permutations and partially ordered patterns*. 2026. [primary source](https://math.colgate.edu/~integers/aa59/aa59.pdf) Location: Problem 1.

**Literature check.** Status for questions 1364, 1365, checked 6 October 2026: Checked 2026-10-06: retained in May final paper; no subsequent solution located.

**Further links.** [1](https://strathprints.strath.ac.uk/96180/)


<a id="q1365"></a>

## Q1365. Count Baxter kings

**Status:** Open · **Kind:** open problem (Problem 2) · **Collection** 14

Determine the enumeration, by length n≥0, of Baxter king permutations.

**Context.** Origin for questions 1364, 1365: Authors’ separate enumeration problems. Setup for questions 1364, 1365: A king permutation σ∈S_n satisfies |σ\_(i+1)−σ\_i|>1 for every adjacent pair. Classical pattern occurrence means a subsequence with the specified relative order. Baxter permutations avoid 2-41-3 and 3-14-2, with the undashed middle entries adjacent.

**Source.** Dan Li; Sergey Kitaev. *King permutations and partially ordered patterns*. 2026. [primary source](https://math.colgate.edu/~integers/aa59/aa59.pdf) Location: Problem 2.

**Literature check.** Status for questions 1364, 1365, checked 6 October 2026: Checked 2026-10-06: retained in May final paper; no subsequent solution located.

**Further links.** [1](https://strathprints.strath.ac.uk/96180/)


<a id="q1366"></a>

## Q1366. Unimodality of pattern intervals

**Status:** Open · **Kind:** conjecture (Conjecture 9.4) · **Collection** 14

For every interval [σ,τ], is (a₀,…,a_(|τ|−|σ|)) unimodal, meaning weakly increasing up to some index and weakly decreasing thereafter?

**Context.** Origin for question 1366: Original Conjecture 9.4; reaffirmed by Vatter (2026), Conjecture 2.2. Setup for question 1366: Order permutations by classical pattern containment: σ≤τ means τ has a subsequence order-isomorphic to σ. For σ≤τ, let a_r count distinct length-|σ|+r permutations in [σ,τ].

**Source.** Peter R. W. McNamara; Einar Steingrímsson. *On the topology of the permutation pattern poset*. 2015. [primary source](https://doi.org/10.1016/j.jcta.2015.02.009) Location: Conjecture 9.4.

**Literature check.** Status for question 1366, checked 6 October 2026: Checked 2026-10-06: explicit 2026 reaffirmation; consecutive-pattern theorem does not apply.

**Results.**

- **Investigated, unresolved** (B3: submitted unresolved): All 200523 classical-pattern intervals with nonempty bottom and top length<=7 are unimodal; 206436 if the empty bottom is included. Literal subset enumeration independently checks downsets through length5. Remaining/limits: The infinite interval conjecture remains unresolved. The rank vector (1,2,5,5,1) is a log-concavity failure, not a unimodality failure. [Report](../../solutions/b3-2026-10-06/README.md).

**Further links.** [1](https://arxiv.org/abs/1305.5569) · [2](https://arxiv.org/abs/2602.16355)


<a id="q1367"></a>

## Q1367. A small non-differentially-algebraic class

**Status:** Open · **Kind:** conjecture (Conjecture 5.3) · **Collection** 14

Is F(x) not differentially algebraic?

**Context.** Origin for question 1367: Authors’ Conjecture 5.3; reaffirmed by Vatter 2026, Conjecture 5.8. Setup for question 1367: Let a_n count permutations of [n] avoiding the classical patterns 4123,4231,4312 and F(x)=Σ\_(n≥0)a_n x^n. Differential algebraicity means satisfying a nonzero polynomial equation P(x,F,F′,…,F^(r))=0 over Q.

**Source.** Michael H. Albert; Cheyne Homberger; Jay Pantone; Nathaniel Shar; Vincent Vatter. *Generating Permutations with Restricted Containers*. 2018. [primary source](https://doi.org/10.1016/j.jcta.2018.02.006) Location: Conjecture 5.3.

**Literature check.** Status for question 1367, checked 6 October 2026: Checked 2026-10-06: explicit February 2026 reaffirmation; no subsequent resolution found.

**Further links.** [1](https://arxiv.org/abs/1510.00269) · [2](https://arxiv.org/abs/2602.16355)


<a id="q1451"></a>

## Q1451. Force a triangle from five dense parts

**Status:** Open · **Kind:** open problem · **Collection** 15

Must every finite graph partitioned into five nonempty independent sets V₁,…,V₅ contain a triangle whenever e(V_i,V_j)>|V_i||V_j|/2 for every i≠j?

**Context.** Doctoral context for question 1451: Nicholas Robert Crawford. Extremal Combinatorics and Optimization: The Method and Application of Flag Algebras and Circuits of the Coloring Polytope. PhD, University of Colorado Denver, 2025. Advisors: Steffen Borgwardt; Florian Pfender. Origin for question 1451: Pfender’s conjecture, restated in Crawford’s thesis, Chapter III, p. 50.

**Source.** Florian Pfender. *Complete subgraphs in multipartite graphs*. 2012. [primary source](https://www.math.uni-rostock.de/~pfender/papers/18.pdf) Location: §1, conjecture immediately before Theorem 4, p. 2.

**Literature check.** Status for question 1451, checked 6 October 2026: Checked 2026-10-06: the 2025 thesis retains it; no matching resolution located.

**Further links.** [1](https://arxiv.org/abs/0910.1447) · [2](https://digital.auraria.edu/downloads/2c0n5-qkt30/Crawford_ucdenver_0765D_12005.pdf) · [3](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v31i4p51/pdf/)


<a id="q1452"></a>

## Q1452. Exclude sparse minimal treewidth classes

**Status:** Open · **Kind:** conjecture (Conjecture 1.5) · **Collection** 15

Does every hereditary class of unbounded treewidth whose members have uniformly bounded arboricity contain no minimal hereditary subclass of unbounded treewidth?

**Context.** Doctoral context for question 1452: Daniel Cocks. Minimal hereditary graph classes of unbounded clique-width. PhD, The Open University, 2024. Advisor: Robert Brignall. Origin for question 1452: Cocks’s paper conjecture, repeated in his thesis as Conjecture 1.31. Setup for question 1452: A class is hereditary if closed under induced subgraphs. Minimal unbounded treewidth means unbounded treewidth with every proper hereditary subclass of bounded treewidth. Arboricity is the fewest forests covering the edges.

**Source.** Daniel Cocks. *t-sails and sparse hereditary classes of unbounded tree-width*. 2024. [primary source](https://oro.open.ac.uk/98017/2/98017.pdf) Location: Conjecture 1.5, p. 4; thesis Conjecture 1.31, p. 22.

**Literature check.** Status for question 1452, checked 6 October 2026: Checked 2026-10-06: also retained in current Hajebi arXiv:2510.19120; no resolution located.

**Further links.** [1](https://oro.open.ac.uk/99116/1/Thesis_DCocks_05-08-24.pdf) · [2](https://arxiv.org/abs/2510.19120) · [3](https://www.rbrignall.org.uk/)


<a id="q1453"></a>

## Q1453. Realize every six-net uniquely

**Status:** Open · **Kind:** open problem · **Collection** 15

Does every 6-net have an undented Euclidean realization by unit equilateral triangular faces, unique up to ambient isometry?

**Context.** Doctoral context for question 1453: Matthew Ellison. Simplicial Decomposition and Realization. PhD, Dartmouth College, 2025. Advisor: Peter Doyle. Origin for question 1453: Joint post-thesis conjectures; not claimed to originate in Ellison’s dissertation. Setup for question 1453: A 6-net is a simplicial triangulation of S² with vertex degrees ≤6. Undented means every vertex has a local support plane. Allow flat doubled-triangular-lattice “pancake” limits of embedded realizations. Neoconvex means undented with nonnegative intrinsic angle defects.

**Source.** Peter Doyle; Matthew Ellison. *Neoplatonic solids*. 2026. [primary source](https://arxiv.org/abs/2607.26363) Location: §2, Neoplatonic Conjecture.

**Literature check.** Status for question 1453, checked 6 October 2026: Checked 2026-10-06: v1 retains both; Euclidean existence is certified through 50 vertices, not general uniqueness.

**Further links.** [1](https://arxiv.org/html/2607.26363v1) · [2](https://digitalcommons.dartmouth.edu/dissertations/401/) · [3](https://math.dartmouth.edu/~mellison/)


<a id="q1454"></a>

## Q1454. Realize avoidance counts as moments

**Status:** Open · **Kind:** open problem · **Collection** 15

For every permutation β of length at least two, let a_n count permutations of [n] with no subsequence order-isomorphic to β, including a₀=1. Does some nonnegative Borel measure μ on [0,∞) satisfy a_n=∫xⁿ dμ(x) for every n≥0?

**Context.** Doctoral context for question 1454: Andrew Elvey Price. Selected problems in enumerative combinatorics: permutation classes, random walks and planar maps. PhD, University of Melbourne, 2018. Advisor: Anthony J. Guttmann. Origin for question 1454: Elvey Price’s 2018 doctoral question, p. 227; restated in this paper and Vatter 2026, Question 2.7.

**Source.** Alin Bostan; Andrew Elvey Price; Anthony John Guttmann; Jean-Marie Maillard. *Stieltjes moment sequences for pattern-avoiding permutations*. 2020. [primary source](https://arxiv.org/abs/2001.00393) Location: §4.2, Remark 1, unnumbered Open question, printed p. 40 in arXiv v3.

**Literature check.** Status for question 1454, checked 6 October 2026: Checked 2026-10-06: explicitly reaffirmed in Vatter’s v2; no matching resolution located.

**Results.**

- **Investigated, unresolved** (B3: submitted unresolved): Known Catalan and finite-atomic moment cases supply explicit nonnegative measures and exact PSD/rank controls for the toolkit. Remaining/limits: No general principal-pattern avoidance moment theorem. These are calibration cases, not claimed new family results. [Report](../../solutions/b3-2026-10-06/README.md).

**Further links.** [1](https://doi.org/10.37236/9402) · [2](https://arxiv.org/abs/2602.16355) · [3](https://hdl.handle.net/11343/219277) · [4](https://www.idpoisson.fr/elveyprice/en/) · [5](https://ms.unimelb.edu.au/__data/assets/pdf_file/0004/3265447/Issue-14-January-2020.pdf)


<a id="q1455"></a>

## Q1455. Sharp hypergraph connectivity threshold

**Status:** Open · **Kind:** conjecture (Conjecture 9.1) · **Collection** 15

Fix integers k≥r≥3. For all sufficiently large n, must every n-vertex r-uniform hypergraph H with no (k+1)-connected subhypergraph satisfy e(H)≤binom(n,r)−binom(n−k,r)+(n/k−2)binom(k,r)?

**Context.** Origin for question 1455: v2 attributes the hypergraph conjecture to Tian–Lai–Meng (2019), Conjecture 2; do not attribute its invention to the 2026 authors. Setup for question 1455: Hypergraph paths join consecutive vertices lying in a common edge. Vertex deletion removes incident edges; (k+1)-connectivity means connectivity survives deletion of any k vertices.

**Source.** Jie Ma; Shengjie Xie; Zhiheng Zheng. *Hypergraphs without Subgraphs of Given Connectivity*. 2026. [primary source](https://arxiv.org/abs/2604.17038) Location: Conjecture 9.1, §9.

**Literature check.** Status for question 1455, checked 6 October 2026: Checked 2026-10-06: July 2026 v2 retains the exact bound; its leading-term theorem leaves an O(n) gap.

**Further links.** [1](https://arxiv.org/html/2604.17038v2)


<a id="q1456"></a>

## Q1456. Diameter bound for multiset tree dimension

**Status:** Open · **Kind:** conjecture (Conjecture 2) · **Collection** 15

Must every finite tree T with mdim(T)<∞ satisfy mdim(T)≤|V(T)|−diam(T)+1?

**Context.** Origin for question 1456: Authors’ Conjecture 2, not their older general-graph conjecture. Setup for question 1456: For a finite connected graph G, mdim(G) is the least |S| for which the multisets {d(v,s):s∈S} differ for every two vertices v; set mdim(G)=∞ if no such S exists.

**Source.** Yusuf Hafidh; Rizki Kurniawan; Suhadi Saputro; Rinovia Simanjuntak; Steven Tanujaya; Saladin Uttunggadewa. *Multiset Dimensions of Trees*. 2019. [primary source](https://arxiv.org/abs/1908.05879) Location: Conjecture 2, p. 7.

**Literature check.** Status for question 1456, checked 6 October 2026: Checked 2026-10-06: retained as Problem 3 of the July 2026 survey. Allikvere’s general-graph counterexamples do not settle this tree bound.

**Results.**

- **Investigated, unresolved** (B7: submitted unresolved): No new analysis or status promotion in this return. Remaining/limits: not_attempted Intake: Scope and identity checked; no independent proof or renewed literature audit of this question. [Report](../../solutions/b7-2026-10-07/README.md).

**Further links.** [1](https://arxiv.org/abs/2607.10311) · [2](https://arxiv.org/abs/2607.28813)


<a id="q1458"></a>

## Q1458. Finiteness of random multiset dimension

**Status:** Open · **Kind:** open problem · **Collection** 15

For fixed 1/8&lt;x≤1/2 and (n−1)p=nˣ, is mdim(G(n,p)) finite with probability tending to one as n→∞, where each possible edge is independently present with probability p?

**Context.** Origin for question 1458: Authors’ first future-research question in §5. Setup for question 1458: For a finite connected graph G, mdim(G) is the least |S| for which the multisets {d(v,s):s∈S} differ for every two vertices v; set mdim(G)=∞ if no such S exists.

**Source.** Austin Eide; Paweł Prałat. *Multiset Metric Dimension of Binomial Random Graphs*. 2025. [primary source](https://arxiv.org/abs/2507.11686) Location: §5, first proposed direction.

**Literature check.** Status for question 1458, checked 6 October 2026: Checked 2026-10-06: September 2, 2026 v2 still states the question. Finiteness proved for 0&lt;x≤1/8; infinitude for x>1/2.

**Results.**

- **Investigated, unresolved** (B7: submitted unresolved): No new analysis or status promotion in this return. Remaining/limits: not_attempted Intake: Scope and identity checked; no independent proof or renewed literature audit of this question. [Report](../../solutions/b7-2026-10-07/README.md).

**Further links.** [1](https://arxiv.org/html/2507.11686v2)


<a id="q1459"></a>

## Q1459. Polynomially color capped graphs

**Status:** Open · **Kind:** conjecture (Conjecture 1.5) · **Collection** 15

Is there a polynomial p such that χ(G)≤p(ω(G)) for every finite capped graph G?

**Context.** Origin for question 1459: Authors’ Conjecture 1.5 in the expanded journal version (conference version 2021). Setup for question 1459: An ordered graph (G,<) is capped if a&lt;b&lt;c&lt;d and ac,bd∈E(G) imply ad∈E(G).

**Source.** James Davies; Tomasz Krawczyk; Rose McCarty; Bartosz Walczak. *Colouring polygon visibility graphs and their generalizations*. 2023. [primary source](https://ruj.uj.edu.pl/server/api/core/bitstreams/8b9c184a-a38a-465f-b163-b209cedf2ec9/content) Location: Conjecture 1.5, journal p. 271.

**Literature check.** Status for question 1459, checked 6 October 2026: Checked 2026-10-06: later labeling results do not prove a polynomial chromatic bound; no resolution located.

**Further links.** [1](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SoCG.2021.29)


<a id="q1460"></a>

## Q1460. Uniformly reconnect integer flows

**Status:** Open · **Kind:** open problem (Problem 1.2) · **Collection** 15

Does there exist an integer k≥6 such that F(G,k) is connected for every 2-edge-connected G?

**Context.** Origin for question 1460: Authors’ Problems 1.2 and 2.6; v4 has expanded authorship and resolved several earlier questions. Setup for question 1460: Fix an orientation of a finite loopless multigraph G. An integer k-flow conserves flow at vertices and has 0<|f(e)|&lt;k. Two flows are adjacent when their difference is supported on one connected 2-regular subgraph. F(G,k) is this reconfiguration graph; F(G,Z_k) uses nonzero values modulo k.

**Source.** Louis Esperet; Kevin Hendrey; Aurélie Lagoutte; Margaux Marseloo; Sergey Norin; Raphael Steiner. *Nowhere-zero flow reconfiguration*. 2025. [primary source](https://arxiv.org/abs/2512.17342) Location: Problem 1.2; §8 final remarks.

**Literature check.** Status for question 1460, checked 6 October 2026: Checked 2026-10-06: July 2026 v4 retains both. Cranston et al. 2606.24685 reaffirm the modular-lifting question; group connectivity alone does not settle integer flows.

**Further links.** [1](https://arxiv.org/html/2512.17342v4) · [2](https://arxiv.org/abs/2606.24685)


<a id="q1461"></a>

## Q1461. Polynomial vertex-minor Ramsey bound

**Status:** Open · **Kind:** conjecture (Conjecture 1.5) · **Collection** 15

Is R_vm(k) bounded by a polynomial in k, where R_vm(k) is the least n such that every n-vertex graph has the edgeless k-vertex graph as a vertex-minor?

**Context.** Origin for question 1461: Authors’ vertex-minor Ramsey conjecture. Setup for question 1461: A vertex-minor is obtained by deleting vertices and locally complementing neighborhoods (toggling edges among neighbors of a chosen vertex).

**Source.** Ruben Ascoli; Bryce Frederickson; Sarah Frederickson; Caleb McFarland; Logan Post. *Almost All Graphs Are Vertex-Minor Universal*. 2026. [primary source](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.APPROX/RANDOM.2026.38) Location: Conjecture 1.5 (full preprint); conference abstract and introduction.

**Literature check.** Status for question 1461, checked 6 October 2026: Checked 2026-10-06: the September 2026 RANDOM paper explicitly retains it; exact small values do not settle polynomial growth.

**Further links.** [1](https://arxiv.org/abs/2602.09049) · [2](https://arxiv.org/abs/2604.13434)


<a id="q1462"></a>

## Q1462. Force an induced sun

**Status:** Open · **Kind:** open problem (Problem 1) · **Collection** 15

Is there a universal constant c such that every finite triangle-free graph with chromatic number greater than c contains an induced t-sun for some t≥4?

**Context.** Origin for question 1462: Nicolas Trotignon’s question, restated by Hajebi–Spirkl. Setup for question 1462: For t≥4, a t-sun consists of a t-cycle with one new leaf attached to each cycle vertex.

**Source.** Sepehr Hajebi; Sophie Spirkl. *Suns in Triangle-Free Graphs of Large Chromatic Number*. 2026. [primary source](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v33i1p55) Location: Problem 1, §1.

**Literature check.** Status for question 1462, checked 6 October 2026: Checked 2026-10-06: final March 2026 article expressly says it remains open; its bound handles a 4-sun with one leaf missing instead.

**Further links.** [1](https://doi.org/10.37236/14443) · [2](https://arxiv.org/abs/2506.10227)


<a id="q1463"></a>

## Q1463. Deletion-saturate every noncomplete graph

**Status:** Open · **Kind:** conjecture (Conjecture 1.7) · **Collection** 15

For every finite noncomplete graph H, is there a finite graph G with at least one edge and no induced H, such that deleting any edge of G creates an induced H?

**Context.** Origin for question 1463: Joint paper conjecture; also recorded in Sahab Hajebi’s 2025 Waterloo thesis. No doctoral-origin claim is made.

**Source.** Xinyue Fan; Sahab Hajebi; Sepehr Hajebi; Sophie Spirkl. *Asymmetric induced saturation*. 2026. [primary source](https://arxiv.org/abs/2606.24763) Location: Conjecture 1.7, §1.

**Literature check.** Status for question 1463, checked 6 October 2026: Checked 2026-10-06: current v1 states the conjecture, proving it for all noncomplete graphs on at most six vertices and several infinite families; no general resolution located.

**Further links.** [1](https://arxiv.org/html/2606.24763) · [2](https://hdl.handle.net/10012/22753)


<a id="q1464"></a>

## Q1464. Hit maximum stable sets at bounded rank-width

**Status:** Open · **Kind:** open problem (Problem 13) · **Collection** 15

For every integer r, is there a function f_r such that every finite graph G of rank-width at most r has a vertex set of size ≤f_r(ω(G)) meeting every maximum independent set?

**Context.** Origin for questions 1464, 1465, 1466: Questions attributed individually to Xiying Du/Rose McCarty, Julien Codsi, and Michał Pilipczuk.

**Source.** Julien Codsi (collector). *Open Problems for the 2026 Barbados Graph Theory Workshop*. 2026. [primary source](https://web.math.princeton.edu/~pds/barbados26/problems.pdf) Location: Problem 13 (Xiying Du and Rose McCarty).

**Literature check.** Status for questions 1464, 1465, 1466, checked 6 October 2026: Checked 2026-10-06: current workshop list and target searches; no matching resolutions located.


<a id="q1465"></a>

## Q1465. Balance planar graphs with two geodesics

**Status:** Open · **Kind:** open problem (Problem 31) · **Collection** 15

Does every finite planar graph G have two shortest paths whose union S leaves every component of G−S with at most |V(G)|/2 vertices?

**Context.** Origin for questions 1464, 1465, 1466: Questions attributed individually to Xiying Du/Rose McCarty, Julien Codsi, and Michał Pilipczuk.

**Source.** Julien Codsi (collector). *Open Problems for the 2026 Barbados Graph Theory Workshop*. 2026. [primary source](https://web.math.princeton.edu/~pds/barbados26/problems.pdf) Location: Problem 31 (Julien Codsi).

**Literature check.** Status for questions 1464, 1465, 1466, checked 6 October 2026: Checked 2026-10-06: current workshop list and target searches; no matching resolutions located.


<a id="q1466"></a>

## Q1466. Polynomial weak-diameter two-coloring

**Status:** Open · **Kind:** open problem (Problem 28) · **Collection** 15

Is there a polynomial p such that every finite graph G with treewidth at most k admits a two-coloring whose monochromatic connected components have diameter at most p(k), with distances measured in G?

**Context.** Origin for questions 1464, 1465, 1466: Questions attributed individually to Xiying Du/Rose McCarty, Julien Codsi, and Michał Pilipczuk.

**Source.** Julien Codsi (collector). *Open Problems for the 2026 Barbados Graph Theory Workshop*. 2026. [primary source](https://web.math.princeton.edu/~pds/barbados26/problems.pdf) Location: Problem 28 (Michał Pilipczuk).

**Literature check.** Status for questions 1464, 1465, 1466, checked 6 October 2026: Checked 2026-10-06: current workshop list and target searches; no matching resolutions located.


<a id="q1467"></a>

## Q1467. Near-linear two-scale treewidth threshold

**Status:** Open · **Kind:** conjecture (Conjecture 19) · **Collection** 15

For all integers p,q≥1, is ℓ(p,q)=O\*(pq)?

**Context.** Origin for question 1467: Authors’ Conjecture 19; reiterated in Barbados 2026, Problem 11. Setup for question 1467: Let ℓ(p,q) be the least treewidth threshold forcing pairwise vertex-disjoint connected subgraphs, each of treewidth ≥p, whose simultaneous contraction yields a minor of treewidth ≥q. O\* suppresses polylogarithmic factors.

**Source.** Kevin Hendrey; David R. Wood. *Polynomial Bounds in the Apex Minor Theorem*. 2025. [primary source](https://arxiv.org/abs/2503.04228) Location: §7, Conjecture 19.

**Literature check.** Status for question 1467, checked 6 October 2026: Checked 2026-10-06: current primary paper and workshop restatement retain the conjecture; no sharper matching result located.

**Further links.** [1](https://arxiv.org/html/2503.04228) · [2](https://web.math.princeton.edu/~pds/barbados26/problems.pdf)


<a id="q1471"></a>

## Q1471. A linear minimum of distinct abelian squares

**Status:** Open · **Kind:** conjecture (Conjecture 1) · **Collection** 15

Does every binary word of length n contain at least ⌊n/4⌋ distinct abelian-square factors?

**Context.** Origin for question 1471: Conjecture 1 restates Fici–Saarela’s 2014 conjecture. Setup for question 1471: An abelian square is uv with u,v nonempty and having equal letter counts. Distinct factors are counted as strings, not occurrences or Parikh-vector classes.

**Source.** Szilárd Zsolt Fazekas, Adam Mammoliti, Robert Mercaş, Jamie Simpson. *Binary Words Containing Few Abelian Squares*. 2026. [primary source](https://arxiv.org/abs/2604.23188v1) Location: Conjecture 1, p. 1.

**Literature check.** Status for question 1471, checked 6 October 2026: The latest version proves restricted letter-count cases and explicitly retains the general conjecture; no later resolution found.

**Further links.** [1](https://drops.dagstuhl.de/storage/04dagstuhl-reports/volume04/Issue03/DagRep.4.3/DagRep.4.3.pdf)


<a id="q1472"></a>

## Q1472. Exact rich-word repetition thresholds

**Status:** Open · **Kind:** conjecture (Conjecture 3) · **Collection** 15

Is R_d=1+1/(3−λ\_d) for every integer d≥2?

**Context.** Origin for question 1472: Conjecture 3 together with equation (4), specialized to u_(2d−1). Setup for question 1472: A rich infinite word has exactly n+1 distinct palindromic factors, including ε, in each length-n factor. E(w) is the supremum of |v|/per(v) over nonempty factors v, using least period. R_d is the infimum of E(w) over rich words on d letters. Let λ\_d be the unique root in (2,3) of x^(2d−2)(x−2)^2−1=0.

**Source.** Ľubomíra Dvořáková and Edita Pelantová. *The Limit of Repetition Thresholds of Rich Sequences*. 2026. [primary source](https://doi.org/10.37236/14600) Location: Conjecture 3, p. 3; equation (4), p. 5.

**Literature check.** Status for question 1472, checked 6 October 2026: The paper proves lim R_d=2 but leaves this exact formula conjectural. No subsequent resolution located.

**Further links.** [1](https://arxiv.org/abs/2509.06104)


<a id="q1473"></a>

## Q1473. Avoid every nontrivial ternary abelian square

**Status:** Open · **Kind:** open problem (Question 2) · **Collection** 15

Does an infinite word over {0,1,2} exist such that every abelian-square factor belongs to {00,11,22}?

**Context.** Origin for questions 1473, 1474: Ternary-square question is attributed to Mäkelä; the binary-cube question is the authors’ surviving weakened formulation after refuting period-two avoidance. Setup for questions 1473, 1474: An abelian k-power is a concatenation of k nonempty blocks with identical letter-count vectors; their common length is its period.

**Source.** Michaël Rao and Matthieu Rosenfeld. *Avoidability of long k-abelian repetitions*. 2015. [primary source](https://arxiv.org/abs/1507.02581) Location: Question 2, p. 2.

**Literature check.** Status for questions 1473, 1474, checked 6 October 2026: Reaffirmed by Fici–Puzynina’s 2023 survey, Conjecture 20 and Problem 21. No subsequent solution found.

**Further links.** [1](https://arxiv.org/abs/2207.09937)


<a id="q1474"></a>

## Q1474. Bound all binary abelian-cube periods

**Status:** Open · **Kind:** open problem (Question 3) · **Collection** 15

Do an integer p≥1 and an infinite binary word exist with no abelian-cube factor of period at least p?

**Context.** Origin for questions 1473, 1474: Ternary-square question is attributed to Mäkelä; the binary-cube question is the authors’ surviving weakened formulation after refuting period-two avoidance. Setup for questions 1473, 1474: An abelian k-power is a concatenation of k nonempty blocks with identical letter-count vectors; their common length is its period.

**Source.** Michaël Rao and Matthieu Rosenfeld. *Avoidability of long k-abelian repetitions*. 2015. [primary source](https://arxiv.org/abs/1507.02581) Location: Question 3, p. 5.

**Literature check.** Status for questions 1473, 1474, checked 6 October 2026: Reaffirmed by Fici–Puzynina’s 2023 survey, Conjecture 20 and Problem 21. No subsequent solution found.

**Further links.** [1](https://arxiv.org/abs/2207.09937)


<a id="q1475"></a>

## Q1475. An abelian power-or-antipower dichotomy

**Status:** Open · **Kind:** open problem (Problem 14) · **Collection** 15

Must every infinite word over a finite alphabet contain abelian powers of every order or abelian antipowers of every order?

**Context.** Origin for question 1475: Problem 14 is the source’s abelian analogue of the Fici–Restivo–Silva–Zamboni power/antipower theorem. Setup for question 1475: An abelian k-power has k consecutive nonempty blocks with equal letter-count vectors. An abelian k-antipower has k consecutive equal-length blocks with pairwise distinct letter-count vectors.

**Source.** Gabriele Fici and Svetlana Puzynina. *Abelian Combinatorics on Words: a Survey*. 2022. [primary source](https://arxiv.org/abs/2207.09937v2) Location: Problem 14, §4.4, p. 12.

**Literature check.** Status for question 1475, checked 6 October 2026: The survey explicitly leaves the dichotomy open; paperfolding results establish only that special class. No subsequent general result located.

**Further links.** [1](https://doi.org/10.1016/j.cosrev.2022.100532) · [2](https://doi.org/10.1016/j.aam.2019.04.001)


<a id="q1476"></a>

## Q1476. Tangram avoidance within an additive constant

**Status:** Open · **Kind:** open problem (Problem 1) · **Collection** 15

Is there a constant C such that t(k)≤log₂k+C for every integer k≥1?

**Context.** Origin for question 1476: Source Problem 1; the paper proves t(k)=Θ(log k). Setup for question 1476: A tangram is a nonempty word in which every letter count is even. Its cut number is the fewest cuts into nonempty consecutive pieces that can be permuted into two identical words. t(k) is the smallest alphabet size admitting an infinite word without a factor of cut number≤k.

**Source.** Michał Dębski, Jarosław Grytczuk, Bartłomiej Pawlik, Jakub Przybyło, Małgorzata Śleszyńska-Nowak. *Words Avoiding Tangrams*. 2024. [primary source](https://doi.org/10.1007/s00026-024-00736-9) Location: §5, Problem 1.

**Literature check.** Status for question 1476, checked 6 October 2026: Ochem–Pierron 2025 settles t(3),t(4), but not this additive-constant asymptotic bound. No later resolution located.

**Further links.** [1](https://arxiv.org/abs/2407.03819) · [2](https://doi.org/10.46298/dmtcs.15310)


<a id="q1477"></a>

## Q1477. The first unresolved tangram alphabet size

**Status:** Open · **Kind:** open problem · **Collection** 15

What is the exact value of t(5)?

**Context.** Origin for question 1477: The authors’ concluding question after proving t(3)=t(4)=4. Setup for question 1477: A tangram is a nonempty word in which every letter count is even. Its cut number is the fewest cuts into nonempty consecutive pieces that can be permuted into two identical words. t(k) is the smallest alphabet size admitting an infinite word without a factor of cut number≤k.

**Source.** Pascal Ochem and Théo Pierron. *4-tangrams are 4-avoidable*. 2025. [primary source](https://doi.org/10.46298/dmtcs.15310) Location: §4, concluding remarks, p. 5.

**Literature check.** Status for question 1477, checked 6 October 2026: The final version states 4≤t(5)≤6; no later exact value located.

**Further links.** [1](https://arxiv.org/abs/2502.20774v3) · [2](https://www.lirmm.fr/~ochem/publi.htm)


<a id="q1551"></a>

## Q1551. Subpolynomial interval-colouring thickness

**Status:** Open · **Kind:** open problem · **Collection** 16

Is θ(n)=n^{o(1)} as n→∞?

**Context.** Origin for questions 1551, 1552, 1553: Paper conjectures from 2023 preprint, published 2024; restated in Tamitegama’s thesis §4.3. Setup for questions 1551, 1552, 1553: Graphs are finite and simple. An interval colouring is a proper positive-integer edge colouring whose colours incident to each nonisolated vertex are consecutive. Let θ(G) be the fewest interval-colourable parts in an edge partition and θ(n)=max_{|V(G)|=n}θ(G). Biregular means bipartite with constant degree on each side.

**Source.** Maria Axenovich; António Girão; Lawrence Hollom; Julien Portier; Emil Powierski; Michael Savery; Youri Tamitegama; Leo Versteegen. *A note on interval colourings of graphs*. 2024. [primary source](https://doi.org/10.1016/j.ejc.2024.103956) Location: Conj. 10, §5.

**Literature check.** Status for questions 1551, 1552, 1553, checked 6 October 2026: The 2025 thesis retains these questions; through 6 October 2026 no matching proof or counterexample was found. Near-interval results for specific degree pairs do not settle interval colourability.

**Further links.** [1](https://arxiv.org/abs/2303.04782) · [2](https://wwwalt.math.kit.edu/iag6/~axenovich/seite/publications/media/interval-thickness-joint-european-2023-5-18.pdf) · [3](https://ora.ox.ac.uk/objects/uuid:20d85c21-c0ae-4a4c-9dec-af456d9eafd2) · [4](https://doi.org/10.1016/j.dam.2025.03.011) · [5](https://publikationen.bibliothek.kit.edu/1000171530/153053361)


<a id="q1552"></a>

## Q1552. Interval-colour every biregular graph

**Status:** Open · **Kind:** open problem · **Collection** 16

Is every biregular graph interval colourable?

**Context.** Origin for questions 1551, 1552, 1553: Paper conjectures from 2023 preprint, published 2024; restated in Tamitegama’s thesis §4.3. Setup for questions 1551, 1552, 1553: Graphs are finite and simple. An interval colouring is a proper positive-integer edge colouring whose colours incident to each nonisolated vertex are consecutive. Let θ(G) be the fewest interval-colourable parts in an edge partition and θ(n)=max_{|V(G)|=n}θ(G). Biregular means bipartite with constant degree on each side.

**Source.** Maria Axenovich; António Girão; Lawrence Hollom; Julien Portier; Emil Powierski; Michael Savery; Youri Tamitegama; Leo Versteegen. *A note on interval colourings of graphs*. 2024. [primary source](https://doi.org/10.1016/j.ejc.2024.103956) Location: Conj. 12, §5.

**Literature check.** Status for questions 1551, 1552, 1553, checked 6 October 2026: The 2025 thesis retains these questions; through 6 October 2026 no matching proof or counterexample was found. Near-interval results for specific degree pairs do not settle interval colourability.

**Further links.** [1](https://arxiv.org/abs/2303.04782) · [2](https://wwwalt.math.kit.edu/iag6/~axenovich/seite/publications/media/interval-thickness-joint-european-2023-5-18.pdf) · [3](https://ora.ox.ac.uk/objects/uuid:20d85c21-c0ae-4a4c-9dec-af456d9eafd2) · [4](https://doi.org/10.1016/j.dam.2025.03.011) · [5](https://publikationen.bibliothek.kit.edu/1000171530/153053361)


<a id="q1553"></a>

## Q1553. Decompose into few forests and biregular graphs

**Status:** Open · **Kind:** open problem · **Collection** 16

Can every n-vertex graph be edge-partitioned into n^{o(1)} parts, each a forest or a biregular graph?

**Context.** Origin for questions 1551, 1552, 1553: Paper conjectures from 2023 preprint, published 2024; restated in Tamitegama’s thesis §4.3. Setup for questions 1551, 1552, 1553: Graphs are finite and simple. An interval colouring is a proper positive-integer edge colouring whose colours incident to each nonisolated vertex are consecutive. Let θ(G) be the fewest interval-colourable parts in an edge partition and θ(n)=max_{|V(G)|=n}θ(G). Biregular means bipartite with constant degree on each side.

**Source.** Maria Axenovich; António Girão; Lawrence Hollom; Julien Portier; Emil Powierski; Michael Savery; Youri Tamitegama; Leo Versteegen. *A note on interval colourings of graphs*. 2024. [primary source](https://doi.org/10.1016/j.ejc.2024.103956) Location: Q. 14, §5.

**Literature check.** Status for questions 1551, 1552, 1553, checked 6 October 2026: The 2025 thesis retains these questions; through 6 October 2026 no matching proof or counterexample was found. Near-interval results for specific degree pairs do not settle interval colourability.

**Further links.** [1](https://arxiv.org/abs/2303.04782) · [2](https://wwwalt.math.kit.edu/iag6/~axenovich/seite/publications/media/interval-thickness-joint-european-2023-5-18.pdf) · [3](https://ora.ox.ac.uk/objects/uuid:20d85c21-c0ae-4a4c-9dec-af456d9eafd2) · [4](https://doi.org/10.1016/j.dam.2025.03.011) · [5](https://publikationen.bibliothek.kit.edu/1000171530/153053361)


<a id="q1554"></a>

## Q1554. Only four partial-shattering growth rates

**Status:** Open · **Kind:** open problem · **Collection** 16

For every fixed k,t, must f_k(n,t) have one of the orders Θ(1), Θ(log log n), Θ(√log n), or Θ(log n)?

**Context.** Doctoral context for questions 1554, 1555: see question 1551. Origin for questions 1554, 1555: New questions in the 2024 preprint; thesis Questions 7.15 and 7.16; journal publication 4 March 2026. Setup for questions 1554, 1555: For fixed integers k≥1 and 1≤t≤k!, f_k(n,t) is the least size of a family of permutations of [n] inducing at least t distinct orders on every k-subset. Asymptotics are as n→∞.

**Source.** António Girão; Lukas Michel; Youri Tamitegama. *Small Families of Partially Shattering Permutations*. 2026. [primary source](https://doi.org/10.1007/s00493-026-00201-6) Location: Q. 4.1, §4.

**Literature check.** Status for questions 1554, 1555, checked 6 October 2026: Both are explicitly reaffirmed in the 4 March 2026 journal version. Searches through 6 October found no subsequent matching resolution; k≤4 is solved, but k≥5 contains an unsettled range.

**Further links.** [1](https://link.springer.com/article/10.1007/s00493-026-00201-6) · [2](https://arxiv.org/abs/2407.05773) · [3](https://ora.ox.ac.uk/objects/uuid:20d85c21-c0ae-4a4c-9dec-af456d9eafd2)


<a id="q1555"></a>

## Q1555. Sharp threshold for logarithmic shattering

**Status:** Open · **Kind:** open problem · **Collection** 16

For all fixed k≥3 and 1≤t≤2^{k−1}, is f_k(n,t)=o(log n)?

**Context.** Doctoral context for questions 1554, 1555: see question 1551. Origin for questions 1554, 1555: New questions in the 2024 preprint; thesis Questions 7.15 and 7.16; journal publication 4 March 2026. Setup for questions 1554, 1555: For fixed integers k≥1 and 1≤t≤k!, f_k(n,t) is the least size of a family of permutations of [n] inducing at least t distinct orders on every k-subset. Asymptotics are as n→∞.

**Source.** António Girão; Lukas Michel; Youri Tamitegama. *Small Families of Partially Shattering Permutations*. 2026. [primary source](https://doi.org/10.1007/s00493-026-00201-6) Location: Conj. 4.2, §4.

**Literature check.** Status for questions 1554, 1555, checked 6 October 2026: Both are explicitly reaffirmed in the 4 March 2026 journal version. Searches through 6 October found no subsequent matching resolution; k≤4 is solved, but k≥5 contains an unsettled range.

**Further links.** [1](https://link.springer.com/article/10.1007/s00493-026-00201-6) · [2](https://arxiv.org/abs/2407.05773) · [3](https://ora.ox.ac.uk/objects/uuid:20d85c21-c0ae-4a4c-9dec-af456d9eafd2)


<a id="q1556"></a>

## Q1556. Polynomial diameter for polytope graphs

**Status:** Open · **Kind:** open problem (Problem 5.0.3) · **Collection** 16

Does one polynomial p bound the vertex-edge graph diameter of every d-dimensional polytope with m facets by p(m,d)?

**Context.** Origin for questions 1556, 1557: Polynomial Hirsch conjecture, restated in the thesis; do not confuse with the disproved linear Hirsch bound or the solved circuit-diameter variant.

**Source.** Alexander E. Black. *Monotone Paths on Polytopes: Combinatorics and Optimization*. 2024. Advisor(s): Jesús A. De Loera. [primary source](https://www.math.ucdavis.edu/~webfiles/dissertations/202403_Alex_Black_DeLoera.pdf) Location: Problem 5.0.3, p. 84.

**Literature check.** Status for questions 1556, 1557, checked 6 October 2026: The ordinary polynomial Hirsch problem is expressly retained in Black–Xue (13 July 2026). A separate September 2026 result disproves polynomial monotone diameter for bounded-coordinate lattice polytopes, not the bounded-subdeterminant question. No matching resolution of that question was found.

**Further links.** [1](https://arxiv.org/html/2607.11628v1) · [2](https://arxiv.org/abs/2609.08647) · [3](https://arxiv.org/abs/2602.06958)


<a id="q1557"></a>

## Q1557. Subdeterminant control of monotone diameter

**Status:** Open · **Kind:** open problem (Problem 5.2.3) · **Collection** 16

Does one polynomial p(n,Δ) bound, for every bounded full-dimensional P={x∈Rⁿ:Ax≤b} with integral A and every square subdeterminant of A at most Δ in absolute value, the shortest strictly objective-increasing edge path from any vertex to an optimum, uniformly over linear objectives?

**Context.** Origin for questions 1556, 1557: Polynomial Hirsch conjecture, restated in the thesis; do not confuse with the disproved linear Hirsch bound or the solved circuit-diameter variant.

**Source.** Alexander E. Black. *Monotone Paths on Polytopes: Combinatorics and Optimization*. 2024. Advisor(s): Jesús A. De Loera. [primary source](https://www.math.ucdavis.edu/~webfiles/dissertations/202403_Alex_Black_DeLoera.pdf) Location: Problem 5.2.3, p. 87.

**Literature check.** Status for questions 1556, 1557, checked 6 October 2026: The ordinary polynomial Hirsch problem is expressly retained in Black–Xue (13 July 2026). A separate September 2026 result disproves polynomial monotone diameter for bounded-coordinate lattice polytopes, not the bounded-subdeterminant question. No matching resolution of that question was found.

**Further links.** [1](https://arxiv.org/html/2607.11628v1) · [2](https://arxiv.org/abs/2609.08647) · [3](https://arxiv.org/abs/2602.06958)


<a id="q1558"></a>

## Q1558. Decompose highly connected infinite graphs into trees

**Status:** Open · **Kind:** open problem · **Collection** 16

For every finite tree T with at least one edge, is there an integer k(T) such that every infinite simple k(T)-edge-connected graph admits an edge partition into subgraphs isomorphic to T?

**Context.** Origin for question 1558: Merker’s thesis Conjecture 2.6.1; related primary paper is Decomposing highly edge-connected graphs into homomorphic copies of a fixed tree (2016 preprint; JCTB 2017).

**Source.** Martin Merker. *Graph Decompositions*. 2016. Advisor(s): Carsten Thomassen. [primary source](https://backend.orbit.dtu.dk/ws/portalfiles/portal/128006095/phd431_Merker_M.pdf) Location: Conj. 2.6.1, p. 52.

**Literature check.** Status for question 1558, checked 6 October 2026: The source proves the locally finite case, and pseudo-decompositions in general. Searches through 6 October 2026 found no resolution of arbitrary infinite graphs.

**Further links.** [1](https://arxiv.org/abs/1603.00198)


<a id="q1559"></a>

## Q1559. One extra forest bounds all diameters

**Status:** Open · **Kind:** open problem · **Collection** 16

For every integer k≥4, is there d(k) such that every graph whose edges partition into k forests also partitions into k+1 forests whose components all have diameter at most d(k)?

**Context.** Doctoral context for questions 1559, 1560: see question 1558. Origin for questions 1559, 1560: Merker–Postle conjectures from the 2016 preprint and Merker’s 2016 thesis; journal issue year 2019, online November 2018. Setup for questions 1559, 1560: All graphs here are finite and simple; a forest’s diameter bound applies separately to every component.

**Source.** Martin Merker; Luke Postle. *Bounded diameter arboricity*. 2019. [primary source](https://doi.org/10.1002/jgt.22416) Location: Conj. 1.2.

**Literature check.** Status for questions 1559, 1560, checked 6 October 2026: The general conjecture is known for k≤3. Mies’s 2025 thesis explicitly retains the forest-exchange question. Searches through 6 October 2026 found no general resolution.

**Further links.** [1](https://backend.orbit.dtu.dk/ws/portalfiles/portal/162440759/Bounded_Diameter_Arboricity.pdf) · [2](https://arxiv.org/abs/1608.05352) · [3](https://openscience.ub.uni-mainz.de/bitstreams/db2c6b84-8332-44dd-a125-635d09470cc1/download) · [4](https://backend.orbit.dtu.dk/ws/portalfiles/portal/128006095/phd431_Merker_M.pdf)


<a id="q1560"></a>

## Q1560. Spread a diameter bound across two forests

**Status:** Open · **Kind:** open problem · **Collection** 16

For every integer d≥3, is there f(d) such that any edge-disjoint union of a forest and a forest with component diameters at most d can be repartitioned into two forests with all component diameters at most f(d)?

**Context.** Doctoral context for questions 1559, 1560: see question 1558. Origin for questions 1559, 1560: Merker–Postle conjectures from the 2016 preprint and Merker’s 2016 thesis; journal issue year 2019, online November 2018. Setup for questions 1559, 1560: All graphs here are finite and simple; a forest’s diameter bound applies separately to every component.

**Source.** Martin Merker; Luke Postle. *Bounded diameter arboricity*. 2019. [primary source](https://doi.org/10.1002/jgt.22416) Location: Conj. 4.3.

**Literature check.** Status for questions 1559, 1560, checked 6 October 2026: The general conjecture is known for k≤3. Mies’s 2025 thesis explicitly retains the forest-exchange question. Searches through 6 October 2026 found no general resolution.

**Further links.** [1](https://backend.orbit.dtu.dk/ws/portalfiles/portal/162440759/Bounded_Diameter_Arboricity.pdf) · [2](https://arxiv.org/abs/1608.05352) · [3](https://openscience.ub.uni-mainz.de/bitstreams/db2c6b84-8332-44dd-a125-635d09470cc1/download) · [4](https://backend.orbit.dtu.dk/ws/portalfiles/portal/128006095/phd431_Merker_M.pdf)


<a id="q1561"></a>

## Q1561. Strong Nine Dragon beyond the proved range

**Status:** Open · **Kind:** open problem · **Collection** 16

For integers k≥1 and d>2(k+1), does γ(G)≤k+d/(d+k+1) guarantee an edge partition into k+1 forests, one of which has at most d edges in each component?

**Context.** Origin for question 1561: Strong Nine Dragon Tree conjecture of Montassier, Ossona de Mendez, Raspaud and Zhu (2012). Located through Mies’s 2025 doctoral thesis; its public supervisor names are redacted, so none are inferred. Setup for question 1561: For a finite loopless multigraph G, put γ(G)=max_{H⊆G, |V(H)|≥2}|E(H)|/(|V(H)|−1).

**Source.** Sebastian Mies; Benjamin Moore. *The Strong Nine Dragon Tree Conjecture is True for d ≤ 2(k+1)*. 2024. [primary source](https://arxiv.org/abs/2403.05178) Location: Conj. 1.4, p. 3.

**Literature check.** Status for question 1561, checked 6 October 2026: Mies’s 2025 thesis and the 2025 pseudoforest paper retain the forest conjecture. The case d≤2(k+1) is proved; bounded searches through 6 October 2026 found no general proof for larger d.

**Further links.** [1](https://arxiv.org/abs/2406.05022) · [2](https://doi.org/10.1016/j.ejc.2025.104214) · [3](https://openscience.ub.uni-mainz.de/items/87ef5ac4-3441-471e-a175-411c9abcb512)


<a id="q1562"></a>

## Q1562. A uniformly thin spanning tree

**Status:** Open · **Kind:** open problem · **Collection** 16

Is there an absolute C>0 such that every k-edge-connected G has a spanning tree T satisfying |E(T)∩δ\_G(S)|≤(C/k)|δ\_G(S)| for every S⊆V(G)?

**Context.** Origin for question 1562: Goddyn’s thin-tree question (2004), strengthened to C/k by Asadpour and coauthors. Setup for question 1562: G is a finite loopless undirected multigraph; δ\_G(S) is its cut at S.

**Source.** Nathan Klein; Neil Olver; Zi Song Yeoh. *Thin Trees for near Minimum Cuts*. 2026. [primary source](https://doi.org/10.4230/LIPIcs.ICALP.2026.129) Location: §1.

**Literature check.** Status for question 1562, checked 6 October 2026: The July 2026 ICALP paper retains this conjecture and proves only a near-minimum-cut bound. No later resolution found.

**Further links.** [1](https://arxiv.org/abs/2605.12669) · [2](https://arxiv.org/html/2605.12669v1)


<a id="q1563"></a>

## Q1563. Balance two spanning trees within two

**Status:** Open · **Kind:** open problem · **Collection** 16

If a finite loopless multigraph is the edge-disjoint union of two spanning trees, must it admit such a partition T₁,T₂ with |deg_{T₁}(v)−deg_{T₂}(v)|≤2 at every vertex v?

**Context.** Origin for questions 1563, 1564: Conjecture 27 and Question 29 of the authors.

**Source.** Freddie Illingworth; Emil Powierski; Alex Scott; Youri Tamitegama. *Balancing Connected Colourings of Graphs*. 2023. [primary source](https://doi.org/10.37236/11256) Location: Conj. 27, p. 24.

**Literature check.** Status for questions 1563, 1564, checked 6 October 2026: No matching resolution found; the proved uniform degree-difference bound for two spanning trees is four.

**Further links.** [1](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v30i1p54/pdf/) · [2](https://arxiv.org/abs/2205.04984)


<a id="q1564"></a>

## Q1564. Balance many rooted arborescences in two colours

**Status:** Open · **Kind:** open problem · **Collection** 16

Are there absolute integers c≥0 and t≥2 such that every finite digraph that is the arc-disjoint union of t spanning out-arborescences with one common root has a red/blue arc colouring, each colour containing a spanning out-arborescence, with |d_R⁺(v)−d_B⁺(v)|≤c for every v?

**Context.** Origin for questions 1563, 1564: Conjecture 27 and Question 29 of the authors.

**Source.** Freddie Illingworth; Emil Powierski; Alex Scott; Youri Tamitegama. *Balancing Connected Colourings of Graphs*. 2023. [primary source](https://doi.org/10.37236/11256) Location: Q. 29, p. 25.

**Literature check.** Status for questions 1563, 1564, checked 6 October 2026: No matching resolution found; the proved uniform degree-difference bound for two spanning trees is four.

**Further links.** [1](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v30i1p54/pdf/) · [2](https://arxiv.org/abs/2205.04984)


<a id="q1565"></a>

## Q1565. Two irregular colours after doubling every edge

**Status:** Open · **Kind:** open problem · **Collection** 16

For every finite connected simple graph G≠K₂, can the multigraph obtained by replacing each edge with two parallel edges be red/blue edge-coloured so that endpoints of every red edge have different red degrees, and endpoints of every blue edge have different blue degrees?

**Context.** Origin for question 1565: Grzelec–Woźniak conjecture (2022 preprint; 2023 paper), restated as Conjecture 2 in the 2026 paper.

**Source.** Igor Grzelec; Alfréd Onderko; Mariusz Woźniak. *On local irregularity conjecture for 2-multigraphs*. 2026. [primary source](https://doi.org/10.1016/j.amc.2025.129832) Location: Conj. 2, §1.

**Literature check.** Status for question 1565, checked 6 October 2026: The April 2026 paper explicitly retains the conjecture and proves regular, split, and certain subcubic cases. No full resolution located through 6 October 2026.

**Further links.** [1](https://www.sciencedirect.com/science/article/pii/S0096300325005570) · [2](https://arxiv.org/abs/2412.04200) · [3](https://arxiv.org/abs/2208.08809)


<a id="q1566"></a>

## Q1566. Two locally irregular total colours

**Status:** Open · **Kind:** open problem · **Collection** 16

Can every finite simple graph G have its vertices and edges coloured red/blue so that, for each colour a and each a-coloured edge uv, deg_a(u)+1_{u has colour a}≠deg_a(v)+1_{v has colour a}? Here deg_a counts incident a-coloured edges.

**Context.** Origin for question 1566: Baudon, Bensmail, Przybyło and Woźniak’s 2015 conjecture, restated as Conjecture 4.

**Source.** Anna Flaszczyńska; Aleksandra Gorzkowska; Igor Grzelec; Alfréd Onderko; Mariusz Woźniak. *Locally Irregular Total Colorings of Graphs*. 2026. [primary source](https://arxiv.org/abs/2603.13178) Location: Conj. 4, §1.

**Literature check.** Status for question 1566, checked 6 October 2026: March 2026 paper explicitly retains the conjecture and proves cacti, subcubic and split cases (regular and bipartite cases are also known). No full resolution located through 6 October 2026.

**Further links.** [1](https://arxiv.org/html/2603.13178v1)


<a id="q1650"></a>

## Q1650. Enumerate arbitrary bipartite-forbidden graphs

**Status:** Open · **Kind:** conjecture (Conjecture 1.3) · **Collection** 17

For every fixed bipartite graph H containing a cycle, is the number of labelled simple H-free graphs on [n] at most 2^{O_H(ex(n,H))}? Here H-free means forbidding H as a subgraph, and ex(n,H) is the largest edge count of such a graph.

**Context.** Origin for question 1650: Kleitman–Winston (1982), as attributed in Conjecture 1.3; restated in Dong’s 2025 thesis, Conjecture 3.1.3.

**Source.** Dingding Dong; Nitya Mani; Yufei Zhao. *On the number of error correcting codes*. 2023. [primary source](https://doi.org/10.1017/S0963548323000111) Location: Conjecture 1.3; thesis Conjecture 3.1.3.

**Literature check.** Status for question 1650, checked 6 October 2026: The 2023 journal and 2025 thesis retain the arbitrary-H counting conjecture. Morris–Ortega–Rué (July 2026), §1.3, still cites a conditional theorem assuming ex(n,H)=Θ(n^α); this does not settle arbitrary bipartite H. No matching general proof or counterexample found through 6 October 2026.

**Further links.** [1](https://arxiv.org/abs/2205.12363) · [2](https://arxiv.org/pdf/2205.12363) · [3](https://dash.harvard.edu/entities/publication/84e1e974-6469-4dbc-be04-b0237c5ac712) · [4](https://arxiv.org/html/2607.17746v1) · [5](https://doi.org/10.1017/fms.2025.10163) · [6](https://dash.harvard.edu/bitstreams/fcc8fc04-74db-48fc-b94e-509f6ed54381/download) · [7](https://www.math.harvard.edu/wp-content/uploads/2024-2025-Commencement-Newsletter-Revised.pdf)


<a id="q1651"></a>

## Q1651. Sharp count of progression-free sets

**Status:** Open · **Kind:** open problem · **Collection** 17

For each fixed integer k≥3, let r_k(n) be the maximum size of a subset of [n] containing no k-term arithmetic progression with nonzero common difference. Is the number of all such subsets 2^{(1+o(1))r_k(n)} as n→∞ through all integers?

**Context.** Origin for question 1651: Cameron and Erdős, On the number of sets of integers with various properties (1990), as attributed in §1.1 and reference [9]. Discovered through Dong’s thesis §3.1, but the current-status source is this 2026 paper.

**Source.** Patrick Morris; Miquel Ortega; Juanjo Rué. *Counting subsets of integers free of arithmetic configurations*. 2026. [primary source](https://arxiv.org/abs/2607.17746) Location: Questions 1.1 and 7.1.

**Literature check.** Status for question 1651, checked 6 October 2026: The 20 July 2026 preprint explicitly keeps the full sharp count open in Questions 1.1 and 7.1. Theorem 1.4 proves the weaker 2^{O(r_k(n))} bound for all n; Theorem 1.3 proves the sharp exponent only along an infinite sequence for each k≥5. No subsequent full resolution found through 6 October 2026.

**Further links.** [1](https://arxiv.org/html/2607.17746v1) · [2](https://doi.org/10.1093/imrn/rnw077)


<a id="q1652"></a>

## Q1652. Count SAT functions with growing clause width

**Status:** Open · **Kind:** open problem (Question 1.19) · **Collection** 17

For every fixed 0&lt;c<1/2 and integer sequence 2≤k=k(n)≤(1/2−c)n, is log₂ N_k(n)=(1+o(1))binom(n,k), where N_k(n) counts distinct Boolean functions representable as a disjunction of conjunctions of exactly k literals on distinct variables?

**Context.** Doctoral context for question 1652: see question 1650. Origin for question 1652: Bollobás and Brightwell, The number of k-SAT functions (2003), conjecture recalled immediately before Question 1.19 in the merged 2023 preprint and before thesis Question 2.1.20.

**Source.** József Balogh; Dingding Dong; Bernard Lidický; Nitya Mani; Yufei Zhao. *Nearly all k-SAT functions are unate*. 2023. [primary source](https://arxiv.org/abs/2209.04894) Location: §1.5, paragraph before Question 1.19; thesis §2.1.5.

**Literature check.** Status for question 1652, checked 6 October 2026: The merged October 2023 version and Dong’s 2025 thesis distinguish the proved fixed-k theorem from the growing-k problem, which remains explicit. Searches through 6 October 2026 found no proof for the stated linear range of k; fixed-k unateness is excluded.

**Further links.** [1](https://arxiv.org/pdf/2209.04894v2) · [2](https://doi.org/10.1002/rsa.10079) · [3](https://dash.harvard.edu/entities/publication/84e1e974-6469-4dbc-be04-b0237c5ac712) · [4](https://dash.harvard.edu/bitstreams/fcc8fc04-74db-48fc-b94e-509f6ed54381/download) · [5](https://www.math.harvard.edu/wp-content/uploads/2024-2025-Commencement-Newsletter-Revised.pdf)


<a id="q1653"></a>

## Q1653. Realize unbounded factorial-language complexity

**Status:** Solved here: disproved · **Kind:** conjecture (Conjecture 6.36) · **Collection** 17

Let F⊆{0,1}\* be closed under taking contiguous factors, with unbounded sequence q_F(n)=|F∩{0,1}^n|. Must there be an infinite binary sequence b such that, for every n, exactly q_F(n) distinct length-n words occur infinitely often as contiguous factors of b?

**Context.** Origin for question 1653: Jarvis’s Complexity-equivalence conjecture, Conjecture 6.36.

**Source.** Ben Jarvis. *Pin Classes*. 2026. Advisor(s): Robert Brignall. [primary source](https://oro.open.ac.uk/108335/1/Pin%20Classes.pdf) Location: Conjecture 6.36, p. 173; Definitions 6.1 and 6.5.

**Literature check.** Status for question 1653, checked 6 October 2026: The August 2025 thesis explicitly leaves Conjecture 6.36 open. Inspected Pin Classes I v3 (29 September 2026) and Pin Classes II (April 2026); they establish growth-rate results, not this factorial-language realization statement. Exact-phrase and author/topic searches found no resolution through 6 October 2026.

**Further links.** [1](https://arxiv.org/pdf/2412.04143v3) · [2](https://dmtcs.episciences.org/18082/pdf)

**Result (2026-10-09).** The factor-closed language 0*1* union {10} has complexity 2,4,4,5,6,... . A plateau in recurrent-factor complexity must persist, so no infinite binary word has this complexity at every length. Disproves the exact all-length equality in Conjecture 6.36; no claim about eventual equality or separate permutation-class growth-rate conjectures.

[Proof](../../solutions/round-2026-10-09/discrete/Q1653-recurrent-complexity-counterexample.md) · [Internal review](../../solutions/round-2026-10-09/reviews/root-review.md) · [Exact computational controls](../../solutions/round-2026-10-09/discrete/recurrent-complexity-checks.json). This is a research proposal with a separate internal AI review, not an externally peer-reviewed result.



<a id="q1656"></a>

## Q1656. Force every nonbouncing endpoint path

**Status:** Open · **Kind:** open problem (Question 1) · **Collection** 17

For every positive integer k, must every finite oriented graph G with δ⁰(G)≥k/2 contain every orientation of the k-edge path, except the bouncing orientations when k is even?

**Context.** Origin for question 1656: The authors’ sharpening of Stein’s 2021 path conjecture. Use revised journal Question 1, not the obsolete v1 exclusion of only antidirected paths. Setup for question 1656: An oriented graph has neither loops nor antiparallel arcs, and δ⁰ is its minimum in- or out-degree. For an oriented path p₀…p_k set h₀=0 and h_{i+1}−h_i=1 for p_i→p_{i+1}, −1 otherwise; it is bouncing when every h_i lies in {−1,0,1}.

**Source.** Irena Penev; S Taruni; Stéphan Thomassé; Ana Trujillo-Negrete; Mykhaylo Tyomkyn. *Two-Block Paths in Oriented Graphs of Large Semidegree*. 2026. [primary source](https://doi.org/10.1002/jgt.70131) Location: Journal Question 1, §5; arXiv v2 Question 5.1.

**Literature check.** Status for question 1656, checked 6 October 2026: August 2026 arXiv v2 and September 2026 journal Question 1 explicitly use the bouncing-path exception. The journal acknowledges the correction. No subsequent matching resolution found through 6 October 2026.

**Further links.** [1](https://arxiv.org/html/2503.23191v2)


<a id="q1657"></a>

## Q1657. Bound the cost of one tournament vertex

**Status:** Open · **Kind:** conjecture (Conjecture 9) · **Collection** 17

Is there an absolute C such that R(D)≤C R(D−v) for every finite acyclic digraph D on at least two vertices and every vertex v?

**Context.** Origin for questions 1657, 1658: The authors’ Problem 8 and Conjecture 9; 2024 preprint, 2026 journal. Setup for questions 1657, 1658: For a finite acyclic digraph D, R(D) is the least N such that every N-vertex tournament contains D as a subdigraph. T[k] replaces each vertex of T by k independent vertices and each arc by all k² corresponding arcs.

**Source.** Pierre Aboulker; Frédéric Havet; William Lochet; Raul Lopes; Lucas Picasarri-Arrieta; Clément Rambaud. *Blow-ups and extensions of trees in tournaments*. 2026. [primary source](https://doi.org/10.37236/13540) Location: Conjecture 9, p. 5.

**Literature check.** Status for questions 1657, 1658, checked 6 October 2026: The final Electronic Journal of Combinatorics 33(3), P3.22 (7 August 2026), pp. 4–5 retains both targets. The proved tree-blow-up bound is 2^{10+18k}kn. Source/specific-conjecture searches found no subsequent resolution through 6 October 2026.

**Further links.** [1](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v33i3p22/pdf/) · [2](https://arxiv.org/html/2410.23566)


<a id="q1658"></a>

## Q1658. Find the optimal tree-blow-up base

**Status:** Open · **Kind:** open problem (Problem 8) · **Collection** 17

Determine the infimum of constants C such that, for every positive integer k and all sufficiently large n, every n-vertex oriented tree T satisfies R(T[k])≤C^k kn. The threshold in n may depend on k.

**Context.** Origin for questions 1657, 1658: The authors’ Problem 8 and Conjecture 9; 2024 preprint, 2026 journal. Setup for questions 1657, 1658: For a finite acyclic digraph D, R(D) is the least N such that every N-vertex tournament contains D as a subdigraph. T[k] replaces each vertex of T by k independent vertices and each arc by all k² corresponding arcs.

**Source.** Pierre Aboulker; Frédéric Havet; William Lochet; Raul Lopes; Lucas Picasarri-Arrieta; Clément Rambaud. *Blow-ups and extensions of trees in tournaments*. 2026. [primary source](https://doi.org/10.37236/13540) Location: Problem 8, p. 4.

**Literature check.** Status for questions 1657, 1658, checked 6 October 2026: The final Electronic Journal of Combinatorics 33(3), P3.22 (7 August 2026), pp. 4–5 retains both targets. The proved tree-blow-up bound is 2^{10+18k}kn. Source/specific-conjecture searches found no subsequent resolution through 6 October 2026.

**Further links.** [1](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v33i3p22/pdf/) · [2](https://arxiv.org/html/2410.23566)


<a id="q1659"></a>

## Q1659. Classify digraphs forced by dense high chromatic hosts

**Status:** Open · **Kind:** open problem (Question 4.1) · **Collection** 17

Which finite digraphs H have the following property: for every ε>0 there is c=c(H,ε) such that every finite digraph D without loops or parallel arcs, with χ(D)≥c and minimum out-degree at least ε|V(D)|, contains H as a subdigraph? Here χ is the chromatic number of the underlying undirected graph; antiparallel arcs are allowed.

**Context.** Origin for question 1659: Authors’ Question 4.1, extending their complete classification for cycle orientations.

**Source.** Hidde Koerts; Benjamin Moore; Sophie Spirkl. *Orientations of Cycles in Digraphs of High Chromatic Number and High Minimum Out-Degree*. 2026. [primary source](https://doi.org/10.1007/s00493-026-00207-0) Location: Preprint Question 4.1, §4.

**Literature check.** Status for question 1659, checked 6 October 2026: Published in Combinatorica 46, article 12, 4 March 2026; publisher Crossmark says the document is current. The preprint Question 4.1 asks for arbitrary H, beyond the cycle orientations classified by Theorem 1.3. Later chromatic-profile work only treats particular orientations; no complete general classification located through 6 October 2026.

**Further links.** [1](https://arxiv.org/abs/2503.20045) · [2](https://arxiv.org/html/2503.20045) · [3](https://crossmark.crossref.org/dialog/?doi=10.1007%2Fs00493-026-00207-0)


<a id="q1664"></a>

## Q1664. Two parts with locally distinguishing binary weights

**Status:** Open · **Kind:** open problem · **Collection** 17

Can the edges of every finite connected simple graph on at least four vertices be partitioned into E₁,E₂ and assigned weights 1 or 2 so that, for each i and each uv∈Eᵢ, the sums of weights of Eᵢ-edges incident to u and v differ?

**Context.** Origin for question 1664: The (2,2)-conjecture is attributed to Baudon et al. [1]; restated as Conjectures 3–4 of the 2024 preprint (2026 journal publication).

**Source.** Igor Grzelec; Tomáš Madaras; Alfréd Onderko; Roman Soták. *On a new problem about the local irregularity of graphs*. 2026. [primary source](https://doi.org/10.1016/j.amc.2025.129763) Location: Preprint Conjectures 3–4, p. 4; journal introduction.

**Literature check.** Status for question 1664, checked 6 October 2026: The March 2026 journal retains the (2,2)-conjecture. Searches through 6 October 2026 found no general solution; this is distinct from list-weight and total-weight conjectures with similar names.

**Further links.** [1](https://arxiv.org/abs/2405.13893) · [2](https://arxiv.org/pdf/2405.13893) · [3](https://www.sciencedirect.com/science/article/pii/S0096300325004886)


<a id="q1665"></a>

## Q1665. Spectral extremizers avoiding the icosahedron

**Status:** Open · **Kind:** open problem (Problem 6.1) · **Collection** 17

For all sufficiently large n, which simple n-vertex graphs containing no subgraph isomorphic to the 12-vertex icosahedron graph maximize the adjacency spectral radius?

**Context.** Origin for question 1665: Explicit unresolved example in the authors’ concluding remarks.

**Source.** Longfei Fang; Sergey Goryainov; Denis Krotov; Huiqiu Lin; Mingqing Zhai. *The spectral Turán problem: Characterizing spectral-consistent graphs*. 2026. [primary source](https://arxiv.org/abs/2508.12070) Location: §6, paragraph after Problem 6.1.

**Literature check.** Status for question 1665, checked 6 October 2026: Fresh recheck 6 October 2026: March 2026 v2, §6 still expressly leaves the icosahedron adjacency-spectral extremal problem open; no subsequent matching solution found.

**Further links.** [1](https://arxiv.org/html/2508.12070v2) · [2](https://www.sciencedirect.com/science/article/pii/S0024379525004318)


<a id="q1666"></a>

## Q1666. Pack strongly connected spanning digraphs

**Status:** Open · **Kind:** open problem (Question 30) · **Collection** 17

For every integer t≥2, is there k such that every finite k-vertex-strongly-connected digraph has an arc partition into t strongly connected spanning subdigraphs? Here k-vertex-strong means strong connectivity survives deletion of fewer than k vertices.

**Context.** Origin for question 1666: Conjecture 27 and Questions 29–30 of the authors; this is a primary-paper continuation of the verified Tamitegama research route.

**Source.** Freddie Illingworth; Emil Powierski; Alex Scott; Youri Tamitegama. *Balancing Connected Colourings of Graphs*. 2023. [primary source](https://doi.org/10.37236/11256) Location: §7, Question 30, p. 25.

**Literature check.** Status for question 1666, checked 6 October 2026: Current journal Question 30 explicitly asks for strongly connected spanning arc partitions. Fresh exact-topic searches through 6 October 2026 found no general solution; this statement is not the already-treated degree-balanced double-tree question.

**Further links.** [1](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v30i1p54/pdf/) · [2](https://arxiv.org/abs/2205.04984)


<a id="q1750"></a>

## Q1750. Find independent flats at large girth

**Status:** Open · **Kind:** conjecture (Conjecture 7.9) · **Collection** 18

For every k≥1, does some C_k ensure that every matroid of girth≥5 and rank≥C_k has a rank-k independent flat?

**Context.** Origin for questions 1750, 1751, 1752: Geelen’s conjectures, recorded in Chapter 7. Setup for questions 1750, 1751, 1752: Matroids are finite and simple. A rank-k independent flat has exactly k elements. AG(k,p) is the rank-(k+1) affine-geometry matroid on F_p^k.

**Source.** Matthew Eliot Kroeker. *Some Sylvester-Gallai-Type Theorems for Higher-Dimensional Flats*. 2025. Advisor(s): Jim Geelen. [primary source](https://dspacemainprd01.lib.uwaterloo.ca/server/api/core/bitstreams/faf4b5ff-84de-4d2d-8604-8fbfcc9e00b1/content) Location: Conjecture 7.9, p. 67.

**Literature check.** Status for questions 1750, 1751, 1752, checked 6 October 2026: Checked 6 October 2026; no later resolution found.

**Further links.** [1](https://uwspace.uwaterloo.ca/items/43e52ae6-b54f-4f7f-a2a2-9b708908dcb6) · [2](https://icms.ac.uk/activities/workshop/simegg-structure-in-matroids-embedded-graphs-and-graphs/) · [3](https://uwspace.uwaterloo.ca/items/43e52ae6-b54f-4f7f-a2a2-9b708908dcb6/full)


<a id="q1751"></a>

## Q1751. Ramsey flats with bounded lines

**Status:** Open · **Kind:** conjecture (Conjecture 7.10) · **Collection** 18

For every k,ℓ≥1, does some N(k,ℓ) ensure that every two-colouring of a matroid of rank≥N(k,ℓ), whose lines have at most ℓ points, contains a monochromatic rank-k flat?

**Context.** Origin for questions 1750, 1751, 1752: Geelen’s conjectures, recorded in Chapter 7. Setup for questions 1750, 1751, 1752: Matroids are finite and simple. A rank-k independent flat has exactly k elements. AG(k,p) is the rank-(k+1) affine-geometry matroid on F_p^k.

**Source.** Matthew Eliot Kroeker. *Some Sylvester-Gallai-Type Theorems for Higher-Dimensional Flats*. 2025. Advisor(s): Jim Geelen. [primary source](https://dspacemainprd01.lib.uwaterloo.ca/server/api/core/bitstreams/faf4b5ff-84de-4d2d-8604-8fbfcc9e00b1/content) Location: Conjecture 7.10, p. 68.

**Literature check.** Status for questions 1750, 1751, 1752, checked 6 October 2026: Checked 6 October 2026; no later resolution found.

**Further links.** [1](https://uwspace.uwaterloo.ca/items/43e52ae6-b54f-4f7f-a2a2-9b708908dcb6) · [2](https://icms.ac.uk/activities/workshop/simegg-structure-in-matroids-embedded-graphs-and-graphs/) · [3](https://uwspace.uwaterloo.ca/items/43e52ae6-b54f-4f7f-a2a2-9b708908dcb6/full)


<a id="q1752"></a>

## Q1752. Force affine geometry in fixed characteristic

**Status:** Open · **Kind:** conjecture (Conjecture 7.12) · **Collection** 18

For each prime p and k≥1, does every sufficiently high-rank matroid representable over a field of characteristic p contain either a rank-k independent flat or an AG(k,p)-restriction?

**Context.** Origin for questions 1750, 1751, 1752: Geelen’s conjectures, recorded in Chapter 7. Setup for questions 1750, 1751, 1752: Matroids are finite and simple. A rank-k independent flat has exactly k elements. AG(k,p) is the rank-(k+1) affine-geometry matroid on F_p^k.

**Source.** Matthew Eliot Kroeker. *Some Sylvester-Gallai-Type Theorems for Higher-Dimensional Flats*. 2025. Advisor(s): Jim Geelen. [primary source](https://dspacemainprd01.lib.uwaterloo.ca/server/api/core/bitstreams/faf4b5ff-84de-4d2d-8604-8fbfcc9e00b1/content) Location: Conjecture 7.12, p. 68.

**Literature check.** Status for questions 1750, 1751, 1752, checked 6 October 2026: Checked 6 October 2026; no later resolution found.

**Further links.** [1](https://uwspace.uwaterloo.ca/items/43e52ae6-b54f-4f7f-a2a2-9b708908dcb6) · [2](https://icms.ac.uk/activities/workshop/simegg-structure-in-matroids-embedded-graphs-and-graphs/) · [3](https://uwspace.uwaterloo.ca/items/43e52ae6-b54f-4f7f-a2a2-9b708908dcb6/full)


<a id="q1753"></a>

## Q1753. Find ordinary complex flats at sharp rank

**Status:** Open · **Kind:** conjecture (Conjecture 1.2) · **Collection** 18

For every integer k≥3, must every finite complex-representable matroid of rank at least k+2 have an ordinary rank-k flat?

**Context.** Doctoral context for question 1753: see question 1750. Origin for question 1753: Geelen–Kroeker, Conjecture 1.2 (2022 preprint). Setup for question 1753: A rank-k flat F is ordinary when M|F is the direct sum of a rank-one matroid and a rank-(k−1) matroid.

**Source.** Jim Geelen; Matthew E. Kroeker. *A Sylvester-Gallai-type theorem for complex-representable matroids*. 2024. [primary source](https://arxiv.org/abs/2212.03307) Location: Conjecture 1.2, p. 2; thesis Conjecture 7.3.

**Literature check.** Status for question 1753, checked 6 October 2026: Checked 6 October 2026; no later resolution found.

**Further links.** [1](https://arxiv.org/pdf/2212.03307v2) · [2](https://dspacemainprd01.lib.uwaterloo.ca/server/api/core/bitstreams/faf4b5ff-84de-4d2d-8604-8fbfcc9e00b1/content) · [3](https://uwspace.uwaterloo.ca/items/43e52ae6-b54f-4f7f-a2a2-9b708908dcb6) · [4](https://uwspace.uwaterloo.ca/items/43e52ae6-b54f-4f7f-a2a2-9b708908dcb6/full)


<a id="q1754"></a>

## Q1754. Asymptotic complex line average

**Status:** Open · **Kind:** conjecture (Conjecture 2.1) · **Collection** 18

For n-element complex-representable M of rank 3, is a₂(M)≤3+o_n(1), uniformly in M?

**Context.** Doctoral context for questions 1754, 1755, 1756, 1757, 1758: see question 1750. Origin for questions 1754, 1755, 1756, 1757, 1758: Geelen’s conjectures; authors’ Question 2.5. Setup for questions 1754, 1755, 1756, 1757, 1758: Matroids are finite and simple. Write a_j(M) for mean cardinality of rank-j flats; a(M) averages over all flats.

**Source.** Rutger Campbell; Jim Geelen; Matthew E. Kroeker. *Average plane-size in complex-representable matroids*. 2025. [primary source](https://doi.org/10.1007/s00493-025-00181-z) Location: Conjecture 2.1.

**Literature check.** Status for questions 1754, 1755, 1756, 1757, 1758, checked 6 October 2026: Rechecked 6 October 2026; no resolution found.

**Further links.** [1](https://arxiv.org/abs/2310.02826) · [2](https://arxiv.org/html/2310.02826v2) · [3](https://dspacemainprd01.lib.uwaterloo.ca/server/api/core/bitstreams/faf4b5ff-84de-4d2d-8604-8fbfcc9e00b1/content) · [4](https://uwspace.uwaterloo.ca/items/43e52ae6-b54f-4f7f-a2a2-9b708908dcb6) · [5](https://uwspace.uwaterloo.ca/items/43e52ae6-b54f-4f7f-a2a2-9b708908dcb6/full)


<a id="q1755"></a>

## Q1755. Asymptotic complex plane average

**Status:** Open · **Kind:** conjecture (Conjecture 2.2) · **Collection** 18

For n-element complex-representable M of rank 4, not a union of two lines, is a₃(M)≤6+o_n(1), uniformly in M?

**Context.** Doctoral context for questions 1754, 1755, 1756, 1757, 1758: see question 1750. Origin for questions 1754, 1755, 1756, 1757, 1758: Geelen’s conjectures; authors’ Question 2.5. Setup for questions 1754, 1755, 1756, 1757, 1758: Matroids are finite and simple. Write a_j(M) for mean cardinality of rank-j flats; a(M) averages over all flats.

**Source.** Rutger Campbell; Jim Geelen; Matthew E. Kroeker. *Average plane-size in complex-representable matroids*. 2025. [primary source](https://doi.org/10.1007/s00493-025-00181-z) Location: Conjecture 2.2.

**Literature check.** Status for questions 1754, 1755, 1756, 1757, 1758, checked 6 October 2026: Rechecked 6 October 2026; no resolution found.

**Further links.** [1](https://arxiv.org/abs/2310.02826) · [2](https://arxiv.org/html/2310.02826v2) · [3](https://dspacemainprd01.lib.uwaterloo.ca/server/api/core/bitstreams/faf4b5ff-84de-4d2d-8604-8fbfcc9e00b1/content) · [4](https://uwspace.uwaterloo.ca/items/43e52ae6-b54f-4f7f-a2a2-9b708908dcb6) · [5](https://uwspace.uwaterloo.ca/items/43e52ae6-b54f-4f7f-a2a2-9b708908dcb6/full)


<a id="q1756"></a>

## Q1756. Bound planes from mean line length

**Status:** Open · **Kind:** conjecture (Conjecture 2.6) · **Collection** 18

For every α>0, does some β>0 satisfy a₂(M)≤α ⇒ a₃(M)≤β whenever r(M)≥6?

**Context.** Doctoral context for questions 1754, 1755, 1756, 1757, 1758: see question 1750. Origin for questions 1754, 1755, 1756, 1757, 1758: Geelen’s conjectures; authors’ Question 2.5. Setup for questions 1754, 1755, 1756, 1757, 1758: Matroids are finite and simple. Write a_j(M) for mean cardinality of rank-j flats; a(M) averages over all flats.

**Source.** Rutger Campbell; Jim Geelen; Matthew E. Kroeker. *Average plane-size in complex-representable matroids*. 2025. [primary source](https://doi.org/10.1007/s00493-025-00181-z) Location: Conjecture 2.6.

**Literature check.** Status for questions 1754, 1755, 1756, 1757, 1758, checked 6 October 2026: Rechecked 6 October 2026; no resolution found.

**Further links.** [1](https://arxiv.org/abs/2310.02826) · [2](https://arxiv.org/html/2310.02826v2) · [3](https://dspacemainprd01.lib.uwaterloo.ca/server/api/core/bitstreams/faf4b5ff-84de-4d2d-8604-8fbfcc9e00b1/content) · [4](https://uwspace.uwaterloo.ca/items/43e52ae6-b54f-4f7f-a2a2-9b708908dcb6) · [5](https://uwspace.uwaterloo.ca/items/43e52ae6-b54f-4f7f-a2a2-9b708908dcb6/full)


<a id="q1757"></a>

## Q1757. Bound lines from mean plane size

**Status:** Open · **Kind:** conjecture (Conjecture 2.7) · **Collection** 18

For every β>0, does some α>0 satisfy a₃(M)≤β ⇒ a₂(M)≤α whenever r(M)≥4?

**Context.** Doctoral context for questions 1754, 1755, 1756, 1757, 1758: see question 1750. Origin for questions 1754, 1755, 1756, 1757, 1758: Geelen’s conjectures; authors’ Question 2.5. Setup for questions 1754, 1755, 1756, 1757, 1758: Matroids are finite and simple. Write a_j(M) for mean cardinality of rank-j flats; a(M) averages over all flats.

**Source.** Rutger Campbell; Jim Geelen; Matthew E. Kroeker. *Average plane-size in complex-representable matroids*. 2025. [primary source](https://doi.org/10.1007/s00493-025-00181-z) Location: Conjecture 2.7.

**Literature check.** Status for questions 1754, 1755, 1756, 1757, 1758, checked 6 October 2026: Rechecked 6 October 2026; no resolution found.

**Further links.** [1](https://arxiv.org/abs/2310.02826) · [2](https://arxiv.org/html/2310.02826v2) · [3](https://dspacemainprd01.lib.uwaterloo.ca/server/api/core/bitstreams/faf4b5ff-84de-4d2d-8604-8fbfcc9e00b1/content) · [4](https://uwspace.uwaterloo.ca/items/43e52ae6-b54f-4f7f-a2a2-9b708908dcb6) · [5](https://uwspace.uwaterloo.ca/items/43e52ae6-b54f-4f7f-a2a2-9b708908dcb6/full)


<a id="q1758"></a>

## Q1758. Sharp average size of complex flats

**Status:** Open · **Kind:** conjecture (Conjecture 2.3) · **Collection** 18

For every fixed r≥3, is a(M)≤binom(r,2)+o_n(1), uniformly over n-element complex-representable matroids M of rank r?

**Context.** Doctoral context for questions 1754, 1755, 1756, 1757, 1758: see question 1750. Origin for questions 1754, 1755, 1756, 1757, 1758: Geelen’s conjectures; authors’ Question 2.5. Setup for questions 1754, 1755, 1756, 1757, 1758: Matroids are finite and simple. Write a_j(M) for mean cardinality of rank-j flats; a(M) averages over all flats.

**Source.** Rutger Campbell; Jim Geelen; Matthew E. Kroeker. *Average plane-size in complex-representable matroids*. 2025. [primary source](https://doi.org/10.1007/s00493-025-00181-z) Location: Conjecture 2.3.

**Literature check.** Status for questions 1754, 1755, 1756, 1757, 1758, checked 6 October 2026: Rechecked 6 October 2026; no resolution found.

**Further links.** [1](https://arxiv.org/abs/2310.02826) · [2](https://arxiv.org/html/2310.02826v2) · [3](https://dspacemainprd01.lib.uwaterloo.ca/server/api/core/bitstreams/faf4b5ff-84de-4d2d-8604-8fbfcc9e00b1/content) · [4](https://uwspace.uwaterloo.ca/items/43e52ae6-b54f-4f7f-a2a2-9b708908dcb6) · [5](https://uwspace.uwaterloo.ca/items/43e52ae6-b54f-4f7f-a2a2-9b708908dcb6/full)


<a id="q1759"></a>

## Q1759. Reach half the points in incident lines

**Status:** Open · **Kind:** open problem · **Collection** 18

Is there an absolute C such that every finite simple real-representable matroid M of rank≥3 on n elements has an element contained in at least n/2−C rank-two flats?

**Context.** Doctoral context for question 1759: see question 1750. Origin for question 1759: Brass–Moser–Pach’s strong asymptotic form (2005), following Dirac–Motzkin; recalled here.

**Source.** Rutger Campbell; Matthew E. Kroeker; Ben Lund. *Characterizing real-representable matroids with large average hyperplane-size*. 2025. [primary source](https://arxiv.org/abs/2410.05513) Location: §2, paragraph immediately after the Weak Dirac Theorem, p. 9.

**Literature check.** Status for question 1759, checked 6 October 2026: Checked 6 October 2026; no later resolution found.

**Further links.** [1](https://arxiv.org/html/2410.05513) · [2](https://arxiv.org/abs/1202.3110) · [3](https://arxiv.org/html/2501.18406) · [4](https://uwspace.uwaterloo.ca/items/43e52ae6-b54f-4f7f-a2a2-9b708908dcb6) · [5](https://uwspace.uwaterloo.ca/items/43e52ae6-b54f-4f7f-a2a2-9b708908dcb6/full) · [6](https://dspacemainprd01.lib.uwaterloo.ca/server/api/core/bitstreams/faf4b5ff-84de-4d2d-8604-8fbfcc9e00b1/content)


<a id="q1760"></a>

## Q1760. Pin down ternary Dowling extension scale

**Status:** Open · **Kind:** conjecture (Conjecture 10.0.2) · **Collection** 18

Does some c∈[1/2,1] satisfy log₂ ext(D_n)=n2^{n−1}(c+o(1))?

**Context.** Origin for questions 1760, 1761: Redlin Hume’s Conjectures 8.0.3 and 10.0.2. Setup for questions 1760, 1761: ext(M), coext(M) count single-element extensions and coextensions on fixed E(M)∪{e}, with deletion or contraction of e equal to M. Logs are base two; n→∞. PG(n−1,q) is rank-n projective geometry. D_n is the ternary column matroid of {e_i}∪{e_i±e_j:i&lt;j}.

**Source.** Shayla Redlin Hume. *Enumerating matroid extensions*. 2023. Advisor(s): Peter Nelson. [primary source](https://uwspace.uwaterloo.ca/bitstreams/1f9d04c8-605a-4bab-8fa4-a1b65cced5fd/download) Location: Conjecture 10.0.2, p. 127.

**Literature check.** Status for questions 1760, 1761, checked 6 October 2026: Checked 6 October 2026; no later resolution found.

**Further links.** [1](https://uwspace.uwaterloo.ca/items/6beb66c9-6da5-425e-90e9-74df74e472c6)


<a id="q1761"></a>

## Q1761. Sharpen projective coextension enumeration

**Status:** Open · **Kind:** conjecture (Conjecture 8.0.3) · **Collection** 18

For each fixed prime power q≥3, is there a constant c=c(q) such that log₂ coext(PG(n−1,q))=[q^{n²}/(n!(q−1)^n)\](c+o(1))?

**Context.** Origin for questions 1760, 1761: Redlin Hume’s Conjectures 8.0.3 and 10.0.2. Setup for questions 1760, 1761: ext(M), coext(M) count single-element extensions and coextensions on fixed E(M)∪{e}, with deletion or contraction of e equal to M. Logs are base two; n→∞. PG(n−1,q) is rank-n projective geometry. D_n is the ternary column matroid of {e_i}∪{e_i±e_j:i&lt;j}.

**Source.** Shayla Redlin Hume. *Enumerating matroid extensions*. 2023. Advisor(s): Peter Nelson. [primary source](https://uwspace.uwaterloo.ca/bitstreams/1f9d04c8-605a-4bab-8fa4-a1b65cced5fd/download) Location: Conjecture 8.0.3, p. 109.

**Literature check.** Status for questions 1760, 1761, checked 6 October 2026: Checked 6 October 2026; no later resolution found.

**Further links.** [1](https://uwspace.uwaterloo.ca/items/6beb66c9-6da5-425e-90e9-74df74e472c6)


<a id="q1763"></a>

## Q1763. Count connected chordal diagrams

**Status:** Open · **Kind:** conjecture (Conjecture 8.5) · **Collection** 18

For m≥1, are there exactly C_{m−1}² size-m diagrams whose intersection graph is connected and chordal (has no induced cycle of length≥4)?

**Context.** Doctoral context for questions 1763, 1764, 1765: Lukas Nabergall. Enumerative perspectives on chord diagrams. PhD, University of Waterloo, 2022. Advisor: Karen Yeats. Origin for questions 1763, 1764, 1765: Nabergall’s conjectures; also thesis Table 5.1. Setup for questions 1763, 1764, 1765: A size-m chord diagram is a perfect matching of [2m]. Crossing chords alternate endpoints. Its intersection graph joins crossings and orients them by increasing left endpoint. A terminal chord has outdegree zero. Let C_j=binom(2j,j)/(j+1). Set binom(a,b)=0 when b<0 or b>a.

**Source.** Lukas Nabergall. *The combinatorics of a tree-like functional equation for connected chord diagrams*. 2023. Advisor(s): Karen Yeats. [primary source](https://escholarship.org/uc/item/1qg5647z) Location: Conjecture 8.5.

**Literature check.** Status for questions 1763, 1764, 1765, checked 6 October 2026: Checked 6 October 2026; no later resolution found.

**Further links.** [1](https://arxiv.org/abs/2104.02296) · [2](https://escholarship.org/content/qt1qg5647z/qt1qg5647z_noSplash_7c4e7857ef028cae7bff428d260da921.pdf?t=s622w9) · [3](https://uwspace.uwaterloo.ca/items/51239c85-b044-4e6b-97c6-710332c37c93) · [4](https://doi.org/10.1112/jlms.70006) · [5](https://uwspace.uwaterloo.ca/bitstreams/0c42ca6c-8939-48b8-9e44-81734e59f8d5/download) · [6](https://www.math.uwaterloo.ca/~kayeats/students.html)


<a id="q1764"></a>

## Q1764. Count terminal bipartite diagrams

**Status:** Open · **Kind:** conjecture (Conjecture 8.10) · **Collection** 18

For m≥2, is the number of size-m diagrams with bipartite intersection graph and exactly one terminal chord equal to Σ\_{j=1}^{m−1} binom(m,j−1)binom(m,j)binom(m,j+1)/[binom(m,1)binom(m,2)]?

**Context.** Doctoral context for questions 1763, 1764, 1765: Lukas Nabergall. Enumerative perspectives on chord diagrams. PhD, University of Waterloo, 2022. Advisor: Karen Yeats. Origin for questions 1763, 1764, 1765: Nabergall’s conjectures; also thesis Table 5.1. Setup for questions 1763, 1764, 1765: A size-m chord diagram is a perfect matching of [2m]. Crossing chords alternate endpoints. Its intersection graph joins crossings and orients them by increasing left endpoint. A terminal chord has outdegree zero. Let C_j=binom(2j,j)/(j+1). Set binom(a,b)=0 when b<0 or b>a.

**Source.** Lukas Nabergall. *The combinatorics of a tree-like functional equation for connected chord diagrams*. 2023. Advisor(s): Karen Yeats. [primary source](https://escholarship.org/uc/item/1qg5647z) Location: Conjecture 8.10.

**Literature check.** Status for questions 1763, 1764, 1765, checked 6 October 2026: Checked 6 October 2026; no later resolution found.

**Further links.** [1](https://arxiv.org/abs/2104.02296) · [2](https://escholarship.org/content/qt1qg5647z/qt1qg5647z_noSplash_7c4e7857ef028cae7bff428d260da921.pdf?t=s622w9) · [3](https://uwspace.uwaterloo.ca/items/51239c85-b044-4e6b-97c6-710332c37c93) · [4](https://doi.org/10.1112/jlms.70006) · [5](https://uwspace.uwaterloo.ca/bitstreams/0c42ca6c-8939-48b8-9e44-81734e59f8d5/download) · [6](https://www.math.uwaterloo.ca/~kayeats/students.html)


<a id="q1765"></a>

## Q1765. Count terminal triangle-free diagrams

**Status:** Open · **Kind:** conjecture (Conjecture 8.9) · **Collection** 18

For m≥3, is the number of size-m diagrams with triangle-free intersection graph and exactly one terminal chord equal to [24/((m−2)(m−1)²m(m+1))] Σ\_{j=0}^{m−1} binom(m−1,j+2)binom(m+1,j)binom(m+j+1,j+1)?

**Context.** Doctoral context for questions 1763, 1764, 1765: Lukas Nabergall. Enumerative perspectives on chord diagrams. PhD, University of Waterloo, 2022. Advisor: Karen Yeats. Origin for questions 1763, 1764, 1765: Nabergall’s conjectures; also thesis Table 5.1. Setup for questions 1763, 1764, 1765: A size-m chord diagram is a perfect matching of [2m]. Crossing chords alternate endpoints. Its intersection graph joins crossings and orients them by increasing left endpoint. A terminal chord has outdegree zero. Let C_j=binom(2j,j)/(j+1). Set binom(a,b)=0 when b<0 or b>a.

**Source.** Lukas Nabergall. *The combinatorics of a tree-like functional equation for connected chord diagrams*. 2023. Advisor(s): Karen Yeats. [primary source](https://escholarship.org/uc/item/1qg5647z) Location: Conjecture 8.9.

**Literature check.** Status for questions 1763, 1764, 1765, checked 6 October 2026: Checked 6 October 2026; no later resolution found.

**Further links.** [1](https://arxiv.org/abs/2104.02296) · [2](https://escholarship.org/content/qt1qg5647z/qt1qg5647z_noSplash_7c4e7857ef028cae7bff428d260da921.pdf?t=s622w9) · [3](https://uwspace.uwaterloo.ca/items/51239c85-b044-4e6b-97c6-710332c37c93) · [4](https://doi.org/10.1112/jlms.70006) · [5](https://uwspace.uwaterloo.ca/bitstreams/0c42ca6c-8939-48b8-9e44-81734e59f8d5/download) · [6](https://www.math.uwaterloo.ca/~kayeats/students.html)


<a id="q1766"></a>

## Q1766. Exact edge multiset dimension of the six-cube

**Status:** Open, partial results · **Kind:** open problem · **Collection** 18

What is the edge multiset dimension of Q₆, the graph on {0,1}⁶ with adjacency at Hamming distance one?

**Context.** Origin for question 1766: Author’s question after disproving universal infinity. Setup for question 1766: For e=uv, d(e,s)=min{d(u,s),d(v,s)}. The edge multiset dimension is the least |S| such that the multisets {d(e,s):s∈S} are different for all edges e.

**Source.** Jaan Allikvere. *The edge multiset dimension of hypercubes*. 2026. [primary source](https://arxiv.org/abs/2608.09983) Location: §10, Open problem 1.

**Literature check.** Status for question 1766, checked 6 October 2026: currently 6≤edim_m(Q₆)≤15.

**Results.**

- **Partial result**: Computer-assisted interval narrowed to 13–15; exact value remains. Remaining: partial Recorded from the external B7 return  (backfilled 2026-10-08); selected local controls in the intake; external archive not uploaded; not independently re-derived here. [Details](../../solutions/b7-2026-10-07/B7_Research_Report_2026-10-07.md).
- **Related result** (B7-R05: submitted proved): 13 <= edim_m(Q6) <= 15; an independent elementary proof gives the lower bound 8. Remaining/limits: Exclude sizes 13 and 14 or exhibit a smaller resolving set to determine the exact value. Locally verified interval is 8–15; submitted 13–15 depends on missing search records. [Report](../../solutions/b7-2026-10-07/README.md).

**Further links.** [1](https://arxiv.org/html/2608.09983)


<a id="q1852"></a>

## Q1852. Force Hamilton cycles in path powers

**Status:** Open · **Kind:** conjecture (Conjecture 6) · **Collection** 19

For integers n≥4 and k≥2, must every spanning G⊆P_n^k satisfying deg_G(v)≥deg_(P_n^k)(v)/2+2 for every vertex v be Hamiltonian?

**Context.** Origin for questions 1852, 1853: Cycle question: Espuny Díaz–Lichev–Wesolek, Conjecture 1.13 (2024); path question: these authors. Setup for questions 1852, 1853: P_n and C_n are the n-vertex path and cycle. H^k joins distinct vertices at H-distance≤k; subgraphs below are spanning. Hamiltonian means containing a cycle through every vertex.

**Source.** Alberto Espuny Díaz; Pranshu Gupta; Domenico Mergoni Cecchelli; Olaf Parczyk; Amedeo Sgueglia. *Dirac’s Theorem for Graphs of Bounded Bandwidth*. 2026. [primary source](https://doi.org/10.37236/13474) Location: Conjecture 6, §1.2, p. 4.

**Literature check.** Status for questions 1852, 1853, checked 6 October 2026: Explicitly conjectured in January 2026; no later resolution found by 6 October.

**Further links.** [1](https://arxiv.org/abs/2407.05889) · [2](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v33i1p21/pdf/)


<a id="q1853"></a>

## Q1853. Force Hamilton cycles in cycle powers

**Status:** Open · **Kind:** conjecture (Conjecture 1) · **Collection** 19

For integers n≥3 and 1≤k≤floor(n/2), must every spanning G⊆C_n^k with minimum degree at least k+1 be Hamiltonian?

**Context.** Origin for questions 1852, 1853: Cycle question: Espuny Díaz–Lichev–Wesolek, Conjecture 1.13 (2024); path question: these authors. Setup for questions 1852, 1853: P_n and C_n are the n-vertex path and cycle. H^k joins distinct vertices at H-distance≤k; subgraphs below are spanning. Hamiltonian means containing a cycle through every vertex.

**Source.** Alberto Espuny Díaz; Pranshu Gupta; Domenico Mergoni Cecchelli; Olaf Parczyk; Amedeo Sgueglia. *Dirac’s Theorem for Graphs of Bounded Bandwidth*. 2026. [primary source](https://doi.org/10.37236/13474) Location: Conjecture 1, p. 2.

**Literature check.** Status for questions 1852, 1853, checked 6 October 2026: Explicitly conjectured in January 2026; no later resolution found by 6 October.

**Further links.** [1](https://arxiv.org/abs/2407.05889) · [2](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v33i1p21/pdf/)


<a id="q1854"></a>

## Q1854. Find low-rank triangle-free graphs

**Status:** Open · **Kind:** open problem (Problem 8.1) · **Collection** 19

Is there an absolute c>0 such that ν₂(n)=O(n^{1−c}) as n→∞?

**Context.** Origin for question 1854: Beniamini–Linial–Shraibman (2024 preprint). Setup for question 1854: For an n-vertex simple graph G, A_G is its adjacency matrix, ω(G) its clique number, and rank is over R. Set ν\_d(n)=min{rank(A_G+I):|V(G)|=n, ω(G)≤d}.

**Source.** Gal Beniamini; Nati Linial; Adi Shraibman. *The Rank-Ramsey problem and the Log-Rank conjecture*. 2026. [primary source](https://doi.org/10.1017/S0963548326100455) Location: Open Problem 8.1, §8 in journal; Open Problem 1 in preprint.

**Literature check.** Status for question 1854, checked 6 October 2026: Explicitly open in May 2026; no later resolution found by 6 October.

**Further links.** [1](https://arxiv.org/abs/2405.07337) · [2](https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/rankramsey-problem-and-the-logrank-conjecture/C656F3CCA0D66CEC93B4B5F16264BC4F)


<a id="q1855"></a>

## Q1855. Attain the cubelike cospectral bound

**Status:** Open · **Kind:** open problem · **Collection** 19

For every integer d≥7, is there a cubelike graph on F₂^d with 2^{ceil(d/2)−1} pairwise strongly cospectral vertices?

**Context.** Doctoral context for question 1855: see question 1858. Origin for question 1855: 2021 preprint; thesis §7.1. Setup for question 1855: For a finite simple graph with adjacency matrix A and spectral projections E_θ, vertices u,v are strongly cospectral when E_θe_u=±E_θe_v for every θ. A cubelike graph has vertex set F₂^d and edges xy when x−y belongs to a chosen subset of F₂^d∖{0}.

**Source.** Arnbjörg Soffía Árnadóttir; Chris Godsil. *Strongly cospectral vertices in normal Cayley graphs*. 2023. [primary source](https://arxiv.org/abs/2109.07568) Location: §11, first question; Corollary 8.3.

**Literature check.** Status for question 1855, checked 6 October 2026: no later resolution found.

**Further links.** [1](https://doi.org/10.1016/j.disc.2023.113341) · [2](https://dspacemainprd01.lib.uwaterloo.ca/server/api/core/bitstreams/ac8e8558-6e66-4ed3-902d-39de37164fb4/content) · [3](https://arxiv.org/abs/2207.05211) · [4](https://people.clas.ufl.edu/sin/research/)


<a id="q1856"></a>

## Q1856. Classify valency-three distance-biregular graphs

**Status:** Open · **Kind:** open problem (Problem 3.6.3) · **Collection** 19

Classify the distance-biregular graphs in which every vertex of one bipartition class has degree three.

**Context.** Doctoral context for questions 1856, 1857, 1862, 1863, 1864, 1865, 1866, 1867, 1868: given in the source heading above. Origin for questions 1856, 1857: Lato’s Problems 3.3.1 and 3.6.3; earlier partial classifications cited there. Setup for questions 1856, 1857: Graphs are finite, simple and connected. A bipartite graph with parts Y,Z is distance-biregular if, for vertices u,v at distance i, the numbers of neighbours of v at distances i−1 and i+1 from u depend only on i and the part containing u. A halved graph joins pairs in one part at distance two.

**Source.** Sabrina Lato. *Distance-Biregular Graphs and Orthogonal Polynomials*. 2023. Advisor(s): Chris Godsil. [primary source](https://dspacemainprd01.lib.uwaterloo.ca/server/api/core/bitstreams/ced0fd0d-ebb6-4aa4-b2f4-699597bf3bbe/content) Location: Problem 3.6.3, p. 55; restated pp. 113–114.

**Literature check.** Status for questions 1856, 1857, checked 6 October 2026: Checked 6 October 2026; no later resolution found.

**Further links.** [1](https://uwspace.uwaterloo.ca/items/97b78c88-5c14-44ee-bd7a-6c6469c10eca) · [2](https://arxiv.org/abs/2504.21488)


<a id="q1857"></a>

## Q1857. Classify distance-biregular halves

**Status:** Open · **Kind:** open problem (Problem 3.3.1) · **Collection** 19

Which finite connected distance-regular graphs occur as halved graphs of distance-biregular graphs?

**Context.** Doctoral context for questions 1856, 1857, 1862, 1863, 1864, 1865, 1866, 1867, 1868: given in the source heading above. Origin for questions 1856, 1857: Lato’s Problems 3.3.1 and 3.6.3; earlier partial classifications cited there. Setup for questions 1856, 1857: Graphs are finite, simple and connected. A bipartite graph with parts Y,Z is distance-biregular if, for vertices u,v at distance i, the numbers of neighbours of v at distances i−1 and i+1 from u depend only on i and the part containing u. A halved graph joins pairs in one part at distance two.

**Source.** Sabrina Lato. *Distance-Biregular Graphs and Orthogonal Polynomials*. 2023. Advisor(s): Chris Godsil. [primary source](https://dspacemainprd01.lib.uwaterloo.ca/server/api/core/bitstreams/ced0fd0d-ebb6-4aa4-b2f4-699597bf3bbe/content) Location: Problem 3.3.1, p. 45; restated p. 113.

**Literature check.** Status for questions 1856, 1857, checked 6 October 2026: Checked 6 October 2026; no later resolution found.

**Further links.** [1](https://uwspace.uwaterloo.ca/items/97b78c88-5c14-44ee-bd7a-6c6469c10eca) · [2](https://arxiv.org/abs/2504.21488)


<a id="q1858"></a>

## Q1858. Determine earliest transfer time

**Status:** Open · **Kind:** open problem · **Collection** 19

If G has a cyclic Sylow-2-subgroup and Cay(G,C) admits perfect state transfer, must the least positive transfer time between distinct vertices be π/2?

**Context.** Doctoral context for questions 1855, 1858: given in the source heading above. Origin for question 1858: Thesis §7.2 conjecture. Setup for question 1858: For finite G and inverse- and conjugacy-closed C⊆G∖{e}, let A be the adjacency matrix of Cay(G,C). Perfect state transfer from u to v≠u at time t>0 means |(exp(itA))\_(u,v)|=1.

**Source.** Arnbjörg Soffía Árnadóttir. *State Transfer & Strong Cospectrality in Cayley Graphs*. 2022. Advisor(s): Chris Godsil. [primary source](https://dspacemainprd01.lib.uwaterloo.ca/server/api/core/bitstreams/ac8e8558-6e66-4ed3-902d-39de37164fb4/content) Location: §7.2, p. 113.

**Literature check.** Status for question 1858, checked 6 October 2026: no later resolution found.

**Further links.** [1](https://arxiv.org/abs/2204.09802) · [2](https://doi.org/10.1007/s11128-022-03751-y) · [3](https://arxiv.org/abs/2609.23633)


<a id="q1859"></a>

## Q1859. Exclude unbalanced near-polygon diameters

**Status:** Open · **Kind:** open problem · **Collection** 19

Is there no unbalanced distance-biregular graph of diameter d≥8 and girth 2d−2?

**Context.** Origin for question 1859: Argenti–Siciliano; motivated by Lato’s thesis Problem 5.5.2. Setup for question 1859: A finite simple connected bipartite graph is distance-biregular when its distance-partition intersection numbers depend only on the root’s part. It is unbalanced when vertices in its two parts have different eccentricities (maximum distances), not merely different degrees. Girth deficiency is twice its diameter minus its girth.

**Source.** Sebastiano Argenti; Alessandro Siciliano. *Unbalanced distance-biregular graphs with girth deficiency two*. 2026. [primary source](https://arxiv.org/abs/2609.07817) Location: §7, unnumbered conjecture, p. 55, immediately before Table 2.

**Literature check.** Status for question 1859, checked 6 October 2026: Conjectured September 2026. Remaining even diameters: 8–26, 48, 50 (Theorem 6.15). No later resolution found through 6 October.

**Further links.** [1](https://arxiv.org/html/2609.07817v1) · [2](https://dspacemainprd01.lib.uwaterloo.ca/server/api/core/bitstreams/ced0fd0d-ebb6-4aa4-b2f4-699597bf3bbe/content)


<a id="q1860"></a>

## Q1860. Settle the rainbow Schur density

**Status:** Open · **Kind:** open problem (Problem 1.2) · **Collection** 19

Is lim_(n→∞) Λ\_(n,3)=9/22?

**Context.** Origin for questions 1860, 1861: Counting problem: Parczyk–Spiegel (2024); the 9/22 proposal is Hegde–Kumar–Pratibha’s. Setup for questions 1860, 1861: For c:[n]→[k], let R_n(c) count ordered pairs (x,y) with x+y≤n and c(x),c(y),c(x+y) pairwise distinct. Set Λ\_(n,k)=max_c R_n(c)/binom(n,2).

**Source.** Swaroop Hegde; Hitesh Kumar; Pratibha. *A somewhat sure note on an un-Schur problem*. 2026. [primary source](https://arxiv.org/abs/2609.18474) Location: Problem 1.2, §1.

**Literature check.** Status for questions 1860, 1861, checked 6 October 2026: Explicitly unresolved 16 September 2026; rechecked 6 October.

**Results.**

- **Investigated, unresolved** (B2: submitted unresolved): Exploratory three-color interval/residue searches did not beat 9/22; no certificate of optimality was produced. Remaining/limits: The claimed limiting value 9/22 is neither proved nor disproved. [Report](../../solutions/b2-2026-10-07/README.md).

**Further links.** [1](https://arxiv.org/html/2609.18474v1) · [2](https://doi.org/10.37236/13554)


<a id="q1861"></a>

## Q1861. Find the four-colour Schur density

**Status:** Open, partial results · **Kind:** open problem · **Collection** 19

Determine liminf_(n→∞) Λ\_(n,4) and limsup_(n→∞) Λ\_(n,4), including whether they coincide.

**Context.** Origin for questions 1860, 1861: Counting problem: Parczyk–Spiegel (2024); the 9/22 proposal is Hegde–Kumar–Pratibha’s. Setup for questions 1860, 1861: For c:[n]→[k], let R_n(c) count ordered pairs (x,y) with x+y≤n and c(x),c(y),c(x+y) pairwise distinct. Set Λ\_(n,k)=max_c R_n(c)/binom(n,2).

**Source.** Swaroop Hegde; Hitesh Kumar; Pratibha. *A somewhat sure note on an un-Schur problem*. 2026. [primary source](https://arxiv.org/abs/2609.18474) Location: §1, paragraph after Theorem 1.3, highlighting k=4.

**Literature check.** Status for questions 1860, 1861, checked 6 October 2026: Explicitly unresolved 16 September 2026; rechecked 6 October.

**Results.**

- **Partial result**: Independently verified root-agent construction giving density50368/90905 by exact integer lattice counts at n=t·90905 for t=1,2,3,10,100; checked rectangle counting formula in2548 small cases. Proved liminf Lambda_(n,4)>=50368/90905 with an explicit nine-interval coloring. For all integers t>=1, R_(90905t)=2289351520t^2+25184t; an integer inclusion-exclusion identity certifies every scale. Restricted scope: No hypothesis restriction for the lower-bound theorem; only a one-sided conclusion from the retained determination problem is proved. Remaining: The exact liminf, limsup, and their equality remain unresolved; the cited upper bound 3/4 remains. Recorded from the external B2 return  (backfilled 2026-10-08); selected exact checks in the intake; verification archive not uploaded; not independently re-derived here. [Details](../../solutions/b2-2026-10-07/B2_Research_Report_2026-10-07.md).
- **Related result** (B2-R1: auxiliary proof submission): liminf Lambda_(n,4)>=50368/90905; exact nine-interval count R_(90905t)=2289351520t^2+25184t for every integer t>=1. Location: Part A, section 1. Full retained question(s) remain unresolved; consult intake checks and archive limits. [Report](../../solutions/b2-2026-10-07/README.md).

**Further links.** [1](https://arxiv.org/html/2609.18474v1) · [2](https://doi.org/10.37236/13554)


<a id="q1862"></a>

## Q1862. Sharpen hypergrid saturation growth

**Status:** Open · **Kind:** conjecture (Conjecture 1.8) · **Collection** 19

For each fixed P and t≥2, is s_t(n,P) either O(1) or cn+o(n) for some c=c(P,t)>0 as n→∞?

**Context.** Doctoral context for questions 1862, 1863, 1864: see question 1856. Origin for questions 1862, 1863, 1864: Çiçeksiz–Falgas-Ravry–Lato–Sharifzadeh; extends Boolean-lattice saturation questions. Setup for questions 1862, 1863, 1864: For a finite nonempty poset P, order [t]^n coordinatewise. Where P embeds, s_t(n,P) is the least size of a family containing no induced P but acquiring one after any missing element of [t]^n is added. Induced embeddings preserve and reflect order; t≥2.

**Source.** R. Altar Çiçeksiz; Victor Falgas-Ravry; Sabrina Lato; Maryam Sharifzadeh. *Induced poset saturation in the hypergrid*. 2026. [primary source](https://arxiv.org/abs/2604.12641) Location: Conjecture 1.8, p. 4.

**Literature check.** Status for questions 1862, 1863, 1864, checked 6 October 2026: Explicitly open April 2026; no later resolution found by 6 October.

**Further links.** [1](https://arxiv.org/html/2604.12641v1) · [2](https://doi.org/10.1112/mtk.70115) · [3](https://arxiv.org/abs/2509.10294)


<a id="q1863"></a>

## Q1863. Prove hypergrid saturation monotonicity

**Status:** Open · **Kind:** conjecture (Conjecture 1.9) · **Collection** 19

Is s_t(n,P) nondecreasing in each of n and t throughout the integer parameter domain where P embeds?

**Context.** Doctoral context for questions 1862, 1863, 1864: see question 1856. Origin for questions 1862, 1863, 1864: Çiçeksiz–Falgas-Ravry–Lato–Sharifzadeh; extends Boolean-lattice saturation questions. Setup for questions 1862, 1863, 1864: For a finite nonempty poset P, order [t]^n coordinatewise. Where P embeds, s_t(n,P) is the least size of a family containing no induced P but acquiring one after any missing element of [t]^n is added. Induced embeddings preserve and reflect order; t≥2.

**Source.** R. Altar Çiçeksiz; Victor Falgas-Ravry; Sabrina Lato; Maryam Sharifzadeh. *Induced poset saturation in the hypergrid*. 2026. [primary source](https://arxiv.org/abs/2604.12641) Location: Conjecture 1.9, p. 4.

**Literature check.** Status for questions 1862, 1863, 1864, checked 6 October 2026: Explicitly open April 2026; no later resolution found by 6 October.

**Further links.** [1](https://arxiv.org/html/2604.12641v1) · [2](https://doi.org/10.1112/mtk.70115) · [3](https://arxiv.org/abs/2509.10294)


<a id="q1864"></a>

## Q1864. Change boundedness with grid side length

**Status:** Open · **Kind:** open problem · **Collection** 19

Do there exist a finite poset P and integer T≥3 such that s₂(n,P)=O(1) but s_T(n,P)=Ω(sqrt(n)) as n→∞?

**Context.** Doctoral context for questions 1862, 1863, 1864: see question 1856. Origin for questions 1862, 1863, 1864: Çiçeksiz–Falgas-Ravry–Lato–Sharifzadeh; extends Boolean-lattice saturation questions. Setup for questions 1862, 1863, 1864: For a finite nonempty poset P, order [t]^n coordinatewise. Where P embeds, s_t(n,P) is the least size of a family containing no induced P but acquiring one after any missing element of [t]^n is added. Induced embeddings preserve and reflect order; t≥2.

**Source.** R. Altar Çiçeksiz; Victor Falgas-Ravry; Sabrina Lato; Maryam Sharifzadeh. *Induced poset saturation in the hypergrid*. 2026. [primary source](https://arxiv.org/abs/2604.12641) Location: §3, side-length question, p. 14.

**Literature check.** Status for questions 1862, 1863, 1864, checked 6 October 2026: Explicitly open April 2026; no later resolution found by 6 October.

**Further links.** [1](https://arxiv.org/html/2604.12641v1) · [2](https://doi.org/10.1112/mtk.70115) · [3](https://arxiv.org/abs/2509.10294)


<a id="q1865"></a>

## Q1865. Recognize underlying incidence Cayley graphs

**Status:** Open · **Kind:** open problem (Question 10.1) · **Collection** 19

Characterize inverse-closed S⊆G∖{e} admitting such cells with ℓ≥2,k≥3 and ⋃C_i∖{e}=S.

**Context.** Doctoral context for questions 1865, 1866, 1867: see question 1856. Origin for questions 1865, 1866, 1867: Authors’ Questions 10.1, 10.3 and Problem 10.7. Setup for questions 1865, 1866, 1867: Let G be finite. Cells π={C₁,…,C_ℓ} contain e, have common size k, pairwise intersection {e}, and satisfy s⁻¹C∈π for C∈π,s∈C. Cin(G,π) has parts G and the distinct sets gC, with incidence by membership. It is (ℓ,k)-biregular; its underlying Cayley graph has connection set ⋃C_i∖{e}.

**Source.** Arnbjörg Soffía Árnadóttir; Alexey Gordeev; Sabrina Lato; Tovohery Hajatiana Randrianarisoa; Joannes Vermant. *Cayley incidence graphs*. 2025. [primary source](https://doi.org/10.26493/1855-3974.3510.a82) Location: Question 10.1, p. 27 in accepted manuscript.

**Literature check.** Status for questions 1865, 1866, 1867, checked 6 October 2026: Checked 6 October 2026; no later resolution found.

**Further links.** [1](https://arxiv.org/abs/2411.19428) · [2](https://www.diva-portal.org/smash/get/diva2%3A2072415/FULLTEXT01.pdf) · [3](https://www.famnit.upr.si/en/mathematical-research-seminar/cayley-incidence-graphs-2/)


<a id="q1866"></a>

## Q1866. Recognize non-Cayley regular incidence graphs

**Status:** Open · **Kind:** open problem (Question 10.3) · **Collection** 19

When k=ℓ, characterize the pairs (G,π) for which Cin(G,π) is not isomorphic to a Cayley graph of any group.

**Context.** Doctoral context for questions 1865, 1866, 1867: see question 1856. Origin for questions 1865, 1866, 1867: Authors’ Questions 10.1, 10.3 and Problem 10.7. Setup for questions 1865, 1866, 1867: Let G be finite. Cells π={C₁,…,C_ℓ} contain e, have common size k, pairwise intersection {e}, and satisfy s⁻¹C∈π for C∈π,s∈C. Cin(G,π) has parts G and the distinct sets gC, with incidence by membership. It is (ℓ,k)-biregular; its underlying Cayley graph has connection set ⋃C_i∖{e}.

**Source.** Arnbjörg Soffía Árnadóttir; Alexey Gordeev; Sabrina Lato; Tovohery Hajatiana Randrianarisoa; Joannes Vermant. *Cayley incidence graphs*. 2025. [primary source](https://doi.org/10.26493/1855-3974.3510.a82) Location: Question 10.3, p. 28 in accepted manuscript.

**Literature check.** Status for questions 1865, 1866, 1867, checked 6 October 2026: Checked 6 October 2026; no later resolution found.

**Further links.** [1](https://arxiv.org/abs/2411.19428) · [2](https://www.diva-portal.org/smash/get/diva2%3A2072415/FULLTEXT01.pdf) · [3](https://www.famnit.upr.si/en/mathematical-research-seminar/cayley-incidence-graphs-2/)


<a id="q1867"></a>

## Q1867. Determine full incidence-graph automorphisms

**Status:** Open · **Kind:** open problem (Problem 10.7) · **Collection** 19

Characterize the pairs (G,π) for which the full graph automorphism group Aut(Cin(G,π)) is isomorphic to G.

**Context.** Doctoral context for questions 1865, 1866, 1867: see question 1856. Origin for questions 1865, 1866, 1867: Authors’ Questions 10.1, 10.3 and Problem 10.7. Setup for questions 1865, 1866, 1867: Let G be finite. Cells π={C₁,…,C_ℓ} contain e, have common size k, pairwise intersection {e}, and satisfy s⁻¹C∈π for C∈π,s∈C. Cin(G,π) has parts G and the distinct sets gC, with incidence by membership. It is (ℓ,k)-biregular; its underlying Cayley graph has connection set ⋃C_i∖{e}.

**Source.** Arnbjörg Soffía Árnadóttir; Alexey Gordeev; Sabrina Lato; Tovohery Hajatiana Randrianarisoa; Joannes Vermant. *Cayley incidence graphs*. 2025. [primary source](https://doi.org/10.26493/1855-3974.3510.a82) Location: Problem 10.7, p. 28 in accepted manuscript.

**Literature check.** Status for questions 1865, 1866, 1867, checked 6 October 2026: Checked 6 October 2026; no later resolution found.

**Further links.** [1](https://arxiv.org/abs/2411.19428) · [2](https://www.diva-portal.org/smash/get/diva2%3A2072415/FULLTEXT01.pdf) · [3](https://www.famnit.upr.si/en/mathematical-research-seminar/cayley-incidence-graphs-2/)


<a id="q1868"></a>

## Q1868. Realize the 306-vertex biregular array

**Status:** Open · **Kind:** open problem · **Collection** 19

Does a graph with array ((15;1,3,28,15),(36;1,6,14,36)) exist?

**Context.** Doctoral context for question 1868: see question 1856. Origin for question 1868: Authors’ unresolved feasibility table, following Lato’s thesis tables. Setup for question 1868: Graphs are finite, simple, connected and bipartite with parts Y,Z and valencies k,ℓ. Array ((k;c₁^Y,…,c₄^Y),(ℓ;c₁^Z,…,c₄^Z)) specifies a distance-biregular graph: every vertex in either part has eccentricity four, and c_i^X counts neighbours of v at distance i−1 from u whenever u∈X,d(u,v)=i.

**Source.** Blas Fernández; Ferdinand Ihringer; Sabrina Lato; Akihiro Munemasa. *New Constructions of Distance-Biregular Graphs*. 2026. [primary source](https://arxiv.org/abs/2504.21488) Location: §7, feasibility table, p. 23, fifth row.

**Literature check.** Status for question 1868, checked 6 October 2026: Unknown in July 2026 v4; no later resolution found by 6 October.

**Further links.** [1](https://arxiv.org/pdf/2504.21488v4) · [2](https://dspacemainprd01.lib.uwaterloo.ca/server/api/core/bitstreams/ced0fd0d-ebb6-4aa4-b2f4-699597bf3bbe/content)


<a id="q1951"></a>

## Q1951. Prove the sharp matching intersection threshold

**Status:** Open · **Kind:** open problem · **Collection** 20

For integers t≥3 and n≥3t/2+1, must every t-intersecting family F of perfect matchings of K_(2n) satisfy |F|≤(2n−2t−1)!!, with equality only for canonical families?

**Context.** Origin for question 1951: Godsil–Meagher’s conjecture, restated by Lindzey. Setup for question 1951: A family of perfect matchings is t-intersecting when every two members share at least t edges. A canonical family consists of all perfect matchings containing a fixed t-edge matching.

**Source.** Nathan Lindzey. *Matchings and Representation Theory*. 2018. Advisor(s): Joseph Cheriyan and Chris Godsil. [primary source](https://dspacemainprd01.lib.uwaterloo.ca/server/api/core/bitstreams/9d33772f-c7dc-409f-a4ed-521da8d87890/content) Location: Chapter 4 conjecture, p. 55; §4.10, pp. 97–98.

**Literature check.** Status for question 1951, checked 6 October 2026: Checked 6 October 2026; no later resolution found.

**Further links.** [1](https://uwspace.uwaterloo.ca/items/e78977a2-29ae-43a3-9994-1062d0c36d12/full) · [2](https://doi.org/10.5802/alco.479) · [3](https://uregina.ca/~meagherk/CanaDAM.pdf) · [4](https://nathanlindzey.com/vita.pdf)


<a id="q1952"></a>

## Q1952. Classify sparse-complement eigenvalue obstructions

**Status:** Open · **Kind:** conjecture (Conjecture 5.5) · **Collection** 20

For every n-vertex graph G with n≥3 and |E(Ḡ)|≤n−2, is q(G)=3 exactly when Ḡ≅S_(a,b)⊔K₁ for some a,b≥0, and q(G)=2 otherwise?

**Context.** Doctoral context for question 1952: see question 1965. Origin for question 1952: These authors’ strengthening, Conjecture 5.5. Setup for question 1952: For a finite simple graph G, q(G) is the fewest distinct eigenvalues of a real symmetric matrix whose off-diagonal nonzeros are exactly G’s edges; diagonal entries are unrestricted. S_(a,b) is an edge uv with a leaves attached to u and b to v.

**Source.** Barrett; Fallat; Furst; Nasserasr; Rooney; Tait. *Graphs with bipartite complement that admit two distinct eigenvalues*. 2026. [primary source](https://doi.org/10.13001/ela.2026.9443) Location: Conjecture 5.5, p. 160; S_(a,b) defined p. 148.

**Literature check.** Status for question 1952, checked 6 October 2026: Checked 6 October 2026; no later resolution found.

**Further links.** [1](https://journals.uwyo.edu/index.php/ela/article/download/9443/7389/28681) · [2](https://arxiv.org/abs/2411.12917) · [3](https://uwspace.uwaterloo.ca/items/8228cdbf-5228-4edd-84cc-c90661cae564/full) · [4](https://dspacemainprd01.lib.uwaterloo.ca/server/api/core/bitstreams/9e341e30-a231-4891-a7ea-38cc3144dc7c/content) · [5](https://www.math.uwaterloo.ca/~cgodsil/mine/students.html)


<a id="q1953"></a>

## Q1953. Find Hamilton cycles in all remaining bicirculants

**Status:** Open · **Kind:** conjecture (Conjecture 1) · **Collection** 20

Is every connected bicirculant Hamiltonian, except K₂ and G(m,2) for m≡5 (mod 6)?

**Context.** Origin for question 1953: Bonvicini–Pisanski–Žitnik, first posed in their generalized-rose-window paper (2025 preprint; 2026 journal). Setup for question 1953: A bicirculant is a finite simple regular graph admitting an automorphism with exactly two equally sized vertex-orbits. For m≥5, G(m,2) has vertices u_i,v_i (i∈Z_m) and edges u_i u_(i+1), u_i v_i, v_i v_(i+2).

**Source.** Simona Bonvicini; Tomaž Pisanski; Arjana Žitnik. *On the hamiltonicity problem of bicirculants: a reduction to cyclic Haar graphs*. 2026. [primary source](https://arxiv.org/abs/2604.21607) Location: Conjecture 1, p. 3.

**Literature check.** Status for question 1953, checked 6 October 2026: Checked 6 October 2026; no later resolution found.

**Further links.** [1](https://doi.org/10.1007/s00373-026-03016-w) · [2](https://doi.org/10.1007/s00009-026-03160-w)


<a id="q1954"></a>

## Q1954. Bound isolation games without isolated-edge components

**Status:** Open · **Kind:** conjecture (Conjecture 5.1) · **Collection** 20

For every finite simple graph G with no K₂ component, are both ι\_g(G) and ι′\_g(G) at most ceil(3|V(G)|/7)?

**Context.** Origin for questions 1954, 1955: General bound: Brešar–Dravec–Johnston–Kuenzel–Rall; tree refinement: these authors. Setup for questions 1954, 1955: In the isolation game, players alternately choose a vertex whose closed neighbourhood meets a nontrivial component of G−N[X], where X is the set already chosen. Play stops when G−N[X] has no edges. Dominator minimizes and Staller maximizes the move count. Optimal counts are ι\_g(G) and ι′\_g(G), with Dominator and Staller starting respectively.

**Source.** Bujtás; Dravec; Henning; Klavžar. *Bounds on the game isolation number and exact values for paths and cycles*. 2026. [primary source](https://doi.org/10.46298/dmtcs.16132) Location: Conjecture 5.1, p. 18.

**Literature check.** Status for questions 1954, 1955, checked 6 October 2026: Checked 6 October 2026; no later resolution found.

**Further links.** [1](https://arxiv.org/html/2507.08503v3) · [2](https://doi.org/10.1007/s00373-026-03030-y)


<a id="q1955"></a>

## Q1955. Sharpen the tree isolation-game bound

**Status:** Open · **Kind:** conjecture (Conjecture 5.4) · **Collection** 20

For every tree T on n≥3 vertices, is ι\_g(T)≤3n/7?

**Context.** Origin for questions 1954, 1955: General bound: Brešar–Dravec–Johnston–Kuenzel–Rall; tree refinement: these authors. Setup for questions 1954, 1955: In the isolation game, players alternately choose a vertex whose closed neighbourhood meets a nontrivial component of G−N[X], where X is the set already chosen. Play stops when G−N[X] has no edges. Dominator minimizes and Staller maximizes the move count. Optimal counts are ι\_g(G) and ι′\_g(G), with Dominator and Staller starting respectively.

**Source.** Bujtás; Dravec; Henning; Klavžar. *Bounds on the game isolation number and exact values for paths and cycles*. 2026. [primary source](https://doi.org/10.46298/dmtcs.16132) Location: Conjecture 5.4, p. 20.

**Literature check.** Status for questions 1954, 1955, checked 6 October 2026: Checked 6 October 2026; no later resolution found.

**Further links.** [1](https://arxiv.org/html/2507.08503v3) · [2](https://doi.org/10.1007/s00373-026-03030-y)


<a id="q1956"></a>

## Q1956. Give each clique a uniquely coloured edge

**Status:** Open · **Kind:** conjecture (Conjecture 1.19) · **Collection** 20

For every fixed integer t≥8, is u_(K_t)(n)=n^{o(1)} as n→∞?

**Context.** Origin for question 1956: David Conlon independently; then Fredy Yip. Setup for question 1956: For fixed t≥2, u_(K_t)(n) is the fewest colours in an edge-colouring of K_n such that every K_t-copy has a colour occurring on exactly one of its edges.

**Source.** Fredy Yip. *A variant of the Erdős–Gyárfás problem for K₈*. 2026. [primary source](https://doi.org/10.1016/j.ejc.2025.104267) Location: Conjecture 1.19, p. 4; t≤7 noted there.

**Literature check.** Status for question 1956, checked 6 October 2026: Checked 6 October 2026; no later resolution found.

**Further links.** [1](https://arxiv.org/abs/2409.16778) · [2](https://api.repository.cam.ac.uk/server/api/core/bitstreams/428d0783-a2d0-47c4-9a7b-49b896262665/content)


<a id="q1957"></a>

## Q1957. Separate adaptable and separation choosability arbitrarily

**Status:** Open · **Kind:** open problem (Problem 2.7) · **Collection** 20

For every integer k≥1, does a finite simple graph G exist with ch_ad(G)−ch_sep(G)≥k?

**Context.** Origin for questions 1957, 1958: Casselgren–Eriksson, Problems 2.7 and 4.4. Setup for questions 1957, 1958: For a finite simple graph, ch_sep is the least k such that every assignment of k-element colour lists with adjacent intersections≤1 admits a proper list colouring. ch_ad is the least k such that every k-list assignment and edge colouring f admit c(v)∈L(v) with no edge uv satisfying c(u)=c(v)=f(uv). χ\_sc is the least k such that every assignment of one forbidden ordered pair from [k]² to each edge admits a colouring φ:V(G)→[k] avoiding those pairs.

**Source.** Casselgren; Eriksson. *Single conflict coloring, adaptable choosability and separation choosability*. 2025. [primary source](https://arxiv.org/abs/2509.13913) Location: Problem 2.7, p. 5.

**Literature check.** Status for questions 1957, 1958, checked 6 October 2026: Checked 6 October 2026; no later resolution found.

**Further links.** [1](https://arxiv.org/abs/2601.06990)


<a id="q1958"></a>

## Q1958. Realize the missing planar colouring triple

**Status:** Open · **Kind:** open problem (Problem 4.4) · **Collection** 20

Does a finite simple planar graph G exist with (ch_sep(G),ch_ad(G),χ\_sc(G))=(3,3,4)?

**Context.** Origin for questions 1957, 1958: Casselgren–Eriksson, Problems 2.7 and 4.4. Setup for questions 1957, 1958: For a finite simple graph, ch_sep is the least k such that every assignment of k-element colour lists with adjacent intersections≤1 admits a proper list colouring. ch_ad is the least k such that every k-list assignment and edge colouring f admit c(v)∈L(v) with no edge uv satisfying c(u)=c(v)=f(uv). χ\_sc is the least k such that every assignment of one forbidden ordered pair from [k]² to each edge admits a colouring φ:V(G)→[k] avoiding those pairs.

**Source.** Casselgren; Eriksson. *Single conflict coloring, adaptable choosability and separation choosability*. 2025. [primary source](https://arxiv.org/abs/2509.13913) Location: Problem 4.4, p. 10.

**Literature check.** Status for questions 1957, 1958, checked 6 October 2026: Checked 6 October 2026; no later resolution found.

**Further links.** [1](https://arxiv.org/abs/2601.06990)


<a id="q1959"></a>

## Q1959. Bound projective-cube-free integer sets

**Status:** Open · **Kind:** conjecture (Conjecture 3) · **Collection** 20

Is the maximum size of a 3-cube-free subset of {1,…,N} at most (2/3+o(1))N as N→∞?

**Context.** Origin for questions 1959, 1960: Integer question: Sean Eberhard and Cosmin Pohoata; cyclic question: Meng. Setup for questions 1959, 1960: A projective d-cube generated by a multiset a₁,…,a_d consists of all nonempty subset sums ∑\_(i∈I)a_i. Generators may repeat, and coincident sums are allowed. A set is d-cube-free if it contains no such cube.

**Source.** Yuchen Meng. *On Cube-Free Problems*. 2026. [primary source](https://doi.org/10.37236/14052) Location: Conjecture 3, p. 2.

**Literature check.** Status for questions 1959, 1960, checked 6 October 2026: Checked 6 October 2026; no later resolution found.

**Results.**

- **Investigated, unresolved** (B2: submitted unresolved): No new result supplied. Remaining/limits: No exact closure established in this session. [Report](../../solutions/b2-2026-10-07/README.md).

**Further links.** [1](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v33i1p16/pdf/) · [2](https://seaneberhard.com/2020/01/17/the-avoidance-density-of-kl-sum-free-sets/) · [3](https://gist.github.com/hypnopump/8a369af584796b25c9af586b4fe39385)


<a id="q1960"></a>

## Q1960. Bound projective-cube-free cyclic sets

**Status:** Open · **Kind:** conjecture (Conjecture 4) · **Collection** 20

For all integers d≥2 and N divisible by d, must every d-cube-free A⊆Z/NZ satisfy |A|≤(d−1)N/d?

**Context.** Origin for questions 1959, 1960: Integer question: Sean Eberhard and Cosmin Pohoata; cyclic question: Meng. Setup for questions 1959, 1960: A projective d-cube generated by a multiset a₁,…,a_d consists of all nonempty subset sums ∑\_(i∈I)a_i. Generators may repeat, and coincident sums are allowed. A set is d-cube-free if it contains no such cube.

**Source.** Yuchen Meng. *On Cube-Free Problems*. 2026. [primary source](https://doi.org/10.37236/14052) Location: Conjecture 4, p. 2.

**Literature check.** Status for questions 1959, 1960, checked 6 October 2026: Checked 6 October 2026; no later resolution found.

**Results.**

- **Investigated, unresolved** (B2: submitted unresolved): No new result supplied. Remaining/limits: No exact closure established in this session. [Report](../../solutions/b2-2026-10-07/README.md).

**Further links.** [1](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v33i1p16/pdf/) · [2](https://seaneberhard.com/2020/01/17/the-avoidance-density-of-kl-sum-free-sets/) · [3](https://gist.github.com/hypnopump/8a369af584796b25c9af586b4fe39385)


<a id="q1961"></a>

## Q1961. Prove the five-eighths projective-cube bound

**Status:** Open · **Kind:** conjecture (Conjecture 5.1) · **Collection** 20

For every integer n≥3, must a projective-3-cube-free subset of Z/(2^n)Z have at most 5·2^(n−3) elements?

**Context.** Origin for question 1961: Long–Wagner, Conjecture 5.1 (2018 preprint). Setup for question 1961: In Z/(2^n)Z, a projective 3-cube is {x,y,z,x+y,x+z,y+z,x+y+z}, with repetitions and degeneracies allowed.

**Source.** Jason Long; Adam Zsolt Wagner. *The largest projective cube-free subsets of Z_(2^n)*. 2019. [primary source](https://arxiv.org/abs/1810.01225) Location: Conjecture 5.1, preprint p. 21.

**Literature check.** Status for question 1961, checked 6 October 2026: Checked 6 October 2026; no later resolution found.

**Results.**

- **Investigated, unresolved** (B2: submitted unresolved): No new result supplied. Remaining/limits: No exact closure established in this session. [Report](../../solutions/b2-2026-10-07/README.md).

**Further links.** [1](https://doi.org/10.1016/j.ejc.2019.05.005) · [2](https://doi.org/10.37236/14052) · [3](https://prove2.me/f/combinatorics?status=all)


<a id="q1962"></a>

## Q1962. Force increasing subsequences with few zero entries

**Status:** Open · **Kind:** conjecture (Conjecture 1.2) · **Collection** 20

For all integers 2≤k≤n, must every 12…k-permutation-forcing n×n matrix have at least n(k−2)−k(k−3)/2 zero entries?

**Context.** Origin for question 1962: Brualdi–Cao–Goldwasser, Conjecture 1.2. Setup for question 1962: An n×n (0,1)-matrix A with nonzero permanent is 12…k-permutation forcing if every permutation matrix P≤A corresponds to a permutation containing an increasing subsequence of length k.

**Source.** Richard A. Brualdi; Lei Cao; John L. Goldwasser. *Permutation forcing (0,1)-matrices*. 2026. [primary source](https://ajc.maths.uq.edu.au/pdf/95/ajc_v95_p201.pdf) Location: Conjecture 1.2, p. 203.

**Literature check.** Status for question 1962, checked 6 October 2026: Checked 6 October 2026; no later resolution found.

**Further links.** [1](https://scholars.nova.edu/en/publications/permutation-forcing-0-1-matrices/)


<a id="q1963"></a>

## Q1963. Find induced cycles on half the cubic vertices

**Status:** Open · **Kind:** conjecture (Conjecture 1) · **Collection** 20

Must every finite simple cubic graph G on n vertices satisfy c_ind(G)≥n/2?

**Context.** Origin for question 1963: Michael A. Henning, Felix Joos, Christian Löwenstein and Thomas Sasse, Induced cycles in graphs (2016). Setup for question 1963: For a finite simple graph G, c_ind(G) is the largest size of S⊆V(G) for which every vertex of the induced graph G[S] has degree two.

**Source.** Martin Knor; Jelena Sedlar; Riste Škrekovski. *Counterexamples to two conjectures on (1,2)-domination in cubic graphs*. 2026. [primary source](https://arxiv.org/abs/2608.17851) Location: Conjecture 1, p. 2.

**Literature check.** Status for question 1963, checked 6 October 2026: Checked 6 October 2026; no later resolution found.

**Further links.** [1](https://arxiv.org/html/2608.17851v2)


<a id="q1964"></a>

## Q1964. Acyclically edge-colour with two extra colours

**Status:** Open · **Kind:** conjecture (Conjecture 1) · **Collection** 20

Does every finite simple graph G have an acyclic edge colouring with at most Δ(G)+2 colours?

**Context.** Origin for question 1964: J. Fiamčík (1978); independently Alon–Sudakov–Zaks (2001). Setup for question 1964: An acyclic edge colouring is a proper edge colouring in which no cycle uses only two colours. Δ(G) denotes maximum degree.

**Source.** Nevil Anto; Manu Basavaraju; Shashanka Kulamarva. *Acyclic edge coloring of 3-sparse graphs*. 2026. [primary source](https://doi.org/10.1016/j.disc.2026.115135) Location: Conjecture 1, introduction; preprint p. 2.

**Literature check.** Status for question 1964, checked 6 October 2026: Checked 6 October 2026; no later resolution found.

**Further links.** [1](https://arxiv.org/abs/2501.11281) · [2](https://www.sciencedirect.com/science/article/pii/S0012365X26001597)


<a id="q1965"></a>

## Q1965. Classify maximum independent sets of folded cubes

**Status:** Open · **Kind:** open problem · **Collection** 20

For every odd n≥11, is every maximum independent set of F_n canonical?

**Context.** Doctoral context for questions 1952, 1965: given in the source heading above. Origin for question 1965: Rooney’s maximum-coclique question. Setup for question 1965: For n=2r+1≥3, let F_n be the n-cube with antipodal vertices identified. Put Γ\_i(v)={u:d(u,v)=i}. Its canonical independent sets are ⋃\_{0≤i&lt;r, i≢r (mod 2)} Γ\_i(v).

**Source.** Brendan Rooney. *Spectral Aspects of Cocliques in Graphs*. 2014. Advisor(s): Chris Godsil. [primary source](https://dspacemainprd01.lib.uwaterloo.ca/server/api/core/bitstreams/9e341e30-a231-4891-a7ea-38cc3144dc7c/content) Location: §4.4, pp. 67–68; §4.12, p. 89.

**Literature check.** Status for question 1965, checked 6 October 2026: Checked 6 October 2026; no later resolution found.

**Further links.** [1](https://uwspace.uwaterloo.ca/items/8228cdbf-5228-4edd-84cc-c90661cae564/full) · [2](https://www.math.uwaterloo.ca/~cgodsil/mine/students.html)


<a id="q1966"></a>

## Q1966. Force chords in longest cycles

**Status:** Open · **Kind:** conjecture (Conjecture 1.4) · **Collection** 20

In every 2-connected graph of minimum degree at least three, does every longest cycle have a chord?

**Context.** Origin for question 1966: Daniel J. Harvey’s conjecture, restated by Wu–Zhang. Setup for question 1966: A chord of a cycle joins two nonconsecutive vertices of that cycle. All graphs are finite and simple.

**Source.** Haidong Wu; Shunzhe Zhang. *Chords of longest cycles in graphs with large circumferences*. 2025. [primary source](https://arxiv.org/abs/2511.03422) Location: Conjecture 1.4, preprint p. 2.

**Literature check.** Status for question 1966, checked 6 October 2026: Checked 6 October 2026; no later resolution found.

**Further links.** [1](https://doi.org/10.1016/j.dam.2026.07.025) · [2](https://arxiv.org/abs/2410.19005)


<a id="q1967"></a>

## Q1967. Partition twin-free graphs into locating-dominating sets

**Status:** Open · **Kind:** open problem (Problem 3) · **Collection** 20

Can the vertices of every finite simple isolate-free, twin-free graph be partitioned into two locating-dominating sets?

**Context.** Origin for question 1967: Garijo–González–Márquez; Foucaud–Henning; Foucaud–Henning–Löwenstein–Sasse. Restated as Problem 3. Setup for question 1967: A locating-dominating set S satisfies: every vertex outside S has a neighbour in S, and distinct vertices outside S have distinct neighbourhoods in S. A graph is twin-free if no two vertices have equal open or equal closed neighbourhoods.

**Source.** Dipayan Chakraborty; Florent Foucaud; Michael A. Henning; Tero Laihonen. *A note on partitioning the vertex set of a graph into a dominating set and a locating dominating set*. 2026. [primary source](https://doi.org/10.37236/14049) Location: Problem 3 and following paragraph, pp. 3–4.

**Literature check.** Status for question 1967, checked 6 October 2026: Checked 6 October 2026; no later resolution found.

**Further links.** [1](https://arxiv.org/abs/2610.03131) · [2](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v33i1p51/pdf/)


<a id="q2051"></a>

## Q2051. Odd five-colour all planar graphs

**Status:** Open · **Kind:** conjecture (Conjecture 1.3.1) · **Collection** 21

Does every finite simple planar graph admit an odd colouring with at most five colours?

**Context.** Origin for question 2051: Petruševski–Škrekovski (2021), restated by Petr. Setup for question 2051: An odd colouring is a proper vertex colouring in which every non-isolated vertex has some colour occurring an odd number of times in its open neighbourhood. Graphs are finite and simple.

**Source.** Jan Petr. *Colourings, dominating sets and wreaths*. 2025. Advisor(s): Béla Bollobás. [primary source](https://www.repository.cam.ac.uk/bitstreams/6cb328d0-6f50-4e7b-9c7e-25c7f12d4d57/download) Location: Conjecture 1.3.1, p. 17.

**Literature check.** Status for question 2051, checked 6 October 2026: no later resolution found.

**Further links.** [1](https://www.repository.cam.ac.uk/items/09faf321-7438-442a-9ed1-6487b62ab783) · [2](https://web.xidian.edu.cn/zhangxin/files/68ca43b142f7e.pdf)


<a id="q2052"></a>

## Q2052. Find spines in finite-width posets

**Status:** Open · **Kind:** open problem (Question 2.6.1) · **Collection** 21

Does every finite-width poset P admit a chain C and a partition of P into antichains such that C meets every part?

**Context.** Origin for question 2052: Hollom’s finite-width refinement of Aharoni–Korman (1992). Setup for question 2052: A poset has finite width if some integer bounds the sizes of all its antichains. Its cardinality need not be countable.

**Source.** Lawrence Albert Hollom. *Extremal, Probabilistic, and Infinitary Problems in Combinatorics*. 2025. Advisor(s): Béla Bollobás. [primary source](https://api.repository.cam.ac.uk/server/api/core/bitstreams/a0069f85-e810-476b-ba41-c2babc9c2f0b/content) Location: Question 2.6.1, p. 74.

**Literature check.** Status for question 2052, checked 6 October 2026: no later resolution found.

**Further links.** [1](https://www.repository.cam.ac.uk/items/d9fa2d8e-7393-49d3-933e-0dc3229c2efa) · [2](https://arxiv.org/abs/2411.16844) · [3](https://doi.org/10.37236/14948)


<a id="q2053"></a>

## Q2053. Avoid one-for-two matching improvements

**Status:** Open · **Kind:** open problem (Question 14) · **Collection** 21

Does every such hypergraph have a matching M for which no matching M′ satisfies |M∖M′|=1 and |M′∖M|=2?

**Context.** Origin for questions 2053, 2054: Hollom–Randall Shaw; matching question refines Tardos’s disproved unbounded-edge question. Setup for questions 2053, 2054: Hypergraphs may be infinite, but one finite integer bounds every edge size. A matching consists of disjoint edges; an edge-cover is a set of edges whose union is the vertex set.

**Source.** Lawrence Hollom; Benedict Randall Shaw. *Counterexamples to Conjectures on Strong Maximality and Minimality*. 2026. [primary source](https://doi.org/10.37236/14948) Location: Question 14, p. 11 (preprint Question 4.1).

**Literature check.** Status for questions 2053, 2054, checked 6 October 2026: no later resolution found.

**Further links.** [1](https://arxiv.org/abs/2511.13709) · [2](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v33i2p11/pdf/)


<a id="q2054"></a>

## Q2054. Avoid two-for-one cover improvements

**Status:** Open · **Kind:** open problem (Question 15) · **Collection** 21

Does every such hypergraph without isolated vertices have an edge-cover C for which no edge-cover C′ satisfies |C∖C′|=2 and |C′∖C|=1?

**Context.** Origin for questions 2053, 2054: Hollom–Randall Shaw; matching question refines Tardos’s disproved unbounded-edge question. Setup for questions 2053, 2054: Hypergraphs may be infinite, but one finite integer bounds every edge size. A matching consists of disjoint edges; an edge-cover is a set of edges whose union is the vertex set.

**Source.** Lawrence Hollom; Benedict Randall Shaw. *Counterexamples to Conjectures on Strong Maximality and Minimality*. 2026. [primary source](https://doi.org/10.37236/14948) Location: Question 15, p. 11 (preprint Question 4.2).

**Literature check.** Status for questions 2053, 2054, checked 6 October 2026: no later resolution found.

**Further links.** [1](https://arxiv.org/abs/2511.13709) · [2](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v33i2p11/pdf/)


<a id="q2055"></a>

## Q2055. Sharpen longest-cycle intersections

**Status:** Open · **Kind:** conjecture (Conjecture 1.1) · **Collection** 21

For every integer k≥9, do any two longest cycles in a k-connected graph have at least k common vertices?

**Context.** Origin for questions 2055, 2056, 2057: Smith (1984); separator refinement: these authors and Bucić–Christoph–Pokrovskiy–Steiner; triple-path question: Gallai (BCC15.6, 1997). Setup for questions 2055, 2056, 2057: Graphs are finite and simple. A set S separates subgraphs X,Y if every path from V(X) to V(Y), including trivial paths at their common vertices, meets S.

**Source.** Jie Ma; Bo Ning; Ziyuan Zhao. *Longest cycles intersect linearly in highly connected graphs*. 2026. [primary source](https://arxiv.org/abs/2609.20724) Location: Conjecture 1.1, p. 1; known k≤8 removed.

**Literature check.** Status for questions 2055, 2056, 2057, checked 6 October 2026: these remain open in the September source. Sarkar’s triple-path proof claim was withdrawn as erroneous (May 2024).

**Further links.** [1](https://arxiv.org/abs/2006.16245)


<a id="q2056"></a>

## Q2056. Separate longest cycles efficiently

**Status:** Open · **Kind:** conjecture (Conjecture 9.4) · **Collection** 21

Is there an absolute C>0 such that any two longest cycles X,Y of any 2-connected graph G can be separated by a vertex set of size at most C|V(X)∩V(Y)|?

**Context.** Origin for questions 2055, 2056, 2057: Smith (1984); separator refinement: these authors and Bucić–Christoph–Pokrovskiy–Steiner; triple-path question: Gallai (BCC15.6, 1997). Setup for questions 2055, 2056, 2057: Graphs are finite and simple. A set S separates subgraphs X,Y if every path from V(X) to V(Y), including trivial paths at their common vertices, meets S.

**Source.** Jie Ma; Bo Ning; Ziyuan Zhao. *Longest cycles intersect linearly in highly connected graphs*. 2026. [primary source](https://arxiv.org/abs/2609.20724) Location: Conjecture 9.4, p. 17.

**Literature check.** Status for questions 2055, 2056, 2057, checked 6 October 2026: these remain open in the September source. Sarkar’s triple-path proof claim was withdrawn as erroneous (May 2024).

**Further links.** [1](https://arxiv.org/abs/2006.16245)


<a id="q2057"></a>

## Q2057. Intersect three longest paths

**Status:** Open · **Kind:** open problem · **Collection** 21

Does every triple of longest paths in a finite connected graph have a common vertex?

**Context.** Origin for questions 2055, 2056, 2057: Smith (1984); separator refinement: these authors and Bucić–Christoph–Pokrovskiy–Steiner; triple-path question: Gallai (BCC15.6, 1997). Setup for questions 2055, 2056, 2057: Graphs are finite and simple. A set S separates subgraphs X,Y if every path from V(X) to V(Y), including trivial paths at their common vertices, meets S.

**Source.** Jie Ma; Bo Ning; Ziyuan Zhao. *Longest cycles intersect linearly in highly connected graphs*. 2026. [primary source](https://arxiv.org/abs/2609.20724) Location: §9.4, final paragraph, p. 17.

**Literature check.** Status for questions 2055, 2056, 2057, checked 6 October 2026: these remain open in the September source. Sarkar’s triple-path proof claim was withdrawn as erroneous (May 2024).

**Further links.** [1](https://arxiv.org/abs/2006.16245)

