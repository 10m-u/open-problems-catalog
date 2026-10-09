# B9 local work, 8 October 2026: results

This round worked the B9 group (games with exact strategy and balance targets) locally. Everything below follows
[PREREGISTRATION.md](PREREGISTRATION.md). Its definitions and predictions were fixed before the
runs, and its sections were appended in order: Problems 1–3, the Q2598 method note, then
Problem 4. Every script and JSON output named here is in this folder.

## Summary

| Question | Result | Standing |
|---|---|---|
| Q3188 (Conj. 15, two-move AvA = zero-sum) | **Proved** for all S = {a < b} and all h | Written proof, [PROOF-Q3188.md](PROOF-Q3188.md); every lemma machine-checked to b ≤ 70 |
| Q3189 (period 2 max S of discrepancies) | Holds in every tested case | Evidence: 1,596 sets, h ≤ 6000 |
| Q2598 (flipped Penney best responses) | Holds for every A with n ≤ 17; n = 18 still running | Evidence: exact; Conway and Markov chain agree for n ≤ 10 |
| Q3259–3261 (Markov Penney on S_k) | All three hold for k ≤ 6; both race bounds are tight at exactly 1/2 | Evidence: exact rational linear algebra |
| Q2600 (spiders: every improving sequence finite?) | **No**: an improving cycle on a 9-vertex spider with 3 vacancies | Certificate, checked by an independent verifier and by hand |
| Q2697 (regular, 2–3 vacancies: every improving sequence finite?) | **No**: a 12-move improving cycle on the 3-cube with 3 vacancies | Certificate, checked by an independent verifier and by hand |
| Q2591 (variety, two vacancies: always potential?) | **No**: a 24-move improving cycle on a 4-regular 9-vertex graph with exactly 2 vacancies | Certificate, checked by an independent verifier and by hand; no cycle exists on any connected graph with N ≤ 7 |
| Q2599 (trees weakly acyclic?) | No counterexample, trees with N ≤ 10 | Evidence, capped at 60k states per instance |
| Q2590, Q2696 (equilibrium always exists?) | Every tested instance has an equilibrium | Evidence |
| *Side finding:* source Lemma 9 of arXiv:2510.24280 | **False as stated**, first at S = {4, 7}, h = 34 | Two implementations plus a hand computation; the paper's main Theorem 3 still holds numerically |

Preregistered predictions against outcomes:
- Q3188 holds: 0.75 → proved.
- Q3189: 0.6 (|S| = 2) and 0.5 (|S| = 3) → held throughout.
- Q2598 to n ≤ 18: 0.7 → holding so far.
- Q3259–3261: 0.7, 0.6, 0.6 → held.
- Spider improving cycle found: 0.2 → found.
- Regular-graph cycle with 2–3 vacancies found: 0.3 → found.
- Variety cycle with two vacancies among N ≤ 7: 0.25 → none at N ≤ 7, but one on a 4-regular graph with N = 9.
- Tree that is not weakly acyclic: 0.15 → none.
- Equilibria always exist: 0.9 → held.

## Problem 1: self-interest cumulative subtraction games (arXiv:2510.24280v2)

**Implementation check.** `subtraction.py` implements Definition 2 exactly. It reproduces:
- Table 1 (S = {3, 5}, h ≤ 15);
- the Table 3 values at h = 61 for S = {4, 5, 9}, in both the FvF and AvF rows;
- the Table 2 values at h = 28 and h = 36 for S = {3, 8, 11, 13}.

So the profile conventions, including the asymmetric FvA and AvF, match the source.

**Q3188: proved.** [PROOF-Q3188.md](PROOF-Q3188.md) shows that AvA play is a best response to
a greedy opponent: o¹_AvA = G, where G is the most the mover can collect against an opponent
who always removes the larger amount, and o²_AvA(h) = o¹_AvA(h − b) for h ≥ b. Then

  G(2bN + ρ) = bN + ρ − min_{i ≤ N, ρ+iΔ < 2b} θ(ρ + iΔ),

where Δ = b − a and θ(e) = e − G(e) on [0, 2b). The core is one lemma: AvA's two options are
never strictly better for both players at once. That lemma is what makes AvA's choice
zero-sum optimal.

Support for the proof:
- The preregistered scan, `q3188_scan.py`, found 0 mismatches over b ≤ 60 and h ≤ 4000.
- `q3188_proof_check.py` checks every lemma against a separately written game-tree evaluator:
  0 failures for b ≤ 70, h ≤ 1500.
- A mutation test, swapping in friendly tie-breaking, is caught at once.

Three-move sets do break the identity. The exploratory scan found 18 sets with max S ≤ 30, the
first being S = {6, 13, 17} at h = 76. That is consistent with the source's Conjecture 16
region and with the proof's reliance on h + Δ − b = h − a.

**Q3189: evidence.** `q3189_scan.py` covered every S = {a < b} with b ≤ 40 (780 sets) and every
|S| = 3 with max S ≤ 18 (816 sets), with h ≤ 6000. For every pair of profiles and both
coordinates, D(h + 2 max S) = D(h) throughout the final third. In detail:
- 636 sets have a nonzero discrepancy somewhere.
- The largest |D| is 12, at S = {25, 38} (FvF − FvA, first coordinate).
- The latest periodicity onset is h = 2844, at S = {37, 40}.

Output: `q3189_scan_H6000.json`. This is not a proof. Lemma 4 of PROOF-Q3188 gives the
eventual 2b-periodicity of z and of the AvA outcome, but not of the friendly profiles.

**Side finding: the source's Lemma 9 is false as stated.** Lemma 9 claims that a unilateral
friendly deviation from AvA leaves the deviator's payoff unchanged: o¹_AvA = o¹_FvA and
o²_AvA = o²_AvF.

At S = {4, 7}, h = 34, AvA gives (18, 14) and AvF gives (19, 15). Bob, the deviator, gains 1.
This was checked by hand down the chain 34 → {30, 27} → 26 → 19 → {15, 12} and by the
separate tree evaluator.

Over b ≤ 60 and h ≤ 2000 (`lemma9_check.py`, `lemma9_check_b60_H2000.json`):
- 351 of 1,770 pairs violate the equalities, all with b < 2a.
- The deviator strictly gains at 241,796 heaps.
- The weakened lemma, with each "=" replaced by "≤", never fails.
- The paper's Theorem 3 (FvF ≥ AvA coordinatewise) never fails.

So the main theorem looks true. Its printed proof combines Lemmas 8 and 9, and would go through
with the weakened Lemma 9, but that weakened lemma still needs a proof. Worth telling the
authors.

## Problem 2: Q2598, flipped Penney-Ante (Phillips–Hildebrand, Conjecture 7.3)

In the flipped game II wins when A appears first, so II maximizes P(A before B) over B ≠ A.

**Implementation check.** `penney_flipped.py` uses Conway's formula with integer
cross-multiplication. It reproduces the source's Table 8 rows, including the tie
{THTTH, THTTT} against HTHTT. The bound in the preregistration's method note almost never
separates, so nearly every A got an exhaustive scan over all B.

**Results.**
- n = 3–17: no counterexample. Every optimal response lies in {Hⁿ, Tⁿ, a₂⋯aₙH, a₂⋯aₙT}.
  Outputs: `penney_flipped_n*.json`.
- Optimal sets have size 1 or 2.
- In the n = 16 tallies, II's response is Hⁿ or Tⁿ in about 59% of the A strings and a
  one-symbol shift a₂⋯aₙX otherwise. The two shifts tie in about 11%.
- n = 17 finished after the pause (`penney_flipped_n17.json`, 65,536 strings, no counterexample).
  n = 18 is still running and writes `penney_flipped_n18.json` on completion.

**Independent check.** `penney_markov.py` solves the absorbing Markov chain on prefix states by
fraction-free elimination, for every A (first symbol H) and every B, n ≤ 10. Its optimal sets
and values match Conway's exactly for all 1,020 strings A (`penney_conway_vs_markov.json`).

## Problem 3: Q3259–3261, Markov Penney races on S_k (Lin 2024, Ch. 2)

**Method.** `markov_penney.py` computes the exact fundamental matrix Z = (I − P + Π)⁻¹ with
python-flint. The chain is doubly stochastic, so π is uniform. Then E_π[T_σ] = k!·Z_σσ − 1, and
the race probabilities come from mean first-passage times.

**Independent check.** Direct absorbing-chain solves gave exact agreement:
- every hitting time for k ≤ 4, and sampled hitting times for k = 5–6;
- 80 race pairs per k, including one-way and monotone pairs.

**Results.**

| k | E[T_{12…k}] = max E[T_σ] | Q3260 one-way pairs (min Pr) | Q3261 pairs (max Pr) |
|---|---|---|---|
| 3 | 23/4 | 8 (1/2) | 8 (1/2) |
| 4 | 3943/140 | 82 (1/2) | 44 (1/2) |
| 5 | 3558967/24440 | 586 (1/2) | 236 (1/2) |
| 6 | ≈ 859.3 (exact fraction in `markov_penney_k6.json`) | 4,302 (1/2) | 1,436 (1/2) |

- **Q3259.** E[T_σ] is maximal exactly at 12…k and k…1.
- **Q3260 and Q3261.** Both hold with equality at the same pair, σ = 12…k against
  τ = 12…(k−2)k(k−1). Any proof has to handle this tight pair.

## Problem 4: jump games (Q2590, Q2591, Q2599, Q2600, Q2696, Q2697)

**Method.**
- `jump_games.py` builds the full improving-move digraph on type-configurations. Same-type
  agents are interchangeable, which preserves cycles and sinks.
- Improving cycles are strongly connected components with at least two states.
- Equilibria are sinks.
- Weak acyclicity means every bottom component is a single sink.
- Every flagged certificate is re-verified by `jump_verify.py`. That file is written
  separately and uses Fractions; a mutation test showed it rejects corrupted cycles.

Graph families:
- all connected graphs with N ≤ 7 (994 graphs);
- all trees with N ≤ 10;
- all connected cubic graphs on 8 and 10 vertices and quartic graphs on 8 and 9. These are
  generated by sampling with isomorphism dedupe until the counts match OEIS A002851 and
  A006820.

**Positive control.** The engine rediscovers a variety-seeking improving cycle on a cubic
10-vertex graph with 3 vacancies: 6 moves, types (3, 2, 2). The source's Theorem 3.1 has this
shape.

**Q2600: disproved.** The source proves spiders are potential with one vacancy and conjectures
the same for any number. Counterexample:
- **Spider:** center 1 of degree 4, legs 1–0–2–3, 1–4–5–6, 1–7 and 1–8.
- **Agents:** 3 red and 3 blue on 9 vertices, with 3 vacancies.
- **Cycle:** 10 moves, starting from configuration [0,2,0,0,1,1,2,1,2] (vertex 0..8; 0 = empty,
  1 = red, 2 = blue).
- **First moves:** 5→0 (utility 1/2 → 1), 1→2 (3/4 → 1), 4→1 (0 → 1/3).

The trees sweep found 8 spider instances in all: 5 with 3 vacancies and 3 with 4, the smallest
on 9 vertices. Certificates are in `jump_trees_4_10_cap60000.json`.

**Q2697: disproved.** On the 3-cube Q₃ (cubic, 8 vertices) with 2 red, 2 blue and 1 green
agent and 3 vacancies there is a 12-move improving cycle:
- **Start:** [1,0,0,1,3,2,2,0].
- **First moves:** 0→7 (0 → 1/2), 5→0 (2/3 → 1), 6→2 (0 → 1/2).
- **Certificate:** `jump_regular_3_8_diversity_3_cap120000.json`.

This also settles part of the source's open question. It asked whether the game is potential
on 3-regular graphs, and on 4-regular graphs with 2 or 3 vacancies. For 3-regular graphs it is
not.

What remains open:
- **Two vacancies on regular graphs.** No diversity-seeking cycle on any cubic graph with
  N = 8 or 10, nor any quartic graph with N = 8 or 9. At the 120k-state cap, 114 instances
  were skipped at cubic N = 10 and 16 at quartic N = 9.
- **Three vacancies on 4-regular graphs.** No cycle at N = 8 or 9.

Cubic graphs with three vacancies have cycles at N = 8 (Q₃) and at N = 10 (two instances, both
verified).

**Q2591: disproved.** The variety paper proves potential for 3-regular graphs with two
vacancies, and conjectures it for every graph with two vacancies. Its random-graph experiments
found cycles only with at least three. Counterexample:
- **Graph:** 4-regular on 9 vertices, with neighbourhoods
  0:{3,6,7,8}, 1:{2,3,5,6}, 2:{1,3,4,7}, 3:{0,1,2,8}, 4:{2,5,7,8}, 5:{1,4,6,8}, 6:{0,1,5,7},
  7:{0,2,4,6}, 8:{0,3,4,5}.
- **Agents:** 7, of four types with counts (2, 2, 2, 1). Exactly 2 vacancies.
- **Cycle:** 24 moves, starting from [0,4,0,1,2,3,2,1,3]. It is three repetitions of an 8-move
  pattern with the types rotated.
- **First moves:** 7→0 (utility 1 → 2), 5→2 (2 → 3), 4→7 (1 → 2).
- **Certificate:** `jump_regular_4_9_variety_2_cap120000.json`.

It was the only cycle among the 208 quartic 9-vertex instances run with two vacancies; 16
instances were over the state cap.

**Smaller observations, diversity utility.**
- Improving cycles already occur with 1, 2 or 3 vacancies on small non-regular, non-tree
  graphs (N = 6, 2 vacancies).
- 28 instances with N ≤ 7 and a single vacancy are not weakly acyclic: some configurations
  can never reach an equilibrium. None of these graphs is a tree, so Q2599 is untouched.

**Evidence only.**
- **Variety utility with N ≤ 7.** No improving cycle on any connected graph with N ≤ 7, for
  any number of vacancies or type counts.
- **Q2599.** Every tree with N ≤ 10 is weakly acyclic. Instances above 60k states were skipped
  and are counted in the JSON.
- **Q2590 and Q2696.** Every instance run has an equilibrium.

**Scope restriction (recorded).** The preregistration planned "every count vector" for trees
and regular graphs. Instances above 60,000 configurations (trees) or 120,000 (regular graphs)
were skipped for run time. The skipped counts are reported per vacancy level in each JSON.

## Open items

1. Q2598 at n = 18 (the computation was still running at this snapshot; n ≤ 17 has no counterexample).
2. Prove the weakened Lemma 9, and with it Theorem 3 of arXiv:2510.24280. Q3189 for |S| = 2 should follow from the
   Q3188 machinery extended to the friendly profiles.
3. Not yet attempted in this round: isolation games (Q1954, Q1955), round-robin rest times (Q360) and count-based
   game values (Q2287).
