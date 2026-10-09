# Interval constraints, ultra-log-concavity, and the Q164 gap

7 October 2026. This is a reconstruction and continuation from the supplied intermediate messages, not a recovery of their missing files. The original report and its statement ledger remain unchanged. No literature-priority claim is made.

The main new recoverable result is **arbitrary nonnegative weighted ultra-log-concavity for every binary linear interval-constraint family on at most nine variables**. Its proof combines an exact exhaustive lemma for all symmetric interval families in dimensions 2, 4, 6, 8 with the published conditional-antipodal-pairs theorem. In arbitrary dimension it proves the four inequalities nearest each endpoint. A separate all-dimensional result covers laminar interval systems. None of these results closes Q164 for all powers of all paths and cycles.

## Definitions and source boundary

Let `m>=0`, and let F be the binary words `x=(x_1,...,x_m)` satisfying any finite collection of integer interval bounds

\[
L_{ab}\le\sum_{i=a+1}^{b}x_i\le U_{ab},\qquad 0\le a<b\le m.
\]

Either bound may be omitted. For arbitrary real weights `w_i>=0`, define

\[
f_k(w)=\sum_{x\in F,\ |x|=k}\prod_iw_i^{x_i}.
\]

ULC means log-concavity after division by `binom(m,k)`, with no internal zeros. In exact integer form the required inequalities are

\[
k(m-k)f_k^2\ge(k+1)(m-k+1)f_{k-1}f_{k+1},\quad1\le k<m.
\tag{1}
\]

This is numerical nonnegativity for every fixed weight vector. Even for unrestricted two-variable words, its central defect is `(w_1-w_2)^2`; the coefficient of `w_1*w_2` is negative. Thus this work does **not** assert coefficientwise ULC.

The [initial report](../../b3-2026-10-06/report-extracted.txt), PDF pp. 14–17, already proves ordinary weighted log-concavity by Ahlswede–Daykin. Its application to forbidden unit-part runs closes the submitted Q166 statement, while path-power domination receives only ordinary LC there. Q164 requires ULC of order the number of graph vertices and includes cycles. Exact source definitions are in the root handoff, §3.1; the initial statement ledger is [here](../../b3-2026-10-06/B3_statement_ledger.json).

## Published theorem used

[Kahn–Neiman, *A strong log-concavity property for measures on Boolean algebras*, arXiv:0907.0243](https://arxiv.org/pdf/0907.0243), defines antipodal averages and conditional APP on PDF pp. 1–2. Theorem 1, PDF p. 2, says CAPP implies ULC provided the rank sequence has no internal zeros. Theorem 9, PDF p. 4, gives endpoint inequalities when APP is known only for conditionings leaving `2q` coordinates, `q<=t`. Theorem 4, PDF p. 3, states preservation of ULC under convolution. These are quoted as dependencies, not new theorems here.

Only coordinate **conditioning** is used in the reduction: fix selected coordinates to zero or one, and retain the others in their original order. Projection, which sums over coordinates, is a different operation and is not assumed to preserve the interval description. External fields here mean multiplicative position weights.

## No internal zeros: an elementary proof

For positive weights it suffices to show that the unweighted attainable ranks are consecutive. Write prefix heights `h_0=0`, `h_j=sum_{i<=j}x_i`. Every restriction, including `x_i in {0,1}`, is a difference inequality `h_b-h_a<=c` with an integer `c`; the opposite bound is another such inequality. If two feasible height vectors have ranks `p<r`, take a convex combination whose final height is any chosen integer `k in [p,r]`. It satisfies all the real difference inequalities. Coordinatewise floor preserves every integer difference bound:

`v_b<=v_a+c` implies `floor(v_b)<=floor(v_a)+c`.

The floored initial and final heights remain `0` and `k`. Adjacent differences remain zero or one, so the floored vector is a feasible binary word of rank `k`. Hence there are no internal zeros. This argument also applies after arbitrary coordinate conditioning: each original interval meets the remaining ordered coordinates in an interval, and its bounds change by the number of fixed ones. If some weights are zero, fix those coordinates to zero, apply the same support argument, and take a limit of positive weights in (1). Empty families satisfy all inequalities trivially.

## Exact central reduction and its quantifiers

Condition an interval-family measure on any outside coordinate values, leaving `2q` ordered coordinates. In an original interval let `r` be the number of fixed ones and `s` the number of remaining coordinates. Put `L'=L-r` and `U'=U-r`. A remaining word and its complement both satisfy that interval precisely when

\[
L'\le a\le U',\qquad L'\le s-a\le U',
\]

where `a` is its remaining interval sum. Equivalently,

\[
|2a-s|\le B,\qquad B=\min(2U'-s,\ s-2L').
\tag{2}
\]

Missing bounds may be replaced by the trivial binary bounds before forming (2). If `B<0` the antipodal family is empty. Otherwise `B` has the same parity as `s`; bounds `B>=s` are vacuous. For `s=0` the condition is either vacuous or impossible. Every nonempty reduced restriction is therefore a symmetric band on a **linear** interval of the remaining ordered coordinates.

Let H be any family of binary words on `2q` coordinates satisfying arbitrary symmetric bands `|2 sum_I x_i-|I||<=B_I`. Write `c_j=#{x in H: |x|=j}`. The sufficient central inequality is

\[
q c_q\ge(q+1)c_{q-1}.
\tag{3}
\]

For positive position weights the product of the weight of `x` and of its complement is the constant `prod_i w_i`, independent of `x`. Normalizing the conditioned measure supplies another constant. Its antipodal averages are consequently proportional to `c_j/binom(2q,j)`. Because `binom(2q,q)/binom(2q,q-1)=(q+1)/q`, (3) is exactly APP, with the correct single binomial factor. It is not the squared factor from a coefficientwise version of (1).

Thus (3) for every `q` would give CAPP and arbitrary weighted ULC for all linear interval families. This general central inequality remains a new research question here; we do not infer it from ordinary LC.

## Exhaustive central lemma for `q<=4`

The adjacent [checks.py](checks.py) enumerates every possible intersection of all nonvacuous symmetric interval-band predicates. A family on `n` positions is represented by a `2^n`-bit exact integer, one bit per binary word. For every interval of length `s`, the possible nonempty bandwidths are `s mod 2, s mod 2+2,...,s-2`; larger bounds impose no condition. All negative bandwidths give the separately handled empty family. Duplicate predicates are removed without altering possible intersections.

Start with the full Boolean cube. For each predicate G, replace the stored set of families S by `S union {F intersection G: F in S}`. Induction on the processed predicates proves that the final set contains **exactly all distinct interval-band families**. The checker tests (3) for each resulting family, using exact bit counts. This is complete finite certification over arbitrary collections of constraints, rather than testing a list of path powers or random weights.

| Dimension `2q` | Distinct nonvacuous predicates | Distinct nonempty families | Negative central defects |
|---|---:|---:|---:|
| 2 | 1 | 2 | 0 |
| 4 | 7 | 16 | 0 |
| 6 | 22 | 377 | 0 |
| 8 | 50 | 32,554 | 0 |

The [machine certificate](checks.json) includes canonical family-set SHA-256 digests, equality counts, and the script hash. Running `python3 checks.py` recreates it without dependencies. The completeness argument above supplies the finite quantifier; the integer program supplies the finite calculation. This is a computer-assisted lemma, subject to independent audit of the code and reduction, not a paper-only all-dimensional proof.

**Consequences.** Every linear interval family on `m<=9` variables has CAPP, because every even conditioning leaves at most eight coordinates. By the support proof and Kahn–Neiman Theorem 1, its weighted rank sequence is ULC of order `m`, for all nonnegative weights. For arbitrary `m`, their Theorem 9 with `t=4` proves (1) at every index `k` in `{1,2,3,4} union {m-4,m-3,m-2,m-1}`, restricted to `1<=k<m`. These are the first and last six-term rank segments, not merely a finite-graph screen.

In particular these conclusions apply to dominating sets of `P_m^ell`, every `ell>=1`, since every closed neighborhood is an interval. The program additionally checks 72 exact weighted path-power examples through `m=9`; those are implementation controls, not the basis of the universal finite-dimensional conclusion. The complete cycle target is not covered by this linear conditioning argument.

## A stronger matching claim is false

A tempting route to (3) is to match a lower-rank feasible word to a central-rank feasible superset by adding one 1. That premise already fails in dimension six. Impose

\[
x_1+x_2=x_2+x_3=x_4+x_5=x_5+x_6=1.
\]

Each block of three positions must be `010` or `101`. The feasible words are

`010010, 010101, 101010, 101101`,

with ranks `2,3,3,4`. The unique rank-two word has no feasible rank-three superset: changing any single zero violates one of the adjacent pair equations. The inclusion graph between those ranks has no edges, so even an ordinary inclusion injection is impossible. Nonetheless (3) holds: `3*2>=4*1`. The exact word/mask witness and complete edge list are regenerated in checks.json.

This is a counterexample to the precisely stated one-bit inclusion-matching route, not to (3) or ULC. The original stalled work's actual proposed matching definition was not supplied, so no historical identity of the obstructions is asserted. Prefix-height transformations can change multiple bits and are not refuted by this witness.

## An all-dimensional tractable class: laminar constraints

If all constrained intervals form a laminar family—each pair is disjoint or one contains the other—then the weighted rank sequence is ULC for **every** number of variables.

Proof: add a root containing all variables and singleton leaves. At a node, multiply the generating polynomials of its disjoint child blocks and unconstrained singleton positions; then remove coefficients whose ranks fall outside that node's integer bounds. A singleton weighted sequence `(1,w)` is ULC of order one. Multiplication convolves rank sequences, so the published convolution theorem preserves ULC with order the sum of the child-block sizes. Restricting to a consecutive allowed rank interval preserves every ULC inequality: an interior inequality is unchanged, while at a truncation boundary an adjacent term is zero. The support remains consecutive, including the empty case. Induction from leaves to root proves the claim, with limits for zero weights. Intersecting multiple bounds on one interval just tightens its allowed rank interval.

The laminar theorem is a straightforward consequence of established closure results; novelty is unclaimed. Typical successive path neighborhoods overlap without containment, so it does not close general Q164. It identifies crossing intervals as the genuine obstruction to this simple recursive proof.

## Research questions retained separately

The adjacent [conjectures.json](conjectures.json) records exact quantifiers and evidence for:

1. Central symmetric linear-interval inequality (3), for every `q>=1` and arbitrary integer bands. Verified completely only through `q=4`; a structural proof would yield arbitrary weighted ULC for all linear interval families.
2. The exact catalog Q164 for every path/cycle size and power. Path ordinary LC comes from the initial report; new weighted path ULC is certified for sizes at most nine and for the stated endpoint inequalities in every size. Cycles require separate reasoning.

A useful next structural target is central APP for *crossing* intervals, since laminar systems are already handled. The failed one-bit matching suggests looking for nonlocal exchanges on prefix-height vectors or a weighted reflection/injection argument that retains the normalization in (3). Extending the exhaustive dimension alone should not substitute for that proof.
