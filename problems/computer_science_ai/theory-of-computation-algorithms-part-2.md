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

