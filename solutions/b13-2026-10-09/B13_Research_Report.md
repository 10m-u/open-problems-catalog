# B13 — Research report and exact-statement decisions

Prepared 9 October 2026 UTC from the attached handoff, snapshot 8 October 2026.

## Outcome

This return gives **six complete resolutions of the 30 tracked questions: five proved and one disproved**. It also gives **partial results for six further questions**. The remaining 18 are unresolved in this return.

The complete resolutions are Q1291 (signed-shuffle cutoff), Q1589 (a counterexample to the specified exclusion profile), Q1895 (a Gaussian limit for Sukhatme fixed points), Q2662 (the minimum perfect-matching-scheme gap), Q2664 (repeated-surjection whirling), and Q2665 (real slab-toggle homomesy). The explicit slab coboundary gives the stronger uniform error bound
\[
\left|\frac1N\sum_{t=0}^{N-1}\sum_i(T_\pi^t x)_i-\frac n2\right|
\le \frac{n-r}{2N}.
\]

The partial questions are Q1290, Q1896, Q2290, Q2293, Q2303, and Q3205. Each restriction and remaining quantifier is stated below. In particular, three polynomial-time semigroup subclasses are counted as partial progress on the single multi-part Q3205, not as three additional complete resolutions.

The supplemental Inquiry 30 now has an explicit carry-boundary obstruction: its base pair walk has
\[
t_{\rm mix,pair}(1/4)\ge
\left(\frac{\sqrt{2\pi}}8+o(1)\right)2^w\sqrt w,
\]
despite generating the full symmetric group at every width. Its additive reversibilization has gap at most \((4+o(1))/(w2^w)\). The original nonreversible eigenvalue-modulus asymptotics remain unproved. The numerical hypotheses in this report are explicitly separate from those theorems.

## Reading and evidence conventions

- Sections 1–5 contain the complete proofs or counterexample.
- Sections 6–9 contain shuffle, cycle-count, and semigroup partial results.
- Section 10 contains Inquiry 30 and the hypergraph/Brownian-energy partial results.
- The final register reproduces every original question and stable ID, including the provisional number Q2494.
- The accompanying JSON ledger is the machine-readable decision record. The verification ZIP includes this full report, the ledger, the original input, component proofs, scripts, exact certificates, raw outputs, separate agent audit notes, replay instructions, and an internal SHA-256 manifest.

A proof may import a precisely stated primary theorem. The proof text names every such dependency. The algebraic identities and asymptotic arguments supplied here are written proofs, not compiled formal theorems. Separate agent reviews checked the principal arguments; they are not external peer review. Exact finite certificates, bounded floating-point calculations, and Monte Carlo diagnostics are labeled separately. None of the latter is used as a substitute for an all-parameter argument.

The conclusions are about the handoff's retained mathematical statements. No claim of publication priority is made. In particular, known restricted source theorems are not relabeled as solutions of broader questions, and the withdrawn general exclusion-profile argument is not used.

## Decision table

| Question | Stable statement ID | Decision | Result at the retained scope |
|---|---|---|---|
| Q1285 | 901c05b15569f039ac00 | **unresolved** | No new exact-scope result established in this return. |
| Q1286 | cc2c43f786837e4b7aa2 | **unresolved** | No new exact-scope result established in this return. |
| Q1290 | dd1e1530c8b22bbf943a | **partial** | Separation cutoff proved for every fixed 0<alpha<1; alpha>1 remains unresolved. |
| Q1291 | cc27e5d9e60fdad839fa | **proved** | Total-variation cutoff at tau_n log n for every fixed real alpha, including the full requested nonzero range. |
| Q1405 | 2f935b9be6f6cf5e6ab9 | **unresolved** | No new exact-scope result established in this return. |
| Q1406 | db6847d81b588f311dee | **unresolved** | No new exact-scope result established in this return. |
| Q1407 | f360f758c8bcd6664901 | **unresolved** | No new exact-scope result established in this return. |
| Q1408 | 85e1bb57b7e9ea21e1fe | **unresolved** | No new exact-scope result established in this return. |
| Q1492 | 93a2d63b2ddcbb351782 | **unresolved** | No new exact-scope result established in this return. |
| Q1493 | 543094642ca56218b341 | **unresolved** | No new exact-scope result established in this return. |
| Q1494 | b5ad443ffe0eac2e6b5c | **unresolved** | No new exact-scope result established in this return. |
| Q1589 | b8d510fafe6e359a7aa3 | **disproved** | The proposed unweighted-count Gaussian profile is false: p=1/2, q=1/4 gives a strictly larger sine-statistic TV lower bound. |
| Q1895 | 4faaafa325700071ea75 | **proved** | (F_n-(log n)/e)/sqrt((log n)/e) converges in distribution to N(0,1); E F_n=(log n)/e+O(1). |
| Q1896 | 25f5bc9a09e2c4ffa329 | **partial** | C_n>=(1-o_P(1))log n; E C_n>=log n-O(1); limsup E C_n/(log n)^2<=1/2. No limiting distribution. |
| Q1897 | c0e5e644929150cddbda | **unresolved** | No new exact-scope result established in this return. |
| Q2198 | 9e2e29797ab8b0f064b5 | **unresolved** | No new exact-scope result established in this return. |
| Q2290 | cb376eb93c0b5497e6fb | **partial** | Gap equality for hyperedges restricted to pairs and the full vertex set, including every n<=3 instance. |
| Q2291 | 576df523032c0668f39e | **unresolved** | No new exact-scope result established in this return. |
| Q2292 | 3430a4c6c2d41614aa1a | **unresolved** | No new exact-scope result established in this return. |
| Q2293 | 6e840638a5684077278e | **partial** | Common positive edge weights on the complete graph: gap=c sum(alpha), attained in degree one for all positive alpha. |
| Q2303 | 1bc2b2da7b69544e14b9 | **partial** | Usable-support reduction, abelian obstruction and exact count-flow relaxation; exact classification on usable forests. |
| Q2494 | 20d1798f558ecef53b7b | **unresolved** | No new exact-scope result established in this return. |
| Q2529 | 3f09875aa32e6fb5d8a6 | **unresolved** | No new exact-scope result established in this return. |
| Q2601 | 22c5b3891653baeb4e4b | **unresolved** | No new exact-scope result established in this return. |
| Q2602 | 308eab8632988c80391e | **unresolved** | No new exact-scope result established in this return. |
| Q2603 | b51b1715c73663fb2403 | **unresolved** | No new exact-scope result established in this return. |
| Q2662 | 3aaf2060b2cc3217f8e1 | **proved** | Every nonidentity perfect-matching relation has adjacency gap at least 2n-1 for all n>=5. |
| Q2664 | 3f3121a42f7e5c02851a | **proved** | Every repeated-surjection whirling orbit has each fibre average n/k, proved by an explicit coboundary. |
| Q2665 | 39dd68d5345401fd90b1 | **proved** | Every real slab orbit has average n/2, with uniform error <=(n-r)/(2N). |
| Q3205 | ee813378b94c439e788a | **partial** | Deterministic P for inverse, completely regular, and aperiodic semigroups; aperiodic positive instances have constructive certificates. |


---

## 1. B13 / Q1291 — biased signed transpositions have cutoff

Stable statement ID: `cc27e5d9e60fdad839fa`.

**Decision: proved**, at the exact scope of the handoff. Evidence: written argument with an explicitly identified published/dissertation theorem as a dependency. No compiled formal theorem is claimed.

### Statement

Fix any real number \(\alpha\). Write
\[
S_a(n)=\sum_{j=1}^n j^a,\qquad
\tau_n=\begin{cases}S_\alpha(n)/n^\alpha,&\alpha\le1,\\
S_\alpha(n)/S_{\alpha-1}(n),&\alpha>1.
\end{cases}
\]
At each discrete step choose \(j\) with probability \(j^\alpha/S_\alpha(n)\), choose \(i\) uniformly from \([j]\), and transpose the two cards. Independently toss a fair coin; on one outcome flip the signs of both cards if \(i<j\), and flip the one selected card if \(i=j\). This walk on \(B_n\) has worst-case total-variation cutoff at \(\tau_n\log n\).

The argument also includes \(\alpha=0\), though the question excludes that already-known case. The bias remains fixed as \(n\to\infty\).

### Dependency: unsigned cutoff

Matheau-Raven, *Random walks on the symmetric group: cutoff for one-sided transposition shuffles* (2020), Theorem 3.6.6, establishes total-variation cutoff for the unsigned projection for every fixed real \(\alpha\), with this same \(\tau_n\). In particular, writing its distance as \(d_n^S\),
\[
\lim_{c\to\infty}\limsup_{n\to\infty}
d_n^S(\lfloor\tau_n(\log n+c)\rfloor)=0,
\]
and for every fixed \(\epsilon>0\),
\(d_n^S(\lfloor(1-\epsilon)\tau_n\log n\rfloor)\to1\).

Primary source: <https://etheses.whiterose.ac.uk/id/eprint/28076/1/OMatheauRavenThesis.pdf>, Theorem 3.6.6, printed pp. 84–85; signed question Conjecture 4.4.4, pp. 130–131. The source was inspected directly. The remainder of the argument below establishes the required transfer to signs.

### Lemma 1: conditional sign uniformity

Fix the complete sequence of selected position pairs through time \(t\). Let \(\mathcal G_t\) be the undirected graph on the initial labels \([n]\), obtained by placing an edge between the two *positions* whenever an off-diagonal pair is selected. Record a loop when a diagonal pair is selected. If \(\mathcal G_t\) is connected and at least one loop is recorded, then the final sign vector, conditional on this sequence, is uniform on \(\mathbb F_2^n\).

**Proof.** Identify signs with bits attached to the original card labels. Each fair coin contributes an independent uniform multiple of \(e_a+e_b\), where \(a,b\) are the labels currently at the selected distinct positions, or of \(e_a\) for a diagonal selection. Conditional on the position history, all these vectors are deterministic, and the resulting sum is uniform on their linear span.

The connected components of the graph of label interactions coincide, as sets of initial labels, with those of the position-interaction graph. Initially this is true for singleton components. At any step, every label occupying a position in a component belongs to that component; an edge within a component preserves this fact, and an edge across components merges precisely those two components in both descriptions. This proves the assertion by induction. A loop anchors one label in its component, and that anchor is retained under subsequent mergers.

For a connected graph, its vectors \(e_a+e_b\) span the even-parity subspace: summing vectors along a path produces \(e_a+e_b\) for any two vertices. One loop vector \(e_a\) extends this span to all of \(\mathbb F_2^n\). This proves the lemma. More generally, full span holds if every component has a loop. \(\square\)

If \(d_n^B\) is signed total variation, Lemma 1 implies
\[
d_n^S(t)\le d_n^B(t)
\le d_n^S(t)+\Pr(\mathcal G_t\text{ disconnected})
+\Pr(\text{no diagonal selection by }t).                 \tag{1}
\]
For the upper bound, condition on the history, and replace the signs by an independent uniform vector only on the bad event. On the good event the signs are already conditionally uniform. The modified law is the unsigned marginal times uniform signs; changing the bad part costs at most its probability. This handles any dependence between the graph event and the final unsigned permutation. The lower bound is the projection inequality for total variation.

### Lemma 2: cut estimates

Set \(r_j=j^{\alpha-1}/S_\alpha(n)\); the probability of the unordered choice \(\{i,j\}\), with \(i\le j\), is \(r_j\). For a set \(A\subset[n]\) of size \(k\le n/2\), let
\[
q(A)=\sum_{i\in A,\ j\notin A}r_{\max(i,j)}.
\]
There are constants \(C=\max(1,\alpha)\) and \(b_\alpha>0\), independent of \(n,A\), such that
\[
q(A)\ge \frac{k}{\tau_n}\left(1-\frac{Ck}{n}\right),
\qquad q(A)\ge b_\alpha\frac{k}{\tau_n}.                \tag{2}
\]
One can take \(b_\alpha=1/2\) if \(\alpha\le1\) and \(b_\alpha=4^{-\alpha}\) if \(\alpha>1\).

**Proof for \(\alpha\le1\).** Every edge has probability at least
\(r_n=1/(n\tau_n)\). There are \(k(n-k)\) cut edges, giving both estimates.

**Proof for \(\alpha>1\).** The total probability of selections incident to vertex \(i\), including its loop once, is
\[
d_i=i r_i+\sum_{j>i}r_j\ge\sum_{j=1}^n r_j=\tau_n^{-1},
\]
since \(r_j\) is increasing. The sum of these incident probabilities over \(A\) counts internal edges twice and its loops once. Their combined contribution is at most \(k^2r_n\). Thus
\[
q(A)\ge k/\tau_n-k^2r_n.
\]
Moreover,
\[
\tau_n r_n=\frac{n^{\alpha-1}}{S_{\alpha-1}(n)}\le\frac\alpha n,
\]
using \(S_{\alpha-1}(n)\ge\int_0^n x^{\alpha-1}\,dx=n^\alpha/\alpha\). This gives the first inequality.

At most \(kn/4\) cut pairs have both endpoints below \(n/4\). Since the cut contains at least \(kn/2\) pairs, at least \(kn/4\) of its pairs satisfy \(\max(i,j)\ge n/4\). On these pairs,
\[
\tau_n r_{\max(i,j)}\ge
\frac{(n/4)^{\alpha-1}}{S_{\alpha-1}(n)}
\ge\frac{4^{1-\alpha}}n,
\]
where \(S_{\alpha-1}(n)\le n^\alpha\). Multiplication gives the second inequality. \(\square\)

### Lemma 3: the graph is connected by the cutoff upper window

For every fixed \(c\ge0\), at \(t=\lfloor\tau_n(\log n+c)\rfloor\),
\[
\limsup_{n\to\infty}\Pr(\mathcal G_t\text{ disconnected})
\le \exp(e^{-c})-1.                                    \tag{3}
\]

**Proof.** A disconnected graph has a nonempty component \(A\) of size at most \(n/2\), so a union bound gives
\[
\Pr(\mathcal G_t\text{ disconnected})
\le\sum_{k=1}^{\lfloor n/2\rfloor}\binom nk
\exp\bigl(-t\min_{|A|=k}q(A)\bigr).                    \tag{4}
\]
Here the independent draws give probability \((1-q(A))^t\le e^{-tq(A)}\) for a cut to remain empty. In both bias ranges \(\tau_n\to\infty\), so rounding changes \(t/\tau_n\) by \(o(1)\).

Split the sum into three ranges. For \(k\le n/(\log n)^2\), the first estimate in (2), together with \(\binom nk\le n^k/k!\), bounds the summand by
\[
\frac1{k!}\exp[-(c-o(1))k],
\]
with uniform \(o(1)\). Summing this bound yields \(\exp(e^{-c+o(1)})-1\).

For \(n/(\log n)^2<k\le n/(2C)\), the same estimate gives \(q(A)\ge k/(2\tau_n)\), while
\(\log\binom nk\le k\log(en/k)\le k(1+2\log\log n)\).
Thus this range has total at most
\(n\exp[-\tfrac14(n/(\log n)^2)\log n]\) for all sufficiently large \(n\), which tends to zero. For \(n/(2C)<k\le n/2\), if this range exists, use the second estimate in (2). Its contribution is at most
\[
2^n\exp[-b_\alpha n(\log n+c-o(1))/(2C)]\to0.
\]
This proves (3). \(\square\)

### Completion

The probability of a diagonal selection in one step is
\(\ell_n=S_{\alpha-1}(n)/S_\alpha(n)\ge1/\tau_n\).
For \(\alpha>1\) there is equality; for \(\alpha\le1\), use
\(S_{\alpha-1}(n)\ge n\,n^{\alpha-1}=n^\alpha\). Consequently,
\[
\Pr(\text{no diagonal selection by }t)
\le e^{-t/\tau_n}=n^{-1}e^{-c+o(1)}\to0.
\]
Combining (1), (3), and the unsigned upper bound proves
\[
\lim_{c\to\infty}\limsup_{n\to\infty}
d_n^B(\lfloor\tau_n(\log n+c)\rfloor)=0.
\]
The unsigned lower bound transfers through (1). Therefore the signed walk has cutoff at \(\tau_n\log n\) for every fixed \(\alpha\), proving Q1291. This proof establishes the additive upper window requested by the source conjecture; it does not claim an optimal cutoff window or a full limiting profile.

### Verification scope

The proof is asymptotic and does not depend on computation. `verify_signed_graph.py` exhaustively checks the conditional-span lemma on all pair histories of length at most six for \(n=3\), and checks both cut inequalities on every nonempty cut of size at most half the vertices for \(2\le n\le12\) and the explicitly listed biases. These are controls on the reasoning, not replacements for the proof. The exact history checks use integer bit arithmetic. The cut checks use floating-point power evaluations and are explicitly labeled numerical.


---

## 2. B13 / Q1589 — counterexample to the specified exclusion profile

Stable statement ID: `b8d510fafe6e359a7aa3`.

**Decision: disproved**, at the exact scope of the handoff. The counterexample uses the permitted fixed densities \(p=1/2,q=1/4\). Evidence: written argument plus the stationary fluctuation theorem identified below. No numerical estimate or withdrawn theorem is needed.

### What fails

The stated definition of \(f_{pq}\) uses the **unweighted total particle count** \(S(\eta)=\sum_i\eta_i\). That normalization produces a Gaussian shift strictly smaller than the shift detected by another observable. Hence it cannot equal the worst-case total-variation profile. This is a counterexample to the precise proposed formula; it is not a disproof of cutoff or of every possible Gaussian profile with a different constant.

The original source uses this same unweighted statistic: Tran's thesis, equation (2.8) and Conjecture 2, printed p. 20; \(S\) is defined on p. 18. Primary source: <https://www.unige.ch/~tranh/these-version-240521.pdf>.

### 1. Exact stationary means and covariances

Put \(L=N+1\), \(u_i=i/L\), and take rates exactly as in the question. The stationary mean is
\[
\rho_i=p+(q-p)u_i.
\]
For \(i<j\), its off-diagonal covariance is
\[
\operatorname{Cov}_{\pi_N}(\eta_i,\eta_j)
=-\frac{(p-q)^2 i(L-j)}{L^2(L-1)}.                    \tag{1}
\]
The diagonal variance is \(\rho_i(1-\rho_i)\). These formulas follow by applying the generator to \(\eta_i\) and \(\eta_i\eta_j\): the mean solves the discrete Dirichlet harmonic equation, and the two-site covariance solves the killed two-particle Dirichlet equation with source \(-N^2(\rho_{i+1}-\rho_i)^2\) on adjacent pairs. Substitution verifies (1); uniqueness follows because the finite two-particle absorbing process is eventually killed. This derivation also proves the negative off-diagonal covariances needed below.

Consequently, for bounded continuous \(h\), the variance of
\(N^{-1/2}\sum_i h(u_i)(\eta_i-\rho_i)\) tends to
\[
V(h)=\int_0^1\rho(u)(1-\rho(u))h(u)^2\,du
-(p-q)^2\int_0^1\int_0^1 h(u)G(u,v)h(v)\,du\,dv,       \tag{2}
\]
where \(\rho(u)=p+(q-p)u\) and
\(G(u,v)=\min(u,v)(1-\max(u,v))\), the Green kernel of the negative Dirichlet Laplacian.

The needed **stationary central limit theorem** is Landim–Milanés–Olla, *Stationary and Nonequilibrium Fluctuations in Boundary Driven Exclusion Processes*, Theorem 2.1 and equation (2.4): for smooth Dirichlet test functions, these centered stationary linear statistics converge to a centered Gaussian with variance (2). Primary source: <https://arxiv.org/pdf/math/0608165>; published in *Markov Processes and Related Fields* 14 (2008), 165–184, <https://math-mprf.org/journal/articles/id1149/>. Reflection of the segment interchanges the two reservoir densities if necessary. Replacing their \(N-1\) interior sites by our \(N\) changes no limit. We use the theorem only for \(h(u)=\sin(\pi u)\), which satisfies its Dirichlet smoothness hypotheses.

### 2. A coupling lemma transfers the stationary CLT to the cutoff times

Run \(X_t\) from the all-one state and \(Y_t\) from an independent stationary sample, using the same edge-swap clocks and exactly the same Bernoulli refresh at each boundary event. Monotonicity gives \(X_t\ge Y_t\). The disagreement configuration
\[
D_t=X_t-Y_t\in\{0,1\}^N
\]
is an autonomous SSEP with absorbing, zero-density boundary reservoirs: it swaps at an edge clock and becomes zero at a boundary refresh. Its initial law is \(1-Y_0\), so its distinct-site covariances are nonpositive by (1).

Here is the precise preservation fact. For absorbing SSEP on any finite weighted graph, write \(m_i(t)=\mathbb E D_t(i)\) and \(C_{ij}(t)=\operatorname{Cov}(D_t(i),D_t(j))\), \(i\ne j\). If \(K_2\) is the generator of two exclusion particles killed when either reaches a reset event, then
\[
\partial_t C_{ij}=(K_2 C)_{ij}-c_{ij}(m_i-m_j)^2.        \tag{3}
\]
Indeed, the pair moment evolves by \(K_2\); differentiating \(m_i m_j\) supplies the additional nonnegative term \(c_{ij}(m_i-m_j)^2\). The killed semigroup is positivity preserving. Variation of constants in (3) therefore proves \(C_{ij}(t)\le0\) whenever \(C_{ij}(0)\le0\).

For any nonnegative bounded weights \(h_i\),
\[
\operatorname{Var}\Big(\sum_i h_iD_t(i)\Big)
\le\sum_i h_i^2 m_i(t)
\le\|h\|_\infty^2\sum_i m_i(t).                       \tag{4}
\]
The one-particle killed generator has least positive eigenvalue
\[
\lambda_N=2N^2\left(1-\cos\frac\pi{N+1}\right)
=\pi^2+O(N^{-1}).
\]
Its symmetric semigroup has operator norm \(e^{-\lambda_N t}\), so Cauchy–Schwarz gives
\(\sum_i m_i(t)\le N e^{-\lambda_N t}\).
At the times in the question,
\[
t_N(b)=\frac{\log N}{2\pi^2}+\frac b{\pi^2},
\]
this is \(O_b(\sqrt N)\). Thus (4), divided by \(N\), tends to zero. The weighted disagreement has an asymptotically deterministic value on the fluctuation scale. In particular, the stationary sine-statistic CLT transfers to the law from the all-one state at \(t_N(b)\), with its mean shifted by the expected disagreement. This step does not require a nonequilibrium CLT uniform over growing time intervals.

### 3. Explicit constants at \(p=1/2,q=1/4\)

Here \(\rho(u)=1/2-u/4\), and \(\rho(1-\rho)=1/4-u^2/16\). Define
\[
H_N(\eta)=\sum_{i=1}^N\sin(\pi u_i)\eta_i.
\]
Formula (2) and \((-\Delta_D)^{-1}\sin(\pi u)=\pi^{-2}\sin(\pi u)\) give
\[
\frac1N\operatorname{Var}_{\pi_N}(S)\longrightarrow
V_S=\frac{43}{192},\qquad
\frac1N\operatorname{Var}_{\pi_N}(H_N)\longrightarrow
V_H=\frac{11}{96}-\frac1{64\pi^2}.                    \tag{5}
\]
For example, \(\iint G=1/12\), \(\int u^2\sin^2(\pi u)\,du=1/6-1/(4\pi^2)\), and \(\int\sin^2(\pi u)\,du=1/2\), which directly yield (5).

The mean disagreement solves the killed heat equation from initial profile \(1-\rho_i\). Its first sine coefficient tends to
\[
2\int_0^1(1-\rho(u))\sin(\pi u)\,du=\frac5{2\pi}.
\]
Since \(\sqrt N e^{-\lambda_Nt_N(b)}\to e^{-b}\), spectral expansion gives
\[
\frac{\mathbb E_1S(X_{t_N(b)})-\mathbb E_{\pi_N}S}{\sqrt N}
\longrightarrow \frac5{\pi^2}e^{-b},\qquad
\frac{\mathbb E_1H_N(X_{t_N(b)})-\mathbb E_{\pi_N}H_N}{\sqrt N}
\longrightarrow \frac5{4\pi}e^{-b}.                    \tag{6}
\]
For the sine statistic the first-mode equation is exact. For \(S\), the contribution of all higher modes is bounded in absolute value by \(N e^{-\lambda_{2,N}t}\), and \(\lambda_{2,N}\to4\pi^2\), so it is negligible after division by \(\sqrt N\).

The first limit required in Q1589 therefore forces
\[
f_{1/2,1/4}=A_S:=\frac{5/\pi^2}{\sqrt{43/192}}.
\]
But the normalized sine shift is
\[
A_H:=\frac{5/(4\pi)}{\sqrt{11/96-1/(64\pi^2)}}>A_S.    \tag{7}
\]
The inequality is exact. Squaring reduces it to
\[
43\pi^4-352\pi^2+48>0.
\]
The polynomial \(43z^2-352z+48\) is increasing on \([9,\infty)\) and equals \(363>0\) at \(z=9\); use \(\pi^2>9\).

### 4. The contradiction in total variation

By the stationary CLT and the coupling argument, the variable
\[
Z_N=\frac{H_N-\mathbb E_{\pi_N}H_N}{\sqrt{N V_H}}
\]
converges under stationarity to \(\mathcal N(0,1)\), and under the all-one start at \(t_N(b)\) to \(\mathcal N(A_He^{-b},1)\). Test the event
\(\{Z_N>A_He^{-b}/2\}\). Both limits have continuous distribution functions, so
\[
\liminf_{N\to\infty} d_N(t_N(b))
\ge 2\Phi(A_He^{-b}/2)-1
>2\Phi(A_Se^{-b}/2)-1                              \tag{8}
\]
for every fixed real \(b\), where \(d_N\) is worst-case total variation and \(\Phi\) is the standard normal distribution function. The rightmost expression is exactly the proposed Q1589 profile because its first condition forces \(f=A_S\). This contradicts that assertion and proves Q1589 false.

For orientation only, at \(b=0\) the script reports the two constants and the corresponding strict TV gap. Those decimals are not used in the proof.

### Limits of this result

The proof supplies a lower bound on the true profile, not a matching upper bound. It leaves the correct nonequilibrium profile open. It does not use Joe P. Chen's withdrawn arXiv:2106.03685 argument. The only fluctuation theorem used is the 2006/2008 stationary theorem above, with its exact hypotheses stated.

`verify_exclusion.py` directly solves the stationary finite generators for \(2\le N\le8\) at these rational densities and checks means/covariances and the discrete sine eigenfunction. The all-\(N\) counterexample is the written proof, not that finite computation.


---

## 3. B13 / Q1895: Gaussian limit for Sukhatme fixed points

**Stable statement ID:** `4faaafa325700071ea75`.

**Retained statement:** For the Luce draw-order permutation on `[n]` with weights `n-i+1`, determine a centering, scaling, and nondegenerate limiting distribution for its fixed-point count `F_n`.

**Decision:** proved by the argument below, subject to the standard martingale central limit theorem stated in §5. No change of model or assumptions is made. Evidence: written argument and primary-source comparison; the bounded Monte Carlo diagnostic is supplementary and is not used in the proof. No compiled formal theorem is claimed.

### Theorem

For Sukhatme weights `w_i=n-i+1`,

\[
\boxed{\quad
\frac{F_n-e^{-1}\log n}{\sqrt{e^{-1}\log n}}
\ \xrightarrow[n\to\infty]{\mathrm d}\ \mathcal N(0,1).
\quad}
\tag{1}
\]

Moreover,

\[
\mathbb E F_n=e^{-1}\log n+O(1).
\tag{2}
\]

Thus the requested centering and scale can be taken to be `(log n)/e` and `sqrt((log n)/e)`. The theorem also gives `F_n/log n -> 1/e` in probability. It does not claim a total-variation Poisson approximation or a precise bounded-order correction to the mean.

[Borga–Chatterjee–Diaconis, §1.1 and §5.2](https://arxiv.org/html/2509.07729v2) defines the same weight model and asks for fixed-point asymptotics. Their convention sometimes records the inverse of the draw-order permutation; inversion preserves fixed points, so this convention does not alter the target.

### 1. Exponential clocks and the exact compensator

Take independent variables

\[
T_k\sim\operatorname{Exp}(k),\qquad 1\le k\le n.
\]

Order the clocks from earliest to latest. The next clock among a surviving set `A` has label `k` with probability `k/(sum_{ell in A}ell)`, so this is weighted sampling without replacement. Reversing both the original labels and the original ranks converts the weights `n-i+1` to `k` and the fixed-point condition to

\[
\text{the descending rank of }T_j\text{ is }j.
\tag{3}
\]

All clocks are distinct almost surely. Write their increasing order statistics as

\[
T_{(1)}<\cdots<T_{(n)}.
\]

For `1<=j<n`, define `tau_(n,j)=T_(n-j)`; put `tau_(n,n)=0`. Thus immediately after time `tau_(n,j)`, exactly `j` clocks survive. Define

\[
A_{n,j}=\{k:T_k>\tau_{n,j}\},\qquad
S_{n,j}=\sum_{k\in A_{n,j}}k.
\]

Let `X_(n,j)` indicate that the **next** clock deleted from `A_(n,j)` has label `j`. Condition (3) says precisely

\[
F_n=\sum_{j=1}^n X_{n,j}.
\]

Use the deletion filtration, which reveals clock labels and clock times in increasing order; the chronological stage order is `j=n,n-1,...,1`. By the memoryless property, before the next deletion its conditional success probability is

\[
r_{n,j}:=\mathbb E[X_{n,j}\mid\text{deletion history so far}]
=\mathbf1_{\{j\in A_{n,j}\}}\frac{j}{S_{n,j}}.
\tag{4}
\]

Because `A_(n,j)` consists of exactly `j` distinct positive integers,

\[
S_{n,j}\ge\frac{j(j+1)}2,
\qquad 0\le r_{n,j}\le\frac2{j+1}.
\tag{5}
\]

In particular, the individual fixed-point probability is at most `2/(j+1)`, uniformly in `n>=j`. Put

\[
\mathcal A_n=\sum_{j=1}^n r_{n,j},\qquad
\mathcal M_n=F_n-\mathcal A_n.
\]

The latter is the terminal value of a martingale whose increments have absolute value at most one. Its predictable quadratic variation is

\[
\mathcal V_n=\sum_{j=1}^n r_{n,j}(1-r_{n,j})
=\mathcal A_n+O(1),
\tag{6}
\]

where the error is deterministically bounded, by (5) and convergence of `sum_j 4/(j+1)^2`.

### 2. A summable approximation for the compensator

Set

\[
B_j=\mathbf1_{\{jT_j>1\}},\qquad q=e^{-1}.
\]

The `B_j` are independent Bernoulli variables with parameter `q`, exactly, for every `n`. The main estimate is

\[
\sup_{n\ge1}\sum_{j=1}^n
\mathbb E\left|r_{n,j}-\frac{B_j}{j}\right|<\infty.
\tag{7}
\]

The proof uses only concentration of independent Bernoulli sums. Here are all details, including a uniform quantitative bound.

#### Lemma 2.1: bulk estimate

There is an absolute finite constant `C` such that, for all integers `j>=256` and `n>=4j`, with `s=n/j`,

\[
\mathbb E|jr_{n,j}-B_j|
\le C\left(j^{-1/4}+(s+1)e^{-s/4}\right).
\tag{8}
\]

**Proof.** For a deterministic `y>0`, define

\[
N_j(y)=\sum_{k=1}^n\mathbf1_{\{T_k>y/j\}},\quad
W_j(y)=\sum_{k=1}^n k\mathbf1_{\{T_k>y/j\}},\quad
\mu_j(y)=\mathbb E N_j(y)=\sum_{k=1}^n e^{-ky/j}.
\]

Let `a` be the unique positive solution of `mu_j(a)=j`. This solution exists since `mu_j(0)=n>j` and the function decreases continuously to zero. For `n>=4j` and `j>=256`,

\[
\frac12<a<1.
\tag{9}
\]

Indeed, the infinite geometric sum at `y=1` is less than `j`, giving the upper bound. At `y=1/2`, integral comparison gives

\[
\mu_j(1/2)\ge 2j e^{-1/(2j)}(1-e^{-n/(2j)})>j.
\]

A sharper comparison controls the centering error. The infinite geometric sum differs from `j/a` by a number between zero and one, and its omitted tail is at most `(j/a)e^{-an/j}`. As `mu_j(a)=j`,

\[
0\le1-a\le\frac1j+2e^{-s/2}.
\tag{10}
\]

Put `epsilon=j^{-1/4}<=1/4`. On the interval `[a-epsilon,a+epsilon]`, all arguments lie in `[1/4,5/4]`. On this interval,

\[
-\mu_j'(y)=\sum_{k=1}^n(k/j)e^{-ky/j}\ge c j,
\qquad
\operatorname{Var}N_j(y)\le\mu_j(y)\le4j,
\tag{11}
\]

with an absolute `c>0`: for the derivative lower bound, use the `j` terms `j<=k<2j`, each at least `e^{-5/2}`. Since the expected count crosses `j` with slope at least `cj`, Chebyshev's inequality at the two endpoints gives

\[
\mathbb P\left(\left|j\tau_{n,j}-a\right|>\epsilon\right)
\le\frac{C}{j\epsilon^2}=Cj^{-1/2}.
\tag{12}
\]

To check the stopping-time implication, if `N_j(y)>j`, the process has not yet reached `j` survivors, whereas if `N_j(y)<=j`, that time has already occurred. Equality at a deterministic clock time has probability zero.

For the weighted count, uniformly for `y in [1/4,5/4]`,

\[
\left|\frac{\mathbb E W_j(y)}{j^2}-\frac1{y^2}\right|
\le C\left(j^{-1}+(s+1)e^{-s/4}\right),
\qquad
\operatorname{Var}\left(\frac{W_j(y)}{j^2}\right)\le\frac Cj.
\tag{13}
\]

For completeness, the mean is a Riemann sum for `integral_0^infty x e^{-yx} dx=1/y^2`. The mesh error is `O(1/j)` uniformly because `x e^{-yx}` has uniformly bounded total variation on this interval of `y`. Its omitted tail is at most a constant times `(s+1)e^{-s/4}`. The variance bound follows from independence and

\[
\sum_{k\ge1}k^2e^{-k/(4j)}=O(j^3).
\]

Combining (10), (13), and Cauchy–Schwarz gives, for `y=a-epsilon` and for `y=a+epsilon`,

\[
\mathbb E\left|\frac{W_j(y)}{j^2}-1\right|
\le C\left(j^{-1/4}+(s+1)e^{-s/4}\right).
\tag{14}
\]

On the event in which the stopping time lies between these two deterministic endpoints,

\[
W_j(a+\epsilon)\le S_{n,j}\le W_j(a-\epsilon).
\]

Moreover `S_(n,j)/j^2 >= 1/2` always by (5). Hence its reciprocal satisfies

\[
\left|\frac{j^2}{S_{n,j}}-1\right|
\le 2\left|\frac{S_{n,j}}{j^2}-1\right|,
\qquad
\left|\frac{j^2}{S_{n,j}}-1\right|\le1.
\]

Use the first inequality and the deterministic sandwich on the good event, and the second on the bad event. Equations (12) and (14) yield

\[
\mathbb E\left|\frac{j^2}{S_{n,j}}-1\right|
\le C\left(j^{-1/4}+(s+1)e^{-s/4}\right).
\tag{15}
\]

No independence between `T_j` and the random stopping time is needed to control membership. On the good event, the indicators `1_{T_j>tau_(n,j)}` and `B_j` can differ only if

\[
|jT_j-1|\le |a-1|+\epsilon.
\]

The variable `jT_j` has exponential density bounded by one. Therefore (10) and (12) give

\[
\mathbb E\left|\mathbf1_{\{j\in A_{n,j}\}}-B_j\right|
\le C\left(j^{-1/4}+e^{-s/2}\right).
\tag{16}
\]

Finally,

\[
|jr_{n,j}-B_j|
\le\left|\frac{j^2}{S_{n,j}}-1\right|
+\left|\mathbf1_{\{j\in A_{n,j}\}}-B_j\right|.
\]

Equations (15)–(16) prove (8). All constants above are uniform over the stated `n,j`. ∎

#### Proof of (7)

For `j<256`, use (5) and `B_j<=1`; the resulting finite harmonic sum is bounded independently of `n`. The range `j>n/4` contributes at most

\[
\sum_{j>n/4}\left(\frac2{j+1}+\frac1j\right)=O(1).
\]

For the remaining range, divide (8) by `j`. The first term sums because `sum_j j^{-5/4}<infinity`. For the second, divide the indices into dyadic ranges

\[
2^\ell\le n/j<2^{\ell+1},\qquad \ell\ge2.
\]

The sum of `1/j` on each such range is bounded by an absolute constant, while

\[
(n/j+1)e^{-n/(4j)}
\le(2^{\ell+1}+1)e^{-2^\ell/4}.
\]

The latter bounds are summable over `ell`. This proves (7).

### 3. The random compensator is centered to bounded order

Equation (7) implies

\[
\mathbb E\left|\mathcal A_n-\sum_{j=1}^n\frac{B_j}{j}\right|\le C.
\tag{17}
\]

Since the `B_j` are independent Bernoulli(`q`),

\[
\mathbb E\sum_{j=1}^n\frac{B_j}{j}=qH_n,
\qquad
\operatorname{Var}\left(\sum_{j=1}^n\frac{B_j}{j}\right)
=q(1-q)\sum_{j=1}^n\frac1{j^2}=O(1).
\]

Here `H_n=sum_(j<=n)1/j=log n+O(1)`. Consequently,

\[
\mathcal A_n=q\log n+O_{\mathbb P}(1),
\qquad
\mathbb E\mathcal A_n=q\log n+O(1).
\tag{18}
\]

Because the martingale has mean zero, (18) proves (2). Together with (6), it also gives

\[
\frac{\mathcal V_n}{q\log n}\xrightarrow{\mathbb P}1.
\tag{19}
\]

### 4. Applying the martingale central limit theorem

Normalize each chronological martingale difference `X_(n,j)-r_(n,j)` by `sqrt(q log n)`. Its absolute value is at most `1/sqrt(q log n)`, which tends to zero uniformly. Thus, for every fixed positive Lindeberg threshold, the conditional Lindeberg sum is identically zero for all sufficiently large `n`. The sum of conditional variances tends to one in probability by (19).

The martingale central limit theorem now gives

\[
\frac{\mathcal M_n}{\sqrt{q\log n}}\xrightarrow{\mathrm d}\mathcal N(0,1).
\]

The compensator difference in (18), divided by `sqrt(q log n)`, tends to zero in probability. Slutsky's theorem proves (1).

### 5. Dependency theorem and source scope

The martingale theorem used here is the following standard triangular-array statement. For each `n`, let `D_(n,k)` be square-integrable martingale differences adapted to a filtration `F_(n,k)`. If

\[
\sum_k\mathbb E[D_{n,k}^2\mid\mathcal F_{n,k-1}]
\xrightarrow{\mathbb P}1
\]

and, for each `epsilon>0`,

\[
\sum_k\mathbb E[D_{n,k}^2\mathbf1_{\{|D_{n,k}|>\epsilon\}}
\mid\mathcal F_{n,k-1}]\xrightarrow{\mathbb P}0,
\]

then `sum_k D_(n,k)` converges in distribution to `N(0,1)`. A full proof in exactly this triangular-array form is given in [Péter Major, *Central limit theorems for martingales*, pp. 3–11](https://www.renyi.hu/~major/probability/martingale.pdf), developing the Brown–Dvoretzky theorem. The classical source is B. M. Brown, *Martingale Central Limit Theorems*, Annals of Mathematical Statistics 42(1), 59–66 (1971), [DOI 10.1214/aoms/1177693494](https://doi.org/10.1214/aoms/1177693494).

Every model-specific estimate needed for applying this theorem has been proved above. The proof does not use a local central limit theorem for a Poisson-binomial distribution, and does not infer the limit from a permuton density or finite simulation.

### 6. Bounded diagnostic and files

`sukhatme_check.py` samples independent clocks exactly and records the fixed-point count, compensator, and proxy for `n=100,1000,10000`, with 2000 samples at each size and RNG seed 1895. `sukhatme_output.json` is its raw output. It is intended to detect indexing or orientation mistakes and illustrate finite-size behavior. The asymptotic conclusion is established by the preceding written proof, not by these finite samples.


---

## 4. Q2662: a two-step comparison proves the minimum-gap conjecture

**Stable statement ID:** `3aaf2060b2cc3217f8e1`.

### Result

For every n >= 5 and every nonidentity relation mu in the perfect-matching association scheme,

\[
\lambda_1(A_\mu)-\lambda_2(A_\mu)\geq 2n-1.
\]

Equality is attained by the relation tau=(2,1^(n-2)). Thus Q2662 has an affirmative answer.

The argument proves the following useful comparison for every nonidentity mu:

\[
\boxed{\quad g_\mu\geq \frac{d_\mu}{4n(n-1)}(2n-1),\quad} \tag{1}
\]

where d_mu is the valency and g_mu is the unnormalized adjacency spectral gap. All but one of the nontrivial relations distinct from tau have d_mu >= 4n(n-1), when n>=5. The remaining relation is (n,mu)=(5,(2,2,1)); its spectral gap is 45.

### Primary source and exactly which prior facts are used

Himanshu Gupta, Allen Herman, Alice Lacaze-Masmonteil, Roghayeh Maleki, and Karen Meagher, *On the second largest eigenvalue of certain graphs in the perfect matching association scheme*: <https://arxiv.org/html/2510.17135>; published version <https://doi.org/10.37236/15092>.

The inspected HTML version states the target as Conjecture 6.1. Its Proposition 4.1 gives d_tau=n(n-1) and g_tau=2n-1. Its Table 6 gives the distinct eigenvalues of A_(2,2,1) on perfect matchings of K_10 as

\[
60,\ 15,\ 11,\ 6,\ 5,\ -3,\ -10,
\]

so the exceptional gap is 60-15=45. The argument below proves the missing general comparison. The valency formula is also derived by direct counting below. The attached exact computation independently certifies that the exceptional graph has no nontrivial eigenvalue above 15.

### 1. Every elementary flip has a two-step route in every relation

Let X be the set of perfect matchings of K_(2n). Let H be the graph for tau, so an H-edge replaces two matching edges by one of the two alternative pairings on their four vertices. Fix any such pair M,M'. By relabeling vertices we may assume

\[
M\supset\{12,34\},\qquad
M'=(23)M\supset\{13,24\}.
\]

Let mu be nonidentity. It has a part s>=2. There is a matching Q that is mu-related to M and contains edge 23: put M-edges 12 and 34 in an alternating cycle of length 2s, use s-2 more M-edges to complete that cycle, and realize the other parts of mu on the remaining M-edges. Explicitly, after relabeling the s selected M-edges as 12,34,...,(2s-1,2s), the Q-edges in this component can be 23,45,...,(2s,1).

The transposition (23) fixes Q because 23 is itself a Q-edge. Consequently

\[
\operatorname{type}(M',Q)
=\operatorname{type}((23)M,(23)Q)
=\operatorname{type}(M,Q)=\mu.
\]

Thus M-Q-M' is a length-two path in G_mu. In particular, the common-neighbor set

\[
C(M,M')=N_\mu(M)\cap N_\mu(M')
\]

is nonempty for every oriented H-edge (M,M').

### 2. Equivariant fractional paths and the factor four

For every oriented H-edge (M,M'), choose Q uniformly from C(M,M') and route one unit of demand along the oriented two-step path M,Q,M'. This rule is invariant under every vertex relabeling in S_(2n).

The group S_(2n) is transitive on the oriented edges of G_mu: any two ordered pairs of perfect matchings with the same alternating-cycle lengths can be carried to one another by relabeling their alternating cycles. Therefore every oriented G_mu-edge has the same expected total load.

Write V=|X|, d_0=n(n-1), and d=d_mu. There are V*d_0 oriented H-edges and every routed path has two edges, so the total edge load is 2V*d_0. There are V*d oriented G_mu-edges. The load on each is consequently

\[
L=\frac{2d_0}{d}.
\]

For every real function f on X, the length-two inequality gives

\[
(f(M)-f(M'))^2\leq
2(f(M)-f(Q))^2+2(f(Q)-f(M'))^2.
\]

Average this inequality over Q, then sum over every oriented H-edge. Uniform load yields

\[
\sum_{(M,M')\in E^{\rm or}(H)}(f(M)-f(M'))^2
\leq\frac{4d_0}{d}
\sum_{(U,V)\in E^{\rm or}(G_\mu)}(f(U)-f(V))^2. \tag{2}
\]

Equivalently, for the unnormalized graph Laplacians,

\[
\langle f,L_\mu f\rangle
\geq\frac{d}{4d_0}\langle f,L_0f\rangle.
\]

For mean-zero f, the known flip-graph spectral gap implies

\[
\langle f,L_\mu f\rangle
\geq\frac{d}{4d_0}(2n-1)\langle f,f\rangle.
\]

Taking the minimum Rayleigh quotient proves (1). This argument also proves every nonidentity G_mu is connected, since its Laplacian has no mean-zero vector in its kernel.

### 3. The valency bound

Write m_s for the number of parts of size s in mu and ell(mu)=sum_s m_s. Partition the n edges of a fixed matching M into blocks prescribed by mu. On a block of s edges, the number of matchings forming one alternating 2s-cycle with those edges is 2^(s-1)(s-1)!, including the value 1 when s=1. Thus

\[
d_\mu=\frac{2^{n-\ell(\mu)}n!}{\prod_s s^{m_s}m_s!}. \tag{3}
\]

Put t=n-m_1 and let lambda be the partition formed by deleting all parts 1. Then lambda has no parts 1, and

\[
d_\mu=\binom nt\,d_\lambda^{(t)},
\]

where d_lambda^(t) is the internal valency on its t chosen M-edges.

#### t >= 6

For s>=2 we have s/2^(s-1)<=1. If ell=ell(lambda), then ell<=floor(t/2), and

\[
\frac{\prod_{s\geq2}s^{m_s}m_s!}{2^{t-\ell}}
=\prod_{s\geq2}\left(\frac{s}{2^{s-1}}\right)^{m_s}m_s!
\leq\prod_{s\geq2}m_s!\leq\ell!\leq\lfloor t/2\rfloor!.
\]

Consequently

\[
d_\lambda^{(t)}\geq\frac{t!}{\lfloor t/2\rfloor!}
\geq 4t(t-1),\qquad t\geq6. \tag{4}
\]

For the last inequality, (t-2)!/floor(t/2)! is 4 at t=6 and increases thereafter. It follows that

\[
d_\mu\geq4\binom nt t(t-1)
=4n(n-1)\binom{n-2}{t-2}\geq4n(n-1).
\]

#### The small support sizes

- t=2 gives exactly mu=tau, whose gap is already 2n-1.
- t=3 gives lambda=(3), so d_mu=8*C(n,3)=(4/3)n(n-1)(n-2)>=4n(n-1) for every n>=5.
- t=4 gives lambda=(4) or (2,2), with internal valencies 48 and 12, respectively. Thus d_mu>=12*C(n,4)=(1/2)n(n-1)(n-2)(n-3)>=4n(n-1) for n>=6. At n=5, lambda=(4) has valency 240 and still satisfies the bound; lambda=(2,2) is the single exception discussed next.
- t=5 gives lambda=(5) or (3,2), with internal valencies 384 and 160. Hence d_mu>=160*C(n,5)>=4n(n-1) for every n>=5.

This exhausts all partitions because t=1 is impossible and t=0 is the excluded identity relation.

#### The one exception

When n=5 and mu=(2,2,1), the valency is 60 and the largest nontrivial eigenvalue is 15, giving gap 45>9. This is recorded in Table 6 of the primary source. The exact replay script below also verifies

\[
(A-60I)(A-15I)(A-11I)(A-6I)(A-5I)(A+3I)(A+10I)=0.
\]

It does so using only integer arithmetic and transitivity: it checks the polynomial applied to one basis vector, and automorphism transitivity carries this identity to every basis vector. Because connectivity was already proved in Section 2, the eigenvalue 60 is simple. All remaining possible eigenvalues are at most 15, which independently establishes gap at least 45 and is sufficient for the conjecture.

### 4. Conclusion and replay

For every relation other than tau and the one finite exception, the valency bound inserted into (1) gives g_mu>=2n-1. The base relation and the exception have just been handled. This proves the stated conjecture for all n>=5.

`verify_matching.py` generates the 945 perfect matchings of K_10, constructs the exceptional graph by its two independent flips, and checks its spectral polynomial exactly. It also checks the valency formula and exception classification for all 9,242 relevant partitions with 5<=n<=25. These are sanity checks of an unrestricted proof, not an extrapolation from the finite range.

#### Explicit seven-dimensional exceptional certificate

Fix a base matching M_0. Its stabilizer has seven orbits on the matchings, indexed by the alternating-cycle partition relative to M_0. In the order

\[
(5),\ (4,1),\ (3,2),\ (3,1,1),\ (2,2,1),\ (2,1,1,1),\ (1,1,1,1,1),
\]

their sizes are 384,240,160,80,60,20,1. The adjacency operator for relation (2,2,1), restricted to functions constant on these seven orbits, is represented by

\[
B=\begin{pmatrix}
25&15&10&5&5&0&0\\
24&21&8&4&1&2&0\\
24&12&15&3&3&3&0\\
24&12&6&12&6&0&0\\
32&4&8&8&5&2&1\\
0&24&24&0&6&6&0\\
0&0&0&0&60&0&0
\end{pmatrix}.
\]

Each row can be obtained by choosing one matching in the corresponding orbit and counting its 60 neighbors by their orbit types. Exact integer matrix multiplication gives

\[
(B-60I)(B-15I)(B-11I)(B-6I)(B-5I)(B+3I)(B+10I)=0.
\]

Here is why this quotient identity certifies the full spectrum rather than just a subset of it. The point mass delta_(M_0) belongs to the space of functions constant on stabilizer orbits. Thus the displayed polynomial annihilates A applied to delta_(M_0). The adjacency operator commutes with every vertex relabeling, and the relabeling group is transitive on matchings. Translating delta_(M_0) to any other point mass shows that the polynomial annihilates every basis vector, and hence annihilates the full adjacency matrix.

The script checks that every one of the 945 vertices has the neighbor counts specified by its quotient row. It also verifies the annihilating polynomial directly on the full point-mass vector and independently verifies graph connectivity. All these checks use unbounded integer arithmetic. The matrix, cells, polynomial roots, and check outcomes are saved in `matching_certificate.json`; the complete transcript is `matching_checks.txt`.


---

## 5. Exact coboundaries for repeated-surjection whirling and slab toggling

Prepared 2026-10-09 from the attached B13 handoff. The two identities below give complete proofs of Q2664 and Q2665 as stated in that handoff. They require neither rational initial coordinates nor orbit enumeration.

### Statements and source

- Q2664, stable ID `3f3121a42f7e5c02851a`: every orbit of whirling on functions whose fibres all have size at least m has each fibre-size average n/k.
- Q2665, stable ID `39dd68d5345401fd90b1`: every orbit of coordinate toggling on the slab r <= sum(x_i) <= n-r in [0,1]^n has asymptotic coordinate-sum average n/2.

The source is Michael Joseph, James Propp, and Tom Roby, *Whirling injections, surjections, and other functions between finite sets*, arXiv:1711.02411v6, December 8, 2025, Conjectures 2.11 and 2.28. The exact definitions and conjectures were checked in the primary source at <https://arxiv.org/html/1711.02411v6>. Published article: <https://doi.org/10.46298/dmtcs.14126>.

The following proofs are elementary derivations made in this session. No priority claim is made about these derivations.

### Common elementary observation: a balanced path and a cyclic rotation

Encode an ordered pair of nonnegative real numbers (A,B) by a path that first rises by A and then falls by B. Its net increment is A-B and its maximum above its starting height is A. Concatenate several such factors. The maximum height is the maximum over all factor peaks, also allowing the initial height 0.

Suppose the whole path starts and ends at height 0 and its final factor C has net increment delta. Move C from the end to the beginning. The new maximum is the old maximum plus delta.

Indeed, write the old word as AC, let the maximum heights within A and C relative to their own starting heights be M_A and M_C, and note that A has net increment -delta. The old maximum is max(M_A, -delta+M_C); the rotated maximum is max(M_C, delta+M_A), exactly delta plus the old maximum. This argument works even when a factor has zero length or one of the two subpaths has zero net increment.

We also use that replacing two consecutive factors by two new factors with the same total increment and the same maximum relative to their common starting height leaves the maximum of the whole concatenated path unchanged.

### 1. Q2664: repeated-surjection whirling

#### Theorem and explicit identity

Fix integers n,k,m >= 1 with n >= mk. Let F consist of words f=(f(1),...,f(n)) over [k] such that every letter occurs at least m times. Let W=w_n ... w_1 be forward whirling, so coordinate 1 is treated first. Write c_a(f) for the number of occurrences of a.

If k=1 the conclusion is immediate. Suppose k >= 2. Fix a cyclically adjacent pair of letters i and j=i+1, interpreted modulo k. Define

\[
M_i(f)=\max_{0\leq \ell\leq n}
\sum_{h=n-\ell+1}^{n}
\bigl(\mathbf 1_{f(h)=i}-\mathbf 1_{f(h)=j}\bigr),
\]

where the empty suffix has sum 0, and put

\[
\Psi_i(f)=\max\{c_i(f)-m,M_i(f)\}.
\]

The exact identity is

\[
\boxed{\quad\Psi_i(W^{-1}f)-\Psi_i(f)=c_j(f)-c_i(f).\quad} \tag{S1}
\]

Consequently every finite W-orbit O satisfies

\[
\sum_{f\in O}c_i(f)=\sum_{f\in O}c_j(f).
\]

Doing this for all cyclically adjacent pairs makes all k sums equal. Since the sum of the fibre sizes of each word is n, their common orbit average is n/k. This proves Q2664 for every allowed n,k,m.

#### Why the inverse map has a simple local rule

The inverse of w_h repeatedly decrements f(h) cyclically until admissibility returns. If the current letter is a and its current multiplicity exceeds m, one decrement is already admissible, so the letter changes to a-1. If its multiplicity is exactly m, every different letter would leave fewer than m occurrences of a; the full cycle returns to a, leaving the coordinate unchanged.

Thus inverse whirling at one position is

\[
a\longmapsto b=
\begin{cases}
a-1\pmod k,&c_a>m,\\
a,&c_a=m.
\end{cases}
\]

The complete inverse W^{-1} treats positions n,n-1,...,1 in that order.

#### The auxiliary vector

Set q_a=c_a-m, so every q_a is a nonnegative integer. Whenever one inverse update changes a to b, update

\[
q'_h=q_h+\mathbf1_{b=h}-\mathbf1_{a=h}.
\]

This makes q' exactly the vector of excess multiplicities after that coordinate update. All its entries stay nonnegative. It is convenient to regard this vector as an auxiliary factor that moves past the letters one at a time.

For our fixed adjacent pair i,j, encode a letter a by the factor

\[
(\mathbf1_{a=i},\mathbf1_{a=j}),
\]

and encode the auxiliary vector q by the factor

\[
(q_j,q_i).
\]

Consider the word of factors consisting of the letters f(n),f(n-1),...,f(1), followed by q. Its total increment is

\[
(c_i-c_j)+(q_j-q_i)=0.
\]

Its maximum is precisely Psi_i(f). The maximum reached among the letter factors is the maximum signed suffix sum M_i(f). The peak in the final auxiliary factor is

\[
c_i-c_j+q_j=c_i-m.
\]

#### Local maximum preservation, including k=2

Place q immediately before a letter a, perform its inverse-whirling update to b, and exchange the order of the factors so that b comes immediately before q'. Their total increments agree because q'=q+e_b-e_a.

Let U=q_j and D=q_i. Before the exchange, the maximum relative to the starting height of this two-factor segment is

\[
M=\max\{U,U-D+\mathbf1_{a=i}\}
 =U+\mathbf1_{\{a=i,\,q_i=0\}}. \tag{S2}
\]

The last equality uses the fact that D is a nonnegative integer.

After the exchange, since q'_j=U+1_{b=j}-1_{a=j}, the corresponding maximum is

\[
\begin{aligned}
M'&=\max\{\mathbf1_{b=i},\mathbf1_{b=i}-\mathbf1_{b=j}+q'_j\}\\
&=\mathbf1_{b=i}+\max\{0,U-\mathbf1_{a=j}\}.
\end{aligned} \tag{S3}
\]

These quantities agree:

1. If a=j and U>0, the inverse update gives b=i. Equation (S3) is 1+(U-1)=U, equal to (S2).
2. If a=j and U=0, the update is blocked, so b=j. Equation (S3) is 0, again equal to (S2).
3. If a is not j, the maximum in (S3) is U. In this case b=i occurs exactly when a=i and q_i=0: a moving letter can arrive at i only from j. Therefore (S3) again equals (S2).

This proof covers every k>=2, including the cyclic transition from 1 to k. There is no exceptional two-letter case.

#### The complete sweep

Begin with the balanced path for f(n),...,f(1),q. Move the auxiliary factor from the end to the beginning. Its net increment is

\[
q_j-q_i=c_j-c_i,
\]

so the maximum increases by c_j-c_i by the balanced-path observation.

Now move the auxiliary factor across the letters in order, applying the inverse-whirling rule at every exchange. Every exchange preserves the maximum by (S2)-(S3). When the sweep is complete, the letter word is W^{-1}f in reverse coordinate order, and the final auxiliary vector is its excess-multiplicity vector. Therefore the final maximum is Psi_i(W^{-1}f), proving (S1).

#### Further consequences and arbitrary orders

The argument applies to any order of the coordinate updates: use the reverse of that order in the definition of the suffix maximum. Thus the conclusion also holds for W_pi=w_{pi(n)} ... w_{pi(1)} for every permutation pi.

The potential is bounded: 0 <= Psi_i(f) <= n-(k-1)m. Since (S1) is an exact coboundary, it also gives a discrepancy bound for partial orbit segments, not just equality over a period. The usual orbit-length divisibility consequence follows immediately: every W-orbit length is divisible by k/gcd(n,k).

The case n=mk is included. Every local update is blocked, all orbits are fixed points, and each c_i is m=n/k.

### 2. Q2665: real slab toggling

#### Theorem and explicit identity

Let n >= 1 be an integer, and let r be a real number with 0 <= r <= n/2. Let

\[
P=\{x\in[0,1]^n:r\leq S(x)\leq n-r\},
\qquad S(x)=\sum_{i=1}^n x_i.
\]

Let pi be any permutation, and T_pi be the sweep of the coordinate-reflection toggles in the order pi(1),...,pi(n), exactly as in Q2665. Define

\[
\boxed{
\Psi_\pi(x)=\max\left\{
n-r-S(x),\;
\max_{1\leq h\leq n}
\left(h-x_{\pi(h)}-2\sum_{j<h}x_{\pi(j)}\right)
\right\}.} \tag{P1}
\]

Then

\[
\boxed{\quad\Psi_\pi(T_\pi x)-\Psi_\pi(x)=2S(x)-n.\quad} \tag{P2}
\]

Moreover 0 <= Psi_pi(x) <= n-r throughout P. Hence, for every x in P and N >= 1,

\[
\boxed{
\left|\frac1N\sum_{t=0}^{N-1}S(T_\pi^t x)-\frac n2\right|
\leq\frac{n-r}{2N}.} \tag{P3}
\]

This proves the requested limit for every real starting point, including irrational coordinates and irrational r, with a uniform rate.

#### An auxiliary interval coordinate

Write

\[
w=n-2r,\qquad C=n-r,\qquad z=C-S(x).
\]

The slab condition is exactly 0 <= z <= w. Regard the x_i as coordinates with capacity 1 and z as an auxiliary coordinate with capacity w. Their total content is

\[
z+\sum_i x_i=C=\frac{n+w}{2}.
\]

At a toggle of a coordinate x, put

\[
p=\min(z,1-x),\qquad q=\min(x,w-z).
\]

Then the toggle is precisely

\[
x'=x+p-q,\qquad z'=z-p+q. \tag{P4}
\]

To verify the agreement with the question, let c=x+z and let s be the sum of the other original coordinates. Since z=n-r-s-x, we have c=n-r-s. The admissible endpoints for x are

\[
L=\max(0,c-w),\qquad R=\min(1,c).
\]

Also p=min(c,1)-x and q=x-max(0,c-w), so x+p-q=L+R-x, the required reflection.

#### A local identity for arbitrary capacities

The following algebra works for all nonnegative real capacities a,b and contents 0<=u<=a, 0<=v<=b. Set

\[
p=\min(u,b-v),\qquad q=\min(v,a-u),
\]

\[
v'=v+p-q,\qquad u'=u-p+q.
\]

Encode a capacity/content pair (a,u) by an up step of length a-u followed by a down step of length u. Its net increment is a-2u.

The exchange

\[
((a,u),(b,v))\longmapsto((b,v'),(a,u')) \tag{P5}
\]

preserves both the total increment and the maximum height of these two consecutive factors. The total increment is immediate from u'+v'=u+v. For the maximum, let s=u+v and write t_+=max(t,0). The old maximum is

\[
M=\max(a-u,a-2u+b-v)=a-u+(b-s)_+.
\]

The new maximum is

\[
\begin{aligned}
M'&=\max(b-v',b-2v'+a-u')\\
&=q-p+(b-v)+(a-s)_+.
\end{aligned}
\]

Using p=u-(s-b)_+ and q=v-(s-a)_+ gives

\[
\begin{aligned}
M'&=b-u-(s-a)_++(s-b)_++(a-s)_+\\
&=a+b-u-s+(s-b)_+\\
&=a-u+(b-s)_+=M.
\end{aligned} \tag{P6}
\]

All identities are valid at equality boundaries and for zero capacities.

#### The full balanced path

Arrange the factors in the order

\[
(1,x_{\pi(1)}),...,(1,x_{\pi(n)}),(w,z).
\]

Their total net increment is

\[
n+w-2(S+z)=0.
\]

Their maximum height is exactly Psi_pi(x). The peak in original-coordinate factor h is

\[
\sum_{j<h}(1-2x_{\pi(j)})+1-x_{\pi(h)}
=h-x_{\pi(h)}-2\sum_{j<h}x_{\pi(j)}.
\]

The peak in the final auxiliary factor is

\[
n-2S+w-z=n-r-S=z.
\]

Now rotate the final auxiliary factor to the beginning. Its net increment is

\[
w-2z=2S-n.
\]

The path maximum therefore increases by 2S-n. Move the auxiliary factor across all original-coordinate factors using (P5) with a=w and b=1. Each exchange preserves the maximum by (P6) and applies exactly the toggle (P4). After the sweep, the path is the original-coordinate factors for T_pi x followed by its updated auxiliary coordinate. Its maximum is Psi_pi(T_pi x). This proves (P2).

#### Boundedness and the limit

The maximum is nonnegative because the path begins and ends at 0. Its total upward length is

\[
\sum_i(1-x_i)+(w-z)=n+w-(S+z)=n-r.
\]

Consequently its maximum is at most n-r. Summing (P2) for x,T_pi x,...,T_pi^{N-1}x gives

\[
2\sum_{t=0}^{N-1}\left(S(T_\pi^t x)-\frac n2\right)
=\Psi_\pi(T_\pi^N x)-\Psi_\pi(x),
\]

whose absolute value is at most n-r. This is (P3), and the right side tends to 0 after division by 2N.

When r=n/2, the slab has constant coordinate sum and every toggle is the identity; the proof still applies with w=0. When r=0, the sweep complements every original coordinate. When r=(n-1)/2, the auxiliary capacity is 1, each exchange is a swap, and the sweep cyclically rotates n+1 coordinates of total content (n+1)/2. These special cases are consistent with the general identity.

### 3. Exact computation and replay

The proofs above are independent of computation. The accompanying scripts check the local algebra and the resulting global identities using integer arithmetic; no floating-point tolerance is involved.

- `verify_potentials.py` checks the two local maximum-preservation identities exhaustively in bounded parameter ranges, then checks both global coboundaries on reproducible random integer instances, including nontrivial coordinate orders.
- `check.cpp`, compiled with `g++ -O3 -std=c++17 check.cpp -o check`, enumerates finite whirling state spaces or rational slab grids, decomposes the exact permutation into orbits, and checks the proposed homomesic averages over each complete orbit.
- `jobs.json` records the exact enumeration jobs, and `raw_checks.txt` records their complete output.

Before the proofs were discovered, the orbit checker verified repeated-surjection cases (n,k,m)=(13,3,2),(11,3,2),(11,3,3), encompassing 1,610,532 admissible states and 295,280 orbits. It also verified 33 rational slab-grid cases, with n from 3 through 9, encompassing 1,202,437 admissible states and 341,946 orbits. The raw state budgets were 1,948,617 for the surjection route and 1,725,839 for the slab route. These computations motivated the explicit potentials but are not used to pass from rational to real coordinates; the proof of (P2) is directly valid for real numbers.

### 4. Other assigned questions

Q2662 (matching-scheme spectral gap) was subsequently proved in this session by a two-step path comparison and a valency bound; its complete proof and exact finite exception certificate are in `matching_proof.md`, `verify_matching.py`, `matching_certificate.json`, and `matching_checks.txt` in this directory. The matching source states the minimum-gap conjecture as Conjecture 6.1 in its inspected arXiv HTML version: <https://arxiv.org/html/2510.17135>.

No new closure is claimed for provisional Q2494, stable ID `20d1798f558ecef53b7b` (connected graph/complement exponent). The Kim-Madras article states the remaining exponent lies in [3/4,1]: <https://doi.org/10.1002/jgt.23253>. Its source and example were inspected, but no sharper bound was proved here.


---

## 6. B13 / Q1290 — separation cutoff for 0 < alpha < 1

Stable statement ID: `dd1e1530c8b22bbf943a`.

**Decision: partial** at the full question's scope. The entire range \(0<\alpha<1\) is proved here. The range \(\alpha>1\) remains unresolved in this return. The proof also applies to all fixed \(\alpha\le1\), including the previously established nonpositive biases and the excluded endpoint \(\alpha=1\).

### Theorem

Fix a real \(\alpha\le1\). Let \(P_n\) be the one-sided transposition shuffle in the handoff and put \(\tau_n=S_\alpha(n)/n^\alpha\). Then \(P_n\) has separation cutoff at \(\tau_n\log n\).

Two external inputs are used with their precise normalizations:

1. The unsigned total-variation cutoff at \(\tau_n\log n\), Matheau-Raven's thesis, Theorem 3.6.6: <https://etheses.whiterose.ac.uk/id/eprint/28076/1/OMatheauRavenThesis.pdf>.
2. For the ordinary random-transposition law \(R_n\), with probability \(2/n^2\) for each distinct transposition and \(1/n\) for the identity, separation cutoff occurs at \((n/2)\log n\). This is Theorem 1 of Graham White, *A strong stationary time for random transpositions*: <https://arxiv.org/html/1910.00770v1>.

### Central-component proof

Every distinct transposition \((i,j)\), \(i<j\), has \(P_n\)-mass
\[
\frac{j^{\alpha-1}}{S_\alpha(n)}\ge
\frac{n^{\alpha-1}}{S_\alpha(n)}=\frac1{n\tau_n}.
\]
The total identity mass is \(S_{\alpha-1}(n)/S_\alpha(n)\ge1/\tau_n\). Set
\[
c_n=\frac{n}{2\tau_n}.
\]
This lies strictly between zero and one because
\(\tau_n=\sum_{j=1}^n(j/n)^\alpha\ge\sum_{j=1}^n j/n=(n+1)/2\).
The law \(c_nR_n\) assigns \(1/(n\tau_n)\) to each distinct transposition and \(1/(2\tau_n)\) to the identity. Subtracting it from \(P_n\) leaves a nonnegative measure of mass \(1-c_n\). Thus
\[
P_n=c_nR_n+(1-c_n)Q_n
\]
for a probability law \(Q_n\).

The ordinary random-transposition law is conjugacy invariant, hence central in the group algebra; it commutes with \(Q_n\). Therefore
\[
P_n^t=\sum_{k=0}^t\binom tkc_n^k(1-c_n)^{t-k}
R_n^k*Q_n^{t-k}.                                      \tag{1}
\]
Convolution with a probability measure cannot increase separation from the uniform law: if \(\mu(g)\ge(1-s)/n!\) for every \(g\), the same inequality holds for \(\mu*\nu\). Separation is also convex under mixtures. Consequently, if \(K\sim\operatorname{Bin}(t,c_n)\),
\[
\operatorname{sep}(P_n^t)\le
\mathbb E[\operatorname{sep}(R_n^K)].                  \tag{2}
\]

Fix \(\epsilon>0\) and set \(t=\lfloor(1+\epsilon)\tau_n\log n\rfloor\). Then
\[
\mathbb EK=(1+\epsilon)\frac n2\log n+O(1),\qquad
\operatorname{Var}K\le\mathbb EK.
\]
Chebyshev's inequality implies
\(\Pr[K<(1+\epsilon/2)(n/2)\log n]\to0\). Using the monotonicity of separation in the number of steps and White's theorem in (2) gives \(\operatorname{sep}(P_n^t)\to0\).

For \(0<\epsilon<1\), at \(t=\lfloor(1-\epsilon)\tau_n\log n\rfloor\), the total-variation distance tends to one by the first external input. Since total variation is at most separation, the separation distance tends to one as well. This proves the theorem.

### Scope and limitation

This argument gives an exact cutoff location on the requested interval \(0<\alpha<1\). It does not assert an optimal additive cutoff window. When \(\alpha>1\), the smallest transposition rate occurs at the low indices and the same central-component extraction loses the conjectured time scale, so the proof does not address that interval. This failure of this comparison is not evidence against the conjecture.

No computation is needed for this result. The nonnegativity estimates are explicit and the proof depends on the two source theorems named above.


---

## 7. B13 / Q1896: exact cycle compensator and logarithmic lower bound

**Stable statement ID:** `25f5bc9a09e2c4ffa329`.

**Retained statement:** Determine centering, scaling, and a nondegenerate limiting distribution for the total number `C_n` of cycles in a Sukhatme permutation with weights `n-i+1`.

**Decision: partial.** The exact compensator and the bounds below are proved. A centering, fluctuation scale, and limiting law for the total cycle count are not established. Evidence: written argument, with the clock-concentration estimates already proved in `sukhatme_report.md`. No additional simulation or formal compilation is used.

### Results

For every fixed `epsilon>0`,

\[
\mathbb P\{C_n<(1-\epsilon)\log n\}\longrightarrow0.
\tag{1}
\]

In addition,

\[
\mathbb E C_n\ge\log n-O(1),
\qquad
\limsup_{n\to\infty}\frac{\mathbb E C_n}{(\log n)^2}\le\frac12.
\tag{2}
\]

The upper bound also implies `C_n=O_P((log n)^2)`. The lower coefficient one improves the immediate consequence `C_n>=F_n`, whose coefficient from Q1895 is only `1/e`. These bounds do not identify the actual order between the logarithmic lower and squared-logarithmic upper bounds.

The source [Borga–Chatterjee–Diaconis, §5.2](https://arxiv.org/html/2509.07729v2) asks for the total cycle asymptotics in the same model. Inversion and simultaneous reversal of labels and ranks preserve the cycle count, so the clock formulation below retains the exact model.

### 1. The unique label which closes a cycle

Use independent `T_k~Exp(k)`, and the sets `A_(n,j)` and total rates `S_(n,j)` from the fixed-point report. At the stage with exactly `j` surviving labels, expose the permutation image of domain `j` by assigning it the next deleted label. This reveals the permutation in domain order `n,n-1,...,1`.

The already exposed directed graph has indegrees at most one and outdegrees at most one. It consists of completed cycles and directed paths. Domain `j` has no outgoing edge yet. Follow its incoming path backward until its head, denoted `a_(n,j)`. This head has indegree zero and is therefore an available image label in `A_(n,j)`. Assigning `j -> a_(n,j)` closes exactly one cycle. Every other available choice joins two paths and closes no cycle.

The key deterministic inequality is

\[
a_{n,j}\ge j.
\tag{3}
\]

If the backward path is empty, its head is `j`. Otherwise every predecessor has an exposed outgoing edge and hence is a domain greater than `j`; its eventual head is consequently greater than `j` as well. The path cannot enter a completed cycle because that would violate the indegree-one restriction.

Let `Y_(n,j)` indicate cycle closure at this stage. Its predictable success probability is exactly

\[
u_{n,j}=\frac{a_{n,j}}{S_{n,j}}.
\tag{4}
\]

Every cycle is counted when its smallest domain is exposed, so

\[
C_n=\sum_{j=1}^nY_{n,j}.
\]

Define its compensator

\[
\mathcal K_n=\sum_{j=1}^n u_{n,j}.
\]

Then `C_n-K_n` is a martingale terminal value with increments of absolute value at most one and predictable quadratic variation

\[
\sum_{j=1}^n u_{n,j}(1-u_{n,j}).
\tag{5}
\]

Equations (3)–(4) imply the pathwise bound

\[
\mathcal K_n\ge R_n:=\sum_{j=1}^n\frac{j}{S_{n,j}}.
\tag{6}
\]

### 2. Lower bound on the compensator

The reciprocal estimate (15) in `sukhatme_report.md` and its dyadic summation, without any label-membership indicator, give

\[
\sup_n\sum_{j=1}^n
\mathbb E\left|\frac{j}{S_{n,j}}-\frac1j\right|<\infty.
\tag{7}
\]

For clarity, the bounded end ranges require no new estimate. Always

\[
\frac{j}{S_{n,j}}\le\frac2{j+1}.
\]

Thus the finitely many small indices contribute a constant, and the range `j>n/4` contributes a bounded harmonic interval. For `j>=256` and `n>=4j`, the fixed-point report proves

\[
\mathbb E\left|\frac{j^2}{S_{n,j}}-1\right|
\le C\left[j^{-1/4}+(n/j+1)e^{-n/(4j)}\right].
\]

Dividing by `j` and summing proves (7). In particular,

\[
R_n=H_n+O_{L^1}(1)=\log n+O_{L^1}(1).
\tag{8}
\]

Taking expectations in (6) proves the expectation lower bound in (2), because `E C_n=E K_n`.

To obtain a probability bound despite the potentially larger compensator, fix `theta>0`. At each stage,

\[
\mathbb E[e^{-\theta Y_{n,j}}\mid\text{past}]
=1-(1-e^{-\theta})u_{n,j}
\le e^{-(1-e^{-\theta})u_{n,j}}.
\]

Multiplication over the chronological filtration gives the exponential supermartingale inequality

\[
\mathbb E\exp\{(1-e^{-\theta})\mathcal K_n-\theta C_n\}\le1.
\tag{9}
\]

For `0<epsilon<1`, set `theta=epsilon/2`, `v=(1-epsilon/2)log n`, and `b=(1-epsilon)log n`. By (8),

\[
\mathbb P(\mathcal K_n<v)\le\frac{C_\epsilon}{\log n}.
\]

On the complementary event, (9) and Markov's inequality give

\[
\mathbb P(C_n\le b,\ \mathcal K_n\ge v)
\le e^{\theta b-(1-e^{-\theta})v}
\le n^{-\epsilon^2/8},
\]

where `1-e^{-theta}>=theta-theta^2/2` was used. Therefore

\[
\mathbb P\{C_n\le(1-\epsilon)\log n\}
\le\frac{C_\epsilon}{\log n}+n^{-\epsilon^2/8},
\tag{10}
\]

which proves (1).

### 3. A squared-logarithmic expectation upper bound

The bounds

\[
a_{n,j}\le\max A_{n,j},\qquad
S_{n,j}\ge j(j+1)/2,\qquad u_{n,j}\le1
\tag{11}
\]

provide the upper estimate. The use of `u_(n,j)<=1` on exceptional events is essential: no factor `n` is charged to a bad-event probability.

Fix `0<delta<1/8`. There are constants `J_delta`, `L_delta`, and `C_delta`, independent of `n,j`, such that for `j>=J_delta` and `n>=L_delta j`,

\[
\mathbb P\left\{\tau_{n,j}<\frac{1-\delta}{j}
\ \text{or}\ S_{n,j}<(1-4\delta)j^2\right\}
\le\frac{C_\delta}{j}.
\tag{12}
\]

This follows directly from the deterministic-time estimates in the fixed-point report. Choose `L_delta` so the geometric tails there are below a sufficiently small multiple of `delta`, and `J_delta` so the Riemann-sum errors are also smaller. The expected survivor count at `(1-delta)/j` then exceeds `j` by `c_delta j`, and at `(1+delta)/j` is less than `j` by `c_delta j`; both count variances are `O(j)`. Chebyshev therefore places `tau` between those times with probability `1-O_delta(1/j)`. On this event,

\[
S_{n,j}\ge W_j(1+\delta).
\]

Its normalized mean can be made larger than `1-3delta`, since `(1+delta)^{-2}>=1-2delta` and the omitted tail is arbitrarily small after increasing `L_delta`. Its normalized variance is `O(1/j)`, so another Chebyshev estimate proves the second assertion in (12).

Put `a=1-delta` and

\[
Z_j=\max\{k\le n:T_k>a/j\},
\]

with maximum zero for an empty set. A union bound gives

\[
\mathbb E Z_j\le\frac j{1-\delta}\log j+O_\delta(j).
\tag{13}
\]

Here is a direct bound: set `m=ceil((j/a)log j)`. Then

\[
\mathbb E Z_j
\le m+\sum_{k>m}\mathbb P(Z_j\ge k)
\le m+\sum_{\ell>m}(\ell-m)e^{-a\ell/j}.
\]

The last sum is `O_delta(j^2 e^{-am/j})=O_delta(j)`, proving (13).

On the good event in (12), every surviving label is among those in `Z_j`, and `S_(n,j)>=(1-4delta)j^2`. On its complement use `u_(n,j)<=1`. Consequently,

\[
\mathbb E u_{n,j}
\le\frac{\log j}{j(1-\delta)(1-4\delta)}
+\frac{C_\delta}{j}
\tag{14}
\]

in the interior range. The finite range `j<J_delta` contributes at most `J_delta`. In the upper end range use

\[
u_{n,j}\le\frac{2n}{j(j+1)},\qquad
\sum_{j>n/L_\delta}u_{n,j}\le2L_\delta.
\]

Summing (14) and using `sum_(j<=n)(log j)/j=(log n)^2/2+O(1)` yields

\[
\mathbb E C_n
\le\frac{(\log n)^2}{2(1-\delta)(1-4\delta)}
+O_\delta(\log n).
\]

First let `n` tend to infinity and then let `delta` decrease to zero. This proves the upper bound in (2).

### 4. Remaining obstacle

The weighted survivor sums `S_(n,j)` are already controlled accurately enough for limit theorems. The new variable is the path head `a_(n,j)`, which is selected by the partial permutation and is not simply an independent exponential-clock survival indicator. A full answer requires sharp control of

\[
\mathcal K_n=\sum_j\frac{a_{n,j}}{S_{n,j}},
\]

including its leading term and its fluctuations. The inequalities `j<=a_(n,j)<=max A_(n,j)` leave a logarithmic factor in the upper bound. No independence or local-limit heuristic for the head sequence is used or asserted here.


---

## 8. B13: Complete-mapping recognition and Rees zero-matrix obstructions

Date: 2026-10-09 UTC. Parent handoff snapshot: 2026-10-08.

### Decisions and scope

| Target | Stable statement ID | Decision at the full statement's scope | Established result |
|---|---|---|---|
| Q3205 | `ee813378b94c439e788a` | **partial** | Deterministic polynomial-time decision algorithms for each of the inverse, completely regular, and aperiodic subclasses. The aperiodic algorithm also constructs a complete mapping. General and regular recognition are polynomial-time many-one equivalent. The general problem reduces by a polynomial-time conjunctive oracle reduction to completely 0-simple recognition. |
| Q2303 | `1bc2b2da7b69544e14b9` | **partial** | A usable-support reduction and a group-valued gauge obstruction, with a concrete 19-element negative example. The general odd-by-odd case over groups failing Hall–Paige remains unresolved. |

The three polynomial-time subclass results are algorithmic consequences of the structural theory, with the algorithms and running-time arguments supplied here. They are not claimed to be previously unknown structural theorems. In particular, the source already states the structural inverse criterion. Neither an NP-hardness classification nor a P-completeness lower bound is claimed.

The later `quotient_flow_addendum.md` proves an exact subgroup criterion for the entire abelian quotient count-flow relaxation and an exact classification when the usable support is a forest. These strengthen the partial Q2303 result without changing its overall status.

**Exact retained Q3205 statement.** Given the Cayley table of a finite semigroup, decide whether it has a permutation `f` such that `x -> x f(x)` is a permutation, and determine the complexity on regular, inverse, completely regular, completely 0-simple, and aperiodic inputs. The three subclass results retain this decision question exactly and restrict only to the named input promises already present in it.

**Exact retained Q2303 statement.** For finite `G`, nonempty finite `I,Λ`, and a matrix `P` over `G ∪ {0}` with no zero row or column, determine necessary and sufficient structural conditions for `M^0(G,I,Λ,P)` to have a complete mapping, with multiplication as in the handoff. The obstruction below is necessary only; its converse is not asserted.

### Sources and evidence labels

The primary source is J. Araújo, W. Bentz, P. J. Cameron, K. Hendrey, and M. Kinyon, *Complete Mappings of Semigroups*, arXiv:2608.25092v1, 25 August 2026:

- [Paper HTML](https://arxiv.org/html/2608.25092v1).
- [Paper PDF](https://arxiv.org/pdf/2608.25092).
- [Version and bibliographic record](https://arxiv.org/abs/2608.25092).

Problems 15.9 and 15.10 match the handoff. The source's relevant imported characterizations, stated compactly, are these:

1. A finite group has a complete mapping precisely when its Sylow 2-subgroups are trivial or noncyclic (Theorem 1.1, Hall–Paige).
2. A normalized completely simple Rees matrix semigroup has a complete mapping precisely when its group passes Hall–Paige, its number of nonzero H-classes is even, or its normalized matrix has an even-order entry (Theorem 5.1).
3. An inverse semigroup has a complete mapping precisely when every J-class has either a Hall–Paige-good maximal subgroup or an even number of L-classes (Theorem 10.1).
4. For a Rees 0-matrix semigroup, the balanced-support condition is sufficient if its group passes Hall–Paige or at least one index set has even size, and is always necessary (Theorems 6.2 and 7.5).

**Evidence labels:** The complexity deductions and obstruction proofs below are **written argument**; the four imported characterizations are **primary-source comparison**. The 17 example checks are **finite computation**, not an exhaustive classification. There is **no compiled formal theorem**.

### 1. Elementary reductions used by all the algorithms

Let `S` be a finite semigroup. A complete mapping consists of permutations `f,θ` with `θ(x)=x f(x)`.

#### Lemma 1: regularity is necessary

Write `S^1` for `S` with an identity adjoined if needed. Since `θ(x) ∈ xS^1`, successive applications of the permutation `θ` give a cycle of inclusions of principal right ideals. Consequently `θ(x)S^1=xS^1` for every `x`.

The permutation `δ(y)=f^{-1}(y)y` similarly satisfies `S^1δ(y)=S^1y`: apply the same cyclic-inclusion argument to principal left ideals. Fix `x` and put `y=f(x)`. There exist `u,v ∈ S^1` with

`x=xyu` and `y=vxy`.

Associativity gives `x=x(vxy)u=xv(xyu)=xvx`. If `v∈S`, this witnesses regularity. If `v` is the adjoined identity, then `x=x²`, and `x=xxx` gives a witness in `S`. Thus every element is regular. This proof uses only finiteness, associativity, and the two permutation properties.

#### Lemma 2: factorization by J-classes

If `A` is any two-sided ideal, then `θ(A)⊆A`; finiteness and injectivity give equality. Also `f^{-1}(A)⊆θ^{-1}(A)=A`, again forcing equality. Both permutations therefore preserve every ideal and hence each J-class.

For a J-class `J`, form its principal factor `J^0` on `J ∪ {0}` by retaining products inside `J` and replacing all other products by zero. A complete mapping of `S` restricts to a complete mapping of each `J^0`, fixing its newly adjoined zero. Conversely, complete mappings of all the principal factors can be restricted to their nonzero parts and united: their product maps preserve the disjoint J-classes and are bijective on each one.

Here a complete mapping of any semigroup with an absorbing zero necessarily fixes zero. Indeed its product map sends zero to zero. If a different element were mapped to zero by `f`, its product would also be zero, contradicting injectivity.

Therefore `S` has a complete mapping if and only if every `J^0` has one. For regular finite semigroups the principal factors are completely 0-simple. The standard finite Rees structure theorem identifies them with the Rees 0-matrix semigroups in Q2303.

#### Computing these data from a table

Let `N=|S|`. Compute `xS^1`, `S^1x`, and `S^1xS^1` as explicit subsets using the table. Equality gives R-, L-, and J-classes; H is the intersection of R and L. Idempotents satisfy `e²=e`. Regularity is checked by looking for `b` with `aba=a`. All of this uses polynomially many table accesses, with a direct implementation bounded by `O(N³)` for ideal formation and elementary tests.

In a regular J-class, each H-class containing an idempotent is a maximal subgroup. Its identity and multiplication are already visible in the input. A completely regular semigroup is exactly one in which every element's H-class contains an idempotent. An inverse semigroup can be recognized by the uniqueness, for each `a`, of `b` satisfying both `aba=a` and `bab=b`. A finite semigroup is aperiodic exactly when `a^N=a^{N+1}` for all `a`. These tests are polynomial, so the promise subclasses can also be recognized if desired.

### 2. A polynomial Hall–Paige test from a group table

For a group `G` of order `q`, compute the order of each element by repeated multiplication, using at most `q²` table operations. Write `q=2^d u` with `u` odd.

If `d=0`, accept. Otherwise a Sylow 2-subgroup is cyclic exactly when some element order is divisible by `2^d`. One implication follows by taking a generator of the cyclic Sylow subgroup. For the other, an element whose order has full 2-part has a power of order `2^d`, which generates a Sylow 2-subgroup. All Sylow subgroups are conjugate, so testing one is sufficient.

Thus reject precisely when `d>0` and such an element exists; otherwise accept, by Hall–Paige. This avoids enumerating subsets to find Sylow subgroups. A negative certificate is a single element and its order. A positive decision can be checked against the computed element-order list. The decision algorithm does not assert a polynomial construction of complete mappings for arbitrary group tables.

### 3. Q3205: inverse semigroups are in P

For every J-class, choose an idempotent and its maximal subgroup, count the distinct L-classes, and run the preceding group test. Reject if a class has both an odd L-class count and a Hall–Paige-bad maximal subgroup. Accept otherwise.

The source's Theorem 10.1 proves correctness in both directions, with exactly these conditions. All its input invariants are computed polynomially from the given Cayley table. The criterion is not an instruction to solve a separate group recognition problem: the full element-order procedure above supplies that missing algorithmic step.

**Conclusion:** deciding complete-mapping existence for finite inverse semigroups presented by Cayley tables belongs to deterministic P.

### 4. Q3205: completely regular semigroups are in P

Every J-class of a finite completely regular semigroup is completely simple. Let `m` and `n` be its numbers of R- and L-classes, and let `G` be an H-class group with identity `e`, situated in class `(i0,λ0)`. Each H-class is a group and has a unique idempotent.

Choose `e_i` as the idempotent of `(i,λ0)` and `f_λ` as the idempotent of `(i0,λ)`. Form the `G`-valued matrix

`p_{λi}=f_λ e_i`.

This is a normalized sandwich matrix. To check the coordinate claim, take a Rees representation normalized so its `λ0` row and `i0` column consist of the identity. Then `e_i=(i,1,λ0)` and `f_λ=(i0,1,λ)`; their product is `(i0,p_{λi},λ0)`, exactly the middle coordinate of the sandwich entry. Thus the construction recovers the required normalized entries directly from the input table. In particular, every `p_{λi}` lies in the selected maximal subgroup, and its order is already in the group-order list.

Accept a J-class if its group is Hall–Paige-good, if `mn` is even, or if one of these entries has even order. Reject it otherwise. Accept `S` exactly when every class is accepted. Theorem 5.1 and Lemma 2 give both directions.

**Conclusion:** complete-mapping recognition for finite completely regular semigroups presented by Cayley tables belongs to deterministic P.

### 5. Q3205: aperiodic semigroups are in P, with constructions

First reject nonregular inputs by Lemma 1. In a regular aperiodic semigroup every maximal subgroup is trivial. A principal factor has nonzero elements `(i,λ)∈I×Λ` and multiplication

`(i,λ)(j,μ)=(i,μ)` when `Q_{λj}=1`, and zero otherwise.

The support `Q_{λi}` is read directly from the input: it equals one precisely when the H-class `(i,λ)` contains an idempotent. In the aperiodic regular case every H-class is a singleton, so this is simply a square test on its unique element.

Write `m=|I|`, `n=|Λ|`. Build a flow network with source-to-row capacities `m`, row-to-column capacities `mn` at the ones of `Q`, and column-to-sink capacities `n`. Accept the factor exactly when maximum flow is `mn`. Equivalently, require a nonnegative integer matrix `H` supported on `Q`, with every row sum `m` and every column sum `n`.

#### Necessity

A complete mapping has the form `f(i,λ)=(j,μ)`. Count how often each pair `(λ,j)` is used. Every source ending in `λ` occurs once, giving row sum `m`. Every multiplier beginning in `j` occurs once, giving column sum `n`. No selected entry can produce zero, since zero is already the product at zero. Hence the counts are supported on `Q` and supply a feasible flow.

#### Sufficiency and explicit construction

Take an integral flow `H`. For each `λ`, make `h_{λj}` slots labelled `j` and assign its `m` slots bijectively to the `m` indices `i`. A source pair `(i,λ)` now has a chosen compatible `j`.

Build a bipartite multigraph with one vertex set indexed by source first indices `i` and the other by multiplier first indices `j`. Place one edge for every source pair `(i,λ)`, joining `i` to its assigned `j`. Every vertex on either side has degree `n`: on the first side there is one source pair for each `λ`, and on the second side the column sums of `H` equal `n`.

Decompose this regular bipartite multigraph into `n` perfect matchings and label them by `μ∈Λ`. Such a decomposition follows by Hall's theorem: for any vertex subset `A`, counting incident edges gives `n|A|≤n|N(A)|`; remove a perfect matching and repeat. Give each edge its matching label `μ`, and define `f(i,λ)=(j,μ)`.

At each multiplier vertex `j`, every label `μ` occurs once, so `f` is bijective. At each source vertex `i`, every `μ` occurs once, so the products `(i,μ)` are also bijective. This proves sufficiency and constructs a complete mapping. Applying the construction in every J-class and taking the union gives one for the original semigroup.

An infeasible network supplies a minimum-cut/Hall witness: a row subset `A` with `m|A|>n|N_Q(A)|`. Max flow and the repeated matchings are polynomial-time algorithms with integral capacities bounded by `mn≤N`.

**Conclusion:** aperiodic complete-mapping recognition, including nonregular aperiodic inputs, belongs to deterministic P. A complete mapping is also constructible in polynomial time whenever the answer is yes. A conservative common bound for all the elementary table, flow, and matching implementations in this report is `O(N⁴)` elementary operations; no optimal bound is claimed.

### 6. What follows for the unresolved Q3205 subclasses

Every version is in NP: a permutation `f` is a certificate of `O(N log N)` bits and its two permutation properties can be checked in `O(N)` table lookups once read.

General and regular semigroup recognition are polynomial-time many-one equivalent. To reduce general to regular, test regularity; retain a regular input, and replace a nonregular input by the fixed regular no-instance `C2`. Lemma 1 proves that this preserves the answer. The reverse reduction is inclusion of the promised regular class.

To reduce the general problem to completely 0-simple recognition, reject nonregular inputs, form all principal-factor tables, and require that every factor be accepted by the completely 0-simple oracle. Their total number is at most `N`, and their total table length is polynomial. Lemma 2 proves correctness. This is a **conjunctive polynomial-time oracle reduction**, not a claimed many-one reduction to one completely 0-simple instance.

Consequently a polynomial-time algorithm for completely 0-simple recognition would put every finite semigroup case in P. The converse currently supplied here is only the trivial inclusion/oracle direction. The odd-by-odd Rees case over Hall–Paige-bad groups is the residual structural and algorithmic problem. Neither NP membership nor this reduction settles its complexity.

### 7. Q2303: discard support entries that cannot be used

For arbitrary `G`, let `Q` be the nonzero support of `P`, and let `E*` consist of those support entries positive in at least one balanced weighting with row sums `m` and column sums `n`.

**Usable-support lemma.** Replacing every entry outside `E*` by zero preserves complete-mapping existence.

For a complete mapping, let `c_{λj}` count the source elements ending in `λ` whose multiplier begins in `j`. The row and column sums are `m|G|` and `n|G|`. Thus `c/|G|` is a balanced weighting. Any entry used at least once therefore belongs to `E*`. All selected products are retained after the replacement. The reverse implication holds because a complete mapping for the reduced matrix uses only products unchanged in the original one.

The set `E*` is computable in polynomial time. Maximize each edge's weight in the integral transportation network, or test feasibility after imposing a lower bound of one on that edge. A positive feasible real maximum implies a positive integral maximum, by the integral-flow theorem. Therefore the lower-bound test is exact.

This lemma matters because sandwich labels at unusable edges cannot remove any obstruction, regardless of their orders.

### 8. Q2303: a self-contained group-valued gauge obstruction

Let `χ:G→A` be a surjective homomorphism to a finite abelian group, written additively, and put

`Δ=Σ_{g∈G} χ(g)`.

Suppose that `mnΔ≠0` in `A` and that there are elements `a_λ,b_j∈A` satisfying

`χ(p_{λj})=a_λ+b_j` for every `(λ,j)∈E*`.

**Theorem.** Under these hypotheses `M^0(G,I,Λ,P)` has no complete mapping.

**Proof.** Suppose one exists, and let `c_{λj}` be its counts from the preceding lemma. The sums of the `χ`-images of the group coordinates over the source, multiplier, and product permutations are all `mnΔ`. The multiplication rule therefore implies

`mnΔ=2mnΔ+Σ_{λj} c_{λj} χ(p_{λj})`.

Every used entry lies in `E*`, so its last sum equals

`m|G| Σ_λ a_λ + n|G| Σ_j b_j = 0`.

The last equality holds because every element of `A`, a quotient of `G`, is killed by `|G|`. This gives `mnΔ=0`, the required contradiction. ∎

The potential condition can be checked by a graph traversal: assign potentials along a spanning forest of the bipartite support graph and check all remaining edges. Equivalently, every alternating cycle has zero label sum. This is a genuine obstruction theorem; **a nonzero cycle is not proved sufficient**.

For `G=C_{2^d}` and `χ` the identity, `Δ=2^{d-1}`. Hence the theorem applies whenever `m,n` are odd and the usable sandwich labels are potentials. It also applies through a cyclic 2-group quotient with an odd kernel. This includes the standard Hall–Paige-bad group setting, but the theorem itself requires only the displayed homomorphism and needs no classification theorem in its proof.

#### Exact 19-element example

Take `G=C2={0,1}` in additive notation, `I=Λ={0,1,2}`, and

`P = [[0,1,∅], [∅,0,∅], [∅,∅,0]]`,

where `∅` denotes the absorbing-zero entry, distinct from the group identity `0`.

The support has a perfect matching, so it passes the balanced-support test. The entry `p_{0,1}=1` has order two. Nevertheless, every balanced weighting has `h_{1,1}=3`, forcing `h_{0,1}=0`, and then has `h_{0,0}=h_{2,2}=3`. Thus `E*` is exactly the diagonal. Its labels are all zero, `m n Δ=9·1=1` in `C2`, and the theorem proves that the semigroup has no complete mapping.

This disproves the tempting **auxiliary criterion** “balanced support plus one nonzero sandwich entry of even order suffices.” It does **not** disprove Q2303, which asks for a characterization rather than conjecturing that criterion. The same construction works for odd square triangular support over any group with a nontrivial cyclic 2-group quotient of odd-kernel size, provided its diagonal labels are gauge-trivial. All entries above the diagonal are unusable.

### 9. Reproducible verification and unsuccessful search

Run `python recognition.py` in this directory. It uses no third-party dependencies. `recognition_examples.json` contains all 17 exact Cayley tables, subgroup/order data, flow certificates, and constructed aperiodic complete mappings. `recognition_summary.json` records the result: all checks passed, covering 10 inverse cases, 12 completely regular cases, and 6 aperiodic cases, with overlap between classes. Four positive aperiodic cases include explicitly constructed complete mappings whose multiplier and product permutations are checked directly. Associativity is also checked directly on every listed input. The examples include `C1,C2,C3,C4`, the Klein group, `S3`, two bands, a nonregular nilpotent semigroup, Brandt semigroups over `C2` with 1, 2, and 3 indices, two rectangular-group cases, a twisted Rees case, and two aperiodic support cases.

The scripts are implementations and verification examples for the written theorems. Seventeen inputs are not an exhaustive classification and do not replace those proofs.

A separate attempted search, `explore_c2.py`, tested a stronger proposed criterion involving nonzero cycle labels on usable support. It was stopped after **2,000,000 expanded exact-cover nodes plus one budget-stop call**. Only two gauge-trivial negative cases finished; a third case timed out. It found no useful new mathematical result and supplies no evidence for the proposed converse. `c2_raw.json`, `c2_summary.json`, and `c2_timeout_record.json` retain all data. A null decision means unknown, never false. The original console label at the timeout said “MISMATCH”; that reporting defect was corrected, and the summary explicitly records the correction. No counterexample was obtained from that search.

There are no random seeds because both routines are deterministic. No unreported large search or numerical certificate supports any claim in this report. The parent B13 archive should include this entire directory and its SHA-256 manifest.


---

## 9. B13 Q2303: the exact abelian quotient count-flow obstruction

Stable statement ID: `1bc2b2da7b69544e14b9`. Status for Q2303 remains **partial**. Evidence: **written argument**. This addendum completely solves one necessary relaxation, not the complete-mapping problem itself.

### The count-flow relaxation

Let `S=M^0(G,I,Lambda,P)`, `m=|I|`, `n=|Lambda|`, and `M=|G|`. Assume its support admits a balanced weighting, and delete all unusable edges as in the main report. Let `E*` be the remaining support. Fix an onto homomorphism `chi:G→A` to a finite abelian group, written additively. Put

`Delta=sum_{g in G} chi(g)`, `gamma=-mn Delta`.

Give an edge `(lambda,j)` the label `a_lambda_j=chi(p_lambda_j)`. Let `K<=A` be the subgroup generated by alternating sums of labels around all undirected cycles of the bipartite graph `E*`.

A complete mapping necessarily supplies a nonnegative integer matrix `F` on `E*` with row sums `mM`, column sums `nM`, and

`sum_e F_e a_e = gamma` in `A`.

The margin and label equations follow by counting multiplier indices and summing group coordinates, exactly as in sections 7–8 of the main report.

### Theorem

Such an integer count flow exists **if and only if** `gamma∈K`.

The assumption of a balanced weighting is necessary and retained. If it fails, no count flow exists and no complete mapping exists.

#### Proof of necessity

Choose one integral balanced flow `h0` with row sums `m` and column sums `n`. Such a flow exists by integral max flow. The difference `F-M h0` is an integral circulation on the bipartite support, with forward direction from Lambda to I. Integral circulations are integer sums of cycle circulations, so its label sum lies in `K`.

Every element of `A` is killed by `M`, since `A` is a quotient of the group of order `M`. Therefore `M sum_e h0_e a_e=0`, and the label sum of `F-M h0` is `gamma`. This proves `gamma∈K`.

#### Residual cycles generate all relevant label differences

Construct the residual directed graph for `h0`: every usable support edge has a forward arc, with label `a_e`, and every edge with positive `h0_e` has a reverse arc, with label `-a_e`.

The endpoints of every usable edge belong to one strongly connected component of this residual graph. If `h0_e>0`, both arc directions are present. If `h0_e=0`, usability gives another balanced integral flow `h` with `h_e>0`. The difference `h-h0` decomposes into directed residual cycles and one of them uses the forward arc of `e`, giving a return path. Thus each undirected connected component of usable support is strongly connected in the residual orientation.

Let `H` be the subgroup generated by the label sums of directed residual cycles. Clearly `H<=K`. Conversely, a reversed traversal of any residual arc can be replaced, modulo `H`, by a directed return path: the arc followed by that path is a directed closed walk. Replace reversed arcs in an undirected cycle this way. The resulting directed closed walk has the same label sum modulo `H`, hence zero modulo `H`. Thus `K<=H`, and `H=K`.

Every simple directed residual cycle gives a feasible integral flow `h_C` by adding one on its forward arcs and subtracting one on its reverse arcs. Subtraction is legal because every reversed edge has positive integral `h0` weight. Its label difference from `h0` is the cycle voltage. Consequently the set of differences

`D={sum_e (h_C-h0)_e a_e : C a simple directed residual cycle}`

generates `K`.

#### Proof of sufficiency

Since `K` is finite, the directed Cayley graph with generators `D` is strongly connected: inverses of a generator are positive multiples of that generator. If `gamma∈K`, choose a shortest directed path from zero to `gamma`. It uses `L<=|K|-1<=|A|-1<=M-1` generators, say corresponding to feasible flows `h_1,...,h_L`.

Set

`F=(M-L)h0 + h_1 + ... + h_L`.

This is nonnegative and integral and has the required margins. Its label sum is

`M sum_e h0_e a_e + sum_{t=1}^L sum_e(h_t-h0)_e a_e = 0+gamma`.

Hence it is the desired count flow. ∎

### Algorithmic meaning and limits

The subgroup `K` is computable using a spanning forest and its fundamental cycles, followed by subgroup generation in the explicitly represented finite quotient `A`. Its order is at most `M`; therefore subgroup closure is polynomial in the original Cayley-table input size. The theorem decides this necessary relaxation in polynomial time.

In the Hall–Paige-bad case, take the standard cyclic 2-group quotient `A=C_{2^d}` with odd kernel (the Burnside-transfer consequence recorded as Lemma 5.3 of [the primary semigroup paper](https://arxiv.org/html/2608.25092v1)). Then `Delta` is its unique involution `epsilon`. For odd `m,n`, `gamma=epsilon`. Every nontrivial subgroup of a cyclic 2-group contains `epsilon`. Therefore the quotient count-flow relaxation is feasible exactly when some usable support cycle has nonzero voltage. Equivalently, its only obstruction is that all labels are vertex potentials, precisely the gauge obstruction in the main report.

This establishes the limit of that route: satisfying every row/column count and the abelian quotient sum does **not yet construct the required bijections of source, multiplier, and product elements**. No converse for complete mappings is asserted. Thus the relaxation cannot be advertised as the full answer to Q2303 or as a polynomial algorithm for the remaining Q3205 completely 0-simple case.

### An exact additional structural subclass

If the **usable** support graph is a forest, all cycle voltages vanish for every quotient. In particular, for a Hall–Paige-bad group with odd `m,n`, the gauge obstruction rules out complete mappings. Combining this with the source's balanced-support sufficiency for Hall–Paige-good groups or even `mn` gives an exact classification on the forest subclass:

`M^0` has a complete mapping if and only if balanced support exists and either `G` passes Hall–Paige or `mn` is even.

The criterion includes arbitrary labels on the usable forest and arbitrary labels on deleted unusable edges. It remains a subclass result, not the general characterization requested in Q2303.


---

## 10. B13 spectral subreport: exact pair obstruction and Q2290–Q2293

Date: 2026-10-09 UTC. Input: the attached B13 handoff, snapshot 2026-10-08.

### Results and evidence scopes

The principal new result is an explicit slow observable for the base program in Inquiry 30. It gives an all-width lower bound of order `2^w sqrt(w)` on worst-case pair total-variation mixing, and an upper bound `(4+o(1))/(w 2^w)` on the gap of the **additive reversibilization**. The latter is deliberately distinguished from the second-eigenvalue-modulus statistic in the handoff, since the original walk is nonreversible.

Both programs in Inquiry 30 generate the entire symmetric group at every width. Thus pair irreducibility has a complete algebraic proof, not merely the finite check in the handoff. No full solution of the general statements Q2290–Q2293 is claimed.

| B / statement | Stable statement ID | Exact scope returned | Decision | Evidence |
|---|---|---|---|---|
| B13 / Inquiry 30 | not supplied in handoff | `R; +{0,1}` and its extension by a fair independent MSB XOR generate `S_(2^w)` for all `w>=1`; every ordered distinct tuple action is irreducible; pair chains are aperiodic and uniformly stationary | proved | written argument; exact bounded verification |
| B13 / Inquiry 30 | not supplied | Base program has `t_mix,pair(1/4) >= (sqrt(2*pi)/8+o(1)) 2^w sqrt(w)` | proved | written argument; exact bounded verification |
| B13 / Inquiry 30 | not supplied | Base program's additive-reversibilization gap is at most the exact popcount Rayleigh quotient below, asymptotic to `4/(w2^w)` | proved | written argument; exact bounded verification |
| B13 / Inquiry 30 | not supplied | Modulus gaps in the two original nonreversible kernels, widths 2 through 8 | partial | finite floating-point computation |
| B13 / Q2290 | `cb376eb93c0b5497e6fb` | Arbitrary hypergraphs on at most three vertices; larger graphs plus a whole-vertex hyperedge also reduce to the graph theorem | partial | written reduction; primary-source comparison |
| B13 / Q2291 | `576df523032c0668f39e` | General weighted hypergraphs remain unproved here; source establishes mean-field and codimension-one cases | unresolved | primary-source comparison |
| B13 / Q2292 | `3430a4c6c2d41614aa1a` | General odd-sector ordering remains unproved here; codimension-one case is established in source | unresolved | primary-source comparison |
| B13 / Q2293 | `6e840638a5684077278e` | Every `n>=2`, every positive `alpha`, and equal positive edge weights on the complete graph: exact gap is `c sum(alpha)`, attained in degree one | partial | written argument; primary-source comparison |

No compiled formal theorem was produced. Finite spectral calculations are not interval certificates, and no finite computation is promoted to a theorem outside its enumerated range.

### 1. All-width group generation

Let `N=2^w`, `M=N-1`, and let permutations of `X={0,...,N-1}` act by composition from right to left. Write

\[
T(x)=x+1\pmod N,
\qquad R(x)=\lfloor x/2\rfloor+(N/2)(x\bmod2).
\]

The two maps in the base kernel are `R` and `TR`. Their generated group contains `T=(TR)R^{-1}`, so it equals `<R,T>`.

For `w>=2`, direct evaluation gives

\[
RT^2R^{-1}=(0\;1\;\cdots\;N/2-1)
             (N/2\;N/2+1\;\cdots\;N-1).
\]

Consequently,

\[
(RT^2R^{-1})T^{-1}=(0\;N/2).
\]

Conjugating this transposition by `R^(w-1)` gives `(0 1)`. Conjugating `(0 1)` by the powers of the full cycle `T` gives all adjacent transpositions, and these generate `S_N`. For `w=1`, `R` is the identity and `T` itself generates `S_2`.

In a finite permutation group, the semigroup generated by the support already contains the inverses, since the inverse of a permutation is a nonnegative power of it. Therefore all states in each ordered-distinct-`k`-tuple space communicate, for every `1<=k<=N`.

The extended kernel includes `R` and `TR` among its four maps and hence has the same generation conclusion. Both pair kernels have a self-loop at `(0,N-1)` coming from `R`. Thus irreducibility gives pair aperiodicity. Uniform measure is stationary because every update is a permutation of the pair space.

### 2. A carry-boundary observable

Throughout the next two sections the kernel is the **base** program, with a fair independent choice between `R` and `TR` at each step. Let

\[
\mathcal X=\{(x,y)\in X^2:x\ne y\},\qquad
\pi(x,y)=\frac1{N(N-1)},
\]

and define

\[
\delta(x,y)=(x-y)\pmod M\in\{0,\ldots,M-1\},
\qquad H(x,y)=\operatorname{popcount}(\delta(x,y)).
\]

#### Rotation invariance

For all `x`,

\[
R(x)\equiv (N/2)x\pmod M.
\]

Multiplication by `N/2` modulo `M=2^w-1` is cyclic right rotation of the `w` binary digits. It follows that

\[
H(Rx,Ry)=H(x,y).
\]

If neither coordinate is `M`, simultaneous translation by one changes neither residue difference nor `H`. The only exceptional pairs are

\[
(M,y),\quad 0\le y<M,
\qquad (x,M),\quad 0\le x<M.
\]

For the first family, `delta` decreases by one modulo `M`; for the second, it increases by one. Each family runs through every residue exactly once. This is an exact description of the carry boundary which breaks the rotation invariant.

#### The residue distribution

Among all ordered distinct pairs, the residue `0` has exactly two preimages, `(0,M)` and `(M,0)`. Every nonzero residue has exactly `N+1` preimages. One way to count is to regard the list `0,...,M` as all residues modulo `M` with one extra copy of zero: convolution gives `M+2=N+1` for each nonzero difference. At zero difference the pairs with equal integer coordinates are deleted, leaving two.

Thus the following moment identities hold:

\[
\mathbb E_\pi H=\frac w2-\frac{w}{N(N-1)},
\]

\[
\operatorname{Var}_\pi H=
\frac w4-\frac{w(w-1)}{2(N-1)}
-\frac{w^2}{N^2(N-1)^2}.
\tag{2.1}
\]

For verification, the sums over all `w`-bit words are `sum popcount=wN/2` and `sum popcount^2=w(w+1)N/4`; remove the all-one word, then apply the preimage multiplicities above.

#### Exact energy

Let `h(d)=popcount(d)` for `0<=d<M`, with residue arithmetic modulo `M`. Then

\[
\sum_{d=0}^{M-1}[h(d+1)-h(d)]^2=2(N-w-1).
\tag{2.2}
\]

For an elementary derivation, the corresponding sum around the full binary cycle `0,...,N-1` is `2N-2`, obtained by classifying a word according to its number of trailing ones. Removing the all-one word replaces the last two squared increments `1+w^2` by `(w-1)^2`, giving (2.2).

Since only the two exceptional families contribute and translation is chosen with probability one half,

\[
\mathcal E_P(H,H)
:=\langle H,(I-P)H\rangle_\pi
=\frac12\mathbb E_\pi[(H(X_1)-H(X_0))^2]
=\frac{N-w-1}{N(N-1)}.
\tag{2.3}
\]

The identity uses stationarity, not reversibility. The quadratic form is that of the additive reversibilization `P_a=(P+P*)/2`. Its spectral gap consequently satisfies, for every `w>=2`,

\[
\gamma(P_a)\le
\frac{(N-w-1)/(N(N-1))}
{w/4-w(w-1)/(2(N-1))-w^2/(N^2(N-1)^2)}
=\frac{4+o(1)}{w2^w}.
\tag{2.4}
\]

This proves the existence of a slowly varying pair observable and rules out a uniform Poincare gap for the reversible symmetrization. It is **not** a proof of an upper bound on `1-max{|lambda|:lambda!=1}` for the nonnormal original matrix.

### 3. An exponential-in-width lower bound for pair independence

There is a stronger direct mixing consequence, not dependent on spectral normality. Put

\[
r=\lfloor(w-1)/2\rfloor,
\qquad B_w(r)=\sum_{j=0}^{r}\binom wj,
\qquad A=\{(x,y):H(x,y)\le r\}.
\]

The exact stationary mass is

\[
p_w=\pi(A)=
\frac{(N+1)B_w(r)-(N-1)}{N(N-1)}.
\tag{3.1}
\]

Replace `A` by its complement when necessary, so its mass is `a_w=min(p_w,1-p_w)`. Stationarity implies that the flux is unchanged by this replacement.

An ordinary increment `d -> d+1` can increase binary weight by at most one. It crosses from weight at most `r` to weight greater than `r` precisely when `d` is even and has exactly `r` ones. There are `binom(w-1,r)` such residues. The number of downcrossings equals the number of upcrossings around the residue cycle. Combining the two exceptional families with the fair translation coin gives the exact stationary flux

\[
Q(A,A^c):=\sum_{z\in A}\pi(z)P(z,A^c)
=\frac{\binom{w-1}{r}}{N(N-1)}=:q_w.
\tag{3.2}
\]

Start the pair chain from `pi` conditioned on `A`. At each time its density relative to `pi` is at most `1/a_w`. A union bound over the first transition from `A` to its complement yields

\[
\Pr_{\pi(\cdot\mid A)}(X_t\in A^c)
\le tq_w/a_w.
\]

Consequently, by testing membership in `A`,

\[
d_{\rm worst}(t)
\ge 1-a_w-tq_w/a_w.
\tag{3.3}
\]

This implies the exact lower threshold

\[
t_{\rm mix}(1/4)\ge
\left\lceil\frac{a_w(3/4-a_w)}{q_w}\right\rceil.
\tag{3.4}
\]

Here the right side follows because every integer strictly below the unrounded threshold has distance greater than one quarter. The worst-state bound follows from the conditioned-mixture bound by convexity of total variation.

The elementary central-binomial asymptotics give `a_w -> 1/2` and

\[
q_w=\frac{1+o(1)}{2^w\sqrt{2\pi w}}.
\]

Therefore

\[
t_{\rm mix,pair}(1/4)
\ge\left(\frac{\sqrt{2\pi}}8+o(1)\right)2^w\sqrt w.
\tag{3.5}
\]

The same lower bound applies to every ordered-`k`-tuple chain with `k>=2` for the base program, by projection onto its first two entries. In particular, this fixed program cannot produce uniform worst-case approximate pair independence in depth polynomial in `w`. The slow observable is not an exact invariant, consistent with full symmetric-group generation.

### 4. Bounded spectral experiment and revised hypotheses

The attached `pair_walk.py` constructs the full ordered-pair transition matrix for each width `2<=w<=8`, for both precisely specified kernels. The second program uses an **MSB** XOR bit, matching the handoff's displayed measurements; an LSB XOR bit is a different program.

Matrices are exact up to their entries, which are dyadic probabilities. Eigenvalues use double-precision ARPACK, six largest-modulus candidates, tolerance `1e-11`, maximum `50000` iterations, and a fixed initialization seed `13008`. All communicating classes are checked by a directed strongly-connected-components computation. This is floating-point evidence, not a certified exhaustive ordering of the spectrum. Full output includes residuals and is saved in `pair_output.json` and `pair_output.jsonl`.

| w | Base modulus gap | `w 2^w gap` | Extra MSB XOR modulus gap | `w^2 gap` |
|---:|---:|---:|---:|---:|
| 4 | 0.0448167244083 | 2.86827036213 | 0.102145595325 | 1.63432952520 |
| 5 | 0.0194132018608 | 3.10611229773 | 0.0633467120767 | 1.58366780192 |
| 6 | 0.00845033533603 | 3.24492876904 | 0.0431759722156 | 1.55433499976 |
| 7 | 0.00370577225297 | 3.32037193866 | 0.0317791200541 | 1.55717688265 |
| 8 | 0.00163991511810 | 3.35854616188 | 0.0247125811242 | 1.58160519195 |

For the base program, the dominant returned nonconstant eigenvalue is real positive throughout this displayed range. Its right eigenvector has absolute correlation with centered `H` of approximately `0.90, 0.95, 0.96, 0.94, 0.93`, respectively. This supports the carry-boundary explanation, but `H` is not asserted to be an exact eigenfunction.

**Working hypotheses, not results:** the base modulus gap may scale as a constant times `1/(w2^w)`; the extra-XOR modulus gap may scale as a constant times `1/w^2`. Both fit the bounded data more plausibly than the two plain exponential laws suggested in the handoff. The extra-XOR dominant eigenvalues have arguments near nontrivial `w`th roots of unity; at width eight the returned eigenvalue is `-0.9752874188758`. A proposed explanation must therefore account for rotation-phase persistence, not only a real slow mode.

### 5. Q2290–Q2293: retained scopes and exact partial results

#### Q2290: `cb376eb93c0b5497e6fb`

The full assertion asks for equality of the one-label and interchange gaps on every weighted hypergraph. [Alon–Kozma–Puder, Theorem 1.3](https://arxiv.org/pdf/2311.02505) proves the family in which every positive-weight hyperedge contains one fixed set `B` and has at most two vertices outside `B`. This includes the graph theorem when `B` is empty. Its general hypergraph conjecture remains broader.

An explicit reduction also handles every hypergraph on `n<=3`: singleton and empty updates are identity operations, the two-element updates give an ordinary weighted graph interchange process, and the remaining full-set update has generator `c(I-Pi)`, where `Pi` projects to constants. It therefore adds the same number `c` to every nonconstant eigenvalue of both the interchange and one-label generators. The graph gap equality gives the claimed equality. The same reduction works on any number of vertices when the only effective hyperedges are pairs and the entire vertex set. If the pair graph is disconnected, both second eigenvalues before the full-set update are zero, so the argument still holds.

**Retained exact general statement: unresolved; restricted family above: proved.**

#### Q2291: `576df523032c0668f39e` and Q2292: `3430a4c6c2d41614aa1a`

[Alon–Puder](https://arxiv.org/pdf/2603.00353), Theorems 1.4–1.5, proves Q2291 for mean-field weights and for weights supported on subsets of size at least `n-1`. Corollary 4.15 proves the odd and even subsequence orderings for codimension-one subsets. These are restricted cases, not solutions of the two universal quantifiers in the handoff.

The September manuscript [Caputo–Quattropani–Sau](https://arxiv.org/abs/2609.10450), §1.4.6 and Remark 2.10, explicitly retains the full unitary-group question and odd-index ordering. Its KMP degree-two reduction and even-index monotonicity do not resolve either requested target. For direct inspection, its author manuscript is available as [public full text](https://www.researchgate.net/publication/414159952_Aldous'_spectral_gap_phenomena_in_stochastic_exchange_models).

**Both retained exact general statements: unresolved here.**

#### Q2293: `6e840638a5684077278e`

The same September manuscript, §1.4.6, distinguishes Brownian energy diffusion from its proved exchange models: the general degree-two BEP reduction is retained as open. It records the known one-particle result when every `alpha_x>=1` and an asymptotic two-particle result as all parameters vanish proportionally. Neither closes the handoff's arbitrary-positive-parameter question.

There is a direct complete solution on complete graphs with a common edge weight `c>0`, for all positive parameter vectors. Set `A=sum_i alpha_i`. In the coordinates `eta_1,...,eta_(n-1)`, with `eta_n=1-sum_(i<n)eta_i`, the generator becomes

\[
Lf=c\left[
\sum_{i<n}(\alpha_i-A\eta_i)\partial_i f
+\sum_{i,j<n}\eta_i(\mathbf1_{i=j}-\eta_j)\partial_i\partial_j f
\right].
\tag{5.1}
\]

Let `P_r` be the polynomials of degree at most `r` in these independent coordinates. The generator preserves `P_r`. On its degree-`r` homogeneous quotient the Euler identities give the scalar action

\[
L=-c\,r(r-1+A)I\pmod{P_{r-1}}.
\]

Since `L` is self-adjoint in `L^2(Dir(alpha))`, the subspace

\[
\mathcal H_r=P_r\cap P_{r-1}^{\perp}
\]

is invariant. For `f` in this subspace, both `Lf` and `f` are orthogonal to `P_(r-1)`, while `Lf+c r(r-1+A)f` belongs to `P_(r-1)`. Their intersection is zero, so

\[
Lf=-c\,r(r-1+A)f\qquad(f\in\mathcal H_r).
\]

Polynomials are dense in the continuous functions on the compact simplex, and hence in this `L^2` space. Thus the orthogonal polynomial eigenspaces form a complete eigenbasis. The nonconstant eigenvalues of `-L` are exactly

\[
c\,r(r-1+A),\qquad r=1,2,\ldots,
\]

with multiplicity `binom(n+r-2,r)`. Their minimum is `cA`, attained by, for example, `eta_i-alpha_i/A`. This proves the requested degree-two conclusion, with the stronger degree-one statement, throughout this restricted family. Every connected two-site graph belongs to this family; its eigenfunctions are the usual beta-weighted orthogonal polynomials.

**Retained exact general statement: unresolved; complete graph with a common positive edge weight: proved.**

### 6. Replay files

* `pair_walk.py`: complete pair transition construction and bounded spectral diagnostics.
* `pair_output.json`, `pair_output.jsonl`: full raw floating-point results.
* `verify_pair_identities.py`: exact rational checks of the group identity, moments, energies, and cut fluxes, widths two through twelve.
* `exact_pair_identities.json`: full exact output.

Run `python pair_walk.py --max-width 8 --output pair_output.json` and `python verify_pair_identities.py`. The archived input and archive-wide SHA-256 manifest are supplied by the coordinating report.


---

## 11. Exact original-question register and remaining work

The question text below is copied from the user-supplied attachment. Its definitions and source setups are retained in the archived original handoff and explicitly repeated wherever used in a proof above. Every stable ID is preserved. The numerical recovery label Q2494 remains provisional.


### B13 / Q1285: Cutoff with extreme reservoir densities

**Stable statement ID:** 901c05b15569f039ac00. **Decision:** unresolved.

**Exact retained statement.** On {1,…,N}, each nearest-neighbor edge exchanges its endpoint contents at rate N², and each boundary endpoint independently resets at rate N² to a Bernoulli value of density p_N or q_N. Assume p_N,q_N∈[0,1] and q_N≤min{p_N,1−p_N}. Does worst-case total-variation cutoff occur at π⁻² log[N/(√(Np_N)∨1)] for every such density sequence?

**Result.** No new exact-scope result established in this return.

**Remaining scope.** The entire retained question remains unresolved in this return.


### B13 / Q1286: Product-condition cutoff with unequal reservoirs

**Stable statement ID:** cc2c43f786837e4b7aa2. **Decision:** unresolved.

**Exact retained statement.** Consider connected n-site networks with symmetric exchange rates c_ij≥0 and Bernoulli resets at rates κ_i≥0, not all zero, whose densities lie in [δ,1−δ] for fixed δ>0. Let λ_n be the least eigenvalue of diag(κ_i+Σ_j c_ij)−(c_ij). Is worst-case total-variation cutoff equivalent to λ_n t_mix(ε)→∞ for fixed ε∈(0,1)?

**Result.** No new exact-scope result established in this return.

**Remaining scope.** The entire retained question remains unresolved in this return.


### B13 / Q1290: Separation cutoff for positively biased shuffles

**Stable statement ID:** dd1e1530c8b22bbf943a. **Decision:** partial.

**Exact retained statement.** For every fixed α>0 with α≠1, does this walk on S_n have separation-distance cutoff at t_n,α log n, as n→∞?

**Result.** Separation cutoff proved for every fixed 0<alpha<1; alpha>1 remains unresolved.

**Remaining scope.** The interval alpha>1; no optimal additive separation window is established.


### B13 / Q1291: Total-variation cutoff for biased signed shuffles

**Stable statement ID:** cc27e5d9e60fdad839fa. **Decision:** proved.

**Exact retained statement.** On signed permutations B_n, follow each transposition by a fair coin: on tails flip both selected cards, or flip the single card once if i=j. For every fixed nonzero α∈R, is there total-variation cutoff at t_n,α log n?

**Result.** Total-variation cutoff at tau_n log n for every fixed real alpha, including the full requested nonzero range.

**Remaining scope.** Nothing remains at the original cutoff scope; an optimal window or full profile is not asserted.


### B13 / Q1405: Constant-factor cost of conjugacy in dominating sets

**Stable statement ID:** 2f935b9be6f6cf5e6ab9. **Decision:** unresolved.

**Exact retained statement.** Does an absolute c>0 satisfy γ_u(G)≤c·γ_t(G) for every finite nonabelian simple group G?

**Result.** No new exact-scope result established in this return.

**Remaining scope.** The entire retained question remains unresolved in this return.


### B13 / Q1406: Bounded ratio between spread and uniform spread

**Stable statement ID:** db6847d81b588f311dee. **Decision:** unresolved.

**Exact retained statement.** Does an absolute c>0 satisfy s(G)≤c·u(G) for every finite nonabelian simple group G?

**Result.** No new exact-scope result established in this return.

**Remaining scope.** The entire retained question remains unresolved in this return.


### B13 / Q1407: Exact spread of odd-degree alternating groups

**Stable statement ID:** f360f758c8bcd6664901. **Decision:** unresolved.

**Exact retained statement.** Determine s(A_n) and u(A_n) for all odd n≥5.

**Result.** No new exact-scope result established in this return.

**Remaining scope.** The entire retained question remains unresolved in this return.


### B13 / Q1408: Exact spread of rank-one linear groups

**Stable statement ID:** 85e1bb57b7e9ea21e1fe. **Decision:** unresolved.

**Exact retained statement.** Determine s(PSL₂(q)) and u(PSL₂(q)) for prime powers q≥11 with q≡3 mod 4.

**Result.** No new exact-scope result established in this return.

**Remaining scope.** The entire retained question remains unresolved in this return.


### B13 / Q1492: Infinite interchange cycles in lower dimensions

**Stable statement ID:** 93a2d63b2ddcbb351782. **Decision:** unresolved.

**Exact retained statement.** For each d∈{3,4}, does there exist β₀(d)<∞ such that π_β almost surely has an infinite cycle for every fixed β>β₀(d)?

**Result.** No new exact-scope result established in this return.

**Remaining scope.** The entire retained question remains unresolved in this return.


### B13 / Q1493: Finiteness of planar interchange cycles

**Stable statement ID:** 543094642ca56218b341. **Decision:** unresolved.

**Exact retained statement.** For d=2 and every fixed β>0, does π_β almost surely have only finite cycles?

**Result.** No new exact-scope result established in this return.

**Remaining scope.** The entire retained question remains unresolved in this return.


### B13 / Q1494: A single high-dimensional interchange transition

**Stable statement ID:** b5ad443ffe0eac2e6b5c. **Decision:** unresolved.

**Exact retained statement.** For each d≥5, is there β_c∈(0,∞) such that π_β almost surely has only finite cycles for β<β_c and has infinite cycles for β>β_c?

**Result.** No new exact-scope result established in this return.

**Remaining scope.** The entire retained question remains unresolved in this return.


### B13 / Q1589: Nonequilibrium exclusion cutoff profile

**Stable statement ID:** b8d510fafe6e359a7aa3. **Decision:** disproved.

**Exact retained statement.** For the rate-N² segment SSEP, fix p, q∈(0, 1), q≤min{p, 1−p}, p≠q. Put S(x)=Σ_u x(u), t_N(b)=(log N)/(2π²)+b/π², and let π_N be stationary. Does there exist f_pq>0 with (E_1 S(X_{t_N(b)})−E_{π_N}S)/√Var_{π_N}S→f_pq e^(−b) and worst-case TV distance at t_N(b) tending to TV(N(0, 1), N(f_pq e^(−b), 1)) for every b∈R?

**Result.** The proposed unweighted-count Gaussian profile is false: p=1/2, q=1/4 gives a strictly larger sine-statistic TV lower bound.

**Remaining scope.** The original formula is refuted; the correct nonequilibrium profile and a matching upper bound are not determined.


### B13 / Q1895: Sukhatme fixed points

**Stable statement ID:** 4faaafa325700071ea75. **Decision:** proved.

**Exact retained statement.** Determine centering, scaling and a nondegenerate limiting distribution for F_n as n→∞.

**Result.** (F_n-(log n)/e)/sqrt((log n)/e) converges in distribution to N(0,1); E F_n=(log n)/e+O(1).

**Remaining scope.** Nothing remains at the requested centering/scaling/limit-law scope; no Poisson TV approximation, exact bounded mean correction, or variance asymptotic is asserted.


### B13 / Q1896: Sukhatme cycle count

**Stable statement ID:** 25f5bc9a09e2c4ffa329. **Decision:** partial.

**Exact retained statement.** Determine centering, scaling and a nondegenerate limiting distribution for C_n as n→∞.

**Result.** C_n>=(1-o_P(1))log n; E C_n>=log n-O(1); limsup E C_n/(log n)^2<=1/2. No limiting distribution.

**Remaining scope.** Centering, fluctuation scale and a limiting distribution for the total cycle count; the path-head compensator is not sharply evaluated.


### B13 / Q1897: Sukhatme increasing subsequences

**Stable statement ID:** c0e5e644929150cddbda. **Decision:** unresolved.

**Exact retained statement.** Determine centering, scaling and a nondegenerate limiting distribution for L_n as n→∞.

**Result.** No new exact-scope result established in this return.

**Remaining scope.** The entire retained question remains unresolved in this return.


### B13 / Q2198: Product criterion on bounded-step nilpotent groups

**Stable statement ID:** 9e2e29797ab8b0f064b5. **Decision:** unresolved.

**Exact retained statement.** For every sequence of finite nilpotent groups of uniformly bounded nilpotency class and arbitrary generating sets, does γ t_mix(1/4)→∞ imply cutoff?

**Result.** No new exact-scope result established in this return.

**Remaining scope.** The entire retained question remains unresolved in this return.


### B13 / Q2290: One-label hypergraph spectral gap

**Stable statement ID:** cb376eb93c0b5497e6fb. **Decision:** partial.

**Exact retained statement.** Must λ₂(L_IP)=λ₂(L_RW) for every such weighted hypergraph?

**Result.** Gap equality for hyperedges restricted to pairs and the full vertex set, including every n<=3 instance.

**Remaining scope.** Arbitrary weighted hypergraphs outside the stated restricted family.


### B13 / Q2291: Two representations control unitary gaps

**Stable statement ID:** 576df523032c0668f39e. **Decision:** unresolved.

**Exact retained statement.** Is inf_{ρ nontrivial} λ_ρ=min{ω₁,ω₂} for every such weighted hypergraph?

**Result.** No new exact-scope result established in this return.

**Remaining scope.** The full unitary representation infimum for arbitrary weighted hypergraphs.


### B13 / Q2292: Odd-sector spectral ordering

**Stable statement ID:** 3430a4c6c2d41614aa1a. **Decision:** unresolved.

**Exact retained statement.** Must ω₁≤ω₃≤ω₅≤⋯ hold for every such weighted hypergraph?

**Result.** No new exact-scope result established in this return.

**Remaining scope.** The odd-sector ordering for arbitrary weighted hypergraphs.


### B13 / Q2293: Quadratic Brownian-energy gap

**Stable statement ID:** 6e840638a5684077278e. **Decision:** partial.

**Exact retained statement.** For every such α and w, is the spectral gap attained by a nonconstant polynomial in η of degree at most two?

**Result.** Common positive edge weights on the complete graph: gap=c sum(alpha), attained in degree one for all positive alpha.

**Remaining scope.** General connected edge weights with arbitrary positive parameter vectors.


### B13 / Q2303: Complete mappings of Rees zero-matrix semigroups

**Stable statement ID:** 1bc2b2da7b69544e14b9. **Decision:** partial.

**Exact retained statement.** Give necessary and sufficient structural conditions on finite G,I,Λ,P for M⁰=(I×G×Λ)∪{0} to admit a complete mapping, where G is a group, I,Λ≠∅, P∈(G∪{0})^(Λ×I) has no zero row/column, and (i,g,λ)(j,h,μ)=(i,gp_(λj)h,μ) if p_(λj)≠0, otherwise 0; zero is absorbing.

**Result.** Usable-support reduction, abelian obstruction and exact count-flow relaxation; exact classification on usable forests.

**Remaining scope.** A necessary-and-sufficient characterization in the general Rees zero-matrix case; quotient count feasibility does not supply the required bijections.


### B13 / Q2494: Optimal connected-complement gap exponent

**Stable statement ID:** 20d1798f558ecef53b7b. **Decision:** unresolved. **Numbering is provisional.**

**Exact retained statement.** Determine the smallest p for which some c_p>0 satisfies gap(G)+gap(Ḡ)≥c_p n^{−p} for every n-vertex G with both G and Ḡ connected.

**Result.** No new exact-scope result established in this return.

**Remaining scope.** The entire retained question remains unresolved in this return.


### B13 / Q2529: Uniform expansion of primitive origami orbit graphs

**Stable statement ID:** 3f09875aa32e6fb5d8a6. **Decision:** unresolved.

**Exact retained statement.** Is there ε>0 such that every such orbit graph G in H(2) has |∂_E A|≥ε|A| whenever 0<|A|≤|V(G)|/2, uniformly over n?

**Result.** No new exact-scope result established in this return.

**Remaining scope.** The entire retained question remains unresolved in this return.


### B13 / Q2601: Optimal greedy-base ratio

**Stable statement ID:** 22c5b3891653baeb4e4b. **Decision:** unresolved.

**Exact retained statement.** Determine sup_G g(G)/b(G). Is its value 4/3?

**Result.** No new exact-scope result established in this return.

**Remaining scope.** The entire retained question remains unresolved in this return.


### B13 / Q2602: Asymptotic greedy-base ratio

**Stable statement ID:** 308eab8632988c80391e. **Decision:** unresolved.

**Exact retained statement.** Determine limsup_(k→∞) sup{g(G)/b(G): b(G)=k}. Is its value 9/8?

**Result.** No new exact-scope result established in this return.

**Remaining scope.** The entire retained question remains unresolved in this return.


### B13 / Q2603: Quadratic-rank irredundant-base bound

**Stable statement ID:** b51b1715c73663fb2403. **Decision:** unresolved.

**Exact retained statement.** Is there an absolute constant C such that I(G,Ω)≤Cr²+Ω(e) for every such G and action?

**Result.** No new exact-scope result established in this return.

**Remaining scope.** The entire retained question remains unresolved in this return.


### B13 / Q2662: Smallest matching-scheme spectral gap

**Stable statement ID:** 3aaf2060b2cc3217f8e1. **Decision:** proved.

**Exact retained statement.** For every n≥5 and μ⊢n with μ≠1^n, is λ₁(A_μ)−λ₂(A_μ)≥2n−1, the gap attained by μ=(2,1^{n−2})?

**Result.** Every nonidentity perfect-matching relation has adjacency gap at least 2n-1 for all n>=5.

**Remaining scope.** Nothing remains at the original minimum-gap scope; the exact second eigenvalue for every relation is not claimed.


### B13 / Q2664: Balanced whirling of repeated surjections

**Stable statement ID:** 3f3121a42f7e5c02851a. **Decision:** proved.

**Exact retained statement.** Let n,k,m≥1 with n≥mk. On functions f:[n]→[k] with every fibre of size ≥m, w_i repeatedly increments f(i) cyclically modulo k until admissible again. Does every orbit of w_n∘⋯∘w₁ average |f⁻¹(j)| to n/k for each j∈[k]?

**Result.** Every repeated-surjection whirling orbit has each fibre average n/k, proved by an explicit coboundary.

**Remaining scope.** Nothing remains at the original orbit-average scope.


### B13 / Q2665: Asymptotic homomesy on a slab

**Stable statement ID:** 39dd68d5345401fd90b1. **Decision:** proved.

**Exact retained statement.** For each integer n≥1 and real r with 0≤r≤n/2, put P={x∈[0,1]^n:r≤Σx_i≤n−r}. The toggle t_i replaces x_i by max(0,r−s)+min(1,n−r−s)−x_i, where s=Σ_{j≠i}x_j. For every permutation π and x∈P, does N⁻¹Σ_{j=0}^{N−1}Σ_i(T_π^j x)_i→n/2, where T_π=t_{π(n)}∘⋯∘t_{π(1)}?

**Result.** Every real slab orbit has average n/2, with uniform error <=(n-r)/(2N).

**Remaining scope.** Nothing remains at the original real-slab time-average scope.


### B13 / Q3205: Complexity of recognizing complete mappings

**Stable statement ID:** ee813378b94c439e788a. **Decision:** partial.

**Exact retained statement.** What is the computational complexity, with the Cayley table as input, of deciding whether a finite semigroup has a complete mapping? Determine it also for regular, inverse, completely regular, completely 0-simple and aperiodic semigroups.

**Result.** Deterministic P for inverse, completely regular, and aperiodic semigroups; aperiodic positive instances have constructive certificates.

**Remaining scope.** Full complexity classification for general, regular, and completely 0-simple semigroups; no NP-hardness or P-completeness claim.


## 12. Unresolved questions: precise status

No exact-scope resolution is established here for Q1285–Q1286; Q1405–Q1408; Q1492–Q1494; Q1897; Q2198; Q2291–Q2292; provisional Q2494; Q2529; and Q2601–Q2603.

The signed-shuffle argument does not transfer to extreme-density reservoir cutoff or the unequal-reservoir product criterion. The fixed-point and cycle bounds do not determine the increasing-subsequence statistic. Finite matching-scheme comparison does not settle interchange-cycle phase transitions on infinite lattices. Neither the carry observable nor a reversible Poincare inequality establishes the bounded-step nilpotent-group product criterion. The hypergraph source comparisons do not close the universal unitary-representation or odd-sector assertions. No new exact extremal value, universal group-theoretic bound, or origami expansion theorem is supplied for the remaining algebraic and geometric questions.

These are limitations of this return. They are not assertions that exhaustive current literature searches were completed for all 18 questions.

## 13. Verification and provenance

All computational domains, seeds, budgets, algorithms, and evidence roles are recorded in the JSON ledger and VERIFICATION_README.md. Source proofs and computed controls are both included. The exact matching exception at n=5 is independently replayable by integer arithmetic; the floating-point eigenvalue outputs are not interval certificates.

The verification archive includes an internal MANIFEST.sha256 and verify_archive.py. The separately delivered B13_SHA256.txt records hashes of the three principal deliverables. The manifest verifies file integrity; it does not verify the mathematical arguments.

The original handoff has SHA-256:

c5c6d650d73941c8e8d1f0beb717ceee734f1f1bd2e5d7e4bca04294caa98b25

The archived file inputs/B13_Original_Handoff.md preserves its bytes. No source attachment or external catalog was edited.
