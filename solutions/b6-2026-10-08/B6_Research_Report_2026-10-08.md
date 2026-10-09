# Results and evidence status

This report provides complete written proofs of four exact retained statements, partial results for four further statements, and an executable protocol for the academic-genealogy application. The four exact results are **Q1886, Q1887, Q1888, and Q2399**. The principal partial result determines the height fluctuations of the limited-memory tree for every fixed $0<\beta<1/2$; its parent question asks for all $0<\beta<1$ and therefore remains partial.

“Proved” in the ledger means that a complete written argument appears in this report, including its dependency lemmas and quantifiers. The four exact proofs and the height fluctuation argument were checked independently within this session. These checks are mathematical reviews, not a compiled proof-assistant theorem, external peer review, or a claim of publication priority. Finite computations are labelled separately and supply no asymptotic proof. The original handoff's dated reports of open status remain historical provenance; this report does not claim a comprehensive current literature certification for every unresolved entry.

The attachment is the authority for the 21 retained formulations and their stable IDs. Appendix A reproduces those statements exactly. The accompanying JSON ledger records the exact wording, assumptions, status, proof location, primary-source comparison, executed checks, and remaining gap for every entry. The three recovery-draft question numbers retain their provisional status.

## Four exact statements with complete proofs

### Complete friend-tree hub mass: Q1888

**Stable statement ID:** `7e728675d1726f7676ee`.

In the exact random-friend model of the handoff,

\[
\sum_{i\ge1}Z_i=1\qquad\text{almost surely}.
\]

The argument tracks leaves attached to labels larger than a fixed cutoff. If $N_n$ counts nonleaves, the normalized tail mass has conditional drift at most $N_n/[n(n+1)]$. The published almost-sure polynomial bound on $N_n$ makes that drift summable. Localization converts the pathwise bound into a usable expectation estimate and rules out mass escaping to ever-later labels. The proof also works under the more general condition $\sum_n N_n/[n(n+1)]<\infty$ almost surely. Its essential literature input is the polynomial nonleaf bound in *Random friend trees*, Theorem 4.7 [S1].

Consequences proved in the same chapter include $\ell^1$ convergence of leaf-neighbor mass, excess-degree mass, and nonleaf-degree mass to $(Z_i)$; total-variation convergence of the conditional attachment-label distribution to $(Z_i)$; and a conditional limiting distance law for two uniform vertices. Typical distances are tight. No finite limiting mean distance or unique largest hub is asserted.

### Uniform limit with many internal entries: Q1887

**Stable statement ID:** `8f92afa9a2824a17445b`.

For the uniform permutation with exactly $n$ external and $k$ internal entries, the normalized-rank empirical measure converges weakly in probability to Lebesgue measure whenever $k/n\to\infty$. The proof actually allows every sequence $n\ge4$, including fixed $n$.

Let $S$ be the external skeleton, let $R(S)$ be the region with a skeleton witness in each of its four quadrants, and put $A(S)=\operatorname{Leb}(R(S))$. Conditional on $S$, the internal points are independent and uniform in $R(S)$, while the skeleton distribution is weighted exactly by $A(S)^k$. An elementary encoding bounds the number of square skeleton permutations by $16^n$. An explicit four-corner skeleton supplies a matching factorial denominator in the lower bound. These give

\[
\mathbb P\big(1-A(S)\ge\delta\mid\#\mathrm{external}=n\big)
\le \left(\frac{1024}{\delta^2}\right)^n e^{-\delta k/2},
\qquad 0<\delta<1.
\]

The internal region therefore fills the square; the external points have vanishing empirical mass; and the rank-coordinate conversion preserves the limit. The model was checked against Borga–Duchi–Slivken [S2]. The thesis question numbering is preserved from the supplied handoff, not represented as an independently retrieved thesis-page check.

### Almost-sure sampled BST height: Q1886

**Stable statement ID:** `bf78aed37063121c130a`.

For the first $n$ points of one infinite iid permuton sequence, under exactly the bounded-density and positive continuous left-boundary hypotheses in the handoff,

\[
\frac{H_n}{\log n}\longrightarrow c_*\qquad\text{almost surely},
\qquad c_*\log(2e/c_*)=1,
\quad c_*>2.
\]

Here $c_*\approx4.31107$. The source already establishes the marginal height law; its almost-sure question concerns a planar coupling in which height can decrease when a point is added [S3]. The proof handles that coupling directly.

First, homogeneous height estimates, a thin left strip, independent thinning, and bounds on the trees hanging from that strip give polynomial marginal deviation bounds. De-Poissonization uses retention of a geometry-selected ancestor chain, avoiding a loss of order $\sqrt n$ in the probability estimate. An upward crossing of height $h$ requires the last iid label to lie on a selected chain of $h+1$ vertices, giving the factor $(h+1)/n$. This makes the dyadic upper-crossing sum finite. For the lower bound, a sufficiently dense geometric subsequence and hypergeometric chain retention control every intervening sample size. No monotonicity of the actual height process is assumed.

### Rooted common-subtree scaling: Q2399

**Stable statement ID:** `b252bb236c6d560e7c49`.

Under the exact offspring-law, moment, independence, and root-preservation conventions in the handoff,

\[
L_n^\bullet
=c\min\{H(\tau_n),H(\tau'_n)\}+o_{\mathbb P}(\sqrt n).
\]

Consequently the three coordinates have the asserted joint limit, with rooted Gromov–Hausdorff convergence for the tree coordinates, which is stronger than the requested unmarked convergence.

The proof adapts the uniform exceptional-event estimates in Angel et al., Proposition 4.3 [S4]. A bounded-complexity core controls every common subtree. When a rooted common subtree has a core that misses its root, the root-to-core path is explicitly added; this costs at most one additional leaf. In two independent Brownian CRTs, there are almost surely no branch points at the same positive root distance, so any common root-preserving real subtree is an interval. Upper semicontinuity of a finite-leaf skeleton functional and a matching lower construction along root paths then give the displayed approximation. The reduced-tree density used for the branch-height argument is in Aldous, Lemma 21 and Corollary 22 [S5].

## Four partial entries

### Height fluctuations: provisional Q2495 (stable ID `c8efa831871a9b89e030`)

**Stable statement ID:** `c8efa831871a9b89e030`.

For every fixed $0<\beta<1/2$,

\[
\operatorname{Var}(H_n)\sim s_n^2,
\qquad
\frac{H_n-\mathbb EH_n}{s_n}\Rightarrow\mathcal N(0,1),
\qquad s_n^2=\frac{2}{3(1-\beta)}n^{1-\beta}.
\]

For every fixed $0<\beta<1$, the same variance and normal limit hold for the depth $D_n$ of vertex $n$. The uniform comparison

\[
\|H_n-D_n\|_2=O(n^{\beta/2}\log n)
\]

transfers the depth theorem to height precisely throughout $\beta<1/2$. The proof explores two ancestral lines by always revealing the larger current label; an eligibility invariant gives a geometrically bounded coalescence time, and signed clock increments form a martingale. It does not assume independent vertex depths.

Both depth and subcritical height may be centered at the explicit clock

\[
F(n)=\sum_{m=2}^n\frac{2}{a_m+1},
\qquad
a_m=\min\{m-1,\lfloor(m-1)^\beta\rfloor+1\}.
\]

The leading equivalent $2n^{1-\beta}/(1-\beta)$ need not be accurate enough for central-limit centering. The exact integer window is preserved in the proof and computations. The critical and supercritical height laws are unresolved. The model and original fluctuation question were checked in *Evolution of recursive trees with limited memory*, v1 [S6].

### Critical metric scaling: Q1893

**Stable statement ID:** `1682f687494957159272`.

At $\beta=1/2$,

\[
\frac1{\sqrt n}\max_{v\le n}|D_v-4\sqrt v|\longrightarrow0
\quad\text{in }L^2.
\]

The uniform-vertex distribution of rescaled root distances therefore converges to $4\sqrt U$, for $U$ uniform on $[0,1]$. Its CDF is $r^2/16$ for $0\le r\le4$, with density $r/8$. Any rooted measured subsequential limit must have this radial law and root height four. The argument does not establish GH tightness, the full limiting space, or uniqueness. Uniform control of distance from the root does not bound the number of separated branches.

### Universal BST lower bound: Q1885

**Stable statement ID:** `9555ab5eed7e5e643fb2`.

If a permuton has continuous positive density on just one nondegenerate rectangle $[0,\beta]\times[a,b]$ touching the left edge, then

\[
\liminf_{n\to\infty}\frac{H_n}{\log n}\ge c_*
\qquad\text{almost surely}.
\]

No density or boundedness condition is needed outside that rectangle. This strengthens the convergence mode of the local-density lower bound in [S3]. The retained assertion quantifies over every permuton, including singular measures, and remains unresolved at that full scope.

### Nonleaf normalization: Q1890

**Stable statement ID:** `489730501d06b46aaf17`.

With $L_n(v)$ the number of leaf neighbors and $D_n(v)$ the degree, define

\[
q_n=\frac1{N_n}\sum_{v:D_n(v)\ge2}\frac{L_n(v)}{D_n(v)}.
\]

The exact normalization theorem is

\[
\log N_n-\sum_{k=3}^{n-1}\frac{q_k}{k}\longrightarrow R_\infty\in\mathbb R
\qquad\text{almost surely}.
\]

For a proposed constant $\mu$, convergence of $N_n/n^\mu$ to a finite strictly positive limit is equivalent to real convergence of $\sum_{k<n}(q_k-\mu)/k$. This identifies the missing estimate. No deterministic exponent or nondegeneracy is established. Mere convergence $q_n\to\mu$ would identify only the logarithmic growth exponent and would leave a possible slowly varying correction.

## Academic-genealogy application

The report derives exact null distributions for complete descendant subtrees under uniform attachment and a specifically defined affine, single-parent preferential rule. For $2\le i\le N$, let $S_i(N)$ include its seed. Uniform attachment gives

\[
S_i(N)-1\sim\operatorname{BetaBinomial}(N-i,1,i-1),
\qquad \mathbb ES_i(N)=N/i.
\]

Moreover, for each fixed $i\ge2$, $S_i(N)/N$ converges almost surely to a $\operatorname{Beta}(1,i-1)$ variable. The root has $S_1(N)=N$ deterministically. Random variation survives adjustment by an age-based mean. Exact generating polynomials quantify generation truncation and, under explicitly stated independent edge recording, missing-edge effects.

The supplied graph-audit script preserves distinct advisors and reports unique descendants separately from path counts. It detects duplicate IDs, unknown endpoints, duplicate relations, and cycles; invalid graphs block descendant calculations. It does not infer doctoral arrival order from birth dates. A synthetic diamond illustrates why a depth cap and a unique-person definition matter. The comparison protocol applies the same observation and seed-selection rules to simulated graphs, preserves dependence between seeds, and distinguishes fixed-null randomization from fitted-model bootstrap inference.

The underlying people and edge files were not attached. There is therefore no empirical degree fit, influence ranking, cohort estimate, or newly measured descendant count in this deliverable. The exact obstruction under unrestricted missingness is also proved: arbitrarily many hidden descendants can be added without changing the observed DAG. Inference requires an observation model.

# Complete disposition register

The statuses below refer to the exact retained questions. A partial theorem is not counted as an exact closure. Stable IDs and exact wording appear in Appendix A and in the JSON ledger; provisional numbers include their IDs here as well.

| Question | Status | Result at retained scope |
|---|---|---|
| Q197 | Unresolved | Intrinsic DLA diameter exponent remains. |
| Q198 | Unresolved | DLA one-endedness remains. |
| Q1288 | Unresolved | Genuine attachment critical component scale remains. |
| Q1296 | Unresolved | Deletion/merger survival monotonicity remains. |
| Q1397 | Unresolved | Subcritical attachment metric limits remain. |
| Q1398 | Unresolved | Fixed-two-outedge critical window remains. |
| Q1884 | Unresolved | Critical directed-diameter upper bound remains. |
| Q1885 | Partial | Almost-sure lower bound on a local-density subclass. |
| Q1886 | Proved | Exact nested-coupling almost-sure height law. |
| Q1887 | Proved | Uniform permuton limit when internal entries dominate. |
| Q1888 | Proved | Complete hub mass; attachment and distance-law corollaries. |
| Q1889 | Unresolved | Finite-time order verified through 8 only. |
| Q1890 | Partial | Exact predictable normalization; deterministic exponent remains. |
| Q1891 | Unresolved | Heavy-tail common-subtree limit remains. |
| Q1892 | Unresolved | Mixed-moment common-subtree vanishing remains. |
| Q1893 | Partial | Critical radial profile; full metric limit remains. |
| Q2392 | Unresolved | Specified cladogram spectral-gap bound remains. |
| Q2399 | Proved | Exact rooted joint CRT/common-subtree limit. |
| Q2490 (stable ID `9b2ec4db36d8dc2b752e`) | Unresolved | Yule–Harding labeled agreement bound remains. |
| Q2491 (stable ID `f82ba8d6bddd7e9322b5`) | Unresolved | Existing bounds checked; exact exponent remains. |
| Q2495 (stable ID `c8efa831871a9b89e030`) | Partial | Full subcritical height CLT; critical/supercritical height remain. |

# Remaining mathematical work

The next steps below name the unresolved estimates. They are research directions, not proved reductions unless explicitly described as such.

1. **Random-friend age order, Q1889.** Exact enumeration through eight vertices supports finite-time older-degree stochastic dominance. A proof for all sizes, or a direct limiting coupling, is still needed. Comparing means or observing one random graph does not establish stochastic order of the entire limiting distributions.
2. **Random-friend nonleaf count, Q1890.** Determine the asymptotic drift of the nonleaf core, then control the centered harmonic series and the law of its limit. The exact core-edge identity in the friend chapter records the degree correlations involved. A deterministic exponent without the series estimate would not settle the retained normalization.
3. **Memory-tree transition and critical geometry.** The comparison error $n^{\beta/2}\log n$ is negligible relative to the depth standard deviation only below $1/2$. Critical height requires a sharper description of the maximum relative to a typical ancestral line; supercritical height requires the extremes of the correlated collection of depths. For Q1893, one must control the number and lengths of separated historical branches, including branches without descendants among the last finitely many tips. The radial law and finite-tip limits alone do not give a Hausdorff net.
4. **Universal permuton lower bound, Q1885.** The local homogeneous comparison does not cover arbitrary singular permutons or irregular behavior at the left boundary. A universal argument needs a replacement for that comparison, or a counterexample outside the covered class.
5. **Heavy-tailed and mixed-moment common subtrees, Q1891–Q1892.** The finite-variance bounded-core argument used for Q2399 cannot simply be transported to the stated infinite-variance regimes. Their large offspring vertices and common-subtree decorations require new estimates at the requested scales.
6. **Attachment graph geometry, Q1288 and Q1397–Q1398.** The genuine degree-dependent attachment graph, the fixed-two-outedge uniform graph, and an independent-edge age-kernel graph are different probability models. The independently checked critical-window result for the last model [S8] does not settle either retained critical problem. The subcritical metric question additionally asks for graph distances, not merely component cardinalities.
7. **DLA, deletion/merger monotonicity, directed diameter, and cladogram mixing.** No exact theorem is obtained here for Q197, Q198, Q1296, Q1884, or Q2392. Internal DLA distance and one-endedness are not consequences of ambient growth exponents. A generation-size coupling must survive the state-dependent deletion and merger operations for Q1296. The directed-diameter upper bound and the specified rotation-chain spectral estimate remain separate tasks under the handoff's exact conventions.
8. **Labeled Yule agreement and Brownian Hölder homeomorphisms.** Provisional Q2490 (stable ID `9b2ec4db36d8dc2b752e`) remains unresolved: the checked uniform labeled binary-tree agreement result does not transfer to the Yule–Harding law. Provisional Q2491 (stable ID `f82ba8d6bddd7e9322b5`) remains unresolved. The checked existing results in [S7] give
   \[
   5-2\sqrt6\le\gamma_+\le1-10^{-338},
   \]
   with existence for every exponent strictly below the lower endpoint. These are existing bounds, not an exact determination or a new theorem in this report.

The imported Potts formalization note in the handoff is a separate scope comparison. It supplies no compiled theorem here, and neither its model nor its stated formalization scope settles any of these tree-geometry questions.

# Validation and reproduction

## What actually ran

The asymptotic results rest on written proofs. The following bounded computations ran successfully and are included with raw outputs. Their purpose is algebraic and implementation checking, or finite-size diagnosis; their loss is an assertion failure or a reported diagnostic discrepancy, not an optimized fit to genealogy data.

| Check | Declared finite domain | Outcome |
|---|---|---|
| Friend-tree exact enumeration | All recursive parent arrays for $2\le n\le8$; rational path probabilities | 5,913 states; 46,232 transitions; 34,406 tail-prefix drift checks; all passed |
| BST combinatorial audit | All permutations for $1\le n\le8$; horizontal restrictions through 7 | 46,233 permutations; 362,879 deletions; 158,323 interval restrictions; all passed |
| External-skeleton audit | All permutations through 8; insertions through 7; corner patterns for $4\le n\le100$ | 46,233 permutations; 54,136 insertions; 97 patterns; all passed |
| Memory depth recurrences | Four exact rational exponents; moments through $n=500{,}000$ | Long-double evaluations with exact integer window floors completed |
| Memory full-tree simulations | 2,048 trees per exponent through $n=30{,}000$ | PCG64 seeds 20261008–20261011; all observations retained |
| Genealogy protocol controls | 5,913 recursive trees; exact descendant laws; synthetic DAGs; four model generators | 28 uniform and 28 affine descendant laws; all controls passed |

The friend check used an external 120-second cap and completed in 2.945 seconds. The memory run had a declared 110-second process budget, an outer 115-second cap, and completed in 12.52 seconds. The final protocol self-test declared 120 seconds and completed in about 0.186 seconds. The permutation checks were bounded by their exhaustive ranges; their outputs do not record wall-clock timings, and no timing is invented here. Exhaustive checks have no random seed. No proof assistant, formal kernel check, or empirical data fit ran.

In the memory simulations at $n=30{,}000$, the mean height-minus-terminal-depth gaps were 0.7202, 4.5381, 8.7246, and 13.4731 for $\beta=1/5,2/5,1/2,3/4$. These are finite observations. At $n=500{,}000$, the variance-to-asymptotic ratio for $\beta=1/5$ was only about 0.731, illustrating slow convergence when the integer window is short. The proof uses the exact clock, not a visual normal fit. Critical and supercritical distributions were not inferred from these data.

## Archive contents and commands

The ZIP archive includes the original attached input, this complete report, its PDF, the exact-statement ledger, every cited script, the synthetic inputs and configurations, all raw numerical observations, mathematical review notes, and a SHA-256 manifest. The external research papers are cited by version and location; full copies of those papers are not redistributed in the archive. The input handoff is preserved unchanged.

Run from the extracted archive root. These commands reproduce the declared checks and overwrite their local output files:

```bash
timeout 120s python3 research/friend/exact_friend_audit.py
python3 research/permutations/verify_bst_crossings.py
python3 research/permutations/verify_external_skeleton.py
timeout 115s python3 research/memory/check_memory.py
python3 research/protocol/genealogy_protocol.py selftest \
  --output research/protocol/protocol_checks.json
```

The finite exact checks use Python's standard library. The memory script additionally needs NumPy; the archive records the Python and NumPy versions used. Floating-point moment outputs can vary at the last digits across platforms; their recurrences and integer window choices are exact, but their evaluation is not a formal interval-arithmetic certificate. The raw simulation arrays preserve every observation at the declared checkpoints.

For actual advisor data supplied later, the executable command is:

```bash
python3 research/protocol/genealogy_protocol.py audit \
  --people people.tsv.gz --edges edges.tsv.gz \
  --seed QID_TO_ANALYZE --depth 12 --output observed_audit.json
```

Repeat `--seed` for every chosen seed. This command has not been run on the absent lineage snapshot. All controls that did run are included in `research/protocol/protocol_checks.json`.

# Complete arguments

The following chapters contain the full proofs and protocol, including the lemmas summarized above. Equation numbering is local to each chapter. Standalone copies of these chapters are included in the archive for independent reuse.

# Friend trees: complete mass, consequences, and nonleaf normalization

Prepared 8 October 2026 (UTC). This is a research note, not a proof-assistant certificate or a claim of publication priority. The exact model is the handoff's model: start with edge \(\{1,2\}\); given \(T_n\), choose \(V_n\) uniformly in \([n]\), choose \(W_n\) uniformly among its neighbours, and attach \(n+1\) to \(W_n\).

## Exact targets

**Q1888 — complete hub mass.** Stable statement ID
`7e728675d1726f7676ee`. Retained statement: “Is \(\sum_{i\ge1}Z_i=1\)
almost surely?” **Status: proved by a complete written argument**, using
the primary paper's sublinear polynomial upper bound. No model assumptions
are changed.

**Q1889 — older hubs dominate.** Stable statement ID
`c8f5ea8c27dcbc835ad2`. Retained statement: “For every \(u<v\), does
\(Z_u\) stochastically dominate \(Z_v\)?” **Status: unresolved.** The
finite-state computation below supplies bounded evidence only.

**Q1890 — nonleaf normalization.** Stable statement ID
`489730501d06b46aaf17`. Retained statement: “Do \(\mu>0\) and a
nondegenerate random variable \(X\) exist with
\(n^{-\mu}N_n\to X\) almost surely?” **Status: partial; exact
deterministic-power normalization unresolved.** Section 5 proves an exact
predictable-normalization reduction. No deterministic exponent or
nondegenerate limit under deterministic-power normalization is supplied.

Here \(D_n(i)\) is the degree, \(L_n(i)\) is the number of leaf neighbours of vertex \(i\), and \(N_n\) is the number of vertices of degree at least two. Sequences indexed by \(i\) are extended by zero for \(i>n\). Write \(F_n=\sigma(T_2,\ldots,T_n)\).

## Primary-source comparison

The primary paper read is Addario-Berry, Briend, Devroye, Donderwinkel, Kerriou and Lugosi, *Random friend trees*, arXiv:2403.20185v1, submitted 29 March 2024, 36 PDF pages. The arXiv abstract page currently lists only v1. The handoff reports a July 2026 journal version retaining these questions; that journal-version statement is handoff provenance, not an independent journal-version check in this note.

- [Abstract and version history](https://arxiv.org/abs/2403.20185).
- [Primary PDF](https://arxiv.org/pdf/2403.20185).
- [HTML version](https://arxiv.org/html/2403.20185v1).

The source inputs needed for Q1888 are exactly:

1. Theorem 3.1, printed page 5 (PDF index 4): for each fixed vertex, \(D_n(i)/n\) and \(L_n(i)/n\) converge almost surely to the same \(Z_i\).
2. Theorem 4.7, printed page 7 (PDF index 6): deterministic constants \(0.1<\delta \le \lambda <0.9\) exist such that, for every fixed integer \(k\ge 2\), \(X_n^{\ge k}/n^{\delta}\to \infty\) and \(X_n^{\ge k}/n^{\lambda}\to 0\) almost surely. In particular \(N_n=o(n^{\lambda})\) almost surely. This is an almost-sure bound, not merely an in-probability statement.
3. Section 7, printed page 31 (PDF index 30), items (1), (3), (4) contain Q1890, Q1889, Q1888 respectively.

No full source proof was formally checked. The main theorem below can rederive source input 1 from a bounded-submartingale argument, so only the polynomial upper bound is an essential nontrivial literature input.

## 1. A tail-label estimate

Fix an integer \(m\ge 3\). For \(n\ge m\) define

\[
A_n^{(m)}=\sum_{i=m+1}^{n}L_n(i),\qquad B_n^{(m)}=A_n^{(m)}/n.
\]

\(A_n^{(m)}\) counts leaves whose unique neighbour has label greater than \(m\). At time \(m\), \(A_m^{(m)}=0\).

**Lemma 1 (one-step inequality).** For every \(n\ge m\),

\[
\mathbf E[B_{n+1}^{(m)}\mid F_n]
\le B_n^{(m)}+\frac{N_n}{n(n+1)}. \tag{1}
\]

**Proof.** The newly born leaf contributes one to \(A\) exactly when \(W_n>m\). Any existing leaf that ceases to be a leaf can only remove one from \(A\); no other existing vertex changes leaf status. Therefore

\[
A_{n+1}^{(m)}-A_n^{(m)}\le\mathbf1_{\{W_n>m\}}.
\]

When \(V_n\) is a leaf, its neighbour is determined, and exactly \(A_n^{(m)}\) choices of \(V_n\) lead to \(W_n>m\). All other contributions come from the \(N_n\) nonleaf choices of \(V_n\). Hence

\[
\mathbf P(W_n>m\mid F_n)
=\frac{A_n^{(m)}}n+
\frac1n\sum_{v:D_n(v)\ge2}
\frac{\#\{w\sim v:w>m\}}{D_n(v)}
\le\frac{A_n^{(m)}+N_n}{n}.
\]

Divide the resulting drift inequality for \(A\) by \(n+1\); the terms involving \(A\) satisfy \((A+A/n)/(n+1)=A/n\). This proves (1). ∎

The crucial term is \(N_n/[n(n+1)]\). The argument never assumes that a vertex known to have large degree is certain to remain a hub.

## 2. Q1888: all hub mass is retained

**Theorem 2 (Q1888).** In the random friend tree specified above,

\[
\boxed{\sum_{i\ge1}Z_i=1\quad\text{almost surely}.}
\]

**Proof.** Source Theorem 4.7 gives a deterministic \(\lambda <1\) with \(N_n=o(n^{\lambda})\) almost surely. Source Theorem 3.1 gives simultaneous convergence of all \(L_n(i)/n\) to \(Z_i\) after intersecting countably many probability-one events.

For \(n\ge 3\), every leaf has exactly one neighbour and the total number of leaves is \(n-N_n\), so

\[
\frac{A_n^{(m)}}n
=1-\frac{N_n}{n}-\sum_{i=1}^{m}\frac{L_n(i)}n
\longrightarrow D_m:=1-\sum_{i=1}^{m}Z_i. \tag{2}
\]

Consequently \(D_m\ge 0\), the sequence \(D_m\) is nonincreasing, and its limit is

\[
D_\infty=1-\sum_{i\ge1}Z_i\ge0.
\]

The almost-sure polynomial bound alone need not give a matching expectation bound, so localization is essential. Fix an integer \(K\ge 1\) and let

\[
E_K=\{N_n\le K n^\lambda\ \text{for every }n\ge3\}.
\]

Since \(N_n=o(n^{\lambda})\) almost surely, \(\bigcup_K E_K\) has probability one. For each \(m\), define the stopping time

\[
\tau_{m,K}=\inf\{n\ge m:N_n>K n^\lambda\},
\]

with the usual value \(\infty\) for an empty set, and set

\[
Y_n=B_{n\wedge\tau_{m,K}}^{(m)},\qquad n\ge m.
\]

If \(\tau =m\) then \(Y\) remains its initial value zero. Otherwise stopped increments and (1) give

\[
\mathbf E[Y_{n+1}-Y_n\mid F_n]
\le\mathbf1_{\{n<\tau_{m,K}\}}
\frac{N_n}{n(n+1)}
\le K\frac{n^\lambda}{n(n+1)}.
\]

Since \(Y_m=0\),

\[
\mathbf E Y_n\le
K\sum_{k=m}^{n-1}\frac{k^\lambda}{k(k+1)}
\le\frac{K}{1-\lambda}(m-1)^{\lambda-1}. \tag{3}
\]

On \(E_K\) the stopping time is infinite, so by (2), \(Y_n\to D_m\). Since \(Y_n\ge 0\) everywhere, Fatou's lemma yields

\[
\mathbf E[\mathbf1_{E_K}D_m]
\le\liminf_{n\to\infty}\mathbf E Y_n
\le\frac{K}{1-\lambda}(m-1)^{\lambda-1}.
\]

Let \(m\to \infty\). Dominated convergence applies because \(0\le D_m\le 1\), giving

\[
\mathbf E[\mathbf1_{E_K}D_\infty]=0.
\]

Thus \(D_\infty =0\) almost surely on every \(E_K\), and their countable union has probability one. This proves the assertion. ∎

### Quantitative stopped-tail statement

The proof also gives, for every \(\varepsilon >0\),

\[
\mathbf P\!\left(E_K\cap
\left\{1-\sum_{i\le m}Z_i>\varepsilon\right\}\right)
\le\frac{K(m-1)^{\lambda-1}}{(1-\lambda)\varepsilon}.
\]

This bound controls the intersection with the displayed pathwise envelope event. It is not a bound on the conditional probability given that event, and it does not supply an unconditional deterministic convergence rate, because the distribution of the random envelope constant is not estimated here.

## 3. A more general summable-innovation theorem

**Theorem 3.** For this attachment process, the weaker hypothesis

\[
\sum_{n=3}^{\infty}\frac{N_n}{n(n+1)}<\infty
\quad\text{almost surely} \tag{4}
\]

already implies existence of every normalized-degree limit and their total mass one.

**Proof of the preliminary convergence statements.** First, \((N_n)\) is nondecreasing, and for each \(m\),

\[
\sum_{n=m}^{2m}\frac{N_n}{n(n+1)}
\ge N_m\left(\frac1m-\frac1{2m+1}\right)
\ge\frac{N_m}{2m}.
\]

The tail on the left tends to zero under (4), so \(N_m/m\to 0\).

For a fixed existing vertex \(i\) and \(n\ge \max(3,i)\), the exact leaf drift is

\[
\mathbf E[L_{n+1}(i)-L_n(i)\mid F_n]
=\frac1n\sum_{v\sim i}\frac1{D_n(v)}
-\frac1n\frac{L_n(i)}{D_n(i)}
\ge\frac{L_n(i)-1}{n}.
\]

Thus \((L_n(i)-1)/n\) is a bounded submartingale and converges almost surely by the bounded-submartingale convergence theorem. Call its limit \(Z_i\ge 0\). Since

\[
0\le D_n(i)-L_n(i)\le N_n,
\]

\(D_n(i)/n\to Z_i\) as well. These assertions hold simultaneously for all \(i\) after countable intersection, and (2) again defines nonnegative \(D_m\downarrow D_\infty\).

**Proof of no mass loss under (4).** Put \(c_n=N_n/[n(n+1)]\) and \(C_n=\sum_{k=3}^{n-1}c_k\). For each integer \(K\ge 1\), use the global stopping time

\[
\sigma_K=\inf\{n\ge3:C_n>K\}.
\]

Each \(c_n\le 1/(n+1)\le 1/4\); therefore, pathwise,

\[
\sum_{n=3}^{\sigma_K-1}c_n\le K+\tfrac14.
\]

For every \(m\), start \(B^{(m)}\) at zero at time \(m\) and freeze it immediately if \(\sigma_K\le m\), or at time \(\sigma_K\) otherwise. The stopped version is nonnegative. Its expected increase is at most \(c_n\mathbf1_{\{n<\sigma_K\}}\). Therefore Fatou, just as before, gives

\[
\mathbf E[\mathbf1_{\{\sigma_K=\infty\}}D_m]
\le\mathbf E\sum_{n=m}^{\sigma_K-1}c_n.
\]

The random tail on the right decreases to zero and is bounded by \(K+1/4\), so dominated convergence sends its expectation to zero. Let \(m\to \infty\) and then take the union over \(K\). Under (4), \(\sigma_K=\infty\) for some integer \(K\) almost surely. Hence \(D_\infty =0\) almost surely. ∎

The theorem isolates the mechanism: sampling an existing leaf copies its neighbour's label class, whereas a nonleaf sample can introduce new label classes. Summability of the normalized latter contribution prevents a positive limiting mass from escaping to labels tending to infinity.

## 4. Consequences of the complete-mass theorem

All convergence in this section is almost sure. These are consequences proved here, not additional assumed source theorems.

### 4.1 Convergence in \(\ell^1\)

**Discrete Scheffé lemma.** If \(x_n(i)\ge 0\), \(x_n(i)\to x(i)\) coordinatewise, and \(\sum_i x_n(i)\to \sum_i x(i)<\infty\), then \(\sum_i|x_n(i)-x(i)|\to 0\).

**Proof.** Given \(\varepsilon >0\), select a finite prefix carrying all but \(\varepsilon\) of the mass of \(x\). Coordinatewise convergence controls that prefix, while convergence of total masses controls the complement. Let \(\varepsilon \to 0\). ∎

Apply this lemma to each of the following sequences:

\[
\ell_n(i)=\frac{L_n(i)}n,
\qquad
e_n(i)=\frac{D_n(i)-1}{n}\mathbf1_{\{i\le n\}},
\qquad
r_n(i)=\frac{D_n(i)}n\mathbf1_{\{D_n(i)\ge2\}}.
\]

Every coordinate tends to \(Z_i\). The total masses are respectively

\[
1-\frac{N_n}{n},\qquad 1-\frac2n,
\qquad 1+\frac{N_n-2}{n},
\]

all of which tend to one. Hence

\[
\|\ell_n-Z\|_1\to0,\quad
\|e_n-Z\|_1\to0,\quad
\|r_n-Z\|_1\to0. \tag{5}
\]

The full sequence \(D_n(i)/n\) does **not** converge to \(Z\) in \(\ell^1\): its total mass tends to two. Its mass on the many degree-one vertices accounts for the discrepancy. For every \(p>1\), however, its \(\ell^p\) distance from \(Z\) tends to zero, since the leaf contribution has p-th-power sum at most \(n^{1-p}\) and the nonleaf contribution is controlled by (5).

In particular the normalized maximum degree converges to \(max_i Z_i\), a positive maximum attained by at least one label. No uniqueness of the maximizing label is claimed.

### 4.2 The attachment label distribution and attachment degree

Let

\[
p_n(i)=\mathbf P(W_n=i\mid F_n)
=\frac1n\sum_{v\sim i}\frac1{D_n(v)}.
\]

The contribution from leaf neighbours is exactly \(\ell_n(i)\), so \(p_n(i)-\ell_n(i)\ge 0\). Summing over \(i\) gives

\[
\|p_n-\ell_n\|_1=\frac{N_n}{n}.
\]

Together with (5),

\[
\boxed{\|p_n-Z\|_1\longrightarrow0.} \tag{6}
\]

Thus the conditional distribution of the label selected for attachment converges in total variation to the random probability distribution \((Z_i)\).

For every bounded continuous \(f:[0,1]\to\mathbb R\), a finite-prefix argument applied to (6) and the coordinate limits yields

\[
\mathbf E\!\left[f\!\left(\frac{D_n(W_n)}n\right)\middle|F_n\right]
\longrightarrow\sum_{i\ge1}Z_i f(Z_i).
\]

Equivalently the conditional degree law converges weakly to \(\sum_i Z_i\delta_{Z_i}\). Taking \(f(x)=x\) gives the exact limit

\[
\frac1n\mathbf E[D_n(W_n)\mid F_n]
\longrightarrow\sum_{i\ge1}Z_i^2>0.
\]

### 4.3 A limit law and tightness for distances between uniform vertices

Let \(U_n,V_n\) be independent uniform vertices of \(T_n\), conditionally on the tree. Let \(d_\infty (i,j)\) be the graph distance between fixed labels in the union tree \(T_\infty\). This equals their distance in every \(T_n\) with \(n\ge \max(i,j)\), because adding leaves never changes existing distances.

Define the random probability measure on the nonnegative integers

\[
\nu=\sum_{i,j\ge1}Z_iZ_j\,
\delta_{\,d_\infty(i,j)+2}. \tag{7}
\]

Then

\[
\boxed{\mathcal L(d_{T_n}(U_n,V_n)\mid F_n)
\longrightarrow\nu\quad\text{in total variation, almost surely}.} \tag{8}
\]

**Proof.** The probability that either uniform vertex is a nonleaf is at most \(2N_n/n\to 0\). When the two vertices are distinct leaves with neighbours \(i,j\), their distance is exactly \(d_\infty (i,j)+2\). The probability that the two samples coincide is \(1/n\). The subprobability law of the two neighbour labels when both samples are leaves is \(\ell_n\otimes \ell_n\); (5) implies

\[
\|\ell_n\otimes\ell_n-Z\otimes Z\|_1
\le(\|\ell_n\|_1+\|Z\|_1)\|\ell_n-Z\|_1\to0.
\]

Pushing forward by the fixed map \((i,j)\mapsto d_\infty (i,j)+2\) cannot increase total variation. The nonleaf and coincident-sample errors tend to zero, proving (8). ∎

Consequently typical distances are tight: \(d_{T_n}(U_n,V_n)=O_P(1)\). The conditional probability of distance two converges to \(\sum_i Z_i^2\). A finite limiting mean distance is not asserted: tightness and convergence in distribution alone do not imply moment convergence.

## 5. Q1890: an exact predictable-normalization reduction

This section gives a partial result, without asserting existence of a deterministic exponent.

For \(n\ge 3\), let

\[
S_n=\sum_{v:D_n(v)\ge2}\frac{L_n(v)}{D_n(v)},
\qquad q_n=\frac{S_n}{N_n}\in[0,1].
\]

At these times \(N_n\ge 1\). A new nonleaf is created precisely when \(W_n\) is a leaf. Its current unique neighbour is nonleaf, so

\[
\xi_n:=N_{n+1}-N_n\in\{0,1\},
\qquad
\mathbf E[\xi_n\mid F_n]=\frac{S_n}{n}=\frac{q_nN_n}{n}. \tag{9}
\]

**Theorem 4 (predictable exponential normalization).** There is an almost surely finite real random variable \(R_\infty\) such that

\[
\log N_n-\sum_{k=3}^{n-1}\frac{q_k}{k}\longrightarrow R_\infty.
\tag{10}
\]

Equivalently,

\[
N_n\exp\!\left(-\sum_{k=3}^{n-1}\frac{q_k}{k}\right)
\longrightarrow e^{R_\infty}\in(0,\infty)
\quad\text{almost surely}. \tag{11}
\]

**Proof.** From (9),

\[
\log N_{n+1}-\log N_n
=\xi_n\log(1+1/N_n).
\]

Its conditional mean differs from \(q_n/n\) by an absolutely summable term, since for \(x\ge 1\),

\[
0\le1-x\log(1+1/x)\le\frac1{2x},
\]

and hence the absolute error is at most \(1/(2nN_n)\). The conditional variance of the centered logarithmic increment is at most

\[
\frac{q_nN_n}{n}\log^2(1+1/N_n)
\le\frac1{nN_n}.
\]

Source Theorem 4.7 supplies \(N_n/n^{\delta}\to \infty\) almost surely for a deterministic \(\delta >0\), so \(\sum_n\frac1{nN_n}<\infty\) almost surely. The martingale of centered logarithmic increments therefore converges almost surely by the martingale convergence theorem with finite predictable quadratic variation, proved if desired by stopping at bounded accumulated conditional variance and applying the \(L^2\) martingale convergence theorem. The drift-error series also converges absolutely. Summing the increments proves (10). ∎

For a proposed constant \(\mu\), define

\[
H_n(\mu)=\sum_{k=3}^{n-1}\frac{q_k-\mu}{k}.
\]

Since \(\sum_{k=3}^{n-1}1/k-\log n\) converges, (10) gives the exact equivalence

\[
\begin{gathered}
\frac{N_n}{n^\mu}\ \text{converges almost surely to a finite strictly positive limit}
\\[2pt]\Longleftrightarrow\\[2pt]
H_n(\mu)\ \text{converges almost surely in }\mathbb R.
\end{gathered}\tag{12}
\]

Likewise, \(N_n/n^{\mu}\to 0\) if and only if \(H_n(\mu )\to -\infty\), and it tends to infinity if and only if \(H_n(\mu )\to +\infty\). For a random limit allowed to vanish on some events, the finite-positive equivalence applies on the event where the limit is positive, and the \(-\infty\) condition applies where it is zero.

Even establishing \(q_n\to \mu\) would only prove \(\log N_n/\log n\to \mu\); it does not alone prove the convergence demanded in Q1890. The remaining issue is the convergence of the centered harmonic sum in (12), together with nondegeneracy of the resulting random limit. A purely slowly varying correction remains compatible with \(q_n\to \mu\).

The product

\[
P_n=\prod_{k=3}^{n-1}(1+q_k/k)
\]

also gives a predictable normalization: \((N_n/P_n)\) is a nonnegative martingale by (9), and its almost-sure limit lies in \((0,\infty )\) because \(\log P_n-\sum q_k/k\) has an absolutely convergent difference series. No claim of nondegeneracy or uniform integrability of this martingale is needed for (10)–(12).

### Core-tree expression for the drift

The subgraph induced by the nonleaves is a tree on \(N_n\) vertices, when \(N_n\ge 1\). If \(E_n^{core}\) denotes its edge set, then

\[
q_n
=1-\frac1{N_n}\sum_{\{u,v\}\in E_n^{core}}
\left(\frac1{D_n(u)}+\frac1{D_n(v)}\right). \tag{13}
\]

Indeed \(D_n(v)-L_n(v)\) is the number of core neighbours of \(v\); summing \((D-L)/D\) over nonleaves counts each oriented core edge once. Formula (13) shows exactly which degree correlations govern the normalization problem. A marginal degree distribution alone does not determine the required limit without the edge correlations.

## Evidence and execution status

- Q1888, Lemma 1, and Theorems 2–4 are written mathematical arguments. They use standard martingale convergence and the specific published polynomial bounds above.
- The source arXiv PDF was retrieved and its theorem statements and Section 7 were read. This does not constitute a formal audit of its long polynomial-bound proof.
- No proof assistant was invoked. No compiled formal theorem is claimed.
- No simulations or finite enumeration are used in any proof in this note.
- Q1889 remains unresolved. Q1890 remains partial; its exact deterministic-power normalization is not claimed.

## 6. Bounded exact finite-state audit

The script `exact_friend_audit.py` was executed successfully under an external 120-second wall-clock cap; its measured elapsed time was 2.945 seconds. Its complete machine-readable output, including exact rational degree marginals and every age-pair comparison, is `exact_friend_audit.json`.

The declared domain is every recursive labelled tree on \([n]\) starting with edge \(\{1,2\}\), for \(2\le n\le 8\). Every parent array \(\operatorname{parent}(v)\in[v-1]\) is enumerated, and each tree receives its exact random-friend path probability using Python's `fractions.Fraction`. There is no random seed because the enumeration is exhaustive. It visits 5,913 states, evaluates 46,232 outgoing transitions, and checks 34,406 choices of a state and a label prefix.

All checks passed:

1. State probabilities sum exactly to one at every enumerated size, and the state count is exactly \((n-1)!\).
2. The sum of leaf-neighbour counts is \(n-N_n\).
3. The exact attachment mass exceeds the leaf-neighbour mass coordinatewise and differs in total mass by \(N_n/n\).
4. Every transition satisfies the pathwise tail-leaf increment inequality in Lemma 1; every state and prefix satisfy its conditional-expectation inequality.
5. At each size through eight, every older-label degree distribution stochastically dominates every younger-label degree distribution. No violating threshold was found.

Item 5 is finite evidence only. Q1889 asks about the limiting normalized degrees for every pair of labels. Neither extrapolation in the tree size nor extrapolation to labels beyond eight is justified by this computation. The Q1888 proof above does not depend on any finite enumeration.


# Almost-square permutations: many internal entries

**Prepared:** 2026-10-08 UTC.  
**Handoff stable statement ID:** `8f92afa9a2824a17445b`.  
**Target:** Borga, *Random Permutations — A geometric point of view*, arXiv:2107.09699, Conjecture 5.1.4(e), as transcribed in the attached handoff.  
**Primary model source checked:** Borga–Duchi–Slivken, *Almost square permutations are typically square*, arXiv:1910.04813v2, 8 December 2020, Definition in §1, pp. 1–2; PDF https://arxiv.org/pdf/1910.04813 . This defines $\mathrm{ASq}(n,k)$ as permutations of $n+k$ entries with exactly $n$ external and $k$ internal entries. Theorem 1.4 treats the opposite regime $k=o(n)$.  
**Status of this note:** Complete written proof independently checked within this session. No claim of publication priority, external peer review, or proof-assistant verification. The proof uses only elementary combinatorics, exact conditioning, and the law of large numbers.

## Theorem

Let $n\ge4$ and $k\ge0$ be integers and let $\sigma_{n,k}$ be uniform among permutations with exactly $n$ external and $k$ internal entries. For every sequence with $k/n\to\infty$, the empirical measures

\[
\frac1{n+k}\sum_{i=1}^{n+k}
\delta_{(i/(n+k),\,\sigma_{n,k}(i)/(n+k))}
\]

converge weakly in probability to Lebesgue measure on the unit square. This proves the handoff formulation of Q1887 and does not require $n\to\infty$.

An entry is external if it is a minimum or maximum among the entries to its left, or among those to its right. Equivalently, at least one of its four open axis-aligned quadrants contains no other entry. An entry is internal exactly when all four quadrants contain another entry.

## 1. Exact external-skeleton decomposition

For a finite point set $P$ with distinct $x$- and $y$-coordinates, write $E(P)$ for its external points. For a finite point set $S$, let \(R(S)\subset(0,1)^2\) be the set of points at which every one of the four open quadrants contains a point of $S$. Write

\[
A(S)=\operatorname{Leb}(R(S)).
\]

Call $S$ square when $E(S)=S$. The following equivalence is deterministic:

\[
E(P)=S
\quad\Longleftrightarrow\quad
S\subset P,\quad E(S)=S,\quad P\setminus S\subset R(S).
\tag{1}
\]

**Forward implication.** Deleting points cannot destroy an empty quadrant, so $E(S)=S$. Let $z$ be any internal point of $P$. It has a witness in each quadrant. For its southwest quadrant choose, among all points strictly left of $z$ and strictly below $z$, the point $q$ with smallest $x$-coordinate. There is no point strictly left of $q$ and strictly below $q$: such a point would itself lie southwest of $z$ and have smaller $x$-coordinate than $q$. Thus $q$ is a left-to-right minimum and belongs to $E(P)=S$. The southeast, northwest, and northeast cases follow by the corresponding extremal choice in the same quadrant. Hence all four quadrants of $z$ contain a point of $S$, so $z\in R(S)$.

**Reverse implication.** Each $z\in P\setminus S$ has four witnesses already in $S$, hence is internal in $P$. Fix $s\in S$ and one quadrant $Q$ at $s$ that is empty of $S$. No point $z\in R(S)$ can belong to $Q$: if it did, a witness of $S$ in the same directional quadrant at $z$ would also belong to $Q$ at $s$, a contradiction. Therefore $Q$ remains empty after all points in $P\setminus S$ are inserted, and $s$ remains external. This proves (1).

In particular, the external set is a unique skeleton; internal points neither create new external points nor destroy skeleton records when they lie in $R(S)$.

## 2. Uniform permutations as conditioned independent points

Take $N=n+k$ independent uniform points $Z_1,\ldots,Z_N$ in the unit square and condition on $|E(\{Z_1,\ldots,Z_N\})|=n$. Their rank permutation is then uniform in $\mathrm{ASq}(n,k)$.

For the designated first $n$ points write $S=\{Z_1,\ldots,Z_n\}$. By (1), the event that precisely these labels are external is

\[
\{S\text{ square}\}\cap\{Z_{n+1},\ldots,Z_N\in R(S)\}.
\]

Consequently its probability is

\[
\mathbb E[\mathbf 1_{\{S\text{ square}\}} A(S)^k].
\]

The analogous events over all \(\binom{N}{n}\) label subsets are disjoint and exhaustive. Therefore, for every measurable function $g$ of the unlabelled skeleton,

\[
\mathbb E[g(E(P))\mid |E(P)|=n]
=
\frac{\mathbb E[g(S)\mathbf 1_{\{S\text{ square}\}}A(S)^k]}
{\mathbb E[\mathbf 1_{\{S\text{ square}\}}A(S)^k]}.
\tag{2}
\]

Here $S$ on the right is an unconditioned sample of $n$ independent uniform points. The common binomial factor cancels exactly. Given the skeleton (and its label subset), the $k$ remaining labelled points are independent and uniform in $R(S)$. This is an exact identity for finite $n,k$, without an insertion asymptotic.

## 3. An exponential bound on square permutations

Let $s_n$ be the number of square permutations of size $n$. Assign each entry of a square permutation one of its eligible types, using any fixed deterministic priority:

- left-to-right minimum;
- left-to-right maximum;
- right-to-left minimum;
- right-to-left maximum.

For each type, its entries form a monotone subsequence. The direction is fixed by the type: decreasing, increasing, increasing, decreasing, respectively, when read from left to right.

Record the type word in position order and also the type word in increasing value order. Given both words, the permutation is uniquely reconstructible: for each type, match its positions with its assigned values in the mandated increasing or decreasing order. Thus the two words provide an injection into a set of size $4^n\cdot4^n$, and

\[
s_n\le16^n,
\qquad
\mathbb P(S\text{ square})=s_n/n!\le16^n/n!.
\tag{3}
\]

The much sharper known enumeration is unnecessary. The factorial factor matters because it will cancel against the same factor in the next lower bound.

## 4. A near-full-area skeleton event

Fix $0<\eta<1/2$. Prescribe the $x$-order rank permutation

\[
\pi_n=(n-2,n-3,\ldots,2,n,1,n-1),\qquad n\ge4.
\tag{4}
\]

There are $n-3$ entries in the initial decreasing string. Each is a left-to-right minimum; $n$ is a left-to-right maximum; 1 is a left-to-right minimum; $n-1$ is the last entry. Hence every entry is external.

Further require precisely $n-2$ $x$-coordinates to lie in $(0,\eta)$, and the remaining two in $(1-\eta,1)$; impose the same count condition on $y$-coordinates. Under (4), there is at least one skeleton point in each of the four $\eta$-by-$\eta$ corner squares. Therefore

\[
(\eta,1-\eta)^2\subset R(S),
\qquad A(S)\ge(1-2\eta)^2.
\tag{5}
\]

For an independent uniform sample the two arrays of ordered coordinates and their relative rank permutation are independent. The prescribed rank permutation has probability $1/n!$. Each strip-count event has probability \(\binom n2\eta^n\). Thus the complete favourable event has probability

\[
\binom n2^2\frac{\eta^{2n}}{n!}\ge\frac{\eta^{2n}}{n!}.
\tag{6}
\]

In particular, the denominator of (2) is positive for every $n\ge4$, $k\ge0$ and obeys

\[
\mathbb E[\mathbf1_{\{S\text{ square}\}}A(S)^k]
\ge\frac{\eta^{2n}}{n!}(1-2\eta)^{2k}.
\tag{7}
\]

## 5. Internal area fills the square

From (2), (3), and (7), for every $0<\delta<1$,

\[
\mathbb P\big(A(E(P))\le1-\delta\mid |E(P)|=n\big)
\le
\left(\frac{16}{\eta^2}\right)^n
\left(\frac{1-\delta}{(1-2\eta)^2}\right)^k.
\tag{8}
\]

Choose $\eta=\delta/8$. Since \((1-\delta/4)^2\ge1-\delta/2\),

\[
\frac{1-\delta}{(1-2\eta)^2}
\le\frac{1-\delta}{1-\delta/2}
=1-\frac{\delta}{2-\delta}
\le e^{-\delta/2}.
\]

Consequently the explicit bound

\[
\boxed{\quad
\mathbb P\big(1-A(E(P))\ge\delta\mid |E(P)|=n\big)
\le \left(\frac{1024}{\delta^2}\right)^n e^{-\delta k/2}.
\quad}
\tag{9}
\]

holds. The bound can of course be replaced by its minimum with 1. For fixed $\delta$ and $k/n\to\infty$, its logarithm tends to $-\infty$, proving $A(E(P))\to1$ in probability. This argument remains valid even when the probability of the conditioning event itself is exponentially or superexponentially small at scale $N$.

## 6. Empirical measures and the rank map

Given the skeleton $S$, let $U_1,\ldots,U_k$ be the internal points. They are independent with common distribution $\operatorname{Unif}(R(S))$. The total variation distance, using the sup-over-events convention, is

\[
\|\operatorname{Unif}(R(S))-\operatorname{Leb}\|_{\rm TV}=1-A(S).
\tag{10}
\]

For every bounded continuous $f$, the conditional variance of \(k^{-1}\sum f(U_j)\) is at most \(\|f\|_\infty^2/k\). Its conditional mean differs from \(\int f\,d\operatorname{Leb}\) by at most \(2\|f\|_\infty(1-A(S))\). Equation (9) and $k\to\infty$ therefore show that the internal empirical measure converges weakly in probability to Lebesgue measure. The skeleton has mass $n/(n+k)\to0$, so the full empirical measure of continuous coordinates has the same limit.

For completeness, the requested empirical permutation measure uses ranks instead of the sampled continuous coordinates. Conditional on any rank permutation, the sorted $x$- and sorted $y$-coordinates retain their independent uniform-order-statistic laws. The event of exactly $n$ external entries depends only on the rank permutation; hence this remains true after conditioning. Uniform empirical-CDF convergence (or the Dvoretzky–Kiefer–Wolfowitz inequality) gives

\[
\max_{1\le j\le N}|X_{(j)}-j/N|+
\max_{1\le j\le N}|Y_{(j)}-j/N|
\xrightarrow{\mathbb P}0.
\tag{11}
\]

Moving each sampled point to its pair of normalized ranks therefore changes integrals of continuous functions by $o_{\mathbb P}(1)$, proving the theorem for the exact measure in Q1887.

There is also a self-contained alternative to (11): the continuous empirical measure already proved to converge to Lebesgue has marginal CDFs converging uniformly to the identity; its empirical rank map thus moves every point by $o_{\mathbb P}(1)$.

## 7. Optional finite-sample discrepancy bound

For the empirical measure $\nu_N$ in continuous coordinates define

\[
D_N=\sup_{x,y\in[0,1]}
|\nu_N([0,x]\times[0,y])-xy|.
\]

For every integer $L\ge1$, $0<\delta<1$, and $t>0$,

\[
\mathbb P\left(D_N>\frac{n}{N}+\delta+t+\frac2L\;\middle|\; |E(P)|=n\right)
\le
\left(\frac{1024}{\delta^2}\right)^n e^{-\delta k/2}
+2(L+1)^2e^{-2kt^2}.
\tag{12}
\]

To see this, apply conditional Hoeffding bounds to the internal empirical mass of every lower-left rectangle on the $L$-by-$L$ grid, compare its conditional mean with Lebesgue by (10), and interpolate using monotonicity and the change of area between neighboring grid rectangles. The skeleton contributes at most $n/N$. Formula (12) is not asserted to be sharp; it supplies a quantitative version of the limit.

Writing $r=k/n$, (9) also gives $1-A=O_{\mathbb P}(\log r/r)$ as $r\to\infty$: choose $\delta=C\log r/r$ for any $C>4$. Again, no claim of an optimal rate is intended.

## Audit points

1. The model is exactly uniform conditional on the external count; the raw rarity of that event is never discarded.
2. Every quadrant witness needed for an internal point can be replaced by an external witness.
3. An internal point relative to $S$ cannot destroy any record of $S$, including when many such points are inserted simultaneously.
4. Both counting bounds carry the same $n!$ denominator; this cancellation is essential when $n\log n$ is comparable to, or larger than, $N$.
5. The favourable square pattern works for every $n\ge4$, including $n=4$, where it is $(2,4,1,3)$.
6. Conversion from continuous coordinates to normalized permutation ranks is included.
7. The known $k=o(n)$ regime is not used or extrapolated; the proof exploits the exact area tilt specifically when $k/n\to\infty$.

## Finite deterministic verification

The accompanying `verify_external_skeleton.py` exhaustively checked all 46,233 permutations of sizes 1 through 8. It verified that deleting the internal points leaves a square skeleton and that each deleted point has all four quadrant witnesses in that skeleton. It additionally checked all 54,136 admissible one-point insertions among permutations of sizes through 7, and the favourable four-corner pattern for each $n$ from 4 through 100 (97 patterns). All assertions passed. The asymptotic theorem follows from the written proof; these computations check the declared finite combinatorial domains only. Raw output is in `external_skeleton_verification.json`.


# BST height in the nested planar coupling

**Prepared:** 2026-10-08 UTC.  
**Stable statement ID:** `bf78aed37063121c130a`.  
**Target:** Dubach thesis, Remark 17, pp. 124–125, as transcribed in the handoff.  
**Primary source checked:** Corsini–Dubach–Féray, *Binary search trees of permuton samples*, arXiv:2403.03151v2, 27 January 2025, https://arxiv.org/html/2403.03151v2 . The target also appears as Remark 1 there. The source's Lemmas 3.1–3.2 give the chain restriction property, and its Theorem 1.1 gives convergence in probability under A1.  
**Status:** Complete written proof independently checked by two other agents within this session, including the original A1 hypothesis and Remark 1. No claim of external peer review, publication priority, or formal proof-assistant verification.

## Theorem

Let $\mu$ be a permuton with a bounded density $\rho$ on $[0,1]^2$ that is continuous and positive in a neighborhood of $\{0\}\times[0,1]$. Let $Z_1,Z_2,\ldots$ be a single i.i.d. sequence with law $\mu$. For $P_n=\{Z_1,\ldots,Z_n\}$, form the BST by reading points in increasing $x$-coordinate and inserting their $y$-coordinates. Let $H_n$ be its graph height. Then

\[
\frac{H_n}{\log n}\longrightarrow c_*\qquad\text{almost surely},
\]

where $c_*>2$ is the solution of $c_*\log(2e/c_*)=1$.

The proof has two independent components: an almost-sure upgrade valid whenever fixed-size deviations have polynomial bounds, and a derivation of those polynomial bounds under exactly the stated density hypothesis. In particular, no monotonicity of $H_n$ is assumed.

## 1. Deterministic chain restriction

For distinct-coordinate points, a point $u$ is an ancestor of a point $v$ exactly when $x_u<x_v$ and no point $w$ with $x_w<x_u$ has $y_w$ strictly between $y_u$ and $y_v$. Deleting points therefore preserves every ancestor relation between retained points. In particular, if $P\subset Q$ and $C$ is a chain in $T(Q)$, then $C\cap P$ is a chain in $T(P)$.

Consequences used below are:

1. Adding one point raises height by at most one:
   \[H_{n+1}\le H_n+1.\tag{1}\]
2. If $C$ is a chain of $T(P_M)$, then for every $N\le m\le M$,
   \[H_m\ge |C\cap P_N|-1.\tag{2}\]
3. Restriction to a horizontal interval preserves ancestor relations in both directions. Indeed, any point whose $y$-coordinate lies between two $y$-coordinates in the interval also belongs to the interval. Thus
   \[h(T(P\cap([0,1]\times I)))\le h(T(P))\tag{3}\]
   for every interval $I$.

The first two assertions are the source's chain restriction lemma, restated for the natural nested sample. The third will amplify lower-tail estimates for a homogeneous process.

## 2. General almost-sure upgrade lemma

Suppose an arbitrary atomless-coordinate i.i.d. point model satisfies, for some $c>0$, that for every $\varepsilon\in(0,c)$ there are $a_\varepsilon>0$ and $C_\varepsilon<\infty$ with

\[
\mathbb P\big(|H_n-c\log n|>\varepsilon\log n\big)
\le C_\varepsilon n^{-a_\varepsilon}
\quad(n\text{ sufficiently large}).
\tag{4}
\]

Then $H_n/\log n\to c$ almost surely.

### 2.1. Upward crossings cost only $(h+1)/n$

For every positive integer $h$,

\[
\mathbb P(H_{m-1}<h\le H_m)
\le\frac{h+1}{m}\mathbb P(H_m=h).
\tag{5}
\]

To prove this, (1) shows that an upward crossing has $H_m=h$. Choose a canonical longest chain $C_m$ from the unordered geometry of $P_m$, breaking ties by a coordinate-based rule. If $Z_m$ is not in $C_m$, deletion leaves a chain of $h+1$ vertices, contradicting $H_{m-1}<h$. Conditional on the unordered point set, the label $m$ is uniformly distributed among its $m$ points. On $H_m=h$, the selected chain has exactly $h+1$ points. This proves (5). Neither $H_m$ nor $C_m$ uses the i.i.d. labels in its definition.

Fix $\varepsilon>0$, set $N=2^j$, and $h_j=\lceil(c+\varepsilon)\log N\rceil$. An exceedance of $h_j$ during $[N,2N]$ requires $H_N\ge h_j$ or an upward crossing of $h_j$. For all large $j$ and $N\le m\le2N$, $h_j\ge(c+\varepsilon/2)\log m$. Apply (4) with $\varepsilon/3$ to avoid immaterial strict-versus-nonstrict threshold issues. Then (4)–(5) give

\[
\begin{aligned}
\mathbb P\left(\max_{N\le m\le2N}H_m\ge h_j\right)
&\le \mathbb P(H_N\ge h_j)
+\sum_{m=N+1}^{2N}\frac{h_j+1}{m}\mathbb P(H_m=h_j)\\
&\le C(1+\log N)N^{-a}
\end{aligned}
\tag{6}
\]

for suitable positive $a,C$. This is summable over $j$, so Borel–Cantelli yields, almost surely,

\[
\limsup_{n\to\infty}\frac{H_n}{\log n}\le c+\varepsilon.
\]

### 2.2. A retained endpoint chain supplies the lower bound throughout a block

Fix $\varepsilon\in(0,c)$, put $a=c-\varepsilon/2$ and $b=c-\varepsilon$, and choose $q$ with $1<q<a/b$. Let $N_j=\lfloor q^j\rfloor$ and $M_j=N_{j+1}$. At endpoint $M_j$, except on an event of polynomially small probability, $H_{M_j}\ge a\log M_j$. Select a canonical chain with

\[
L_j=\lceil a\log M_j\rceil+1
\]

vertices on that event. Conditional on the endpoint geometry, its number $K_j$ of labels among $1,\ldots,N_j$ is hypergeometric with parameters $M_j,N_j,L_j$. Its mean is $(N_j/M_j)L_j$, and $N_j/M_j\to1/q>b/a$. Thus the mean exceeds $b\log M_j+1$ by a positive constant times $\log M_j$. The elementary Hoeffding bound for sampling without replacement gives

\[
\mathbb P(K_j-1<b\log M_j\mid P_{M_j})\le M_j^{-d}
\tag{7}
\]

for some $d>0$, uniformly over endpoint configurations where the chain exists and for all large $j$. By (2), $K_j-1$ is a simultaneous lower bound for all heights $H_m$ with $N_j\le m\le M_j$. The endpoint failure probability from (4), together with (7), is summable along $q^j$. Borel–Cantelli gives $\liminf_{n\to\infty}H_n/\log n\ge c-\varepsilon$. Applying this and the upper bound to a countable sequence $\varepsilon\downarrow0$ proves the upgrade lemma.

## 3. Homogeneous BST height has polynomial upper and stretched-exponential lower tails

Write $U_m$ for the height of the BST of a uniform permutation of size $m$, and write $U(t)$ for the height of a homogeneous Poisson sample with expected size $t$ in a rectangle. Rectangle dimensions have no effect on tree shape. The known convergence in probability $U_m/\log m\to c_*$ is sufficient for the lower-bound amplification below.

### 3.1. An elementary upper tail

In the standard uniform BST growth construction, each of the $m$ external leaves is selected with probability $1/m$ at the next insertion. For $z>1$ let $W_m(z)$ be the sum of $z^{\mathrm{depth}}$ over the $m+1$ external leaves after $m$ insertions, starting with $W_0=1$. Replacing a leaf of depth $d$ by two leaves of depth $d+1$ changes $W$ by $(2z-1)z^d$. Hence

\[
\mathbb E W_m(z)=\prod_{i=1}^m\left(1+\frac{2z-1}{i}\right)
\le C_z m^{2z-1}.
\tag{8}
\]

A tree of height $U_m$ has an external leaf of depth $U_m+1$. Markov's inequality therefore gives, for every $a>c_*$ and $z=a/2>1$,

\[
\begin{aligned}
\mathbb P(U_m\ge a\log m)
&\le C_a m^{2z-1-a\log z}\\
&= C_a m^{-I(a)},\qquad
I(a)=1-a\log(2e/a)>0.
\end{aligned}
\tag{9}
\]

For the Poisson model, couple the standard BSTs monotonically in their insertion size and split according to whether a $\operatorname{Poisson}(t)$ count exceeds $2t$. The Poisson upper tail is exponential, and (9), with an arbitrarily small constant slack to absorb $\log(2t)-\log t$, yields

\[
\mathbb P(U(t)>(c_*+\varepsilon)\log t)\le C t^{-a}
\tag{10}
\]

for suitable $a,C>0$ depending on $\varepsilon$. These are distributional comparisons for uniform BSTs, not an assertion that the nested planar-sample heights are monotone.

### 3.2. Lower-tail amplification by disjoint horizontal strips

Fix $\varepsilon\in(0,c_*)$, and choose $\gamma>0$ so small that $(c_*-\varepsilon)/(1-\gamma)<c_*$. Partition the rectangle into $r=\lfloor t^\gamma\rfloor$ horizontal strips of equal area. Their Poisson point processes are independent, each has expected size $t/r$, and its BST height has law $U(t/r)$. By (3), the whole height dominates each strip height. Since

\[
\frac{(c_*-\varepsilon)\log t}{\log(t/r)}
\longrightarrow\frac{c_*-\varepsilon}{1-\gamma}<c_*,
\]

the known homogeneous convergence in probability implies, for all sufficiently large $t$,

\[
\mathbb P\big(U(t/r)\le(c_*-\varepsilon)\log t\big)\le\tfrac12.
\]

Independence now gives

\[
\mathbb P\big(U(t)\le(c_*-\varepsilon)\log t\big)
\le2^{-\lfloor t^\gamma\rfloor}.
\tag{11}
\]

The same conclusions hold for expected size $\lambda t$ with any fixed $\lambda>0$, after absorbing the constant $\log\lambda$ into the $\varepsilon\log t$ slack.

## 4. Polynomial deviation bounds for the top band under A1

Choose $\beta>0$ so that $\rho$ is continuous and bounded away from zero on $[0,\beta]\times[0,1]$. Define

\[
q_0(y)=\rho(0,y),\qquad
J=\int_0^1 q_0(y)\,dy,\qquad
G(y)=J^{-1}\int_0^yq_0(u)\,du.
\]

The map $G$ is increasing. Sending $(x,y)$ to $(x,G(y))$ preserves all permutation orders and BST shapes. The transformed density in the top rectangle is

\[
\widetilde\rho(x,v)=J\frac{\rho(x,G^{-1}(v))}{\rho(0,G^{-1}(v))}.
\tag{12}
\]

By uniform continuity and positivity, its lower and upper bounds $m_\beta,M_\beta$ can be selected with

\[
\frac{m_\beta}{M_\beta}\longrightarrow1\qquad(\beta\downarrow0).
\tag{13}
\]

Consider a Poisson process of intensity $t$ times this density. Couple it below a homogeneous process of intensity $tM_\beta$, and couple a homogeneous process of intensity $tm_\beta$ below it, using independent thinning. If $C$ is a selected chain in the larger process, its retained points form a chain in the smaller process. Conditional on the larger process, each point is retained independently with probability at least $p=m_\beta/M_\beta$.

Fix $\varepsilon>0$. Choose $\beta$ sufficiently small that $p$ is sufficiently close to one. For an upper tail, on a height at least $(c_*+\varepsilon)\log t$ in the variable-density top process, select a chain of $L=\lceil(c_*+\varepsilon)\log t\rceil+1$ vertices. Select $q<p$ with $q(c_*+\varepsilon)>c_*+\varepsilon/2$. Except with probability at most $\exp(-D(q\Vert p)L)$, its thinning into the homogeneous lower process retains at least $qL$ vertices. The latter height then exceeds $(c_*+\varepsilon/2)\log t$ for large $t$. Equation (10) gives a polynomial upper tail.

For a lower tail, start from a homogeneous upper-process chain of $L=\lceil(c_*-\varepsilon/4)\log t\rceil+1$ vertices. Equation (11) ensures its existence except with stretched-exponentially small probability. Choose $q<p$ with $q(c_*-\varepsilon/4)>c_*-\varepsilon/2$ (possible after making $p$ sufficiently close to one). Except with probability at most $\exp(-D(q\Vert p)L)$, thinning retains enough vertices to put the variable-density top height above $(c_*-\varepsilon)\log t$. This gives a polynomial lower tail.

Here $D(q\Vert p)>0$ is the Bernoulli relative entropy for fixed $0<q<p<1$. If $p=1$, thinning has no failures and the homogeneous bounds apply directly. It follows that, for each desired $\varepsilon$, a sufficiently small fixed top-band width $\beta$ gives constants $a,C>0$ such that its height $H_{\rm top}(t)$ satisfies

\[
\mathbb P\big(|H_{\rm top}(t)-c_*\log t|>\varepsilon\log t\big)
\le C t^{-a}.
\tag{14}
\]

This explicitly strengthens the source's top-band convergence argument using its same thinning comparison; convergence in probability alone is not being silently promoted to a rate.

## 5. Hanging-tree heights have arbitrarily strong polynomial bounds

Use the top band in the original $y$-coordinates. Let $m_0>0$ be a lower bound for $\rho$ there and $M<\infty$ a global upper bound. The top points have $y$-coordinates splitting $[0,1]$ into gaps $I_i$. The rest of the BST consists of trees from the points in $(\beta,1]\times I_i$, each attached to the top tree.

Fix $B>0$. Choose a constant $A$ sufficiently large, and partition $[0,1]$ into $\ell=\lceil t/(A\log t)\rceil$ equal intervals. Each corresponding top-band cell has intensity mass at least $t\beta m_0/\ell$. Thus

\[
\mathbb P(\text{some top cell is empty})
\le\ell e^{-t\beta m_0/\ell}\le Ct^{-B}
\tag{15}
\]

when $A$ is chosen large enough. On the complement, every top gap has length at most $2/\ell\le2A\log t/t$.

For any rectangle of area $a_R\le2A\log t/t$, a process of intensity at most $tM$ is dominated by a homogeneous one. The expected number of increasing $r$-point subsequences in the latter is

\[
\frac{(tMa_R)^r}{(r!)^2}\le\frac{(2MA\log t)^r}{(r!)^2}.
\tag{16}
\]

The same bound holds for decreasing subsequences. Every BST chain splits into an increasing and a decreasing subsequence, so its height is at most $\mathrm{LIS}+\mathrm{LDS}$. With $r=\lfloor\varepsilon\log t/2\rfloor$, the chance a given hanging tree has height greater than $\varepsilon\log t$ is bounded by

\[
2\frac{(2MA\log t)^r}{(r!)^2}
=\exp\{-\tfrac{\varepsilon}{2}\log t\log\log t+O(\log t)\}.
\tag{17}
\]

Conditionally on the top process, the right-hand process in each gap is still an independent Poisson process of its restricted intensity. A union bound over its $K+1$ gaps can be averaged using $\mathbb E[K+1]=\beta t+1$. Equations (15)–(17) show that, for any fixed $\varepsilon>0$ and any $B>0$,

\[
\mathbb P\left(\max_i H_{{\rm hang},i}(t)>\varepsilon\log t\right)
=O(t^{-B}).
\tag{18}
\]

The implicit choices of $A$ and constants may depend on $\varepsilon,B,\beta,\rho$; none depends on $t$.

The deterministic top/hanging decomposition gives

\[
H_{\rm top}(t)\le H(t)
\le H_{\rm top}(t)+1+\max_i H_{{\rm hang},i}(t),
\tag{19}
\]

where an empty hanging tree contributes zero in the upper bound. Applying (14) at a smaller $\varepsilon$ and (18) proves that, for the Poisson process of intensity $t\mu$,

\[
\mathbb P\big(|H(t)-c_*\log t|>\varepsilon\log t\big)
\le C_\varepsilon t^{-a_\varepsilon}
\tag{20}
\]

for some positive $a_\varepsilon,C_\varepsilon$.

## 6. De-Poissonization preserves the polynomial rates

A direct conditioning on a Poisson count would lose a factor of order $\sqrt n$, which is unacceptable when $a_\varepsilon$ is small. Chain restriction avoids this loss.

Take the original infinite i.i.d. sequence and independent counts

\[
K_-\sim\operatorname{Poisson}(n-n^{2/3}),\qquad
K_+\sim\operatorname{Poisson}(n+n^{2/3}).
\]

The count events

\[
n-2n^{2/3}\le K_-\le n,
\qquad
n\le K_+\le n+2n^{2/3}
\tag{21}
\]

have complements of probability $O(\exp(-cn^{1/3}))$. The samples $P_{K_\pm}$ have the required Poisson point-process laws.

On the first count event, if $H_n$ is at least $(c_*+\varepsilon)\log n$, select a chain of $L=\lceil(c_*+\varepsilon)\log n\rceil+1$ vertices using only the unordered geometry of $P_n$. Conditional on that geometry and $K_-$, the removed labels form a uniform subset of size at most $2n^{2/3}$. The chance that at least $d=\lceil\varepsilon\log n/3\rceil$ of the $L$ selected chain vertices are deleted is at most

\[
\binom Ld(2n^{-1/3})^d
\le 2^L(2n^{-1/3})^d
=\exp\{-\Theta((\log n)^2)\}.
\tag{22}
\]

If fewer are deleted, the retained chain forces $H_{K_-}$ above $(c_*+\varepsilon/2)\log n$ for all large $n$. Equation (20), with slack to absorb $\log(n-n^{2/3})-\log n=o(1)$, bounds that event by a negative power of $n$. Thus the desired upper deviation bound holds at fixed size $n$.

For the lower deviation, use $K_+$ and a canonical chain in $P_{K_+}$ of $L=\lceil(c_*-\varepsilon/2)\log n\rceil+1$ vertices, when one exists. Conditional on $K_+$ and its unordered geometry, $P_n$ is a uniform subset of size $n$; at most $2n^{2/3}$ points are removed on (21). The same calculation bounds the chance of losing $\lceil\varepsilon\log n/3\rceil$ chain vertices by $\exp(-\Theta((\log n)^2))$. Otherwise the retained chain puts $H_n$ above $(c_*-\varepsilon)\log n$. The chance the endpoint chain does not exist is polynomially small by (20), using a smaller $\varepsilon$ there.

We conclude that for every $\varepsilon\in(0,c_*)$,

\[
\boxed{\quad
\mathbb P\big(|H_n-c_*\log n|>\varepsilon\log n\big)
\le C_\varepsilon n^{-a_\varepsilon}
\quad}
\tag{23}
\]

for suitable positive $a_\varepsilon,C_\varepsilon$ and all sufficiently large $n$. Equation (23) is precisely hypothesis (4) of the upgrade lemma. That lemma completes the proof of Q1886.

## Dependencies and checks

- The only non-elementary asymptotic input is the established uniform BST convergence $U_n/\log n\to c_*$ in probability (Devroye, 1986), already used in the source paper and contained in its Theorem 1.1 specialized to Lebesgue measure.
- The argument explicitly handles the nonmonotone coupling identified in source Remark 1. Its key new estimate is the upward-crossing factor $(h+1)/n$.
- The top-band width is fixed after an error tolerance is chosen. No rate of continuity of $\rho$ is assumed.
- The density is required to be bounded globally only for the hanging-tree estimate; positivity and continuity are used only in a fixed neighborhood of the left edge.
- All bounds use graph height; changes of one caused by vertex-versus-edge conventions are absorbed by the displayed positive $\log n$ margins.
- Conditional thinning and hypergeometric arguments use chains selected from unordered geometry, ensuring the required exchangeability with the i.i.d. labels.
- The proof establishes marginal polynomial rates as an additional result; it does not infer summability merely from convergence in probability or $L^p$ convergence.

## Finite deterministic verification

The accompanying `verify_bst_crossings.py` exhaustively checked all 46,233 permutations of sizes 1 through 8, including 362,879 single-point deletions. Every retained ancestor relation survived, height could rise by at most one on addition, and the number of points whose deletion lowers the current height was at most height plus one. It also checked 158,323 restrictions to horizontal rank intervals for sizes through 7. All assertions passed. These finite checks validate the combinatorial ingredients on their declared domains; the limit theorem follows from the written proof, not from computation. Raw output is in `bst_crossing_verification.json`.


# A local-density partial result for the universal BST lower bound

**Stable statement ID:** `9555ab5eed7e5e643fb2`.  
**Primary source:** Corsini–Dubach–Féray, arXiv:2403.03151v2, 27 January 2025, Conjecture 1 and Proposition 5.5, https://arxiv.org/html/2403.03151v2 .  
**Status:** The universal arbitrary-permuton assertion has not been proved or disproved in this work. The following strengthens the mode of convergence in its established local-density case.

## Corollary

Suppose $\mu$ is a permuton whose restriction to some nondegenerate rectangle

\[
R=[0,\beta]\times[a,b],\qquad \beta>0,\quad 0\le a<b\le1,
\]

has a continuous density that is strictly positive throughout $R$. No assumption is imposed on $\mu$ outside $R$, beyond its being a permuton. For one infinite i.i.d. $\mu$-sequence and its nested sample BST heights $H_n$,

\[
\liminf_{n\to\infty}\frac{H_n}{\log n}\ge c_*
\quad\text{almost surely}.
\]

This covers a continuous positive density in a neighborhood of a single left-edge point. It allows singular components and unbounded or absent densities outside the selected rectangle.

## Proof

Shrink $\beta$ if necessary and transform $y$ monotonically using the integral of the boundary density $\rho(0,y)$. Exactly as in §4 of `Q1886-proof.md`, the transformed density on $R$ can be trapped between positive constants whose ratio is arbitrarily close to one. A homogeneous upper Poisson process, followed by independent thinning and restriction of a selected logarithmic-size chain, gives polynomial lower-tail bounds

\[
\mathbb P\big(h(T(P(t)\cap R))<(c_*-\varepsilon)\log t\big)
\le C_\varepsilon t^{-a_\varepsilon}.
\]

The homogeneous lower-tail input is derived by independent horizontal-strip amplification in §3.2 of that proof. No global upper density bound enters this argument.

Every chain in $T(P\cap R)$ is a chain in $T(P)$. Indeed, the ancestor criterion can only be invalidated by an earlier-$x$ point with $y$ between the two chain endpoints. Points outside $R$ either have $x>\beta$ and hence are later than every point of $R$, or have $y$ outside $[a,b]$ and hence cannot lie between two of its $y$-coordinates. Consequently $H(P)\ge h(T(P\cap R))$. The preceding polynomial lower-tail bound applies to $H(P(t))$ for the entire process.

The lower half of §6 in `Q1886-proof.md` de-Poissonizes this bound without any density assumption: compare a fixed-size sample with an independent $\operatorname{Poisson}(n+n^{2/3})$ endpoint, and restrict a canonical chain. Deleting a fraction $O(n^{-1/3})$ of uniformly random labels loses a positive multiple of $\log n$ selected chain vertices with probability $\exp(-\Theta((\log n)^2))$. Thus

\[
\mathbb P\big(H_n<(c_*-\varepsilon)\log n\big)
\le C_\varepsilon n^{-a_\varepsilon}.
\]

Finally, apply only the endpoint-chain lower-bound part of the upgrade lemma (§2.2). It requires these lower marginal bounds and the chain restriction property, but no upper-tail control. This gives the stated almost-sure liminf.

## Remaining obstruction

This corollary does not handle permutons for which every left-edge neighborhood fails the positive continuous density condition, including general singular permutons. The top/hanging argument proves an upper asymptotic only under A1 and supplies no universal lower comparison in that class. The universal statement in Q1885 must therefore remain listed as unresolved.


# Rooted common-subtree scaling

Stable statement ID: `b252bb236c6d560e7c49`.

Evidence status: complete written proof, checked independently in this session by two other research agents against the primary source. No proof-assistant compilation or external peer review. The proof uses the uniform exceptional-event estimates of Angel, Atamanchuk, Brandenberger, Donderwinkel and Khanfir, *The largest common subtree of two random trees*, arXiv:2601.00119v1 (31 December 2025), Proposition 4.3 and the elementary deterministic estimates in its application. These are hypotheses supplied by an existing primary theorem, not estimates proved anew here.

## Exact statement and assumptions

Let the independent trees $\tau_n,\tau'_n$ have critical, nondegenerate offspring distributions $\mu,\mu'$ conditioned to have $n$ vertices, along their common admissible sizes. Assume $\sigma^2,\sigma'^2\in(0,\infty)$ and $\sum k^{2+\kappa}\mu(k)<\infty$ for some $\kappa>0$. Let $L_n^\bullet$ count vertices in a largest common subtree whose two embeddings map its root to the original roots. Let

$$c=\mathbb E L^\bullet(\tau_*,\tau'_*)$$

with root offspring distributions $(k+1)\mu(k+1)$ and $(k+1)\mu'(k+1)$ and ordinary offspring below the roots. Then, jointly in rooted Gromov--Hausdorff topology for the tree coordinates and the usual topology for the third coordinate,

$$\left(n^{-1/2}\tau_n,n^{-1/2}\tau'_n,n^{-1/2}L_n^\bullet\right)
\Rightarrow
\left(2\mathcal T/\sigma,2\mathcal T'/\sigma',
c\min\{2H(\mathcal T)/\sigma,2H(\mathcal T')/\sigma'\}\right).$$

Forgetting the marks yields exactly the retained statement. The existing moment assumptions give $1\le c<\infty$.

## 1. The precise uniform input

The source's Proposition 4.3, transferred to conditioned trees using its size local limit and degree/height bounds, has the following usable form. Fix sufficiently small $\alpha>0$. A deterministic integer $d$ can be chosen so that for every $\eta>0$ the following statements hold with probability tending to one. In particular, $d$ is independent of both $n$ and $\eta$. Put $a=n^{1/2-2\alpha}$ and $b=n^{1/2-\alpha}$.

1. For every pair of equally long simple paths $(x_0,\ldots,x_\ell)$ and $(x'_0,\ldots,x'_\ell)$, let $C_i,C'_i$ be the components at their respective $i$th vertices after deleting the path edges. Then
   $$\left|c\ell-\sum_{i=0}^{\ell}\big(L^\bullet(C_i,C'_i)\wedge b\big)\right|\le\eta\sqrt n.$$
2. No common subtree has a path with $d$ distinct vertices each carrying an off-path component of more than $a$ vertices.
3. No vertex of a common subtree has $d$ incident components with more than $a$ vertices each.
4. At every vertex of every common subtree, if its incident component sizes are $s_1,\ldots,s_j$, then $\sum_i(s_i\wedge a)\le b-1$.

The integer $d$ can be selected before $\eta$: apply Proposition 4.3 with a polynomial exponent $m>3$. The conditioning probability for each tree is of order $n^{-3/2}$ along admissible sizes, so the exceptional probability remains $o(1).$ The other conditions in its event $A_n$ hold with probability tending to one by the source's Proposition 2.6 and Lemma 2.7. These observations fix all quantifiers needed below.

## 2. A deterministic upper bound that applies to every common subtree

Take any common subtree $S$ on a good event. Define its core $R$ by retaining exactly those edges that split $S$ into two parts of more than $a$ vertices, together with their endpoints. If there is no such edge, let $R$ be a centroid singleton.

The retained edges, when present, form a connected subtree: every edge on the path between two retained edges has one of their large outer components on each side. At any core vertex, every incident core edge leads to a component of more than $a$ vertices, so property 3 bounds the core degree by $d-1$. Every internal core branch vertex on a path has a third large component away from that path. Property 2 therefore bounds the number of core branch vertices on any path by $d-1$.

After suppressing degree-two vertices, the core has a bounded number of vertices and leaves, depending only on $d$. For definiteness, a crude bound $B=1+d+d^2+\cdots+d^{d+2}$ suffices for both numbers. The singleton and single-edge cases are included separately in this bound.

Let $D_u$ be the component at $u\in R$ after deleting core edges from $S$. Every component off the core has at most $a$ vertices. This follows from the definition of a retained edge; in the singleton case it follows from the centroid property. Property 4 therefore gives $|D_u|\le b$.

Partition the core into its suppressed vertices and the open chains joining them. At every vertex interior to such a chain, $D_u$ is a root-preserving common subtree of the ambient path-deletion components, so its size is bounded by their common-subtree size truncated at $b$. Property 1 bounds the sum along each open chain by $c$ times the chain length plus $\eta\sqrt n$ (dropping the nonnegative endpoint terms only improves this upper bound). There are at most $B$ chains and at most $B$ suppressed vertices. Consequently

$$|S|\le c\,|E(R)|+B\eta\sqrt n+B b.\tag{U}$$

The proof never used that $S$ was an unrooted maximum. That uniformity is the crucial feature.

Now suppose $S$ is rooted, and both embeddings preserve the original roots. Enlarge $R$ inside $S$ by the unique path from its root $r$ to $R$, calling the result $R^+$. This is still a common subtree with root-preserving embeddings. Adding one path increases its leaf count by at most one, and $|E(R^+)|\ge |E(R)|$. If $F_N^\bullet(t,t')$ denotes the maximum edge count of a root-preserving common subtree with at most $N$ (unrooted degree-one) leaves, take $N=B+1$. Then (U) implies

$$L_n^\bullet\le c F_N^\bullet(\tau_n,\tau'_n)+B\eta\sqrt n+B b.\tag{RU}$$

This does not assume that the unrooted core already contains the root.

## 3. A rooted lower bound

Put $h_n=\min\{H(\tau_n),H(\tau'_n)\}$. Choose root-starting paths of $h_n$ edges in the two trees and match them from their roots. At each vertex, choose a largest root-preserving common subtree of its two path-deletion components. These choices occupy disjoint ambient components, so gluing them along the matched path gives a root-preserving common subtree of the original pair. Thus property 1 gives

$$L_n^\bullet\ge\sum_{i=0}^{h_n}L^\bullet(C_i,C'_i)
\ge c h_n-\eta\sqrt n.\tag{RL}$$

The component sizes include their attachment vertices, so the sum counts each vertex exactly once; no subtraction is missing.

## 4. Rooted finite-skeleton functional

For rooted compact real trees $(T,r),(T',r')$, define $F_N^\bullet$ as the largest total length of a common real subtree containing the roots and mapping root to root, with at most $N$ leaves. The discrete definition agrees after replacing edges by unit intervals: a real embedding can have its terminal partial edges shortened to vertices, losing at most $N$ in length. Exact equality is unnecessary; after division by $\sqrt n$ this bounded discrepancy vanishes. Branch vertices in a real common subtree necessarily lie at discrete vertices; its marked root is a discrete vertex, and all root-to-branch lengths are integral. Hence the terminal shortening works simultaneously in both embeddings.

**Upper semicontinuity.** For fixed $N$, $F_N^\bullet$ is upper semicontinuous under rooted Gromov--Hausdorff convergence. To see this, choose nearly maximizing common subtrees, enumerate their at most $N$ leaves (repeat leaves if needed), and include the root as an additional marked point. Along a subsequence, all marked points converge through correspondences in the two ambient compact limit trees. Their pairwise distance matrices remain equal, including root distances. The root remains in the span of the limiting leaves: before the limit it lies on a geodesic between a pair of leaves, and a further subsequence fixes that pair. The limiting distance equality keeps it on the same geodesic. The singleton case is immediate. Thus root marking cannot create an extra leaf. The two resulting finite spans are isometric with their roots matched. Their common total length is the limit of the finite-span lengths, and their leaf counts do not increase. This proves the claimed limsup bound. One elementary justification of length continuity is the identity

$$2\operatorname{length}(\operatorname{Span}(z_1,\ldots,z_q))
=\min_{\pi\in\mathfrak S_q}\sum_{i=1}^{q}d(z_{\pi(i)},z_{\pi(i+1)}),\qquad \pi(q+1)=\pi(1).$$

Every tour crosses each spanning-tree edge at least twice, while a depth-first traversal attains equality. This is a minimum of finitely many continuous functions of the distance matrix.

**Independent Brownian CRTs.** Their roots are leaves almost surely. Their branch points form countable sets, enumerable by the common ancestors of pairs of independent samples from the fully supported mass measure. For any fixed pair of such samples, the positive root-to-common-ancestor distance has a continuous distribution, by the Brownian CRT reduced-tree density. Independence and a countable union show that the two deterministic rescalings $2\mathcal T/\sigma$ and $2\mathcal T'/\sigma'$ almost surely have no branch points at equal root distance.

Any common rooted real subtree with a branch point would induce such a pair of equal-depth ambient branch points. Therefore every common rooted real subtree is an interval starting at the root, and for each fixed $N\ge2$,

$$F_N^\bullet(2\mathcal T/\sigma,2\mathcal T'/\sigma')
=\min\{2H(\mathcal T)/\sigma,2H(\mathcal T')/\sigma'\}.\tag{C}$$

Root-height is continuous under rooted Gromov--Hausdorff convergence. The longest common root-starting path supplies a lower bound by the minimum heights. Combining this lower bound, upper semicontinuity, (C), and a Skorokhod representation proves, jointly with the two rooted tree limits,

$$n^{-1/2}F_N^\bullet(\tau_n,\tau'_n)\Rightarrow
\min\{2H(\mathcal T)/\sigma,2H(\mathcal T')/\sigma'\}.$$

More strongly, $n^{-1/2}(F_N^\bullet(\tau_n,\tau'_n)-h_n)\to0$ in probability.

## 5. Completion

On good events, (RL) and (RU) give

$$-\eta\le\frac{L_n^\bullet-c h_n}{\sqrt n}
\le c\frac{F_N^\bullet-h_n}{\sqrt n}+B\eta+B n^{-\alpha}.$$

The integer $B$ is fixed independently of $\eta$. First let $n\to\infty$, then let $\eta\downarrow0$. The exceptional probabilities vanish, and the skeleton discrepancy tends to zero in probability. Hence

$$L_n^\bullet=c\min\{H(\tau_n),H(\tau'_n)\}+o_{\mathbb P}(\sqrt n).$$

Joint rooted CRT convergence and continuity of height finish the proof. No replacement of either offspring law, moment assumption, root convention, isomorphism convention, or admissible-size quantifier was made.

## Primary references and validation

- Angel et al., arXiv:2601.00119v1, §§2, 4.2 and 6(i): https://arxiv.org/html/2601.00119v1 . Proposition 4.3 is the substantive probability input. Its deterministic application is checked directly above for arbitrary common subtrees.
- Aldous, *The continuum random tree III*, Annals of Probability 21 (1993), 248--289, Lemma 21 and equation (33), printed p. 277; Corollary 22, printed p. 279: https://www.stat.berkeley.edu/~aldous/Papers/CRT3.pdf . The positive reduced-edge vector has a density. For two sampled leaves its stem length is the root-to-common-ancestor height and is therefore diffuse. Aldous codes the tree by twice the normalized excursion; the deterministic factor does not affect diffuseness.
- No finite simulation supplies any step in the proof. No formal proof assistant has been run.


# Limited-memory depth and subcritical height fluctuations

**Programme:** B6. **Question:** provisional Q2495 (stable ID `c8efa831871a9b89e030`). **Status at the retained statement's full scope:**
partial. The result below determines the height fluctuations for every fixed
\(0<\beta<1/2\). The critical and supercritical height laws remain unresolved.

The retained question asks: “For each fixed \(\beta\in(0,1)\), determine the
scale and limiting distribution of \(H_n-\mathbb E H_n\), including the
transition at \(\beta=1/2\).” No change is made to the tree model. This is a
complete written argument, independently checked in two parallel mathematical
reviews; no proof assistant was run. A literature search found no matching
fluctuation theorem, but that search does not establish novelty.

## 1. Model and results

Start with vertex \(1\). For each integer \(m\ge2\), independently choose the
parent of \(m\) uniformly from

\[
\left\{\max\!\left(1,m-1-\lfloor(m-1)^\beta\rfloor\right),\ldots,m-1\right\}.
\]

Write

\[
\begin{aligned}
a_m&=\min\!\left(m-1,\lfloor(m-1)^\beta\rfloor+1\right),
&b_m&=\frac{2}{a_m+1},\\
F(1)&=0,
&F(n)&=\sum_{m=2}^n b_m,\\
D_n&=d(1,n),
&H_n&=\max_{1\le v\le n}d(1,v),\\
s_n^2&=\frac{2}{3(1-\beta)}n^{1-\beta}.
\end{aligned}
\]

The finite sum \(F(n)\) retains the exact integer window. Throughout, all
implicit constants may depend on the fixed parameter \(\beta\).

**Theorem A: depth of one vertex.** For every fixed \(0<\beta<1\),

\[
\begin{gathered}
0\le F(n)-\mathbb E D_n=O(\log(n+1)),
\qquad \operatorname{Var}(D_n)\sim s_n^2,\\
\frac{D_n-\mathbb E D_n}{s_n}\ \xrightarrow{d}\ \mathcal N(0,1),
\qquad
\frac{D_n-F(n)}{s_n}\ \xrightarrow{d}\ \mathcal N(0,1).
\end{gathered}
\]

**Theorem B: maximum height below the transition.** For every fixed
\(0<\beta<1/2\),

\[
\begin{gathered}
\operatorname{Var}(H_n)\sim s_n^2,\\
\frac{H_n-\mathbb E H_n}{s_n}\ \xrightarrow{d}\ \mathcal N(0,1),
\qquad
\frac{H_n-F(n)}{s_n}\ \xrightarrow{d}\ \mathcal N(0,1).
\end{gathered}
\]

Theorem A concerns a single vertex. The transfer to the maximum in Theorem B
uses the additional estimate

\[
\|H_n-D_n\|_2=O\!\left(n^{\beta/2}\log(n+1)\right),
\tag{1}
\]

proved below for every fixed \(0<\beta<1\). Its right side is smaller than
\(s_n\) precisely in the subcritical range \(\beta<1/2\).

Although \(F(n)\sim 2n^{1-\beta}/(1-\beta)\), replacing this exact centering
by its leading equivalent is not automatically permissible on the
central-limit scale. The floor corrections are particularly significant when
\(\beta\le1/3\).

## 2. Window regularity and an occupation bound

The sequence \((a_m)\) is nondecreasing, its increments belong to
\(\{0,1\}\), and

\[
a_m\sim m^\beta,\qquad a_m=o(m),\qquad
\frac{a_{m-a_m+1}}{a_m}\longrightarrow1.
\tag{2}
\]

Define the downward jumps of \((b_m)\) by
\(\delta_q=b_q-b_{q+1}\ge0\). At a jump \(a_q=k\), \(a_{q+1}=k+1\),

\[
\delta_q=\frac{2}{(k+1)(k+2)};
\]

otherwise \(\delta_q=0\). Since each integer window size is passed at most
once,

\[
\sum_{q=2}^{n-1}a_q\delta_q=O(\log(n+1)).
\tag{3}
\]

For sufficiently large \(q\), if \(m>q\) and \(m-q\le a_m\), then

\[
q<m\le q+C a_q,\qquad a_q\le a_m\le C a_q.
\tag{4}
\]

Indeed, \(a_m\le m/2\) for all large \(m\), so the displayed condition
implies \(m\le2q\). Regular variation and monotonicity then prove (4).
For each of the finitely many smaller \(q\), the set of such \(m\) is
bounded because \(m-a_m\to\infty\).

Explore the ancestry of \(n\) as a decreasing Markov chain

\[
X_0=n,\qquad X_{i+1}=X_i-U_i,
\qquad
\mathcal L(U_i\mid X_i=m)=\operatorname{Unif}\{1,\ldots,a_m\},
\]

stopped at \(\tau=\inf\{i:X_i=1\}=D_n\). Parent variables at smaller
labels have not yet been exposed, which gives this Markov property.

**Occupation lemma.** Put
\(I_q=\{m>q:m-q\le a_m\}\). Uniformly over the starting label \(n\),

\[
\mathbb E_n\sum_{i<\tau}\mathbf1_{\{X_i\in I_q\}}\le C.
\tag{5}
\]

**Proof.** By (4), \(I_q\subset(q,q+C_0a_q]\). A decreasing chain visits
this interval during at most one time interval. For each step started in
it, the conditional mean decrement is at least \(a_q/2\). The sum of all
decrements started in the interval telescopes to at most its length plus
the final overshoot, which is at most \(C_1a_q\). Taking expectations of
the conditional mean decrements bounds the expected number of visits by a
constant. A path that jumps over the interval contributes no visits. The
finitely many small \(q\) are covered by increasing the constant. \(\square\)

## 3. A clock with only logarithmic accumulated drift

For \(U\) uniform on \(\{1,\ldots,a_m\}\), define

\[
r_m=\mathbb E\big[F(m)-F(m-U)\big]-1.
\]

Monotonicity of \(b_m\) gives

\[
F(m)-F(m-u)=\sum_{j=m-u+1}^m b_j\ge u b_m,
\qquad \mathbb E[U b_m]=1,
\]

so \(r_m\ge0\). Expanding the excess through the jumps of \(b_m\) gives

\[
0\le r_m\le a_m\sum_{q=m-a_m+1}^{m-1}\delta_q.
\tag{6}
\]

Every index here is at least \(2\), because \(m-a_m\ge1\).
Regular variation also gives a uniform bound

\[
0\le F(m)-F(m-u)
\le a_m b_{m-a_m+1}\le C,
\qquad 1\le u\le a_m.
\tag{7}
\]

In particular, \(r_m\) is uniformly bounded.

Let \(R_n=\sum_{i<\tau}r_{X_i}\). Tonelli's theorem, (6), (4), the
occupation lemma and (3) yield

\[
\begin{aligned}
\mathbb E R_n
&\le \sum_{q=2}^{n-1}\delta_q\,
\mathbb E\sum_{i<\tau}a_{X_i}
\mathbf1_{\{q<X_i,\ X_i-q\le a_{X_i}\}}\\
&\le C\sum_{q=2}^{n-1}a_q\delta_q
=O(\log(n+1)).
\end{aligned}
\tag{8}
\]

The indicator in the first line is slightly larger than the one required
by (6), which preserves the upper bound.

The strong Markov property improves (8) to

\[
\mathbb E R_n^2=O(\log^2(n+1)).
\tag{9}
\]

To see this explicitly, let
\(K_n=\sup_{m\le n}\mathbb E_m R_m=O(\log(n+1))\). Expand the square of
the accumulated reward into its diagonal terms and twice the sum over
ordered pairs \(i<j\). Since \(r_m\le B\), the diagonal is at most
\(B R_n\). Conditional on the state just after a given step, the expected
remaining reward is at most \(K_n\). Thus

\[
\mathbb E R_n^2\le(B+2K_n)\mathbb E R_n,
\]

which proves (9).

## 4. Martingale decomposition and the depth limit

For \(i<\tau\), define

\[
Z_i=F(X_i)-F(X_{i+1})-(1+r_{X_i}),
\qquad M_n=\sum_{i<\tau}Z_i.
\]

These are martingale differences in the ancestry-exploration filtration.
Pad the array with zeros after \(\tau\); there are at most \(n-1\)
nonzero terms. By (7), their absolute values are bounded by a fixed
constant. Telescoping gives the exact identity

\[
D_n=F(n)-M_n-R_n.
\tag{10}
\]

Consequently \(\mathbb E D_n=F(n)-\mathbb E R_n\), proving the claimed
mean estimate.

Put

\[
v_m=\operatorname{Var}\big(F(m)-F(m-U)\big),
\qquad U\sim\operatorname{Unif}\{1,\ldots,a_m\}.
\]

Equation (2) implies

\[
\sup_{1\le u\le a_m}
\left|F(m)-F(m-u)-b_mu\right|
\le a_m\left(b_{m-a_m+1}-b_m\right)\longrightarrow0.
\]

Since \(b_mU\) is bounded and

\[
\operatorname{Var}(b_mU)
=\frac{a_m-1}{3(a_m+1)}\longrightarrow\frac13,
\]

we have \(v_m\to1/3\) and \(\sup_m v_m<\infty\). Orthogonality gives

\[
\mathbb E M_n^2
=\mathbb E\sum_{i<\tau}v_{X_i}
\le C\mathbb E D_n\le CF(n).
\tag{11}
\]

Moreover,

\[
F(n)\sim\frac{2}{1-\beta}n^{1-\beta}.
\tag{12}
\]

Combining (8), (10) and (11) proves \(D_n/F(n)\to1\) in \(L^1\).
The predictable quadratic variation satisfies

\[
\frac1{F(n)}\sum_{i<\tau}v_{X_i}\longrightarrow\frac13
\quad\text{in }L^1.
\tag{13}
\]

Indeed, for any \(\varepsilon>0\), choose \(K\) so that
\(|v_m-1/3|\le\varepsilon\) for \(m>K\). The contribution of labels at
most \(K\) is bounded deterministically by \(CK\), since the chain
strictly decreases. The remaining error is at most \(\varepsilon D_n\).
Divide by \(F(n)\), take expectations, and then let \(\varepsilon\downarrow0\).

The martingale triangular-array central limit theorem now applies. Its
conditional Lindeberg condition holds because the unnormalized increments
are uniformly bounded and \(F(n)\to\infty\); its conditional variance
condition is (13). Therefore

\[
\frac{M_n}{\sqrt{F(n)/3}}\xrightarrow{d}\mathcal N(0,1).
\]

By (9), both \(R_n\) and \(R_n-\mathbb E R_n\) are negligible in \(L^2\)
after division by \(\sqrt{F(n)}\). Equation (10), symmetry of the normal
law and (12) prove both central limit statements in Theorem A.

Finally, (13) gives \(\mathbb E M_n^2\sim F(n)/3\). The error in replacing
\(\operatorname{Var}(D_n)\) by \(\operatorname{Var}(M_n)\) is bounded by

\[
O\!\left(\log^2(n+1)+\sqrt{F(n)}\log(n+1)\right)=o(F(n)),
\]

using Cauchy--Schwarz and (9). This proves
\(\operatorname{Var}(D_n)\sim F(n)/3\sim s_n^2\), completing Theorem A.

The standard probabilistic input here is the conditional-variance,
conditional-Lindeberg martingale CLT. See B. M. Brown, *Martingale Central
Limit Theorems*, Annals of Mathematical Statistics **42** (1971), 59–66,
[DOI](https://doi.org/10.1214/aoms/1177693494), and the formulation discussed
by J.-C. Mourrat, *On the rate of convergence in the martingale central
limit theorem*, Bernoulli **19** (2013), 633–645,
[arXiv:1103.5050v2](https://arxiv.org/abs/1103.5050v2). All its hypotheses
are checked above.

## 5. Controlling the drift over the whole tree

Use \(R_v\) for the accumulated clock drift along the full ancestry of
vertex \(v\), in the same tree, and let

\[
R_*^{(n)}=\max_{v\le n}R_v.
\]

The preceding argument gives \(\sup_{v\le n}\mathbb E R_v\le K_n\), with
\(K_n=O(\log(n+1))\), and \(\sup_mr_m\le B\). The strong Markov property
gives constants \(c,C>0\) such that

\[
\mathbb P(R_v>t)\le C\exp\!\left(-\frac{ct}{K_n+B}\right),
\qquad t\ge0.
\tag{14}
\]

For a direct proof, follow one ancestry and stop each time the accumulated
reward since its preceding stop first exceeds \(2K_n\). Markov's inequality
bounds the probability of reaching any such stop by \(1/2\), uniformly over
the starting state. The reward at a stop exceeds \(2K_n\) by at most \(B\).
After each stop the same conditional estimate applies. Hence

\[
\mathbb P\big(R_v>k(2K_n+B)\big)\le2^{-k},
\qquad k\ge1,
\]

which proves (14). No independence between different vertices is required.
A union bound over \(v\le n\) and integration of the tail yield

\[
\mathbb E\left[(R_*^{(n)})^2\right]=O(\log^4(n+1)).
\tag{15}
\]

## 6. Comparing neighboring birth labels

Call \((v,u)\) an *eligible pair* if \(2\le v\le n\) and \(u\) belongs to
the eligible-parent interval of \(v\). There are at most \(n^2\) such
pairs. For a fixed pair, expose the two ancestral lines by always revealing
the parent of the larger active label, stopping when the active labels
coincide.

**Eligibility invariant.** If the active labels are \(x>y\), then \(y\)
belongs to the eligible-parent interval of \(x\). Write
\(\ell(x)=x-a_x\); this lower endpoint is nondecreasing. The invariant is
true initially. If the newly revealed parent \(z\) of \(x\) satisfies
\(z>y\), then \(\ell(z)\le\ell(x)\le y\). If \(z<y\), then
\(z\ge\ell(x)\ge\ell(y)\). These preserve the invariant; \(z=y\) is
coalescence.

The larger active label strictly decreases after every revelation. Thus
each revealed parent is fresh and conditionally uniform on its original
eligible interval. The conditional probability of coalescence is
\(1/a_x\ge1/a_n\). Let \(L_{v,u}\) be the number of revelations. This
counts the sum of both branch lengths up to their most recent common
ancestor, and

\[
\mathbb P(L_{v,u}>t)\le e^{-t/a_n},\qquad t\ge0.
\tag{16}
\]

Give the original \(v\) side sign \(+1\) and the original \(u\) side sign
\(-1\). At each step its sign is predictable. The signed sum of the clock
martingale increments is therefore again a martingale; denote its terminal
value by \(M_{v,u}\). Telescoping the signed clock decreases and generation
counts gives

\[
D_v-D_u=F(v)-F(u)-M_{v,u}-R_{v,u},
\]

where \(R_{v,u}\) is the corresponding signed drift sum. Shared ancestry
cancels exactly, and

\[
|R_{v,u}|\le R_v+R_u\le2R_*^{(n)}.
\]

Since \((v,u)\) is eligible, (7) gives \(F(v)-F(u)\le C\). Consequently,

\[
D_v-D_u\le C+|M_{v,u}|+2R_*^{(n)}.
\tag{17}
\]

**Uniform martingale bound.** We claim

\[
\mathbb E\left[\left(\max_{(v,u)\text{ eligible}}|M_{v,u}|\right)^2\right]
=O\!\left(a_n\log^2(n+1)\right).
\tag{18}
\]

Set

\[
t_n=\min\!\left(n,\left\lceil10a_n\log(n+1)\right\rceil\right).
\]

If \(t_n=n\), all explorations finish by \(t_n\). Otherwise, (16) and a
union bound show that the probability any pair takes longer than \(t_n\)
is at most \(n^{-8}\). Stop each pair martingale at
\(L_{v,u}\wedge t_n\). Its increments have a fixed absolute bound \(B_1\),
so Azuma--Hoeffding and a union bound give

\[
\mathbb P\!\left(\max_{(v,u)}|M^{\mathrm{stopped}}_{v,u}|>x\right)
\le\min\!\left(1,2n^2\exp\!\left(-\frac{x^2}{2B_1^2t_n}\right)\right).
\]

Integration gives an \(O(t_n\log(n+1))\) second moment. Every full or
stopped martingale is bounded in absolute value by \(B_1n\). Thus the
exceptional event contributes at most \(O(n^2n^{-8})\), proving (18).
Independence between different pair explorations is never used.

## 7. Transfer to maximum height

Let \(P_n\) be the root-to-\(n\) path. For each \(2\le v<n\), let \(u\)
be its first vertex with label strictly below \(v\). If \(x\ge v\) is the
preceding vertex on this path, then

\[
u\ge\ell(x)\ge\ell(v),\qquad u<v.
\]

Thus \((v,u)\) is an eligible pair. If \(v\) itself is on \(P_n\), its
parent is the required \(u\). Vertex \(1\) cannot increase the maximum
height and needs no such choice.

Since \(D_u\le D_n\), we have \(D_v-D_n\le D_v-D_u\). The uniform bound
(17) therefore yields

\[
0\le H_n-D_n
\le C+\max_{(v,u)\text{ eligible}}|M_{v,u}|+2R_*^{(n)}.
\]

Applying (15) and (18),

\[
\begin{aligned}
\|H_n-D_n\|_2
&=O\!\left(\sqrt{a_n}\log(n+1)+\log^2(n+1)\right)\\
&=O\!\left(n^{\beta/2}\log(n+1)\right).
\end{aligned}
\tag{19}
\]

The last equality uses fixed \(\beta>0\). In particular, for
\(\beta<1/2\),

\[
\|H_n-D_n\|_2=o\!\left(n^{(1-\beta)/2}\right)=o(s_n).
\tag{20}
\]

Centering changes this \(L^2\) bound by at most a factor of two, so
Theorem A and (20) give the expectation-centered height CLT.
The same \(L^2\) approximation proves
\(\operatorname{Var}(H_n)\sim\operatorname{Var}(D_n)\). Finally,
\(\mathbb E D_n-F(n)=O(\log n)\) and
\(\mathbb E(H_n-D_n)=o(s_n)\), so centering directly by \(F(n)\) is
permissible. This completes Theorem B.

## 8. Bounded numerical checks

The script `check_memory.py` evaluated the exact algebraic recurrences for
the first two depth moments through \(n=500{,}000\), using long-double
floating arithmetic. The rational exponents \(1/5,2/5,1/2,3/4\) used integer
power comparisons for every floor, so the windows match the stated model.

The variance ratio in the last column is \(\operatorname{Var}(D_{500000})/s_{500000}^2\).

| \(\beta\) | \(\mathbb E D_{500000}\) | \(F(500000)-\mathbb E D_{500000}\) | \(\operatorname{Var}(D_{500000})\) | Variance ratio |
|---|---:|---:|---:|---:|
| \(1/5\) | 79,308.9403 | 0.9233 | 22,062.4364 | 0.7306 |
| \(2/5\) | 8,572.7108 | 2.5584 | 2,784.6715 | 0.9542 |
| \(1/2\) | 2,787.5027 | 3.4144 | 917.0708 | 0.9727 |
| \(3/4\) | 195.6014 | 5.7317 | 66.0052 | 0.9308 |

For each exponent, 2,048 independent complete trees were also simulated to
\(n=30{,}000\), using NumPy PCG64 with seeds 20261008–20261011, in the
order above. Every eligible parent's depth was retained in a ring buffer;
the maximum is the actual full-tree height.

| \(\beta\) | Sample mean \(H_{30000}-D_{30000}\) | Sample \(\operatorname{Var}(D_{30000})\) | Sample \(\operatorname{Var}(H_{30000})\) |
|---|---:|---:|---:|
| \(1/5\) | 0.7202 | 1,870.1723 | 1,871.6111 |
| \(2/5\) | 4.5381 | 470.0296 | 469.2343 |
| \(1/2\) | 8.7246 | 214.7579 | 192.4800 |
| \(3/4\) | 13.4731 | 29.4245 | 12.7474 |

All cases completed in 12.52 seconds under the declared 110-second process
budget. The raw observations at \(n=1{,}000,10{,}000,30{,}000\) are in
`raw_beta_1_5.npz`, `raw_beta_2_5.npz`, `raw_beta_1_2.npz` and
`raw_beta_3_4.npz`. Configuration, exact-recurrence evaluations, seed
information, timing and quantile diagnostics are in
`memory_check_results.json`.

The small-\(\beta\) variance convergence is slow: even at \(n=500{,}000\),
the memory window is short. At that size the leading approximation to
\(F(n)\) exceeds its exact value by 11,287.59 when \(\beta=1/5\). The
simulations illustrate the centering issue and the difference between depth
and maximum height. They do not prove a limiting law or identify the
critical or supercritical law. Finite-size and sampling errors remain.

## 9. Source comparison and remaining scope

The model, first-order height result and source question are in O. Angel,
S. Bhamidi, S. Donderwinkel, N. Maitra and A. Sakanaveeti,
*Evolution of recursive trees with limited memory*,
[arXiv:2510.18856v1](https://arxiv.org/html/2510.18856v1), submitted
21 October 2025: Section 1.1, Theorem 2.8 and Section 3.3(c).
Section 6.2 supplies the ancestry-coalescence exploration that motivates
the neighboring-label comparison; its required properties are proved
directly above. The CLTs in this note are absent from the inspected
version, and the arXiv abstract page lists only v1.

The retained Q2495 (stable ID `c8efa831871a9b89e030`) is only partially resolved: the proof covers all fixed
\(\beta<1/2\), while \(\beta=1/2\) and \(\beta>1/2\) remain. The logarithmic
loss in (19) prevents its use at the critical exponent. That failure of a
bound does not determine the critical distribution.

The separate critical-scaling question Q1893, stable ID
`1682f687494957159272`, is addressed only by the necessary radial-profile
result in `critical_profile_formatted.md`. Neither note proves GH
compactness. No empirical academic-genealogy fit was performed.


# Critical memory-tree radial profile

**Programme:** B6. **Question:** Q1893, stable statement ID
`1682f687494957159272`. **Status:** partial; the GH convergence question
remains unresolved.

The retained question asks whether, at \(\beta=1/2\), the rescaled tree
\(n^{-1/2}T_n\) converges in distribution in Gromov–Hausdorff topology to
a nondegenerate compact random metric space. The result below identifies
a necessary radial profile after additionally retaining the natural root
and uniform vertex measure. These extra structures are used only to state
the profile; they are not a modification or resolution of the bare GH
question.

Use the exact clock \(F\), depth \(D_v\), nonnegative drift \(R_v\), and
bounded clock-martingale increments from
`memory_depth_clt_formatted.md`. This is an original written argument; no
proof assistant was run.

## 1. Uniform depth control

**Theorem.** For every fixed \(0<\beta<1\),

\[
\left\|\max_{v\le n}|D_v-F(v)|\right\|_2
=O\!\left(\sqrt{F(n)\log(n+1)}+\log^2(n+1)\right).
\tag{1}
\]

All depths are in the same tree. Independence between different starting
vertices is not assumed.

**Proof.** Fix a starting vertex \(v\le n\) and let its ancestry length
be \(\tau=D_v\). On the event \(\tau>t\), the decrease of its clock
during the first \(t\) steps is at most \(F(v)\), whereas the sum of its
predictable means is at least \(t\), because the drift error is
nonnegative. Its martingale, stopped at \(t\wedge\tau\), therefore satisfies

\[
M_{t\wedge\tau}\le F(v)-t\le F(n)-t
\quad\text{on }\{\tau>t\}.
\]

If \(B\) bounds the absolute increments, Azuma–Hoeffding gives, for
\(t\ge2F(n)\),

\[
\mathbb P(D_v>t)\le\exp\!\left(-\frac{t}{8B^2}\right).
\tag{2}
\]

Take

\[
T=\min\!\left(n,
\left\lceil2F(n)+80B^2\log(n+1)\right\rceil\right).
\]

If \(T=n\), every ancestry finishes by \(T\). Otherwise, (2) and a union
bound yield

\[
\mathbb P\!\left(\max_{v\le n}D_v>T\right)\le n^{-9}.
\]

Stop each full-root martingale at \(\tau\wedge T\). A second application
of Azuma–Hoeffding, followed by a union bound over \(v\le n\), gives

\[
\mathbb P\!\left(\max_{v\le n}|M_v^{\mathrm{stopped}}|>x\right)
\le\min\!\left(1,2n\exp\!\left(-\frac{x^2}{2B^2T}\right)\right).
\]

Integrating the tail gives an \(O(T\log(n+1))\) second moment. Full and
stopped martingales are bounded in absolute value by \(Bn\), so the
exceptional event contributes at most \(O(n^2n^{-9})\).

Section 5 of the depth-CLT note gives

\[
\left\|\max_{v\le n}R_v\right\|_2=O(\log^2(n+1)).
\]

The exact identity \(D_v-F(v)=-M_v-R_v\) now proves (1). \(\square\)

## 2. The critical specialization

At \(\beta=1/2\), the exact window satisfies

\[
b_m=\frac2{\sqrt m}+O(m^{-1}),
\qquad
F(m)=4\sqrt m+O(\log(m+1)).
\]

The second estimate follows by summing the first and comparing
\(\sum_{j\le m}j^{-1/2}\) with its integral. The constants are uniform
over \(m\ge1\). Applying (1) gives

\[
\frac1{\sqrt n}\max_{1\le v\le n}
\left|D_v-4\sqrt v\right|\longrightarrow0
\quad\text{in }L^2.
\tag{3}
\]

Thus the root depths ordered by birth label, with interpolation at the
origin, have the deterministic uniform limit

\[
t\longmapsto4\sqrt t,\qquad 0\le t\le1.
\]

The uniform-vertex radial measure

\[
\nu_n=\frac1n\sum_{v=1}^n\delta_{D_v/\sqrt n}
\]

therefore converges weakly in probability to the law of \(4\sqrt U\),
where \(U\) is uniform on \([0,1]\). Its distribution function and density
are

\[
\mathbb P(4\sqrt U\le r)=\frac{r^2}{16}
\quad(0\le r\le4),
\qquad
f(r)=\frac r8
\quad(0<r<4).
\tag{4}
\]

For a direct measure argument, if \(g\) is bounded and 1-Lipschitz, then
the difference between its integral against \(\nu_n\) and against

\[
\frac1n\sum_{v=1}^n\delta_{4\sqrt{v/n}}
\]

is bounded by the maximum error in (3). The latter deterministic measures
converge by Riemann sums to (4). This proves the asserted weak convergence.

Consequently, any subsequential rooted Gromov–Hausdorff–Prokhorov limit
\((T,d,\rho,\mu)\), if such a limit exists with the inherited uniform
vertex measure, must almost surely satisfy

\[
\big(x\mapsto d(\rho,x)\big)_*\mu
=\mathcal L(4\sqrt U).
\tag{5}
\]

Its root height is \(4\). Equation (5) is a constraint on a possible
limit, not proof of tightness or uniqueness.

## 3. Remaining compactness issue

The argument controls root distances. It does not bound the number of
mutually separated branches, which is required for GH precompactness.
The youngest-vertex finite-subtree limits in Theorem 2.11 of Angel et al.
identify a genealogy of those tips. Their displayed branchpoint rates have
the form of a time change of Kingman coalescence. This does not by itself
show that finitely many late tips approximate the full historical tree in
Hausdorff distance. Branches without surviving late descendants must also
be controlled in any such proof.

No claim is made that these branches actually destroy compactness. The
full limiting metric space, tightness and uniqueness remain unresolved.
The present result is also compatible with the source's first-order
ancestor concentration; it is not an independent solution of its metric
scaling conjecture.

**Primary comparison:** O. Angel, S. Bhamidi, S. Donderwinkel, N. Maitra
and A. Sakanaveeti, *Evolution of recursive trees with limited memory*,
[arXiv:2510.18856v1](https://arxiv.org/html/2510.18856v1), Theorems 2.8 and
2.11, Proposition 6.1, Corollary 6.2, and open question 3.3(d).


# Age nulls and the advisor-graph observation protocol

These calculations address the programme's academic-genealogy motivation. They are model calculations, not empirical estimates. The attached handoff contains a description of a stored advisor graph, but not its people or edge data. No degree distribution, fitted influence ranking, cohort effect, or missing-edge rate has been inferred here.

## 1. Fix the measured quantity before fitting

Read each source relation as student -> advisor, then orient the analysis graph advisor -> student. Deduplicate identical relations for graph calculations, while reporting their original multiplicities. Retain all distinct advisors. A person with no recorded advisor is an observed root, without an assertion that the person's training history began there.

For a named seed and depth cap D, report separately:

1. Unique reachable people with shortest directed distance at most D, excluding the seed.
2. Unique people by their shortest generation.
3. The number of directed paths of each exact length 1,...,D.
4. Distinct direct students, distinct recorded advisors, and birth/death field-presence summaries.

The first statistic avoids duplicate ancestry paths. The third measures routes and can count the same person several times or at several lengths. For example, the synthetic graph A->B, A->C, B->D, C->D, D->E has four unique descendants of A within depth three but six ancestry paths. Its unique shortest-generation counts are (2,1,1), whereas its exact-length path counts are (2,2,2).

The executable reports direct-student and distinct recorded-advisor counts for each seed, presence flags for the seed's own birth and death fields, and field-completeness counts over its unique descendants within the requested depth cap, excluding the seed. It also reports global completeness over all input person records, with that denominator stated explicitly; duplicate-ID rows remain separate in this global summary until the structural audit resolves them. A field is present when its value is non-null and nonempty after trimming whitespace. Absent keys, nulls, empty strings and whitespace-only strings count as absent. Values are not parsed or validated, and death-field absence is not interpreted as either a living person or missing historical data.

Before computing genealogical statistics, test for duplicate person IDs, unknown edge endpoints, self-relations, and directed cycles. The script uses a topological sort. Its residual is explicitly labelled 'cycle or downstream residual', because that residual need not consist only of cycle vertices. Invalid endpoints, duplicate person IDs, or a cyclic graph block the descendant calculations. No edge is silently deleted to force a tree.

The handoff's person fields contain birth and death dates but do not supply doctoral-entry dates. A birth date does not determine attachment order. Analyses using a birth cohort should name it as a proxy; the exact arrival-index calculations below require the stated arrival order. Ties and missing dates need declared sensitivity analyses, not an arbitrary total ordering presented as factual.

## 2. Uniform attachment: exact age distribution

Let T_N be the uniform recursive tree: vertex 1 is the root, and vertex n+1 chooses one of 1,...,n uniformly and independently. Let S_i(N) count the subtree of vertex i, including i, with 2<=i<=N.

At time n, the subtree grows with probability S_i(n)/n. Its size and its complement therefore form a two-colour Polya urn with initial masses 1 and i-1 at time i. Direct multiplication over any sequence containing x subtree additions gives

$$\Pr(S_i(N)-1=x)=\binom{N-i}{x}
\frac{(1)^{\overline x}(i-1)^{\overline{N-i-x}}}
{i^{\overline{N-i}}},\qquad 0\le x\le N-i.$$

Here $a^{\overline j}=a(a+1)\cdots(a+j-1)$ and $a^{\overline0}=1$. The order of the additions does not affect this probability; summing over their binomially many orders proves the formula. Equivalently, S_i(N)-1 is beta-binomial with N-i trials and parameters 1,i-1. In particular,

$$\mathbb E S_i(N)=\frac Ni,\qquad
\operatorname{Var}S_i(N)=\frac{(N-i)(i-1)N}{i^2(i+1)}.$$

The expected number of descendants excluding i is N/i-1. The root has S_1(N)=N deterministically and is treated separately.

The normalized subtree proportion is a bounded urn martingale. Its limiting moments, obtained from the same formula or the urn's factorial-moment martingales, are those of Beta(1,i-1); compact support makes the moments determining. Thus S_i(N)/N converges almost surely to that beta variable. For a fixed early arrival, substantial random variation survives even after dividing by its age-based expectation. An observed departure from a mean age curve cannot by itself separate individual influence from attachment randomness.

## 3. Affine preferential attachment: another exact age null

Use the explicitly specified single-parent rule with attachment weight

$$w_n(v)=\operatorname{children}_n(v)+\theta,\qquad\theta>0.$$

For the descendant formulas in this section, take $2\le i\le N$. The root still has $S_1(N)=N$ deterministically and is excluded from the beta distributions below.

The total weight at time n is $(1+\theta)n-1$. A complete descendant subtree of size S has S-1 child edges and total weight $(1+\theta)S-1$. Put $a=(1+\theta)^{-1}$ and $r=1-a=\theta/(1+\theta)$. The chance of adding to the subtree is

$$\frac{S-a}{n-a}.$$

The resulting urn has red mass r and blue mass i-1 at time i. Hence

$$S_i(N)-1\sim\operatorname{BetaBinomial}(N-i,r,i-1),$$

$$\mathbb E S_i(N)=a+(N-a)\frac{1-a}{i-a}.$$

The fixed-i limiting proportion has Beta(r,i-1) law by the same urn argument. This rule differs from an undirected-degree-plus-delta model at the initial root and from every fixed-outdegree graph with two or more advisor edges. Its formula must not be applied to those models without deriving their corresponding weights.

Uniform attachment is recovered in the limit theta->infinity. The supplied script verifies the uniform law and the theta=1 affine law by exact enumeration through N=8, including the complete descendant probability mass functions.

## 4. Depth truncation and edge missingness have exact effects

For the uniform recursive tree, set

$$G_{i,n}(z)=\sum_{v\text{ descending from }i}z^{d(i,v)},$$

including i at depth zero. A new child of a depth-k vertex contributes $z^{k+1}$. Therefore

$$\mathbb E[G_{i,n+1}(z)\mid T_n]=(1+z/n)G_{i,n}(z),$$

and induction gives the exact generating polynomial

$$\mathbb E G_{i,N}(z)=\prod_{t=i}^{N-1}(1+z/t).$$

The expected number of descendants within D generations is the sum of coefficients of z^1 through z^D in this product. At z=1 the product telescopes to N/i, recovering the full-subtree mean. The coefficient recurrence in the script is exact rational arithmetic and works directly at D=12.

If each edge is independently recorded with a known common probability p, a true descendant at depth k remains connected to the seed with probability p^k. Linearity of expectation, without any assumption that these survival events are mutually independent, gives

$$\mathbb E G_{i,N}^{\mathrm{observed}}(z)
=\prod_{t=i}^{N-1}(1+pz/t).$$

This formula assumes a genuine tree, independent edge recording, known p, and no additional node selection. It does not describe the supplied snapshot unless these assumptions are independently justified. In a multiple-advisor DAG, several routes can preserve a connection, and replacing the reachability probability by p^k is generally wrong.

## 5. A precise identifiability obstruction

**Proposition.** Without a restriction on unobserved vertices and relations, a finite observed DAG gives no finite upper bound on a seed's true number of descendants. For two seeds incomparable under observed reachability, unrestricted missing data can reverse their descendant ranking.

**Proof.** For any positive integer M, attach M fresh, unobserved child vertices to the chosen seed and retain the original observed graph as the observation. The extended graph is still acyclic and has at least M additional true descendants. For two incomparable seeds, making M sufficiently large at either selected seed produces either ranking while leaving the observation unchanged. Ancestor-descendant pairs are excluded from the ranking assertion: in a DAG an ancestor's descendant set necessarily contains the descendant's set and the descendant itself. This proves both claims. 

This is an obstruction for an unspecified observation mechanism. It does not prevent inference under an explicit, testable missingness model. It explains why the observation contract is mathematically necessary.

## 6. Reproducible comparison design

The primary endpoint should be unique descendants within the observed generation cap, with direct students and complete untruncated simulated descendants as secondary quantities. Define ranked seeds before looking at their descendant scores. If the graph was collected by expanding ranked seeds, preserve that selection and collection rule when comparing simulated graphs.

Use three explicit layers of comparison:

- A uniform single-parent tree provides the exact age baseline above.
- An affine preferential tree and a friend tree test the additional variability produced by degree preference and local redirection. The complete-mass theorem in the report describes their asymptotic difference; it does not fit either mechanism to this dataset.
- A limited-memory tree tests a specific temporal eligibility restriction. Birth cohorts can motivate a sensitivity parameter but do not themselves identify the memory exponent or doctoral arrival order.

When retaining multiple advisors, define and simulate a DAG model with the observed number of advisors per arriving person and an explicit candidate-advisor set. Existing tree theorems then serve as comparisons, with their scope clearly limited. A primary-advisor projection can be a sensitivity analysis if the selection rule is supplied; it is not a data-cleaning step that leaves the estimand unchanged.

Estimate only parameters identified under the declared model and available observations; unknown recording parameters may require external validation or an explicit identification argument. Use declared training cohorts and evaluate descendant discrepancies on held-out cohorts or seeds. Shared descendants induce dependence between seed statistics. Simulate the entire graph in every replicate and compute all seed statistics jointly. A maximum-statistic calibration can then evaluate unusually large residuals while retaining that dependence. The usual finite-sample randomization guarantee for the Monte Carlo rank p-value $(1+\#\{T_b\ge T_{obs}\})/(B+1)$ requires the observed and simulated statistics to be exchangeable under the declared null. Separating training and evaluation data does not by itself restore that exchangeability when simulations use estimated parameters. A refitted parametric bootstrap is an approximate procedure and should be described accordingly.

Apply the observation operator to each latent simulation: date availability, edge recording, seed selection, unique-person deduplication, and the same generation cap. If that operator cannot be specified, report descriptive model comparisons conditional on the recorded graph instead of an inferential influence ranking.

## 7. Execution and supplied inputs

`genealogy_protocol.py selftest --output protocol_checks.json` ran successfully. Its declared budget is 120 seconds. The archive preserves its exact synthetic people and relations, four synthetic parent arrays (uniform, affine preferential, friend, memory), the fixed seed 20261008, all finite ranges, and the resulting audit. It enumerates every recursive parent array for sizes 2 through 8 and checks the uniform and theta=1 preferential descendant distributions exactly. It also checks the generating-polynomial profile against exhaustive counts. The five-person DAG control verifies the new seed degree counts and global/per-seed birth/death presence summaries, including an absent key, a null, empty and whitespace-only strings, and a nonempty invalid date value that correctly counts as present. The existing cyclic-input control still blocks descendant calculations.

For supplied real inputs, the command is:

```bash
python genealogy_protocol.py audit \
  --people people.tsv.gz --edges edges.tsv.gz \
  --seed QID_TO_ANALYZE --depth 12 --output observed_audit.json
```

Repeat `--seed` for each explicitly selected seed. The script deliberately does not infer a ranked-seed list, a birth order, unrecorded advisors, or a causal interpretation. Its source and all executed controls are part of the reproducibility archive.


# Primary references and coverage

- **[S1]** L. Addario-Berry, S. Briend, L. Devroye, S. Donderwinkel, C. Kerriou, G. Lugosi, *Random friend trees*, [arXiv:2403.20185v1](https://arxiv.org/html/2403.20185v1), 29 March 2024. Theorem 3.1, printed p. 5; Theorem 4.7, p. 7; Section 7, p. 31. These primary theorem statements were checked. The handoff's journal-version claim is recorded as handoff provenance; the complete journal text was not independently compared.
- **[S2]** J. Borga, E. Duchi, E. Slivken, *Almost square permutations are typically square*, [arXiv:1910.04813v2](https://arxiv.org/pdf/1910.04813v2), 8 December 2020; AIHP Probability and Statistics 57(4), 1834–1856 (2021). Section 1, pp. 1–2 defines the exact model. Borga's thesis [arXiv:2107.09699](https://arxiv.org/abs/2107.09699), Conjecture 5.1.4(e), is the handoff attribution; thesis metadata was checked, but the question page was not independently retrieved.
- **[S3]** B. Corsini, V. Dubach, V. Féray, *Binary search trees of permuton samples*, [arXiv:2403.03151v2](https://arxiv.org/html/2403.03151v2), 27 January 2025. Sections 1.2–1.3, Theorem 1.1, Remark 1, Conjecture 1, Lemmas 3.1–3.2 and 3.5, Proposition 3.3, and Proposition 5.5. The homogeneous input is the established uniform BST height law, attributed there to L. Devroye, JACM 33(3), 489–498 (1986), Theorem 5.1; its specialization in Theorem 1.1 suffices as the inspected dependency.
- **[S4]** O. Angel, C. Atamanchuk, A. Brandenberger, S. Donderwinkel, R. Khanfir, *The largest common subtree of two random trees*, [arXiv:2601.00119v1](https://arxiv.org/html/2601.00119v1), 31 December 2025. Proposition 2.6, Lemma 2.7, Proposition 4.3 and its deterministic application in Section 4.2; Section 6(i)–(iii). The uniform estimates are an existing probability theorem used as a dependency, not re-proved here.
- **[S5]** D. Aldous, *The continuum random tree III*, Annals of Probability 21 (1993), 248–289, [primary PDF](https://www.stat.berkeley.edu/~aldous/Papers/CRT3.pdf). Lemma 21 and equation (33), p. 277; Corollary 22, p. 279. The reduced-tree edge-length density supplies diffuseness of sampled common-ancestor height. Its deterministic factor-of-two coding convention does not affect that property.
- **[S6]** O. Angel, S. Bhamidi, S. Donderwinkel, N. Maitra, A. Sakanaveeti, *Evolution of recursive trees with limited memory*, [arXiv:2510.18856v1](https://arxiv.org/html/2510.18856v1), 21 October 2025. Section 1.1, Theorems 2.8–2.11, Section 3.3(c,d), Proposition 6.1, Corollary 6.2, and Section 6.2. The exact parent-window convention is retained. The current notes prove the required clock and coalescence estimates directly.
- **[S7]** T. Budzinski, D. Sénizergues, *Maximum Agreement Subtrees and Hölder homeomorphisms between Brownian trees*, Journal de l'École polytechnique — Mathématiques 11 (2024), 395–430, [primary PDF](https://numdam.org/item/10.5802/jep.256.pdf). Theorem 2, Theorem 22, and Section 5.2. The displayed Hölder interval is an existing bound; the Yule law is not replaced by the uniform labeled binary-tree law.
- **[S8]** [arXiv:2512.18937](https://arxiv.org/abs/2512.18937), independent-edge age-kernel critical-window result. Its abstract and model description were inspected only for scope comparison. Its critical scale is not claimed as a result for the fixed-outdegree or degree-dependent models in this programme.
- **[S9]** B. M. Brown, *Martingale central limit theorems*, Annals of Mathematical Statistics 42 (1971), 59–66, [DOI](https://doi.org/10.1214/aoms/1177693494); J.-C. Mourrat, *On the rate of convergence in the martingale central limit theorem*, [arXiv:1103.5050v2](https://arxiv.org/abs/1103.5050v2), Bernoulli 19(2) (2013), 633–645. The standard bounded-increment martingale CLT is applied only after its normalized conditional-variance and Lindeberg hypotheses are proved. The Mourrat primary abstract was inspected for that criterion; no formalized library theorem was compiled.

The other primary-source locations and model setups remain in the attached input. Their historical collector notes have not been silently promoted to new literature checks. The report's mathematical status concerns the exact written results above.

# Appendix A: exact retained statements and stable IDs

The wording in this appendix is extracted from the attachment without mathematical alteration. Every status below is this report's result at that exact scope. Full supplied setups and historical provenance remain in the unchanged input, while the ledger gives the active assumptions and evidence for each entry.

## Q197: Retained statement

**Programme:** B6. **Stable statement ID:** `2fb7624f5493d80f9245`. **Status:** unresolved.

**Exact retained statement:**

```text
For the DLA tree X_m after m edges, does lim_(m→∞) log(diam_(X_m)(X_m))/log m exist almost surely, and what is its value? Diameter uses internal tree distance.
```

**Model and assumptions.** DLA tree in the supplied Pfeffer/Gwynne setup; diameter is intrinsic graph/tree distance after m edges, not ambient distance.

**Result and remaining scope.** No new intrinsic-diameter exponent theorem obtained. Existence and value of the almost-sure internal diameter exponent remain.

**Changed assumptions.** None; the retained model and assumptions are preserved.

## Q198: Retained statement

**Programme:** B6. **Stable statement ID:** `c1a6ddcd43922d127073`. **Status:** unresolved.

**Exact retained statement:**

```text
Is the infinite DLA tree X_∞ almost surely one-ended: after deleting any finite-radius internal ball about its root, exactly one infinite component remains?
```

**Model and assumptions.** Infinite DLA tree in the supplied Pfeffer/Gwynne setup; one-endedness after deleting every finite-radius intrinsic root ball.

**Result and remaining scope.** No new one-endedness theorem obtained. Control of infinite components after deleting intrinsic root balls remains.

**Changed assumptions.** None; the retained model and assumptions are preserved.

## Q1288: Critical component scale in genuine attachment graphs

**Programme:** B6. **Stable statement ID:** `fe43a1729f391b7ded90`. **Status:** unresolved.

**Exact retained statement:**

```text
For δ>0, independently retain edges with probability π_c, the threshold for a positive limiting giant-component proportion. What is the asymptotic order, as n→∞, of the largest connected component?
```

**Model and assumptions.** Thesis model (d): start with two vertices joined by m parallel edges, m>=2; each new vertex adds m edges sequentially to older vertices with weights current degree+delta. Retained question has delta>0; independent edge percolation at pi_c.

**Result and remaining scope.** Neighboring independent-edge critical-window result checked and rejected as a model match. Largest-component order in the genuine degree-dependent fixed-outdegree model remains.

**Changed assumptions.** None; the retained model and assumptions are preserved.

## Q1296: Monotonicity under branching, deletion and merging

**Programme:** B6. **Stable statement ID:** `1d82caacb8c09e80ef97`. **Status:** unresolved.

**Exact retained statement:**

```text
Is P(Z_n>0 for every n) nondecreasing in p and nonincreasing in q?
```

**Model and assumptions.** p>-1, q in [0,1]. Poisson((1+p)(1-q)^k_u) children for each last-generation vertex, with k_u the current distance-three count; independently mark distance-four pairs of new vertices with probability q and merge the generated equivalence classes. Z_n is generation size.

**Result and remaining scope.** No monotonicity proof or counterexample obtained. A coupling must respect state-dependent suppression and merger equivalence classes.

**Changed assumptions.** None; the retained model and assumptions are preserved.

## Q1397: Geometry of large subcritical attachment components

**Programme:** B6. **Stable statement ID:** `c513ac78091df42c2868`. **Status:** unresolved.

**Exact retained statement:**

```text
For fixed 0<π<π_c, determine the metric scaling limits of the largest connected components, including the correct rescaling of graph distances; the cardinality normalization n^{(1−√(8π²−8π+1))/2} is already known.
```

**Model and assumptions.** Start with one vertex; each arrival chooses two independently uniform older endpoints, then independently retain each edge with probability pi. pi_c=(2-sqrt(2))/4. Fixed 0<pi<pi_c; requested object is graph-distance geometry of largest components.

**Result and remaining scope.** No metric scaling theorem obtained. Distance rescaling and metric limits of largest subcritical fixed-two-outedge components remain.

**Changed assumptions.** None; the retained model and assumptions are preserved.

## Q1398: Critical window for fixed-outdegree uniform attachment

**Programme:** B6. **Stable statement ID:** `e1dfbdf43eae91c58029`. **Status:** unresolved.

**Exact retained statement:**

```text
For π_n=π_c+b/(log n)² with fixed b∈R, determine the asymptotic scales and limiting laws of the largest component sizes in the fixed-two-outedge model.
```

**Model and assumptions.** The same fixed-two-outedge uniform attachment/percolation model as Q1397, with pi_n=pi_c+b/(log n)^2, fixed real b.

**Result and remaining scope.** Independent-edge critical-window theorem is a scope nonmatch. Critical-window component laws for the exact fixed-two-outedge model remain.

**Changed assumptions.** None; the retained model and assumptions are preserved.

## Q1884: Critical directed diameter

**Programme:** B6. **Stable statement ID:** `45d9aec35f166c99cecf`. **Status:** unresolved.

**Exact retained statement:**

```text
Is Diam(G_n)=Θ_P(n^(1/3)), meaning that Diam(G_n)/n^(1/3) and its reciprocal are tight?
```

**Model and assumptions.** iid critical directed degree pairs with E D-=E D+=E(D-D+)>0, all supplied moments through total degree 3 plus (1,3),(3,1), strongly aperiodic D--D+; condition equal totals and graphicality and sample a uniform simple digraph. Diameter is the largest finite directed distance.

**Result and remaining scope.** No new upper bound obtained. The exact tight upper bound for largest finite directed distance remains.

**Changed assumptions.** None; the retained model and assumptions are preserved.

## Q1885: Universal BST lower bound

**Programme:** B6. **Stable statement ID:** `9555ab5eed7e5e643fb2`. **Status:** partial.

**Exact retained statement:**

```text
For every μ and ε>0, is P(h(T_n)<(c_*−ε)log n)→0?
```

**Model and assumptions.** Arbitrary permuton mu (uniform marginals); sort iid mu-points by x and insert y-values into a BST; graph height and \(c_*\)>2 satisfying \(c_*\) log(2e/\(c_*\))=1.

**Result and remaining scope.** Almost-sure liminf H_n/log n >= \(c_*\) if mu has continuous positive density on any nondegenerate rectangle touching the left edge; no condition outside that rectangle. The universal arbitrary-permuton lower bound, including singular cases, remains.

**Changed assumptions.** For the partial theorem only: restrict mu to a continuous positive density on one nondegenerate left-edge rectangle; outside it mu may be singular. Convergence is strengthened to an almost-sure liminf in the nested iid coupling.

## Q1886: Almost-sure sampled BST height

**Programme:** B6. **Stable statement ID:** `bf78aed37063121c130a`. **Status:** proved.

**Exact retained statement:**

```text
Use the first n points of one infinite iid μ-sequence. If μ has bounded density, continuous and positive near {0}×[0,1], does h(T_n)/log n→c_* almost surely?
```

**Model and assumptions.** The first n points of one infinite iid permuton sequence, ordered by x and inserted by y; mu has globally bounded density, continuous and positive on a neighborhood of the entire edge {0}x[0,1].

**Result and remaining scope.** H_n/log n -> \(c_*\) almost surely in the exact nested iid planar-sample coupling under the exact retained density hypotheses. Polynomial marginal deviation bounds are also proved. No mathematical gap identified in the complete written argument; external peer review and formal verification are not claimed.

**Changed assumptions.** None; the retained model and assumptions are preserved.

## Q1887: Uniform limit with many internals

**Programme:** B6. **Stable statement ID:** `8f92afa9a2824a17445b`. **Status:** proved.

**Exact retained statement:**

```text
Whenever n,k→∞ and k/n→∞, does (n+k)⁻¹∑_{i=1}^{n+k}δ_{(i/(n+k),σ_{n,k}(i)/(n+k))} converge weakly in probability to Lebesgue measure on [0,1]²?
```

**Model and assumptions.** Uniform permutation of n+k entries with exactly n external records (an empty strict quadrant) and k internal entries; normalized permutation ranks, not arbitrary independent continuous coordinates.

**Result and remaining scope.** Normalized permutation-rank empirical measures converge weakly in probability to Lebesgue whenever k/n -> infinity. Stronger range: every n>=4, without requiring n -> infinity. No mathematical gap identified in the complete written argument. Thesis question-page numbering remains attachment provenance.

**Changed assumptions.** No narrowing: the proved theorem additionally allows fixed n>=4 while k/n tends to infinity.

## Q1888: Complete hub mass

**Programme:** B6. **Stable statement ID:** `7e728675d1726f7676ee`. **Status:** proved.

**Exact retained statement:**

```text
Is ∑_{i≥1}Z_i=1 almost surely?
```

**Model and assumptions.** T_2 is edge {1,2}; select a uniform vertex, then a uniform neighbor, and attach the new vertex to that neighbor. Z_i=lim degree(i)/n.

**Result and remaining scope.** Sum_i Z_i=1 almost surely. Also l1 limits for leaf mass, excess-degree mass, and degree mass on nonleaves; TV attachment-label convergence, a conditional TV distance-law limit, and tight typical distances. Depends on the primary polynomial nonleaf bound; no external peer review or formal verification claimed.

**Changed assumptions.** None; the retained model and assumptions are preserved.

## Q1889: Older hubs dominate

**Programme:** B6. **Stable statement ID:** `c8f5ea8c27dcbc835ad2`. **Status:** unresolved.

**Exact retained statement:**

```text
For every u<v, does Z_u stochastically dominate Z_v?
```

**Model and assumptions.** The same random-friend tree, all fixed birth labels u<v, and stochastic order of the entire limiting degree-share distributions.

**Result and remaining scope.** Exact finite-time older-degree stochastic-order comparisons pass for all sizes 2 through 8. No proof for arbitrary sizes or limiting label pairs; neighboring degrees obstruct a scalar degree induction.

**Changed assumptions.** None; the retained model and assumptions are preserved.

## Q1890: Nonleaf normalization

**Programme:** B6. **Stable statement ID:** `489730501d06b46aaf17`. **Status:** partial.

**Exact retained statement:**

```text
Do μ>0 and a nondegenerate random variable X exist with n^(−μ)N_n→X almost surely?
```

**Model and assumptions.** The same random-friend tree; N_n is the number of degree-at-least-two vertices; deterministic mu>0 and an almost-sure nondegenerate normalized limit are requested.

**Result and remaining scope.** With q_n=N_n^{-1} sum_{v:D_n(v)>=2} L_n(v)/D_n(v), log N_n-sum_{k=3}^{n-1} q_k/k has a finite real almost-sure limit. A deterministic exponent, convergence of the centered harmonic drift, and nondegeneracy remain. Positive finite power-normalized limits are equivalent to real convergence of the centered harmonic series.

**Changed assumptions.** None; the retained model and assumptions are preserved.

## Q1891: Heavy-tail common-subtree limit

**Programme:** B6. **Stable statement ID:** `24273db763cecc5254b2`. **Status:** unresolved.

**Exact retained statement:**

```text
If μ([k,∞))∼ck^(−α) and μ′([k,∞))∼c′k^(−α′), with c,c′>0 and 1<α≤α′<2, does n^(−1/α′)L_n converge in distribution to a finite positive random variable?
```

**Model and assumptions.** Independent critical nondegenerate Bienayme trees conditioned on n vertices along common admissible sizes; unlabelled unordered unrooted graph-subtree isomorphism; stated regularly varying offspring tails, 1<alpha<=alpha_prime<2.

**Result and remaining scope.** No heavy-tail common-subtree limit obtained. Large-degree decoration control and the proposed n^(1/alpha_prime) limit remain.

**Changed assumptions.** None; the retained model and assumptions are preserved.

## Q1892: Mixed-moment common subtrees

**Programme:** B6. **Stable statement ID:** `d6a1058cd1299f2c8603`. **Status:** unresolved.

**Exact retained statement:**

```text
If μ has a finite (2+κ)-moment for some κ>0 while μ′ has infinite second moment, is L_n/√n→0 in probability?
```

**Model and assumptions.** The same conditioned unlabelled unordered unrooted common-subtree model; mu has some finite (2+kappa)-moment, while mu_prime has infinite second moment.

**Result and remaining scope.** No mixed-moment vanishing theorem obtained. The finite-variance/infinite-variance comparison at scale sqrt(n) remains.

**Changed assumptions.** None; the retained model and assumptions are preserved.

## Q1893: Critical memory-tree scaling

**Programme:** B6. **Stable statement ID:** `1682f687494957159272`. **Status:** partial.

**Exact retained statement:**

```text
For β=1/2, does n^(−1/2)T_n converge in distribution in the Gromov–Hausdorff topology to a nondegenerate compact random metric space?
```

**Model and assumptions.** Root 1; independently attach vertex n+1 uniformly to {max(1,n-floor(n^beta)),...,n}; beta=1/2 and graph distance, with bare GH convergence requested.

**Result and remaining scope.** At beta=1/2, ||max_{v<=n}|D_v-4 sqrt(v)|/sqrt(n)||_2 -> 0. Uniform-vertex radial measure converges to the law of 4 sqrt(U); any rooted measured subsequential limit has this law and height 4. GH tightness/compactness, the full metric object, and uniqueness remain; root-distance control is not a covering-number bound.

**Changed assumptions.** No GH convergence asserted. A root and uniform-vertex measure are retained only for the necessary radial-profile statement.

## Q2392: Sharp cladogram branch rotation

**Programme:** B6. **Stable statement ID:** `1959a17dd98d050f8c68`. **Status:** unresolved.

**Exact retained statement:**

```text
Consider rooted unordered binary trees with n leaves labeled [n] and a root stem. Pick uniformly a nonstem edge, detach its descendant subtree, and suppress its attachment vertex, making edge e. Choose each existing edge adjacent to e with probability 1/4 and regraft at its midpoint; unused probability holds. Is inverse spectral gap O(n^(3/2))?
```

**Model and assumptions.** Rooted unordered binary cladograms with n labelled leaves and a root stem; the exact uniform-nonstem-edge detachment, adjacent-edge regraft at probability 1/4 each, and holding convention of the attachment.

**Result and remaining scope.** No sharper spectral-gap estimate obtained. The O(n^(3/2)) inverse-gap bound for the exact rotation and holding rule remains.

**Changed assumptions.** None; the retained model and assumptions are preserved.

## Q2399: Rooted common-subtree scaling law

**Programme:** B6. **Stable statement ID:** `b252bb236c6d560e7c49`. **Status:** proved.

**Exact retained statement:**

```text
Does (n^(−1/2)τ_n,n^(−1/2)τ′_n,n^(−1/2)L•(τ_n,τ′_n)) converge jointly in distribution to (2T/σ,2T′/σ′,c min{2H(T)/σ,2H(T′)/σ′}), with Gromov–Hausdorff convergence in the first two coordinates?
```

**Model and assumptions.** Independent critical nondegenerate Bienayme trees conditioned on common admissible size n; finite positive variances sigma^2,sigma_prime^2, and a finite (2+kappa)-moment for mu. Common subtrees preserve the original roots and ignore order and labels. c=E L_bullet(tau_star,tau_prime_star) for root offspring (k+1)mu(k+1) and (k+1)mu_prime(k+1). Independent normalized-excursion Brownian CRTs.

**Result and remaining scope.** L_n^bullet=c min(H(tau_n),H(tau_prime_n))+o_P(sqrt(n)), giving the exact asserted joint CRT limit and rooted GH convergence. Uses Proposition 4.3 uniform estimates from the primary source. No mathematical gap identified in the independent written reviews; no formal verification.

**Changed assumptions.** No narrowing: rooted GH convergence of the tree coordinates is proved in addition to the retained unmarked conclusion.

## Q2490 (stable ID `9b2ec4db36d8dc2b752e`): Sub-square-root Yule agreement bound

**Programme:** B6. **Stable statement ID:** `9b2ec4db36d8dc2b752e`. **Status:** unresolved.

**Exact retained statement:**

```text
Grow a Yule–Harding unrooted binary tree from one edge by repeatedly splitting a uniformly chosen leaf into a node with two new leaves; label its n leaves uniformly by [n]. For independent copies Y_n,Y′_n, does some ε>0 satisfy P(MAST(Y_n,Y′_n)≤n^(1/2−ε))→1? MAST preserves leaf labels and suppresses degree-two vertices after restriction.
```

**Model and assumptions.** Yule–Harding unrooted binary trees from the specified leaf-splitting growth, independently and uniformly labelled by [n]; MAST preserves leaf labels and suppresses degree-two vertices after restriction.

**Result and remaining scope.** Checked that the existing uniform-labelled binary-tree result does not settle the Yule–Harding law. A sub-square-root high-probability agreement bound for the exact Yule growth law remains.

**Changed assumptions.** None; the retained model and assumptions are preserved.

## Q2491 (stable ID `f82ba8d6bddd7e9322b5`): Optimal Brownian-tree Hölder exponent

**Programme:** B6. **Stable statement ID:** `f82ba8d6bddd7e9322b5`. **Status:** unresolved.

**Exact retained statement:**

```text
Let T,T′ be independent Brownian CRTs coded by normalized Brownian excursions. Determine γ_+=inf{γ≥0: almost surely no homeomorphism Ψ:T→T′ satisfies d′(Ψx,Ψy)≤C d(x,y)^γ for some finite C and all x,y}.
```

**Model and assumptions.** Independent Brownian CRTs coded by normalized excursions; one-direction gamma-Holder homeomorphism with a finite random global constant; gamma_+ as the infimum in the exact retained statement.

**Result and remaining scope.** Verified existing bounds 5-2 sqrt(6) <= gamma_+ <= 1-10^(-338); existence is for every exponent strictly below 5-2 sqrt(6). The exact optimal Holder exponent remains; these bounds are existing results, not new progress claimed here.

**Changed assumptions.** None; the retained model and assumptions are preserved.

## Q2495 (stable ID `c8efa831871a9b89e030`): Memory-tree height fluctuations

**Programme:** B6. **Stable statement ID:** `c8efa831871a9b89e030`. **Status:** partial.

**Exact retained statement:**

```text
For each fixed β∈(0,1), determine the scale and limiting distribution of H_n−E H_n, including the transition at β=1/2.
```

**Model and assumptions.** Root 1; vertex n+1 independently chooses a uniform parent in {max(1,n-floor(n^beta)),...,n}; fixed beta in (0,1), full-tree root height H_n, centered by E H_n.

**Result and remaining scope.** For every fixed 0<beta<1/2, Var H_n ~ 2 n^(1-beta)/(3(1-beta)) and the corresponding centered normal limit. The same depth theorem holds for all fixed 0<beta<1; ||H_n-D_n||_2=O(n^(beta/2) log n). Exact clock F(n) is a valid centering. Critical and supercritical height scales and distributions remain. The all-beta auxiliary theorem concerns D_n, not H_n.

**Changed assumptions.** No model change. Height theorem restricted to fixed beta in (0,1/2); the auxiliary single-vertex depth theorem covers fixed beta in (0,1).

