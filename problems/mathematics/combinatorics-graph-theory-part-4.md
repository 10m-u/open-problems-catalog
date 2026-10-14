# Combinatorics & Graph Theory (part 4 of 4)

[Subject overview](combinatorics-graph-theory.md) · Parts: [1](combinatorics-graph-theory-part-1.md) · [2](combinatorics-graph-theory-part-2.md) · [3](combinatorics-graph-theory-part-3.md) · [4](combinatorics-graph-theory-part-4.md)

<a id="q4774"></a>

## Q4774. For each even d, are there finitely many equivalence classes of thin Δ with lattice width≥2?

**Status:** Open · **Kind:** conjecture (Conjecture 6) · **Collection** 48

For each even d, are there finitely many equivalence classes of thin Δ with lattice width≥2?

**Context.** Setup: Let Δ=conv(v₀,…,v_d)⊂R^d be a full-dimensional lattice simplex, d≥1. Call Δ thin when {Σ\_{i=0}^d a_i(v_i,1):0&lt;a_i<1} contains no point of Z^{d+1}. Its lattice width is min_{0≠u∈Z^d}(max_{x∈Δ}u·x−min_{x∈Δ}u·x). Equivalence means affine unimodular equivalence. Audited provenance and status: Subject: Discrete geometry and Ehrhart theory Vadym Kurylenko; Local Ehrhart Theory and Gale Duality; SISSA, 2024; Fernando Rodriguez Villegas. Conjectures 6–7, p.102. https://iris.sissa.it/handle/20.500.11767/144210 https://arxiv.org/abs/2404.03975v2 https://arxiv.org/abs/2602.20765v2 Degree: PhD, defended 2024-12-16. Advisor verified on thesis cover. Earlier-paper origin; the thesis retains both conjectures. Final: Conjectures 1.5–1.6, p.5/PDF6; setup §§2.1,2.3,2.6. https://escholarship.org/uc/item/2s97z8wq https://doi.org/10.5070/c6.68698 2026-10-13: Final retains both; dimensions≤4 are known. Scope inference: checked later Cayley constructions have width1; no matching resolution located. Checks: https://arxiv.org/abs/2602.20765v2 §§3–5; https://arxiv.org/abs/2507.03661v2 §§1,6.2–6.4.

**Source.** Vadym Kurylenko. *Local Ehrhart Theory and Gale Duality*. SISSA, 2024. Advisor(s): Fernando Rodriguez Villegas. [primary source](https://iris.sissa.it/handle/20.500.11767/144210) Location: Thesis Conjecture 6, p.102; final Conjecture 1.5.

**Literature check.** Status: Scope inference: checked later Cayley constructions have width1; no matching resolution located.

**Further links.** [1](https://arxiv.org/abs/2404.03975v2) · [2](https://arxiv.org/abs/2602.20765v2) · [3](https://escholarship.org/uc/item/2s97z8wq) · [4](https://doi.org/10.5070/c6.68698) · [5](https://arxiv.org/abs/2507.03661v2)


<a id="q4775"></a>

## Q4775. Does every odd-dimensional thin Δ have lattice width1?

**Status:** Open · **Kind:** conjecture (Conjecture 7) · **Collection** 48

Does every odd-dimensional thin Δ have lattice width1?

**Context.** Setup: Let Δ=conv(v₀,…,v_d)⊂R^d be a full-dimensional lattice simplex, d≥1. Call Δ thin when {Σ\_{i=0}^d a_i(v_i,1):0&lt;a_i<1} contains no point of Z^{d+1}. Its lattice width is min_{0≠u∈Z^d}(max_{x∈Δ}u·x−min_{x∈Δ}u·x). Equivalence means affine unimodular equivalence. Audited provenance and status: Subject: Discrete geometry and Ehrhart theory Vadym Kurylenko; Local Ehrhart Theory and Gale Duality; SISSA, 2024; Fernando Rodriguez Villegas. Conjectures 6–7, p.102. https://iris.sissa.it/handle/20.500.11767/144210 https://arxiv.org/abs/2404.03975v2 https://arxiv.org/abs/2602.20765v2 Degree: PhD, defended 2024-12-16. Advisor verified on thesis cover. Earlier-paper origin; the thesis retains both conjectures. Final: Conjectures 1.5–1.6, p.5/PDF6; setup §§2.1,2.3,2.6. https://escholarship.org/uc/item/2s97z8wq https://doi.org/10.5070/c6.68698 2026-10-13: Final retains both; dimensions≤4 are known. Scope inference: checked later Cayley constructions have width1; no matching resolution located. Checks: https://arxiv.org/abs/2602.20765v2 §§3–5; https://arxiv.org/abs/2507.03661v2 §§1,6.2–6.4.

**Source.** Vadym Kurylenko. *Local Ehrhart Theory and Gale Duality*. SISSA, 2024. Advisor(s): Fernando Rodriguez Villegas. [primary source](https://iris.sissa.it/handle/20.500.11767/144210) Location: Thesis Conjecture 7, p.102; final Conjecture 1.6.

**Literature check.** Status: Scope inference: checked later Cayley constructions have width1; no matching resolution located.

**Further links.** [1](https://arxiv.org/abs/2404.03975v2) · [2](https://arxiv.org/abs/2602.20765v2) · [3](https://escholarship.org/uc/item/2s97z8wq) · [4](https://doi.org/10.5070/c6.68698) · [5](https://arxiv.org/abs/2507.03661v2)


<a id="q4799"></a>

## Q4799. Is a_f(G)−a\*\_f(G) unbounded as G and f vary?

**Status:** Open · **Kind:** open problem · **Collection** 48

Is a_f(G)−a\*\_f(G) unbounded as G and f vary?

**Context.** For a finite loopless multigraph G and f:V(G)→ℤ≥2, let 𝔉 be its forest edge-sets satisfying d_F(v)≤f(v) for every vertex. Define a_f(G)=min{|𝒞|:𝒞⊆𝔉,⋃𝒞=E(G)} and a\*\_f(G)=min{Σ\_F y_F:y_F≥0,Σ\_{F∋e}y_F≥1 for every e∈E(G)}. Audited provenance and status: Subject: Graph theory Ronen Wdowinski, Waterloo PhD2024; advisor Penny Haxell. Graph theory. Thesis-origin question; fractional setup also occurs in earlier paper. Scope inference: newer simple-graph bounds and infinite-graph results do not settle this multigraph gap. 2507.20500: accepted JEMS; preprint checked. Degree-f forest/arboricity definitions: §1.2 p5.

**Source.** Ronen Wdowinski. *Arboricity and transversal problems on bounded degree graphs*. University of Waterloo, 2024. Advisor(s): Penny Haxell. [primary source](https://uwspace.uwaterloo.ca/items/98a6f345-a367-4523-b77e-bb693f46a402) Location: Thesis §3.4(2) p58; definitions §1.2 p5 and §3.1 pp45–46.

**Literature check.** Status: Related2024 final unread; newer thesis retains target. Checked2026-10-13: no matching resolution found.

**Further links.** [1](https://arxiv.org/abs/2301.09933v1) · [2](https://doi.org/10.1016/j.disc.2023.113777) · [3](https://arxiv.org/abs/2507.20500v1) · [4](https://arxiv.org/abs/2610.02065v1) · [5](https://arxiv.org/abs/2507.20500)


<a id="q4801"></a>

## Q4801. Three upward families: singleton-cell product bound

**Status:** Open · **Kind:** conjecture (Conjecture 1.1.8) · **Reviewed extraction** 2026-10-13

Let A, B, C be upward-closed subsets of the Boolean lattice 2^[n], each of the same uniform density α. Put a=μ(A∩Bᶜ∩Cᶜ), b=μ(Aᶜ∩B∩Cᶜ), and c=μ(Aᶜ∩Bᶜ∩C), where μ is uniform probability. Is ab+ac+bc≤16/243 for every n and every such triple?

**Source.** Kada Williams. *Hypercube Inequalities and Other Combinatorial Results*. University of Cambridge, 2025. [primary source](https://www.repository.cam.ac.uk/bitstreams/46870253-ce97-4c6f-84ff-e5c0bfbc4a04/download) · [record](https://www.repository.cam.ac.uk/handle/1810/405119) Location: Conjecture 1.1.8, printed p. 3 / PDF p. 11; definitions §1.1, PDF pp. 9–11.

**Literature check.** Reviewed 2026-10-13: The December 2025 thesis states this conjecture separately from its proved counterexample to Kahn’s total-singleton-density question. Targeted searches found no later proof or counterexample to this product bound.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13/main-review.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

<a id="q4802"></a>

## Q4802. Minimum cube dimension for non-layered graphs of large girth

**Status:** Open · **Kind:** open problem (Question 3.1.4) · **Reviewed extraction** 2026-10-13

For even g≥6, let N(g) be the least n such that the n-dimensional hypercube graph Q_n has a subgraph of girth exactly g that is not isomorphic to a subgraph of any edge layer of any hypercube. An edge layer consists of vertices of Hamming weights k−1 and k with all cube edges between them. Determine the asymptotic growth of N(g) as g→∞ through even integers.

**Source.** Kada Williams. *Hypercube Inequalities and Other Combinatorial Results*. University of Cambridge, 2025. [primary source](https://www.repository.cam.ac.uk/bitstreams/46870253-ce97-4c6f-84ff-e5c0bfbc4a04/download) · [record](https://www.repository.cam.ac.uk/handle/1810/405119) Location: Question 3.1.4, printed p. 22 / PDF p. 30; Definition 3.1.1, printed p. 21 / PDF p. 29.

**Literature check.** Reviewed 2026-10-13: The published paper proves existence and leaves the required dimension open; its construction has dimension of order g^g. The December 2025 thesis retains the growth-rate question. No subsequent determination located.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13/main-review.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://arxiv.org/abs/2404.18014) · [2](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v31i4p21/pdf/)

<a id="q4803"></a>

## Q4803. Almost maximum independent sets of toroidal queens

**Status:** Open · **Kind:** conjecture (Conjecture 6.2.3) · **Reviewed extraction** 2026-10-13

For each fixed integer d≥3, does there exist C_d such that, for all sufficiently large positive integers n, at least n^(d−1)−C_d n^(d−2) pairwise nonattacking queens can be placed on (ℤ/nℤ)^d? Distinct positions attack exactly when their difference equals λe for a nonzero e∈{−1,0,1}^d and a nonzero λ∈ℤ/nℤ. There is no restriction on the prime factors of n.

**Source.** Kada Williams. *Hypercube Inequalities and Other Combinatorial Results*. University of Cambridge, 2025. [primary source](https://www.repository.cam.ac.uk/bitstreams/46870253-ce97-4c6f-84ff-e5c0bfbc4a04/download) · [record](https://www.repository.cam.ac.uk/handle/1810/405119) Location: Conjecture 6.2.3, printed p. 49 / PDF p. 57; queen definition §6.1 and proof of Theorem 6.2.2. Later paper: Conjecture 2, arXiv:2404.18237v3.

**Literature check.** Reviewed 2026-10-13: The June 24, 2026 revision explicitly retains the general conjecture and proves a restricted least-prime-factor case. Older v1/v2 abstracts claim the general bound; the revised statement and Theorem 3 supersede that claim. No later general resolution located.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13/main-review.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://arxiv.org/abs/2404.18237v3) · [2](https://arxiv.org/html/2404.18237v3#S2)

<a id="q4804"></a>

## Q4804. Greedy conference gossiping below full dissemination

**Status:** Open · **Kind:** open problem (Question 7.3.1) · **Reviewed extraction** 2026-10-13

Initially each of n people knows a distinct gossip item. In a conference call exactly k people all learn the union of the items they currently know. The score is the sum, over people, of the number of items known. For fixed integers 3≤k≤n and 0≤m below the minimum number of k-person calls required for everyone to know all n items, does every greedy m-call sequence attain the largest possible final score? A greedy sequence chooses at each step a call maximizing the immediate score increase, with arbitrary choices among ties.

**Source.** Kada Williams. *Hypercube Inequalities and Other Combinatorial Results*. University of Cambridge, 2025. [primary source](https://www.repository.cam.ac.uk/bitstreams/46870253-ce97-4c6f-84ff-e5c0bfbc4a04/download) · [record](https://www.repository.cam.ac.uk/handle/1810/405119) Location: Question 7.3.1, printed p. 61 / PDF p. 69; September 22, 2026 journal version, Conjecture 3.2.

**Literature check.** Reviewed 2026-10-13: The September 2026 publication still states the conference-call extension as conjectural. Pairwise calls and the forest range m(k−1)≤n−1 are proved. The question here retains the full conference-call ambition; no resolution of the remaining range located.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13/main-review.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://combinatorialpress.com/cn-articles/volume-238/greedy-gossiping/) · [2](https://arxiv.org/abs/2506.17804)

<a id="q4955"></a>

## Q4955. Vanishing density of nonlinear graph codes avoiding K₄ differences

**Status:** Open · **Kind:** open problem (Question 5.1) · **Reviewed extraction** 2026-10-13-250

Let d_{K₄}(n) be 2^{-binom(n,2)} times the largest size of a family C of labelled simple graphs on [n] such that, for distinct G,H∈C, their edge symmetric difference is never a copy of K₄ with all other vertices isolated. Does d_{K₄}(n)→0 as n→∞?

**Source.** Leo Versteegen. *Games, Graphs, and Groups*. University of Cambridge, 2024. [primary source](https://www.repository.cam.ac.uk/bitstreams/00692ee0-e6c9-41c5-9410-79354acbce71/download) · [record](https://www.repository.cam.ac.uk/handle/1810/370042) Location: Question 5.1, printed p. 75 / held PDF p. 83; definitions in the relevant chapter.

**Literature check.** Reviewed 2026-10-13: The 2025 linear-graph-code paper gives vanishing bounds for linear subspaces, not arbitrary nonlinear families. Later even-decomposition and odd-Ramsey papers concern linear constructions and colouring bounds; no full nonlinear-density resolution was located.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/root-reviews/versteegen-2024.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://onlinelibrary.wiley.com/doi/10.1002/rsa.21263) · [2](https://arxiv.org/abs/2409.11152) · [3](https://api.repository.cam.ac.uk/server/api/core/bitstreams/e8fbcbff-df10-4497-9424-255eebb24e46/content) · [4](https://arxiv.org/abs/2507.14321) · [5](https://arxiv.org/abs/2301.05202) · [6](https://arxiv.org/abs/2006.02668) · [7](https://kam.mff.cuni.cz/~spring/media/papers/6/34ConjectureForDominationGame.pdf) · [8](https://research-explorer.ista.ac.at/download/20482/20954/2026_EuropJourCombinatorics_Boyadzhiyska.pdf)

<a id="q4956"></a>

## Q4956. Subpolynomial odd-Ramsey colour counts outside even decomposability

**Status:** Open · **Kind:** conjecture (Conjecture 5.15) · **Reviewed extraction** 2026-10-13-250

Fix a finite graph H with a positive even number of edges. An even decomposition is V(H)=V₀⊃⋯⊃V_m=∅ with V_{i−1}∖V_i independent and with an even number of edges between V_{i−1}∖V_i and V_i at each step. Suppose H has no even decomposition. Let r_H(n) be the least number of colours in an edge-colouring of K_n in which every embedded copy of H has some colour occurring an odd number of times on its edges. Must r_H(n)=n^{o(1)} as n→∞?

**Source.** Leo Versteegen. *Games, Graphs, and Groups*. University of Cambridge, 2024. [primary source](https://www.repository.cam.ac.uk/bitstreams/00692ee0-e6c9-41c5-9410-79354acbce71/download) · [record](https://www.repository.cam.ac.uk/handle/1810/370042) Location: Conjecture 5.15, printed p. 88 / held PDF p. 96; definitions in the relevant chapter.

**Literature check.** Reviewed 2026-10-13: The published counterpart retains the general conjecture beyond clique cases. Current 2026 odd-Ramsey results concern specific complete bipartite or clique graphs and do not provide the theorem for every non-even-decomposable H. No general closure was located.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/root-reviews/versteegen-2024.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://onlinelibrary.wiley.com/doi/10.1002/rsa.21263) · [2](https://arxiv.org/abs/2409.11152) · [3](https://api.repository.cam.ac.uk/server/api/core/bitstreams/e8fbcbff-df10-4497-9424-255eebb24e46/content) · [4](https://arxiv.org/abs/2507.14321) · [5](https://arxiv.org/abs/2301.05202) · [6](https://arxiv.org/abs/2006.02668) · [7](https://kam.mff.cuni.cz/~spring/media/papers/6/34ConjectureForDominationGame.pdf) · [8](https://research-explorer.ista.ac.at/download/20482/20954/2026_EuropJourCombinatorics_Boyadzhiyska.pdf)

<a id="q4957"></a>

## Q4957. Uniform finite obstructions to dense binary sumsets

**Status:** Open · **Kind:** open problem (Question 5.22) · **Reviewed extraction** 2026-10-13-250

For every ε>0, is there k(ε) such that for every n and A⊂F₂^n with |A|≥ε2^n, B=F₂^n∖(A+A) can be partitioned into S₁,…,S_k with sets X₁,…,X_k⊂F₂^n such that |{x∈X_i:x·y=0}|<ε|X_i| for every i and every y∈S_i? Here x·y is the standard F₂ dot product.

**Source.** Leo Versteegen. *Games, Graphs, and Groups*. University of Cambridge, 2024. [primary source](https://www.repository.cam.ac.uk/bitstreams/00692ee0-e6c9-41c5-9410-79354acbce71/download) · [record](https://www.repository.cam.ac.uk/handle/1810/370042) Location: Question 5.22, printed p. 94 / held PDF p. 102; definitions in the relevant chapter.

**Literature check.** Reviewed 2026-10-13: The source explicitly poses this finite-obstruction question. Current approximate-Fourier/coset questions and graph-code papers do not imply it for arbitrary dense A; exact obstruction and sumset retrieval located no full resolution.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/root-reviews/versteegen-2024.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://onlinelibrary.wiley.com/doi/10.1002/rsa.21263) · [2](https://arxiv.org/abs/2409.11152) · [3](https://api.repository.cam.ac.uk/server/api/core/bitstreams/e8fbcbff-df10-4497-9424-255eebb24e46/content) · [4](https://arxiv.org/abs/2507.14321) · [5](https://arxiv.org/abs/2301.05202) · [6](https://arxiv.org/abs/2006.02668) · [7](https://kam.mff.cuni.cz/~spring/media/papers/6/34ConjectureForDominationGame.pdf) · [8](https://research-explorer.ista.ac.at/download/20482/20954/2026_EuropJourCombinatorics_Boyadzhiyska.pdf)

<a id="q4958"></a>

## Q4958. Unbounded equality of cop number and independence number

**Status:** Open · **Kind:** open problem (Question 6.9) · **Reviewed extraction** 2026-10-13-250

For every positive integer k, does some finite connected simple graph G satisfy c(G)=α(G)≥k? Here α(G) is its maximum independent-set size. In the standard perfect-information Cops and Robbers game, cops choose starting vertices, the robber then chooses a vertex, and turns alternate; each player can stay or traverse one edge, all cops move together, and capture occurs when a cop and robber occupy the same vertex. c(G) is the least number of cops with a winning strategy.

**Source.** Leo Versteegen. *Games, Graphs, and Groups*. University of Cambridge, 2024. [primary source](https://www.repository.cam.ac.uk/bitstreams/00692ee0-e6c9-41c5-9410-79354acbce71/download) · [record](https://www.repository.cam.ac.uk/handle/1810/370042) Location: Question 6.9, printed p. 105 / held PDF p. 113; definitions in the relevant chapter.

**Literature check.** Reviewed 2026-10-13: The primary 2025 clique-cover/cops paper adds a counterexample at independence number three to an earlier strict-inequality conjecture. It does not give equality at arbitrarily large independence number. The held question already knows examples through three; no unbounded family was located.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/root-reviews/versteegen-2024.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://onlinelibrary.wiley.com/doi/10.1002/rsa.21263) · [2](https://arxiv.org/abs/2409.11152) · [3](https://api.repository.cam.ac.uk/server/api/core/bitstreams/e8fbcbff-df10-4497-9424-255eebb24e46/content) · [4](https://arxiv.org/abs/2507.14321) · [5](https://arxiv.org/abs/2301.05202) · [6](https://arxiv.org/abs/2006.02668) · [7](https://kam.mff.cuni.cz/~spring/media/papers/6/34ConjectureForDominationGame.pdf) · [8](https://research-explorer.ista.ac.at/download/20482/20954/2026_EuropJourCombinatorics_Boyadzhiyska.pdf)

<a id="q4959"></a>

## Q4959. The half-order game-domination bound at minimum degree two

**Status:** Open · **Kind:** conjecture (Conjecture 8.2) · **Reviewed extraction** 2026-10-13-250

In the domination game on a finite simple graph, Dominator and Staller alternately select a vertex whose closed neighbourhood contains a previously undominated vertex. Play ends when all vertices are dominated; Dominator minimizes and Staller maximizes the number of moves. Let γ\_g(G) be that number under optimal play when Dominator starts. Does every graph G on n vertices with minimum degree at least two satisfy γ\_g(G)≤ceil(n/2)?

**Source.** Leo Versteegen. *Games, Graphs, and Groups*. University of Cambridge, 2024. [primary source](https://www.repository.cam.ac.uk/bitstreams/00692ee0-e6c9-41c5-9410-79354acbce71/download) · [record](https://www.repository.cam.ac.uk/handle/1810/370042) Location: Conjecture 8.2, printed p. 156 / held PDF p. 164; definitions in the relevant chapter.

**Literature check.** Reviewed 2026-10-13: The source and primary Portier–Versteegen theorem give (10n+1)/17, leaving the half-order bound. Fresh current minimum-degree and domination-game retrieval located restricted results but no full minimum-degree-two closure.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/root-reviews/versteegen-2024.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://onlinelibrary.wiley.com/doi/10.1002/rsa.21263) · [2](https://arxiv.org/abs/2409.11152) · [3](https://api.repository.cam.ac.uk/server/api/core/bitstreams/e8fbcbff-df10-4497-9424-255eebb24e46/content) · [4](https://arxiv.org/abs/2507.14321) · [5](https://arxiv.org/abs/2301.05202) · [6](https://arxiv.org/abs/2006.02668) · [7](https://kam.mff.cuni.cz/~spring/media/papers/6/34ConjectureForDominationGame.pdf) · [8](https://research-explorer.ista.ac.at/download/20482/20954/2026_EuropJourCombinatorics_Boyadzhiyska.pdf)

<a id="q4960"></a>

## Q4960. Rall’s half-order bound for traceable graphs

**Status:** Open · **Kind:** conjecture (Conjecture 8.25) · **Reviewed extraction** 2026-10-13-250

In the domination game on a finite simple graph, Dominator and Staller alternately select a vertex whose closed neighbourhood contains a previously undominated vertex. Play ends when all vertices are dominated; Dominator minimizes and Staller maximizes the number of moves. Let γ\_g(G) be that number under optimal play when Dominator starts. If G has a Hamiltonian path and n vertices, must γ\_g(G)≤ceil(n/2)?

**Source.** Leo Versteegen. *Games, Graphs, and Groups*. University of Cambridge, 2024. [primary source](https://www.repository.cam.ac.uk/bitstreams/00692ee0-e6c9-41c5-9410-79354acbce71/download) · [record](https://www.repository.cam.ac.uk/handle/1810/370042) Location: Conjecture 8.25, printed p. 167 / held PDF p. 175; definitions in the relevant chapter.

**Literature check.** Reviewed 2026-10-13: Current primary Rall and diameter-two studies retain the traceable-graph conjecture or support proper subcases. The source minimum-degree bound does not cover all graphs with Hamiltonian paths; no complete traceable-graph resolution was located.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/root-reviews/versteegen-2024.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://onlinelibrary.wiley.com/doi/10.1002/rsa.21263) · [2](https://arxiv.org/abs/2409.11152) · [3](https://api.repository.cam.ac.uk/server/api/core/bitstreams/e8fbcbff-df10-4497-9424-255eebb24e46/content) · [4](https://arxiv.org/abs/2507.14321) · [5](https://arxiv.org/abs/2301.05202) · [6](https://arxiv.org/abs/2006.02668) · [7](https://kam.mff.cuni.cz/~spring/media/papers/6/34ConjectureForDominationGame.pdf) · [8](https://research-explorer.ista.ac.at/download/20482/20954/2026_EuropJourCombinatorics_Boyadzhiyska.pdf)

<a id="q4961"></a>

## Q4961. Connected extremal graphs for the total-domination three-quarter bound

**Status:** Open · **Kind:** open problem (Problem 9.19) · **Reviewed extraction** 2026-10-13-250

In the total domination game on a finite simple graph, Dominator and Staller alternately select a vertex whose open neighbourhood contains a previously undominated vertex. Selecting a vertex does not itself dominate that vertex. Play ends when every vertex has a selected neighbour; Dominator minimizes and Staller maximizes the number of moves. Let γ\_tg(G) be this number under optimal play when Dominator starts. Classify all finite connected simple graphs G with n≥3 vertices satisfying γ\_tg(G)=3n/4.

**Source.** Leo Versteegen. *Games, Graphs, and Groups*. University of Cambridge, 2024. [primary source](https://www.repository.cam.ac.uk/bitstreams/00692ee0-e6c9-41c5-9410-79354acbce71/download) · [record](https://www.repository.cam.ac.uk/handle/1810/370042) Location: Problem 9.19, printed p. 190 / held PDF p. 198; definitions in the relevant chapter.

**Literature check.** Reviewed 2026-10-13: The 2025 published three-quarter theorem retains the connected extremal classification, with its known twelve-vertex tree example. Proving the universal upper bound does not classify equality cases; no later full classification was located.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/root-reviews/versteegen-2024.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://onlinelibrary.wiley.com/doi/10.1002/rsa.21263) · [2](https://arxiv.org/abs/2409.11152) · [3](https://api.repository.cam.ac.uk/server/api/core/bitstreams/e8fbcbff-df10-4497-9424-255eebb24e46/content) · [4](https://arxiv.org/abs/2507.14321) · [5](https://arxiv.org/abs/2301.05202) · [6](https://arxiv.org/abs/2006.02668) · [7](https://kam.mff.cuni.cz/~spring/media/papers/6/34ConjectureForDominationGame.pdf) · [8](https://research-explorer.ista.ac.at/download/20482/20954/2026_EuropJourCombinatorics_Boyadzhiyska.pdf)

<a id="q4962"></a>

## Q4962. Optimal asymptotic total-domination game constant at minimum degree two

**Status:** Open · **Kind:** open problem (Question 9.20) · **Reviewed extraction** 2026-10-13-250

In the total domination game on a finite simple graph, Dominator and Staller alternately select a vertex whose open neighbourhood contains a previously undominated vertex. Selecting a vertex does not itself dominate that vertex. Play ends when every vertex has a selected neighbour; Dominator minimizes and Staller maximizes the number of moves. Let γ\_tg(G) be this number under optimal play when Dominator starts. Determine inf{c>0: there is N such that γ\_tg(G)≤c|V(G)| for every graph G with minimum degree at least two and |V(G)|≥N}. In particular, is this infimum 2/3?

**Source.** Leo Versteegen. *Games, Graphs, and Groups*. University of Cambridge, 2024. [primary source](https://www.repository.cam.ac.uk/bitstreams/00692ee0-e6c9-41c5-9410-79354acbce71/download) · [record](https://www.repository.cam.ac.uk/handle/1810/370042) Location: Question 9.20, printed p. 190 / held PDF p. 198; definitions in the relevant chapter.

**Literature check.** Reviewed 2026-10-13: The published successor retains the optimal-constant question, allowing an additive one and explaining its asymptotic equivalence. Disjoint triangles force the lower bound 2/3; the known five-sevenths upper bound does not identify the infimum. No exact full result was located.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/root-reviews/versteegen-2024.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://onlinelibrary.wiley.com/doi/10.1002/rsa.21263) · [2](https://arxiv.org/abs/2409.11152) · [3](https://api.repository.cam.ac.uk/server/api/core/bitstreams/e8fbcbff-df10-4497-9424-255eebb24e46/content) · [4](https://arxiv.org/abs/2507.14321) · [5](https://arxiv.org/abs/2301.05202) · [6](https://arxiv.org/abs/2006.02668) · [7](https://kam.mff.cuni.cz/~spring/media/papers/6/34ConjectureForDominationGame.pdf) · [8](https://research-explorer.ista.ac.at/download/20482/20954/2026_EuropJourCombinatorics_Boyadzhiyska.pdf)

<a id="q4963"></a>

## Q4963. A universal additive constant above the half-order domination-game bound

**Status:** Open · **Kind:** conjecture (Conjecture 9.21) · **Reviewed extraction** 2026-10-13-250

In the domination game on a finite simple graph, Dominator and Staller alternately select a vertex whose closed neighbourhood contains a previously undominated vertex. Play ends when all vertices are dominated; Dominator minimizes and Staller maximizes the number of moves. Let γ\_g(G) be that number under optimal play when Dominator starts. Does some universal constant C satisfy γ\_g(G)≤|V(G)|/2+C for every graph G with minimum degree at least two?

**Source.** Leo Versteegen. *Games, Graphs, and Groups*. University of Cambridge, 2024. [primary source](https://www.repository.cam.ac.uk/bitstreams/00692ee0-e6c9-41c5-9410-79354acbce71/download) · [record](https://www.repository.cam.ac.uk/handle/1810/370042) Location: Conjecture 9.21, printed p. 190 / held PDF p. 198; definitions in the relevant chapter.

**Literature check.** Reviewed 2026-10-13: The source explicitly distinguishes this relaxed conjecture from the exact half-order bound. The current (10n+1)/17 theorem leaves a linear rather than constant gap; no full additive-constant result was located.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/root-reviews/versteegen-2024.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://onlinelibrary.wiley.com/doi/10.1002/rsa.21263) · [2](https://arxiv.org/abs/2409.11152) · [3](https://api.repository.cam.ac.uk/server/api/core/bitstreams/e8fbcbff-df10-4497-9424-255eebb24e46/content) · [4](https://arxiv.org/abs/2507.14321) · [5](https://arxiv.org/abs/2301.05202) · [6](https://arxiv.org/abs/2006.02668) · [7](https://kam.mff.cuni.cz/~spring/media/papers/6/34ConjectureForDominationGame.pdf) · [8](https://research-explorer.ista.ac.at/download/20482/20954/2026_EuropJourCombinatorics_Boyadzhiyska.pdf)

<a id="q4979"></a>

## Q4979. Equilateral sets of size dimension plus one in every normed space

**Status:** Open · **Kind:** stated as open (Petty conjecture, introductory discussion) · **Reviewed extraction** 2026-10-13-250

For every integer d≥1 and every d-dimensional real normed space (X,‖·‖), must there be distinct x₀,…,x_d∈X and a number c>0 with ‖x_i−x_j‖=c whenever i≠j?

**Source.** Nóra Frankl. *On some problems in combinatorial geometry*. London School of Economics and Political Science, 2020. [primary source](https://researchonline.lse.ac.uk/id/eprint/135101/1/Frankl_On-some-problems-combinatorial-geometry.pdf) · [record](https://researchonline.lse.ac.uk/id/eprint/135101/) Location: Petty conjecture, introductory discussion, printed p.106 / held PDF p.107; nearby definitions read.

**Literature check.** Reviewed 2026-10-13: The published small-codimension theorem proves restricted families. The2025 primary paper on the three-dimensional Petty space concerns one norm; the bounded dated scan found no universal lower-bound resolution.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/root-reviews/frankl-2020.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://link.springer.com/article/10.1007/s00454-023-00526-9) · [2](https://link.springer.com/article/10.1007/s00454-023-00489-x) · [3](https://eprints.lse.ac.uk/101727/1/Embedding_graphs_in_Euclidean_space.pdf) · [4](https://arxiv.org/abs/1912.00224) · [5](https://link.springer.com/article/10.1007/s00454-023-00503-2) · [6](https://link.springer.com/article/10.1007/s00454-020-00272-2) · [7](https://arxiv.org/abs/2609.36220) · [8](https://arxiv.org/abs/2608.11736) · [9](https://arxiv.org/abs/2510.15677) · [10](https://arxiv.org/abs/2511.09673)

<a id="q4980"></a>

## Q4980. The chromatic number of the Euclidean plane

**Status:** Open · **Kind:** stated as open (Introductory Hadwiger–Nelson discussion) · **Reviewed extraction** 2026-10-13-250

Determine the least integer q for which there is a colouring c:ℝ²→{1,…,q} with c(x)≠c(y) whenever ‖x−y‖₂=1. The colouring is arbitrary; no measurability condition is imposed.

**Source.** Nóra Frankl. *On some problems in combinatorial geometry*. London School of Economics and Political Science, 2020. [primary source](https://researchonline.lse.ac.uk/id/eprint/135101/1/Frankl_On-some-problems-combinatorial-geometry.pdf) · [record](https://researchonline.lse.ac.uk/id/eprint/135101/) Location: Introductory Hadwiger–Nelson discussion, printed p.13 / held PDF p.14; nearby definitions read.

**Literature check.** Reviewed 2026-10-13: The September2026 Alon–Bucić–Davies typical-norm theorem explicitly distinguishes its new2d result from the Euclidean problem. The full Euclidean value was not resolved in the current primary scan.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/root-reviews/frankl-2020.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://link.springer.com/article/10.1007/s00454-023-00526-9) · [2](https://link.springer.com/article/10.1007/s00454-023-00489-x) · [3](https://eprints.lse.ac.uk/101727/1/Embedding_graphs_in_Euclidean_space.pdf) · [4](https://arxiv.org/abs/1912.00224) · [5](https://link.springer.com/article/10.1007/s00454-023-00503-2) · [6](https://link.springer.com/article/10.1007/s00454-020-00272-2) · [7](https://arxiv.org/abs/2609.36220) · [8](https://arxiv.org/abs/2608.11736) · [9](https://arxiv.org/abs/2510.15677) · [10](https://arxiv.org/abs/2511.09673)

<a id="q4981"></a>

## Q4981. Classify finite Euclidean Ramsey sets

**Status:** Open · **Kind:** open problem (Introductory Euclidean Ramsey discussion) · **Reviewed extraction** 2026-10-13-250

Characterize the finite sets S⊂ℝᵈ, allowing any d≥1, such that for every integer k≥1 there is an integer D≥d for which every colouring of ℝᴰ with at most k colours has a monochromatic isometric copy of S.

**Source.** Nóra Frankl. *On some problems in combinatorial geometry*. London School of Economics and Political Science, 2020. [primary source](https://researchonline.lse.ac.uk/id/eprint/135101/1/Frankl_On-some-problems-combinatorial-geometry.pdf) · [record](https://researchonline.lse.ac.uk/id/eprint/135101/) Location: Introductory Euclidean Ramsey discussion, printed p.15 / held PDF p.16; nearby definitions read.

**Literature check.** Reviewed 2026-10-13: The2025 Behague primary abstract retains the spherical Ramsey conjecture, and Mirabi’s August2026 one-point-extension theorem supplies a construction operation, not an all-set characterization. No full classification was located.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/root-reviews/frankl-2020.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://link.springer.com/article/10.1007/s00454-023-00526-9) · [2](https://link.springer.com/article/10.1007/s00454-023-00489-x) · [3](https://eprints.lse.ac.uk/101727/1/Embedding_graphs_in_Euclidean_space.pdf) · [4](https://arxiv.org/abs/1912.00224) · [5](https://link.springer.com/article/10.1007/s00454-023-00503-2) · [6](https://link.springer.com/article/10.1007/s00454-020-00272-2) · [7](https://arxiv.org/abs/2609.36220) · [8](https://arxiv.org/abs/2608.11736) · [9](https://arxiv.org/abs/2510.15677) · [10](https://arxiv.org/abs/2511.09673)

<a id="q4982"></a>

## Q4982. Tree-copy counts as powers of point count and unit-distance extremals

**Status:** Open · **Kind:** conjecture (Conjecture2.12) · **Reviewed extraction** 2026-10-13-250

For a fixed finite tree T, let C_T(n) be the maximum, over n-point sets P⊂ℝ² and assignments of a positive length δ\_e to each edge e of T, of the number of injective maps f:V(T)→P with ‖f(u)−f(v)‖₂=δ\_{uv} on every edge. Let u₂(n) be the maximum number of unordered unit-distance pairs in an n-point planar set. For every fixed tree T, do there exist integers m,ℓ∈ℤ such that C_T(n)=Θ\_T(n^m u₂(n)^ℓ) as n→∞?

**Source.** Nóra Frankl. *On some problems in combinatorial geometry*. London School of Economics and Political Science, 2020. [primary source](https://researchonline.lse.ac.uk/id/eprint/135101/1/Frankl_On-some-problems-combinatorial-geometry.pdf) · [record](https://researchonline.lse.ac.uk/id/eprint/135101/) Location: Conjecture2.12, printed p.39 / held PDF p.40; nearby definitions read.

**Literature check.** Reviewed 2026-10-13: The source asks this planar prescribed-length tree question after its path results. The current Frankl–Woodruff publication treats spherical paths/cycles and3-dimensional3-regular patterns; the bounded exact-tree scan found no theorem resolving this planar target.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/root-reviews/frankl-2020.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://link.springer.com/article/10.1007/s00454-023-00526-9) · [2](https://link.springer.com/article/10.1007/s00454-023-00489-x) · [3](https://eprints.lse.ac.uk/101727/1/Embedding_graphs_in_Euclidean_space.pdf) · [4](https://arxiv.org/abs/1912.00224) · [5](https://link.springer.com/article/10.1007/s00454-023-00503-2) · [6](https://link.springer.com/article/10.1007/s00454-020-00272-2) · [7](https://arxiv.org/abs/2609.36220) · [8](https://arxiv.org/abs/2608.11736) · [9](https://arxiv.org/abs/2510.15677) · [10](https://arxiv.org/abs/2511.09673)

<a id="q4983"></a>

## Q4983. Prescribed-distance copies of a twice-subdivided three-arm star

**Status:** Open · **Kind:** open problem (Problem2.13) · **Reviewed extraction** 2026-10-13-250

For a fixed finite tree T, let C_T(n) be the maximum, over n-point sets P⊂ℝ² and assignments of a positive length δ\_e to each edge e of T, of the number of injective maps f:V(T)→P with ‖f(u)−f(v)‖₂=δ\_{uv} on every edge. Let u₂(n) be the maximum number of unordered unit-distance pairs in an n-point planar set. Let T_{2,3} consist of three paths of two edges sharing just their initial vertex. Is C_{T_{2,3}}(n)=Θ(n³)?

**Source.** Nóra Frankl. *On some problems in combinatorial geometry*. London School of Economics and Political Science, 2020. [primary source](https://researchonline.lse.ac.uk/id/eprint/135101/1/Frankl_On-some-problems-combinatorial-geometry.pdf) · [record](https://researchonline.lse.ac.uk/id/eprint/135101/) Location: Problem2.13, printed p.39 / held PDF p.40; nearby definitions read.

**Literature check.** Reviewed 2026-10-13: The source asks this planar prescribed-length tree question after its path results. The current Frankl–Woodruff publication treats spherical paths/cycles and3-dimensional3-regular patterns; the bounded exact-tree scan found no theorem resolving this planar target.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/root-reviews/frankl-2020.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://link.springer.com/article/10.1007/s00454-023-00526-9) · [2](https://link.springer.com/article/10.1007/s00454-023-00489-x) · [3](https://eprints.lse.ac.uk/101727/1/Embedding_graphs_in_Euclidean_space.pdf) · [4](https://arxiv.org/abs/1912.00224) · [5](https://link.springer.com/article/10.1007/s00454-023-00503-2) · [6](https://link.springer.com/article/10.1007/s00454-020-00272-2) · [7](https://arxiv.org/abs/2609.36220) · [8](https://arxiv.org/abs/2608.11736) · [9](https://arxiv.org/abs/2510.15677) · [10](https://arxiv.org/abs/2511.09673)

<a id="q4984"></a>

## Q4984. Prescribed-distance copies of a three-edge-arm star

**Status:** Open · **Kind:** open problem (Problem2.14) · **Reviewed extraction** 2026-10-13-250

For a fixed finite tree T, let C_T(n) be the maximum, over n-point sets P⊂ℝ² and assignments of a positive length δ\_e to each edge e of T, of the number of injective maps f:V(T)→P with ‖f(u)−f(v)‖₂=δ\_{uv} on every edge. Let u₂(n) be the maximum number of unordered unit-distance pairs in an n-point planar set. Let T_{3,3} consist of three paths of three edges sharing just their initial vertex. Is C_{T_{3,3}}(n)=Θ(max{n⁴,u₂(n)³})?

**Source.** Nóra Frankl. *On some problems in combinatorial geometry*. London School of Economics and Political Science, 2020. [primary source](https://researchonline.lse.ac.uk/id/eprint/135101/1/Frankl_On-some-problems-combinatorial-geometry.pdf) · [record](https://researchonline.lse.ac.uk/id/eprint/135101/) Location: Problem2.14, printed p.39 / held PDF p.40; nearby definitions read.

**Literature check.** Reviewed 2026-10-13: The source asks this planar prescribed-length tree question after its path results. The current Frankl–Woodruff publication treats spherical paths/cycles and3-dimensional3-regular patterns; the bounded exact-tree scan found no theorem resolving this planar target.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/root-reviews/frankl-2020.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://link.springer.com/article/10.1007/s00454-023-00526-9) · [2](https://link.springer.com/article/10.1007/s00454-023-00489-x) · [3](https://eprints.lse.ac.uk/101727/1/Embedding_graphs_in_Euclidean_space.pdf) · [4](https://arxiv.org/abs/1912.00224) · [5](https://link.springer.com/article/10.1007/s00454-023-00503-2) · [6](https://link.springer.com/article/10.1007/s00454-020-00272-2) · [7](https://arxiv.org/abs/2609.36220) · [8](https://arxiv.org/abs/2608.11736) · [9](https://arxiv.org/abs/2510.15677) · [10](https://arxiv.org/abs/2511.09673)

<a id="q4985"></a>

## Q4985. One complementary graph has half-order Euclidean dimension

**Status:** Open · **Kind:** open problem (Problem3.16) · **Reviewed extraction** 2026-10-13-250

For every integer d≥1 and every finite simple graph G on2d+1 vertices, must either G or its complement admit an injective placement of its vertices in ℝᵈ with every edge having Euclidean length1? Nonedges may also have length1.

**Source.** Nóra Frankl. *On some problems in combinatorial geometry*. London School of Economics and Political Science, 2020. [primary source](https://researchonline.lse.ac.uk/id/eprint/135101/1/Frankl_On-some-problems-combinatorial-geometry.pdf) · [record](https://researchonline.lse.ac.uk/id/eprint/135101/) Location: Problem3.16, printed p.54 / held PDF p.55; nearby definitions read.

**Literature check.** Reviewed 2026-10-13: The primary graph-embedding paper gives the adjacent upper/lower bounds. Newer annulus/rigid-pattern results retrieved concern other notions, and no exact half-order Euclidean-dimension closure was located.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/root-reviews/frankl-2020.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://link.springer.com/article/10.1007/s00454-023-00526-9) · [2](https://link.springer.com/article/10.1007/s00454-023-00489-x) · [3](https://eprints.lse.ac.uk/101727/1/Embedding_graphs_in_Euclidean_space.pdf) · [4](https://arxiv.org/abs/1912.00224) · [5](https://link.springer.com/article/10.1007/s00454-023-00503-2) · [6](https://link.springer.com/article/10.1007/s00454-020-00272-2) · [7](https://arxiv.org/abs/2609.36220) · [8](https://arxiv.org/abs/2608.11736) · [9](https://arxiv.org/abs/2510.15677) · [10](https://arxiv.org/abs/2511.09673)

<a id="q4986"></a>

## Q4986. Smiling congruent copies of every bouquet

**Status:** Open · **Kind:** conjecture (Conjecture4.1) · **Reviewed extraction** 2026-10-13-250

Let C₁,…,C_n be unit circles in ℝ² sharing a specified point O. For every finite colouring c of ℝ² using at least two colours, must there be a Euclidean isometry f, points p_i∈f(C_i), and a colour a such that c(p_i)=a for every i but c(f(O))≠a?

**Source.** Nóra Frankl. *On some problems in combinatorial geometry*. London School of Economics and Political Science, 2020. [primary source](https://researchonline.lse.ac.uk/id/eprint/135101/1/Frankl_On-some-problems-combinatorial-geometry.pdf) · [record](https://researchonline.lse.ac.uk/id/eprint/135101/) Location: Conjecture4.1, printed p.55 / held PDF p.56; nearby definitions read.

**Literature check.** Reviewed 2026-10-13: Published2023 Conjecture1.1 retains exactly the unrestricted bouquet question, while its lattice-like theorem requires proper colouring. The current bounded bouquet scan found no general closure.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/root-reviews/frankl-2020.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://link.springer.com/article/10.1007/s00454-023-00526-9) · [2](https://link.springer.com/article/10.1007/s00454-023-00489-x) · [3](https://eprints.lse.ac.uk/101727/1/Embedding_graphs_in_Euclidean_space.pdf) · [4](https://arxiv.org/abs/1912.00224) · [5](https://link.springer.com/article/10.1007/s00454-023-00503-2) · [6](https://link.springer.com/article/10.1007/s00454-020-00272-2) · [7](https://arxiv.org/abs/2609.36220) · [8](https://arxiv.org/abs/2608.11736) · [9](https://arxiv.org/abs/2510.15677) · [10](https://arxiv.org/abs/2511.09673)

<a id="q4987"></a>

## Q4987. Almost-monochromatic configurations in progression-free colourings

**Status:** Open · **Kind:** open problem (Problem4.4) · **Reviewed extraction** 2026-10-13-250

For each integer d≥1, characterize pairs (S,s₀) with finite S⊂ℝᵈ, |S|≥3 and s₀∈S, such that every finite colouring c:ℝᵈ→A containing no monochromatic infinite arithmetic progression {x+nv:n∈ℕ} with v≠0 has a similar copy f(S) on which f(S∖{s₀}) is monochromatic but f(s₀) has a different colour. A similarity f is an isometry composed with multiplication by a nonzero scalar.

**Source.** Nóra Frankl. *On some problems in combinatorial geometry*. London School of Economics and Political Science, 2020. [primary source](https://researchonline.lse.ac.uk/id/eprint/135101/1/Frankl_On-some-problems-combinatorial-geometry.pdf) · [record](https://researchonline.lse.ac.uk/id/eprint/135101/) Location: Problem4.4, printed p.56 / held PDF p.57; nearby definitions read.

**Literature check.** Reviewed 2026-10-13: Published2023 Problem1.4 retains this full classification after proving the integral case. The contemporary general Euclidean-Ramsey extension results have a different congruence target; no full AM classification was located.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/root-reviews/frankl-2020.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://link.springer.com/article/10.1007/s00454-023-00526-9) · [2](https://link.springer.com/article/10.1007/s00454-023-00489-x) · [3](https://eprints.lse.ac.uk/101727/1/Embedding_graphs_in_Euclidean_space.pdf) · [4](https://arxiv.org/abs/1912.00224) · [5](https://link.springer.com/article/10.1007/s00454-023-00503-2) · [6](https://link.springer.com/article/10.1007/s00454-020-00272-2) · [7](https://arxiv.org/abs/2609.36220) · [8](https://arxiv.org/abs/2608.11736) · [9](https://arxiv.org/abs/2510.15677) · [10](https://arxiv.org/abs/2511.09673)

<a id="q4988"></a>

## Q4988. Product constructions maximize nearly k-distance sets except finitely often

**Status:** Open · **Kind:** conjecture (Conjecture5.3) · **Reviewed extraction** 2026-10-13-250

For integers k,d≥1, let m_k(d) be the maximum cardinality of a finite subset of ℝᵈ with at most k distinct distances between its points. A finite set is ε-nearly k-distance if its pairwise distances lie in ⋃\_{i=1}^k[t_i,t_i+ε] for some 1≤t₁≤⋯≤t_k. Let M_k(d)=lim_{ε↓0} max{|S|:S⊂ℝᵈ is ε-nearly k-distance}. Define M′\_k(d)=max{∏\_{i=1}^s m_{k_i}(d_i):s≥1, k_i≥1, d_i≥0, Σ\_i k_i=k, Σ\_i d_i=d}, using m_j(0)=1. Is M_k(d)=M′\_k(d) for all but finitely many integer pairs (k,d) with k,d≥1?

**Source.** Nóra Frankl. *On some problems in combinatorial geometry*. London School of Economics and Political Science, 2020. [primary source](https://researchonline.lse.ac.uk/id/eprint/135101/1/Frankl_On-some-problems-combinatorial-geometry.pdf) · [record](https://researchonline.lse.ac.uk/id/eprint/135101/) Location: Conjecture5.3, printed p.77 / held PDF p.78; nearby definitions read.

**Literature check.** Reviewed 2026-10-13: Published2023 Conjecture1.11 retains this equality together with a further flat-set equality. Its fixed-k large-d theorem and small-k theorems do not settle globally finite exceptions; no later full closure was located.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/root-reviews/frankl-2020.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://link.springer.com/article/10.1007/s00454-023-00526-9) · [2](https://link.springer.com/article/10.1007/s00454-023-00489-x) · [3](https://eprints.lse.ac.uk/101727/1/Embedding_graphs_in_Euclidean_space.pdf) · [4](https://arxiv.org/abs/1912.00224) · [5](https://link.springer.com/article/10.1007/s00454-023-00503-2) · [6](https://link.springer.com/article/10.1007/s00454-020-00272-2) · [7](https://arxiv.org/abs/2609.36220) · [8](https://arxiv.org/abs/2608.11736) · [9](https://arxiv.org/abs/2510.15677) · [10](https://arxiv.org/abs/2511.09673)

<a id="q4989"></a>

## Q4989. Removing flatness losses from nearly k-distance extremals

**Status:** Open · **Kind:** open problem (Problem5.27) · **Reviewed extraction** 2026-10-13-250

For integers k,d≥1, let m_k(d) be the maximum cardinality of a finite subset of ℝᵈ with at most k distinct distances between its points. A finite set is ε-nearly k-distance if its pairwise distances lie in ⋃\_{i=1}^k[t_i,t_i+ε] for some 1≤t₁≤⋯≤t_k. Let M_k(d)=lim_{ε↓0} max{|S|:S⊂ℝᵈ is ε-nearly k-distance}. For S⊂ℝ^{d+1}, call S (d,α)-flat at p∈S if some d-dimensional linear subspace makes angle at most α with every nonzero vector p−q for q∈S. Let N_k(d+1) be the largest N such that for every ε,α>0 there is an ε-nearly k-distance set S⊂ℝ^{d+1} of size N flat at every p∈S. Define A_k(d+1,d) in the same way, allowing at most two exceptional p. For every k,d≥1, is A_k(d+1,d)=N_k(d+1)=M_k(d)?

**Source.** Nóra Frankl. *On some problems in combinatorial geometry*. London School of Economics and Political Science, 2020. [primary source](https://researchonline.lse.ac.uk/id/eprint/135101/1/Frankl_On-some-problems-combinatorial-geometry.pdf) · [record](https://researchonline.lse.ac.uk/id/eprint/135101/) Location: Problem5.27, printed p.102 / held PDF p.103; nearby definitions read.

**Literature check.** Reviewed 2026-10-13: The published successor still conjectures N_k(d+1)=M_k(d), while proving restricted small-k/large-d regimes. The source’s stronger almost-flat equality was not resolved in the checked primary literature.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/root-reviews/frankl-2020.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://link.springer.com/article/10.1007/s00454-023-00526-9) · [2](https://link.springer.com/article/10.1007/s00454-023-00489-x) · [3](https://eprints.lse.ac.uk/101727/1/Embedding_graphs_in_Euclidean_space.pdf) · [4](https://arxiv.org/abs/1912.00224) · [5](https://link.springer.com/article/10.1007/s00454-023-00503-2) · [6](https://link.springer.com/article/10.1007/s00454-020-00272-2) · [7](https://arxiv.org/abs/2609.36220) · [8](https://arxiv.org/abs/2608.11736) · [9](https://arxiv.org/abs/2510.15677) · [10](https://arxiv.org/abs/2511.09673)

<a id="q4990"></a>

## Q4990. Exact nearly k-distance extremals at fixed dimension and large k

**Status:** Open · **Kind:** open problem (Problem5.28) · **Reviewed extraction** 2026-10-13-250

For integers k,d≥1, let m_k(d) be the maximum cardinality of a finite subset of ℝᵈ with at most k distinct distances between its points. A finite set is ε-nearly k-distance if its pairwise distances lie in ⋃\_{i=1}^k[t_i,t_i+ε] for some 1≤t₁≤⋯≤t_k. Let M_k(d)=lim_{ε↓0} max{|S|:S⊂ℝᵈ is ε-nearly k-distance}. For every fixed integer d≥1, determine the exact value of M_k(d) for all sufficiently large integers k, with the threshold allowed to depend on d.

**Source.** Nóra Frankl. *On some problems in combinatorial geometry*. London School of Economics and Political Science, 2020. [primary source](https://researchonline.lse.ac.uk/id/eprint/135101/1/Frankl_On-some-problems-combinatorial-geometry.pdf) · [record](https://researchonline.lse.ac.uk/id/eprint/135101/) Location: Problem5.28, printed p.102 / held PDF p.103; nearby definitions read.

**Literature check.** Reviewed 2026-10-13: The source and published successor provide the order of growth and particular regimes, but not the requested exact fixed-d large-k values. No complete later formula was located in the bounded current-primary scan.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/root-reviews/frankl-2020.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://link.springer.com/article/10.1007/s00454-023-00526-9) · [2](https://link.springer.com/article/10.1007/s00454-023-00489-x) · [3](https://eprints.lse.ac.uk/101727/1/Embedding_graphs_in_Euclidean_space.pdf) · [4](https://arxiv.org/abs/1912.00224) · [5](https://link.springer.com/article/10.1007/s00454-023-00503-2) · [6](https://link.springer.com/article/10.1007/s00454-020-00272-2) · [7](https://arxiv.org/abs/2609.36220) · [8](https://arxiv.org/abs/2608.11736) · [9](https://arxiv.org/abs/2510.15677) · [10](https://arxiv.org/abs/2511.09673)

<a id="q5012"></a>

## Q5012. Disconnected placements in a three-dimensional convex Kakeya body

**Status:** Open · **Kind:** open problem (Question 2.5.1) · **Reviewed extraction** 2026-10-13-250

A compact convex set K⊂R^d is S-Kakeya if, for every ρ∈SO(d), some w∈R^d satisfies ρS+w⊂K. Two placements (ρ₀,w₀),(ρ₁,w₁) connect within K if continuous paths ρ:[0,1]→SO(d), w:[0,1]→R^d join them and satisfy ρ(t)S+w(t)⊂K throughout. Do there exist nonempty compact convex S,K⊂R³ such that K is S-Kakeya and two placements of S in K cannot connect within K?

**Source.** Barnabás Janzer. *Extremal results for graphs and hypergraphs and other combinatorial problems*. University of Cambridge, 2023. [primary source](https://www.repository.cam.ac.uk/bitstreams/8d9c782b-f6e1-4de5-9505-54ac2d6a7627/download) · [record](https://www.repository.cam.ac.uk/handle/1810/357672) Location: Question 2.5.1, printed p. 31 / held PDF p. 39; definitions in the same source chapter.

**Literature check.** Reviewed 2026-10-13: The published 2024 paper retains this question as Question5.1; its counterexample needs d≥4. No later exact three-dimensional resolution was located in the dated primary scan.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/root-reviews/janzer-2023.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://link.springer.com/article/10.1007/s00454-024-00639-9)

<a id="q5013"></a>

## Q5013. Shapes with connected placements in every convex Kakeya body

**Status:** Open · **Kind:** open problem (Question 2.5.2) · **Reviewed extraction** 2026-10-13-250

A compact convex set K⊂R^d is S-Kakeya if, for every ρ∈SO(d), some w∈R^d satisfies ρS+w⊂K. Two placements (ρ₀,w₀),(ρ₁,w₁) connect within K if continuous paths ρ:[0,1]→SO(d), w:[0,1]→R^d join them and satisfy ρ(t)S+w(t)⊂K throughout. Does there exist d≥3 and a nonempty compact convex S⊂R^d, neither a segment nor a closed Euclidean ball, such that any two placements of S connect within every compact convex S-Kakeya set K?

**Source.** Barnabás Janzer. *Extremal results for graphs and hypergraphs and other combinatorial problems*. University of Cambridge, 2023. [primary source](https://www.repository.cam.ac.uk/bitstreams/8d9c782b-f6e1-4de5-9505-54ac2d6a7627/download) · [record](https://www.repository.cam.ac.uk/handle/1810/357672) Location: Question 2.5.2, printed p. 32 / held PDF p. 40; definitions in the same source chapter.

**Literature check.** Reviewed 2026-10-13: The published 2024 paper retains this question as Question5.2. Segments and balls are known positive cases; arbitrary shapes have higher-dimensional counterexamples. No exact new-shape answer was located in the bounded scan.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/root-reviews/janzer-2023.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://link.springer.com/article/10.1007/s00454-024-00639-9)

<a id="q5014"></a>

## Q5014. Nearly linear exact shuffles for every fixed tuple size

**Status:** Open · **Kind:** open problem (Question 9.4.2) · **Reviewed extraction** 2026-10-13-250

A lazy transposition on [n] independently applies a specified swap (a,b) with a specified probability p∈[0,1], and otherwise does nothing. Let U_k^all(n) be the minimum length of one sequence of independent lazy transpositions whose product sends every ordered tuple of k distinct starting elements to the uniform distribution on all (n)\_k=n(n−1)⋯(n−k+1) ordered distinct tuples. For every fixed positive integer k and every ε>0, is U_k^all(n)=O_(k,ε)(n^(1+ε)) as n→∞?

**Source.** Barnabás Janzer. *Extremal results for graphs and hypergraphs and other combinatorial problems*. University of Cambridge, 2023. [primary source](https://www.repository.cam.ac.uk/bitstreams/8d9c782b-f6e1-4de5-9505-54ac2d6a7627/download) · [record](https://www.repository.cam.ac.uk/handle/1810/357672) Location: Question 9.4.2, printed p. 133 / held PDF p. 141; definitions in the same source chapter.

**Literature check.** Reviewed 2026-10-13: The primary shuffle paper retains the full fixed-k question. The known k=1 Θ(n log n) and k=2 O(n log²n) bounds answer only small-k cases. The 2025 reachability paper concerns positive-probability destinations from a fixed starting tuple. No full exact fixed-k result was located.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/root-reviews/janzer-2023.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://arxiv.org/pdf/2210.13286) · [2](https://epubs.siam.org/doi/pdf/10.1137/22M1530677?download=true) · [3](https://dmtcs.episciences.org/16803/pdf)

<a id="q5015"></a>

## Q5015. The sharp order of exact all-pair shuffling

**Status:** Open · **Kind:** open problem (Question 9.4.3) · **Reviewed extraction** 2026-10-13-250

A lazy transposition on [n] independently applies a specified swap (a,b) with a specified probability p∈[0,1], and otherwise does nothing. Let U_k^all(n) be the minimum length of one sequence of independent lazy transpositions whose product sends every ordered tuple of k distinct starting elements to the uniform distribution on all (n)\_k=n(n−1)⋯(n−k+1) ordered distinct tuples. Is U_2^all(n)=Θ(n log n) as n→∞?

**Source.** Barnabás Janzer. *Extremal results for graphs and hypergraphs and other combinatorial problems*. University of Cambridge, 2023. [primary source](https://www.repository.cam.ac.uk/bitstreams/8d9c782b-f6e1-4de5-9505-54ac2d6a7627/download) · [record](https://www.repository.cam.ac.uk/handle/1810/357672) Location: Question 9.4.3, printed p. 133 / held PDF p. 141; definitions in the same source chapter.

**Literature check.** Reviewed 2026-10-13: The primary paper retains this sharper question, with Ω(n log n) and O(n log²n) bounds. Current dated primary retrieval found no matching Θ(n log n) all-pair result.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/root-reviews/janzer-2023.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://arxiv.org/pdf/2210.13286) · [2](https://epubs.siam.org/doi/pdf/10.1137/22M1530677?download=true) · [3](https://dmtcs.episciences.org/16803/pdf)

<a id="q5016"></a>

## Q5016. Sharp lengths of all-tuple reachability networks

**Status:** Open · **Kind:** open problem (Question 9.4.4) · **Reviewed extraction** 2026-10-13-250

For fixed k≥1, let R_k^all(n) be the minimum length of one sequence of independent lazy transpositions on [n] whose product sends every ordered tuple of k distinct starting elements to every ordered tuple of k distinct destinations with positive probability. A lazy transposition independently applies a specified swap with a specified probability in [0,1], otherwise doing nothing. Determine R_k^all(n) exactly or to leading asymptotic order as n→∞, with no restriction that swaps share a common endpoint.

**Source.** Barnabás Janzer. *Extremal results for graphs and hypergraphs and other combinatorial problems*. University of Cambridge, 2023. [primary source](https://www.repository.cam.ac.uk/bitstreams/8d9c782b-f6e1-4de5-9505-54ac2d6a7627/download) · [record](https://www.repository.cam.ac.uk/handle/1810/357672) Location: Question 9.4.4, printed p. 133 / held PDF p. 141; definitions in the same source chapter.

**Literature check.** Reviewed 2026-10-13: Thesis Question9.4.4 and primary Question4.4 ask this exact/leading-order target. The 2025 fixed-start t-reachability results do not determine the simultaneous all-start quantity. No complete fixed-k classification was located.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/root-reviews/janzer-2023.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://arxiv.org/pdf/2210.13286) · [2](https://epubs.siam.org/doi/pdf/10.1137/22M1530677?download=true) · [3](https://dmtcs.episciences.org/16803/pdf)

<a id="q5017"></a>

## Q5017. Leading constants for clique bootstrap running times

**Status:** Open · **Kind:** open problem (Problem 8.4.1) · **Reviewed extraction** 2026-10-13-250

Fix integers k>r≥2. On vertex set [n], start with any set of infected r-element edges. In each parallel round infect every edge belonging to a copy of the complete r-uniform hypergraph K_k^(r) that is missing at most one edge; retain previous infections. Let M_k^r(n) be the maximum, over all initial infections, of the number of rounds until no further edge is infected. For each fixed k>r≥2, does lim_(n→∞) M_k^r(n)/n^r exist, and if so what is its value?

**Source.** Barnabás Janzer. *Extremal results for graphs and hypergraphs and other combinatorial problems*. University of Cambridge, 2023. [primary source](https://www.repository.cam.ac.uk/bitstreams/8d9c782b-f6e1-4de5-9505-54ac2d6a7627/download) · [record](https://www.repository.cam.ac.uk/handle/1810/357672) Location: Problem 8.4.1, printed p. 115 / held PDF p. 123; definitions in the same source chapter.

**Literature check.** Reviewed 2026-10-13: Published2024 Problem11 retains this question. A 2026 primary paper improves upper constants through Turán density π(F−e), including a nontrivial clique upper bound; this is partial progress, without matching general constants or a full limit classification. No exact general limit was located.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/root-reviews/janzer-2023.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://eprints.lse.ac.uk/120360/1/1_s2.0_S0195669823001002_main.pdf) · [2](https://arxiv.org/abs/2208.13489) · [3](https://arxiv.org/html/2604.22630v2)

<a id="q5018"></a>

## Q5018. Maximum running times of multi-edge clique infections

**Status:** Open · **Kind:** open problem (Problem 8.4.2) · **Reviewed extraction** 2026-10-13-250

For fixed integers k>r≥2 and 1≤m≤binom(k,r), start with any infected r-element edges on [n]. In each parallel round, for every k-vertex set currently missing at most m of its r-element edges, infect all those missing edges. Let M_(K_k^(r),m)(n) be the maximum number of rounds until stabilization over all initial infections. Determine its asymptotic growth as n→∞ for every fixed triple (k,r,m).

**Source.** Barnabás Janzer. *Extremal results for graphs and hypergraphs and other combinatorial problems*. University of Cambridge, 2023. [primary source](https://www.repository.cam.ac.uk/bitstreams/8d9c782b-f6e1-4de5-9505-54ac2d6a7627/download) · [record](https://www.repository.cam.ac.uk/handle/1810/357672) Location: Problem 8.4.2, printed p. 116 / held PDF p. 124; definitions in the same source chapter.

**Literature check.** Reviewed 2026-10-13: Published2024 Problem12 retains the general classification. It solves (k,r,m)=(4,3,2) exactly and (5,3,2) up to Θ(n³), alongside ordinary m=1 orders. The 2026 Turán-density upper-bound theorem adds ordinary-process partial progress; a matching classification for every multi-infection triple was not located.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/root-reviews/janzer-2023.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://eprints.lse.ac.uk/120360/1/1_s2.0_S0195669823001002_main.pdf) · [2](https://arxiv.org/abs/2208.13489) · [3](https://arxiv.org/html/2604.22630v2)

<a id="q5019"></a>

## Q5019. Copies of K6 with no rainbow K4

**Status:** Open · **Kind:** stated as open (Source discussion §5.5.1) · **Reviewed extraction** 2026-10-13-250

Let ex(n,K₆,rainbow-K₄) be the maximum number of six-vertex cliques in an n-vertex finite simple graph with a proper edge-colouring containing no rainbow K₄. Proper means incident edges have different colours, and rainbow means all six edges of the K₄ have distinct colours. Determine the asymptotic order of ex(n,K₆,rainbow-K₄) as n→∞.

**Source.** Barnabás Janzer. *Extremal results for graphs and hypergraphs and other combinatorial problems*. University of Cambridge, 2023. [primary source](https://www.repository.cam.ac.uk/bitstreams/8d9c782b-f6e1-4de5-9505-54ac2d6a7627/download) · [record](https://www.repository.cam.ac.uk/handle/1810/357672) Location: Source discussion §5.5.1, printed p. 57 / held PDF p. 65; definitions in the same source chapter.

**Literature check.** Reviewed 2026-10-13: The source discussion retains the (6,4) case after proving its construction. Current primary clique/rainbow scans found no matching order; the same-rainbow-Kr result in the primary abstract is a different target.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/root-reviews/janzer-2023.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://arxiv.org/abs/2003.02754)

<a id="q5020"></a>

## Q5020. Monochromatic initial sums with fixed endpoint coefficients

**Status:** Open · **Kind:** open problem (Question 3.5) · **Reviewed extraction** 2026-10-13-250

For every finite colouring c:N_{>0}→{1,…,q}, does there exist a sequence (y_i)\_(i≥1) of positive integers such that all sums Σ\_(i=1)^k a_i y_i, for every k≥1 and all a_i∈{1,2} with a_1=a_k=1, have one common colour? Every sum uses the complete initial segment y_1,…,y_k; no zero coefficients or gaps are allowed.

**Source.** Maria Ivan. *Poset saturation and other combinatorial results*. University of Cambridge, 2023. [primary source](https://www.repository.cam.ac.uk/bitstreams/f145b6b3-ef5a-412e-b9c9-f8723aa14b33/download) · [record](https://www.repository.cam.ac.uk/handle/1810/352866) Location: Question 3.5, printed p. 57 / held PDF p. 69; definitions in the same chapter.

**Literature check.** Reviewed 2026-10-13: The primary word/Ramsey paper retains Question5 with these precise endpoint/no-gap restrictions. Related Hindman–Leader–Strauss and Milliken–Taylor statements have different coefficient/index patterns. No exact answer was located in the dated scan.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/root-reviews/ivan-2023.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://arxiv.org/pdf/2010.09081)

<a id="q5021"></a>

## Q5021. Preventing monochromatic word concatenations across bounded gaps

**Status:** Open · **Kind:** open problem (Question 3.6) · **Reviewed extraction** 2026-10-13-250

Let X be any nonempty alphabet, finite or infinite, and let x=x_1x_2⋯ be an infinite word that is not eventually periodic. Let X\* here denote its nonempty finite words. For a factor u of x, let A_x(u) be the first position where u occurs and B_x(u)=A_x(u)+|u|, the position just after that occurrence. Must there exist a finite colouring of X\* for which no infinite sequence of factors (u_i) and finite integer C≥0 satisfy 0≤A_x(u_(i+1))−B_x(u_i)≤C for every i, while all concatenations u_(k_1)⋯u_(k_j), j≥1 and k_1<⋯&lt;k_j, have one common colour?

**Source.** Maria Ivan. *Poset saturation and other combinatorial results*. University of Cambridge, 2023. [primary source](https://www.repository.cam.ac.uk/bitstreams/f145b6b3-ef5a-412e-b9c9-f8723aa14b33/download) · [record](https://www.repository.cam.ac.uk/handle/1810/352866) Location: Question 3.6, printed p. 58 / held PDF p. 70; definitions in the same chapter.

**Literature check.** Reviewed 2026-10-13: The primary paper retains Question6. Its eventual-periodicity characterization settles C=0; shift-orbit-closure and sequential-colouring results do not settle bounded first-occurrence gaps. No full answer was located.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/root-reviews/ivan-2023.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://arxiv.org/pdf/2010.09081)

<a id="q5022"></a>

## Q5022. A structural characterization of weak cop-win graphs

**Status:** Open · **Kind:** open problem (Question 4.19) · **Reviewed extraction** 2026-10-13-250

On a connected undirected loopless graph, the cop chooses a starting vertex, then the robber chooses one. They alternate moves, cop first, each moving to an adjacent vertex or staying put; capture occurs when they meet. Call the graph weak cop-win if the cop has a strategy guaranteeing capture or that the robber visits every vertex only finitely often. Characterize the graphs with this weak cop-win property in terms of their graph structure, allowing infinite graphs without a local-finiteness restriction.

**Source.** Maria Ivan. *Poset saturation and other combinatorial results*. University of Cambridge, 2023. [primary source](https://www.repository.cam.ac.uk/bitstreams/f145b6b3-ef5a-412e-b9c9-f8723aa14b33/download) · [record](https://www.repository.cam.ac.uk/handle/1810/352866) Location: Question 4.19, printed p. 99 / held PDF p. 111; definitions in the same chapter.

**Literature check.** Reviewed 2026-10-13: The source and published constructible-graphs paper retain the classification after their counterexamples. Later computability work studies strategies and multiple cops, rather than a full structural characterization. No general classification was located.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/root-reviews/ivan-2023.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://api.repository.cam.ac.uk/server/api/core/bitstreams/b221050e-872e-406e-b38e-b0c03a634b2f/content) · [2](https://journals.sagepub.com/doi/10.3233/COM-240016)

<a id="q5023"></a>

## Q5023. Does finite-set evacuation imply local constructibility?

**Status:** Open · **Kind:** open problem (Question 4.20) · **Reviewed extraction** 2026-10-13-250

On a connected undirected loopless graph, the cop chooses a starting vertex, then the robber chooses one. They alternate moves, cop first, each moving to an adjacent vertex or staying put; capture occurs when they meet. Call the graph weak cop-win if the cop has a strategy guaranteeing capture or that the robber visits every vertex only finitely often. Suppose the cop has one strategy ensuring that, against every robber play and for every finite vertex set V, the robber leaves V at some time or is captured, with later return allowed. Must the graph be locally constructible: for every finite vertex set V, does some finite U⊇V have a constructible induced graph G[U]? A finite graph is constructible if it admits an order v_1,…,v_s such that, for each i>1, some earlier v_j has N[v_i]⊆N[v_j] within the induced graph on v_1,…,v_i, where N[v] is the closed neighbourhood.

**Source.** Maria Ivan. *Poset saturation and other combinatorial results*. University of Cambridge, 2023. [primary source](https://www.repository.cam.ac.uk/bitstreams/f145b6b3-ef5a-412e-b9c9-f8723aa14b33/download) · [record](https://www.repository.cam.ac.uk/handle/1810/352866) Location: Question 4.20, printed p. 99 / held PDF p. 111; definitions in the same chapter.

**Literature check.** Reviewed 2026-10-13: The source and published paper ask whether this weaker evacuation property characterizes local constructibility. Their locally constructible non-weak-win counterexample does not answer the converse. No full converse proof or counterexample was located.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/root-reviews/ivan-2023.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://api.repository.cam.ac.uk/server/api/core/bitstreams/b221050e-872e-406e-b38e-b0c03a634b2f/content) · [2](https://journals.sagepub.com/doi/10.3233/COM-240016)

<a id="q5024"></a>

## Q5024. Arbitrarily delayed repeated returns in a weak cop-win graph

**Status:** Open · **Kind:** open problem (Question 4.21) · **Reviewed extraction** 2026-10-13-250

On a connected undirected loopless graph, the cop chooses a starting vertex, then the robber chooses one. They alternate moves, cop first, each moving to an adjacent vertex or staying put; capture occurs when they meet. Call the graph weak cop-win if the cop has a strategy guaranteeing capture or that the robber visits every vertex only finitely often. Does there exist a weak cop-win graph such that, for every cop starting vertex, the robber can choose a starting vertex v with this property: for every pair of positive integers m,n, the robber has a strategy against every cop play that avoids capture and either stays within some finite vertex set forever or visits v at a time t≥m and again at a time s≥t+n? The robber strategy may depend on m,n.

**Source.** Maria Ivan. *Poset saturation and other combinatorial results*. University of Cambridge, 2023. [primary source](https://www.repository.cam.ac.uk/bitstreams/f145b6b3-ef5a-412e-b9c9-f8723aa14b33/download) · [record](https://www.repository.cam.ac.uk/handle/1810/352866) Location: Question 4.21, printed p. 99 / held PDF p. 111; definitions in the same chapter.

**Literature check.** Reviewed 2026-10-13: The source and published paper retain this precise recurrence question. Their two-ended weak-win example gives one arbitrarily delayed return, which is a proper weaker result. No exact two-return construction or impossibility result was located.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/root-reviews/ivan-2023.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://api.repository.cam.ac.uk/server/api/core/bitstreams/b221050e-872e-406e-b38e-b0c03a634b2f/content) · [2](https://journals.sagepub.com/doi/10.3233/COM-240016)

<a id="q5025"></a>

## Q5025. The union-closed conjecture for horizontal and vertical three-tiles

**Status:** Open · **Kind:** open problem (Question 5.3) · **Reviewed extraction** 2026-10-13-250

For every n≥3 and every three-element R⊂Z/nZ, let F be the family of all unions of translates in (Z/nZ)² of R×{0} and {0}×R, including the empty union. Must some point belong to at least half the members of F? Equivalently, since F is invariant under all torus translations, is the average |S| over S∈F at least n²/2?

**Source.** Maria Ivan. *Poset saturation and other combinatorial results*. University of Cambridge, 2023. [primary source](https://www.repository.cam.ac.uk/bitstreams/f145b6b3-ef5a-412e-b9c9-f8723aa14b33/download) · [record](https://www.repository.cam.ac.uk/handle/1810/352866) Location: Question 5.3, printed p. 105 / held PDF p. 117; definitions in the same chapter.

**Literature check.** Reviewed 2026-10-13: Primary Question3 retains the torus target, alongside the R={0,1,2} case and one-dimensional theorem. October2026 improves universal abundance to0.3828852549667978, below1/2; September2026 formalizes the single cyclic-translate theorem. Neither settles both translate orbits for arbitrary R in the torus family.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/root-reviews/ivan-2023.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://research-information.bris.ac.uk/ws/portalfiles/portal/353082521/UCC_3_.pdf) · [2](https://arxiv.org/abs/2010.08795) · [3](https://arxiv.org/abs/2610.02295) · [4](https://arxiv.org/abs/2609.20876)

<a id="q5026"></a>

## Q5026. Deciding square-grid tilings by one polyomino

**Status:** Open · **Kind:** stated as open (Source discussion §2.1) · **Reviewed extraction** 2026-10-13-250

A polyomino is a finite nonempty subset P⊂Z² connected by unit horizontal/vertical steps. A permitted copy is z+RP, with z∈Z² and R a signed permutation matrix, so rotations and reflections of the square grid are allowed. A tiling is a partition of Z² into such copies. Is there an algorithm that, given P, always halts and decides whether a tiling exists?

**Source.** Vytautas Gruslys. *Tilings and other combinatorial results*. University of Cambridge, 2018. [primary source](https://www.repository.cam.ac.uk/bitstreams/dbf27713-bf8e-4c3c-be50-28310cfbcbd8/download) · [record](https://www.repository.cam.ac.uk/handle/1810/271311) Location: Source discussion §2.1, printed p. 9 / held PDF p. 21; definitions in the relevant chapter.

**Literature check.** Reviewed 2026-10-13: Recent primary undecidability results concern multiple planar tiles or a translational polycube in3D. The 2025 primary retains one/two-prototile isometry questions; no exact single-polyomino algorithm or undecidability result was located in the bounded scan.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/root-reviews/gruslys-2018.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://drops.dagstuhl.de/storage/00lipics/lipics-vol332-socg2025/html/LIPIcs.SoCG.2025.39/LIPIcs.SoCG.2025.39.html) · [2](https://arxiv.org/abs/2508.10067) · [3](https://arxiv.org/abs/2610.12392)

<a id="q5027"></a>

## Q5027. A single polyomino with no periodic tiling

**Status:** Open · **Kind:** stated as open (Source discussion §2.1) · **Reviewed extraction** 2026-10-13-250

A polyomino is a finite nonempty subset P⊂Z² connected by unit horizontal/vertical steps. A permitted copy is z+RP, with z∈Z² and R a signed permutation matrix, so rotations and reflections of the square grid are allowed. A tiling is a partition of Z² into such copies. Does some P admit a tiling but no tiling invariant under two linearly independent translation vectors in Z²?

**Source.** Vytautas Gruslys. *Tilings and other combinatorial results*. University of Cambridge, 2018. [primary source](https://www.repository.cam.ac.uk/bitstreams/dbf27713-bf8e-4c3c-be50-28310cfbcbd8/download) · [record](https://www.repository.cam.ac.uk/handle/1810/271311) Location: Source discussion §2.1, printed p. 9 / held PDF p. 21; definitions in the relevant chapter.

**Literature check.** Reviewed 2026-10-13: The recent arbitrary-polygon aperiodic monotile and3D translational tile do not provide a square-grid polyomino. Current single/polyomino primary searches found no matching construction or impossibility theorem; this remains a bounded status assessment.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/root-reviews/gruslys-2018.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://drops.dagstuhl.de/storage/00lipics/lipics-vol332-socg2025/html/LIPIcs.SoCG.2025.39/LIPIcs.SoCG.2025.39.html) · [2](https://arxiv.org/abs/2508.10067) · [3](https://arxiv.org/abs/2610.12392)

<a id="q5028"></a>

## Q5028. A tile-cardinality bound on the required dimension

**Status:** Open · **Kind:** conjecture (Conjecture 2.21) · **Reviewed extraction** 2026-10-13-250

For every positive integer t, does there exist an integer d=d(t)≥1 such that every finite nonempty T⊂Z with |T|≤t tiles Z^d, meaning Z^d can be partitioned into subsets Euclidean-isometric to T embedded in R^d? Copies may be translated, rotated and reflected; no scaling is allowed.

**Source.** Vytautas Gruslys. *Tilings and other combinatorial results*. University of Cambridge, 2018. [primary source](https://www.repository.cam.ac.uk/bitstreams/dbf27713-bf8e-4c3c-be50-28310cfbcbd8/download) · [record](https://www.repository.cam.ac.uk/handle/1810/271311) Location: Conjecture 2.21, printed p. 32 / held PDF p. 44; definitions in the relevant chapter.

**Literature check.** Reviewed 2026-10-13: The arbitrary-tiles theorem gives a dimension depending on the whole tile, not just its cardinality. The 2021 punctured-interval primary still states this cardinality conjecture. No full cardinality-only bound was located.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/root-reviews/gruslys-2018.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://arxiv.org/pdf/1505.03697) · [2](https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112%2Fmtk.12085)

<a id="q5029"></a>

## Q5029. Bounded-remainder packing by an arbitrary finite poset

**Status:** Open · **Kind:** open problem (Question 3.17) · **Reviewed extraction** 2026-10-13-250

For every finite nonempty poset P, is there a constant c(P) such that for every n≥1 the Boolean lattice (2^[n],⊆) contains pairwise disjoint induced copies of P covering at least 2^n−c(P) elements? An induced copy is an injective map φ:P→2^[n] satisfying x≤\_P y if and only if φ(x)⊆φ(y).

**Source.** Vytautas Gruslys. *Tilings and other combinatorial results*. University of Cambridge, 2018. [primary source](https://www.repository.cam.ac.uk/bitstreams/dbf27713-bf8e-4c3c-be50-28310cfbcbd8/download) · [record](https://www.repository.cam.ac.uk/handle/1810/271311) Location: Question 3.17, printed p. 52 / held PDF p. 64; definitions in the relevant chapter.

**Literature check.** Reviewed 2026-10-13: Tomon’s 2018 primary proves the target for posets having a minimum and maximum, and retains arbitrary P as Conjecture4. Later bounded queries found no unrestricted finite-poset result.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/root-reviews/gruslys-2018.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v25i1p38/pdf/)

<a id="q5030"></a>

## Q5030. Forcing monochromatic lines from many long lines

**Status:** Open · **Kind:** open problem (Question 5.5) · **Reviewed extraction** 2026-10-13-250

For a finite point set S⊂R², a line means S∩ℓ for an affine line ℓ containing at least two points of S; all points of S on ℓ are included. Such a line is monochromatic if all its points have one colour. For every fixed k≥3 and l≥4, does some m=m(k,l) exist such that, whenever S determines at least m distinct lines each containing exactly l points and no line containing more than l points, every k-colouring of S has a monochromatic line?

**Source.** Vytautas Gruslys. *Tilings and other combinatorial results*. University of Cambridge, 2018. [primary source](https://www.repository.cam.ac.uk/bitstreams/dbf27713-bf8e-4c3c-be50-28310cfbcbd8/download) · [record](https://www.repository.cam.ac.uk/handle/1810/271311) Location: Question 5.5, printed p. 66 / held PDF p. 78; definitions in the relevant chapter.

**Literature check.** Reviewed 2026-10-13: The published primary retains this strengthened question after its cubic-curve counterexample to the original geometric Hales–Jewett claim. The original no4-point-line counterexample and two-colour results do not answer it. No exact closure was located.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/root-reviews/gruslys-2018.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://jocg.org/index.php/jocg/article/download/2933/2627/7266)

<a id="q5031"></a>

## Q5031. Three colours with one four-point line

**Status:** Open · **Kind:** open problem (Question 5.6) · **Reviewed extraction** 2026-10-13-250

For a finite point set S⊂R², a line means S∩ℓ for an affine line ℓ containing at least two points of S; all points of S on ℓ are included. Such a line is monochromatic if all its points have one colour. Does there exist N such that every finite S⊂R² with |S|≥N, at least one line containing exactly four points, and no line containing five or more points has a monochromatic line under every three-colouring?

**Source.** Vytautas Gruslys. *Tilings and other combinatorial results*. University of Cambridge, 2018. [primary source](https://www.repository.cam.ac.uk/bitstreams/dbf27713-bf8e-4c3c-be50-28310cfbcbd8/download) · [record](https://www.repository.cam.ac.uk/handle/1810/271311) Location: Question 5.6, printed p. 67 / held PDF p. 79; definitions in the relevant chapter.

**Literature check.** Reviewed 2026-10-13: The primary concluding question retains precisely the one4-point-line three-colour version. No later exact result was located in the bounded scan.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/root-reviews/gruslys-2018.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://jocg.org/index.php/jocg/article/download/2933/2627/7266)

<a id="q5032"></a>

## Q5032. Fixed intersections just above twice the subset size

**Status:** Open · **Kind:** conjecture (Conjecture 7.11) · **Reviewed extraction** 2026-10-13-250

Write [r]^(p) for all p-element subsets of {1,…,r}. A function f fixes an intersection if some distinct A,B in its domain satisfy |f(A)∩f(B)|=|A∩B|. For all positive integers n,p with n>2p, must every nonconstant f:[n]^(p)→[n]^(p) fix an intersection?

**Source.** Vytautas Gruslys. *Tilings and other combinatorial results*. University of Cambridge, 2018. [primary source](https://www.repository.cam.ac.uk/bitstreams/dbf27713-bf8e-4c3c-be50-28310cfbcbd8/download) · [record](https://www.repository.cam.ac.uk/handle/1810/271311) Location: Conjecture 7.11, printed p. 123 / held PDF p. 135; definitions in the relevant chapter.

**Literature check.** Reviewed 2026-10-13: The source and primary prove the property when n is sufficiently large depending on p, but retain n>2p. No full sharp-threshold answer was located.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/root-reviews/gruslys-2018.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://arxiv.org/pdf/1311.7082)

<a id="q5033"></a>

## Q5033. Fixed-intersection thresholds for an unbounded codomain

**Status:** Open · **Kind:** open problem (Question 7.30) · **Reviewed extraction** 2026-10-13-250

Write [r]^(p) for all p-element subsets of {1,…,r}. A function f fixes an intersection if some distinct A,B in its domain satisfy |f(A)∩f(B)|=|A∩B|. Determine all integer pairs r≥p≥2 for which every nonconstant f:[r]^(p)→N^(p) fixes an intersection, where N^(p) is the family of p-element subsets of the positive integers.

**Source.** Vytautas Gruslys. *Tilings and other combinatorial results*. University of Cambridge, 2018. [primary source](https://www.repository.cam.ac.uk/bitstreams/dbf27713-bf8e-4c3c-be50-28310cfbcbd8/download) · [record](https://www.repository.cam.ac.uk/handle/1810/271311) Location: Question 7.30, printed p. 139 / held PDF p. 151; definitions in the relevant chapter.

**Literature check.** Reviewed 2026-10-13: The primary retains the pair classification; sufficiently-large-r positive results and the source(11,5) counterexample are proper partial cases. No complete classification was located.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/root-reviews/gruslys-2018.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://arxiv.org/pdf/1311.7082)

<a id="q5034"></a>

## Q5034. Fixed intersections under permutations of p-subsets

**Status:** Open · **Kind:** open problem (Question 7.31) · **Reviewed extraction** 2026-10-13-250

Write [r]^(p) for all p-element subsets of {1,…,r}. A function f fixes an intersection if some distinct A,B in its domain satisfy |f(A)∩f(B)|=|A∩B|. Determine all integer pairs r≥p≥2 for which every bijection f:[r]^(p)→[r]^(p) fixes an intersection.

**Source.** Vytautas Gruslys. *Tilings and other combinatorial results*. University of Cambridge, 2018. [primary source](https://www.repository.cam.ac.uk/bitstreams/dbf27713-bf8e-4c3c-be50-28310cfbcbd8/download) · [record](https://www.repository.cam.ac.uk/handle/1810/271311) Location: Question 7.31, printed p. 139 / held PDF p. 151; definitions in the relevant chapter.

**Literature check.** Reviewed 2026-10-13: The source and primary retain this classification, with a simple sufficiently-large-r=Ω(p²) positive bound. No complete pair classification was located.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/root-reviews/gruslys-2018.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://arxiv.org/pdf/1311.7082)

<a id="q5035"></a>

## Q5035. Exact minima and extremizers for edges lying in F-copies

**Status:** Open · **Kind:** open problem (Question 6.57) · **Reviewed extraction** 2026-10-13-250

For every fixed finite simple graph F with an edge, every n≥1 and every integer 0≤e≤binom(n,2), determine the minimum, over n-vertex finite simple graphs G with exactly e edges, of the number of edges of G belonging to at least one subgraph isomorphic to F; characterize all graphs attaining the minimum. Count each such edge once, irrespective of the number of F-copies containing it, and do not require F-copies to be induced.

**Source.** Vytautas Gruslys. *Tilings and other combinatorial results*. University of Cambridge, 2018. [primary source](https://www.repository.cam.ac.uk/bitstreams/dbf27713-bf8e-4c3c-be50-28310cfbcbd8/download) · [record](https://www.repository.cam.ac.uk/handle/1810/271311) Location: Question 6.57, printed p. 117 / held PDF p. 129; definitions in the relevant chapter.

**Literature check.** Reviewed 2026-10-13: The primary final Problem57 retains this full classification. Exact triangle results for sufficiently large n and dense asymptotic3-chromatic results are known partial cases. No unrestricted exact F/n/e classification was located.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/root-reviews/gruslys-2018.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://discovery.ucl.ac.uk/id/eprint/10107276/1/triangle-corrected.pdf)

<a id="q5042"></a>

## Q5042. Equation-free subset guarantee and circle extremal density

**Status:** Open · **Kind:** conjecture (Conjecture 1.7.1) · **Reviewed extraction** 2026-10-13-250

Let E be an equation a_1x_1+⋯+a_rx_r=0 with integer coefficients, at least one positive and at least one negative. A subset B of an abelian group is E-free if no tuple (x_1,…,x_r)∈B^r satisfies E; repetitions are allowed. Put δ\_E=inf_{∅≠A⊂N finite} max_{B⊂A, B E-free}|B|/|A|, where N={1,2,…}. For the circle group T=R/Z with normalized Haar measure μ put d_E(T)=sup{μ(S): S⊂T is measurable and E-free}, where E is interpreted in T. Is δ\_E=d_E(T) for every such E?

**Source.** Sean Eberhard. *Some combinatorial problems in group theory*. University of Oxford, 2016. [primary source](https://ora.ox.ac.uk/objects/uuid:b92af6aa-df2a-4634-882d-236d8f828857/files/m319cd33bf409a03bc95a499695769acf) · [record](https://ora.ox.ac.uk/objects/uuid:b92af6aa-df2a-4634-882d-236d8f828857) Location: Conjecture 1.7.1, printed p. 24; physical PDF p. 29.

**Literature check.** Reviewed 2026-10-13: The source proves special sum-free and k-sum-free cases. The current primary author list, original Følner paper and prime-modulus convergence paper supply partial results with different or narrower quantifiers. No full arbitrary-equation δ\_E=d_E(T) resolution was verified in the dated bounded scan.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/eberhard-2016.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://arxiv.org/pdf/1401.6390) · [2](https://arxiv.org/pdf/1212.3681) · [3](https://arxiv.org/a/eberhard_s_1.html) · [4](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf) · [5](https://arxiv.org/pdf/2604.28116) · [6](https://arxiv.org/abs/2201.09402) · [7](https://link.springer.com/article/10.1007/s00208-023-02567-0) · [8](https://arxiv.org/abs/2003.01798) · [9](https://arxiv.org/abs/2205.15191)

<a id="q5045"></a>

## Q5045. Leading constant for the multistage triangle game with stop

**Status:** Open · **Kind:** open problem (Problem 7.3.2) · **Reviewed extraction** 2026-10-13-250

Start with the board E(K_n) and winning sets the three-edge sets of triangles. In each stage Maker moves first, claiming one free edge per turn, and Breaker then claims at most one free edge. Stop the stage immediately when Maker has claimed a whole triangle, before the next Breaker turn. Remove only the edges claimed by Breaker in that stage; retain all Maker edges and all still free edges as the next board, and reset the ownership of retained edges for the next stage. Continue with triangles fully contained in the current board. If Maker cannot complete a triangle in a stage, the game terminates. Let τ\_stop(n) be the maximum number of successful stages Maker can guarantee against every Breaker strategy. Determine whether τ\_stop(n)/n² has a limit and, if it does, its value.

**Source.** Amedeo Sgueglia. *On some problems in extremal hypergraph theory*. London School of Economics and Political Science, 2022. [primary source](https://researchonline.lse.ac.uk/id/eprint/135365/1/Sgueglia_On-some-problems-extremal-hypergraph-theory.pdf) · [record](https://researchonline.lse.ac.uk/id/eprint/135365/) Location: Problem 7.3.2, explicit H=K₃, b=1 clause; printed p. 137 / held PDF p. 145.

**Literature check.** Reviewed 2026-10-13: The 2023 revised primary retains Problem 8.4 and explicitly singles out H=K₃, b=1. Its Θ(n²) observation gives the scale, not the leading constant. No exact constant or refutation was located in the dated bounded primary scan.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/root-reviews/sgueglia-2022.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://arxiv.org/html/2202.04344v2) · [2](https://www.sciencedirect.com/science/article/pii/S0012365X23001644)

<a id="q5049"></a>

## Q5049. Cut-involution edge transitivity implies a graph norm

**Status:** Open · **Kind:** conjecture (Conjecture 6.42) · **Reviewed extraction** 2026-10-13-250

Let H be a finite connected simple bipartite graph with at least one edge. For a bounded real symmetric measurable function f on [0,1]², put t_H(|f|)=∫\_[0,1]^{V(H)} ∏\_{uv∈E(H)}|f(x_u,x_v)| ∏\_{v∈V(H)}dx_v. Call H weakly norming if f↦t_H(|f|)^(1/|E(H)|) is a norm on this vector space modulo equality almost everywhere. A cut involution is a graph automorphism σ with σ²=id whose fixed vertices F separate H and for which V(H)∖F splits into nonempty sets L,R with no edges between them and σ(L)=R. Let W_H be the subgroup of Aut(H) generated by all cut involutions. If W_H acts transitively on E(H), must H be weakly norming?

**Source.** Joonkyung Lee. *Sidorenko’s conjecture, graph norms, and pseudorandomness*. University of Oxford, 2017. [primary source](https://ora.ox.ac.uk/objects/uuid:5666a58e-77ae-4709-a41e-587cf176840a/files/mae4adeee4071a7ed1861b93e08a87e9d) · [record](https://ora.ox.ac.uk/objects/uuid:5666a58e-77ae-4709-a41e-587cf176840a) Location: Conjecture 6.42, printed p. 117 / held PDF p. 125; cut-involution domain and definition at printed p. 83 / PDF p. 91.

**Literature check.** Reviewed 2026-10-13: Coregliano 2408.14257 retains the stronger cut-percolation conjecture and characterizes percolation by absence of nonmonochromatic fold-stable colorings. That extra condition is not implied by its theorem from edge transitivity alone. Sidorenko’s ordinary automorphism-edge-transitivity necessity is also weaker than this source cut-group sufficiency target. No exact sufficiency proof or counterexample was verified in the dated bounded primary scan.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/root-reviews/joonkyung-lee-2017.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://arxiv.org/html/2408.14257v1) · [2](https://www.its.caltech.edu/~dconlon/norming.pdf) · [3](https://arxiv.org/abs/1611.05784)
