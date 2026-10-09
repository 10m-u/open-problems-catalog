# Graph-constrained testing: sharp path cases and decision targets

2026-09-30. First resolution work from bridge B4.

**Result.** In noiseless vertex testing on a path with free endpoints, exact nonadaptive recovery with at most two defects requires exactly n tests. Every optimal n-test menu consists of the singleton tests. For one guaranteed defect the optimum is `ceil(n/2)` when `n≥2`, while adaptation reduces it to `ceil(log₂ n)`. If the required output is a binary decision label rather than the defect location, the nonadaptive optimum is `ceil((r−1)/2)`, where r is the number of constant-label runs along the path.

**Continuation:** [Overlapping acceptable actions](path-acceptable-actions.md) now gives an exact polynomial-time construction for arbitrary finite action overlap under either the exactly-one or at-most-one promise. It recovers the one-defect formulas below and closes the proposed overlapping-action extension in that model.

These hand results resolve explicit special cases of the thesis's graph-sensitive lower-bound direction and connect them to decision-specific sensing. They do not settle optimal testing for arbitrary graphs, dynamic graphs or noise. They are presented as deductions and checked benchmarks, with no claim of new research priority.

## Source, historical status and assumptions

Thesis: Amin Karbasi, *Graph-Based Information Processing: Scaling Laws and Applications* (2012), concluding discussion of Chapter 4, printed p. 134 (PDF leaf 150). [EPFL source](https://infoscience.epfl.ch/server/api/core/bitstreams/5f1ffc27-1d8d-49fb-a75c-fc5376f35d02/content); local text; subject page. Exact lower-bound extract: `a89c4a7fea1f6a2b1d26`. Its extractor position `13` is not the printed thesis page. The adjacent discussion asks about adaptive testing and dynamic graphs.

Historical reconciliation matters here. Karbasi and Zadimoghaddam's *Sequential Group Testing with Graph Constraints* (ITW 2012, pp. 292–296) already reports graph-sensitive lower bounds and a worst-case factor-two adaptive approximation. It uses connected walk supports. The thesis lists that paper as forthcoming, so this is same-year work, not a newly discovered later resolution of the entire conclusion. Its existence prevents treating the general adaptive direction as untouched. [Author-hosted paper](https://iid.yale.edu/files/amin-12d.pdf).

The underlying [Cheraghchi et al. graph-testing paper](https://arxiv.org/abs/1001.1445) includes different choices of walk endpoints and test designs. The present model fixes these assumptions explicitly:

- Vertices are items, and a test of pool T returns `1` exactly when `T∩D` is nonempty, where D is the defective set.
- On the path `1,…,n`, every nonempty interval `[a,b]` is admissible. Test endpoints are freely chosen; singleton intervals are allowed.
- Tests cost one, are deterministic and noiseless, and the graph is static.
- A nonadaptive menu is chosen in advance; an adaptive policy may choose the next interval from the previous results.
- The admitted defective sets are specified separately for each theorem. Zero defects is included whenever the promise says **at most**.

A path walk's visited set is an interval, and every interval can be traversed, so connected-set, simple-path and unrestricted walk-support pools coincide on this graph. Fixed monitors, compulsory terminals or inaccessible singleton tests would define another model.

## 1. A graph-sensitive masking bound

For an arbitrary finite simple graph, suppose every pool induces a connected subgraph and all sets of at most d defects are admitted. Define

`L_d = {v : degree(v) ≤ d−1}`.

**Lemma.** Every exact nonadaptive menu must contain `{v}` for every `v∈L_d`. Thus its cost is at least `|L_d|`, in addition to the usual binary-information lower bound.

**Proof.** Compare the admitted states `D=N(v)` and `D'=N(v)∪{v}`. A test distinguishes them only if it contains v and avoids all neighbors of v. A connected pool containing v and another vertex contains a path from v to that vertex; its first edge includes a neighbor of v. Hence the only distinguishing admissible pool is `{v}`. A fixed menu must contain that pool for each low-degree vertex. ∎

This gives n necessary tests whenever the maximum degree is at most `d−1`; the n singleton tests attain the bound. A bounded-degree graph can therefore force linear nonadaptive cost even though the number of sparse defect sets has logarithmic information cost for fixed d. The lemma does not establish the same n lower bound for adaptive policies: different states can lead to different purchased tests.

## 2. At most two defects on a path: exactly n tests

The masking lemma gives the whole-path conclusion when `d≥3`. Order structure gives a stronger result already for `d=2`.

**Theorem.** For `n≥1` and any promise admitting every set of at most two defects, the exact nonadaptive optimum on the path is n. If a successful menu has exactly n tests, all its tests are singletons.

**Proof.** For each `i=2,…,n`, compare `{i−1}` and `{i−1,i}`. A distinguishing interval must contain i and avoid `i−1`, so its left endpoint is exactly i. The comparison `{2}` versus `{1,2}` additionally requires `[1,1]`. Thus for `n≥2` every left endpoint `1,…,n` must occur among the tests, giving at least n tests.

Reversing the argument requires every right endpoint `1,…,n` as well: compare `{i+1}` and `{i,i+1}` for `i<n`, and compare `{n−1}` with `{n−1,n}` for the endpoint n.

If there are exactly n intervals, their left endpoints and right endpoints are each a permutation of `1,…,n`. The sums of the two endpoint lists agree. Since each interval has `right≥left`, every interval must have zero width, hence be a singleton. These n tests recover every defective set, even without a sparsity promise. For `n=1`, distinguishing the empty set from `{1}` requires its one singleton test. ∎

The important resource here is the fixed menu. A binary-splitting adaptive procedure starts by testing the whole path, then tests both halves of each positive nonsingleton interval. With at most d defects it uses at most

`1 + 2d ceil(log₂ n)`

tests: at each depth there are at most d positive intervals, and the balanced splitting tree has at most `ceil(log₂ n)` levels. For fixed `d≥2`, the gap between n nonadaptive tests and this logarithmic adaptive upper bound grows with n. This bound is sufficient to prove the gap; it is not an asserted exact adaptive optimum.

## 3. One defect: the promise changes the optimum

Let `c_i∈{0,1}^m` be the joint test signature for vertex i. A row arising from an interval has at most two transitions as i moves along the path.

| Promise | Exact nonadaptive optimum | Exact adaptive worst-case optimum |
|---|---:|---:|
| Exactly one defect, `n≥2` | `ceil(n/2)` | `ceil(log₂ n)` |
| Exactly one defect, `n=1` | 0 | 0 |
| At most one defect, `n≥1` | `ceil((n+1)/2)` | `ceil(log₂(n+1))` |

**Exactly-one lower bound.** Distinct signatures require a transition at all `n−1` internal boundaries, so `n−1≤2m`. The remaining possible equality case `n=2m+1` would use every row's two transitions. Each interval would then start after vertex 1 and end before vertex n, giving `c_1=c_n=0`, a collision. Therefore `n≤2m`.

**At-most-one lower bound.** The empty defective set has signature zero, so every vertex signature must be nonzero. Append virtual zero signatures just outside both ends. There must be a transition at all `n+1` boundaries, including both exterior boundaries, whereas every interval contributes exactly two. Hence `n+1≤2m`.

**Attainment.** For m tests, take intervals `[j,j+m−1]`, `j=1,…,m`. On the first `2m−1` vertices their signatures are the distinct nonempty prefixes of `{1,…,m}`, followed by the distinct proper nonempty suffixes. An additional vertex `2m` has the zero signature. Truncate to the required n vertices, clipping each interval to the remaining path. This attains both bounds: exactly-one recovery may use the zero signature for a vertex, while at-most-one recovery must reserve it for the empty state. The one-vertex exactly-one case needs no observations.

**Adaptive attainment.** Arrange the possible locations in path order, adding the no-defect state as an extra final position when admitted. A prefix-interval test divides the remaining ordered possibilities at a chosen threshold. Balanced binary search attains the displayed ceilings; a binary decision tree with that many possible states requires at least those depths. The no-defect state always follows the negative branch. ∎

## 4. A binary decision target: exactly `ceil((r−1)/2)` tests

Now assume exactly one defect, but return only its prescribed label `q(i)∈{0,1}`. Let r be the number of maximal constant-label runs along the path. Every vertex is still admitted, and the menu must be correct at every vertex.

**Theorem.** The optimal nonadaptive interval-menu cost is

`ceil((r−1)/2) = floor(r/2)`.

**Proof.** At every boundary between unlike labels, the adjacent vertex signatures must differ. There are `r−1` such boundaries, and an interval can split at most two, so `2m≥r−1`.

For attainment, test each run of the label occurring in fewer runs. If r is odd, choose the label opposite the common endpoint label, which occupies `(r−1)/2` runs. If r is even, either label occupies `r/2` runs. Each chosen run is an admissible interval. A positive result in any of these tests returns its label; an all-zero vector returns the other label. Exactly one defect guarantees this rule. For a constant target, `r=1`, no test is needed. ∎

For example, three long runs labelled `0,1,0` need only one test, namely the middle run, regardless of n. Full location recovery on that same path needs `ceil(n/2)` fixed tests. An alternating label at every vertex retains a linear lower bound. Decision-specific savings therefore depend on the target's geometry, rather than being automatic whenever the output is just one bit.


## Exact controls and remaining scope

```sh
python3 solutions/catalog-research/graph-testing-check.py
```

Add `--write` to regenerate [the result JSON](graph-testing-checks.json). [The standard-library checker](graph-testing-check.py) rejects every interval menu cheaper than the three claimed full-recovery optima for `n=1,…,6`, then checks attaining constructions. It computes exact adaptive one-defect costs by decision-tree dynamic programming for `n=1,…,8`. It checks all 254 binary labelings for paths through seven vertices against every cheaper menu, and the masking lemma on every simple graph through four vertices, 75 graphs in total.

The proofs establish all sizes; enumeration is an audit of their logic and constructions. The general thesis lower-bound direction receives a **partial** resolution mark and remains eligible for review. An exact arbitrary-graph optimum, constrained terminals, stochastic failures, time-varying graphs, and a tight general adaptive bound remain outside this result.
