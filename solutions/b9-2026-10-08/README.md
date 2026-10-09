# B9: games with exact strategy and balance targets

Preregistered work: definitions, decision rules and predictions were fixed before each computation. Q3188 has a written proof whose lemmas are machine-checked against an independent evaluator. Every counterexample is re-verified by a separately written checker. Not peer reviewed.

| Problem | Title | Status | Result |
|---|---|---|---|
| [Q2590](../../problems/game_theory/algorithmic-game-theory-learning-network-games.md#q2590) | Variety-seeking equilibrium existence | evidence | Every instance tested has an equilibrium; no proof. |
| [Q2591](../../problems/game_theory/algorithmic-game-theory-learning-network-games.md#q2591) | Two-vacancy variety improvement | disproved | Counterexample: a 24-move improving-response cycle on a 4-regular 9-vertex graph with exactly two vacancies. |
| [Q2598](../../problems/game_theory/foundations-zero-sum-matrix-games.md#q2598) | Four flipped-game responses | evidence | Holds for every string of length n ≤ 17 (exact computation); no proof. |
| [Q2599](../../problems/game_theory/algorithmic-game-theory-learning-network-games.md#q2599) | Weak acyclicity on trees | evidence | Every tree with at most 10 vertices tested is weakly acyclic (state cap 60k); no proof. |
| [Q2600](../../problems/game_theory/algorithmic-game-theory-learning-network-games.md#q2600) | Finite improvement on spiders | disproved | Counterexample: a 10-move improving-response cycle on a 9-vertex spider with three vacancies. |
| [Q2696](../../problems/game_theory/algorithmic-game-theory-learning-network-games.md#q2696) | Equilibrium without stubborn agents | evidence | Every instance tested has an equilibrium; no proof. |
| [Q2697](../../problems/game_theory/algorithmic-game-theory-learning-network-games.md#q2697) | Regular-graph improvement cycles | disproved | Counterexample: a 12-move improving-response cycle on the 3-cube with three vacancies. |
| [Q3188](../../problems/mathematics/combinatorics-graph-theory-part-2.md#q3188) | Two-action antagonistic and zero-sum agreement | proved | Proved for every two-move set: antagonistic play coincides with zero-sum play. |
| [Q3189](../../problems/mathematics/combinatorics-graph-theory-part-2.md#q3189) | Eventual periodicity of self-interest discrepancies | evidence | Holds in all 1,596 tested subtraction sets (h ≤ 6000); no proof. |
| [Q3259](../../problems/mathematics/combinatorics-graph-theory-part-2.md#q3259) | Monotone patterns maximize Markov waiting | evidence | Holds for k ≤ 6 (exact rational linear algebra); no proof. |
| [Q3260](../../problems/mathematics/combinatorics-graph-theory-part-2.md#q3260) | One-way overlaps favor the first pattern | evidence | Holds for k ≤ 6, with equality at one pair; no proof. |
| [Q3261](../../problems/mathematics/combinatorics-graph-theory-part-2.md#q3261) | Monotone patterns never beat nonmonotone ones | evidence | Holds for k ≤ 6, with equality at one pair; no proof. |

## Files

- [PREREGISTRATION.md](PREREGISTRATION.md)
- [PROOF-Q3188.md](PROOF-Q3188.md)
- [REPORT.md](REPORT.md)
- [graph_families.py](graph_families.py)
- [jump_atlas_6.json](jump_atlas_6.json)
- [jump_atlas_7.json](jump_atlas_7.json)
- [jump_games.py](jump_games.py)
- [jump_regular_3_10_diversity_2_cap120000.json](jump_regular_3_10_diversity_2_cap120000.json)
- [jump_regular_3_10_diversity_3_cap120000.json](jump_regular_3_10_diversity_3_cap120000.json)
- [jump_regular_3_10_variety_2_cap120000.json](jump_regular_3_10_variety_2_cap120000.json)
- [jump_regular_3_8_diversity_2_cap120000.json](jump_regular_3_8_diversity_2_cap120000.json)
- [jump_regular_3_8_diversity_3_cap120000.json](jump_regular_3_8_diversity_3_cap120000.json)
- [jump_regular_3_8_variety_2_cap120000.json](jump_regular_3_8_variety_2_cap120000.json)
- [jump_regular_4_8_diversity_2_cap120000.json](jump_regular_4_8_diversity_2_cap120000.json)
- [jump_regular_4_8_diversity_3_cap120000.json](jump_regular_4_8_diversity_3_cap120000.json)
- [jump_regular_4_8_variety_2_cap120000.json](jump_regular_4_8_variety_2_cap120000.json)
- [jump_regular_4_9_diversity_2_cap120000.json](jump_regular_4_9_diversity_2_cap120000.json)
- [jump_regular_4_9_diversity_3_cap120000.json](jump_regular_4_9_diversity_3_cap120000.json)
- [jump_regular_4_9_variety_2_cap120000.json](jump_regular_4_9_variety_2_cap120000.json)
- [jump_sweep.py](jump_sweep.py)
- [jump_trees_4_10_cap60000.json](jump_trees_4_10_cap60000.json)
- [jump_verify.py](jump_verify.py)
- [lemma9_check.py](lemma9_check.py)
- [lemma9_check_b60_H2000.json](lemma9_check_b60_H2000.json)
- [markov_penney.py](markov_penney.py)
- [markov_penney_k3.json](markov_penney_k3.json)
- [markov_penney_k4.json](markov_penney_k4.json)
- [markov_penney_k5.json](markov_penney_k5.json)
- [markov_penney_k6.json](markov_penney_k6.json)
- [penney_conway_vs_markov.json](penney_conway_vs_markov.json)
- [penney_flipped.py](penney_flipped.py)
- [penney_flipped_n10.json](penney_flipped_n10.json)
- [penney_flipped_n11.json](penney_flipped_n11.json)
- [penney_flipped_n12.json](penney_flipped_n12.json)
- [penney_flipped_n13.json](penney_flipped_n13.json)
- [penney_flipped_n14.json](penney_flipped_n14.json)
- [penney_flipped_n15.json](penney_flipped_n15.json)
- [penney_flipped_n16.json](penney_flipped_n16.json)
- [penney_flipped_n17.json](penney_flipped_n17.json)
- [penney_flipped_n18.json](penney_flipped_n18.json)
- [penney_flipped_n3.json](penney_flipped_n3.json)
- [penney_flipped_n4.json](penney_flipped_n4.json)
- [penney_flipped_n5.json](penney_flipped_n5.json)
- [penney_flipped_n6.json](penney_flipped_n6.json)
- [penney_flipped_n7.json](penney_flipped_n7.json)
- [penney_flipped_n8.json](penney_flipped_n8.json)
- [penney_flipped_n9.json](penney_flipped_n9.json)
- [penney_markov.py](penney_markov.py)
- [penney_markov_n3-10.json](penney_markov_n3-10.json)
- [q3188_proof_check.py](q3188_proof_check.py)
- [q3188_proof_check_b40_H600.json](q3188_proof_check_b40_H600.json)
- [q3188_proof_check_b70_H1500.json](q3188_proof_check_b70_H1500.json)
- [q3188_scan.json](q3188_scan.json)
- [q3188_scan.py](q3188_scan.py)
- [q3189_scan.py](q3189_scan.py)
- [q3189_scan_H6000.json](q3189_scan_H6000.json)
- [subtraction.py](subtraction.py)

