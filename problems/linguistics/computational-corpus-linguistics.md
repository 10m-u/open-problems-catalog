# Computational & Corpus Linguistics

8 problems: 8 open.

[All subjects](../README.md) · [Index by number](../INDEX.md)

| Q | Title | Status |
|---|---|---|
| [Q162](computational-corpus-linguistics.md#q162) | For a fixed symbolic probabilistic grammar G, characterize exactly the pseudodim… | Open |
| [Q163](computational-corpus-linguistics.md#q163) | For string maps f:Σ\*→Σ\*, is Yolyan’s weak determinism via simultaneous applicati… | Open |
| [Q238](computational-corpus-linguistics.md#q238) | In Oakden’s length-preserving, single-copy BMRS setting, are the left-output-str… | Open |
| [Q239](computational-corpus-linguistics.md#q239) | In Graf’s movement-generalized Minimalist grammars, can every PBC-obeying upward… | Open |
| [Q302](computational-corpus-linguistics.md#q302) | For each fixed pair j,k≥0 with j=0 or k=0, is the class of (j,k)-neighborhood-di… | Open |
| [Q303](computational-corpus-linguistics.md#q303) | Are all trigram languages and all precedence languages in the range of Heinz’s F… | Open |
| [Q1379](computational-corpus-linguistics.md#q1379) | Dyck inclusion for multiple context-free languages | Open |
| [Q1380](computational-corpus-linguistics.md#q1380) | Double-exponential downward closures with variable dimension | Open |

<a id="q162"></a>

## Q162. For a fixed symbolic probabilistic grammar G, characterize exactly the pseudodim…

**Status:** Open · **Kind:** open problem · **Collection** 2

For a fixed symbolic probabilistic grammar G, characterize exactly the pseudodimension of its derivation-level negative-log-likelihood family F(G), taking account of dependencies among rule/event-count features rather than merely counting parameters.

**Context.** Origin: Author’s explicit exact-dimension question, subsequently repeated with Smith in Computational Linguistics (2012), §7.4.2. Shared notation: The model is hθ(y)=∏ₖ,ᵢ θₖ,ᵢ^(ψₖ,ᵢ(y)) on valid derivations y, with each θₖ a multinomial and ψₖ,ᵢ(y) the corresponding event count; F(G)={−log hθ : θ∈ΘG}. This concerns complete derivations, not log-sums over hidden parses.

**Source.** Shay Cohen. *Computational Learning of Probabilistic Grammars in the Unsupervised Setting*. Carnegie Mellon University, 2011. Advisor(s): Noah A. Smith. [primary source](https://www.lti.cs.cmu.edu/people/alumni/alumni-thesis/cohen-shay-thesis.pdf) · [record](https://www.lti.cs.cmu.edu/research/dissertations/2011-2007.html) Location: §9.1.1, unnumbered open problem under “Sharper Bounds…”, printed p.168 (PDF p.169); definitions §2.1 and §4.2, pp.18 and 48. Status evidence, checked 5 October 2026: The 2012 joint paper explicitly retains the exact characterization as open. Searches for pseudodimension of probabilistic/context-free grammars and the author’s current work found no general resolution. This is a bounded-negative check, not a recent author confirmation.

**Further links.** [1](https://aclanthology.org/J12-3003/) · [2](https://homepages.inf.ed.ac.uk/scohen/cl12pgerm.pdf) · [3](https://homepages.inf.ed.ac.uk/scohen/publications.html)


<a id="q163"></a>

## Q163. For string maps f:Σ\*→Σ\*, is Yolyan’s weak determinism via simultaneous applicati…

**Status:** Open · **Kind:** open problem · **Collection** 2

For string maps f:Σ\*→Σ\*, is Yolyan’s weak determinism via simultaneous application of predecessor-only and successor-only Boolean Monadic Recursive Schemes equivalent to Meinhardt–Mai–Baković–McCollum’s 2024 bimachine definition of weak determinism? Use the general program formalism, including copy sets.

**Context.** Origin: Author’s own comparison question; also appears in the author’s April 2025 JoLLI paper, before dissertation filing. Shared notation: BMRS simultaneous application flips an input-predicate truth value exactly when either component flips it. The bimachine condition is: ω(qL,x,qR)=y iff [∀r∈QR, ω(qL,x,r)=y] or [∀l∈QL, ω(l,x,qR)=y], for all states qL,qR, input letters x and output strings y.

**Source.** Tatevik Arayevna Yolyan. *Phonological Expressivity and Learning via Boolean Monadic Recursive Schemes*. Rutgers, The State University of New Jersey, 2025. Advisor(s): Adam Jardine. [primary source](https://adamjardine.net/files/yolyan2025dissertation.pdf) · [record](https://sites.rutgers.edu/lgsa/tatevik-yolyan-successfully-defends-dissertation/) Location: §6.4, unnumbered equivalence question, printed p.161 (PDF p.171); Definition 6.2, p.134; simultaneous application Definition 5.4. Status evidence, checked 5 October 2026: Explicitly unresolved in the 2025 dissertation and JoLLI §6.3. Yolyan–Comer’s July 2026 paper establishes total BMRS/modal μ-calculus equivalence, not the weak-determinism comparison. Targeted searches found no proof or counterexample for the latter.

**Further links.** [1](https://doi.org/10.1007/s10849-025-09429-9) · [2](https://doi.org/10.1007/s11049-023-09578-1) · [3](https://aclanthology.org/2026.scil-main.51/)


<a id="q238"></a>

## Q238. In Oakden’s length-preserving, single-copy BMRS setting, are the left-output-str…

**Status:** Open · **Kind:** open problem · **Collection** 3

In Oakden’s length-preserving, single-copy BMRS setting, are the left-output-strictly-local functions closed under parallel satisfaction, and likewise the right-output-strictly-local functions? Both operands have the same input alphabet and the same output alphabet; their recursive output references run in the same direction. BMRS means Boolean Monadic Recursive Schemes, the thesis’s recursive transduction formalism.

**Context.** Origin: New closure question for the author’s parallel-satisfaction operation. Setup for question 238: Parallel satisfaction T₁⊖T₂ replaces each output equation’s final term in T₁ by the corresponding equation of T₂; recursive output references refer to the joined output. Output-strict locality means that the current input symbol and a bounded window of previously produced output determine each output, in the chosen direction.

**Source.** Christopher Donal Oakden. *Modeling Phonological Interactions using Recursive Schemes*. Rutgers, The State University of New Jersey, 2021. Advisor(s): Adam Jardine. [primary source](https://ling.rutgers.edu/images/dissertations/Oakden_dissertation.pdf) · [record](https://sites.rutgers.edu/lgsa/chris-oakden-defends-his-dissertation-successfully/) Location: §7.4.1, unnumbered closure question, printed pp.208–209 (PDF pp.218–219); §6.2.1 Definitions 4–5, pp.151–152; §6.2.3, p.158.

**Further links.** [1](https://doi.org/10.1162/ling_a_00510) · [2](https://aclanthology.org/2026.scil-main.51/) · [3](https://adamjardine.net/index.html)


<a id="q239"></a>

## Q239. In Graf’s movement-generalized Minimalist grammars, can every PBC-obeying upward…

**Status:** Open · **Kind:** open problem · **Collection** 3

In Graf’s movement-generalized Minimalist grammars, can every PBC-obeying upward movement be replaced by downward movement while preserving the generated tree structures? Conversely, can every downward movement not preceded by upward movement be replaced by PBC-obeying upward movement?

**Context.** Origin: The author’s companion conjectures in his own 2012 movement framework; retained together as one equivalence problem. Setup for question 239: The Proper Binding Condition (PBC) requires each mover to c-command all its traces, excluding remnant movement. The framework permits movement parameters definable in monadic second-order logic over derivation trees; the comparison concerns tree structures, not merely string yields.

**Source.** Thomas Graf. *Local and Transderivational Constraints in Syntax and Semantics*. University of California, Los Angeles, 2013. Advisor(s): Edward P. Stabler. [primary source](https://linguistics.ucla.edu/wp-content/uploads/2021/11/Graf_dissertation2013.pdf) · [record](https://linguistics.ucla.edu/wp-content/uploads/2021/11/Graf_dissertation2013.pdf) Location: §2.2.2, final two unnumbered conjectures, printed p.95 (PDF p.117); surrounding discussion pp.94–95; PBC definition §2.1.3, p.67.

**Further links.** [1](https://thomasgraf.net/doc/papers/lacl2012.pdf) · [2](https://thomasgraf.net/doc/papers/Graf23SCiL.pdf) · [3](https://thomasgraf.net/news.html)


<a id="q302"></a>

## Q302. For each fixed pair j,k≥0 with j=0 or k=0, is the class of (j,k)-neighborhood-di…

**Status:** Open · **Kind:** open problem · **Collection** 4

For each fixed pair j,k≥0 with j=0 or k=0, is the class of (j,k)-neighborhood-distinct languages over a finite alphabet closed under binary intersection?

**Context.** Discovery path (advisor ascent; student → supervisor):
Christopher Donal Oakden → Adam Jardine: https://ling.rutgers.edu/images/dissertations/Oakden_dissertation.pdf
Adam Jardine → Jeffrey Heinz: https://www.jeffreyheinz.net/advisees/2016_AdamJardine_dissertation.pdf
Jeffrey Nicholas Heinz → Edward P. Stabler and Kie Zuraw: https://www.jeffreyheinz.net/diss/heinz-2007-UCLA-diss.pdf Origin: Original closure and learner-range questions from Heinz’s dissertation. The forward-backward conjecture is distinct from his refuted forward-only conjecture. Shared setup for questions 302, 303: For a finite alphabet Σ, use finite-state acceptors with every state on an accepting path. The (j,k)-neighborhood of q consists of its initial/final flags and the sets of labels of paths of length at most j ending at q and at most k starting at q. An acceptor is (j,k)-neighborhood-distinct if these tuples distinguish its states; a language has this property if some such acceptor recognizes it. The acceptor need not be deterministic.

**Source.** Jeffrey Nicholas Heinz. *Inductive Learning of Phonotactic Patterns*. University of California, Los Angeles, 2007. Advisor(s): Edward P. Stabler; Kie Zuraw. [primary source](https://www.jeffreyheinz.net/diss/heinz-2007-UCLA-diss.pdf) · [record](https://www.jeffreyheinz.net/diss/) Location: Chapter 6 §4, question after Corollary 16, printed p. 213 (PDF p. 235); definitions pp. 204–206 (PDF pp. 226–228).

**Further links.** [1](https://ling.rutgers.edu/images/dissertations/Oakden_dissertation.pdf) · [2](https://www.jeffreyheinz.net/advisees/2016_AdamJardine_dissertation.pdf) · [3](https://www.jeffreyheinz.net/papers/Heinz-2009-RLLSP.pdf) · [4](https://www.jeffreyheinz.net/papers/Heinz-2008-LRIL.pdf) · [5](https://sites.socsci.uci.edu/~lpearl/colareadinggroup/readings/Heinz2011_CompPhon2.pdf) · [6](https://www.jeffreyheinz.net/papers/heinz_papers.html)


<a id="q303"></a>

## Q303. Are all trigram languages and all precedence languages in the range of Heinz’s F…

**Status:** Open · **Kind:** open problem · **Collection** 4

Are all trigram languages and all precedence languages in the range of Heinz’s Forward Backward Neighborhood Learner? Specifically, does every such L have a finite positive sample S⊆L for which the learner outputs an acceptor for exactly L? The learner merges equal (1,1)-neighborhood states to a fixed point separately in the sample’s prefix and suffix trees, then intersects their accepted languages. Trigram languages constrain boundary-marked contiguous blocks of length three; precedence languages prohibit specified ordered symbol pairs as possibly noncontiguous subsequences.

**Context.** Discovery path (advisor ascent; student → supervisor):
Christopher Donal Oakden → Adam Jardine: https://ling.rutgers.edu/images/dissertations/Oakden_dissertation.pdf
Adam Jardine → Jeffrey Heinz: https://www.jeffreyheinz.net/advisees/2016_AdamJardine_dissertation.pdf
Jeffrey Nicholas Heinz → Edward P. Stabler and Kie Zuraw: https://www.jeffreyheinz.net/diss/heinz-2007-UCLA-diss.pdf Origin: Original closure and learner-range questions from Heinz’s dissertation. The forward-backward conjecture is distinct from his refuted forward-only conjecture. Shared setup for questions 302, 303: For a finite alphabet Σ, use finite-state acceptors with every state on an accepting path. The (j,k)-neighborhood of q consists of its initial/final flags and the sets of labels of paths of length at most j ending at q and at most k starting at q. An acceptor is (j,k)-neighborhood-distinct if these tuples distinguish its states; a language has this property if some such acceptor recognizes it. The acceptor need not be deterministic.

**Source.** Jeffrey Nicholas Heinz. *Inductive Learning of Phonotactic Patterns*. University of California, Los Angeles, 2007. Advisor(s): Edward P. Stabler; Kie Zuraw. [primary source](https://www.jeffreyheinz.net/diss/heinz-2007-UCLA-diss.pdf) · [record](https://www.jeffreyheinz.net/diss/) Location: Chapter 6 §3.3, printed p. 210 (PDF p. 232); learner Chapter 5 §4; trigram and precedence definitions Chapters 3–4.

**Further links.** [1](https://ling.rutgers.edu/images/dissertations/Oakden_dissertation.pdf) · [2](https://www.jeffreyheinz.net/advisees/2016_AdamJardine_dissertation.pdf) · [3](https://www.jeffreyheinz.net/papers/Heinz-2009-RLLSP.pdf) · [4](https://www.jeffreyheinz.net/papers/Heinz-2008-LRIL.pdf) · [5](https://sites.socsci.uci.edu/~lpearl/colareadinggroup/readings/Heinz2011_CompPhon2.pdf) · [6](https://www.jeffreyheinz.net/papers/heinz_papers.html)


<a id="q1379"></a>

## Q1379. Dyck inclusion for multiple context-free languages

**Status:** Open · **Kind:** open problem · **Collection** 14

Is it decidable whether the language of a given MCFG is contained in a given Dyck language?

**Context.** Origin for questions 1379, 1380: Two explicit questions in §8, p. 74:27. Setup for questions 1379, 1380: MCFG nonterminals derive tuples of words using linear, possibly deleting concatenation rules. Dimension is maximum tuple arity; rank is maximum rule arity. Both are input parameters unless fixed. L↓ contains all scattered subwords of words in L. Dyck languages consist of correctly nested, typed parentheses.

**Source.** C. Aiswarya, Pascal Baumann, Prakash Saivasan, Lia Schütze, Georg Zetzsche. *Bounded Treewidth, Multiple Context-Free Grammars, and Downward Closures*. 2026. [primary source](https://doi.org/10.1145/3776716) Location: §8, first paragraph, p. 74:27.

**Literature check.** Status for questions 1379, 1380, checked 6 October 2026: January 2026 questions retained; July 2026 indexed-language bounds concern a different grammar model.

**Further links.** [1](https://pure.mpg.de/rest/items/item_3699283_1/component/file_3699284/content) · [2](https://doi.org/10.4230/LIPIcs.LICS.2026.69)


<a id="q1380"></a>

## Q1380. Double-exponential downward closures with variable dimension

**Status:** Open · **Kind:** open problem · **Collection** 14

Given an MCFG G with dimension part of the input, can an NFA for L(G)↓ be constructed in time 2^{2^{poly(|G|)}}?

**Context.** Origin for questions 1379, 1380: Two explicit questions in §8, p. 74:27. Setup for questions 1379, 1380: MCFG nonterminals derive tuples of words using linear, possibly deleting concatenation rules. Dimension is maximum tuple arity; rank is maximum rule arity. Both are input parameters unless fixed. L↓ contains all scattered subwords of words in L. Dyck languages consist of correctly nested, typed parentheses.

**Source.** C. Aiswarya, Pascal Baumann, Prakash Saivasan, Lia Schütze, Georg Zetzsche. *Bounded Treewidth, Multiple Context-Free Grammars, and Downward Closures*. 2026. [primary source](https://doi.org/10.1145/3776716) Location: §8, last paragraph, p. 74:27; Theorem 3.4.

**Literature check.** Status for questions 1379, 1380, checked 6 October 2026: January 2026 questions retained; July 2026 indexed-language bounds concern a different grammar model.

**Further links.** [1](https://pure.mpg.de/rest/items/item_3699283_1/component/file_3699284/content) · [2](https://doi.org/10.4230/LIPIcs.LICS.2026.69)

