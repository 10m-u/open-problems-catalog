# Thesis statements: Classical Statistical Machine Learning

Discipline: Computer Science & Artificial Intelligence. 312 statements from 35 theses. [All subjects](../README.md)

Automatically extracted, not reviewed: OCR noise and fragments are common, and a passage may describe a problem that is now solved. Always check the thesis page cited.

## Alexander Spence Wein (2018)

*Statistical estimation in the presence of group actions* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/2b834cdb-8b89-4ff8-9748-cae60005caf2/content) · [record](https://dspace.mit.edu/handle/1721.1/117314)

- *proposed (author conjectures or asks)* (p. 30): Indeed, we conjecture based on ideas from statistical physics that in many regimes our algorithm is statistically optimal, providing a minimum mean square error (MMSE) estimator asymptotically as the matrix dimensions become infinite (see Section 2.
- *proposed (author conjectures or asks)* (p. 31): It is known that inefficient estimators can beat the A = 1 threshold (see Chapter 3) but we conjecture that no efficient algorithm is able to break this barrier, thus concluding in Section 2.
- *proposed (author conjectures or asks)* (p. 72): ) As is standard for these types of problems, we conjecture that AMP is optimal among all polynomial-time algorithms.
- *proposed (author conjectures or asks)* (p. 95): In fact, we conjecture that A > 1 is required for any efficient algorithm to succeed at detection (see Chapter 2), although there are inefficient algorithms that succeed below this (as we will show in Section 3.
- *proposed (author conjectures or asks)* (p. 101): Of course we cannot test this for all values of L, but we conjecture that the A\* = 1 trend continues indefinitely.
- **Problem 4.1.1 (orbit recovery)** (p. 116): Let V = RP and let 0 E V be the unknown signal. Let G be a compact group that acts linearly, continuously, and orthogonally on V. For i C [n] = { 1, 2,..., n} we observe yi = gi - 0 + i where gi ~ Haar(G) and j ~ A'(O, aIPxP) , all independently. The goal is to estimate 0. Note that we can only hope to recover 0 up to action by G; thus we aim to recover the orbit {g-0 : gEG}of0. In practical applications, a- is often known in advance and, when it is not, it can generally be estimated accurately on the basis of the samples. We therefore assume throughout that a- is known and do not pursue the question of its estimation in this work. Our primary goal is to study the sample complexity of the problem: how must the number of samples n scale with the noise level a- (as a -+ oc with G and V fixed) in order for orbit recovery to be statistically possible? All of our results will furthermore apply to a generalized orbit recovery problem (Problem 4.2.3) allowing for projection and heterogeneity (see Section 4.1.6). Our work reveals that it is natural to consider several different settings in which to state the orbit recovery problem. We consider the following two decisions:
- **Problem 4.2.3 (generalized orbit recovery)** (p. 123): Let f = RP and W = Rq . Let C be a compact group acting linearly, continuously, and orthogonally on V. Let H : V -+ W be a linear map. Let 9 = (01, ... , OK, 7) E V A gBK G EK be an unknown collection of K signals with mixing weights w E AK. For i E [n] = {1, 2, ... , n} we observe yi = H( gi - Oki) + i where gi ~ Haar(O), ki - [K], (i ~/(0, .2 Iqxq), all independently. The goal is to estimate the orbit of 9 under G " OK X SK. Note that this serves as a reduction from the heterogeneous setup to the basic setup in the sense that we are still only concerned with recovering the orbit of a vector 9 under the action of some compact group. As discussed previously, we apply the method of moments. The moments are now defined as follows.
- **Question 4.2.8** (p. 124): Fix 0 E V. How large must d be in order for U Td to uniquely resolve 0? How large must d be in order for U'd to list-resolve 0? The answer depends on G and V but also on whether 6 is a generic or worst-case signal, and whether we ask for unique recovery or list recovery. As discussed previously (see Section 4.1.5), the sample complexity of the generalized orbit recovery problem is E(0.2d) where — **partial here** ([details](../../solutions/catalog-research/cyclic-orbit-degree.md))
- **Conjecture 4.4.3** (p. 138): For MRA with projection, for any odd p ;> 3, generic list recovery is possible at degree 3. Note that generic list recovery is impossible at degree 2 because the addition of the projection step to basic MRA can only make it harder for U' to list-resolve 0.
- *proposed (author conjectures or asks)* (p. 138): 2) on a computer, and we conjecture that this trend continues.
- **Conjecture 4.4.4** (p. 139): For heterogeneous (K > 2) MRA, generic list recovery is possible at degree 3 precisely if U > Kp + K -
- **Conjecture 4.4.6** (p. 142): Consider the S2 registration problem with 0 F. We conjecture the following. \* Generic list recovery is possible at degree 3 if and only if dim(R[x] + dim(R[x]) trdeg(R[x]G) (where trdeg(R[x]G) is computed above and dim(R[X]G) can be computed from Proposition 4.4.7 below). " In particular, if F = {1, 2,. . . , F} then generic list recovery is possible at degree 3 if and only if F > 10. The reason it is convenient to exclude the trivial representation is because it simplifies the parameter-counting: if we use the trivial representation then we have a degree-1 invariant f and so there is an algebraic relation between the degree-2 invariant f 2 and the degree-3 invariant f 3 . We now discuss how to compute dim(R[x]G). Using the methods in Section 4.6 of [551, we can give a formula for the Hilbert series of R[x]G; see Section 4.7.1. However, if one wants to extract a specific coefficient dim(R[x]G) of the Hilbert series, we give an alternative (and somewhat simpler) formula:
- **Conjecture 4.4.10** (p. 145): If S > 2 then the degree-3 method of moments achieves generic list recovery (regardless of F).
- *proposed (author conjectures or asks)* (p. 146): Based on testing the Jacobian criterion on small examples, we conjecture that the degree-3 method of moments achieves generic list recovery if and only if dim(U) + dim(UT) > trdeg(R{x]G).
- *stated as open* (p. 146): 5 Open questions We leave the following as directions for future work.
- *proposed (author conjectures or asks)* (p. 146): In cases where unique recovery is impossible, it would be nice to give a tight bound on the size of the list; for instance, for MRA with projection, we conjecture that the list has size exactly 2 (due to "chirality"), but we lack a proof for this fact.
- *proposed (author conjectures or asks)* (p. 162): 3 we will see an alternative method for arriving at this conjecture.
- **Conjecture 5.3.1** (p. 164): Consider the generalized orbit recovery problem (with heterogeneity and projection) with random signals. List recovery from the third moment is possible in polynomial time provided that trdeg(Uf) 6(Kp 3 / 2 ). For comparison, recall from Chapter 4 that statistically, recovery from the third moment requires roughly trdeg(Uf) > Kp (assuming p > dim(G)). Note that list recovery is necessary in some cases; for instance, in cryo-EM we can only hope to recover the molecule up to chirality. For example, in heterogeneous MRA we have trdeg(Uf) = e(p2 ), leading us to predict the computational threshold K < Q(V/p). This matches the conjecture of [35] discussed above. For cryo-EM with S shells and F frequencies we have trdeg(U') ~ S3F2/4 and p - SF2 (see Appendix C.1.6) and so we expect efficient recovery when K < f(S 3/2 /F). In particular, homogeneous (K = 1) cryo-EM should require S3/2 > F.
- **Conjecture C.1** (p. 197): 1. Consider heterogeneous cryo-EM with F > 2 frequencies. " trdeg(R[x]G) = K[S(F2 + 2F) - 3] + K - 1, \* dim(Uf) = 1S(S + 1)F, " dim(U3T) = IX(S, F)I - E(S), " generic list recovery is possible at degree 3 if and only if dim(Uf) + dim(U3T) > trdeg(R[x]G). When S and F are large, the dominant term in dim(U2T) + dim(Uf) is IX(S, F) S3F2 /4 and so generic list recovery is possible when (roughly) K S2 /4.
- *proposed (author conjectures or asks)* (p. 197): ) We can now put it all together and state our conjecture.

## Alvarez Melis, David. (2019)

*Optimal transport in structured domains : algorithms and applications* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/fc052e06-6bda-4c79-8874-c3e2b2bdbef2/content) · [record](https://dspace.mit.edu/handle/1721.1/124059)

- *stated as open* (p. 5): Chief among them is Suvrit Sra, whose enthusiasm for research, high standards for theoretical soundness and perpetual quest for open problems, are models that I aspire to.
- *stated as open* (p. 20): Very recently, there has been important progress towards modeling structure in OT, particularly in the context of computer graphics [163, 57], though various important open problems and untouched applications remain.
- *stated as open* (p. 25): However, addressing Point (3) through the lens of optimal transport remains largely an open problem.
- *proposed (author conjectures or asks)* (p. 86): Here, we formulate the problem for the case where the ground metric c is the squared euclidean distance, i.
- *proposed (author conjectures or asks)* (p. 101): We conjecture that the ordering in which word embeddings are provided (higher-frequency words first, in every language) helps ensure that the solution of the initial problem of reduced size is consistent with the full-size problem.
- *proposed (author conjectures or asks)* (p. 121): 2 We conjecture that this could be due - 2 to Russian's rich morphology (a trait shared by romance languages but not D English).
- *stated as open* (p. 128): Thus, effective fully-unsupervised alignment of hierarchical datasets remains largely an open problem.
- *proposed (author conjectures or asks)* (p. 132): We conjecture that the cause of this invariance is the use of negative sampling for normalization in that loss function, which has the effect of putting emphasis on preserving distance between entities that are ancestrally related in the hierarchy, at the cost of down-weighting distances between unrelated entities.

## Boix-Adsera, Enric (2024)

*Characterizations of how neural networks learn* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/62c9a038-30ff-4862-8261-dcc01cebaf8b/content) · [record](https://dspace.mit.edu/handle/1721.1/156306)

- *proposed (author conjectures or asks)* (p. 28): We report results for 3 different magnitudes of initializing the weights of attention mechanism (1 times, 8 times, and 64 times the standard initialization), and find that larger initialization helps, which we conjecture is due to the softmax being in the saturated regime, which leads to more weight on the relational features.
- *stated as open* (p. 39): This chapter concludes with the open problem of deriving a necessary and sufficient condition on what can be efficiently learned using neural networks.
- *stated as open* (p. 39): • In Chapters 2 and 3, we resolve this open problem in the case of multi-index functions.
- *stated as open* (p. 44): In particular, it is not known how to obtain the emulation results of [AKM+21] for “regular” architectures and initializations as defined in Definition 1.
- *proposed (author conjectures or asks)* (p. 44): However, we conjecture that Sj→n(x) is not learnable by regular networks trained with gradient descent 2These reductions are for polynomial-time algorithms and for polynomial precisions on the gradients.
- *proposed (author conjectures or asks)* (p. 51): We conjecture that if the network is trained end-to-end instead of layer-wise, then one can avoid this technical difficulty and set λ1 = λ2 and p1 = p2, because of a backward feature correction phenomenon [AL20] where the lower layers’ accuracy improves as higher levels are trained.
- *stated as open* (p. 52): Set R ∈R+ ∪{∞} and consider any sequence of 3Such a conjecture was recently made by [BDM20], which leaves as an open problem in Section 1.
- *proposed (author conjectures or asks)* (p. 54): For instance, if ˆg(S)̸ = 0, one may require that there exists an S′ such that |S′| < |S| and |S∆S′| = O(1), and we conjecture that regular networks will still learn sparse polynomials with this structure.
- *proposed (author conjectures or asks)* (p. 54): We emphasize that these limitations are purely technical as they make the analysis tractable, and we conjecture from our experiments that ReLU ResNets trained with SGD efficiently learn functions satisfying the staircase property.
- *stated as open* (p. 56): However, these works do not provide tractable algorithms and the question of when SGD-trained neural networks can adapt to sparsity remains largely open.
- *proposed (author conjectures or asks)* (p. 68): For example, we conjecture that l-leap MSP (i.
- *proposed (author conjectures or asks)* (p. 68): We conjecture that such an exponential scaling is needed, i.
- **Conjecture 3.1.2** (p. 75): Let f∗: Rd →R in L2(μ⊗d) for μ either N(0, 1) or Unif{+1, −1} satisfying the low-latent-dimension hypothesis f∗(x) = h∗(Mx) in (3.1.2) for some P = Od(1). Let ˆf t NN be the output of training a fully-connected neural network with poly(d)-edges and rotationally-invariant weight initialization with t steps of online-SGD on the square loss. Then, for all but a measure-0 set of functions (see below), the risk is bounded by R( ˆf t NN) := Ex h  ˆf t NN(x) −f∗(x) 2i ≤ε if and only if t = ̃Ωd(dLeap(h∗)−1∨1)poly(1/ε) . So the total time complexity4 is ̃Ωd(dLeap(h∗)∨2)poly(1/ε) for bounded width/depth networks5. The “measure-0” statement in the conjecture means the following. For any set {S1, . . . , Sm} of nonzero (Fourier or Hermite) basis elements, the conjecture holds for all h∗with S(h∗) = {S1, . . . , Sm} in the decomposition (3.1.4), except for a set of coefficients {(ˆh∗(Si))i∈[m]} ⊂Rm of Lebesgue-measure 0. This part of the conjecture is needed for Boolean functions, since it was proved in [ABM22] that a measure-0 set of “degenerate” leap-1 functions on the hypercube are not learned in Θ(d) SGD-steps by 2-layer neural networks in the mean-field scaling.
- *proposed (author conjectures or asks)* (p. 75): However, we further conjecture that in the case of Gaussian data the measure-0 modification can be removed if we instead use a rotationally invariant version of the leap.
- *proposed (author conjectures or asks)* (p. 77): We conjecture in fact that n = eΘ(dmax(Leap/2,1)) is optimal for ERM.
- *proposed (author conjectures or asks)* (p. 77): They show that it can be learned in n = Θ(d2) samples with one-gradient descent step on the first layer weights, while we conjecture (and show for a subset of those polynomials) that ̃Θ(d) online-SGD steps is sufficient.
- *proposed (author conjectures or asks)* (p. 77): [BEG+22] considers learning degree-k monomials on the hypercube and shows that n = dO(k) samples are sufficient, using one gradient descent step on the first layer, while we conjecture (and prove in the Gaussian case) a tighter scaling of ̃Θ(dk−1) online-SGD steps7.
- *proposed (author conjectures or asks)* (p. 78): However we conjecture that the same scaling as the Boolean case should hold.
- *proposed (author conjectures or asks)* (p. 92): As evidence for this conjecture, we have proved lower-bounds showing dΩ(Leap(h∗)) complexity of learning in the Correlational Statistical Query (CSQ) framework (Proposition 3.
- *stated as open* (p. 95): This raises an exciting open question for future work: can we explain and improve algorithms like LoRA by better understanding and quantifying the incremental dynamics of large transformers?
- *proposed (author conjectures or asks)* (p. 134): Although we use the cosine activation function, we conjecture that this result holds for most non-polynomial activation functions.
- *proposed (author conjectures or asks)* (p. 139): In this paper, we ask the following question: Can we give tight conditions for when the NTK approximation is valid?
- *stated as open* (p. 171): While distillation is widely used in practice, and sometimes succeeds in replacing large, complex models by smaller or simpler models with a minor loss in accuracy, a number of basic questions remain largely open: 1.
- *stated as open* (p. 172): • Open problems: Finally, we discuss extensions and new open directions; see Section 9.
- *stated as open* (p. 185): For arbitrary distributions, our distillation algorithm takes exponential time in the depth, and thus is truly polynomial-time only when r = O(log(s)) It is an interesting open problem whether it is possible to obtain polynomial dependence on the depth under the LRH condition.
- *proposed (author conjectures or asks)* (p. 201): In light of these examples, it is natural to conjecture that the VC dimension of the Pareto frontier of functions will fully characterize the sample complexity of agnostic distillation.
- *proposed (author conjectures or asks)* (p. 201): However, this conjecture turns out to be false, as we show below.
- *stated as open* (p. 203): Basic statistical and computational theory Fundamental open questions include: • Growing the web of reductions.
- *proposed (author conjectures or asks)* (p. 1104): 3 Merged-staircase functions when including all degree-1 monomials We conjecture that the optimal dependence on P for learning vanilla staircase functions with unregularized SGD by two-layer neural networks should be on the order of exp(O(P)), but the results of Propositions B.
- **Problem E.4** (p. 1296): 4. The (d, n, γ)-secretly-flipped sum-mod-8 (SFSM8) problem is parametrized by γ > 0, and integers d, n > 0. It is as follows: • Unknown: sign-flip vector s ∈Hd. • Input: query vector q ∼Hd, modified samples (xi ⊙s, yi)i∈[n], where (xi, yi)i∈[n] i.i.d. ∼ D(fmod8, Hd, γ). • Task: return fmod8(q ⊙s) ∈{0, . . . , 7}.
- *proposed (author conjectures or asks)* (p. 1319): Although in our proof we use the cosine activation function, we conjecture that this result should morally hold for sufficiently generic non-polynomial activation functions.
- *proposed (author conjectures or asks)* (p. 1325): We provide a general lemma that allows us to guarantee the invertibility if the activation function is a shifted cosine, although we conjecture such a result to be true for most non-polynomial activation functions φ.

## Carter, Brandon M. (2023)

*Interpretations of Machine Learning and Their Application to Therapeutic Design* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/423ff1b4-44ae-46a2-875c-971db29f73e5/content) · [record](https://dspace.mit.edu/handle/1721.1/151487)

- *proposed (author conjectures or asks)* (p. 85): We conjecture the cause of both the increase in the accuracy and SIS size for ensembles is the same.
- *proposed (author conjectures or asks)* (p. 85): We conjecture that random dropout of input pixels disrupts spurious signals that lead to overinterpretation.
- *stated as open* (p. 96): In addition, we do not know how well existing peptide prediction methods function on glycosylated peptides.
- *stated as open* (p. 134): , 2022) and are in clinical trials (NCT05113862, NCT0488536, NCT05069623, NCT04954469), but identifying the mechanisms behind the efficacy of pure T cell vaccines remains an open question.

## Chen, Sitan (2021)

*Rethinking Algorithm Design for Modern Challenges in Data Science* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/6394b44a-568d-4899-9f05-fb4d1c91e4c6/content) · [record](https://dspace.mit.edu/handle/1721.1/139922)

- *proposed (author conjectures or asks)* (p. 3): In the final part of this thesis, we ask whether these and related ideas in data science can help shed light on problems in the sciences.
- **Question 1** (p. 25): Are there natural settings where one can prove that rich classes of functions, e.g. neural networks, are learnable in the realizable case? 1This holds under a plausible complexity-theoretic conjecture regarding random constraint satisfaction problems.
- **Question 2** (p. 27): How do we mitigate the effect of noisy and untrustworthy data, especially in settings where even the “clean” parts of the data are heavy-tailed, dynamically generated, or otherwise misbehaved? Related questions have been studied for some time in the robust statistics literature, and in Chapters 4 to 6, we give a detailed overview of known results and clarify the ways in which they come up short. In this part of the thesis, we study Question 2 in the context of distribution estimation, linear regression, and contextual bandits, giving the first algorithms to obtain near-optimal statistical guarantees in the presence of corrupted data for these problems. We overview the relevant models and our results in Section 1.2.2 and provide the technical details in Chapters 4 to 6. In the third part of the thesis, we ask how the algorithmic landscape for such problems changes if we assume additional structure on the noise inherent in real-world data. Specifically, we focus on structure that arises from heterogeneity.
- **Question 3** (p. 28): What are the most powerful algorithmic primitives for discerning subpopulation structure from heterogeneous data? In the third part of this thesis we answer Question 3 by giving faster algorithms for two well-studied mixture models (stylized models of data with subpopulation structure). Importantly, as we describe in Section 1.2.3 and subsequently in greater detail in Chapters 7 and 8, the algorithmic primitives we design help shed new light on the connections between two powerful techniques in learning theory for handling such problems: Fourier analysis and the method of moments.
- *stated as open* (p. 29): Dynamic Data and Quantum Learning With noisy intermediate-scale quantum computing looming on the horizon, it is timely to explore what ideas in machine learning on classical computers are transferable to the quantum setting, where analogues of even the most basic classical learning problems remain open.
- *stated as open* (p. 40): They also showed a matching information-theoretic lower bound showing that achieving o(ω+ η/ √ k) error is impossible in general, leaving as an open question whether one can match this lower bound with an efficient algorithm.
- *proposed (author conjectures or asks)* (p. 97): Note that while we ask the question for isotropic Gaussian covariates, our guarantees immediately carry over to general Gaussians, because the space of low-rank polynomials is affine invariant.
- *stated as open* (p. 105): While we can currently show that there is at least one such eigenvalue, we do not know if the matrix Mτhas rank at least rand it seems considerably more challenging to prove.
- *stated as open* (p. 176): depth two ReLU networks where we additionally assume the W1 has all positive entries, it remains a major open question to obtain a polynomial-time algorithm (see [DK20] for the strongest-known result).
- *stated as open* (p. 182): Non-Homogeneous ReLU Networks We leave as an open question whether our result can be extended to non-homogeneous networks of the form F(x) ≜WL+1φ(WLφ(· · · φ(W0x+ b0) + b1) · · · + bL), where b0, .
- *stated as open* (p. 228): The main open question of our work is to push this philosophy further, and explore what other sorts of provably robust algorithms can be built out of different choices of test functions.
- *stated as open* (p. 284): Finally, we remark that in a very recent follow-up to these two works, Jain and Orlitsky [JO21] managed to answer the remaining open question of achieving the tight sample complexity scaling as s· d/ε2.
- *stated as open* (p. 614): The main open question of our work is to prove matching upper and lower bounds that pin down the true diffraction limit.
- *stated as open* (p. 653): 6 Conclusion and Open Problems We hope that our work will be a stepping-stone towards developing a rigorous theory of resolution limits in more sophisticated optical systems.
- **Problem 2 (Hypothesis Testing)** (p. 655): Suppose we know the parameter d, and we know that either ρ= ρ0 or ρ= ρ1. Given samples from ρ, decide whether ρ= ρ0 or ρ= ρ1. For Problem 1, Helstrom [Hel64,Hel69,Hel70] studied the maximum likelihood estimator and computed Cramer-Rao lower bounds for a host of point-spread functions including the Airy PSF, both for the SDM and for progressively more physically sophisticated (though less practically relevant) models. The conceptual insights and problem formulation of [Hel64] were refined, or often rediscovered, numerous times [TD79,BVDDD+99,SM04,SM06,RWO06, Far66, CWO16], and the primary thrust of this line of work has been centered on CramerRao-style calculations for assorted point-spread functions and, to a lesser extent, analysis of the optimization landscape of the log-likelihood from the perspective of singularity theory [VDB01,VdBDD01,BVDDD+99,DD96]. For Problem 2, Helstrom [Hel64] computed the reliability of the likelihood ratio test for various PSFs, under a CLT appoximation to the log-likelihood ratio. Similar calculations for the log-likelihood ratio for other PSFs followed in [Har64,AH97,SM04,SM06,Far66].
- *stated as open* (p. 681): learning and testing tasks was posed as an open problem in [Wri16].
- *stated as open* (p. 718): Obtaining tight bounds in this setting is an interesting open question, though we reiterate that this is not known even for mixedness testing.

## Cheng Mao (2018)

*Matrix estimation with latent permutations* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/b56a28da-5016-4bd8-bc65-af6a4c3aef45/content) · [record](https://dspace.mit.edu/handle/1721.1/117863)

- *stated as open* (p. 18): However, it is not known whether a computationally efficient estimator could achieve the fast rate.
- *stated as open* (p. 20): 8) into sharp oracle inequalities remains an interesting open problem.
- *stated as open* (p. 27): Achieving sharper bounds to explain such a phenomenon also remains an interesting open question out of the scope of the present work.
- *proposed (author conjectures or asks)* (p. 39): We conjecture that achieving optimal rates of estimation in the
- *stated as open* (p. 58): Closing this logarithmic gap for other problems involving latent permutations [CD16, FMR16, SBGW17, PWC17] remains an open question.
- *stated as open* (p. 63): 4 Discussion and open problems In this chapter, we focused on minimax estimation of the latent permutation ir\*.
- *stated as open* (p. 63): For the MS algorithm, it remains an open question whether analogous upper bounds can be established for sampling without replacement.
- *proposed (author conjectures or asks)* (p. 63): We conjecture that this is the case because of the empirical evidence in Section 3.
- *proposed (author conjectures or asks)* (p. 105): In fact, we conjecture that any algorithm that only exploits partial row and column sums cannot achieve a rate faster than 0(n3/ 4) for the SST class.

## Chewi, Sinho (2023)

*An optimization perspective on log-concave sampling and beyond* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/66fa6f59-23d3-43b9-ad22-06ea9fbdd8f8/content) · [record](https://dspace.mit.edu/handle/1721.1/151333)

- *stated as open* (p. 19): In the first application, we resolve an open question of [BE19] by showing that the entropic barrier for a convex body, which is known to be a self-concordant barrier for that body, in fact attains the optimal barrier parameter of d, where d is the ambient dimension.
- *stated as open* (p. 20): In particular, it was an open question of [Bar+18] to show that the convolution of a measure with compact support and a Gaussian satisfies an LSI with a dimension-free constant (depending only on the radius of the support and the variance of the Gaussian).
- *stated as open* (p. 63): As a corollary, we resolve an open question of [VW19] on the size of the “R ́enyi bias” in this setting (see Corollary 3.
- *stated as open* (p. 68): Since our guarantee is stable with respect to the number of iterations N, we can let N →∞and obtain an estimate on the asymptotic bias of (LMC) in R ́enyi divergence; this answers an open question of [VW19].
- *stated as open* (p. 106): Consequently, we have resolved the open questions of estimating the R ́enyi bias of LMC (Corollary 3.
- *proposed (author conjectures or asks)* (p. 107): Hence, we ask whether R ́enyi convergence guarantees can be proved for more sophisticated algorithms, such as randomized midpoint discretizations [SL19; HBE20].
- *proposed (author conjectures or asks)* (p. 109): To overcome these issues, we ask the following question: since LMC can be interpreted as a discretization of the Wasserstein gradient flow for the KL divergence, are there better methods of implementing this flow?
- *stated as open* (p. 119): Related to the first point, it is currently not known how to perform a discretization analysis of the Langevin algorithm with linear dependence on the condition number ˆκ = β α under 1/α-LSI or 1/α-PI.
- *stated as open* (p. 359): It is an interesting open question to extend our results on MALA to other natural function classes, such as smooth and weakly convex potentials, as well as to other sampling algorithms.
- *stated as open* (p. 362): Yet, despite several decades of progress, many fundamental theoretical questions remain open about the complexity of sampling.
- *stated as open* (p. 365): Unfortunately, any improvement to these ULMC warm start bounds appears to require overcoming fundamental difficulties with studying hypocoercive differential equations which remain unsolved today, despite being the focus of intensive research activity within the PDE community since the work of Kolmogorov [Kol34].
- *stated as open* (p. 367): And regarding the condition number dependence, any further progress beyond eO(κ) in the high-dimensional regime4 would constitute a major breakthrough in the complexity of sampling since it is currently unknown whether an acceleration phenomenon holds in the sampling context.
- *stated as open* (p. 367): The open question mentioned here is really: can one improve the condition dependence beyond near-linear while also maintaining comparable dimension dependence?
- *stated as open* (p. 371): However, this is still a relatively nascent area of PDE and many important questions remain wide open; see the prior work in §6.
- *proposed (author conjectures or asks)* (p. 371): Namely, instead of trying to directly establish hyperequilibration via hypocoercivity techniques, we ask whether it can be deduced from simpler Wasserstein coupling arguments.
- *stated as open* (p. 372): Finally, we note that our analysis answers the open question raised in [AT22b] of how to use the shifted divergence technique in order to obtain sampling guarantees for discretized diffusions w.
- *stated as open* (p. 376): This answers the open questions in [LW22] regarding warm starting the zigzag sampler.
- *proposed (author conjectures or asks)* (p. 384): Details on this conjecture are provided in §6.
- *stated as open* (p. 386): 2 for a detailed discussion of the technical obstacles related to this, and the connections to open problems about hypocoercivity in the PDE literature.
- **Conjecture 6.6.1** (p. 399): For any R ́enyi order q ≥1, noise variance σ2 > 0, shift w ≥0, and mean x ∈Rd, R(w) q  normal(x, σ2Id) normal(0, σ2Id)  = Rq  normal(cx, σ2Id) normal(0, σ2Id)  = c2q ∥x∥2 2σ2 , where c := max(0, 1 −w√log 2/∥x∥).
- *proposed (author conjectures or asks)* (p. 399): This conjecture states that the shifted R ́enyi divergence between two isotropic Gaussians with same covariance is achieved by a deterministic shift.
- *stated as open* (p. 510): As mentioned in our open questions, this points to the intriguing possibility of developing more stable variants of NLA, which would mirror the development of such strategies for Newton’s method [CGT00; NP06].
- *proposed (author conjectures or asks)* (p. 511): In a different direction, we ask the following question: are there appropriate variants of other popular sampling methods, such as accelerated Langevin [Ma+21] or Hamiltonian Monte Carlo [Nea11], which also enjoy the scale invariance of NLD?
- *stated as open* (p. 523): In light of our result, we believe that it is an interesting open question to resolve their conjecture.
- *stated as open* (p. 524): It remains an open question to remove this latter restriction from their work, and moreover to obtain similar results under the more usual definitions of relative convexity/smoothness and self-concordance that we adopt in this work.
- *stated as open* (p. 547): 12, it is an open question to determine if the analyses of [Zha+20; Li+22] can be improved to obtain vanishing bias for the Euler–Maruyama discretization of MLD under weaker assumptions.
- *stated as open* (p. 595): However, the low-dimensional complexity of computing stationary points remains open.
- *stated as open* (p. 623): • The main question motivating this work remains open, namely, for randomized algorithms using zeroth- and first-order information, is it possible to prove a Ω(1/ε2) complexity lower bound with a construction in dimension d = O(log(1/ε))?
- *proposed (author conjectures or asks)* (p. 636): (lower bounds) We ask whether one can prove matching lower bounds on the complexity of outputting a sample whose Fisher information w.
- *stated as open* (p. 636): In §14, we investigate this lower bound question in detail and in doing so we establish further connections between non-convex optimization and non-log-concave sampling, although pinning down the complexity of obtaining Fisher information guarantees is still an open question in many regimes.
- *stated as open* (p. 640): It is an open question to close this gap.
- *stated as open* (p. 640): The problem of obtaining sampling lower bounds is a notorious open problem raised in many prior works [see, e.
- *stated as open* (p. 793): Indeed, obtaining a polynomial-time convergence analysis for SGMs that holds for multi-modal distributions was posed as an open question in [LLT22].
- *stated as open* (p. 794): This answers the open question of [LLT22] regarding whether or not SGMs can sample from multimodal distributions, e.
- *proposed (author conjectures or asks)* (p. 795): 3, we conjecture that SGMs based on the CLD do not exhibit improved dimension dependence compared to the original DDPM algorithm.
- *proposed (author conjectures or asks)* (p. 807): Hence, in general, we conjecture that under our assumptions, SGMs based on the CLD do not achieve a better dimension dependence than DDPM.
- *proposed (author conjectures or asks)* (p. 807): We provide evidence for our conjecture via a lower bound.
- *proposed (author conjectures or asks)* (p. 807): We believe that it provides compelling evidence for our conjecture, i.
- *proposed (author conjectures or asks)* (p. 819): In another direction, and in light of the interpretation of our result as a reduction of the task of sampling to the task of score function estimation, we ask whether there are situations of interest in which it is easier to learn the score function (not necessarily via a neural network) than it is to (directly) sample.

## Claire Monteleoni (2006)

*Learning with online constraints : shifting concepts and active learning* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/a424d2f1-9cc7-47a9-b03f-ae0791258366/content) · [record](https://dspace.mit.edu/handle/1721.1/38308)

- *stated as open* (p. 10): 1 Motivation: open problem in active learning .
- *stated as open* (p. 16): The individual contribution of this dissertation to the fields of theoretical machine learning, and computational learning theory, is focused on several constraints to the learning problem that we have chosen because they are well motivated by fundamental questions of AI, they are relevant to practical applications, and they address open problems in the literature.
- *stated as open* (p. 65): Open problems include obtaining performance guarantees for our algorithm, or appropriate variants, in such settings.
- *stated as open* (p. 67): We then relax the distributional assumptions from Chapter 3 in various ways, motivated in part by an open problem in active learning which we present in Section 4.
- *stated as open* (p. 76): One motivation for attaining performance guarantees under distributional assumptions that are more relaxed than those of Chapter 3, is that such an analysis could potentially provide a preliminary answer to an open problem we recently proposed in [Mon06], and present here.
- *stated as open* (p. 76): This is a general problem in active learning so it could be solved by the analysis of a batch algorithm; however, solving it via the analysis of an online algorithm such as DKM would suffice, and would provide even more efficiency than required by the open problem.
- *stated as open* (p. 76): 1 Motivation: open problem in active learning Here we describe an open problem concerning efficient algorithms for general active learning.
- *stated as open* (p. 76): The purpose of this open problem is to probe to what extent the PAC-like selective sampling model of active learning helps in yielding label-complexity savings beyond PAC sample complexity.
- *stated as open* (p. 76): While the analysis of selective sampling is still in its infancy, we focus here on one of the (seemingly) simplest problems that remain open.
- *stated as open* (p. 76): No prior distribution is assumed over the concept class, however the problem remains open even under the realizability assumption: there exists a target hypothesis in the concept class that perfectly classifies all examples, and the labeling oracle is noiseless.
- *stated as open* (p. 77): Other open variants Along with the simple version stated here, the following variants remain open.
- *stated as open* (p. 77): It is clearly also an open problem when D is unknown to the learner.
- *stated as open* (p. 77): 1, here we characterize them with respect to the open problem.
- *stated as open* (p. 78): Possible approaches It is important to note that solving this open problem might only require a new analysis, not necessarily a new algorithm.
- *stated as open* (p. 78): If this were the case, then perhaps the solution to this open problem could actually be with an algorithm that is online in the sense we are concerned with in this thesis.
- *stated as open* (p. 83): The extent to which Theorem 7 addresses the open problem from Section 4.
- *stated as open* (p. 83): To the extent that the class of distributions is considered general, it answers the open problem in that it is polynomial in the salient parameters.
- *stated as open* (p. 93): Along the way, we introduced several analysis techniques, raised some interesting open problems, and made progress towards bridging theory and practice for machine learning in general, and for learning with online constraints, and active learning, in particular.

## David A Sontag (2007)

*Cutting plane algorithms for variational inference in graphical models* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/62c82638-a604-4d70-af39-5acbc57ea30f/content) · [record](https://dspace.mit.edu/handle/1721.1/40327)

- *stated as open* (p. 49): One open question is whether these cycle inequalities can be derived from our projection scheme, which 5This definition is consistent with, and slightly more general than, the definition that we gave in the beginning of the chapter.
- *stated as open* (p. 60): The results in this thesis lead to several interesting open problems.

## David Duvenaud (2014)

*Automatic Model Construction with Gaussian Processes* · [thesis](https://www.repository.cam.ac.uk/bitstreams/7baac148-8518-4895-9348-85d89980a462/download) · [record](https://doi.org/10.17863/CAM.14087)

- *stated as open* (p. 3): The time I got to spend with Roger Grosse was mind-expanding – he constantly surprised me by pointing out basic unsolved questions about decades-old methods, and had extremely high standards for his own work.
- *stated as open* (p. 214): Another open question is whether the inductive bias of deep GPs can be made to allow the sorts of long-range extrapolation shown in chapters 2 and 3.

## Edelman, Benjamin (2024)

*Combinatorial Tasks as Model Systems of Deep Learning* · [thesis](https://dash.harvard.edu/server/api/core/bitstreams/fec96a5d-45c9-4bea-a7d8-9e5503e37bde/content) · [record](https://dash.harvard.edu/handle/1/37379085)

- *stated as open* (p. 73): Analogous statements for these cases (as well as other activations and losses) would require Fourier gaps for population gradient functions other than majority; lower bounds on the degree-(k −1) coefficients (“Fourier anti-concentration”) are particularly elusive in the literature, and we leave it as an open challenge to establish them in more general settings.
- *stated as open* (p. 78): It is an open problem to extend our theoretical results to the smallbatch setting, as well as to the full range of architectures and losses in our experiments.
- *proposed (author conjectures or asks)* (p. 96): variants of SGD on MLPs which interpolate along the problem’s resource tradeoff frontier, in this section we ask whether the same can be observed end-to-end with standard training and regularization.

## Eric Xing (2004)

*Probabilistic graphical models and algorithms for genomic analysis* · [thesis](https://www.cs.cmu.edu/~epxing/papers/thesis.pdf) · [record](https://www.cs.cmu.edu/~epxing/papers/thesis.pdf)

- *stated as open* (p. 27): , 1999], provide an alternative solution, but their generality and quality remain an open problem, which hinders their widespread application.
- *stated as open* (p. 42): Chapter 6 summarizes the results of this thesis, draws a few conclusions and presents a set of open questions and directions for further investigation.
- *stated as open* (p. 62): Thus, striking the right balance between expressiveness and complexity remains an open research problem in motif modeling.
- *stated as open* (p. 216): 17) The choice of a more informative p(a) is an open issue.
- *stated as open* (p. 225): Correlating this representation of gene expression with cis-regulatory sequences is an intriguing open problem, which demands much effort in both computational image analysis and the development of appropriate probabilistic models that can interface the image models and the sequence models.

## Gane, Georgiana Andreea. (2019)

*Building generative models over discrete structures : from graphical models to deep learning* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/baf47b9e-826f-4807-9376-059fc035288e/content) · [record](https://dspace.mit.edu/handle/1721.1/121611)

- *stated as open* (p. 3): Designed explicitly for efficient sampling, Perturbation Models are strong candidates for building generative models over structures, and the leading open questions pertain to understanding the properties of the induced models and developing practical learning algorithms.
- *stated as open* (p. 7): Through to his unique research insights in a fast-moving field, his hard-working style, his contagious enthusiasm for the unsolved, and, finally, through his sense of humor, Tommi has set himself up to be one of my most influential role models for years to come.
- *stated as open* (p. 15): 2-9 Unsolved samples at various iterations.
- *stated as open* (p. 15): Note that in the unsolved examples, the model correctly builds a structure in the middle of the image, but it fails to capture the finer grained structure.
- *proposed (author conjectures or asks)* (p. 18): Instead, we ask whether we can fix M and search for predictable (not necessarily BFS) orderings.
- *stated as open* (p. 32): The models are shown to provide unbiased samples from the Gibbs distribution when perturbations are independent across assignments [116, 140] and have been applied to several applications where the underlying combinatorial problem is easy to optimize, but difficult to sample from, including boundary annotation [98] and image partitioning [77], but having a full account of the properties and power of perturbation models remains an open problem.
- *stated as open* (p. 32): Furthermore, while conditioning in Gibbs' distributions is straightforward, conditioning in perturbation models implies restricting the randomizations to a non-trivial set and performing this efficiently is still an open problem.
- *proposed (author conjectures or asks)* (p. 41): 3 Markov Properties and Perturbation Models Given that typically low order perturbations lead to high order dependencies, we ask whether enforcing the Markov properties is possible in this case.
- *stated as open* (p. 44): On the other hand, conditioning in perturbation models is a challenging open problem.
- *stated as open* (p. 47): One remaining open question is whether there are distributions of perturbations -y for which the statement is more generally true.
- *stated as open* (p. 52): Unfortunately the methods do not easily extend to conditioning on sets of variables, which remains an open question.
- *stated as open* (p. 88): Figure 2-9: Unsolved samples at various iterations.
- *stated as open* (p. 93): Another essential open problem pertains to the evaluation of perturbation models.
- *stated as open* (p. 94): In short, the task of evaluating implicit models remains an open problem which requires creative application-specific metrics.
- *stated as open* (p. 94): From this perspective, both exploring more efficient implementations of the resulting QP instances, as well as identifying more problems where Sinkhorn-like operators can be applied, are exciting open problems to be addressed.

## Gerber, Patrik Róbert (2024)

*Likelihood-Free Hypothesis Testing and Applications of the Energy Distance* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/1fba062c-78fc-4c33-8240-62e759e8da0b/content) · [record](https://dspace.mit.edu/handle/1721.1/155358)

- *stated as open* (p. 43): In this case we know the distributions PZ exactly, but we do not know whether it is equal to PX or PY .
- *stated as open* (p. 45): This relation between the sample complexity of estimation and goodness-of-fit testing has not been observed before to our knowledge, and the generality of this phenomenon remains open.
- *stated as open* (p. 61): However, this result leaves open questions about the sample complexity of their test, and in particular, whether it is able to achieve known minimax rates.
- *stated as open* (p. 76): This can be regarded as a sort of unsupervised step in the classifier training procedure, since we do not know whether PZ = PX or PZ = PY .
- **Open problem 1** (p. 130): Study the dependence on M > 2 of likelihood-free testing with M hypotheses. Another possible avenue of research is the study of local minimax/instance optimal rates, which is the focus of recent work [199, 13, 45, 44, 137] in the case of goodness-of-fit and two-sample testing. Open problem 2. Define and study the local minimax rates of likelihood-free hypothesis testing. Our discussion of the Hellinger case in Section 2.3.4 is quite limited, natural open problems in this direction include the following. Open problem 3. Let P ∈{PH(β, d, C), PDb(k, CDb), PD(k)}. (i) Study nGoF and nTS for P under Hellinger separation. (ii) Determine the trade-off RLF for P under Hellinger separation. More ambitiously, one might ask for a characterization of ‘regular‘ models (P, d) for which goodness-of-fit testing and two-sample testing are equally hard and the region RLF is given by the trade-off in Theorem 2.3.2. Open problem 4. Find a general family of ‘regular‘ models (P, d) for which nGoF(ε, d, P) ≍nTS(ε, d, P) and RLF(ε, d, P) ≍{m ≥1/ε2, n ≥nGoF(ε, d, P), mn ≥n2 GoF(ε, d, P)}.
- **Open problem 2** (p. 130): Define and study the local minimax rates of likelihood-free hypothesis testing. Our discussion of the Hellinger case in Section 2.3.4 is quite limited, natural open problems in this direction include the following. Open problem 3. Let P ∈{PH(β, d, C), PDb(k, CDb), PD(k)}. (i) Study nGoF and nTS for P under Hellinger separation. (ii) Determine the trade-off RLF for P under Hellinger separation. More ambitiously, one might ask for a characterization of ‘regular‘ models (P, d) for which goodness-of-fit testing and two-sample testing are equally hard and the region RLF is given by the trade-off in Theorem 2.3.2. Open problem 4. Find a general family of ‘regular‘ models (P, d) for which nGoF(ε, d, P) ≍nTS(ε, d, P) and RLF(ε, d, P) ≍{m ≥1/ε2, n ≥nGoF(ε, d, P), mn ≥n2 GoF(ε, d, P)}. Recent follow-up work [74] showed that Scheffé’s test is also minimax optimal and achieves the entire trade-off in Figure 2.1. It appears that the optimality of Scheffé’s test is a consequence of the minimax point of view. Basically, in the worst-case the log-likelihood ratio between the hypotheses is close to being binary, hence quantizing it to {0, 1} does not lose optimality.
- **Open problem 3** (p. 130): Let P ∈{PH(β, d, C), PDb(k, CDb), PD(k)}. (i) Study nGoF and nTS for P under Hellinger separation. (ii) Determine the trade-off RLF for P under Hellinger separation. More ambitiously, one might ask for a characterization of ‘regular‘ models (P, d) for which goodness-of-fit testing and two-sample testing are equally hard and the region RLF is given by the trade-off in Theorem 2.3.2. Open problem 4. Find a general family of ‘regular‘ models (P, d) for which nGoF(ε, d, P) ≍nTS(ε, d, P) and RLF(ε, d, P) ≍{m ≥1/ε2, n ≥nGoF(ε, d, P), mn ≥n2 GoF(ε, d, P)}. Recent follow-up work [74] showed that Scheffé’s test is also minimax optimal and achieves the entire trade-off in Figure 2.1. It appears that the optimality of Scheffé’s test is a consequence of the minimax point of view. Basically, in the worst-case the log-likelihood ratio between the hypotheses is close to being binary, hence quantizing it to {0, 1} does not lose optimality. Consequently, an important future direction is to better understand the competitive properties of various tests and studying some notion of regret, see [2] for prior related work. Open problem 5.
- **Open problem 4** (p. 130): Find a general family of ‘regular‘ models (P, d) for which nGoF(ε, d, P) ≍nTS(ε, d, P) and RLF(ε, d, P) ≍{m ≥1/ε2, n ≥nGoF(ε, d, P), mn ≥n2 GoF(ε, d, P)}. Recent follow-up work [74] showed that Scheffé’s test is also minimax optimal and achieves the entire trade-off in Figure 2.1. It appears that the optimality of Scheffé’s test is a consequence of the minimax point of view. Basically, in the worst-case the log-likelihood ratio between the hypotheses is close to being binary, hence quantizing it to {0, 1} does not lose optimality. Consequently, an important future direction is to better understand the competitive properties of various tests and studying some notion of regret, see [2] for prior related work. Open problem 5. Study the competitive optimality of likelihood-free hypothesis testing algorithms, and Scheffé’s test in particular.
- **Open problem 5** (p. 130): Study the competitive optimality of likelihood-free hypothesis testing algorithms, and Scheffé’s test in particular.
- *stated as open* (p. 130): 5 Open problems A natural follow-up direction to the present paper would be to study multiple hypothesis testing where PX and PY are replaced by PX1, .
- *stated as open* (p. 172): We leave the removal of extra logarithmic factors for classifier-accuracy tests as an open problem.
- *stated as open* (p. 342): 9 Limitations and Future Directions Finally, we discuss several limitations of our work and raise open questions that we hope will be addressed in future works.
- *stated as open* (p. 342): Third, it remains open to extend our theory to include data-dependent K, as opposed to fixed K.

## Golowich, Noah (2025)

*Theoretical Foundations for Learning in Games and Dynamic Environments* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/209ed58a-6a99-4877-8ddd-db5b48ab822a/content) · [record](https://dspace.mit.edu/handle/1721.1/164054)

- *stated as open* (p. 3): Additionally we obtain near-optimal bounds on the communication and query complexity of approximating correlated equilibria in normal-form games (to constant approximation error), addressing several open problems in the literature.
- *stated as open* (p. 26): For general games, the computational complexity of computing a Nash equilibrium remained an open problem for many decades until it was resolved by celebrated work of [DGP09; 2For instance, evidence for the game of Mancala may date to 1500 BC [Nat95], and The Royal Game of Ur, which may have been a predecessor to Backgammon, dates back to roughly 2500 BC [Dep20].
- *stated as open* (p. 26): A subsequent work of his in 1924 [Bor24; Bor53a] established the minimax theorem for N = 5 actions (while still speculating its falsehood in general), and follow-up work of his in 1927 [Bor27; Bor53b] expressed belief that it is also true for N = 7 and explicitly posed its veracity in general as an open problem.
- **Question 1.1.1** (p. 28): What is the optimal rate of convergence of decentralized algorithms to equilibria? What is the strongest type of equilibrium which can be computed? Can we answer 6This can be cast into the setting of repeated play in games by viewing the adversary’s action space as the set of all possible [0, 1]-valued utility vectors.
- **Question 1.2.1 (Computationally efficient RL)** (p. 36): Are there computationally efficient algorithms for RL in environments with very large or infinite state spaces, but which do not rely on intractable oracles? Recently, there has been broader interest in reinforcement learning techniques due to their utility in fine-tuning large language models (LLMs) [Hua+25a; Roh+25; Hua+25b; FMR25]. In such settings, the number of states is enormous, as states correspond to text in the context window of the LLM, and computational efficiency is paramount due to the massive scale of such models. Thus, there is reason to be hopeful that some of the insights gleaned when answering Question 1.2.1 might prove useful for these LLM-related problems as well. 13Technically, these bounds require that ε be polynomially small,. Moreover, they apply more generally to the setting of regret minimization, in which one aims to bound the cumulative performance of all policies over the multiple episodes of interaction.
- **Question 1.3.1** (p. 42): Are there more modular approaches for efficiently learning equilibria in Markov games in the decentralized setting, analogous to the case of normal-form games? Can these lead to structurally simpler equilibria?
- *stated as open* (p. 43): Decentralized reinforcement learning with policy gradient methods is poorly understood, and attaining global convergence results is considered an important open problem [ZYB19b, Section 6].
- *stated as open* (p. 46): While numerous specific concrete open problems are discussed in the body of the thesis, here we reflect on some high-level directions.
- *stated as open* (p. 57): 2 for further discussion and explanations of how the results presented in this thesis address some of the open questions pertaining to online regression.
- **Conjecture 2.6.3 (PCP for PPAD conjecture [BPR15])** (p. 64): There are constants ε, δ > 0 so that EOTL has a polynomial-time reduction to (ε, δ)-GCircuit. We remark that Conjecture 2.6.3 is slightly weaker (i.e., more plausible) than [BPR15,
- *stated as open* (p. 380): 3Whether such a poly log T factor can be removed remains an open question.
- *stated as open* (p. 384): In the online setting, the effect of localization can be obtained in some special cases, such as learning with square loss, by using offset Rademacher complexities [RS14b; LRS15b]; extending such techniques to our setting of realizability with absolute loss is an interesting open problem.
- *stated as open* (p. 596): Obtaining such a characterization for proper learners remains open.
- *stated as open* (p. 599): Determining the complexity of ε-CE was a well-known open question in this field; see e.
- *stated as open* (p. 600): Another advantage of our result is an improved total runtime of ̃O(N) for constant ε, compared to the previous Ω(N 3) runtime of [BM07], which answers an open question from that paper for constant ε.
- *stated as open* (p. 753): Moreover, [Pen25] used an algorithm which is very similar to TreeSwap (and similar analysis) to come up with the first polynomial-time algorithm for d-dimensional calibration, thus resolving decade-old open questions of [AM11; HK12].
- **Question 6.1.1** (p. 756): Is there a forecaster which guarantees expected calibration error O(T 2/3−ε), for some constant ε > 0?
- **Question 8.1.1** (p. 877): Is there an algorithm which learns an ε-optimal policy in an unknown linear Bellman complete MDP using poly(H, d, |A|, ε−1) samples and time? A sizeable portion of the work on computationally efficient RL in the last several years has been focused on answering Question 8.1.1 for settings which are strict special cases of linear Bellman completeness. The simplest such setting is the tabular setting, which describes the case that |S|, |A| are finite and the goal is to obtain sample and computational complexities scaling as poly(H, |S|, |A|). In this setting, there are several computationally efficient algorithms which can be viewed as variants of value iteration that are optimistic in the sense that they add bonuses to the rewards to induce exploration: these include UCBVI [AOM17] and Q-learning-UCB [Jin+18; ZZJ20], which are known to obtain near-optimal rates. Tabular MDPs are generalized by the linear MDP setting, in which feature vectors φh(s, a) ∈Rd are given, and the state-action transition probabilities are assumed to be linear in φh.
- **Problem 8.4.5 (Bonus function)** (p. 893): Fix h, t (which determine (Σ′, Λ′) = truncσ((Σ(t) h )−1/2) as above), and some β > 1. Can we find a Bellman-linear function F (t) h : S →R≥0 which satisfies:
- **Question 9.1.1** (p. 942): Given poly(k, log d) ≪d interactions with the environment, can we efficiently leverage the sparsity of the model to learn a near-optimal policy? As suggested by the terminology, sparse linear MDPs are connected to the well-studied supervised learning problem of sparse linear regression. In particular, consider the static setting where in each step we observe a covariate x and a reward y that is assumed to be a sparse linear function of x. Sparse linear regression usually refers to the problem of estimating E[y|x] from few samples. There is a rich literature on the sample complexity of this problem, not only from the perspective of information-theoretic rates [SC16; RXZ19] but also from the perspective of computationally efficient algorithms such as Orthogonal Matching Pursuit [TG07; CW11], the Lasso [Tib96; Wai09], and variants thereof [CT07; NT09; BCW11; Kel+22]. The Lasso, in particular, is the workhorse behind feature selection in a wide range of applications [UGH09; ZMW19; Ily+22] because of its simplicity and efficacy.
- **Question 9.2.3** (p. 945): Are there any well-motivated classes of block MDPs for which we can give computationally efficient learning algorithms? Given that efficient supervised learning is a prerequisite, it is natural to start from decoding functions for which the associated concept class already has a distribution-independent2 PAC learning algorithm in the presence of stochastic noise. 2The reduction in [GMR24b, Appendix F] shows that distribution-specific supervised learning is a prerequisite for learning in horizon-2 block MDPs, where the distribution for the supervised learning problem
- *stated as open* (p. 966): In fact, since it is not known how to efficiently solve generic convex programs exactly, we need to be more careful with our analysis of the computational complexity.
- *stated as open* (p. 1461): Thus, identifying an assumption which enables efficient planning in overcomplete POMDPs is an intriguing open question.
- *stated as open* (p. 1461): However, numerous open questions remain, from specific problems such as planning in overcomplete POMDPs, to the broad agenda of computationally efficient RL.
- **Conjecture 10.7.1 (ETH [IP01])** (p. 1542): There is no 2o(n)-time algorithm which can determine whether a given 3SAT formula on n variables is satisfiable. Let φ be a 3SAT formula on n variables and m clauses. Fix some γ > 0 satisfying 1/n ≤γ ≤1/2. We next construct a γ-observable POMDP Mφ based on φ as follows. At a high level, a plan for the POMDP Mφ,γ specifies, for each of some number T of independent trials, an assignment of the n variables of φ. For each trial, Mφ,γ chooses one of the m clauses uniformly at random (as enconded in Mφ,γ’s transition matrices), and the subsequent transitions of that trial check whether the chosen assignment satisfies that clause. The value of any policy for Mφ,γ lies in [0, 1]; in order for the value of some policy to be close to 1, it is necessary that the assignments chosen by that policy satisfy all of the T trials with high probability. As we will show, by making T large enough compared to γ, we can ensure that if (and only if) there is a policy that satisfies all T trials with high probability, then φ is satisfiable.
- **Conjecture 10.7.1** (p. 1545): We remark that the lower bound of Theorem 10.7.4 uses POMDPs Mφ,γ for which all observation matrices are of the type in item 2 of Example 10.9.1. With minimal changes to the proof it may readily be seen the same lower bound holds instead using observation matrices of the type in item 1 of Example 10.9.1 (in particular, it only remains to note that in Lemma 10.7.3 the actions are still independent of the clause under the event E).
- *stated as open* (p. 1806): As a whole, the issue of developing computationally efficient algorithms for RL problems is wide open, with a plethora of intriguing open questions (see, e.
- *stated as open* (p. 1807): Finding a general model of learning in “approximate MDPs” which yields nonvacuous regret bounds in our setting is an interesting open problem.
- *stated as open* (p. 2067): 15 Open Questions In this chapter we have demonstrated the first quasipolynomial-time (and quasipolynomialsample) algorithm for learning observable POMDPs.
- *stated as open* (p. 2067): Even the planning version of this question (where the parameters of the POMDP are known and the problem is to find a near-optimal policy) is open.
- *stated as open* (p. 2108): While these methods are foundational and perform well in practice [Sch+15; Sch+17; KT00], especially in settings with large or continuous action spaces, their theoretical convergence remained poorly understood and a major open problem [ZYB19b, Section 6].
- *stated as open* (p. 2110): 1, we leave the question of developing provable guarantees for strongly decentralized algorithms of this type as an important open question.
- *stated as open* (p. 2114): While our guarantees are stronger than GDA, we believe that giving guarantees that hold for individual (in particular, last) iterates rather than on average over iterates is an important open problem.
- **Problem 13.4.2** (p. 2117): Does the extragradient method with constant learning rate have last-iterate convergence for the ratio game (13.12) for any fixed ζ > 0? Additional experiments with multi-state games generated at random suggest that the extragradient method has last-iterate convergence for general Markov games with a positive stopping probability. Proving such a convergence result for extragradient or for relatives such as the optimistic gradient method would be of interest not only because it would guarantee last-iterate convergence, but because it would provide an algorithm that is strongly independent in the sense that two-timescale updates are not required. — **partial here** ([details](../../solutions/catalog-research/round3.md))
- **Problem 14.1.1** (p. 2212): Is there an efficient algorithm that, when adopted by all agents in a Markov game and run independently, leads to sublinear regret for each individual agent?
- *proposed (author conjectures or asks)* (p. 2212): Motivated by these successes, we ask whether an analogous theory can be developed for Markov games.

## Hamilton, Linus (2022)

*Applications and limits of convex optimization* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/57ca9609-c9ac-472f-9fb9-a93374312a84/content) · [record](https://dspace.mit.edu/handle/1721.1/145023)

- *stated as open* (p. 3): The Paulsen problem, a longstanding open problem in operator theory, was recently resolved by Kwok et al [40].
- **Question 1** (p. 12): Let v1, . . . , vn∈Rdbe an arbitrary ε-nearly equal norm Parseval frame. Does there necessarily exist an exactly equal norm Parseval frame w1, . . . , wn∈Rd, such that the total squared distance ∑︀‖vi−wi‖2 is at most poly(d, ε)? What is the best upper bound on the total squared distance?1
- **Problem 4 (Operator Scaling)** (p. 14): Given matrices V1, . . . , Vn: Rd→Rnwhere d> n, find matrices S: Rn→Rnand A: Rd→Rdso that, setting Wi= SViA, we have ∑︁ WiWT i= In and ∑︁ WT iWi= m dId. The two equality conditions here should spark déjà vu back to the definition of an equal-norm Parseval frame. Kwok et al [40] noticed that Problem 2, our lineartransformation-based strategy for the Paulsen problem, can be reduced to operator scaling. Say we want to solve Problem 2 for a certain list of vectors v1, . . . , vn∈Rd. Construct an equivalent instance of operator scaling by defining each Vias the matrix whose ith column is viand whose other columns are zero. Why is this equivalent? Well, let (S, A) be the solution to this operator scaling problem. The matrix Ais the solution to the original instance of Problem 2, taking the role of transforming each vector vivia the same linear transformation. Then, Sscales each resulting vector to have unit norm. The two equality conditions in the operator scaling problem mandate the unit norm and Parseval conditions respectively. The fastest known algorithm for operator scaling uses convex optimization [3].
- *stated as open* (p. 46): This means if we could improve the running time to no(r) this would yield the first no(k) algorithm for learning k-sparse parities with noise, which is a long-standing open question.

## Jan-Christian Jan-Christian Klaus Hütter (2019)

*Minimax estimation with structured data : shape constraints, causal models, and optimal transport* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/358fad17-7a60-4d33-829a-c46692be60f3/content) · [record](https://dspace.mit.edu/handle/1721.1/122184)

- *proposed (author conjectures or asks)* (p. 60): We conjecture that a similar bound holds true for a version of the least-squares estimator where the projection onto Mv is replaced by the unrestricted version M, but our current proof technique does not allow us to conclude this.
- *proposed (author conjectures or asks)* (p. 97): Lower bounds for the SVT estimator Since the anti-Monge matrix 6 in the above proof cannot be approximated by a lowrank matrix at a better rate, we conjecture that for this choice of 6, the rate of convergence given by Theorem 3.
- *proposed (author conjectures or asks)* (p. 97): 2 ) entries, we conjecture that for any choice of threshold p in the estimator (3.
- *proposed (author conjectures or asks)* (p. 141): We conjecture that these might be relaxed while maintaining many of the guarantees we give in Section 5.
- *stated as open* (p. 196): Though the parametric n-1/ 2 rate is optimal, we do not know whether the dependence on k or d in Theorem 6.

## Jerry Li (2018)

*Principled approaches to robust machine learning and beyond* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/b28fb8c2-dcd8-4405-9bf1-fac90b86f4b4/content) · [record](https://dspace.mit.edu/handle/1721.1/120382)

- **Question 1** (p. 23): Given adversarially corrupted high dimensional data, how can we efficiently extract meaningful information from it? This question is purposefully left somewhat vague, and in this thesis we will explore a number of variations on this theme. In general, this question is of great interest to data scientists and computer scientists, both in theory and in practice. Classically this field has been known as robust statistics; more recently it has gained a lot of attention in machine learning as adversarial ML. This problem has been studied in both statistics and machine learning for over fifty years [Tuk60, Hub64], yet until recently the algorithmic aspects of this question were shockingly poorly understood.
- *stated as open* (p. 97): More specifically, we leave the following as a very interesting open question: given
- **Question 3.2.1** (p. 100): Do the statistical gains (achievable by computationally efficient algorithms) for sparse estimation problems persist in the presence of noise? More formally: Suppose we are asked to solve some estimation task given samples from some distribution Dwith some underlying sparsity constraint (e.g. sparse PCA). Suppose now an ε-fraction of the samples are corrupted. Can we still solve the same
- *stated as open* (p. 100): We leave it as an interesting open question to give a systematic way of doing so.
- **Conjecture 3.2.1** (p. 102): Any efficient algorithm for robust sparse mean estimation needs̃︀ Ω(k2 log d ε2 ) samples. In Appendix C.3 we give some intuition for why it seems to be true. At a high level, it seems that any technique to detect outliers for the mean must look for sparse directions in which the variance is much larger than it should be; at which point the problem faces the same computational difficulties as sparse PCA. We leave closing this gap as an interesting open problem. Robust sparse PCA Here, we study the natural robust analogue of the spiked covariance model. Classically, two problems are studied in this setting. The detection problem is given as follows: given sample access to the distributions, we are asked to distinguish between N(0, I), and N(0, I+ ρvv⊤) where vis a k-sparse unit vector. That is, we wish to understand if we can detect the presence of any sparse principal component. Our main result is the following:
- *proposed (author conjectures or asks)* (p. 102): This phenomenon only seems to appear in the presence of noise, and we conjecture that this is inherent: Conjecture 3.
- *proposed (author conjectures or asks)* (p. 105): We conjecture that a similar phenomenon occurs when we inject noise into the sparse mean estimation problem.
- *proposed (author conjectures or asks)* (p. 106): We conjecture this is necessary for any efficient algorithm.
- *stated as open* (p. 108): We leave it as an interesting open problem to show if this rate is achievable or not in the presence of error when ρ= ω(1).
- **Problem 1.4** (p. 191): 1, and present a different algorithm for this problem. Rather than assign weights to individual points corresponding to our belief as to whether or not the point is corrupted or not, this framework will simply repeatedly throw away the points which it considers the most suspicious. The key point to our analysis will be to show that under a fixed set of determinstic conditions, the algorithm always (or in some cases, in expectation) throws away more corrupted points than uncorrupted points. How does the algorithm decide how “suspicious” a point is? Recall the idea of spectral signatures, which were also key for the framework based on convex programming. For concreteness, consider the problem of robustly learning the mean of a
- *stated as open* (p. 197): We leave it as an interesting open question to give a simple, unified approach for designing the removal algorithm.
- *stated as open* (p. 235): We leave it as an interesting open question if this is necessary or not.

## Jonathan Niles-Weed (2019)

*Statistical problems in transport and alignment* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/059c8692-5fd8-410c-889c-b2a3566c4634/content) · [record](https://dspace.mit.edu/handle/1721.1/122183)

- *stated as open* (p. 54): Though the parametric n-1/ 2 rate and dependence on d are optimal, we do not know whether the dependence on k in Theorem 4.
- *stated as open* (p. 66): We do not know whether under some conditions the W, distance is in fact equivalent to a particular Besov norm S.
- *stated as open* (p. 89): We note that our results do not address the dependence on the dimension L, and obtaining sharp dependence on L is an attractive open problem.

## Liu, Allen (2025)

*Learning Theoretic Foundations for Understanding Quantum Systems* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/737b0f84-ffbb-4682-bb86-094be3507585/content) · [record](https://dspace.mit.edu/handle/1721.1/164041)

- **Question 1** (p. 21): How does temperature affect entanglement in quantum many-body systems. Specifically, at what values of βcan the Gibbs state ρβbe entangled? The study of the relationship between temperature and entanglement dates back to the start of modern quantum information [179, 22, 173]. However, the wealth of ideas generated since then has yielded surprisingly little insight into this basic question. Here, we find new insight in a departure from previous approaches. We will take inspiration from classical algorithms for approximate counting and sampling to deliver a striking new law.
- *stated as open* (p. 21): Intractability of computation is a major barrier to resolving open problems like finding the phase diagram of various canonical families of Hamiltonians, so having better algorithmic tools is of key importance in this domain [149].
- **Conjecture ([13])** (p. 22): Could low temperature Gibbs states be pseudorandom, which would explain the difficulty in finding a time efficient algorithm? This leaves us at an impasse. Quantum phenomena are most prominent at zero or near-zero temperature [9], precisely where approaches such as high-temperature series expansions fail [149]. In fact, many of these approaches work precisely because complex quantum phenomena like long-range entanglement do not arise at high temperatures. Given the seeming intractability at low temperatures, one might wonder whether quantum Hamiltonian learning, as a framework for benchmarking quantum devices or learning about the underlying physics of quantum systems, is inherently a dead end. Nevertheless, we return to the central question, which has been posed as an open question throughout the community [15, 103, 7, 13], and examine it in a new light.
- **Question 2** (p. 22): Can we give efficient algorithms for Hamiltonian learning from Gibbs states at low temperatures? We will show a surprising resolution to this question, upending prevailing beliefs. We
- **Question 4** (p. 26): What is the copy complexity of quantum state tomography with t-copy measurements? The essence of the above question is understanding whether we can interpolate between the single-copy and unconstrained multi-copy settings for quantum state tomography. Prior to the work discussed here, there has been very little understanding of this intermediate regime. Remarkably, it was not even known if we could achieve the optimal Θ(d2/ε2) copy complexity in the unconstrained setting just using measurements of t= 2 copies at a time! The t-copy setting poses an important conceptual and algorithmic challenge — the approaches in the single-copy and unconstrained multicopy extremes are very different, and seem fundamentally incompatible. To address this, we will need to develop a new algorithmic framework to synthesize the two techniques.
- *stated as open* (p. 30): Designing efficient algorithms for structure learning from Gibbs states remains an interesting open question.
- *stated as open* (p. 93): Along the way we develop several new tools of independent interest, and ultimately give a semi-definite ∗It is an interesting open question to improve our doubly exponential dependence to singly exponential.
- *stated as open* (p. 95): It is an interesting open problem whether one can extract a new kind of “locality” statement from our algorithm, to understand how general our approach is for learning quantum systems.
- *stated as open* (p. 196): However, as was the case for tomography, due to the difficulty of implementing coherent measurements over many copies, there has been a considerable amount of attention in recent years devoted to understanding the statistical power of algorithms that only use incoherent measurements, which was also posed as an open problem in Wright’s thesis [215].
- *stated as open* (p. 196): By completely pinning down the copy complexity of mixedness testing with incoherent measurements, this answers open questions of [215] and [54].
- *proposed (author conjectures or asks)* (p. 197): Here, we ask whether or not a similar characterization can be obtained for the quantum version of the question.
- *proposed (author conjectures or asks)* (p. 198): In light of this, we ask whether we can give an instance-optimal characterization of the complexity of state certification with incoherent measurements.
- *proposed (author conjectures or asks)* (p. 198): Still, we conjecture that for all σ, the copy complexity of state certification to σ with incoherent and non-adaptive measurements is the same as that with arbitrary incoherent measurements.
- *stated as open* (p. 200): Understanding the power of such algorithms in the context of mixedness testing and, more generally, spectrum testing was posed as an open problem in [215].
- *proposed (author conjectures or asks)* (p. 243): We believe that the restriction that t⩽1/εc is ultimately an artifact of our techniques, and we conjecture that̃︀Θ (︁ d3 √ tε2 )︁ is the right rate for all t⩽O(d2).

## Lu, Chen (2023)

*Upper and Lower Bounds for Sampling* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/6fe99501-47f2-4d28-a8bf-aabf70fc2b85/content) · [record](https://dspace.mit.edu/handle/1721.1/152686)

- *proposed (author conjectures or asks)* (p. 36): In a different direction, we ask the following question: are there appropriate variants of other popular sampling methods, such as accelerated Langevin [Ma+19] or Hamiltonian Monte Carlo [Nea12], which also enjoy the scale invariance of NLD?
- *stated as open* (p. 98): 7 Conclusion We conclude this chapter with some interesting open questions.
- *stated as open* (p. 321): It is an interesting open question to extend our results on MALA to other natural function classes, such as smooth and weakly convex potentials, as well as to other sampling algorithms.
- *stated as open* (p. 329): In this chapter, we establish the first lower bounds for Fisher information guarantees for sampling, resolving an open question posed in [Bal+22].
- *stated as open* (p. 330): It is an open question to close this gap.
- *stated as open* (p. 330): The problem of obtaining sampling lower bounds is a notorious open problem raised in many prior works [see, e.
- *stated as open* (p. 444): The true dimension dependence of log-concave sampling is more likely to be polynomial, and that remains an interesting open problem.
- *proposed (author conjectures or asks)* (p. 446): We conjecture that Theorem 37 holds for all κ for which √κ log d ≤d, and we leave this question for future work.
- *stated as open* (p. 532): Nevertheless, this falls short of capturing the full regime √κ log d ≤O(d), and we leave this as an open question.

## Miguel García-Ortegón (2024)

*Transfer learning in small-molecule drug discovery: From physics-based in-silico scores to realistic preclinical endpoints* · [thesis](https://www.repository.cam.ac.uk/bitstreams/73b7401c-8b5e-468c-8ae9-2786c41d4d70/download) · [record](https://www.repository.cam.ac.uk/handle/1810/379366)

- *stated as open* (p. 29): Similarly, finding the best molecular representation remains an open problem.

## Nathan Srebro (2004)

*Learning with matrix factorizations* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/90c11385-71df-4ea7-af62-32f303ced4a7/content) · [record](https://dspace.mit.edu/handle/1721.1/28743)

- *stated as open* (p. 88): The problem of finding a consistent estimator for the linear-subspace of natural parameters when Ya Xa forms an exponential family, or in other general settings, remains open.

## Neil Houlsby (2014)

*Efficient Bayesian active learning and matrix modelling* · [thesis](https://www.repository.cam.ac.uk/bitstreams/aa0b9691-a2a2-4de6-951d-df8c6c137190/download) · [record](https://www.repository.cam.ac.uk/handle/1810/248885)

- *stated as open* (p. 6): Further open issues include extending models to include covariates or to use other forms of feedback, such as binary preferences, being robust when there is very little data available, and collecting entries in an active manner.
- *stated as open* (p. 6): Dealing with partially missing inputs in discriminative models is, in general, unsolved.
- *stated as open* (p. 6): Designing a method that can smoothly interpolate between CP and CPU with partially missing inputs is an open problem.

## Persu, Elena-Mădălina (2018)

*Tensors, sparse problems and conditional hardness* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/fe076984-5b9c-486f-942b-ef32e3521ba0/content) · [record](https://dspace.mit.edu/handle/1721.1/120418)

- *proposed (author conjectures or asks)* (p. 50): We bring Young Flattenings to the TCS community and we conjecture that the tensor machinery developed in this thesis can be used to obtain algorithms for tensor decomposition, again under the smoothed model.
- *proposed (author conjectures or asks)* (p. 63): 6 We conjecture that our noise disentangling lemmas from Section 3.
- **Conjecture 47 (k-Clique Conjecture)** (p. 85): Solving the Exact-Weight-k-Clique Problem on 2hypergraphs (regular graphs) requires nk-o(l) time.

## Pérez-Breva, Luis (2007)

*DNA binding economies* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/ce332309-1c24-434b-8682-f5c2066f53dc/content) · [record](https://dspace.mit.edu/handle/1721.1/42057)

- *stated as open* (p. 151): Equilibrium uniqueness, however, remains open for the site and promoter specific economies.

## Scott W Linderman (2016)

*Bayesian Methods for Discovering Structure in Neural Spike Trains* · [thesis](https://dash.harvard.edu/server/api/core/bitstreams/2f20073f-6221-45b6-9baf-69b0552a17c2/content) · [record](https://dash.harvard.edu/handle/1/33493391)

- **Conjecture 1** (p. 192): For all b > 0, Φ(ω | b) is a monotonically decreasing function of ω with, lim 0←ω Φ(ω | b) = 1, and, lim ω→∞Φ(ω | b) = 0. Assuming this conjecture is true, as our plots suggest, all three terms in (8.10) are nonnegative. With Φ(ω | b) ≤1, the product α−1(b, ψ) pIG(ω | b |ψ|, b2) must dominate pJ∗(ω | b, ψ). Thus, the inverse Gaussian is a natural proposal distribution for a rejection sampling algorithm. To determine whether a proposed value of ω is accepted, we must sample u ∼Unif(0, 1), and check whether u < Φ(ω | b). The acceptance probability is α(b, ψ), the inverse of the scaling constant. It is bounded between [ 1 2, 1] when b ≤1. The lower bound (worst case) is achieved when ψ = 0 and b = 1. The upper bound (best case) is approached as b goes to zero or |ψ| goes to infinity. This is illustrated in Figure 8.2b for a range of b and ψ. In fact, this rejection sampling algorithm works for b ≥1 as well, but as b increases, the acceptance probability goes to zero. For this regime, the existing approaches of Windle et al. (2014) are a better choice. Determining acceptance In order to determine whether to accept or reject a proposed value of ω, we need to compare against Φ(ω | b).
- *stated as open* (p. 197): 7 considers some important open problems and directions for future work.

## Stepaniants, George (2024)

*Inference from Limited Observations in Statistical, Dynamical, and Functional Problems* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/30432aa6-2285-4fe3-a406-e7c63cf44397/content) · [record](https://dspace.mit.edu/handle/1721.1/155887)

- *stated as open* (p. 71): We leave the statistical properties of the Sinkhorn GW estimator, or more generally the construction of a polynomial-time minimax optimal estimator, as outstanding open problems.
- *stated as open* (p. 84): This would essentially be the case if bΣm were the empirical covariance computed from Xm in the original observation model, while under the oracle model it is unknown if bΣm is unbiased and/or Wishart distributed.
- *stated as open* (p. 102): Despite such substantial progress, however, applications to experimental data from nonlinear biophysical and biochemical systems still face many open problems, as existing methods require long time series recordings with low noise (e.

## Stromme, Austin J. (2023)

*Statistical aspects of optimal transport* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/d7a2c30c-4c18-4f8d-9f96-e9242708240b/content) · [record](https://dspace.mit.edu/handle/1721.1/152775)

- *stated as open* (p. 91): The authors of that work observed empirically that their smoothness assumption seemed unnecessary and left it as an open problem to remove that assumption.
- *stated as open* (p. 160): 6 Open questions We conclude by discussing some interesting directions left open in this chapter.

## Stromme, Austin J.(Austin James) (2020)

*Wasserstein barycenters : statistics and optimization* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/d669ace2-3ae0-45b7-82f2-02c3be57de88/content) · [record](https://dspace.mit.edu/handle/1721.1/127364)

- *stated as open* (p. 13): The following theorem, from our work [22], resolves this open problem.
- *stated as open* (p. 43): We provide the first analysis of exponential convergence of gradient descent in this setting, resolving an open question of [6].
- *stated as open* (p. 50): However, ensuring lower bounds along W2-geodesics is a difficult open problem [53].

## Suárez Colmenares, Felipe (2023)

*Perspectives on Geometry and Optimization: from Measures to Neural Networks* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/5bcabec7-d7d2-4f19-a0e4-daef64cde3df/content) · [record](https://dspace.mit.edu/handle/1721.1/152831)

- *proposed (author conjectures or asks)* (p. 86): We conjecture it is always possible to find a polytope representation in O(poly(log(|V|))) dimensions with the maximal entry condition.
- *proposed (author conjectures or asks)* (p. 106): We conjecture that this equivalence holds for higher order derivatives.
- *proposed (author conjectures or asks)* (p. 137): , if we perturb each iterate of GD with a vanishing amount of noise from a continuous distribution, and we conjecture that for any step size η> 0, the assumption holds for all but a measure zero set of initializations.

## Tony S. Jebara (2002)

*Discriminative, generative, and imitative learning* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/cbc63f97-bd89-40b1-aefa-50e1866004d5/content) · [record](https://dspace.mit.edu/handle/1721.1/8323)

- *stated as open* (p. 162): We complete the chapter with a brief summary and open questions.

## Turner, Paxton Mark (2021)

*Combinatorial Methods in Statistics* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/8ba90db5-1722-4fd6-b6fd-b8b3a43fc6d0/content) · [record](https://dspace.mit.edu/handle/1721.1/139383)

- *stated as open* (p. 12): Still many questions remain wide open such as the Beck– Fiala conjecture, which states that D(X1, .
- *stated as open* (p. 14): In the univariate case, it is a longstanding open question as to whether this gap can be closed, and there is evidence from statistical physics [Boettcher and Mertens, 2008], worst-case reductions [Hoberg et al.
- *stated as open* (p. 14): This remains an interesting and challenging open question.
- *proposed (author conjectures or asks)* (p. 15): We also conjecture that the GKK design performs well on models with more complicated correlation structures and unobserved covariates as is typical in problems in causal inference.
- *stated as open* (p. 32): We leave it as an interesting open question to study allocation schemes based on random bipartite matching problems for which sharp results have recently been discovered [Ledoux and Zhu, 2019].
- *stated as open* (p. 33): It is an open question as to whether there exists a polynomial-time algorithm achieving O(1) 4See Appendix 2.
- **Question 2.1** (p. 34): Suppose that m= nγfor some γ∈(0, 1). Let X denote a random m× nmatrix with independent standard Gaussian entries. What is the smallest possible value of |Xσ|∞that can be achieved algorithmically in polynomial time? In particular, it is an open problem as to whether the partial coloring method can be used to guarantee subconstant discrepancy for standard Gaussians when m= nγ. 5Karmarkar and Karp [1982] give two algorithms for number partitioning. The first one is a simple greedy heuristic, but its analysis was only performed for the uniform distribution over a decade later by Yakir [1996]. Our algorithm presented here generalizes the second one which was rigorously analyzed in the original paper of Karmarkar and Karp [1982].
- *stated as open* (p. 34): It is an open question as to whether or not the guarantee of Theorem 2.
- *proposed (author conjectures or asks)* (p. 74): To compare these results with ours on the problem of density estimation, for each method under consideration we raise the question: How large does m, the size of the coreset, need to be to guarantee that sup f∈PH(β,L) Ef‖^gS−f‖2 = Oβ,d,L (︂ n− β 2β+d )︂ ?
- **Question 5.1** (p. 117): What theoretical guarantees can be established for pedigree reconstruction in the context of our generative model when αis very close to 2? What about when the size of the alphabet Σ is finite? Can we analyze more generic models of inheritance where blocks are not inherited i.i.d. from parents? A more subtle consequence of our generative model is inbreeding, a term we use to refer to the following phenomena: (1) the presence of multiple lowest common ancestors for a pair of extant nodes, and (2) the presence of mated couples such that the two individuals in the couple have a lowest common ancestor (LCA) (see Definition 5.5 for the formal definition of an LCA). The degree of inbreeding qualitatively refers to the frequency of such structures in the pedigree. Moreover, inbreeding as in (2) is mathematically equivalent to having cycles in the pedigree. In general, a higher degree of inbreeding makes the pedigree reconstruction problem more difficult and in some cases information-theoretically impossible (see Section 5.2.1 for detailed examples). Our choice of model allows for some degree of inbreeding, and our algorithm and analysis are carefully tailored to circumvent this obstacle.
- **Question 5.2** (p. 117): What theoretical guarantees can be established for reconstruction of pedigrees in generative models with some combination of (i) a higher degree of inbreeding, (ii) mutations, (iii) non-monogamous mating, and (iv) inter-generational mating?
- *stated as open* (p. 117): Our first open question considers relaxing the previously discussed assumptions.

## Varun Kanade (2012)

*Computational Questions in Evolution* · [thesis](https://dash.harvard.edu/server/api/core/bitstreams/77670bb4-6ebf-446a-a882-8c62be6885bb/content) · [record](https://dash.harvard.edu/handle/1/9795488)

- *stated as open* (p. 30): It is not known whether these mutations occur uniformly at random across the genome (see for example [33]).
- *stated as open* (p. 147): All of these characterizations are in the fixed distribution setting, and the corresponding question in the distributionindependent case is still open.

## Yeang, Chen-Hsiang, 1969- (2004)

*Inferring regulatory networks from multiple sources of genomic data* · [thesis](https://dspace.mit.edu/server/api/core/bitstreams/0f00c68b-79bc-40e8-bb7e-b1bc89161d12/content) · [record](https://dspace.mit.edu/handle/1721.1/28731)

- *stated as open* (p. 24): Therefore, studying the gene regulatory effects of protein modifications remains an open problem.
- *stated as open* (p. 46): Using these building blocks to construct the entire network of gene regulation remains an open problem due to the incomplete knowledge in biology and the complexity of the underlying system.
- *stated as open* (p. 81): Since we do not know whether an interaction exists a priori, it is difficult to evaluate this probability from empirical data.
- *proposed (author conjectures or asks)* (p. 189): Rather than setting the stringent criterion that all genes experience significant and coherent changes in all experiments, we ask whether a gene set as a whole has the propensity of significant changes in each experiment.
