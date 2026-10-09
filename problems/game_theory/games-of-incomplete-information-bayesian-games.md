# Games of Incomplete Information & Bayesian Games

11 problems: 11 open.

[All subjects](../README.md) · [Index by number](../INDEX.md)

| Q | Title | Status |
|---|---|---|
| [Q585](games-of-incomplete-information-bayesian-games.md#q585) | Efficient optimal cheap-talk filters beyond binary actions | Open |
| [Q586](games-of-incomplete-information-bayesian-games.md#q586) | Efficient sender-optimal filters with multiple senders | Open |
| [Q587](games-of-incomplete-information-bayesian-games.md#q587) | Polynomial-time persuasion with a privately informed binary receiver | Open |
| [Q588](games-of-incomplete-information-bayesian-games.md#q588) | Sharp regret for learning an unknown private information channel | Open |
| [Q784](games-of-incomplete-information-bayesian-games.md#q784) | Polynomial statistical dependence with hidden follower types | Open |
| [Q786](games-of-incomplete-information-bayesian-games.md#q786) | Optimal conventions robust to choosing whose advice to inspect | Open |
| [Q788](games-of-incomplete-information-bayesian-games.md#q788) | Can extra signal labels reduce binary persuasion learning regret? | Open |
| [Q789](games-of-incomplete-information-bayesian-games.md#q789) | Finite patience and information value | Open |
| [Q790](games-of-incomplete-information-bayesian-games.md#q790) | Sharp ergodic discount convergence | Open |
| [Q973](games-of-incomplete-information-bayesian-games.md#q973) | Finite versus asymptotic value of longer dialogues | Open |
| [Q974](games-of-incomplete-information-bayesian-games.md#q974) | Exact joint optimization of framing and Bayesian signals | Open |

<a id="q585"></a>

## Q585. Efficient optimal cheap-talk filters beyond binary actions

**Status:** Open · **Kind:** open problem · **Collection** 6

For one sender and at least three receiver actions, can a sender-optimal or receiver-optimal filter be computed in polynomial time from rational game data?

**Context.** Attribution: Separate questions in the TARK 2025 conclusion. Shared setup for questions 585, 586: A finite cheap-talk game has a full-support common prior p on Ω and utilities u_i(ω,a). A filter X commits to random private state observations before play; senders cannot commit to subsequent messages. The uninformed receiver acts after messages. Optimality maximizes the specified player’s payoff over Nash equilibria of the filtered game. With multiple senders, all receive the same observation and message separately.

**Source.** Itai Arieli; Ivan Geffner; Moshe Tennenholtz. *Optimal Information Design in Sender-Receiver Cheap Talk Interactions*. 2025. [primary source](https://arxiv.org/abs/2401.03671) Location: §7; §§2.1–2.3.

**Literature check.** Status for questions 585, 586, checked 5 October 2026: The November 2025 version retains both questions. No resolution located; continuous ordered-state cheap-talk results concern a different model.

**Further links.** [1](https://arxiv.org/html/2401.03671) · [2](https://sites.duke.edu/attilaambrus/files/2026/03/Optimal_Information_Structures_for_Strategic_Communication.pdf)


<a id="q586"></a>

## Q586. Efficient sender-optimal filters with multiple senders

**Status:** Open · **Kind:** open problem · **Collection** 6

For binary receiver actions and multiple senders, can a filter maximizing a specified sender’s best-equilibrium payoff be computed in polynomial time?

**Context.** Attribution: Separate questions in the TARK 2025 conclusion. Shared setup for questions 585, 586: A finite cheap-talk game has a full-support common prior p on Ω and utilities u_i(ω,a). A filter X commits to random private state observations before play; senders cannot commit to subsequent messages. The uninformed receiver acts after messages. Optimality maximizes the specified player’s payoff over Nash equilibria of the filtered game. With multiple senders, all receive the same observation and message separately.

**Source.** Itai Arieli; Ivan Geffner; Moshe Tennenholtz. *Optimal Information Design in Sender-Receiver Cheap Talk Interactions*. 2025. [primary source](https://arxiv.org/abs/2401.03671) Location: §7; §§2.1–2.3.

**Literature check.** Status for questions 585, 586, checked 5 October 2026: The November 2025 version retains both questions. No resolution located; continuous ordered-state cheap-talk results concern a different model.

**Further links.** [1](https://arxiv.org/html/2401.03671) · [2](https://sites.duke.edu/attilaambrus/files/2026/03/Optimal_Information_Structures_for_Strategic_Communication.pdf)


<a id="q587"></a>

## Q587. Polynomial-time persuasion with a privately informed binary receiver

**Status:** Open · **Kind:** open problem · **Collection** 6

With μ, utilities and ψ rational and known, is an exact optimal φ computable in polynomial input-size time?

**Context.** Attribution: Separate explicit computational and statistical questions. Shared setup for questions 587, 588: Let θ∼μ independently each round, with finite states, known full-support prior and known [0,1] utilities. Before θ, sender commits to φ(s|θ); receiver observes s and private r∼ψ(r|θ), conditionally independently given θ, then Bayesian-best-responds between two actions, favoring sender on ties. Sender observes θ and action, not r. Write V(φ,ψ) for expected sender utility.

**Source.** I. Arda Vurankaya; Ufuk Topcu. *Learning to Persuade Privately Informed Receivers*. 2026. [primary source](https://arxiv.org/abs/2607.28342) Location: Remark following Lemma 6, offline-computation paragraph; program (3).

**Literature check.** Status for questions 587, 588, checked 5 October 2026: Open in the July 2026 primary paper; no later resolution located by 2026-10-05.


<a id="q588"></a>

## Q588. Sharp regret for learning an unknown private information channel

**Status:** Open · **Kind:** open problem · **Collection** 6

With ψ unknown and |R| known, determine minimax T-dependence of regret TV\*−EΣ\_tV(φ\_t,ψ), V\*=max_φV(φ,ψ): is ~O(T^{3/4}) improvable? Assume d_min=min_θ|u^R(a₀,θ)−u^R(a₁,θ)|>0, distinct H_r={p:Σ\_θp_θψ(r|θ)[u^R(a₀,θ)−u^R(a₁,θ)]=0} after merging proportional likelihoods, and known γ>0 with ∀ action-pattern cell C ∃μ\_C∈C ∀r: |n_rᵀμ\_C|≥γ; n_r is H_r’s unit normal.

**Context.** Attribution: Separate explicit computational and statistical questions. Shared setup for questions 587, 588: Let θ∼μ independently each round, with finite states, known full-support prior and known [0,1] utilities. Before θ, sender commits to φ(s|θ); receiver observes s and private r∼ψ(r|θ), conditionally independently given θ, then Bayesian-best-responds between two actions, favoring sender on ties. Sender observes θ and action, not r. Write V(φ,ψ) for expected sender utility.

**Source.** I. Arda Vurankaya; Ufuk Topcu. *Learning to Persuade Privately Informed Receivers*. 2026. [primary source](https://arxiv.org/abs/2607.28342) Location: Conclusion; Assumptions 1–3 and Theorem 1; equation (4).

**Literature check.** Status for questions 587, 588, checked 5 October 2026: Open in the July 2026 primary paper; no later resolution located by 2026-10-05.


<a id="q784"></a>

## Q784. Polynomial statistical dependence with hidden follower types

**Status:** Open · **Kind:** open problem · **Collection** 8

In repeated Bayesian Stackelberg games with L leader actions, n followers, K types per follower and A follower actions, can action-only feedback achieve expected regret poly(n,K,L,A)√T (up to logarithms) against the optimal fixed leader mixture? Types are drawn i.i.d. each round from an unknown possibly correlated joint distribution; payoffs are known, each follower myopically best responds without inter-follower externalities, and ties favor the leader. Computational time may be exponential in L; the question concerns regret dependence.

**Context.** Attribution: Explicit question in the primary work.

**Source.** Gerson Personnat; Tao Lin; Safwan Hossain; David C. Parkes. *Learning to Play Multi-Follower Bayesian Stackelberg Games*. 2025. [primary source](https://arxiv.org/abs/2510.01387) Location: §5, after Corollary 5.1.

**Literature check.** Status for question 784, checked 5 October 2026: Explicitly open in the ICLR 2026 paper; no later resolution located.

**Further links.** [1](https://openreview.net/pdf?id=8hMaqBagPd) · [2](https://tao-l.github.io/)


<a id="q786"></a>

## Q786. Optimal conventions robust to choosing whose advice to inspect

**Status:** Open · **Kind:** open problem · **Collection** 8

For a rational finite normal-form game with a fixed number n of players, what is the complexity of maximizing expected social welfare over anonymous linear correlated equilibria? Such an equilibrium is a distribution μ over mixed profiles x, satisfying E_μ[u_i(φ\_i(x),x_{−i})−u_i(x)]≤0 for every player i and every linear map φ\_i:∏\_jΔ(A_j)→Δ(A_i). Exact or additive-ε optimum should have an explicit bit/precision complexity. Restricting μ to pure profiles changes the problem.

**Context.** Doctoral connection: Brian Hu Zhang; dissertation and supervision listed under question 781. Attribution: Joint doctoral paper; repeated in Zhang’s thesis.

**Source.** Brian Hu Zhang; Ioannis Anagnostides; Emanuel Tewolde; Ratip Emin Berker; Gabriele Farina; Vincent Conitzer; Tuomas Sandholm. *Expected Variational Inequalities*. 2025. [primary source](https://arxiv.org/abs/2502.18605) Location: Appendix E, after Proposition E.4.

**Literature check.** Status for question 786, checked 5 October 2026: Optimal-value question retained; efficient existence algorithms do not resolve it.

**Further links.** [1](https://openreview.net/pdf?id=LCbHsdtvOR) · [2](https://arxiv.org/abs/2605.17665) · [3](https://brianhzhang.github.io/thesis.pdf)


<a id="q788"></a>

## Q788. Can extra signal labels reduce binary persuasion learning regret?

**Status:** Open · **Kind:** open problem · **Collection** 8

In repeated persuasion with two receiver actions, known bounded sender/receiver payoffs and an unknown full-support prior μ, what is the optimal regret order if the designer may use more than two signals per round? The receiver knows μ, updates by Bayes’ rule and best responds; the designer sees only the signal and chosen action. States are i.i.d.; retain the known positive prior lower bound and non-dominated-action assumption. Regret is T·OPT(μ) minus cumulative expected sender utility. The Ω(log log T) lower bound currently assumes two signals, even with two states.

**Context.** Attribution: Explicit question in the primary work.

**Source.** Ce Li; Tao Lin. *Information Design with Unknown Prior*. 2024. [primary source](https://arxiv.org/abs/2410.05533) Location: Theorem 4 and footnote 2.

**Literature check.** Status for question 788, checked 5 October 2026: The September 2025 revision retains this signal-alphabet qualification; no later resolution located.

**Further links.** [1](https://tao-l.github.io/pub_conference/2025-unknown-prior/) · [2](https://www.bu.edu/econ/files/2025/10/BU-Placement-Brochure-2025_26.pdf)


<a id="q789"></a>

## Q789. Finite patience and information value

**Status:** Open · **Kind:** open problem · **Collection** 8

An informed sender commits to signals about a finite irreducible Markov chain M. A myopic Bayesian receiver, with finite actions or [0,1], breaks ties for the sender. Let v_δ(q)=sup_σE[(1−δ)Σ\_nδ^(n−1)u(p_n)], where p_n is its posterior and u≥0 is upper-semicontinuous. For invariant π and point-masses e_k, set Φ(δ)=v_δ(π), Ψ(δ)=Σ\_kπ\_kv_δ(e_k). Can Φ>Ψ below some δ₀∈(0,1), with Φ(δ₀)=Ψ(δ₀)?

**Context.** Attribution: Two explicit questions in the primary paper.

**Source.** Dimitry Shaiderman. *On the Monotonicity and Rate of Convergence of the Markovian Persuasion Value*. 2025. [primary source](https://arxiv.org/abs/2512.06794) Location: §3.2.1, Corollary 1.

**Literature check.** Status for questions 789, 790, checked 5 October 2026: Source-stated questions; no later resolution located.

**Further links.** [1](https://pubsonline.informs.org/doi/10.1287/moor.2023.0296)


<a id="q790"></a>

## Q790. Sharp ergodic discount convergence

**Status:** Open · **Kind:** open problem · **Collection** 8

For finite zero-sum Markov-chain games with an exogenous irreducible aperiodic transition matrix M, determine the sharp worst-case order, as δ↑1, of sup_q|V_δ(q)−V_∞|. Player 1 observes the current state and hence the payoff matrix; Player 2 does not. Actions are simultaneous and then public; only Player 1 observes the realized payoff. The known uniform bound is O((1−δ)log²(1/(1−δ))), with game-dependent constants. Is the logarithmic loss necessary, and how does the sharp bound depend on mixing?

**Context.** Attribution: Two explicit questions in the primary paper.

**Source.** Dimitry Shaiderman. *On the Monotonicity and Rate of Convergence of the Markovian Persuasion Value*. 2025. [primary source](https://arxiv.org/abs/2512.06794) Location: §3.4, Theorem 5.

**Literature check.** Status for questions 789, 790, checked 5 October 2026: Source-stated questions; no later resolution located.

**Further links.** [1](https://pubsonline.informs.org/doi/10.1287/moor.2023.0296)


<a id="q973"></a>

## Q973. Finite versus asymptotic value of longer dialogues

**Status:** Open · **Kind:** open problem · **Collection** 10

With binary types and arbitrary finite actions, characterize finite attainment of sup_T W_T, stopping-round bounds, and otherwise the convergence rate. Is the finite/asymptotic case efficiently decidable?

**Context.** Attribution: September 2026 v5, §4 “Beyond binary actions” and §5. Shared setup for question 973: Independent finite private types have known rational priors/payoffs and an explicit finite Alice-action menu. Committed speakers alternate type/transcript-dependent public messages, Bob last. Only Alice acts afterward, best responding, ties favoring Bob. Every Bob type’s payoff conditional on each terminal transcript must be at least its no-communication baseline. Optimize expected total utility. Write W_T for optimal T-message welfare.

**Source.** Renato Paes Leme; Jon Schneider; Heyang Shang; Shuran Zheng. *Bayesian Conversations*. 2026. [primary source](https://arxiv.org/abs/2307.08827v5) Location: §4 “Beyond binary actions”; §5 second limitation; Theorem 4.2.

**Literature check.** Status for question 973, checked 5 October 2026: Current v5 leaves this finite-versus-asymptotic extension open; no later resolution located.

**Further links.** [1](https://heyangshang.github.io/) · [2](https://www.renatoppl.com/)


<a id="q974"></a>

## Q974. Exact joint optimization of framing and Bayesian signals

**Status:** Open · **Kind:** open problem · **Collection** 10

For rational μ₀, u, v, determine the exact complexity of max_(μ∈ΔΩ,π)Σμ₀(ω)π(a|ω)u(a,ω), subject to stochasticπ and Σμ(ω)π(a|ω)[v(a,ω)−v(a′,ω)]≥0 for all a, a′. General state-dependent u is essential; all receiver actions are strictly inducible.

**Context.** Attribution: Named full-simplex case of the explicit joint-complexity question. Shared setup for question 974: Finite states Ω and actions A have known rational payoffs; ties favor the sender. The sender chooses a state-independent framing inducing receiver priorμ, then a state-contingent action recommendationπ. Actual states use sender priorμ₀; the receiver updates the induced prior by Bayes and follows an obedient recommendation. All receiver actions are strictly inducible by some belief, as assumed in §2.

**Source.** Paul Dütting; Safwan Hossain; Tao Lin; Renato Paes Leme; Sai Srivatsa Ravindranath; Haifeng Xu; Song Zuo. *Information Design With Large Language Models*. 2026. [primary source](https://arxiv.org/abs/2509.25565v2) Location: §4.2 Eq.(8), Theorem 3; §6.

**Literature check.** Status for question 974, checked 5 October 2026: March 2026 source leaves exact joint complexity open; its exact theorem assumes state-independent u.

**Further links.** [1](https://www.renatoppl.com/) · [2](https://safwanhossain.github.io/files/framing.pdf) · [3](https://tao-l.github.io/files/Non-Bayesian-Info-Design-2026-1.pdf)

