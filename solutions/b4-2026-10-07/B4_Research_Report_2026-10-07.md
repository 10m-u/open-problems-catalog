# B4: Optimal stopping and search under partial information

## Research update to the 7 October 2026 handoff

**Research session:** 8 October 2026 UTC (7 October in America/Chicago).  
**Scope:** the seven retained statements in the attached B4 handoff.  
**Deliverables:** this complete research report, `B4_Statement_Ledger_2026-10-07.json`, and the verification archive.  
**Evidence level:** written mathematical proofs, independent written audits, primary-source comparisons, and executed exact finite computations. No theorem was compiled in a proof assistant. No novelty, publication, or peer-review claim is made.

The strongest results are a conditional no-PTAS theorem for the full Q535 model, exact-policy counting hardness for Q536, and exact-order counting hardness for Q541. Constructive results include a fixed-scenario FPTAS for Q536, a support-band prophet inequality and an exact binary-alphabet algorithm for Q540, and a fixed-scenario/fixed-type FPTAS for Q767. The exact unrestricted formulations of Q540, Q767, Q1496, and Q2390 remain unresolved in this work; Q536's approximation classification for an unrestricted number of scenarios also remains incomplete.

### Results at the retained statement scope

| Question | Disposition | Result established here | Boundary that remains |
|---|---|---|---|
| [Q535](#q535) | Conditional negative resolution of the PTAS branch | A deterministic PTAS with deterministic execution implies P=NP. Randomized schemes are excluded under NP not contained in BPP. Hardness holds with zero costs, no decay, equal delays, Bernoulli rewards, and at most two useful times per box. | The instant-inspection and time-independent-distribution special cases are outside this reduction. |
| [Q536](#q536) | Partial | Exact executable-policy synthesis is #P-hard under polynomial-time Turing reductions already for two scenarios and at most four values. Every fixed number of scenarios admits an FPTAS for nonnegative rewards. | A universal constant or PTAS when the scenario count varies is not established. |
| [Q540](#q540) | Partial | An explicit support-band guarantee, a 3/4 guarantee for a common two-point residue alphabet, and an exact O(nm)-arithmetic algorithm for finite-support common binary residues. | The half-prophet theorem for unrestricted bounded nonnegative residues remains unresolved. |
| [Q541](#q541) | Counting-hardness resolution | Producing an optimal permutation is #P-hard under polynomial-time Turing reductions, even with n=d+1 and strictly positive rational probabilities. That restricted search problem is Turing equivalent to permanent. | No many-one completeness, strong-hardness, fixed-color classification, or matching general upper classification is claimed. |
| [Q767](#q767) | Partial | An FPTAS when both the scenario count and number of interchangeable box types are fixed; an unbounded gap between optimal fixed orders and fully adaptive search. | Polynomial universal-constant approximation for unrestricted mixtures and box types remains unresolved. |
| [Q1496](#q1496) | Unresolved | Source scope and prior numerical evidence are preserved. | No exact limiting Robbins value or certified enclosure is produced. |
| [Q2390](#q2390) | Unresolved | Current primary-source theorem scope is checked. | No ordinal 1/e theorem for all finite matroids is proved here. |

Here “disproved” in the machine ledger for Q535 means that the affirmative PTAS proposition is ruled out under the stated complexity assumption. It does not mean an unconditional separation of complexity classes. For Q541, “proved” labels the written hardness theorem, not a many-one NP-completeness assertion. These are proposed reconciliations; the handoff's historical catalog decisions have not been overwritten.

### Main formulas and their implications

For Q535, a scheduling optimum of \(K^*\) is transformed into an optimal expected search utility

\[
\mathrm{OPT}=g(K^*),\qquad g(K)=1-\left(1-\frac1{2n}\right)^K.
\]

A policy's trajectory under all-zero observations supplies a feasible schedule. The utility slope estimate converts a deterministic \((1-\varepsilon)\) policy into a \((1-2\varepsilon)\) schedule. For randomized policies it first gives the corresponding expected schedule-size bound; the proof states the separate probabilistic extraction and complexity assumption. Integer compression proves that the horizon is polynomial as a numerical value, so the reduction does not hide a pseudo-polynomial encoding.

For Q536, two rational Bernoulli product laws \(P,Q\) give a stopping gadget with

\[
C(P,Q)=1+\frac12\operatorname{TV}(P,Q).
\]

An initial deterministic offer turns the first policy action into a comparison with \(C\). Polynomially many such comparisons recover the exact rational value. This handles the requested executable-policy output. The approximation algorithm rounds probabilities to geometric subprobabilities and keeps relative likelihood exponents; it never reveals the latent scenario.

For Q540, if \(X_i\in\{0\}\cup[\ell,u]\) and \(c=u/\ell\), an observable rule guarantees

\[
\mathbb E Y_\tau\ge
\frac{3}{c+1+2\sqrt{c^2-c+1}}\,\mathbb E\max_iY_i.
\]

The factor is \(3/4\) for a common binary residue alphabet and at least \(1/2\) when \(c\le2\sqrt2-1\). The proof actually needs only independence of the common cause from the whole residue vector, a weaker condition than the canonical mutual independence. The support restriction is a genuine remaining condition.

For Q541, the mandatory exhaustion rule and \(n=d+1\) give

\[
\mathbb E T=n-\Pr(\text{the first }d\text{ dice cover all colors}).
\]

The completion probability is a permanent. The proof goes further than value hardness: a two-candidate construction makes the last die of every optimal permutation answer a strict comparison, permitting a recursive count using only returned orders. A quantitative perturbation preserves the winner while making all probabilities positive.

For Q767, the same geometric likelihood idea extends to nonnegative opening charges and a nonnegative terminal minimum. Costs are charged on their pre-opening histories; missing rounded mass removes only future charges. Fixed box types make the remaining inventory compact. The separate adaptivity-gap example has fully adaptive cost \(5/4\), while its best fixed-order cost is \((m+1)/2\).

### Exact observations about the value of memory

| Model and fully specified instance | Full-history optimum | Best arbitrary rule using only time and current value | Best fixed threshold |
|---|---:|---:|---:|
| Q536: two hidden product scenarios, two low-valued signals, safe 1, final 2 or 0 | 5/4 | 1 | 1 |
| Q540: independent Bernoulli base/residues with probabilities 3/8, 1/8, 1/4, 3/8 | 469/512 | 107/128 | 1701/2048 |

These comparisons allow all deterministic functions of the stated simpler information, rather than checking one chosen threshold. Randomization cannot improve the finite maxima. The Q540 full-history gain over the best current-value rule is \(41/428\), approximately 9.579%, relative to that rule's payoff; the Q536 gain is 25%. Both examples preserve the hidden-state observation restrictions. A utility gap alone does not establish enjoyment or a good game design.

### Evidence and reproduction

The full exact suite executed six processes for five questions, all with exit code zero, in 7.341451 seconds on Python 3.12.14. It uses standard-library rational arithmetic and no external service. Run `python run_all.py` from the extracted `b4_research` directory. `REPRODUCIBILITY.md` gives complete domains, fixed seeds, commands, output paths, and the distinction between exact controls and optional floating exploration.

The archive contains the original attached handoff unchanged, all proof chapters, independent audit notes, scripts, input fixtures, generated exact certificates, policy enumeration output, and the complete suite log. A SHA-256 manifest identifies the packaged files. Prior Robbins numbers and the Family 111 import remain prior evidence, with their original limitations. No inaccessible catalog files were presumed or reconstructed.

The independent reviews checked the following concrete risks: integer interval compression and the explicit horizon; deterministic versus randomized approximation assumptions; extracting a hard quantity from an action or order without a value oracle; ties and zero-probability histories; rational encoding sizes; subprobability rounding without renormalization; paid-cost accounting; and the full-support perturbation gap. These are written reviews by separate agents in the same session, not external peer review.

The main external hardness dependencies are the published equal-length, two-alternative Job Interval Selection theorem, the exact total-variation counting-hardness theorem for Bernoulli products, and Valiant's permanent theorem. Each relevant chapter identifies the source and imported scope. The original 1999 scheduling proof PDF was not retrieved successfully; its precise strengthened restriction was verified in a primary author restatement. The new transfers below are written in full.

## Complete arguments and retained formulations

The quoted formulations at the start of each question are copied verbatim from the handoff. Each chapter then distinguishes assumptions, argument, computation, and remaining scope.

---

<a id="q535"></a>

## Q535: Does time-dependent Pandora search admit a PTAS?

**Stable statement ID:** `e73cca50c72b11a00581`.

**Exact retained statement:**

> In Pandora’s Box Over Time there are n boxes, integer processing delays p_i≥0, and an explicit horizon H≥n+∑_i p_i. Inspecting unused box i at time t costs c_i(t)≥0, draws V_it from a known nonnegative distribution D_it, and prevents another inspection before t+1+p_i. All box-time draws are independent. Stopping is allowed only after every initiated inspection has completed (t_i+p_i≤T). At stopping time T≤H, collect max_{inspected i} v̄_i(V_it,T−t−p_i), minus all inspection costs; 0≤v̄_i(v,τ)≤v̄_i(v,0)=v. Waiting and adaptive inspection/stopping are allowed. Does this optimization problem admit a polynomial-time approximation scheme, or can one rule out a PTAS under a standard complexity assumption? Preserve the source’s value-oracle access for expected maxima of reservation-truncated independent rewards, or state an explicit finite-support encoding. Approximation is multiplicative relative to optimal expected net utility, with stopping without inspection available.

**Programme:** B4. **Question:** Q535. **Stable statement ID:** `e73cca50c72b11a00581`.

**Retained target.** Does Pandora's Box Over Time, with the independent box-time draws, explicit finite horizon, waiting, processing delays, deterioration rules, and multiplicative expected-net-utility benchmark in the handoff, admit a PTAS?

**Result.** A deterministic PTAS would imply P=NP. A randomized polynomial-time approximation scheme (including a policy that randomizes its decisions) would yield a randomized PTAS for an APX-hard scheduling problem, and is excluded under NP not contained in BPP. This result already holds with zero costs, no deterioration, identical processing delays, a reward alphabet of {0,1}, and at most two times at which each box has a nonzero reward probability. The horizon and every input table have polynomial size. It is therefore a negative answer to the general PTAS target under a standard complexity assumption. It does not resolve the source's instant-inspection or time-independent-distribution special cases.

**Evidence:** written reduction, primary-source comparison, and exact finite checks. No proof assistant was used. No priority claim is made for the reduction.

### 1. External hardness dependency

Job Interval Selection (JISP) asks for a largest set of pairwise disjoint intervals, using at most one of the intervals assigned to each job. Spieksma proves MAX-SNP hardness even when every job has two alternative intervals and all intervals have equal length. The source is F. C. R. Spieksma, *On the approximability of an interval scheduling problem*, Journal of Scheduling 2 (1999), 215–227, DOI https://doi.org/10.1002/(SICI)1099-1425(199909/10)2:5%3C215::AID-JOS27%3E3.0.CO;2-Y. The equal-length/two-alternative restriction is explicitly restated by the same author with T. Erlebach in *Simple Algorithms for a Weighted Interval Selection Problem*, ISAAC 2000, §1.1, printed p. 2 of the author manuscript: https://www.researchgate.net/publication/225552747_Simple_Algorithms_for_a_Weighted_Interval_Selection_Problem .

The general no-PTAS conclusion and the strengthened restriction were checked against these primary author/publisher materials. The original 1999 full PDF was not successfully retrieved through the web reader; the proof below takes the published JISP hardness theorem as an external dependency and proves the transfer in full. Several mirrors or restatements of one theorem do not constitute independent proofs of that theorem.

The source for Q535 is Amanatidis et al., *Pandora's Box Problem With Time Constraints*, arXiv:2407.15261v3, 15 November 2025, §§2 and 5: https://arxiv.org/html/2407.15261v3 . Section 5 explicitly asks whether a PTAS can be ruled out. The transfer here exploits arbitrary time dependence and a positive common processing delay.

### 2. Polynomial integer encoding of equal-length intervals

This step prevents a hidden pseudo-polynomial dependence on the horizon.

Suppose there are N rational equal-length intervals. First normalize their length to one and sort their left endpoints u_1<=...<=u_N. Use half-open intervals. If the original convention declares endpoint contact a conflict, increase the common length by a positive rational smaller than every positive gap between disjoint intervals, and normalize again. This preserves all conflicts and has polynomial bit complexity.

Set L=N+1. For every i<j impose the following difference constraints on integer left endpoints x_i:

- x_i-x_j<=0;
- if the original intervals intersect, x_j-x_i<=L-1;
- otherwise, x_i-x_j<=-L.

These constraints are feasible. Before scaling, the corresponding bounds are 0, 1 (strict), and -1. Any directed simple cycle has an integer bound sum C>=0. If the cycle includes r>=1 strict inequalities, feasibility of the original representation implies C>0, hence C>=1. After scaling and tightening its bound sum becomes LC-r>=N+1-N>0. A cycle without strict inequalities has nonnegative bound sum. Thus the integer constraint graph has no negative cycle. Shortest-path potentials from a new source give integer solutions. Every simple path has at most N edges of magnitude at most L, so after translation the starts lie in [1,1+NL].

The intervals [x_i,x_i+L) have precisely the original conflict graph: intersecting pairs have start difference at most L-1 and disjoint pairs have start difference at least L. The job partition is unchanged. The conversion is polynomial and preserves the optimum exactly.

### 3. Constructing the Pandora instance

Let there be n jobs and let K* be the maximum number schedulable. After the preceding conversion, job i has at most two integer starts A_i and common interval length L. Construct n boxes as follows:

1. Every box has processing delay p_i=L-1.
2. Inspection costs are identically zero.
3. There is no deterioration: vbar_i(v,tau)=v.
4. Let theta=1/(2n). At an allowed time t in A_i, V_it is Bernoulli(theta) on {0,1}. At any other time it is deterministically zero.
5. All box-time variables are mutually independent, as required by Q535.
6. Take H=max(nL,max_i max(A_i)+L). Then H>=n+sum_i p_i and all useful inspections complete within H.

The explicit arrays (costs, support/probabilities and deterioration rule) have polynomial length: N<=2n and H=O(n^2). Stopping without inspection is allowed and returns zero. Waiting is allowed exactly as in the target model.

Starting a box at t occupies the interval [t,t+L), because another inspection cannot start before t+1+p_i=t+L. Its outcome is available by t+p_i. This agrees with the scheduling conflict constraints.

### 4. Exact characterization of the optimal utility

Define \(g(k)=1-(1-\theta)^k\).

**Lemma.** The constructed instance has optimal expected net utility g(K*).

**Proof.** A feasible JISP solution of size K* supplies an inspection schedule. Inspect along it and stop at the first outcome one. If every inspection gives zero, stop after the last one. This earns g(K*).

For the reverse inequality, fix all random bits of an arbitrary feasible policy. Follow its trajectory on which every observed outcome is zero. The useful inspections on this trajectory form a feasible JISP schedule, of some size K<=K*. Inspections at other times produce no reward and cannot increase this size. Before the first success the actual observations coincide with this trajectory. Independence makes the probability of at least one success exactly 1-(1-theta)^K. The final reward is at most one and is zero if no success occurs. Therefore expected utility is at most g(K)<=g(K*). Average over the policy's random bits if necessary. This proves the lemma. ∎

In particular, the bound covers adaptive inspection decisions, arbitrary waiting, policies that continue after a success, and policies that stop early on failure.

### 5. Approximation-preserving transfer

For 0<=K<=K*<=n,

\[
\begin{aligned}
g(K^*)-g(K)
&=\theta\sum_{j=K}^{K^*-1}(1-\theta)^j\\
&\ge\theta(1-\theta)^{n-1}(K^*-K)\\
&\ge\frac{\theta}{2}(K^*-K).
\end{aligned}
\]

where the last bound uses (1-theta)^(n-1)>=1-(n-1)theta>=1/2. Also g(K*)<=theta K*.

If a deterministic policy earns U>=(1-epsilon)g(K*), its all-zero trajectory has size K and U<=g(K). Consequently,

\[
K^*-K\le\frac{2}{\theta}\bigl(g(K^*)-g(K)\bigr)
\le\frac{2\varepsilon}{\theta}g(K^*)\le2\varepsilon K^*.
\]

The trajectory is obtainable with at most H rounds and n simulated observations. A PTAS for the Pandora problem, invoked with epsilon=delta/2, would therefore be a PTAS for JISP. This contradicts its MAX-SNP hardness unless P=NP.

For a randomized scheme, let K be the size extracted from a random seed's zero trajectory. Its guarantee implies E[g(K)]>=(1-epsilon)g(K*), hence E[K*-K]<=2epsilon K*. By Markov's inequality, K>=(1-4epsilon)K* with probability at least one half (the weak endpoint convention does not affect amplification). Independently repeating and selecting the largest extracted schedule gives a polynomial-time randomized approximation scheme. This contradicts NP not contained in BPP via the standard constant-gap consequence of MAX-SNP hardness. A deterministic synthesis procedure that outputs a genuinely randomized policy falls under this randomized conclusion unless a suitable seed can also be found deterministically.

### 6. Oracle contract

The reduction uses explicit two-point distributions and thus meets the finite-support option in Q535. It also does not hide any computational difficulty in the paper's expected-maximum oracle. A set of a active Bernoulli proxies and any number of deterministic-zero proxies has expected maximum 1-(1-theta)^a. More generally, for reservation-truncated two-point variables, sort their nonzero heights and evaluate the expected maximum by a product of zero probabilities at each level; this is exact rational polynomial-time arithmetic. Zero costs can use reservation value one (or any value at least one).

### 7. Computational checks and limits

`verify.py` separately implements (a) exhaustive interval-choice enumeration and (b) a time/subset Bellman recursion, and verifies OPT=g(K*) on an exhaustive family and seeded cases. It also tests the integer compression by checking every pairwise conflict before and after conversion and checks the quantitative approximation-transfer inequality with fractions. `results.json` records the generator, seed, ranges, all instance results, and run counts. These checks test the implementation and the finite identities. They do not establish complexity hardness by experiment; the reduction above establishes that claim.

---

<a id="q536"></a>

## Q536: Efficient optimal stopping under a finite mixture of product distributions

**Stable statement ID:** `85ea7e49998acbab5d24`.

**Exact retained statement:**

> There are m known scenarios, each specifying n distributions on a common set of k reward values. A scenario is sampled uniformly once; conditional on it, the n rewards are sampled independently. Rewards arrive in their fixed order. A policy observes the prefix and must irrevocably stop on one observed current reward, maximizing expected payoff. Can an optimal online stopping policy be computed in time polynomial in m,n,k (and the bit length for rational inputs)? If exact optimization is intractable, what approximation to the optimal online payoff is possible? The computational output must permit the policy’s stop/continue decision at an observed history without expanding an exponential history tree.

Research date: 7 October 2026 (America/Chicago). Stable statement ID: **85ea7e49998acbab5d24**.

### Disposition

**The exact polynomial-time policy-synthesis target has a negative answer unless FP = #P, and therefore unless P = NP.** The reduction below already uses a uniform mixture of two product distributions and at most four reward values. It applies to the requested computational output: a policy whose decision at an observed history is efficiently evaluable. Hardness of merely reporting the policy's expected value would not establish that conclusion; Section 3 explicitly supplies the missing policy-decision reduction.

For nonnegative rewards, **every fixed number m of scenarios admits a deterministic FPTAS** with an explicitly stored policy table and polynomial-time online decisions. The dependence on m is exponential. When m is part of the input, a simple polynomial-time policy attains a factor **1/min(m,n,k₊)**, where k₊ is the number of distinct positive reward values. A universal constant or PTAS for variable m is not established here.

These are written mathematical arguments with exact finite computational checks. No proof assistant theorem was compiled. Independent written audits were completed during this session; their scope is recorded in `cross_audit.md`. The whole question's disposition is **partial**, with its exact-computation branch resolved conditionally and its general approximation classification still incomplete.

### 1. Retained model and source comparison

An input consists of a common reward set R={r₁,…,r_k}, m scenarios s∈{1,…,m}, and rational probabilities p_{s,i}(r) for each i∈{1,…,n}. The scenario S is uniform. Conditional on S=s, rewards X₁,…,X_n are mutually independent and X_i has distribution p_{s,i}. The policy observes only the reward prefix, accepts the current reward irrevocably, and must accept by time n. It never observes S directly. Input numerators and denominators use binary encoding. Both preprocessing and the output policy's history-decision computation must be polynomial for the exact target.

Cristi's original question is model (2) in Section 4.2, printed pages 172–173 of [Approximation Algorithms for Stochastic Optimization, Dagstuhl Seminar 25132](https://drops.dagstuhl.de/storage/04dagstuhl-reports/volume15/issue03/25132/DagRep.15.3.159/DagRep.15.3.159.pdf), DOI [10.4230/DagRep.15.3.159](https://doi.org/10.4230/DagRep.15.3.159). Its uniform scenario, conditional independence, common support, fixed order, and online comparator are retained. The handoff adds the rational bit and policy-output contracts, also retained here.

The hardness result uses only nonnegative rewards and allows probability zero or one; “supported in a common set” does not require strictly positive mass on every value. The FPTAS and multiplicative baselines explicitly assume nonnegative rewards. If the Q536 wording is read to permit signed rewards, these approximation results are a specialization; a multiplicative approximation to a negative optimum is not an appropriate performance contract. Section 5 gives a signed-reward additive consequence.

#### External hardness dependency

Arnab Bhattacharyya, Sutanu Gayen, Kuldeep S. Meel, Dimitrios Myrisiotis, A. Pavan, and N. V. Vinodchandran, *Total Variation Distance for Product Distributions is #P-Complete*, [arXiv:2405.08255v1](https://arxiv.org/html/2405.08255v1), 14 May 2024; published in *Information Processing Letters* 189 (March 2025), article 106560, DOI [10.1016/j.ipl.2025.106560](https://doi.org/10.1016/j.ipl.2025.106560).

Theorem 1, Section 2, printed page 2, establishes #P-hardness of exact total variation between two product distributions of rational Bernoulli variables. The displayed domain is p_i,q_i∈[0,1]. The source's proof uses counting subset products and permits polynomial-time Turing reductions. Only that hardness theorem, its domain, and its reduction type are imported here. The stopping reduction and approximation proof below are independent deductions. No claim is made that their novelty has been exhaustively checked.

### 2. A stopping gadget computes total variation

Let P=⊗_{i=1}^r Bern(p_i) and Q=⊗_{i=1}^r Bern(q_i), with rational parameters. Define

\[
\operatorname{TV}(P,Q)=\sum_{x\in\{0,1\}^r}(P(x)-Q(x))_+.
\]

Choose a hidden scenario uniformly from {P,Q}. The r first observations encode the corresponding Bernoulli bits as rewards 0 or 1. The next reward is deterministically 1 under both scenarios. The final reward is deterministically 2 under scenario P and deterministically 0 under scenario Q. Thus n=r+2, m=2, and R={0,1,2}.

Every signal reward is at most the later guaranteed reward 1. A policy can therefore postpone any proposed signal-stage stop until the guaranteed 1 without losing reward. An optimal policy may be chosen to reject all signals. After observing signal string x of positive mixture probability, the posterior probability of P is P(x)/(P(x)+Q(x)). At the guaranteed 1, continuing has conditional expected payoff 2P(x)/(P(x)+Q(x)), while stopping returns 1. Hence the optimal value of the gadget is

\[
\begin{aligned}
C(P,Q)
&=\frac12\sum_x\max\{P(x)+Q(x),2P(x)\}\\
&=\frac12\sum_x\bigl(P(x)+Q(x)+(P(x)-Q(x))_+\bigr)\\
&=1+\frac12\operatorname{TV}(P,Q).
\end{aligned}
\]

Strings with P(x)+Q(x)=0 contribute zero and require no posterior definition. All random coordinates are independent conditional on the selected scenario; deterministic coordinates preserve that property. No hidden label is revealed before the last reward.

**Value conclusion.** Exact optimal-value computation is #P-hard under polynomial-time Turing reductions even for m=2,k=3. The policy for this unprefixed gadget is nevertheless easy to implement: reject signals and compare the two likelihoods at the guaranteed 1. Consequently, this value result alone is not a hardness proof for synthesizing a policy.

### 3. From an optimal policy's first decision to the exact hard quantity

Prepend one deterministic reward b∈[1,3/2] to the preceding gadget. The new instance has n=r+3, m=2 and the common support {0,1,b,2}, of cardinality at most four. Its optimal value is max{b,C(P,Q)}.

At its first observation, every optimal deterministic policy must continue if b<C(P,Q), and must stop if b>C(P,Q). Either decision is permitted at equality. Suppose a polynomial-time algorithm produces an optimal policy with polynomial-time history decisions. Running the algorithm on this instance and evaluating its policy at history (b) provides exactly this comparison. Its first decision is reached with probability one, so off-policy or unreachable-history ambiguities cannot matter.

#### Polynomial encoding and reconstruction

Write p_i=a_i/b_i and q_i=c_i/d_i in rational form and let

\[
D=\prod_{i=1}^{r}b_i d_i.
\]

The binary length of D is at most the sum of the input denominator lengths. Each mass P(x) and Q(x) is an integer multiple of 1/D. Thus TV(P,Q)=z/D for some integer 0≤z≤D, and C(P,Q) lies on the known lattice (1/(2D))ℤ inside [1,3/2].

Maintain a closed interval [l,u] initially [1,3/2]. Query b=(l+u)/2. If the returned optimal decision continues, replace l by b; if it stops, replace u by b. In a strict comparison the retained half is forced. At equality both choices retain the exact value as an endpoint. Thus arbitrary tie conventions preserve the invariant C(P,Q)∈[l,u].

After t=⌊log₂D⌋+1 queries, the interval width is 2^{−t−1}<1/(2D). Its endpoints have O(log D) bits, so every probe instance is polynomial in the original rational input length. Exactly one lattice point remains. It is recovered by computing ceil(2Dl)=floor(2Du), and TV(P,Q)=2(C(P,Q)−1) follows.

**Policy theorem.** Exact optimal-policy synthesis with polynomial-time online decisions is #P-hard under polynomial-time Turing reductions, even for a uniform mixture of two scenarios and at most four nonnegative reward values. A deterministic polynomial-time solution implies FP=#P, hence P=NP.

This is a Turing-hardness result, not a claimed many-one PP-completeness classification of a decision language. It does not show that every instance needs a large policy representation; the hard computation can reside in one first-action bit. Randomized policies cannot improve the optimum of this finite stopping problem. If a randomized policy is exactly optimal, a strict first-step comparison still forces the correct action with probability one; no bounded-error synthesis complexity collapse is asserted without specifying that algorithmic contract.

#### General space upper bound

Exact value computation and exact history decisions can be performed in polynomial space by depth-first Bellman recursion. To see the bit bound, multiply m, every input probability denominator, and every reward denominator into a common integer M. For every deterministic policy, each scenario/outcome contribution to expected reward has denominator dividing M, as does their sum. Every subtree can be evaluated using unnormalized joint scenario/history masses, avoiding repeated conditional denominators. Its rational numerator and denominator have polynomially many bits. Recursion depth is n, and only polynomially many such rationals need be retained along one active branch. This is an FPSPACE upper bound for exact value and a PSPACE upper bound for threshold comparison, with exponential time; no matching completeness claim is proved here.

### 4. Fixed-m deterministic FPTAS

Assume r≥0 for every r∈R. Let 0<ε<1 be rational and put q=1+ε/n. For each positive conditional probability p_{s,i}(r), define

\[
d_{s,i,r}=\min\{d\in\mathbb Z_{\ge0}:q^{-d}\le p_{s,i}(r)\},
\qquad \widetilde p_{s,i}(r)=q^{-d_{s,i,r}}.
\]

Set \(\widetilde p=0\) when p=0. Every positive entry satisfies

\[
q^{-1}p<\widetilde p\le p.
\]

The rounded entries sum to at most one in each row. They are **subprobabilities**, and they must not be normalized back to one. Their role is to assign a slightly reduced mass to every stopping leaf. Equivalently, missing mass may be viewed as an artificial zero-payoff termination after each stage; this is a computational comparison, not information available to the actual policy.

#### Lemma 1: every policy's payoff is multiplicatively preserved

For a deterministic prefix-measurable policy π, let \(\widetilde U(\pi)\) be the sum of its accepted reward at each stopping leaf times the rounded joint scenario/prefix mass. Let U(π) be its actual expected payoff. A leaf at time t has one conditional probability factor for each of its t observations. Its mass is reduced by a factor in [q^{−t},1], and its reward is nonnegative. Summing over leaves and scenarios gives

\[
q^{-n}U(\pi)\le\widetilde U(\pi)\le U(\pi).
\]

The same inequality holds for randomized policies by averaging, although a deterministic maximizer suffices. Crucially, no additive truncation of rare histories is used.

#### Lemma 2: the rounded model has polynomially many states for fixed m

After a prefix, its unnormalized rounded scenario weights have the form q^{−E_s}/m, where E_s is the sum of the corresponding d entries. If any observed entry has probability zero in scenario s, that coordinate is permanently absent and is denoted ∞. Put D₀=max d_{s,i,r} over positive entries and J=nD₀. Every finite E_s lies between 0 and J.

The vector E, together with the current time, is sufficient: future conditional laws depend only on the scenario, and all accumulated likelihood information is encoded in these weights. A direct dynamic programme has at most n(J+2)^m states, with ∞ included as an additional coordinate value.

Homogeneity improves this bound. Subtract the minimum finite exponent from every finite coordinate. The removed common factor scales both stop and continue values equally and cannot change an action. The normalized state has at least one zero coordinate and all others in {0,…,J,∞}. There are at most m(J+2)^{m−1} such states per stage. All-zero scenario mass produces no reachable observation and is ignored.

#### Explicit Bellman recurrence and online policy

Let e be a normalized exponent vector before time i and let W_i(e) be the unnormalized rounded future value with weights q^{−e_s}. For an observed reward r, add d_{s,i,r} to finite coordinates, setting a coordinate to ∞ if its transition probability is zero. If all coordinates are ∞, this branch contributes zero. Otherwise let c be the minimum finite updated coordinate and e′ its normalized vector after subtracting c. Then

\[
W_i(e)=\sum_{r\in R}q^{-c(i,e,r)}
\begin{cases}
r\sum_{s:e'_s<\infty}q^{-e'_s}, & i=n,\\
\max\left\{r\sum_{s:e'_s<\infty}q^{-e'_s},\ W_{i+1}(e')\right\}, & i<n.
\end{cases}
\]

The rounded optimum is W₁(0,…,0)/m. The output policy stores the W table and the d entries. It maintains e by updating it at each observation. After observing r at time i, it stops exactly when i=n or

\[
r\sum_{s:e_s<\infty}q^{-e_s}\ge W_{i+1}(e).
\]

This uses only the observed prefix through its accumulated exponent vector. Preprocessing and table size are polynomial for fixed m; each online decision requires O(m) rational operations and a table lookup once the current state is retained. A decision supplied an entire history can reconstruct this state in O(nm) updates.

#### Lemma 3: bit complexity is polynomial

Let L bound the total binary input length. The smallest positive input probability is at least 2^{−L}. Since ln(1+ε/n)≥ε/(2n),

\[
D_0\le\left\lceil\frac{2nL\ln2}{\varepsilon}\right\rceil,
\qquad J=O(n^2L/\varepsilon).
\]

Exact exponents can be found by doubling and binary search with rational comparisons; floating logarithms are unnecessary. Write q=A/B in lowest terms. For a reachable state at its actual stage, every accumulated probability term has denominator dividing A^J. A full table that also materializes unreachable exponent vectors may instead use A^(2J), which preserves the polynomial bit bound. Multiplying by all reward denominators gives a common denominator of polynomial bit length for every Bellman value at a reachable stage/state. Magnitudes are bounded by m times the largest reward. The number of rational operations is at most O(nkm²(J+2)^{m−1}) using the normalized table, and each operation uses polynomially many bits. This is polynomial in L,n,k,1/ε for every fixed m. The factor exponential in m is explicit.

#### Approximation theorem

Let π* maximize the actual payoff and let \(\widetilde\pi\) maximize the rounded objective using the dynamic programme. Lemma 1 gives

\[
U(\widetilde\pi)\ge\widetilde U(\widetilde\pi)
\ge\widetilde U(\pi^*)\ge q^{-n}\mathrm{OPT}
\ge(1-\varepsilon)\mathrm{OPT},
\]

where the last inequality is (1+ε/n)^{−n}≥1−ε. The zero-optimum case is included. Therefore the algorithm is a deterministic FPTAS for each fixed m. This does not contradict exact #P-hardness at m=2: the reduction may require precision exponentially small in the bit length, while the FPTAS is polynomial in 1/ε.

### 5. Polynomial baselines when m varies

Three simple families are efficiently evaluable because, conditional on each scenario, their acceptance sets depend only on time and current reward.

1. For each scenario s, compute its independent-input optimal stopping policy π_s by ordinary backward induction. Let u_s be its payoff when the scenario is known to be s. For the actual uniform mixture, U(π_s)≥u_s/m by nonnegativity, while OPT≤(1/m)∑_s u_s. Averaging the U(π_s) bounds shows that the best of these m policies earns at least OPT/m. Their true mixture payoffs can be evaluated exactly in O(m²nk) rational operations.
2. A policy that chooses in advance the index with the largest marginal expectation earns at least OPT/n, because E[max_i X_i]≤∑_i E[X_i].
3. For each positive support value a, try the policy that accepts the first reward at least a, taking the last if necessary. Its payoff is at least a·Pr(max_i X_i≥a). Summing these lower bounds over the k₊ positive support values dominates E[max_i X_i], so the best policy in this family earns at least OPT/k₊. Each such policy is exactly evaluable under each product scenario.

Choosing the best actual mixture payoff across these families yields a deterministic **1/min(m,n,k₊)** approximation in polynomial time. If there are no positive rewards, the optimum is zero. This is a baseline bound, not an optimality claim for the approximation factor.

For signed rewards in [a,b], apply the fixed-m FPTAS to X_i−a. Its policy obeys

\[
E[X_\tau]\ge\mathrm{OPT}-\varepsilon(\mathrm{OPT}-a)
\ge\mathrm{OPT}-\varepsilon(b-a).
\]

### 6. Exact example and independent computational controls

The illustrative instance uses two signal stages with rewards 0 and 1/4, then a guaranteed reward 1, then a final reward 2 in P and 0 in Q. The scenario prior is uniform. Conditional signal laws are

\[
P=\mathrm{Bern}(3/4)\otimes\mathrm{Bern}(1/4),\qquad
Q=\mathrm{Bern}(1/4)\otimes\mathrm{Bern}(3/4).
\]

The bits in the table encode low/high signal rewards, not scenario observations.

| Signal bits | P mass | Q mass | Mixture mass | Posterior P | Optimal action at guaranteed 1 |
|---|---:|---:|---:|---:|---|
| 00 | 3/16 | 3/16 | 3/16 | 1/2 | Either action |
| 01 | 1/16 | 9/16 | 5/16 | 1/10 | Stop |
| 10 | 9/16 | 1/16 | 5/16 | 9/10 | Continue |
| 11 | 3/16 | 3/16 | 3/16 | 1/2 | Either action |

The exact total variation is 1/2, and the optimal payoff is 5/4. The best policy whose decisions use only the time and current reward earns 1. This comparator allows arbitrary accept/reject functions of those inputs, not merely monotone thresholds. Full history improves payoff by 1/4, or 25% of the simpler policy's value.

The complete control enumerated all **1,024** deterministic full-history policies at the ten possible nonterminal decision nodes and all **32** time-and-current-value policies at their five possible decision nodes. Independently, an exact rational Bellman solver and an exact full-trajectory evaluator both returned 5/4. The low signal reward is essential to this particular memory comparison; if signals are encoded as reward 1, survival can implicitly encode some information and the current-value comparator changes. The hardness proof only needs weak dominance, so its smaller alphabet is still valid.

The probe reconstruction was checked with both “stop at equality” and “continue at equality.” With D=256, both recovered C=5/4 and TV=1/2 using nine first-decision queries.

The FPTAS implementation was additionally checked on 16 generated rational instances with n=5,k=3,m alternating between two and three, reward set {0,2,7}, ε=1/5 for the first eight and ε=1/10 for the last eight. Each conditional row came from three pseudorandom counts in {0,1,2,3,4}, normalized exactly; an all-zero count row was replaced by (1,0,0). The seed was **53620261007**. Every case enumerated all 3^5=243 complete reward strings for independent policy evaluation, summing exact conditional-scenario masses. No Monte Carlo payoff estimates were used.

All cases satisfied

\[
(1-\varepsilon)\mathrm{OPT}\le\widetilde{\mathrm{OPT}}
\le U(\widetilde\pi)\le\mathrm{OPT}.
\]

The minimum achieved ratio in this finite test set was 1917023/1917039. This numerical quality is a finite control; the FPTAS theorem is justified by the written leaf-mass proof, not by the test set.

#### Verification archive

- `verify_q536.py`: complete Python 3 standard-library implementation of exact DP, rounded DP, full-trajectory evaluation, both exhaustive policy controls, and the probe experiment. It ran successfully.
- `q536_inputs.json`: all 16 generated input instances, including each rational probability and ε.
- `q536_certificate.json`: complete signal table, exact example values, enumerated policy counts and maximizers, both probe traces, all test outputs and assertions.
- `q536_ledger.json`: machine-readable per-result statement ledger.

Reproduction command: `python verify_q536.py`. It overwrites the two JSON experiment files deterministically. Runtime in the supplied environment was under one second. All arithmetic used Python `fractions.Fraction`. No external packages, hidden data, network access, or proof assistant are required to reproduce the computations.

### 7. Remaining scope

The fixed-m FPTAS does not give polynomial time when m grows with the input. A universal constant approximation, a PTAS for variable m, or a matching approximation hardness barrier is not supplied. The exact result establishes a standard conditional impossibility, not an unconditional separation of complexity classes. The report uses the published total-variation hardness theorem as a dependency and does not re-prove #SubsetProd completeness. Policy compactness and policy synthesis are kept distinct throughout.

---

<a id="q540"></a>

## Q540: Half-prophet utility under an unobserved additive common cause

**Stable statement ID:** `6ffd1bba3a75f8698d0c`.

**Exact retained statement:**

> Let Z,X_1,…,X_n be mutually independent nonnegative random variables with known bounded-support laws. Only Y_i=Z+X_i is revealed, sequentially in fixed order; neither Z nor any X_i is directly observed. Does every such instance admit a possibly randomized stopping rule τ∈{1,…,n}, adapted to the revealed Y-prefixes, satisfying E[Y_τ]≥(1/2)E[max_iY_i]? The rule may use the whole observation history and must accept a current value irrevocably, taking the last value if necessary. It is not restricted to one fixed threshold.

Research date: 7 October 2026 (America/Chicago; execution crossed into 8 October UTC).

**Canonical target.** Q540, stable statement ID `6ffd1bba3a75f8698d0c`: for every collection of mutually independent bounded-support nonnegative random variables `Z,X_1,...,X_n`, with only `Y_i=Z+X_i` observed in fixed order, does some stopping time adapted to the `Y` prefixes and forced to accept by `n` satisfy `E Y_tau >= (1/2) E max_i Y_i`?

**Disposition: partial.** The unrestricted target remains unresolved here. The results below prove a substantial support-restricted version, give a polynomial exact algorithm for a common binary alphabet, and certify a strict value of observation history in a tiny nondegenerate instance. These are written mathematical arguments plus executed exact rational computations. No proof assistant was used; no novelty or priority claim is made.

### 1. Source comparison and limits of the literature check

Correa, Fichtl, Jlibene, Laraki, Livanos, Schewior and Verdugo, *Threshold Dynamics and Correlated Prophet Inequalities*, arXiv:2607.09887v1, 10 July 2026, §1.1 and §3, explicitly distinguish the adaptive half-prophet question from their single-threshold-with-last family. Their reported 0.41 guarantee and Proposition 5 upper bound below 0.475 concern that restricted family. This report does not promote the latter to an impossibility for adaptive stopping.

Primary links: <https://arxiv.org/abs/2607.09887>, <https://arxiv.org/html/2607.09887v1>, <https://arxiv.org/pdf/2607.09887>. The investigating subagent retrieved indexed primary text but encountered direct-fetch errors. The root agent subsequently retrieved the full primary HTML and checked the relevant model and theorem scope. Follow-up searches did not locate a resolution; this is not an exhaustive literature-status claim. The handoff is the source of the canonical question wording, not independent evidence for the new arguments.

### 2. A support-width theorem, including a 3/4 binary guarantee

#### Theorem 1: zero or a bounded positive band

Fix `n>=1`, `0<ell<=u`, and `c=u/ell`. Let `Z>=0` be integrable and independent of the **whole** random vector `(X_1,...,X_n)`. The coordinates of that vector need not be independent. Suppose

\[
 X_i\in\{0\}\cup[\ell,u]\quad\text{almost surely for every }i.
\]

There exists a deterministic stopping rule observing only the `Y` prefixes, with forced final acceptance, such that

\[
 \mathbb E Y_\tau\ \ge\ \gamma(c)\,\mathbb E\max_iY_i,
 \qquad
 \gamma(c)=\frac{3}{c+1+2\sqrt{c^2-c+1}}.
\]

The rule is one of two explicit policies:

- **T:** accept the first `Y_i>=ell`; accept `Y_n` if no earlier value qualifies.
- **R:** retain `Y_1`, then accept the first later `Y_i>Y_1`; accept `Y_n` if none qualifies. For `n=1`, take `Y_1`.

Thus this guarantee needs at most the first observed value as retained observation history. The chosen policy is determined from the known law before any observation.

**Corollary 1a.** When every residue has the common binary alphabet `{0,d}`, the guarantee is `3/4`.

**Corollary 1b.** The original half-prophet inequality holds whenever

\[
 \frac{u}{\ell}\le 2\sqrt 2-1\approx1.828427124746.
\]

This includes arbitrary continuous distributions within the positive band. The support restriction is essential to the present proof. It is not a proof for unrestricted bounded supports.

**Corollary 1c.** If all residues have a common alphabet `{a,b}` with `0<=a<b`, applying Corollary 1a after subtracting the known `a` yields

\[
 \mathbb E Y_\tau\ge\frac34\mathbb E\max_iY_i+\frac a4.
\]

Here T uses the original-value threshold `b`, and R is unchanged.

#### Proof of Theorem 1

Scale by `ell`, so the positive residues lie in `[1,c]`. Write

\[
 e=\mathbb E Z,\quad
 q=\Pr(\exists i:X_i>0),\quad
 p=\Pr(X_1>0),\quad
 r=\Pr(Z\ge1).
\]

The scaled `Z` is meant in this display. The only properties needed below are `0<=p<=q<=1`, `0<=r<=1`, and `e>=r`. The last follows from nonnegativity of `Z`.

If `Z<1`, policy T selects a positive residue whenever any exists, so its selected residue is at least one on that event. If `Z>=1`, it accepts the first value and its selected residue is at least `1{X_1>0}`. Independence of `Z` from the residue vector therefore gives

\[
 \mathbb E Y_T\ge e+(1-r)q+rp
                 =e+q-r(q-p). \tag{1}
\]

For R, on the event `X_1=0` and some residue is positive, the first positive residue is a strict rise from `Y_1=Z`, and is accepted. On all other events the selected residue is nonnegative. Hence

\[
 \mathbb E Y_R\ge e+q-p. \tag{2}
\]

Both policies receive the same realized additive base `Z` at their stopping time; taking its expectation does not require the stopping time to be independent of `Z`.

Choose T if `r(q-p)<=p`, and R otherwise. Equations (1)–(2) then guarantee

\[
 A:=\mathbb E Y_\tau
 \ge e+q-\min\{p,r(q-p)\}
 \ge e+\frac q{1+r}. \tag{3}
\]

To check the second inequality, if `p<=rq/(1+r)`, use the first member of the minimum. If `p>=rq/(1+r)`, then `r(q-p)<=rq/(1+r)`.

The prophet is at most

\[
 P:=\mathbb E\max_iY_i\le e+cq. \tag{4}
\]

If `q=0`, both policies achieve the prophet exactly. Otherwise the ratio

\[
 \frac{e+q/(1+r)}{e+cq}
\]

is nondecreasing in `e` and nonincreasing in `q`, for fixed `r` and `c>=1`. Since `e>=r` and `q<=1`, equations (3)–(4) imply

\[
 \frac A P\ge
 \frac{r+1/(1+r)}{r+c}
 =\frac{r^2+r+1}{(r+1)(r+c)}. \tag{5}
\]

The derivative of the last function has the sign of

\[
 c r^2+2(c-1)r-1.
\]

Its unique nonnegative root is

\[
 r_c=\frac{\sqrt{c^2-c+1}-c+1}{c}\in(0,1],
\]

and substitution into (5) gives

\[
 \min_{0\le r\le1}\frac{r+1/(1+r)}{r+c}
 =\frac{3}{c+1+2\sqrt{c^2-c+1}}.
\]

This proves the theorem. At `c=1` it equals `3/4`. The condition `gamma(c)>=1/2`, for `c>=1`, is exactly `c<=2 sqrt(2)-1`. Subtracting a common known lower value `a` proves Corollary 1c. ∎

**Algorithmic access.** In the independent-input finite-support setting, the initial choice uses `p=Pr(X_1>0)`, `q=1-product_i Pr(X_i=0)`, and `r=Pr(Z>=ell)`. These are rational and efficiently computable from the explicit input. No hidden-state observation or posterior oracle is used. The theorem also holds under the stated weaker independence assumption, but efficient computation of `q` for an arbitrary succinct correlated law is not claimed.

### 3. Exact polynomial optimization for a common binary alphabet

#### Theorem 2: a deadline formula

Retain the canonical mutual independence assumption, and suppose `X_i` is supported on the common alphabet `{a,b}`, with `0<=a<b`, and `p_i=Pr(X_i=b)`. Let `Z` have `m` explicitly listed rational support points and rational probabilities. The optimal expected reward and an optimal observation-adapted policy can be computed with `O(nm)` rational arithmetic operations, in time polynomial in the explicit input bit length. Policy decisions do not expand a history tree.

Let `d=b-a`, `q_i=1-p_i`. For `k=1,...,n`, define empty products as one and empty sums as zero, and set

\[
 A_k=1-\prod_{j=2}^{k}q_j,
 \qquad
 B_k=\sum_{j=2}^{k}
 \left(\prod_{t=2}^{j-1}p_t\right)
 \left(\prod_{t=j}^{n}q_t\right).
\]

For each possible first observation `y`, define the **joint masses**, not normalized posterior probabilities,

\[
 \alpha_y=\Pr(Z=y-a)q_1,
 \qquad
 \beta_y=\Pr(Z=y-b)p_1.
\]

There are at most `2m` such observations. The exact optimum is

\[
 \boxed{\quad
 V^*=\sum_y\left[
 y(\alpha_y+\beta_y)
 +d\max_{1\le k\le n}(\alpha_y A_k-\beta_y B_k)
 \right].\quad} \tag{6}
\]

For each `y`, retain any maximizing deadline `k(y)`.

**Policy.** After the first value `y`, if all observations so far equal `y`, continue until time `k(y)` and then accept. A first change upward reveals `Z=y-a` and a current residue `b`, so accept immediately. A first change downward reveals `Z=y-b` and a current residue `a`; from that point accept the first residue `b`, taking the last value if needed. A deadline applies only while no change has occurred.

#### Proof of Theorem 2

The first observation `y` permits at most two latent states: `Z=y-a` with first residue `a`, and `Z=y-b` with first residue `b`. Their joint masses are `alpha_y` and `beta_y`. Any first change is exactly `+d` or `-d` and identifies which state holds. Future residues remain independent with their original laws, since the variables are mutually independent.

Once the base is known, accepting the first available residue `b` and otherwise the last value is optimal: `b` is the largest possible residue, while rejecting `a` retains only opportunities of value at least `a`. Until the first change, the entire observed prefix consists of repetitions of `y`. A deterministic policy therefore has a first time `k` at which it would stop on that constant history. Every optimal deterministic policy can be represented by such a deadline followed by the optimal known-base continuation after a change. Randomization cannot improve the maximum expected reward of this finite decision problem.

Use stopping immediately at `y` as the baseline. In the `alpha_y` state, waiting until a deadline `k` gains `d` exactly when some upper residue occurs in times `2,...,k`, with probability `A_k`.

In the `beta_y` state, the baseline residue is already `b`. A loss of `d` occurs exactly when the first downward change is at some `j<=k` and no `b` occurs thereafter. For a given `j`, the residues in times `2,...,j-1` must all be `b`, and those in times `j,...,n` must all be `a`. The events for different `j` are disjoint, and their total probability is `B_k`. This proves the gain `d(alpha_y A_k-beta_y B_k)` and equation (6).

All `A_k,B_k` are computed in `O(n)` operations using prefix and suffix products. Evaluating all deadlines for at most `2m` first observations costs `O(nm)` further operations. Product and sum denominators have polynomial bit length because the formulas use products of explicitly supplied rational probabilities, each from finitely many input positions; a common product denominator suffices. The finite table of first observations and deadlines, plus the first observation or inferred base, provides polynomial-size policy output. ∎

**What this does not establish.** For three or more residual levels, a first observation change need not identify `Z`, and constant histories no longer describe all ambiguous branches. Theorem 2 supplies no polynomial bound for that general case.

### 4. An exact tiny instance where history improves utility

All four variables are mutually independent, with the following Bernoulli laws on `{0,1}`:

| Variable | Probability of 1 |
|---|---:|
| `Z` | `3/8` |
| `X_1` | `1/8` |
| `X_2` | `1/4` |
| `X_3` | `3/8` |

Only `Y_i=Z+X_i` is observed. The latent base is not separately revealed. Stopping is irrevocable, no recall is permitted, and the third value must be accepted if necessary. Inputs, posteriors, policy values and certificates use exact rational arithmetic.

#### Exact comparison

| Policy class / benchmark | Exact value | Approximate value |
|---|---:|---:|
| Full-history optimum | `469/512` | 0.916015625 |
| Best arbitrary rule using only `(time,current Y)` | `107/128` | 0.835937500 |
| Best time-dependent thresholds | `107/128` | 0.835937500 |
| Best single threshold with last acceptance | `1701/2048` | 0.83056640625 |
| Prophet | `247/256` | 0.964843750 |

Thus full history improves expected reward over the best fixed threshold by `175/2048`, or `25/243 = 10.288...%` of that threshold's reward. It improves over the best arbitrary current-value-only rule by `41/512`, or `41/428 = 9.579...%`. The adaptive-to-prophet ratio is `469/494 = 0.94939...`. This instance exhibits a history gap; it is not close to disproving the unrestricted half guarantee.

#### Optimal policy

At time 1, stop on 2 and continue on 0 or 1. At time 2:

- After `(0,1)`, stop.
- After `(1,1)`, continue.
- Stop on 2; continue on 0.

At time 3, stop. Prefixes starting with 2 are unreachable under this policy; the certificate nevertheless includes their Bellman values.

The opposite decisions at current value 1 have a direct posterior explanation. After `(0,1)`, the base is certainly zero. Continuing has conditional expected reward `3/8`, below the current reward 1. After `(1,1)`,

\[
 \Pr(Z=1\mid Y_1=Y_2=1)=\frac{63}{68},
\]

so continuing has conditional expectation

\[
 \frac{63}{68}+\frac38=\frac{177}{136}>1.
\]

Both histories have positive probability under the optimal policy. The distinction is therefore operational, not an unreachable-node artifact.

#### Short direct evaluation

The masses of first observations `0,1,2` are `35/64`, `13/32`, and `3/64`. Their optimal unnormalized contributions are respectively

\[
 \frac{595}{2048},\qquad
 \frac{1089}{2048},\qquad
 \frac{192}{2048},
\]

which sum to `469/512`. The prophet equals

\[
 \mathbb E Z+\Pr(\exists i:X_i=1)
 =\frac38+1-\frac78\frac34\frac58
 =\frac{247}{256}.
\]

For the single-threshold class, all thresholds fall into four effective classes: `t<=0`, `0<t<=1`, `1<t<=2`, and `t>2`. Their values are respectively `1/2`, `1619/2048`, `1701/2048`, and `3/4`. Time-dependent thresholds `t_1=2,t_2=1` attain `107/128`; exhaustive enumeration confirms that no arbitrary current-value-only rule does better.

### 5. General exact posterior DP and independent enumeration

For arbitrary finite-support common-base inputs, an exact DP is available, without a polynomial-time claim. For a prefix `h=(y_1,...,y_i)`, retain unnormalized posterior weights

\[
 w_h(z)=\Pr(Z=z)\prod_{j=1}^{i}\Pr(X_j=y_j-z).
\]

For a candidate next value `y`, set `w_y(z)=w_h(z) Pr(X_{i+1}=y-z)` and `m_y=sum_z w_y(z)`. The DP compares the stop contribution `y m_y` with the recursively computed continuation contribution on weights `w_y`; at the last time, it takes `y m_y`. Sum these maxima over the possible next observations. This follows from conditioning on the observed prefix and the finite-horizon Bellman principle. A deterministic maximum is sufficient at each node.

The general recursion can visit exponentially many observation prefixes. The small posterior vector does not by itself prove efficient policy computation. That limitation is preserved in the code and result ledger.

The tiny instance has 16 raw product worlds, 3 first-observation nodes, and 7 second-observation nodes. Thus there are `2^(3+7)=1024` deterministic full-history policies. A separate control enumerated all 1024 policies over the raw product worlds. Their maximum agrees with the posterior DP and with Theorem 2's formula. All 64 arbitrary `(time,current value)` policies were enumerated separately, as were all 16 time-dependent threshold combinations and all 4 fixed threshold classes. Randomized policies cannot beat these maxima because their expected rewards are convex combinations of deterministic-policy rewards.

The binary formula was also checked on 70 exactly generated cases, 10 for each `n=1,...,7`, with seed 540, Bernoulli probabilities `j/8` for `j=0,...,8`, and base support `{0,1,2,3}` with normalized random positive integer weights. Every case gave exact agreement among the general posterior DP, the binary formula and raw-world policy evaluation. The `3/4` inequality was checked exactly on each case. These are implementation controls, not replacements for the proofs.

### 6. Exploration, artifacts and reproducibility

The exploratory search exhausted 2,401 Bernoulli instances with each of the four success probabilities in `{1/8,...,7/8}`. It used floating arithmetic and selected the displayed fixture for a large history advantage. A separate seeded differential-evolution run examined the same four-parameter family. It reached its 100-iteration limit without a convergence-success flag; its best floating candidate is preserved only as exploratory output. It does not establish a minimum competitive ratio or a global maximum policy gap.

Run the exact reproduction with Python's standard library:

```bash
python exact_common_cause.py
```

The following files comprise the local verification archive:

| File | Contents / execution status |
|---|---|
| `exact_common_cause.py` | General posterior solver, binary formula, raw-world policy evaluator, exhaustive controls; executed successfully |
| `tiny_input.json` | Exact law and observation/objective contract |
| `tiny_certificate.json` | All 16 worlds, all 25 observation nodes and rational Bellman values, posterior probabilities, comparisons, deadlines and control results |
| `all_history_policies.csv` | All 1,024 policy masks and exact expected rewards; bit-to-history mapping is in the certificate |
| `run_output.json` | Compact exact output and successful-assertion record |
| `search_binary.py` | Floating grid and seeded optimizer; executed |
| `search_binary_output.json` | Raw search output, domain, seed, counts, budget, convergence flag |
| `Q540_ledger.json` | Machine-readable scope and evidence decisions |

`search_binary.py` additionally requires NumPy and SciPy. The exact certificate does not. Proof-assistant artifact: none. Compiled formal theorem: none. External manuscript proofs were not independently formalized.

### 7. Remaining questions

The original unrestricted common-base half-prophet statement is still open in this report. The useful next mathematical boundary is whether the support-band hypothesis can be removed or replaced by a decomposition that preserves one observable stopping rule. Applying a separate rule to each band does not automatically combine into a global guarantee: one cannot identify the current residue's band from `Y_i` while `Z` remains hidden. The binary exact algorithm similarly relies on identification after the first change and therefore cannot be generalized by simply adding residue levels.

The present results already give an exact small-instance balance oracle, a provable support-restricted performance floor, and a controlled example where retaining the first observation has measurable utility. They do not establish that the resulting choice structure is enjoyable for players.

---

<a id="q541"></a>

## Q541: Exact complexity of finite coupon-collection query scheduling

**Stable statement ID:** `5eb5c8b65ab784bcfab0`.

**Exact retained statement:**

> There are n independent dice with known rational outcome probabilities on d colors, each usable once. Choose a permutation before observing outcomes; reveal dice in that order until every color has appeared or all n dice have been revealed. Minimize the expected number of reveals. What is the exact computational complexity of finding an optimal permutation: is there a polynomial-time algorithm in the explicit n×d probability input and its bit length, or is the optimization NP-hard? The prescribed rule keeps revealing if collecting every color has become impossible, until all dice are exhausted.

**Date:** 7 October 2026.  
**Stable statement ID:** `5eb5c8b65ab784bcfab0`.  
**Result status:** proved by the written argument below; exact finite verification completed; no proof-assistant compilation.  
**Reduction convention:** polynomial-time Turing reductions. A many-one hardness classification of a threshold decision language is not asserted.

### 1. Retained problem and conclusion

There are \(n\) independent dice with explicitly encoded rational probability vectors on \(d\) colors, each usable once. Before observing any outcome, choose a permutation. Reveal dice in that order until all \(d\) colors have appeared or all \(n\) dice have been revealed. In particular, continue revealing when complete collection has become impossible. The objective is the expected number of reveals. The required output is an optimal permutation, not merely its value.

**Theorem.** Computing an optimal permutation for this exact problem is **#P-hard under polynomial-time Turing reductions**, even on the restricted family

\[
n=d+1
\]

and even when **every probability is strictly positive**. Consequently, a deterministic polynomial-time algorithm for finding an optimal permutation would put all #P functions in FP and would imply \(P=NP\).

For the restriction \(n=d+1\), finding an optimal permutation and computing the permanent of a \(0/1\) matrix are polynomial-time Turing equivalent. This establishes a matching oracle-complexity classification on the restricted family. For unrestricted \(n,d\), the lower bound still applies; no matching upper classification for the entire optimization problem is claimed here.

The proof extracts a comparison from the identity of the last die in *any* optimal permutation. It therefore establishes hardness of producing the order itself. It does not infer ordering hardness merely from the difficulty of evaluating an order.

The original source is Brody, Diwan, Hellerstein, and Lidbetter, *On Extensions of the Unanimous Vote Problem*, arXiv:2609.36508v1, 29 September 2026. Section 4, Definition 7 gives the retained stopping rule; Theorem 7 gives an \(O(\log d)\) approximation; Section 6, printed page 11, leaves its computational hardness open. Its different \(d\)-ary Unanimous Vote hardness theorem concerns stopping after **two** colors and is not used as a reduction here. The live HTML displays version v1 on inspection on 7 October 2026. [Primary paper](https://arxiv.org/html/2609.36508).

### 2. Dependency and notation

For a square matrix \(M=(M_{ij})_{i,j\in[m]}\), write

\[
\operatorname{per}(M)=\sum_{\sigma\in S_m}\prod_{i=1}^m M_{i,\sigma(i)}.
\]

The sole counting-hardness dependency is Valiant's theorem that computing the permanent of a \(0/1\) matrix is #P-complete. The original paper states this as Theorem 1. Its proof uses polynomial-time oracle reductions involving arithmetic. See L. G. Valiant, *The complexity of computing the permanent*, **Theoretical Computer Science** 8(2), 189–201 (1979), especially Theorem 1, printed page 194. [Publisher](https://doi.org/10.1016/0304-3975(79)90044-6); [primary-paper PDF mirror](https://www.cs.bu.edu/faculty/gacs/courses/cs535/papers/Valiant_permanent.pdf).

Other ingredients are proved here, apart from the elementary polynomial-time augmenting-path algorithm for bipartite matching. That algorithm is also implemented in the verification script.

All arithmetic below is exact rational arithmetic. Empty permanents equal 1. An oracle for the search problem may return any optimal permutation; it need not use any prescribed tie breaking.

### 3. Completion one step before exhaustion

**Lemma 1.** Suppose \(n=d+1\). For an order \(\pi\), let \(Q_\pi\) be the probability that its first \(d\) dice display all \(d\) colors. Then

\[
\mathbb E[T_\pi]=n-Q_\pi.
\]

**Proof.** Fewer than \(d\) single-color reveals cannot collect all \(d\) colors. At time \(d\), the rule stops exactly on the event defining \(Q_\pi\). On its complement the rule makes the final reveal, including when collection is already impossible. Thus \(T_\pi=d\) with probability \(Q_\pi\), and \(T_\pi=d+1=n\) otherwise. The displayed identity follows. ∎

For any specified first \(d\) dice, \(Q_\pi\) is the permanent of their \(d\times d\) probability matrix: collecting all colors in exactly \(d\) draws means obtaining a bijection from dice to colors. In particular, the objective depends only on the last die. The order of the first \(d\) dice has no effect.

### 4. The comparison construction

Let \(M\in\{0,1\}^{m\times m}\) have a perfect matching. Fix an entry \((r,j)\) belonging to a perfect matching, and define

\[
P=\operatorname{per}(M),\qquad
K=\operatorname{per}(M_{-r,-j}).
\]

Both \(P\) and \(K\) are positive integers. Let \(t>0\) be any rational. There are \(m+1\) colors: the original columns \(1,\ldots,m\), and a special color \(z\). Let

\[
w_i=\sum_{c=1}^{m}M_{ic}+t\mathbf 1_{i=r},\qquad
D=\prod_{i=1}^m w_i,\qquad
\varepsilon=\frac1{2D}.
\]

Every row of \(M\) contains a 1, so \(w_i\ge1\), \(D\ge1\), and \(0<\varepsilon\le1/2\).

Construct \(m\) independent **base dice**, with probabilities

\[
p_{ic}=\frac{M_{ic}}{w_i}\quad(c\in[m]),\qquad
p_{iz}=\frac{t\mathbf1_{i=r}}{w_i}.
\]

Add two independent dice:

\[
A:\quad p_{Az}=1;
\qquad
B:\quad p_{Bz}=1-\varepsilon,\quad p_{Bj}=\varepsilon.
\]

Unspecified probabilities are zero. Every die is normalized, and the resulting instance has \(n=m+2\) dice and \(d=m+1\) colors, hence \(n=d+1\). Denote by \(Q_{-x}\) the probability of complete collection among all dice except \(x\).

**Lemma 2.** The completion probabilities satisfy

\[
Q_{-B}=\frac{P}{D},\qquad
Q_{-A}=\frac{(1-\varepsilon)P+\varepsilon tK}{D},
\]

and for every base die \(i\),

\[
Q_{-i}\le\varepsilon<\frac{P}{D}.
\]

**Proof.** If \(B\) is omitted, die \(A\) supplies \(z\). The base dice must form a bijection to the original \(m\) colors. Their total probability is \(P/D\).

If \(A\) is omitted, condition on the outcome of \(B\). When \(B=z\), the base dice again have success probability \(P/D\). When \(B=j\), base die \(r\) is the only remaining die that can supply \(z\), and must do so. The other base dice must form a bijection to the original columns other than \(j\). Their combined success probability, including die \(r\)'s special outcome, is \(tK/D\). The first two identities follow.

If a base die is omitted, both \(A\) and \(B\) occur among the first \(d\) dice. Since there are exactly \(d\) draws and \(d\) colors to collect, their outcomes must all differ. Die \(A\) is \(z\), so \(B\) must be \(j\). This has probability \(\varepsilon\), establishing the upper bound. Finally \(P\ge1\) and \(\varepsilon=1/(2D)<P/D\). ∎

Consequently **every** optimal order places either \(A\) or \(B\) last. Its last die supplies a comparison:

\[
\begin{array}{c|c|c}
\text{Comparison}&\text{Unique optimal last die}&\text{Included candidate}\\ \hline
tK>P&A&B\\
tK<P&B&A
\end{array}
\]

At equality, either \(A\) or \(B\) is an optimal last die. There are still no optimal orders ending with a base die.

No assumption about knowing \(P\) or \(K\) was used to normalize the dice except that the caller supplies \(t\). The construction of \(D\) uses row sums of \(M\), not permanent values.

### 5. Counting a permanent using only optimal orders

Consider an oracle \(\mathcal O\) that returns an optimal permutation for each rational finite-coupon instance. The following recursive algorithm computes the permanent of an arbitrary input \(0/1\) matrix \(M\).

1. Find a perfect matching by augmenting paths. If none exists, return 0. If \(M\) is empty, return 1.
2. Choose a matched entry \((r,j)\). Recursively compute \(K=\operatorname{per}(M_{-r,-j})\). The chosen perfect matching minus that entry proves \(K\ge1\).
3. The unknown positive integer \(P=\operatorname{per}(M)\) lies in \([1,m!]\). Binary search this integer interval. At an integer split \(s\), set

   \[
   t=\frac{s+1/2}{K}=\frac{2s+1}{2K}.
   \]

4. Construct the dice in Section 4 and ask \(\mathcal O\) for an optimal permutation. If its last die is \(A\), then \(tK>P\), so the integer \(P\le s\). If the last die is \(B\), then \(P>tK\), so \(P\ge s+1\). Update the interval accordingly.
5. Return the sole integer left in the interval.

There are no comparison ties: \(P\) is an integer and \(tK=s+1/2\) is a half integer. The algorithm does not ask the oracle for an objective value, inspect revealed outcomes, or independently evaluate the returned order.

There is one recursion branch at every dimension. The total number of oracle calls is at most

\[
\sum_{k=1}^{m}\lceil\log_2(k!)\rceil=O(m^2\log m).
\]

All constructed instances have polynomial bit length. Indeed, \(s\le m!\) and \(K\le(m-1)!\), so \(t\) has \(O(m\log m)\) numerator/denominator bits. Only one row sum contains \(t\), while the others are integers in \([1,m]\). Hence \(D\), \(\varepsilon\), and every probability have \(O(m\log m)\) bits up to a constant-factor bound, and there are \(O(m^2)\) entries. Exact rational arithmetic and binary search therefore require polynomial work outside the oracle.

Valiant's theorem now proves #P-hardness under polynomial-time Turing reductions. In particular, if \(\mathcal O\) were an ordinary polynomial-time algorithm, the algorithm above would count \(0/1\) permanents in polynomial time, yielding \(\mathrm{FP}=\#\mathrm P\), in the usual sense that every #P function would be in FP.

### 6. Strictly positive probabilities

Zeros are allowed in the retained Q541 input, so Section 5 already proves the lower bound for the original question. The same argument also yields a full-support lower bound.

At a binary-search comparison \(tK=s+1/2\), the difference between the two candidate omission probabilities is

\[
|Q_{-A}-Q_{-B}|=\frac{\varepsilon}{D}|tK-P|
\ge\frac1{4D^2}.
\]

The winning candidate omission has probability at least \(P/D\ge1/D\). Every base omission has probability at most \(\varepsilon=1/(2D)\). Its separation from the winning candidate is therefore at least \(1/(2D)\ge1/(4D^2)\).

Set

\[
\eta=\frac1{16dD^2}
\]

and replace every die distribution \(p_i\) by

\[
p_i'=(1-\eta)p_i+\eta\,\operatorname{Uniform}([d]).
\]

All entries are now strictly positive rationals with polynomial bit length. Couple each perturbed die to the original one by retaining the original outcome with probability \(1-\eta\) and resampling uniformly otherwise. For any set of \(d\) dice, the probability that any resampling occurs is at most \(d\eta\). Therefore each omission's completion probability changes by at most \(d\eta\), and the difference between any two omission probabilities changes by at most

\[
2d\eta=\frac1{8D^2}<\frac1{4D^2}.
\]

The unique optimal last die is preserved. Sending the perturbed instances to the oracle therefore supplies exactly the same strict integer comparisons. This proves the asserted positive-probability restriction.

The construction uses probabilities that can be exponentially small as numbers, while their binary encodings remain polynomial. It makes no claim of strong NP-hardness, nor a lower bound when all positive probabilities have inverse-polynomial lower bounds.

### 7. Upper bound on the restricted family

For \(n=d+1\), it suffices to evaluate \(n\) rational permanents, one for each possible last die. Each permanent has a polynomial-size rational denominator. Clear denominators row by row, obtaining nonnegative integer entries \(a_{ij}\) and a known common product denominator \(L\).

The integer numerator

\[
\sum_{\sigma\in S_d}\prod_i a_{i,\sigma(i)}
\]

is a #P function. One nondeterministically guesses an encoding of a permutation \(\sigma\), rejects invalid encodings, and for each row guesses an integer in \([0,a_{i,\sigma(i)}-1]\); each valid permutation contributes exactly its product of entries. The witness lengths and membership tests are polynomial in the input bit length. Thus a #P oracle can evaluate each numerator, and exact rational comparison identifies an optimal last die. This gives membership in \(\mathrm{FP}^{\#\mathrm P}\) for the restricted search problem.

Together with Section 5, the restricted problem is polynomial-time Turing equivalent to \(0/1\)-permanent. The conclusion is an oracle/search classification, not a statement that a threshold language is NP-complete.

### 8. General exact subset algorithm and exchange identity

For a set \(S\subseteq[n]\), let \(q(S)\) be the probability that its dice contain all \(d\) colors. Inclusion-exclusion gives

\[
q(S)=\sum_{A\subseteq[d]}(-1)^{|A|}
\prod_{i\in S}\left(1-\sum_{c\in A}p_{ic}\right).
\]

If \(S_k\) is a permutation's set of first \(k\) dice, the tail-sum formula gives

\[
\mathbb E[T]=\sum_{k=0}^{n-1}(1-q(S_k)).
\]

Define \(F(\varnothing)=0\) and, for nonempty \(S\),

\[
F(S)=\min_{i\in S}\bigl[F(S\setminus\{i\})+1-q(S\setminus\{i\})\bigr].
\]

Then \(F([n])\) is the exact optimal expected cost, with an optimal order recovered from the minimizing predecessors. To prove the recurrence, partition all orders of \(S\) by their last element; the previous prefixes contribute \(F(S\setminus\{i\})\), and the additional tail-sum term is \(1-q(S\setminus\{i\})\). This argument does not allow adaptive selection or early stopping on impossibility.

The probability precomputation can be implemented by streaming over the \(2^d\) color subsets and computing products for all \(2^n\) dice subsets by a least-significant-bit recurrence. It uses \(O(2^{n+d}+nd2^d)\) rational arithmetic operations, followed by \(O(n2^n)\) DP operations. The rational numbers have polynomial bit length in the explicit input. If \(d>n\), every order has cost \(n\), and no exponential computation is needed.

For adjacent dice \(a,b\) after a common prefix set \(S\), all tail-sum terms except the intermediate prefix cancel, giving the exact exchange identity

\[
\mathbb E[T_{S,a,b,\ldots}]-\mathbb E[T_{S,b,a,\ldots}]
=q(S\cup\{b\})-q(S\cup\{a\}).
\]

Writing \(h_c(S)\) for the probability that color \(c\) is the *only* missing color after revealing \(S\), independence further gives

\[
q(S\cup\{i\})=q(S)+\sum_{c=1}^d h_c(S)p_{ic}.
\]

Thus the exchange difference equals \(\sum_c h_c(S)(p_{bc}-p_{ac})\). The weights depend on the whole selected prefix, which explains why a universal fixed pairwise sorting score does not follow from this identity.

### 9. An exact comparison certificate

Take

\[
M=\begin{pmatrix}1&1&0\\1&1&1\\0&1&1\end{pmatrix},\quad
(r,j)=(1,1),\quad P=3,\quad K=2,\quad t=7/4.
\]

Then \(D=45/2\), \(\varepsilon=1/45\), and the five dice, with colors ordered \(1,2,3,z\), are

| Die | Color 1 | Color 2 | Color 3 | Special color |
|---|---:|---:|---:|---:|
| Base 1 | \(4/15\) | \(4/15\) | \(0\) | \(7/15\) |
| Base 2 | \(1/3\) | \(1/3\) | \(1/3\) | \(0\) |
| Base 3 | \(0\) | \(1/2\) | \(1/2\) | \(0\) |
| A | \(0\) | \(0\) | \(0\) | \(1\) |
| B | \(1/45\) | \(0\) | \(0\) | \(44/45\) |

The exact completion probabilities after four reveals are:

| Last die | Complete-collection probability |
|---|---:|
| Base 1 | \(15/2025\) |
| Base 2 | \(6/2025\) |
| Base 3 | \(4/2025\) |
| A | \(271/2025\) |
| B | \(270/2025\) |

Every optimum places \(A\) last and has expected cost \(5-271/2025=9854/2025\). This answers the comparison \(P<7/2\). Repeating with \(t=5/4\) places \(B\) last and answers \(P>5/2\). Since \(P\) is an integer, the two comparisons identify \(P=3\).

The directly enumerated verifier also checks the equality case \(t=P/K\), where precisely \(2\cdot4!=48\) orders are optimal for this example; the two strict cases each have exactly \(4!=24\) optimal orders.

### 10. Executed verification and residual scope

Run with the Python 3 standard library:

```bash
python3 verify_q541.py
```

The script writes `verification.json`. The completed run used exact fractions throughout and took 4.523 seconds in this workspace. Its finite domain and controls were:

* Every \(0/1\) matrix of dimensions \(1,2,3\): \(2+16+512=530\) matrices. A permutation-sum permanent and a subset-recurrence permanent agreed on every input. The matching test agreed with positivity on every input.
* All half-integer comparison thresholds \(s+1/2\), \(0\le s\le m!\), for every positive-permanent matrix in that exhaustive domain: **1,752 comparison constructions**, with every candidate formula, base-omission bound, unique winner, and stated gap checked exactly.
* The full recursive counting reduction on all 530 matrices: **976 optimal-order oracle calls**, with each recovered count checked against direct permutation enumeration.
* Seed 541, 64 matrices of dimension 4, 32 of dimension 5, and 8 of dimension 6: **804 oracle calls using the strictly positive smoothing construction**. Every reconstructed permanent agreed with direct permutation enumeration.
* Complete realization enumeration for every permutation of two small comparison constructions, with thresholds below, at, and above equality: \(3\cdot24+3\cdot120=432\) entire-order controls. These checks explicitly implement forced exhaustion.
* A separate general \(n=5,d=3\) instance: all 120 permutations and their full outcome spaces checked against the inclusion-exclusion subset DP. The optimum was **\(371/90\)**, attained, for example, by the one-based order \((5,4,2,1,3)\). All **480 adjacent-exchange identities** agreed exactly.

The finite checks are controls for transcription and implementation. The universal counting-hardness theorem rests on the quantifier-complete written reduction, its bit analysis, and Valiant's dependency. No Lean/Coq/Isabelle theorem was compiled, and no claim is made of peer review or a published resolution. The reduction proves Turing hardness; a many-one classification, strong hardness, and the complexity when \(d\ge3\) is fixed are not established by this argument.

### Files

* `report.md`: retained statement, proof, source comparison, scope and limitations.
* `statement_ledger.json`: machine-readable claims and evidence labels.
* `verify_q541.py`: all generators, exact algorithms, finite controls, and the worked oracle reduction.
* `verification.json`: actual output from the completed run, including the fixed example's complete oracle trace.

---

<a id="q767"></a>

## Q767: Constant approximation for search under a latent mixture

**Stable statement ID:** `95579efa54844e655376`.

**Exact retained statement:**

> A known finite latent state S makes nonnegative box values conditionally independent. Opening unused box i costs c_i and reveals its value; S stays hidden. Is a universal constant approximation to E[opening costs+minimum opened value] computable in polynomial time, including online decisions, for explicit rational finite-support mixtures without a separation promise? At least one box must be opened.

**Programme:** B4. **Question:** Q767. **Stable statement ID:** `95579efa54844e655376`.

**Retained target.** Polynomial-time universal constant approximation to optimal fully adaptive expected opening costs plus minimum opened value, for arbitrary explicit rational finite-support latent product mixtures, with no separation promise and at least one opening.

**Status:** partial. The unrestricted constant-approximation question remains unresolved here. The results below do not replace the fully adaptive benchmark with a precommitted order.

**Evidence:** written proofs and exact rational finite computations. No proof-assistant theorem and no claim of publication priority.

### 1. Exact posterior dynamic programme

Write rho_s for the prior scenario probability and p_{is}(v) for a box's conditional value law. After a history h of opened box/value pairs, retain unused boxes U, current minimum b (infinity before any opening), and the unnormalized scenario weights

\[
w_s=\rho_s\prod_{(i,v)\in h}p_{is}(v).
\]

At a state with positive total weight W=sum_s w_s, let J(U,b,w) be the weight-scaled optimal remaining disutility, excluding costs already paid. Stopping costs bW and is available only when b is finite. Opening i costs c_i W and reveals v with updated weight vector w^v_s=w_s p_{is}(v). Therefore

\[
J(U,b,w)=\min\left\{bW,\ \min_{i\in U}\left[c_iW+
\sum_v J\bigl(U\setminus\{i\},\min(b,v),w^v\bigr)\right]\right\},
\]

where the stop term is omitted before the first opening, zero-mass branches are omitted, and at U=empty one stops. This recurrence carries the posterior without revealing the latent state. It is exact rational arithmetic, but exponential size in general. The full remaining set U is a separate source of difficulty from posterior storage.

### 2. An explicit unbounded gap between fixed-order and fully adaptive policies

For any integer m>=2, choose a uniform hidden scenario S in {1,...,m}. There are m target boxes B_1,...,B_m, each of cost one, and one diagnostic box A of cost 1/4. Let H=m+1. Conditional on S=s, all values are deterministic:

- B_s has value zero;
- each B_j with j!=s has value H;
- A has value H+s.

Degenerate distributions are conditionally independent, so this is an explicit finite-support product mixture in the exact Q767 model. Observations reveal box values only; the value of A identifies S as an inference.

**Theorem.** The fully adaptive optimum is 5/4. The optimum among fixed orders with adaptive stopping is (m+1)/2. The ratio is 2(m+1)/5, and is unbounded.

**Proof of the adaptive optimum.** Open A and then B_S. The cost is exactly 1/4+1 and the final minimum is zero. Any policy beginning with A must pay at least one further target-opening cost to beat the diagnostic's value, so cannot improve on 5/4. If its first opening is a target B_j, it pays one. With probability (m-1)/m it fails to find zero. On that event, stopping gives a remaining value H>=3, and continuing until a zero requires at least one more unit-cost target opening. Thus any policy beginning with a target has cost at least 1+(m-1)/m>=3/2. Randomization cannot improve the minimum over first actions. ∎

**Proof of the fixed-order optimum.** A fixed-order policy is a permutation, followed until an adaptively chosen stopping position; it cannot reorder or skip unopened earlier positions. Before the zero target is reached, every opened value is at least H. Continuing through all remaining targets costs at most m, so stopping before finding zero is dominated. Consequently each scenario pays at least the position of its target among the m targets. Averaging these positions gives (m+1)/2. The diagnostic cannot lower the minimum, cannot change target order, and adds a nonnegative cost. Omitting it (or putting it last) attains the bound. ∎

For m=3 this is a four-box exact instance: adaptive cost 5/4, best fixed-order cost 2, and gap 3/4. The executable certificate evaluates every one of the 24 permutations by a separate scenario-consistent stopping recursion and compares it with the fully adaptive posterior DP. It also checks m=2 and m=4.

This is an adaptivity-gap theorem, not computational inapproximability for adaptive policies. It explains why a constant approximation to the best fixed order does not settle Q767. It also exhibits a small information-design instance in which observing a costly diagnostic has measurable value.

### 3. An FPTAS when the number of scenarios and box types are fixed

Assume there are m latent scenarios and d box types. A type consists of an opening cost and one finite-support distribution in each scenario. There can be any number of boxes of each type, independent conditional on the scenario. Let n be the total number of boxes and k the number of distinct possible values. Equal-type unused boxes are exchangeable.

**Theorem.** For each fixed m and d, there is an FPTAS for the fully adaptive Q767 objective, with no separation assumption. Both policy construction and each decision at an observed history take time polynomial in n, k, input bit length, and 1/epsilon. The output value is at most (1+epsilon)OPT for 0<epsilon<=1, including instances with OPT=0.

**Probability rounding.** Set q=1+epsilon/(2n). Replace each nonzero conditional probability p by p'=q^{-ceil(log_q(1/p))}; keep zero probabilities zero. The exponent is found using exact rational comparisons with powers of q, not floating-point logarithms. Thus p/q<p'<=p, with equality p'=p possible at a power. Every conditional law becomes a subprobability law; do not renormalize it. Its missing mass is an artificial absorbing event with no future cost or terminal-value charge.

**Uniform multiplicative comparison for any policy.** Decompose expected disutility into nonnegative terms: the cost of each possible opening times the probability of reaching its history, plus each stopping minimum times the probability of its terminal history. Each history has length at most n. Under rounded subprobabilities, each term's probability lies between q^{-n} and one times its true probability. If J(pi) and J'(pi) denote these two objectives, then

\[
q^{-n}J(\pi)\le J'(\pi)\le J(\pi)
\]

for every observation-adapted policy pi. Costs already paid on an artificial absorption are still accounted for by the opening-cost terms; they are not charged again or canceled. This decomposition is why nonnegative costs and values matter.

**Finite sufficient state.** Keep the remaining multiplicity of each type, the current minimum, and the cumulative rounded exponent e_s for each scenario; a zero likelihood gets a separate infinity marker. The rounded weight of scenario s is rho_s q^{-e_s}. If B bounds the bit length of the input probability denominators, the largest one-step exponent D is O(nB/epsilon). Along any history e_s<=nD. The resulting state count is at most

\[
(n+1)^d(k+1)(nD+2)^m.
\]

Use the exact recurrence in §1 on this state space, with subprobability transition laws. Initial stopping remains forbidden. Exchangeability makes an opening action a choice of type, not a choice among exponentially many subsets. All exponents and arithmetic bit lengths are polynomially bounded. At an observed history, update the type count, minimum, and exponents, and consult the table.

Let pi' minimize the rounded objective. Then

\[
J(\pi')\le q^nJ'(\pi')\le q^nJ'(\pi^*)
\le q^nJ(\pi^*)\le(1+\varepsilon)\mathrm{OPT}.
\]

For the final inequality use q^n<=exp(epsilon/2)<=1+epsilon for 0<=epsilon<=1. The last elementary bound follows by monotonicity of 1+epsilon-exp(epsilon/2) on this interval. This also proves the claim when OPT=0. ∎

**Changed assumptions:** fixed m and fixed number d of interchangeable box types. This is not polynomial jointly in unrestricted m and d, so it does not close the question as registered. The FPTAS is proved here by adapting the likelihood-rounding argument developed for Q536 in the same research packet; it does not depend on the separated-mixture theorem in the literature.

### 4. Primary-source scope comparison

Singla's thesis, Question 13.3.1, printed p.197 (PDF p.211), supplies the hidden-state disutility objective: https://faculty.cc.gatech.edu/~ssingla7/papers/thesis_Sahil.pdf . Chawla, Gergatsouli, McMahan and Tzamos, arXiv:2108.12976v4 (21 July 2023), §6, obtain a constant factor under an identical-or-TV-separated condition, with running time n^{tilde O(m^2/delta^2)}: https://arxiv.org/html/2108.12976v4 . Bansal, Huang and Zhu, arXiv:2509.17029v2 (10 October 2025), §2.2, use the optimal partially adaptive fixed-order policy as comparator: https://arxiv.org/html/2509.17029v2 . Neither comparison establishes a polynomial universal constant against the unrestricted fully adaptive optimum here.

### 5. Reproducibility

`verify.py` uses Python's exact `Fraction` arithmetic, no sampling and no external packages. Its outputs are in `results.json`, including all fixed-order values and a noisy, repeated-type instance checking the FPTAS decision table under the original (unrounded) distributions. The finite certificate is independent of the asymptotic complexity proof.

---

<a id="q1496"></a>

## Q1496: The limiting full-information expected rank

**Stable statement ID:** `8b77f8589cc4d5f5cdc9`.

**Exact retained statement:**

> Determine the exact value of v=lim_{n→∞}v_n.

**Source setup retained from the handoff:** Observe independent U(0,1) variables X₁,…,X_n sequentially. Select exactly one by a stopping time τ≤n adapted to the observed values, without recall. Its final rank is R_τ=Σ_{j=1}^n1{X_j≤X_τ}; set v_n=inf_τ ER_τ.

**Status: unresolved.** No new theorem or numerical certificate for this retained statement is established in this report.

---

The handoff's values V(5)=1.5707281364801 and V(6)=1.6320777151 remain prior numerical results with tolerance agreement, not interval-certified enclosures. The corrected memoryless comparison and fitted sufficiency-ladder percentages retain their original numerical and model limitations. The finite-n computations do not identify the exact limit. No original numerical source artifacts were supplied and no new V(7) calculation was attempted.

The primary author page describes an MDP approach to numerical improvement and calls Robbins' problem open: [Léonard Brice, Other Research](https://lnrdbrice.github.io/other-research.html), section “Robbins' problem”. Primary indexed metadata for [arXiv:2608.27419](https://arxiv.org/abs/2608.27419) was found, but the full manuscript could not be retrieved through the reader in this session. This limited check supplies no exact asymptotic solution. Details and access failures are recorded in `q1496_q2390_scope.md`.

---

<a id="q2390"></a>

## Q2390: Optimal ordinal matroid secretary ratio

**Stable statement ID:** `20bb4427a9a4677b822d`.

**Exact retained statement:**

> For every finite M, does such an algorithm guarantee E[w(A)]≥e^(−1) max_{I∈I}w(I) for every weight assignment?

**Source setup retained from the handoff:** A known finite matroid M=(E,I) has adversarial nonnegative weights, hidden until elements arrive in uniformly random order. An ordinal online algorithm sees only relative weight rankings and matroid information, and irrevocably accepts an independent subset; computation is unrestricted.

**Status: unresolved.** No new theorem or numerical certificate for this retained statement is established in this report.

---

The full primary manuscript [Abdi, Banihashem, Hajiaghayi and Mittal, arXiv:2609.19118v1](https://arxiv.org/pdf/2609.19118), was retrieved. Its Theorem 1.2, printed p.3, states an ordinal 1/e guarantee for **linear** matroids, using finite linear programmes without a polynomial-time bound. Corollary 1.4 states a 1/64 ordinal guarantee for all matroids. Section 3 and Theorem A.2 characterize the optimum for a fixed matroid by a finite LP; they do not give a universal 1/e lower bound. These are source-scope comparisons, not independently verified new theorems in this report.

The handoff's Family 111 claim concerns a one-sample prophet model with an adversary that sees samples, values, and the complete random seed. Its claimed factor 2^−310 and lack of polynomial-time guarantee remain an unchecked import. It is **scope-nonmatch** to the retained ordinal random-arrival question, and no kernel compilation was performed. Neither a sample-access guarantee nor a theorem for a proper matroid subclass closes Q2390.

---

## Proposed next mathematical steps

The next steps follow the remaining gaps in the proofs rather than increasing finite computation indiscriminately.

1. **Q535 and Q541:** obtain external specialist review of the approximation-preserving and search-oracle reductions. For Q535, check the original 1999 hardness proof directly when available. For Q541, a separate investigation could classify the fixed-color regime or strengthen the reduction type; neither is needed for the present conditional exclusion of a polynomial exact optimizer.
2. **Q536:** seek state compression whose exponent does not depend on the scenario count, or prove approximation hardness for a specified factor. The present exact reduction uses an exponentially fine rational lattice and does not supply constant-factor hardness. The fixed-scenario FPTAS identifies precisely why exact counting hardness leaves room for approximation.
3. **Q540:** remove or replace the positive-support-band restriction while preserving one observation-adapted rule. Separate rules for hidden residue scales cannot simply be combined, because an observed sum does not reveal its residue scale. For exact computation beyond the common binary alphabet, first identify a sufficient state that remains compact when observation changes fail to identify the base.
4. **Q767:** separate the costs of posterior uncertainty and arbitrary remaining-box subsets. The current FPTAS controls both only when scenario count and type count are fixed. The unbounded order gap prevents transferring a fixed-order guarantee to the fully adaptive target without another argument.
5. **Q1496:** a certified enclosure for the already reported finite-n value is a bounded independent objective, but requires validated integration and the actual numerical source artifacts. It would still not determine the infinite-n limit. No V(7) computation was started.
6. **Q2390:** a proof for all matroids must address nonrepresentable matroids or give a different general argument. Source theorems for linear matroids, a fixed-matroid LP, and sample-access prophet models do not by themselves give the retained ordinal 1/e statement. No unverified import has been promoted to a compiled theorem.

## Archive guide

| Location in the archive | Contents |
|---|---|
| `B4_Research_Report_2026-10-07.md` | This complete report, including all proofs and exact retained statements |
| `B4_Statement_Ledger_2026-10-07.json` | Seven-question machine-readable reconciliation, subresults, assumptions and evidence labels |
| `inputs/B4_Handoff_2026-10-07.md` | Original attached handoff, unchanged bytes |
| `q535/` | Timing reduction, verifier, independent boundary audit, complete rational outputs |
| `q536/` | Policy hardness, FPTAS, inputs, policy enumeration and probe certificates |
| `q540/` | Band theorem, binary exact algorithm, posterior certificate, policy CSV, optional exploration and its nonconvergence record |
| `q541/` | Optimal-order reduction, positive-probability variant, subset algorithm and counting controls |
| `q767/` | Posterior search DP, structured FPTAS, adaptivity gap and all fixed-order values |
| `cross_audit.md` and per-question audit notes | Independent written checks and their stated limitations |
| `q1496_q2390_scope.md` | Narrow source checks and explicit access limits for the two unresolved tracks |
| `run_all.py`, `REPRODUCIBILITY.md`, `run_all_results.json` | Reproduction entry point, instructions, captured successful run and artifact hashes |
| `MANIFEST_SHA256.json` | Content hashes for the packaged files, excluding the manifest itself |

No raw floating search result is treated as a proof. No finite test set is used to infer a universal theorem. All changes to the historical question register are proposed in the new ledger, with the original handoff retained separately.
