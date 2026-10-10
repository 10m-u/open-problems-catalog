# Theory of Computation & Algorithms (part 2 of 2)

[Subject overview](theory-of-computation-algorithms.md) · Parts: [1](theory-of-computation-algorithms-part-1.md) · [2](theory-of-computation-algorithms-part-2.md)

<a id="q3080"></a>

## Q3080. Three additive clocks

**Status:** Open · **Kind:** open problem (Problem 24.6) · **Collection** 31

Is language emptiness decidable for these three-clock timed automata?

**Context.** Origin for question 3080: Older three-clock problem restated on an original contributor page. Setup for question 3080: Finite-state timed automata have three nonnegative real clocks, increasing together at unit rate and reset only to zero. Guards permit ordinary rational clock comparisons and additive comparisons x+y ⋈ c, with ⋈∈{<,≤,=,≥,>} and rational c. Acceptance is finite-run reachability of a final state.

**Source.** R. Govind. *Emptiness-checking for 3-clock Timed Automata with additive constraints (Autobóz Problem 24.6)*. 2024. [primary source](https://automata.exchange/24.06-emptiness-checking-for-3-clock-timed-automata-with-additive-constraints/) Location: Problem 24.6; Bouyer tutorial §5.3.3.

**Literature check.** Status for question 3080, checked 8 October 2026: Problem page and Bouyer’s exact-model exposition checked; no later matching resolution located.

**Further links.** [1](https://lsv.ens-paris-saclay.fr/~bouyer/files/bouyer-tutorial.pdf)


<a id="q3082"></a>

## Q3082. Maximal order type of graph minors

**Status:** Open · **Kind:** open problem · **Collection** 31

What is the exact ordinal o(G)?

**Context.** Origin for question 3082: Older ordinal-analysis frontier explicitly proposed in the thesis conclusion. Setup for question 3082: Let G be the isomorphism classes of finite undirected graphs, ordered by the graph-minor relation. Its maximal order type o(G) is the supremum of order types of well-order linear extensions of this partial order.

**Source.** Isa Vialard. *Measuring well quasi-orders and complexity of verification*. 2024. Advisor(s): Philippe Schnoebelen. [primary source](https://isavialard.github.io/home/mwqo.pdf) Location: Conclusion, printed p. 110, paragraph beginning “Adding operations”.

**Literature check.** Status for question 3082, checked 8 October 2026: Thesis and subsequent author bibliography checked; no matching computation located.


<a id="q3083"></a>

## Q3083. Minimizing visible pebbles

**Status:** Open · **Kind:** open problem · **Collection** 31

Given a pebble transducer computing f and k≥2, is it decidable whether a k-pebble transducer computes f?

**Context.** Origin for questions 3083, 3084, 3085: Explicit thesis targets. Setup for questions 3083, 3084, 3085: Machines deterministically compute total finite-word functions. A k-pebble transducer nests two-way transducers k levels deep: calls mark their input position; outputs concatenate. All marks are visible. Last-pebble machines see only the most recent mark. Marble calls instead receive the prefix strictly before the calling position. Recursive last-pebble machines allow unbounded call depth.

**Source.** Gaëtan Douéneau-Tabot. *Optimization of string transducers*. 2023. Advisor(s): Olivier Carton, Emmanuel Filiot. [primary source](https://gdoueneau.github.io/pages/DOUENEAU-TABOT_Optimization-transducers_v2.pdf) Location: Open question 1.52, p. 66.

**Literature check.** Status for questions 3083, 3084, 3085, checked 8 October 2026: January 2026 follow-up proves only polyregularity for polynomial-growth recursive last-pebble machines, not last-pebble definability.

**Further links.** [1](https://arxiv.org/abs/2501.10270) · [2](https://gdoueneau.github.io/pages/phd.html)


<a id="q3084"></a>

## Q3084. Last-pebble to marble membership

**Status:** Open · **Kind:** open problem · **Collection** 31

Given a last-pebble transducer computing f, is it decidable whether a marble transducer computes f?

**Context.** Origin for questions 3083, 3084, 3085: Explicit thesis targets. Setup for questions 3083, 3084, 3085: Machines deterministically compute total finite-word functions. A k-pebble transducer nests two-way transducers k levels deep: calls mark their input position; outputs concatenate. All marks are visible. Last-pebble machines see only the most recent mark. Marble calls instead receive the prefix strictly before the calling position. Recursive last-pebble machines allow unbounded call depth.

**Source.** Gaëtan Douéneau-Tabot. *Optimization of string transducers*. 2023. Advisor(s): Olivier Carton, Emmanuel Filiot. [primary source](https://gdoueneau.github.io/pages/DOUENEAU-TABOT_Optimization-transducers_v2.pdf) Location: Open question 4.20, p. 106.

**Literature check.** Status for questions 3083, 3084, 3085, checked 8 October 2026: January 2026 follow-up proves only polyregularity for polynomial-growth recursive last-pebble machines, not last-pebble definability.

**Further links.** [1](https://arxiv.org/abs/2501.10270) · [2](https://gdoueneau.github.io/pages/phd.html)


<a id="q3085"></a>

## Q3085. Eliminating unbounded last-pebble recursion

**Status:** Open · **Kind:** conjecture (Conjecture 4.56) · **Collection** 31

Can every polynomial-output-growth recursive last-pebble transducer effectively be converted to an equivalent bounded-depth last-pebble transducer?

**Context.** Origin for questions 3083, 3084, 3085: Explicit thesis targets. Setup for questions 3083, 3084, 3085: Machines deterministically compute total finite-word functions. A k-pebble transducer nests two-way transducers k levels deep: calls mark their input position; outputs concatenate. All marks are visible. Last-pebble machines see only the most recent mark. Marble calls instead receive the prefix strictly before the calling position. Recursive last-pebble machines allow unbounded call depth.

**Source.** Gaëtan Douéneau-Tabot. *Optimization of string transducers*. 2023. Advisor(s): Olivier Carton, Emmanuel Filiot. [primary source](https://gdoueneau.github.io/pages/DOUENEAU-TABOT_Optimization-transducers_v2.pdf) Location: Conjecture 4.56, p. 120.

**Literature check.** Status for questions 3083, 3084, 3085, checked 8 October 2026: January 2026 follow-up proves only polyregularity for polynomial-growth recursive last-pebble machines, not last-pebble definability.

**Further links.** [1](https://arxiv.org/abs/2501.10270) · [2](https://gdoueneau.github.io/pages/phd.html)


<a id="q3086"></a>

## Q3086. Polynomial ambiguity in tree height

**Status:** Open · **Kind:** open problem · **Collection** 31

Is it decidable whether the number of accepting runs of a given unweighted tree automaton is bounded by a polynomial in the input tree’s height?

**Context.** Origin for questions 3086, 3087: Explicit open questions in §6.1. Setup for questions 3086, 3087: Trees are finite ordered ranked trees. For finite bottom-up tree automata, ambiguity counts runs with final root state. An N-weighted automaton assigns nonnegative integer transition and final weights; its value sums products of these weights over runs. Set g_A(n)=max{|A(t)|:|t|≤n}, with empty maximum zero and |t| counting nodes.

**Source.** Gallot; Lhote; Nguyễn. *The structure of polynomial growth for tree automata/transducers and MSO set queries*. 2026. [primary source](https://arxiv.org/abs/2501.10270) Location: §6.1, “Ambiguity vs height”, before Theorem 88.

**Literature check.** Status for questions 3086, 3087, checked 8 October 2026: TheoretiCS accepted 29 September; its listing links to v4, which retains these targets. Auxiliary use: Corollary 13 gives only a weaker consequence of Douéneau-Tabot’s recursion conjecture.


<a id="q3087"></a>

## Q3087. An exponential rate for weighted trees

**Status:** Open · **Kind:** open problem · **Collection** 31

If g_A(n)=2^{Θ(n)} for an N-weighted tree automaton A, must lim_{n→∞} g_A(n)^{1/n} exist?

**Context.** Origin for questions 3086, 3087: Explicit open questions in §6.1. Setup for questions 3086, 3087: Trees are finite ordered ranked trees. For finite bottom-up tree automata, ambiguity counts runs with final root state. An N-weighted automaton assigns nonnegative integer transition and final weights; its value sums products of these weights over runs. Set g_A(n)=max{|A(t)|:|t|≤n}, with empty maximum zero and |t| counting nodes.

**Source.** Gallot; Lhote; Nguyễn. *The structure of polynomial growth for tree automata/transducers and MSO set queries*. 2026. [primary source](https://arxiv.org/abs/2501.10270) Location: §6.1, question immediately before Theorem 90.

**Literature check.** Status for questions 3086, 3087, checked 8 October 2026: TheoretiCS accepted 29 September; its listing links to v4, which retains these targets. Auxiliary use: Corollary 13 gives only a weaker consequence of Douéneau-Tabot’s recursion conjecture.


<a id="q3088"></a>

## Q3088. Arena-independent constrained SPE memory

**Status:** Open · **Kind:** open problem · **Collection** 31

Does f:{1,2,…}→{1,2,…} exist such that, for every n≥1, every n-player game and every W⊆{1,…,n}, existence of an SPE in which each player in W wins implies existence of such an SPE with each player using at most f(n) memory states?

**Context.** Origin for question 3088: Thesis frontier, explicitly asked on the author’s 2025 problem page. Setup for question 3088: Games are turn-based, deterministic, perfect-information, with finitely many players, countably many vertices and actions, an initial vertex and no deadlocks. Each player wins by visiting their target set. Strategies are pure. An SPE is a Nash equilibrium after every feasible history from the initial vertex, retaining already achieved targets. Finite-memory strategies use finitely many modes; action choice depends on the current vertex and mode, and deterministic mode updates depend on the vertex, mode and observed action.

**Source.** James C. A. Main. *The Many Faces of Strategy Complexity*. 2025. Advisor(s): Mickaël Randour. [primary source](https://orbi.umons.ac.be/bitstream/20.500.12907/53243/1/main.pdf) Location: §22.2, pp. 393–394; problem-page item 3.

**Literature check.** Status for question 3088, checked 8 October 2026: 2026 follow-ons prove finite-memory Nash equilibria or randomised memoryless SPEs on finite arenas; neither settles the uniform pure-SPE memory bound.

**Further links.** [1](https://automata.exchange/25.26-memory-requirements-of-subgame-perfect-equilibria-in-reachability-games/) · [2](https://orbi.umons.ac.be/handle/20.500.12907/53243)


<a id="q3089"></a>

## Q3089. Composition at exponential growth

**Status:** Open · **Kind:** open problem · **Collection** 31

If a finite composition of expregular functions has exponential growth, must the composite function be expregular?

**Context.** Origin for question 3089: Explicit question in the final paper’s discussion. Setup for question 3089: A string-to-string MSO set interpretation chooses output positions among colourings of input positions by a fixed finite set F. MSO formulas over the input order and letter predicates define the chosen colourings, their total order and a partition into output letters. The resulting total finite-word functions are called expregular. Exponential growth means output length at most 2^{O(n)}, not 2^{n^{O(1)}}.

**Source.** Thomas Colcombet; Nathan Lhote; Pierre Ohlmann. *Expregular Functions*. 2026. [primary source](https://doi.org/10.4230/LIPIcs.ICALP.2026.176) Location: §4 Discussion, growth paragraph; model §2.1 and Remark 1.4.

**Literature check.** Status for question 3089, checked 8 October 2026: ICALP final and May 2026 v3 checked; no later matching resolution located.

**Further links.** [1](https://arxiv.org/abs/2602.21019)


<a id="q3122"></a>

## Q3122. Polynomial Khovanov computation at fixed braid index

**Status:** Open · **Kind:** conjecture (Conjecture 1.1) · **Collection** 32

For every fixed number k of strands, is there an algorithm computing integral Kh of the braid closure in time polynomial in the input word length?

**Context.** Doctoral context for question 3122: Tuomas Kelomäki. Algorithms and computations in Khovanov homology. PhD, 2026, Aalto University. Advisors: Kalle Kytölä; Alexander Engström; Gregory Arone. Origin for question 3122: Przytycki–Silvero’s conjecture, restated in Kelomäki–Schütz and the dissertation. Setup for question 3122: Kh is unreduced bigraded Khovanov homology. Input is a braid word in Artin generators, with length its number of letters. Homology is output by graded ranks and torsion data, using binary integer encoding. T(n,m) closes (σ₁⋯σ\_{n−1})^m.

**Source.** Tuomas Kelomäki and Dirk Schütz. *On computational complexity of Khovanov homology*. 2026. [primary source](https://arxiv.org/pdf/2601.02119v1) Location: Conjecture 1.1, p. 1; Theorem 1.3 and discussion pp. 2–3.

**Literature check.** Status for question 3122, checked 8 October 2026: The January 2026 paper solves 3-braids and bounded extremal homological ranges; arbitrary fixed braid index remains open.

**Further links.** [1](https://research.aalto.fi/en/publications/algorithms-and-computations-in-khovanov-homology/)


<a id="q3177"></a>

## Q3177. Semigroup frontier for guarded data logic

**Status:** Open · **Kind:** open problem · **Collection** 32

Characterize the finite semigroups S for which finite satisfiability of this logic with guards recognized by S is decidable.

**Context.** Origin for question 3177: Explicit final-conclusion research target. Setup for question 3177: Finite data words have letters in finite Σ and values in an infinite equality-only domain. A sentence existentially quantifies n monadic predicates, then uses two-variable FO with letter predicates, order, successor, data equality and same-data successor. Guards read Γ=Σ×{0,1}ⁿ, with bits recording those predicates: L̃(x,y) requires x&lt;y, equal data, and the Γ-word strictly between x,y in L. All guards share one unit-reflecting h:Γ\*→S¹, h⁻¹(1)={ε}, with L=h⁻¹(P). S¹=S for monoids, otherwise adjoin an identity.

**Source.** Shibashis Guha; Amaldev Manuel; S. P. Rishal. *Set Automata and Limits of Decidability of Two-Variable Logic on Data Words*. 2026. [primary source](https://doi.org/10.4230/LIPIcs.ICALP.2026.181) Location: §6; recognition conventions§ 1; full-version§ 6.

**Literature check.** Status for question 3177, checked 8 October 2026: Final ICALP text and current full version checked; no later classification located.

**Further links.** [1](https://arxiv.org/abs/2605.09077)


<a id="q3257"></a>

## Q3257. Approximate graph homomorphism hardness

**Status:** Open · **Kind:** open problem · **Collection** 33

For fixed finite nonbipartite loopless undirected G,H admitting a homomorphism G→H, is it NP-hard to distinguish input graphs X with X→G from those with no homomorphism X→H? Homomorphisms map adjacent vertices to adjacent vertices.

**Context.** Doctoral context for question 3257: Gianluca Tasinato. PhD, 2025, Institute of Science and Technology Austria. Advisors: Uli Wagner. Origin for question 3257: Brakensiek–Guruswami’s older approximate-homomorphism conjecture, restated in the thesis.

**Source.** Gianluca Tasinato. *Topological Methods in Discrete Geometry and Theoretical Computer Science*. Institute of Science and Technology Austria, 2025. Advisor(s): Uli Wagner. [primary source](https://doi.org/10.15479/AT-ISTA-20339) Location: §2.1, p. 4.

**Literature check.** Status for question 3257, checked 8 October 2026: The April 2026 primary paper retains the general graph target.

**Further links.** [1](https://research-explorer.ista.ac.at/download/20339/20345/2025_Tasinato_Gianluca_Thesis.pdf) · [2](https://arxiv.org/abs/2604.27336v1) · [3](https://doi.org/10.4230/LIPIcs.ICALP.2026.184) · [4](https://arxiv.org/abs/2605.09815) · [5](https://research-explorer.ista.ac.at/record/20339) · [6](https://gtasinato.github.io/about/)


<a id="q3264"></a>

## Q3264. Minimum-color cycle complexity

**Status:** Open · **Kind:** open problem (Problem 8) · **Collection** 33

Is there a polynomial-time algorithm finding a minimum-cost cycle, or reporting that no cycle exists?

**Context.** Origin for question 3264: Authors’ Hedge Minimum Cycle question, reiterated on Korhonen’s current problem page. Setup for question 3264: The input is a finite undirected edge-colored multigraph; parallel edges are allowed and form two-edge cycles. A cycle’s cost is its number of distinct edge colors.

**Source.** Fedor V. Fomin; Petr A. Golovach; Tuukka Korhonen; Daniel Lokshtanov; Giannos Stamoulis. *Shortest Cycles with Monotone Submodular Costs*. 2023. [primary source](https://doi.org/10.1145/3626824) Location: §6, p. 2:15; Korhonen Problem 8.

**Literature check.** Status for question 3264, checked 8 October 2026: 8 October: final ACM text and September16 author page retain the question.

**Further links.** [1](https://fedorvf.github.io/articles/2024/2024g.pdf) · [2](https://tuukkakorhonen.com/problems.html)


<a id="q3265"></a>

## Q3265. FPT path-width from a connectivity oracle

**Status:** Open · **Kind:** open problem (Problem 7.1) · **Collection** 33

Given value-oracle access to f and integer k≥0, can one decide whether its path-width is at most k in time g(k)n^{O(1)} for some computable g, counting oracle evaluation as one operation?

**Context.** Origin for question 3265: Authors’ Problem 7.1; their branch-width theorem does not solve path-width. Setup for question 3265: A connectivity function f:2^V→Z is symmetric, submodular, and f(∅)=0. Its path-width is min_{v₁…v_n}max_i f({v₁,…,v_i}), over vertex orderings.

**Source.** Tuukka Korhonen; Sang-il Oum. *Branch-width of connectivity functions is fixed-parameter tractable*. 2026. [primary source](https://arxiv.org/abs/2601.04756v2) Location: Problem 7.1, p. 11.

**Literature check.** Status for question 3265, checked 8 October 2026: 8 October: corrected February v2 remains current; no later resolution located.


<a id="q3276"></a>

## Q3276. Equivalence under subsequence constraints

**Status:** Open · **Kind:** open problem · **Collection** 33

Is equality of these languages decidable when r(u,v) means that u is a subsequence of v?

**Context.** Origin for questions 3276, 3277, 3278: Explicit decidability conjectures following Corollary4. Setup for questions 3276, 3277, 3278: Fix a finite alphabet Σ with |Σ|≥2. An input is a nonempty finite pattern over Σ and variables, each variable occurring once, with finitely many ordered binary constraints r(x,y). Its non-erasing language consists of all substitutions fixing Σ, assigning each variable a nonempty word, and satisfying every constraint. Two inputs use the same relation r.

**Source.** Klaus Jansen; Dirk Nowotka; Lis Pirotton; Corinna Wambsganz; Max Wiedenhöft. *An Analysis of Decision Problems for Relational Pattern Languages under Various Constraints*. 2026. [primary source](https://arxiv.org/abs/2512.07476v4) Location: §3.1, after Corollary4, p. 6.

**Literature check.** Status for questions 3276, 3277, 3278, checked 8 October 2026: July full version and October proceedings version compared; no later resolution located.

**Further links.** [1](https://arxiv.org/abs/2610.07119v1) · [2](https://doi.org/10.4204/EPTCS.451.13)


<a id="q3277"></a>

## Q3277. Equivalence under reversal constraints

**Status:** Open · **Kind:** open problem · **Collection** 33

Is equality decidable when r(u,v) means u=v^R?

**Context.** Origin for questions 3276, 3277, 3278: Explicit decidability conjectures following Corollary4. Setup for questions 3276, 3277, 3278: Fix a finite alphabet Σ with |Σ|≥2. An input is a nonempty finite pattern over Σ and variables, each variable occurring once, with finitely many ordered binary constraints r(x,y). Its non-erasing language consists of all substitutions fixing Σ, assigning each variable a nonempty word, and satisfying every constraint. Two inputs use the same relation r.

**Source.** Klaus Jansen; Dirk Nowotka; Lis Pirotton; Corinna Wambsganz; Max Wiedenhöft. *An Analysis of Decision Problems for Relational Pattern Languages under Various Constraints*. 2026. [primary source](https://arxiv.org/abs/2512.07476v4) Location: §3.1, after Corollary4, p. 6.

**Literature check.** Status for questions 3276, 3277, 3278, checked 8 October 2026: July full version and October proceedings version compared; no later resolution located.

**Further links.** [1](https://arxiv.org/abs/2610.07119v1) · [2](https://doi.org/10.4204/EPTCS.451.13)


<a id="q3278"></a>

## Q3278. Equivalence under word-power constraints

**Status:** Open · **Kind:** open problem · **Collection** 33

Is equality decidable when r(u,v) means u∈{v}\*?

**Context.** Origin for questions 3276, 3277, 3278: Explicit decidability conjectures following Corollary4. Setup for questions 3276, 3277, 3278: Fix a finite alphabet Σ with |Σ|≥2. An input is a nonempty finite pattern over Σ and variables, each variable occurring once, with finitely many ordered binary constraints r(x,y). Its non-erasing language consists of all substitutions fixing Σ, assigning each variable a nonempty word, and satisfying every constraint. Two inputs use the same relation r.

**Source.** Klaus Jansen; Dirk Nowotka; Lis Pirotton; Corinna Wambsganz; Max Wiedenhöft. *An Analysis of Decision Problems for Relational Pattern Languages under Various Constraints*. 2026. [primary source](https://arxiv.org/abs/2512.07476v4) Location: §3.1, after Corollary4, p. 6.

**Literature check.** Status for questions 3276, 3277, 3278, checked 8 October 2026: July full version and October proceedings version compared; no later resolution located.

**Further links.** [1](https://arxiv.org/abs/2610.07119v1) · [2](https://doi.org/10.4204/EPTCS.451.13)


<a id="q3281"></a>

## Q3281. Verification with two ReLU neurons per layer

**Status:** Open · **Kind:** open problem · **Collection** 33

What is the computational complexity of deciding whether some x∈[0,1] satisfies the output constraint? In particular, is this width-two problem NP-hard?

**Context.** Origin for question 3281: Explicit width-two question in §6. Setup for question 3281: Input networks N:R→R are finite compositions A_out∘R_L∘⋯∘R_1∘A_in. Each hidden layer is R_ℓ(z)=ReLU(W_ℓz+b_ℓ) on R², applied coordinatewise, with ReLU(t)=max(t,0). All affine maps have binary-encoded rational coefficients. Depth is unbounded and explicitly represented. The verification input also specifies one rational affine equality or inequality on N(x).

**Source.** Olivier Bournez; Johanne Cohen; Laura Cohen; Adrian Wurm. *Fractal Gadgets for Neural Networks: The Complexity of the Narrow Regime*. 2026. [primary source](https://arxiv.org/abs/2610.06092v1) Location: §6, pp. 29–30; Definition 2.1, p. 4.

**Literature check.** Status for question 3281, checked 8 October 2026: October v1 retains the width-two case; no later resolution located.


<a id="q3282"></a>

## Q3282. Global identifiability with independent HMM entries

**Status:** Open · **Kind:** open problem · **Collection** 33

Determine the complexity of deciding whether every M′∈U(M\*,μ) with M′≡M\* satisfies M′=M\*. Is it ∀R-complete?

**Context.** Origin for questions 3282, 3283: Explicit complexity questions in the new primary paper. Setup for questions 3282, 3283: An n-state HMM M=(π,A,B) has an initial probability vector and stochastic transition/emission matrices over a finite alphabet of size≥2, using emit-then-transition. M≡M′ means equal probabilities for every finite output word. Input target M\* has binary-encoded rational entries. A mask fixes selected entries to M\* and leaves all other entries independent real parameters, subject only to stochasticity; call this family U(M\*,μ). State labels are fixed.

**Source.** Markel Zubia; Nils Jansen. *On the Computational Complexity of Hidden Markov Model Identification*. 2026. [primary source](https://arxiv.org/abs/2610.09104v1) Location: §8, p. 15; Definitions 4 and16; Theorem 17.

**Literature check.** Status for questions 3282, 3283, checked 8 October 2026: Latest v1 retains these cases; no later resolution located.

**Further links.** [1](https://ai-fm.org/people/) · [2](https://nilsjansen.org/assets/pdf/cv-jansen.pdf)


<a id="q3283"></a>

## Q3283. Local identifiability of a fixed HMM

**Status:** Open · **Kind:** open problem (Problem 33) · **Collection** 33

Determine the complexity of deciding whether some δ>0 makes M\* the unique n-state HMM M′ with M′≡M\* and ||M′−M\*||₂≤δ.

**Context.** Origin for questions 3282, 3283: Explicit complexity questions in the new primary paper. Setup for questions 3282, 3283: An n-state HMM M=(π,A,B) has an initial probability vector and stochastic transition/emission matrices over a finite alphabet of size≥2, using emit-then-transition. M≡M′ means equal probabilities for every finite output word. Input target M\* has binary-encoded rational entries. A mask fixes selected entries to M\* and leaves all other entries independent real parameters, subject only to stochasticity; call this family U(M\*,μ). State labels are fixed.

**Source.** Markel Zubia; Nils Jansen. *On the Computational Complexity of Hidden Markov Model Identification*. 2026. [primary source](https://arxiv.org/abs/2610.09104v1) Location: §8, p. 15; Problem 33 and Theorem 35, p. 13.

**Literature check.** Status for questions 3282, 3283, checked 8 October 2026: Latest v1 retains these cases; no later resolution located.

**Further links.** [1](https://ai-fm.org/people/) · [2](https://nilsjansen.org/assets/pdf/cv-jansen.pdf)


<a id="q3372"></a>

## Q3372. Integer feasibility in atom-dimension two

**Status:** Open · **Kind:** open problem · **Collection** 34

Is existence of a finite integer solution decidable for all such systems?

**Context.** Origin for question 3372: Thesis question; earlier joint linear-programming work asks the same dimension boundary. Setup for question 3372: Let A be countably infinite equality atoms, acted on by all permutations. Input integer linear inequalities Mx≥b have hereditarily orbit-finite row and variable sets and finitely supported coefficients, specified by finite orbit presentations. Relative to the input support S, every row and variable index has support of size at most two outside S. A finite solution x has only finitely many nonzero integer coordinates; all matrix products use finite sums of nonzero terms.

**Source.** Arka Ghosh. *Linear Algebra in Orbit-finite Dimension*. 2025. Advisor(s): Sławomir Lasota; assistant supervisor Piotr Hofman. [primary source](https://www.mimuw.edu.pl/media/uploads/doctorates/thesis-arka-ghosh.pdf) Location: Remark 5.13, p. 93.

**Literature check.** Status for question 3372, checked 8 October 2026: 2025 thesis retains the dimension-two boundary; no later resolution found.

**Further links.** [1](https://www.mimuw.edu.pl/en/doctorates/arka-ghosh/)


<a id="q3377"></a>

## Q3377. Recognizing fully universal representations

**Status:** Open · **Kind:** open problem (Question 7.1) · **Collection** 34

Is existence of a fully universal representation decidable from A?

**Context.** Doctoral context for questions 3377, 3378, 3379: Simon Knäuer. Constraint Network Satisfaction for Finite Relation Algebras. PhD, 2023, Technische Universität Dresden. Advisors: Manuel Bodirsky. Origin for questions 3377, 3378, 3379: Questions in the expanded joint paper, reached through Knäuer’s thesis. Setup for questions 3377, 3378, 3379: Let A be a finite relation algebra given by operation tables. Representations are injective and preserve its Boolean operations, identity, converse and composition; the unit may be an equivalence relation rather than a full square. An atomic network f:V²→Atoms(A) is consistent if f(x,x)≤Id, f(x,y)=f(y,x)˘ and f(x,z)≤f(x,y)∘f(y,z). A representation is fully universal if every finite consistent atomic network has a satisfying vertex map. NSP(A) asks whether an arbitrary finite A-labelled network has such a map into some representation.

**Source.** Manuel Bodirsky; Moritz Jahn; Simon Knäuer; Matěj Konečný; Paul Winkler. *Network Satisfaction over Four-Atom Relation Algebras: Complexity and Representations*. 2026. [primary source](https://arxiv.org/abs/2507.09324v3) Location: Question 7.1, p. 68.

**Literature check.** Status for questions 3377, 3378, 3379, checked 8 October 2026: October 2026 v3 retains all three targets; no later resolution found.

**Further links.** [1](https://tud.qucosa.de/en/landing-page/https%3A%2F%2Ftud.qucosa.de%2Fapi%2Fqucosa%253A85503%2Fmets/)


<a id="q3378"></a>

## Q3378. Smallest network problem outside NP

**Status:** Open · **Kind:** open problem (Question 7.3) · **Collection** 34

What is the least size of A for which NSP(A) is not in NP?

**Context.** Doctoral context for questions 3377, 3378, 3379: Simon Knäuer. Constraint Network Satisfaction for Finite Relation Algebras. PhD, 2023, Technische Universität Dresden. Advisors: Manuel Bodirsky. Origin for questions 3377, 3378, 3379: Questions in the expanded joint paper, reached through Knäuer’s thesis. Setup for questions 3377, 3378, 3379: Let A be a finite relation algebra given by operation tables. Representations are injective and preserve its Boolean operations, identity, converse and composition; the unit may be an equivalence relation rather than a full square. An atomic network f:V²→Atoms(A) is consistent if f(x,x)≤Id, f(x,y)=f(y,x)˘ and f(x,z)≤f(x,y)∘f(y,z). A representation is fully universal if every finite consistent atomic network has a satisfying vertex map. NSP(A) asks whether an arbitrary finite A-labelled network has such a map into some representation.

**Source.** Manuel Bodirsky; Moritz Jahn; Simon Knäuer; Matěj Konečný; Paul Winkler. *Network Satisfaction over Four-Atom Relation Algebras: Complexity and Representations*. 2026. [primary source](https://arxiv.org/abs/2507.09324v3) Location: Question 7.3, p. 68.

**Literature check.** Status for questions 3377, 3378, 3379, checked 8 October 2026: October 2026 v3 retains all three targets; no later resolution found.

**Further links.** [1](https://tud.qucosa.de/en/landing-page/https%3A%2F%2Ftud.qucosa.de%2Fapi%2Fqucosa%253A85503%2Fmets/)


<a id="q3379"></a>

## Q3379. Atomic-or-unconstrained network classification

**Status:** Open · **Kind:** open problem (Problem 7.4) · **Collection** 34

For every A with at most four atoms, classify the complexity of NSP(A) restricted to networks whose labels are atoms or the Boolean top element 1.

**Context.** Doctoral context for questions 3377, 3378, 3379: Simon Knäuer. Constraint Network Satisfaction for Finite Relation Algebras. PhD, 2023, Technische Universität Dresden. Advisors: Manuel Bodirsky. Origin for questions 3377, 3378, 3379: Questions in the expanded joint paper, reached through Knäuer’s thesis. Setup for questions 3377, 3378, 3379: Let A be a finite relation algebra given by operation tables. Representations are injective and preserve its Boolean operations, identity, converse and composition; the unit may be an equivalence relation rather than a full square. An atomic network f:V²→Atoms(A) is consistent if f(x,x)≤Id, f(x,y)=f(y,x)˘ and f(x,z)≤f(x,y)∘f(y,z). A representation is fully universal if every finite consistent atomic network has a satisfying vertex map. NSP(A) asks whether an arbitrary finite A-labelled network has such a map into some representation.

**Source.** Manuel Bodirsky; Moritz Jahn; Simon Knäuer; Matěj Konečný; Paul Winkler. *Network Satisfaction over Four-Atom Relation Algebras: Complexity and Representations*. 2026. [primary source](https://arxiv.org/abs/2507.09324v3) Location: Problem 7.4, p. 68.

**Literature check.** Status for questions 3377, 3378, 3379, checked 8 October 2026: October 2026 v3 retains all three targets; no later resolution found.

**Further links.** [1](https://tud.qucosa.de/en/landing-page/https%3A%2F%2Ftud.qucosa.de%2Fapi%2Fqucosa%253A85503%2Fmets/)


<a id="q3386"></a>

## Q3386. Sampling hardness against shallow parity circuits

**Status:** Open · **Kind:** open problem (Question 1) · **Collection** 34

Is there such an explicit family (D_n) with distance 1−o(1) from the output distribution of every AC⁰[⊕] sampler family?

**Context.** Origin for question 3386: Explicit question in the final primary article, reached through the Goodman sampling branch. Setup for question 3386: Explicit distributions D_n on {0,1}^n must be samplable by a uniform randomized algorithm in time polynomial in n. AC⁰[⊕] samplers are nonuniform constant-depth circuits with unbounded-fan-in AND, OR and parity gates and NOT gates, n output bits, polynomially many gates, and arbitrarily many independent uniform random input bits. Distance is total variation.

**Source.** Farzan Byramji; Daniel M. Kane; Jackson Morris; Anthony Ostuni. *Hard-To-Sample Distributions from Robust Extractors*. 2026. [primary source](https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2026.37) Location: §5 Question 1, p. 37:18.

**Literature check.** Status for question 3386, checked 8 October 2026: Final RANDOM 2026 retains this target; no later matching resolution found.

**Further links.** [1](https://aostuni.github.io/)


<a id="q3387"></a>

## Q3387. Pseudo-Siggers tractability for normal relation algebras

**Status:** Open · **Kind:** open problem (Problem 4.53) · **Collection** 34

If Pol(B) contains s:B⁶→B and unary e₁,e₂ with e₁(s(x,x,y,y,z,z))=e₂(s(y,z,x,z,x,y)) for all x,y,z∈B, must NSP(A) be in P?

**Context.** Doctoral context for question 3387: see question 3377. Origin for question 3387: Thesis question repeating the general algebraic tractability conjecture in the normal-representation setting. Setup for question 3387: Let A be a finite relation algebra and B a countable normal representation: it is square, homogeneous, and realizes every consistent atomic A-network. Here consistency is f(x,x)≤Id, f(x,y)=f(y,x)˘ and f(x,z)≤f(x,y)∘f(y,z). Pol(B) consists of operations preserving every represented relation coordinatewise. NSP(A) asks whether a finite A-labelled network has a satisfying map to a representation.

**Source.** Simon Knäuer. *Constraint Network Satisfaction for Finite Relation Algebras*. 2023. Advisor(s): Manuel Bodirsky. [primary source](https://tud.qucosa.de/en/api/qucosa%3A85503/attachment/ATT-0/) Location: Problem 4.53, p. 85.

**Literature check.** Status for question 3387, checked 8 October 2026: No later resolution located.

**Further links.** [1](https://tud.qucosa.de/en/landing-page/https%3A%2F%2Ftud.qucosa.de%2Fapi%2Fqucosa%253A85503%2Fmets/)


<a id="q3388"></a>

## Q3388. Explicit local-source dispersers below square-root entropy

**Status:** Open · **Kind:** open problem · **Collection** 34

Do there exist an explicit family (D_n) and k(n)=o(√n) such that, for all sufficiently large n, D_n disperses every 2-local n-bit source with min-entropy at least k(n)?

**Context.** Origin for question 3388: Thesis question sharpening the earlier joint-paper program for local sources. Setup for question 3388: A 2-local source on {0,1}^n has the form g(U_m), for arbitrary m, where U_m is uniform and each output coordinate of g depends on at most two input bits. Its min-entropy is H∞(X)=−log₂ max_x Pr[X=x]. A disperser D_n:{0,1}^n→{0,1} must take both values on the support of every allowed source. Explicit means one deterministic algorithm evaluates D_n(x) in time polynomial in n.

**Source.** Jesse Goodman. *Seedless Extractors*. 2023. Advisor(s): Eshan Chattopadhyay. [primary source](https://jpmgoodman.com/thesis.pdf) Location: §8.7, p. 184.

**Literature check.** Status for question 3388, checked 8 October 2026: Thesis target survives later non-explicit results; no matching resolution found.

**Further links.** [1](https://jpmgoodman.com/)


<a id="q3433"></a>

## Q3433. Deterministic mean-payoff decomposition

**Status:** Open · **Kind:** open problem · **Collection** 35

For each of the two Val choices, must every deterministic Val-automaton A admit deterministic Val-automata B,C, respectively safe and live, with A(w)=min{B(w),C(w)} for all w?

**Context.** Origin: Thesis p. 105 and published joint-paper question after Theorem 9.5. Setup: Over finite nonempty Σ, a total deterministic finite-state automaton with rational transition weights assigns w∈Σ^ω its unique-run value Val(a)=liminf_n n⁻¹∑\_{i&lt;n}a_i or limsup_n n⁻¹∑\_{i&lt;n}a_i. For a real-valued property F put F\*(u)=sup_{v∈Σ^ω}F(uv), T_F=sup_wF(w). Safety means F(w)=inf_{u≺w}F\*(u); liveness means for every w with F(w)&lt;T_F some t>F(w) satisfies F\*(u)≥t for every u≺w. Supporting sources: https://research-explorer.ista.ac.at/record/20147

**Source.** Udi Boker, Thomas A. Henzinger, Nicolas Mazzocchi, N. Ege Saraç. *Safety and Liveness of Quantitative Properties and Automata*. 2025. [primary source](https://faculty.runi.ac.il/udiboker/files/QuanSafetyLivenessLMCS.pdf) Location: LMCS p. 2:49, after Theorem 9.5; thesis p. 105.

**Literature check.** Status checked 2026-10-09: Published 2025 text retains deterministic decomposition; no later resolution located.

**Further links.** [1](https://research-explorer.ista.ac.at/record/20147)


<a id="q3434"></a>

## Q3434. Exact complexity with many successors

**Status:** Open · **Kind:** open problem · **Collection** 35

What is the exact complexity of satisfiability for this input-dependent-successor logic, measured in total input length, including the explicitly represented signature?

**Context.** Doctoral context: Piotr Witkowski, Wrocław doctorate 2015; advisor Witold Charatonik. This is later joint work. Origin: Later joint-paper complexity question. Setup: Input is a finite FO² sentence using only two reusable variable names, with equality, k≥1 distinguished binary symbols S_i, with input-dependent k, and additional unary/binary predicates; no constants or function symbols. A model is nonempty, finite or infinite. For each i there must exist a linear order <\_i of arbitrary order type on that domain with S_i(x,y) iff x <\_i y and no z satisfies x <\_i z <\_i y. The orders are absent from the syntax. Metadata: https://ii.uni.wroc.pl/badania/general (doctorates, 20 October 2015). Formulation correction: the complexity parameter includes the represented signature.

**Source.** Jakub Michaliszyn and Piotr Witkowski. *Two-Variable Logic with Arbitrarily Many Successor Relations*. 2026. [primary source](https://arxiv.org/abs/2610.09758v1) Location: Introduction p. 3, Consequences and the size of the finite part.

**Literature check.** Status checked 2026-10-09: October 2026 v1 reports NEXPTIME-hardness and a 2-NEXPTIME upper bound.

**Further links.** [1](https://ii.uni.wroc.pl/badania/general)


<a id="q3489"></a>

## Q3489. Exact connected-set evaluation at minus two

**Status:** Open, partial results · **Kind:** open problem · **Collection** 35

Is C_G(−2) computable in time polynomial in the input size of G?

**Context.** Origin: Thesis question. Setup: For an input finite simple graph G, let C_G(z)=Σ\_S z^|S|, where S ranges over nonempty vertex sets inducing connected subgraphs. Exact evaluation outputs an integer in binary.

**Source.** Lucas Mol. *On Connectedness and Graph Polynomials*. Dalhousie University, 2016. Advisor(s): Jason Brown (acknowledgements and departmental degree record). [primary source](https://central.bac-lac.gc.ca/.item?app=Library&id=TC-NSHD-71408&oclc_number=1033184059&op=pdf) Location: §6.4, p. 166.

**Literature check.** Status checked 9 October 2026: Full thesis §6.4 retains the exceptional point. Later node-reliability/connected-set complexity and correction searches found no resolution.

**Result (2026-10-09).** Exact C_G(-2) evaluation is #P-hard by an explicit polynomial-size single-call reduction and belongs to GapP; it is polynomial-time computable if and only if FP=#P. Rooted attachments also classify every nonzero fixed algebraic evaluation point as #P-hard. The signed function is not called #P-complete. No separation FP != #P is proved; exact algebraic outputs use a fixed-number-field bit model.

[Proof](../../solutions/round-2026-10-09/discrete/Q3489-connected-set-evaluation.md) · [Internal review](../../solutions/round-2026-10-09/reviews/root-review.md) · [Exact computational controls](../../solutions/round-2026-10-09/discrete/connected-set-checks.json). This is a research proposal with a separate internal AI review, not an externally peer-reviewed result.



<a id="q3490"></a>

## Q3490. Unrestricted orbit-finite linear feasibility

**Status:** Open · **Kind:** open problem (Question 8.4) · **Collection** 35

Is there an algorithm deciding whether Mx≤b has a real solution x:C→ℝ, with no finite atom-support requirement on x?

**Context.** Origin: Joint doctoral-paper question retained in the dissertation; rational input and real solutions are explicit in the companion paper. Setup: Let A be a countably infinite set of atoms. For supplied finite S⊂A, B,C are finite unions of orbits, under permutations fixing S, of finitely supported objects built from A. A rational matrix M:B×C→ℚ and vector b:B→ℚ are invariant under those permutations and supplied by finite orbit descriptions. Products Mx are defined only when each row has finitely many nonzero summands. Finite atom support means invariance under all permutations fixing some finite atom set pointwise.

**Source.** Arka Ghosh. *Linear Algebra in Orbit-finite Dimension*. University of Warsaw, 2025. Advisor(s): Sławomir Lasota, Piotr Hofman (auxiliary). [primary source](https://www.mimuw.edu.pl/media/uploads/doctorates/thesis-arka-ghosh.pdf) Location: Thesis Question 8.4, p. 171; §§2.3–2.4; companion 2302.00802v4 §3 p. 8 and §10 Question 1 p. 27.

**Literature check.** Status checked 9 October 2026: thesis and latest companion retain the question; 2026 finite-length results concern finite-support span membership, not unrestricted feasibility. No later resolution located.

**Further links.** [1](https://arxiv.org/pdf/2302.00802v4)


<a id="q3559"></a>

## Q3559. Are GKAT guarded-string languages closed under intersection?

**Status:** Open · **Kind:** open problem · **Collection** 36

Are GKAT guarded-string languages closed under intersection?

**Context.** Sources: https://eprints.illc.uva.nl/2287/1/DS-2024-01.text.pdf and Rooduijn–Kozen–Silva, final IJCAR 2024, https://doi.org/10.1007/978-3-031-63501-4_14 GKAT expressions combine Boolean tests and primitive actions by sequencing, if-then-else, and while. Their languages L(e) consist of finite strings alternating test valuations and actions; sequencing fuses matching endpoint valuations and tests filter the current valuation.

**Source.** Jan Rooduijn. *Fragments and Frame Classes: Towards a Uniform Proof Theory for Modal Fixed Point Logics*. University of Amsterdam, 2024. Advisor(s): Yde Venema and Johannes F. Marti. [primary source](https://eprints.illc.uva.nl/2287/1/DS-2024-01.text.pdf) Location: Thesis Remark 6.6.14, p.185.

**Literature check.** Status: The dissertation’s proof-search upper-bound question was subsequently solved. Two 2026 GKAT follow-ups were inspected and do not settle these questions.

**Further links.** [1](https://doi.org/10.1007/978-3-031-63501-4_14)


<a id="q3560"></a>

## Q3560. For syntax-tree GKAT expressions over a fixed finite nonempty test alphabet and a fixed nonempty…

**Status:** Open · **Kind:** open problem · **Collection** 36

For syntax-tree GKAT expressions over a fixed finite nonempty test alphabet and a fixed nonempty action alphabet, what is the exact complexity of L(e)⊆L(f)? Is the nondeterministic-logspace upper bound optimal?

**Context.** Sources: https://eprints.illc.uva.nl/2287/1/DS-2024-01.text.pdf and Rooduijn–Kozen–Silva, final IJCAR 2024, https://doi.org/10.1007/978-3-031-63501-4_14 GKAT expressions combine Boolean tests and primitive actions by sequencing, if-then-else, and while. Their languages L(e) consist of finite strings alternating test valuations and actions; sequencing fuses matching endpoint valuations and tests filter the current valuation.

**Source.** Jan Rooduijn. *Fragments and Frame Classes: Towards a Uniform Proof Theory for Modal Fixed Point Logics*. University of Amsterdam, 2024. Advisor(s): Yde Venema and Johannes F. Marti. [primary source](https://eprints.illc.uva.nl/2287/1/DS-2024-01.text.pdf) Location: Final article §7, p.273; full version p.17.

**Literature check.** Status: The dissertation’s proof-search upper-bound question was subsequently solved. Two 2026 GKAT follow-ups were inspected and do not settle these questions.

**Further links.** [1](https://doi.org/10.1007/978-3-031-63501-4_14)


<a id="q3571"></a>

## Q3571. Forbidden-subgraph injective labelling

**Status:** Open · **Kind:** open problem (Problem 5.1) · **Collection** 36

For each fixed noncomplete H containing a triangle, classify the complexity of deciding L′(2,1)-labellability of H-free G with input k.

**Context.** Degree: Doctorate Advisors: Jan Kratochvíl. Source type: Doctoral dissertation Origin: Thesis questions; semibalanced pure cases classified. Setup: H-free means no induced H. An L′(2,1)-labelling is an injective f:V(G)→{0,…,k} with |f(u)−f(v)|≥2 on edges. Signed graphs have positive/negative edges, allowing loops and opposite-sign parallel pairs. Switching reverses signs on incident nonloop edges. A signed homomorphism becomes sign-preserving after input switching; lists constrain vertex images. Semibalanced means switching can eliminate purely negative edges; mixed means some vertices have loops and others do not.

**Source.** Nikola Jedličková. *Different perspectives on graph homomorphism problems*. Charles University, 2025. Advisor(s): Jan Kratochvíl. [primary source](https://dspace.cuni.cz/handle/20.500.11956/201659) Location: Problem 5.1, p.155.

**Literature check.** Status: No resolution located by 2026-10-09.

**Further links.** [1](https://dspace.cuni.cz/bitstream/handle/20.500.11956/201659/140128785.pdf?sequence=1&isAllowed=y)


<a id="q3572"></a>

## Q3572. Mixed semibalanced targets

**Status:** Open · **Kind:** open problem (Problem 5.3) · **Collection** 36

Classify fixed mixed semibalanced signed targets H by polynomial-time solvability versus NP-completeness of their list-homomorphism problems.

**Context.** Degree: Doctorate Advisors: Jan Kratochvíl. Source type: Doctoral dissertation Origin: Thesis questions; semibalanced pure cases classified. Setup: H-free means no induced H. An L′(2,1)-labelling is an injective f:V(G)→{0,…,k} with |f(u)−f(v)|≥2 on edges. Signed graphs have positive/negative edges, allowing loops and opposite-sign parallel pairs. Switching reverses signs on incident nonloop edges. A signed homomorphism becomes sign-preserving after input switching; lists constrain vertex images. Semibalanced means switching can eliminate purely negative edges; mixed means some vertices have loops and others do not.

**Source.** Nikola Jedličková. *Different perspectives on graph homomorphism problems*. Charles University, 2025. Advisor(s): Jan Kratochvíl. [primary source](https://dspace.cuni.cz/handle/20.500.11956/201659) Location: Problem 5.3, p.156.

**Literature check.** Status: No resolution located by 2026-10-09.

**Further links.** [1](https://dspace.cuni.cz/bitstream/handle/20.500.11956/201659/140128785.pdf?sequence=1&isAllowed=y)


<a id="q3584"></a>

## Q3584. Polynomial-time functional approximation of matroid branch-depth

**Status:** Open · **Kind:** open problem (Problem 7.2) · **Collection** 36

Do a computable f and a polynomial-time independence-oracle algorithm exist that, for every input matroid M with |E(M)|≥2, produce a branch-depth decomposition of width and radius at most f(bd(M))?

**Context.** Degree: PhD defence verified; award unverified. Advisors: Daniel Král. Source type: Later joint paper; verified doctoral genealogy Paper: Measuring Depth of Matroids Authors: Jakub Balabán, Petr Hliněný, Jan Jedelský, Kristýna Pekárková Origin: Problem 7.2 in the revised paper; the v1 question bearing that number is different. Setup: For a finite matroid M with |E|≥2, a branch-depth decomposition is a tree with an internal vertex and leaves bijectively labelled by E. Its width is max_X[r(X)+r(E−X)−r(E)], over unions X of components after deleting an internal vertex. The branch-depth bd(M) minimizes the maximum of tree radius and width.

**Source.** Jakub Balabán, Petr Hliněný, Jan Jedelský, Kristýna Pekárková. *Measuring Depth of Matroids*. 2026. [primary source](https://arxiv.org/abs/2604.04896v3) Location: Version 3, Problem 7.2, p.35; Definition 4.2.

**Literature check.** Status: Latest v3 dated 2026-10-02 inspected; bounded 2026-10-09 check found no resolution.


<a id="q3661"></a>

## Q3661. Is satisfiability for PML(p,s,¬) EXPTIME-complete with unbounded input relation symbols and arities?

**Status:** Open · **Kind:** open problem · **Collection** 37

Is satisfiability for PML(p,s,¬) EXPTIME-complete with unbounded input relation symbols and arities?

**Context.** On nonempty W, Boolean formulas use ⟨R⟩(φ₁,…,φ\_k), true at w when some (w,w₁,…,w_k)∈R has φ\_i true at w_i. Relation operations p,s cyclically permute coordinates and swap the last two; ¬ complements in W^arity, and ∩ intersects equal-arity relations.

**Source.** Reijo Jaakkola. *Complexity of Polyadic Boolean Modal Logics*. 2023. [primary source](https://doi.org/10.4230/LIPIcs.CSL.2023.26) Location: §6, p.26:16.

**Literature check.** Status: These are distinct unsolved extensions of the paper’s theorems. Later work checked October 9, 2026; no resolution located.


<a id="q3662"></a>

## Q3662. For fixed c≥2, is satisfiability for PML(p,s,¬,∩) plus binary identity I={(w,w):w∈W}…

**Status:** Open · **Kind:** open problem · **Collection** 37

For fixed c≥2, is satisfiability for PML(p,s,¬,∩) plus binary identity I={(w,w):w∈W} EXPTIME-complete, allowing at most c relation symbols of arity at most c?

**Context.** On nonempty W, Boolean formulas use ⟨R⟩(φ₁,…,φ\_k), true at w when some (w,w₁,…,w_k)∈R has φ\_i true at w_i. Relation operations p,s cyclically permute coordinates and swap the last two; ¬ complements in W^arity, and ∩ intersects equal-arity relations.

**Source.** Reijo Jaakkola. *Complexity of Polyadic Boolean Modal Logics*. 2023. [primary source](https://doi.org/10.4230/LIPIcs.CSL.2023.26) Location: §6, p.26:17.

**Literature check.** Status: These are distinct unsolved extensions of the paper’s theorems. Later work checked October 9, 2026; no resolution located.


<a id="q3666"></a>

## Q3666. For every fixed finite nonbipartite simple graph H, is its oracular quantum homomorphism problem…

**Status:** Open · **Kind:** open problem · **Collection** 37

For every fixed finite nonbipartite simple graph H, is its oracular quantum homomorphism problem recursively-enumerable-complete? Input: finite simple G. A solution consists of d≥1 and complex Hermitian projections P_{x,a}, indexed by x∈V(G),a∈V(H), with Σ\_a P_{x,a}=I_d; P_{x,a}P_{y,b}=0 whenever xy∈E(G),ab∉E(H); and [P_{x,a},P_{y,b}]=0 for every a,b whenever xy∈E(G).

**Source.** Ciardo, Hebbeker, Joubert, Kreiß and Mottet. *Schrijver-Delsarte rigidity in association schemes and undecidability of quantum graph homomorphism*. 2026. [primary source](https://arxiv.org/abs/2609.20678) Location: §2, p.12; Definition 2.1, p.4.

**Literature check.** Status: The latest paper proves special target families and explicitly leaves this classification open. Later-result check October 9, 2026 found no resolution.


<a id="q3667"></a>

## Q3667. Fix c≥1 and a finite family F of finite simple graphs with edges colored from [c]. Given a…

**Status:** Open · **Kind:** open problem (Problem 1) · **Collection** 37

Fix c≥1 and a finite family F of finite simple graphs with edges colored from [c]. Given a finite simple graph G, ask whether its edges admit a [c]-coloring such that no member of F has a color-preserving graph homomorphism into G. For every fixed c,F, is this decision problem in P or NP-complete?

**Source.** Barsukov, Mottet and Perinti. *Edge-coloring problems with forbidden patterns and planted colors*. 2026. [primary source](https://arxiv.org/abs/2507.19000) Location: Problem 1, p.1; §1.1, p.2.

**Literature check.** Status: This restates the earlier GMSNP dichotomy problem. The latest paper handles special forbidden families; current versions and later results checked October 9, 2026, with no general resolution located.


<a id="q3668"></a>

## Q3668. Are cyclic arithmetic and Peano arithmetic exponentially separated in shortest proof size?…

**Status:** Open · **Kind:** open problem · **Collection** 37

Are cyclic arithmetic and Peano arithmetic exponentially separated in shortest proof size? Precisely, do ε>0 and arbitrarily large cyclic proofs π of sentences φ exist such that every PA proof of φ has size ≥2^{|π|^ε}? Use the ordinary sequent calculi with cut and symbol-count size. Cyclic arithmetic replaces induction by finite directed proof graphs over Robinson arithmetic; every infinite unfolded branch must admit, on some tail, a term trace respecting substitutions, nonincreasing at each step and strictly decreasing infinitely often through antecedent inequalities.

**Source.** Dominik Wehr. *Cyclic Proof Theory*. University of Gothenburg, 2025. Advisor(s): Graham E. Leigh and Bahareh Afshari. [primary source](https://hdl.handle.net/2077/89733) Location: Dissertation §3.5, p.57; Das, On the logical complexity of cyclic arithmetic (2020), §§2–3,10.2.

**Literature check.** Status: The dissertation reaffirms Das’s question. Leigh–Wehr’s September 2026 publisher final, §6.4, gives translation upper bounds and does not settle separation. Current sources checked October 9, 2026.


<a id="q3684"></a>

## Q3684. Subquadratic-logarithmic generating-set algorithm

**Status:** Open · **Kind:** open problem · **Collection** 37

Does GENERATING SET admit an O\*(2^{o((log s)²)})-time algorithm?

**Context.** Doctoral connection: Algorithms and Graph Structures for Splitting Network Flows, in Theory and Practice; University of Helsinki, 2025; advisers Alexandru I. Tomescu. Given a nonempty finite set A of positive integers and positive integer k, GENERATING SET asks whether some k-element set Z of positive integers has every a∈A as a subset sum. Put s=max A; O\*(·) suppresses polynomial factors in binary input length. Authors: Andreas Grigorjew, Wanchote Jiamjitrak, Brendan Mumey, Alexandru I. Tomescu. Explicit question in the conclusion; linked to minimum-flow-decomposition complexity.

**Source.** Andreas Grigorjew, Wanchote Jiamjitrak, Brendan Mumey and Alexandru I. Tomescu. *Width Parameters for Minimum Flow Decomposition*. 2024. [primary source](https://arxiv.org/abs/2409.20278) Location: Section 6, p.17; Definition 10, p.6.

**Literature check.** Status: v2, 2025-11-26; no later resolution found by 2026-10-09.


<a id="q3824"></a>

## Q3824. Polynomial Cutting Planes proofs of Tseitin contradictions

**Status:** Open · **Kind:** open problem · **Collection** 39

Does a polynomial p bound the number of lines in some Cutting Planes refutation of every F by p(|F|), with |F| its CNF encoding length?

**Context.** Paper authors: Noah Fleming, Mika Göös, Russell Impagliazzo, Toniann Pitassi, Robert Robere, Li-Yang Tan, Avi Wigderson. On the Power and Limitations of Branch and Cut, Theory of Computing 22(2), 2026. Let G be finite simple and χ:V(G)→{0,1} have odd sum. Let F directly encode ⊕\_{e∋v}x_e=χ(v) as CNF. Translate clauses to literal-sum ≥1, interpreting ¬x as 1−x, and include 0≤x_e≤1. Cutting Planes permits nonnegative integer combinations and division of a·x≥b by positive integers dividing every coefficient of a, rounding b/d upward. Refutations derive 0≥1.

**Source.** Noah Fleming, Mika Göös, Russell Impagliazzo, Toniann Pitassi, Robert Robere, Li-Yang Tan and Avi Wigderson. *On the Power and Limitations of Branch and Cut*. 2026. [primary source](https://www.theoryofcomputing.org/articles/v022a002/) Location: Existing proof-complexity question restated in the doctoral-linked joint paper. Locator: final §6, p.30; definitions pp.3,10–11.

**Literature check.** Status: Inspected June 2026 publisher final and thesis. No later resolution located, 10 October 2026.

**Further links.** [1](https://noahrfleming.github.io/papers/Thesis.pdf) · [2](https://www.cs.toronto.edu/~noahfleming/Vita.pdf)


<a id="q3861"></a>

## Q3861. Do there exist families f_N,g_N∈C[x_1,…,x_N] and integers d_N≥2 with f_N=g_N^{d_N},…

**Status:** Open · **Kind:** open problem · **Collection** 39

Do there exist families f_N,g_N∈C[x_1,…,x_N] and integers d_N≥2 with f_N=g_N^{d_N}, deg(f_N)=N^{O(1)}, and W(f_N)=N^{O(1)}, while W(g_N) is not bounded by any polynomial in N?

**Context.** Paper origin: Robert Andrews, Jules Armand, Prateek Dwivedi, Magnus Rahbek Dalgaard Hansen, Nutan Limaye, Srikanth Srinivasan and Sébastien Tavenas, On Closure Properties of Read-Once Oblivious Algebraic Branching Programs, ITCS 2026, §6, p.9:17; published version read. Setup: Over C, an roABP is a layered directed source–sink graph whose ith-layer edge labels are univariate polynomials in x_{π(i)}, for one variable ordering π. It computes the sum of products along source–sink paths. Let W(f) be its minimum width over all variable orders; width is the largest layer size. Use the paper’s polynomial-degree, polynomial-size family convention; size and width are polynomially related.

**Source.** Robert Andrews, Jules Armand, Prateek Dwivedi, Magnus Rahbek Dalgaard Hansen, Nutan Limaye, Srikanth Srinivasan and Sébastien Tavenas. *On Closure Properties of Read-Once Oblivious Algebraic Branching Programs*. 2026. [primary source](https://doi.org/10.4230/LIPIcs.ITCS.2026.9) Location: §6, p.9:17; published version read.

**Literature check.** Status: This expresses the paper’s easy-power/hard-root question in the characteristic-zero setting. No later resolution found through 10 October 2026.


<a id="q3862"></a>

## Q3862. Does every unitary U on X satisfying UR(σ)=R(σ)U for all σ∈Γ admit an exact Γ-symmetric…

**Status:** Open · **Kind:** open problem · **Collection** 39

Does every unitary U on X satisfying UR(σ)=R(σ)U for all σ∈Γ admit an exact Γ-symmetric implementation, allowing ancillas returned to |0⟩?

**Context.** Paper origin: Davi Castro-Silva, Tom Gur and Sergii Strelchuk, Symmetric Quantum Computation, ITCS 2026, §5, p.35:8; full definitions in arXiv:2501.01214v2, Definitions 9–12, pp.16–18. Setup: Γ≤S_X acts by permuting a finite set X of active qubits. Circuits may use finitely many ancillas initially |0⟩, arbitrary one-qubit unitaries, and gates flipping a target bit when the sum of a disjoint set of control bits is ≥t or =t, for a nonnegative integer t. Gates are grouped into ordered layers, each containing mutually commuting gates. A circuit is Γ-symmetric if every σ∈Γ extends to a permutation of all its qubits that preserves each layer, including gate types, parameters and supports. Write R(σ) for the permutation of the active qubits’ tensor factors.

**Source.** Davi Castro-Silva, Tom Gur and Sergii Strelchuk. *Symmetric Quantum Computation*. 2026. [primary source](https://doi.org/10.4230/LIPIcs.ITCS.2026.35) Location: §5, p.35:8; full definitions in arXiv:2501.01214v2, Definitions 9–12, pp.16–18.

**Literature check.** Status: The published paper leaves arbitrary Γ open after proving partition-permutation cases. No matching resolution found through 10 October 2026.

**Further links.** [1](https://arxiv.org/abs/2501.01214v2)


<a id="q3863"></a>

## Q3863. Given oracle maps f,g:[N]→[N], Nephew asks for v with f(f(g(v)))≠f(v) or f(g(v))=v. Does Nephew…

**Status:** Open · **Kind:** open problem · **Collection** 39

Given oracle maps f,g:[N]→[N], Nephew asks for v with f(f(g(v)))≠f(v) or f(g(v))=v. Does Nephew admit a black-box reduction to Lossy-Code of poly(log N) complexity? Here complexity is log L+d, where L is target-table bit length and d bounds bit-query depth for each target bit and for decoding any target solution. The authors conjecture no.

**Context.** Paper origin: Noah Fleming, Stefan Grosser, Siddhartha Jain, Jiawei Li, Hanlin Ren, Morgan Shirley and Weiqiang Yuan, Total Search Problems in ZPP, ITCS 2026, pp.60:2,60:5–6,60:9–11,60:21; final version read. Setup: For m≥1, Lossy-Code receives C:{0,1}^m→{0,1}^{m−1} and D:{0,1}^{m−1}→{0,1}^m and asks for y with D(C(y))≠y. Maps are oracle tables in the black-box model and Boolean circuits in the white-box model.

**Source.** Noah Fleming, Stefan Grosser, Siddhartha Jain, Jiawei Li, Hanlin Ren, Morgan Shirley and Weiqiang Yuan. *Total Search Problems in ZPP*. 2026. [primary source](https://doi.org/10.4230/LIPIcs.ITCS.2026.60) Location: pp.60:2,60:5–6,60:9–11,60:21; final version read.

**Literature check.** Status: Both remain unresolved in the current sources; no later resolution found through 10 October 2026.

**Further links.** [1](https://arxiv.org/abs/2512.01138)


<a id="q3864"></a>

## Q3864. Given binary N≥2, can finding a prime N&lt;p<2N be reduced deterministically in polynomial time to…

**Status:** Open · **Kind:** open problem · **Collection** 39

Given binary N≥2, can finding a prime N&lt;p<2N be reduced deterministically in polynomial time to white-box Lossy-Code, with every target solution decoding to a valid prime?

**Context.** Paper origin: Noah Fleming, Stefan Grosser, Siddhartha Jain, Jiawei Li, Hanlin Ren, Morgan Shirley and Weiqiang Yuan, Total Search Problems in ZPP, ITCS 2026, pp.60:2,60:5–6,60:9–11,60:21; final version read. Setup: For m≥1, Lossy-Code receives C:{0,1}^m→{0,1}^{m−1} and D:{0,1}^{m−1}→{0,1}^m and asks for y with D(C(y))≠y. Maps are oracle tables in the black-box model and Boolean circuits in the white-box model.

**Source.** Noah Fleming, Stefan Grosser, Siddhartha Jain, Jiawei Li, Hanlin Ren, Morgan Shirley and Weiqiang Yuan. *Total Search Problems in ZPP*. 2026. [primary source](https://doi.org/10.4230/LIPIcs.ITCS.2026.60) Location: pp.60:2,60:5–6,60:9–11,60:21; final version read.

**Literature check.** Status: Both remain unresolved in the current sources; no later resolution found through 10 October 2026.

**Further links.** [1](https://arxiv.org/abs/2512.01138)


<a id="q3879"></a>

## Q3879. Is there an algorithm that, given only an n-vertex graph G, finds a maximum-cardinality…

**Status:** Open · **Kind:** open problem (Question 9) · **Collection** 39

Is there an algorithm that, given only an n-vertex graph G, finds a maximum-cardinality independent set in time 2^{O(cw(G))}n^{O(1)}, without receiving a clique-width expression?

**Context.** Doctoral source: Tuukka Korhonen, Computing Width Parameters of Graphs, University of Bergen PhD, May 2024; advisor Fedor V. Fomin, co-advisor Petr A. Golovach. Question 9, p.308 (PDF p.326), restates a question of Oum, Sæther and Vatshelle (2014). Setup: For a finite simple graph G, a k-expression constructs G using at most k vertex labels and four operations: creating one labeled vertex, taking disjoint unions, relabeling every vertex of one label, and adding all edges between two different labels. The clique-width cw(G) is the least such k. An independent set contains no adjacent pair of vertices.

**Source.** Tuukka Korhonen. *Computing Width Parameters of Graphs*. University of Bergen, 2024. Advisor(s): Fedor V. Fomin; co-advisor Petr A. Golovach. [primary source](https://tuukkakorhonen.com/papers/phd-thesis.pdf) Location: Question 9, p.308 (PDF p.326), restates a question of Oum, Sæther and Vatshelle (2014).

**Literature check.** Status: The author’s 16 September 2026 problem list retains this algorithmic gap. The known decomposition-free bound is 2^{O(k log k)}n^{O(1)}. No matching resolution found through 10 October 2026.

**Further links.** [1](https://tuukkakorhonen.com/problems.html)


<a id="q3880"></a>

## Q3880. Is C_k≥2^{c k log₂k} for some absolute c>0 and all sufficiently large k?

**Status:** Open · **Kind:** open problem · **Collection** 39

Is C_k≥2^{c k log₂k} for some absolute c>0 and all sufficiently large k?

**Context.** Paper source: Kacper Kluk and Jesper Nederlof, Lower Bounds on Pure Dynamic Programming for Connectivity Problems on Graphs of Bounded Path-Width, ICALP 2026, §§4.1,7, pp.130:12–13,130:21; published version read. Setup: M_k has rows and columns indexed by permutations of [k], with M_k(ρ,σ)=1 exactly when σρ is a single k-cycle. Let C_k be the minimum number of all-one combinatorial rectangles needed to cover all its 1-entries.

**Source.** Kacper Kluk and Jesper Nederlof. *Lower Bounds on Pure Dynamic Programming for Connectivity Problems on Graphs of Bounded Path-Width*. 2026. [primary source](https://doi.org/10.4230/LIPIcs.ICALP.2026.130) Location: §§4.1,7, pp.130:12–13,130:21; published version read.

**Literature check.** Status: No matching resolution found through 10 October 2026.

**Notes.** This older Raz–Spieker frontier is explicitly reaffirmed here.


<a id="q3881"></a>

## Q3881. For every finite simple undirected n-vertex graph G of treewidth k, does the convex hull of…

**Status:** Open · **Kind:** open problem · **Collection** 39

For every finite simple undirected n-vertex graph G of treewidth k, does the convex hull of incidence vectors of its Hamiltonian cycles admit an extended formulation with 2^{O(k)}n^{O(1)} inequalities? An extended formulation is a polyhedron projecting linearly onto that convex hull. Treewidth minimizes the largest bag size minus one over tree-indexed bags covering vertices and edges, with each vertex’s bags connected.

**Context.** Paper source: Kacper Kluk and Jesper Nederlof, Lower Bounds on Pure Dynamic Programming for Connectivity Problems on Graphs of Bounded Path-Width, ICALP 2026, §§4.1,7, pp.130:12–13,130:21; published version read. Setup: M_k has rows and columns indexed by permutations of [k], with M_k(ρ,σ)=1 exactly when σρ is a single k-cycle. Let C_k be the minimum number of all-one combinatorial rectangles needed to cover all its 1-entries.

**Source.** Kacper Kluk and Jesper Nederlof. *Lower Bounds on Pure Dynamic Programming for Connectivity Problems on Graphs of Bounded Path-Width*. 2026. [primary source](https://doi.org/10.4230/LIPIcs.ICALP.2026.130) Location: §§4.1,7, pp.130:12–13,130:21; published version read.

**Literature check.** Status: No matching resolution found through 10 October 2026.


<a id="q3882"></a>

## Q3882. Is deciding existence of a 3-visit schedule strongly NP-complete when all deadlines are distinct?

**Status:** Open · **Kind:** conjecture (Conjecture 62) · **Collection** 39

Is deciding existence of a 3-visit schedule strongly NP-complete when all deadlines are distinct?

**Context.** Paper source: Sotiris Kanellopoulos, Giorgos Mitropoulos, Christos Pergaminelis and Thanos Tolias, Hardness, Tractability and Density Thresholds of finite Pinwheel Scheduling Variants. ICALP 2026 final, Conjecture 62 and §8; later arXiv:2604.16030v5, 11 August 2026, Conjecture 1 and §8, pp.27–28. Q3882–28 restate Kanellopoulos, Pergaminelis, Kokkou, Markou and Pagourtzis (SODA 2026). Setup: A binary-encoded list of positive deadlines d₁,…,d_n describes n distinct tasks, even when deadlines repeat. An r-visit schedule is a word of length rn containing each task exactly r times. Task i first occurs by position d_i; successive occurrences of task i must be at most d_i positions apart. There is no terminal deadline after its last occurrence.

**Source.** Sotiris Kanellopoulos, Giorgos Mitropoulos, Christos Pergaminelis and Thanos Tolias. *Hardness, Tractability and Density Thresholds of finite Pinwheel Scheduling Variants*. 2026. [primary source](https://doi.org/10.4230/LIPIcs.ICALP.2026.122) Location: Conjecture 62 and §8; later arXiv:2604.16030v5, 11 August 2026, Conjecture 1 and §8, pp.27–28.

**Literature check.** Status: Current versions retain all three; no matching later resolution found through 10 October 2026.

**Further links.** [1](https://arxiv.org/abs/2604.16030v5)


<a id="q3883"></a>

## Q3883. Does 2-visit feasibility have a deterministic algorithm with running time f(p)L^{O(1)}, where p…

**Status:** Open · **Kind:** conjecture (Conjecture 62) · **Collection** 39

Does 2-visit feasibility have a deterministic algorithm with running time f(p)L^{O(1)}, where p is the number of distinct deadlines, L the input bit length, and f is computable?

**Context.** Paper source: Sotiris Kanellopoulos, Giorgos Mitropoulos, Christos Pergaminelis and Thanos Tolias, Hardness, Tractability and Density Thresholds of finite Pinwheel Scheduling Variants. ICALP 2026 final, Conjecture 62 and §8; later arXiv:2604.16030v5, 11 August 2026, Conjecture 1 and §8, pp.27–28. Q3882–28 restate Kanellopoulos, Pergaminelis, Kokkou, Markou and Pagourtzis (SODA 2026). Setup: A binary-encoded list of positive deadlines d₁,…,d_n describes n distinct tasks, even when deadlines repeat. An r-visit schedule is a word of length rn containing each task exactly r times. Task i first occurs by position d_i; successive occurrences of task i must be at most d_i positions apart. There is no terminal deadline after its last occurrence.

**Source.** Sotiris Kanellopoulos, Giorgos Mitropoulos, Christos Pergaminelis and Thanos Tolias. *Hardness, Tractability and Density Thresholds of finite Pinwheel Scheduling Variants*. 2026. [primary source](https://doi.org/10.4230/LIPIcs.ICALP.2026.122) Location: Conjecture 62 and §8; later arXiv:2604.16030v5, 11 August 2026, Conjecture 1 and §8, pp.27–28.

**Literature check.** Status: Current versions retain all three; no matching later resolution found through 10 October 2026.

**Further links.** [1](https://arxiv.org/abs/2604.16030v5)


<a id="q3884"></a>

## Q3884. Must every list with Σ\_i1/d_i≤1 admit a 2-visit schedule?

**Status:** Open · **Kind:** conjecture (Conjecture 62) · **Collection** 39

Must every list with Σ\_i1/d_i≤1 admit a 2-visit schedule?

**Context.** Paper source: Sotiris Kanellopoulos, Giorgos Mitropoulos, Christos Pergaminelis and Thanos Tolias, Hardness, Tractability and Density Thresholds of finite Pinwheel Scheduling Variants. ICALP 2026 final, Conjecture 62 and §8; later arXiv:2604.16030v5, 11 August 2026, Conjecture 1 and §8, pp.27–28. Q3882–28 restate Kanellopoulos, Pergaminelis, Kokkou, Markou and Pagourtzis (SODA 2026). Setup: A binary-encoded list of positive deadlines d₁,…,d_n describes n distinct tasks, even when deadlines repeat. An r-visit schedule is a word of length rn containing each task exactly r times. Task i first occurs by position d_i; successive occurrences of task i must be at most d_i positions apart. There is no terminal deadline after its last occurrence.

**Source.** Sotiris Kanellopoulos, Giorgos Mitropoulos, Christos Pergaminelis and Thanos Tolias. *Hardness, Tractability and Density Thresholds of finite Pinwheel Scheduling Variants*. 2026. [primary source](https://doi.org/10.4230/LIPIcs.ICALP.2026.122) Location: Conjecture 62 and §8; later arXiv:2604.16030v5, 11 August 2026, Conjecture 1 and §8, pp.27–28.

**Literature check.** Status: Current versions retain all three; no matching later resolution found through 10 October 2026.

**Further links.** [1](https://arxiv.org/abs/2604.16030v5)


<a id="q3885"></a>

## Q3885. Does this optimization problem admit a polynomial-time approximation algorithm with…

**Status:** Open · **Kind:** conjecture (Conjecture 5.1) · **Collection** 39

Does this optimization problem admit a polynomial-time approximation algorithm with approximation ratio (log k)^{1+o(1)} as k→∞, returning feasible flows for the selected pairs?

**Context.** Paper origin: Nikhil Bansal, Arun Jambulapati and Thatchaphol Saranurak, Expander Decomposition with Almost Optimal Overhead, ICALP 2026, Conjecture 5.1, §5, p.22:15; published version read. Setup: Input is an undirected graph with unit edge capacities and k specified source–sink pairs. Select as many pairs as possible and route one unit of flow for each selected pair. Each commodity may split among several paths, but the sum of the loads of all commodities on every edge must be at most one. Let OPT be the maximum number of simultaneously routable pairs.

**Source.** Nikhil Bansal, Arun Jambulapati and Thatchaphol Saranurak. *Expander Decomposition with Almost Optimal Overhead*. 2026. [primary source](https://doi.org/10.4230/LIPIcs.ICALP.2026.22) Location: Conjecture 5.1, §5, p.22:15; published version read.

**Literature check.** Status: The current final and April arXiv revision retain this conjecture. Their improved expander decomposition does not itself establish the all-or-nothing guarantee; no matching resolution found through 10 October 2026. This is the multicommodity selection problem, distinct from the unrelated edge-wise zero-or-capacity flow problem bearing the same name.


<a id="q3886"></a>

## Q3886. Is deciding whether such an assignment exists strongly NP-complete, equivalently NP-complete…

**Status:** Open · **Kind:** conjecture (Conjecture 2) · **Collection** 39

Is deciding whether such an assignment exists strongly NP-complete, equivalently NP-complete even when the input integers are encoded in unary?

**Context.** Paper origin: Sotiris Kanellopoulos, Finite Pinwheel Covering, arXiv:2607.28574v4, 7 October 2026, Definition 3, p.5, and Conjecture 2, p.15; current full version read. Setup: Input consists of n pairwise distinct positive integers f₁,…,f_n, encoded in binary. A feasible assignment pairs each frequency f_i with a distinct position b_i∈{1,…,n} and a distinct position c_i∈{n+1,…,2n}, using every position exactly once, such that c_i−b_i≥f_i. This is the paper’s explicit numerical-matching definition of 2-Visits Covering: each task is performed twice, with a minimum recovery gap rather than a maximum deadline gap.

**Source.** Sotiris Kanellopoulos. *Finite Pinwheel Covering*. 2026. [primary source](https://arxiv.org/abs/2607.28574v4) Location: Definition 3, p.5, and Conjecture 2, p.15; current full version read.

**Literature check.** Status: Conjecture 2 names this Definition 3 problem. The paper’s finite-window Definition 2 has a boundary discrepancy; its claimed equivalence is not used here. The 7 October version leaves pairwise-distinct frequencies unresolved. Its hardness result permits repeated frequencies. No later matching resolution found through 10 October 2026; no doctoral attribution is claimed.


<a id="q3903"></a>

## Q3903. With vertex weights in {1,…,n}, can a maximum-weight independent set be found in time…

**Status:** Open · **Kind:** open problem · **Collection** 40

With vertex weights in {1,…,n}, can a maximum-weight independent set be found in time O(n+m)+f(tw(G)) for some computable f, without a supplied decomposition? The constant in O(n+m) must be parameter-independent.

**Context.** Paper origin: Tuukka Korhonen, Daniel Lokshtanov and Saket Saurabh, Courcelle’s Theorem in Truly Linear FPT, arXiv:2607.11230v1, 13 July 2026, §6, p.15; computational model §2, p.4. Setup: Input is a finite simple n-vertex, m-edge graph, given as vertex and edge lists. Use word-RAM with Θ(log(n+m+2))-bit words. A tree decomposition comprises tree-indexed vertex bags covering every vertex and edge, with each vertex’s bags forming a connected subtree. Treewidth tw(G) is the minimum, over such decompositions, of the largest bag size minus one. An independent set contains no adjacent pair.

**Source.** Tuukka Korhonen, Daniel Lokshtanov and Saket Saurabh. *Courcelle’s Theorem in Truly Linear FPT*. 2026. [primary source](https://arxiv.org/abs/2607.11230v1) Location: §6, p.15; computational model §2, p.4.

**Literature check.** Status: The source explicitly retains this weighted question after proving its unweighted results. No matching later resolution found through 10 October 2026.


<a id="q3904"></a>

## Q3904. Determine q(n,c) asymptotically, up to universal constant factors, throughout the regimes…

**Status:** Open · **Kind:** open problem · **Collection** 40

Determine q(n,c) asymptotically, up to universal constant factors, throughout the regimes integers n≥1 and c≥0.

**Context.** Paper source: Xudong Wu, Guangxu Yang and Penghui Yao, A Lifting Theorem for Hybrid Classical-Quantum Communication Complexity, ICALP 2026, §1.4(5), p.155:6; model in §2.3, pp.155:9–10. Published version read. Setup: Alice receives x∈{0,1}^n and Bob receives y∈{0,1}^n; they must decide whether some coordinate has x_i=y_i=1. First they exchange at most c classical bits using deterministic classical computation. Then they exchange at most q qubits using quantum computation. Arbitrary prior entanglement is allowed but cannot be accessed during the classical phase. Communication is interactive in each phase; the worst-case error is at most 1/10 on every input. Let q(n,c) be the least such quantum communication cost.

**Source.** Xudong Wu, Guangxu Yang and Penghui Yao. *A Lifting Theorem for Hybrid Classical-Quantum Communication Complexity*. 2026. [primary source](https://doi.org/10.4230/LIPIcs.ICALP.2026.155) Location: §1.4(5), p.155:6; model in §2.3, pp.155:9–10.

**Literature check.** Status: The final explicitly leaves this tight tradeoff open; its lifting theorem uses much larger gadgets and does not settle the two-bit AND gadget underlying disjointness. No matching later resolution found through 10 October 2026.


<a id="q3913"></a>

## Q3913. Can every n-vertex graph obtain a maximal independent set in O(√log n·(loglog n)^C) rounds, for…

**Status:** Open · **Kind:** open problem · **Collection** 40

Can every n-vertex graph obtain a maximal independent set in O(√log n·(loglog n)^C) rounds, for some constant C, with failure probability at most 1/n?

**Context.** LOCAL algorithms know n and unique polynomial-range identifiers, use synchronous neighbor communication with unbounded messages and computation, and independent vertex randomness. An LCL uses fixed finite input/output alphabets and fixed-radius local validity rules on graphs of some fixed maximum degree. In deterministic VOLUME, a query starts at its requested vertex and adaptively discovers neighboring vertices; it knows n and unique polynomial-range vertex identifiers. All separately computed labels must form a valid solution. Complexity counts worst-case probes per requested vertex.

**Source.** Václav Rozhoň. *Invitation to Local Algorithms*. 2024. [primary source](https://arxiv.org/abs/2406.19430) Location: Problems 1.13 and 3.4; thesis genealogy led to this survey.

**Literature check.** Status: No resolution found through 10 October 2026; Peng’s July 2026 paper explicitly retains Q3914.

**Further links.** [1](https://www.podc.org/2025-principles-of-distributed-computing-doctoral-dissertation-award/) · [2](https://arxiv.org/abs/2607.09626)


<a id="q3914"></a>

## Q3914. Does a solvable LCL have optimal deterministic VOLUME complexity ω(log\*n) and o(n) on…

**Status:** Open · **Kind:** open problem · **Collection** 40

Does a solvable LCL have optimal deterministic VOLUME complexity ω(log\*n) and o(n) on bounded-degree graphs?

**Context.** LOCAL algorithms know n and unique polynomial-range identifiers, use synchronous neighbor communication with unbounded messages and computation, and independent vertex randomness. An LCL uses fixed finite input/output alphabets and fixed-radius local validity rules on graphs of some fixed maximum degree. In deterministic VOLUME, a query starts at its requested vertex and adaptively discovers neighboring vertices; it knows n and unique polynomial-range vertex identifiers. All separately computed labels must form a valid solution. Complexity counts worst-case probes per requested vertex.

**Source.** Václav Rozhoň. *Invitation to Local Algorithms*. 2024. [primary source](https://arxiv.org/abs/2406.19430) Location: Problems 1.13 and 3.4; thesis genealogy led to this survey.

**Literature check.** Status: No resolution found through 10 October 2026; Peng’s July 2026 paper explicitly retains Q3914.

**Further links.** [1](https://www.podc.org/2025-principles-of-distributed-computing-doctoral-dissertation-award/) · [2](https://arxiv.org/abs/2607.09626)


<a id="q3915"></a>

## Q3915. An offline vertex set V is known initially. Vertices w arrive sequentially, revealing triples…

**Status:** Open · **Kind:** open problem · **Collection** 40

An offline vertex set V is known initially. Vertices w arrive sequentially, revealing triples {u,v,w} with u,v∈V. The algorithm irrevocably selects at most one arriving triple, keeping all selected triples vertex-disjoint. Does a randomized algorithm achieve expected cardinality at least (1/3+ε)OPT for some absolute ε>0 on every finite instance fixed independently of its randomness, without a degree bound? OPT is the offline maximum matching cardinality.

**Context.** Locators: thesis §4.1 and Conclusion p.165; §7.1; journal matching §6; heap §1.

**Source.** Danish Kashaev. *Approximation via Duality in Offline, Online and Strategic Settings*. University of Amsterdam, 2026. Advisor(s): Guido Schäfer and Daniel Dadush. [primary source](https://eprints.illc.uva.nl/id/eprint/2410/) Location: thesis §4.1 and Conclusion p.165; §7.1; journal matching §6; heap §1.

**Literature check.** Status: No resolution found through 10 October 2026; April 2026 matching final retains Q3915.

**Further links.** [1](https://doi.org/10.1007/s10107-026-02360-2) · [2](https://doi.org/10.1007/s10107-024-02145-5)


<a id="q3916"></a>

## Q3916. In an infinite rooted binary heap with distinct real keys increasing along root-to-leaf paths,…

**Status:** Open · **Kind:** open problem · **Collection** 40

In an infinite rooted binary heap with distinct real keys increasing along root-to-leaf paths, an explorer starts at the root and learns keys only by visiting vertices; each edge traversal costs one. Must every always-correct randomized algorithm identifying the nth smallest key have superlinear worst-case expected travel cost, even with unrestricted memory and an oblivious adversary?

**Context.** Locators: thesis §4.1 and Conclusion p.165; §7.1; journal matching §6; heap §1.

**Source.** Danish Kashaev. *Approximation via Duality in Offline, Online and Strategic Settings*. University of Amsterdam, 2026. Advisor(s): Guido Schäfer and Daniel Dadush. [primary source](https://eprints.illc.uva.nl/id/eprint/2410/) Location: thesis §4.1 and Conclusion p.165; §7.1; journal matching §6; heap §1.

**Literature check.** Status: No resolution found through 10 October 2026; April 2026 matching final retains Q3915.

**Further links.** [1](https://doi.org/10.1007/s10107-026-02360-2) · [2](https://doi.org/10.1007/s10107-024-02145-5)


<a id="q3917"></a>

## Q3917. Writing R_L(n) and R_V(n) for optimal randomized LCA and VOLUME probe complexities of an LCL,…

**Status:** Open · **Kind:** open problem (Question 58) · **Collection** 40

Writing R_L(n) and R_V(n) for optimal randomized LCA and VOLUME probe complexities of an LCL, must R_V(n)=O((R_L(n)+1)^C) for some constant C depending on the LCL, or can an LCL have a superpolynomial separation?

**Context.** Consider solvable LCLs on finite graphs of fixed bounded degree, with fixed finite input/output alphabets and fixed-radius validity rules. Vertices have polynomial-range unique identifiers and ordered ports; algorithms know n. A graph-oracle probe returns a vertex’s input label, adjacency list and ports. A stateless randomized LCA may probe any identifier and uses a random tape shared across queries. VOLUME instead must grow the probed region connectedly from the queried vertex, and sees only independent random strings attached to probed vertices, consistently shared across queries. Each algorithm’s simultaneously induced labeling must be valid with probability ≥1−1/n. Complexity is maximum probes for one vertex query.

**Source.** Sijin Peng. *New Complexity Classes in Locally Checkable Labeling for Local Computation Algorithms*. 2026. [primary source](https://arxiv.org/abs/2607.09626) Location: Question 58.

**Literature check.** Status: No later version, resolution or matching claim found through 10 October 2026.


<a id="q3918"></a>

## Q3918. With nonnegative rational edge weights, is maximizing the weight of a triangle-free 2-matching…

**Status:** Open · **Kind:** open problem · **Collection** 40

With nonnegative rational edge weights, is maximizing the weight of a triangle-free 2-matching polynomial-time solvable, or NP-hard?

**Context.** A 2-matching is an edge subset M of a finite simple undirected graph with every vertex having degree at most two in M.

**Source.** Miguel Bosch Calvo. *Approximation Algorithms for Connectivity Problems*. Università della Svizzera italiana, 2026. Advisor(s): Fabrizio Grandoni. [primary source](https://sonar.rero.ch/documents/334875/files/2026INF002.pdf) Location: Older problems restated in Chapter 6, printed page 123, items 1, 2, 4 and 7.

**Literature check.** Status: No resolution found through 10 October 2026. The 2026 weighted PTAS does not settle exact complexity; the September journal final retains Q3919.

**Further links.** [1](https://doi.org/10.1007/978-3-032-28691-8_2) · [2](https://doi.org/10.1007/s10107-026-02419-0)


<a id="q3919"></a>

## Q3919. Is maximizing |M| subject to M containing neither a 3-cycle nor a 4-cycle polynomial-time…

**Status:** Open · **Kind:** open problem · **Collection** 40

Is maximizing |M| subject to M containing neither a 3-cycle nor a 4-cycle polynomial-time solvable, or NP-hard?

**Context.** A 2-matching is an edge subset M of a finite simple undirected graph with every vertex having degree at most two in M.

**Source.** Miguel Bosch Calvo. *Approximation Algorithms for Connectivity Problems*. Università della Svizzera italiana, 2026. Advisor(s): Fabrizio Grandoni. [primary source](https://sonar.rero.ch/documents/334875/files/2026INF002.pdf) Location: Older problems restated in Chapter 6, printed page 123, items 1, 2, 4 and 7.

**Literature check.** Status: No resolution found through 10 October 2026. The 2026 weighted PTAS does not settle exact complexity; the September journal final retains Q3919.

**Further links.** [1](https://doi.org/10.1007/978-3-032-28691-8_2) · [2](https://doi.org/10.1007/s10107-026-02419-0)


<a id="q3920"></a>

## Q3920. Does some constant ε>0 permit a polynomial-time (8/7−ε)-approximation for minimum-weight…

**Status:** Open · **Kind:** open problem · **Collection** 40

Does some constant ε>0 permit a polynomial-time (8/7−ε)-approximation for minimum-weight Hamiltonian cycle in complete undirected graphs on at least three vertices with edge weights in {1,2}?

**Context.** A 2-matching is an edge subset M of a finite simple undirected graph with every vertex having degree at most two in M.

**Source.** Miguel Bosch Calvo. *Approximation Algorithms for Connectivity Problems*. Università della Svizzera italiana, 2026. Advisor(s): Fabrizio Grandoni. [primary source](https://sonar.rero.ch/documents/334875/files/2026INF002.pdf) Location: Older problems restated in Chapter 6, printed page 123, items 1, 2, 4 and 7.

**Literature check.** Status: No resolution found through 10 October 2026. The 2026 weighted PTAS does not settle exact complexity; the September journal final retains Q3919.

**Further links.** [1](https://doi.org/10.1007/978-3-032-28691-8_2) · [2](https://doi.org/10.1007/s10107-026-02419-0)


<a id="q3921"></a>

## Q3921. Does some constant ε>0 permit a polynomial-time (2−ε)-approximation for a minimum-weight…

**Status:** Open · **Kind:** open problem · **Collection** 40

Does some constant ε>0 permit a polynomial-time (2−ε)-approximation for a minimum-weight 2-edge-connected spanning subgraph of an arbitrary finite simple 2-edge-connected graph with nonnegative rational edge weights? Each input edge may be selected only once; 2-edge-connected means remaining connected after deletion of any one edge.

**Context.** A 2-matching is an edge subset M of a finite simple undirected graph with every vertex having degree at most two in M.

**Source.** Miguel Bosch Calvo. *Approximation Algorithms for Connectivity Problems*. Università della Svizzera italiana, 2026. Advisor(s): Fabrizio Grandoni. [primary source](https://sonar.rero.ch/documents/334875/files/2026INF002.pdf) Location: Older problems restated in Chapter 6, printed page 123, items 1, 2, 4 and 7.

**Literature check.** Status: No resolution found through 10 October 2026. The 2026 weighted PTAS does not settle exact complexity; the September journal final retains Q3919.

**Further links.** [1](https://doi.org/10.1007/978-3-032-28691-8_2) · [2](https://doi.org/10.1007/s10107-026-02419-0)


<a id="q3924"></a>

## Q3924. For integers n,k,b≥2, must every linearizable, nondeterministic solo-terminating n-process…

**Status:** Open · **Kind:** open problem · **Collection** 40

For integers n,k,b≥2, must every linearizable, nondeterministic solo-terminating n-process implementation of a scannable object with k fully reusable b-state components use at least k+ceil(n/(b−1)) b-state base objects?

**Context.** A scannable object has k components, each supporting a read of its full state: Apply(i,op) invokes a component operation; Scan returns their entire state vector atomically. A component is fully reusable if every state can reach every other by operations. All n processes may apply and scan. Base objects are atomic deterministic state machines; their domain sizes count their complete states, including auxiliary information. Here solo-termination means that from every reachable configuration, each process with an unfinished operation has some finite solo execution completing it. Linearizability requires operations to behave as an atomic sequential execution respecting real-time precedence.

**Source.** Sean Garnet Ovens. *The Space Complexity of Asynchronous Algorithms from Bounded Size Base Objects*. University of Toronto, 2023. Advisor(s): Faith Ellen. [primary source](https://utoronto.scholaris.ca/bitstreams/b8edd80a-a35f-47d6-944c-cc2f4ebf045a/download) Location: Thesis conjecture, printed page 72.

**Literature check.** Status: No resolution or matching claim found through 10 October 2026. This is the thesis’s strengthened conjecture, not the earlier DISC 2022 bound; restricting to a single updater invalidates it.

**Further links.** [1](https://doi.org/10.4230/LIPIcs.DISC.2022.30) · [2](https://www.podc.org/2025-principles-of-distributed-computing-doctoral-dissertation-award/) · [3](https://www.seanovens.com/uploads/CV_Sean_Ovens.pdf)


<a id="q3925"></a>

## Q3925. For every fixed d≥2 and ε>0, is there a polynomial-time (d+ε)-approximation for the…

**Status:** Open · **Kind:** open problem · **Collection** 40

For every fixed d≥2 and ε>0, is there a polynomial-time (d+ε)-approximation for the maximum-cardinality independent set of d-oriented polygons?

**Context.** For d≥2, d-oriented polygons are bounded convex planar polygons with nonempty interiors whose edges follow a common supplied set of d pairwise nonparallel integer-vector directions, with rational half-plane descriptions. Independent polygons have disjoint interiors; boundary touching is allowed. Origin: Q3925 is proposed as a follow-up improvement; Q3926 is an older barrier restated in the dissertation. Polynomial time refers to binary input size. The polygon model permits boundary touching; the segment problem requires disjoint sets.

**Source.** Antoine Tinguely. *Approximating Packing Problems*. Università della Svizzera italiana, 2025. Advisor(s): Fabrizio Grandoni. [primary source](https://sonar.ch/documents/333906/files/2025INF016.pdf) Location: Thesis §5.2, printed page 152.

**Literature check.** Status: No resolution found through 10 October 2026. September’s segment hitting-set final explicitly retains the independent-set factor-two barrier.

**Further links.** [1](https://doi.org/10.4230/LIPIcs.SoCG.2024.61) · [2](https://doi.org/10.20382/jocg.v14i1a5) · [3](https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2026.14) · [4](https://www.inf.usi.ch/en/node/11454)


<a id="q3926"></a>

## Q3926. Does some constant ε>0 permit a polynomial-time (2−ε)-approximation for a maximum-total-weight…

**Status:** Open · **Kind:** open problem · **Collection** 40

Does some constant ε>0 permit a polynomial-time (2−ε)-approximation for a maximum-total-weight pairwise-disjoint subfamily of finitely many nondegenerate closed horizontal and vertical line segments with rational endpoints and positive rational weights?

**Context.** For d≥2, d-oriented polygons are bounded convex planar polygons with nonempty interiors whose edges follow a common supplied set of d pairwise nonparallel integer-vector directions, with rational half-plane descriptions. Independent polygons have disjoint interiors; boundary touching is allowed. Origin: Q3925 is proposed as a follow-up improvement; Q3926 is an older barrier restated in the dissertation. Polynomial time refers to binary input size. The polygon model permits boundary touching; the segment problem requires disjoint sets.

**Source.** Antoine Tinguely. *Approximating Packing Problems*. Università della Svizzera italiana, 2025. Advisor(s): Fabrizio Grandoni. [primary source](https://sonar.ch/documents/333906/files/2025INF016.pdf) Location: Thesis §5.2, printed page 152.

**Literature check.** Status: No resolution found through 10 October 2026. September’s segment hitting-set final explicitly retains the independent-set factor-two barrier.

**Further links.** [1](https://doi.org/10.4230/LIPIcs.SoCG.2024.61) · [2](https://doi.org/10.20382/jocg.v14i1a5) · [3](https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2026.14) · [4](https://www.inf.usi.ch/en/node/11454)


<a id="q3927"></a>

## Q3927. Is there a polynomial-time constant-factor approximation for this problem on arbitrary inputs,…

**Status:** Open · **Kind:** open problem · **Collection** 40

Is there a polynomial-time constant-factor approximation for this problem on arbitrary inputs, without increasing any edge capacity?

**Context.** An input is a finite m-edge path with positive integer capacities u(e), and tasks i with positive integer profit w_i, demand d_i, processing length 1≤p_i≤m, and a contiguous window W_i of at least p_i edges. A selected task occupies p_i consecutive edges within W_i, without preemption. On each edge, total selected demand cannot exceed u(e); maximize total selected profit.

**Source.** Alexander Armbruster, Fabrizio Grandoni, Edin Husić, Antoine Tinguely and Andreas Wiese. *On the Approximability of Unsplittable Flow on a Path with Time Windows*. 2026. [primary source](https://doi.org/10.1007/s10107-026-02408-3) Location: Explicit open problem in final §1.1 after Theorem 3.

**Literature check.** Status: Origin and status: Explicit open problem in final §1.1 after Theorem 3. Its quasi-polynomial (2+ε)-approximation permits capacity augmentation and therefore does not answer this question. No later correction, resolution or matching claim was found through 10 October 2026. Runtime is polynomial in the binary-encoded input length, including the explicitly listed path.


<a id="q3929"></a>

## Q3929. For q=2 and |R|≤3, is this optimization problem polynomial-time solvable or NP-hard?

**Status:** Open · **Kind:** open problem · **Collection** 40

For q=2 and |R|≤3, is this optimization problem polynomial-time solvable or NP-hard?

**Context.** Given a finite undirected graph J with nonnegative rational edge costs and a specified terminal set R, seek a minimum-cost subgraph H in which every two distinct terminals have at least q edge-disjoint connecting paths. Each available edge may be purchased once; vertices outside R may be used freely. Infeasibility can be reported. Polynomial time refers to the complete binary-encoded input. Origin: The thesis restates the complexity questions from joint work with Michael Dinitz, Guy Kortsarz and Zeev Nutov. The known factor-two approximation for survivable network design does not give exact algorithms. Later relative-connectivity algorithms and hardness results do not classify these ordinary fixed-demand problems. No resolution or matching claim found through 10 October 2026.

**Source.** Ama Koranteng. *Approximation Algorithms for New Problems in Network Design*. Johns Hopkins University, 2025. Advisor(s): Michael Dinitz. [primary source](https://jscholarship.library.jhu.edu/bitstreams/1462afa3-e477-40bb-8dd7-a399f6447c6e/download) Location: Thesis §3.4.1, pages 47–48.

**Literature check.** Status: Origin: The thesis restates the complexity questions from joint work with Michael Dinitz, Guy Kortsarz and Zeev Nutov. The known factor-two approximation for survivable network design does not give exact algorithms. Later relative-connectivity algorithms and hardness results do not classify these ordinary fixed-demand problems. No resolution or matching claim found through 10 October 2026.

**Further links.** [1](https://doi.org/10.1007/978-3-031-49815-2_14) · [2](https://amakora0.github.io/) · [3](https://doi.org/10.4230/LIPIcs.ESA.2025.38)


<a id="q3930"></a>

## Q3930. For q=3 and |R|≤4, is this optimization problem polynomial-time solvable or NP-hard?

**Status:** Open · **Kind:** open problem · **Collection** 40

For q=3 and |R|≤4, is this optimization problem polynomial-time solvable or NP-hard?

**Context.** Given a finite undirected graph J with nonnegative rational edge costs and a specified terminal set R, seek a minimum-cost subgraph H in which every two distinct terminals have at least q edge-disjoint connecting paths. Each available edge may be purchased once; vertices outside R may be used freely. Infeasibility can be reported. Polynomial time refers to the complete binary-encoded input. Origin: The thesis restates the complexity questions from joint work with Michael Dinitz, Guy Kortsarz and Zeev Nutov. The known factor-two approximation for survivable network design does not give exact algorithms. Later relative-connectivity algorithms and hardness results do not classify these ordinary fixed-demand problems. No resolution or matching claim found through 10 October 2026.

**Source.** Ama Koranteng. *Approximation Algorithms for New Problems in Network Design*. Johns Hopkins University, 2025. Advisor(s): Michael Dinitz. [primary source](https://jscholarship.library.jhu.edu/bitstreams/1462afa3-e477-40bb-8dd7-a399f6447c6e/download) Location: Thesis §3.4.1, pages 47–48.

**Literature check.** Status: Origin: The thesis restates the complexity questions from joint work with Michael Dinitz, Guy Kortsarz and Zeev Nutov. The known factor-two approximation for survivable network design does not give exact algorithms. Later relative-connectivity algorithms and hardness results do not classify these ordinary fixed-demand problems. No resolution or matching claim found through 10 October 2026.

**Further links.** [1](https://doi.org/10.1007/978-3-031-49815-2_14) · [2](https://amakora0.github.io/) · [3](https://doi.org/10.4230/LIPIcs.ESA.2025.38)


<a id="q4002"></a>

## Q4002. Can |F_C(n,k)| for edgeless C be computed exactly in 2^{O(k²)}n^{O(1)} time?

**Status:** Open · **Kind:** open problem · **Collection** 41

Can |F_C(n,k)| for edgeless C be computed exactly in 2^{O(k²)}n^{O(1)} time?

**Context.** Input: integers n≥1 and 0≤k≤n. Let F_C(n,k) contain the simple graphs on [n] admitting deletion of at most k vertices into class C. Count each graph once, regardless of deletion sets. FPT means f(k)n^{O(1)} time for computable f; counting is deterministic, sampling expected-time. Origin: Thesis residuals; no resolution found through 2026-10-10.

**Source.** Úrsula Hébert-Johnson. *Efficient Algorithms for Graph Counting and Sampling from a Parameterized Perspective*. University of California, Santa Barbara, 2025. Advisor(s): Daniel Lokshtanov. [primary source](https://escholarship.org/uc/item/9646w20k) Location: Thesis §5.3, pages 222–223.

**Literature check.** Status: Origin: Thesis residuals; no resolution found through 2026-10-10.

**Further links.** [1](https://sites.cs.ucsb.edu/~daniello/students.html)


<a id="q4003"></a>

## Q4003. Can |F_C(n,k)| be computed exactly in FPT time for cographs (no induced four-vertex path)?

**Status:** Open · **Kind:** open problem · **Collection** 41

Can |F_C(n,k)| be computed exactly in FPT time for cographs (no induced four-vertex path)?

**Context.** Input: integers n≥1 and 0≤k≤n. Let F_C(n,k) contain the simple graphs on [n] admitting deletion of at most k vertices into class C. Count each graph once, regardless of deletion sets. FPT means f(k)n^{O(1)} time for computable f; counting is deterministic, sampling expected-time. Origin: Thesis residuals; no resolution found through 2026-10-10.

**Source.** Úrsula Hébert-Johnson. *Efficient Algorithms for Graph Counting and Sampling from a Parameterized Perspective*. University of California, Santa Barbara, 2025. Advisor(s): Daniel Lokshtanov. [primary source](https://escholarship.org/uc/item/9646w20k) Location: Thesis §5.3, pages 222–223.

**Literature check.** Status: Origin: Thesis residuals; no resolution found through 2026-10-10.

**Further links.** [1](https://sites.cs.ucsb.edu/~daniello/students.html)


<a id="q4004"></a>

## Q4004. Can |F_C(n,k)| be computed exactly in FPT time for forests?

**Status:** Open · **Kind:** open problem · **Collection** 41

Can |F_C(n,k)| be computed exactly in FPT time for forests?

**Context.** Input: integers n≥1 and 0≤k≤n. Let F_C(n,k) contain the simple graphs on [n] admitting deletion of at most k vertices into class C. Count each graph once, regardless of deletion sets. FPT means f(k)n^{O(1)} time for computable f; counting is deterministic, sampling expected-time. Origin: Thesis residuals; no resolution found through 2026-10-10.

**Source.** Úrsula Hébert-Johnson. *Efficient Algorithms for Graph Counting and Sampling from a Parameterized Perspective*. University of California, Santa Barbara, 2025. Advisor(s): Daniel Lokshtanov. [primary source](https://escholarship.org/uc/item/9646w20k) Location: Thesis §5.3, pages 222–223.

**Literature check.** Status: Origin: Thesis residuals; no resolution found through 2026-10-10.

**Further links.** [1](https://sites.cs.ucsb.edu/~daniello/students.html)


<a id="q4005"></a>

## Q4005. Is exact uniform sampling from F_C(n,k) FPT when C consists of disjoint unions of cliques?

**Status:** Open · **Kind:** open problem · **Collection** 41

Is exact uniform sampling from F_C(n,k) FPT when C consists of disjoint unions of cliques?

**Context.** Input: integers n≥1 and 0≤k≤n. Let F_C(n,k) contain the simple graphs on [n] admitting deletion of at most k vertices into class C. Count each graph once, regardless of deletion sets. FPT means f(k)n^{O(1)} time for computable f; counting is deterministic, sampling expected-time. Origin: Thesis residuals; no resolution found through 2026-10-10.

**Source.** Úrsula Hébert-Johnson. *Efficient Algorithms for Graph Counting and Sampling from a Parameterized Perspective*. University of California, Santa Barbara, 2025. Advisor(s): Daniel Lokshtanov. [primary source](https://escholarship.org/uc/item/9646w20k) Location: Thesis §5.3, pages 222–223.

**Literature check.** Status: Origin: Thesis residuals; no resolution found through 2026-10-10.

**Further links.** [1](https://sites.cs.ucsb.edu/~daniello/students.html)


<a id="q4006"></a>

## Q4006. Is exact uniform sampling from F_C(n,k) FPT when C consists of split graphs, partitionable into…

**Status:** Open · **Kind:** open problem · **Collection** 41

Is exact uniform sampling from F_C(n,k) FPT when C consists of split graphs, partitionable into a clique and an independent set?

**Context.** Input: integers n≥1 and 0≤k≤n. Let F_C(n,k) contain the simple graphs on [n] admitting deletion of at most k vertices into class C. Count each graph once, regardless of deletion sets. FPT means f(k)n^{O(1)} time for computable f; counting is deterministic, sampling expected-time. Origin: Thesis residuals; no resolution found through 2026-10-10.

**Source.** Úrsula Hébert-Johnson. *Efficient Algorithms for Graph Counting and Sampling from a Parameterized Perspective*. University of California, Santa Barbara, 2025. Advisor(s): Daniel Lokshtanov. [primary source](https://escholarship.org/uc/item/9646w20k) Location: Thesis §5.3, pages 222–223.

**Literature check.** Status: Origin: Thesis residuals; no resolution found through 2026-10-10.

**Further links.** [1](https://sites.cs.ucsb.edu/~daniello/students.html)


<a id="q4007"></a>

## Q4007. Is exact uniform sampling FPT for tournaments on [n] that become acyclic after deleting at most…

**Status:** Open · **Kind:** open problem · **Collection** 41

Is exact uniform sampling FPT for tournaments on [n] that become acyclic after deleting at most k vertices?

**Context.** Input: integers n≥1 and 0≤k≤n. Let F_C(n,k) contain the simple graphs on [n] admitting deletion of at most k vertices into class C. Count each graph once, regardless of deletion sets. FPT means f(k)n^{O(1)} time for computable f; counting is deterministic, sampling expected-time. Origin: Thesis residuals; no resolution found through 2026-10-10.

**Source.** Úrsula Hébert-Johnson. *Efficient Algorithms for Graph Counting and Sampling from a Parameterized Perspective*. University of California, Santa Barbara, 2025. Advisor(s): Daniel Lokshtanov. [primary source](https://escholarship.org/uc/item/9646w20k) Location: Thesis §5.3, pages 222–223.

**Literature check.** Status: Origin: Thesis residuals; no resolution found through 2026-10-10.

**Further links.** [1](https://sites.cs.ucsb.edu/~daniello/students.html)


<a id="q4008"></a>

## Q4008. Is there an exact uniform sampler and an absolute constant C such that, for every n≥1 and every…

**Status:** Open · **Kind:** open problem · **Collection** 41

Is there an exact uniform sampler and an absolute constant C such that, for every n≥1 and every G∈U_n, E[T_n|X_n=G]≤n^C+C?

**Context.** A chordal graph is a finite simple graph with no induced cycle of length at least four. Let U_n be its n-vertex isomorphism classes. An unlabeled sampler outputs a representative, with every class receiving probability 1/|U_n|, rather than assigning equal probability to all labeled graphs. Let T_n be its running time and X_n its output class.

**Source.** Úrsula Hébert-Johnson and Daniel Lokshtanov. *Sampling Unlabeled Chordal Graphs in Expected Polynomial Time*. 2025. [primary source](https://doi.org/10.4230/LIPIcs.STACS.2025.46) Location: Explicit residual in final §5, page 46:19.

**Literature check.** Status: Origin and status: Explicit residual in final §5, page 46:19. The established algorithm bounds unconditional expected time only. Sun’s July 2026 exact enumeration has a subexponential, explicitly non-polynomial bound and does not provide this conditional runtime guarantee. No matching resolution found through 2026-10-10.

**Further links.** [1](https://arxiv.org/abs/2607.02613)


<a id="q4010"></a>

## Q4010. Is this problem FPT parameterized by k, or W[1]-hard?

**Status:** Open · **Kind:** open problem · **Collection** 41

Is this problem FPT parameterized by k, or W[1]-hard?

**Context.** Input is a finite simple unweighted undirected graph G on n vertices and 1≤k≤n. Decide whether V(G) partitions into k nonempty paths, each shortest between its endpoints in G; singleton paths are allowed. FPT for parameter p means time f(p)n^{O(1)}, for computable f. A tree decomposition is a tree of vertex bags covering all vertices and edges, with the bags containing each vertex connected. Treewidth minimizes the largest bag size minus one.

**Source.** Dibyayan Chakraborty, Oscar Defrain, Florent Foucaud, Mathieu Mari and Prafullkumar Tale. *Parameterized Complexity of Isometric Path Partition: Treewidth and Diameter*. 2026. [primary source](https://doi.org/10.4230/LIPIcs.WG.2026.11) Location: Final §6, page 11:14, poses both residuals.

**Literature check.** Status: Origin and status: Final §6, page 11:14, poses both residuals. These are paper-origin questions, not attributed to the dissertation. The paper's hardness for unrestricted treewidth does not resolve either. No later resolution found through 10 October 2026.

**Further links.** [1](https://dibyayancg.github.io/Research/thesis.pdf) · [2](https://dibyayancg.github.io/index.html)


<a id="q4011"></a>

## Q4011. On planar graphs, is this problem FPT parameterized by treewidth?

**Status:** Open · **Kind:** open problem · **Collection** 41

On planar graphs, is this problem FPT parameterized by treewidth?

**Context.** Input is a finite simple unweighted undirected graph G on n vertices and 1≤k≤n. Decide whether V(G) partitions into k nonempty paths, each shortest between its endpoints in G; singleton paths are allowed. FPT for parameter p means time f(p)n^{O(1)}, for computable f. A tree decomposition is a tree of vertex bags covering all vertices and edges, with the bags containing each vertex connected. Treewidth minimizes the largest bag size minus one.

**Source.** Dibyayan Chakraborty, Oscar Defrain, Florent Foucaud, Mathieu Mari and Prafullkumar Tale. *Parameterized Complexity of Isometric Path Partition: Treewidth and Diameter*. 2026. [primary source](https://doi.org/10.4230/LIPIcs.WG.2026.11) Location: Final §6, page 11:14, poses both residuals.

**Literature check.** Status: Origin and status: Final §6, page 11:14, poses both residuals. These are paper-origin questions, not attributed to the dissertation. The paper's hardness for unrestricted treewidth does not resolve either. No later resolution found through 10 October 2026.

**Further links.** [1](https://dibyayancg.github.io/Research/thesis.pdf) · [2](https://dibyayancg.github.io/index.html)


<a id="q4012"></a>

## Q4012. For each n≥3, find an explicit finite presentation of CT(n) using these circuit generators:…

**Status:** Open · **Kind:** open problem · **Collection** 41

For each n≥3, find an explicit finite presentation of CT(n) using these circuit generators: finitely many valid equations from which every equality of generator words follows.

**Context.** Put ω=exp(iπ/4), H=2^(−1/2)[[1,1],[1,−1]], T=diag(1,ω), S=T² and CZ=diag(1,1,1,−1). Let CT(n)≤U(2^n) be generated by these one- and two-qubit gates on any wires, together with ωI. Equality retains global phase; auxiliary qubits are not allowed.

**Source.** Xiaoning Bian. *Generators and Relations for Some Classes of Quantum Circuits*. Dalhousie University, 2023. Advisor(s): Peter Selinger. [primary source](https://www.mathstat.dal.ca/~xbian/thesis/thesis.pdf) Location: Chapter 6, p.67.

**Literature check.** Status: No resolution found through 10 October 2026. Blake’s FSCD 2026 presentation covers Clifford+T only through two qubits; Clément’s LICS 2026 conclusion still identifies the higher-dimensional presentation obstacle.

**Further links.** [1](https://www.mathstat.dal.ca/~xbian/) · [2](https://doi.org/10.4230/LIPIcs.FSCD.2026.6) · [3](https://doi.org/10.4230/LIPIcs.LICS.2026.28)


<a id="q4030"></a>

## Q4030. Classify the complexity of deciding whether such a path exists for each fixed pair of integers…

**Status:** Open · **Kind:** open problem · **Collection** 41

Classify the complexity of deciding whether such a path exists for each fixed pair of integers k≥4 and 1≤q≤k−3.

**Context.** The input is an explicitly listed finite k-uniform hypergraph H and distinct vertices x,y. A q-linear path is a sequence e₁,…,e_L, L≥1, with 1≤|e_i∩e_(i+1)|≤q, and e_i∩e_j empty whenever |i−j|>1. It joins x to y when x belongs to e₁ only and y to e_L only; a single-edge path containing both is allowed.

**Source.** Florian Galliot, Sylvain Gravier and Isabelle Sivignon. *(k−2)-linear connected components in hypergraphs of rank k*. 2023. [primary source](https://doi.org/10.46298/dmtcs.10202) Location: §6, p.30.

**Literature check.** Status: The final solves q=k−2; q=k−1 is ordinary connectivity. No resolution of the remaining parameter range found through 10 October 2026.


<a id="q4148"></a>

## Q4148. For each fixed integer g≥5, classify Injective Colouring on graphs of girth≥g, both with input k…

**Status:** Open · **Kind:** open problem · **Collection** 42

For each fixed integer g≥5, classify Injective Colouring on graphs of girth≥g, both with input k and with each fixed k≥4.

**Context.** Doctoral context: Siani Alice Smith, Graph Partitioning With Input Restrictions, Durham University, January 2022; PhD in Computer Science. Supervisors: Barnaby Martin (Director of Studies) and Daniël Paulusma (second supervisor). Durham lists her doctoral study as completed in 2022. The questions below retain their actual joint-paper origins. Sources: https://etheses.durham.ac.uk/id/eprint/14442/ ; https://durham-repository.worktribe.com/person/211543/barnaby-martin/supervisions Graphs are finite and simple; colourings are proper (adjacent vertices differ). Acyclic, star and injective colourings require every two colour classes to induce, respectively, a forest, disjoint stars, or a matching plus isolated vertices. Decide existence with at most k colours. H-free excludes induced H; P_n is the n-vertex path; + denotes disjoint union. Girth is shortest-cycle length, or ∞ for forests. Origin: Joint-paper residuals; no resolution found through 10 October 2026.

**Source.** Jan Bok, Nikola Jedličková, Barnaby Martin, Pascal Ochem, Daniël Paulusma and Siani Smith. *Acyclic, Star and Injective Colouring: A Complexity Picture for H-Free Graphs*. 2020. [primary source](https://arxiv.org/abs/2008.09415v6) Location: §6, Problems 1–4, pp.21–22.

**Literature check.** Status: Origin: Joint-paper residuals; no resolution found through 10 October 2026.

**Further links.** [1](https://etheses.durham.ac.uk/id/eprint/14442/) · [2](https://durham-repository.worktribe.com/person/211543/barnaby-martin/supervisions)


<a id="q4149"></a>

## Q4149. For each fixed integer g≥5 and k≥4, classify Star k-Colouring on graphs of girth≥g.

**Status:** Open · **Kind:** open problem · **Collection** 42

For each fixed integer g≥5 and k≥4, classify Star k-Colouring on graphs of girth≥g.

**Context.** Doctoral context: Siani Alice Smith, Graph Partitioning With Input Restrictions, Durham University, January 2022; PhD in Computer Science. Supervisors: Barnaby Martin (Director of Studies) and Daniël Paulusma (second supervisor). Durham lists her doctoral study as completed in 2022. The questions below retain their actual joint-paper origins. Sources: https://etheses.durham.ac.uk/id/eprint/14442/ ; https://durham-repository.worktribe.com/person/211543/barnaby-martin/supervisions Graphs are finite and simple; colourings are proper (adjacent vertices differ). Acyclic, star and injective colourings require every two colour classes to induce, respectively, a forest, disjoint stars, or a matching plus isolated vertices. Decide existence with at most k colours. H-free excludes induced H; P_n is the n-vertex path; + denotes disjoint union. Girth is shortest-cycle length, or ∞ for forests. Origin: Joint-paper residuals; no resolution found through 10 October 2026.

**Source.** Jan Bok, Nikola Jedličková, Barnaby Martin, Pascal Ochem, Daniël Paulusma and Siani Smith. *Acyclic, Star and Injective Colouring: A Complexity Picture for H-Free Graphs*. 2020. [primary source](https://arxiv.org/abs/2008.09415v6) Location: §6, Problems 1–4, pp.21–22.

**Literature check.** Status: Origin: Joint-paper residuals; no resolution found through 10 October 2026.

**Further links.** [1](https://etheses.durham.ac.uk/id/eprint/14442/) · [2](https://durham-repository.worktribe.com/person/211543/barnaby-martin/supervisions)


<a id="q4150"></a>

## Q4150. Classify Injective Colouring with input k on (2P₁+P₄)-free graphs.

**Status:** Open · **Kind:** open problem · **Collection** 42

Classify Injective Colouring with input k on (2P₁+P₄)-free graphs.

**Context.** Doctoral context: Siani Alice Smith, Graph Partitioning With Input Restrictions, Durham University, January 2022; PhD in Computer Science. Supervisors: Barnaby Martin (Director of Studies) and Daniël Paulusma (second supervisor). Durham lists her doctoral study as completed in 2022. The questions below retain their actual joint-paper origins. Sources: https://etheses.durham.ac.uk/id/eprint/14442/ ; https://durham-repository.worktribe.com/person/211543/barnaby-martin/supervisions Graphs are finite and simple; colourings are proper (adjacent vertices differ). Acyclic, star and injective colourings require every two colour classes to induce, respectively, a forest, disjoint stars, or a matching plus isolated vertices. Decide existence with at most k colours. H-free excludes induced H; P_n is the n-vertex path; + denotes disjoint union. Girth is shortest-cycle length, or ∞ for forests. Origin: Joint-paper residuals; no resolution found through 10 October 2026.

**Source.** Jan Bok, Nikola Jedličková, Barnaby Martin, Pascal Ochem, Daniël Paulusma and Siani Smith. *Acyclic, Star and Injective Colouring: A Complexity Picture for H-Free Graphs*. 2020. [primary source](https://arxiv.org/abs/2008.09415v6) Location: §6, Problems 1–4, pp.21–22.

**Literature check.** Status: Origin: Joint-paper residuals; no resolution found through 10 October 2026.

**Further links.** [1](https://etheses.durham.ac.uk/id/eprint/14442/) · [2](https://durham-repository.worktribe.com/person/211543/barnaby-martin/supervisions)


<a id="q4151"></a>

## Q4151. Classify Acyclic Colouring with input k on 2P₂-free graphs.

**Status:** Open · **Kind:** open problem · **Collection** 42

Classify Acyclic Colouring with input k on 2P₂-free graphs.

**Context.** Doctoral context: Siani Alice Smith, Graph Partitioning With Input Restrictions, Durham University, January 2022; PhD in Computer Science. Supervisors: Barnaby Martin (Director of Studies) and Daniël Paulusma (second supervisor). Durham lists her doctoral study as completed in 2022. The questions below retain their actual joint-paper origins. Sources: https://etheses.durham.ac.uk/id/eprint/14442/ ; https://durham-repository.worktribe.com/person/211543/barnaby-martin/supervisions Graphs are finite and simple; colourings are proper (adjacent vertices differ). Acyclic, star and injective colourings require every two colour classes to induce, respectively, a forest, disjoint stars, or a matching plus isolated vertices. Decide existence with at most k colours. H-free excludes induced H; P_n is the n-vertex path; + denotes disjoint union. Girth is shortest-cycle length, or ∞ for forests. Origin: Joint-paper residuals; no resolution found through 10 October 2026.

**Source.** Jan Bok, Nikola Jedličková, Barnaby Martin, Pascal Ochem, Daniël Paulusma and Siani Smith. *Acyclic, Star and Injective Colouring: A Complexity Picture for H-Free Graphs*. 2020. [primary source](https://arxiv.org/abs/2008.09415v6) Location: §6, Problems 1–4, pp.21–22.

**Literature check.** Status: Origin: Joint-paper residuals; no resolution found through 10 October 2026.

**Further links.** [1](https://etheses.durham.ac.uk/id/eprint/14442/) · [2](https://durham-repository.worktribe.com/person/211543/barnaby-martin/supervisions)


<a id="q4152"></a>

## Q4152. Classify Star Colouring with input k on 2P₂-free graphs.

**Status:** Open · **Kind:** open problem · **Collection** 42

Classify Star Colouring with input k on 2P₂-free graphs.

**Context.** Doctoral context: Siani Alice Smith, Graph Partitioning With Input Restrictions, Durham University, January 2022; PhD in Computer Science. Supervisors: Barnaby Martin (Director of Studies) and Daniël Paulusma (second supervisor). Durham lists her doctoral study as completed in 2022. The questions below retain their actual joint-paper origins. Sources: https://etheses.durham.ac.uk/id/eprint/14442/ ; https://durham-repository.worktribe.com/person/211543/barnaby-martin/supervisions Graphs are finite and simple; colourings are proper (adjacent vertices differ). Acyclic, star and injective colourings require every two colour classes to induce, respectively, a forest, disjoint stars, or a matching plus isolated vertices. Decide existence with at most k colours. H-free excludes induced H; P_n is the n-vertex path; + denotes disjoint union. Girth is shortest-cycle length, or ∞ for forests. Origin: Joint-paper residuals; no resolution found through 10 October 2026.

**Source.** Jan Bok, Nikola Jedličková, Barnaby Martin, Pascal Ochem, Daniël Paulusma and Siani Smith. *Acyclic, Star and Injective Colouring: A Complexity Picture for H-Free Graphs*. 2020. [primary source](https://arxiv.org/abs/2008.09415v6) Location: §6, Problems 1–4, pp.21–22.

**Literature check.** Status: Origin: Joint-paper residuals; no resolution found through 10 October 2026.

**Further links.** [1](https://etheses.durham.ac.uk/id/eprint/14442/) · [2](https://durham-repository.worktribe.com/person/211543/barnaby-martin/supervisions)


<a id="q4153"></a>

## Q4153. Determine the complexity of deciding whether a graph of diameter at most three admits an acyclic…

**Status:** Open · **Kind:** open problem · **Collection** 42

Determine the complexity of deciding whether a graph of diameter at most three admits an acyclic three-colouring.

**Context.** Doctoral context: Siani Alice Smith, Graph Partitioning With Input Restrictions, Durham University, January 2022; PhD in Computer Science. Supervisors: Barnaby Martin (Director of Studies) and Daniël Paulusma (second supervisor). Durham lists her doctoral study as completed in 2022. The questions below retain their actual joint-paper origins. Sources: https://etheses.durham.ac.uk/id/eprint/14442/ ; https://durham-repository.worktribe.com/person/211543/barnaby-martin/supervisions Graphs are finite, simple and connected. A proper three-colouring assigns vertices at most three colours, with adjacent vertices different. It is acyclic if no cycle is two-coloured, and star if no four-vertex path is two-coloured; paths need not be induced. Diameter is maximum vertex distance. Origin: Joint-paper residual classifications. The four star-diameter cases are grouped as one threshold problem, rather than counted separately. No matching later resolution found through 10 October 2026.

**Source.** Christoph Brause, Petr A. Golovach, Barnaby Martin, Pascal Ochem, Daniël Paulusma and Siani Smith. *Acyclic, Star, and Injective Colouring: Bounding the Diameter*. 2022. [primary source](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v29i2p43/pdf/) Location: Theorems 2–3 and following discussion, p.5; §5, p.26.

**Literature check.** Status: Origin: Joint-paper residual classifications. The four star-diameter cases are grouped as one threshold problem, rather than counted separately. No matching later resolution found through 10 October 2026.

**Further links.** [1](https://etheses.durham.ac.uk/id/eprint/14442/) · [2](https://durham-repository.worktribe.com/person/211543/barnaby-martin/supervisions)


<a id="q4154"></a>

## Q4154. For each fixed d∈{4,5,6,7}, determine the complexity of deciding whether a graph of diameter at…

**Status:** Open · **Kind:** open problem · **Collection** 42

For each fixed d∈{4,5,6,7}, determine the complexity of deciding whether a graph of diameter at most d admits a star three-colouring.

**Context.** Doctoral context: Siani Alice Smith, Graph Partitioning With Input Restrictions, Durham University, January 2022; PhD in Computer Science. Supervisors: Barnaby Martin (Director of Studies) and Daniël Paulusma (second supervisor). Durham lists her doctoral study as completed in 2022. The questions below retain their actual joint-paper origins. Sources: https://etheses.durham.ac.uk/id/eprint/14442/ ; https://durham-repository.worktribe.com/person/211543/barnaby-martin/supervisions Graphs are finite, simple and connected. A proper three-colouring assigns vertices at most three colours, with adjacent vertices different. It is acyclic if no cycle is two-coloured, and star if no four-vertex path is two-coloured; paths need not be induced. Diameter is maximum vertex distance. Origin: Joint-paper residual classifications. The four star-diameter cases are grouped as one threshold problem, rather than counted separately. No matching later resolution found through 10 October 2026.

**Source.** Christoph Brause, Petr A. Golovach, Barnaby Martin, Pascal Ochem, Daniël Paulusma and Siani Smith. *Acyclic, Star, and Injective Colouring: Bounding the Diameter*. 2022. [primary source](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v29i2p43/pdf/) Location: Theorems 2–3 and following discussion, p.5; §5, p.26.

**Literature check.** Status: Origin: Joint-paper residual classifications. The four star-diameter cases are grouped as one threshold problem, rather than counted separately. No matching later resolution found through 10 October 2026.

**Further links.** [1](https://etheses.durham.ac.uk/id/eprint/14442/) · [2](https://durham-repository.worktribe.com/person/211543/barnaby-martin/supervisions)


<a id="q4155"></a>

## Q4155. Determine the complexity of Disjoint Paths on 3P₁-free graphs.

**Status:** Open · **Kind:** open problem (Problem 1) · **Collection** 42

Determine the complexity of Disjoint Paths on 3P₁-free graphs.

**Context.** Doctoral context: Siani Alice Smith, Graph Partitioning With Input Restrictions, Durham University, January 2022; PhD in Computer Science. Supervisors: Barnaby Martin (Director of Studies) and Daniël Paulusma (second supervisor). Durham lists her doctoral study as completed in 2022. The questions below retain their actual joint-paper origins. Sources: https://etheses.durham.ac.uk/id/eprint/14442/ ; https://durham-repository.worktribe.com/person/211543/barnaby-martin/supervisions Graphs are finite, simple and undirected; the positive integer k is part of the input. Disjoint Paths asks, given k pairwise disjoint terminal pairs (s_i,t_i), with s_i≠t_i, for pairwise vertex-disjoint paths joining the prescribed pairs. Disjoint Connected Subgraphs instead receives pairwise disjoint terminal sets Z_i and asks for pairwise vertex-disjoint connected subgraphs containing the respective sets. H-free means no induced H; P_n is an n-vertex path; + denotes disjoint union. Origin: Joint-paper residuals, also Smith’s thesis Problem18. No matching later resolution found through 10 October 2026.

**Source.** Walter Kern, Barnaby Martin, Daniël Paulusma, Siani Smith and Erik Jan van Leeuwen. *Disjoint paths and connected subgraphs for H-free graphs*. 2022. [primary source](https://dspace.library.uu.nl/bitstream/handle/1874/416033/1_s2.0_S0304397521006344_main.pdf?sequence=1) Location: §7, Open Problem 1, p.67; also Smith’s thesis Problem 18

**Literature check.** Status: Origin: Joint-paper residuals, also Smith’s thesis Problem18. No matching later resolution found through 10 October 2026.

**Further links.** [1](https://etheses.durham.ac.uk/id/eprint/14442/) · [2](https://durham-repository.worktribe.com/person/211543/barnaby-martin/supervisions)


<a id="q4156"></a>

## Q4156. Determine the complexity of Disjoint Paths on (2P₁+P₂)-free graphs.

**Status:** Open · **Kind:** open problem (Problem 1) · **Collection** 42

Determine the complexity of Disjoint Paths on (2P₁+P₂)-free graphs.

**Context.** Doctoral context: Siani Alice Smith, Graph Partitioning With Input Restrictions, Durham University, January 2022; PhD in Computer Science. Supervisors: Barnaby Martin (Director of Studies) and Daniël Paulusma (second supervisor). Durham lists her doctoral study as completed in 2022. The questions below retain their actual joint-paper origins. Sources: https://etheses.durham.ac.uk/id/eprint/14442/ ; https://durham-repository.worktribe.com/person/211543/barnaby-martin/supervisions Graphs are finite, simple and undirected; the positive integer k is part of the input. Disjoint Paths asks, given k pairwise disjoint terminal pairs (s_i,t_i), with s_i≠t_i, for pairwise vertex-disjoint paths joining the prescribed pairs. Disjoint Connected Subgraphs instead receives pairwise disjoint terminal sets Z_i and asks for pairwise vertex-disjoint connected subgraphs containing the respective sets. H-free means no induced H; P_n is an n-vertex path; + denotes disjoint union. Origin: Joint-paper residuals, also Smith’s thesis Problem18. No matching later resolution found through 10 October 2026.

**Source.** Walter Kern, Barnaby Martin, Daniël Paulusma, Siani Smith and Erik Jan van Leeuwen. *Disjoint paths and connected subgraphs for H-free graphs*. 2022. [primary source](https://dspace.library.uu.nl/bitstream/handle/1874/416033/1_s2.0_S0304397521006344_main.pdf?sequence=1) Location: §7, Open Problem 1, p.67; also Smith’s thesis Problem 18

**Literature check.** Status: Origin: Joint-paper residuals, also Smith’s thesis Problem18. No matching later resolution found through 10 October 2026.

**Further links.** [1](https://etheses.durham.ac.uk/id/eprint/14442/) · [2](https://durham-repository.worktribe.com/person/211543/barnaby-martin/supervisions)


<a id="q4157"></a>

## Q4157. Determine the complexity of Disjoint Connected Subgraphs on (2P₁+P₂)-free graphs.

**Status:** Open · **Kind:** open problem (Problem 1) · **Collection** 42

Determine the complexity of Disjoint Connected Subgraphs on (2P₁+P₂)-free graphs.

**Context.** Doctoral context: Siani Alice Smith, Graph Partitioning With Input Restrictions, Durham University, January 2022; PhD in Computer Science. Supervisors: Barnaby Martin (Director of Studies) and Daniël Paulusma (second supervisor). Durham lists her doctoral study as completed in 2022. The questions below retain their actual joint-paper origins. Sources: https://etheses.durham.ac.uk/id/eprint/14442/ ; https://durham-repository.worktribe.com/person/211543/barnaby-martin/supervisions Graphs are finite, simple and undirected; the positive integer k is part of the input. Disjoint Paths asks, given k pairwise disjoint terminal pairs (s_i,t_i), with s_i≠t_i, for pairwise vertex-disjoint paths joining the prescribed pairs. Disjoint Connected Subgraphs instead receives pairwise disjoint terminal sets Z_i and asks for pairwise vertex-disjoint connected subgraphs containing the respective sets. H-free means no induced H; P_n is an n-vertex path; + denotes disjoint union. Origin: Joint-paper residuals, also Smith’s thesis Problem18. No matching later resolution found through 10 October 2026.

**Source.** Walter Kern, Barnaby Martin, Daniël Paulusma, Siani Smith and Erik Jan van Leeuwen. *Disjoint paths and connected subgraphs for H-free graphs*. 2022. [primary source](https://dspace.library.uu.nl/bitstream/handle/1874/416033/1_s2.0_S0304397521006344_main.pdf?sequence=1) Location: §7, Open Problem 1, p.67; also Smith’s thesis Problem 18

**Literature check.** Status: Origin: Joint-paper residuals, also Smith’s thesis Problem18. No matching later resolution found through 10 October 2026.

**Further links.** [1](https://etheses.durham.ac.uk/id/eprint/14442/) · [2](https://durham-repository.worktribe.com/person/211543/barnaby-martin/supervisions)


<a id="q4158"></a>

## Q4158. For every fixed nonempty linear forest H and each fixed integer ℓ≥2, is this problem…

**Status:** Open · **Kind:** open problem · **Collection** 42

For every fixed nonempty linear forest H and each fixed integer ℓ≥2, is this problem polynomial-time solvable on H-free graphs when |Z_i|≤ℓ for all i?

**Context.** Doctoral context: Siani Alice Smith, Graph Partitioning With Input Restrictions, Durham University, January 2022; PhD in Computer Science. Supervisors: Barnaby Martin (Director of Studies) and Daniël Paulusma (second supervisor). Durham lists her doctoral study as completed in 2022. The questions below retain their actual joint-paper origins. Sources: https://etheses.durham.ac.uk/id/eprint/14442/ ; https://durham-repository.worktribe.com/person/211543/barnaby-martin/supervisions For finite simple undirected G and pairwise disjoint terminal sets Z₁,…,Z_k, Induced Disjoint Connected Subgraphs asks for vertex sets D_i⊇Z_i such that each G[D_i] is connected, the D_i are pairwise disjoint, and no edge joins distinct D_i. The number k is part of the input. H-free means no induced H; P_n is the n-vertex path; a linear forest is a disjoint union of paths. Origin: Joint-paper residuals. The final gives quasipolynomial algorithms for Q4158 and leaves Q4159 as its single remaining unrestricted-terminal-size case. No matching later resolution found through 10 October 2026.

**Source.** Barnaby Martin, Daniël Paulusma, Siani Smith and Erik Jan van Leeuwen. *Induced Disjoint Paths and Connected Subgraphs for H-Free Graphs*. 2023. [primary source](https://link.springer.com/article/10.1007/s00453-023-01109-z) Location: §7, pp.2602–2603; definitions pp.2581–2582.

**Literature check.** Status: Origin: Joint-paper residuals. The final gives quasipolynomial algorithms for Q4158 and leaves Q4159 as its single remaining unrestricted-terminal-size case. No matching later resolution found through 10 October 2026.

**Further links.** [1](https://etheses.durham.ac.uk/id/eprint/14442/) · [2](https://durham-repository.worktribe.com/person/211543/barnaby-martin/supervisions)


<a id="q4159"></a>

## Q4159. Determine its computational complexity on P₆-free graphs when terminal-set sizes are unbounded.

**Status:** Open · **Kind:** open problem · **Collection** 42

Determine its computational complexity on P₆-free graphs when terminal-set sizes are unbounded.

**Context.** Doctoral context: Siani Alice Smith, Graph Partitioning With Input Restrictions, Durham University, January 2022; PhD in Computer Science. Supervisors: Barnaby Martin (Director of Studies) and Daniël Paulusma (second supervisor). Durham lists her doctoral study as completed in 2022. The questions below retain their actual joint-paper origins. Sources: https://etheses.durham.ac.uk/id/eprint/14442/ ; https://durham-repository.worktribe.com/person/211543/barnaby-martin/supervisions For finite simple undirected G and pairwise disjoint terminal sets Z₁,…,Z_k, Induced Disjoint Connected Subgraphs asks for vertex sets D_i⊇Z_i such that each G[D_i] is connected, the D_i are pairwise disjoint, and no edge joins distinct D_i. The number k is part of the input. H-free means no induced H; P_n is the n-vertex path; a linear forest is a disjoint union of paths. Origin: Joint-paper residuals. The final gives quasipolynomial algorithms for Q4158 and leaves Q4159 as its single remaining unrestricted-terminal-size case. No matching later resolution found through 10 October 2026.

**Source.** Barnaby Martin, Daniël Paulusma, Siani Smith and Erik Jan van Leeuwen. *Induced Disjoint Paths and Connected Subgraphs for H-Free Graphs*. 2023. [primary source](https://link.springer.com/article/10.1007/s00453-023-01109-z) Location: §7, pp.2602–2603; definitions pp.2581–2582.

**Literature check.** Status: Origin: Joint-paper residuals. The final gives quasipolynomial algorithms for Q4158 and leaves Q4159 as its single remaining unrestricted-terminal-size case. No matching later resolution found through 10 October 2026.

**Further links.** [1](https://etheses.durham.ac.uk/id/eprint/14442/) · [2](https://durham-repository.worktribe.com/person/211543/barnaby-martin/supervisions)


<a id="q4160"></a>

## Q4160. For each fixed connected non-bipartite H, determine a constant c_H permitting c_H^w n^{O(1)}…

**Status:** Open · **Kind:** open problem (Problem 1) · **Collection** 42

For each fixed connected non-bipartite H, determine a constant c_H permitting c_H^w n^{O(1)} time for Hom(H), given n-vertex G and a width-w ordering, while SETH excludes (c_H−ε)^w n^{O(1)} time for every 0<ε&lt;c_H.

**Context.** Marta Piecyk’s doctoral route: Graph Homomorphisms – Exploring the Boundaries of Tractability, Warsaw University of Technology, 2024 PhD dissertation in mathematics; supervisors Zbigniew Lonc and Paweł Rzążewski. Degree award unverified. Q4160 restates thesis Open Problem 1, p.18; subsequent questions follow her publication network. Field: Graph algorithms and matrix invariants. SETH denotes the Strong Exponential Time Hypothesis. Graphs are finite, simple, undirected. Hom(H) decides existence of an edge-preserving map G→H. An ordering’s width w is the maximum number of edges crossing a prefix cut. For finite square 0–1 matrices A, mim(A) is the largest order of a permutation submatrix, and him(A) that of a triangular submatrix with diagonal 1; rows/columns may be permuted independently. Put mimsup(A)=sup_{r≥1}mim(A^{⊗r})^{1/r}, using Kronecker powers. Joint-paper questions: Open Problem 1, p.77:3; §6, p.77:17. No resolution found through 10 October 2026.

**Source.** Carla Groenland, Isja Mannens, Jesper Nederlof, Marta Piecyk and Paweł Rzążewski. *ICALP 2024, Article 77 (title not given in the supplied text)*. 2024. [primary source](https://doi.org/10.4230/LIPIcs.ICALP.2024.77) Location: Open Problem 1, p.77:3; §6, p.77:17.

**Literature check.** Status: Joint-paper questions: Open Problem 1, p.77:3; §6, p.77:17. No resolution found through 10 October 2026.

**Further links.** [1](https://www.bip.pw.edu.pl/index.php/content/download/74183/706088/file/M.PIECYK_phd-main.pdf)


<a id="q4161"></a>

## Q4161. Can mimsup(A) be nonintegral?

**Status:** Open · **Kind:** open problem (Problem 1) · **Collection** 42

Can mimsup(A) be nonintegral?

**Context.** Marta Piecyk’s doctoral route: Graph Homomorphisms – Exploring the Boundaries of Tractability, Warsaw University of Technology, 2024 PhD dissertation in mathematics; supervisors Zbigniew Lonc and Paweł Rzążewski. Degree award unverified. Q4160 restates thesis Open Problem 1, p.18; subsequent questions follow her publication network. Field: Graph algorithms and matrix invariants. SETH denotes the Strong Exponential Time Hypothesis. Graphs are finite, simple, undirected. Hom(H) decides existence of an edge-preserving map G→H. An ordering’s width w is the maximum number of edges crossing a prefix cut. For finite square 0–1 matrices A, mim(A) is the largest order of a permutation submatrix, and him(A) that of a triangular submatrix with diagonal 1; rows/columns may be permuted independently. Put mimsup(A)=sup_{r≥1}mim(A^{⊗r})^{1/r}, using Kronecker powers. Joint-paper questions: Open Problem 1, p.77:3; §6, p.77:17. No resolution found through 10 October 2026.

**Source.** Carla Groenland, Isja Mannens, Jesper Nederlof, Marta Piecyk and Paweł Rzążewski. *ICALP 2024, Article 77 (title not given in the supplied text)*. 2024. [primary source](https://doi.org/10.4230/LIPIcs.ICALP.2024.77) Location: Open Problem 1, p.77:3; §6, p.77:17.

**Literature check.** Status: Joint-paper questions: Open Problem 1, p.77:3; §6, p.77:17. No resolution found through 10 October 2026.

**Further links.** [1](https://www.bip.pw.edu.pl/index.php/content/download/74183/706088/file/M.PIECYK_phd-main.pdf)


<a id="q4162"></a>

## Q4162. Is mimsup(A) bounded by a function of him(A), uniformly over A?

**Status:** Open · **Kind:** open problem (Problem 1) · **Collection** 42

Is mimsup(A) bounded by a function of him(A), uniformly over A?

**Context.** Marta Piecyk’s doctoral route: Graph Homomorphisms – Exploring the Boundaries of Tractability, Warsaw University of Technology, 2024 PhD dissertation in mathematics; supervisors Zbigniew Lonc and Paweł Rzążewski. Degree award unverified. Q4160 restates thesis Open Problem 1, p.18; subsequent questions follow her publication network. Field: Graph algorithms and matrix invariants. SETH denotes the Strong Exponential Time Hypothesis. Graphs are finite, simple, undirected. Hom(H) decides existence of an edge-preserving map G→H. An ordering’s width w is the maximum number of edges crossing a prefix cut. For finite square 0–1 matrices A, mim(A) is the largest order of a permutation submatrix, and him(A) that of a triangular submatrix with diagonal 1; rows/columns may be permuted independently. Put mimsup(A)=sup_{r≥1}mim(A^{⊗r})^{1/r}, using Kronecker powers. Joint-paper questions: Open Problem 1, p.77:3; §6, p.77:17. No resolution found through 10 October 2026.

**Source.** Carla Groenland, Isja Mannens, Jesper Nederlof, Marta Piecyk and Paweł Rzążewski. *ICALP 2024, Article 77 (title not given in the supplied text)*. 2024. [primary source](https://doi.org/10.4230/LIPIcs.ICALP.2024.77) Location: Open Problem 1, p.77:3; §6, p.77:17.

**Literature check.** Status: Joint-paper questions: Open Problem 1, p.77:3; §6, p.77:17. No resolution found through 10 October 2026.

**Further links.** [1](https://www.bip.pw.edu.pl/index.php/content/download/74183/706088/file/M.PIECYK_phd-main.pdf)


<a id="q4163"></a>

## Q4163. Is deciding proper 3-colorability polynomial-time solvable for graphs of diameter at most 2?

**Status:** Open · **Kind:** open problem · **Collection** 42

Is deciding proper 3-colorability polynomial-time solvable for graphs of diameter at most 2?

**Context.** Marta Piecyk’s doctoral route: Graph Homomorphisms – Exploring the Boundaries of Tractability, Warsaw University of Technology, 2024 PhD dissertation in mathematics; supervisors Zbigniew Lonc and Paweł Rzążewski. Degree award unverified. Q4160 restates thesis Open Problem 1, p.18; subsequent questions follow her publication network. Field: Graph algorithms and matrix invariants. SETH denotes the Strong Exponential Time Hypothesis. For each fixed integer k≥2 and finite simple undirected G, Hom(C_{2k+1}) asks for a map from V(G) to the vertices of the (2k+1)-cycle that maps edges to edges. Diameter is maximum shortest-path distance. Proper 3-coloring assigns adjacent vertices different colors from {1,2,3}. Origin: Q4163 is an older problem; Q4164 comes from Piecyk’s paper. The revised full text follows MFCS 2024 and withdraws an earlier assertion about diameter k+3; it retains this exact question. No later matching resolution found through 10 October 2026.

**Source.** Marta Piecyk. *C_{2k+1}-Coloring of Bounded-Diameter Graphs*. 2024. [primary source](https://arxiv.org/abs/2403.06694v3) Location: §8, p.24; definition p.1.

**Literature check.** Status: Origin: Q4163 is an older problem; Q4164 comes from Piecyk’s paper. The revised full text follows MFCS 2024 and withdraws an earlier assertion about diameter k+3; it retains this exact question. No later matching resolution found through 10 October 2026.

**Further links.** [1](https://www.bip.pw.edu.pl/index.php/content/download/74183/706088/file/M.PIECYK_phd-main.pdf)


<a id="q4164"></a>

## Q4164. Is Hom(C_{2k+1}) NP-hard on graphs of diameter at most k+2, for every fixed k≥2?

**Status:** Open · **Kind:** open problem · **Collection** 42

Is Hom(C_{2k+1}) NP-hard on graphs of diameter at most k+2, for every fixed k≥2?

**Context.** Marta Piecyk’s doctoral route: Graph Homomorphisms – Exploring the Boundaries of Tractability, Warsaw University of Technology, 2024 PhD dissertation in mathematics; supervisors Zbigniew Lonc and Paweł Rzążewski. Degree award unverified. Q4160 restates thesis Open Problem 1, p.18; subsequent questions follow her publication network. Field: Graph algorithms and matrix invariants. SETH denotes the Strong Exponential Time Hypothesis. For each fixed integer k≥2 and finite simple undirected G, Hom(C_{2k+1}) asks for a map from V(G) to the vertices of the (2k+1)-cycle that maps edges to edges. Diameter is maximum shortest-path distance. Proper 3-coloring assigns adjacent vertices different colors from {1,2,3}. Origin: Q4163 is an older problem; Q4164 comes from Piecyk’s paper. The revised full text follows MFCS 2024 and withdraws an earlier assertion about diameter k+3; it retains this exact question. No later matching resolution found through 10 October 2026.

**Source.** Marta Piecyk. *C_{2k+1}-Coloring of Bounded-Diameter Graphs*. 2024. [primary source](https://arxiv.org/abs/2403.06694v3) Location: §8, p.24; definition p.1.

**Literature check.** Status: Origin: Q4163 is an older problem; Q4164 comes from Piecyk’s paper. The revised full text follows MFCS 2024 and withdraws an earlier assertion about diameter k+3; it retains this exact question. No later matching resolution found through 10 October 2026.

**Further links.** [1](https://www.bip.pw.edu.pl/index.php/content/download/74183/706088/file/M.PIECYK_phd-main.pdf)


<a id="q4165"></a>

## Q4165. For each fixed k≥3, determine the complexity of List k-Coloring on X-free ordered graphs.

**Status:** Open · **Kind:** open problem · **Collection** 42

For each fixed k≥3, determine the complexity of List k-Coloring on X-free ordered graphs.

**Context.** Marta Piecyk’s doctoral route: Graph Homomorphisms – Exploring the Boundaries of Tractability, Warsaw University of Technology, 2024 PhD dissertation in mathematics; supervisors Zbigniew Lonc and Paweł Rzążewski. Degree award unverified. Q4160 restates thesis Open Problem 1, p.18; subsequent questions follow her publication network. Field: Graph algorithms and matrix invariants. SETH denotes the Strong Exponential Time Hypothesis. An ordered graph has a supplied linear vertex order; H-free means no order-preserving induced copy of H. List k-Coloring asks for a proper coloring (adjacent vertices differ) from lists L(v)⊆{1,…,k}. Let X and N each have vertices 1<2<3<4, with edges {13,24} and {14,23}, respectively. All graphs are finite, simple and undirected. Origin: Joint-paper questions after Piecyk’s dissertation. The quadratic hardness reduction for Q4166 excludes only 2^{o(√n)} time under the Exponential Time Hypothesis. No matching later resolution found through 10 October 2026.

**Source.** Marta Piecyk and Paweł Rzążewski. *List Coloring Ordered Graphs with Forbidden Induced Subgraphs*. 2026. [primary source](https://doi.org/10.4230/LIPIcs.STACS.2026.74) Location: Final §5, p.74:16; definitions p.74:4; Theorem 12, p.74:10.

**Literature check.** Status: Origin: Joint-paper questions after Piecyk’s dissertation. The quadratic hardness reduction for Q4166 excludes only 2^{o(√n)} time under the Exponential Time Hypothesis. No matching later resolution found through 10 October 2026.

**Further links.** [1](https://www.bip.pw.edu.pl/index.php/content/download/74183/706088/file/M.PIECYK_phd-main.pdf)


<a id="q4166"></a>

## Q4166. Does List 4-Coloring on n-vertex N-free ordered graphs admit a 2^{o(n)}-time algorithm?

**Status:** Open · **Kind:** open problem · **Collection** 42

Does List 4-Coloring on n-vertex N-free ordered graphs admit a 2^{o(n)}-time algorithm?

**Context.** Marta Piecyk’s doctoral route: Graph Homomorphisms – Exploring the Boundaries of Tractability, Warsaw University of Technology, 2024 PhD dissertation in mathematics; supervisors Zbigniew Lonc and Paweł Rzążewski. Degree award unverified. Q4160 restates thesis Open Problem 1, p.18; subsequent questions follow her publication network. Field: Graph algorithms and matrix invariants. SETH denotes the Strong Exponential Time Hypothesis. An ordered graph has a supplied linear vertex order; H-free means no order-preserving induced copy of H. List k-Coloring asks for a proper coloring (adjacent vertices differ) from lists L(v)⊆{1,…,k}. Let X and N each have vertices 1<2<3<4, with edges {13,24} and {14,23}, respectively. All graphs are finite, simple and undirected. Origin: Joint-paper questions after Piecyk’s dissertation. The quadratic hardness reduction for Q4166 excludes only 2^{o(√n)} time under the Exponential Time Hypothesis. No matching later resolution found through 10 October 2026.

**Source.** Marta Piecyk and Paweł Rzążewski. *List Coloring Ordered Graphs with Forbidden Induced Subgraphs*. 2026. [primary source](https://doi.org/10.4230/LIPIcs.STACS.2026.74) Location: Final §5, p.74:16; definitions p.74:4; Theorem 12, p.74:10.

**Literature check.** Status: Origin: Joint-paper questions after Piecyk’s dissertation. The quadratic hardness reduction for Q4166 excludes only 2^{o(√n)} time under the Exponential Time Hypothesis. No matching later resolution found through 10 October 2026.

**Further links.** [1](https://www.bip.pw.edu.pl/index.php/content/download/74183/706088/file/M.PIECYK_phd-main.pdf)


<a id="q4169"></a>

## Q4169. For every fixed integer k≥0, is MWIS quasipolynomial-time solvable on H_k-free graphs, where H_k…

**Status:** Open · **Kind:** open problem · **Collection** 42

For every fixed integer k≥0, is MWIS quasipolynomial-time solvable on H_k-free graphs, where H_k has vertices 1<...<2k+4 and exactly edges {1,2k+4},{k+2,k+3}?

**Context.** Marta Piecyk’s doctoral route: Graph Homomorphisms – Exploring the Boundaries of Tractability, Warsaw University of Technology, 2024 PhD dissertation in mathematics; supervisors Zbigniew Lonc and Paweł Rzążewski. Degree award unverified. Q4160 restates thesis Open Problem 1, p.18; subsequent questions follow her publication network. Field: Graph algorithms and matrix invariants. SETH denotes the Strong Exponential Time Hypothesis. The finite simple undirected input graph has a linear vertex order. H-free means excluding induced copies preserving that order. MWIS finds a pairwise nonadjacent vertex set of maximum total positive rational weight.

**Source.** Paweł Rafał Bieliński, Marta Piecyk and Paweł Rzążewski. *Maximum Weight Independent Set in Hereditary Classes of Ordered Graphs*. 2026. [primary source](https://doi.org/10.4230/LIPIcs.ESA.2026.30) Location: §4 p. 30:12; definitions pp. 30:1–3,6.

**Literature check.** Status: ETH asserts that 3-SAT has no subexponential-time algorithm in its variable count. No matching resolution found, 10 October 2026.

**Further links.** [1](https://www.bip.pw.edu.pl/index.php/content/download/74183/706088/file/M.PIECYK_phd-main.pdf)


<a id="q4170"></a>

## Q4170. Assuming the Exponential-Time Hypothesis, does maximum-cardinality independent set on F-free…

**Status:** Open · **Kind:** open problem · **Collection** 42

Assuming the Exponential-Time Hypothesis, does maximum-cardinality independent set on F-free n-vertex ordered graphs have no 2^{o(n)}-time algorithm, where F has vertices 1<2<3<4<5 and exactly edges {1,5},{2,4}?

**Context.** Marta Piecyk’s doctoral route: Graph Homomorphisms – Exploring the Boundaries of Tractability, Warsaw University of Technology, 2024 PhD dissertation in mathematics; supervisors Zbigniew Lonc and Paweł Rzążewski. Degree award unverified. Q4160 restates thesis Open Problem 1, p.18; subsequent questions follow her publication network. Field: Graph algorithms and matrix invariants. SETH denotes the Strong Exponential Time Hypothesis. The finite simple undirected input graph has a linear vertex order. H-free means excluding induced copies preserving that order. MWIS finds a pairwise nonadjacent vertex set of maximum total positive rational weight.

**Source.** Paweł Rafał Bieliński, Marta Piecyk and Paweł Rzążewski. *Maximum Weight Independent Set in Hereditary Classes of Ordered Graphs*. 2026. [primary source](https://doi.org/10.4230/LIPIcs.ESA.2026.30) Location: §4 p. 30:12; definitions pp. 30:1–3,6.

**Literature check.** Status: ETH asserts that 3-SAT has no subexponential-time algorithm in its variable count. No matching resolution found, 10 October 2026.

**Further links.** [1](https://www.bip.pw.edu.pl/index.php/content/download/74183/706088/file/M.PIECYK_phd-main.pdf)

