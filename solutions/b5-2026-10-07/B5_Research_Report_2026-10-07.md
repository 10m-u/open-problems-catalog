# B5 research report: dependency coverage, grouped sampling, and three counterexamples

**Date:** 7 October 2026. **Input:** B5 Walks and Covering — Agent Handoff, 7 October 2026.

## Findings and exact scope

This investigation gives negative answers to three exact retained questions: Q946, Q2298, and Q2397. It also supplies the explicit model correspondence needed by the main research program, sharp lag-design results, sharp grouped-coverage bounds, a four-variable entropy theorem, and a constructive stationary particle law. The two pinned random-environment manuscripts were audited substantially but were not independently verified in full.

The statement ledger records **3 disproved, 2 partial, and 33 unresolved** questions. The central dependency and grouped-sampling theorems have no catalog question numbers in the handoff and are recorded separately. An unresolved status means this investigation has not established a complete answer; it is not a claim that a comprehensive current literature search found no solution. No historical-priority claim is made for any result.

| Target | Conclusion established here | Evidence and limit |
|---|---|---|
| Q946 — 0c62464d2a79195bced5 | The universal repeated-cover bound is false. A lazy directed cycle gives an unbounded ratio of order log n / loglog n. | Complete family proof with exact source counting convention; the displayed numeric table is supplementary. |
| Q2298 — 348fcb55ace5031ea7ed | Collaborating stationary reversible walks need not stochastically dominate one walk with the same total lifespan. | Explicit seven-state rational chain; symbolic enumeration and two separate exact computations. |
| Q2397 — c01e8789e7f81d3f949c | Greedy walk length can depend logarithmically on its start, even on degree-three weighted trees. | Complete construction with unique distances, plus a matching harmonic-order universal upper bound. |
| Inquiry 03/20 | Dependency cover equals the primitive exponent of a Boolean companion matrix. Fixed-size lag layouts have a sharp optimum. | Complete correspondence and design proofs; the classical exponent bound is explicitly sourced. |
| Inquiry 27 | Uniformity exactly characterizes the upper coverage curve. Injective equal-size groups improve expected coverage at equal cost. | Complete probability inequalities and fully specified exact examples. The original toy map was not supplied. |
| Q2396 — adf6fb6ae4ba18aaf563 | Entropy is strictly concave for every four positive weights, and for larger separated-block families. | Exhaustive exact computer-assisted proof with all inputs and verifier outputs. General n remains unresolved. |
| Q2395 — c7b23369c6f031f11c93 | The stationary law has an explicit nonnegative finite-dimensional series with a certified truncation bound. | Complete construction based on known RSK facts. Its underlying representation already appears in the source; intended stronger explicitness is not settled. |
| Q1789 — 8bae191e2b95d4bb0733; Q1790 — dcf3adbfb27d291659db | Pinned candidate theorem statements match the retained models; actual solution source closures were retrieved and audited. | No Lean compilation or kernel check. Neither question is promoted to solved. |

### What changes for the central program

The productive correspondence is to simultaneous reachability in a companion graph. A structural cone records every possible ancestry path. A trajectory records one sequence of choices. These quantities can differ by an unbounded factor in either direction even on the natural companion encoding. This gives both a usable exact model and a precise limit on transferring random-walk or rotor-walk cover estimates.

For M=16 and four permitted lags, the best structural cover time is 20, attained by {1,6,11,16}. The motivating {2,7,15,16} has cover time 26. The first comparison allows lag 1; excluding it is a different design problem. The original Frobenius number 5 remains consistent with time 26 because each initial coordinate has an additional final-edge constraint.

For grouped sampling, the individual target hit probabilities determine expected coverage. Mean image size and within-group injectivity do not determine those probabilities. Nevertheless, injectivity has a useful rigorous consequence under a uniform equal-size partition: at a fixed number of function evaluations, the grouped protocol has at least as much expected coverage as independent uniform inputs through the same fixed map. A balanced-fiber condition then yields the exact uniform curve.

### Evidence labels

The counterexample families and structural/probability identities are justified by written mathematical arguments. Exact finite calculations independently check concrete instances or, in the entropy result, exhaust a provably finite classification and certify every parameter interval. Python integer and rational arithmetic was actually run. Its trusted implementation is not a proof-assistant kernel.

The random-environment audit is source comparison and bounded proof review. An import closure without literal proof placeholders is stronger evidence than a theorem title, but it is not successful elaboration or kernel verification. The original authority files and supplied handoff were not modified. A separate report and ledger are returned for exact-ID reconciliation.

All scripts, computational inputs, certificates, raw outputs, peer reviews, pinned licensed formal source, and a verification runner are in the accompanying archive. The exact retained wording of all 38 questions is reproduced below and in the machine-readable ledger.

## 1. The core program: structural correspondence and grouped coverage

Date: 2026-10-07. These results address the programme's Inquiry 03/20/27 objectives. The handoff assigns no catalog Q number or stable statement ID to these objectives. No assertion of historical novelty is made: the handoff mentions earlier constructive layout work, and the companion-matrix literature contains several corollaries below.

### 1. Dependency covering is a primitive companion-matrix exponent

Fix a nonempty finite set D of positive integers, M=max D≥2, and s=|D|. Let C(t)={t} for 0≤t<M and C(t)=⋃_{d∈D}C(t−d) for t≥M. Write T(D) for the first t with C(t)={0,…,M−1}.

Use the Boolean semiring: addition is OR and multiplication is AND. Define the M×M matrix A=A_D by

\[
 A_{i,i+1}=1\quad(0\le i<M-1),\qquad
 A_{M-1,M-d}=1\quad(d\in D),
\]

with other entries zero. Let e_i denote a singleton row vector.

**Theorem S1.** For every t≥0, the support of e_0 A^t is exactly C(t). Once C(t) is full, every later cone is full. Moreover,

\[
 T(D)<\infty\iff\gcd(D)=1,
 \qquad T(D)=\operatorname{exp}(A_D)
 \quad\text{when }\gcd(D)=1.
\]

Here exp(A) is the least positive integer t for which every entry of A^t is one.

**Proof.** For t<M, e_0 A^t=e_t. At t=M,

\[
 e_0 A^M=\bigvee_{d\in D} e_{M-d}.
\]

Right multiplication by A^{t−M} gives the same recurrence as C(t), so induction proves the support identity. Every column of A has a nonzero entry: column zero receives the lag-M edge, and column j>0 receives the shift edge from j−1. Consequently the full row remains full on multiplication by A. This proves persistence.

Since e_i=e_0 A^i for 0≤i<M, row i of A^t equals e_0 A^{t+i}. If C(t) is full, persistence makes every row of A^t full. Conversely, A^t full implies its row zero is full. Their first positive times are therefore equal.

The directed graph of A is strongly connected because it contains the cycle 0→1→⋯→M−1→0. Every elementary directed cycle uses the last vertex and has length d for some d∈D; all these cycles occur. Thus its period is gcd(D). A finite strongly connected digraph is primitive exactly when this period is one. Alternatively, when gcd(D)>1, every ancestor r obeys r≡t modulo gcd(D), which prevents coverage; when gcd(D)=1, the supplied Apéry formula proves eventual coverage. ∎

The degenerate case D={1}, M=1 has T=0 and should be handled separately from the convention that a matrix exponent is positive.

The standard companion matrix is exactly the class studied by Nej and Reddy, *A Note on the Exponents of Primitive Companion Matrices*, arXiv:1903.09963v1, pp. 1–2. Their Theorem 3.2 and the classical Wielandt bound give the following sharp comparison after the proved correspondence:

\[
 \boxed{M\le T(D)\le(M-1)^2+1.}
\]

The lower bound is attained by D={1,…,M}; the upper bound by D={M−1,M}. These are bounds on the exact dependency-covering object, not on a different random walk. Source: https://arxiv.org/pdf/1903.09963 , Theorems 3.2–3.3, PDF pp. 6–7.

### 2. Consequences for the supplied Apéry formula

Let S=⟨D⟩, gcd(D)=1, and w_j=min{u∈S:u≡j mod M}. With the handoff's notation

\[
 E_x(\rho)=\min_{d\in D,\ d\ge x}
 [M-x+d+w_{(\rho-(M-x+d))\bmod M}],
\]

the established minimax expression admits a second form:

\[
 \boxed{T(D)=1-M+\max_{x,\rho}E_x(\rho).}
\]

**Proof.** In residue ρ, the last time at or above M missing the initial coordinate M−x is E_x(ρ)−M, if this lies at or above M. At smaller times there are always missing coordinates because M≥2. The maximum of E_x(ρ)−M is at least M−1: for r=0 the lag-M translate alone applies, and its last missing time is M+F(S)≥M−1, with F(ℕ_0)=−1. Persistence from Theorem S1 now makes T exactly one plus the largest missing time. ∎

Let d_0=0<d_1<⋯<d_s=M and G=max_i(d_i−d_{i−1}). Then

\[
 \boxed{M+F(S)+1\le T(D)\le M+F(S)+G.}
\]

For the lower bound, coordinate zero cannot be reached at time M+F(S); when F=−1 this reduces to T≥M. For the upper bound, at any initial coordinate r=M−x choose the least d∈D with d≥x. Then 0≤d−x≤G−1. If t≥M+F+G, the residual t−(M−x+d) is at least F+1 and hence belongs to S. The required final edge reaches r, so every initial coordinate is reached.

The Frobenius number alone therefore bounds but does not specify T. For D={2,7,15,16}, S=⟨2,7⟩, F=5, G=8; these inequalities give 22≤T≤29. The exact formula gives T=26. At time 25 the only missing coordinate is 13: the permitted final lags 7,15,16 leave residuals 5,−3,−4, none in S.

### 3. Two exact design theorems

**Theorem S2 (two lags).** If 1≤a<M and gcd(a,M)=1, then

\[
 \boxed{T(\{a,M\})=M+a(M-2).}
\]

**Proof.** For 0≤r<M−a, only the lag M can be the final edge into r, so r∈C(t) iff t−r−M∈⟨a,M⟩, for t≥M. For M−a≤r<M, both final lags are allowed, and (a+S)∪(M+S)=S\{0}; since t>r, reachability is equivalent to t−r∈S. These two blocks of conditions require precisely the M consecutive integers

\[
 [t-2M+a+1,\ t-M+a]\subseteq S.
\]

Because M∈S, an interval of M consecutive members propagates to all larger integers. Such an interval begins at or beyond F(S)+1, and every interval beginning there is contained in S. The Apéry representatives of ⟨a,M⟩ are ja for 0≤j<M, in their respective residues, so F(S)=aM−a−M. Solving for t gives M+a(M−2). This includes a=1 with F=−1. ∎

**Theorem S3 (optimal fixed-cardinality layout).** For every M≥2 and 2≤s≤M,

\[
 \boxed{\min_{\substack{D\subseteq\{1,\ldots,M\}\\M\in D,\ |D|=s}}T(D)
 =M-1+\left\lceil\frac{M-1}{s-1}\right\rceil.}
\]

**Proof of the lower bound.** At time M−1 the support is a singleton. Every row of A except the last has one outgoing edge, and the last has s. Thus a support can grow by at most s−1 per multiplication, even when all images are distinct. If k=T−(M−1), then M≤1+k(s−1), giving the bound.

**Construction and upper bound.** Take

\[
 d_j=1+\left\lfloor\frac{j(M-1)}{s-1}\right\rfloor,
 \qquad 0\le j\le s-1.
\]

These are s distinct lags including 1 and M. More generally, whenever 1∈D, the last vertex has a loop, so a path can wait there before taking its final exit. Starting at M−1, the first time every vertex is reachable at the same length is the maximum directed distance from M−1 to a vertex. Those distances equal one plus the number of subsequent shift edges after the nearest permitted landing point. Their maximum is G, the maximum consecutive lag gap, including the initial gap from zero. Hence T=M−1+G. In the displayed construction, G=ceil((M−1)/(s−1)), completing the proof. ∎

For M=16,s=4, the optimum is 20, attained by {1,6,11,16}. The motivating set {2,7,15,16} takes 26. This comparison permits lag 1; a design problem forbidding that lag has different constraints.

### 4. Exact finite-state encoding and limits of rotor-cover comparisons

For a finite alphabet A and a fixed update Φ, the window map is

\[
 (x_0,\ldots,x_{M-1})\mapsto
 (x_1,\ldots,x_{M-1},\Phi(x_{M-d}:d\in D)).
\]

This is a subgraph of the de Bruijn shift graph, with exactly one selected outgoing edge from every state. It does not automatically satisfy irreducibility or uniform rotor initialization. Treating it as a rotor graph with one outgoing edge per state yields only a deterministic functional graph.

For a fully specified example, take A=F_2, D={1,3}, and Φ(x_2,x_0)=x_2⊕x_0. The eight window states split into one fixed point 000 and one cycle of length seven. The structural cover is T=4. The actual output a_4=a_0⊕a_1⊕a_2 uses all three inputs, but a_5=a_0⊕a_1 loses the a_2 coefficient through cancellation while C(5) remains full. The complete cycles and coefficients are in the exact computation output.

There is a different legitimate walk on the M-vertex companion graph: shift deterministically from i to i+1 for i<M−1, and at the last vertex choose lag d with positive probability p_d, jumping to M−d. Its stationary distribution is

\[
 \pi_j=\frac{\sum_{d\ge M-j}p_d}{\sum_d d p_d},\qquad 0\le j<M.
\]

**Proof.** Successive returns to the last vertex are regenerative cycles. A cycle of selected length d visits each vertex in {M−d,…,M−1} once, and has length d. The expected visit reward divided by expected cycle length gives the formula. Direct substitution in πP=π gives the same identity. In particular π_min=p_M/(∑d p_d).

For this genuine Markov chain, T(D) is the first common time at which its transition probabilities from vertex zero are all positive. It is not its trajectory cover time. Two explicit separations rule out constant-factor comparison in either direction, even without changing this graph construction.

1. For D={M−1,M} with equal exit probabilities, T=(M−1)^2+1. Starting at M−1, the expected trajectory cover time is (3M−2)/2. Indeed, the number F of failed lag-(M−1) cycles before the first lag-M choice has P(F=f)=2^{−f−1}. If F=0, covering takes M−1 steps; if F≥1 it takes F(M−1)+1, because the failed cycle already covered vertices 1,…,M−1. Summing gives the displayed expectation. A rotor alternating the two exits covers in either M−1 or M steps, depending on its initial phase. Thus T divided by either walk-cover quantity is unbounded.
2. For D={1,…,M}, T=M. A rotor trying exits in lag order 1,2,…,M requires Σ_{d=1}^{M−1}d+1=M(M−1)/2+1 steps to cover from M−1. With uniform random exit choices, the failed cycles before the first lag M already have expected total length Σ_{d<M}p_d d/p_M=M(M−1)/2. Therefore the expected random cover time divided by T also diverges. These examples refute universal comparisons for this particular natural encoding; they do not prove that no useful alternative encoding exists.

Holroyd and Propp's *Rotor Walks and Markov Chains* (arXiv:0904.4507v3), Theorems 1–4, give genuine rotor-versus-Markov comparisons for hitting and occupation statistics under a specified rotor mechanism. The companion support statistic is different; the displayed separations explain why those bounds cannot simply be renamed dependency-cover bounds. Source: https://arxiv.org/pdf/0904.4507 .

### 5. Grouped coverage: exact law and sharp uniformity criterion

Let Y be a finite target set of size N, and let A_1,A_2,… be iid random subsets of Y, obtained as the distinct images of independently reset input groups under one fixed map. Put q_y=P(y∈A_1), μ=E|A_1|=Σ_y q_y, and

\[
 C_K=\frac1N\mathbb E\left|\bigcup_{j=1}^K A_j\right|.
\]

For every integer K≥1,

\[
 C_K=1-\frac1N\sum_y(1-q_y)^K.
\]

This formula is already present in the handoff; its proof is independence of the K miss events for each fixed target and linearity of expectation.

**Theorem G1 (sharp bounds for a fixed mean image size).** Write μ=m+θ with integer m=floor μ and 0≤θ<1. Then

\[
 \boxed{\frac{m+1-(1-\theta)^K}{N}
 \le C_K\le 1-(1-\mu/N)^K.}
\]

For K≥2, equality in the upper bound holds exactly when all q_y are equal. Both bounds are attainable by random-set laws.

**Proof.** The function f(q)=1−(1−q)^K is concave on [0,1], strictly concave for K≥2. Jensen gives the upper bound and equality condition. To minimize Σ f(q_y) under 0≤q_y≤1 and Σq_y=μ, move mass between two nonintegral coordinates until one reaches zero or one; concavity ensures one endpoint choice does not increase the sum. Repeating leaves m ones, one θ, and zeros. This vector is realized by always including m fixed targets and independently including one additional target with probability θ. The uniform vector is realized, for example, by including each target independently with probability μ/N. ∎

For integer μ=b, even an injective b-element image group can have C_K=b/N for all K, by always choosing the same image set. Conversely an invariant group law under a transitive output symmetry forces q_y constant and attains the upper curve. Within-group injectivity alone does not supply that symmetry.

**Variance diagnostic.** Let v=N^{-1}Σ_y(q_y−μ/N)^2. At K=1 the loss from the uniform upper curve is zero. At K=2 it is exactly v. More generally, for K≥2, Taylor's theorem yields

\[
 0\le \big[1-(1-\mu/N)^K\big]-C_K
 \le\frac{K(K-1)}2(1-q_{\min})^{K-2}v.
\]

Thus a quantitative near-uniformity estimate, rather than merely mean efficiency, justifies a quantitative approximation.

### 6. Equal evaluation cost: a useful positive comparison

**Theorem G2.** Suppose a finite input domain is partitioned into G equal groups of size b. Each group is selected uniformly and independently, the same fixed map F is retained, and F is injective on every group. Let p_y be the image probability of one uniformly sampled input. Then

\[
 q_y=b p_y,
\]

and for every K≥1, expected target coverage after K groups is at least coverage after bK independent uniformly sampled inputs through the same map.

**Proof.** Let m_y=|F^{-1}(y)|. Injectivity means its m_y preimages occupy m_y distinct groups, so q_y=m_y/G and p_y=m_y/(Gb). Bernoulli's inequality gives (1−p_y)^b≥1−bp_y=1−q_y. Raising to K and comparing miss probabilities proves the claim target by target. ∎

Balanced fibers are a sufficient extra condition for a single exact curve: if all m_y=Gb/N, then q_y=b/N and C_K=1−(1−b/N)^K. The comparison is about expectation and does not assert stochastic dominance of the total coverage random variable, a distinction made concrete by Q2298.

#### Fully specified 16-input examples

The domain is {(g,h):0≤g,h≤3}; a group consists of the four inputs with one fixed g. Choose g uniformly afresh at each reset and evaluate all four inputs. Targets are {0,…,7}. Each table row gives F(g,0),…,F(g,3).

| g | Balanced map | Unbalanced map |
|---|---|---|
| 0 | 0,1,2,3 | 0,1,2,3 |
| 1 | 4,5,6,7 | 0,1,2,3 |
| 2 | 0,1,2,3 | 0,1,4,5 |
| 3 | 4,5,6,7 | 0,1,6,7 |

Both maps are surjective and injective on each group, and both have exactly four distinct outputs per group. The balanced map has q_y=1/2 for all y. The unbalanced map has hit vector (1,1,1/2,1/2,1/4,1/4,1/4,1/4). Therefore

\[
 C_K^{\rm bal}=1-2^{-K},\qquad
 C_K^{\rm unbal}=1-\frac14 2^{-K}-\frac12(3/4)^K.
\]

At K=2 the values are 3/4 and 21/32; at K=4 they are 15/16 and 423/512. Their identical one-round injectivity and mean image size do not determine their later curves. The provided script also computes the appropriate iid-input benchmarks separately for each fixed map at exactly 4K evaluations.

### 7. Verification record and residual scope

`dependency_cover.py` exhaustively checks all 4,094 lag sets with 2≤M≤12: 4,015 primitive sets and 79 imprimitive sets. It compares the direct recurrence, Boolean matrix powers, and the Apéry formula; checks persistence, the second Apéry expression, Frobenius bounds, all two-lag formulas, and the optimal fixed-cardinality constructions. Four separate M=16 examples are also recorded. All assertions passed. These checks are bounded evidence for the implementations; the universal conclusions rest on the preceding proofs.

`grouped_coverage.py` uses exact rational arithmetic for both maps, calculates curves through K=8, and independently enumerates every group sequence through K=6. It checks the equal-cost comparison and the exact K=2 variance identity. All assertions passed. No random seed is used because both experiments are exhaustive.

The unknown Inquiry 27 toy-compression map and its prior datasets were not supplied. These results apply to the fully specified maps and general hypotheses above; they do not certify the unprovided original experiment's per-target probabilities or diffusion behavior.

## 2. Q946 is false: a lazy directed cycle

**Programme:** B5. **Question:** Q946. **Stable statement ID:** 0c62464d2a79195bced5.

**Exact retained statement.** For every finite irreducible Markov chain and k≥1, let t_cov^(k) be the worst-start expected time to visit every state k times, t_cov=t_cov^(1), and π*=min_iπ_i. Does t_cov^(k)≤C(t_cov+k/π*) hold with a universal C? Reversible chains are settled; the general bound loses log n. Periodic chains are included.


**Retained statement ID:** `0c62464d2a79195bced5`.
**Question status:** DISPROVED. **Evidence:** `Written proof of the negation — explicit counterexample family with matching first-order asymptotics`.
**Scope:** Finite irreducible Markov chains, with the paper's exact counting convention N_i(t)=Σ_{s=1}^t 1{X_s=i}. The counterexamples are aperiodic, are 1/2-lazy (their holding probabilities exceed 1/2), and have uniform stationary distribution. No altered assumptions are required. Counting X₀ instead changes all worst-start expectations here by exactly one and leaves the conclusion unchanged.

### Primary-source check

Chan, Ding and Li, *Learning and Testing Irreducible Markov Chains via the k-Cover Time*, ALT 2021, [PDF](https://proceedings.mlr.press/v132/chan21a/chan21a.pdf): Section 2.2, PDF p. 5, defines counts along X₁,…,X_t; Definition 4, PDF p. 6, defines k-cover time; Section 5, PDF p. 17, states the conjectured universal order t_cov^(k)=Θ(t_cov+k/π_min). Theorem 22, PDF p. 18, proves a bound with a logarithmic loss.

### Family and result

For each integer m≥3, let n=m^m and take the state space Z/nZ. Define

\[
P(i,i)=1-\frac1m,\qquad
P(i,i+1\bmod n)=\frac1m.
\]

The chain moves only clockwise, waiting a geometric number of steps at each vertex. It is irreducible, aperiodic, and doubly stochastic. Thus π_i=1/n and π_min=1/n. Its transition kernel is nonreversible for n≥3, because P(i,i+1)>0 but P(i+1,i)=0. Set the repeated-coverage demand to k=m.

For this family,

\[
\boxed{t_{\rm cov}^{(m)}=(1+o(1))nm^2},
\qquad
\boxed{t_{\rm cov}=1+(n-1)m},
\]

and therefore

\[
\boxed{
\frac{t_{\rm cov}^{(m)}}{t_{\rm cov}+m/\pi_{\min}}
\sim \frac m2
\sim \frac{\log n}{2\log\log n}.
}
\]

In particular there is no universal constant C satisfying the retained inequality.

### Exact ordinary cover time

First use the inclusive convention that counts X₀. Starting from any vertex, the chain covers the cycle when it makes its (n−1)-st clockwise move. The waits between these moves are independent Geom(1/m) random variables on {1,2,…}, each of mean m. Hence the inclusive expected ordinary cover time is (n−1)m.

For the paper's convention, the observed sequence starts at X₁. Cyclic translation makes the expected inclusive cover time from X₁ the same deterministic value for every possible X₁. Adding the time index shift gives

\[
t_{\rm cov}=1+(n-1)m.
\]

The same shift identity holds for m-cover expectations.

### Independent geometric residence blocks

Start at state 0. For i∈Z/nZ and j≥1, let G_{i,j} be the number of visits during the j-th consecutive residence at i, from the arrival at i up to and including the last time before departing i. The collection (G_{i,j}) is independent, with

\[
\Pr(G_{i,j}=a)=\left(1-\frac1m\right)^{a-1}\frac1m,
\quad a\ge1,\qquad
\mathbb EG_{i,j}=m,\quad
\operatorname{Var}(G_{i,j})=m(m-1).
\]

Let S_r be the time of the r-th completed clockwise circuit, so

\[
S_r=\sum_{i=0}^{n-1}\sum_{j=1}^{r}G_{i,j}.
\]

Under the paper's convention, at the circuit endpoint the local counts satisfy the exact identity

\[
N_i(S_r)=\sum_{j=1}^{r}G_{i,j}\quad\text{for every }i.
\]

For i≠0, all the counted visits lie in the completed residence blocks. For i=0, omitting the initial X₀ and including the terminal X_{S_r}=0 cancel. This is the only endpoint correction needed.

### A deficient state after m−1 complete circuits

Put r=m−1 and B=S_{m−1}. For every state i, consider the event

\[
A_i=\{G_{i,1}=G_{i,2}=\cdots=G_{i,m-1}=1\}.
\]

These events are independent across i and have probability

\[
\Pr(A_i)=m^{-(m-1)}.
\]

On A_i, the exact count at time B is N_i(B)=m−1, so the chain has not m-covered the state space. Since n=m^m,

\[
\Pr\left(\bigcup_i A_i\right)
=1-\left(1-m^{-(m-1)}\right)^{m^m}
\ge 1-e^{-m}.
\]

Consequently, the random m-cover time T_m obeys T_m>B with probability at least 1−e^(−m).

The circuit duration has mean and variance

\[
\mathbb EB=n m(m-1),\qquad
\operatorname{Var}(B)=n m(m-1)^2.
\]

Chebyshev's inequality at relative deviation 1/m gives

\[
\Pr\left(B<\left(1-\frac1m\right)\mathbb EB\right)
\le \frac{m}{n}.
\]

No independence between this concentration event and the deficient-state event is needed: the union bound gives

\[
\Pr\bigl(T_m>n(m-1)^2\bigr)
\ge 1-e^{-m}-\frac mn.
\]

Therefore

\[
\boxed{
\mathbb ET_m\ge
n(m-1)^2\left(1-e^{-m}-\frac mn\right).
}
\]

All starts give the same expectation by cyclic symmetry, so this is a bound on the worst-start m-cover time.

### Matching upper bound

Every residence block contains at least one visit. After m complete circuits all states therefore have at least m visits. Thus T_m≤S_m pathwise and

\[
\boxed{\mathbb ET_m\le\mathbb ES_m=nm^2.}
\]

The lower and upper bounds combine to yield

\[
\left(1-\frac1m\right)^2
\left(1-e^{-m}-m^{1-m}\right)
\le \frac{t_{\rm cov}^{(m)}}{nm^2}\le1,
\]

and both endpoints converge to one. Since

\[
t_{\rm cov}+m/\pi_{\min}=(2n-1)m+1,
\]

the displayed ratio asymptotic follows.

Finally, log n=m log m, so m∼log n/log log n. This establishes a necessary loss of order at least log n/log log n relative to the proposed sum, while the cited paper's general upper bound loses log n. The exact optimal dependence on n after this disproof is a separate open optimization problem; no universal matching upper bound is claimed here.

### Counting conventions and structural restrictions

The paper counts visits at every discrete time, including self-loop steps. The argument uses precisely that convention. If 'visit' were redefined to count only arrivals after moving, it would be a different problem. Under the ordinary inclusive-time-zero convention, the m-cover time differs here by exactly one, as explained above. The same unbounded ratio therefore holds under either standard convention.

The example has uniform stationary measure, an explicit normal circulant transition matrix, holding probability at least 2/3 at every state, and a deterministic clockwise embedded jump chain. Periodicity, nonuniform stationary measures, and complicated state-space geometry are unnecessary for the failure.

### Reproducibility

`q946_bound_table.py` evaluates the rigorous lower and upper bounds and their normalized ratios for several m without simulating an exponentially large chain. `q946_bounds.csv` records these arithmetic evaluations. The mathematical proof above establishes the family; the numeric table is explanatory only.

## 3. Q2298 is false: a seven-state lazy birth–death counterexample

**Programme:** B5. **Question:** Q2298. **Stable statement ID:** 348fcb55ace5031ea7ed.

**Exact retained statement.** For every k≥2, positive integer lifespans t_i, and y>0, is P(|⋃_{i=1}^kR_i(t_i)|≥y)≥P(|R(Σ_it_i)|≥y)?

**Supplied setup.** Let X,X₁,…,X_k be independent copies of the same finite irreducible aperiodic reversible discrete-time Markov chain, all starting independently in its stationary law π. Put R_i(t)={X_i(s):0≤s≤t} and R(t)={X(s):0≤s≤t}.


**Retained statement ID:** `348fcb55ace5031ea7ed`.
**Question status:** DISPROVED. **Evidence:** `Written proof of the negation — exact counterexample, with symbolic path enumeration and independent rational-DP certificate`.
**Scope:** Exactly the finite irreducible aperiodic reversible, independently stationary-started discrete-time chain in the supplied handoff. No alteration of the assumptions is needed. Visits at time 0 count. The counterexample is also 1/2-lazy and has even total lifespan.

### Primary-source scope check

Dey, Kim and Terlov, *Collaboration of Random Walks on Graphs*, arXiv:2302.14241, [PDF](https://arxiv.org/pdf/2302.14241), Section 1.2, Assumption I (PDF pp. 2–3), allows any finite time-homogeneous, reversible, irreducible, aperiodic chain. The source discusses weighted networks in Section 1.1. Its additional lazy/even-time hypotheses used for the expectation theorem are both satisfied here. Question 3.6 is on PDF p. 11.

The handoff uses the upper-tail event |R|≥y. The PDF's strict-tail presentation can equivalently use y=6.5 below.

### Chain and stationary law

Let r>0, q=r/(r+1), p=1/(r+1), and set a=1/2. The state space is V={0,1,2,3,4,5,6}. At every vertex the chain stays put with probability 1/2. The remaining transitions are

- P(0,1)=P(6,5)=1/2;
- P(i,i+1)=q/2 and P(i,i−1)=p/2 for 1≤i≤5.

Write S=1+r+r²+r³+r⁴+r⁵. Its stationary probabilities are

\[
\pi_0=\frac1{2S},\qquad
\pi_j=\frac{(r+1)r^{j-1}}{2S}\quad(1\le j\le5),\qquad
\pi_6=\frac{r^5}{2S}.
\]

They sum to one. The edge balance equations π_i P(i,i+1)=π_{i+1}P(i+1,i) hold directly, proving stationarity and reversibility. Both directions of each edge have positive probability, so the chain is irreducible. All diagonal entries are positive, so it is aperiodic.

Take two independent stationary copies X₁,X₂, each run for three steps, and a single stationary copy X run for six steps. Put

\[
C=\Pr\bigl(R_1(3)\cup R_2(3)=V\bigr),\qquad
F=\Pr\bigl(R(6)=V\bigr).
\]

### Exact single-walk probability

To visit all seven vertices in six steps a path must be exactly 0,1,…,6 or its reversal. Reversibility makes their stationary probabilities equal. Therefore

\[
F=2\pi_0 a^6 q^5.
\]

### Exact two-walk probability

Every three-step range is an interval with at most four vertices. Let

\[
A_2=\Pr(R(3)=[0,2]),\quad A_3=\Pr(R(3)=[0,3]),
\quad B_3=\Pr(R(3)=[3,6]),\quad B_4=\Pr(R(3)=[4,6]).
\]

For two such intervals to cover all seven vertices, one must contain 0 and the other 6. The only possible unordered pairs are

\[
([0,2],[3,6]),\qquad([0,3],[3,6]),\qquad([0,3],[4,6]).
\]

The walkers can be assigned to each pair in two ways. Thus independence gives

\[
C=2(A_2B_3+A_3B_3+A_3B_4).
\]

The four interval probabilities are

\[
\begin{aligned}
A_2&=2\pi_0 a^3 q(4+p),&
A_3&=2\pi_0 a^3 q^2,\\
B_3&=2\pi_3 a^3 q^3,&
B_4&=2\pi_4 a^3 q^2(4+q).
\end{aligned}
\]

For completeness, the three-edge intervals A₃ and B₃ require monotone traversal and its time reversal. For A₂, the two-edge monotone traversal has one holding step, giving six paths and total mass 6π₀a³q; the four paths with three actual moves form two reversal pairs, of masses 2π₀a³qp and 2π₀a³q. Their sum is A₂ above. At the right endpoint, the same enumeration gives the holding contribution 6π₄a³q² and backtracking contributions 2π₄a³q² and 2π₄a³q³, giving B₄. These alternatives are mutually exclusive and exhaust the three-step paths with the specified ranges.

Dividing C by F and using p+q=1 gives

\[
\begin{aligned}
\frac CF
&=4\left(\frac{\pi_3(4+p)}q+\pi_3+\frac{\pi_4(4+q)}q\right)\\
&=\frac4q\left(5\pi_3+(4+q)\pi_4\right)\\
&=\boxed{\frac{2r(5r^2+9r+5)}{r^4+r^2+1}}.
\end{aligned}
\]

Here S=(r+1)(r⁴+r²+1) was used in the last step.

### Concrete rational counterexample

Set r=20. Then the internal transition probabilities are 1/42 to the left, 1/2 to stay, and 10/21 to the right. The endpoint holding and inward probabilities are both 1/2. The stationary vector can be written

\[
\pi=\frac{(1,21,420,8400,168000,3360000,3200000)}{6736842}.
\]

The exact probabilities are

\[
F=\frac{50000}{13756971574521},\qquad
C=\frac{4370000000}{2206631997524742921},
\]

with

\[
\frac CF=\frac{87400}{160401}<1,
\qquad
F-C=\frac{3650050000}{2206631997524742921}>0.
\]

Thus

\[
\Pr\bigl(|R_1(3)\cup R_2(3)|\ge7\bigr)
<
\Pr\bigl(|R(6)|\ge7\bigr),
\]

which disproves the retained universal stochastic dominance statement.

### Stronger implication

The ratio above is asymptotic to 10/r as r→∞. Therefore the failure can be arbitrarily large multiplicatively, while keeping seven states, half-laziness, two walkers, and lifespans three fixed. There is no positive universal c such that the collaborating upper tail always exceeds c times the single-walk upper tail, even within this fixed seven-state class.

This does not contradict the expected-range comparison proved in the cited paper. The exact certificate computes expected range sizes 1822242897175847/880446180769344 for the single walk and 1352275726180174855/640473686356387968 for the collaborating pair; the latter is larger. Stochastic dominance is strictly stronger than this first-moment inequality.

### Reproducibility

`collaboration_counterexample.py` uses only Python's standard library. It propagates the exact joint law of (visited-set bitmask,current state), using `fractions.Fraction`, starting from the exact stationary law and counting the initial state. It computes the independent union law by a product of two exact three-step range laws. Assertions verify probability normalization, detailed balance, the four closed-form interval probabilities, the exhaustive interval-pair formula, the single-walk formula, and the strict inequality. `collaboration_counterexample.json` records the full matrix, stationary law, exact probabilities, and expectations. This is finite exact arithmetic and a certificate for the displayed chain, not a simulation.

## 4. Q2397 is false: logarithmic dependence on the greedy walk's start

**Programme:** B5. **Question:** Q2397. **Stable statement ID:** c01e8789e7f81d3f949c.

**Exact retained statement.** Is sup_G max_v L(G,v)/min_v L(G,v)<∞, over all such graphs with at least two vertices?

**Supplied setup.** For a finite connected positively weighted graph, use shortest-path distance d. Assume unique choices. Starting at v, repeatedly go to the nearest unvisited vertex; L(G,v) is total distance until all vertices are visited, without returning. Random models below start uniformly over vertices.


**Retained statement ID:** `c01e8789e7f81d3f949c`.
**Question status:** DISPROVED. **Evidence:** `Written proof of the negation — explicit weighted-tree counterexample family`.
**Scope:** Finite connected undirected graphs with positive edge lengths. Each nearest-unvisited choice is unique, every shortest path is unique, and after the explicit perturbation even all distances between distinct unordered vertex pairs are different. Length is measured until all vertices have been visited, without returning to the start.

### Primary sources and construction provenance

Aldous, *The Nearest Unvisited Vertex Walk on Random Graphs*, [arXiv:1912.13175 PDF](https://arxiv.org/pdf/1912.13175), Section 1 defines the model and no-return convention; Section 2.4, Open Problem 4 asks whether the ratio between the largest and smallest starting-vertex lengths is universally bounded.

The construction below modifies the recursive spiked-path trees in Robin Fritsch, *Online Graph Exploration on Trees, Unicyclic Graphs and Cactus Graphs*, [arXiv:2004.06690 PDF](https://arxiv.org/pdf/2004.06690), Section 2, Lemma 2.1 and Theorem 2.2. That paper compares a bad nearest-neighbor tour with the offline optimum. The present proof uses two starts of the same graph and different spike weights, with explicit perturbations enforcing uniqueness. This additional comparison is proved here, rather than inferred from an approximation ratio against the optimum.

### The unperturbed family

Put b=3/4 and c=5/4. Let G₁ be the path with vertices l₁,r₁,m₁, where l₁r₁ has length 1 and r₁m₁ has length b. Regard l₁r₁ as the backbone and r₁m₁ as a spike.

For h≥2, take left and right copies G′_{h−1},G″_{h−1}. Join r′_{h−1} to l″_{h−1} by an edge of length h. Add one new leaf m_h joined to l″_{h−1} by a spike of length c. Set l_h=l′_{h−1} and r_h=r″_{h−1}.

An equivalent nonrecursive description is especially simple. Use backbone vertices i=0,…,2^h−1. Give edge (i−1,i) length 1+ν₂(i), where ν₂(i) is the exponent of 2 dividing i. Attach one leaf at each i≥1: its edge has length 3/4 when i is odd and 5/4 when i is even. The bad start is backbone vertex 0, and the good start is the leaf attached to vertex 2^h−1.

This is a tree consisting of a weighted backbone path with single leaves attached to it. It has

\[
n_h=2^{h+1}-1
\]

vertices. Write p_h=d(l_h,r_h). The recursion p₁=1, p_h=2p_{h−1}+h gives

\[
p_h=2^{h+1}-h-2.
\]

Write q_h=d(m_h,r_h). Then q₁=b, while q_h=c+p_{h−1} for h≥2. In every case,

\[
d(m_h,l_h)=q_h+h.
\tag{1}
\]

The two lengths compared below are

\[
\boxed{B_h=(h+1)2^h-\frac{11}{4}\quad(h\ge2)},
\qquad
\boxed{H_h=2^{h+2}-h-\frac{21}{4}}.
\]

Here B_h is the greedy length from l_h and H_h is the greedy length from the rightmost base spike leaf. Hence B_h/H_h∼h/4.

### Strict greedy traversal from the bad start

The following induction establishes the complete nearest-unvisited order, including the inequalities needed to avoid ties.

Consider a copy of G_j embedded in a larger tree of the constructed family. Edges leaving that copy occur only at l_j and r_j. Every edge leaving at l_j has length at least c, and every edge leaving at r_j has length at least j+1. These statements follow directly from the recursive construction. At the moment the copy is entered at l_j, all its other vertices are unvisited. Any unvisited vertex outside the copy must be reached through one of those boundary edges; some exterior vertices may already have been visited, which only makes the stated lower bounds stronger.

The claim is that the greedy walk visits all vertices of the copy before an exterior unvisited vertex, finishes at m_j, and uses the recursively described order.

For j=1, the walk chooses the backbone edge of length 1 over any exterior edge at l₁, whose length is at least c>1. At r₁ it chooses the spike of length b<1, strictly shorter than any route to an exterior unvisited vertex. This proves the base case, with length B₁=1+b=7/4.

For j=h≥2, the two subcopies satisfy the same boundary assumptions. The induction hypothesis first explores the left copy and finishes at m′_{h−1}. By (1), its distance to the next vertex l″_{h−1} is q_{h−1}+h. Any unvisited exterior vertex reached through l_h is at distance at least

\[
q_{h-1}+(h-1)+c
=(q_{h-1}+h)+(c-1).
\]

The latter is longer by c−1=1/4. Any unvisited vertex on the right is reached through l″_{h−1}, so that vertex is strictly nearest. The new spike m_h is also farther than l″_{h−1}, because the latter is on its path.

The walk then recursively explores the right copy and finishes at m″_{h−1}. Its distance to the remaining spike m_h is

\[
q_{h-1}+(h-1)+c.
\]

Any exterior unvisited vertex reached through r_h is at distance at least q_{h−1}+h+1, which exceeds this by 2−c=3/4. Any reached through l_h requires, in addition to reaching l″_{h−1}, crossing the bridge and the entire left backbone, and is strictly farther. Thus m_h is the unique next unvisited vertex, completing the induction.

All comparisons have a margin of at least 1/4; after selecting a nearest boundary vertex, every vertex farther along its route is separated by at least the shortest edge length b=3/4.

The resulting length satisfies

\[
B_h=2B_{h-1}+2q_{h-1}+2h-1+c.
\]

At h=2 this gives B₂=37/4. For h≥3, substituting q_{h−1}=c+p_{h−2} and p_{h−2}=2^{h−1}−h gives

\[
B_h=2B_{h-1}+2^h+\frac{11}{4}.
\]

Solving with B₂=37/4 gives B_h=(h+1)2^h−11/4.

### Strict greedy traversal from the good start

Let z_h be the leaf of the rightmost base spike, the copy of m₁ at the right end. Starting at z_h, the walk goes to r_h and sweeps the backbone monotonically from right to left, visiting each spike immediately when its attachment vertex is reached.

At a base spike attachment, the spike length is b=3/4 and the next backbone edge to the left has length 1, so the spike is strictly closer. At every other spike attachment, the spike has length c=5/4 and the backbone edge to the left is a recursive bridge of length at least 2, so again the spike is strictly closer. All vertices farther left can only be reached through that next backbone vertex, and everything to the right has already been visited. This proves the greedy rule at every step, with a margin at least 1/4.

There are 2^{h−1} base spikes of length b and 2^{h−1}−1 other spikes of length c. Their total length is

\[
S_h=2^{h-1}b+(2^{h-1}-1)c=2^h-c.
\]

The backbone is traversed once. Every spike is traversed twice except the initial one, which is traversed once. Thus

\[
H_h=p_h+2S_h-b=2^{h+2}-h-\frac{21}{4}.
\]

This is a length until coverage, not a return tour.

### Explicit perturbation giving distinct distances

The two displayed greedy walks already have unique choices, and the graph is a tree, so shortest paths are unique. To satisfy the stronger assumption that all pairwise distances are different, enumerate the E=n_h−1 edges as e₀,…,e_{E−1} and replace each length by

\[
\ell'(e_j)=\ell(e_j)+2^{-(j+10)}.
\]

The total increase over all edges is less than 1/512. Therefore each path length changes by less than 1/512, and every strict greedy comparison with original margin at least 1/4 is preserved. The two vertex orders proved above remain exactly the greedy orders after perturbation.

Every original path length is an integer multiple of 1/4. Paths with different original lengths cannot become equal under these small changes. If two paths had equal original length, their edge sets are distinct because they have different unordered endpoint pairs in a tree. The finite sums of distinct powers 2^{−(j+10)} over different edge sets are distinct, so the perturbed distances are unequal. Thus all distances between different unordered pairs are different.

The bad greedy length can only increase. The good walk traverses every edge at most twice, so its length increases by less than 1/256. Consequently the perturbed tree G′_h satisfies

\[
\frac{\max_v L_{\rm NUV}(G'_h,v)}{\min_v L_{\rm NUV}(G'_h,v)}
\ge
\frac{(h+1)2^h-11/4}{2^{h+2}-h-21/4+1/256}
\sim\frac h4\longrightarrow\infty.
\]

This disproves the retained universal boundedness statement.

### Quantitative scale

Since h=log₂(n_h+1)−1, the example forces a loss of order log n. A direct argument gives the matching general upper bound

\[
\frac{\max_v L_{\rm NUV}(G,v)}{\min_v L_{\rm NUV}(G,v)}\le H_{n-1},\qquad H_{n-1}=\sum_{j=1}^{n-1}\frac1j.
\]

To prove it, fix any nearest-unvisited walk and sort its n−1 step lengths as a₁≥a₂≥⋯≥a_{n−1}. The starting vertices of its k longest steps, together with its final vertex, are k+1 points at pairwise distance at least a_k: at the earlier of any two chosen starting vertices, the later one and the final vertex were still unvisited, so the nearest-unvisited step was no longer than the distance to either. Any walk covering the graph must visit these k+1 points and therefore has length at least k a_k, by ordering their first visits and adding the distances between consecutive selected points. In particular, if L is the best-start nearest-unvisited length, then a_k≤L/k. Summing gives the harmonic upper bound.

Consequently the supremum of the ratio over graphs with at most N vertices has order Θ(log N). The construction resolves boundedness and matches the order of this universal upper bound. This paragraph is an independent direct proof; it does not infer a two-start comparison merely from a bad-to-optimal approximation example.

### Reproducibility and limits

`q2397_spiked_path.py` constructs this exact family at heights 1 through 8, computes tree distances with exact integer arithmetic, and checks the nearest-unvisited walk from both designated starts. It verifies every choice is unique, both length formulas hold, the explicit binary perturbation preserves the orders, all unordered pairwise distances become distinct, and the good length changes by less than 1/256. The output `q2397_spiked_path.json` contains every finite graph as a quarter-unit edge list plus the exact perturbation rule, the two full orders, the exact lengths, and the resulting ratios. There is no randomized search or simulation. The universal proof is the induction above; these bounded finite computations supply an additional reproducible check.

The construction's recursive skeleton is credited to Fritsch. This report makes no historical-priority claim for the additional two-start comparison or the perturbation; it gives a complete proof under the retained statement's exact assumptions.

## 5. Q2396: an exact four-weight entropy theorem

**Programme:** B5. **Question:** Q2396. **Stable statement ID:** adf6fb6ae4ba18aaf563.

**Exact retained statement.** Is H_n concave on [0,1] for every such sequence and every n≥1?

**Supplied setup.** For integers 2=a₁<a₂<⋯, put P₁(p)=(p,1−p), P_{n+1}(p)=p(P_n(p),0,…,0)+(1−p)(0,…,0,P_n(p)) in R^{a_{n+1}}. Set H_n(p)=−Σ_jP_{n,j}(p)log P_{n,j}(p), with 0log0=0.

Retained formulation and weighted-sum representation

For integers `2=a_1<a_2<...`, the retained vectors are

\[
 P_1=(p,1-p),\qquad
 P_{n+1}=p(P_n,0,\ldots,0)+(1-p)(0,\ldots,0,P_n).
\]

Their entropy is the entropy of

\[
 S=\sum_{i=1}^n w_i B_i,
 \quad w_1=1,\quad w_{i+1}=a_{i+1}-a_i>0,
 \quad B_i\stackrel{\mathrm{iid}}\sim\operatorname{Bernoulli}(1-p).
\]

Reflection of the parameter preserves concavity. For arbitrary positive real weights use iid Bernoulli(p) variables and write

\[
 q_s(p)=\sum_{k=0}^n N_{s,k}p^k(1-p)^{n-k},
 \quad N_{s,k}=\#\{A\subseteq[n]: |A|=k,\ \sum_{i\in A}w_i=s\}.
\]

The entropy depends only on the multiset of coefficient rows `N_s`, not on the numerical support values. Complementation of subsets gives `H(p)=H(1-p)`.

### Theorem 1 (exact computer-assisted four-variable theorem)

For every `w_1,w_2,w_3,w_4>0`, the function

\[
 H(p)=H\!\left(\sum_{i=1}^4 w_i B_i\right)
\]

satisfies `H''(p)<0` for every `0<p<1`. In particular, it is strictly concave on `[0,1]`. This implies Q2396 for `n=4`.

The proof has a finite exact combinatorial part and an exact interval part. Both are implemented with Python standard-library integer/Fraction arithmetic. Floating-point values printed in JSON are displays only and never enter a proof decision.

#### Exact exhaustion of coefficient patterns

A collision of two distinct subset sums is an equation `u·w=0`, where `u` has coordinates in `{-1,0,1}`. Positivity of the weights forces `u` to have both signs. Identifying `u` and `-u` leaves exactly 25 hyperplanes in four dimensions.

For any actual positive vector `w`, let `R` be the row space generated by all its collision vectors. Since `w` is nonzero and orthogonal to `R`, `dim R<=3`. Thus some subset of at most three of the 25 vectors forms a basis of `R`. Enumerating all such subsets and taking exact reduced row echelon forms exhausts all possible relation spaces. It gives 522 distinct spaces.

For each candidate space `R`, the script examines the rational polytope

\[
 \{w\in\mathbb R^4: Rw=0,\ w_i\ge0,\ \textstyle\sum_i w_i=1\}.
\]

Every vertex has at most `rank(R)+1` nonzero coordinates. Enumerating all supports of that size or smaller and solving the linear systems exactly finds all vertices. The polytope contains a strictly positive point if and only if the sum of its vertices has every coordinate positive. This retains 216 spaces.

For a retained space, two subset indicators are equivalent if their difference belongs to `R`; exact row reduction tests this. Every actual positive weight vector is included. Conversely, the relatively open positive part of the null space contains a point outside every additional collision hyperplane, because a finite union of proper hyperplanes cannot cover an open set. Thus the enumeration is exact rather than an overapproximation.

Counting subset cardinalities in each equivalence class and discarding the names of the classes gives exactly 23 entropy patterns. Representatives are recorded in `patterns4.json`. `classify4.py` checks that the supplied pattern set equals the set generated by the exact enumeration.

#### Removing the endpoint logarithmic singularity

For a coefficient row define `r_s=min{k:N_{s,k}>0}`, `ell_s=max{k:N_{s,k}>0}`, `t_s=4-ell_s`, and

\[
 R_s(p)=\sum_{k=r_s}^{\ell_s}N_{s,k}p^{k-r_s}(1-p)^{\ell_s-k}.
\]

Then `q_s=p^{r_s}(1-p)^{t_s}R_s`. Put

\[
 A(p)=\sum_s r_s q_s(p),\quad B(p)=\sum_s t_s q_s(p).
\]

Writing `A(p)=sum_{j=1}^4 a_jp^j`, one has `a_1=4`, since all four one-element subsets contribute to first order. Therefore

\[
 H=-A\log p-B\log(1-p)-\sum_s q_s\log R_s.
\]

Let `z=p`, `q=1-p`. The following expression is exactly `pH''(p)`:

\[
\begin{aligned}
 C(p)={}&-A''(p)[p\log p]
       +\sum_{j=1}^4(1-2j)a_jp^{j-1}\\
 &+p\left[-B''\log q+\frac{2B'}q+\frac B{q^2}\right]\\
 &+p\sum_s\left[-q_s''\log R_s
 -\frac{2q_s'R_s'}{R_s}
 -\frac{q_sR_s''}{R_s}
 +q_s\left(\frac{R_s'}{R_s}\right)^2\right].
\end{aligned}
\]

This extends continuously to `C(0)=-4`. On every interval touching zero and contained in `[0,1/4]`, monotonicity of `p log p` gives the exact enclosure `[b log b,0]` for `0<=p<=b`. All other logarithms have positive arguments. Symmetry permits restriction to `[0,1/2]`.

#### Rational logarithm bounds and interval certificate

All intervals have endpoints represented in units of `2^{-64}`. Addition, multiplication, division and polynomial evaluation round outward with integer floor/ceiling operations. To enclose `log x`, reduce `x=2^k y`, `1<=y<2`, and put `t=(y-1)/(y+1)`, so `0<=t<1/3`. The verifier uses

\[
 \log y=2\sum_{j=0}^{23}\frac{t^{2j+1}}{2j+1}+E,
 \quad |E|\le\frac{2|t|^{49}}{49(1-t^2)}.
\]

The same formula at `t=1/3` encloses `log 2`. Every quantity in these bounds is rational. Natural interval evaluation of `C` is then performed on dyadic subintervals, bisecting whenever the upper bound is not strictly negative.

For all 23 patterns the verifier terminates, using 130 terminal subintervals in total. At most five bisections from the initial interval `[0,1/2]` are needed; the smallest terminal interval width is `2^{-6}=1/64`. Every stored upper-bound numerator is strictly negative. Each pattern in `certificate4.json` includes the full sorted list `[left_numerator,right_numerator,curvature_upper_numerator]`, all in units of `2^{-64}`. The verifier explicitly checks that the intervals are contiguous, begin at zero, and end at `1/2`. The least negative displayed bound is approximately `-0.0002709522840406739`; it is certified by the exact inequality

\[
 C(p)\le-4998187439885368/18446744073709551616<0
\]

on the corresponding terminal interval. This loose interval upper bound is not an estimate of the actual minimum curvature margin.

These boxes cover `[0,1/2]`; for `p>0`, `C<0` implies `H''<0`. Symmetry gives the other half. Continuity at the endpoints then proves concavity on the closed interval, and strict negativity in its interior gives strict concavity.

#### Reproduction

Run from the workspace root:

```
python b5_work/entropy/classify4.py
python b5_work/entropy/certify4.py
```

Neither proof script needs third-party dependencies. `explore4.py` is a separate, non-proof exploratory script requiring NumPy. The JSON files `classification4.json` and `certificate4.json` record the exact enumeration counts and certificate summaries.

### Corollary 2 (arbitrarily many summands with separated blocks)

Partition the weights into nonempty blocks of size at most four. Suppose the map from the tuple of attainable block sums to their total sum is injective. Then the total entropy is the sum of the block entropies, hence is strictly concave in the common Bernoulli parameter.

For integer weights, an explicit family with genuine collisions inside each block is

\[
 (1,1,2,3),\quad M(1,1,2,3),\quad M^2(1,1,2,3),\quad\ldots,
 \qquad M\ge8.
\]

Each block sum lies in `{0,...,7}`. Uniqueness of base-`M` digit representations implies the required injectivity. Every finite initial collection of full blocks therefore has strictly concave entropy; partial final blocks also do, by the corresponding cases of size at most three. Arranging these positive weights after an initial weight 1 yields a retained overlap sequence through successive partial sums.

### Proposition 3 (endpoint concavity for every fixed finite vector)

For any fixed `n>=1` and positive real weights, as `p↓0`,

\[
 H''(p)=-\frac np+O(|\log p|+1).
\]

Consequently entropy is strictly concave in neighborhoods of both endpoints.

Proof. Let the distinct weight values have multiplicities `m_1,...,m_d`, so `sum m_j=n`. The atom at zero has mass `(1-p)^n`. Every nonzero atom has form `p^r c(1+O(p))` for some positive integer `c` and `r>=1`. The first-order atoms, exactly those reached by singleton subsets, have leading coefficients `m_j`. Expand their logarithms after factoring out `p^r`; the remaining factors are analytic and positive near zero. Summing gives

\[
 H(p)=-np\log p+\left(n-\sum_{j=1}^d m_j\log m_j\right)p
      +O(p^2|\log p|).
\]

The factored analytic expansions permit termwise differentiation, giving the stated second-derivative expansion. Complement symmetry treats `p↑1`.

This proposition does not exclude an interior counterexample when `n>=5`.

### Correction to a retrieved source calculation

For weights `(a,a,2a)`, the entropy loss from merging equal-weight singleton/pair configurations is `2p(1-p)log 2`, while the cross-cardinality collision loses `p(1-p)h(p)`. Therefore

\[
 H(p)=3h(p)-2p(1-p)\log2-p(1-p)h(p).
\]

The retrieved answer prints `4p(1-p)log2` and later inconsistent second-derivative signs. Its qualitative common-parameter concavity conclusion is still correct, and its separate heterogeneous counterexample with `(p_1,p_2,p_3)=(1/5+t,1/5-t,1/2)` remains valid. None of the four-variable certificate relies on those displayed source computations.


### Proof for one, two and three weights


Write `v=p(1-p)` and `h=-p log p-(1-p)log(1-p)`. For one weight, `H=h`. For two weights, the weights are either distinct, giving `H=2h`, or equal, giving `H=2h-2v log2`. Their second derivatives are negative because `h''=-1/v` and `v''=-2`.

For three sorted positive weights `a<=b<=c`, subset-sum collisions have exactly five types. Equal-cardinality collisions force equal weights. If all weights are distinct, the only possible collision across cardinalities is `c=a+b`: positivity rules out every other one-versus-two collision, and the empty/full subsets are isolated. If exactly two weights are equal, the only possible additional collision is the multiset `(a,a,2a)`. Thus the exhaustive entropy formulas are:

| Weight pattern | Entropy |
|---|---|
| No subset-sum collision | `3h` |
| Exactly two equal weights, without another collision | `3h-2v log2` |
| All three weights equal | `3h-3v log3` |
| Three distinct weights with `c=a+b` | `(3-v)h` |
| Weights `(a,a,2a)` | `(3-v)h-2v log2` |

The first three have second derivative at most `-12+6log3<0`. For either of the last two, write `H=(3-v)h-c_0v`, where `c_0=0` or `2log2`. Direct differentiation gives

\[
 H''=-\frac{3-v}{v}
      -2(1-2p)\log\frac{1-p}{p}
      +2h+2c_0.
\]

The product `(1-2p)log((1-p)/p)` is nonnegative, `v<=1/4`, and `h<=log2`. Consequently

\[
 H''\le-11+6\log2<0.
\]

This establishes all block cases of sizes one to four used in Corollary 2 without relying on erroneous displayed formulas in the retrieved answer.


### Equality closure in the finite enumeration


The enumerated object is a **row space**, not merely a selected list of collision equations. If `U` is a selected independent list and `R=span(U)`, the complete forced collision set is

\[
 \operatorname{Cl}(R)=\{u\in\{-1,0,1\}^4:\ u\text{ has both signs and }u\in R\}/\{u\sim-u\}.
\]

The implementation tests equivalence of subset indicators by reducing their difference modulo the entire row space `R`. It therefore automatically includes every additional collision equation in `Cl(R)`; it never treats the selected basis as the entire collision set. Since each enumerated `R` is generated by collision vectors, `span Cl(R)=R`.

For any actual positive weight vector, its full collision row space is present by the basis enumeration. For any enumerated space whose null space meets the positive orthant, choose a vector in that relatively open intersection outside the finitely many hyperplanes associated with collision vectors not belonging to `R`. Such vectors exist because none of those hyperplanes contains the null space. For the chosen vector, the full collision set is exactly `Cl(R)` and the full collision row space is exactly `R`. This verifies both directions, including equality closure.


**Source comparison.** The retained common-parameter statement and the four-variable numerical pattern claim were checked against the original [MathOverflow question and answer](https://mathoverflow.net/questions/514729/a-recursive-overlap-construction-of-finite-bernoulli-sum-laws-and-an-entropy-con/515134). The full arXiv paper was unavailable through the attempted reader. The result here rests on the exact verifier and its written reduction, not on the source's numerical checks.

## 6. Q2395: a computable stationary law

**Programme:** B5. **Question:** Q2395. **Stable statement ID:** c7b23369c6f031f11c93.

**Exact retained statement.** Give an explicit description of the unique stationary distribution of this infinite particle system.

**Supplied setup.** For each k, particles 0<X₁<⋯<X_k obey dX_i/dt=X_i. At every point (x,t) of a unit-intensity Poisson process on (0,∞)², move the nearest particle strictly right of x to x, if one exists. The k-particle laws form a consistent infinite system.



Let `f^lambda` denote the number of standard Young tableaux of a partition `lambda`, with `f^emptyset=1`. Let `f^{nu/lambda}` denote the number of standard tableaux of the skew diagram, and set it to zero unless `lambda⊆nu`. All these integers are computable recursively; for ordinary shapes,

\[
 f^\lambda=|\lambda|!/\prod_{c\in\lambda}h(c).
\]

### Theorem 4 (Plancherel construction of the stationary law)

Start a discrete partition chain at `Lambda_0=emptyset`. From a shape `lambda` of size `n`, add a single box to obtain `nu` with probability

\[
 P(\lambda,\nu)=\frac{f^\nu}{(n+1)f^\lambda}.
\]

Independently, let `T_n=E_1+...+E_n` for iid Exp(1) variables. Define

\[
 K_i=\inf\{n:(\Lambda_n)_1=i\},\qquad X_i=T_{K_i}.
\]

Then `(X_1,X_2,...)` has the unique stationary law in Q2395. This gives a sampling rule and a law involving only explicit tableau counts and independent exponential variables.

#### Proof

Let a unit Poisson process fall in the positive quadrant with coordinates `(y,s)`. Run the ordinary Hammersley process from the empty configuration at time `s=0`; if an event has no particle to its right, create one there. Each bounded horizontal prefix is determined by its own finitely many Poisson events over a bounded time interval: if there is no particle to the right within that prefix, create one at the event. Events farther right cannot affect its restriction. These finite-prefix constructions are consistent and define the infinite process. Write `Y_i(s)` for its ordered particles. All fixed particle indices exist at every `s>0` almost surely, and there are finitely many in every bounded interval.

Set `s=e^t` and `X_i(t)=sY_i(s)`. Between events, `dX_i/dt=X_i`. The change `(y,s)→(x=sy,t=log s)` has Jacobian one for the intensity measure: `dy ds=dx dt`. Events therefore form a unit space-time Poisson process in `(x,t)`, and multiplying coordinates by a positive scalar preserves the nearest-particle-to-the-right rule. The first `k` coordinates thus have the dynamics in Q2395.

The area-preserving map `(y,s)→(cy,s/c)` shows that the law of `sY_i(s)` does not depend on `s`. Equivalently, translating `t` induces an intensity-preserving transformation of the underlying Poisson process, proving stationarity. The uniqueness supplied in Aldous's question identifies this stationary construction with the requested law.

At `s=1`, the number of particles up to horizontal position `x` equals the length of the longest increasing sequence of Poisson points in `[0,x]×[0,1]`, by the patience-sorting rule. Scan those points by increasing horizontal coordinate. Their horizontal arrival positions are a rate-one Poisson process, and their vertical marks are independent uniform variables. Applying RSK to the successive marks makes the first-row length equal to that longest increasing subsequence length.

For a uniform random permutation of `n` elements, the RSK correspondence is a bijection to pairs `(P,Q)` of standard tableaux of the same shape. A specified recording tableau `Q` of shape `lambda` occurs with probability `f^lambda/n!`. A one-box extension of `Q` to shape `nu` therefore has conditional probability `f^nu/((n+1)f^lambda)`. These are exactly the transitions above. The Poisson arrival positions are independent of the uniform marks and hence of the shape chain. The first-row hitting times are exactly the particle locations.

The chain reaches every first-row size almost surely: the longest increasing subsequence length of an infinite iid continuous sequence is unbounded almost surely, for example by taking infinitely many disjoint blocks and requiring one specified increasing block of a given length.

### All finite-dimensional probabilities

Let `0=x_0<x_1<...<x_m`, `Delta_j=x_j-x_{j-1}`, and set `lambda^(0)=emptyset`. For nested partitions `lambda^(0)⊆...⊆lambda^(m)`, put `n_j=|lambda^(j)|` and `d_j=n_j-n_{j-1}`. Then

\[
\boxed{
 \Pr\{\Lambda_{N(x_j)}=\lambda^{(j)},\ 1\le j\le m\}
 =e^{-x_m}\frac{f^{\lambda^{(m)}}}{n_m!}
    \prod_{j=1}^m
       \frac{f^{\lambda^{(j)}/\lambda^{(j-1)}}\Delta_j^{d_j}}{d_j!}.
}
\]

To obtain any joint particle event, sum this expression over the corresponding first-row restrictions, using

\[
 \{X_i\le x\}=\{(\Lambda_{N(x)})_1\ge i\},\quad
 \{X_i>x\}=\{(\Lambda_{N(x)})_1<i\}.
\]

For example, a joint survivor probability at increasing thresholds is obtained by imposing `(lambda^(j))_1<i_j`. For arbitrary thresholds, first sort their distinct values and collect the restrictions at each value. This gives the complete finite-dimensional stationary distribution.

Proof of the formula: in `d` discrete additions, the number of paths from `lambda` to `nu` is `f^{nu/lambda}`. Multiplying the one-box probabilities along a path telescopes to `f^nu |lambda|!/(f^lambda |nu|!)`. Multiply over intervals and then by the independent Poisson increment probabilities `e^{-Delta_j}Delta_j^{d_j}/d_j!`.

The series is absolutely convergent because every summand is nonnegative and the unrestricted sum equals one. Truncation to `n_m<=M` incurs error at most

\[
 \Pr\{\operatorname{Poisson}(x_m)>M\}.
\]

For `M+1>x_m`, a simple explicit bound is

\[
 e^{-x_m}\frac{x_m^{M+1}}{(M+1)!}
 \left(1-\frac{x_m}{M+2}\right)^{-1}.
\]

Thus, at computable input thresholds, the formula is computable with a certified absolute error and does not require solving an unknown stationary density equation.

### Checks and simpler consequences

1. `K_1=1`, so `X_1~Exp(1)`. Moreover `X_1=E_1` is independent of the entire shifted configuration `(X_2-X_1,X_3-X_1,...)`, since that configuration depends only on the shape chain and `E_2,E_3,...`.
2. For `b>=2`, `Pr(K_2=b)=1/[b(b-2)!]`. Before the second first-row box is added the shape is a column. The probability of staying a column through size `b-1` is `1/(b-1)!`; the chance of growing the first row at the next step is `(b-1)/b`. This recovers the source's formula.
3. Consequently, for `0<x_1<x_2` and `z=x_2-x_1`,

\[
 p_2(x_1,x_2)=e^{-x_2}\sum_{m=0}^\infty\frac{z^m}{(m+2)(m!)^2}.
\]

This agrees with equations (46)–(48) of Aldous's 1993 notes. It is a check rather than a new result.
4. Every one-point survivor is a finite Bessel determinant:

\[
 \Pr(X_k>x)=e^{-x}\det[I_{i-j}(2\sqrt{x})]_{i,j=1}^{k-1},
\]

where the empty determinant for `k=1` is one and `I_r` is the modified Bessel function (`I_{-r}=I_r`). This follows by taking first-row length at most `k-1` and applying Proposition 7 of the 1999 paper. For `k=2`, it gives `e^{-x}I_0(2sqrt x)` and hence `E X_2=e`, consistent with the source's mean gap `e-1`.

### What this does and does not settle

The Plancherel chain and skew-tableau sum specify the entire stationary law, with explicit nonnegative terms and quantitative truncation. They are a rigorous constructive answer to a literal request for a fairly explicit description. The cited notes already contain a closely related random-permutation representation, so it would be premature to mark Q2395 as a new solution in an open-problem registry without checking whether this degree of explicitness meets the original intended question. A compact joint density, a factorization of all gaps, or a finite determinant for all multipoint probabilities has not been established here.


### Exact computation and independent RSK verification


`plancherel_stationary_check.py` implements ordinary tableau counts by the hook formula, skew-tableau counts by removing the largest-entry corner, and the explicit transition and finite-dimensional coefficient formulas. Its input and exact output are archived in `plancherel_stationary_input.json` and `plancherel_stationary_output.json`. It requires only the standard library and resolves its files relative to its own location.

The independent check directly performs row-insertion RSK on every permutation of sizes zero through seven: **5,914 permutations** in total. For the stated prefix observations it compares each complete joint-shape histogram with the skew-tableau product formula. The same permutation data independently evaluates the two-time event below with final Poisson count at most seven and gives exactly the coefficient

\[
 2662339429/650280960.
\]

This agrees with the separate tableau calculator. Through size twelve, all **195 transition rows** at sizes zero through eleven normalize exactly. Ordinary counts agree with the independently recursive skew counts, and `sum_{lambda⊢n}(f^lambda)^2=n!` is checked at each size. With no first-row restrictions, the two-time coefficient at thresholds `1/2,3/2` is exactly

\[
 \sum_{n=0}^{12}\frac{(3/2)^n}{n!}
 =\frac{36185315027}{8074035200},
\]

which verifies the required Poisson normalization and absence of an extraneous factorial or exponential factor.

#### One-time numerical problem, retained in exact symbolic form

For the stationary event `X_2>1`, write `P_1` for its true probability. At cutoff twelve the calculation gives

\[
 0\le P_1-
 e^{-1}\frac{523033825507476769}{229442532802560000}
 \le e^{-1}\frac1{5782233600}.
\]

The computed coefficient agrees exactly with the first thirteen terms of `I_0(2)=sum_{n>=0}1/(n!)^2`.

#### Two-time example

For `P_2=Pr(X_2>1/2, X_3>3/2)`, the restrictions are first-row lengths at most one and at most two at the respective thresholds. At cutoff twelve,

\[
 0\le P_2-
 e^{-3/2}\frac{3847668197480346050089}{939796614359285760000}
 \le e^{-3/2}\frac{6561}{187432960000}.
\]

All displayed coefficients and all verification decisions are exact rational arithmetic. The error bounds are the elementary Poisson-tail bounds from the theorem. No simulation or floating-point assertion is used.

Run:

```
python b5_work/entropy/plancherel_stationary_check.py
```

**Primary sources.** [Aldous's exact problem page](https://www.stat.berkeley.edu/~aldous/Research/OP/left_Hamm.html); [unfinished 1993 notes](https://www.stat.berkeley.edu/~aldous/Research/OP/patience.pdf), Sections 4.1–4.2, equations (42), (46)–(48); [Aldous–Diaconis 1999](https://www.stat.berkeley.edu/~aldous/Papers/me86.pdf), Section 2.1 and Proposition 7. The 1993 notes already contain the Poisson-embedded permutation representation. The complete finite-dimensional series is derived explicitly here without claiming novelty for its ingredients.

## 7. Random-environment and cookie-walk audit

### Disposition

The pinned candidate manuscripts match Q1789 and Q1790 at the level of both the mathematical model and their theorem statements. A bounded manual review of substantial proof sections found no explicit counterexample or decisive proof error. This is **not** a completed independent verification. No Lean executable was available on PATH, no kernel check was run, and no build was attempted. Neither target should be relabelled as independently solved on this evidence alone.

The source-level formalization check is appreciably stronger than the handoff's scope-note inspection: the actual Q1789, Q1790 and velocity-hemisphere solutions, their complete local dependency closures, their models, and the comparator-to-solution mappings were retrieved at the pinned commit. The challenge files contain placeholders; the actual solution files are different files.

### Exact target mapping

| Stable ID | Retained question | Candidate relationship | Remaining qualification |
|---|---|---|---|
| `8bae191e2b95d4bb0733` | Q1789, a.s. directional transience implies positive liminf speed, iid uniformly elliptic nearest-neighbor rows, d ≥ 2 | Ballisticity manuscript Theorem 1.1, printed/PDF p. 3, asserts the stronger deterministic vector LLN with positive projection | Full analytic argument and kernel verification not completed |
| `dcf3adbfb27d291659db` | Q1790, each fixed nonzero real direction has annealed escape probability 0 or 1, iid strictly elliptic nearest-neighbor rows, d ≥ 3 | Strict-ellipticity manuscript Theorem 1.1, printed/PDF p. 2, matches all retained assumptions | Full independent verification not completed |
| `80f9b93340290f8ce5da` | Q1185, almost-sure openness of the *random pathwise* set of transient directions, bounded jumps and a.s. quenched irreducibility, d ≥ 2 | No full match | Bounded jumps are more general than nearest-neighbor uniform ellipticity; the fixed-direction probability hemisphere is not itself a simultaneous pathwise theorem |
| `34cba2e1eafff79891a2` | Q2498, bounded-cookie directional zero-one law | No match | A visit-indexed cookie stack does not fix a transition row at a site |
| `3a9c8d8a68e36d9511bf` | Q2499, cookie recurrence–transience dichotomy without bounding cookies | No match | Both the model and the asserted dichotomy differ |

The environment coordinate in the retrieved Lean transition kernels is retained verbatim when a step is taken. The initial law samples its product environment once; the trajectory subsequently samples steps from the row at the current site. This agrees with ordinary fixed-environment RWRE and does not silently resample the environment on a return visit.

### What the manual proof review checked

#### Q1790

The manuscript has 34 pages including references. The review read the fresh-row and regeneration arguments, the finite-radius argument, the opposite-ray reduction, the bridge and common-block construction, the entropy comparison, the posterior maximum estimate, the first-contact estimate, and the final incompatible bounds for contact scales.

The following delicate points were explicitly considered rather than inferred from a theorem assertion:

1. A finite path uses departure rows. Stopping a second path at its first *arrival* in the first departure set does not consume the row at that contact. This makes the initial independent/shared-environment transfer legitimate. An environment-dependent classification must be made after that transfer.
2. Regeneration cuts depend on the future. Their independence is obtained by enumerating finite words and factoring a fresh infinite suffix, rather than using an annealed stopping-time Markov property at such a cut.
3. The real direction need not produce discrete heights. Counting ordinary record *indices* instead of height values produces an integer renewal process and the finite expected projected width.
4. The radius argument does not require finite time duration: its forced script has distinct fresh departure rows and its subsequent template first separates by a tilted linear functional and then by height.
5. In the contact estimate, endpoint posteriors remain in the unrevealed annealed path filtration. Their stopped path marginal agrees with the fresh comparison path; no martingale property is assumed after the whole environment has been exposed.
6. A complete positive path and the negative path's unique first-contact prefix are counted once. This avoids a multiplicity from arbitrary overlapping prefixes.
7. The entropy comparison randomizes both the chunk count and the buffer count. The resulting entropy increments telescope. The later lower-bound argument conditions on a cut of probability bounded below, and then explicitly removes that conditioning; it does not claim that the unconditioned lower event has probability tending to one.

These checks did not reveal a decisive error. They do not substitute for checking every lemma and every limiting argument. The central proof-bearing propositions are 3.1 (spatial radius), 5.1 (upper contact count), 6.2 (first contact), and 7.1 (lower contact count). A future independent audit should start with these and their exact formal counterparts.

#### Q1789

The manuscript has 58 pages including references. The review examined the model and main theorem; the true-word/finite-radius reduction; the conditional crossing-probability-to-speed argument; the stated Gaussian-scale and clipping machinery; and the stationary-profile/entropy contradiction in the final section. The lengthy shared-environment and multiscale construction in §§3–7 was not checked line by line.

The proof separates three notions which must stay separate in the research ledger: finite regeneration spatial radius; finite regeneration duration; and a deterministic positive velocity. The speed conclusion is conditional, until the small crossing-probability estimate is established. In the final profile argument, the tail statistic is translation invariant, a class is marked uniformly rather than by its evolving mass, and the finite entropy comparison is applied at each fixed episode-window length before sending that length to infinity. These are substantive mathematical steps, not proof receipts.

The remaining audit tasks are specific: the shared-environment joint scaling limit with only spatial first moments; the uniformly local approximation in the outward-order kernel estimate; the adaptive episode construction; and the limiting stationary array with its entropy bound. No failure of one of these steps was established during this bounded audit. Calling them “gaps” would overstate the evidence.

### Formal-source evidence

The following comparator JSON files identify the actual solution modules:

| Comparator | Actual solution module |
|---|---|
| `DirectionalWalk` | `OAI.Probability.DirectionalWalk.Main` |
| `DirectionalBallisticity` | `OAI.Probability.Ballisticity.Main` |
| `VelocityHemisphere` | `OAI.Probability.Ballisticity.VelocityHemisphere` |

Each JSON lists the permitted axioms `propext`, `Quot.sound`, and `Classical.choice`. That is a configuration, not the result of a local axiom audit. The challenge statements' `sorry` terms are not in the actual solution modules.

The complete reachable OAI source closures have these sizes:

| Result | Reachable OAI files | Lines | Bytes |
|---|---:|---:|---:|
| Q1790 zero-one theorem | 69 | 18,194 | 951,618 |
| Q1789 ballisticity theorem | 513 | 98,412 | 5,012,403 |
| Velocity-hemisphere theorem | 585 | 116,839 | 5,974,000 |

There are no missing OAI imports in these closures. Their only external import is `Mathlib`. A literal scan of all 585 files found no `sorry`, `admit`, `axiom`, `unsafe`, `implemented_by`, `opaque`, custom `elab`/`syntax`/`macro`, `native_decide`, `initialize`, `run_tac`, or `run_elab`. This rules out those straightforward source shortcuts in the retrieved closures; it does not prove successful elaboration, kernel correctness, or semantic equivalence of all intermediate definitions.

The comparator's complete definition prefix before its requested theorem is byte-for-byte identical to the beginning of the actual `Model.lean` in both Q1790 (3,089 bytes) and Q1789 (3,828 bytes). The hemisphere bridge was also inspected: it pushes nonnegative-real rows to real rows and proves equality of the resulting annealed path measures, rather than merely identifying two suggestively named models.

The pinned toolchain is `leanprover/lean4:v4.34.1`. The pinned Mathlib revision is `d13f23b723b8a846827a245b89c10fc7d3f11612`, from the standard `leanprover-community/mathlib4` repository. The runtime and that dependency were not installed for this audit.

Machine-readable provenance is in `all_dependency_closures.json`, `directional_static_scan.json`, `ballisticity_static_scan.json`, `comparator_model_prefix_check.json`, and `pdf_sha256.json`. The fetching scripts preserve the pinned commit and individual SHA-256 digests. These are source provenance records, not mathematical certificates.

### Restricted consequence for Q1185

Here is a rigorously justified, explicitly conditional corollary that avoids an uncountable-null-set inference.

**Planar conditional corollary.** Suppose an iid uniformly elliptic nearest-neighbor RWRE on Z² has positive probability of escape in some deterministic direction. Assume the candidate Q1789 ballisticity theorem is valid. Then its pathwise set of unit transient directions is almost surely an open hemisphere.

**Proof.** The established planar directional zero-one law upgrades positive-probability transience to probability one. The assumed ballisticity theorem gives a deterministic nonzero velocity v. On the single probability-one event of vector convergence, every direction u with v·u > 0 escapes to positive infinity, and every u with v·u < 0 escapes to negative infinity; these assertions hold simultaneously by applying the deterministic limit to each u. The equator in dimension two consists of exactly two deterministic unit directions. If either equatorial direction had positive escape probability, the planar zero-one law followed by the assumed ballisticity theorem would give another deterministic velocity with positive projection on that direction. Uniqueness of the almost-sure vector limit makes that velocity equal to v, a contradiction. The union of these two equatorial null events is null. Hence the pathwise set equals {u : v·u > 0}. ∎

This is conditional on the unverified candidate theorem and covers only the stated planar nearest-neighbor regime with an existing deterministic transient direction. It does not solve the retained Q1185.

In higher dimension, the equator is uncountable. One possible additional route is to exploit the iid regeneration-word tail sigma field and the convexity of the escape cone intersected with v⊥. To turn that route into a theorem one must justify measurability of the closed equatorial escape cone and its tail invariance, then use deterministic relative interiors. That extra argument was not promoted to a result in this audit.

### Cookie scope and cited nonmatches

The Kosygina–Zerner survey's Problem 3.20 explicitly asks whether (IID), (BD), and (UEL) suffice in d ≥ 2; Problem 3.21 asks for recurrence or transience under (IID) and (UEL). These are printed on preprint p.16. Bounded cookies mean that every site has a bounded finite initial stack followed by simple-random-walk rows, not that the whole process becomes a fixed-environment walk after a deterministic global time. New sites continue to expose new initial cookies.

The linked arXiv:1304.7287 result is one-dimensional. It therefore does not close these retained d ≥ 2 questions. Qin's arXiv:2609.30045 studies M(2,1,2), with horizontal first departures and full planar later departures, and related balanced finite-total-strength stacks. It does not establish either general cookie question. It also does not answer the packet's M(2,1,1) question; its p.2 expressly leaves that model's recurrence conjectural.

### Primary references and retrieval notes

All OpenAI source URLs below use commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`.

- [Strict-ellipticity manuscript](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-directional-zero-one-law-under-strict-ellipticity-September-23-2026/paper.pdf).
- [Ballisticity manuscript](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Directional-transience-implies-ballisticity-September-23-2026/paper.pdf).
- [Q1790 actual main proof](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Probability/DirectionalWalk/Main.lean).
- [Q1789 actual main proof](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Probability/Ballisticity/Main.lean).
- [Velocity hemisphere actual proof](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Probability/Ballisticity/VelocityHemisphere.lean).
- [Drewitz–Ramírez source](https://arxiv.org/abs/1005.0376).
- [Zerner planar zero-one source](https://arxiv.org/abs/0706.0745).
- [Slonim bounded-jump paper](https://alea.impa.br/articles/v21/21-27.pdf).
- [Kosygina–Zerner survey](https://www.math.uni-tuebingen.de/user/zerner/pub/KosyginaZerner.pdf), downloaded directly and extracted locally.
- [Amir–Berger–Orenshtein one-dimensional cookie theorem](https://arxiv.org/abs/1304.7287).
- [Qin primary PDF](https://arxiv.org/pdf/2609.30045), downloaded directly and extracted locally.

Web opens of the pinned GitHub and raw GitHub PDFs returned DisabledError. Direct authorized urllib downloads of those exact raw URLs succeeded; the full PDFs and extracted text are retained next to this note. Thus a failed web-parser response should not be cited as if it contained the paper.

## 8. Exact statement register and dispositions

The statements and model setups in this section are transcribed from the supplied packet. Source locations are inherited unless a comparison in the corresponding result section says otherwise. Every provisional Q number is accompanied by its stable ID. Historical collector status is retained in the JSON ledger, separately from the new disposition.

### Q946: A sharp repeated-coverage bound without reversibility

**Stable ID:** 0c62464d2a79195bced5. **Disposition:** disproved.

**Exact retained statement.** For every finite irreducible Markov chain and k≥1, let t_cov^(k) be the worst-start expected time to visit every state k times, t_cov=t_cov^(1), and π*=min_iπ_i. Does t_cov^(k)≤C(t_cov+k/π*) hold with a universal C? Reversible chains are settled; the general bound loses log n. Periodic chains are included.

**Outcome of this investigation.** Lazy directed cycles with n=m^m and k=m have t_cov=1+(n-1)m, pi_min=1/n, and t_cov^(m)~nm^2; the proposed ratio is asymptotic to m/2.

**Remaining.** The optimal universal dimensional loss between the necessary order log(n)/loglog(n) and the published logarithmic upper bound is not determined.

**Primary source:** [Siu On Chan; Qinghua Ding; Sing Hei Li: Learning and Testing Irreducible Markov Chains via the k-Cover Time](https://proceedings.mlr.press/v132/chan21a.html). Definition 4; §5; §6.

### Q1185: Openness of random transient directions

**Stable ID:** 80f9b93340290f8ce5da. **Disposition:** unresolved.

**Exact retained statement.** For an iid random environment on Z^d, d≥2, with uniformly bounded jump range and almost surely irreducible quenched walk X starting at 0, is {ℓ∈S^{d−1}:X_n·ℓ→+∞} almost surely open in S^{d−1} under the annealed law?

**Outcome of this investigation.** A restricted planar corollary is proved conditionally on the unverified ballisticity theorem: under iid uniform ellipticity, nearest-neighbor jumps, and an existing deterministic transient direction, the pathwise transient set is an open hemisphere.

**Changed assumptions for the stated partial result.** Restrict to dimension two and uniformly elliptic nearest-neighbor environments. Assume positive-probability escape in some deterministic direction. Assume validity of the pinned, unverified Q1789 candidate theorem.

**Remaining.** The full bounded-jump, pathwise random-set openness statement remains unresolved.

**Primary source:** [Daniel Slonim: Random Walks in Dirichlet Environments with Bounded Jumps](https://danielslonim.github.io/SlonimThesis.pdf). Conjecture 3.4.1, pp.68–69; assumptions (C1)–(C3), p.14.

### Q1186: Sharp transience on doubled trees

**Stable ID:** 6db619f632f33288eec5. **Disposition:** unresolved.

**Exact retained statement.** If b>1+δ−δ/(3+2δ), must the walk have positive probability never to return to the root after its first step?

**Supplied setup.** Double every edge of an infinite locally finite rooted tree T. A walk starts at the root and chooses incident edges proportionally to weights: initially 1, then 1+δ after first traversal, δ>0. Put b=sup{s>0:inf_π Σ_{v∈π}|v|^{−s}>0}, where π runs over vertex cutsets meeting every infinite root-ray and |v| is root-distance.

**Outcome of this investigation.** No new proof, counterexample, or independently validated exact-scope resolution was obtained in this investigation.

**Remaining.** The exact retained statement remains unresolved in this investigation.

**Primary source:** [Pawel Rudnicki: Random walks with reinforcement](https://purehost.bath.ac.uk/ws/portalfiles/portal/344232966/Pawel_Rudnicki_-_Thesis.pdf). Chapter 4, Conjecture 2.4, p.149; definitions pp.145–148.

### Q1187: Slow exceptional branching minima

**Stable ID:** 4d8ce788167e3a7856ee. **Disposition:** unresolved.

**Exact retained statement.** On the rooted binary tree, independently put Bernoulli(1/2) labels on edges and refresh each at rate 1. Let M_n(t) be the minimum label-sum over root-to-level-n paths. For every γ>2, do exceptional times t≥0 almost surely exist with liminf_n log(γ)M_n(t)/loglog n≤1?

**Outcome of this investigation.** No new proof, counterexample, or independently validated exact-scope resolution was obtained in this investigation.

**Remaining.** The exact retained statement remains unresolved in this investigation.

**Primary source:** [Martin Prigent: Noise Sensitivity And Exceptional Times](https://purehost.bath.ac.uk/ws/portalfiles/portal/221647004/MPrigent_UoB_Thesis_Final.pdf). Conjecture 4.1, pp.140–142.

### Q1188: Planar switch transience

**Stable ID:** 59fb44c4695a865ff813. **Disposition:** unresolved.

**Exact retained statement.** Let X_j(t) be independent uniform {1,i,−1,−i} variables, each refreshed at rate 1, and Z_n(t)=Σ_{k≤n}∏_{j≤k}X_j(t). Does {t≥0:Z_n(t)=0 for only finitely many n} almost surely have Hausdorff dimension 1?

**Outcome of this investigation.** No new proof, counterexample, or independently validated exact-scope resolution was obtained in this investigation.

**Remaining.** The exact retained statement remains unresolved in this investigation.

**Primary source:** [Martin Prigent: Noise Sensitivity And Exceptional Times](https://purehost.bath.ac.uk/ws/portalfiles/portal/221647004/MPrigent_UoB_Thesis_Final.pdf). Conjecture 5.3, pp.180–181.

### Q1189: Critical escape scale for switch walks

**Stable ID:** 822b7cee623f61895eed. **Disposition:** unresolved.

**Exact retained statement.** Is {t∈[0,1]:liminf_n Z_n(t)/√n>0} almost surely empty?

**Supplied setup.** Independent stationary Rademacher coordinates X_j(t) refresh at rate 1. Put Z_n(t)=Σ_{k≤n}∏_{j≤k}X_j(t).

**Outcome of this investigation.** No new proof, counterexample, or independently validated exact-scope resolution was obtained in this investigation.

**Remaining.** The exact retained statement remains unresolved in this investigation.

**Primary source:** [Martin Prigent; Matthew I. Roberts: Noise sensitivity and exceptional times of transience for a simple symmetric random walk in one dimension](https://link.springer.com/article/10.1007/s00440-020-00978-7). §1, immediately after Theorem 1.

### Q1384: A monotone recurrence boundary for lattice frogs

**Stable ID:** 2238464a0bd21ac55452. **Disposition:** unresolved.

**Exact retained statement.** For every d≥2, is there a nonincreasing f_d:[0,1]→[0,1] such that the model is recurrent when w<f_d(α) and transient when w>f_d(α)?

**Supplied setup.** On Z^d, start one active frog at 0 and one sleeping frog elsewhere. Activated frogs independently make discrete-time nearest-neighbor walks, waking sleeping frogs they visit. For w,α∈[0,1], jumps ±e₁ have probabilities w(1±α)/2 and each ±e_j, j≥2, has probability (1−w)/(2(d−1)). Recurrence means infinitely many visits to 0 almost surely.

**Outcome of this investigation.** No new proof, counterexample, or independently validated exact-scope resolution was obtained in this investigation.

**Remaining.** The exact retained statement remains unresolved in this investigation.

**Primary source:** [Christian Döbler, Nina Gantert, Thomas Höfelsauer, Serguei Popov, Felizitas Weidner: Recurrence and Transience of Frogs with Drift on Z^d](https://arxiv.org/abs/1709.00038). Paper Conjecture 4.1, pp.20–21; thesis Conjecture 1.18, p. 14.

### Q1385: Concavity of the fastest-frog speed

**Stable ID:** 228ba1e208c05c2a7a54. **Disposition:** unresolved.

**Exact retained statement.** Is v(p) concave on [1/2,1]?

**Supplied setup.** On Z place one active frog at 0 and one sleeper at every other integer. After activation, frogs independently jump right with probability p∈[1/2,1] and left with probability 1−p each discrete step, waking visited sleepers. Let M_n be the rightmost active position and v(p)=lim_n M_n/n, the deterministic maximum speed.

**Outcome of this investigation.** No new proof, counterexample, or independently validated exact-scope resolution was obtained in this investigation.

**Remaining.** The exact retained statement remains unresolved in this investigation.

**Primary source:** [Thomas Höfelsauer; Felizitas Weidner: The speed of frogs with drift on Z. Markov Processes and Related Fields 22](https://arxiv.org/abs/1505.05006). Paper Conjecture 3.1; thesis Conjecture 1.24, p. 18.

### Q1386: The two unresolved tree degrees

**Stable ID:** 124e758489f92975df9b. **Disposition:** unresolved.

**Exact retained statement.** Is the model almost surely recurrent on T_3 and almost surely transient on T_4, where recurrence means infinitely many root visits?

**Supplied setup.** T_d is the infinite rooted d-ary tree. Initially the root has one active frog and every other vertex one sleeping frog. Active frogs make independent discrete-time simple random walks forever and activate sleepers they visit.

**Outcome of this investigation.** No new proof, counterexample, or independently validated exact-scope resolution was obtained in this investigation.

**Remaining.** The exact retained statement remains unresolved in this investigation.

**Primary source:** [Christopher Hoffman, Tobias Johnson, Matthew Junge: Recurrence and transience for the frog model on trees](https://arxiv.org/abs/1404.6238). Conjecture 2, p. 3; reaffirmation: Ahmed–Junge 2025, p. 1.

### Q1387: Monotonicity without frog deaths

**Stable ID:** 12e6c894ec1fc4ac77a7. **Disposition:** unresolved.

**Exact retained statement.** For each d≥2, is the recurrence probability nondecreasing in p on 0<p<1/2?

**Supplied setup.** On the infinite rooted d-ary tree, d≥2, start one active frog at the root and one sleeper elsewhere. Active frogs independently walk forever, waking visited sleepers. Away from the root they move to the parent with probability p and to each child with probability (1−p)/d. At the root they always choose a uniform child. Recurrence means infinitely many total root visits.

**Outcome of this investigation.** No new proof, counterexample, or independently validated exact-scope resolution was obtained in this investigation.

**Remaining.** The exact retained statement remains unresolved in this investigation.

**Primary source:** [Erin Beckman, Natalie Frank, Yufeng Jiang, Matthew Junge, Si Tang: The frog model on trees with drift](https://arxiv.org/abs/1808.03283). Introduction, pp.2–3; model definition, p. 1.

### Q1388: A single rotor bias threshold

**Stable ID:** de84ddb8c965600c60ca. **Disposition:** unresolved.

**Exact retained statement.** If each initial arrow points west with probability p and each other direction with probability (1−p)/3, is there a single p_c separating almost-sure recurrence for p<p_c from transience for p>p_c?

**Supplied setup.** A rotor walk starts at 0; each step advances the current vertex’s arrow in a fixed cyclic order and follows it. Initial arrows are independent. On Z² the order is clockwise; with uniform arrows the visited set R_t, scaled by t^(−1/3), has deterministic convex limit B.

**Outcome of this investigation.** No new proof, counterexample, or independently validated exact-scope resolution was obtained in this investigation.

**Remaining.** The exact retained statement remains unresolved in this investigation.

**Primary source:** [Ahmed Bou-Rabee; Yuval Peres: Eulerian walkers on Z^2 have range exponent 2/3](https://arxiv.org/abs/2608.23545). §7, Problem 2, pp.25–26.

### Q1389: Roundness of the rotor-walk limit

**Stable ID:** 8ad91c20025f42868a26. **Disposition:** unresolved.

**Exact retained statement.** For uniform initial arrows on the clockwise square lattice, is B a Euclidean disk?

**Supplied setup.** A rotor walk starts at 0; each step advances the current vertex’s arrow in a fixed cyclic order and follows it. Initial arrows are independent. On Z² the order is clockwise; with uniform arrows the visited set R_t, scaled by t^(−1/3), has deterministic convex limit B.

**Outcome of this investigation.** No new proof, counterexample, or independently validated exact-scope resolution was obtained in this investigation.

**Remaining.** The exact retained statement remains unresolved in this investigation.

**Primary source:** [Ahmed Bou-Rabee; Yuval Peres: Eulerian walkers on Z^2 have range exponent 2/3](https://arxiv.org/abs/2608.23545). §7, Problem 3, p. 26.

### Q1390: Diffusive limits above dimension two

**Stable ID:** bd4e13709dd3a1869380. **Disposition:** unresolved.

**Exact retained statement.** On Z^d, d>2, for every fixed translation-invariant cyclic rotor mechanism and independent uniform initial arrows, does the diffusively rescaled walk converge in law to Brownian motion?

**Supplied setup.** A rotor walk starts at 0; each step advances the current vertex’s arrow in a fixed cyclic order and follows it. Initial arrows are independent. On Z² the order is clockwise; with uniform arrows the visited set R_t, scaled by t^(−1/3), has deterministic convex limit B.

**Outcome of this investigation.** No new proof, counterexample, or independently validated exact-scope resolution was obtained in this investigation.

**Remaining.** The exact retained statement remains unresolved in this investigation.

**Primary source:** [Ahmed Bou-Rabee; Yuval Peres: Eulerian walkers on Z^2 have range exponent 2/3](https://arxiv.org/abs/2608.23545). §7, Problem 4, p. 26.

### Q1784: The unbiased critical-state limit

**Stable ID:** e9f34afc617ca1d72d44. **Disposition:** unresolved.

**Exact retained statement.** For every λ>0, does π_DD(λ,1/2) exist, with π_DD(λ,θ) converging locally to it as θ→1/2?

**Supplied setup.** ARW particles jump at rate one, right with probability θ; lone particles sleep at rate λ>0 and awaken on contact. Write ρ_c(λ,θ) for the infinite-line critical density and π_DD(λ,θ) for the local limit of finite-interval driven-dissipative stationary laws (exits killed). This limit exists for θ≠1/2.

**Outcome of this investigation.** No new proof, counterexample, or independently validated exact-scope resolution was obtained in this investigation.

**Remaining.** The exact retained statement remains unresolved in this investigation.

**Primary source:** [Joshua Meisel: Self-organized criticality in biased activated random walk](https://academicworks.cuny.edu/cgi/viewcontent.cgi?article=7992&context=gc_etds). §1.3, p. 10.

### Q1785: Critical cycle states in biased ARW

**Stable ID:** 81349e2d00ff067d348e. **Disposition:** unresolved.

**Exact retained statement.** Fix λ>0 and θ∈(0,1)\{1/2}. Stabilize ⌊ρ_c n⌋ particles placed independently uniformly on the n-cycle. Do the resulting laws, viewed near zero, converge locally to π_DD(λ,θ) as n→∞?

**Supplied setup.** ARW particles jump at rate one, right with probability θ; lone particles sleep at rate λ>0 and awaken on contact. Write ρ_c(λ,θ) for the infinite-line critical density and π_DD(λ,θ) for the local limit of finite-interval driven-dissipative stationary laws (exits killed). This limit exists for θ≠1/2.

**Outcome of this investigation.** No new proof, counterexample, or independently validated exact-scope resolution was obtained in this investigation.

**Remaining.** The exact retained statement remains unresolved in this investigation.

**Primary source:** [Joshua Meisel: Self-organized criticality in biased activated random walk](https://academicworks.cuny.edu/cgi/viewcontent.cgi?article=7992&context=gc_etds). Conjecture 3, p. 10; §1.2.4.

### Q1786: Spherical activated-walk aggregate

**Stable ID:** 0fd6f66812be3281c66d. **Disposition:** unresolved.

**Exact retained statement.** For n particles initially at zero, is there ρ_a>0 such that, for every ε∈(0,1), the visited set lies between the centered lattice balls of Euclidean volumes (1−ε)n/ρ_a and (1+ε)n/ρ_a with probability tending to one?

**Supplied setup.** Fix d≥2 and λ>0. In ARW on Z^d, active particles make rate-one simple random walks, sleep at rate λ when alone, and awaken on contact. Let S denote stabilization and ρ_c the infinite-volume fixation threshold.

**Outcome of this investigation.** No new proof, counterexample, or independently validated exact-scope resolution was obtained in this investigation.

**Remaining.** The exact retained statement remains unresolved in this investigation.

**Primary source:** [Lionel Levine and Vittoria Silvestri: Universality conjectures for activated random walk](https://arxiv.org/abs/2306.01698). Conjecture 1.

### Q1787: Higher-dimensional critical-time cutoff

**Stable ID:** 059ed0777612eb63205f. **Disposition:** unresolved.

**Exact retained statement.** On V_L=Z^d∩B(0,L), add a particle uniformly and stabilize each step, killing exits. Writing N_L for the stationary particle count, does some ρ_s>0 satisfy N_L/|V_L|→ρ_s in probability and t_mix(ε)/|V_L|→ρ_s for every ε∈(0,1), with worst-case total-variation mixing?

**Supplied setup.** Fix d≥2 and λ>0. In ARW on Z^d, active particles make rate-one simple random walks, sleep at rate λ when alone, and awaken on contact. Let S denote stabilization and ρ_c the infinite-volume fixation threshold.

**Outcome of this investigation.** No new proof, counterexample, or independently validated exact-scope resolution was obtained in this investigation.

**Remaining.** The exact retained statement remains unresolved in this investigation.

**Primary source:** [Lionel Levine and Vittoria Silvestri: Universality conjectures for activated random walk](https://arxiv.org/abs/2306.01698). Conjectures 11 and 19.

### Q1788: Forgetting dense initial configurations

**Stable ID:** a015b029d2e14d9a01f6. **Disposition:** unresolved.

**Exact retained statement.** For every ζ∈(ρ_c,1), does sup d_TV(Law(Sη),Law(Sη̃))→0 on (Z/LZ)^d, where the supremum is over active configurations with equal particle count in [ζL^d,L^d]?

**Supplied setup.** Fix d≥2 and λ>0. In ARW on Z^d, active particles make rate-one simple random walks, sleep at rate λ when alone, and awaken on contact. Let S denote stabilization and ρ_c the infinite-volume fixation threshold.

**Outcome of this investigation.** No new proof, counterexample, or independently validated exact-scope resolution was obtained in this investigation.

**Remaining.** The exact retained statement remains unresolved in this investigation.

**Primary source:** [Lionel Levine and Vittoria Silvestri: Universality conjectures for activated random walk](https://arxiv.org/abs/2306.01698). Conjecture 24.

### Q1789: Directional transience forces positive speed

**Stable ID:** 8bae191e2b95d4bb0733. **Disposition:** unresolved.

**Exact retained statement.** For every unit vector ℓ, does P_0(X_n·ℓ→+∞)=1 imply liminf_{n→∞} X_n·ℓ/n>0 almost surely?

**Supplied setup.** Let X start at zero in Z^d, d≥2, and jump to nearest neighbors using iid sitewise transition vectors ω(x,·), with a deterministic κ>0 satisfying ω(x,e)≥κ almost surely for every e∈{±e₁,…,±e_d}. P_0 averages over both environment and walk.

**Outcome of this investigation.** Pinned candidate theorem matches the retained target. Actual solution modules and complete local dependency closure were obtained; bounded analytic and source-level audits were performed.

**Remaining.** Full independent analytic verification and a build/kernel check with the pinned dependencies remain outstanding.

**Primary source:** [Alexander Drewitz and Alejandro F. Ramírez: Quenched exit estimates and ballisticity conditions for higher-dimensional random walk in random environment](https://arxiv.org/abs/1005.0376). Conjecture 1.1, p. 2.

### Q1790: Higher-dimensional directional zero-one law

**Stable ID:** dcf3adbfb27d291659db. **Disposition:** unresolved.

**Exact retained statement.** For every nonzero ℓ∈R^d, must P_0(lim_{n→∞}X_n·ℓ=+∞) belong to {0,1}?

**Supplied setup.** Consider nearest-neighbor RWRE X on Z^d, d≥3, started at zero. Sitewise transition vectors are iid and elliptic: each of the 2d nearest-neighbor jumps has strictly positive probability almost surely. P_0 is the annealed law.

**Outcome of this investigation.** Pinned candidate theorem matches the retained target. Actual solution modules and complete local dependency closure were obtained; bounded analytic and source-level audits were performed.

**Remaining.** Full independent analytic verification and a build/kernel check with the pinned dependencies remain outstanding.

**Primary source:** [Martin P. W. Zerner: The zero-one law for planar random walks in i.i.d](https://arxiv.org/abs/0706.0745). Introduction, p. 327.

### Q1791: Recurrence of the planar balanced excited walk

**Stable ID:** 1e520a66d369dc85d7bc. **Disposition:** unresolved.

**Exact retained statement.** Does Z visit every vertex infinitely often almost surely?

**Supplied setup.** Start Z_0=0 in Z². On first departure from any vertex take a vertical ±1 step; on later departures take a horizontal ±1 step. Signs are independent fair choices. Let R_n=|{Z_0,…,Z_n}|.

**Outcome of this investigation.** The linked later planar balanced-walk paper was checked as a possible route and concerns a different model.

**Remaining.** Neither the retained recurrence question nor its range-exponent question is resolved.

**Primary source:** [Omer Angel, Mark Holmes, Alejandro Ramírez: Balanced excited random walk in two dimensions](https://arxiv.org/abs/2110.15889). Introduction, after Theorem 1.1.

### Q1792: Existence of a balanced-walk range exponent

**Stable ID:** 8b6e6c22412067afaae6. **Disposition:** unresolved.

**Exact retained statement.** Is there a deterministic α∈[1/2,1] such that log R_n/log n→α in probability?

**Supplied setup.** Start Z_0=0 in Z². On first departure from any vertex take a vertical ±1 step; on later departures take a horizontal ±1 step. Signs are independent fair choices. Let R_n=|{Z_0,…,Z_n}|.

**Outcome of this investigation.** The linked later planar balanced-walk paper was checked as a possible route and concerns a different model.

**Remaining.** Neither the retained recurrence question nor its range-exponent question is resolved.

**Primary source:** [Omer Angel, Mark Holmes, Alejandro Ramírez: Balanced excited random walk in two dimensions](https://arxiv.org/abs/2110.15889). Open Problem 1.3.

### Q2087: Small reinforcement in dimensions three to five

**Stable ID:** 496e9bf6a22ffef49b95. **Disposition:** unresolved.

**Exact retained statement.** For every d∈{3,4,5}, is there a_d>0 such that this walk on Z^d is almost surely transient whenever 0<a<a_d?

**Supplied setup.** A walk starts at 0. Each undirected edge initially has weight 1, permanently changed to 1+a after its first crossing, a>0. At every discrete step it selects an incident edge proportionally to its current weight. Recurrence means infinitely many returns to 0.

**Outcome of this investigation.** No new proof, counterexample, or independently validated exact-scope resolution was obtained in this investigation.

**Remaining.** The exact retained statement remains unresolved in this investigation.

**Primary source:** [Dor Elboim and Gady Kozma: Once-reinforced random walk in high dimensions, 2026](https://arxiv.org/abs/2601.17972). Introduction and §1.1, pp. 1–2.

### Q2088: Large-reinforcement lattice recurrence

**Stable ID:** 0786dc65fb2e5fa1f4f3. **Disposition:** unresolved.

**Exact retained statement.** For every d≥3, is there A_d<∞ such that this walk on Z^d is almost surely recurrent whenever a>A_d?

**Supplied setup.** A walk starts at 0. Each undirected edge initially has weight 1, permanently changed to 1+a after its first crossing, a>0. At every discrete step it selects an incident edge proportionally to its current weight. Recurrence means infinitely many returns to 0.

**Outcome of this investigation.** No new proof, counterexample, or independently validated exact-scope resolution was obtained in this investigation.

**Remaining.** The exact retained statement remains unresolved in this investigation.

**Primary source:** [Dor Elboim and Gady Kozma: Once-reinforced random walk in high dimensions, 2026](https://arxiv.org/abs/2601.17972). §1.1, pp. 1–2.

### Q2089: Recurrence across strip reinforcements

**Stable ID:** 3eebebdd3e5714daaac5. **Disposition:** unresolved.

**Exact retained statement.** On Z×{1,…,m} with nearest-neighbor edges, is the walk recurrent for every m≥3 and every a>0?

**Supplied setup.** A walk starts at 0. Each undirected edge initially has weight 1, permanently changed to 1+a after its first crossing, a>0. At every discrete step it selects an incident edge proportionally to its current weight. Recurrence means infinitely many returns to 0.

**Outcome of this investigation.** No new proof, counterexample, or independently validated exact-scope resolution was obtained in this investigation.

**Remaining.** The exact retained statement remains unresolved in this investigation.

**Primary source:** [Dor Elboim and Gady Kozma: Once-reinforced random walk in high dimensions, 2026](https://arxiv.org/abs/2601.17972). §1.2, p. 2.

### Q2090: Upper range bound for strong reinforcement

**Stable ID:** 2682e0f19c510a2c0a1b. **Disposition:** unresolved.

**Exact retained statement.** For every d≥2, does some β₀(d)<∞ satisfy Eβ|R_n|=O_{d,β}(n^{d/(d+1)}) for every fixed β≥β₀(d), as n→∞?

**Supplied setup.** On Z^d, start at 0; untraversed edges have weight 1 and traversed edges weight β≥1. Choose the next edge proportionally to weight. Set R_n={X₀,…,X_n}.

**Outcome of this investigation.** No new proof, counterexample, or independently validated exact-scope resolution was obtained in this investigation.

**Remaining.** The exact retained statement remains unresolved in this investigation.

**Primary source:** [Ahmed Bou-Rabee and Yuval Peres: Once-reinforced random walk on Z^d has range exponent at least d/(d+1), 2026](https://arxiv.org/abs/2610.00090). Introduction, pp. 1–2, predicted order preceding Theorem 1.1.

### Q2298: Stochastic advantage of collaborating walks

**Stable ID:** 348fcb55ace5031ea7ed. **Disposition:** disproved.

**Exact retained statement.** For every k≥2, positive integer lifespans t_i, and y>0, is P(|⋃_{i=1}^kR_i(t_i)|≥y)≥P(|R(Σ_it_i)|≥y)?

**Supplied setup.** Let X,X₁,…,X_k be independent copies of the same finite irreducible aperiodic reversible discrete-time Markov chain, all starting independently in its stationary law π. Put R_i(t)={X_i(s):0≤s≤t} and R(t)={X(s):0≤s≤t}.

**Outcome of this investigation.** A seven-state half-lazy reversible birth-death chain with bias ratio r=20 gives P(two stationary three-step ranges cover)/P(one stationary six-step range covers)=87400/160401<1. The ratio tends to zero as r grows.

**Remaining.** No stochastic dominance is claimed from the separate expected-range theorem. Transitive or narrower model classes were not resolved.

**Primary source:** [Partha S. Dey: Daesung Kim and Grigory Terlov, Collaboration of Random Walks on Graphs, arXiv 2023; Proc.AMS153](https://arxiv.org/abs/2302.14241). Question 3.6, p. 11; AssumptionI, pp. 2–3.

### Q2300: Bounded-degree hitting-time anticoncentration

**Stable ID:** c33d47de12875247669d. **Disposition:** unresolved.

**Exact retained statement.** For every fixed integer D≥2, does C_D<∞ exist such that P_x(τ_y=t)≤C_D√(log n)/t for every such G with maximum degree≤D, every x≠y and every integer t≥1?

**Supplied setup.** Let G be a finite connected simple graph with n≥2 vertices, X its nonlazy simple random walk started at x, and τ_y=inf{t≥0:X_t=y}.

**Outcome of this investigation.** The exact source model was checked; no proof or counterexample was obtained.

**Remaining.** The retained hitting-time anticoncentration question remains unresolved.

**Primary source:** [Rafael Chiclana: Nonconcentration of hitting times for random walks on graphs](https://arxiv.org/abs/2605.17513). Introduction after Proposition 1.4, p. 2; Remark7.2.

### Q2393: Limit constant for common planar orders

**Stable ID:** 9d7cf007609c71b6670d. **Disposition:** unresolved.

**Exact retained statement.** Independently sample two lists of n iid uniform points in [0,1]², labeled [n], inducing coordinatewise partial orders. Let C_n be the largest label subset on which the two orders agree. Is E C_n∼c n^(1/3) for some c∈(0,∞)?

**Outcome of this investigation.** No new proof, counterexample, or independently validated exact-scope resolution was obtained in this investigation.

**Remaining.** The exact retained statement remains unresolved in this investigation.

**Primary source:** [David Aldous: Some Open Problems](https://www.stat.berkeley.edu/~aldous/Research/OP/problems_old.pdf). §2 Example 4, pp. 5–6.

### Q2394: Asymptotic optimal online tree cost

**Stable ID:** 68e22605cbc1c800dc5b. **Disposition:** unresolved.

**Exact retained statement.** Does c_n converge as n→∞, and what is its limit?

**Supplied setup.** Edges of K_n, with iid Uniform[0,1] costs, arrive in independent uniformly random order. On seeing each edge and cost, an online policy irrevocably accepts or rejects it, ultimately selecting a spanning tree. Let c_n be the infimum expected total cost over all such policies.

**Outcome of this investigation.** No new proof, counterexample, or independently validated exact-scope resolution was obtained in this investigation.

**Remaining.** The exact retained statement remains unresolved in this investigation.

**Primary source:** [David Aldous: Omer Angel and Nathanaël Berestycki, Online Random Weight Minimal Spanning Trees and a Stochastic Coalescent](https://www.stat.berkeley.edu/~aldous/Research/OP/Beres2008.pdf). Introduction, pp. 1–2; author problem page.

### Q2395: Stationary law of the drift-jump system

**Stable ID:** c7b23369c6f031f11c93. **Disposition:** partial.

**Exact retained statement.** Give an explicit description of the unique stationary distribution of this infinite particle system.

**Supplied setup.** For each k, particles 0<X₁<⋯<X_k obey dX_i/dt=X_i. At every point (x,t) of a unit-intensity Poisson process on (0,∞)², move the nearest particle strictly right of x to x, if one exists. The k-particle laws form a consistent infinite system.

**Outcome of this investigation.** A complete constructive finite-dimensional stationary law is given by Poissonized Plancherel growth and an explicit nonnegative skew-tableau sum, with a Poisson-tail error bound at computable thresholds.

**Remaining.** A compact all-particle joint density, general gap factorization, or finite multipoint determinant has not been established. Registry status is deliberately conservative.

**Primary source:** [David Aldous: A one-dimensional drift-jump particle process](https://www.stat.berkeley.edu/~aldous/Research/OP/left_Hamm.html). Problem paragraph and preceding two paragraphs.

### Q2396: Concavity under recursive overlap

**Stable ID:** adf6fb6ae4ba18aaf563. **Disposition:** partial.

**Exact retained statement.** Is H_n concave on [0,1] for every such sequence and every n≥1?

**Supplied setup.** For integers 2=a₁<a₂<⋯, put P₁(p)=(p,1−p), P_{n+1}(p)=p(P_n(p),0,…,0)+(1−p)(0,…,0,P_n(p)) in R^{a_{n+1}}. Set H_n(p)=−Σ_jP_{n,j}(p)log P_{n,j}(p), with 0log0=0.

**Outcome of this investigation.** Strict entropy concavity is proved for every four positive real weights by an exhaustive exact computer-assisted proof; one to three weights have elementary proofs. Arbitrarily large separated blocks of at most four also satisfy concavity.

**Changed assumptions for the stated partial result.** The universal-n target is restricted to n<=4, or to a specified injectively encoded separated-block class. Within the n=4 theorem the weight domain is enlarged from positive integers with w_1=1 to arbitrary positive real weights.

**Remaining.** General interior concavity for n>=5 remains unresolved. The certificate is not a kernel-checked formal proof.

**Primary source:** [Jörg Neunhäuserer: Recursive overlap Bernoulli distributions and an entropy concavity conjecture, v2](https://arxiv.org/abs/2609.05546). Conjecture 3.1, p. 3.

### Q2397: Uniform dependence on greedy-walk start

**Stable ID:** c01e8789e7f81d3f949c. **Disposition:** disproved.

**Exact retained statement.** Is sup_G max_v L(G,v)/min_v L(G,v)<∞, over all such graphs with at least two vertices?

**Supplied setup.** For a finite connected positively weighted graph, use shortest-path distance d. Assume unique choices. Starting at v, repeatedly go to the nearest unvisited vertex; L(G,v) is total distance until all vertices are visited, without returning. Random models below start uniformly over vertices.

**Outcome of this investigation.** Explicit positive weighted trees of degree at most three have a start ratio growing as h/4 with n=2^(h+1)-1. An explicit rational perturbation makes all pair distances distinct. A general harmonic upper bound proves worst-case order Theta(log N).

**Remaining.** No sharp leading constant for the maximum start ratio is claimed; no historical-priority claim is made.

**Primary source:** [David Aldous: The Nearest Unvisited Vertex Walk on Random Graphs, v2](https://arxiv.org/abs/1912.13175). Problem 4, p. 8.

### Q2398: Planar-grid greedy-walk law of large numbers

**Stable ID:** eceb66c01f9008e57d1f. **Disposition:** unresolved.

**Exact retained statement.** For G_m the m×m nearest-neighbor grid with iid Exponential(1) edge lengths, does m^(−2)L(G_m,V) converge in probability to a deterministic constant?

**Supplied setup.** For a finite connected positively weighted graph, use shortest-path distance d. Assume unique choices. Starting at v, repeatedly go to the nearest unvisited vertex; L(G,v) is total distance until all vertices are visited, without returning. Random models below start uniformly over vertices.

**Outcome of this investigation.** No new proof, counterexample, or independently validated exact-scope resolution was obtained in this investigation.

**Remaining.** The exact retained statement remains unresolved in this investigation.

**Primary source:** [David Aldous: The Nearest Unvisited Vertex Walk on Random Graphs, v2](https://arxiv.org/abs/1912.13175). §4.1, after Corollary 6, p. 11.

### Q2489 (provisional): Gaussian fluctuations of Euclidean greedy length

**Stable ID:** 744730a8db774c763294. **Disposition:** unresolved.

**Exact retained statement.** For n iid uniform points in [0,1]² with Euclidean distances, does L_n−E L_n converge in distribution to N(0,σ²) for some σ>0?

**Supplied setup.** From a uniformly chosen point among n iid uniform points in [0,1]², repeatedly move to the nearest unvisited point in Euclidean distance. Let L_n be total length until all points are visited, without returning.

**Outcome of this investigation.** No new proof, counterexample, or independently validated exact-scope resolution was obtained in this investigation.

**Remaining.** The exact retained statement remains unresolved in this investigation.

**Primary source:** [David Aldous: The Nearest Unvisited Vertex Walk on Random Graphs](https://arxiv.org/abs/1912.13175). §3, after equation4, pp. 9–10.

### Q2492 (provisional): Critical branching minimum escape

**Stable ID:** d52b689e2ce17ee9a73f. **Disposition:** unresolved.

**Exact retained statement.** For 0<λ<d and m=(d+λ)/(2√(λd)), determine the sublinear asymptotic escape rate of L_n.

**Supplied setup.** Let T be a Galton–Watson tree with offspring law p, p₀=0, finite mean>1 and d=min{k:p_k>0}≥2. Independently, each particle has offspring law μ with μ₀=0 and finite mean m>1. Start one particle at the root; each child moves to its parent with probability λ/(λ+k), or to each of k children with probability 1/(λ+k); at the root choose a child uniformly. Let L_n be the minimum root-distance in generation n.

**Outcome of this investigation.** No new proof, counterexample, or independently validated exact-scope resolution was obtained in this investigation.

**Remaining.** The exact retained statement remains unresolved in this investigation.

**Primary source:** [Julien Berestycki; Nina Gantert; David Geldbach; Quan Shi: Biased branching random walks on Bienaymé–Galton–Watson trees](https://arxiv.org/abs/2502.07363). §2.9(v), p. 27; Theorem 1.3.

### Q2498 (provisional): Directional zero-one law for bounded cookies

**Stable ID:** 34cba2e1eafff79891a2. **Disposition:** unresolved.

**Exact retained statement.** If some deterministic M makes ω(x,e,i)=1/(2d) for all i>M, must P_0(X_n·ℓ→+∞)∈{0,1} for every nonzero ℓ?

**Supplied setup.** On Z^d, d≥2, iid stacks (ω(x,e,i))_{e,i} specify the nearest-neighbor jump distribution on the ith visit to x. Assume a deterministic κ>0 bounds every ω(x,e,i) below. The walk starts at zero; P_0 is annealed.

**Outcome of this investigation.** The ordinary fixed-environment RWRE candidate theorems do not apply to visit-indexed cookie stacks.

**Remaining.** The original cookie question remains unresolved in this investigation.

**Primary source:** [Elena Kosygina; Martin P. W. Zerner: Excited random walks: results, methods, open problems](https://www.math.uni-tuebingen.de/user/zerner/pub/KosyginaZerner.pdf). Problem 3.20, p. 16 preprint / p. 127 journal.

### Q2499 (provisional): Recurrence–transience dichotomy for cookie walks

**Stable ID:** 3a9c8d8a68e36d9511bf. **Disposition:** unresolved.

**Exact retained statement.** Without bounding the number of cookies, must either every vertex be visited infinitely often almost surely, or every vertex be visited only finitely often almost surely?

**Supplied setup.** On Z^d, d≥2, iid stacks (ω(x,e,i))_{e,i} specify the nearest-neighbor jump distribution on the ith visit to x. Assume a deterministic κ>0 bounds every ω(x,e,i) below. The walk starts at zero; P_0 is annealed.

**Outcome of this investigation.** The ordinary fixed-environment RWRE candidate theorems do not apply to visit-indexed cookie stacks.

**Remaining.** The original cookie question remains unresolved in this investigation.

**Primary source:** [Elena Kosygina; Martin P. W. Zerner: Excited random walks: results, methods, open problems](https://www.math.uni-tuebingen.de/user/zerner/pub/KosyginaZerner.pdf). Problem 3.21; Definition 3.1.

## 9. Reproducibility, computation protocol, and evidence limits

Unpack the verification archive and run the following from its top-level directory:

~~~bash
python3 verify.py
~~~

The runner first validates the SHA-256 manifest. It copies the computational subdirectories to a temporary working directory inside the unpacked archive and executes the checks there, preserving the archived inputs and outputs. It also repeats the pinned formal-source import and placeholder scan. The latter is explicitly a static check: the runner does not install Lean, download Mathlib, or claim to compile a formal proof.

| Calculation | Declared domain or budget | Independent controls and actual execution |
|---|---|---|
| Structural dependency coverage | Every lag set with 2≤M≤12: 4,094 sets, plus four M=16 examples | Direct cone recurrence, Boolean matrix powers, and Apéry thresholds agree; persistence, bounds, and optimum checks passed. |
| Grouped sampling | Two explicit fixed maps on 16 inputs and 8 outputs; curves through K=8; every group sequence through K=6 | Exact rational formula, exhaustive union enumeration, equal-cost iid-input control, and K=2 variance identity passed. |
| Q946 supplement | m=3,4,5,6,8,10,20,50,100,200; n=m^m defined symbolically | Evaluates proved bounds without instantiating huge chains. Floating displays are explanatory, not an interval certificate. |
| Q2298 | Seven states, two three-step stationary walks versus one six-step walk | Rational visited-set dynamic programming and a separate complete-path implementation agree. The latter enumerates 149 three-step and 3,387 six-step paths. A further peer check is included. |
| Q2397 | Explicit tree heights 1–8, hence 3–511 vertices | Recursive and independent flat-spine constructions agree. Both start orders, exact lengths, uniqueness, and perturbation preservation passed. |
| Q2396 classification | 25 possible collision hyperplanes; independent bases of sizes 0–3 | Exact row-space and positive-polytope calculation: 522 spaces, 216 positive realizable spaces, 23 entropy patterns. |
| Q2396 curvature | All 23 patterns on [0,1/2], with endpoint normalization and reflection | Outward integer/rational interval proof: 130 terminal boxes, every upper bound negative, largest dyadic denominator 64 for parameter intervals. |
| Q2395 | Every permutation through size 7; partition sizes through 12; explicit one- and two-threshold examples | 5,914 direct RSK calculations, 195 normalized growth rows, independent skew counts, Poisson normalization, exact event coefficients and analytic error bounds passed. |
| RWRE candidate audit | Fixed commit and complete reachable OAI source closures | Retrieved and hashed 585 files in the union; exact comparator-model prefixes checked. No local compilation or kernel verification. |

All finite proof decisions use exact integers or rational numbers. No Monte Carlo estimate or random seed is used in these checks. The optional exploratory entropy script uses NumPy and is explicitly excluded from the proof chain and the offline verification runner.

### Experimental specification

For dependency coverage, the observable is the structural ancestor bitset, the loss is first failure to cover all initial coordinates, and the resource is the time index. The generator exhausts every lag set in the stated range. The separate functional example over the two-element field observes actual coefficients, exposing cancellations that structural ancestry cannot detect.

For grouped coverage, the generator independently resets a uniformly selected group of four inputs; the fixed map is retained across resets. The observable is its target image set, loss is the uncovered target fraction, and resource is exactly 4K map evaluations. Controls use 4K iid uniform individual inputs through each same map. Both maps and all rational per-target probabilities are supplied. These examples do not purport to reconstruct the unprovided Inquiry 27 compression function or datasets.

For the finite Markov counterexample, the full transition matrix, exact stationary distribution, positive-probability paths, lifespan, target tail event, and expectations are recorded. For the greedy example, the complete finite edge lists, binary perturbation rule, designated starts, and all selected-vertex orders are recorded. The universal conclusions in both cases follow from the written proofs, not extrapolation from the finite checks.

### Archive contents and provenance

The archive includes the original supplied handoff, the complete report and ledger, all scripts cited here, computational inputs and raw outputs, certificate data, independent reviews, the verifier, and a SHA-256 manifest. It retains the pinned OpenAI source and manuscripts under the accompanying Apache 2.0 license. Other external papers are cited by URL and location; their downloaded PDF hashes are retained where applicable, and their complete texts are not redistributed.

The verified computational subprojects require only the Python standard library. Source-fetching scripts are preserved for provenance but are not run by the offline verifier. The pinned Lean toolchain and Mathlib revision are recorded for a future full build; the source archive is not represented as a complete installed Lean environment.

The checked mathematics has several separate trust levels. Ordinary proofs can be assessed from the report. Exact finite calculations require the supplied code and data, whose critical logic was reviewed; a rerun reproduces those calculations. Independent implementation was used for both finite counterexample families where practical. Source comparison does not independently validate the mathematical result asserted by a third-party manuscript. No result in this report is labelled as a compiled formal theorem.

## 10. Research directions made concrete by these results

1. **Refine the repeated-cover bound after Q946.** The false universal constant must be replaced by a dimension-dependent factor. The constructed family forces order at least log n / loglog n, while the cited general upper estimate loses log n. A useful next target is to close this gap or identify a natural nonreversible class that excludes the residence-block obstruction. The reversible case is outside the counterexample's scope.

2. **Study stochastic collaboration under narrower symmetries.** Q2298 fails even with reversibility and half-laziness, and its multiplicative tail advantage can tend to zero on seven states. The counterexample uses highly nonuniform stationary mass. Vertex-transitive or other balanced cases require a separate argument. The proved first-moment comparison remains useful for the program's expected-coverage objective.

3. **Extend the entropy classification or find a structural curvature inequality.** Every positive four-weight pattern is settled, and any counterexample for a fixed larger vector must lie away from both parameter endpoints. Five weights are a concrete next finite classification target. A proof valid for arbitrary collision partitions induced by positive subset sums would be more informative than a rapidly expanding case computation.

4. **Optimize lag layouts under the actual engineering restrictions.** The unrestricted fixed-cardinality optimum is explicit. If lag 1 is excluded, certain taps are forbidden, or an update rule has cancellations, the objective and constraints must be stated anew. The Boolean companion and Apéry formulations provide exact oracles against which constrained constructions can be tested.

5. **Measure or prove per-target balance in Inquiry 27.** Record the fixed map, group generator, reset rule, and per-target hit probabilities. The variance identity gives an exact two-round diagnostic; the Taylor bound converts a uniformity estimate into a quantitative multi-round coverage guarantee. Without those inputs the original experiment cannot be certified.

6. **Complete the candidate RWRE verification at its pinned revision.** Build the actual solution modules with the recorded Lean and Mathlib versions, inspect the resulting theorem types and allowed axioms, and finish the specified analytic checkpoints. The bounded source audit provides a reproducible starting point. Its cookie and pathwise-random-direction scope exclusions remain essential even if those two ordinary RWRE theorems are verified.

7. **Clarify the desired explicitness for Q2395.** The finite-dimensional series already gives certified evaluations and a sampling construction. A compact joint density, multipoint determinant, or useful gap description would address a stronger interpretation of the original question. The report does not conflate those prospective formulas with the construction already obtained.

The remaining catalog members are preserved in the exact statement register. No unsupported transfer from a neighboring walk model is used to close them.
