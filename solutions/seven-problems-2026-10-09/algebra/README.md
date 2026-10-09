# Q3101 and Q3102: completely regular semigroups

Date: 2026-10-09. The proofs received separate internal reviews by other research agents; they are not externally peer reviewed or formally verified.

| Catalog question | Result | Status and scope |
|---|---|---|
| [Q3101](../../../problems/mathematics/algebra-representation-theory-part-2.md#q3101) | [Odd-cycle obstructions](Q3101-odd-girth-obstructions.md) | Partial. Every triangle-free commuting graph of a finite band is bipartite. In the completely regular class with triangle-free commuting graph, the noncentral idempotents induce a bipartite graph; any odd cycle requires at least two nonidempotent involutions with central subgroup identities. |
| [Q3102](../../../problems/mathematics/algebra-representation-theory-part-2.md#q3102) | [No knit degree three](Q3102-no-knit-degree-three.md) | Proposed complete negative answer. Every length-three left path in a finite completely regular semigroup constructively yields a length-two left path. |

The complete source statements were verified in Paulista's arXiv:2511.10612v1, Problems 7.3–7.4, p. 28. In both questions the commuting graph omits central elements. **Q3102 is answered by a nonexistence theorem, not by a counterexample construction. Q3101 remains open for the full completely regular class.**

## Files and verification

- [Source and search log](SOURCES.md): primary-source locations, dated searches, access limitations, and prior-work comparisons.
- [Results metadata](results.json): the exact theorem scopes and recommended catalog statuses.
- [Standard-library checker](verify_semigroups.py): all table associativity checks, graph computations, and constructive proof controls.
- [Verification report](verification.json): successful checks on 13 explicit semigroups, 49,725 associativity triples, and 674 constructive collapses. Cases A, B, and C are all exercised.
- [Finite examples](finite-examples.json): labels and complete multiplication tables, with table hashes in the verification report.
- [Optional finite-model search](search_semigroups.py) and [bounded results](smt-exploration.json): exploratory Z3 queries, explicitly excluded from the premises of the universal proofs.

Run from the repository root:

```sh
python solutions/seven-problems-2026-10-09/algebra/verify_semigroups.py
```

The script regenerates the two verification JSON files deterministically and requires no third-party packages. It reconstructs attributed published examples outside the hypotheses: an 11-element nilpotent semigroup of knit degree three and a 21-element nilpotent semigroup whose commuting graph is a 5-cycle. These controls confirm why a theorem about arbitrary semigroups would be false.

Separate reviews are [Q3101](../analysis/review-Q3101.md) and [Q3102](../combinatorics/review-Q3102.md).
