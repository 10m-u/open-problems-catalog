# Thesis statements: Optimization & Operations Research

Discipline: Mathematics. 199 statements from 52 theses. [All subjects](../README.md)

Automatically extracted, not reviewed: OCR noise and fragments are common, and a passage may describe a problem that is now solved. Always check the thesis page cited.

## Altschuler, Jason (Jason M.) (2018)

*Greed, hedging, and acceleration in convex optimization* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/d482e1ec-d62b-4eeb-a233-cca937ed0666/content) · [record](https://dspace.mit.edu/handle/1721.1/120409)

- *stated as open* (p. 97): infinite-horizon setting n = 00 [Nemirovskii and Yudin, 19831, but it is an open question for any n E N (more details about the relevant literature shortly).
- *stated as open* (p. 97): Second, this shows as an immediate corollary that randomization does not help (possibly adaptive) Krylov-subspace algorithms for any finite number of iterations, settling the open question discussed in Subsection 2.
- *stated as open* (p. 102): Proof sketches Moreover, since these quadratic functions were hard regardless of the randomization and adaptivity of the algorithm, we get as an immediate corollary that neither randomization nor adaptivity helps Krylov-subspace algorithms for any finite number of iterations, settling the open problem mentioned in Subsection 2.
- *stated as open* (p. 103): Second, this shows an immediate corollary that randomization does not help (possibly adaptive) Krylov-subspace algorithms for any finite number of iterations, settling the open question discussed in Subsection 2.
- *stated as open* (p. 104): This settles the open problem mentioned in Subsection 2.
- **Conjecture 5.22** (p. 119): Consider the notation of Theorem 5.21. The rate (5.18) is strictly larger than Racc if the orthogonal polynomials corresponding to P do not have asymptotically regular growth behavior. We also conjecture that asymptotically regular root-distribution behavior is both necessary and sufficient for the quadratic function to be asymptotically optimal. This seems somewhat reasonable in light of our characterizations of optimal Krylov-subspace algorithms in Theorems 3.13 and 3.21. Note that by
- **Conjecture 5.23** (p. 119): Consider the notation of Theorem 5.21. The rate (5.18) is equal to Racc if and only if the the orthogonal polynomials corresponding to v have asymptotically regular growth behavior, and otherwise is strictly greater than Racc.
- *proposed (author conjectures or asks)* (p. 119): First, we conjecture that the converse is true, stated formally below.
- *stated as open* (p. 131): Indeed, it is a fundamental open question whether there is a complexity gap between these two problems.

## Altschuler, Jason M. (2022)

*Transport and Beyond: Efficient Optimization over Probability Distributions* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/11d844d8-16cf-4447-9fd7-2d2afdbb6d14/content) · [record](https://dspace.mit.edu/handle/1721.1/150436)

- *stated as open* (p. 25): Despite the recent introduction of several algorithms with good empirical performance, it is unknown whether general Optimal Transport distances can be approximated in near-linear time.
- *stated as open* (p. 27): In particular, the existence of algorithms to compute or approximate general OT distances in time nearly linear in the input size n2 is an open question.
- *proposed (author conjectures or asks)* (p. 39): We conjecture that this is related to the fact that GREENKHORN only updates salient rows and columns at each step, whereas SINKHORN wastes time updating rows and columns corresponding to background pixels, which have negligible impact.
- *stated as open* (p. 46): Two remaining open questions that this chapter seeks to address are: 4We assume throughout that the diagonal of K is zero.
- *stated as open* (p. 47): 1) addresses the two open questions above by showing that a simple random variant of the ubiquitously used Osborne’s algorithm has runtime that is (i) near-linear in the input sparsity m, and also (ii) linear in the inverse accuracy ε−1 for well-connected inputs.
- *stated as open* (p. 56): 9 concludes with several open questions.
- *stated as open* (p. 80): 9 Discussion We conclude with several open questions: 1.
- *stated as open* (p. 81): (This is the analog to the third open question in [198, §6] for Max-Balancing.
- **Conjecture 5.6.3** (p. 133): Assuming P̸ = NP, there is no poly(n, k)-time algorithm solving MOTC with the Coulomb potential cost (5.7). In this section, we make progress towards the conjecture by proving hardness of DFT with the related Coulomb-Buckingham potential, which is similar to the Coulomb potential, but has extra energy terms that grow as 1/r6 and exp(−Θ(r)). The Coulomb-Buckingham potential is popular for modeling the structures of ionic crystals [1], and is defined for two particles at distance r with charges q1, q2 ∈{−1, +1} as: U(r, q1, q2) = ( M, r = 0 Aq1q2 exp(Bq1q2r) − Cq1q2 r6 + q1q2 r , r > 0 , where A+1, A−1, B+1, B−1, C+1, C−1 are constants determining the relative strengths of the terms in the interaction, and M > 0 is a large constant (that should be intuitively thought of as infinite) penalizing two ions being in the same place. Given ions with charges qj ∈{−1, +1} at positions xj ∈R3, the corresponding MOT cost is given by: Cj1,...,jk = ( M, P i∈[k] qji̸ = 0 P 1⩽i&lt;i′⩽k U(∥xji −xji′∥2, qji, qji′), P i∈[k] qji = 0 . (5.8)
- *proposed (author conjectures or asks)* (p. 133): We conjecture that in fact solving MOT with the Coulomb potential is NP-hard.
- *stated as open* (p. 139): However, the number of MOT problems that are known to be solvable in polynomial time is small, and it is unknown if these techniques can be extended to the many other MOT problems arising in applications.
- *stated as open* (p. 148): 1), this generalizes the previously open problem of approximately computing the smallest entry of a constant-rank tensor with nk entries in poly(n, k) time.
- *stated as open* (p. 148): 3It is an interesting open question if the MIN oracle can similarly be implemented in poly(n, k) time.
- *stated as open* (p. 201): It is unknown if there is a practically efficient implementation of the SMINC,S oracle (and thus of SINKHORN) for both best-case or worst-case reliability.
- *stated as open* (p. 204): Second, it is an interesting open question if the poly(n, k, Cmax/ ε) runtime for the ε-approximate AMINC oracle can be improved to poly(n, k, log(Cmax/ ε)), as this would imply a poly(n, k) runtime for the MINC oracle and thus for this class of MOT problems (see also Footnote 3 in the introduction).
- **Open problem** (p. 254): computing barycenters in polynomial time. A key issue that determines how useful Wasserstein barycenters are in applications is whether they can be computed efficiently. Note that in most computational applications, each measure μi is a discrete distribution: it is a “point cloud” over data points. This motivates the following fundamental question, which has remained open despite considerable research attention (see the previous work section). Are Wasserstein barycenters of discrete distributions computable in polynomial time? That is, can the optimization problem (7.1) be solved in time that is polynomial in the number of distributions k, the dimension d, the maximum support size n of the input distributions μi, and the bit complexity log U of each entry in the input measures and weights? This constitutes a running time that is polynomial in the input size since each discrete measure is naturally described as a list of at most n point locations and the corresponding probability masses.
- *stated as open* (p. 254): Open problem: computing barycenters in polynomial time.
- *stated as open* (p. 255): Introduction 205 A highly related open problem is whether Wasserstein barycenters can be computed to high accuracy, i.

## Amir Ali Ahmadi (2008)

*Non-monotonic Lyapunov functions for stability of nonlinear and switched systems : theory and computation* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/0020c40c-80d1-4f2b-bb1c-4394ddfe51e8/content) · [record](https://dspace.mit.edu/handle/1721.1/44206)

- **Conjecture 5.2.1** (p. 75): Suppose A is a 2 × 2 Hurwitz matrix. Then there always exist scalars τ1 ≥0 and τ2 ≥0 such that τ2(A3 + 3ATA2 + 3AT 2A + AT 3) + τ1(A2 + 2ATA + AT 2) + (A + AT) ≺0. We have evidence to believe that this conjecture is true. If we succeed in proving this conjecture it would imply that instead of searching for the three free parameters of a 2 × 2 positive definite symmetric matrix P such that V (x) = xTPx decreases monotonically along trajectories, one can always fix P = I and search for the two unknowns τ1 and τ2 in (5.11). The natural extension of this conjecture would be that when x ∈Rn, instead of searching for 1 2n(n+1) entries of P as in standard Lyapunov theory, it is enough to fix P = I and search for n unknown coefficients multiplying derivatives of order up to n + 1. Although from a practical point of view this is not so significant2, the result is of theoretical interest. We know that the stability of a continuous time linear system is completely determined by the real part of its n eigenvalues. In that sense, it makes intuitive sense that one should be able to reduce the free parameters of a quadratic Lyapunov function to n numbers. — **proved here** ([details](../../solutions/catalog-research/quick-closures.md))

## Aylward, Erin M (2006)

*Robust stability and contraction analysis of nonlinear systems via semidefinite optimization* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/ba5009d9-ec5c-4819-89c0-cfad4283a6f9/content) · [record](https://dspace.mit.edu/handle/1721.1/37850)

- *stated as open* (p. 78): At this point, we do not know if the full converse of Lemma 26 holds.

## Chaitanya Bandi (2013)

*Tractable stochastic analysis in high dimensions via robust optimization* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/918443d0-ca25-44c8-82fa-e5c5a0c3492a/content) · [record](https://dspace.mit.edu/handle/1721.1/82870)

- *stated as open* (p. 3): Correspondingly, some of its major areas of application remain unsolved when the underlying systems become multidimensional: Queueing networks, auction design in multi-item, multi-bidder auctions, network information theory, pricing multi-dimensional financial contracts, among others.
- *stated as open* (p. 17): If the distribution of interarrival and service times is not exponential, we do not know how to calculate this expectation exactly, and two avenues available to make progress are simulation and approximation.
- *stated as open* (p. 32): However, "for GI/GI/m, (m > 1), stochastic network calculus based analysis remains plain blank" and "feedback analysis is perhaps the most critical open challenge for stochastic network calculus", as remarked by Jiang [2012].
- *stated as open* (p. 70): While the analysis of the GI/GI/m queue is still an open problem under traditional queueing theory, we proposed an uncertainty
- *stated as open* (p. 75): The more general problem, however, remains open in the setting of public budget constraints under probabilistic assumptions.
- *stated as open* (p. 77): Under this approach, it is desirable to identify the right kind of performance benchmarks, but this problem is still open.
- *stated as open* (p. 128): in Verdu and McLaughlin [1998], the capacity region of even the simplest twouser memoryless Gaussian interference channel remains an open problem.

## Chaoxu Tong (2016)

*Some Resource Allocation Problems* · [thesis](https://ecommons.cornell.edu/server/api/core/bitstreams/a43a5774-5594-4790-a248-8842a82e55cf/content) · [record](https://ecommons.cornell.edu/handle/1813/43582)

- *stated as open* (p. None): [43] extends the model proposed by [1] to cover the case where each customer makes a choice among the itineraries that are open for sale.
- *stated as open* (p. None): One particularly notable open problem is to derive good algorithms for the setting in which the opening/ordering costs are submodular set functions of the set of demand points assigned (or for suitably general special cases).

## Chen, Annie I-An (2012)

*Fast distributed first-order methods* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/e7f5b067-65e6-4f8e-89c2-d435d6fec806/content) · [record](https://dspace.mit.edu/handle/1721.1/75628)

- *stated as open* (p. 50): It is an open question as to what condition is required of the weight matrix so as to guarantee this performance.

## Colin Pawlowski (2019)

*Machine learning for problems with missing and uncertain data with applications to personalized medicine* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/9a8017a8-f50e-4405-9b66-25acb4ddce5f/content) · [record](https://dspace.mit.edu/handle/1721.1/122473)

- *proposed (author conjectures or asks)* (p. 22): ∙We formulate the problem of predicting drug response as the problem of tensor completion with noisy side information.
- *stated as open* (p. 29): Without extensive computational experiments, we do not know if these robust classifiers yield gains in out-of-sample accuracy in practice, especially in comparison with regularized methods.
- *stated as open* (p. 125): Given the optimization formulations introduced in this work, there are multiple open questions for future research.
- *stated as open* (p. 126): 1) fast and accurately for any of the three examples of non-convex, non-linear cost functions c(U, W, V; X) remains an open question.
- *proposed (author conjectures or asks)* (p. 135): We formulate the problem of missing data imputation with time series information under the MedImpute framework, extending the OptImpute framework proposed in
- *proposed (author conjectures or asks)* (p. 166): 2, we state the problem of tensor completion with noisy side information.
- *proposed (author conjectures or asks)* (p. 168): 2 Tensor Completion Problem In this section, we state the problem of tensor completion with noisy side information.

## Cory-Wright, Ryan (2022)

*Integer and Matrix Optimization: A Nonlinear Approach* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/63075b44-eef7-4ab2-8653-6b892585d109/content) · [record](https://dspace.mit.edu/handle/1721.1/144644)

- *stated as open* (p. 214): It is, however, an open question whether a weaker notion than matrix convexity could ensure the joint convexity of tr(gf).

## Dan Stratila (2009)

*Combinatorial optimization problems with concave costs* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/e650fcb6-274f-43fd-b176-c6aeb74e5c43/content) · [record](https://dspace.mit.edu/handle/1721.1/46661)

- *stated as open* (p. 31): On the other hand, it is an interesting open question to find out the minimum number of required pieces when E is not fixed and may be arbitrarily close to zero, at least to within a constant factor.
- *stated as open* (p. 37): An interesting open question is to find upper and lower bounds on the number of required pieces that are tight, or tight within a constant factor as e -+ 0.
- *stated as open* (p. 81): Bridging the gap between our technique and the lower bound is an interesting open question arising from Chapter 2.
- *stated as open* (p. 82): An interesting open question arising out of Chapter 3 is to develop a technique for obtaining algorithms that operate directly on concave cost problems based on LP rounding algorithms for combinatorial optimization problems.

## Daniel Fleischman (2016)

*Computational Approaches For Hard Discrete Optimization Problems* · [thesis](https://ecommons.cornell.edu/server/api/core/bitstreams/bd8aa6cc-00b4-4a7d-96b1-3240d23aacd3/content) · [record](https://ecommons.cornell.edu/handle/1813/45162)

- *proposed (author conjectures or asks)* (p. None): We conjecture that Armbruster’s code actually uses W+ ≤(1+ε)W/2 (without the ceiling).

## Daniel Freund (2018)

*Models and Algorithms for Transportation in the Sharing Economy* · [thesis](https://ecommons.cornell.edu/server/api/core/bitstreams/7d8a8940-48d2-4848-a93b-a72dad7bc775/content) · [record](https://ecommons.cornell.edu/handle/1813/59625)

- *stated as open* (p. None): A few of these problems were tackled in this thesis, but many others are yet unsolved.
- *stated as open* (p. None): Below, we list a number of open questions, some of theoretical interest, some of practical interest, that remain unanswered.
- *stated as open* (p. None): An obvious open question seeks to improve the approximation guarantee or prove the current guarantee is the best possible.

## Das Gupta, Shuvomoy (2024)

*Advances in Computer-Assisted Design and Analysis of First-Order Optimization Methods and Related Problems* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/dee1e38c-5da9-4064-a841-384b4a8ec368/content) · [record](https://dspace.mit.edu/handle/1721.1/155495)

- *proposed (author conjectures or asks)* (p. 30): We formulate the problem of finding the optimal optimization method as a nonconvex quadratically constrained quadratic problem (QCQP).
- **Conjecture 2.1** (p. 95): The optimal FSFOM for reducing gradient of smooth nonconvex functions satisfies min i∈[0:N] ∥∇f(xi)∥2 ≤6 √ 3L(f(x0) −f⋆) 8N + 3 √
- *proposed (author conjectures or asks)* (p. 146): In this PEP approach, we formulate the problems of computing the worst-case ratios of f(xk+1)−f⋆/f(xk)−f⋆as the following optimization problem:                   maximize f,n,xk,xk+1,dk,dk+1, γk,βk f(xk+1)−f⋆ f(xk)−f⋆ subject to n ∈N, f ∈Fμ,L(Rn), dk, xk ∈Rn, ⟨∇f(xk) | dk⟩= ∥∇f(xk)∥2, ∥dk∥2 ≤c∥∇f(xk)∥2, (xk+1, dk+1, βk) generated by (M) from xk and dk.
- *proposed (author conjectures or asks)* (p. 147): 2 Computing worst-case search directions In this section, we formulate the problems of computing the worst-case ratios of ∥dk∥/∥∇f(xk)∥.

## David Brown (2006)

*Risk and robust optimization* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/b2608715-d85d-4f89-b14c-a05a73de87b7/content) · [record](https://dspace.mit.edu/handle/1721.1/37894)

- *stated as open* (p. 23): Finally, Chapter 6 considers the multi-stage problem with linear systems and quadratic costs, and Chapter 7 concludes the thesis and presents a summary of the results as well as important, open questions for future research.
- *stated as open* (p. 131): Quantifying the tightness of this inner approximation is an open question of interest.
- *stated as open* (p. 195): 7 Conclusions A primary open question of interest is how to simplify this approach even further in the presence of constraints.
- *stated as open* (p. 195): Finally, an open question is if there are classes of constrained LQC problems for which a certainty equivalence principle holds.
- *stated as open* (p. 197): There are a number of open problems related to these ideas which demand further research efforts.
- *stated as open* (p. 197): 1 Open theoretical questions The following problems represent some of the critical open problems related to the theory developed in this thesis.
- *stated as open* (p. 200): An interesting, open problem is developing an axiomatized description of risk measures in a dynamic setting (e.

## Eoin O'Mahony (2015)

*Smarter Tools For (Citi)Bike Sharing* · [thesis](https://ecommons.cornell.edu/server/api/core/bitstreams/af2eaec5-8ee2-4f6e-80d1-a72d3830c42f/content) · [record](https://ecommons.cornell.edu/handle/1813/40922)

- *proposed (author conjectures or asks)* (p. None): Using these observations, we formulate the problem as trying to find a set of truck routes that rebalances as much of the system as possible in the time available.
- *stated as open* (p. None): 2 Open Questions and Future Directions Bike-sharing and the wider domain of vehicle sharing present a vast number of interesting, relevant and worthwhile problems.
- *stated as open* (p. None): There are a number of open problems related to the models presented in this paper.
- *proposed (author conjectures or asks)* (p. None): Similarly we conjecture that the linear relaxation of the capacity placement integer program presented in Chapter 3 is integral.

## Fallah, Alireza (2023)

*Algorithmic Interactions With Strategic Users: Incentives, Interplay, and Impact* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/24011594-1bc9-4e3e-941d-c4d83cea5f3b/content) · [record](https://dspace.mit.edu/handle/1721.1/152735)

- *stated as open* (p. 20): Another line of work tackles the open question posed by Ghosh and Roth [2011] on whether a model with distributional assumption on users’ costs and Bayesian mechanism design approach could be used to develop optimal mechanism for collecting data with privacy guarantees.

## Gwen Spencer (2012)

*Approximation Algorithms For Stochastic Combinatorial Optimization, With Applications In Sustainability* · [thesis](https://ecommons.cornell.edu/server/api/core/bitstreams/772e21f1-8a93-4b80-8d9c-5d484aab61d9/content) · [record](https://ecommons.cornell.edu/handle/1813/31423)

- **Conjecture 4.6.1** (p. None): There is a deterministic, polynomial-time algorithm that, given a metric space (X, δ) with |X| = n, produces a master tour τ with ρ(X, δ, τ) = O(log n). Several interesting avenues for future work are also suggested by Theorem 4.5.2. A natural question is whether any general relationship holds between universal lower bounds and a priori approximation ratios for randomized algorithms. If the number of samples is allowed to depend on, for example, the inverse probability of the least commonly occurring active set, is it still possible to prove some kind of universal-to-a-priori lower bound translation in the spirit of Theorem 4.5.2? We note that in the case of 2-stage build-with-recourse stochastic optimization models (see [24]), most algorithms yielding a constant approximation ratio rely on either nice properties of the objective function (such as submodularity) or strong bounds on the inflation of the cost function in the recourse stage;
- *proposed (author conjectures or asks)* (p. None): Working towards this conjecture, Hajiaghayi, Kleinberg & Leighton showed in [25] that any master tour of the vertices of the n × n grid has its competitive ratio bounded by Ω( 6p log n/ log log n).
- *stated as open* (p. None): 6 Open problems The conjecture of Bertsimas & Grigni [7] that the lower bound of Ω(log n) holds even for finite subsets of the plane remains open.
- *proposed (author conjectures or asks)* (p. None): We conjecture that this expected guarantee for a fixed S can be matched by a deterministic guarantee for all S.

## Hamza Fawzi (2016)

*Power and limitations of convex formulations via linear and semidefinite programming lifts* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/15996193-cf3a-48c4-8355-e8df85439a62/content) · [record](https://dspace.mit.edu/handle/1721.1/107331)

- *proposed (author conjectures or asks)* (p. 77): We will prove this conjecture in the next chapter (see Theorem 26).
- *stated as open* (p. 152): Comments and open questions We see from Table 6.
- *stated as open* (p. 152): There are several open questions concerning acv, that it would be interesting to explore further:

## Harris, Mitchell (2025)

*Computational Tradeoffs and Symmetry in Polynomial Nonnegativity* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/8d162f8a-f7fa-4660-9654-6d0e7d0efe19/content) · [record](https://dspace.mit.edu/handle/1721.1/159891)

- *stated as open* (p. 62): An open question is whether there are other reasonable low-complexity choices for the decision variables (that may violate the hypotheses of Proposition 2.
- *stated as open* (p. 77): Finally, a problem affecting convergence of any infeasible method is that it is unknown how many constraints are active at optimality.
- *stated as open* (p. 274): We leave this as an open question: Which polynomials have Gram matrices supported on each Nj?
- *stated as open* (p. 313): Several important questions remain open, particularly the characterization of polynomials whose Gram matrices are supported within specific irreducible subspaces.

## Huizhen Yu (2006)

*Approximate solution methods for partially observable Markov and semi-Markov decision processes* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/3d103fc4-e6b9-42fc-8764-de9df4effc91/content) · [record](https://dspace.mit.edu/handle/1721.1/35299)

- *stated as open* (p. 27): We do not know if the optimal limsup function is necessarily concave.
- *stated as open* (p. 122): Similar to the case of POMDPs, there are many open questions relating to the average cost POSMDP problem.

## Janice Hammond (1985)

*Solving asymmetric variational inequality problems and systems of equations with generalized nonlinear programming algorithms* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/71e7378e-1442-4266-99ee-a75dcaaebf7a/content) · [record](https://dspace.mit.edu/handle/1721.1/89244)

- *stated as open* (p. 181): The convergence of the generalized Frank-Wolfe method and the fictitious play algorithm for problems defined over polyhedral sets remain important open problems.

## Jean Pauphilet (2020)

*Algorithmic advancements in discrete optimization : applications to machine learning and healthcare operations* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/48839185-8d7e-4da5-93fb-a660ce5ae5b5/content) · [record](https://dspace.mit.edu/handle/1721.1/127298)

- *proposed (author conjectures or asks)* (p. 33): Second, we formulate the problem as a multi-stage robust decision problem so as to inform the first-stage decisions with future bed requests and discharges.
- *stated as open* (p. 234): Defining how to properly value implementation in academic research remains an open question and a critical challenge for our community.

## Koduri, Nihal (2021)

*Essays on Decision Making Under Uncertainty* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/7ec3a8a4-522e-4505-a941-443d22042945/content) · [record](https://dspace.mit.edu/handle/1721.1/139032)

- *stated as open* (p. 335): 3 discusses one aspect of the methodology that address an important open problem from Bertsimas and Koduri (2021).

## Lamperski, Jourdain Bernard. (2020)

*Structural and algorithmic aspects of linear inequality systems* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/94dce0e7-9a12-47ba-bd16-0511e0cbe81b/content) · [record](https://dspace.mit.edu/handle/1721.1/128971)

- *stated as open* (p. 3): This addresses an open question that is motivated by the idea that such local structure could be leveraged algorithmically to develop faster algorithms or a strongly polynomial algorithm.
- *stated as open* (p. 15): For example, it is not known if there is a strongly polynomial time algorithm that decides if a linear inequality system is feasible or not.
- *stated as open* (p. 15): That is, it is not known if there is an algorithm that decides if a linear inequality system is feasible (or not) in a number of operations that is bounded above by a polynomial in the number of variables and constraints of the system [43].
- *stated as open* (p. 17): Although Khachiyan established the existence of a weakly polynomial time algorithm, it is still not known if there is an algorithm that decides if a linear inequality system is feasible in strongly polynomial time.
- *stated as open* (p. 19): 2 Unique sink orientations for homogeneous linear inequality systems As briefly mentioned earlier, it is still not known if there is an algorithm that solves linear inequality systems in strongly polynomial time.
- *stated as open* (p. 22): It is known that the conjecture holds for totally balanced (or chordal bipartite) graphs, which are balanced graphs that do not contain a hole of length greater than 4, but as noted by Conforti and Rao [13], it is not known whether the conjecture holds for linear balanced graphs, which are balanced graphs that do not contain a hole of length 4.
- *stated as open* (p. 97): 1 Introduction As mentioned in Chapter 1, it is not known if there is an algorithm that solves linear inequality systems in strongly polynomial time.
- **Conjecture 4.1.1** (p. 131): Every balanced graph Gcontains an edge esuch that G∖eis balanced.
- **Conjecture 4.1** (p. 132): 1 is clearly equivalent to:
- **Conjecture 4.1.2** (p. 132): Every balanced graph contains an edge that is not the unique chord of a cycle. It is known that the Conjecture 4.1.2 holds for totally balanced (or chordal bipartite) graphs, which are balanced graphs that do not contain a hole of length greater than 4, because every totally balanced graph contains a bisimplicial edge, see [26]. On the other hand, as noted in [13], it is not known if the conjecture holds for linear balanced graphs, which are balanced graphs that do not contain a hole of length 4. We make progress on Conjecture 4.1.2 and show that it holds for balanced graphs that do not contain a uniquely-chorded cycle with one and only one hole of length 4, which we will call moderately balanced graphs.

## Li, Michael Lingzhi (2022)

*Algorithms for Large-scale Data Analytics and Applications to the COVID-19 Pandemic* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/335672dc-13f3-4729-97bb-f66655afc1d0/content) · [record](https://dspace.mit.edu/handle/1721.1/143205)

- *stated as open* (p. 134): However, a question remains open: how to plan vaccine distribution across populations, that is, how to allocate a limited vaccine supply across communities, across provinces, and even across countries?

## Ma, Yu (2025)

*Artificial Intelligence for System Medicine: Methods and Applications* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/414e9bb2-e78e-4db3-bd03-b50918ab61fa/content) · [record](https://dspace.mit.edu/handle/1721.1/159920)

- *proposed (author conjectures or asks)* (p. 127): Because the optimal ensemble is trained to replicate the ground truth even more closely, we conjecture that it is more susceptible to intra-observer variability and, thus, is less robust across physicians and may be more biased toward the contouring of those samples.

## Marcucci, Tobia (2024)

*Graphs of Convex Sets with Applications to Optimal Control and Motion Planning* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/4923a7cf-9676-4f75-b614-0c731d4cfb39/content) · [record](https://dspace.mit.edu/handle/1721.1/156598)

- *stated as open* (p. 11): However, the efficient blending of discrete and continuous decision making remains an open challenge.
- *proposed (author conjectures or asks)* (p. 69): We formulate the problem just described as an SPP in GCS.
- *proposed (author conjectures or asks)* (p. 75): We formulate the problem above as an FLP in GCS.

## Maurice Cheung (2012)

*Lp-Based Approximation Algorithms For Scheduling And Inventory Management Problems* · [thesis](https://ecommons.cornell.edu/server/api/core/bitstreams/50bcc232-63f4-4a7a-afbd-fc95cc8b3515/content) · [record](https://ecommons.cornell.edu/handle/1813/31470)

- *stated as open* (p. None): 67 4 Conclusion and Open Problems 71 Bibliography 74 vii CHAPTER 1 INTRODUCTION 1.
- *stated as open* (p. None): It is an interesting open question to improve the efficiency of the primal-dual scheduling algorithm.
- *stated as open* (p. None): 70 CHAPTER 4 CONCLUSION AND OPEN PROBLEMS In this thesis, we develop LP-based approximation algorithms for problems in scheduling and inventory management.
- *stated as open* (p. None): Here we mention several open problems related to the work in this thesis: • Is there an approximation algorithm with better performance guarantee for the general min-sum single machine scheduling problem (1|| P fj)?

## Nathan Kallus (2015)

*From data to decisions through new interfaces between optimization and statistics* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/a515237e-3d3a-40f3-9ad6-9484da5c8402/content) · [record](https://dspace.mit.edu/handle/1721.1/98570)

- *proposed (author conjectures or asks)* (p. 69): Next we ask the question of when can we even solve the problem (3.
- *stated as open* (p. 116): It is an open question whether the LCX-based test is uniformly consistent – in addition to being consistent – for unbounded Ξ.
- *proposed (author conjectures or asks)* (p. 179): 0007 Discrepancy øø Optimum Bound Incumbent continuous auxilliary variable dand letting μp(x) = 1 k n ∑︁ i=1 w′ ixip and σ2 p(x) = 1 k n ∑︁ i=1 (w′ i)2 xip, we formulate the problem as follows: Zopt m(ρ) = min x max p̸=q (︀ |μp(x) −μq(x)| + ρ⃒⃒σ2 p(x) −σ2 q(x)⃒⃒ )︀ = min x,dd (6.

## Nogueira, Alexandre Belloni (2006)

*Studies integrating geometry, probability, and optimization under convexity* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/a378d13e-071e-4ce1-a6a8-500e175e72a9/content) · [record](https://dspace.mit.edu/handle/1721.1/36227)

- *stated as open* (p. 26): This work also contains a variety of discussions of open questions as well as unproved conjectures regarding the symmetry function and its connection to other areas of convexity theory.
- *proposed (author conjectures or asks)* (p. 35): 1 Remark 2 We conjecture that any symmetry point x\* satisfies f(x\*) 2 maxyes f(y) - 2.
- *proposed (author conjectures or asks)* (p. 37): For an arbitrary convex body S, note that in the extreme cases where sym(S) = 1 or sym(S) = 1/n the difference between sym(S) and sym(xC, S) is zero; we conjecture that tight bounds on this difference are only small when sym(S) is either very close to 1 or very close to 1/n.
- *proposed (author conjectures or asks)* (p. 39): We conjecture that Theorem 10 can be strengthened to prove the existence of a (sy())-rounding of S.
- *stated as open* (p. 59): It is an open question whether there is a more efficient scheme than solving (2.
- *stated as open* (p. 158): As indicated in Chapter 3, there are many open questions concerning the projective pre-conditioners.

## Pablo Parrilo (2000)

*Structured semidefinite programs and semialgebraic geometry methods in robustness and optimization* · [thesis](https://www.mit.edu/~parrilo/pubs/files/thesis.pdf) · [record](https://www.mit.edu/~parrilo/pubs/files/thesis.pdf)

- *stated as open* (p. 27): LMI techniques not only have provided alternative (sometimes simpler) derivations of known results, but also supplied answers for previously unsolved problems.
- *stated as open* (p. 58): In fact, one of the questions in his famous list of twenty-three unsolved problems presented at the International Congress of Mathematicians at Paris in 1900, deals with the representation of a definite form as a sum of squares of rational functions.

## Patrick Steele (2017)

*Vehicle Routing Problems* · [thesis](https://ecommons.cornell.edu/server/api/core/bitstreams/5325bd43-6232-4fc3-bdcf-cb8a85dcf1c0/content) · [record](https://ecommons.cornell.edu/handle/1813/47797)

- *stated as open* (p. 68): We now augment P and Plfor each l∈L to include the potential new SA aircraft, and denote ˆP ⊆P as the set of aircraft that will be guaranteed to remain open after the first stage decisions.

## Pattathil, Sarath (2023)

*Optimization and Generalization of Minimax Algorithms* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/26ad6205-1225-4365-8732-14f0eb8c0a8c/content) · [record](https://dspace.mit.edu/handle/1721.1/152869)

- *stated as open* (p. 129): Moreover, we also address two open questions in the literature: establishing generalization error bounds for primal risk and primal-dual risk without strong concavity or assuming that the maximization and expectation can be interchanged, while at least one of these assumptions was needed in the literature [43, 73, 134, 137].
- *stated as open* (p. 152): The generalization bounds for ζP genof algorithms for problems in terms of stability without strong concavity is still open to the best of our knowledge.
- *stated as open* (p. 152): As mentioned in [73], finding generalization bounds without the strong concavity assumption is an interesting open problem.
- *stated as open* (p. 173): Several open questions remain in this direction.

## Paul Douglas Martin (2004)

*Cost Sharing and Approximation* · [thesis](https://ecommons.cornell.edu/server/api/core/bitstreams/21801d09-7915-4731-bea4-eae0f37c408a/content) · [record](https://ecommons.cornell.edu/handle/1813/224)

- *stated as open* (p. None): [63] recently obtained 2-budget-balanced cost sharing for the Steiner Network problem, resolving an open question whether Steiner network admits a constant-budget balanced cross-monotonic cost sharing.
- *stated as open* (p. None): (The question whether it suffices to obtain full β-strictness remains open, although Section 5.

## Paul Jerome Schweitzer (1965)

*Perturbation theory and Markovian decision processes.* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/9bcbb569-4541-4160-bc8f-ce6c412af217/content) · [record](https://dspace.mit.edu/handle/1721.1/46414)

- *proposed (author conjectures or asks)* (p. 30): N-State Semi-Markov Model: Asymptotic Behavior We conjecture (see below) that for a fixed policy A, A v'At' a}- i A(a) a < 1 (2.
- *proposed (author conjectures or asks)* (p. 31): Similarly we conjecture (see below) that for the optimal timedependent policy, v.
- *proposed (author conjectures or asks)* (p. 225): This conjecture is correct and is formally stated as Corollary 5 Theorem 8.

## Premal Shah (2006)

*No-arbitrage bounds on American Put Options with a single maturity* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/afe805a1-7271-464c-8726-f054cdd31edb/content) · [record](https://dspace.mit.edu/handle/1721.1/36232)

- *stated as open* (p. 20): r&lt;T Apriori, it is not known if an optimal exercise policy exists.

## Richard Tekee Wong (1978)

*Accelerating Benders decomposition for network design.* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/8fbbbf50-fdae-48c7-aa1a-6886f56574ad/content) · [record](https://dspace.mit.edu/handle/1721.1/34293)

- *proposed (author conjectures or asks)* (p. 129): \-129additional worst-cases analyses or some computational tests in order to verify this conjecture.

## Romvary, Jordan (Jordan Joseph) (2015)

*A numerical study of Witsenhausen's Counterexample* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/c7699793-634c-4d60-b482-5f45a0c61035/content) · [record](https://dspace.mit.edu/handle/1721.1/99843)

- **Conjecture 1.1** (p. 20): 4 In any LQG team, the optimal control laws are linear.
- **Conjecture 1.1** (p. 20): 4 is reasonable given Theorems 1.1.2 and 1.1.3, but consider the following system for some k E R+ L =(X + U + U2)2+ k2U2 Z = Y AX (1.11) Z2 =Y 2 AX+U+V 2 At first glance, this problem stipulation looks very similar to that of (1.8). However, the underlying information structure is NOT the partially nested information structure that was present in that problem. Indeed, while DM 1 has perfect measurement of the state X, the only information that DM 2 has about the underlying state X is wholly affected by the choice of control action of DM1 . Therefore there is no equivalence to (1.7) as there was in the case of (1.8) because knowledge of the control law -y1 does not help in the same way. We can interpret this problem as follows: DM 1 observes the state of the system X and then performs the action U1, advancing the state of the system to Xi = X + U1. DM2 then receives a noisy measurement of this state, Z2 = X + U1 + V2, and chooses a control action accordingly. The goal for DM1 is to try and cancel out X using as little energy as possible in its control action U1 , whereas DM 2 desires to cancel out X+U1 .
- *stated as open* (p. 43): General solutions for such problems, even in the finite-dimensional case, remain elusive, and the solution to these optimization problems are currently an open problem.

## Rossi, Baptiste T. (2025)

*Learning Nonlinear Dynamics: Methods and Applications* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/ce8cc671-c0b9-4c34-828c-d1fbbff502b1/content) · [record](https://dspace.mit.edu/handle/1721.1/164511)

- *stated as open* (p. 113): Despite centuries of research, accurately modeling turbulence remains an open and challenging problem, crucial for reliable predictions in diverse engineering and scientific applications, including aerospace design, weather forecasting, and climate modeling [89, 142–144].

## Song, Dogyoon (2021)

*Addressing Missing Data and Scalable Optimization for Data-driven Decision Making* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/f7a53355-9663-4188-a66e-9cb066b2ccc3/content) · [record](https://dspace.mit.edu/handle/1721.1/139254)

- *proposed (author conjectures or asks)* (p. 3): Specifically, we ask the question: “how closely can we approximate the set of unit-trace n × n positive semidefinite (PSD) matrices, denoted by Dn, using at most N number of k × k PSD constraints?
- **Question 1.1 (central question of Part II, informal)** (p. 21): When we have only access to a partial dataset with missing values, can we solve the statistical learning problems with imputed datasets nearly as accurately as if the complete dataset were provided?
- **Question 1.2** (p. 23): Given two positive integers k ≤n, how many k ×k-sized PSD constraints are required to approximate the feasible set of the SDP of the form (1.1) so that the optimality gap (difference in the optimal value) is less than ε? In essence, Quesetion 2 asks how many k × k-sized PSD constraints are necessary for approximating the expressive power of a single n × n PSD constraint. Note that the case with k = 1 corresponds to an LP approximation of SDP, and the case with k = 2 is an SOCP approximation of SDP. ■1.3 Outline and Contributions of the Thesis Part I of this thesis provides some mathematical preliminaries that will be used in our analysis in later chapters. The remainder of this thesis is mainly divided into two parts, each of which contains two or three chapters. In Part II of the thesis, we study the utility of data imputation based on low-rank matrix completion for predictive learning tasks. To this end, we begin our discussion by providing a brief literature review on data imputation and matrix completion, and then discuss error guarantees of low-rank matrix completion algorithms (Chapter 3).
- *proposed (author conjectures or asks)* (p. 23): Specifically, we ask the following question: Question 1.
- **Problem 3.1 (Matrix completion, exact recovery)** (p. 103): Given matrices M and Z generated as per (3.1), is there an estimator φMC : R n1×n2 →Rn1×n2 such that φMC(Z) = M? Note that Problem 3.1 is ill-posed even in the noiseless case (E = 0), unless we make additional assumptions on M. It is because there are n1n2 degrees of freedom in an n1 × n2 matrix, whereas the constraint φMC(Z) = M consists of only |Ω| < n1n2 equations. A typical model assumption imposed on M is that rank(M) ≪n1∧n2. The matrix completion problem with low rank assumption is commonly referred to as the low-rank matrix completion. It is remarkable that under some assumptions that are standard by now (e.g., incoherence of the subspaces), exact recovery is possible as soon as |Ω| exceeds the degree of freedom in the model for M, and moreover, there are efficient algorithms to compute φMC(Z) [32, 116].
- *proposed (author conjectures or asks)* (p. 305): We conjecture that it might be possible to achieve improved upper bounds on the l2,∞-norm, e.
- **Conjecture 3.4.8** (p. 317): There exist matrix completion algorithms that achieve
- *proposed (author conjectures or asks)* (p. 317): However, we also conjecture that the analysis in this section is order-optimal for the SVT algorithm and cannot be improved, based on the empirical evidences, e.
- *proposed (author conjectures or asks)* (p. 544): We conjecture that the right order of dependence on p is 1/p, instead of 1/p2, for an ‘optimal’ matrix completion method.
- *stated as open* (p. 544): However, we do not know whether the scaling of 1/p is achievable by other matrix completion methods.
- *stated as open* (p. 544): Again, we do not know whether this is an artifact of our analysis, or it is due to the fundamental limitation of the SVT method.
- *proposed (author conjectures or asks)* (p. 544): However, we conjecture that it might be possible to improve our analyses of simple SVT for these two norms to sharper upper bounds, e.
- *stated as open* (p. 544): , error bounds in l2,∞-norm and l∞-norm, is an interesting open question.
- *stated as open* (p. 544): It would be an interesting open question to see if ∥φMC(Z) −M∥∞≲η p r/np is achievable.
- *stated as open* (p. 992): Especially, the ability of PCR to handle covariate data with noisy, missing entries is less understood, and its analysis remain as an open challenge.
- *proposed (author conjectures or asks)* (p. 1124): We conjecture that this upper bound provides a tight analysis for the SVT algorithm, and thus, for the PCR.
- *stated as open* (p. 1126): An interesting open question for further research is to investigate if the imputation idea can be also beneficial in kernel regression setting, or more broadly, in the nonlinear settings such as autoencoders.
- **Question 5.1** (p. 1135): Is there a class of Q∗-functions, which can be learned from only o(|S × A|) number of samples?
- **Question 5.2** (p. 1135): If the answer to Question 5.1 is positive, then is there an algorithmic procedure for sample-efficient Q-learning? What would be its sample complexity to produce ˆQ such that ∥ˆQ −Q∗∥∞≤ε?
- *stated as open* (p. 1137): In a sense, the results in this chapter provide a formal framework to understand the empirical success reported in [164], resolving the theoretical open problems raised in that work.
- *stated as open* (p. 1185): Our experiments suggest that traditional optimization-based methods are likely to satisfy the property, but we do not know the answer yet and leave it as an open question.
- *proposed (author conjectures or asks)* (p. 1453): Specifically, we ask the following question in this part of the thesis: “How closely can we approximate Sn + with a cone K that can be described using at most N number of k × k PSD constraints?
- *proposed (author conjectures or asks)* (p. 1459): 1 Introduction In this chapter, we ask the following question: “How closely can we approximate the cone of n × n positive semidefinite matrices, with a cone that can be described using at most N number of k×k PSD constraints?
- *stated as open* (p. 1462): Nevertheless, we do not know whether our extension complexity lower bounds are tight.
- *stated as open* (p. 1462): We are curious if it could be possible to achieve a matching exponential complexity lower bound of order exp(n) for k = 1, and leave it as an interesting open problem.
- *stated as open* (p. 1470): In fact, we do not know whether our lower bound is tight.
- *stated as open* (p. 1476): Lastly, we mention that we do not know whether the extension complexity lower bounds in Theorem 7.
- *stated as open* (p. 1476): We are curious if it could be possible to close this gap between the upper and the lower bounds, either by proving a stronger exponential complexity lower bound or by inventing a clever construction scheme with smaller size, and leave it as an interesting open problem.
- *stated as open* (p. 1478): • We do not know whether our lower bounds in Theorems 7.
- *stated as open* (p. 1539): Nevertheless, we do not know whether this lower bound is tight, or can be further improved.
- *stated as open* (p. 1539): We leave it as an open question to resolve this discrepancy, either by proving a stronger exponential complexity lower bound or by inventing a construction scheme with smaller size.
- *proposed (author conjectures or asks)* (p. 1539): We conjecture that the ‘plateau’ observed in our lower bound (Theorem 7.
- *proposed (author conjectures or asks)* (p. 1539): Specifically, we conjecture that if S is an ε-approximation of BH  Sn +  , then S must have extension complexity bounded from below as xcSk +(S) ≥exp  C · 1 1 + ε n k  .

## Soroush Alamdari (2018)

*Exact and Approximate Algorithms for Some Combinatorial Problems* · [thesis](https://ecommons.cornell.edu/server/api/core/bitstreams/96d0c7c7-dea4-40c1-8395-c5502dbd7474/content) · [record](https://ecommons.cornell.edu/handle/1813/59333)

- *stated as open* (p. None): One particularly notable open problem is to derive good algorithms for the setting in which the opening/ordering costs are submodular set functions of the set of demand points assigned (or for suitably general special cases).
- *proposed (author conjectures or asks)* (p. None): The k-center and k-median problems are, in many respects, antipodal extremes among possible weighting functions for the order median problem; since we have shown that any convex combination of those two weighting functions can be approximated within a constant factor of optimal, we believe that it is natural to conjecture that such a result can be obtained for the general ordered median problem as well.

## Sun, Xu Andy (2011)

*Advances in electric power systems : robustness, adaptability, and fairness* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/5348270d-52b5-4590-84a6-8b69fbb2864d/content) · [record](https://dspace.mit.edu/handle/1721.1/68971)

- *proposed (author conjectures or asks)* (p. 130): Based on our computational experience, we conjecture that ti(A) is actually concave in the domain where ti(A) is strictly positive, and ti (A) has a unique maximizer.
- *stated as open* (p. 149): Many interesting research questions are open.

## Timothy Carnes (2010)

*Approximation Algorithms Via The Primal-Dual Schema: Applications Of The Simple Dual-Ascent Method To Problems From Logistics* · [thesis](https://ecommons.cornell.edu/server/api/core/bitstreams/75ecca21-dcfa-422a-8518-fd2be16be602/content) · [record](https://ecommons.cornell.edu/handle/1813/17733)

- *stated as open* (p. None): To achieve both goals simultaneously would prove that P = NP, a statement widely believed to be false, though this remains one of the biggest open questions in the field of computer science.
- *stated as open* (p. None): One long-standing open question concerns whether there exists an LP-based approximation algorithm for the capacitated facility location problem with a constant performance guarantee.

## Vanli, Nuri Denizcan (2021)

*Large-Scale Optimization Methods: Theory and Applications* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/0da48267-7532-4c17-b42c-a42cfc6715f2/content) · [record](https://dspace.mit.edu/handle/1721.1/140096)

- *proposed (author conjectures or asks)* (p. 72): Furthermore, it has been conjectured that the expected performance of RPCD should be no worse than the expected performance of RCD [124] (see also [74, 154] for related work on this conjecture).

## Velibor Misic (2016)

*Data, models and decisions for large-scale stochastic optimization problems* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/64550cdf-1a45-4361-b396-e50ca4b61b90/content) · [record](https://dspace.mit.edu/handle/1721.1/105003)

- *stated as open* (p. 117): Note, however, that the Markov chain choice model as presented in [25] can only be estimated when one has historical data corresponding to a specific set of n+ 1 assortments, where nis the number of products; the estimation of the model when one has an arbitrary collection of historical assortments remains an open problem.

## Venkat Chandrasekaran (2007)

*Modeling and estimation in Gaussian graphical models : maximum-entropy methods and walk-sum analysis* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/7d988322-3830-4454-a464-61141abfedbe/content) · [record](https://dspace.mit.edu/handle/1721.1/40521)

- *stated as open* (p. 71): Adaptively choosing the K next-best subgraphs jointly with the goal of achieving the greatest reduction in error after K iteration remains an interesting open problem.

## Vishal Gupta (2014)

*Data-driven models for uncertainty and behavior* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/8096b6a6-e0c1-4fec-b619-a0652ef68fd1/content) · [record](https://dspace.mit.edu/handle/1721.1/91301)

- *stated as open* (p. 82): Extending this analysis to more complex queueing networks is an open question, but likely can be accomplished along the lines in [10].
- *stated as open* (p. 172): Extending the above techniques to this case remains an open area of research.

## Xiong, Zikai (2025)

*New Theory and New Practical Methods for Solving Large-Scale Linear and Conic Optimization* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/fb10c17d-9822-4423-acfd-e0b53fef979f/content) · [record](https://dspace.mit.edu/handle/1721.1/162139)

- *stated as open* (p. 162): We end this paper with a short list of open questions for further investigation: 1.
- *proposed (author conjectures or asks)* (p. 255): We conjecture that the Stage-I iteration count might actually be bounded by eO(n1.
- *stated as open* (p. 277): We conclude this paper with a short list of open questions for further investigation: 1.
- *proposed (author conjectures or asks)* (p. 312): This conjecture is further supported by the empirical convergence behavior illustrated in Figure 6.

## Xuan Vinh Doan (2010)

*Optimization under moment, robust, and data-driven models of uncertainty* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/b58411bb-b87c-4665-b992-9911f833f6ac/content) · [record](https://dspace.mit.edu/handle/1721.1/57538)

- *stated as open* (p. 25): there are still many open problems currently and research on general multivariate integrals is very much active due to its importance as well as its difficulties.

## Ying Daisy Zhuo (2018)

*New algorithms in machine learning with applications in personalized medicine* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/85b95644-8183-4c14-a661-f75bbb00b88f/content) · [record](https://dspace.mit.edu/handle/1721.1/119284)

- *stated as open* (p. 60): Given the optimization formulations introduced in this chapter, there are multiple open questions for future research.
- *stated as open* (p. 60): 1) fast and accurately for any of the three examples of non-convex, nonlinear cost functions c(U, W, V; X) proposed in this work remains an open question.
- *stated as open* (p. 69): Without extensive computational experiments, we do not know if these robust classifiers yield gains in out-of-sample accuracy in practice, especially in comparison with regularized methods.

## Yuan, Chenyang (2022)

*Polynomial Structure in Semidefinite Relaxations and Non-Convex Formulations* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/3d1e5b32-6c54-4630-a722-280ea1e5a959/content) · [record](https://dspace.mit.edu/handle/1721.1/147562)

- **Conjecture 3.5.1** (p. 55): Given A= V†V, where viare the columns of V, recall that r(A) is the maximum of a product of linear forms as defined in (3.1). Then n! nnr(A) ≤per(A) ≤r(A). (3.9)
- *proposed (author conjectures or asks)* (p. 55): We conjecture that the exact solution to this optimization problem is a tighter relaxation of the permanent.
- **Conjecture 3.5.2 (Pate’s conjecture [87])** (p. 56): Given any n× nHPSD matrix A, let A⊗Jkbe the Kronecker product of Awith the k× kall-ones matrix. Then per(A⊗Jk) ≥per(A)k(k!)n. (3.10) This conjecture has been proved in the case where n= 2, see [107] for a survey of subsequent progress on this conjecture. Using the integral representation of the permanent (Proposition 3.2.7), we can write (3.10) as: E x∼CN(0,In) [︃n ∏︁ i=1 |⟨vi, x⟩|2k ]︃1/k ≥per(A) E x∼CN(0,In) [︃n ∏︁ i=1 |xi|2k ]︃1/k Since both expectations are taken over homogeneous polynomials of degree d, we can apply Fact 3.2.5, take k→∞and get: max ‖x‖2=n n ∏︁ i=1 |⟨vi, x⟩|2 ≥per(A) max ‖x‖2=n n ∏︁ i=1 |xi|2 = per(A).
- *proposed (author conjectures or asks)* (p. 57): Although it is natural to conjecture the hardness of computing r(A), we do not know of any formal results establishing this.
- **Conjecture 4.2.4 ([82])** (p. 68): Let v1, . . . , vdand xbe vectors in Rd. min ‖v1‖=1,...,‖vd‖=1 max ‖x‖=1⃒⃒⃒⃒⃒ d ∏︁ i=1 ⟨vi, x⟩⃒⃒⃒⃒⃒= d−d/2 (4.5) And is achieved when viare (up to rotation) the basis vectors ei. We see that (4.5) is a minimax problem with its inner maximization problem equivalent to solving the following optimization problem: max ‖x‖=1 (︃d ∏︁ i=1 ⟨vi, x⟩2 )︃1/d (4.6) Which is exactly (4.1) with Ai= viv† i. Exact values for cd(Kn) where K = R or C and d> n are not known, but [82] computed the asymptotic value limd→∞cd(Kn)1/d. We will use these results later to construct integrality gap instances in Sections 4.5 and 4.6.5.
- *proposed (author conjectures or asks)* (p. 87): Then we state a conjecture involving an identity of pseudoexpectations which if true, the same bound applies to all instances.
- **Conjecture 4.6.8** (p. 91): (︃d ∏︁ i=1 ̃Ex[μ(x) ⟨x, Aix⟩] )︃(d−1 k−1) ≥ ∏︁ I∈Sk ̃Ex [︃∏︁ i∈I ⟨x, Aix⟩ ]︃ . For example, in the case where k= d, the above inequality reduces to d ∏︁ i=1 ̃E [μ(x) ⟨x, Aix⟩] = d ∏︁ i=1 ̃E [︁ ⟨v, x⟩2(d−1) ⟨x, Aix⟩ ]︁ ̃E [︁ ⟨v, x⟩2(d−1)]︁ ≥ ̃E [︃d ∏︁ i=1 ⟨x, Aix⟩ ]︃ .
- *stated as open* (p. 98): Another open problem is to extend the analysis of the performance ratio of the Sum-ofSquares relaxation in section 4.
- *proposed (author conjectures or asks)* (p. 159): However, we conjecture that a version of Theorem 6.

## Yuriy Zinchenko (2005)

*THE LOCAL BEHAVIOR OF THE SHRINK-WRAPPING ALGORITHM FOR LINEAR PROGRAMMING* · [thesis](https://ecommons.cornell.edu/server/api/core/bitstreams/3a85d54b-29cd-4a32-967e-39e9c66a990d/content) · [record](https://ecommons.cornell.edu/handle/1813/2197)

- **Conjecture** (p. None): In addition, limt↑∞x(t) = x∗ To gain a sense why this would be a reasonable choice for the dynamics of d(t), simply observe cT ̇d(t) = cTx(d(t)) −cTd(t) < 0 since d(t) is strictly feasible for the relaxed problem of which x(d(t)) is optimal. This setting has a connection with interior-point methods. To explain, we introduce the notion of a central swath CSk(P) := {d ∈Rn ++ : (P(d)) corresp. to Kk,d has an optimal solution}
- *stated as open* (p. None): In particular one of the open questions is whether the hyperbolicity cones are more general than the linear sections of Sn + (and consequently, whether hyperbolic programming is any more general than SDP).
- *stated as open* (p. None): It remains open whether similar representations hold for hyperbolicity cones in more than three variables, although such representations have been established for important broad families of hyperbolicity cones (in particular, the so-called homogeneous cones,[14]).
- *proposed (author conjectures or asks)* (p. None): The only part that is missing to make this a complete argument is to show that such ef ∈C1 does exist (We conjecture that we need to extend ef for ρ ≥0 only and this indeed can be done).
