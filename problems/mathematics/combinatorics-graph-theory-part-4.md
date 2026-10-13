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

