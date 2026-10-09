# Optimal path sensing with overlapping acceptable actions

2026-09-30. Continues [the graph-testing result](graph-testing.md).

**Result.** The minimum fixed interval-test count has an exact characterization for arbitrary finite overlapping acceptable action sets, with either exactly one defect or at most one defect. It is zero if a common action works in every admitted state. Otherwise it is `ceil(c*/2)`, where c* is the fewest compatible arcs partitioning a specified cyclic ordering of the states. A greedy scan over all starting positions computes c* in polynomial time and constructs an optimal menu and a valid decoder.

This closes the one-defect overlapping-action extension proposed in the first research pass. It supplies an exact algorithm for a whole structural class rather than another chosen action triangle. The broader thesis problem remains partially resolved. This is a local hand result with independent finite checks; external novelty has not been established.

## Relation to the thesis and nearest prior work

Karbasi's concluding graph-testing discussion asks for lower bounds reflecting the constraint graph and for the benefits of adaptation. Exact extract `a89c4a7fea1f6a2b1d26`, printed p. 134. [Thesis source](https://infoscience.epfl.ch/server/api/core/bitstreams/5f1ffc27-1d8d-49fb-a75c-fc5376f35d02/content). The new result concerns the nonadaptive decision problem obtained by allowing several acceptable responses to each possible defect location. Recovery of the whole defect set is one special contract.

Two close antecedents delimit what is being claimed:

- Cicalese, Damaschke and Vaccaro's 2005 interval group-testing work studies staged full recovery, including a comprehensive one-positive analysis and a bound on pool length. The institutional abstract was inspected; its full results were not audited here. Interval testing and its one-positive problem are established subjects. [Institutional record and abstract](https://research.chalmers.se/en/publication/11137).
- Javdani et al. (2014), §2 and the opening of §3, formulate **Decision Region Determination** with arbitrary overlapping regions, deterministic tests and a Bayesian expected policy cost. They develop an adaptive approximation approach. For action a, our region is `R_a={x:a∈G(x)}`. The contribution below is an exact fixed-menu solution under interval observations, rather than a new general definition of decision regions. [*Near Optimal Bayesian Active Learning for Decision Making*](https://publications.ri.cmu.edu/storage/publications/pub_files/2014/4/javdani14hec_extended.pdf).

A generic obstruction-cover formulation and an adaptive recurrence were already available from earlier work in this project. The additional claim here is exact tractability with unrestricted action overlap when the observations have this path geometry. A feasible menu below the stated bound, or a failure of the constructed decoder under the assumptions, would refute it. The bounded literature check establishes these antecedents and the model comparison, not absence of an earlier identical theorem.

## Model and the cyclic partition parameter

There are physical vertices `1,…,n`, `n≥1`. Test `[a,b]` returns one exactly when the defect lies in that interval. Endpoints are freely chosen; tests are noiseless and cost one. The menu is purchased in advance.

Each admitted state x has a nonempty set `G(x)⊆A` of acceptable actions, for a finite action alphabet A. The decoder must select one action acceptable in **every** state sharing its observed signature. Action regions may overlap arbitrarily; they need not be intervals or satisfy a pairwise-intersection rule.

For an exactly-one promise, order the states as

`1,2,…,n`.

For an at-most-one promise, the no-defect state is an additional admitted world with its own nonempty action set. Order the states as

`1,2,…,n,∅`.

Close the chosen list into a cycle. This is a fixed ordering for counting changes; optimization concerns partitions of that known ordering. Every physical interval has at most two signature transitions around this cycle. With ∅ present, its signature is always zero.

A **compatible arc** is a nonempty contiguous block in the cyclic ordering whose action sets have nonempty common intersection. A partition into compatible arcs covers every state exactly once. The one-block partition is allowed. Let c* be the smallest number of blocks in such a partition. It is always finite because singleton states are compatible.

## Exact theorem

For either promise, the optimal nonadaptive test count is

`M* = 0` if `c*=1`, and **`M* = ceil(c*/2)`** otherwise.

### Lower bound

Zero tests puts all admitted states into one observation fibre. This is feasible exactly when their action sets have a common action, equivalently `c*=1`.

Now suppose `c*≥2` and a feasible menu uses m tests. Its joint signature cannot be constant. Partition the cyclic list into maximal arcs of constant joint signature, and let their number be t. Every such arc lies within a single observation fibre, so it has a common acceptable action. Hence `c*≤t`.

Every boundary between two signature arcs changes at least one test bit. Each interval's bit changes at most twice around the circle; therefore `t≤2m`. Combining the bounds gives `m≥ceil(c*/2)`. This uses the common-action condition on whole fibres, so it remains valid for bad sets of size three or greater. ∎

### Attaining menu and decoder

Take a compatible partition with c blocks, `c≥2`. Designate one block Z to receive the all-zero signature. If ∅ is admitted, use its block; otherwise use the block containing physical vertex 1. All other blocks are ordinary physical intervals. In path order write them as `B₁,…,B_k`, where `k=c−1`.

Set `m=ceil(c/2)`. For `j=1,…,m`, test the physical interval consisting of

`B_j ∪ B_(j+1) ∪ … ∪ B_min(j+m−1,k)`.

These unions are intervals: the complement of Z is contiguous along the physical path, and the B blocks are consecutive inside it. Also `m≤k≤2m−1`, so each test is nonempty.

Z has signature zero. For block i, the set of positive tests is

- `{1,…,i}` if `i≤m`;
- `{i−m+1,…,m}` if `i>m`.

All these signatures are nonempty and distinct: prefixes differ by their endpoint, suffixes differ by their starting point, and every proper suffix omits 1 while every prefix contains 1. Thus every observed signature identifies one partition block. Select any action in that block's common intersection. This includes the possibly wrapping block Z and its no-defect state when present.

The construction uses `ceil(c/2)` tests. Choosing `c=c*` attains the lower bound. For `c*=1`, return a common action without testing. ∎

## Computing the optimum

For a fixed starting point, scan the linearized state list. Extend the current block while its running action intersection remains nonempty; cut immediately before an addition would empty it. Repeat to the end.

This greedy scan minimizes the number of compatible blocks for that starting point. Let g be the end of its first maximal prefix, and suppose g lies in block j of another feasible partition. Replace that partition's first j blocks by the greedy prefix and, if g falls before block j's end, the remaining suffix of block j. The suffix is compatible because it is a subset of a compatible block. If `j=1`, maximality forces g to equal that block's end, so one block replaces one. If `j≥2`, at most two blocks replace at least two. All later blocks stay unchanged. Thus an optimal partition can begin with the greedy choice; induction applies to the remaining suffix.

Run this scan from every cyclic starting point and retain the fewest blocks. Any cyclic partition has a boundary at one of these starts, so its linearization is considered. Conversely, every scanned partition is a valid cyclic partition. The minimum is therefore c*.

There are N starts and N states per scan, where `N=n` or `n+1`. With bitset action intersections this gives a straightforward `O(N²|A|)` bit-operation bound, followed by the explicit menu construction. The input consists of the acceptable action sets; the algorithm does not need a list of minimal bad sets.

## Examples and recovered cases

A small action triangle has

| State | Acceptable actions |
|---|---|
| 1 | `{a,b}` |
| 2 | `{b,c}` |
| 3 | `{a,c}` |

Every pair has a common action, but all three do not. The compatible partition `({1,2},{3})` gives `c*=2` and one test: `[3,3]`. A negative result permits b; a positive result permits a. Checking only bad pairs would incorrectly permit zero tests. Preselecting distinct labels a, b and c would instead impose a stronger contract costing two tests. The theorem optimizes the acceptable actions jointly with the menu.

The prior formulas now follow as special cases:

- Unique actions for all n defect locations give `c*=n`, hence `ceil(n/2)` for `n≥2`; the one-state case needs zero tests.
- Unique actions for n defect locations and ∅ give `c*=n+1`, hence `ceil((n+1)/2)`.
- For a nonconstant binary target with r linear runs, `c*=r` when the endpoints differ and `c*=r−1` when they agree. Binary runs alternate, giving `ceil(c*/2)=floor(r/2)`.

The no-defect action is substantive. If all physical vertices permit only a, exactly-one sensing costs zero. Adding ∅ with sole acceptable action b raises the cost to one: test the whole path and choose a on a positive result, b on a negative result.

## Boundary of the result

The cyclic block count determines this **fixed-menu cost**, but does not determine adaptive cost. On six vertices, unique location labels and alternating binary labels both have `c*=6` and fixed optimum three. Unique location recovery has adaptive optimum three. The alternating binary target has adaptive optimum two: first test `[2,4]`; on a positive result test `[3,3]`, and on a negative result test `[6,6]`. Return the prescribed alternating label. One test is impossible by the fixed-menu lower bound. Thus the adaptive question needs additional information about the action pattern.

The one-defect assumption is equally necessary. With at most two defects on three vertices, seven possible worlds have unique recovery actions. Any cyclic singleton-action partition would have seven blocks and incorrectly predict four tests. The three physical singleton tests recover all seven worlds. Pool signatures over defective **subsets** no longer have two transitions in the state ordering used by this theorem.

Weighted acquisition costs, restricted endpoints, pool-length limits, noise and arbitrary constraint graphs require their own optimization. This note establishes neither their optimal costs nor an empirical plant-measurement result. The general Karbasi extract retains a partial mark.

## Tools and independent controls

[The solver](path_action_sensing.py) returns an optimal menu, compatible partition, observation fibres and decoder. With no argument it solves the action triangle:

```sh
python3 solutions/catalog-research/path_action_sensing.py
```

For a new finite contract, pass a JSON file containing `acceptable_actions`, a list of nonempty lists of action names in vertex order. Include `empty_actions` to admit ∅. For example:

```json
{"acceptable_actions": [["a","b"],["b","c"],["a","c"]]}
```

Reproduce the independent audit with:

```sh
python3 solutions/catalog-research/path_action_sensing_checks.py
```

Add `--write` to regenerate [the result JSON](path-action-sensing-checks.json). The checker compares the solver with all interval menus up to an independently verified full-recovery bound and with all cyclic cut sets. It checks all 39,207 nonempty three-action assignments through five total states for both promises, plus 1,800 seeded assignments through seven physical vertices, with three, four or six actions. It independently reconstructs every observation fibre and checks the returned action. The triangle, no-defect distinction and adaptive-cost boundary also pass.

These controls audit the algorithm without reusing its greedy partition logic. The hand proof establishes all finite sizes; this is not proof-assistant verification or an external priority determination.
