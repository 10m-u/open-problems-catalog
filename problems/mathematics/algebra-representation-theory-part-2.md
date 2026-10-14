# Algebra & Representation Theory (part 2 of 3)

[Subject overview](algebra-representation-theory.md) · Parts: [1](algebra-representation-theory-part-1.md) · [2](algebra-representation-theory-part-2.md) · [3](algebra-representation-theory-part-3.md)

<a id="q2911"></a>

## Q2911. Normal Sylow subgroups from degree-square sums

**Status:** Open · **Kind:** open problem · **Collection** 30

Does G have a normal Sylow p-subgroup if and only if S_p(G)\_(p′)=|G|\_(p′)?

**Context.** Origin for question 2911: Navarro’s 2004 proposed character-degree test, explicitly recalled here. Setup for question 2911: For a finite group G and prime p, put S_p(G)=Σ\_(χ∈Irr(G),p∤χ(1))χ(1)². For a positive integer n, n_(p′)=n/p^(v_p(n)).

**Source.** Nguyen N. Hung, J. Miquel Martínez, Gabriel Navarro. *Sum of the squares of the p′-character degrees*. 2026. [primary source](https://msp.org/pjm/2026/342-2/pjm-v342-n2-p07-p.pdf) Location: Introduction, p. 353, final displayed condition.

**Literature check.** Status for question 2911, checked 7 October 2026: The 2026 paper leaves the test open; no later proof or counterexample located.

**Further links.** [1](https://arxiv.org/abs/2505.21267) · [2](https://sites.google.com/view/nguyen-ngoc-hung/publications)


<a id="q2912"></a>

## Q2912. Representation dimension of an idempotent corner

**Status:** Open · **Kind:** open problem · **Collection** 30

For every Artin algebra A and idempotent e∈A, must rep.dim(eAe)≤rep.dim(A)?

**Context.** Origin for question 2912: Xi’s idempotent-corner conjecture. Setup for question 2912: For an Artin algebra A, rep.dim(A)=inf_M gl.dim End_A(M), where M ranges over finitely generated generator-cogenerators of A-mod.

**Source.** Changchang Xi. *The relative Auslander–Reiten theory of modules (undated revised preprint)*. [primary source](https://www.wemath.cn/~ccxi/Papers/Articles/rart.pdf) Location: Closing conjecture after Theorem 7.2, author p. 25.

**Literature check.** Status for question 2912, checked 7 October 2026: The source states the conjecture; later searches found no general resolution.

**Further links.** [1](https://www.wemath.cn/~ccxi/EngOpenProblem.php) · [2](https://www.wemath.cn/~ccxi/Papers/EngshowArt.php?Artmode=3)


<a id="q2913"></a>

## Q2913. Rationality level under Lusztig induction

**Status:** Open · **Kind:** conjecture (Conjecture C) · **Collection** 30

For every prime p with p∤χ(1), does max{lev_p(ψ),lev_p(χ)}≥2 imply lev_p(χ)=lev_p(ψ)?

**Context.** Origin for question 2913: Hung’s August 2026 extension from maximal tori to arbitrary Levi subgroups. Setup for question 2913: For a virtual character ξ, let c(ξ)=min{m:Q(ξ)⊆Q(ζ\_m)} and lev_p(ξ)=v_p(c(ξ)). Let G be a connected reductive algebraic group over an algebraic closure of F_r, F a Steinberg endomorphism, L an F-stable Levi subgroup of a parabolic P≤G, and ψ∈Irr(L^F). Write χ=R^G_(L≤P)(ψ) for Lusztig induction.

**Source.** Nguyen N. Hung. *On the p-rationality of Deligne–Lusztig characters*. 2026. [primary source](https://arxiv.org/abs/2608.17871) Location: Conjecture C, pp. 3–4.

**Literature check.** Status for question 2913, checked 7 October 2026: The defining-characteristic and certain solvable-Levi cases are proved; no general resolution located.

**Further links.** [1](https://arxiv.org/html/2608.17871v1) · [2](https://sites.google.com/view/nguyen-ngoc-hung/publications)


<a id="q2914"></a>

## Q2914. Recovering derived equivalence from mirrors

**Status:** Open · **Kind:** open problem · **Collection** 30

If (R(A,e),e) and (R(B,f),f) are derived equivalent as pairs, must A and B be derived equivalent?

**Context.** Origin for questions 2914, 2915: Authors’ concluding questions. Setup for questions 2914, 2915: A,B are finite-dimensional gendo-symmetric k-algebras: each is End_Λ(Λ⊕M) for symmetric Λ. Choose idempotents e,f with Ae,Bf faithful projective-injective. Put X=Ae⊗\_(eAe)eA and R(A,e)=A⊕X, with (a,x)(b,y)=(ab,ay+xb+xy), where (u⊗v)(u′⊗v′)=uvu′⊗v′; define R(B,f) similarly. Pairs (C,c),(D,d) are derived equivalent if a triangle equivalence D(C-Mod)→D(D-Mod) restricts to K^b(add Cc)→K^b(add Dd). Stable equivalence of Morita type means finite-dimensional bimodules, projective on both sides, whose tensor composites are the regular bimodules plus projective bimodules.

**Source.** Hongxing Chen, Changchang Xi. *Derived equivalences for mirror-reflective algebras*. 2023. [primary source](https://www.wemath.cn/~ccxi/Papers/Articles/defmra.pdf) Location: Concluding question (1), author p. 15; Definition 2.3.

**Literature check.** Status for questions 2914, 2915, checked 7 October 2026: The concluding questions remain unanswered in later searches.

**Further links.** [1](https://arxiv.org/abs/2309.13964) · [2](https://www.wemath.cn/~ccxi/EngOpenProblem.php) · [3](https://pnp.mathematik.uni-stuttgart.de/iaz/iaz1/Oberseminar/abstracts/yipingchen26082025.html)


<a id="q2915"></a>

## Q2915. Stable Morita equivalence of mirrors

**Status:** Open · **Kind:** open problem · **Collection** 30

If A and B are stably equivalent of Morita type, must R(A,e) and R(B,f) be stably equivalent of Morita type?

**Context.** Origin for questions 2914, 2915: Authors’ concluding questions. Setup for questions 2914, 2915: A,B are finite-dimensional gendo-symmetric k-algebras: each is End_Λ(Λ⊕M) for symmetric Λ. Choose idempotents e,f with Ae,Bf faithful projective-injective. Put X=Ae⊗\_(eAe)eA and R(A,e)=A⊕X, with (a,x)(b,y)=(ab,ay+xb+xy), where (u⊗v)(u′⊗v′)=uvu′⊗v′; define R(B,f) similarly. Pairs (C,c),(D,d) are derived equivalent if a triangle equivalence D(C-Mod)→D(D-Mod) restricts to K^b(add Cc)→K^b(add Dd). Stable equivalence of Morita type means finite-dimensional bimodules, projective on both sides, whose tensor composites are the regular bimodules plus projective bimodules.

**Source.** Hongxing Chen, Changchang Xi. *Derived equivalences for mirror-reflective algebras*. 2023. [primary source](https://www.wemath.cn/~ccxi/Papers/Articles/defmra.pdf) Location: Concluding question (2), author p. 15.

**Literature check.** Status for questions 2914, 2915, checked 7 October 2026: The concluding questions remain unanswered in later searches.

**Further links.** [1](https://arxiv.org/abs/2309.13964) · [2](https://www.wemath.cn/~ccxi/EngOpenProblem.php) · [3](https://pnp.mathematik.uni-stuttgart.de/iaz/iaz1/Oberseminar/abstracts/yipingchen26082025.html)


<a id="q2916"></a>

## Q2916. Hochschild cohomology algebras of matrix centralizers

**Status:** Open · **Kind:** open problem · **Collection** 30

Determine the graded k-algebra HH\*(C(c)) for arbitrary fields k, integers n≥1 and matrices c∈M_n(k).

**Context.** Origin for question 2916: Xi’s February 2026 problem-page question, not a dissertation-origin problem. Setup for question 2916: For a field k and c∈M_n(k), set C(c)={X∈M_n(k):Xc=cX}. Write HH\*(C(c))=Ext\*\_(C(c)⊗\_k C(c)^op)(C(c),C(c)), with its cup product.

**Source.** Changchang Xi. *Open problems*. 2026. [primary source](https://www.wemath.cn/~ccxi/EngOpenProblem.php) Location: February 2026 entry, third bullet.

**Literature check.** Status for question 2916, checked 7 October 2026: August–September 2026 work computes the center and HH₀, not the full cohomology algebra; no complete answer located.

**Further links.** [1](https://arxiv.org/abs/2608.15460) · [2](https://arxiv.org/abs/2608.21922)


<a id="q2917"></a>

## Q2917. Stable equivalences preserve the number of nonprojective simples

**Status:** Open · **Kind:** open problem · **Collection** 30

Must stably equivalent Artin algebras have the same number of isomorphism classes of nonprojective simple modules?

**Context.** Origin for question 2917: Auslander–Reiten’s conjecture on stable equivalences, restated by Xi–Zhang. Setup for question 2917: A,B are Artin algebras over a commutative Artin ring k. The stable category of A has finitely generated left A-modules and morphisms modulo maps factoring through projectives. Stable equivalence means a k-linear equivalence of these categories.

**Source.** Changchang Xi, Jinbi Zhang. *New invariants of stable equivalences and Auslander–Reiten conjecture*. 2026. [primary source](https://www.wemath.cn/~ccxi/Papers/Articles/xz3online.pdf) Location: Introduction (ARC), p. 2; §2.1.

**Literature check.** Status for question 2917, checked 7 October 2026: The 2026 article proves special classes only; later searches found no general answer.

**Further links.** [1](https://doi.org/10.1007/s00208-026-03422-8) · [2](https://arxiv.org/abs/2207.10848) · [3](https://arxiv.org/abs/2511.19051)


<a id="q2918"></a>

## Q2918. Signed Cartan determinants under stable Morita equivalence

**Status:** Open · **Kind:** open problem (Question 3) · **Collection** 30

If A and B are stably equivalent of Morita type, must det(C_A)=det(C_B)?

**Context.** Origin for question 2918: Xi’s Question 3. Setup for question 2918: A,B are Artin algebras over a commutative Artin ring k. C_A has entries [P_j:S_i], the composition multiplicities in projective covers P_j of the simple modules S_j; define C_B similarly. Stable Morita equivalence uses finitely generated bimodules projective on both sides whose tensor products are the regular bimodules plus projective bimodules.

**Source.** Changchang Xi. *Stable equivalences of adjoint type*. 2008. [primary source](https://www.wemath.cn/~ccxi/Papers/Articles/staadj_FM.pdf) Location: Question 3, p. 95; standing conventions p. 82.

**Literature check.** Status for question 2918, checked 7 October 2026: Only equality of absolute determinants is proved in Proposition 5.1; no later general sign-preservation result located.

**Further links.** [1](https://doi.org/10.1515/FORUM.2008.004) · [2](https://www.wemath.cn/~ccxi/EngOpenProblem.php) · [3](https://arxiv.org/abs/2603.20643)


<a id="q2929"></a>

## Q2929. Profinite invariance of rational solvable filtrations

**Status:** Open · **Kind:** open problem (Question 10.3) · **Collection** 30

If finitely generated residually finite Γ,Λ have isomorphic profinite completions and Γ is RFRS, must Λ be RFRS?

**Context.** Doctoral context for question 2929: Ismael Morales López. L2-invariants in abstract and profinite group theory. DPhil, University of Oxford, 2025; supervisors Dawid Kielak and Richard Wade. Origin for question 2929: Morales’s question on profinite invariance of RFRS. Setup for question 2929: Write Ĝ for the inverse limit of G’s finite quotients. A group is RFRS if G=G₀≥G₁≥⋯ are finite-index normal subgroups of G, ⋂Gᵢ=1, and ker(Gᵢ→H₁(Gᵢ;Q))⊂Gᵢ₊₁.

**Source.** Ismael Morales. *On the profinite rigidity of free and surface groups*. 2024. [primary source](https://pmc.ncbi.nlm.nih.gov/articles/PMC11424743/) Location: Question 10.3, preprint p. 33.

**Literature check.** Status for question 2929, checked 7 October 2026: The 2024 article explicitly poses this; later rigidity results impose extra hypotheses. No general resolution found.

**Further links.** [1](https://arxiv.org/abs/2211.12390) · [2](https://sites.google.com/view/ismaelmorales/home) · [3](https://arxiv.org/abs/2312.12293) · [4](https://arxiv.org/abs/2608.07350) · [5](https://arxiv.org/abs/2603.16763) · [6](https://ora.ox.ac.uk/objects/uuid%3Acaa81b48-6ada-4b87-8703-51bb482a4aae)


<a id="q2933"></a>

## Q2933. An infinite group of transitivity degree four

**Status:** Open · **Kind:** open problem · **Collection** 30

Does an infinite group G with td(G)=4 exist?

**Context.** Origin for question 2933: Previously open group-theoretic question explicitly recalled by Rybak. Setup for question 2933: The transitivity degree td(G) is the supremum of integers k for which G admits a faithful k-transitive permutation action. k-transitive means transitive on ordered k-tuples of distinct points.

**Source.** Ekaterina Rybak. *Boundary dynamics, triple transitivity, and mixed identities in weakly hyperbolic groups*. 2026. [primary source](https://arxiv.org/pdf/2605.14159v3) Location: §1.3, paragraph before Corollary J, p. 7.

**Literature check.** Status for question 2933, checked 7 October 2026: The current paper excludes certain weakly hyperbolic groups, not all infinite groups; no general resolution located.

**Further links.** [1](https://sites.google.com/view/ekaterinarybak/home) · [2](https://arxiv.org/abs/2605.14159)


<a id="q3001"></a>

## Q3001. Unique shortest-path weights

**Status:** Open · **Kind:** open problem · **Collection** 31

For every u,v∈W, do all shortest directed paths from u to v have equal weight?

**Context.** Origin for questions 3001, 3002: General affine extension of Postnikov’s finite-type theorem; the diamond exception is Dean’s conjecture. Setup for questions 3001, 3002: Let W be an affine Weyl group, Φ⁺ its positive real roots, ℓ its Coxeter length, and ρ the sum of fundamental weights. QBG(W) has vertices W and edges w→ws_α of weight 0 when ℓ(ws_α)=ℓ(w)+1, or weight α∨ when ℓ(ws_α)=ℓ(w)+1−⟨α∨,2ρ⟩. Path weight is the sum of edge weights.

**Source.** Lewis Dean. *Affine quantum Bruhat graphs and double affine Demazure products*. University of Glasgow, 2026. Advisor(s): Dinakar Muthiah and Misha Feigin. [primary source](https://theses.gla.ac.uk/86179/2/2026DeanPhD.pdf) Location: §1.1.3, p. 4; §2.5.1, pp. 27–29.

**Literature check.** Status for questions 3001, 3002, checked 8 October 2026: The 2026 thesis retains both targets; the final 2025 paper proves shortest-weight uniqueness only in affine A₁.

**Further links.** [1](https://theses.gla.ac.uk/86179/) · [2](https://doi.org/10.1007/s00209-025-03832-5) · [3](https://arxiv.org/abs/2411.14170)


<a id="q3002"></a>

## Q3002. Exact affine diamond exception

**Status:** Open · **Kind:** conjecture (Conjecture 2.5.7) · **Collection** 31

For every two-edge path u→us_α→v with u≠v, is it the unique two-edge path from u to v exactly when its weight is nonzero and purely imaginary, with exactly two such paths otherwise?

**Context.** Origin for questions 3001, 3002: General affine extension of Postnikov’s finite-type theorem; the diamond exception is Dean’s conjecture. Setup for questions 3001, 3002: Let W be an affine Weyl group, Φ⁺ its positive real roots, ℓ its Coxeter length, and ρ the sum of fundamental weights. QBG(W) has vertices W and edges w→ws_α of weight 0 when ℓ(ws_α)=ℓ(w)+1, or weight α∨ when ℓ(ws_α)=ℓ(w)+1−⟨α∨,2ρ⟩. Path weight is the sum of edge weights.

**Source.** Lewis Dean. *Affine quantum Bruhat graphs and double affine Demazure products*. University of Glasgow, 2026. Advisor(s): Dinakar Muthiah and Misha Feigin. [primary source](https://theses.gla.ac.uk/86179/2/2026DeanPhD.pdf) Location: Conjecture 2.5.7, p. 29; Proposition 2.5.6.

**Literature check.** Status for questions 3001, 3002, checked 8 October 2026: The 2026 thesis retains both targets; the final 2025 paper proves shortest-weight uniqueness only in affine A₁.

**Further links.** [1](https://theses.gla.ac.uk/86179/) · [2](https://doi.org/10.1007/s00209-025-03832-5) · [3](https://arxiv.org/abs/2411.14170)


<a id="q3003"></a>

## Q3003. Finitely generated finite-generation ideal

**Status:** Open · **Kind:** open problem (Question 6.3.4) · **Collection** 31

Does there exist a non-finitely generated monomial K-subalgebra R⊂K[x₁,…,x_n], for some finite n, whose ideal f_R is finitely generated as an R-ideal?

**Context.** Origin for questions 3003, 3004: Hart’s concluding questions, motivated by computations of non-finitely generated invariant rings. Setup for questions 3003, 3004: Let K be an algebraically closed field of characteristic zero. For a K-domain R, let f_R={0}∪{f∈R\\{0}:R[1/f] is finitely generated over K}; this is its finite-generation ideal. A monomial subalgebra is generated by monomials.

**Source.** Simon Hart. *Hilbert’s fourteenth problem and finite generation ideals*. University of York, 2025. Advisor(s): Emilie Dufresne and Michael Bate. [primary source](https://etheses.whiterose.ac.uk/id/eprint/36388/1/Thesis__Final_SH_09_24.pdf) Location: Question 6.3.4, p. 127.

**Literature check.** Status for questions 3003, 3004, checked 8 October 2026: Thesis full text retains these questions; its counterexample concerns general monomial algebras, not invariant rings.

**Further links.** [1](https://etheses.whiterose.ac.uk/id/eprint/36388/) · [2](https://pure.york.ac.uk/portal/en/publications/hilberts-fourteenth-problem-and-finite-generation-ideals) · [3](https://doi.org/10.1080/00927872.2024.2404704)


<a id="q3004"></a>

## Q3004. Invariant finite-generation ideal beyond finite radicals

**Status:** Open · **Kind:** open problem · **Collection** 31

Does an algebraic group acting by morphisms on an irreducible affine K-variety have an invariant ring R whose f_R is not the radical of any finitely generated R-ideal?

**Context.** Origin for questions 3003, 3004: Hart’s concluding questions, motivated by computations of non-finitely generated invariant rings. Setup for questions 3003, 3004: Let K be an algebraically closed field of characteristic zero. For a K-domain R, let f_R={0}∪{f∈R\\{0}:R[1/f] is finitely generated over K}; this is its finite-generation ideal. A monomial subalgebra is generated by monomials.

**Source.** Simon Hart. *Hilbert’s fourteenth problem and finite generation ideals*. University of York, 2025. Advisor(s): Emilie Dufresne and Michael Bate. [primary source](https://etheses.whiterose.ac.uk/id/eprint/36388/1/Thesis__Final_SH_09_24.pdf) Location: §6.3 final paragraph, p. 127; Chapter 7.

**Literature check.** Status for questions 3003, 3004, checked 8 October 2026: Thesis full text retains these questions; its counterexample concerns general monomial algebras, not invariant rings.

**Further links.** [1](https://etheses.whiterose.ac.uk/id/eprint/36388/) · [2](https://pure.york.ac.uk/portal/en/publications/hilberts-fourteenth-problem-and-finite-generation-ideals) · [3](https://doi.org/10.1080/00927872.2024.2404704)


<a id="q3005"></a>

## Q3005. Infinitely many power-cograph projective groups

**Status:** Open · **Kind:** open problem · **Collection** 31

Are there infinitely many prime powers q≥4 for which PSL₂(q) has a power graph that is a cograph?

**Context.** Origin for questions 3005, 3006: Older infinitude problems of Manna–Cameron–Mehatari, retained by Kaja; not thesis-origin questions. Setup for questions 3005, 3006: For a group G, its undirected power graph joins distinct g,h if either is a positive integer power of the other. A cograph has no induced path on four vertices.

**Source.** Eda Kaja. *Classifications at the intersection of group and graph theory*. TU Darmstadt, 2025. Advisor(s): Pascal Schweitzer. [primary source](https://d-nb.info/1361444797/34) Location: §2.6, p. 47.

**Literature check.** Status for questions 3005, 3006, checked 8 October 2026: The structural classification does not settle infinitude; no later resolution located.

**Further links.** [1](https://tuprints.ulb.tu-darmstadt.de/entities/publication/a9ce0a3f-7d38-4fce-a549-b27682c06fd8) · [2](https://arxiv.org/abs/2203.02362) · [3](https://doi.org/10.37236/9961) · [4](https://arxiv.org/abs/2010.05198) · [5](https://arxiv.org/abs/2106.14217) · [6](https://doi.org/10.1016/j.jalgebra.2021.09.034)


<a id="q3006"></a>

## Q3006. Infinitely many power-cograph Suzuki groups

**Status:** Open · **Kind:** open problem · **Collection** 31

Are there infinitely many integers e≥2 for which Sz(2^(2e+1)) has a power graph that is a cograph?

**Context.** Origin for questions 3005, 3006: Older infinitude problems of Manna–Cameron–Mehatari, retained by Kaja; not thesis-origin questions. Setup for questions 3005, 3006: For a group G, its undirected power graph joins distinct g,h if either is a positive integer power of the other. A cograph has no induced path on four vertices.

**Source.** Eda Kaja. *Classifications at the intersection of group and graph theory*. TU Darmstadt, 2025. Advisor(s): Pascal Schweitzer. [primary source](https://d-nb.info/1361444797/34) Location: After Theorem 2.2.4, pp. 18–19.

**Literature check.** Status for questions 3005, 3006, checked 8 October 2026: The structural classification does not settle infinitude; no later resolution located.

**Further links.** [1](https://tuprints.ulb.tu-darmstadt.de/entities/publication/a9ce0a3f-7d38-4fce-a549-b27682c06fd8) · [2](https://arxiv.org/abs/2203.02362) · [3](https://doi.org/10.37236/9961) · [4](https://arxiv.org/abs/2010.05198) · [5](https://arxiv.org/abs/2106.14217) · [6](https://doi.org/10.1016/j.jalgebra.2021.09.034)


<a id="q3007"></a>

## Q3007. Four classes of closed full inverse monoids

**Status:** Open · **Kind:** conjecture (Conjecture 5.57) · **Collection** 31

Is every I₁-closed inverse submonoid M⊆I_X containing E_X equivalent under ≈ to exactly one of I_X, PStab(P_ω), PStab(P₂), E_X?

**Context.** Origin for question 3007: Thesis Conjecture 5.57. Setup for question 3007: Let X be countably infinite and I_X its monoid of partial bijections. Put A≼B when A⊆⟨B∪F⟩ for some finite F⊂I_X, and A≈B when both comparisons hold. E_X consists of partial identities. PStab(P) is the subgroup of all permutations of X fixing every block of P setwise. Let P₂ have two-element blocks, and P_ω finite blocks of unbounded size. Let I₁ be the topology generated by {f∈I_X:(x,y)∈f} and their complements, for x,y∈X.

**Source.** Martin Hampenberg Christensen. *Submonoids of Infinite Symmetric Inverse Monoids*. University of Hertfordshire, 2025. Advisor(s): Yann Péresse. [primary source](https://arxiv.org/abs/2509.04200) Location: Conjecture 5.57, p. 119; Theorem 2.75; Definitions 5.2–5.4.

**Literature check.** Status for question 3007, checked 8 October 2026: Thesis v2 retains the conjecture. The September 2026 follow-up classifies maximal subsemigroups, not these closed-full-monoid equivalence classes.

**Further links.** [1](https://arxiv.org/pdf/2509.04200) · [2](https://arxiv.org/abs/2509.08468v2) · [3](https://www.herts.ac.uk/research/groups-and-units/mathematics-and-mathematical-physics/people)


<a id="q3008"></a>

## Q3008. Asphericity of τ-cluster morphism categories

**Status:** Open · **Kind:** conjecture (Conjecture 1.1.1) · **Collection** 31

Must BW(A) be a K(π,1), equivalently have all higher homotopy groups zero?

**Context.** Origin for question 3008: Earlier picture-category asphericity problem, attributed to Igusa, Problem 3.0.5; retained in Kaipel’s thesis. Setup for question 3008: Let A be a finite-dimensional algebra over a field K with finitely many basic support τ-tilting modules. Its τ-cluster morphism category W(A) has τ-perpendicular wide subcategories as objects; arrows from W to J_W(M,P)=M^⊥∩{}^⊥τ\_W M∩P^⊥ are indexed by basic pairs (M,P), with P projective in W and Hom(M,τ\_W M)=Hom(P,M)=0, composed by τ-tilting reduction. Here τ\_W is Auslander–Reiten translation and perpendiculars mean Hom-orthogonality. BW(A) is the geometric realization of its nerve.

**Source.** Maximilian Kaipel. *New approaches to a homotopical problem in representation theory*. University of Cologne, 2025. Advisor(s): Sibylle Schroll and Hipolito Treffinger. [primary source](https://kups.ub.uni-koeln.de/79030/1/New_approaches_to_a%20homotopical_problem_in_representation_theory.pdf) Location: Conjecture 1.1.1, p. 6; Definition 2.3.1, p. 21.

**Literature check.** Status for question 3008, checked 8 October 2026: Børve–Kaipel, August 2026, still labels general asphericity conjectural; results cover special classes.

**Further links.** [1](https://kups.ub.uni-koeln.de/79030/) · [2](https://kaipel.net/maximilian/index.html) · [3](https://arxiv.org/abs/2608.13175) · [4](https://doi.org/10.1007/s00209-026-03957-1) · [5](https://doi.org/10.1016/j.jalgebra.2026.04.036)


<a id="q3009"></a>

## Q3009. Sharp square-modulus transversal differences

**Status:** Open · **Kind:** conjecture (Conjecture 8.2) · **Collection** 31

For every odd prime p and integer r≥1, is δ((Z/p²Z)^r,p(Z/p²Z)^r)=(2p−1)^r?

**Context.** Origin for question 3009: Authors’ higher-rank conjecture, including their square-plane conjecture. Setup for question 3009: For finite abelian H≤G, let δ(G,H)=min_T|T−T|, where T contains exactly one representative of each coset of H in G.

**Source.** Mugurel Barcau, Vicenţiu Paşol and George C. Ţurcaş. *Transversal Difference Numbers in Finite Abelian Quotients*. 2026. [primary source](https://arxiv.org/abs/2606.27961) Location: Conjecture 8.2; Conjecture 6.2 is the r=2 case.

**Literature check.** Status for question 3009, checked 8 October 2026: June 2026 v1 remains latest; only bounds and special cases are proved. No later resolution located.

**Further links.** [1](https://arxiv.org/html/2606.27961v1) · [2](https://github.com/georgeturcasubb/transversals)


<a id="q3010"></a>

## Q3010. Minimal lengths determine large finite groups

**Status:** Open · **Kind:** open problem (Question 5.2) · **Collection** 31

Does there exist N≥1 such that finite groups H,K with identical systems of minimal lengths for P(H),P(K) and max{|H|,|K|}≥N must be isomorphic?

**Context.** Origin for questions 3010, 3011: Questions 5.2–5.3 are distinct from the survey’s previously delivered questions. Setup for questions 3010, 3011: For a monoid H, P(H) comprises finite identity-containing subsets, multiplied setwise. An irreducible X≠{1} cannot be a product of two proper subsets in P(H). Factorizations use irreducibles; a factorization is minimal if no shorter factorization of the same X uses a submultiset of its factors in any order. L(X) and Lᵐ(X) record lengths and minimal lengths, with L({1})=Lᵐ({1})={0}. Their systems comprise the nonempty sets obtained as X varies.

**Source.** Salvatore Tringali. *Power monoids and their arithmetic: a survey*. 2026. [primary source](https://arxiv.org/abs/2602.15754v3) Location: Question 5.2, pp. 15–16.

**Literature check.** Status for questions 3010, 3011, checked 8 October 2026: Latest v3 and September author bibliography retain these targets; no resolution located.

**Further links.** [1](https://salvo-tringali.github.io/home/biblio-on-power-semigroups.html)


<a id="q3011"></a>

## Q3011. Interval unions of factorization lengths

**Status:** Open · **Kind:** open problem (Question 5.3) · **Collection** 31

For every monoid H and k≥1, are both ⋃{L(X):k∈L(X)} and ⋃{Lᵐ(X):k∈Lᵐ(X)} integer intervals, allowing the empty interval?

**Context.** Origin for questions 3010, 3011: Questions 5.2–5.3 are distinct from the survey’s previously delivered questions. Setup for questions 3010, 3011: For a monoid H, P(H) comprises finite identity-containing subsets, multiplied setwise. An irreducible X≠{1} cannot be a product of two proper subsets in P(H). Factorizations use irreducibles; a factorization is minimal if no shorter factorization of the same X uses a submultiset of its factors in any order. L(X) and Lᵐ(X) record lengths and minimal lengths, with L({1})=Lᵐ({1})={0}. Their systems comprise the nonempty sets obtained as X varies.

**Source.** Salvatore Tringali. *Power monoids and their arithmetic: a survey*. 2026. [primary source](https://arxiv.org/abs/2602.15754v3) Location: Question 5.3, p. 16.

**Literature check.** Status for questions 3010, 3011, checked 8 October 2026: Latest v3 and September author bibliography retain these targets; no resolution located.

**Further links.** [1](https://salvo-tringali.github.io/home/biblio-on-power-semigroups.html)


<a id="q3012"></a>

## Q3012. Simultaneously minimal Sylow intersections

**Status:** Open · **Kind:** open problem (Problem 21.26) · **Collection** 31

For every nontrivial finite G, choose one Sylow subgroup H_p for each prime p∣|G|. Is there x∈G such that every H_p∩H_p^x is inclusion-minimal among {H_p∩H_p^g:g∈G}?

**Context.** Origin for questions 3012, 3013, 3014, 3015: Original problems attributed individually below.

**Source.** E. I. Khukhro and V. D. Mazurov (editors). *Unsolved Problems in Group Theory. The Kourovka Notebook, 21st edition (v48)*. 2026. [primary source](https://arxiv.org/abs/1401.0300v48) Location: Problem 21.26, p. 180; F. Lisi–L. Sabatini, submitted by T. Burness.

**Literature check.** Status for questions 3012, 3013, 3014, 3015, checked 8 October 2026: Unmarked in v48. September 2026 Sylow results settle odd-order and simple groups, not general groups; Wilson’s finitely generated case is known.

**Further links.** [1](https://arxiv.org/abs/1401.0300) · [2](https://arxiv.org/pdf/1401.0300v48) · [3](https://arxiv.org/html/2609.28403v1) · [4](https://doi.org/10.1007/s00013-023-01851-4)


<a id="q3013"></a>

## Q3013. Asymptotic maximum p-length

**Status:** Open · **Kind:** open problem (Problem 21.55) · **Collection** 31

Fix q=p^a. If m_n(q) is the maximum p-length of a p-solvable subgroup of GL_n(F_q), does m_n(q)/log₂n→1 as n→∞?

**Context.** Origin for questions 3012, 3013, 3014, 3015: Original problems attributed individually below.

**Source.** E. I. Khukhro and V. D. Mazurov (editors). *Unsolved Problems in Group Theory. The Kourovka Notebook, 21st edition (v48)*. 2026. [primary source](https://arxiv.org/abs/1401.0300v48) Location: Problem 21.55, p. 185; İ. Güloğlu.

**Literature check.** Status for questions 3012, 3013, 3014, 3015, checked 8 October 2026: Unmarked in v48. September 2026 Sylow results settle odd-order and simple groups, not general groups; Wilson’s finitely generated case is known.

**Further links.** [1](https://arxiv.org/abs/1401.0300) · [2](https://arxiv.org/pdf/1401.0300v48) · [3](https://arxiv.org/html/2609.28403v1) · [4](https://doi.org/10.1007/s00013-023-01851-4)


<a id="q3014"></a>

## Q3014. Character degrees detect trivial solvable radical

**Status:** Open · **Kind:** open problem (Problem 21.135) · **Collection** 31

If finite groups G,H have identical multisets of irreducible complex character degrees and G has trivial solvable radical, must H also have trivial solvable radical?

**Context.** Origin for questions 3012, 3013, 3014, 3015: Original problems attributed individually below.

**Source.** E. I. Khukhro and V. D. Mazurov (editors). *Unsolved Problems in Group Theory. The Kourovka Notebook, 21st edition (v48)*. 2026. [primary source](https://arxiv.org/abs/1401.0300v48) Location: Problem 21.135, p. 197; A. V. Vasil’ev.

**Literature check.** Status for questions 3012, 3013, 3014, 3015, checked 8 October 2026: Unmarked in v48. September 2026 Sylow results settle odd-order and simple groups, not general groups; Wilson’s finitely generated case is known.

**Further links.** [1](https://arxiv.org/abs/1401.0300) · [2](https://arxiv.org/pdf/1401.0300v48) · [3](https://arxiv.org/html/2609.28403v1) · [4](https://doi.org/10.1007/s00013-023-01851-4)


<a id="q3015"></a>

## Q3015. Few infinite-order conjugacy classes

**Status:** Open · **Kind:** open problem (Problem 21.136) · **Collection** 31

If a profinite group has fewer than 2^{ℵ₀} conjugacy classes of infinite-order elements, must every element have finite order?

**Context.** Origin for questions 3012, 3013, 3014, 3015: Original problems attributed individually below.

**Source.** E. I. Khukhro and V. D. Mazurov (editors). *Unsolved Problems in Group Theory. The Kourovka Notebook, 21st edition (v48)*. 2026. [primary source](https://arxiv.org/abs/1401.0300v48) Location: Problem 21.136, p. 197; John S. Wilson.

**Literature check.** Status for questions 3012, 3013, 3014, 3015, checked 8 October 2026: Unmarked in v48. September 2026 Sylow results settle odd-order and simple groups, not general groups; Wilson’s finitely generated case is known.

**Further links.** [1](https://arxiv.org/abs/1401.0300) · [2](https://arxiv.org/pdf/1401.0300v48) · [3](https://arxiv.org/html/2609.28403v1) · [4](https://doi.org/10.1007/s00013-023-01851-4)


<a id="q3101"></a>

## Q3101. Odd girths for completely regular semigroups

**Status:** Open, partial results · **Kind:** open problem (Problem 7.3) · **Collection** 32

For every odd integer n≥3, does some finite noncommutative completely regular semigroup S satisfy girth(Γ(S))=n?

**Context.** Doctoral context for questions 3101, 3102: Tânia Patrícia Lopes Paulista. Commuting graphs of semigroups. PhD, 2025, NOVA University Lisbon. Advisors: António Malheiro; Alan J. Cain. Origin for questions 3101, 3102: Thesis Chapters 10–11; paper’s explicit open problems. Setup for questions 3101, 3102: For finite noncommutative S, Γ(S) has vertices S∖Z(S), joining distinct commuting elements. A left path x₀–⋯–x_l has l≥1 and x₀x_i=x_lx_i for every i; kd(S) is its minimum length, if defined. Inverse means unique semigroup inverses; completely regular means a union of subgroups.

**Source.** Tânia Paulista. *Commuting graphs of inverse semigroups and completely regular semigroups*. 2025. [primary source](https://arxiv.org/abs/2511.10612v1) Location: Problem 7.3, p. 28.

**Literature check.** Status for questions 3101, 3102, checked 8 October 2026: Current November 2025 v1 retains these questions; no later resolution located.

**Further links.** [1](https://arxiv.org/abs/2511.10612) · [2](https://www.dm.fct.unl.pt/teses-doutoramento-2025) · [3](https://run.unl.pt/entities/publication/4f3cfb38-a679-419c-8de9-f7b2f8b3a5f2) · [4](https://arxiv.org/html/2511.10612v1)

**Result (2026-10-09).** Every triangle-free commuting graph of a finite band is bipartite. In any finite completely regular semigroup with triangle-free commuting graph, the noncentral idempotents induce a bipartite graph, and every odd cycle contains at least two nonidempotent involutions whose subgroup identities are central. Odd girths at least five for general finite completely regular semigroups remain unresolved.

[Proof](../../solutions/seven-problems-2026-10-09/algebra/Q3101-odd-girth-obstructions.md) · [Internal review](../../solutions/seven-problems-2026-10-09/analysis/review-Q3101.md) · [Computational controls](../../solutions/seven-problems-2026-10-09/algebra/verification.json). This research proposal has a separate internal AI review; it is not externally peer reviewed.


<a id="q3102"></a>

## Q3102. Knit degree three for completely regular semigroups

**Status:** Solved here: disproved · **Kind:** open problem (Problem 7.4) · **Collection** 32

Does some finite noncommutative completely regular semigroup S satisfy kd(S)=3?

**Context.** Doctoral context for questions 3101, 3102: Tânia Patrícia Lopes Paulista. Commuting graphs of semigroups. PhD, 2025, NOVA University Lisbon. Advisors: António Malheiro; Alan J. Cain. Origin for questions 3101, 3102: Thesis Chapters 10–11; paper’s explicit open problems. Setup for questions 3101, 3102: For finite noncommutative S, Γ(S) has vertices S∖Z(S), joining distinct commuting elements. A left path x₀–⋯–x_l has l≥1 and x₀x_i=x_lx_i for every i; kd(S) is its minimum length, if defined. Inverse means unique semigroup inverses; completely regular means a union of subgroups.

**Source.** Tânia Paulista. *Commuting graphs of inverse semigroups and completely regular semigroups*. 2025. [primary source](https://arxiv.org/abs/2511.10612v1) Location: Problem 7.4, p. 28.

**Literature check.** Status for questions 3101, 3102, checked 8 October 2026: Current November 2025 v1 retains these questions; no later resolution located.

**Further links.** [1](https://arxiv.org/abs/2511.10612) · [2](https://www.dm.fct.unl.pt/teses-doutoramento-2025) · [3](https://run.unl.pt/entities/publication/4f3cfb38-a679-419c-8de9-f7b2f8b3a5f2) · [4](https://arxiv.org/html/2511.10612v1)

**Result (2026-10-09).** Every length-three left path in a finite completely regular semigroup constructively yields a length-two left path. Consequently no finite completely regular semigroup has knit degree three. No mathematical gap identified in the written proof and separate internal review. This is a nonexistence theorem, not a counterexample construction; it does not apply to arbitrary semigroups.

[Proof](../../solutions/seven-problems-2026-10-09/algebra/Q3102-no-knit-degree-three.md) · [Internal review](../../solutions/seven-problems-2026-10-09/combinatorics/review-Q3102.md) · [Computational controls](../../solutions/seven-problems-2026-10-09/algebra/verification.json). This research proposal has a separate internal AI review; it is not externally peer reviewed.


<a id="q3103"></a>

## Q3103. Largest commutative transformation semigroups

**Status:** Open · **Kind:** conjecture (Conjecture 7.5) · **Collection** 32

Is ξ(n)+1 the largest size of a commutative subsemigroup of T(X), with equality precisely for N_{B,b}∪{id_X}, where |B|=α(n) and b∈B?

**Context.** Doctoral context for question 3103: see question 3101. Origin for question 3103: Thesis Chapters 3–4; explicit paper conjecture. Setup for question 3103: Let |X|=n≥7 and T(X) be all self-maps under composition. Set ξ(n)=max_{1≤t≤n} t^(n−t), and let α(n) be the largest maximizing t. For B⊆X and b∈B, put N_{B,b}={f:X→B : f(B)={b}}.

**Source.** Tânia Paulista. *Characterizing the largest commutative (full and partial) transformation semigroups of certain types*. 2025. [primary source](https://arxiv.org/abs/2511.09495v1) Location: Conjecture 7.5, p. 69; Definitions 4.1 and 4.3, pp. 13–14.

**Literature check.** Status for question 3103, checked 8 October 2026: Current November 2025 v1 retains the conjecture; no later resolution located.

**Further links.** [1](https://arxiv.org/abs/2511.09495) · [2](https://www.dm.fct.unl.pt/teses-doutoramento-2025) · [3](https://run.unl.pt/entities/publication/4f3cfb38-a679-419c-8de9-f7b2f8b3a5f2) · [4](https://arxiv.org/html/2511.10612v1)


<a id="q3104"></a>

## Q3104. Henselian parahoric torsor injectivity

**Status:** Open · **Kind:** open problem (Question 2.0.2) · **Collection** 32

Is the restriction H¹\_et(R,𝒢)→H¹\_et(K,G) injective?

**Context.** Origin for question 3104: Bayer-Fluckiger–First’s older question; henselian case retained in the thesis. Setup for question 3104: Let R be a henselian discrete valuation ring with fraction field K, G a connected reductive K-group, and 𝒢 a parahoric R-model of G with connected fibres.

**Source.** Anis Zidani. *Arithmetic of Bruhat-Tits Group Schemes over a Semi-Local Dedekind Ring*. Kiel University, 2026. Advisor(s): Ralf Köhl and Philippe Gille. [primary source](https://d-nb.info/1388840782/34) Location: Question 2.0.2(2), pp. 63–64; open henselian clause p. 64.

**Literature check.** Status for question 3104, checked 8 October 2026: January 2026 author revision retains this case; March 2026 work gives only special cases.

**Further links.** [1](https://webusers.imj-prg.fr/~anis.zidani/publications/) · [2](https://webusers.imj-prg.fr/~anis.zidani/articles/Article_henselien_en.pdf) · [3](https://arxiv.org/abs/2603.05554) · [4](https://scop.math.berkeley.edu/collaboration-members/)


<a id="q3105"></a>

## Q3105. Local equality in the mixed-multiplicity bound

**Status:** Open · **Kind:** conjecture (Conjecture 6.2) · **Collection** 32

Is lct(I)=E_ℓ(I) equivalent to Ī=overline((y₁^{d₁},…,y_ℓ^{d_ℓ})) for some regular system of parameters y₁,…,y_n and positive integers d₁,…,d_ℓ? Here bars denote integral closure.

**Context.** Origin for question 3105: Author’s local extension of earlier diagonal-ideal results. Setup for question 3105: Let R=ℂ[[x₁,…,x_n]], m=(x₁,…,x_n), 1≤ℓ≤n, and I⊊R have height≥ℓ. Set σ₀=1 and σ\_j=sup_{t≥1} e((I+m^t)^{⟨j⟩},m^{⟨n−j⟩}), where e is mixed Hilbert–Samuel multiplicity and ⟨r⟩ means r repetitions. Put E_ℓ(I)=Σ\_{j=1}^ℓ σ\_{j−1}/σ\_j.

**Source.** Benjamin Baily. *Homogeneous ideals with minimal singularity thresholds*. [primary source](https://arxiv.org/abs/2603.08698v1) Location: Conjecture 6.2, p. 41; Definitions 2.36 and 2.38, pp. 11–12.

**Literature check.** Status for question 3105, checked 8 October 2026: March 2026 v1 proves the homogeneous and dimension-two cases; general case remains conjectural.

**Further links.** [1](https://bbaily.github.io/) · [2](https://arxiv.org/abs/2603.08698) · [3](https://sites.lsa.umich.edu/kesmith/graduate-students/)


<a id="q3111"></a>

## Q3111. Reciprocal irreducibility over unique-factorization domains

**Status:** Open · **Kind:** open problem · **Collection** 32

Are these equivalent: (i) G(g^e)=span_K{1,g,…,g^e} for all e≥1; (ii) 1/g is irreducible in R(D); (iii) G(g)=K+Kg?

**Context.** Origin for question 3111: New open equivalence following the authors’ Theorem 3.3.6. Setup for question 3111: For a domain D let R(D)⊆Frac(D) be generated by {1/f : 0≠f∈D}. Assume D is a UFD, K=D∩R(D) is a field algebraically closed in Frac(D), and g∈D∖K. Write G(g^e)={f∈D : f/g^e∈R(D)}.

**Source.** Neil Epstein and Lorenzo Guerrieri. *An introduction to reciprocal complements of integral domains*. 2026. [primary source](https://arxiv.org/abs/2512.20801v2) Location: Remark 3.3.13, p. 17; Theorem 3.3.6, pp. 14–15.

**Literature check.** Status for question 3111, checked 8 October 2026: August 2026 v2 retains the question; the general-domain counterexamples are not UFDs.

**Further links.** [1](https://arxiv.org/abs/2512.20801) · [2](https://arxiv.org/abs/2604.19253)


<a id="q3201"></a>

## Q3201. Right coherence of free left h-Ehresmann monoids

**Status:** Open · **Kind:** open problem (Question 6.1) · **Collection** 33

Is F_X right coherent for every set X?

**Context.** Doctoral context for questions 3201, 3202: Daniel Heath. Graphical approaches to left adequate monoids. PhD, 2025, University of Manchester. Advisors: Mark Kambites; Nóra Szakács. Origin for questions 3201, 3202: Post-thesis paper questions; monogenic question attributed to Gould–Johnson. Setup for questions 3201, 3202: Let F_X be free on X among monoids with unary + satisfying x⁺x=x, (x⁺y⁺)⁺=x⁺y⁺=y⁺x⁺, (xy)⁺=(xy⁺)⁺ and (xz⁺y)⁺=(xy)⁺(xz)⁺. A monoid is right coherent when every finitely generated subact of every finitely presented right act is finitely presented; left coherence is dual.

**Source.** Daniel Heath. *Free left h-Ehresmann semigroups*. 2025. [primary source](https://arxiv.org/abs/2608.24657) Location: Question 6.1, p. 21.

**Literature check.** Status for questions 3201, 3202, checked 8 October 2026: August 2026 v1 and Gould–Johnson’s June 2026 final retain these questions; no later resolution located.

**Further links.** [1](https://dpheath.github.io/research.html) · [2](https://eprints.whiterose.ac.uk/id/eprint/241685/) · [3](https://eprints.whiterose.ac.uk/id/eprint/241685/8/1-s2.0-S0021869326003091-main.pdf) · [4](https://research.manchester.ac.uk/en/studentTheses/graphical-approaches-to-left-adequate-monoids/) · [5](https://dpheath.github.io/)


<a id="q3202"></a>

## Q3202. Left coherence in the monogenic h-Ehresmann case

**Status:** Open · **Kind:** open problem (Question 6.1) · **Collection** 33

Is the monogenic F_{ {x} } left coherent?

**Context.** Doctoral context for questions 3201, 3202: Daniel Heath. Graphical approaches to left adequate monoids. PhD, 2025, University of Manchester. Advisors: Mark Kambites; Nóra Szakács. Origin for questions 3201, 3202: Post-thesis paper questions; monogenic question attributed to Gould–Johnson. Setup for questions 3201, 3202: Let F_X be free on X among monoids with unary + satisfying x⁺x=x, (x⁺y⁺)⁺=x⁺y⁺=y⁺x⁺, (xy)⁺=(xy⁺)⁺ and (xz⁺y)⁺=(xy)⁺(xz)⁺. A monoid is right coherent when every finitely generated subact of every finitely presented right act is finitely presented; left coherence is dual.

**Source.** Daniel Heath. *Free left h-Ehresmann semigroups*. 2025. [primary source](https://arxiv.org/abs/2608.24657) Location: Paragraph after Question 6.1, p. 21.

**Literature check.** Status for questions 3201, 3202, checked 8 October 2026: August 2026 v1 and Gould–Johnson’s June 2026 final retain these questions; no later resolution located.

**Further links.** [1](https://dpheath.github.io/research.html) · [2](https://eprints.whiterose.ac.uk/id/eprint/241685/) · [3](https://eprints.whiterose.ac.uk/id/eprint/241685/8/1-s2.0-S0021869326003091-main.pdf) · [4](https://research.manchester.ac.uk/en/studentTheses/graphical-approaches-to-left-adequate-monoids/) · [5](https://dpheath.github.io/)


<a id="q3203"></a>

## Q3203. Hypercentrality of all Dedekind skew braces

**Status:** Open · **Kind:** open problem (Question 3.13) · **Collection** 33

Does the upper central series of every Dedekind skew brace reach B?

**Context.** Origin for questions 3203, 3204: Article’s explicit questions. Setup for questions 3203, 3204: A skew brace B has groups (B,+),(B,∘) with a∘(b+c)=a∘b−a+a∘c. Write λ\_a(b)=−a+a∘b and Z(B)=kerλ∩Z(B,+)∩Z(B,∘). Dedekind means every common subgroup is an ideal: normal in both groups and λ-invariant. Its upper central series starts at 0, takes the preimage of Z(B/Z_α) at successors and unions at limits.

**Source.** Andrea Caranti, Ilaria Del Corso, Massimiliano Di Matteo, Maria Ferrara and Marco Trombetti. *On Dedekind Skew Braces*. [primary source](https://doi.org/10.1007/s00025-026-02619-2) Location: Question 3.13, first bullet.

**Literature check.** Status for questions 3203, 3204, checked 8 October 2026: April 2026 final article retains these questions; no later resolution located.

**Further links.** [1](https://link.springer.com/article/10.1007/s00025-026-02619-2) · [2](https://arxiv.org/abs/2507.23550)


<a id="q3204"></a>

## Q3204. Central nilpotency without finite Hirsch length

**Status:** Open · **Kind:** open problem (Question 3.13) · **Collection** 33

Suppose B is Dedekind and has a finite ideal series with factors whose two operations coincide. If at least one underlying group has only finitely many primes dividing the orders of its torsion elements, must Z_c(B)=B for some finite c?

**Context.** Origin for questions 3203, 3204: Article’s explicit questions. Setup for questions 3203, 3204: A skew brace B has groups (B,+),(B,∘) with a∘(b+c)=a∘b−a+a∘c. Write λ\_a(b)=−a+a∘b and Z(B)=kerλ∩Z(B,+)∩Z(B,∘). Dedekind means every common subgroup is an ideal: normal in both groups and λ-invariant. Its upper central series starts at 0, takes the preimage of Z(B/Z_α) at successors and unions at limits.

**Source.** Andrea Caranti, Ilaria Del Corso, Massimiliano Di Matteo, Maria Ferrara and Marco Trombetti. *On Dedekind Skew Braces*. [primary source](https://doi.org/10.1007/s00025-026-02619-2) Location: Question 3.13, third bullet; Corollary 3.9(2).

**Literature check.** Status for questions 3203, 3204, checked 8 October 2026: April 2026 final article retains these questions; no later resolution located.

**Further links.** [1](https://link.springer.com/article/10.1007/s00025-026-02619-2) · [2](https://arxiv.org/abs/2507.23550)


<a id="q3205"></a>

## Q3205. Complexity of recognizing complete mappings

**Status:** Open, partial results · **Kind:** open problem (Problem 15.10) · **Collection** 33

What is the computational complexity, with the Cayley table as input, of deciding whether a finite semigroup has a complete mapping? Determine it also for regular, inverse, completely regular, completely 0-simple and aperiodic semigroups.

**Context.** Origin for question 3205: Paper’s explicit problems. Setup for question 3205: A complete mapping of a finite semigroup S is a permutation f for which x↦x·f(x) is also a permutation.

**Source.** João Araújo, Wolfram Bentz, Peter J. Cameron, Kevin Hendrey and Michael Kinyon. *Complete Mappings of Semigroups*. [primary source](https://arxiv.org/abs/2608.25092) Location: Problem 15.10, p. 60.

**Literature check.** Status for question 3205, checked 8 October 2026: August 2026 preprint checked; no later resolution located.

**Results.**

- **Partial result**: Deterministic P for inverse, completely regular, and aperiodic semigroups; aperiodic positive instances have constructive certificates. Scope: inverse semigroups completely regular semigroups aperiodic semigroups general and regular semigroups completely 0-simple semigroups Restrictions/extensions: inverse semigroups; completely regular semigroups; aperiodic semigroups; general and regular semigroups; completely 0-simple semigroups Remaining: Full complexity classification for general, regular, and completely 0-simple semigroups; no NP-hardness or P-completeness claim. Filed from the external B13 return; scope reading only, not an independent proof audit or a formal certificate. [Details](../../solutions/b13-2026-10-09/B13_Research_Report.md).


<a id="q3209"></a>

## Q3209. Exact idempotent growth of the free adequate monoid

**Status:** Open · **Kind:** open problem (Question 4.19) · **Collection** 33

Determine the asymptotic growth of e_n, including its exponential rate λ\_E.

**Context.** Doctoral context for question 3209: see question 3201. Origin for question 3209: Explicit paper questions from Heath’s doctoral research. Setup for question 3209: Let s_n count isomorphism classes of finite directed trees with n edges and distinguished vertices s,t joined by a possibly empty directed path, admitting no nonidentity retraction fixing s,t. A retraction is an idempotent directed-graph endomorphism; isomorphisms preserve direction and distinguished vertices. Let e_n count those with s=t. These are the length-n elements and idempotents of the monogenic free adequate monoid; length counts generator occurrences, not unary operations. Put λ\_E=limsup e_n^(1/n), λ\_S=limsup s_n^(1/n).

**Source.** Thomas Aird and Daniel Heath. *Growth and identities of monogenic free adequate monoids*. 2025. [primary source](https://arxiv.org/abs/2509.09543v1) Location: Question 4.19, p. 12; Corollary 4.4, p. 7; §2.3.

**Literature check.** Status for question 3209, checked 8 October 2026: September 2025 v1 remains current; only an exponential lower bound is proved.

**Further links.** [1](https://arxiv.org/abs/2509.09543) · [2](https://dpheath.github.io/research.html) · [3](https://research.manchester.ac.uk/en/studentTheses/graphical-approaches-to-left-adequate-monoids/)


<a id="q3210"></a>

## Q3210. Semiprimitivity of every integral group ring

**Status:** Open · **Kind:** conjecture (Conjecture A) · **Collection** 33

Is J(ℤ[G])=0 for every group G?

**Context.** Origin for question 3210: Older integral group-ring conjecture restated as Conjecture A. Setup for question 3210: For a unital ring R, J(R) is the intersection of its maximal right ideals. ℤ[G] is the ring of finite integer linear combinations of elements of G.

**Source.** F. E. A. Johnson. *On the radical of group rings*. [primary source](https://doi.org/10.1007/s00013-025-02208-9) Location: Conjecture A,p. 239.

**Literature check.** Status for question 3210, checked 8 October 2026: January 2026 final article proves special classes, including residually finite groups; no general resolution located.

**Further links.** [1](https://link.springer.com/article/10.1007/s00013-025-02208-9) · [2](https://discovery.ucl.ac.uk/id/eprint/10217355/)


<a id="q3211"></a>

## Q3211. Fourfold codegree prime bound

**Status:** Open · **Kind:** open problem (Problem 21.108) · **Collection** 33

Does |π(|G|)|≤4σ(G) hold for every finite group G?

**Context.** Origin for questions 3211, 3212, 3213: Explicit questions in the 21st edition. Setup for questions 3211, 3212, 3213: For finite G, let Cod(G)={|G:kerχ|/χ(1):χ∈Irr_ℂ(G)}, let π(m) denote the prime divisors of m, and set σ(G)=max_{c∈Cod(G)}|π(c)|. Write G⁽⁰⁾=G, G⁽ᵢ⁺¹⁾=[G⁽ᵢ⁾,G⁽ᵢ⁾].

**Source.** E. I. Khukhro and V. D. Mazurov (editors). *Unsolved Problems in Group Theory: The Kourovka Notebook, 21st edition*. [primary source](https://arxiv.org/abs/1401.0300v48) Location: Problem 21.108,p. 193(Qian).

**Literature check.** Status for questions 3211, 3212, 3213, checked 8 October 2026: 6 October 2026 v48 leaves all three unmarked as solved or proof-claimed; targeted searches found no resolution.

**Further links.** [1](https://sites.google.com/site/lucasabatinimath/research/papers) · [2](https://arxiv.org/abs/2606.27065) · [3](https://arxiv.org/abs/2107.00735)


<a id="q3212"></a>

## Q3212. Derived length from distinct character codegrees

**Status:** Open · **Kind:** open problem (Problem 21.109) · **Collection** 33

For every finite solvable group G, is its derived length at most |Cod(G)|−1?

**Context.** Origin for questions 3211, 3212, 3213: Explicit questions in the 21st edition. Setup for questions 3211, 3212, 3213: For finite G, let Cod(G)={|G:kerχ|/χ(1):χ∈Irr_ℂ(G)}, let π(m) denote the prime divisors of m, and set σ(G)=max_{c∈Cod(G)}|π(c)|. Write G⁽⁰⁾=G, G⁽ᵢ⁺¹⁾=[G⁽ᵢ⁾,G⁽ᵢ⁾].

**Source.** E. I. Khukhro and V. D. Mazurov (editors). *Unsolved Problems in Group Theory: The Kourovka Notebook, 21st edition*. [primary source](https://arxiv.org/abs/1401.0300v48) Location: Problem 21.109,p. 193(Qian).

**Literature check.** Status for questions 3211, 3212, 3213, checked 8 October 2026: 6 October 2026 v48 leaves all three unmarked as solved or proof-claimed; targeted searches found no resolution.

**Further links.** [1](https://sites.google.com/site/lucasabatinimath/research/papers) · [2](https://arxiv.org/abs/2606.27065) · [3](https://arxiv.org/abs/2107.00735)


<a id="q3213"></a>

## Q3213. Uniform derived length for weakly ab-maximal groups

**Status:** Open · **Kind:** open problem (Problem 21.114) · **Collection** 33

Is there an absolute c such that G⁽ᶜ⁾=1 for every finite group G satisfying |H/[H,H]|≤|G/[G,G]| for every subgroup H≤G?

**Context.** Origin for questions 3211, 3212, 3213: Explicit questions in the 21st edition. Setup for questions 3211, 3212, 3213: For finite G, let Cod(G)={|G:kerχ|/χ(1):χ∈Irr_ℂ(G)}, let π(m) denote the prime divisors of m, and set σ(G)=max_{c∈Cod(G)}|π(c)|. Write G⁽⁰⁾=G, G⁽ᵢ⁺¹⁾=[G⁽ᵢ⁾,G⁽ᵢ⁾].

**Source.** E. I. Khukhro and V. D. Mazurov (editors). *Unsolved Problems in Group Theory: The Kourovka Notebook, 21st edition*. [primary source](https://arxiv.org/abs/1401.0300v48) Location: Problem 21.114,p. 194(Sabatini).

**Literature check.** Status for questions 3211, 3212, 3213, checked 8 October 2026: 6 October 2026 v48 leaves all three unmarked as solved or proof-claimed; targeted searches found no resolution.

**Further links.** [1](https://sites.google.com/site/lucasabatinimath/research/papers) · [2](https://arxiv.org/abs/2606.27065) · [3](https://arxiv.org/abs/2107.00735)


<a id="q3214"></a>

## Q3214. Equality on modules of even order

**Status:** Open · **Kind:** open problem (Question 9.1) · **Collection** 33

If V is completely reducible, |V| is even and |G:G′|=M(G,V)/p, must G be nilpotent? For p≥5, must |G′|=p?

**Context.** Origin for questions 3214, 3215, 3216: New questions in the paper. Setup for questions 3214, 3215, 3216: Let G be finite nonabelian of odd order, p its smallest prime divisor, G′=[G,G], and M(G,V)=max_{v∈V}|v^G|. Modules are finite and faithful; completely reducible modules may have mixed characteristic.

**Source.** Thomas Michael Keller. *Abelian quotients and the largest orbit sizes of linear groups of odd order*. [primary source](https://arxiv.org/abs/2610.08690v1) Location: Question 9.1, p. 29.

**Literature check.** Status for questions 3214, 3215, 3216, checked 8 October 2026: 6 October 2026 v1 is current; no later resolution located.


<a id="q3215"></a>

## Q3215. Sharp orbit ratio for nonnilpotent odd-order groups

**Status:** Open · **Kind:** open problem (Question 9.2) · **Collection** 33

For each prime p≥5, determine inf M(G,V)/|G:G′| over nonnilpotent G with smallest prime divisor p and completely reducible V of odd order.

**Context.** Origin for questions 3214, 3215, 3216: New questions in the paper. Setup for questions 3214, 3215, 3216: Let G be finite nonabelian of odd order, p its smallest prime divisor, G′=[G,G], and M(G,V)=max_{v∈V}|v^G|. Modules are finite and faithful; completely reducible modules may have mixed characteristic.

**Source.** Thomas Michael Keller. *Abelian quotients and the largest orbit sizes of linear groups of odd order*. [primary source](https://arxiv.org/abs/2610.08690v1) Location: Question 9.2, first part, p. 29.

**Literature check.** Status for questions 3214, 3215, 3216, checked 8 October 2026: 6 October 2026 v1 is current; no later resolution located.


<a id="q3216"></a>

## Q3216. Orbit bound without complete reducibility

**Status:** Open · **Kind:** open problem (Question 9.3) · **Collection** 33

If V has odd characteristic s and O_s(G)=1, must |G:G′|≤M(G,V)/p? Here O_s(G) is the largest normal s-subgroup.

**Context.** Origin for questions 3214, 3215, 3216: New questions in the paper. Setup for questions 3214, 3215, 3216: Let G be finite nonabelian of odd order, p its smallest prime divisor, G′=[G,G], and M(G,V)=max_{v∈V}|v^G|. Modules are finite and faithful; completely reducible modules may have mixed characteristic.

**Source.** Thomas Michael Keller. *Abelian quotients and the largest orbit sizes of linear groups of odd order*. [primary source](https://arxiv.org/abs/2610.08690v1) Location: Question 9.3, p. 29.

**Literature check.** Status for questions 3214, 3215, 3216, checked 8 October 2026: 6 October 2026 v1 is current; no later resolution located.


<a id="q3217"></a>

## Q3217. Surjective restriction to classical Springer fibers

**Status:** Open · **Kind:** conjecture (Conjecture 1.6) · **Collection** 33

Is H\*(B)→H\*(B_e) surjective exactly when: (C) g=sp₂ₙ and e is regular in a Levi sp₂ₐ×∏gl_bᵢ with bᵢ∈{2a+1,2a,2a−1,1}; (B) g=so₂ₙ₊₁ and e is regular in a Levi so₂ₐ₊₁×∏gl_bᵢ with bᵢ∈{2a+2,2a+1,2a}; or (D) g=so₂ₙ and e’s partition is ((2a+2)^(2d₁),(2a+1)^(2d₂)), ((2a+1)^(2d₁),(2a)^(2d₂)), ((2a+3)^(2d₁+1),(2a+2)^(2d₂),(2a+1)^(2d₃+1)), ((2a+1)^(2d₁+1),(2b+1)^(2d₂+1)), or ((2a+1)^(2d₁+1),(2a)^(2d₂),2^(2d₃),1^(2d₄+1)), with nonnegative integers a,b,dᵢ and positive integer Levi block sizes?

**Context.** Doctoral context for question 3217: Do Kien Hoang. Representation theory, Geometry and Combinatorics associated to Springer fibers. PhD, 2025, Yale University. Advisors: Ivan Losev. Origin for question 3217: Doctoral research; joint conjecture with Krylov and Matvieievskyi, also Conjecture B.7 of arXiv:2410.20512. Setup for question 3217: Let g be a complex classical Lie algebra, e nilpotent, B its flag variety, and B_e the Borel subalgebras containing e. Cohomology has complex coefficients. In partitions, r^m denotes m parts r; zero parts are omitted.

**Source.** Do Kien Hoang. *Hikita conjecture for classical Lie algebras*. 2025. [primary source](https://arxiv.org/abs/2409.13914v3) Location: Conjecture 1.6, pp. 4–5; companion B.7, pp. 73–74.

**Literature check.** Status for question 3217, checked 8 October 2026: Current v3 and later companion retain the classification conjecture; only partial cases proved.

**Further links.** [1](https://arxiv.org/abs/2409.13914) · [2](https://arxiv.org/abs/2410.20512) · [3](https://sites.google.com/view/dokienhoangnortheastern/home) · [4](https://elischolar.library.yale.edu/gsas_dissertations/1573/)


<a id="q3301"></a>

## Q3301. Dense section orbits

**Status:** Open · **Kind:** open problem (Question 1) · **Collection** 34

Must some g∈G have {g|\_v:v∈T} dense in G?

**Context.** Doctoral context for question 3301: Jorge Fariña-Asategui. Groups acting on rooted trees: Dimension, subgroups, randomness and dynamics. PhD defended 22 May 2026; thesis title page verifies both co-supervisors, Lund University / University of the Basque Country. Advisors: Anitha Thillaisundaram; Gustavo A. Fernández-Alcober. Origin for question 3301: Doctoral-research paper; later included in the thesis. Setup for question 3301: Let T be the regular rooted m-ary tree, m≥2. Let G≤Aut(T) be closed in the level-stabilizer topology. For every g∈G and vertex v, require its section g|\_v∈G and {h|\_v:h∈G fixes v}=G. Level-transitivity is not assumed.

**Source.** Jorge Fariña-Asategui. *Cyclicity, hypercyclicity and randomness in self-similar groups*. 2026. [primary source](https://doi.org/10.1007/s00605-025-02061-6) Location: Question 1, p. 276 (PDF p. 2); §2.3 and Definition 3.3.

**Literature check.** Status for question 3301, checked 8 October 2026: Final 2025 article retains the question; later finite-type results do not cover arbitrary fractal groups.

**Further links.** [1](https://d-nb.info/136471132X/34) · [2](https://arxiv.org/abs/2505.21134) · [3](https://lup.lub.lu.se/record/718511b0-6347-4ee9-9ed3-2b99bf54c08a) · [4](https://lup.lub.lu.se/search/files/248603771/kappa-farina.pdf)


<a id="q3302"></a>

## Q3302. Bicompact torsion classes

**Status:** Open · **Kind:** conjecture (Conjecture 1.2) · **Collection** 34

If T=T(M) and T⊥=F(N) for some M,N∈mod A, must T consist of all quotients of finite direct sums of one module P∈mod A?

**Context.** Origin for question 3302: Conjecture introduced in this paper. Setup for question 3302: Let A be a finite-dimensional algebra over a field K, and mod A its finitely generated modules. A torsion class is a full subcategory closed under quotients and extensions; a torsion-free class is closed under submodules and extensions. Write T(M), F(N) for the smallest such classes containing M,N, and T⊥={X:Hom_A(T,X)=0}.

**Source.** Sota Asai. *Bicompact torsion classes and conjectures on brick infinite algebras*. [primary source](https://arxiv.org/abs/2604.04505v1) Location: Conjecture 1.2; Definition 1.1, p. 1.

**Literature check.** Status for question 3302, checked 8 October 2026: April 2026 v1 retains it; hereditary and semistable cases are proved.


<a id="q3303"></a>

## Q3303. Groups without picky elements

**Status:** Open · **Kind:** open problem (Question 8.4) · **Collection** 34

Classify all pairs (G,p) for which no nonidentity p-element belongs to exactly one Sylow p-subgroup of G.

**Context.** Origin for questions 3303, 3304: Classification questions posed in this paper. Setup for questions 3303, 3304: Throughout, G is finite and p is prime. For x∈G, let Sub_G(x)=⟨g∈G:⟨x⟩ is subnormal in ⟨x,g⟩⟩. A p-element has p-power order.

**Source.** Alexander Moretó. *Alperin’s Main Problem of Block Theory*. [primary source](https://arxiv.org/abs/2605.11988v3) Location: Question 8.4, p. 50.

**Literature check.** Status for questions 3303, 3304, checked 8 October 2026: June 2026 v3 retains both questions; its primitive character bijection conjecture is a different target.

**Further links.** [1](https://arxiv.org/abs/2606.04526) · [2](https://doi.org/10.1017/fms.2025.10117)


<a id="q3304"></a>

## Q3304. Maximal subnormalizers

**Status:** Open · **Kind:** open problem (Question 8.5) · **Collection** 34

Classify all pairs (G,p) for which Sub_G(x)=G for every nonidentity p-element x∈G.

**Context.** Origin for questions 3303, 3304: Classification questions posed in this paper. Setup for questions 3303, 3304: Throughout, G is finite and p is prime. For x∈G, let Sub_G(x)=⟨g∈G:⟨x⟩ is subnormal in ⟨x,g⟩⟩. A p-element has p-power order.

**Source.** Alexander Moretó. *Alperin’s Main Problem of Block Theory*. [primary source](https://arxiv.org/abs/2605.11988v3) Location: Question 8.5, p. 50.

**Literature check.** Status for questions 3303, 3304, checked 8 October 2026: June 2026 v3 retains both questions; its primitive character bijection conjecture is a different target.

**Further links.** [1](https://arxiv.org/abs/2606.04526) · [2](https://doi.org/10.1017/fms.2025.10117)


<a id="q3305"></a>

## Q3305. Jordan structure after grading

**Status:** Open · **Kind:** open problem (Problem 4.14) · **Collection** 34

For a finite generating set X of axes, let L_r span all nonassociative words in X of lengths 1,…,r, with L₀=0. Must ⊕\_{r≥1}L_r/L_{r−1} be Jordan?

**Context.** Origin for questions 3305, 3306: Questions attributed to Rowen (grading) and Tkachev (identity); the central-extension repeat is excluded. Setup for questions 3305, 3306: Over a field k of characteristic ≠2, A is commutative, generated by idempotents a with A=A₁(a)⊕A₀(a)⊕A_{1/2}(a), A₁(a)=ka. Here A_λ(a)={u:au=λu}; the fusion inclusions are A₁A₀=0, A₀²⊆A₀, (A₁+A₀)A_{1/2}⊆A_{1/2}, and A_{1/2}²⊆A₁+A₀. Jordan means (x²y)x=x²(yx).

**Source.** I. Gorshkov and S. Shpectorov. *Axial Algebras: Questions and Conjectures*. [primary source](https://arxiv.org/abs/2606.30048v1) Location: Problem 4.14, p. 18.

**Literature check.** Status for questions 3305, 3306, checked 8 October 2026: June survey retains these; September Rowen v4 does not settle them.

**Further links.** [1](https://arxiv.org/abs/2606.30048) · [2](https://doi.org/10.1016/j.jalgebra.2024.09.001) · [3](https://arxiv.org/abs/2508.16427v4)


<a id="q3306"></a>

## Q3306. A common one-variable identity

**Status:** Open · **Kind:** open problem (Problem 4.4) · **Collection** 34

Does a nonzero polynomial in the free commutative nonassociative k-algebra on one variable vanish under every evaluation in every such A?

**Context.** Origin for questions 3305, 3306: Questions attributed to Rowen (grading) and Tkachev (identity); the central-extension repeat is excluded. Setup for questions 3305, 3306: Over a field k of characteristic ≠2, A is commutative, generated by idempotents a with A=A₁(a)⊕A₀(a)⊕A_{1/2}(a), A₁(a)=ka. Here A_λ(a)={u:au=λu}; the fusion inclusions are A₁A₀=0, A₀²⊆A₀, (A₁+A₀)A_{1/2}⊆A_{1/2}, and A_{1/2}²⊆A₁+A₀. Jordan means (x²y)x=x²(yx).

**Source.** I. Gorshkov and S. Shpectorov. *Axial Algebras: Questions and Conjectures*. [primary source](https://arxiv.org/abs/2606.30048v1) Location: Problem 4.4, p. 15.

**Literature check.** Status for questions 3305, 3306, checked 8 October 2026: June survey retains these; September Rowen v4 does not settle them.

**Further links.** [1](https://arxiv.org/abs/2606.30048) · [2](https://doi.org/10.1016/j.jalgebra.2024.09.001) · [3](https://arxiv.org/abs/2508.16427v4)


<a id="q3313"></a>

## Q3313. Solvable detection of orientation reversal

**Status:** Open · **Kind:** conjecture (Conjecture 1) · **Collection** 34

If det(g|V^H)=−1 for some H≤G and g∈N_G(H), must a solvable subgroup K≤G satisfy dim(V^K)≢dim(V) mod 2?

**Context.** Doctoral context for question 3313: Sam Kim Miller. Permutation modules and endotrivial complexes. PhD, 2025, University of California, Santa Cruz. Advisors: Robert Boltje. Origin for question 3313: Post-thesis conjecture. Setup for question 3313: Let V be a finite-dimensional real representation of a finite group G. For H≤G, write V^H for its fixed subspace.

**Source.** Sam K. Miller. *Non-orientable representation spheres*. 2025. [primary source](https://arxiv.org/abs/2608.18015v1) Location: Conjecture 1, p. 7; Theorem 2.4 and Proposition 2.5.

**Literature check.** Status for question 3313, checked 8 October 2026: August v1 retains it. The current author page says “under revision”; no newer public text was located.

**Further links.** [1](https://arxiv.org/abs/2608.18015) · [2](https://www.samkmiller.com/research/) · [3](https://escholarship.org/uc/item/9h73j2g4) · [4](https://www.samkmiller.com/)


<a id="q3316"></a>

## Q3316. Abstractly different nonsplit extensions

**Status:** Open · **Kind:** open problem (Question 5.1) · **Collection** 34

For a finite abelian H-module M with H²(H,M)≠0, must some nonzero cohomology class yield an extension E of M by H, inducing the given action, with E not isomorphic as an abstract group to M⋊H?

**Context.** Doctoral context for questions 3316, 3317: Nowras Naufel Ali Mahamoud Otmen. Current doctoral student, University of Padua. Advisors: Andrea Lucchini (supervisor); Martino Garonzi (co-supervisor). Origin for questions 3316, 3317: Questions from current doctoral research, not a completed dissertation. Setup for questions 3316, 3317: All groups and factors are finite. A section is a quotient of a subgroup. Call G sectionally indecomposable if G being a section of A×B forces it to be a section of A or B. Monolithic means having one minimal nontrivial normal subgroup.

**Source.** Andrea Lucchini and Nowras Otmen. *Sectionally indecomposable groups*. [primary source](https://arxiv.org/abs/2606.28080v1) Location: Question 5.1, p. 11.

**Literature check.** Status for questions 3316, 3317, checked 8 October 2026: June 2026 v1 retains both; the primitive case and several p-group families are settled.

**Further links.** [1](https://arxiv.org/abs/2606.28080) · [2](https://dottorato.math.unipd.it/people/phd_students)


<a id="q3317"></a>

## Q3317. Sectionally indecomposable p-groups

**Status:** Open · **Kind:** open problem (Question 5.3) · **Collection** 34

For some prime p, does a noncyclic monolithic p-group exist that is sectionally indecomposable?

**Context.** Doctoral context for questions 3316, 3317: Nowras Naufel Ali Mahamoud Otmen. Current doctoral student, University of Padua. Advisors: Andrea Lucchini (supervisor); Martino Garonzi (co-supervisor). Origin for questions 3316, 3317: Questions from current doctoral research, not a completed dissertation. Setup for questions 3316, 3317: All groups and factors are finite. A section is a quotient of a subgroup. Call G sectionally indecomposable if G being a section of A×B forces it to be a section of A or B. Monolithic means having one minimal nontrivial normal subgroup.

**Source.** Andrea Lucchini and Nowras Otmen. *Sectionally indecomposable groups*. [primary source](https://arxiv.org/abs/2606.28080v1) Location: Question 5.3, p. 12.

**Literature check.** Status for questions 3316, 3317, checked 8 October 2026: June 2026 v1 retains both; the primitive case and several p-group families are settled.

**Further links.** [1](https://arxiv.org/abs/2606.28080) · [2](https://dottorato.math.unipd.it/people/phd_students)


<a id="q3401"></a>

## Q3401. Abundant free idempotent-generated semigroups

**Status:** Open · **Kind:** open problem · **Collection** 35

Characterize the normal bands B for which IG(B) is abundant.

**Context.** Origin: Gould’s question, pursued in the thesis. Setup: Let B be a semigroup satisfying x²=x and xyzx=xzyx (a normal band). Define IG(B)=⟨ē (e∈B) | ēf̄=overline(ef) whenever {e,f}∩{ef,fe}≠∅⟩. In a semigroup S, a L\* b means ax=ay⇔bx=by for all x,y∈S¹; R\* is dual. S is abundant when every L\*-class and R\*-class contains an idempotent.

**Source.** Nouf Abdulrahman Alqahtani. *Abundant semigroups and constructions*. University of York, 2021. Advisor(s): Victoria Gould, Brent Everitt. [primary source](https://etheses.whiterose.ac.uk/id/eprint/30676/8/Alqahtani_202053642_Thesis.pdf) Location: Chapter 8, p. 173; Chapter 6, p. 79; Definition 3.1.3, Lemma 3.1.1 and §5.3.1.

**Literature check.** Status: Thesis retains general classification after proving the iso-normal case; bounded follow-up search found no resolution.


<a id="q3402"></a>

## Q3402. Separating free regular subalgebras

**Status:** Open · **Kind:** open problem (Problem 2.6.13) · **Collection** 35

For every finitely generated subalgebra A≤FCR(X) and u∉A, does a homomorphism φ to a finite completely regular algebra exist with φ(u)∉φ(A)?

**Context.** Origin: Thesis problem. Setup: Let X be a set with |X|≥2. Let FCR(X) be free on X in the variety with multiplication and inversion satisfying associativity, (x⁻¹)⁻¹=x, xx⁻¹x=x and xx⁻¹=x⁻¹x. Subalgebras are closed under both operations; finite quotients preserve both.

**Source.** Gerard Aidan O’Reilly. *Separability properties of semigroups and algebras*. University of St Andrews, 2021. Advisor(s): Nik Ruškuc, Martyn Quick. [primary source](https://research-repository.st-andrews.ac.uk/bitstream/handle/10023/29944/Thesis-Gerard-Aidan-O%27Reilly-complete-version.pdf?isAllowed=y&sequence=2) Location: Open Problem 2.6.13, p. 84; variety identities pp. 63–64.

**Literature check.** Status: This target remains asked. The rank-one free algebra is settled; the separate higher-rank monogenic-subalgebra problem remains unresolved.

**Notes.** Supporting sources:

**Further links.** [1](https://research-repository.st-andrews.ac.uk/handle/10023/29944)


<a id="q3403"></a>

## Q3403. Schützenberger subgroup separation

**Status:** Open · **Kind:** open problem (Problem 3.7) · **Collection** 35

If S is WSS, must Γ(H) be LERF for every H-class H?

**Context.** Origin: Doctoral-research paper, incorporated in the thesis. Setup: Write WSS for: every finitely generated subsemigroup T and s∉T are separated by a homomorphism φ to a finite semigroup, φ(s)∉φ(T). For S¹=S with identity adjoined if necessary, a H b means aS¹=bS¹ and S¹a=S¹b. Put Stab(H)={s∈S¹:Hs=H} and Γ(H)=Stab(H)/∼, where s∼t iff hs=ht for every h∈H. LERF means finitely generated subgroups are separable in finite group quotients.

**Source.** Craig Miller, Gerard O’Reilly, Martyn Quick, Nik Ruškuc. *On separability finiteness conditions in semigroups*. 2021. [primary source](https://doi.org/10.1017/S1446788721000124) Location: Open Problem 3.7, p. 412 (PDF p. 11).

**Literature check.** Status: Published text retains both problems; solvable maximal subgroups settle only a restricted second case.


<a id="q3404"></a>

## Q3404. Finitely many H-classes

**Status:** Open · **Kind:** open problem (Problem 6.6) · **Collection** 35

For S with finitely many H-classes, is S WSS exactly when every Γ(H) is WSS as a semigroup?

**Context.** Origin: Doctoral-research paper, incorporated in the thesis. Setup: Write WSS for: every finitely generated subsemigroup T and s∉T are separated by a homomorphism φ to a finite semigroup, φ(s)∉φ(T). For S¹=S with identity adjoined if necessary, a H b means aS¹=bS¹ and S¹a=S¹b. Put Stab(H)={s∈S¹:Hs=H} and Γ(H)=Stab(H)/∼, where s∼t iff hs=ht for every h∈H. LERF means finitely generated subgroups are separable in finite group quotients.

**Source.** Craig Miller, Gerard O’Reilly, Martyn Quick, Nik Ruškuc. *On separability finiteness conditions in semigroups*. 2021. [primary source](https://doi.org/10.1017/S1446788721000124) Location: Open Problem 6.6, p. 425 (PDF p. 24).

**Literature check.** Status: Published text retains both problems; solvable maximal subgroups settle only a restricted second case.

**Notes.** Supporting sources:

**Further links.** [1](https://research-repository.st-andrews.ac.uk/bitstream/10023/24053/1/Miller_2021_On_separability_finiteness_JAMS_CCBY.pdf) · [2](https://research-repository.st-andrews.ac.uk/handle/10023/29944) · [3](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/495E096D4B4312909F031D2C3F1F7AC3/S1446788721000124a.pdf/div-class-title-on-separability-finiteness-conditions-in-semigroups-div.pdf)


<a id="q3405"></a>

## Q3405. Must the product of two SSS semigroups be WSS?

**Status:** Open · **Kind:** open problem (Problem 3.10) · **Collection** 35

Must the product of two SSS semigroups be WSS?

**Context.** Doctoral context: O’Reilly, St Andrews PhD 2021, supervisors Ruškuc and Quick; thesis Chapter 4. Origin: joint doctoral-research paper. A nonempty semigroup is MSS/WSS/SSS if every point outside a one-generated/finitely generated/arbitrary subsemigroup is separated from it by a homomorphism to a finite semigroup. Products are componentwise.

**Source.** Gerard O’Reilly, Martyn Quick and Nik Ruškuc. *On separability properties in direct products of semigroups*. 2022. [primary source](https://doi.org/10.1007/s00605-021-01570-4) Location: Open Problem 3.10, p. 342.

**Literature check.** Status checked 9 October 2026: final publisher text retains all five questions; bounded later-source checks found no resolution. This does not establish absolute openness.


<a id="q3406"></a>

## Q3406. Characterize finite T such that S×T is WSS for every WSS semigroup S.

**Status:** Open · **Kind:** open problem (Problem 4.7) · **Collection** 35

Characterize finite T such that S×T is WSS for every WSS semigroup S.

**Context.** Doctoral context: O’Reilly, St Andrews PhD 2021, supervisors Ruškuc and Quick; thesis Chapter 4. Origin: joint doctoral-research paper. A nonempty semigroup is MSS/WSS/SSS if every point outside a one-generated/finitely generated/arbitrary subsemigroup is separated from it by a homomorphism to a finite semigroup. Products are componentwise.

**Source.** Gerard O’Reilly, Martyn Quick and Nik Ruškuc. *On separability properties in direct products of semigroups*. 2022. [primary source](https://doi.org/10.1007/s00605-021-01570-4) Location: Open Problem 4.7, p. 345.

**Literature check.** Status checked 9 October 2026: final publisher text retains all five questions; bounded later-source checks found no resolution. This does not establish absolute openness.


<a id="q3407"></a>

## Q3407. If S×T is WSS, must S or T be WSS?

**Status:** Open · **Kind:** open problem (Problem 4.9) · **Collection** 35

If S×T is WSS, must S or T be WSS?

**Context.** Doctoral context: O’Reilly, St Andrews PhD 2021, supervisors Ruškuc and Quick; thesis Chapter 4. Origin: joint doctoral-research paper. A nonempty semigroup is MSS/WSS/SSS if every point outside a one-generated/finitely generated/arbitrary subsemigroup is separated from it by a homomorphism to a finite semigroup. Products are componentwise.

**Source.** Gerard O’Reilly, Martyn Quick and Nik Ruškuc. *On separability properties in direct products of semigroups*. 2022. [primary source](https://doi.org/10.1007/s00605-021-01570-4) Location: Open Problem 4.9, p. 345.

**Literature check.** Status checked 9 October 2026: final publisher text retains all five questions; bounded later-source checks found no resolution. This does not establish absolute openness.


<a id="q3408"></a>

## Q3408. If S×T is MSS, must S or T be MSS?

**Status:** Open · **Kind:** open problem (Problem 5.16) · **Collection** 35

If S×T is MSS, must S or T be MSS?

**Context.** Doctoral context: O’Reilly, St Andrews PhD 2021, supervisors Ruškuc and Quick; thesis Chapter 4. Origin: joint doctoral-research paper. A nonempty semigroup is MSS/WSS/SSS if every point outside a one-generated/finitely generated/arbitrary subsemigroup is separated from it by a homomorphism to a finite semigroup. Products are componentwise.

**Source.** Gerard O’Reilly, Martyn Quick and Nik Ruškuc. *On separability properties in direct products of semigroups*. 2022. [primary source](https://doi.org/10.1007/s00605-021-01570-4) Location: Open Problem 5.16, p. 352.

**Literature check.** Status checked 9 October 2026: final publisher text retains all five questions; bounded later-source checks found no resolution. This does not establish absolute openness.


<a id="q3409"></a>

## Q3409. Characterize pairs of MSS semigroups whose product is MSS.

**Status:** Open · **Kind:** open problem (Problem 5.15) · **Collection** 35

Characterize pairs of MSS semigroups whose product is MSS.

**Context.** Doctoral context: O’Reilly, St Andrews PhD 2021, supervisors Ruškuc and Quick; thesis Chapter 4. Origin: joint doctoral-research paper. A nonempty semigroup is MSS/WSS/SSS if every point outside a one-generated/finitely generated/arbitrary subsemigroup is separated from it by a homomorphism to a finite semigroup. Products are componentwise.

**Source.** Gerard O’Reilly, Martyn Quick and Nik Ruškuc. *On separability properties in direct products of semigroups*. 2022. [primary source](https://doi.org/10.1007/s00605-021-01570-4) Location: Open Problem 5.15, p. 352.

**Literature check.** Status checked 9 October 2026: final publisher text retains all five questions; bounded later-source checks found no resolution. This does not establish absolute openness.


<a id="q3445"></a>

## Q3445. Boundary-transitive tree groups are CCR

**Status:** Open · **Kind:** open problem · **Collection** 35

Must every closed subgroup G≤Aut(T) acting 2-transitively on ∂T be CCR?

**Context.** Setup: Let T be a locally finite tree whose vertices have degree at least 3; ∂T is its space of ends. Give Aut(T) the topology of pointwise convergence on vertices. A locally compact group G is CCR if π(f)=∫G f(g)π(g)dg is compact for every irreducible strongly continuous unitary representation π on a complex Hilbert space and every f∈L¹(G), using left Haar measure.

**Source.** Lancelot Semal. *Irreducibly represented Lie groups and Nebbia’s CCR conjecture on trees*. Université catholique de Louvain, 2023. Advisor(s): Pierre-Emmanuel Caprace. [primary source](https://arxiv.org/pdf/2306.04310v1) Location: Introduction, Nebbia’s conjecture, p. 6; Chapter 6, p. 191.

**Literature check.** Status checked 9 October 2026: Thesis solves Radu-group cases. Later published companion retains the general gap; no subsequent resolution located through 2026-10-09.

**Notes.** Origin: Nebbia 1999 conjecture; doctoral restatement and partial resolution. September status: https://arxiv.org/pdf/2609.17052v1, p. 2.

**Further links.** [1](https://arxiv.org/pdf/2609.17052v1)


<a id="q3448"></a>

## Q3448. Non-split quaternion coordinatization

**Status:** Open · **Kind:** open problem · **Collection** 35

Classify unital alternative F-algebras A equipped with a unital embedding ι:H→A, up to F-algebra isomorphisms commuting with ι.

**Context.** Doctoral context: Victor Hugo López Solís, Universidade de São Paulo PhD 2017; advisors Ivan Chestakov. Thesis: O problema de Nathan Jacobson e questões relacionadas. Setup: Fix a field F and a quaternion division F-algebra H (a central division algebra of F-dimension 4). An F-algebra A is alternative if x²y=x(xy) and (yx)x=yx² for all x,y∈A. No finite-dimensionality assumption is imposed on A.

**Source.** Victor Hugo López Solís and Ivan P. Shestakov. *On a problem by Nathan Jacobson*. 2022. [primary source](https://ems.press/content/serial-article-files/39052) Location: §7(1), p. 1237; introduction, pp. 1219–1220.

**Literature check.** Status checked 9 October 2026: The split case is settled. The later Grishkov–Shestakov construction covers M₂(F), including the free-algebra target; no non-split resolution located through 2026-10-09.

**Notes.** Origin: Remaining non-split case of Jacobson’s 1954 problem; doctoral research.


<a id="q3501"></a>

## Q3501. Must ell(M)>=gll(R) for every nonzero R-module M of finite projective dimension?

**Status:** Open · **Kind:** open problem · **Collection** 36

Must ell(M)>=gll(R) for every nonzero R-module M of finite projective dimension?

**Context.** For Noetherian local (R,m,k=R/m), put ell(M)=inf{n>=0:m^nM=0} (inf empty=infinity) and gll(R)=min_Q ell(R/Q), over parameter ideals.

**Source.** Nawaj KC. *Modules of Finite Projective Dimension and Singularities*. Nebraska–Lincoln, 2025. [primary source](https://arxiv.org/abs/2404.18368) · [dissertation](https://digitalcommons.unl.edu/dissunl/308) Location: Modules of Finite Projective Dimension and Singularities. Follow-through to KC–Pollitz’s Loewy-length paper. Final-labelled arXiv:2404.18368v3, Conjectures A/3.1, pp. 2/10; DOI 10.1016/j.aim.2025.110309. No general resolution located.

**Literature check.** Status: No general resolution located.


<a id="q3502"></a>

## Q3502. Must gll(R)<=gll(S) for every flat local map of Cohen–Macaulay rings with infinite residue fields?

**Status:** Open · **Kind:** open problem · **Collection** 36

Must gll(R)<=gll(S) for every flat local map of Cohen–Macaulay rings with infinite residue fields?

**Context.** For Noetherian local (R,m,k=R/m), put ell(M)=inf{n>=0:m^nM=0} (inf empty=infinity) and gll(R)=min_Q ell(R/Q), over parameter ideals.

**Source.** Nawaj KC. *Modules of Finite Projective Dimension and Singularities*. Nebraska–Lincoln, 2025. [primary source](https://arxiv.org/abs/2404.18368) · [dissertation](https://digitalcommons.unl.edu/dissunl/308) Location: Modules of Finite Projective Dimension and Singularities. Follow-through to KC–Pollitz’s Loewy-length paper. Final-labelled arXiv:2404.18368v3, Conjectures A/3.1, pp. 2/10; DOI 10.1016/j.aim.2025.110309. No general resolution located.

**Literature check.** Status: No general resolution located.


<a id="q3503"></a>

## Q3503. Let A range over finite-dimensional algebras over an algebraically closed field whose…

**Status:** Open · **Kind:** open problem (Question 4.30) · **Collection** 36

Let A range over finite-dimensional algebras over an algebraically closed field whose indecomposable projective left modules are uniserial. For finite right B-modules X, define dell_B(X)=min{n>=0:Omega^n X is a stable direct summand of Omega^{n+1}Y for some finite Y}; stable means modulo projectives, and min(empty)=infinity. Put dell(B)=max_{X simple}dell_B(X). Let Findim(A) be the supremum of finite projective dimensions of all right A-modules. Is dell(A^op)-Findim(A) unbounded?

**Source.** Ruoyu Guo. *Developments in the finitistic dimension conjecture*. Brandeis, 2025. [primary source](https://arxiv.org/abs/2506.02307) · [dissertation](https://scholarworks.brandeis.edu/esploro/outputs/doctoral/Developments-in-the-finitistic-dimension-conjecture/9924505434301921) Location: Developments in the finitistic dimension conjecture, Question 4.30, p. 96. Later exact reaffirmation: Homological Invariants of Left and Right Serial Quiver Algebras, arXiv:2506.02307v2, 8 August 2026, Question 4.9, p. 14. No later resolution located.

**Literature check.** Status: No later resolution located.

**Notes.** Later exact reaffirmation: Homological Invariants of Left and Right Serial Quiver Algebras, arXiv:2506.02307v2, 8 August 2026, Question 4.9, p. 14.


<a id="q3504"></a>

## Q3504. Must each probabilistic identity w admit an open subgroup H<=G and a_1,...,a_d in G such that…

**Status:** Open · **Kind:** open problem · **Collection** 36

Must each probabilistic identity w admit an open subgroup H<=G and a_1,...,a_d in G such that w(a_1h_1,...,a_dh_d)=1 for every tuple from H?

**Context.** Let mu be normalized Haar measure on a profinite group G. A probabilistic identity is a nontrivial reduced word w in d variables with mu^d{g in G^d:w(g)=1}>0.

**Source.** Tommaso Toti. *Probabilistic identities in profinite groups*. joint Milano–Bicocca/Pavia/INdAM–UPV/EHU, 2025. Advisor(s): Thomas Weigel and Gustavo Adolfo Fernández-Alcober. [primary source](https://iris.unipv.it/retrieve/33bb0292-fb63-4848-9aa8-ab3d8481bb6e/Thesis%20Final%20pdf-A.pdf) Location: Probabilistic identities in profinite groups, Questions 2.1/2.3, pp. 49/53. These develop earlier identity questions, including Larsen–Shalev's. Inspected 2026 follow-ups establish special cases, not the general assertions.

**Literature check.** Status: Inspected 2026 follow-ups establish special cases, not the general assertions.


<a id="q3505"></a>

## Q3505. If G is topologically finitely generated and has a probabilistic identity, must some nontrivial…

**Status:** Open · **Kind:** open problem · **Collection** 36

If G is topologically finitely generated and has a probabilistic identity, must some nontrivial word v, possibly different from w, vanish on every tuple from G?

**Context.** Let mu be normalized Haar measure on a profinite group G. A probabilistic identity is a nontrivial reduced word w in d variables with mu^d{g in G^d:w(g)=1}>0.

**Source.** Tommaso Toti. *Probabilistic identities in profinite groups*. joint Milano–Bicocca/Pavia/INdAM–UPV/EHU, 2025. Advisor(s): Thomas Weigel and Gustavo Adolfo Fernández-Alcober. [primary source](https://iris.unipv.it/retrieve/33bb0292-fb63-4848-9aa8-ab3d8481bb6e/Thesis%20Final%20pdf-A.pdf) Location: Probabilistic identities in profinite groups, Questions 2.1/2.3, pp. 49/53. These develop earlier identity questions, including Larsen–Shalev's. Inspected 2026 follow-ups establish special cases, not the general assertions.

**Literature check.** Status: Inspected 2026 follow-ups establish special cases, not the general assertions.


<a id="q3506"></a>

## Q3506. Let k be a field and R subseteq S commutative k-algebras, with an R-linear retraction S->R.…

**Status:** Open · **Kind:** conjecture (Conjecture 1.2) · **Collection** 36

Let k be a field and R subseteq S commutative k-algebras, with an R-linear retraction S->R. Write D_k(T) for the ring of k-linear Grothendieck differential operators on T. If D_k(S) has no nonzero proper two-sided ideal, must D_k(R) also have none?

**Source.** Taylor Jeffrey Murray. *Bass Numbers of Veronese Submodules and Lifting the Frobenius Trace*. Nebraska–Lincoln, 2026. [primary source](https://arxiv.org/abs/math/0209275) · [dissertation](https://digitalcommons.unl.edu/dissunl/449) Location: Bass Numbers of Veronese Submodules and Lifting the Frobenius Trace, §5.1, p. 90. Restates Smith–Van den Bergh's 1997 Conjecture 1.2; 2002 author posting inspected, with exact 2026 reaffirmation. No general resolution located.

**Literature check.** Status: Restates Smith–Van den Bergh's 1997 Conjecture 1.2; 2002 author posting inspected, with exact 2026 reaffirmation.

**Literature check.** Status: No general resolution located.


<a id="q3507"></a>

## Q3507. For a Noetherian Gorenstein local ring (R,m) with infinite residue field, set…

**Status:** Open · **Kind:** open problem (Question 4.5) · **Collection** 36

For a Noetherian Gorenstein local ring (R,m) with infinite residue field, set gll(R)=min{n>=1:m^n subseteq Q for a parameter ideal Q}. Must some parameter ideal Q simultaneously satisfy m^{gll(R)} subseteq Q and Qm^r=m^{r+1} for an integer r>=0?

**Source.** Alessandro De Stefani. *A counterexample to a conjecture of Ding*. Syracuse, 2015. [primary source](https://arxiv.org/abs/1506.09168) · [dissertation](https://surface.syr.edu/etd/1922/) Location: Numerical invariants of Cohen-Macaulay local and graded rings, p. 37, leads to De Stefani's referee-suggested Question 4.5(ii), A counterexample to a conjecture of Ding, arXiv:1506.09168v2, p. 9. Exactly reaffirmed in 2025.

**Literature check.** Status: Exactly reaffirmed in 2025.


<a id="q3508"></a>

## Q3508. For finite transitive G<=Sym(Omega), join x,y in G when xy^{-1} fixes no point of Omega. Is…

**Status:** Open · **Kind:** conjecture (Conjecture 1) · **Collection** 36

For finite transitive G<=Sym(Omega), join x,y in G when xy^{-1} fixes no point of Omega. Is there a function F:N->N such that |Omega|<=F(k) whenever this graph has no k-clique?

**Source.** Marco Fusari. *Derangements and Normal Coverings*. joint Milano–Bicocca/Pavia/INdAM, 2025. [primary source](https://arxiv.org/abs/2601.20500) · [dissertation](https://iris.unipv.it/handle/11571/1539217) Location: Derangements and Normal Coverings, Conjecture 1, p. 6. Earlier Meagher–Razafimahatratra–Spiga question; reaffirmed by Anzanello–Spiga, arXiv:2601.20500v2, Conjecture 1.1, p. 2. September 2026 primary work gives further partial results.

**Literature check.** Status: Earlier Meagher–Razafimahatratra–Spiga question; reaffirmed by Anzanello–Spiga, arXiv:2601.20500v2, Conjecture 1.1, p. 2.


<a id="q3512"></a>

## Q3512. Let char(k)=p, G=(C_p)^n, q=p^n, and W be a faithful indecomposable two-dimensional kG-module.…

**Status:** Open · **Kind:** conjecture (Conjecture 6.1) · **Collection** 36

Let char(k)=p, G=(C_p)^n, q=p^n, and W be a faithful indecomposable two-dimensional kG-module. Put V_i=(Sym^{i-1}W)^\* and M=V_p direct-sum V_{2p} direct-sum ... direct-sum V_q. Write X~\_M Y if X,Y become isomorphic after adding direct summands of M tensor_k Z, with Z finite-dimensional. Suppose 1<=i,j&lt;q, i+j<=q, i=rp+i', j=sp+j', 0<=i',j'&lt;p, and i'+j'<=p. Is V_i tensor_k V_j ~\_M direct-sum_{l=1}^{min(i',j')}V_{i+j-(2l-1)}?

**Source.** Kazal Majid Kadr. *Formulae for symmetric powers and tensor products of modular representations of elementary abelian p-groups*. Middlesex, 2025. [primary source](https://doi.org/10.1007/s13366-026-00855-9) · [dissertation](https://repository.mdx.ac.uk/item/367y11) Location: Formulae for symmetric powers and tensor products of modular representations of elementary abelian p-groups, Conjecture 6.1(a), p. 70. Elmer–Kadr's publisher-final June 2026 paper retains Conjecture 3.7(a), PDF p. 17; its corrected notation controls.

**Literature check.** Status: Elmer–Kadr's publisher-final June 2026 paper retains Conjecture 3.7(a), PDF p. 17; its corrected notation controls.


<a id="q3513"></a>

## Q3513. Let N=(F_3^2 semidirect Q_8) times C_2, with Q_8<=SL_2(F_3) acting naturally;…

**Status:** Open · **Kind:** open problem (Problem 20) · **Collection** 36

Let N=(F_3^2 semidirect Q_8) times C_2, with Q_8<=SL_2(F_3) acting naturally; N=SmallGroup(144,187). For every finite group G containing N as a normal subgroup and every subgroup N<=H<=G with gcd(|N|,[G:H])=1, does a complement of N in H imply a complement in G? A complement K in a group J means J=NK and N intersect K=1.

**Source.** Benjamin Sambale. *On the converse of Gaschütz’s complement theorem*. 2023. [primary source](https://www.iazd.uni-hannover.de/fileadmin/iazd/sambale/pdfs/GaConverse.pdf) Location: Following Obeidi's earlier master's research with Benjamin Sambale: his On the converse of Gaschütz's complement theorem, June 2023 author revision, Problem 20, p. 11. This revision postdates journal online publication and explicitly retains the problem; no later resolution located.

**Literature check.** Status: This revision postdates journal online publication and explicitly retains the problem; no later resolution located.


<a id="q3514"></a>

## Q3514. Let (R,m,k) be commutative Noetherian local and E the injective hull of k. For finite M, put…

**Status:** Open · **Kind:** open problem (Question 1.3) · **Collection** 36

Let (R,m,k) be commutative Noetherian local and E the injective hull of k. For finite M, put M^vee=Hom_R(M,E) and W(M)=image[Tor_\*^R(k,M) tensor_k Tor_\*^R(k,M^vee)->Tor_\*^R(k,E)], using evaluation. Must some uniform n>=0 satisfy W(Omega^n M)=0 for every finite M, where Omega denotes minimal syzygy?

**Source.** Iyengar, Maitra and Tribone. *Unstable elements in cohomology and a question of Lescot*. Syracuse, 2025. [primary source](https://arxiv.org/abs/2507.23213) · [dissertation](https://surface.syr.edu/etd/1436/) Location: Matrix Factorizations With More Than Two Factors. Subsequent-paper route to Iyengar–Maitra–Tribone, Unstable elements in cohomology and a question of Lescot, arXiv:2507.23213v1, Question 1.3, p. 3. March 2026 publisher-final abstract exactly reaffirms finiteness of Lescot's invariant; full final was not inspected.

**Literature check.** Status: March 2026 publisher-final abstract exactly reaffirms finiteness of Lescot's invariant; full final was not inspected.

**Further links.** [1](https://doi.org/10.1007/s00209-026-03978-w)


<a id="q3515"></a>

## Q3515. Let R be commutative Noetherian local and M,N nonzero finitely generated R-modules, both of…

**Status:** Open · **Kind:** open problem (Question 3) · **Collection** 36

Let R be commutative Noetherian local and M,N nonzero finitely generated R-modules, both of finite projective dimension. If M tensor_R N has finite length, must dim M+dim N<=dim R?

**Source.** Linquan Ma. *Counterexamples to Peskine–Szpiro’s conjecture on modules of finite projective dimension*. 2026. [primary source](https://arxiv.org/abs/2608.24018) Location: KC's dissertation and advisor Mark Walker's collaborations led to Linquan Ma's Counterexamples to Peskine–Szpiro's conjecture on modules of finite projective dimension, arXiv:2608.24018v1, 25 August 2026. Question 3, p. 3, explicitly retains this case after disproving the unrestricted conjecture. No later resolution located.

**Literature check.** Status: Question 3, p. 3, explicitly retains this case after disproving the unrestricted conjecture.

**Literature check.** Status: No later resolution located.


<a id="q3516"></a>

## Q3516. For every commutative Noetherian local (R,m) and nonzero finite-length R-module M of finite…

**Status:** Open · **Kind:** conjecture (Conjecture 2.3.11) · **Collection** 36

For every commutative Noetherian local (R,m) and nonzero finite-length R-module M of finite projective dimension, must length_R(M)>=e_m(R), the Hilbert–Samuel multiplicity of R?

**Source.** Iyengar, Ma and Walker. *Multiplicities and Betti numbers in local algebra via lim Ulrich points*. 2022. [primary source](https://arxiv.org/abs/2104.10140) Location: KC's dissertation, Conjecture 2.3.11, pp. 24–25, restates the conjecture of Iyengar–Ma–Walker. Multiplicities and Betti numbers in local algebra via lim Ulrich points, to-appear manuscript arXiv:2104.10140v2, Conjecture 1, p. 2; ANT 16 (2022), 1213–1257. Exact 2025 thesis reaffirmation; no general resolution located.

**Literature check.** Status: Exact 2025 thesis reaffirmation; no general resolution located.


<a id="q3517"></a>

## Q3517. For every prime p, does a function f_p on integers b>1 coprime to p exist such that every finite…

**Status:** Open · **Kind:** conjecture (Conjecture 1.6) · **Collection** 36

For every prime p, does a function f_p on integers b>1 coprime to p exist such that every finite transitive permutation group of degree p^a b with a>f_p(b) contains a fixed-point-free element of p-power order?

**Source.** Liu and Gan. *The order of quasiprimitive permutation groups and the Isbell conjecture*. 2026. [primary source](https://doi.org/10.1360/SSM-2026-0094) Location: Fusari’s dissertation, Conjecture 1.6, p. 17, restates generalized Isbell. Latest exact reaffirmation: Liu–Gan, The order of quasiprimitive permutation groups and the Isbell conjecture, publisher-final, 1 July 2026, Conjecture 1.1, p. 2. The paper proves the p=2 quasiprimitive case, leaving the general conjecture.

**Notes.** Latest exact reaffirmation: Liu–Gan, The order of quasiprimitive permutation groups and the Isbell conjecture, publisher-final, 1 July 2026, Conjecture 1.1, p. 2.


<a id="q3602"></a>

## Q3602. Symmetric rings with non-NR power series

**Status:** Open · **Kind:** open problem · **Collection** 37

Does an associative unital ring R exist such that abc=0 implies acb=0 for every a,b,c in R, but the set {f in R[[x]]: f^m=0 for some integer m>=1} is not a possibly nonunital subring of R[[x]]? The indeterminate x is central.

**Source.** Nolan Ison. *Power Series Rings over Noncommutative Rings: Symmetry, Reversibility, and Semicommutativity*. Brigham Young University, 2025. [primary source](https://scholarsarchive.byu.edu/etd/10816/) Location: Section 1.2, printed pp.4–5; definitions in Section 1.1

**Literature check.** Status: No later full resolution located, 9 October 2026.


<a id="q3606"></a>

## Q3606. Embedding quadratic Lie algebras into Koszul ones

**Status:** Open · **Kind:** open problem (Question 2.19) · **Collection** 37

Must every quadratic Lie algebra of finite cohomological dimension embed in a Koszul Lie algebra?

**Context.** Setup: Work over a field k of characteristic !=2 with positively graded Lie algebras finitely generated in degree one. Quadratic means having quadratic relations; Koszul means Ext^{i,j}\_{U(L)}(k,k)=0 for i!=j.

**Source.** Simone Blumer. *Koszul Lie algebras and their subalgebras*. 2026. [primary source](https://www.boa.unimib.it/retrieve/404582f4-d4eb-46a4-b395-e474a7d568ed/Blumer-2026-Journal%20of%20Algebra-VoR.pdf) Location: Question 2.19, p.19

**Literature check.** Status: No later full resolution located, 9 October 2026.


<a id="q3607"></a>

## Q3607. Separativity for exchange rings

**Status:** Open · **Kind:** open problem · **Collection** 37

For exchange R and finitely generated projective right modules P,Q, must P⊕P≅P⊕Q≅Q⊕Q imply P≅Q?

**Context.** Setup: A unital ring R is exchange if every a admits idempotent e∈aR with 1−e∈(1−a)R. V(R) denotes finitely generated projective right-module classes under ⊕.

**Source.** Ara, Goodearl, Nielsen, O’Meara, Pardo and Perera. *Levels of cancellation for monoids and modules*. 2026. [primary source](https://mathdept.byu.edu/~pace/levels-of-cancellation-for-monoids-and-modules.pdf) Location: Problems 8.4, p.174; equation (8-1)

**Literature check.** Status: No later full resolution located, 9 October 2026.


<a id="q3608"></a>

## Q3608. Realizing countable refinement monoids

**Status:** Open · **Kind:** open problem · **Collection** 37

Is every countable conical refinement commutative monoid with an order-unit isomorphic to V(R) for a unital exchange R? Conical means a+b=0⇒a=b=0; refinement means each a_1+a_2=b_1+b_2 admits c_ij with those row/column sums; order-unit u means every a satisfies a+b=nu for some b,n>=1.

**Context.** Setup: A unital ring R is exchange if every a admits idempotent e∈aR with 1−e∈(1−a)R. V(R) denotes finitely generated projective right-module classes under ⊕.

**Source.** Ara, Goodearl, Nielsen, O’Meara, Pardo and Perera. *Levels of cancellation for monoids and modules*. 2026. [primary source](https://mathdept.byu.edu/~pace/levels-of-cancellation-for-monoids-and-modules.pdf) Location: Problems 8.4, p.174

**Literature check.** Status: No later full resolution located, 9 October 2026.


<a id="q3611"></a>

## Q3611. Three-variable power-sum complete intersections

**Status:** Open · **Kind:** conjecture (Conjecture 1.3) · **Collection** 37

For n=3, 0&lt;a&lt;b&lt;c and gcd(a,b,c)=1, is the common zero locus of p_a,p_b,p_c just {0} iff 6|abc?

**Context.** Setup: For integers n,a≥1, set p_a=sum_{j=1}^n x_j^a in C[x_1,...,x_n].

**Source.** Conca, Singh and Soundararajan. *Ideals generated by power sums*. 2025. [primary source](https://imar.ro/journals/Revue_Mathematique/pdfs/2025/1-2/5.pdf) Location: Conjecture 1.3, p.50

**Literature check.** Status: No later full resolution located, 9 October 2026. Q3611 is reaffirmed in https://arxiv.org/html/2609.07932v1, Section 1.

**Further links.** [1](https://arxiv.org/html/2609.07932v1)


<a id="q3612"></a>

## Q3612. Four-variable power-sum complete intersections

**Status:** Open · **Kind:** conjecture (Conjecture 1.4) · **Collection** 37

For n=4 and A={a_1&lt;a_2&lt;a_3&lt;a_4} with gcd(A)=1, is the common zero locus of {p_a:a∈A} just {0} iff 24|product_i a_i, {v_2(a_i)} contains two distinct positive values, and A contains no {d,2d,5d} with integer d≥1? Here v_2 is the 2-adic valuation.

**Context.** Setup: For integers n,a≥1, set p_a=sum_{j=1}^n x_j^a in C[x_1,...,x_n].

**Source.** Conca, Singh and Soundararajan. *Ideals generated by power sums*. 2025. [primary source](https://imar.ro/journals/Revue_Mathematique/pdfs/2025/1-2/5.pdf) Location: Conjecture 1.4, p.51

**Literature check.** Status: No later full resolution located, 9 October 2026. Q3611 is reaffirmed in https://arxiv.org/html/2609.07932v1, Section 1.

**Further links.** [1](https://arxiv.org/html/2609.07932v1)


<a id="q3614"></a>

## Q3614. Zassenhaus algebras with mixed 2-adic labels

**Status:** Open · **Kind:** open problem (Question 9.3) · **Collection** 37

Let p be prime and Gamma a finite mixed graph without directed cycles; edges are plain or arrows, with arrow labels ell(a) in 1+pZ_p. Let G be the pro-p group with vertex generators and relations [v,u]=1 on plain edges and u^v=u^{ell(u,v)} on arrows, where u^v=v^{-1}uv. Let D_j={g:g-1 lies in omega^j} for the augmentation ideal omega of F_p[[G]]. Is direct_sum_{j>=1} D_j/D_{j+1} isomorphic to the graded restricted F_p-Lie algebra on degree-one vertex generators with defining relations [v,u]=u^[2] precisely on arrows u->v with p=2 and v_2(ell(u,v)-1)=1, and [v,u]=0 on every other edge?

**Source.** Leoni, Martínez-Pérez and Weigel. *Generalising a Theorem of Lichtman*. 2026. [primary source](https://arxiv.org/abs/2606.27528) Location: Question 9.3, pp.21–22; equations (9.1),(9.2)

**Literature check.** Status: No later full resolution located, 9 October 2026.


<a id="q3616"></a>

## Q3616. Grassmannian prefixes of reflections

**Status:** Open · **Kind:** open problem (Problem 2) · **Collection** 37

For a finite-rank Coxeter system (W,S), let length be word length in S and T={wsw^{-1}:w in W,s in S}. Characterize the elements u with exactly one right descent, meaning exactly one s in S satisfies length(us)&lt;length(u), for which there is a reflection t of length 2\*length(u)-1 having a reduced word beginning with a reduced word for u.

**Source.** Elisa Sasso. *Diagram calculus for affine Coxeter systems and properties of their associated root systems*. University of Bologna, 2026. [primary source](https://arxiv.org/abs/2602.16361) Location: Section 5, Problem 2, p.30; Proposition 3.1

**Literature check.** Status: No later full resolution located, 9 October 2026.


<a id="q3617"></a>

## Q3617. Realizability of strongly Koszul masks

**Status:** Solved here: disproved · **Kind:** open problem (Question 2.16) · **Collection** 37

Fix a field F, n>=1, put [n]={1,...,n}, and E={(A,k):A subset [n],k notin A}. Suppose M:E->2^[n] satisfies: A subset M(A,k); A subset B and k notin B imply M(A,k) subset M(B,k); j in M(A,k) iff k in M(A,j) for j,k notin A; and M(M(A,k),j)=M(M(A,j),k) whenever j notin M(A,k). Suppose functions F_A in Z[[z]] exist with F_[n]=1 and F_A=F_{A union {k}}+z F_{M(A,k)}. Must some standard graded commutative F-algebra R with F-basis x_1,...,x_n of R_1 satisfy (x_i:i in A):x_j=(x_i:i in M(A,j)) for every (A,j) in E?

**Source.** Luca Fiorindo. *Perazzo algebras, strongly Koszulness, Arithmetic Complexes, and Vasconcelos invariant*. University of Genova, 2026. Advisor(s): Aldo Conca. [primary source](https://unige.iris.cineca.it/retrieve/9b01309f-fa18-40af-87dd-aae58f1137f2/phdunige_5530713.pdf) Location: Definition 2.13 and Question 2.16, pp.44–45

**Literature check.** Status: No later full resolution located, 9 October 2026.

**Results.**

- **Disproved**: No. On n = 3 the mask with M(∅,k) = ∅; M({1},2) = {1,2}, M({1},3) = {1,3}; M({2},1) = M({3},1) = {2,3}, M({2},3) = {1,2}, M({3},2) = {1,3}; and M(A,k) = [3] for |A| = 2 satisfies every listed condition, with F_∅ = (1+z)²/(1−z). No algebra realizes it over any field: the forced Hilbert series leaves a two-dimensional space of quadric relations, the colon conditions remove x² from all of them, and M({2,3},1) = [3] needs x² ∈ (y,z). The catalog wording matches Definition 2.13 and Question 2.16 of the source; its follow-up (which properties to add) is not addressed. Reconstructed checkpoint without its original checkers; re-derived here by hand and spot-checked with independent exact computations on 10 October 2026. Not external peer review or a novelty certification. Filed from the public-repo research round seven-problems-2026-10-10. [Details](../../solutions/seven-problems-2026-10-10/Q3617.md).


<a id="q3645"></a>

## Q3645. Regular mixed groups without a specific lattice

**Status:** Open · **Kind:** open problem (Question 2) · **Collection** 37

Does a regular mixed lattice group exist for which ≼ is not a lattice order?

**Context.** Doctoral route: Mixed Lattice Structures; Tampere University; 2024 Advisors: Lassi Paunonen Setup: A mixed lattice group is an Abelian group with translation-invariant partial orders ≤,≼ for which x∧ₘy=max≤{z:z≼x,z≤y} and x∨ₘy=min≤{z:x≼z,y≤z} exist. It is regular if C={x:0≼x} is closed under both mixed operations and G=C−C. Origin: Dissertation Conclusions Question 2.

**Source.** Jani Jokela. *Mixed Lattice Structures*. Tampere University, 2024. Advisor(s): Lassi Paunonen. [primary source](https://trepo.tuni.fi/bitstream/10024/155949/2/978-952-03-3407-9.pdf) Location: Conclusions Question 2, p.38; definitions pp.20–24.

**Literature check.** Status: The 2026 final mixed-order paper’s discrete and irregular examples do not settle the regular case.


<a id="q3653"></a>

## Q3653. For a commutative monoid Π, let P(Π) be its multiplication-compatible total preorders, with the…

**Status:** Open · **Kind:** open problem · **Collection** 37

For a commutative monoid Π, let P(Π) be its multiplication-compatible total preorders, with the coarsest topology making {≼:u≺v} closed for every u,v∈Π. Characterize Π for which every closed point of P(Π) is antisymmetric. Here u≺v means u≼v but not v≼u; a closed point has closed singleton. Compatibility means monotonicity under multiplication.

**Source.** Draisma, Metcalfe and Santschi. *The space of preorders on a commutative monoid*. 2026. [primary source](https://arxiv.org/abs/2607.07473) Location: §7, p.40.

**Literature check.** Status: Latest version and later-result searches checked October 9, 2026; no resolution located.


<a id="q3701"></a>

## Q3701. Left tensor-nilpotence and cones

**Status:** Open · **Kind:** open problem · **Collection** 38

Does there exist an essentially small monoidal triangulated category K and a morphism f:x→y such that the full subcategory N_f={z∈K: f^{⊗n}⊗id_z=0 for some integer n≥1} is not triangulated?

**Source.** Sam K. Miller. *On functoriality and the tensor product property in noncommutative tensor-triangular geometry*. 2025. [primary source](https://arxiv.org/abs/2505.01899v3) Location: Remark 10.2, p.25.

**Literature check.** Status: Current v3 inspected; no later resolution located, 9 October 2026.

**Further links.** [1](https://escholarship.org/content/qt9h73j2g4/qt9h73j2g4.pdf)


<a id="q3706"></a>

## Q3706. Quadratic filtrations of Koszul Lie algebras

**Status:** Open · **Kind:** open problem (Question 3.24) · **Collection** 38

Work over a field k with char(k)!=2. A quadratic Lie algebra is positively graded, generated by finitely many degree-one elements with degree-two defining relations. Call it Koszul if Ext^{i,j}\_{U(L)}(k,k)=0 for i!=j, where j is internal degree. Must every Koszul L have a chain L=L_0 ⊃ L_1 ⊃ ... ⊃ L_d=0 in which each L_i is quadratic, generated by its degree-one part, and dim_k (L_i)\_1=dim_k (L_{i+1})\_1+1?

**Source.** Simone Blumer. *Koszul Lie algebras and their subalgebras*. 2026. [primary source](https://www.boa.unimib.it/retrieve/404582f4-d4eb-46a4-b395-e474a7d568ed/Blumer-2026-Journal%20of%20Algebra-VoR.pdf) Location: Question 3.24, p.31; filtration definition p.8

**Literature check.** Status: Final re-inspected; no later resolution located, 9 October 2026.

**Further links.** [1](https://zaguan.unizar.es/record/136232/files/TESIS-2024-335.pdf)


<a id="q3707"></a>

## Q3707. Prime ideals generated by power sums

**Status:** Open · **Kind:** open problem (Question 2.1) · **Collection** 38

For n>=1 and a finite nonempty set A of distinct positive integers, classify the pairs (n,A) for which (sum_{j=1}^n x_j^a : a in A) is a prime ideal of C[x_1,...,x_n].

**Source.** Conca, Singh and Soundararajan. *Ideals generated by power sums*. 2025. [primary source](https://imar.ro/journals/Revue_Mathematique/pdfs/2025/1-2/5.pdf) Location: Question 2.1(5), p.51

**Literature check.** Status: Final re-inspected; no later resolution located, 9 October 2026.

**Further links.** [1](https://unige.iris.cineca.it/retrieve/9b01309f-fa18-40af-87dd-aae58f1137f2/phdunige_5530713.pdf) · [2](https://sites.google.com/view/fiorindo)


<a id="q3708"></a>

## Q3708. Positivity of the local conjugating function

**Status:** Open · **Kind:** conjecture (Conjecture 3.5) · **Collection** 38

For a finite group G and any set π of primes, write C_G(g)={h∈G:hg=gh} and define Π\_{π,G}(g)=|C_G(g)| when every prime divisor of the order of g lies in π, and Π\_{π,G}(g)=0 otherwise. Is Π\_{π,G} always the character of a finite-dimensional complex representation of G?

**Context.** Genealogy: Invariants of finite groups, Binghamton PhD 2026, advisor Hung P. Tong-Viet; later-paper conjecture addressing a related question of Robinson. https://arxiv.org/abs/2609.26464v1

**Source.** Christopher A. Schroeder. *Refining invariants of finite groups with class functions*. 2026. [primary source](https://arxiv.org/abs/2609.26464v1) Location: Example 2.6, p.4; Conjecture 3.5, p.7

**Literature check.** Status: Explicit conjecture in the current version; π-separable groups and π=p′ are proved.

**Further links.** [1](https://wiki.mathmig.binghamton.edu/doku.php?id=news:2026:0907_chris_schroeder)


<a id="q3709"></a>

## Q3709. Submultiplicativity of finite-group quantum invariants

**Status:** Solved here: proved · **Kind:** open problem · **Collection** 38

For a finite group H and an integer h≥1 put q_h(H)=|H|^{-1}∑\_{χ∈Irr(H)}χ(1)^{2−2h}, where Irr(H) is the set of irreducible complex characters. For every finite group G, normal subgroup N, and h≥1, must q_h(G)≤q_h(N)q_h(G/N)?

**Context.** Genealogy: Schroeder’s Binghamton PhD 2026, Invariants of finite groups, advisor Tong-Viet; question taken from their final paper. https://msp.org/pjm/2026/344-1/pjm-v344-n1-p07-s.pdf

**Source.** Christopher A. Schroeder and Hung P. Tong-Viet. *On the invariants of finite groups arising in a topological quantum field theory*. 2026. [primary source](https://msp.org/pjm/2026/344-1/pjm-v344-n1-p07-s.pdf) Location: definition p.152, Remark 1.8, p.155

**Literature check.** Status: Final source retains the unresolved inequality; h=1 is known.

**Results.**

- **Proved**: Yes for every integer genus h ≥ 1. Counting products of h commutators shows that each central-character sector has degree sum at most that of the quotient by the centre, so projective degree sums are at most ordinary ones; with an index bound for subgroups and Clifford theory this gives ζ(G) ≤ ζ(N)ζ(G/N) for ζ = Σ χ(1)^(2−2h). Limits: no claim for non-integer exponents. Reconstructed checkpoint without its original checkers; re-derived here by hand and spot-checked with independent exact computations on 10 October 2026. Not external peer review or a novelty certification. Filed from the public-repo research round seven-problems-2026-10-10. [Details](../../solutions/seven-problems-2026-10-10/Q3709.md).

**Further links.** [1](https://wiki.mathmig.binghamton.edu/doku.php?id=news:2026:0907_chris_schroeder)


<a id="q3710"></a>

## Q3710. Prime-order elements with singular commutators

**Status:** Open · **Kind:** open problem · **Collection** 38

Let G be a finite group, p a prime, and x∈G an element of order p. If every commutator [x,g]=x^{-1}g^{-1}xg, g∈G, is either the identity or has order divisible by p, must x belong to O_p(G), the largest normal p-subgroup of G?

**Context.** Genealogy: Advisor follow-through from Christopher Schroeder’s Binghamton PhD (2026), Invariants of finite groups, supervised by Tong-Viet. This restates the Guralnick–Robinson conjecture. https://arxiv.org/abs/2507.10882v4

**Source.** Hung P. Tong-Viet. *Orders of commutators and Products of conjugacy classes in finite groups*. 2025. [primary source](https://arxiv.org/abs/2507.10882v4) Location: Remark 1.3(ii), p.2

**Literature check.** Status: Explicitly conjectural in the current version; known when O_p(G) is abelian.

**Further links.** [1](https://wiki.mathmig.binghamton.edu/doku.php?id=news:2026:0907_chris_schroeder)


<a id="q3711"></a>

## Q3711. Full dualizability forces rigidity

**Status:** Open · **Kind:** open problem (Question 5.8) · **Collection** 38

Over a perfect field k, a finite pre-multitensor category is a finite k-linear abelian monoidal category with right-exact tensor product in each variable and with left and right duals for every projective object. Let B be such a category equipped with a braiding. In the symmetric monoidal Morita 4-category whose objects are braided finite pre-multitensor categories and whose 1-, 2-, 3-, and 4-morphisms are respectively finite central pre-multitensor categories, finite central bimodule categories, right-exact centered bimodule functors, and bimodule natural transformations, does full dualizability of B force every object of B to have left and right duals?

**Context.** Genealogy: Stroiński, Uppsala PhD 2025, Module categories in absence of adjunctions; supervisors Volodymyr Mazorchuk and Julian Külshammer. Later-paper question. https://arxiv.org/abs/2604.10753v1

**Source.** Thibault Décoppet and Mateusz Stroiński. *Finite Pre-Tensor Categories that are Morita Equivalent to Finite Tensor Categories*. 2026. [primary source](https://arxiv.org/abs/2604.10753v1) Location: Definition 2.8 and §5.2, Question 5.8

**Literature check.** Status: Explicitly open in the current submitted version.

**Further links.** [1](https://uu.diva-portal.org/smash/get/diva2%3A1947744/FULLTEXT01.pdf) · [2](https://sites.google.com/view/stroinski)


<a id="q3712"></a>

## Q3712. Products of iterated commutators detect the p-core

**Status:** Open · **Kind:** conjecture (Conjecture 1) · **Collection** 38

Let G be finite, p a prime divisor of |G|, and x∈G have p-power order. Define [a,b]=a^{-1}b^{-1}ab and c_1(g)=[g,x], c_{j+1}(g)=[c_j(g),x]. If for some integer k≥1 every product c_k(g)c_k(h), with g,h∈G, has p-power order, must x lie in O_p(G), the largest normal p-subgroup?

**Context.** Genealogy: Advisor follow-through from Christopher Schroeder’s Binghamton PhD (2026), Invariants of finite groups, supervised by Tong-Viet. https://doi.org/10.1112/jlms.70057

**Source.** Robert M. Guralnick, Hung P. Tong-Viet and Gareth Tracey. *Weakly subnormal subgroups and variations of the Baer–Suzuki theorem*. 2025. [primary source](https://doi.org/10.1112/jlms.70057) Location: Conjecture 1, p.6

**Literature check.** Status: Conjectural in the final version; pair-products cannot be replaced by individual commutators.

**Further links.** [1](https://wiki.mathmig.binghamton.edu/doku.php?id=news:2026:0907_chris_schroeder)


<a id="q3802"></a>

## Q3802. Is every finite permutative semigroup finitely related?

**Status:** Open · **Kind:** open problem (Problem 7.1) · **Collection** 39

Is every finite permutative semigroup finitely related?

**Context.** A finite semigroup is finitely related if finitely many finitary relations have precisely its nonempty-word operations as positive-arity polymorphisms. Permutative means satisfying x₁⋯xₙ=x_{π(1)}⋯x_{π(n)} for some nonidentity permutation π. Let B={0,I₂,e₁₁,e₁₂,e₂₁,e₂₂} under matrix multiplication, using standard matrix units. Origins/locators: thesis Problems 7.1, 7.12, 7.14, pp.119,122,124. Q3802 is thesis-origin; Q3803 restates Glasson (2024), Problem 4.21; Q3804 restates Mayr (2013), Problem 8.4. Both journal finals inspected; later Sapir accepted v3 checked.

**Source.** Daniel Glasson. *Finitely Related Semigroups and Associated Structures*. RMIT University, 2024. Advisor(s): Marcel Jackson, Asha Rao, Graham Clarke. [primary source](https://doi.org/10.25439/rmt.28478171) Location: thesis Problem 7.1, p.119 (thesis-origin)

**Literature check.** Status, 2026-10-10: no resolution found in bounded searches.

**Further links.** [1](https://ndownloader.figshare.com/files/52581998) · [2](https://doi.org/10.1007/s00233-024-10452-8) · [3](https://doi.org/10.1007/s00233-012-9455-6) · [4](https://arxiv.org/abs/2502.02157v3)


<a id="q3803"></a>

## Q3803. Can finitely related finite semigroups S,T have non-finitely-related product S×T?

**Status:** Open · **Kind:** open problem (Problem 7.12) · **Collection** 39

Can finitely related finite semigroups S,T have non-finitely-related product S×T?

**Context.** A finite semigroup is finitely related if finitely many finitary relations have precisely its nonempty-word operations as positive-arity polymorphisms. Permutative means satisfying x₁⋯xₙ=x_{π(1)}⋯x_{π(n)} for some nonidentity permutation π. Let B={0,I₂,e₁₁,e₁₂,e₂₁,e₂₂} under matrix multiplication, using standard matrix units. Origins/locators: thesis Problems 7.1, 7.12, 7.14, pp.119,122,124. Q3802 is thesis-origin; Q3803 restates Glasson (2024), Problem 4.21; Q3804 restates Mayr (2013), Problem 8.4. Both journal finals inspected; later Sapir accepted v3 checked.

**Source.** Daniel Glasson. *Finitely Related Semigroups and Associated Structures*. RMIT University, 2024. Advisor(s): Marcel Jackson, Asha Rao, Graham Clarke. [primary source](https://doi.org/10.25439/rmt.28478171) Location: thesis Problem 7.12, p.122; restates Glasson (2024), Problem 4.21

**Literature check.** Status, 2026-10-10: no resolution found in bounded searches.

**Further links.** [1](https://ndownloader.figshare.com/files/52581998) · [2](https://doi.org/10.1007/s00233-024-10452-8) · [3](https://doi.org/10.1007/s00233-012-9455-6) · [4](https://arxiv.org/abs/2502.02157v3)


<a id="q3804"></a>

## Q3804. Is every finite semigroup admitting an injective semigroup homomorphism B→S non-finitely-related?

**Status:** Open · **Kind:** open problem (Problem 7.14) · **Collection** 39

Is every finite semigroup admitting an injective semigroup homomorphism B→S non-finitely-related?

**Context.** A finite semigroup is finitely related if finitely many finitary relations have precisely its nonempty-word operations as positive-arity polymorphisms. Permutative means satisfying x₁⋯xₙ=x_{π(1)}⋯x_{π(n)} for some nonidentity permutation π. Let B={0,I₂,e₁₁,e₁₂,e₂₁,e₂₂} under matrix multiplication, using standard matrix units. Origins/locators: thesis Problems 7.1, 7.12, 7.14, pp.119,122,124. Q3802 is thesis-origin; Q3803 restates Glasson (2024), Problem 4.21; Q3804 restates Mayr (2013), Problem 8.4. Both journal finals inspected; later Sapir accepted v3 checked.

**Source.** Daniel Glasson. *Finitely Related Semigroups and Associated Structures*. RMIT University, 2024. Advisor(s): Marcel Jackson, Asha Rao, Graham Clarke. [primary source](https://doi.org/10.25439/rmt.28478171) Location: thesis Problem 7.14, p.124; restates Mayr (2013), Problem 8.4

**Literature check.** Status, 2026-10-10: no resolution found in bounded searches.

**Further links.** [1](https://ndownloader.figshare.com/files/52581998) · [2](https://doi.org/10.1007/s00233-024-10452-8) · [3](https://doi.org/10.1007/s00233-012-9455-6) · [4](https://arxiv.org/abs/2502.02157v3)


<a id="q3830"></a>

## Q3830. Finite-codimension generalized Witt subalgebras

**Status:** Open · **Kind:** open problem (Question 5.9.2) · **Collection** 39

Give an explicit classification of the finite-codimension Lie subalgebras embedded in W_Γ.

**Context.** Origin: Explicitly posed in thesis Questions 5.9.2(1),(2),(4); no first-publication claim. Setup: Let k be algebraically closed of characteristic zero and Γ an additive subgroup of k. The k-Lie algebra W_Γ has basis e_γ (γ∈Γ), with [e_γ,e_δ]=(δ−γ)e_(γ+δ). Sources:

**Source.** Lucas Buzaglo. *Lie algebras of derivations and their universal enveloping algebras*. University of Edinburgh, 2024. Advisor(s): Susan Sierra. [primary source](https://mathweb.ucsd.edu/~lbuzaglo/thesis.pdf) Location: pp. 101–102, Question 5.9.2(1)

**Literature check.** Status: Checked 10 October 2026: no general resolution found. The 2026 curve results do not cover arbitrary Γ.

**Further links.** [1](https://mathweb.ucsd.edu/~lbuzaglo/) · [2](https://arxiv.org/abs/2606.21748v1)


<a id="q3831"></a>

## Q3831. Derivations of generalized Witt subalgebras

**Status:** Open · **Kind:** open problem (Question 5.9.2) · **Collection** 39

Determine Der_k(g) for every infinite-dimensional Lie subalgebra g⊂W_Γ.

**Context.** Origin: Explicitly posed in thesis Questions 5.9.2(1),(2),(4); no first-publication claim. Setup: Let k be algebraically closed of characteristic zero and Γ an additive subgroup of k. The k-Lie algebra W_Γ has basis e_γ (γ∈Γ), with [e_γ,e_δ]=(δ−γ)e_(γ+δ). Sources:

**Source.** Lucas Buzaglo. *Lie algebras of derivations and their universal enveloping algebras*. University of Edinburgh, 2024. Advisor(s): Susan Sierra. [primary source](https://mathweb.ucsd.edu/~lbuzaglo/thesis.pdf) Location: p. 102, Question 5.9.2(2)

**Literature check.** Status: Checked 10 October 2026: no general resolution found. The 2026 curve results do not cover arbitrary Γ.

**Further links.** [1](https://mathweb.ucsd.edu/~lbuzaglo/) · [2](https://arxiv.org/abs/2606.21748v1)


<a id="q3832"></a>

## Q3832. Isomorphisms between generalized Witt subalgebras

**Status:** Open · **Kind:** open problem (Question 5.9.2) · **Collection** 39

Determine when two infinite-dimensional Lie subalgebras of W_Γ are isomorphic as k-Lie algebras.

**Context.** Origin: Explicitly posed in thesis Questions 5.9.2(1),(2),(4); no first-publication claim. Setup: Let k be algebraically closed of characteristic zero and Γ an additive subgroup of k. The k-Lie algebra W_Γ has basis e_γ (γ∈Γ), with [e_γ,e_δ]=(δ−γ)e_(γ+δ). Sources:

**Source.** Lucas Buzaglo. *Lie algebras of derivations and their universal enveloping algebras*. University of Edinburgh, 2024. Advisor(s): Susan Sierra. [primary source](https://mathweb.ucsd.edu/~lbuzaglo/thesis.pdf) Location: p. 102, Question 5.9.2(4)

**Literature check.** Status: Checked 10 October 2026: no general resolution found. The 2026 curve results do not cover arbitrary Γ.

**Further links.** [1](https://mathweb.ucsd.edu/~lbuzaglo/) · [2](https://arxiv.org/abs/2606.21748v1)


<a id="q3833"></a>

## Q3833. Explicit subalgebra structure on arbitrary curves

**Status:** Open · **Kind:** open problem (Question 9.9) · **Collection** 39

Describe explicitly all infinite-dimensional Lie subalgebras of L_C for every such curve C.

**Context.** Origin: Joint-paper Question 9.9. Doctoral context: Buzaglo, above. Setup: Let k be algebraically closed of characteristic zero. For a smooth affine irreducible k-curve C, set L_C=Der_k(O(C)). Sources:

**Source.** Lucas Buzaglo and Colin Ingalls. *Lie subalgebras of vector fields on curves*. 2026. [primary source](https://arxiv.org/abs/2606.21748) Location: p. 26, Question 9.9; global conventions §2, p. 4

**Literature check.** Status: Checked 10 October 2026: v1 remains current; no resolution found. Theorem 1.1 gives a finite-codimension embedding into L_D, not this explicit description.

**Further links.** [1](https://arxiv.org/pdf/2606.21748v1)


<a id="q3836"></a>

## Q3836. Polynomially bounded nonpolynomial automorphic growth

**Status:** Open · **Kind:** open problem (Question 8.2) · **Collection** 39

Does some finitely generated G have polynomially bounded α\_G that is not ∼-equivalent to any nonzero polynomial?

**Context.** Doctoral context: Alexander Evetts: Aspects of Growth in Finitely Generated Groups, Heriot-Watt PhD, June 2020; supervisor Laura Ciobanu. Origin: Joint-paper Questions 8.2, 8.3, 8.7; dissertation-led follow-up, not thesis-origin. Setup: For finitely generated G, α\_G(n) counts Aut(G)-orbits meeting a word ball of radius n. Define f≼g by f(n)≤λg(λn+λ)+λ for some integer λ≥1 and all n≥0; f∼g means both directions. Thompson’s F comprises orientation-preserving piecewise-linear homeomorphisms of [0,1] with finitely many dyadic breakpoints and slopes powers of two. Sources:

**Source.** Luna Elliott, Alex Evetts and Alex Levine. *Counting automorphic orbits in finitely generated groups*. 2026. [primary source](https://arxiv.org/abs/2604.18104) Location: p. 41, Question 8.2

**Literature check.** Status: Checked 10 October 2026: v2 and Elliott’s June list retain these; no resolution found.

**Further links.** [1](https://le27.github.io/L-Elliott/questions/) · [2](https://www.ros.hw.ac.uk/server/api/core/bitstreams/e4de7b9f-71ed-4985-b1ab-3c60e61101c9/content) · [3](https://www.macs.hw.ac.uk/~lc45/GroupTheory/Papers.html)


<a id="q3837"></a>

## Q3837. Automorphic growth of virtually abelian groups

**Status:** Open · **Kind:** open problem (Question 8.3) · **Collection** 39

Classify α\_G up to ∼ for every finitely generated virtually abelian group G.

**Context.** Doctoral context: Alexander Evetts: Aspects of Growth in Finitely Generated Groups, Heriot-Watt PhD, June 2020; supervisor Laura Ciobanu. Origin: Joint-paper Questions 8.2, 8.3, 8.7; dissertation-led follow-up, not thesis-origin. Setup: For finitely generated G, α\_G(n) counts Aut(G)-orbits meeting a word ball of radius n. Define f≼g by f(n)≤λg(λn+λ)+λ for some integer λ≥1 and all n≥0; f∼g means both directions. Thompson’s F comprises orientation-preserving piecewise-linear homeomorphisms of [0,1] with finitely many dyadic breakpoints and slopes powers of two. Sources:

**Source.** Luna Elliott, Alex Evetts and Alex Levine. *Counting automorphic orbits in finitely generated groups*. 2026. [primary source](https://arxiv.org/abs/2604.18104) Location: p. 41, Question 8.3

**Literature check.** Status: Checked 10 October 2026: v2 and Elliott’s June list retain these; no resolution found.

**Further links.** [1](https://le27.github.io/L-Elliott/questions/) · [2](https://www.ros.hw.ac.uk/server/api/core/bitstreams/e4de7b9f-71ed-4985-b1ab-3c60e61101c9/content) · [3](https://www.macs.hw.ac.uk/~lc45/GroupTheory/Papers.html)


<a id="q3838"></a>

## Q3838. Automorphic growth of Thompson’s F

**Status:** Open · **Kind:** open problem (Question 8.7) · **Collection** 39

Determine α\_F up to ∼.

**Context.** Doctoral context: Alexander Evetts: Aspects of Growth in Finitely Generated Groups, Heriot-Watt PhD, June 2020; supervisor Laura Ciobanu. Origin: Joint-paper Questions 8.2, 8.3, 8.7; dissertation-led follow-up, not thesis-origin. Setup: For finitely generated G, α\_G(n) counts Aut(G)-orbits meeting a word ball of radius n. Define f≼g by f(n)≤λg(λn+λ)+λ for some integer λ≥1 and all n≥0; f∼g means both directions. Thompson’s F comprises orientation-preserving piecewise-linear homeomorphisms of [0,1] with finitely many dyadic breakpoints and slopes powers of two. Sources:

**Source.** Luna Elliott, Alex Evetts and Alex Levine. *Counting automorphic orbits in finitely generated groups*. 2026. [primary source](https://arxiv.org/abs/2604.18104) Location: p. 41, Question 8.7

**Literature check.** Status: Checked 10 October 2026: v2 and Elliott’s June list retain these; no resolution found.

**Further links.** [1](https://le27.github.io/L-Elliott/questions/) · [2](https://www.ros.hw.ac.uk/server/api/core/bitstreams/e4de7b9f-71ed-4985-b1ab-3c60e61101c9/content) · [3](https://www.macs.hw.ac.uk/~lc45/GroupTheory/Papers.html)


<a id="q3889"></a>

## Q3889. A general Engel bound from one multilinear identity

**Status:** Open · **Kind:** conjecture (Conjecture 1.5) · **Collection** 39

For every integer k≥2, does the identity t_k=0 on A imply e_{3^(k−2)}(x,y)=0 for all x,y∈A?

**Context.** Origin: Paper-origin: On a conjecture of Dotsenko on weak nilpotence and the Engel identity, current author-hosted 2026 submitted manuscript. Setup: Let A be a vector space over a characteristic-zero field with a commutative bilinear product, not assumed associative or unital. Define t_k(a₁,…,a_k) by summing all distinct multilinear degree-k nonassociative monomials, identifying only those equal by commutativity. Let e_m(x,y)=(((xy)y)⋯y), with m copies of y. Sources:

**Source.** Oisín Flynn-Connolly. *On a conjecture of Dotsenko on weak nilpotence and the Engel identity*. 2026. [primary source](https://flynncoo.github.io/pdfs/papers/dotsenko-weak-nilpotence-engel.pdf) Location: Conjecture 1.5, p.2; definitions p.1.

**Literature check.** Status: Checked 10 October 2026: k=3,4 are proved; no general resolution found.

**Further links.** [1](https://flynncoo.github.io/) · [2](https://flynncoo.github.io/pdfs/theses/PhD_thesis__ED_version_.pdf)


<a id="q3892"></a>

## Q3892. Koszul Roller Coaster algebras

**Status:** Open, partial results · **Kind:** conjecture (Conjecture 5.8) · **Collection** 39

Over a characteristic-zero field K, for all sufficiently large d and every permutation π of {1,…,⌊d/2⌋}, is there an Artinian Gorenstein Koszul K-algebra of socle degree d with h_{π(1)}<⋯&lt;h_{π(⌊d/2⌋)}?

**Context.** Origin: Paper-origin: Holleben–Lisa Nicklasson, Roller Coaster Gorenstein algebras and Koszul algebras failing the weak Lefschetz property, JPAA230(2026),108238; full final. Setup: All algebras are standard graded. For Artinian A, write h_i=dim_K A_i. WLP means some ℓ∈A₁ makes every map A_i→A_{i+1}, u↦ℓu, have maximal rank. Sources:

**Source.** Thiago Holleben and Lisa Nicklasson. *Roller Coaster Gorenstein algebras and Koszul algebras failing the weak Lefschetz property*. 2026. [primary source](https://www.diva-portal.org/smash/get/diva2%3A2053155/FULLTEXT01.pdf) Location: Conjecture 5.8, printed p.18 (PDF p.19); thesis Question 7.3.1, p.163; characteristic-zero context: thesis p.118.

**Literature check.** Status: Checked 10 October 2026: both retained in the final; no general resolution found.

**Results.**

- **Partial result**: For every d>=3, the flag join of q=d-1 discrete sets of common size s>=2q+1 gives a characteristic-zero Artinian Gorenstein Koszul algebra with h_i=binom(q,i)s^i+binom(q,i-1)s^(d-i) and h_1>...>h_floor(d/2). Other arbitrary permutations in every sufficiently large degree remain unresolved. The flag-join algebra family is source-known; the all-degree ordering inequality is proved in the local packet. Internally reviewed at this scope; no novelty or external peer-review claim. [Details](../../solutions/b3-all-targets-2026-10-13/koszul/Q3892-RESULTS.md).
- **Partial result** (B3-ALL-TARGETS-Q3892-DESCENDING: Every socle degree admits a descending Koszul half-row): For every d>=3, the flag join of q=d-1 discrete sets of common size s>=2q+1 gives a characteristic-zero Artinian Gorenstein Koszul algebra with h_i=binom(q,i)s^i+binom(q,i-1)s^(d-i) and h_1>...>h_floor(d/2). Remaining/limits: Other arbitrary permutations in every sufficiently large degree remain unresolved. The flag-join algebra family is source-known; the all-degree ordering inequality is proved in the local packet. [Report](../../solutions/b3-all-targets-2026-10-13/koszul/Q3892-RESULTS.md).
- **Investigated, unresolved** (B3-ALL-TARGETS-STOP-REGISTER: Reviewed B3 failed routes and per-target stopping decisions): 45 targets have each reached five consecutive substantive distinct full-target failures. STATUS.json records every accepted route, written analysis, evidence path and review provenance. Partial results do not reset counters. Rejected proposed attempts, source-range replays, service errors and shared mechanisms remain explicit rather than supplying extra counts. Remaining/limits: These questions remain mathematically unresolved. A failure-limit stop is an operational disposition, not a counterexample or proof. Missing historical archives remain separate evidence issues. [Report](../../solutions/b3-all-targets-2026-10-13/STATUS.json).

**Further links.** [1](https://doi.org/10.1016/j.jpaa.2026.108238) · [2](https://hollebenthiago.github.io/phd/thesis.pdf) · [3](https://hollebenthiago.github.io/)


<a id="q3893"></a>

## Q3893. Whiskering forces Lefschetz failure

**Status:** Solved here: proved · **Kind:** conjecture (Conjecture 1.3) · **Collection** 39

For every finite simple graph G on [n] with independence number≥3, let w(G) add one pendant vertex at each vertex. Over any field K, must K[x₁,…,x₂ₙ]/(x_ix_j:{i,j}∈E(w(G)); x₁²,…,x₂ₙ²) fail WLP?

**Context.** Origin: Paper-origin: Holleben–Lisa Nicklasson, Roller Coaster Gorenstein algebras and Koszul algebras failing the weak Lefschetz property, JPAA230(2026),108238; full final. Setup: All algebras are standard graded. For Artinian A, write h_i=dim_K A_i. WLP means some ℓ∈A₁ makes every map A_i→A_{i+1}, u↦ℓu, have maximal rank. Sources:

**Source.** Thiago Holleben and Lisa Nicklasson. *Roller Coaster Gorenstein algebras and Koszul algebras failing the weak Lefschetz property*. 2026. [primary source](https://www.diva-portal.org/smash/get/diva2%3A2053155/FULLTEXT01.pdf) Location: Conjecture 1.3, p.3; 3.15, p.10.

**Literature check.** Status: Checked 10 October 2026: both retained in the final; no general resolution found.

**Literature check.** Research update, 10 October 2026: proposed complete proof recorded in seven-selected-2026-10-10. The statement uses the exact square relations and complete whiskering in the source conjecture. It makes no extension to arbitrary higher truncation powers or general very-well-covered graphs.

**Further links.** [1](https://doi.org/10.1016/j.jpaa.2026.108238) · [2](https://hollebenthiago.github.io/phd/thesis.pdf) · [3](https://hollebenthiago.github.io/)

**Result (2026-10-10).** For every graph G on n vertices with an independent triple, the square-truncated algebra of its fully whiskered graph fails the weak Lefschetz property over every field. Every linear form fails maximal rank from degree ceil(n/2) to degree ceil(n/2)+1. A shear yields invariant summands forcing a kernel and a cokernel in the same map. The statement uses the exact square relations and complete whiskering in the source conjecture. It makes no extension to arbitrary higher truncation powers or general very-well-covered graphs.

[Proof](../../solutions/seven-selected-2026-10-10/algebra/3893.md) · [Internal review](../../solutions/seven-selected-2026-10-10/discrete/review-Q3893.md) · [Computational controls](../../solutions/seven-selected-2026-10-10/verification.json) · [Source check](../../solutions/seven-selected-2026-10-10/algebra/SOURCES.md). Separate internal AI review found no blocking defect; not external peer review, formal certification, or a novelty certification.



<a id="q3894"></a>

## Q3894. Strong Lefschetz for unexpected reductions

**Status:** Open · **Kind:** open problem (Question 7.1) · **Collection** 39

Must A have the strong Lefschetz property: some ℓ∈A₁ makes multiplication by ℓʲ from A_i to A_{i+j} have maximal rank for every i,j≥0?

**Context.** Origin: Paper-origin, also restated in thesis Question 7.1.1. Setup: Let Δ be a d-dimensional Q-homology sphere on [n], meaning every face link has the reduced rational homology of a sphere of its dimension. Set R=C[x₁,…,xₙ], I=I_Δ, the ideal generated by squarefree monomials of nonfaces, and L=Σx_i. Let a≥1 and positive-degree homogeneous θ₁,…,θ\_{d+1} make A=R/(I,θ₁,…,θ\_{d+1}) finite-dimensional. Put t=Σdeg θ\_i and J=I+(x₁ᵃ,…,xₙᵃ). Assume t≥d+1, L,x₁ᵃ,…,xₙᵃ∈(I,θ₁,…,θ\_{d+1}), and dim_C(R/J)\_t≤dim_C(R/J)\_{t−1}. Sources:

**Source.** Thiago Holleben. *From points to complexes: A concept of unexpectedness for simplicial complexes*. 2026. [primary source](https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/jlms.70632) Location: Question 7.1; Definition 3.2(U1–U5); thesis p.157.

**Literature check.** Status: Checked 10 October 2026: final retains the question; no later resolution found.

**Further links.** [1](https://hollebenthiago.github.io/phd/thesis.pdf) · [2](https://hollebenthiago.github.io/research/)


<a id="q3895"></a>

## Q3895. A shorter normality test

**Status:** Open · **Kind:** open problem (Question 3.17) · **Collection** 39

If I is minimally generated by q≥4 monomials, is normality equivalent to overline(Iʳ)=Iʳ for every 2≤r≤q−2?

**Context.** Origin: Paper-origin; Holleben’s verified doctoral context is given above. Setup: Let R=k[x₁,…,xₙ] over a field k. For a squarefree monomial ideal I, write overline(Iʳ) for the integral closure of Iʳ and I^(s)=∩\_{P∈Min(I)}(IˢR_P∩R). The ideal I is normal when overline(Iʳ)=Iʳ for every r≥1. Sources:

**Source.** Trung Chau, Art Duval, Sara Faridi, Thiago Holleben, Susan Morey and Liana Şega. *Symbolic powers and integral closures via extremal ideals*. 2026. [primary source](https://arxiv.org/abs/2602.05076v1) Location: Question 3.17, p.16; Theorem 3.16.

**Literature check.** Status: Checked 10 October 2026: current v1 and author publication lists retain the questions; no general resolution found.

**Further links.** [1](https://hollebenthiago.github.io/research/)


<a id="q3896"></a>

## Q3896. Universal integral-closure containments

**Status:** Open · **Kind:** open problem (Question 4.12) · **Collection** 39

For each q≥1, determine all positive integer pairs (r,s) for which I^(s)⊆overline(Iʳ) holds for every squarefree monomial ideal I generated by q elements, in every polynomial ring over a field.

**Context.** Origin: Paper-origin; Holleben’s verified doctoral context is given above. Setup: Let R=k[x₁,…,xₙ] over a field k. For a squarefree monomial ideal I, write overline(Iʳ) for the integral closure of Iʳ and I^(s)=∩\_{P∈Min(I)}(IˢR_P∩R). The ideal I is normal when overline(Iʳ)=Iʳ for every r≥1. Sources:

**Source.** Trung Chau, Art Duval, Sara Faridi, Thiago Holleben, Susan Morey and Liana Şega. *Symbolic powers and integral closures via extremal ideals*. 2026. [primary source](https://arxiv.org/abs/2602.05076v1) Location: Question 4.12, p.22.

**Literature check.** Status: Checked 10 October 2026: current v1 and author publication lists retain the questions; no general resolution found.

**Further links.** [1](https://hollebenthiago.github.io/research/)


<a id="q3932"></a>

## Q3932. Is there an involution semigroup with exactly five elements, no identity element, and no finite…

**Status:** Open · **Kind:** open problem (Question 1.2) · **Collection** 40

Is there an involution semigroup with exactly five elements, no identity element, and no finite identity basis?

**Context.** An involution semigroup is an associative semigroup S equipped with a unary operation \* satisfying (x\*)\*=x and (xy)\*=y\*x\*. It is finitely based if all identities valid in the signature (multiplication,\*) follow from a finite set of such identities.

**Source.** Meng Gao, Edmond W. H. Lee, Yan Feng Luo and Wen Ting Zhang. *Finite basis problem for involution semigroups of order four*. 2026. [primary source](https://doi.org/10.2140/pjm.2026.342.163) Location: Question 1.2 and following paragraph, p.165.

**Literature check.** Status: This is the authors' explicit remaining case of uniqueness at order five: the unique non-finitely-based order-five involution monoid is already known. Paper-origin question; the 2026 final and arXiv:2305.19494v2 (14 April 2026), Question 1.2, retain the nonunital case. No matching later resolution found in the documented 10 October 2026 search.

**Further links.** [1](https://arxiv.org/abs/2305.19494v2)


<a id="q3936"></a>

## Q3936. Must there exist a bounded complex C of finite-dimensional p-permutation kG-modules such that,…

**Status:** Open · **Kind:** conjecture (Conjecture 9.0.7) · **Collection** 40

Must there exist a bounded complex C of finite-dimensional p-permutation kG-modules such that, for every P∈X_V, C(P) has one-dimensional homology in degree f(P) and vanishing homology otherwise?

**Context.** Let G be finite, k a field with char(k)=p>0, and V a finite-dimensional p-permutation kG-module with all indecomposable summand dimensions divisible by p. Put X_V={P≤G:P a p-subgroup,V(P)=0}, using Brauer quotients, applied termwise to complexes. Let f:X_V→Z be conjugacy-invariant. Require these Borel–Smith conditions whenever every displayed f-value is defined: for H◁L, L/H≅C_p and p odd, f(H)−f(L) is even; for H◁L◁N≤N_G(H), L/H≅C_2, require f(H)−f(L) to be divisible by 2 or 4 when N/H≅C_4 or Q_8, respectively; for H◁L, L/H≅C_p×C_p, require f(H)−f(L)=Σ\_{H&lt;K&lt;L}(f(K)−f(L)). All groups in these chains are p-subgroups of G; N need not belong to X_V.

**Source.** Sam Kim Miller. *Permutation modules and endotrivial complexes*. University of California, Santa Cruz, 2025. Advisor(s): Robert Boltje. [primary source](https://escholarship.org/uc/item/9h73j2g4) Location: Conjecture 9.0.7(i), p.123, restates Relatively endotrivial complexes, Conjecture 10.7(i), accepted arXiv:2402.08042v3; JPAA 229 (2025), 107867.

**Literature check.** Status: Theorem 1.2(a) gives this equivalent local formulation; later integral classification is non-relative. No matching resolution found, 10 October 2026.

**Further links.** [1](https://arxiv.org/abs/2402.08042v3) · [2](https://arxiv.org/abs/2605.31128v1)


<a id="q3937"></a>

## Q3937. For each prime p and integer r≥2, do there exist finite p-groups G of arbitrarily large…

**Status:** Open · **Kind:** open problem (Question 5.1) · **Collection** 40

For each prime p and integer r≥2, do there exist finite p-groups G of arbitrarily large nilpotence class such that Z(G)≅(C_p)^r and every g∈G\Z(G) is conjugate to every element of gZ(G)?

**Source.** Alexander Moretó. *On the minimal dimension of a faithful linear representation of a finite group*. 2026. [primary source](https://doi.org/10.2140/ant.2026.20.219) Location: Question 5.1 and its discussion, p.233.

**Literature check.** Status: The conjugacy condition says (G,Z(G)) is a Camina pair; the source explicitly identifies it with its character-theoretic hypothesis. The r=1 case is already affirmative and is excluded. Moretó states the general question, crediting Reichstein with earlier r=1,2 questions. Paper-origin residual, not a new doctoral attribution. No matching resolution found in the documented 10 October 2026 search.


<a id="q3938"></a>

## Q3938. Under these hypotheses, does maximal Cohen–Macaulayness of F_R^e(N)⊗\_R M, for some e≫0, force N…

**Status:** Open · **Kind:** open problem (Question 4.12) · **Collection** 40

Under these hypotheses, does maximal Cohen–Macaulayness of F_R^e(N)⊗\_R M, for some e≫0, force N to be free?

**Context.** Let (R,m,k) be a commutative Noetherian local ring of characteristic p>0, and M,N finitely generated R-modules. Assume Supp_R(M)=Spec(R) and N_q is free over R_q for every q∈Ass(R). Write F_R^e(N)=N⊗\_{R,F^e}R, with scalar action on the second factor; F^e(r)=r^{p^e}. A nonzero finite module is maximal Cohen–Macaulay when its depth equals dim(R).

**Source.** Olgur Celikbas, Arash Sadeghi and Yongwei Yao. *On the test properties of the Frobenius endomorphism*. 2026. [primary source](https://doi.org/10.2140/pjm.2026.342.235) Location: Question 4.12, p.255; Frobenius convention pp.235,237.

**Literature check.** Status: Paper-origin question. The final proves this when M is Cohen–Macaulay and leaves the displayed hypothesis without that assumption open. The source's “some e≫0” convention is preserved. No matching later resolution found, 10 October 2026.


<a id="q3958"></a>

## Q3958. Is A⊗\_k B necessarily noetherian whenever both factors are noetherian connected graded…

**Status:** Open · **Kind:** open problem · **Collection** 40

Is A⊗\_k B necessarily noetherian whenever both factors are noetherian connected graded Artin–Schelter regular k-algebras?

**Context.** Fix a field k. A connected N-graded k-algebra T has T₀=k. It is Artin–Schelter regular if it has finite global dimension d, finite Gelfand–Kirillov dimension, left and right injective dimension d, and using graded Ext on both sides, Ext^i_T(k,T)=0 for i≠d while Ext^d_T(k,T)≅k(ℓ) for an integer ℓ. The notation k(ℓ) shifts internal grading.

**Source.** Ellen Kirkman, Robert Won and James J. Zhang. *Homological regularities and concavities*. 2026. [primary source](https://doi.org/10.2140/ant.2026.20.1559) Location: final Remark 5.8, p.1591; Definition 0.2, p.1560.

**Literature check.** Status: Noetherian means both left and right noetherian. This is a paper-reported open question. The final explicitly leaves tensor-product noetherianity unresolved before discussing additivity of other invariants; those conditional additivity statements do not answer it. No matching later resolution found, 10 October 2026.


<a id="q4038"></a>

## Q4038. Call G resistant if, for every field k, each element of kG with support size>1 generates a…

**Status:** Open · **Kind:** open problem (Question 19) · **Collection** 41

Call G resistant if, for every field k, each element of kG with support size>1 generates a proper two-sided ideal. Are arbitrary direct products of resistant groups resistant?

**Source.** George M. Bergman. *Some questions for possible submission to the next Kourovka notebook*. 2026. [primary source](https://arxiv.org/abs/1904.04298v2) Location: Q3(ii), p. 2; originally 2021 Question 19

**Literature check.** Status: Author’s updated list retains these; no later resolution found, 10 October 2026. Paper-origin.

**Further links.** [1](https://math.berkeley.edu/~gbergman/papers/prin_ids_in_kG.pdf) · [2](https://math.berkeley.edu/~gbergman/papers/kG_in_D.pdf)


<a id="q4039"></a>

## Q4039. For a group G with a right-invariant total order and a field k, let k((G)) be formal k-linear…

**Status:** Open · **Kind:** open problem (Question 13) · **Collection** 41

For a group G with a right-invariant total order and a field k, let k((G)) be formal k-linear sums with well-ordered support. For nonzero x₁,x₂,y₁,y₂∈kG, must the operator y₁y₂⁻¹−x₁x₂⁻¹ on k((G)) be zero or invertible? Products act on the right; inverses mean inverse right-multiplication operators.

**Source.** George M. Bergman. *Some questions for possible submission to the next Kourovka notebook*. 2026. [primary source](https://arxiv.org/abs/1904.04298v2) Location: Q4, p. 2; originally 2019 Question 13

**Literature check.** Status: Author’s updated list retains these; no later resolution found, 10 October 2026. Paper-origin.

**Further links.** [1](https://math.berkeley.edu/~gbergman/papers/prin_ids_in_kG.pdf) · [2](https://math.berkeley.edu/~gbergman/papers/kG_in_D.pdf)


<a id="q4040"></a>

## Q4040. For a group variety V (a class defined by group identities), let F_V(r) be its relatively free…

**Status:** Open · **Kind:** open problem · **Collection** 41

For a group variety V (a class defined by group identities), let F_V(r) be its relatively free group on r generators. Can F_V(2) have polynomial word growth while F_V(3) does not? Polynomial growth means |B(n)|≤Cnᵈ for some C,d and all n≥1, where B(n) comprises group elements representable by words of length≤n in generators and inverses.

**Source.** George M. Bergman. *Some questions for possible submission to the next Kourovka notebook*. 2026. [primary source](https://arxiv.org/abs/1904.04298v2) Location: Q22(i), pp. 3–4

**Literature check.** Status: Author’s updated list retains these; no later resolution found, 10 October 2026. Paper-origin.

**Further links.** [1](https://math.berkeley.edu/~gbergman/papers/prin_ids_in_kG.pdf) · [2](https://math.berkeley.edu/~gbergman/papers/kG_in_D.pdf)


<a id="q4187"></a>

## Q4187. If a finite group G is generated by two elements and its generating graph has no induced…

**Status:** Open · **Kind:** conjecture (Conjecture 2.11) · **Collection** 42

If a finite group G is generated by two elements and its generating graph has no induced four-vertex path, must G be soluble? This graph has vertex set G, with distinct x,y adjacent exactly when ⟨x,y⟩=G.

**Source.** Daniele Nemmi. *Problems on generation of finite groups and on class related graphs*. University of Padova, 2024. Advisor(s): Andrea Lucchini. [primary source](https://www.research.unipd.it/handle/11577/3515010) Location: Conjecture 2.11, p. 11, and Problem 7.65, p. 122, restate earlier joint-paper questions.

**Literature check.** Status checked 10 October 2026: The published originals retain these questions: Lucchini–Nemmi (2022), Conjecture 1.11, p. 927; Burness–Lucchini–Nemmi (2023), Problem 8.1, p. 37. No later resolution was found.

**Further links.** [1](https://doi.org/10.5802/alco.229) · [2](https://doi.org/10.1016/j.jcta.2022.105708)


<a id="q4188"></a>

## Q4188. Does some finite insoluble group G with trivial soluble radical have soluble graph of diameter…

**Status:** Open · **Kind:** conjecture (Conjecture 2.11) · **Collection** 42

Does some finite insoluble group G with trivial soluble radical have soluble graph of diameter five? Its vertices are G∖{1}, and distinct x,y are adjacent exactly when ⟨x,y⟩ is soluble.

**Source.** Daniele Nemmi. *Problems on generation of finite groups and on class related graphs*. University of Padova, 2024. Advisor(s): Andrea Lucchini. [primary source](https://www.research.unipd.it/handle/11577/3515010) Location: Conjecture 2.11, p. 11, and Problem 7.65, p. 122, restate earlier joint-paper questions.

**Literature check.** Status checked 10 October 2026: The published originals retain these questions: Lucchini–Nemmi (2022), Conjecture 1.11, p. 927; Burness–Lucchini–Nemmi (2023), Problem 8.1, p. 37. No later resolution was found.

**Further links.** [1](https://doi.org/10.5802/alco.229) · [2](https://doi.org/10.1016/j.jcta.2022.105708)


<a id="q4260"></a>

## Q4260. Is b̃\_e=b_e for every e equivalent to existence of d≥1 and a surjective R-linear φ:F_\*^dR→R…

**Status:** Open · **Kind:** conjecture (Conjecture IV.3.13) · **Collection** 43

Is b̃\_e=b_e for every e equivalent to existence of d≥1 and a surjective R-linear φ:F_\*^dR→R satisfying φ(F_\*^db_(e+d))⊆b_e for every e?

**Context.** Let R be a commutative Noetherian F-finite strongly F-regular ring of characteristic p>0. A p-family is a sequence of ideals b_e, e≥1, with b_e^[p]⊆b_(e+1), where I^[p]=(x^p:x∈I). Define b̃\_e={r∈R:r^(p^f)∈b_(e+f) for all sufficiently large f}. The Frobenius-twisted module F_\*^dR has scalar action a·F_\*^dr=F_\*^d(a^(p^d)r).

**Source.** Anna Brosowsky. *The Cartier Core Map and F-Graded Systems*. University of Michigan, 2024. Advisor(s): Karen E. Smith. [primary source](https://sites.lsa.umich.edu/kesmith/wp-content/uploads/sites/1309/2024/06/BrosowskyThesis.pdf) Location: Thesis-origin Conjecture IV.3.13, p. 51, reaffirmed in Cartier algebras through the lens of p-families, arXiv:2605.22987v1 (2026), Conjecture 5.13, p. 13.

**Literature check.** Status checked 10 October 2026: Current v1 proves special cases and retains the conjecture; no later resolution found.

**Further links.** [1](https://arxiv.org/abs/2605.22987v1)


<a id="q4261"></a>

## Q4261. If I is licci, must m^d(I) fail to be contained in I?

**Status:** Open · **Kind:** conjecture (Conjecture 1.3) · **Collection** 43

If I is licci, must m^d(I) fail to be contained in I?

**Context.** Let (S,m) be a regular local ring and I a proper m-primary ideal. An ideal is licci if it can be linked to a complete-intersection ideal by finitely many links: J and K are linked when J=a:K and K=a:J for some complete-intersection ideal a. Write μ(I) for the minimum number of generators and d(I)=μ(I)−dim(S).

**Source.** Craig Huneke, Claudia Polini and Bernd Ulrich. *Restrictions on the Betti tables of licci ideals*. 2026. [primary source](https://arxiv.org/abs/2608.06019v1) Location: Conjecture 1.3, p. 3.

**Literature check.** Status checked 10 October 2026: Current v1 proves several special cases, retaining the general conjecture. Its graded and squarefree consequences are not separately counted; no later resolution found.

**Further links.** [1](https://arxiv.org/abs/2606.11467v1)


<a id="q4262"></a>

## Q4262. For every J and post-Nichols algebra R over J, is R left Noetherian exactly when R is affine…

**Status:** Open · **Kind:** conjecture (Conjecture 22) · **Collection** 43

For every J and post-Nichols algebra R over J, is R left Noetherian exactly when R is affine with finite GKdim?

**Context.** Work over algebraically closed k of characteristic zero; J,H,K,M denote Hopf algebras with bijective antipodes. Affine means finitely generated as an algebra; GKdim denotes Gelfand–Kirillov dimension. A post-Nichols algebra R=⊕R_n is a connected, coradically graded braided Hopf algebra in the left-left Yetter–Drinfeld category over J, with R_1=V. Write # for bosonization (Radford biproduct). The diagram of pointed H is R in its coradical graded decomposition gr H=R#kG(H).

**Source.** Nicolás Andruskiewitsch, István Heckenberger and Leandro Vendramin. *On Noetherian pointed Hopf algebras*. 2026. [primary source](https://arxiv.org/abs/2608.15856v1) Location: Conjecture 22, pp.4–5,18–20.

**Literature check.** Status: No later matching resolution found, 10 October2026.


<a id="q4263"></a>

## Q4263. Is the diagram of every pointed Noetherian affine H with polycyclic-by-finite G(H) affine?

**Status:** Open · **Kind:** open problem (Problem 53) · **Collection** 43

Is the diagram of every pointed Noetherian affine H with polycyclic-by-finite G(H) affine?

**Context.** Work over algebraically closed k of characteristic zero; J,H,K,M denote Hopf algebras with bijective antipodes. Affine means finitely generated as an algebra; GKdim denotes Gelfand–Kirillov dimension. A post-Nichols algebra R=⊕R_n is a connected, coradically graded braided Hopf algebra in the left-left Yetter–Drinfeld category over J, with R_1=V. Write # for bosonization (Radford biproduct). The diagram of pointed H is R in its coradical graded decomposition gr H=R#kG(H).

**Source.** Nicolás Andruskiewitsch, István Heckenberger and Leandro Vendramin. *On Noetherian pointed Hopf algebras*. 2026. [primary source](https://arxiv.org/abs/2608.15856v1) Location: Problem 53, pp.4–5,18–20.

**Literature check.** Status: No later matching resolution found, 10 October2026.


<a id="q4264"></a>

## Q4264. If M is Noetherian and its coradical M_0 is a Hopf subalgebra with finite GKdim, must GKdim M be…

**Status:** Open · **Kind:** open problem (Question 65) · **Collection** 43

If M is Noetherian and its coradical M_0 is a Hopf subalgebra with finite GKdim, must GKdim M be finite?

**Context.** Work over algebraically closed k of characteristic zero; J,H,K,M denote Hopf algebras with bijective antipodes. Affine means finitely generated as an algebra; GKdim denotes Gelfand–Kirillov dimension. A post-Nichols algebra R=⊕R_n is a connected, coradically graded braided Hopf algebra in the left-left Yetter–Drinfeld category over J, with R_1=V. Write # for bosonization (Radford biproduct). The diagram of pointed H is R in its coradical graded decomposition gr H=R#kG(H).

**Source.** Nicolás Andruskiewitsch, István Heckenberger and Leandro Vendramin. *On Noetherian pointed Hopf algebras*. 2026. [primary source](https://arxiv.org/abs/2608.15856v1) Location: Question 65, pp.4–5,18–20.

**Literature check.** Status: No later matching resolution found, 10 October2026.


<a id="q4265"></a>

## Q4265. If K is cosemisimple and R is an affine post-Nichols algebra over K, both Noetherian, must R#K…

**Status:** Open · **Kind:** open problem (Question 69) · **Collection** 43

If K is cosemisimple and R is an affine post-Nichols algebra over K, both Noetherian, must R#K be Noetherian?

**Context.** Work over algebraically closed k of characteristic zero; J,H,K,M denote Hopf algebras with bijective antipodes. Affine means finitely generated as an algebra; GKdim denotes Gelfand–Kirillov dimension. A post-Nichols algebra R=⊕R_n is a connected, coradically graded braided Hopf algebra in the left-left Yetter–Drinfeld category over J, with R_1=V. Write # for bosonization (Radford biproduct). The diagram of pointed H is R in its coradical graded decomposition gr H=R#kG(H).

**Source.** Nicolás Andruskiewitsch, István Heckenberger and Leandro Vendramin. *On Noetherian pointed Hopf algebras*. 2026. [primary source](https://arxiv.org/abs/2608.15856v1) Location: Question 69, pp.4–5,18–20.

**Literature check.** Status: No later matching resolution found, 10 October2026.


<a id="q4266"></a>

## Q4266. Over any field k, let K be a finite-dimensional Hopf algebra and R a finite-dimensional braided…

**Status:** Open · **Kind:** open problem (Question 1.1) · **Collection** 43

Over any field k, let K be a finite-dimensional Hopf algebra and R a finite-dimensional braided Hopf algebra in the category of left-left Yetter–Drinfeld modules over K. For an augmented algebra A, write fgc when Ext\*\_A(k,k) is finitely generated as a k-algebra and Ext\*\_A(k,M) is finitely generated over it for every finitely generated A-module M. If K and R have fgc, must their Radford bosonization R#K have fgc?

**Context.** Earlier antecedent: Andruskiewitsch–Natale, On the finite generation of the cohomology of abelian extensions of Hopf algebras, §4.1, asks the semisimple-K case. No matching resolution located through 10 October 2026.

**Source.** Nicolás Andruskiewitsch, David Jaklitsch, Van C. Nguyen, Amrei Oswald, Julia Plavnik, Anne V. Shepler and Xingting Wang. *On the finite generation of the cohomology of bosonizations*. 2025. [primary source](https://doi.org/10.1016/j.jalgebra.2025.10.057) Location: Question 1.1, full author manuscript dated 11 November 2025, p.1; the published introduction preview reaffirms this exact question.

**Literature check.** Status: Earlier antecedent: Andruskiewitsch–Natale, On the finite generation of the cohomology of abelian extensions of Hopf algebras, §4.1, asks the semisimple-K case. No matching resolution located through 10 October 2026.


<a id="q4339"></a>

## Q4339. Determine d_mat(S) for every numerical semigroup of multiplicity m(S)=4.

**Status:** Open · **Kind:** open problem · **Collection** 44

Determine d_mat(S) for every numerical semigroup of multiplicity m(S)=4.

**Context.** A numerical semigroup is an additive submonoid S⊆N={0,1,…} with finite complement. Put m(S)=min(S∖{0}). For A∈M_d(Q), set S(A)={n≥0:A^n∈M_d(Z)} and d_mat(S)=min{d≥1:∃A∈M_d(Q), S(A)=S}. Paper origins: Q4339, IV (17 October 2025); Q4340, Arsh Chhabra and Stephan Ramon Garcia, Numerical semigroups from rational matrices III, arXiv:2506.11554v1 (13 June 2025), Problem8.2. No dissertation-origin claim. Status checked 11 October 2026: current arXiv v1 and the paginated publisher final retain both problems; the paper settles multiplicities at most3. No matching later resolution located.

**Source.** Theo Chinn, Junshu Feng, Stephan Ramon Garcia and Peiting Jiang. *Numerical semigroups from rational matrices IV: computation of the matricial dimensions of numerical semigroups with small Frobenius number or genus*. 2026. [primary source](https://arxiv.org/abs/2510.15209v1) Location: Problems 6.2–6.3, p.347; definitions, pp.333–334.

**Literature check.** Status: Paper origins: Q4339, IV (17 October 2025); Q4340, Arsh Chhabra and Stephan Ramon Garcia, Numerical semigroups from rational matrices III, arXiv:2506.11554v1 (13 June 2025), Problem8.2. No dissertation-origin claim. Status checked 11 October 2026: current arXiv v1 and the paginated publisher final retain both problems; the paper settles multiplicities at most3. No matching later resolution located.

**Further links.** [1](https://doi.org/10.1017/S0004972726101063) · [2](https://arxiv.org/abs/2506.11554v1)


<a id="q4340"></a>

## Q4340. Determine d_mat(⟨5,7,16,18⟩), where brackets mean the additive semigroup generated by these…

**Status:** Open · **Kind:** open problem · **Collection** 44

Determine d_mat(⟨5,7,16,18⟩), where brackets mean the additive semigroup generated by these integers. The known bounds are 3≤d_mat≤5.

**Context.** A numerical semigroup is an additive submonoid S⊆N={0,1,…} with finite complement. Put m(S)=min(S∖{0}). For A∈M_d(Q), set S(A)={n≥0:A^n∈M_d(Z)} and d_mat(S)=min{d≥1:∃A∈M_d(Q), S(A)=S}. Paper origins: Q4339, IV (17 October 2025); Q4340, Arsh Chhabra and Stephan Ramon Garcia, Numerical semigroups from rational matrices III, arXiv:2506.11554v1 (13 June 2025), Problem8.2. No dissertation-origin claim. Status checked 11 October 2026: current arXiv v1 and the paginated publisher final retain both problems; the paper settles multiplicities at most3. No matching later resolution located.

**Source.** Theo Chinn, Junshu Feng, Stephan Ramon Garcia and Peiting Jiang. *Numerical semigroups from rational matrices IV: computation of the matricial dimensions of numerical semigroups with small Frobenius number or genus*. 2026. [primary source](https://arxiv.org/abs/2510.15209v1) Location: Problems 6.2–6.3, p.347; definitions, pp.333–334.

**Literature check.** Status: Paper origins: Q4339, IV (17 October 2025); Q4340, Arsh Chhabra and Stephan Ramon Garcia, Numerical semigroups from rational matrices III, arXiv:2506.11554v1 (13 June 2025), Problem8.2. No dissertation-origin claim. Status checked 11 October 2026: current arXiv v1 and the paginated publisher final retain both problems; the paper settles multiplicities at most3. No matching later resolution located.

**Further links.** [1](https://doi.org/10.1017/S0004972726101063) · [2](https://arxiv.org/abs/2506.11554v1)


<a id="q4341"></a>

## Q4341. For every odd prime p and finite p-group G, must cl(G)≤b(G)+1, where cl(G) is the nilpotency…

**Status:** Open · **Kind:** open problem · **Collection** 44

For every odd prime p and finite p-group G, must cl(G)≤b(G)+1, where cl(G) is the nilpotency class and b(G)=max_{g∈G}log_p[G:C_G(g)], with C_G(g) the centralizer of g?

**Context.** Origin: the odd-prime residual of Leedham-Green, P. Neumann and Wiegold’s 1969 class–breadth conjecture; counterexamples exist at p=2. This is not Skutin’s stronger relative-group conjecture.

**Source.** Alexander A. Skutin. *On the class-breadth conjecture for p>2-groups*. 2026. [primary source](https://arxiv.org/abs/2606.13423v1) Location: introductory conjecture and definition, p.1.

**Literature check.** Status checked 11 October 2026: current v1 explicitly leaves the unrestricted odd-prime case open. Its additional-hypothesis theorem is partial; the 2026 Eick–Fernández Ayala results concern algebras and torsion-free nilpotent groups. No matching resolution located.

**Further links.** [1](https://doi.org/10.1016/j.jalgebra.2025.04.023)


<a id="q4351"></a>

## Q4351. Hyperbolicity and complete monotonicity

**Status:** Open · **Kind:** open problem (Question 5.1) · **Collection** 44

After one overall sign choice, must f=q/p satisfy (−1)^rD_v₁⋯D_vᵣf(x)≥0 for every r≥0 and x,v₁,…,vᵣ∈C?

**Context.** Doctoral connection: Elia Mazzucchelli, Positive Singularities and Volumes in Scattering Amplitudes, LMU Munich physics doctorate; supervisor Johannes M. Henn; defended 16 July 2026; deposited 4 August 2026. Paper-stated question; thesis treats multiple-conic cases. Setup: Let (P^m,P) be a projective positive geometry with P full-dimensional, quasi-compact, open and semialgebraic: its unique canonical rational top form Ω\_P has only logarithmic boundary poles with recursively canonical residues, normalized to ±1 at points. Write Ω\_P=(q/p)dx with standard homogeneous projective volume form. Suppose P is a hyperbolicity region of its algebraic boundary p=0: the open pointed cone C over P is a hyperbolicity cone of p, so p(e)>0 and t↦p(x+te) has only real zeros for every x∈R^(m+1) and e∈C.

**Source.** Elia Mazzucchelli and Prashanth Raman. *Canonical Forms as Dual Volumes*. 2025. [primary source](https://arxiv.org/abs/2509.02239v1) Location: Mazzucchelli–Prashanth Raman, Canonical Forms as Dual Volumes, arXiv:2509.02239v1, Question 5.1, p.33; Definitions2.1,2.3,3.1,3.18.

**Literature check.** Status checked 11 October 2026: the converse is proved; the paper retains the question; the thesis leaves the general case open.

**Further links.** [1](https://edoc.ub.uni-muenchen.de/37510/)


<a id="q4352"></a>

## Q4352. Two-unitary involutions in dimensions nine and thirty-six

**Status:** Open · **Kind:** open problem · **Collection** 44

For each d∈{3,6}, does there exist a complex array (u_ijkl), 0≤i,j,k,l&lt;d, whose three d²×d² flattenings with row/column indices (ij,kl), (ik,jl), and (il,kj) are all unitary, and whose first flattening U satisfies U²=I and U≠I?

**Context.** Student: Paulina L. A. Goedicke. Thesis: Perfect Tensors from Multiple Angles and (Quantum) Combinatorial Structures in Category Theory, University of Cologne, Dr. rer. nat.; cover 2025, oral examination 16 January 2026, deposited 23 January 2026. Primary advisor unverified; David Gross and Karol Życzkowski are explicitly identified as referees, not necessarily primary advisors.

**Source.** Paulina L. A. Goedicke. *Perfect Tensors from Multiple Angles and (Quantum) Combinatorial Structures in Category Theory*. University of Cologne, 2025. [primary source](https://kups.ub.uni-koeln.de/79668/) Location: thesis §3.4.1, pp.129–131, and conclusion p.157; Definition 2.17 and equations(2.23)–(2.25), p.20.

**Literature check.** Status checked 11 October 2026: the thesis explicitly leaves both dimensions open; its order-three constructions do not answer this involution question. The related Gross–Goedicke arXiv:2504.15401v2 and later searches yielded no order-two resolution. The two dimensions are retained together as one question.

**Further links.** [1](https://arxiv.org/abs/2504.15401v2)


<a id="q4353"></a>

## Q4353. The two-element condition for simple groups

**Status:** Open · **Kind:** open problem (Question 8.3) · **Collection** 44

For every finite nonabelian simple group G and every conjugacy class C⊆G, do there exist x,y,a₀,a₁∈C and an odd-order h∈G such that {a∈C:axa⁻¹=y}={a₀,a₁} and ha₀h⁻¹=a₁? The elements a₀,a₁ may coincide.

**Context.** Doctoral connection: Charlotte Roelants is a current Vrije Universiteit Brussel PhD candidate; her homepage and advisor’s team page identify supervisors Leandro Vendramin and Kevin Piterman. No completed dissertation is asserted.

**Source.** Carsten Dietzel and Charlotte Roelants. *Non-degeneracy of Killing forms on real conjugacy classes of finite groups*. [primary source](https://arxiv.org/abs/2605.30408v1) Location: Carsten Dietzel–Charlotte Roelants, Non-degeneracy of Killing forms on real conjugacy classes of finite groups, arXiv:2605.30408v1, Question 8.3, p.23; condition(2EC), p.2.

**Literature check.** Status checked 11 October 2026: the May 2026 preprint retains the question. Computations cover all conjugacy classes for |G|≤10⁸, and real classes for |G|≤10⁹; these do not settle unrestricted G. The weaker real-class question and the resulting Killing-form conjecture are not counted separately.

**Further links.** [1](https://sites.google.com/view/charlotteroelants/home) · [2](https://leandrovendramin.org/team/)


<a id="q4358"></a>

## Q4358. Let K be a commutative unital ring, R a unital associative K-algebra whose additive commutators…

**Status:** Open · **Kind:** open problem (Question 7) · **Collection** 44

Let K be a commutative unital ring, R a unital associative K-algebra whose additive commutators generate R as a two-sided ideal, and f∈K⟨x₁,…,x_t⟩. For integer n>1, set P={b₁⋯b_n:b_i∈f(R)}, where f(R) consists of all evaluations on R. If the additive subgroup generated by P is R, must some integer N≥1 satisfy R={a₁+⋯+a_N:a_i∈P}?

**Context.** Doctoral connection: Trần Nam Sơn, Images of polynomials on certain classes of algebras, VNUHCM University of Science; defended 28 March 2026 under Mai Hoàng Biên. Award and deposit dates unverified. Questions below are paper-stated. Source: Tsiu-Kwen Lee–Tran Nam Son, On the structural behavior of images of polynomials, arXiv:2605.04464v1, Questions 7 and 16, pp.5,10; definitions pp.1,3,5. Origin: Q4359 is the remaining case of Brešar–Gardella–Thiel’s Question 4.6 (2024 preprint; 2025 final).

**Source.** Tsiu-Kwen Lee and Tran Nam Son. *On the structural behavior of images of polynomials*. [primary source](https://arxiv.org/abs/2605.04464v1) Location: Question 7, p.5.

**Literature check.** Status checked 11 October 2026: current v1 retains both. Theorem 8 handles multilinear f; Theorem 17 handles |F|>n. No general resolution or newer final found.

**Further links.** [1](https://en.hcmus.edu.vn/doctoral-thesis-defence-researcher-tran-nam-son-successfully-defends-doctoral-thesis-in-algebra-and-number-theory/) · [2](https://doi.org/10.4153/S0008439524000523)


<a id="q4359"></a>

## Q4359. For every division ring D infinite-dimensional over its finite center F, every n≥3 and every…

**Status:** Open · **Kind:** open problem (Question 16) · **Collection** 44

For every division ring D infinite-dimensional over its finite center F, every n≥3 and every A∈GL_n(D), do B,C,E,H∈M_n(D) exist with A=(BC−CB)(EH−HE)?

**Context.** Doctoral connection: Trần Nam Sơn, Images of polynomials on certain classes of algebras, VNUHCM University of Science; defended 28 March 2026 under Mai Hoàng Biên. Award and deposit dates unverified. Questions below are paper-stated. Source: Tsiu-Kwen Lee–Tran Nam Son, On the structural behavior of images of polynomials, arXiv:2605.04464v1, Questions 7 and 16, pp.5,10; definitions pp.1,3,5. Origin: Q4359 is the remaining case of Brešar–Gardella–Thiel’s Question 4.6 (2024 preprint; 2025 final).

**Source.** Tsiu-Kwen Lee and Tran Nam Son. *On the structural behavior of images of polynomials*. [primary source](https://arxiv.org/abs/2605.04464v1) Location: Question 16, p.10.

**Literature check.** Status checked 11 October 2026: current v1 retains both. Theorem 8 handles multilinear f; Theorem 17 handles |F|>n. No general resolution or newer final found.

**Further links.** [1](https://en.hcmus.edu.vn/doctoral-thesis-defence-researcher-tran-nam-son-successfully-defends-doctoral-thesis-in-algebra-and-number-theory/) · [2](https://doi.org/10.4153/S0008439524000523)


<a id="q4435"></a>

## Q4435. Separability of derived centers

**Status:** Open · **Kind:** open problem · **Collection** 45

If A is separable, must Z(A) be separable?

**Context.** Setup: C is an additive presentably symmetric monoidal ∞-category; tensor product preserves colimits separately. An associative algebra A is separable when multiplication A⊗A^op→A has an A-bimodule section. Write Z(A)=Hom_{A⊗A^op}(A,A) for its internal derived center. A is Azumaya when its left-module category is invertible among presentable C-module categories under relative tensor product.

**Source.** Maxime Ramzi. *Separability in homotopy theory and topological Hochschild homology*. University of Copenhagen, 2024. Advisor(s): Jesper Grodal and Markus Land. [primary source](https://web.math.ku.dk/~jg/students/ramzi-phdthesis.pdf) Location: Questions 2.0.1 and 3.3.1, pp.75,94.

**Literature check.** Status checked 11 October 2026: Thesis and current precursor retain both; the author lists the work as submitted. Special cases do not settle arbitrary C.

**Further links.** [1](https://arxiv.org/abs/2305.17236v2)


<a id="q4436"></a>

## Q4436. Central separable algebras

**Status:** Open · **Kind:** open problem · **Collection** 45

If A is separable, dualizable in C, and the unit map 1_C→Z(A) is an equivalence, must A be Azumaya?

**Context.** Setup: C is an additive presentably symmetric monoidal ∞-category; tensor product preserves colimits separately. An associative algebra A is separable when multiplication A⊗A^op→A has an A-bimodule section. Write Z(A)=Hom_{A⊗A^op}(A,A) for its internal derived center. A is Azumaya when its left-module category is invertible among presentable C-module categories under relative tensor product.

**Source.** Maxime Ramzi. *Separability in homotopy theory and topological Hochschild homology*. University of Copenhagen, 2024. Advisor(s): Jesper Grodal and Markus Land. [primary source](https://web.math.ku.dk/~jg/students/ramzi-phdthesis.pdf) Location: Questions 2.1.13 and 3.3.2, pp.80,94. Thesis questions already posed in the 2023 paper Separability in homotopical algebra, arXiv:2305.17236v2, Questions 6.1,6.14.

**Literature check.** Status checked 11 October 2026: Thesis and current precursor retain both; the author lists the work as submitted. Special cases do not settle arbitrary C.

**Further links.** [1](https://arxiv.org/abs/2305.17236v2)


<a id="q4438"></a>

## Q4438. One Frobenius Tor vanishing

**Status:** Open · **Kind:** open problem (Question 7.1.4) · **Collection** 45

If char(R)=p>0, M has finite CI-dimension, and Tor_i^R(M,{}^nR)=0 for some i,n>0, must pd_R(M)<∞?

**Context.** Setup: R is commutative Noetherian local; modules are finitely generated. Finite CI-dimension means some local diagram R→R′←Q has R→R′ flat, Q→R′ surjective with regular-sequence kernel, and pd_Q(M⊗\_R R′)<∞. For characteristic p>0, {}^nR has scalar action r·s=r^{p^n}s. Origin: Chapter 7 is joint work with Anna Brosowsky and Thomas Marley; Chapter 6 follows Martins–Mendoza Rubio–Nason, arXiv:2601.07811.

**Source.** Victor Daniel Mendoza Rubio. *A study concerning the finiteness of homological dimensions*. University of São Paulo, São Carlos, 2026. Advisor(s): Victor Hugo Jorge Pérez. [primary source](https://teses.usp.br/teses/disponiveis/55/55135/tde-10092026-125601/en.html) Location: Question 7.1.4, p. 96.

**Literature check.** Status checked 11 October 2026: retained in the revised thesis; known Frobenius results impose additional conditions.

**Further links.** [1](https://arxiv.org/abs/2601.07811)


<a id="q4439"></a>

## Q4439. Eventual Frobenius Tor vanishing (equivalent local formulation)

**Status:** Open · **Kind:** open problem (Question 7.4.6) · **Collection** 45

If char(R)=p>0 and Tor_i^R(M,{}^nR)=0 for all sufficiently large i, for one n>0, must pd_R(M)<∞?

**Context.** Setup: R is commutative Noetherian local; modules are finitely generated. Finite CI-dimension means some local diagram R→R′←Q has R→R′ flat, Q→R′ surjective with regular-sequence kernel, and pd_Q(M⊗\_R R′)<∞. For characteristic p>0, {}^nR has scalar action r·s=r^{p^n}s. Origin: Chapter 7 is joint work with Anna Brosowsky and Thomas Marley; Chapter 6 follows Martins–Mendoza Rubio–Nason, arXiv:2601.07811.

**Source.** Victor Daniel Mendoza Rubio. *A study concerning the finiteness of homological dimensions*. University of São Paulo, São Carlos, 2026. Advisor(s): Victor Hugo Jorge Pérez. [primary source](https://teses.usp.br/teses/disponiveis/55/55135/tde-10092026-125601/en.html) Location: Question 7.4.6, p. 102.

**Literature check.** Status checked 11 October 2026: retained in the revised thesis; known Frobenius results impose additional conditions.

**Further links.** [1](https://arxiv.org/abs/2601.07811)


<a id="q4440"></a>

## Q4440. Direct sums and complete-intersection dimension

**Status:** Open · **Kind:** open problem · **Collection** 45

If M,N have finite CI-dimension, must M⊕N also?

**Context.** Setup: R is commutative Noetherian local; modules are finitely generated. Finite CI-dimension means some local diagram R→R′←Q has R→R′ flat, Q→R′ surjective with regular-sequence kernel, and pd_Q(M⊗\_R R′)<∞. For characteristic p>0, {}^nR has scalar action r·s=r^{p^n}s. Origin: Chapter 7 is joint work with Anna Brosowsky and Thomas Marley; Chapter 6 follows Martins–Mendoza Rubio–Nason, arXiv:2601.07811.

**Source.** Victor Daniel Mendoza Rubio. *A study concerning the finiteness of homological dimensions*. University of São Paulo, São Carlos, 2026. Advisor(s): Victor Hugo Jorge Pérez. [primary source](https://teses.usp.br/teses/disponiveis/55/55135/tde-10092026-125601/en.html) Location: Remark 6.3.1, p. 78.

**Literature check.** Status checked 11 October 2026: retained in the revised thesis; known Frobenius results impose additional conditions.

**Further links.** [1](https://arxiv.org/abs/2601.07811)


<a id="q4441"></a>

## Q4441. Failure of the spectral analogue

**Status:** Open · **Kind:** open problem · **Collection** 45

Classify finite groups G admitting B such that, for every integer N≥1 and every 0≤m≤N, B^m∘B̃^{N−m} is not the constant map with value e.

**Context.** Setup: A Rota–Baxter operator on a group G is a map B:G→G satisfying B(g)B(h)=B(gB(g)hB(g)^{-1}) for all g,h. Put B̃(g)=g^{-1}B(g^{-1}). Powers below mean repeated composition, with zeroth power the identity. Locator: §5.1, p. 22; definitions, pp. 1 and 3.

**Source.** Andrey Savelyev. *Rota–Baxter operators on extraspecial groups*. 2026. [primary source](https://arxiv.org/abs/2608.28291v1) Location: §5.1, p. 22; definitions, pp. 1 and 3.

**Literature check.** Status checked 11 October 2026: current v1 retains both questions; Heisenberg and extraspecial constructions are partial results, not classifications for all finite groups.

**Further links.** [1](https://arxiv.org/abs/2608.28291)


<a id="q4442"></a>

## Q4442. Two bijective operators

**Status:** Open · **Kind:** open problem · **Collection** 45

Classify finite groups G admitting B for which both B and B̃ are bijections.

**Context.** Setup: A Rota–Baxter operator on a group G is a map B:G→G satisfying B(g)B(h)=B(gB(g)hB(g)^{-1}) for all g,h. Put B̃(g)=g^{-1}B(g^{-1}). Powers below mean repeated composition, with zeroth power the identity. Locator: §5.1, p. 22; definitions, pp. 1 and 3.

**Source.** Andrey Savelyev. *Rota–Baxter operators on extraspecial groups*. 2026. [primary source](https://arxiv.org/abs/2608.28291v1) Location: §5.1, p. 22; definitions, pp. 1 and 3.

**Literature check.** Status checked 11 October 2026: current v1 retains both questions; Heisenberg and extraspecial constructions are partial results, not classifications for all finite groups.

**Further links.** [1](https://arxiv.org/abs/2608.28291)


<a id="q4445"></a>

## Q4445. Two equations set-theoretically

**Status:** Open · **Kind:** open problem · **Collection** 45

In characteristic zero, is every P_n the radical of an ideal generated by two elements of k[[x,y,z]]?

**Context.** Setup: For n≥3, put a=n(n−1)/2 and q=2⌊(n+1)/2⌋−1. Over a field k, let P_n be the kernel of k[[x,y,z]]→k[[t]] sending x↦t^a(1+t^q), y↦t^{a+1}, z↦t^{a+2}. Write μ(I) for the minimal number of generators of I. Locator: §6.1, pp. 141–143; defining map, §5.2.

**Source.** Laura González Hernández. *On families of prime ideals with an unbounded minimal number of generators in a three-dimensional power series ring*. Universitat Politècnica de Catalunya, 2026. Advisor(s): Francesc d’Assís Planas Vilanova. [primary source](https://hdl.handle.net/2117/460106) Location: §6.1, pp. 141–143; defining map, §5.2.

**Literature check.** Status checked 11 October 2026: the April 2026 companion arXiv:2604.00638 still poses the intersection and characteristic problems; the characteristic-three equality remains computational evidence in the thesis.

**Further links.** [1](https://arxiv.org/abs/2604.00638)


<a id="q4446"></a>

## Q4446. The characteristic-three subfamily

**Status:** Open · **Kind:** open problem · **Collection** 45

In characteristic three, does μ(P_{3^m+3})=3^m+3 for every integer m≥0?

**Context.** Setup: For n≥3, put a=n(n−1)/2 and q=2⌊(n+1)/2⌋−1. Over a field k, let P_n be the kernel of k[[x,y,z]]→k[[t]] sending x↦t^a(1+t^q), y↦t^{a+1}, z↦t^{a+2}. Write μ(I) for the minimal number of generators of I. Locator: §6.1, pp. 141–143; defining map, §5.2.

**Source.** Laura González Hernández. *On families of prime ideals with an unbounded minimal number of generators in a three-dimensional power series ring*. Universitat Politècnica de Catalunya, 2026. Advisor(s): Francesc d’Assís Planas Vilanova. [primary source](https://hdl.handle.net/2117/460106) Location: §6.1, pp. 141–143; defining map, §5.2.

**Literature check.** Status checked 11 October 2026: the April 2026 companion arXiv:2604.00638 still poses the intersection and characteristic problems; the characteristic-three equality remains computational evidence in the thesis.

**Further links.** [1](https://arxiv.org/abs/2604.00638)


<a id="q4447"></a>

## Q4447. Unbounded generators in positive characteristic

**Status:** Open · **Kind:** open problem · **Collection** 45

For every field k of positive characteristic, are the numbers μ(P), for prime ideals P⊂k[[x,y,z]], unbounded?

**Context.** Setup: For n≥3, put a=n(n−1)/2 and q=2⌊(n+1)/2⌋−1. Over a field k, let P_n be the kernel of k[[x,y,z]]→k[[t]] sending x↦t^a(1+t^q), y↦t^{a+1}, z↦t^{a+2}. Write μ(I) for the minimal number of generators of I. Locator: §6.1, pp. 141–143; defining map, §5.2.

**Source.** Laura González Hernández. *On families of prime ideals with an unbounded minimal number of generators in a three-dimensional power series ring*. Universitat Politècnica de Catalunya, 2026. Advisor(s): Francesc d’Assís Planas Vilanova. [primary source](https://hdl.handle.net/2117/460106) Location: §6.1, pp. 141–143; defining map, §5.2.

**Literature check.** Status checked 11 October 2026: the April 2026 companion arXiv:2604.00638 still poses the intersection and characteristic problems; the characteristic-three equality remains computational evidence in the thesis.

**Further links.** [1](https://arxiv.org/abs/2604.00638)


<a id="q4457"></a>

## Q4457. Brace additivity versus the operadic center

**Status:** Open · **Kind:** conjecture (Conjecture 5.4.29) · **Collection** 45

Over a characteristic-zero field k, let P be a binary quadratic Koszul dg operad in nonpositive cochain degrees, C=P¡ its Koszul-dual cooperad, and A a dg P-algebra with structure twisting element α. Assume C has an admissible Hopf-counital structure: its conilpotent coalgebras, with Koszul weak equivalences, form a symmetric monoidal model category. Fix a compatible Hopf-cooperad map coCom_nc→C. Write C_cu for the counital extension, adding k in arity zero. Give T=Conv(C_cu,End_A)^α its canonical C-brace structure. Does Safronov’s additivity construction, transported through Bar–Cobar equivalence, give add(T)≃Z(A) as E₁-algebras in Alg_P(D(k))? Here Z(A) is the universal operadic center, and Alg_P(D(k)) carries the transported monoidal structure.

**Context.** Student: Sonja Maria Farr, University of Nevada, Reno, PhD 2026; advisor Christopher Rogers. Thesis: Derived operadic centers in algebraic geometry and deformation quantization, Conjecture 5.4.29, p.97; setup pp.90–96. Over a characteristic-zero field k, let P be a binary quadratic Koszul dg operad in nonpositive cochain degrees, C=P¡ its Koszul-dual cooperad, and A a dg P-algebra with structure twisting element α. Assume C has an admissible Hopf-counital structure: its conilpotent coalgebras, with Koszul weak equivalences, form a symmetric monoidal model category. Fix a compatible Hopf-cooperad map coCom_nc→C. Write C_cu for the counital extension, adding k in arity zero. Give T=Conv(C_cu,End_A)^α its canonical C-brace structure. Does Safronov’s additivity construction, transported through Bar–Cobar equivalence, give add(T)≃Z(A) as E₁-algebras in Alg_P(D(k))? Here Z(A) is the universal operadic center, and Alg_P(D(k)) carries the transported monoidal structure.

**Source.** Sonja Maria Farr. *Derived operadic centers in algebraic geometry and deformation quantization*. University of Nevada, Reno, 2026. Advisor(s): Christopher Rogers. [primary source](https://arxiv.org/abs/2607.05455) Location: Conjecture 5.4.29, p.97; setup pp.90–96.

**Literature check.** Status checked 11 October 2026: The current thesis retains the conjecture; the earlier paper establishes Gerstenhaber operations, not this full comparison.

**Further links.** [1](https://sonjafarr.com/cv.pdf)


<a id="q4461"></a>

## Q4461. Is the log canonical threshold of J_G at the origin equal to P(G) for every G?

**Status:** Open · **Kind:** conjecture (Conjecture 1.3) · **Collection** 45

Is the log canonical threshold of J_G at the origin equal to P(G) for every G?

**Context.** Origin: Adam LaClair, Invariants of binomial edge ideals via linear programs, Journal of Algebraic Combinatorics62:16 (2025), first preprint2023. Field: Commutative algebra; graph optimization. Doctoral connection: LaClair, Purdue PhD2025, advisor Uli Walther; paper-origin questions. For a finite simple graph G on [n], put J_G=(x_i y_j−x_j y_i:{i,j}∈E(G))⊂C[x_1,…,x_n,y_1,…,y_n]. Let P(G) maximize Σ\_{e∈E(G)}w_e over rational w_e≥0, subject to Σ\_{e∈E(G[U])}w_e≤|U|−1 for every U⊆V(G) with |U|≥2, and Σ\_{e∋v}w_e≤2 for every vertex v. G[U] denotes the induced subgraph. Locator: Final Conjecture1.3(1)/(2), p5; program(4), p4; threshold convention p3. Checked11October2026: the publisher’s final retains both parts, proving block-graph and König-type cases. The two assertions concern, respectively, equality with a singularity invariant and arithmetic of the optimization value.

**Source.** Adam LaClair. *Invariants of binomial edge ideals via linear programs*. 2025. [primary source](https://doi.org/10.1007/s10801-025-01439-x) Location: Conjecture 1.3(1), p.5.


<a id="q4462"></a>

## Q4462. Is P(G) always dyadic rational, that is, an element of Z[1/2]?

**Status:** Open · **Kind:** conjecture (Conjecture 1.3) · **Collection** 45

Is P(G) always dyadic rational, that is, an element of Z[1/2]?

**Context.** Origin: Adam LaClair, Invariants of binomial edge ideals via linear programs, Journal of Algebraic Combinatorics62:16 (2025), first preprint2023. Field: Commutative algebra; graph optimization. Doctoral connection: LaClair, Purdue PhD2025, advisor Uli Walther; paper-origin questions. For a finite simple graph G on [n], put J_G=(x_i y_j−x_j y_i:{i,j}∈E(G))⊂C[x_1,…,x_n,y_1,…,y_n]. Let P(G) maximize Σ\_{e∈E(G)}w_e over rational w_e≥0, subject to Σ\_{e∈E(G[U])}w_e≤|U|−1 for every U⊆V(G) with |U|≥2, and Σ\_{e∋v}w_e≤2 for every vertex v. G[U] denotes the induced subgraph. Locator: Final Conjecture1.3(1)/(2), p5; program(4), p4; threshold convention p3. Checked11October2026: the publisher’s final retains both parts, proving block-graph and König-type cases. The two assertions concern, respectively, equality with a singularity invariant and arithmetic of the optimization value.

**Source.** Adam LaClair. *Invariants of binomial edge ideals via linear programs*. 2025. [primary source](https://doi.org/10.1007/s10801-025-01439-x) Location: Conjecture 1.3(2), p.5.


<a id="q4466"></a>

## Q4466. Central control of rational Iwasawa primes

**Status:** Open · **Kind:** conjecture (Conjecture A) · **Collection** 45

Let p be prime, K/Q_p finite, O its integer ring, and G a nilpotent p-valuable group: G is complete for a p-valuation ω:G→R∪{∞} and gr_ωG has finite rank over F_p[t], where gr_ωG=⊕\_r G_r/G_{r+}, G_r={g:ω(g)≥r}, G_{r+}={g:ω(g)>r}, and t is induced by pth powers. Such ω satisfies ω(g)=∞⇔g=1, ω(g)>1/(p−1), ω(gh⁻¹)≥min{ω(g),ω(h)}, ω([g,h])≥ω(g)+ω(h), and ω(g^p)=ω(g)+1. Put KG=K⊗\_O \varprojlim_U O[G/U], over open normal U≤G, and Z=Z(G). For every two-sided prime ideal P⊂KG with {g∈G:g−1∈P}={1}, must P=(P∩KZ)KG?

**Context.** Doctoral connection: Jones, Prime ideals of Iwasawa algebras over solvable groups, Oxford DPhil 2020, advisor Konstantin Ardakov. Earlier conjecture, reaffirmed in this paper. Let p be prime, K/Q_p finite, O its integer ring, and G a nilpotent p-valuable group: G is complete for a p-valuation ω:G→R∪{∞} and gr_ωG has finite rank over F_p[t], where gr_ωG=⊕\_r G_r/G_{r+}, G_r={g:ω(g)≥r}, G_{r+}={g:ω(g)>r}, and t is induced by pth powers. Such ω satisfies ω(g)=∞⇔g=1, ω(g)>1/(p−1), ω(gh⁻¹)≥min{ω(g),ω(h)}, ω([g,h])≥ω(g)+ω(h), and ω(g^p)=ω(g)+1. Put KG=K⊗\_O \varprojlim_U O[G/U], over open normal U≤G, and Z=Z(G). For every two-sided prime ideal P⊂KG with {g∈G:g−1∈P}={1}, must P=(P∩KZ)KG? Checked 11 October 2026: current v1 and author page retain the preprint; primitive-ideal results and selected Lie-type cases leave this general question posed.

**Source.** Adam Jones and William Woods. *New directions in the study of prime ideals in rational, nilpotent Iwasawa algebras*. 2026. [primary source](https://arxiv.org/abs/2603.26626) Location: Conjecture A, pp.2–3; Definitions 2.2–2.5, pp.4–5.

**Further links.** [1](https://sites.google.com/view/adam-jones/home)


<a id="q4518"></a>

## Q4518. For every prime power q, determine the set of attainable values of ρ(C) for each parameter pair…

**Status:** Open · **Kind:** open problem · **Collection** 46

For every prime power q, determine the set of attainable values of ρ(C) for each parameter pair (n,d)∈{(5,3),(6,3),(6,4),(7,4)}.

**Context.** DL-S14 — Rank-metric coding theory Primary-paper source: Giuseppe Marino, Alessandro Neri and Alessia Vallefuoco, Covering radius of rank-metric codes via covering lifts and clubs, arXiv:2610.11926v1 (8 October 2026), §4.3 pp.23–25 and Table 4. Setup: Let q be a prime power and C≤F_{q^6}^n be a one-dimensional F_{q^6}-linear code. For x=(x_1,…,x_n), define wt_R(x)=dim_{F_q}span{x_1,…,x_n}. Its minimum rank distance is d=min_{0≠c∈C}wt_R(c), and its covering radius is ρ(C)=max_x min_{c∈C}wt_R(x−c).

**Source.** Giuseppe Marino, Alessandro Neri and Alessia Vallefuoco. *Covering radius of rank-metric codes via covering lifts and clubs*. 2026. [primary source](https://arxiv.org/abs/2610.11926) Location: §4.3 pp.23–25 and Table 4.

**Literature check.** Status checked 11 October 2026: the source identifies these four unresolved extension-degree-six cases. It confines the first radius to {3,4} and the other three to {4,5}; computations settle q=2,3, and constructions give some values for general q.

**Further links.** [1](https://arxiv.org/abs/2610.11926v1)


<a id="q4527"></a>

## Q4527. Which numbers occur as χ(Y) for finite semilattices Y?

**Status:** Open · **Kind:** open problem · **Collection** 46

Which numbers occur as χ(Y) for finite semilattices Y?

**Context.** Setup: Semigroups are nonempty and have multiplication only. Diag(S) consists of subsets of S×S containing every (s,s) and closed under componentwise multiplication. Cong(S) consists of those members that are equivalence relations. Call S DSC when Diag(S)=Cong(S). For finite S set χ(S)=|Cong(S)|/|Diag(S)|. A semilattice is a commutative idempotent semigroup. Checked 11 October 2026: current preprint retains the semilattice targets; the prior publisher final retains product closure. No matching later resolution located.

**Source.** Callum Barber and Nik Ruškuc. *Comparing Numbers of Diagonal Subsemigroups and Congruences for Semigroups*. 2026. [primary source](https://arxiv.org/abs/2602.17286) Location: §4, p.15; and Semigroup Congruences and Subsemigroups of the Direct Square, Bulletin of the Australian Mathematical Society 113 (2026), §5, p.133.

**Literature check.** Status: Checked 11 October 2026: current preprint retains the semilattice targets; the prior publisher final retains product closure. No matching later resolution located.

**Further links.** [1](https://doi.org/10.1017/S0004972725100166) · [2](https://arxiv.org/abs/2602.17286v2)


<a id="q4528"></a>

## Q4528. Does max{χ(Y):Y is an n-element semilattice} tend to zero as n→∞?

**Status:** Open · **Kind:** open problem · **Collection** 46

Does max{χ(Y):Y is an n-element semilattice} tend to zero as n→∞?

**Context.** Setup: Semigroups are nonempty and have multiplication only. Diag(S) consists of subsets of S×S containing every (s,s) and closed under componentwise multiplication. Cong(S) consists of those members that are equivalence relations. Call S DSC when Diag(S)=Cong(S). For finite S set χ(S)=|Cong(S)|/|Diag(S)|. A semilattice is a commutative idempotent semigroup. Checked 11 October 2026: current preprint retains the semilattice targets; the prior publisher final retains product closure. No matching later resolution located.

**Source.** Callum Barber and Nik Ruškuc. *Comparing Numbers of Diagonal Subsemigroups and Congruences for Semigroups*. 2026. [primary source](https://arxiv.org/abs/2602.17286) Location: §4, p.15; and Semigroup Congruences and Subsemigroups of the Direct Square, Bulletin of the Australian Mathematical Society 113 (2026), §5, p.133.

**Literature check.** Status: Checked 11 October 2026: current preprint retains the semilattice targets; the prior publisher final retains product closure. No matching later resolution located.

**Further links.** [1](https://doi.org/10.1017/S0004972725100166) · [2](https://arxiv.org/abs/2602.17286v2)


<a id="q4529"></a>

## Q4529. Must S×T be DSC whenever S and T are DSC semigroups?

**Status:** Open · **Kind:** open problem · **Collection** 46

Must S×T be DSC whenever S and T are DSC semigroups?

**Context.** Setup: Semigroups are nonempty and have multiplication only. Diag(S) consists of subsets of S×S containing every (s,s) and closed under componentwise multiplication. Cong(S) consists of those members that are equivalence relations. Call S DSC when Diag(S)=Cong(S). For finite S set χ(S)=|Cong(S)|/|Diag(S)|. A semilattice is a commutative idempotent semigroup. Checked 11 October 2026: current preprint retains the semilattice targets; the prior publisher final retains product closure. No matching later resolution located.

**Source.** Callum Barber and Nik Ruškuc. *Comparing Numbers of Diagonal Subsemigroups and Congruences for Semigroups*. 2026. [primary source](https://arxiv.org/abs/2602.17286) Location: §4, p.15; and Semigroup Congruences and Subsemigroups of the Direct Square, Bulletin of the Australian Mathematical Society 113 (2026), §5, p.133.

**Literature check.** Status: Checked 11 October 2026: current preprint retains the semilattice targets; the prior publisher final retains product closure. No matching later resolution located.

**Further links.** [1](https://doi.org/10.1017/S0004972725100166) · [2](https://arxiv.org/abs/2602.17286v2)


<a id="q4536"></a>

## Q4536. Detect inseparable linkage

**Status:** Open · **Kind:** open problem (Question 5.2) · **Collection** 46

Does ed(C₁,C₂)=2 for (C₁,C₂)∈LCA_{p,2}(F) force inseparable linkage?

**Context.** Fix algebraically closed k of prime characteristic p. For F/k, [a,b) is generated by x,y with x^p−x=a, y^p=b, yxy⁻¹=x+1, where a∈F,b∈F×. Let LCA_{p,n}(F) consist of tuples ([a,b₁),…,[a,bₙ)), up to componentwise isomorphism. Inseparably linked means admitting presentations with one common second slot. For a tuple T, ed(T) minimizes trdeg_k(E) over k⊂E⊂F permitting descent within LCA; ed_p(T) additionally permits finite extensions of F of degree prime to p. For the functor, take suprema over all F,T. Checked 11 October 2026: final published article retains both questions; no later resolution located.

**Source.** Adam Chapman and Kelly McKinnie. *Essential Dimension of Central Simple Algebras when the Characteristic is Bad*. 2026. [primary source](https://doi.org/10.65908/gja.2026.8103.1010) Location: Question 5.2, p8.

**Literature check.** Status: Checked 11 October 2026: final published article retains both questions; no later resolution located.


<a id="q4537"></a>

## Q4537. Linked-tuple dimension

**Status:** Open · **Kind:** open problem (Question 5.4) · **Collection** 46

For every prime p and integer n≥1, is ed(LCA_{p,n})=ed_p(LCA_{p,n})=n+1?

**Context.** Fix algebraically closed k of prime characteristic p. For F/k, [a,b) is generated by x,y with x^p−x=a, y^p=b, yxy⁻¹=x+1, where a∈F,b∈F×. Let LCA_{p,n}(F) consist of tuples ([a,b₁),…,[a,bₙ)), up to componentwise isomorphism. Inseparably linked means admitting presentations with one common second slot. For a tuple T, ed(T) minimizes trdeg_k(E) over k⊂E⊂F permitting descent within LCA; ed_p(T) additionally permits finite extensions of F of degree prime to p. For the functor, take suprema over all F,T. Checked 11 October 2026: final published article retains both questions; no later resolution located.

**Source.** Adam Chapman and Kelly McKinnie. *Essential Dimension of Central Simple Algebras when the Characteristic is Bad*. 2026. [primary source](https://doi.org/10.65908/gja.2026.8103.1010) Location: Question 5.4, p8.

**Literature check.** Status: Checked 11 October 2026: final published article retains both questions; no later resolution located.


<a id="q4545"></a>

## Q4545. Non-realizable tropical linear varieties

**Status:** Open · **Kind:** open problem · **Collection** 46

Is V(I) a non-realizable tropical linear space for some tropical ideal I⊂T[x₁,…,x_n]? Here I is tropical when each degree-bounded coefficient space I_{≤d} is tropical linear; V(I) consists of points where every polynomial's minimum is attained at least twice or equals ∞.

**Context.** Set T=(R∪{∞},min,+). For a rank-r valuated matroid p on [n], let L_p⊂T^n be spanned by vectors (p_{A∪{i}})\_i for |A|=r−1, with coordinate ∞ when i∈A. Its circuit vectors have coordinates p_{B∖{i}} for i∈B, ∞ otherwise, where |B|=r+1. Let Q_p be T^n modulo relations identifying each circuit vector with each vector obtained by setting one coordinate to ∞. Realizability means arising by valuating the Plücker coordinates of a linear space over some valued field. Checked 11 October 2026: current v2 retains both targets; no later resolution located.

**Source.** Jeffrey Giansiracusa, Kevin Kühn, Stefano Mereta and Eduardo Vital. *Three lectures on tropical algebra*. 2026. [primary source](https://arxiv.org/abs/2602.08664) Location: Question1.9.4, p13; §§1.8–1.9.

**Literature check.** Status: Checked 11 October 2026: current v2 retains both targets; no later resolution located.


<a id="q4546"></a>

## Q4546. Duality for tropical linear spaces

**Status:** Open · **Kind:** open problem · **Collection** 46

Is the coordinate-evaluation map Q_p→Hom_T(L_p,T) always an isomorphism?

**Context.** Set T=(R∪{∞},min,+). For a rank-r valuated matroid p on [n], let L_p⊂T^n be spanned by vectors (p_{A∪{i}})\_i for |A|=r−1, with coordinate ∞ when i∈A. Its circuit vectors have coordinates p_{B∖{i}} for i∈B, ∞ otherwise, where |B|=r+1. Let Q_p be T^n modulo relations identifying each circuit vector with each vector obtained by setting one coordinate to ∞. Realizability means arising by valuating the Plücker coordinates of a linear space over some valued field. Checked 11 October 2026: current v2 retains both targets; no later resolution located.

**Source.** Jeffrey Giansiracusa, Kevin Kühn, Stefano Mereta and Eduardo Vital. *Three lectures on tropical algebra*. 2026. [primary source](https://arxiv.org/abs/2602.08664) Location: Conjecture3.3.1, p20.

**Literature check.** Status: Checked 11 October 2026: current v2 retains both targets; no later resolution located.


<a id="q4549"></a>

## Q4549. Exact symmetric relation bounds

**Status:** Open · **Kind:** open problem · **Collection** 46

Determine sup{ρ(Γ):Γ symmetric with e minimal generators} as a function of e.

**Context.** Let Γ=⟨g₁<⋯&lt;g_e⟩⊂N₀ be a cofinite additive submonoid, minimally generated, with e≥2. Set F=max(Z∖Γ), PF(Γ)={z∉Γ:z+(Γ∖{0})⊂Γ}, and t(Γ)=|PF(Γ)|. Over a field k, let ρ(Γ) be the minimal number of generators of ker(k[x₁,…,x_e]→k[t]), x_i↦t^{g_i}. Symmetric means F−z∈Γ for every z∉Γ. Almost symmetric means that, for every z∉Γ, either F−z∈Γ or both z and F−z belong to PF(Γ). Checked 11 October 2026: current v3 retains both exact-value targets; no general resolution located. Earlier catalogued boundedness questions do not determine these extrema.

**Source.** Alessio Moscariello and Alessio Sammartano. *Open problems on relations of numerical semigroups*. 2026. [primary source](https://arxiv.org/abs/2406.00790) Location: Problem16, p7.

**Literature check.** Status: Checked 11 October 2026: current v3 retains both exact-value targets; no general resolution located. Earlier catalogued boundedness questions do not determine these extrema.


<a id="q4550"></a>

## Q4550. Exact almost-symmetric type bounds

**Status:** Open · **Kind:** open problem · **Collection** 46

Determine sup{t(Γ):Γ almost symmetric with e minimal generators} as a function of e.

**Context.** Let Γ=⟨g₁<⋯&lt;g_e⟩⊂N₀ be a cofinite additive submonoid, minimally generated, with e≥2. Set F=max(Z∖Γ), PF(Γ)={z∉Γ:z+(Γ∖{0})⊂Γ}, and t(Γ)=|PF(Γ)|. Over a field k, let ρ(Γ) be the minimal number of generators of ker(k[x₁,…,x_e]→k[t]), x_i↦t^{g_i}. Symmetric means F−z∈Γ for every z∉Γ. Almost symmetric means that, for every z∉Γ, either F−z∈Γ or both z and F−z belong to PF(Γ). Checked 11 October 2026: current v3 retains both exact-value targets; no general resolution located. Earlier catalogued boundedness questions do not determine these extrema.

**Source.** Alessio Moscariello and Alessio Sammartano. *Open problems on relations of numerical semigroups*. 2026. [primary source](https://arxiv.org/abs/2406.00790) Location: Problem18, p8.

**Literature check.** Status: Checked 11 October 2026: current v3 retains both exact-value targets; no general resolution located. Earlier catalogued boundedness questions do not determine these extrema.


<a id="q4598"></a>

## Q4598. Spectral sheaves on the real line

**Status:** Open · **Kind:** open problem · **Collection** 46

For E=Sp, the category of spectra, is Pic(Shv(R;Sp),⋆) equivalent as an E∞-group to R_disc×R_disc×Pic(Sp)? Here Pic is the maximal ∞-groupoid of invertible objects; R_disc is the additive real group with discrete topology.

**Context.** Algebraic topology. Sources: https://www.math.ku.dk/bibliotek/arkivet/phd-theses/2025/phd25qb.pdf ; https://qingybai.github.io/pdf/Picard_group_of_real_line.pdf The first target belongs to the joint Bai–Burklund manuscript included as Paper B. The second is the thesis's explicitly unresolved SL₂(R) case of a question credited to Oscar Harr and Branko Juran. For a Lie group G, Shv(G;E) means all sheaves with values in E, without constructibility restrictions. Use convolution F⋆H=m_!(F⊠H), where m is multiplication and ! denotes compactly supported pushforward. Its unit is the coefficient-unit skyscraper at the identity. Locator: thesis introduction, pp11–12. Checked 12 October 2026: current author manuscript retains the spectral conjecture; no resolution located for either target.

**Source.** Qingyuan Bai. *Variations on the theme of toric mirror symmetry*. University of Copenhagen, 2025. Advisor(s): Dustin Clausen and Lars Hesselholt. [primary source](https://www.math.ku.dk/bibliotek/arkivet/phd-theses/2025/phd25qb.pdf) Location: Paper B, Conjecture14, p10.

**Literature check.** Status: Checked 12 October 2026: current author manuscript retains the spectral conjecture; no resolution located for either target.

**Further links.** [1](https://qingybai.github.io/pdf/Picard_group_of_real_line.pdf)


<a id="q4599"></a>

## Q4599. Convolution inverses on SL₂(R)

**Status:** Open · **Kind:** open problem · **Collection** 46

Let Mod_k denote k-module spectra. For a field k, classify up to equivalence the objects F in Shv(SL₂(R);Mod_k) admitting H with F⋆H≃H⋆F≃δ\_e(k).

**Context.** Algebraic topology. Sources: https://www.math.ku.dk/bibliotek/arkivet/phd-theses/2025/phd25qb.pdf ; https://qingybai.github.io/pdf/Picard_group_of_real_line.pdf The first target belongs to the joint Bai–Burklund manuscript included as Paper B. The second is the thesis's explicitly unresolved SL₂(R) case of a question credited to Oscar Harr and Branko Juran. For a Lie group G, Shv(G;E) means all sheaves with values in E, without constructibility restrictions. Use convolution F⋆H=m_!(F⊠H), where m is multiplication and ! denotes compactly supported pushforward. Its unit is the coefficient-unit skyscraper at the identity. Locator: thesis introduction, pp11–12. Checked 12 October 2026: current author manuscript retains the spectral conjecture; no resolution located for either target.

**Source.** Qingyuan Bai. *Variations on the theme of toric mirror symmetry*. University of Copenhagen, 2025. Advisor(s): Dustin Clausen and Lars Hesselholt. [primary source](https://www.math.ku.dk/bibliotek/arkivet/phd-theses/2025/phd25qb.pdf) Location: Thesis introduction, pp.11–12, unresolved SL₂(R) case.

**Literature check.** Status: Checked 12 October 2026: current author manuscript retains the spectral conjecture; no resolution located for either target.

**Further links.** [1](https://qingybai.github.io/pdf/Picard_group_of_real_line.pdf)


<a id="q4600"></a>

## Q4600. Characterize the admissible data T,V for which (T,V)-Cat is doubly-infinitary distributive: it…

**Status:** Open · **Kind:** open problem (Question 7.1) · **Collection** 46

Characterize the admissible data T,V for which (T,V)-Cat is doubly-infinitary distributive: it has small products and coproducts, and for every small family (C_{ji}), the canonical map ⨿\_{r∈∏\_{j∈J}I_j}∏\_{j∈J}C_{j,r(j)}→∏\_{j∈J}⨿\_{i∈I_j}C_{ji}, induced by coproduct injections and product projections, is invertible.

**Context.** DL-S28 — Category theory and logic Origin: 2024 Nunes–Vákár, https://doi.org/10.1007/s10485-026-09887-7, Open Question 7.1; thesis Chapter5. Setup: Use Clementino’s (T,V)-categories (TAC36:368–378, §§2,4). V is nondegenerate, complete, cocomplete, symmetric monoidal closed, with strict initial object. T is a Set-monad preserving pullbacks along monomorphisms, with a chosen coherent lax extension to V-Rel; its unit and multiplication extend oplax-naturally. Require T(fᵒ)=(Tf)ᵒ for Set-maps f, and invertible composition comparisons κ\_{s,r}:Ts·Tr→T(s·r) whenever r, s, or sᵒ is a Set-map. Objects are sets X with V-relations a:TX→X and coherent unit/composition cells; morphisms are structure-preserving (T,V)-functors. Checked 12 October 2026: publisher final and v10 retain the question; no later resolution located.

**Source.** Fernando Lucatelli Nunes, Freely Generated Categorical Structures and Automatic Differentiation. *Utrecht PhD*. 2026. [primary source](https://doi.org/10.33540/3399) Location: Open Question 7.1; thesis Chapter5.

**Literature check.** Status: Checked 12 October 2026: publisher final and v10 retain the question; no later resolution located.

**Further links.** [1](https://doi.org/10.1007/s10485-026-09887-7)


<a id="q4607"></a>

## Q4607. If S is completely regular and LEF, can every such finite H be embedded in this way into a…

**Status:** Open · **Kind:** open problem · **Collection** 47

If S is completely regular and LEF, can every such finite H be embedded in this way into a finite completely regular semigroup F?

**Context.** DL47-RS30 — Semigroup theory Origin: Kudryavtsev, York seminar 21May2025, slide13; https://arxiv.org/abs/2510.21349v1, p9 preceding Remark1. Setup: A semigroup S is completely regular if every element belongs to a subgroup of S. It is LEF if each finite H⊆S admits an injection f:H→F into some finite semigroup satisfying f(xy)=f(x)f(y) whenever x,y,xy∈H. Checked 12 October 2026: latest v1 retains this question; no later resolution or publisher final located. Audited provenance and status: Subject: Semigroup theory

**Source.** Dmitry Kudryavtsev. *Local Embeddability and Related Properties of Semigroups*. 2025. [primary source](https://arxiv.org/abs/2510.21349v1) Location: p9 preceding Remark1.

**Literature check.** Status: Checked 12 October 2026: latest v1 retains this question; no later resolution or publisher final located.

**Further links.** [1](https://research.manchester.ac.uk/en/studentTheses/local-embeddability-and-related-properties-of-semigroups/)


<a id="q4617"></a>

## Q4617. Determine, for every positive integer n, exactly which pairs (p,m) of positive integers occur as…

**Status:** Open · **Kind:** open problem · **Collection** 47

Determine, for every positive integer n, exactly which pairs (p,m) of positive integers occur as (pd(A),ind(A)) for A∈Mn(T) generating a finite semigroup.

**Context.** Setup: T=R∪{−∞}, with addition max and multiplication ordinary addition. Mn(T) uses tropical matrix multiplication. For A generating a finite semigroup, ind(A) is the least positive m such that A^m=A^k for some positive k≠m; pd(A) is the least positive p with A^(m+p)=A^m at m=ind(A). Audited provenance and status: Subject: Semigroup theory

**Source.** Alice Clayphan-Taylor. *On Tropical Matrix Semigroups*. University of Manchester, 2025. Advisor(s): Marianne Johnson; co-advisor Mark Kambites. [primary source](https://research.manchester.ac.uk/en/studentTheses/on-tropical-matrix-semigroups/) Location: thesis introduction,p15 explicitly poses the monogenic-representation classification; Definition5.1.1,p114 and §5.4,p142.

**Literature check.** Status2026-10-12: no later complete classification located. This full classification is independent of the defective Conjecture5.4.4.

**Notes.** Status2026-10-12: no later complete classification located. This full classification is independent of the defective Conjecture5.4.4.


<a id="q4622"></a>

## Q4622. Deciding finite SAGBI bases

**Status:** Open · **Kind:** open problem · **Collection** 47

Is there an algorithm that, given a finite polynomial list f₁,…,fₛ, always decides whether A has a finite SAGBI basis for the fixed order?

**Context.** Commutative algebra. Source: https://leokayser.github.io/assets/pdf/papers/Computation_and_Complexity_in_Algebraic_Geometry.pdf These questions restate the author's earlier polynomial-subalgebra paper. Fix a computable field K and a computable global monomial ordering rule ≺, such as lexicographic order. The input number n of variables may vary. For A=K[f₁,…,fₛ], define in≺(A)=K[LM≺(f):0≠f∈A], where LM denotes the greatest monomial. A finite SAGBI basis is a finite subset S⊂A whose leading monomials generate in≺(A). Locator: §3.5.2, p115, following Proposition3.5.6; definitions p19. Checked 12 October 2026: the September3 thesis revision retains both questions. Semi-decision procedures and the homogeneous-input membership theorem leave these general decision problems open; no later resolution located. Audited provenance and status: Subject: Commutative algebra ISSAC2025 final unread; September2026 thesis explicitly updated.

**Source.** Leonie Kayser. *Computation and Complexity in Algebraic Geometry*. Leipzig University, 2026. Advisor(s): Simon Telen. [primary source](https://leokayser.github.io/assets/pdf/papers/Computation_and_Complexity_in_Algebraic_Geometry.pdf) Location: §3.5.2, p115, following Proposition3.5.6; definitions p19.

**Literature check.** Status: Checked 12 October 2026: the September3 thesis revision retains both questions. Semi-decision procedures and the homogeneous-input membership theorem leave these general decision problems open; no later resolution located.


<a id="q4623"></a>

## Q4623. Membership in initial subalgebras

**Status:** Open · **Kind:** open problem · **Collection** 47

Is there an algorithm that, given f₁,…,fₛ and α∈Nⁿ, always decides whether x^α belongs to in≺(A)?

**Context.** Commutative algebra. Source: https://leokayser.github.io/assets/pdf/papers/Computation_and_Complexity_in_Algebraic_Geometry.pdf These questions restate the author's earlier polynomial-subalgebra paper. Fix a computable field K and a computable global monomial ordering rule ≺, such as lexicographic order. The input number n of variables may vary. For A=K[f₁,…,fₛ], define in≺(A)=K[LM≺(f):0≠f∈A], where LM denotes the greatest monomial. A finite SAGBI basis is a finite subset S⊂A whose leading monomials generate in≺(A). Locator: §3.5.2, p115, following Proposition3.5.6; definitions p19. Checked 12 October 2026: the September3 thesis revision retains both questions. Semi-decision procedures and the homogeneous-input membership theorem leave these general decision problems open; no later resolution located. Audited provenance and status: Subject: Commutative algebra ISSAC2025 final unread; September2026 thesis explicitly updated.

**Source.** Leonie Kayser. *Computation and Complexity in Algebraic Geometry*. Leipzig University, 2026. Advisor(s): Simon Telen. [primary source](https://leokayser.github.io/assets/pdf/papers/Computation_and_Complexity_in_Algebraic_Geometry.pdf) Location: §3.5.2, p115, following Proposition3.5.6; definitions p19.

**Literature check.** Status: Checked 12 October 2026: the September3 thesis revision retains both questions. Semi-decision procedures and the homogeneous-input membership theorem leave these general decision problems open; no later resolution located.


<a id="q4634"></a>

## Q4634. Derived depth beyond Cohen–Macaulay rings

**Status:** Open · **Kind:** open problem (Question 2.3.16) · **Collection** 47

If M has finite reducing projective dimension and Tor_i^R(M,N)=0 for all sufficiently large i, must depth_R(M)+depth_R(N)=depth(R)+depth_R(M⊗\_R^L N)?

**Context.** Commutative algebra. Source: https://researchrepository.wvu.edu/etd/13347/ Let (R,m,k) be a commutative Noetherian local ring, and M,N nonzero finitely generated R-modules. Say M has finite reducing projective dimension if there are r≥0 and exact sequences 0→Kᵢ₋₁^⊕aᵢ→Kᵢ→(Ω\_R^nᵢKᵢ₋₁)^⊕bᵢ→0 (1≤i≤r), where K₀=M, aᵢ,bᵢ≥1, nᵢ≥0, and Kᵣ has finite projective dimension. Here Ω\_R^n is the nth syzygy in a free resolution. For a homologically indexed complex X, put depth_R(X)=−sup{i:Hᵢ(RHom_R(k,X))≠0}. Checked 12 October 2026: later grade results retain Cohen–Macaulay assumptions; quasi-projective-dimension results do not cover this full target. No matching resolution located. Audited provenance and status: Subject: Commutative algebra The 2025 joint paper’s publisher final was not inspected.

**Source.** Brian McCourt Laverty. *Studies on the Depth Formula and on Reducing Dimensions*. West Virginia University, 2026. Advisor(s): Olgur Celikbas. [primary source](https://researchrepository.wvu.edu/etd/13347/) Location: Question 2.3.16, p33; §§1.2.3–1.2.6 identify its finite reducing-CI hypothesis with the chain condition above. The thesis explicitly retains this generalization of the joint 2025 paper.

**Literature check.** Status: Checked 12 October 2026: later grade results retain Cohen–Macaulay assumptions; quasi-projective-dimension results do not cover this full target. No matching resolution located.


<a id="q4679"></a>

## Q4679. Blocks of symmetric-group centralizer algebras

**Status:** Open · **Kind:** open problem · **Collection** 47

Let k be algebraically closed of prime characteristic p, and let 0≤l≤m be integers. Embed S_l in S_m by fixing l+1,…,m, and set A={a∈kS_m: ax=xa for all x∈kS_l}. For primitive central idempotents e∈kS_m and f∈kS_l with ef≠0, must ef be a primitive central idempotent of A? Here a central idempotent is primitive if it is nonzero and cannot be expressed as the sum of two nonzero orthogonal central idempotents. This is the source’s equivalent assertion that every combinatorial block is a single block.

**Context.** Representation theory. Hecke Algebras and Combinatorics of Partitions, dissertation2025; Fayers–Putignano, Ribbon blocks for centraliser algebras of symmetric groups,2502.13867v2 (October7,2026). https://arxiv.org/abs/2502.13867 Ellers–Murray conjecture restated in the dissertation and current paper. Audited provenance and status: Subject: Representation theory October7 revision retains the conjecture after January2026 publication; the publisher route was unavailable. Author copy is accepted-version, not publisher-final. Checked 12 October 2026: no matching resolution was located.

**Source.** Matthew Fayers and Lorenzo Putignano. *Ribbon blocks for centraliser algebras of symmetric groups*. 2026. [primary source](https://arxiv.org/abs/2502.13867v2) Location: thesis Conjecture2.4.1 and following paragraph, p16; current Conjecture2.5 and idempotent formulation, pp9–10.

**Literature check.** Status: Checked 12 October 2026: no matching resolution was located.

**Further links.** [1](https://arxiv.org/abs/2502.13867)


<a id="q4696"></a>

## Q4696. Determine LinDim_F(PSL_n(q),Ω) for every prime power q, integer n≥4, integer 1&lt;k&lt;n−1 and field…

**Status:** Open · **Kind:** open problem · **Collection** 47

Determine LinDim_F(PSL_n(q),Ω) for every prime power q, integer n≥4, integer 1&lt;k&lt;n−1 and field F, where Ω is the set of k-dimensional subspaces of F_qⁿ with its natural action.

**Context.** Setup: For a finite G-set Ω and field F, define LinDim_F(G,Ω) as the minimum dimension of an F-vector space V admitting a homomorphism ρ:G→GL(V) and an injective map φ:Ω→V with φ(gω)=ρ(g)φ(ω). Audited provenance and status: Subject: Representation theory Only arXiv v1, dated18December2025; no journal final identified.

**Source.** Devillers, Giudici, Hawtin, Lukas Klawuhn and Morgan. *Linear dimension of group actions*. 2025. [primary source](https://arxiv.org/abs/2512.16079v1) Location: Devillers–Giudici–Hawtin–Klawuhn–Morgan, Linear dimension of group actions, arXiv2512.16079v1, Problem10.3 p27; definition p1.

**Literature check.** Status: Origin: Devillers–Giudici–Hawtin–Klawuhn–Morgan, Linear dimension of group actions, arXiv2512.16079v1, Problem10.3 p27; definition p1. Separate paper-origin target. Checked12October2026; no matching resolution located.


<a id="q4703"></a>

## Q4703. Virtual finite classifying spaces

**Status:** Open · **Kind:** open problem (Question 9.2.2) · **Collection** 48

For every such AΓ, does Out(AΓ) have a finite-index subgroup H admitting a finite CW complex K(H,1)?

**Context.** For a finite simplicial graph Γ with integer edge labels mₛₜ≥2, let AΓ=⟨V(Γ) | Π(s,t,mₛₜ)=Π(t,s,mₛₜ), {s,t}∈E(Γ)⟩, where Π(s,t,m) is the alternating word of length m beginning with s. Write Out(A)=Aut(A)/Inn(A). Locators: thesis Question9.2.2, p215; §9.1 discussion, p213. Audited provenance and status: Subject: Geometric group theory Full accepted thesis read; defense July10,2026. The 2024 recorded talk, posted January2026, predates the thesis; its abstract does not claim the finite-conjugacy classification. October5 v5 treats cyclic splittings, big-chunk invariance and acylindrical hyperbolicity. Its main results and remaining directions do not settle either selected target.

**Source.** Oli Jones. *Automorphisms of Artin groups*. TU Berlin, 2026. Advisor(s): Laura Ciobanu. [primary source](https://doi.org/10.14279/depositonce-26500) Location: Thesis Question 9.2.2, p.215.

**Literature check.** Status: Bregman–Charney–Vogtmann’s August2025 final proves the untwisted-subgroup case and explicitly leaves full Out open. Jones’s current page lists the VF paper as forthcoming.

**Literature check.** Status: Current author list retains the August2025 untwisted-subgroup article; no newer matching resolution was located.


<a id="q4704"></a>

## Q4704. Finite subgroups of RAAG outer automorphism groups

**Status:** Open · **Kind:** open problem · **Collection** 48

If every edge label equals 2, does Out(AΓ) have finitely many conjugacy classes of finite subgroups?

**Context.** For a finite simplicial graph Γ with integer edge labels mₛₜ≥2, let AΓ=⟨V(Γ) | Π(s,t,mₛₜ)=Π(t,s,mₛₜ), {s,t}∈E(Γ)⟩, where Π(s,t,m) is the alternating word of length m beginning with s. Write Out(A)=Aut(A)/Inn(A). Locators: thesis Question9.2.2, p215; §9.1 discussion, p213. Audited provenance and status: Subject: Geometric group theory Full accepted thesis read; defense July10,2026. The 2024 recorded talk, posted January2026, predates the thesis; its abstract does not claim the finite-conjugacy classification. October5 v5 treats cyclic splittings, big-chunk invariance and acylindrical hyperbolicity. Its main results and remaining directions do not settle either selected target.

**Source.** Oli Jones. *Automorphisms of Artin groups*. TU Berlin, 2026. Advisor(s): Laura Ciobanu. [primary source](https://doi.org/10.14279/depositonce-26500) Location: Thesis §9.1, p.213.

**Literature check.** Status: Bregman–Charney–Vogtmann’s August2025 final proves the untwisted-subgroup case and explicitly leaves full Out open. Jones’s current page lists the VF paper as forthcoming.

**Literature check.** Status: Current author list retains the August2025 untwisted-subgroup article; no newer matching resolution was located.


<a id="q4708"></a>

## Q4708. Must every Hopf\*-ideal I⊆J_N for which A_N/I is the polynomial Hopf\*-algebra of a compact matrix…

**Status:** Open · **Kind:** open problem · **Collection** 48

Must every Hopf\*-ideal I⊆J_N for which A_N/I is the polynomial Hopf\*-algebra of a compact matrix quantum group equal either0 or J_N, for every integer N≥6?

**Context.** For N≥6 let A_N be the universal unital complex \*-algebra generated by projections u_ij, pairwise orthogonal within each row and column, with each row and column summing to1. Its Hopf structure is Δ(u_ij)=Σ\_k u_ik⊗u_kj, ε(u_ij)=δ\_ij and S(u_ij)=u_ji. Let J_N be the ideal generated by all commutators. A Hopf\*-ideal I is a two-sided \*-ideal with Δ(I)⊆I⊗A_N+A_N⊗I, ε(I)=0 and S(I)⊆I. Audited provenance and status: Subject: Quantum groups Doctoral discovery route: Doctoral discovery: Björn Schäfer, Saarland2026; supervisor Moritz Weber. Selected questions are paper-origin. Current status: J.P. McCarthy2603.21759v1, Conjecture1.2,p.1, retains quantum-permutation maximality; p.3 reports N≤5 settled. Submitted23March2026, title-page date18February. No journal reference or later version on arXiv. Current McCarthy v1 was read. The related Nature final’s exact Definition1 was readable in the primary indexed text; its direct page redirected to an inaccessible cookie-authorization endpoint.

**Source.** J. P. McCarthy. *Maximality Levels of the classical permutation group in the quantum permutation group*. 2026. [primary source](https://arxiv.org/abs/2603.21759v1) Location: Conjecture1.2,p.1; definitions§2,pp.4–5.

**Literature check.** Status: Author’s25March2026 post labels the work a preprint; current homepage has no later maximality announcement.

**Literature check.** Status: Bounded current primary-source and full-history checks found no matching resolution.


<a id="q4720"></a>

## Q4720. Alternating double covers

**Status:** Open · **Kind:** conjecture (Conjecture 6.7.2) · **Collection** 48

For R=abab⁻² and Γ without a source, is G_Γ(R) isomorphic to C₇×SL₂(F₅) when n=3, and to 2·A_(n+2) when n≥4? Here C₇ is cyclic of order7, and 2·A_k denotes the non-split central double cover of the alternating group A_k.

**Context.** Let Γ be an n-vertex tournament, n≥3: exactly one directed edge joins each pair of distinct vertices. For a word R(a,b), define G_Γ(R)=⟨x_v (v∈VΓ) | R(x_u,x_v)=1 for every edge u→v⟩. A source has all its incident edges outgoing; a sink has them all incoming. Audited provenance and status: Subject: Combinatorial group theory Mehmet Sefa Cihan: Essex PhD awarded8September2022; supervisor Gerald Williams. Thesis-origin questions. Complete thesis read. The three selected formulations remain outside the inspected later papers. The n=3 group need not be perfect. Published2024 final read: TheoremsA–B treat Johnson and Mennicke relators, distinct from both selected words. Published2024 final read. Its classification assumes triangle-free underlying graphs, excluding the selected tournaments. Published2025 final read. It assumes exactly one more arc than vertices; no tournament with n≥3 satisfies that equality. Its residual cases do not concern the selected targets.

**Source.** Mehmet Sefa Cihan. *Digraph Groups and Related Groups*. University of Essex, 2022. Advisor(s): Gerald Williams. [primary source](https://repository.essex.ac.uk/33375/1/Dissertation.pdf) Location: Thesis Conjecture 6.7.2.


<a id="q4721"></a>

## Q4721. Source infinitude

**Status:** Open · **Kind:** open problem (Question 6.7.3) · **Collection** 48

For R=abab⁻² and Γ with a source, is G_Γ(R) infinite?

**Context.** Let Γ be an n-vertex tournament, n≥3: exactly one directed edge joins each pair of distinct vertices. For a word R(a,b), define G_Γ(R)=⟨x_v (v∈VΓ) | R(x_u,x_v)=1 for every edge u→v⟩. A source has all its incident edges outgoing; a sink has them all incoming. Audited provenance and status: Subject: Combinatorial group theory Mehmet Sefa Cihan: Essex PhD awarded8September2022; supervisor Gerald Williams. Thesis-origin questions. Complete thesis read. The three selected formulations remain outside the inspected later papers. The n=3 group need not be perfect. Published2024 final read: TheoremsA–B treat Johnson and Mennicke relators, distinct from both selected words. Published2024 final read. Its classification assumes triangle-free underlying graphs, excluding the selected tournaments. Published2025 final read. It assumes exactly one more arc than vertices; no tournament with n≥3 satisfies that equality. Its residual cases do not concern the selected targets.

**Source.** Mehmet Sefa Cihan. *Digraph Groups and Related Groups*. University of Essex, 2022. Advisor(s): Gerald Williams. [primary source](https://repository.essex.ac.uk/33375/1/Dissertation.pdf) Location: Thesis Question 6.7.3.


<a id="q4722"></a>

## Q4722. Derived length

**Status:** Open · **Kind:** conjecture (Conjecture 6.8.2) · **Collection** 48

For R=ab²a²b⁻² and Γ without a sink, does G_Γ(R) have derived length exactly2 or3? Derived length is the least ℓ with G^(ℓ)=1, where G^(0)=G and G^(i+1)=[G^(i),G^(i)].

**Context.** Let Γ be an n-vertex tournament, n≥3: exactly one directed edge joins each pair of distinct vertices. For a word R(a,b), define G_Γ(R)=⟨x_v (v∈VΓ) | R(x_u,x_v)=1 for every edge u→v⟩. A source has all its incident edges outgoing; a sink has them all incoming. Audited provenance and status: Subject: Combinatorial group theory Mehmet Sefa Cihan: Essex PhD awarded8September2022; supervisor Gerald Williams. Thesis-origin questions. Complete thesis read. The three selected formulations remain outside the inspected later papers. The n=3 group need not be perfect. Published2024 final read: TheoremsA–B treat Johnson and Mennicke relators, distinct from both selected words. Published2024 final read. Its classification assumes triangle-free underlying graphs, excluding the selected tournaments. Published2025 final read. It assumes exactly one more arc than vertices; no tournament with n≥3 satisfies that equality. Its residual cases do not concern the selected targets.

**Source.** Mehmet Sefa Cihan. *Digraph Groups and Related Groups*. University of Essex, 2022. Advisor(s): Gerald Williams. [primary source](https://repository.essex.ac.uk/33375/1/Dissertation.pdf) Location: Thesis Conjecture 6.8.2.


<a id="q4724"></a>

## Q4724. For every integer a≥2, are there infinitely many N with τ\_N=a?

**Status:** Open · **Kind:** conjecture (Conjecture 2) · **Collection** 48

For every integer a≥2, are there infinitely many N with τ\_N=a?

**Context.** Martina Iannella: Udine PhD October2023; supervisor Alberto Marcone, co-supervisor Vincenzo Dimonte. Setup: For each integer N≥1, let ⋆\_N be the unique operation on {1,…,N} satisfying a⋆\_N1=a+1 for a&lt;N, N⋆\_N1=1, and a⋆\_N(b+1)=(a⋆\_Nb)⋆\_N(a⋆\_N1) for 1≤a≤N and 1≤b&lt;N. Put τ\_N=min{p∈{1,…,N}:1⋆\_Np=N}. Audited provenance and status: Subject: Universal algebra Paper-origin: Aguilera–Iannella, Non-dyadic Laver algebras, 2610.06106v1, Conjecture2 p10; definitions pp1–2,6. Checked12October2026: only October5 version located; no matching resolution. Doctoral title: From real-life to very strong axioms. Classification problems in Descriptive Set Theory & regularity properties in Generalized Descriptive Set Theory. Adjacent Conjecture1 is held: its literal limit τ\_N→∞ contradicts Conjecture2’s infinitely recurring fixed values. No limsup repair is inserted.

**Source.** Juan P. Aguilera; Martina Iannella. *Non-dyadic Laver algebras*. 2026. [primary source](https://arxiv.org/abs/2610.06106v1) Location: Conjecture 2, p.10; definitions pp.1–2,6.

**Literature check.** Status: Paper-origin: Aguilera–Iannella, Non-dyadic Laver algebras, 2610.06106v1, Conjecture2 p10; definitions pp1–2,6. Checked12October2026: only October5 version located; no matching resolution.

**Further links.** [1](https://arxiv.org/abs/2610.06106) · [2](https://arxiv.org/pdf/2610.06106v1) · [3](https://martinaiannella.github.io/) · [4](https://www.ailalogica.it/wp-content/uploads/2025/05/MONTAGNA_PRIZE_2025-FINAL_REPORT.pdf)


<a id="q4733"></a>

## Q4733. Quaternionic super Brauer group

**Status:** Open · **Kind:** open problem (Question 6.2) · **Collection** 48

Determine the group Br(E).

**Context.** Let E be the real symmetric monoidal category of finite-dimensional complex ℤ/2-graded vector spaces V with an even antilinear map J satisfying J²(v)=(−1)^i v for v∈V_i. Morphisms are even complex-linear maps commuting with J. Tensor product is the usual graded complex tensor product with J_{V⊗W}=J_V⊗J_W, and symmetry is the Koszul signed interchange. The tensor unit is ℂ in even degree with complex conjugation. For associative unital algebra objects in E, use Morita equivalence implemented by invertible bimodule objects in E. Their Morita classes form a monoid under tensor product; let Br(E) be its group of units. Thus a class [A] lies in Br(E) when some algebra object B makes A⊗B Morita-equivalent to the tensor unit. Audited provenance and status: Subject: Category theory Sean Sanford: Indiana PhD 2022; advisor Julia Plavnik. The older dissertation was not inspected; this is a paper restatement of an earlier public question. Earlier 2016 discussion proposes ℤ/4 but explicitly lacks a complete proof; its homotopy-fixed-point premise was unchecked. October 6 primary paper still poses Question 6.2.

**Source.** Sean Sanford. *On the Mext groups of sVec_R and sVec_H*. 2026. [primary source](https://arxiv.org/abs/2609.20153v2) Location: Question 6.2, restating Johnson-Freyd’s 2016 question.

**Further links.** [1](https://arxiv.org/abs/2609.20153)


<a id="q4738"></a>

## Q4738. Infinitude of higher weak-commutativity groups

**Status:** Open · **Kind:** open problem · **Collection** 48

Is χₙ(H) infinite for every finite noncyclic group H and every integer n≥4?

**Context.** For a group H and an integer n≥2, let H₁,…,Hₙ be labelled isomorphic copies of H, with hᵢ denoting the copy of h∈H in Hᵢ. Define χₙ(H) as the quotient of the free product H₁∗⋯∗Hₙ by the normal closure of all commutators [hᵢ,hⱼ], for h∈H and 1≤i&lt;j≤n. Here [x,y]=x⁻¹y⁻¹xy; no further relations between different copies are imposed. Audited provenance and status: Subject: Group theory Ricardo Nunes de Oliveira: Brasília PhD 2007; advisor Said Najati Sidki. The repository permits only partial thesis release; thesis mathematics was not inspected. This target is taken from the later paper. October 5 primary version states this expectation; it is not labelled a numbered conjecture. Checked12October2026: no later version or matching resolution was located.

**Source.** Said N. Sidki; Noraí R. Rocco; Ricardo N. de Oliveira; Dmytro Savchuk (appendix). *On weak commutativity between n isomorphic groups, n ≥ 2*. 2026. [primary source](https://arxiv.org/abs/2610.07330v1) Location: Group theory. Sidki, Rocco and de Oliveira, with an appendix by Savchuk, arXiv:2610.07330v1 (2026), introductory expectation, p2.

**Literature check.** Status: Checked12October2026: no later version or matching resolution was located.

**Further links.** [1](https://arxiv.org/abs/2610.07330)


<a id="q4757"></a>

## Q4757. The flag-dimension bound for general linear groups

**Status:** Open · **Kind:** open problem · **Collection** 48

Must GKdim(Π)≤[K:Q_p]n(n−1)/2 hold for every such Π?

**Context.** Let p be prime, let K and L be finite extensions of Q_p, and let n≥2. Let Π be a nonzero continuous L-Banach representation of GL_n(K). For a compact open uniform pro-p subgroup H, put A=L⊗\_{O_L}O_L[[H]] and M=Hom_cont,L(Π,L). Assume Π is admissible, meaning M is finitely generated over A. Let Π^la denote its locally Q_p-analytic vectors. Assume Z(U(L⊗\_{Q_p}gl_n(K))) acts on Π^la through an L-algebra homomorphism to L. Define GKdim(Π)=dim_{Q_p}(H)−inf{i≥0:Ext_A^i(M,A)≠0}. Audited provenance and status: Subject: p-adic representation theory Reinier Sorgdrager: Amsterdam/Paris-Saclay doctorate, defended28September2026; supervisors Benjamin Schraen and Lenny Taelman, co-supervisor Arno Kret. This is the thesis’s explicitly singled-out general-linear-group restatement of the older bound problem, not a newly originated conjecture. The full September thesis retains the target; n=2 is proved for p>2, while n=3,4 are described only as expected computations. The April2023 author manuscript was inspected; the older2023 publisher final remains unread. The inspected2026 publisher final bounds smooth mod-p Jacquet–Langlands transfers; it predates the September thesis and gives no general Banach bound.

**Source.** Reinier Sorgdrager. *Gelfand–Kirillov dimensions and the p-adic Langlands program*. University of Amsterdam / Paris-Saclay, 2026. Advisor(s): Benjamin Schraen; Lenny Taelman; Arno Kret. [primary source](https://www.dare.uva.nl/id/c42a0660-f0af-4c7e-b347-a8fe61e57f31) Location: §1.5, p39, restating the Dospinescu–Paškūnas–Schraen bound problem.


<a id="q4759"></a>

## Q4759. Completely prime ideals

**Status:** Open · **Kind:** conjecture (Conjecture 4.3.4) · **Collection** 48

Is A/P a domain for every proper two-sided prime ideal P of A? Here prime means IJ⊆P implies I⊆P or J⊆P for two-sided ideals I,J.

**Context.** Let k be an uncountable algebraically closed field of characteristic zero. Let W=k[t]∂, where ∂=d/dt and [f∂,g∂]=(fg′−f′g)∂, and let A=U(W). Give A the Z-grading induced by deg(t^{i+1}∂)=i for i≥−1, and denote its degree-zero subring by A_0. Audited provenance and status: Subject: Lie and associative algebras Tuan Anh Pham: Edinburgh doctoral thesis2026; primary supervisor Susan J. Sierra, second advisor Alexander Shapiro. Both targets appear in the thesis; degree-zero Noetherianity restates Pham–Timmins2025, while October’s paper independently singles out the prime-ideal target. The inspected October1 paper retains the prime-ideal conjecture and proves only orbit-image cases; degree-zero Noetherianity remains explicitly conjectural in the September thesis. October’s citation points to an earlier primitive-only conjecture.

**Source.** Tuan Anh Pham. *Two-sided ideals of the enveloping algebras of the Virasoro and related Lie algebras*. University of Edinburgh, 2026. Advisor(s): Susan J. Sierra; Alexander Shapiro. [primary source](https://doi.org/10.7488/era/7765) Location: Thesis Conjecture 4.3.4; October paper Conjecture 1.5.


<a id="q4760"></a>

## Q4760. Degree-zero Noetherianity

**Status:** Open · **Kind:** conjecture (Conjecture 5.1.7) · **Collection** 48

Is A_0 left and right Noetherian, meaning every ascending chain of left ideals and every ascending chain of right ideals stabilizes?

**Context.** Let k be an uncountable algebraically closed field of characteristic zero. Let W=k[t]∂, where ∂=d/dt and [f∂,g∂]=(fg′−f′g)∂, and let A=U(W). Give A the Z-grading induced by deg(t^{i+1}∂)=i for i≥−1, and denote its degree-zero subring by A_0. Audited provenance and status: Subject: Lie and associative algebras Tuan Anh Pham: Edinburgh doctoral thesis2026; primary supervisor Susan J. Sierra, second advisor Alexander Shapiro. Both targets appear in the thesis; degree-zero Noetherianity restates Pham–Timmins2025, while October’s paper independently singles out the prime-ideal target. The inspected October1 paper retains the prime-ideal conjecture and proves only orbit-image cases; degree-zero Noetherianity remains explicitly conjectural in the September thesis. October’s citation points to an earlier primitive-only conjecture.

**Source.** Tuan Anh Pham. *Two-sided ideals of the enveloping algebras of the Virasoro and related Lie algebras*. University of Edinburgh, 2026. Advisor(s): Susan J. Sierra; Alexander Shapiro. [primary source](https://doi.org/10.7488/era/7765) Location: Thesis Conjecture 5.1.7.


<a id="q4773"></a>

## Q4773. Must every smooth C admit a single compact generator?

**Status:** Open · **Kind:** conjecture (Conjecture 0.2.8) · **Collection** 48

Must every smooth C admit a single compact generator?

**Context.** Setup: R is an E∞-ring spectrum and C a dualizable, presentable, stable R-linear ∞-category, with R-linear dual C∨. Smoothness means the coevaluation Mod_R→C⊗\_R C∨ admits a colimit-preserving R-linear right adjoint. A compact generator is a compact object whose stable, colimit-closed generated subcategory is C. Audited provenance and status: Subject: Higher category theory Matteo Montagnani, SISSA PhD (25 September 2026); advisors Nicolò Sibilla and Mauro Porta. Thesis: A Non-Commutative Approach to Rigid Analytic Geometry; Conjecture 0.2.8, p.12; Definition 0.2.5, p.11. Earlier-paper origin: Ramzi, arXiv:2410.21537v1, Conjecture 0.6; Montagnani’s arXiv:2605.21024v1 retains it as Conjecture 1.6 (p.8). Checked 13 October 2026: retained in thesis. Invertible/truncated-connective results and broader-base counterexamples do not settle it.

**Source.** Matteo Montagnani. *A Non-Commutative Approach to Rigid Analytic Geometry*. SISSA, 2026. Advisor(s): Nicolò Sibilla; Mauro Porta. [primary source](https://iris.sissa.it/handle/20.500.11767/153671) Location: Conjecture 0.2.8, p.12; Definition 0.2.5, p.11.

**Literature check.** Status: Related later primary papers checked; no matching resolution found.

**Further links.** [1](https://arxiv.org/abs/2410.21537v1) · [2](https://arxiv.org/abs/2605.21024v1) · [3](https://arxiv.org/abs/2307.16337v2) · [4](https://arxiv.org/abs/2509.14231v1) · [5](https://arxiv.org/abs/2608.04898v1) · [6](https://arxiv.org/abs/2608.10681v1)


<a id="q4783"></a>

## Q4783. Let G be an almost simple connected complex algebraic group of type D_m (m≥4) or E₆. Define h(G)…

**Status:** Open · **Kind:** open problem · **Collection** 48

Let G be an almost simple connected complex algebraic group of type D_m (m≥4) or E₆. Define h(G) as the least positive integer h such that every finite family of parabolic subgroups of G shares a maximal torus whenever every subfamily of at most h members does. Determine h(G).

**Context.** Audited provenance and status: Subject: Algebraic groups and discrete geometry Shaoyu Huang; Pittsburgh PhD2025; advisor Kiumars Kaveh. Restricted residual of thesis Problem3.1.34,p41 and earlier joint-paper Problem6.4,p827. Later-paper formulation: Definition4.1,p13; Corollaries4.5,p16–17 and6.2,p23. Known: h(D_m)∈{m+1,m+2}; h(E₆)∈{7,8}. Other complex almost-simple types are settled. The later definition explicitly restricts to finite families. Paper fallback; finite-family convention only.

**Source.** Boris Tsvelikhovskiy. *Helly Numbers for Connected Reductive Groups and Splitting of Toric Principal Bundles*. 2026. [primary source](https://arxiv.org/abs/2610.11340v1) Location: Thesis/final say “any k”; canonical uses later Definition4.1’s “at most h”.

**Literature check.** Status: No matching resolution located through October13,2026.

**Further links.** [1](https://d-scholarship.pitt.edu/downloads/051978f8-d0c3-4934-9717-64b4194bb578?locale=en) · [2](https://doi.org/10.4171/DM/962)


<a id="q4829"></a>

## Q4829. Groups admitting polynomial geodesic growth

**Status:** Open · **Kind:** open problem (Question 1) · **Reviewed extraction** 2026-10-13-250

Characterize finitely generated groups G for which some finite monoid-generating set S has polynomial geodesic growth: there are constants C,d such that the number of words w over S with |w|≤n and |w| equal to the S-word length of their product is at most C(1+n)^d for every n≥0. S need not be symmetric.

**Source.** Corentin Bodart. *Geometric and algorithmic aspects of nilpotent groups*. Université de Genève, 2024. [primary source](https://access.archive-ouverte.unige.ch/access/metadata/0a2c7af3-5c4e-4ce9-8447-7c622895253d/download) · [record](https://archive-ouverte.unige.ch/unige:181560) Location: Question1, Chapter4, printed53

**Literature check.** Reviewed 2026-10-13: The current geodesic paper retains the higher-step symmetric question and the finite-action classification; no global characterization was found in the author current list or targeted current primary retrieval.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/bodart-2024.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://arxiv.org/pdf/2306.10381v3) · [2](https://sites.google.com/view/corentin-bodart/papers)

<a id="q4830"></a>

## Q4830. Polynomial geodesic growth forces virtual class two

**Status:** Open · **Kind:** conjecture (Conjecture 4) · **Reviewed extraction** 2026-10-13-250

Let G be a group with a finite symmetric generating set S. If the number of geodesic words over S of length at most n is bounded by a polynomial in n, must G have a finite-index nilpotent subgroup of nilpotency class at most2?

**Source.** Corentin Bodart. *Geometric and algorithmic aspects of nilpotent groups*. Université de Genève, 2024. [primary source](https://access.archive-ouverte.unige.ch/access/metadata/0a2c7af3-5c4e-4ce9-8447-7c622895253d/download) · [record](https://archive-ouverte.unige.ch/unige:181560) Location: Conjecture4.A, printed70

**Literature check.** Reviewed 2026-10-13: Still stated verbatim as ConjectureA in §5 of the December6,2025 v3 geodesic paper. Current author list through October2026 contains no claimed closure.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/bodart-2024.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://arxiv.org/pdf/2306.10381v3) · [2](https://sites.google.com/view/corentin-bodart/papers)

<a id="q4831"></a>

## Q4831. Polynomial geodesic growth of the asymmetric virtually Engel example

**Status:** Open · **Kind:** conjecture (Conjecture 4) · **Reviewed extraction** 2026-10-13-250

Let vE be the group generated by a,t with t²=1; writing b=t⁻¹at and c=[a,[a,b]], impose [b,[a,b]]=c and require c to commute with a and b. Is its geodesic growth with respect to the finite monoid-generating set S={a,b,(ab)⁻¹,t} bounded above by a polynomial? Here geodesic growth counts words over S of length at most n that minimize S-word length for their product.

**Source.** Corentin Bodart. *Geometric and algorithmic aspects of nilpotent groups*. Université de Genève, 2024. [primary source](https://access.archive-ouverte.unige.ch/access/metadata/0a2c7af3-5c4e-4ce9-8447-7c622895253d/download) · [record](https://archive-ouverte.unige.ch/unige:181560) Location: Conjecture4.B, printed70

**Literature check.** Reviewed 2026-10-13: Still explicit ConjectureB in §5 of the current v3 geodesic paper.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/bodart-2024.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://arxiv.org/pdf/2306.10381v3) · [2](https://sites.google.com/view/corentin-bodart/papers)

<a id="q4832"></a>

## Q4832. Algorithmic finite-action facet classification

**Status:** Open · **Kind:** open problem (Problem 4) · **Reviewed extraction** 2026-10-13-250

Characterize the finite subgroups F≤GL_d(Z) for which there exists a finite centrally symmetric set A⊂Z^d such that P=conv({f(a):f∈F,a∈A}) is full-dimensional and each facet of P contains at most one point of A. In particular, is there an algorithm deciding this property when F is supplied as its finite list of integer matrices?

**Source.** Corentin Bodart. *Geometric and algorithmic aspects of nilpotent groups*. Université de Genève, 2024. [primary source](https://access.archive-ouverte.unige.ch/access/metadata/0a2c7af3-5c4e-4ce9-8447-7c622895253d/download) · [record](https://archive-ouverte.unige.ch/unige:181560) Location: Problem4.C, printed71

**Literature check.** Reviewed 2026-10-13: Explicitly retained as ProblemC in current §5. No current full characterization found.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/bodart-2024.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://arxiv.org/pdf/2306.10381v3) · [2](https://sites.google.com/view/corentin-bodart/papers)

<a id="q4833"></a>

## Q4833. One orbit suffices for the symmetric facet condition

**Status:** Open · **Kind:** open problem (Question 4) · **Reviewed extraction** 2026-10-13-250

For every finite subgroup F≤GL_d(Z), are the following properties equivalent? (i) Some finite centrally symmetric A⊂Z^d makes conv(F·A) full-dimensional with each facet containing at most one point of A. (ii) Some a∈Z^d makes conv(F·{a,−a}) full-dimensional.

**Source.** Corentin Bodart. *Geometric and algorithmic aspects of nilpotent groups*. Université de Genève, 2024. [primary source](https://access.archive-ouverte.unige.ch/access/metadata/0a2c7af3-5c4e-4ce9-8447-7c622895253d/download) · [record](https://archive-ouverte.unige.ch/unige:181560) Location: Question4.D, printed71

**Literature check.** Reviewed 2026-10-13: Explicit current QuestionD; source expects a negative answer but does not exhibit a counterexample.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/bodart-2024.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://arxiv.org/pdf/2306.10381v3) · [2](https://sites.google.com/view/corentin-bodart/papers)

<a id="q4834"></a>

## Q4834. Cube-root word-versus-Stoll error in metabelian nilpotent groups

**Status:** Open · **Kind:** conjecture (Conjecture 4) · **Reviewed extraction** 2026-10-13-250

Let H be a finitely generated torsion-free metabelian nilpotent group and X a finite monoid-generating set. In its Mal’cev completion define ||h||\_Stoll,X as the infimum of ∑μ\_i over all products h=x_1^{μ\_1}⋯x_k^{μ\_k}, with x_i∈X and real μ\_i>0. Is there a constant C depending only on H,X such that 0≤||h||\_X−||h||\_Stoll,X≤C(1+||h||\_X)^{1/3} for every h∈H?

**Source.** Corentin Bodart. *Geometric and algorithmic aspects of nilpotent groups*. Université de Genève, 2024. [primary source](https://access.archive-ouverte.unige.ch/access/metadata/0a2c7af3-5c4e-4ce9-8447-7c622895253d/download) · [record](https://archive-ouverte.unige.ch/unige:181560) Location: Conjecture4.E, printed71

**Literature check.** Reviewed 2026-10-13: Thesis explicitly proposes this weakening. Current v3 geodesic paper retains unresolved sharp higher-step bounds and disproves only O(1); author current list and exact metabelian/Stoll searches did not locate a full result for this cube-root statement.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/bodart-2024.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://arxiv.org/pdf/2306.10381v3) · [2](https://sites.google.com/view/corentin-bodart/papers)

<a id="q4835"></a>

## Q4835. Simultaneously intermediate volume and geodesic growth

**Status:** Open · **Kind:** open problem (Question 4) · **Reviewed extraction** 2026-10-13-250

Does there exist a finitely generated group G and a finite monoid-generating set S for which both β(n)=#{g∈G:||g||\_S≤n} and γ(n)=#{w∈S\*:|w|≤n,|w|=||ev(w)||\_S} have intermediate growth, meaning each is superpolynomial and subexponential?

**Source.** Corentin Bodart. *Geometric and algorithmic aspects of nilpotent groups*. Université de Genève, 2024. [primary source](https://access.archive-ouverte.unige.ch/access/metadata/0a2c7af3-5c4e-4ce9-8447-7c622895253d/download) · [record](https://archive-ouverte.unige.ch/unige:181560) Location: Question4.F (Grigorchuk Problem13), printed72

**Literature check.** Reviewed 2026-10-13: Retained as QuestionE in current v3 paper §5; the author explicitly distinguishes it from the solved existence of intermediate geodesic growth.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/bodart-2024.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://arxiv.org/pdf/2306.10381v3) · [2](https://sites.google.com/view/corentin-bodart/papers)

<a id="q4836"></a>

## Q4836. Countable word-metric horoboundaries characterize virtual abelianness

**Status:** Open · **Kind:** conjecture (Conjecture 5) · **Reviewed extraction** 2026-10-13-250

For a finite symmetric generating set S, ∂(G,d_S) consists of pointwise limits, along sequences escaping finite sets, of h↦d_S(x,h)−d_S(x,e). For every finitely generated group G and every such S, is ∂(G,d_S) countable if and only if G is virtually abelian?

**Source.** Corentin Bodart. *Geometric and algorithmic aspects of nilpotent groups*. Université de Genève, 2024. [primary source](https://access.archive-ouverte.unige.ch/access/metadata/0a2c7af3-5c4e-4ce9-8447-7c622895253d/download) · [record](https://archive-ouverte.unige.ch/unige:181560) Location: Conjecture5.A, printed101

**Literature check.** Reviewed 2026-10-13: Retained as Conjecture1(a) in Bodart–Tashiro. November2025 finite-Busemann boundary theorem characterizes virtual cyclicity; it leaves countability versus virtual abelianness untouched.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/bodart-2024.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://arxiv.org/pdf/2407.11943) · [2](https://arxiv.org/abs/2511.20495) · [3](https://sites.google.com/view/corentin-bodart/papers)

<a id="q4837"></a>

## Q4837. Finitely many Busemann orbits for class-two nilpotent groups

**Status:** Open · **Kind:** conjecture (Conjecture 5) · **Reviewed extraction** 2026-10-13-250

For a finite symmetric generating set S, ∂(G,d_S) consists of pointwise limits, along sequences escaping finite sets, of h↦d_S(x,h)−d_S(x,e). If G is finitely generated nilpotent of class at most2, must the left-translation action on its Busemann points have finitely many orbits? A Busemann point here is a horofunction obtained as the limit along a geodesic ray; the action is (g·φ)(h)=φ(g⁻¹h)−φ(g⁻¹).

**Source.** Corentin Bodart. *Geometric and algorithmic aspects of nilpotent groups*. Université de Genève, 2024. [primary source](https://access.archive-ouverte.unige.ch/access/metadata/0a2c7af3-5c4e-4ce9-8447-7c622895253d/download) · [record](https://archive-ouverte.unige.ch/unige:181560) Location: Conjecture5.B, printed102

**Literature check.** Reviewed 2026-10-13: Current primary source still conjectures the general class2/virtual-class2 extension. The cyclic-derived theorem is not a closure of all class2 groups.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/bodart-2024.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://arxiv.org/pdf/2407.11943) · [2](https://sites.google.com/view/corentin-bodart/papers)

<a id="q4838"></a>

## Q4838. Rational-subset membership in all higher Heisenberg groups

**Status:** Open · **Kind:** conjecture (Conjecture 6) · **Reviewed extraction** 2026-10-13-250

For every m≥2, is rational-subset membership decidable in H_{2m+1}(Z)=⟨x_1,…,x_m,y_1,…,y_m,z | [x_i,y_i]=z, all other basic commutators are1⟩? The input is an element g and a finite-state automaton with group-element-labelled edges; decide whether g equals the product of labels along an accepted path. Group elements may be supplied as words in fixed generators.

**Source.** Corentin Bodart. *Geometric and algorithmic aspects of nilpotent groups*. Université de Genève, 2024. [primary source](https://access.archive-ouverte.unige.ch/access/metadata/0a2c7af3-5c4e-4ce9-8447-7c622895253d/download) · [record](https://archive-ouverte.unige.ch/unige:181560) Location: Conjecture6.A, printed127

**Literature check.** Reviewed 2026-10-13: Explicit current ConjectureA in published 2025 Membership problems. Current manuscript notes Shafrir progress only for a restricted rational-set shape.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/bodart-2024.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://arxiv.org/html/2401.15504v6) · [2](https://sites.google.com/view/corentin-bodart/papers)

<a id="q4839"></a>

## Q4839. Groups whose rational subsets have bounded regular representatives

**Status:** Open · **Kind:** open problem (Question 6) · **Reviewed extraction** 2026-10-13-250

Characterize finitely generated groups G such that, for every rational subset R⊂G, there exists a bounded regular language L′ over a finite alphabet of elements of G with ev(L′)=R. Here rational means R=ev(L) for some regular L, and bounded means L′⊂w_1\*⋯w_k\* for finitely many fixed words w_i. In particular, determine this property for all class-two nilpotent groups with cyclic derived subgroup.

**Source.** Corentin Bodart. *Geometric and algorithmic aspects of nilpotent groups*. Université de Genève, 2024. [primary source](https://access.archive-ouverte.unige.ch/access/metadata/0a2c7af3-5c4e-4ce9-8447-7c622895253d/download) · [record](https://archive-ouverte.unige.ch/unige:181560) Location: Question6.C, printed128

**Literature check.** Reviewed 2026-10-13: Published 2025 paper retains the stronger effective classification and the cyclic-derived family. No exact global existential classification found; original thesis remains explicit source of this weaker formulation.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/bodart-2024.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://arxiv.org/html/2401.15504v6) · [2](https://sites.google.com/view/corentin-bodart/papers)

<a id="q4848"></a>

## Q4848. Baumslag’s Parafree Conjecture

**Status:** Open · **Kind:** conjecture (Conjecture) · **Reviewed extraction** 2026-10-13-250

Let G be a finitely generated residually nilpotent group such that, for a free group F, G/γ\_n(G)≅F/γ\_n(F) for every n≥1, where γ\_1(G)=G and γ\_{n+1}(G)=[G,γ\_n(G)]. Must H_2(G;Z)=0?

**Source.** Samuel P. Fisher. *L²-Betti numbers and kernels of maps to ℤ*. University of Oxford, 2025. [primary source](https://ora.ox.ac.uk/objects/uuid:a95972ee-b2e7-49e9-bed9-bca1332c0373/files/dd791sg858) · [record](https://ora.ox.ac.uk/objects/uuid:a95972ee-b2e7-49e9-bed9-bca1332c0373) Location: §1.2.1, unnumbered Baumslag Parafree Conjecture, printed p.8 / PDF p.14; repeated before Corollary 4.3.15, printed p.57 / PDF p.63.

**Literature check.** Reviewed 2026-10-13: The March 2026 Coherent RFRS paper still calls this the Parafree Conjecture and proves a dimension-two equivalence, not the unrestricted statement. August 2026 counterexamples concern associative algebras, not groups; September 2026 Lie-algebra results assume homology vanishing.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/fisher-2025.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://arxiv.org/html/2603.16763) · [2](https://arxiv.org/abs/2608.20570) · [3](https://arxiv.org/abs/2609.19595)

<a id="q4850"></a>

## Q4850. Embedding torsion-free group algebras into division rings

**Status:** Open · **Kind:** conjecture (Conjecture 1.3.2) · **Reviewed extraction** 2026-10-13-250

For every torsion-free group G and field k, does there exist an injective unital ring homomorphism k[G]→D into a division ring D?

**Source.** Samuel P. Fisher. *L²-Betti numbers and kernels of maps to ℤ*. University of Oxford, 2025. [primary source](https://ora.ox.ac.uk/objects/uuid:a95972ee-b2e7-49e9-bed9-bca1332c0373/files/dd791sg858) · [record](https://ora.ox.ac.uk/objects/uuid:a95972ee-b2e7-49e9-bed9-bca1332c0373) Location: Conjecture 1.3.2, printed p.9 / PDF p.15; published counterpart Conjecture 1.1, J. Comb. Algebra 10 (2026).

**Literature check.** Reviewed 2026-10-13: Retained in published Conjecture 1.1. Proved embeddings for particular geometric classes do not resolve arbitrary torsion-free G.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/fisher-2025.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://ems.press/content/serial-article-files/52395)

<a id="q4851"></a>

## Q4851. Integral virtual algebraic fibring from vanishing over every prime field

**Status:** Open · **Kind:** conjecture (Conjecture B.1) · **Reviewed extraction** 2026-10-13-250

Fix n≥0 and a residually finite rationally solvable (RFRS) group G of type FP_{n+1}(Z). Is the existence of a finite-index subgroup H≤G with an epimorphism H→Z whose kernel is of type FP_n(Z) equivalent to b_i^{(2)}(G;F_p)=0 for every prime p and every 0≤i≤n? Here FP_j(R) means that the trivial R[G]-module has a projective resolution finitely generated through degree j. For an RFRS group, b_i^{(2)}(G;F_p)=dim_{D_p}H_i(G;D_p), with D_p the unique Hughes-free division ring generated by F_p[G].

**Source.** Samuel P. Fisher. *L²-Betti numbers and kernels of maps to ℤ*. University of Oxford, 2025. [primary source](https://ora.ox.ac.uk/objects/uuid:a95972ee-b2e7-49e9-bed9-bca1332c0373/files/dd791sg858) · [record](https://ora.ox.ac.uk/objects/uuid:a95972ee-b2e7-49e9-bed9-bca1332c0373) Location: Conjecture B.1, printed p.83 / PDF p.89; Definitions 2.2.1–2.2.2 and 2.5.1, printed pp.12,20 / PDF pp.18,26.

**Literature check.** Reviewed 2026-10-13: The later Poincaré-duality virtual-fibring theorem treats a special class and field finiteness; it does not prove this general integral FP_n criterion. Current author work and exact-theme searches locate no full resolution.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/fisher-2025.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://arxiv.org/html/2506.14666) · [2](https://sampfisher.github.io/)

<a id="q4852"></a>

## Q4852. Virtual specialness versus virtual free-by-cyclic structure for one-relator groups

**Status:** Open · **Kind:** conjecture (Conjecture B.2) · **Reviewed extraction** 2026-10-13-250

Is a one-relator group G virtually free-by-cyclic if and only if it is virtually special? Here one-relator means a finite presentation with a single defining relator; virtually free-by-cyclic means that some finite-index H≤G fits into 1→F→H→Z→1 with F free, not assumed finitely generated. Virtually special means that a finite-index subgroup is the fundamental group of a special nonpositively curved cube complex in the sense of Haglund–Wise.

**Source.** Samuel P. Fisher. *L²-Betti numbers and kernels of maps to ℤ*. University of Oxford, 2025. [primary source](https://ora.ox.ac.uk/objects/uuid:a95972ee-b2e7-49e9-bed9-bca1332c0373/files/dd791sg858) · [record](https://ora.ox.ac.uk/objects/uuid:a95972ee-b2e7-49e9-bed9-bca1332c0373) Location: Actual Conjecture B.2.1, printed p.85 / PDF p.91. The automatic label Conjecture B.2 followed by 1. is an extraction split.

**Literature check.** Reviewed 2026-10-13: The current RFRS coherence theorem gives a structural equivalence under an RFRS hypothesis and the cited cubulated hyperbolic result is a restricted case. No full one-relator equivalence was located in the current primary author work.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/fisher-2025.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://arxiv.org/html/2603.16763) · [2](https://sampfisher.github.io/)

<a id="q4853"></a>

## Q4853. Coherence of finitely generated parafree groups

**Status:** Open · **Kind:** conjecture (Conjecture B.4) · **Reviewed extraction** 2026-10-13-250

Is every finitely generated parafree group coherent, meaning that each of its finitely generated subgroups is finitely presented? Parafree means residually nilpotent with the same lower-central-series quotients as a free group.

**Source.** Samuel P. Fisher. *L²-Betti numbers and kernels of maps to ℤ*. University of Oxford, 2025. [primary source](https://ora.ox.ac.uk/objects/uuid:a95972ee-b2e7-49e9-bed9-bca1332c0373/files/dd791sg858) · [record](https://ora.ox.ac.uk/objects/uuid:a95972ee-b2e7-49e9-bed9-bca1332c0373) Location: Conjecture B.4, printed p.85 / PDF p.91; parafree definition printed p.8 / PDF p.14.

**Literature check.** Reviewed 2026-10-13: Current Coherent RFRS §1 and its parafree application retain the general conjectural relation and solve only the dimension-two comparison, not coherence for all finitely generated parafree groups.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/fisher-2025.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://arxiv.org/html/2603.16763)

<a id="q4854"></a>

## Q4854. Group coherence versus coherence of its group algebra

**Status:** Open · **Kind:** open problem (Question B.5) · **Reviewed extraction** 2026-10-13-250

For every group G and field k, is G coherent if and only if k[G] is coherent? A group is coherent if every finitely generated subgroup is finitely presented; a ring is coherent if every finitely generated one-sided ideal is finitely presented as a module (for group algebras, left and right coherence are equivalent).

**Source.** Samuel P. Fisher. *L²-Betti numbers and kernels of maps to ℤ*. University of Oxford, 2025. [primary source](https://ora.ox.ac.uk/objects/uuid:a95972ee-b2e7-49e9-bed9-bca1332c0373/files/dd791sg858) · [record](https://ora.ox.ac.uk/objects/uuid:a95972ee-b2e7-49e9-bed9-bca1332c0373) Location: Question B.5, printed p.85 / PDF p.91.

**Literature check.** Reviewed 2026-10-13: The March 2026 paper explicitly calls the general equivalence open and proves it for two-dimensional virtually RFRS groups. Its Corollary 4.1 does not settle arbitrary G.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/fisher-2025.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://arxiv.org/html/2603.16763)

<a id="q4855"></a>

## Q4855. Coherence of group algebras of 3-manifold groups

**Status:** Open · **Kind:** conjecture (Conjecture B.6) · **Reviewed extraction** 2026-10-13-250

For every connected 3-manifold M and every field k, is k[π\_1(M)] coherent, meaning that every finitely generated one-sided ideal is finitely presented as a module?

**Source.** Samuel P. Fisher. *L²-Betti numbers and kernels of maps to ℤ*. University of Oxford, 2025. [primary source](https://ora.ox.ac.uk/objects/uuid:a95972ee-b2e7-49e9-bed9-bca1332c0373/files/dd791sg858) · [record](https://ora.ox.ac.uk/objects/uuid:a95972ee-b2e7-49e9-bed9-bca1332c0373) Location: Conjecture B.6, printed p.85 / PDF p.91.

**Literature check.** Reviewed 2026-10-13: The held thesis asks this full question. Current geometric embedding and two-dimensional coherence results are not a theorem for all 3-manifold group algebras. Exact-theme and author-publication checks locate no full resolution.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/fisher-2025.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://ems.press/content/serial-article-files/52395) · [2](https://arxiv.org/html/2603.16763) · [3](https://sampfisher.github.io/)

<a id="q4856"></a>

## Q4856. Separating rational and integral group-ring coherence

**Status:** Open · **Kind:** open problem (Question B.7) · **Reviewed extraction** 2026-10-13-250

Does there exist a group G for which Q[G] is coherent but Z[G] is not coherent? Ring coherence means that all finitely generated one-sided ideals are finitely presented modules.

**Source.** Samuel P. Fisher. *L²-Betti numbers and kernels of maps to ℤ*. University of Oxford, 2025. [primary source](https://ora.ox.ac.uk/objects/uuid:a95972ee-b2e7-49e9-bed9-bca1332c0373/files/dd791sg858) · [record](https://ora.ox.ac.uk/objects/uuid:a95972ee-b2e7-49e9-bed9-bca1332c0373) Location: Question B.7, printed p.85 / PDF p.91.

**Literature check.** Reviewed 2026-10-13: The explicit thesis question remains outside the current field-based coherence and embedding results. Targeted current coefficient/coherence searches located no exact witness or impossibility theorem.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/fisher-2025.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://arxiv.org/html/2603.16763) · [2](https://matematicas.uam.es/~andrei.jaikin/preprints/coherencegroupalgebra.pdf) · [3](https://sampfisher.github.io/)

<a id="q4857"></a>

## Q4857. Integral coherence for free-by-cyclic and one-relator groups

**Status:** Open · **Kind:** conjecture (Conjecture B.8) · **Reviewed extraction** 2026-10-13-250

Is Z[G] coherent whenever G is free-by-cyclic or is a one-relator group? Free-by-cyclic means 1→F→G→Z→1 with F a free group; a one-relator group has a finite presentation with one relator. Coherent means that every finitely generated one-sided ideal is finitely presented as a Z[G]-module.

**Source.** Samuel P. Fisher. *L²-Betti numbers and kernels of maps to ℤ*. University of Oxford, 2025. [primary source](https://ora.ox.ac.uk/objects/uuid:a95972ee-b2e7-49e9-bed9-bca1332c0373/files/dd791sg858) · [record](https://ora.ox.ac.uk/objects/uuid:a95972ee-b2e7-49e9-bed9-bca1332c0373) Location: Conjecture B.8, printed p.85 / PDF p.91.

**Literature check.** Reviewed 2026-10-13: Current field-coherence theorems do not imply this integral assertion; Jaikin-Zapirain’s source explicitly distinguishes its field argument from integral one-relator group rings. No exact full theorem was located.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/fisher-2025.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://matematicas.uam.es/~andrei.jaikin/preprints/coherencegroupalgebra.pdf) · [2](https://arxiv.org/html/2603.16763) · [3](https://sampfisher.github.io/)

<a id="q4858"></a>

## Q4858. Universal Hughes-free division rings for torsion-free one-relator groups

**Status:** Open · **Kind:** conjecture (Conjecture B.10) · **Reviewed extraction** 2026-10-13-250

For every torsion-free one-relator group G and every field k, does k[G] admit an epic embedding into a division ring D which is both Hughes-free and universal? Hughes-free means that D is generated by k[G] and, for every N◁H≤G with H finitely generated and H/N≅Z, distinct powers of a lift of a generator of H/N are left-linearly independent over the division closure of k[N] in D. A k[G]-division ring is epic if the image of k[G] generates it as a division ring; it is universal if its matrix-rank function dominates that of every epic k[G]-division ring (equivalently it admits a specialization to each, in the sense of a homomorphism from a suitable local subring).

**Source.** Samuel P. Fisher. *L²-Betti numbers and kernels of maps to ℤ*. University of Oxford, 2025. [primary source](https://ora.ox.ac.uk/objects/uuid:a95972ee-b2e7-49e9-bed9-bca1332c0373/files/dd791sg858) · [record](https://ora.ox.ac.uk/objects/uuid:a95972ee-b2e7-49e9-bed9-bca1332c0373) Location: Conjecture B.10, printed p.86 / PDF p.92; Definitions 2.3.8 and 2.3.12–2.3.14, printed pp.15–17 / PDF pp.21–23.

**Literature check.** Reviewed 2026-10-13: Published Question 7.13 leaves general positive-characteristic Hughes-freeness unresolved; Remark 7.5 distinguishes rank maximality from universality. Neither the known characteristic-zero construction nor special-group results give the full assertion.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/fisher-2025.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://ems.press/content/serial-article-files/52395)

<a id="q4859"></a>

## Q4859. Universality of Hughes-free division rings for locally indicable 3-manifold groups

**Status:** Open · **Kind:** open problem (Question B.11) · **Reviewed extraction** 2026-10-13-250

Let G=π\_1(M) be the locally indicable fundamental group of a connected 3-manifold and let k be a field. Must its Hughes-free division ring D_{k[G]} be universal as an epic k[G]-division ring? Locally indicable means that every nontrivial finitely generated subgroup surjects onto Z. Hughes-free means that D is generated by k[G] and, for every N◁H≤G with H finitely generated and H/N≅Z, distinct powers of a lift of a generator of H/N are left-linearly independent over the division closure of k[N] in D. A k[G]-division ring is epic if the image of k[G] generates it as a division ring; it is universal if its matrix-rank function dominates that of every epic k[G]-division ring (equivalently it admits a specialization to each, in the sense of a homomorphism from a suitable local subring).

**Source.** Samuel P. Fisher. *L²-Betti numbers and kernels of maps to ℤ*. University of Oxford, 2025. [primary source](https://ora.ox.ac.uk/objects/uuid:a95972ee-b2e7-49e9-bed9-bca1332c0373/files/dd791sg858) · [record](https://ora.ox.ac.uk/objects/uuid:a95972ee-b2e7-49e9-bed9-bca1332c0373) Location: Question B.11, printed p.86 / PDF p.92; Hughes-free existence Theorem 5.3.7, printed pp.72–73 / PDF pp.78–79, within the cited Theorem 5.3.8.

**Literature check.** Reviewed 2026-10-13: The geometric construction establishes Hughes-freeness. The published rank-maximality remark does not establish universality; current exact property searches locate no full universality theorem.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/fisher-2025.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://ems.press/content/serial-article-files/52395) · [2](https://sampfisher.github.io/)

<a id="q4860"></a>

## Q4860. Universality for locally indicable virtually compact special groups

**Status:** Open · **Kind:** open problem (Question B.12) · **Reviewed extraction** 2026-10-13-250

Let G be a locally indicable virtually compact special group and k any field. Is the unique Hughes-free epic division ring generated by k[G] universal? Virtually compact special means that a finite-index subgroup is the fundamental group of a compact special nonpositively curved cube complex. Hughes-free means that D is generated by k[G] and, for every N◁H≤G with H finitely generated and H/N≅Z, distinct powers of a lift of a generator of H/N are left-linearly independent over the division closure of k[N] in D. A k[G]-division ring is epic if the image of k[G] generates it as a division ring; it is universal if its matrix-rank function dominates that of every epic k[G]-division ring (equivalently it admits a specialization to each, in the sense of a homomorphism from a suitable local subring).

**Source.** Samuel P. Fisher. *L²-Betti numbers and kernels of maps to ℤ*. University of Oxford, 2025. [primary source](https://ora.ox.ac.uk/objects/uuid:a95972ee-b2e7-49e9-bed9-bca1332c0373/files/dd791sg858) · [record](https://ora.ox.ac.uk/objects/uuid:a95972ee-b2e7-49e9-bed9-bca1332c0373) Location: Question B.12, printed p.86 / PDF p.92; Theorem 5.2.4 and Corollary 5.2.6, printed pp.67–69 / PDF pp.73–75.

**Literature check.** Reviewed 2026-10-13: The current published construction gives the Hughes-free ring, while its maximal-rank discussion explicitly cautions that maximal is weaker than universal. No exact general universality resolution was found.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/fisher-2025.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://ems.press/content/serial-article-files/52395) · [2](https://sampfisher.github.io/)

<a id="q4865"></a>

## Q4865. Vanishing of all degree-two cup products in free-group bounded cohomology

**Status:** Open · **Kind:** open problem (Question 1.2.1) · **Reviewed extraction** 2026-10-13-250

For every non-abelian free group F, is the cup product H_b²(F;ℝ)×H_b²(F;ℝ)→H_b⁴(F;ℝ), with trivial real coefficients, identically zero?

**Source.** Nicolaus Heuer. *Constructions in stable commutator length and bounded cohomology*. University of Oxford, 2019. [primary source](https://ora.ox.ac.uk/objects/uuid:0b46aef4-bdc7-4216-8ae3-e69db490c81c/files/mfc92d40b03b548491654af1a9d162570) · [record](https://ora.ox.ac.uk/objects/uuid:0b46aef4-bdc7-4216-8ae3-e69db490c81c) Location: Questions1.2.1 and4.0.1

**Literature check.** Reviewed 2026-10-13: Amontova–Bucher proves cup vanishing for a specified quasimorphism class against arbitrary positive degrees and still states the general question. Kastenholz2503.22511 was withdrawn September21,2026 for a fatal error; replacement2609.27476 explicitly leaves higher free-group bounded cohomology unknown. Neither is a closure of this cup question.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/heuer-2019.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://arxiv.org/pdf/2102.06394) · [2](https://arxiv.org/abs/2503.22511) · [3](https://arxiv.org/pdf/2609.27476)

<a id="q4866"></a>

## Q4866. Characterizing stable commutator length one-half in free groups

**Status:** Open · **Kind:** conjecture (Conjecture 6.3.1) · **Reviewed extraction** 2026-10-13-250

Let F be a non-abelian free group and f∈[F,F] satisfy scl_F(f)=1/2, where cl_F(g) is the minimum number of commutators multiplying to g and scl_F(g)=lim_{n→∞}cl_F(gⁿ)/n. Must either cl_F(f)=1 or there exist t∈F with cl_F(ftft⁻¹)=1?

**Source.** Nicolaus Heuer. *Constructions in stable commutator length and bounded cohomology*. University of Oxford, 2019. [primary source](https://ora.ox.ac.uk/objects/uuid:0b46aef4-bdc7-4216-8ae3-e69db490c81c/files/mfc92d40b03b548491654af1a9d162570) · [record](https://ora.ox.ac.uk/objects/uuid:0b46aef4-bdc7-4216-8ae3-e69db490c81c) Location: Conjecture6.3.1

**Literature check.** Reviewed 2026-10-13: Latest Chen–Heuer2026 orbifold paper concerns a uniform positive gap from zero (explicit1/36 generically), not this equality-case classification in free groups. Louder–Wilton only shows π(f)>2⇒scl(f)>1/2. Exact classification is not supplied by either result; bounded current searches found no full proof/counterexample.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/heuer-2019.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://arxiv.org/pdf/2604.21059v2) · [2](https://link.springer.com/article/10.1007/s00222-024-01246-4)

<a id="q4867"></a>

## Q4867. Primitivity-rank lower bound for stable commutator length

**Status:** Open · **Kind:** conjecture (Conjecture 6.3.2) · **Reviewed extraction** 2026-10-13-250

For every non-abelian finitely generated free group F and nontrivial w∈[F,F], does 2 scl_F(w)≥π\_F(w)−1 hold? Here scl_F(w)=lim_{n→∞}cl_F(wⁿ)/n, and π\_F(w)=min{rank(K):K≤F,w∈K,and w is not part of a free basis ofK}, with the minimum∞ if no suchK exists.

**Source.** Nicolaus Heuer. *Constructions in stable commutator length and bounded cohomology*. University of Oxford, 2019. [primary source](https://ora.ox.ac.uk/objects/uuid:0b46aef4-bdc7-4216-8ae3-e69db490c81c/files/mfc92d40b03b548491654af1a9d162570) · [record](https://ora.ox.ac.uk/objects/uuid:0b46aef4-bdc7-4216-8ae3-e69db490c81c) Location: Conjecture6.3.2

**Literature check.** Reviewed 2026-10-13: Louder–Wilton Conj1.7 is the exact target; its provedCorD is onlyπ>2⇒2scl>1. Puder–Shomroni May2026v4 Cor4.10 proves sπ≤2scl but invokes still-conjectural sπ=π−1 to reach Heuer’s bound. Their stable Fourier-coefficient sequel therefore does not settle ordinaryπ.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/heuer-2019.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://link.springer.com/article/10.1007/s00222-024-01246-4) · [2](https://arxiv.org/pdf/2311.17733v4)

<a id="q4868"></a>

## Q4868. Equivalence of the Gromov and finite-vanishing seminorms on free-group bounded cohomology

**Status:** Open · **Kind:** conjecture (Conjecture 6.5.1) · **Reviewed extraction** 2026-10-13-250

Fix a non-abelian finitely generated free group F. For every integer n≥3, is there C_n>0 such that C_n⁻¹‖α‖∞≤‖α‖∞,0≤C_n‖α‖∞ for every α∈H_bⁿ(F;ℝ)? Here ‖α‖∞ is the infimum of supremum norms of bounded cocycle representatives. In the homogeneous complex Cⁿ⁻¹(F)^F of invariant real functions on Fⁿ, set ‖α‖\_S=inf{‖δφ‖∞:φ∈Cⁿ⁻¹(F)^F,[δφ]=α,and φ|\_{Sⁿ}=0} for finiteS⊂F, and ‖α‖∞,0=sup_{S finite}‖α‖\_S; an empty infimum is∞.

**Source.** Nicolaus Heuer. *Constructions in stable commutator length and bounded cohomology*. University of Oxford, 2019. [primary source](https://ora.ox.ac.uk/objects/uuid:0b46aef4-bdc7-4216-8ae3-e69db490c81c/files/mfc92d40b03b548491654af1a9d162570) · [record](https://ora.ox.ac.uk/objects/uuid:0b46aef4-bdc7-4216-8ae3-e69db490c81c) Location: Conjecture6.5.1

**Literature check.** Reviewed 2026-10-13: FFPS defines the second seminorm and proves it dominates the first. Its constructed continuum-dimensional zero subspace has both seminorms zero, so that theorem is not a counterexample to equivalence. Lemma2.4’s infinity result is degree2, deliberately excluded. No dated primary closure of the n≥3 free-group comparison was identified; recommend withB grade.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/heuer-2019.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://arxiv.org/pdf/1703.03752) · [2](https://arxiv.org/pdf/2609.27476)

<a id="q4869"></a>

## Q4869. Finiteness of fixed-rank free-fibre orbits

**Status:** Open · **Kind:** open problem (Question 9.6.3) · **Reviewed extraction** 2026-10-13-250

A free-by-cyclic group here means G=F_r⋊\_ΦZ with F_r nontrivial and of finite rank. Fix n≥1 and let X_n(G) be the epimorphisms χ:G→Z with kerχ isomorphic to the free group F_n. Characterize when the precomposition action of Out(G) on X_n(G) has finitely many orbits.

**Source.** Monika Kudlinska. *Profinite and residual properties of fibred groups*. University of Oxford, 2024. [primary source](https://ora.ox.ac.uk/objects/uuid:2b52aee9-f134-4e46-b11c-bf5a242aeec9/files/dp2676w30c) · [record](https://ora.ox.ac.uk/objects/uuid:2b52aee9-f134-4e46-b11c-bf5a242aeec9) Location: Question9.6.3, printed147; corrected primitive-character scope in2026 Problem4

**Literature check.** Reviewed 2026-10-13: Current2026 Problem4 explicitly retains orbit finiteness after establishing computability of the set of primitive fixed-rank fibres. Thus BNS computability and full-dimensional-polytope finite cases do not close the general orbit question.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/kudlinska-2024.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://arxiv.org/html/2606.31774v1) · [2](https://sites.google.com/site/monkudlinska/papers)

<a id="q4870"></a>

## Q4870. Geometric three-manifold characterization of nonhyperbolic separable free-by-cyclic groups

**Status:** Open · **Kind:** open problem (Question 10.0.1) · **Reviewed extraction** 2026-10-13-250

A free-by-cyclic group here means G=F_r⋊\_ΦZ with F_r nontrivial and of finite rank. If G is not word-hyperbolic and is subgroup separable, must G be commensurable with the fundamental group of a geometric3-manifold? Subgroup separable means every finitely generated subgroup is closed in the profinite topology; commensurable means the two groups have isomorphic finite-index subgroups. Geometric refers to a manifold carrying one of Thurston’s eight geometries; no closedness assumption is added.

**Source.** Monika Kudlinska. *Profinite and residual properties of fibred groups*. University of Oxford, 2024. [primary source](https://ora.ox.ac.uk/objects/uuid:2b52aee9-f134-4e46-b11c-bf5a242aeec9/files/dp2676w30c) · [record](https://ora.ox.ac.uk/objects/uuid:2b52aee9-f134-4e46-b11c-bf5a242aeec9) Location: Question10.0.1, printed157

**Literature check.** Reviewed 2026-10-13: Current subgroup-separability source proves the polynomial subcase; the2026 conjugacy-separability paper proves a different separation property, and does not state full LERF classification.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/kudlinska-2024.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://arxiv.org/html/2211.05752v2) · [2](https://arxiv.org/html/2509.22346v2) · [3](https://sites.google.com/site/monkudlinska/papers)

<a id="q4871"></a>

## Q4871. Quasiconvexity or virtual fibre for hyperbolic free-by-cyclic subgroups

**Status:** Open · **Kind:** conjecture (Conjecture 10.0.2) · **Reviewed extraction** 2026-10-13-250

A free-by-cyclic group here means G=F_r⋊\_ΦZ with F_r nontrivial and of finite rank. If G is word-hyperbolic, is every finitely generated H≤G quasiconvex unless H is a virtual fibre or virtual semi-fibre of some free-by-cyclic subgroup G₀≤G containing H? A virtual fibre means that after passing to a finite-index G₁≤G₀, H∩G₁ is the kernel of a homomorphism G₁→Z; a virtual semi-fibre means that some such G₁ is a proper ascending HNN extension with base H∩G₁. Quasiconvex means geodesics between elements of H in a Cayley graph of G stay a uniformly bounded distance from H.

**Source.** Monika Kudlinska. *Profinite and residual properties of fibred groups*. University of Oxford, 2024. [primary source](https://ora.ox.ac.uk/objects/uuid:2b52aee9-f134-4e46-b11c-bf5a242aeec9/files/dp2676w30c) · [record](https://ora.ox.ac.uk/objects/uuid:2b52aee9-f134-4e46-b11c-bf5a242aeec9) Location: Conjecture10.0.2, printed158; virtual semi-fibre definition printed157

**Literature check.** Reviewed 2026-10-13: Latest largest-acylindrical-action theorem characterizes stable/strongly quasiconvex subgroups through geometry, but does not classify all distorted subgroups as fibres/semi-fibres. No current full closure located.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/kudlinska-2024.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://arxiv.org/html/2512.05293v1) · [2](https://sites.google.com/site/monkudlinska/papers)

<a id="q4872"></a>

## Q4872. Subgroup separability versus virtual BNS symmetry

**Status:** Open · **Kind:** conjecture (Conjecture 10.0.3) · **Reviewed extraction** 2026-10-13-250

A free-by-cyclic group here means G=F_r⋊\_ΦZ with F_r nontrivial and of finite rank. Write Σ¹(K) for the Bieri–Neumann–Strebel invariant: nonzero real character rays whose nonnegative-level subgraph of a Cayley graph is connected; symmetry means [χ]∈Σ¹(K) iff [−χ]∈Σ¹(K). For G word-hyperbolic with irreducible monodromy Φ, is G subgroup separable if and only if Σ¹(G₁) is symmetric for every finite-index subgroup G₁≤G? Irreducible means Φ preserves no nontrivial proper free-factor system of F_r.

**Source.** Monika Kudlinska. *Profinite and residual properties of fibred groups*. University of Oxford, 2024. [primary source](https://ora.ox.ac.uk/objects/uuid:2b52aee9-f134-4e46-b11c-bf5a242aeec9/files/dp2676w30c) · [record](https://ora.ox.ac.uk/objects/uuid:2b52aee9-f134-4e46-b11c-bf5a242aeec9) Location: Conjecture10.0.3, printed158

**Literature check.** Reviewed 2026-10-13: June2026 BNS-computation result supplies an algorithm for each group’s invariant, not a theorem equating the virtual symmetry condition with LERF. Current papers distinguish conjugacy and subgroup separability; no exact full closure located.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/kudlinska-2024.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://arxiv.org/html/2606.31774v1) · [2](https://arxiv.org/html/2211.05752v2) · [3](https://arxiv.org/html/2509.22346v2) · [4](https://sites.google.com/site/monkudlinska/papers)

<a id="q4873"></a>

## Q4873. Existence of regular profinite identifications for free-by-cyclic groups

**Status:** Open · **Kind:** open problem (Question 10.0.5) · **Reviewed extraction** 2026-10-13-250

A free-by-cyclic group here means G=F_r⋊\_ΦZ with F_r nontrivial and of finite rank. If G and H have isomorphic profinite completions, must there exist a continuous isomorphism Θ:Ĝ→Ĥ whose map on completed free abelianizations is μ·Ξ̂ for some μ∈Ẑ× and integral isomorphism Ξ:G^fab→H^fab? Here K^fab is K^ab modulo its torsion subgroup.

**Source.** Monika Kudlinska. *Profinite and residual properties of fibred groups*. University of Oxford, 2024. [primary source](https://ora.ox.ac.uk/objects/uuid:2b52aee9-f134-4e46-b11c-bf5a242aeec9/files/dp2676w30c) · [record](https://ora.ox.ac.uk/objects/uuid:2b52aee9-f134-4e46-b11c-bf5a242aeec9) Location: Question10.0.5, printed159; Definition6.3.2 printed85

**Literature check.** Reviewed 2026-10-13: Hughes–Kudlinska2025 retains the stronger regularity question. HananyJuly2026 proves regularity for hyperbolic3-manifolds, while free-by-cyclic Corollary4.3 expressly assumes Ẑ×-regularity; it does not provide the missing isomorphism for all free-by-cyclic groups.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/kudlinska-2024.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://arxiv.org/html/2303.16834v3) · [2](https://arxiv.org/html/2607.04530v1) · [3](https://sites.google.com/site/monkudlinska/papers)

<a id="q4874"></a>

## Q4874. Twisted Alexander polynomials detect semifibering in free-by-cyclic groups

**Status:** Open · **Kind:** open problem (Question 10.0.6) · **Reviewed extraction** 2026-10-13-250

A free-by-cyclic group here means G=F_r⋊\_ΦZ with F_r nontrivial and of finite rank. Write Σ¹(K) for the Bieri–Neumann–Strebel invariant: nonzero real character rays whose nonnegative-level subgraph of a Cayley graph is connected; symmetry means [χ]∈Σ¹(K) iff [−χ]∈Σ¹(K). For each field F∈{Q,F_p:p prime}, does every such G have the following property for every nonzero χ:G→Z? Either [χ] or [−χ] lies in Σ¹(G) if and only if, for every epimorphism α:G→Q_f to a finite group, the modules H_i(G;F[Q_f][t,t⁻¹]) have rank0 over F[t,t⁻¹] for i=0,1. The coefficient action is g·(a⊗t^j)=α(g)a⊗t^{j+χ(g)}. Equivalently, all these twisted Alexander polynomials are nonzero; this property is G∈TAP₁(F).

**Source.** Monika Kudlinska. *Profinite and residual properties of fibred groups*. University of Oxford, 2024. [primary source](https://ora.ox.ac.uk/objects/uuid:2b52aee9-f134-4e46-b11c-bf5a242aeec9/files/dp2676w30c) · [record](https://ora.ox.ac.uk/objects/uuid:2b52aee9-f134-4e46-b11c-bf5a242aeec9) Location: Question10.0.6, printed159; Hughes–Kielak Definition3.1

**Literature check.** Reviewed 2026-10-13: Explicitly retained in Hughes–Kudlinska2025 Question1.2. The2025 TAP theorem covers finitely presented LERF groups/products of limit groups, not every free-by-cyclic group; BNS computability2026 does not imply detection by finite-quotient Alexander polynomials.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/kudlinska-2024.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://arxiv.org/html/2303.16834v3) · [2](https://arxiv.org/pdf/2206.11347) · [3](https://arxiv.org/html/2606.31774v1) · [4](https://sites.google.com/site/monkudlinska/papers)

<a id="q4875"></a>

## Q4875. Irreducible monodromy as a profinite invariant

**Status:** Open · **Kind:** open problem (Question 10.0.7) · **Reviewed extraction** 2026-10-13-250

A free-by-cyclic group here means G=F_r⋊\_ΦZ with F_r nontrivial and of finite rank. If Ĝ≅Ĥ for two free-by-cyclic groups and G admits irreducible monodromy, must H admit irreducible monodromy? Irreducible means no nontrivial proper free-factor system is invariant.

**Source.** Monika Kudlinska. *Profinite and residual properties of fibred groups*. University of Oxford, 2024. [primary source](https://ora.ox.ac.uk/objects/uuid:2b52aee9-f134-4e46-b11c-bf5a242aeec9/files/dp2676w30c) · [record](https://ora.ox.ac.uk/objects/uuid:2b52aee9-f134-4e46-b11c-bf5a242aeec9) Location: Question10.0.7(1), printed159; counterpart Question1.3

**Literature check.** Reviewed 2026-10-13: The published2025 primary paper explicitly says hyperbolicity is detected but irreducibility is not yet shown and asks this exact question. Later2026 papers found concern conjugacy separation, norm and algorithmic BNS, not this finite-quotient recognition conclusion.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/kudlinska-2024.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://arxiv.org/html/2303.16834v3) · [2](https://arxiv.org/html/2606.31774v1) · [3](https://sites.google.com/site/monkudlinska/papers)

<a id="q4881"></a>

## Q4881. Division-ring homological independence of retracts in limit groups

**Status:** Open · **Kind:** conjecture (Conjecture 3.4.1) · **Reviewed extraction** 2026-10-13-250

Let L be a finitely generated fully residually free group (a limit group), and H≤L a retract, so there is r:L→H with r|\_H=id. Is H D_{K[L]}-independent for every field K? For a field K in the coefficient setup, D_{K[L]} denotes the unique epic Hughes-free division ring generated by K[L]. A subgroup H≤L is D_{K[L]}-independent when the natural inclusion-induced map H₁(H;D_{K[L]})→H₁(L;D_{K[L]}) is injective.

**Source.** Ismael Morales. *L2-invariants in abstract and profinite group theory*. University of Oxford, 2025. [primary source](https://ora.ox.ac.uk/objects/uuid:caa81b48-6ada-4b87-8703-51bb482a4aae/files/dk0698831p) · [record](https://ora.ox.ac.uk/objects/uuid:caa81b48-6ada-4b87-8703-51bb482a4aae) Location: Conjecture 3.4.1, printed p.65 / PDF p.73; Definitions 3.0.2–3.0.4, printed p.36 / PDF p.44.

**Literature check.** Reviewed 2026-10-13: The source explicitly isolates the retract assertion as conjectural despite proving the Hall property. Current published Hall results and fresh exact-topic retrieval supply no general retract theorem for all limit groups/all fields.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/morales-2025.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://sites.google.com/view/ismaelmorales/) · [2](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/D48EF6DC3997F72EDAE8DFBFFB1D407C/S0010437X25007444a.pdf/the-hanna-neumann-conjecture-for-graphs-of-free-groups-with-cyclic-edge-groups.pdf) · [3](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/AABCA00E7D74BE96CB547BC4FF76D000/S0010437X22007709a.pdf/the-hanna-neumann-conjecture-for-surface-groups.pdf)

<a id="q4882"></a>

## Q4882. Free-product closure for residually finite L²-Hall groups

**Status:** Open · **Kind:** open problem (Question 3.4.3) · **Reviewed extraction** 2026-10-13-250

If A and B are finitely generated residually finite L²-Hall groups, must A\*B be L²-Hall? A group J is L²-Hall if every finitely generated U≤J lies in a finite-index J₀≤J such that the kernel of H₁(U;N(J₀))→H₁(J₀;N(J₀)) has zero von Neumann dimension; N(J₀) is the group von Neumann algebra.

**Source.** Ismael Morales. *L2-invariants in abstract and profinite group theory*. University of Oxford, 2025. [primary source](https://ora.ox.ac.uk/objects/uuid:caa81b48-6ada-4b87-8703-51bb482a4aae/files/dk0698831p) · [record](https://ora.ox.ac.uk/objects/uuid:caa81b48-6ada-4b87-8703-51bb482a4aae) Location: Question 3.4.3, printed p.65 / PDF p.73; Definition 1.3.1, printed p.4 / PDF p.12.

**Literature check.** Reviewed 2026-10-13: The published paper explicitly leaves the residually finite case unclear and gives a non-residually-finite counterexample. That counterexample does not meet the source hypotheses. No later closure result located.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/morales-2025.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://sites.google.com/view/ismaelmorales/) · [2](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/D48EF6DC3997F72EDAE8DFBFFB1D407C/S0010437X25007444a.pdf/the-hanna-neumann-conjecture-for-graphs-of-free-groups-with-cyclic-edge-groups.pdf)

<a id="q4883"></a>

## Q4883. Positive-characteristic failure of the L²-Hall property

**Status:** Open · **Kind:** open problem (Question 3.4.5) · **Reviewed extraction** 2026-10-13-250

Does there exist an L²-Hall group G and a field K of positive characteristic for which D_{K[G]} is defined but G is not D_{K[G]}-Hall? A group J is L²-Hall if every finitely generated U≤J lies in a finite-index J₀≤J such that the kernel of H₁(U;N(J₀))→H₁(J₀;N(J₀)) has zero von Neumann dimension; N(J₀) is the group von Neumann algebra. For a field K in the coefficient setup, D_{K[G]} denotes the unique epic Hughes-free division ring generated by K[G]. A subgroup H≤G is D_{K[G]}-independent when the natural inclusion-induced map H₁(H;D_{K[G]})→H₁(G;D_{K[G]}) is injective. G is D_{K[G]}-Hall when every finitely generated subgroup H≤G is contained in a finite-index G₀≤G in which H is independent in this sense; coefficient extension to the ambient division ring gives the same condition.

**Source.** Ismael Morales. *L2-invariants in abstract and profinite group theory*. University of Oxford, 2025. [primary source](https://ora.ox.ac.uk/objects/uuid:caa81b48-6ada-4b87-8703-51bb482a4aae/files/dk0698831p) · [record](https://ora.ox.ac.uk/objects/uuid:caa81b48-6ada-4b87-8703-51bb482a4aae) Location: Question 3.4.5, printed p.66 / PDF p.74; Definitions 1.3.1 and 3.0.2–3.0.4, printed pp.4,36 / PDF pp.12,44.

**Literature check.** Reviewed 2026-10-13: The thesis asks this coefficient separation. Current examples prove equality in specific hierarchical families; fresh exact-topic and author checks locate no general witness or impossibility result.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/morales-2025.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://sites.google.com/view/ismaelmorales/) · [2](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/D48EF6DC3997F72EDAE8DFBFFB1D407C/S0010437X25007444a.pdf/the-hanna-neumann-conjecture-for-graphs-of-free-groups-with-cyclic-edge-groups.pdf)

<a id="q4884"></a>

## Q4884. Field independence of division-ring homological subgroup independence

**Status:** Open · **Kind:** open problem (Question 3.4.6) · **Reviewed extraction** 2026-10-13-250

Let H≤G be finitely generated, and let K₁,K₂ be fields for which the Hughes-free coefficient rings D_{K₁[G]} and D_{K₂[G]} exist. If H is D_{K₁[G]}-independent in G, must it be D_{K₂[G]}-independent? For a field K in the coefficient setup, D_{K[G]} denotes the unique epic Hughes-free division ring generated by K[G]. A subgroup H≤G is D_{K[G]}-independent when the natural inclusion-induced map H₁(H;D_{K[G]})→H₁(G;D_{K[G]}) is injective.

**Source.** Ismael Morales. *L2-invariants in abstract and profinite group theory*. University of Oxford, 2025. [primary source](https://ora.ox.ac.uk/objects/uuid:caa81b48-6ada-4b87-8703-51bb482a4aae/files/dk0698831p) · [record](https://ora.ox.ac.uk/objects/uuid:caa81b48-6ada-4b87-8703-51bb482a4aae) Location: Question 3.4.6, printed p.66 / PDF p.74; Definition 3.0.2, printed p.36 / PDF p.44.

**Literature check.** Reviewed 2026-10-13: The source says even the free-group case is open beyond the known F₂-versus-Q comparison. Current Hall results for named families and fresh coefficient-independence retrieval provide no all-field comparison theorem.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/morales-2025.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://sites.google.com/view/ismaelmorales/) · [2](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/D48EF6DC3997F72EDAE8DFBFFB1D407C/S0010437X25007444a.pdf/the-hanna-neumann-conjecture-for-graphs-of-free-groups-with-cyclic-edge-groups.pdf)

<a id="q4885"></a>

## Q4885. The L²-Hall and strengthened Hanna Neumann properties for finite abelian hierarchies

**Status:** Open · **Kind:** conjecture (Conjecture 3.4.8) · **Reviewed extraction** 2026-10-13-250

Define C₀={1}. Inductively, C_{j+1} consists of groups virtually in C_j and groups obtained as HNN extensions H\*\_A or amalgams H\*\_A K with H,K∈C_j and A finitely generated free abelian. Let G lie in some C_j and be torsion-free and hyperbolic relative to virtually abelian subgroups. Must G be L²-Hall and satisfy the strengthened Hanna Neumann inequality Σ\_{t∈U\G/V} χ̄(U∩tVt⁻¹)≤χ̄(U)χ̄(V) for every finitely generated U,V≤G? Here χ̄(J)=max{−χ(J),0} is reduced Euler characteristic. A group J is L²-Hall if every finitely generated U≤J lies in a finite-index J₀≤J such that the kernel of H₁(U;N(J₀))→H₁(J₀;N(J₀)) has zero von Neumann dimension; N(J₀) is the group von Neumann algebra.

**Source.** Ismael Morales. *L2-invariants in abstract and profinite group theory*. University of Oxford, 2025. [primary source](https://ora.ox.ac.uk/objects/uuid:caa81b48-6ada-4b87-8703-51bb482a4aae/files/dk0698831p) · [record](https://ora.ox.ac.uk/objects/uuid:caa81b48-6ada-4b87-8703-51bb482a4aae) Location: Conjecture 3.4.8 and hierarchy Definition 3.4.7, printed p.66 / PDF p.74. Published counterpart Conjecture 1.3.

**Literature check.** Reviewed 2026-10-13: Retained in published Conjecture 1.3. Theorems for limit groups and cyclic-edge graphs are proper subcases; current author and exact-topic checks locate no full finite-abelian-hierarchy theorem.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/morales-2025.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://sites.google.com/view/ismaelmorales/) · [2](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/D48EF6DC3997F72EDAE8DFBFFB1D407C/S0010437X25007444a.pdf/the-hanna-neumann-conjecture-for-graphs-of-free-groups-with-cyclic-edge-groups.pdf)

<a id="q4886"></a>

## Q4886. Finite-group word measures determine the free-group automorphism orbit

**Status:** Open · **Kind:** conjecture (Conjecture 4.1.1) · **Reviewed extraction** 2026-10-13-250

Let F be free on a finite basis x₁,…,x_d and u,w∈F. For a finite group A, a word v defines v_A:A^d→A by substitution. Suppose |u_A⁻¹(a)|=|w_A⁻¹(a)| for every finite A and a∈A. Must there exist φ∈Aut(F) with u=φ(w)?

**Source.** Ismael Morales. *L2-invariants in abstract and profinite group theory*. University of Oxford, 2025. [primary source](https://ora.ox.ac.uk/objects/uuid:caa81b48-6ada-4b87-8703-51bb482a4aae/files/dk0698831p) · [record](https://ora.ox.ac.uk/objects/uuid:caa81b48-6ada-4b87-8703-51bb482a4aae) Location: Conjecture 4.1.1, printed p.69 / PDF p.77; repeated discussion printed p.90 / PDF p.98.

**Literature check.** Reviewed 2026-10-13: The current prosolvable-rigidity paper retains the general conjecture, and February 2026 Subgroup measures and profinite rigidity in free groups still states it while extending the framework to subgroups. No general closure located.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/morales-2025.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://arxiv.org/html/2312.12293) · [2](https://arxiv.org/html/2602.12815) · [3](https://sites.google.com/view/ismaelmorales/)

<a id="q4887"></a>

## Q4887. Profinite rigidity of doubles among cyclic-edge graphs of free groups

**Status:** Open · **Kind:** open problem (Question 4.8.1) · **Reviewed extraction** 2026-10-13-250

Let F be a finitely generated free group and u∈F, and let D_u=F\*\_{⟨u⟩}F be the double formed by identifying corresponding copies of ⟨u⟩. If H is the fundamental group of a finite graph of finitely generated free groups with cyclic edge groups and Ĥ≅D̂\_u, must H≅D_u?

**Source.** Ismael Morales. *L2-invariants in abstract and profinite group theory*. University of Oxford, 2025. [primary source](https://ora.ox.ac.uk/objects/uuid:caa81b48-6ada-4b87-8703-51bb482a4aae/files/dk0698831p) · [record](https://ora.ox.ac.uk/objects/uuid:caa81b48-6ada-4b87-8703-51bb482a4aae) Location: Question 4.8.1, printed p.90 / PDF p.98; corresponding double construction discussed in §4.6.

**Literature check.** Reviewed 2026-10-13: The source retains this general double recognition question. Published surface recognition and 2026 free-factor detection results concern narrower words or additional structure; no full arbitrary-double recognition theorem located.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/morales-2025.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://arxiv.org/html/2312.12293) · [2](https://sites.google.com/view/ismaelmorales/)

<a id="q4888"></a>

## Q4888. Parafree Mel’nikov groups are free

**Status:** Open · **Kind:** conjecture (Conjecture 4.8.3) · **Reviewed extraction** 2026-10-13-250

Let G be parafree and suppose every finite-index subgroup of G is a one-relator group. Must G be free? Parafree means that G is residually nilpotent and has the same lower-central-series quotients as some free group; one-relator means a finite presentation with one defining relation.

**Source.** Ismael Morales. *L2-invariants in abstract and profinite group theory*. University of Oxford, 2025. [primary source](https://ora.ox.ac.uk/objects/uuid:caa81b48-6ada-4b87-8703-51bb482a4aae/files/dk0698831p) · [record](https://ora.ox.ac.uk/objects/uuid:caa81b48-6ada-4b87-8703-51bb482a4aae) Location: Conjecture 4.8.3, printed p.90 / PDF p.98.

**Literature check.** Reviewed 2026-10-13: The source proves the parasurface case but explicitly leaves the parafree case. Current parafree results do not supply this all-finite-index one-relator classification. It is related to existing Q2722 but has a narrower hypothesis and a sharper free conclusion.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/morales-2025.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://arxiv.org/html/2312.12293) · [2](https://sites.google.com/view/ismaelmorales/) · [3](https://arxiv.org/abs/2609.19595)

<a id="q4889"></a>

## Q4889. Virtual nonzero second Betti number in one-relator groups

**Status:** Open · **Kind:** open problem (Question 4.8.4) · **Reviewed extraction** 2026-10-13-250

Classify the one-relator groups G for which some finite-index subgroup H≤G has b₂(H)=dim_Q H₂(H;Q)>0. In particular, does every one-ended hyperbolic one-relator group have such a finite-index subgroup?

**Source.** Ismael Morales. *L2-invariants in abstract and profinite group theory*. University of Oxford, 2025. [primary source](https://ora.ox.ac.uk/objects/uuid:caa81b48-6ada-4b87-8703-51bb482a4aae/files/dk0698831p) · [record](https://ora.ox.ac.uk/objects/uuid:caa81b48-6ada-4b87-8703-51bb482a4aae) Location: Question 4.8.4, printed p.91 / PDF p.99.

**Literature check.** Reviewed 2026-10-13: The prosolvable-rigidity result uses virtual nonzero second homology as an additional hypothesis rather than proving it in all groups. Current two-dimensional L²/coherence theorems concern a different invariant, and no full classification or general named-family theorem was located.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/morales-2025.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://arxiv.org/html/2312.12293) · [2](https://arxiv.org/html/2603.16763) · [3](https://sites.google.com/view/ismaelmorales/)

<a id="q4890"></a>

## Q4890. Virtual positive second homology of one-ended hyperbolic special groups

**Status:** Open · **Kind:** conjecture (Conjecture 4.8.5) · **Reviewed extraction** 2026-10-13-250

Must every one-ended hyperbolic special group G have a finite-index subgroup H≤G with b₂(H)=dim_Q H₂(H;Q)>0? Special means the fundamental group of a special nonpositively curved cube complex in the sense of Haglund–Wise.

**Source.** Ismael Morales. *L2-invariants in abstract and profinite group theory*. University of Oxford, 2025. [primary source](https://ora.ox.ac.uk/objects/uuid:caa81b48-6ada-4b87-8703-51bb482a4aae/files/dk0698831p) · [record](https://ora.ox.ac.uk/objects/uuid:caa81b48-6ada-4b87-8703-51bb482a4aae) Location: Conjecture 4.8.5, printed p.91 / PDF p.99.

**Literature check.** Reviewed 2026-10-13: The thesis explicitly proposes this virtual-homology assertion. Current L²-coherence and profinite recognition theorems do not establish it, and exact-topic searches yielded no full theorem or counterexample.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/morales-2025.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://arxiv.org/html/2312.12293) · [2](https://arxiv.org/html/2603.16763) · [3](https://sites.google.com/view/ismaelmorales/)

<a id="q4914"></a>

## Q4914. Compute exact distance in the free factor complex

**Status:** Open · **Kind:** open problem (Question 3) · **Reviewed extraction** 2026-10-13-250

For n≥3, let FFₙ have vertices the conjugacy classes [H] of nontrivial proper free factors H≤Fₙ, and an edge when representatives of two classes are comparable by inclusion. Is there an algorithm which, given finite generators for two free factors, returns their combinatorial distance in the 1-skeleton of FFₙ?

**Source.** Dario Ascari. *Free groups and Stallings' folding*. University of Oxford, 2023. [primary source](https://ora.ox.ac.uk/objects/uuid:8b614a9f-978e-4d53-b420-e1b928a7dc03/files/d8w32r626t) · [record](https://ora.ox.ac.uk/objects/uuid:8b614a9f-978e-4d53-b420-e1b928a7dc03) Location: Question 3; Definition 3.3.1 printed71 (physical76)

**Literature check.** Reviewed 2026-10-13: The published 2024 paper still provides algorithms only for distances1,2,3 and4 with a codimension-one factor. Fresh exact-distance searches located no full closure.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/ascari-2023.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://ems.press/content/serial-article-files/42594) · [2](https://www.cmup.pt/sites/default/files/2024-09/2306.12533v1.pdf) · [3](https://arxiv.org/abs/math/0306380)

<a id="q4915"></a>

## Q4915. Recognize the fixed subgroup of a single free-group automorphism

**Status:** Open · **Kind:** open problem (Question 4) · **Reviewed extraction** 2026-10-13-250

Is there an algorithm which, given n≥2 and a finite list of words generating H≤Fₙ, decides whether H=Fix(φ)={w∈Fₙ:φ(w)=w} for some single automorphism φ∈Aut(Fₙ)?

**Source.** Dario Ascari. *Free groups and Stallings' folding*. University of Oxford, 2023. [primary source](https://ora.ox.ac.uk/objects/uuid:8b614a9f-978e-4d53-b420-e1b928a7dc03/files/d8w32r626t) · [record](https://ora.ox.ac.uk/objects/uuid:8b614a9f-978e-4d53-b420-e1b928a7dc03) Location: Question4; §3.4 printed75

**Literature check.** Reviewed 2026-10-13: Carvalho 2023 primary introduction explicitly retains recognition for a single automorphism as undecided (Question8.6). Martino–Ventura structural description2003 is not claimed to be an effective recognition procedure. No later full algorithm located.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/ascari-2023.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://ems.press/content/serial-article-files/42594) · [2](https://www.cmup.pt/sites/default/files/2024-09/2306.12533v1.pdf) · [3](https://arxiv.org/abs/math/0306380)

<a id="q4916"></a>

## Q4916. Generalized Tarski problem with the finite radical

**Status:** Open · **Kind:** stated as open · **Reviewed extraction** 2026-10-13-250

A group is acylindrically hyperbolic if it admits a non-elementary acylindrical isometric action on a Gromov-hyperbolic space; acylindrical means that for each ε>0 there are R,N such that at most N elements move each of any two points distance≥R by≤ε. For every such G, write E(G) for its maximal finite normal subgroup and G\*=⟨G,t | [t,e]=1 for all e∈E(G)⟩=G\*ₑ₍G₎(E(G)×ℤ). Are G and G\* elementarily equivalent? More strongly, is the canonical inclusion G→G\* an elementary embedding?

**Source.** Jonathan Fruchter. *Beyond limit groups: formal solutions and the profinite topology*. University of Oxford, 2023. [primary source](https://ora.ox.ac.uk/objects/uuid:f4668eab-9f91-4a0e-88d5-d31dc134ca51/files/d3n203z80f) · [record](https://ora.ox.ac.uk/objects/uuid:f4668eab-9f91-4a0e-88d5-d31dc134ca51) Location: Generalised Tarski Problem physical12–13; introductory open sentence

**Literature check.** Reviewed 2026-10-13: André–Fruchter published paper jlms.12526 retains generalized Tarski problem and explains that its theorem proves only ∃∀∃ embedding. Fresh2026 queries and author work list found no full elementary-theory closure.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/fruchter-2023.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/jlms.12526) · [2](https://arxiv.org/html/2209.14925v3) · [3](https://arxiv.org/html/2505.20960v1) · [4](https://webusers.imj-prg.fr/~simon.andre/anglais.html)

<a id="q4917"></a>

## Q4917. A non-acylindrically hyperbolic group equivalent to its free product with ℤ

**Status:** Open · **Kind:** open problem (Question III.8.2) · **Reviewed extraction** 2026-10-13-250

A group is acylindrically hyperbolic if it admits a non-elementary acylindrical isometric action on a Gromov-hyperbolic space; acylindrical means that for each ε>0 there are R,N such that at most N elements move each of any two points distance≥R by≤ε. Does there exist a finitely generated G that is not acylindrically hyperbolic but is elementarily equivalent to G\*ℤ? Does such a G at least exist with the same ∀∃-theory as G\*ℤ (the same sentences ∀x∃y ψ(x,y) with quantifier-free ψ)?

**Source.** Jonathan Fruchter. *Beyond limit groups: formal solutions and the profinite topology*. University of Oxford, 2023. [primary source](https://ora.ox.ac.uk/objects/uuid:f4668eab-9f91-4a0e-88d5-d31dc134ca51/files/d3n203z80f) · [record](https://ora.ox.ac.uk/objects/uuid:f4668eab-9f91-4a0e-88d5-d31dc134ca51) Location: QuestionIII.8.2

**Literature check.** Reviewed 2026-10-13: Published Question10.2 retains exactly these alternatives. Its conditional connection to preservation is not a counterexample. No exact later closure located in fresh searches.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/fruchter-2023.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/jlms.12526) · [2](https://arxiv.org/html/2209.14925v3) · [3](https://arxiv.org/html/2505.20960v1) · [4](https://webusers.imj-prg.fr/~simon.andre/anglais.html)

<a id="q4918"></a>

## Q4918. Elementary invariance of acylindrical hyperbolicity for finitely generated groups

**Status:** Open · **Kind:** open problem (Question III.8.3) · **Reviewed extraction** 2026-10-13-250

A group is acylindrically hyperbolic if it admits a non-elementary acylindrical isometric action on a Gromov-hyperbolic space; acylindrical means that for each ε>0 there are R,N such that at most N elements move each of any two points distance≥R by≤ε. If finitely generated groups G,H satisfy exactly the same first-order sentences in the language of groups and G is acylindrically hyperbolic, must H be acylindrically hyperbolic?

**Source.** Jonathan Fruchter. *Beyond limit groups: formal solutions and the profinite topology*. University of Oxford, 2023. [primary source](https://ora.ox.ac.uk/objects/uuid:f4668eab-9f91-4a0e-88d5-d31dc134ca51/files/d3n203z80f) · [record](https://ora.ox.ac.uk/objects/uuid:f4668eab-9f91-4a0e-88d5-d31dc134ca51) Location: QuestionIII.8.3

**Literature check.** Reviewed 2026-10-13: Published Question10.3 explicitly retains the finite-generation version. Hyperbolicity/cubulability invariance and the special splitting proposition do not settle acylindrical hyperbolicity. No later general closure located.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/fruchter-2023.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/jlms.12526) · [2](https://arxiv.org/html/2209.14925v3) · [3](https://arxiv.org/html/2505.20960v1) · [4](https://webusers.imj-prg.fr/~simon.andre/anglais.html)

<a id="q4919"></a>

## Q4919. Virtual cohomology spectra of limit groups and HGFC-groups

**Status:** Open · **Kind:** open problem (Question V.4.9) · **Reviewed extraction** 2026-10-13-250

A limit group is a finitely generated fully residually free group: every finite subset is mapped injectively by some homomorphism to a free group. An HGFC-group is a word-hyperbolic group which is the fundamental group of a finite graph of finitely generated free groups with infinite cyclic edge groups. For a given such G, field k and integer i≥0, determine Spectrumᵏᵢ(G)={dimₖ Hⁱ(H;k):H≤G and [G:H]<∞}. In particular, which integers occur, rather than merely whether this set is bounded?

**Source.** Jonathan Fruchter. *Beyond limit groups: formal solutions and the profinite topology*. University of Oxford, 2023. [primary source](https://ora.ox.ac.uk/objects/uuid:f4668eab-9f91-4a0e-88d5-d31dc134ca51/files/d3n203z80f) · [record](https://ora.ox.ac.uk/objects/uuid:f4668eab-9f91-4a0e-88d5-d31dc134ca51) Location: QuestionV.4.9; DefinitionV.4.8

**Literature check.** Reviewed 2026-10-13: Current paper2209.14925v3 Question5.8(1) retains this target after proving virtual Betti boundedness classification.2025 torsion-abundance paper does not calculate these spectra. Fresh exact-spectrum query located no closure.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/fruchter-2023.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/jlms.12526) · [2](https://arxiv.org/html/2209.14925v3) · [3](https://arxiv.org/html/2505.20960v1) · [4](https://webusers.imj-prg.fr/~simon.andre/anglais.html)

<a id="q4920"></a>

## Q4920. Rigidity from filtered second Betti spectra

**Status:** Open · **Kind:** open problem (Question V.4.10) · **Reviewed extraction** 2026-10-13-250

A limit group is a finitely generated fully residually free group: every finite subset is mapped injectively by some homomorphism to a free group. An HGFC-group is a word-hyperbolic group which is the fundamental group of a finite graph of finitely generated free groups with infinite cyclic edge groups. For each field k let FSpectrum²ₖ(G)={dimₖ H²(H;k)/[G:H]:H≤G and [G:H]<∞}. Which groups G in the union of the limit-group and HGFC classes are characterized up to isomorphism within that union by this invariant? That is, for which G does equality FSpectrum²ₖ(G)=FSpectrum²ₖ(H) force H≅G for every H in these classes?

**Source.** Jonathan Fruchter. *Beyond limit groups: formal solutions and the profinite topology*. University of Oxford, 2023. [primary source](https://ora.ox.ac.uk/objects/uuid:f4668eab-9f91-4a0e-88d5-d31dc134ca51/files/d3n203z80f) · [record](https://ora.ox.ac.uk/objects/uuid:f4668eab-9f91-4a0e-88d5-d31dc134ca51) Location: QuestionV.4.10 and preceding filtered-spectrum definition

**Literature check.** Reviewed 2026-10-13: Current primary Question5.8(2) retains filtered-spectrum classification. The2025 free-product profinite-rigidity theorem uses all finite quotients, a stronger invariant, and does not answer this question. No full closure located.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/fruchter-2023.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/jlms.12526) · [2](https://arxiv.org/html/2209.14925v3) · [3](https://arxiv.org/html/2505.20960v1) · [4](https://webusers.imj-prg.fr/~simon.andre/anglais.html)

<a id="q4921"></a>

## Q4921. Three normal generators for Epstein’s relation subgroup

**Status:** Open · **Kind:** stated as open · **Reviewed extraction** 2026-10-13-250

Let F=F(a,b,c,d), and let R be the normal closure in F of [a,b], b², [c,d], d³. Can R be normally generated in F by three elements? Equivalently, can the marked presentation of (ℤ×ℤ/2)\*(ℤ×ℤ/3) on a,b,c,d be replaced by three defining relators?

**Source.** Giles Gardam. *Encoding and detecting properties in finitely presented groups*. University of Oxford, 2017. [primary source](https://ora.ox.ac.uk/objects/uuid:0c8a7009-7e04-4f66-911b-298ad87061fb/files/m4392ba4e8cd5c325080c1cfdf63b2719) · [record](https://ora.ox.ac.uk/objects/uuid:0c8a7009-7e04-4f66-911b-298ad87061fb) Location: Gardam thesis, printed21 (physical35)

**Literature check.** Reviewed 2026-10-13: Held source and Harlander primary relation-gap lecture retain the Epstein example. Fresh Epstein/relation-gap searches found no proof that this R is normally3-generated or requires4.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/gardam-2017.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://www.gilesgardam.com/) · [2](https://arxiv.org/pdf/1705.09348) · [3](https://arxiv.org/html/2501.18306v1) · [4](https://arxiv.org/abs/2303.05976) · [5](https://mathshistory.st-andrews.ac.uk/Groups/2013/slides/harlander.pdf) · [6](https://arxiv.org/abs/2508.20110) · [7](https://arxiv.org/abs/2412.05229) · [8](https://arxiv.org/html/2505.20960v1)

<a id="q4922"></a>

## Q4922. Four-relator cores detecting commutativity from coprime powers

**Status:** Open · **Kind:** open problem (Question 2.45) · **Reviewed extraction** 2026-10-13-250

For coprime positive integers m,n let F=F(a,b), F^(r)=⟨uʳ:u∈F⟩, and Qₘ,ₙ=⟨a,b | [u,v], u,v∈F^(m); [u,v], u,v∈F^(n)⟩. For which m,n does a four-relator subpresentation of Qₘ,ₙ already present ℤ² via the natural map on a,b? In particular, for which pairs is Δₘ,ₙ=⟨a,b | [aᵐ,bᵐ],[aⁿ,bⁿ],[(ab)ᵐ,(ba)ᵐ],[(ab)ⁿ,(ba)ⁿ]⟩ isomorphic to ℤ²?

**Source.** Giles Gardam. *Encoding and detecting properties in finitely presented groups*. University of Oxford, 2017. [primary source](https://ora.ox.ac.uk/objects/uuid:0c8a7009-7e04-4f66-911b-298ad87061fb/files/m4392ba4e8cd5c325080c1cfdf63b2719) · [record](https://ora.ox.ac.uk/objects/uuid:0c8a7009-7e04-4f66-911b-298ad87061fb) Location: Gardam thesis, printed43 (physical57)

**Literature check.** Reviewed 2026-10-13: Primary2019 paper (arXiv1705.09348)§6 Questions1–2 retain both targets; the(2,3) example and bounded computations do not resolve all coprime pairs. Fresh four-relator/Gardam query found no later closure.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/gardam-2017.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://www.gilesgardam.com/) · [2](https://arxiv.org/pdf/1705.09348) · [3](https://arxiv.org/html/2501.18306v1) · [4](https://arxiv.org/abs/2303.05976) · [5](https://mathshistory.st-andrews.ac.uk/Groups/2013/slides/harlander.pdf) · [6](https://arxiv.org/abs/2508.20110) · [7](https://arxiv.org/abs/2412.05229) · [8](https://arxiv.org/html/2505.20960v1)

<a id="q4923"></a>

## Q4923. Minimum core size for nilpotency detected in power subgroups

**Status:** Open · **Kind:** open problem (Question 2.46) · **Reviewed extraction** 2026-10-13-250

For c≥1 and coprime positive m,n, set k=c+1, F=F(x₁,…,xₖ), F^(r)=⟨uʳ:u∈F⟩, and ν\_c(y₁,…,yₖ)=[[…[y₁,y₂],y₃],…,yₖ]. Let Q=⟨x₁,…,xₖ | ν\_c(u₁,…,uₖ), uᵢ∈F^(m); ν\_c(v₁,…,vₖ),vᵢ∈F^(n)⟩. Determine the minimum cardinality of a finite subset of these relators presenting the same marked group, as a function of c,m,n.

**Source.** Giles Gardam. *Encoding and detecting properties in finitely presented groups*. University of Oxford, 2017. [primary source](https://ora.ox.ac.uk/objects/uuid:0c8a7009-7e04-4f66-911b-298ad87061fb/files/m4392ba4e8cd5c325080c1cfdf63b2719) · [record](https://ora.ox.ac.uk/objects/uuid:0c8a7009-7e04-4f66-911b-298ad87061fb) Location: Gardam thesis, printed44 (physical58)

**Literature check.** Reviewed 2026-10-13: Question2 in current primary1705.09348§6 retains this exact complexity target; explicit8-relator abelian construction is a bound, not minimality. No later exact formula located.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/gardam-2017.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://www.gilesgardam.com/) · [2](https://arxiv.org/pdf/1705.09348) · [3](https://arxiv.org/html/2501.18306v1) · [4](https://arxiv.org/abs/2303.05976) · [5](https://mathshistory.st-andrews.ac.uk/Groups/2013/slides/harlander.pdf) · [6](https://arxiv.org/abs/2508.20110) · [7](https://arxiv.org/abs/2412.05229) · [8](https://arxiv.org/html/2505.20960v1)

<a id="q4924"></a>

## Q4924. Classify laws detectable in coprime power subgroups

**Status:** Open · **Kind:** open problem (Question 2.47) · **Reviewed extraction** 2026-10-13-250

For a word w∈F(x₁,…,xₖ), say G satisfies w if w(g₁,…,gₖ)=1 for every k-tuple in G. Write G^(r)=⟨gʳ:g∈G⟩. Classify words w such that, for every group G and every pair of coprime positive integers m,n, G satisfies w whenever both G^(m) and G^(n) satisfy w.

**Source.** Giles Gardam. *Encoding and detecting properties in finitely presented groups*. University of Oxford, 2017. [primary source](https://ora.ox.ac.uk/objects/uuid:0c8a7009-7e04-4f66-911b-298ad87061fb/files/m4392ba4e8cd5c325080c1cfdf63b2719) · [record](https://ora.ox.ac.uk/objects/uuid:0c8a7009-7e04-4f66-911b-298ad87061fb) Location: Gardam thesis, printed44 (physical58)

**Literature check.** Reviewed 2026-10-13: Author primary page and1705.09348§6 Question3 retain classification. Its nilpotent/locally-nilpotent results and metabelian counterexample are partial classification only. No full characterization found.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/gardam-2017.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://www.gilesgardam.com/) · [2](https://arxiv.org/pdf/1705.09348) · [3](https://arxiv.org/html/2501.18306v1) · [4](https://arxiv.org/abs/2303.05976) · [5](https://mathshistory.st-andrews.ac.uk/Groups/2013/slides/harlander.pdf) · [6](https://arxiv.org/abs/2508.20110) · [7](https://arxiv.org/abs/2412.05229) · [8](https://arxiv.org/html/2505.20960v1)

<a id="q4925"></a>

## Q4925. Automaticity of one-relator groups without unbalanced Baumslag–Solitar subgroups

**Status:** Open · **Kind:** open problem (Problem 3.1 ([MUW11, Problem 1.5])) · **Reviewed extraction** 2026-10-13-250

Let G have a finite presentation with one defining relator. Suppose G contains no subgroup isomorphic to BS(m,n)=⟨a,t | t⁻¹aᵐt=aⁿ⟩ with m,n nonzero integers and |m|≠|n|. Must G be automatic: admit a finite generating set and a regular language of representatives with a synchronous fellow-traveller bound for pairs representing elements differing by a generator?

**Source.** Giles Gardam. *Encoding and detecting properties in finitely presented groups*. University of Oxford, 2017. [primary source](https://ora.ox.ac.uk/objects/uuid:0c8a7009-7e04-4f66-911b-298ad87061fb/files/m4392ba4e8cd5c325080c1cfdf63b2719) · [record](https://ora.ox.ac.uk/objects/uuid:0c8a7009-7e04-4f66-911b-298ad87061fb) Location: Gardam thesis, printed45 (physical59)

**Literature check.** Reviewed 2026-10-13: Gardam primary author list retains census results; current one-relator survey covers geometric improvements but no universal automaticity theorem located. Fresh CAT/automatic searches find counterexamples to biautomaticity only, which do not refute this target.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/gardam-2017.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://www.gilesgardam.com/) · [2](https://arxiv.org/pdf/1705.09348) · [3](https://arxiv.org/html/2501.18306v1) · [4](https://arxiv.org/abs/2303.05976) · [5](https://mathshistory.st-andrews.ac.uk/Groups/2013/slides/harlander.pdf) · [6](https://arxiv.org/abs/2508.20110) · [7](https://arxiv.org/abs/2412.05229) · [8](https://arxiv.org/html/2505.20960v1)

<a id="q4926"></a>

## Q4926. Polynomial-time word problem for every one-relator group

**Status:** Open · **Kind:** stated as open · **Reviewed extraction** 2026-10-13-250

For every fixed finite one-relator presentation G=⟨X | r⟩, does there exist a deterministic algorithm deciding whether an input word in X∪X⁻¹ is trivial in G in time polynomial in its length?

**Source.** Giles Gardam. *Encoding and detecting properties in finitely presented groups*. University of Oxford, 2017. [primary source](https://ora.ox.ac.uk/objects/uuid:0c8a7009-7e04-4f66-911b-298ad87061fb/files/m4392ba4e8cd5c325080c1cfdf63b2719) · [record](https://ora.ox.ac.uk/objects/uuid:0c8a7009-7e04-4f66-911b-298ad87061fb) Location: Gardam thesis, printed46 (physical60)

**Literature check.** Reviewed 2026-10-13: 2025 Linton–Nyberg-Brodda primary survey2501.18306§2.8.3 explicitly retains Question2.8.3. Known polynomial algorithms for Baumslag–Gersten groups do not settle all one-relator groups.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/gardam-2017.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://www.gilesgardam.com/) · [2](https://arxiv.org/pdf/1705.09348) · [3](https://arxiv.org/html/2501.18306v1) · [4](https://arxiv.org/abs/2303.05976) · [5](https://mathshistory.st-andrews.ac.uk/Groups/2013/slides/harlander.pdf) · [6](https://arxiv.org/abs/2508.20110) · [7](https://arxiv.org/abs/2412.05229) · [8](https://arxiv.org/html/2505.20960v1)

<a id="q4927"></a>

## Q4927. Profinite rigidity among finite-volume hyperbolic 3-manifolds

**Status:** Open · **Kind:** open problem (Question 5.1) · **Reviewed extraction** 2026-10-13-250

Let M,N be connected complete finite-volume hyperbolic3-manifolds. If π₁(M) and π₁(N) have the same finite quotient groups up to isomorphism, must π₁(M)≅π₁(N), and hence must M,N be isometric?

**Source.** Giles Gardam. *Encoding and detecting properties in finitely presented groups*. University of Oxford, 2017. [primary source](https://ora.ox.ac.uk/objects/uuid:0c8a7009-7e04-4f66-911b-298ad87061fb/files/m4392ba4e8cd5c325080c1cfdf63b2719) · [record](https://ora.ox.ac.uk/objects/uuid:0c8a7009-7e04-4f66-911b-298ad87061fb) Location: Gardam thesis, printed85 (physical99)

**Literature check.** Reviewed 2026-10-13: 2025 primary survey2508.20110 still studies the hyperbolic rigidity problem.2026 version of Xu2412.05229 gives specified links/knots/surgeries, not every finite-volume manifold; no general closure found.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/gardam-2017.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://www.gilesgardam.com/) · [2](https://arxiv.org/pdf/1705.09348) · [3](https://arxiv.org/html/2501.18306v1) · [4](https://arxiv.org/abs/2303.05976) · [5](https://mathshistory.st-andrews.ac.uk/Groups/2013/slides/harlander.pdf) · [6](https://arxiv.org/abs/2508.20110) · [7](https://arxiv.org/abs/2412.05229) · [8](https://arxiv.org/html/2505.20960v1)

<a id="q4928"></a>

## Q4928. Volume from maximal asymptotic homological torsion growth

**Status:** Open · **Kind:** conjecture (Conjecture 5.2) · **Reviewed extraction** 2026-10-13-250

For a connected complete finite-volume hyperbolic3-manifold M, put G=π₁(M). Is limsup_{[G:K]→∞} log|Tor H₁(K;ℤ)|/[G:K]=Vol(M)/(6π), where K ranges over all finite-index subgroups of G?

**Source.** Giles Gardam. *Encoding and detecting properties in finitely presented groups*. University of Oxford, 2017. [primary source](https://ora.ox.ac.uk/objects/uuid:0c8a7009-7e04-4f66-911b-298ad87061fb/files/m4392ba4e8cd5c325080c1cfdf63b2719) · [record](https://ora.ox.ac.uk/objects/uuid:0c8a7009-7e04-4f66-911b-298ad87061fb) Location: Gardam thesis, printed87 (physical101)

**Literature check.** Reviewed 2026-10-13: 2025 Ascari–Fruchter introduction retains exponential torsion-growth challenge; abundance of finite torsion summands is not rate control. Fresh volume/torsion review found no attainment of the asserted limsup for all hyperbolic3-manifolds. The known upper bound is recorded.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/gardam-2017.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://www.gilesgardam.com/) · [2](https://arxiv.org/pdf/1705.09348) · [3](https://arxiv.org/html/2501.18306v1) · [4](https://arxiv.org/abs/2303.05976) · [5](https://mathshistory.st-andrews.ac.uk/Groups/2013/slides/harlander.pdf) · [6](https://arxiv.org/abs/2508.20110) · [7](https://arxiv.org/abs/2412.05229) · [8](https://arxiv.org/html/2505.20960v1)

<a id="q4929"></a>

## Q4929. Hyperbolic 3-manifolds from index-marked abelianizations of covers

**Status:** Open · **Kind:** open problem (Question 5) · **Reviewed extraction** 2026-10-13-250

For a connected complete finite-volume hyperbolic3-manifold M define FIA(M)={([H₁(K;ℤ)],[π₁(M):K]):K≤π₁(M),[π₁(M):K]<∞}, where [H₁(K;ℤ)] is its abelian-group isomorphism class. If FIA(M)=FIA(N) for two such manifolds, must M,N be isometric?

**Source.** Giles Gardam. *Encoding and detecting properties in finitely presented groups*. University of Oxford, 2017. [primary source](https://ora.ox.ac.uk/objects/uuid:0c8a7009-7e04-4f66-911b-298ad87061fb/files/m4392ba4e8cd5c325080c1cfdf63b2719) · [record](https://ora.ox.ac.uk/objects/uuid:0c8a7009-7e04-4f66-911b-298ad87061fb) Location: Gardam thesis, printed88 (physical102)

**Literature check.** Reviewed 2026-10-13: Gardam primaryQuestion5.1′ remains stronger than the unresolved full profinite-rigidity question; modern hyperbolic profinite literature proves special examples using stronger invariants. No general FIA rigidity closure located.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/gardam-2017.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://www.gilesgardam.com/) · [2](https://arxiv.org/pdf/1705.09348) · [3](https://arxiv.org/html/2501.18306v1) · [4](https://arxiv.org/abs/2303.05976) · [5](https://mathshistory.st-andrews.ac.uk/Groups/2013/slides/harlander.pdf) · [6](https://arxiv.org/abs/2508.20110) · [7](https://arxiv.org/abs/2412.05229) · [8](https://arxiv.org/html/2505.20960v1)

<a id="q4933"></a>

## Q4933. Finite asymptotic dimension for all Artin groups

**Status:** Open · **Kind:** open problem (Question 1) · **Reviewed extraction** 2026-10-13-250

For a finite graph Γ whose edges have integer labels mₐᵦ≥2, let AΓ=⟨VΓ | alternating(a,b,mₐᵦ)=alternating(b,a,mₐᵦ) on every edge⟩. Give AΓ a word metric. Asdim X≤d means that for every R>0, X admits a uniformly bounded cover such that every R-ball meets at most d+1 sets. Does every AΓ have finite asymptotic dimension?

**Source.** Panagiotis Tselekidis. *Asymptotic dimension of one-relator groups and coxeter groups*. University of Oxford, 2023. [primary source](https://ora.ox.ac.uk/objects/uuid:d4e43aa9-50b2-4c98-a66a-b6ff285280b1/files/d4q77fr93f) · [record](https://ora.ox.ac.uk/objects/uuid:d4e43aa9-50b2-4c98-a66a-b6ff285280b1) Location: Question1; definitions§3.1 printed55

**Literature check.** Reviewed 2026-10-13: Tselekidis current arXiv2203.05746 gives special-case bounds and retains the general conjecture. Hagen–Martin–Sisto2109.04387 proves finite dimension for extra-large and large/hyperbolic type only. Fresh searches found no all-Artin closure.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/tselekidis-2023.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://arxiv.org/abs/2203.05746) · [2](https://arxiv.org/abs/2109.04387) · [3](https://msp.org/agt/2023/23-8/agt-v23-n8-p05-s.pdf)

<a id="q4934"></a>

## Q4934. Artin asymptotic dimension bounded by clique number

**Status:** Open · **Kind:** conjecture (Conjecture 3.0.1) · **Reviewed extraction** 2026-10-13-250

For a finite graph Γ whose edges have integer labels mₐᵦ≥2, let AΓ=⟨VΓ | alternating(a,b,mₐᵦ)=alternating(b,a,mₐᵦ) on every edge⟩. Give AΓ a word metric. Asdim X≤d means that for every R>0, X admits a uniformly bounded cover such that every R-ball meets at most d+1 sets. Writing Sim(Γ) for the number of vertices in a largest clique, must asdim AΓ≤Sim(Γ)?

**Source.** Panagiotis Tselekidis. *Asymptotic dimension of one-relator groups and coxeter groups*. University of Oxford, 2023. [primary source](https://ora.ox.ac.uk/objects/uuid:d4e43aa9-50b2-4c98-a66a-b6ff285280b1/files/d4q77fr93f) · [record](https://ora.ox.ac.uk/objects/uuid:d4e43aa9-50b2-4c98-a66a-b6ff285280b1) Location: Conjecture3.0.1; introductory Conjecture2 part1

**Literature check.** Reviewed 2026-10-13: Current primary paper2203.05746 explicitly conjectures this bound. Its Coxeter corollary proves only the Coxeter branch. No universal Artin closure located.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/tselekidis-2023.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://arxiv.org/abs/2203.05746) · [2](https://arxiv.org/abs/2109.04387) · [3](https://msp.org/agt/2023/23-8/agt-v23-n8-p05-s.pdf)

<a id="q4994"></a>

## Q4994. A locally finite transitive graph whose every automorphism fixes a vertex

**Status:** Open · **Kind:** open problem (Question0.2.13) · **Reviewed extraction** 2026-10-13-250

Does there exist a connected, locally finite, simple graph G with at least two vertices such that Aut(G) acts transitively on V(G) and every automorphism of G fixes at least one vertex? The fixed vertex may depend on the automorphism.

**Source.** Sébastien Martineau. *Percolation sur les groupes et modèles dirigés*. Agence Bibliographique de l'Enseignement Supérieur, 2014. [primary source](https://theses.hal.science/tel-01127079/document) · [record](https://doi.org/10.70675/0d9bae56z3585z495bzaa0cz148706f40749) Location: Question0.2.13, printed p.34 / held PDF p.43.

**Literature check.** Reviewed 2026-10-13: Current published2025 source and arXiv§4 retain strongly rotarily nice graph as openQ4.1; subgroup-action theorem does not answer full-Aut target.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/martineau-2015.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://gradmath.org/2025/martineau/) · [2](https://arxiv.org/pdf/1605.06054) · [3](https://math.bme.hu/~gabor/PGG.pdf) · [4](https://link.springer.com/article/10.1007/s00208-025-03116-7) · [5](https://ems.press/content/serial-article-files/51184) · [6](https://arxiv.org/html/2511.01851v1) · [7](https://arxiv.org/abs/2409.12283) · [8](https://arxiv.org/abs/1412.0150) · [9](https://alea.impa.br/articles/v14/14-15.pdf) · [10](https://www.cambridge.org/core/journals/journal-of-applied-probability/article/diffusion-limited-aggregation-in-the-layers-model/3A58EFC965F0DE2D46E3384F87FBCB10) · [11](https://arxiv.org/html/1803.09686v2) · [12](https://arxiv.org/abs/2310.10983) · [13](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Nonuniqueness-of-percolation-on-nonamenable-quasi-transitive-graphs-September-24-2026/paper.pdf)

<a id="q4995"></a>

## Q4995. Unimodular transitive graphs and Cayley geometry

**Status:** Open · **Kind:** stated as open (Unlabelled remark after Proposition0.2.11) · **Reviewed extraction** 2026-10-13-250

Is every connected, locally finite, vertex-transitive simple graph G quasi-isometric to a Cayley graph of a finitely generated group? Assume G is unimodular: for every Aut(G)-invariant f:V(G)×V(G)→[0,∞] and every o∈V(G), the sums ∑\_v f(o,v) and ∑\_v f(v,o) agree. A quasi-isometry is a map that distorts distances by uniform multiplicative and additive constants and whose image lies within a uniform distance of every vertex of the target.

**Source.** Sébastien Martineau. *Percolation sur les groupes et modèles dirigés*. Agence Bibliographique de l'Enseignement Supérieur, 2014. [primary source](https://theses.hal.science/tel-01127079/document) · [record](https://doi.org/10.70675/0d9bae56z3585z495bzaa0cz148706f40749) Location: Unlabelled remark after Proposition0.2.11, printed p.32 / held PDF p.41.

**Literature check.** Reviewed 2026-10-13: Primary current-accessible lecture notes explicitly askQ16.4; 2025 rational-cohomological/tree result covers only tree geometry.

**Review evidence.** [Source and scope review](../../reviews/statement-promotions/2026-10-13-250/agent-reviews/martineau-2015.json) · [Promotion review index](../../reviews/statement-promotions/README.md).

**Further links.** [1](https://gradmath.org/2025/martineau/) · [2](https://arxiv.org/pdf/1605.06054) · [3](https://math.bme.hu/~gabor/PGG.pdf) · [4](https://link.springer.com/article/10.1007/s00208-025-03116-7) · [5](https://ems.press/content/serial-article-files/51184) · [6](https://arxiv.org/html/2511.01851v1) · [7](https://arxiv.org/abs/2409.12283) · [8](https://arxiv.org/abs/1412.0150) · [9](https://alea.impa.br/articles/v14/14-15.pdf) · [10](https://www.cambridge.org/core/journals/journal-of-applied-probability/article/diffusion-limited-aggregation-in-the-layers-model/3A58EFC965F0DE2D46E3384F87FBCB10) · [11](https://arxiv.org/html/1803.09686v2) · [12](https://arxiv.org/abs/2310.10983) · [13](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Nonuniqueness-of-percolation-on-nonamenable-quasi-transitive-graphs-September-24-2026/paper.pdf)
