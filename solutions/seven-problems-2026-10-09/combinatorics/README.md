# Proper total domination: Q256 and Q257

This packet addresses two open, nonprovisional catalog entries with no earlier repository result at the start of the round. It uses the source's open-neighborhood definition throughout.

| Problem | Result | Status |
|---|---|---|
| [Q256](Q0256-caterpillars.md) | A necessary and sufficient 16-state characterization of caterpillar leaf words; minimum proper total dominating sets in linear time from the spine representation. Pendant multiplicities truncate at 3, sharply; neighbor sums truncate at 4, sharply. | Proposed complete algorithmic characterization. |
| [Q257](Q0257-tree-pairs.md) | Every tree pair satisfies a+1≤b≤6a−4 and has a representative of order at most 6a−4. Complete slices: a=2 gives b∈{3,5}; a=3 gives b∈{6,7}. | Partial. The full classification for a≥4 remains open. |

These are written mathematical arguments with exact finite controls. They are not peer reviewed, and the bounded literature search does not establish historical novelty. The [source and search log](SEARCH-LOG.md) records the direct-access limitations for the thesis and primary publisher pages and identifies the accessible authoritative statements used instead.

## Files

- [Q0256-caterpillars.md](Q0256-caterpillars.md): two theorems, sharpness examples, full transition rule, minimization, and scope.
- [Q0257-tree-pairs.md](Q0257-tree-pairs.md): strict inequality, complete small slices, core bound, simultaneous leaf reduction, and finite representative theorem.
- [caterpillar.py](caterpillar.py): dependency-free recognition and minimum-witness implementation.
- [verify.py](verify.py): independent exact subset controls.
- [tree_enumeration.py](tree_enumeration.py): exhaustive unlabeled-tree generation and direct subset minimization used by the verifier.
- [verification.json](verification.json): machine-readable finite results and explicit representatives of observed pairs.
- [results.json](results.json): integration metadata.

## Reproduce the finite controls

From the repository root, run:

```sh
python solutions/seven-problems-2026-10-09/combinatorics/verify.py
```

No third-party dependencies are required. The checked default scope is every unlabeled tree of orders 2 through 13, plus separately generated short caterpillar leaf words. The verification took seconds in the research environment; no timing guarantee is made.

The saved run checked:

| Check | Count or result |
|---|---:|
| Unlabeled trees, orders 2–13 | 2,287 |
| Trees with a proper total set | 1,333 |
| Caterpillars compared against exact subset enumeration | 1,086 |
| Nontrivial general leaf reductions compared exactly | 388 |
| Additional short leaf words with capacities up to 5 | 554 |
| Large input represented by 200 spine counts | 20,020,100 vertices; optimum 302 |
| Sharpness of selected-leaf cap 3 and neighbor-sum cap 4 | Passed |

The large-input check compares the original and capped spine representations; it does not materialize or exhaust 20 million vertices. All finite comparisons passed. They supplement, rather than replace, the arbitrary-order proofs.

### Why the finite tree enumeration is complete

A rooted tree is determined by the multiset of rooted trees attached to its root. The generator builds every multiset of previously generated smaller rooted trees whose orders sum to n−1. Induction on n therefore generates every rooted tree of order n, with one canonical multiset encoding for each rooted isomorphism class. It converts each rooted shape to an adjacency list, repeatedly deletes outer layers to locate the one or two centers, and uses the lexicographically smaller recursively sorted rooted code at a center as the unrooted canonical form. Two trees have the same such code exactly when they are isomorphic. Deduplicating these forms gives all unrooted trees in the stated finite range.

The direct parameter checker first forces the neighbor of every leaf into the candidate set, a necessary condition for total domination, then enumerates every remaining membership choice. It computes all neighbor sums using adjacency bit masks. It minimizes cardinality separately for total domination and for positive unequal adjacent sums. It shares neither the finite-state recurrence nor its local predicate with the caterpillar implementation.

To inspect an individual caterpillar, supply the numbers of leaves along its non-leaf spine:

```sh
python solutions/seven-problems-2026-10-09/combinatorics/caterpillar.py 1 1 2 1
```

This returns a minimum witness of size 9. A one-vertex spine requires at least two leaves; a longer spine requires a positive count at each endpoint. Labels 0 through k−1 are the spine, followed by consecutive blocks of pendant leaves in spine order.

## Interpretation of finite pair records

The saved `observed_pairs` entries are existence certificates within the tested order bound. A pair absent from them may occur at larger order. Only the a=2 and a=3 slices are proved complete here, by structural arguments independent of the finite search. The general reduction gives a finite search bound of 6a−4 but this packet does not exhaust that bound for all a.
