# Social Choice & Voting Theory

13 problems: 13 open.

[All subjects](../README.md) · [Index by number](../INDEX.md)

| Q | Title | Status |
|---|---|---|
| [Q131](social-choice-voting-theory.md#q131) | Must every individually strategyproof, U-continuous mechanism selecting core all… | Open |
| [Q132](social-choice-voting-theory.md#q132) | Start all individual allocations at zero. Each turn, one agent (re)distributes h… | Open |
| [Q133](social-choice-voting-theory.md#q133) | For m≥4 alternatives and arbitrary finite electorates with strict rankings, is 3… | Open |
| [Q134](social-choice-voting-theory.md#q134) | For finite project sets and arbitrary finite sets of donors with nonempty approv… | Open |
| [Q135](social-choice-voting-theory.md#q135) | Fix m candidates, scoring vector α∈R^m, and t&lt;m such that all t-subset queries d… | Open |
| [Q136](social-choice-voting-theory.md#q136) | For sufficiently many voters n and m candidates, what minimum asymptotic t(m) pe… | Open |
| [Q353](social-choice-voting-theory.md#q353) | What are the optimal worst-case approximation guarantees for the maximum Copelan… | Open |
| [Q364](social-choice-voting-theory.md#q364) | Determine the complexity of this decision problem. Registered voters V and poten… | Open |
| [Q3472](social-choice-voting-theory.md#q3472) | Smallest B-unstable roommate instance | Open |
| [Q3473](social-choice-voting-theory.md#q3473) | Hardness of B-maximal stability | Open |
| [Q3474](social-choice-voting-theory.md#q3474) | Three-halves W-maximal stability | Open |
| [Q3475](social-choice-voting-theory.md#q3475) | Ternary symmetric justified envy | Open |
| [Q3476](social-choice-voting-theory.md#q3476) | Smallest symmetric justified-envy obstruction | Open |

<a id="q131"></a>

## Q131. Must every individually strategyproof, U-continuous mechanism selecting core all…

**Status:** Open · **Kind:** open problem (Problem 1) · **Collection** 2

Must every individually strategyproof, U-continuous mechanism selecting core allocations equal NASH? U-continuity requires convergence of outcome utilities, evaluated at original utilities, as reported weights converge.

**Context.** Date note: Submitted November 2024; accepted March 2025. Advisor independently listed under doctoral supervision in Brandt’s official CV, p. 11. Origin: Extensions of thesis theorems from joint work with Felix Brandt, Erel Segal-Halevi, and Warut Suksompong. Shared notation: There are finitely many agents and projects. Agents contribute Cᵢ>0 and have utilities uᵢ(δ)=min_(vᵢₓ>0) δₓ/vᵢₓ for normalized nonnegative nonzero vᵢ. NASH maximizes ∏ᵢuᵢ(δ)^Cᵢ over δ≥0, ∑ₓδₓ=∑ᵢCᵢ. Core allocations admit no coalition redistribution of its contributions strictly improving every member regardless of remaining contributions.

**Source.** Matthias S. Greger. *Collective Choice from the Probability Simplex with Application to Donor Coordination*. Technical University of Munich, 2025. Advisor(s): Felix Brandt. [primary source](https://mediatum.ub.tum.de/doc/1759811/document.pdf) · [record](https://pub.dss.in.tum.de/brandt/cv_english.pdf) Location: Open Problem 1, p. 97 (PDF p. 113); definitions 2.13 and 3.2, pp. 15, 25; Theorem 5.36, p. 76. Status evidence, checked 5 October 2026: The later Mathematics of Operations Research article retains the group-strategyproof characterization for ordinary Leontief utilities. Its individual-strategyproof characterization is for the different leximin-Leontief domain and does not settle this question. Targeted searches located no solution to the ordinary-Leontief problem.

**Further links.** [1](https://pubsonline.informs.org/doi/10.1287/moor.2024.0723) · [2](https://arxiv.org/html/2305.10286v3)


<a id="q132"></a>

## Q132. Start all individual allocations at zero. Each turn, one agent (re)distributes h…

**Status:** Open · **Kind:** open problem (Problem 5) · **Collection** 2

Start all individual allocations at zero. Each turn, one agent (re)distributes her entire Cᵢ as a best response to current others. If every agent is selected infinitely often, must aggregate allocations converge to NASH, without a uniform finite bound on waiting times?

**Context.** Date note: Submitted November 2024; accepted March 2025. Advisor independently listed under doctoral supervision in Brandt’s official CV, p. 11. Origin: Extensions of thesis theorems from joint work with Felix Brandt, Erel Segal-Halevi, and Warut Suksompong. Shared notation: There are finitely many agents and projects. Agents contribute Cᵢ>0 and have utilities uᵢ(δ)=min_(vᵢₓ>0) δₓ/vᵢₓ for normalized nonnegative nonzero vᵢ. NASH maximizes ∏ᵢuᵢ(δ)^Cᵢ over δ≥0, ∑ₓδₓ=∑ᵢCᵢ. Core allocations admit no coalition redistribution of its contributions strictly improving every member regardless of remaining contributions.

**Source.** Matthias S. Greger. *Collective Choice from the Probability Simplex with Application to Donor Coordination*. Technical University of Munich, 2025. Advisor(s): Felix Brandt. [primary source](https://mediatum.ub.tum.de/doc/1759811/document.pdf) · [record](https://pub.dss.in.tum.de/brandt/cv_english.pdf) Location: Open Problem 5, p. 99 (PDF p. 115); redistribution dynamics and Theorem 5.24, pp. 65–67. Status evidence, checked 5 October 2026: The October 2025 revision of Coordinating Charitable Donations with Leontief Preferences still imposes the bounded-waiting K assumption in Theorem 3. The following discussion removes it only for binary Leontief utilities. Searches through the check date found no general resolution.

**Further links.** [1](https://arxiv.org/html/2305.10286v3) · [2](https://arxiv.org/abs/2305.10286)


<a id="q133"></a>

## Q133. For m≥4 alternatives and arbitrary finite electorates with strict rankings, is 3…

**Status:** Open · **Kind:** open problem · **Collection** 2

For m≥4 alternatives and arbitrary finite electorates with strict rankings, is 3/m the largest uniform lower bound alpha such that a randomized social decision scheme satisfying SD-participation can assign probability at least alpha to every Condorcet winner? SD-participation means that, according to each voter’s ranking, the lottery when voting weakly stochastically dominates the lottery after that voter abstains. A Condorcet winner defeats every other alternative by strict pairwise majority. Choosing a uniformly random triple and applying maximin attains 3/m; the question is whether any scheme can attain alpha>3/m uniformly over all profiles.

**Context.** Date note: Submitted December 2024; accepted April 2025. Advisor confirmed by doctoral-supervision list in Brandt’s official CV, p. 11. Origin: The thesis reports its own linear-programming evidence for the 3/m upper bound on small instances and its own matching lower-bound construction; it explicitly leaves the general upper bound unresolved. This quantitative problem differs from the earlier qualitative no-show impossibility it cites.

**Source.** René Romen. *Performance Guarantees in Probabilistic Social Choice and Online Coalition Formation*. Technical University of Munich, 2025. Advisor(s): Felix Brandt. [primary source](https://mediatum.ub.tum.de/doc/1764812/1764812.pdf) · [record](https://pub.dss.in.tum.de/brandt/cv_english.pdf) Location: §4.1, p. 39 (PDF p. 53); conclusion, p. 45. Status evidence, checked 5 October 2026: The 2025 thesis explicitly leaves the bound open. Searches combining Romen, participation, approximate Condorcet consistency and 3/m found no later resolution. The author’s earlier joint paper concerns strategyproofness (a stronger axiom), so its 2/m theorem does not settle this participation problem.

**Further links.** [1](https://arxiv.org/abs/2201.10418)


<a id="q134"></a>

## Q134. For finite project sets and arbitrary finite sets of donors with nonempty approv…

**Status:** Open · **Kind:** open problem · **Collection** 2

For finite project sets and arbitrary finite sets of donors with nonempty approval sets A_i and positive endowments C_i, does there exist a distribution rule f assigning the pooled budget among projects that simultaneously satisfies Pareto efficiency, approval monotonicity and contribution incentive-compatibility? Utilities are u_i(delta)=sum_(x in A_i)delta_x. Approval monotonicity means that adding x to one donor’s approval set cannot decrease the allocation to x. Contribution incentive-compatibility requires u_i(f(A))≥u_i(f(A_(-i)))+C_i for each donor when at least two participate; the reduced profile omits both i and C_i. The thesis shows pairwise compatibility but leaves this three-way compatibility open.

**Context.** Date note: Accepted July 2025. Brandt’s official CV lists doctoral supervision, June 2017–July 2025; thesis examiners are not treated as co-advisors. Origin: Explicit open problem in Stricker’s own joint EC 2021 paper with Florian Brandl, Felix Brandt and Dominik Peters, reproduced as a thesis contribution. The older Bogomolnaia et al. conjecture in the adjacent paragraph is solved and is not the retained question.

**Source.** Christian Stricker. *Analyzing Non-Deterministic Collective Choice Rules via Computer-Aided Methods*. Technical University of Munich, 2025. Advisor(s): Felix Brandt. [primary source](https://mediatum.ub.tum.de/doc/1765146/document.pdf) · [record](https://pub.dss.in.tum.de/brandt/cv_english.pdf) Location: Appended paper Distribution Rules Under Dichotomous Preferences: Two Out of Three Ain’t Bad, §6; thesis p. 179 (PDF p. 193), reproduced paper p. 177; definitions 6–7, thesis pp. 168–169. Status evidence, checked 5 October 2026: The thesis and currently hosted primary paper retain the three-way compatibility question. Searches for the exact three axioms and later donor-coordination work found no proof or counterexample. This is weaker than strategyproofness, so known efficiency/strategyproofness/fairness impossibilities do not answer it.

**Further links.** [1](https://pub.dss.in.tum.de/brandt-research/posshare.pdf) · [2](https://doi.org/10.1145/3465456.3467653)


<a id="q135"></a>

## Q135. Fix m candidates, scoring vector α∈R^m, and t&lt;m such that all t-subset queries d…

**Status:** Open · **Kind:** open problem · **Collection** 2

Fix m candidates, scoring vector α∈R^m, and t&lt;m such that all t-subset queries determine an α-winner. An unknown distribution σ on strict rankings answers Q, |Q|≤t, with its exact induced ranking distribution. Determine optimal worst-case success probability for randomized adaptive algorithms using ≤q queries to output a maximizer of E_(r∼σ)[α\_(rank_r(c))].

**Context.** Origin: Chapter 4 is joint with Safwan Hossain and Jamie Tucker-Foltz; Chapter 5 with Soroush Ebadian and Evi Micha.

**Source.** Daniel Halpern. *New Paradigms in Social Choice*. Harvard University, 2025. Advisor(s): Ariel D. Procaccia. [primary source](https://dash.harvard.edu/server/api/core/bitstreams/7f78d41b-9850-41b8-800e-ad45fb8fc596/content) · [record](https://dash.harvard.edu/handle/1/42725824) Location: §4.6, p. 117 (PDF p. 128); model §4.2.1–4.2.3, pp. 89–91; bounds §4.5. Status evidence, checked 5 October 2026: The currently available primary paper explicitly retains the general randomized problem. Searches through 2026 found no resolution. Later improvement-feedback work studies a different oracle, and Halpern’s 2026 moment-based paper assumes a different linear model; neither settles this unrestricted ranking-distribution problem.

**Further links.** [1](https://arxiv.org/abs/2402.11104) · [2](https://daniel-halpern.com/files/social-choice-queries.pdf) · [3](https://arxiv.org/abs/2603.19510)


<a id="q136"></a>

## Q136. For sufficiently many voters n and m candidates, what minimum asymptotic t(m) pe…

**Status:** Open · **Kind:** open problem · **Collection** 2

For sufficiently many voters n and m candidates, what minimum asymptotic t(m) permits deterministic bounded-distortion metric social choice with ≤t pairwise candidate comparisons per voter? Fix each voter’s batch before their answers; batches may depend on other voters. Distortion is sup_d ∑ᵢd(i,a)/min_b∑ᵢd(i,b), over consistent metrics. More generally, close the distortion gap for t=ω(m/log m).

**Context.** Origin: Chapter 4 is joint with Safwan Hossain and Jamie Tucker-Foltz; Chapter 5 with Soroush Ebadian and Evi Micha.

**Source.** Daniel Halpern. *New Paradigms in Social Choice*. Harvard University, 2025. Advisor(s): Ariel D. Procaccia. [primary source](https://dash.harvard.edu/server/api/core/bitstreams/7f78d41b-9850-41b8-800e-ad45fb8fc596/content) · [record](https://dash.harvard.edu/handle/1/42725824) Location: §5.4.3, concluding paragraph p. 138 (PDF p. 149); model §5.2, pp. 122–125; Theorem 5.4.5, p. 136. Status evidence, checked 5 October 2026: The primary IJCAI 2024 paper and 2025 thesis explicitly leave the threshold open. Targeted title and intra-agent-nonadaptivity searches through the check date located no later resolution. Results improving distortion with complete ordinal rankings do not resolve the comparison-budget restriction.

**Further links.** [1](https://www.ijcai.org/proceedings/2024/0309.pdf) · [2](https://daniel-halpern.com/files/metric-distortion-with-queries.pdf)


<a id="q353"></a>

## Q353. What are the optimal worst-case approximation guarantees for the maximum Copelan…

**Status:** Open · **Kind:** open problem · **Collection** 4

What are the optimal worst-case approximation guarantees for the maximum Copeland score obtainable by deterministic voting trees and distributions over them? A voting tree is a finite rooted binary tree whose leaves are candidate names, with repetitions allowed. On a tournament T over m candidates, each internal match returns the candidate beating the other child; Γ(T) is the root winner. The guarantee is inf_T d⁺\_T(Γ(T))/max_v d⁺\_T(v), or the corresponding expected numerator for randomized trees. The tree or distribution is fixed before T is known.

**Context.** Metadata note: The thesis is dated September 2008; some degree summaries use 2009. Discovery path (advisor ascent; student → supervisor):
Daniel Halpern → Ariel D. Procaccia: https://dash.harvard.edu/server/api/core/bitstreams/7f78d41b-9850-41b8-800e-ad45fb8fc596/content
Ariel D. Procaccia → Jeffrey S. Rosenschein: https://comsoc-community.org/assets/theses/phd-procaccia.pdf Origin: Procaccia’s Chapter 4 develops his joint work with Felix Fischer and Alex Samorodnitsky and explicitly asks to close both approximation gaps. Their COMSOC 2008 paper and 2011 Random Structures & Algorithms article formulate the same questions.

**Source.** Ariel D. Procaccia. *Computational Voting Theory: Of the Agents, By the Agents, For the Agents*. Hebrew University of Jerusalem, 2008. Advisor(s): Jeffrey S. Rosenschein. [primary source](https://comsoc-community.org/assets/theses/phd-procaccia.pdf) · [record](https://procaccia.info/publications/) Location: §4.7, printed p. 43 (PDF p. 56); definitions §4.2.

**Further links.** [1](https://dash.harvard.edu/server/api/core/bitstreams/7f78d41b-9850-41b8-800e-ad45fb8fc596/content) · [2](https://drops.dagstuhl.de/storage/00lipics/lipics-vol145-approx-random2019/LIPIcs.APPROX-RANDOM.2019.13/LIPIcs.APPROX-RANDOM.2019.13.pdf) · [3](https://maths.qmul.ac.uk/~ffischer/publications/fps_trees.pdf) · [4](https://arxiv.org/abs/1211.0515)


<a id="q364"></a>

## Q364. Determine the complexity of this decision problem. Registered voters V and poten…

**Status:** Open · **Kind:** open problem · **Collection** 4

Determine the complexity of this decision problem. Registered voters V and potential voters W rank the same candidates strictly; p is distinguished and k is a budget. For each w∈W, its bundle κ(w) contains exactly the voters in W whose rankings differ from w’s by at most two adjacent swaps. Assume |κ(w)|≤3. Can at most k leaders be selected so that adding the union of their bundles makes p a plurality co-winner?

**Context.** Metadata note: Defended 18 December 2015; the publisher edition is dated 2016. Discovery path (advisor ascent; student → supervisor):
Sofia Henna Elisa Simola → Jiehua Chen: https://repositum.tuwien.at/handle/20.500.12708/225560?mode=full
Jiehua Chen → Rolf Niedermeier: https://www.ac.tuwien.ac.at/jchen/2022/04/07/memorial-rolf/ Origin: Chen identifies this exact missing case in her own joint combinatorial voter-control model with Bulteau, Faliszewski, Niedermeier and Talmon (TCS 2015; earlier MFCS 2014).

**Source.** Jiehua Chen. *Exploiting Structure in Computationally Hard Voting Problems*. Technische Universität Berlin, 2015. Advisor(s): Rolf Niedermeier. [primary source](https://depositonce.tu-berlin.de/bitstreams/01ad4a50-8834-4ecd-9607-88785af545eb/download) · [record](https://depositonce.tu-berlin.de/items/4acffe32-6224-4477-a7e0-357a6c87f7f3) Location: §6.8, printed p. 149 (PDF p. 177); Definitions 6.2–6.3, pp. 111–112; §6.4 and Table 6.1.

**Further links.** [1](https://repositum.tuwien.at/handle/20.500.12708/225560?mode=full) · [2](https://www.ac.tuwien.ac.at/jchen/2022/04/07/memorial-rolf/) · [3](https://igm.univ-mlv.fr/~bulteau/pdf/BCFNT-tcs15.pdf) · [4](https://fpt.akt.tu-berlin.de/publications/voter_control_tamc17.pdf) · [5](https://arxiv.org/abs/1701.05108)


<a id="q3472"></a>

## Q3472. Smallest B-unstable roommate instance

**Status:** Open · **Kind:** open problem · **Collection** 35

Under B preferences, what is the smallest 3n for which some instance has no stable matching (a matching with no blocking triple)?

**Context.** Origin: Thesis questions. Setup: There are 3n agents, each strictly ranking all others. A matching partitions them into triples. Under B/W preferences, an agent compares triples by her best/worst companion. A triple blocks if all three strictly prefer it to their assigned triples. Let N(M) count all nonblocking three-element subsets.

**Source.** Michael McKay. *Algorithmic Aspects of Fixed-Size Coalition Formation*. University of Glasgow, 2023. Advisor(s): David Manlove. [primary source](https://theses.gla.ac.uk/83367/3/2023McKayPhD.pdf) Location: §4.5, p. 53.

**Literature check.** Status checked 9 October 2026: Thesis retains these targets; targeted title/model/author and later-publication searches found no resolution.


<a id="q3473"></a>

## Q3473. Hardness of B-maximal stability

**Status:** Open · **Kind:** open problem · **Collection** 35

Under B preferences, is maximizing N(M) APX-hard?

**Context.** Origin: Thesis questions. Setup: There are 3n agents, each strictly ranking all others. A matching partitions them into triples. Under B/W preferences, an agent compares triples by her best/worst companion. A triple blocks if all three strictly prefer it to their assigned triples. Let N(M) count all nonblocking three-element subsets.

**Source.** Michael McKay. *Algorithmic Aspects of Fixed-Size Coalition Formation*. University of Glasgow, 2023. Advisor(s): David Manlove. [primary source](https://theses.gla.ac.uk/83367/3/2023McKayPhD.pdf) Location: §4.5, pp. 53–54.

**Literature check.** Status checked 9 October 2026: Thesis retains these targets; targeted title/model/author and later-publication searches found no resolution.


<a id="q3474"></a>

## Q3474. Three-halves W-maximal stability

**Status:** Open · **Kind:** open problem · **Collection** 35

Under W preferences, is there a polynomial-time algorithm returning M with N(M)≥(2/3) max_M′ N(M′)?

**Context.** Origin: Thesis questions. Setup: There are 3n agents, each strictly ranking all others. A matching partitions them into triples. Under B/W preferences, an agent compares triples by her best/worst companion. A triple blocks if all three strictly prefer it to their assigned triples. Let N(M) count all nonblocking three-element subsets.

**Source.** Michael McKay. *Algorithmic Aspects of Fixed-Size Coalition Formation*. University of Glasgow, 2023. Advisor(s): David Manlove. [primary source](https://theses.gla.ac.uk/83367/3/2023McKayPhD.pdf) Location: §5.4, pp. 61–62.

**Literature check.** Status checked 9 October 2026: Thesis retains these targets; targeted title/model/author and later-publication searches found no resolution.


<a id="q3475"></a>

## Q3475. Ternary symmetric justified envy

**Status:** Open · **Kind:** open problem · **Collection** 35

What is the complexity of deciding existence of a j-envy-free partition for symmetric valuations in {0,1,2}?

**Context.** Doctoral context: McKay, above. Origin: Thesis Chapter 7; joint paper. Setup: Partition 3n agents into triples; agent i has nonnegative integer values v_i(j) and utility equal to the sum over her two companions. Justified envy of j means i would strictly gain by replacing j, and both companions of j strictly prefer i to j. A partition is j-envy-free if no such pair exists. Symmetric means v_i(j)=v_j(i).

**Source.** Michael McKay, Ágnes Cseh, David Manlove. *Envy-freeness in 3D hedonic games*. 2024. [primary source](https://eprints.gla.ac.uk/319085/3/319085.pdf) Location: §5, pp. 37–38.

**Literature check.** Status checked 9 October 2026: The final 2024 article retains both questions. Targeted subsequent-result, title and correction searches found no resolution.


<a id="q3476"></a>

## Q3476. Smallest symmetric justified-envy obstruction

**Status:** Open · **Kind:** open problem · **Collection** 35

What is the smallest number 3n of agents admitting symmetric valuations but no j-envy-free partition?

**Context.** Doctoral context: McKay, above. Origin: Thesis Chapter 7; joint paper. Setup: Partition 3n agents into triples; agent i has nonnegative integer values v_i(j) and utility equal to the sum over her two companions. Justified envy of j means i would strictly gain by replacing j, and both companions of j strictly prefer i to j. A partition is j-envy-free if no such pair exists. Symmetric means v_i(j)=v_j(i).

**Source.** Michael McKay, Ágnes Cseh, David Manlove. *Envy-freeness in 3D hedonic games*. 2024. [primary source](https://eprints.gla.ac.uk/319085/3/319085.pdf) Location: §5, p. 38.

**Literature check.** Status checked 9 October 2026: The final 2024 article retains both questions. Targeted subsequent-result, title and correction searches found no resolution.

