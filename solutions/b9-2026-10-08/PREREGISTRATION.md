# B9 local work — preregistration (8 October 2026)

The user asked for B9 to be worked here before it returns to the external agent. This file
fixes the definitions, decision rules and predictions **before** any computation. Later
sections are appended for each problem before its runs, and nothing above them is edited
afterwards.

## Standing rules

- **Counterexamples.** A counterexample counts only if two independent implementations
  agree on it exactly: different code paths, written separately. The second is direct
  game-tree or brute-force evaluation, not a copy of the dynamic programme. The exact
  objects (sets, heap sizes, strings, graphs) must be printed in the report.
- **Proofs.** A proof is a written argument whose finite base cases, if any, are checked
  exhaustively. Agreement up to a bound is reported as evidence, never as a proof.
- **Scope changes.** Any change of model from the catalog statement is recorded as a
  restriction. Example: the source's tie-breaking definition versus the catalog paraphrase.
- **Failed checks.** A run whose sanity checks fail is discarded and recorded as discarded,
  not kept.
- **Arithmetic.** All arithmetic is exact (integers or `fractions.Fraction`); no floating
  comparisons decide anything.

## Problem 1: Q3188 and Q3189, self-interest cumulative subtraction games

**Source.** Bhagat–Kulkarni–Larsson–Murali, arXiv:2510.24280v2, Definition 2 (p. 4),
Conjecture 15 (p. 12), §6 Problem 2 and Conjecture 17 (p. 12). Local text:
`texts/papers/collections-c1c7ae3fbd3d2518.txt.gz`.

**Definitions.**
- Profiles: τ = {FvF, FvA, AvF, AvA}. The first letter is the tie-breaking rule of the player
  to move from h; the dual d swaps the letters.
- The game ends at h < min S, where o¹_X = o² _X = 0.
- Otherwise o¹_X(h) = max_{s∈S, s≤h} [s + o²_{d(X)}(h−s)].
- S*(h) is the set of maximizing s. Then o²_X(h) = o¹_{d(X)}(h−s*). Here s* minimizes
  o¹_{d(X)}(h−s) over S*(h) when the mover is antagonistic (X ∈ {AvF, AvA}) and maximizes it
  otherwise.
- The zero-sum value is z(h) = max_{s≤h} (s − z(h−s)), with z = 0 below min S.

**Tests.**
- **Q3188:** every S = {a < b} with b ≤ 60, every h ≤ 4000. Compare z(h) with
  o¹_AvA(h) − o²_AvA(h).
- **Q3189:**
  - every S = {a < b} with b ≤ 40, and every S with |S| = 3 and max S ≤ 18;
  - h ≤ 6000;
  - for all ordered profile pairs (X, Y) and both coordinates, test whether
    D(h) = O_X(h) − O_Y(h) satisfies D(h + 2 max S) = D(h) for every h in the final third of
    the range;
  - record the boundedness of D across the range (Conjecture 17), and the first h after
    which periodicity holds through the end.

**Decision rules.**
- **Q3188:** a mismatch confirmed by direct game-tree recursion (memoized minimax over the
  explicit tree for the AvA profile, written separately) disproves the conjecture. If no
  mismatch appears, attempt a proof for |S| = 2.
- **Q3189:** a pair (X, Y) whose D fails the 2 max S period at large h is evidence against
  the conjecture. It counts as a disproof only if D is shown not eventually periodic with
  that period, either by a proof or by an explicit linear-growth law. Finite data alone
  cannot prove non-periodicity, but it can exhibit a different exact eventual period. A
  different minimal period P with P ∤ 2 max S, holding through a long stable range, would be
  reported as a counterexample candidate together with the structure that forces it.

**Predictions** (before any run):
- Q3188 holds for every tested pair: probability 0.75.
- Discrepancies are bounded for every tested S: 0.8.
- Q3189's 2 max S period holds for all |S| = 2: 0.6; for all tested |S| = 3: 0.5.

## Problem 2: Q2598, flipped Penney-Ante optimal responses

**Source.** Phillips–Hildebrand, Integers 27 (2027 volume pagination as supplied), §7
Conjecture 7.3, with Conway's leading-number formula. The local texts must be checked for
the exact definition of "optimal" before running.

**Plan.**
- Compute II's winning probability exactly for every A, B ∈ {H,T}ⁿ, B ≠ A, n ≤ 18, using
  Conway's formula. The odds that B beats A are (AA − AB) : (BB − BA), with AB the
  correlation number.
- In the flipped game, II wins when A appears first, so II's probability of winning is the
  probability that A appears first.
- Find all maximizing B, and test whether every one lies in
  {Hⁿ, Tⁿ, a₂⋯aₙH, a₂⋯aₙT} \ {A}.
- **Independent check:** the absorbing Markov chain on suffix states, with exact rational
  linear algebra, for every A at n ≤ 10, and for any counterexample at any n.

**Prediction:** Conjecture 7.3 holds for all n ≤ 18, probability 0.7.

## Problem 3: Q3259–3261, Markov Penney races on S_k

**Source.** Yixin Lin, Dartmouth thesis 2024, Chapter 2. The thesis PDF is not local; the
setup is taken from the catalog statement and the Elizalde–Lin paper
(`texts/papers/collections-ce0c06e237821f58.txt.gz`).

**Chain.** On S_k, X₀ is uniform. P(σ, τ) = 1/k when st(σ₂…σ_k) = st(τ₁…τ_{k−1}), and 0
otherwise. T_σ = min{t ≥ 0 : X_t = σ}.

**Tests**, by exact rational linear algebra:
- **Q3259:** E[T_σ] for every σ, k ≤ 6.
- **Q3260 and Q3261:** Pr(T_σ < T_τ) for every relevant ordered pair, k ≤ 5 exhaustively,
  and k = 6 for all pairs with Q3261's monotonicity condition and a random sample of the
  rest.

**Independent check:** a separate first-step recursion on the product chain, and exact
enumeration of path probabilities truncated at length L with a rational tail bound for
k = 3, 4.

**Predictions:**
- Q3259 holds for k ≤ 6: 0.7.
- Q3260: 0.6.
- Q3261: 0.6.

## Method note for Problem 2 (added 8 October 2026, before any Q2598 run)

Evaluating every pair (A, B) at n = 18 is 6.9·10¹⁰ pairs, which is out of reach. The maximizers
are found instead with a rigorous bound, and the question is unchanged.

**The bound.** Write X = BB − BA and Y = AA − AB, so that P(A first) = X/(X + Y). Take any
B ∉ {Hⁿ, Tⁿ, a₂⋯aₙH, a₂⋯aₙT}. Then δ₂(A, B) = 0 and B is not constant, which gives
AB ≤ 2^{n−2} − 1 and BB ≤ 3·2^{n−2} − 1. Hence P(A first) ≤ U(A) = (3·2^{n−2} − 1)/(2^{n−1} + AA).

**Decision rule.**
- If the best candidate value is strictly above U(A), the conjecture holds for that A.
- Otherwise every B is evaluated exactly for that A.

All comparisons are integer cross-multiplications.

**Independent check.** For n ≤ 10, for every A and every B, P(A first) is also computed from
the absorbing Markov chain on prefix states, solved by fraction-free integer elimination. The
two methods must agree exactly.

## Problem 4: jump games (Q2590, Q2591, Q2599, Q2600, Q2696, Q2697), added before any run

**Sources.**
- Variety-seeking: Narayanan, Opatrny, Tummala and Voudouris, arXiv 2505.10005 (local
  `collections-8c936615867f1403`). Covers Q2590 and Q2591.
- Diversity-seeking: Narayanan, Sabbagh and Voudouris, arXiv 2305.17757 (local
  `collections-8a81d415af12f6a4`). Covers Q2599, Q2600, Q2696 and Q2697.

**Model, as in the sources.**
- G is connected with |V| > n. There are k ≥ 2 nonempty types, and every agent is strategic
  (no stubborn agents).
- Variety utility: the number of distinct types other than one's own among the occupied
  neighbours.
- Diversity utility: the fraction of occupied neighbours of another type, or 0 if there are
  none.
- A move takes an agent to any empty vertex. It is improving when the agent's utility after
  the move, computed with its old vertex now empty, is strictly larger.

**State reduction.** The search runs on type-configurations V → {empty, 1..k} with the given
type counts. Agents of one type are interchangeable. A cycle of configurations lifts to an
improving response cycle (IRC) of labelled agents by repeating it; the lift is a cycle because
the label permutation has finite order. Sinks correspond to sinks. Type labels are symmetric,
so sorted count vectors suffice.

**Tests.**
- **(a) Exhaustive small graphs.** All connected graphs on N ≤ 7 vertices (the networkx atlas),
  every number of empty vertices e from 1 to N − 2, every sorted count vector with k ≥ 2, under
  both utilities. For each instance record:
  - whether an IRC exists (a strongly connected component with at least two states);
  - whether an equilibrium exists (a sink);
  - whether the instance is weakly acyclic (every bottom component is a single sink).
- **(b) Trees** (Q2599, Q2600). All trees up to the largest N the run time allows (target
  N ≤ 11), every e, every count vector, diversity utility. Spiders are reported separately.
- **(c) Regular graphs** (Q2697). Those in (a), plus the cubic graphs on 8 and 10 vertices and
  4-regular graphs on 8–9 vertices, if they can be generated exhaustively. Otherwise random
  samples, recorded as samples. Diversity utility with e ∈ {2, 3}. For Q2591 the variety
  utility is run with e = 2 on the same families.

**Decision rules.**
- An IRC certificate disproves "every improving sequence terminates" for the class it lies in:
  Q2591, Q2600 or Q2697. The certificate is an explicit cycle of configurations with the
  utility before and after each move, and it must be re-verified by a separately written
  checker.
- An instance with no sink disproves equilibrium existence (Q2590, Q2696), after the same
  re-verification.
- A tree instance with a state that cannot reach a sink disproves Q2599.
- Finding nothing is reported as exhaustive evidence for the stated range only.

**Predictions** (before any run):
- An IRC for variety with e = 2 appears among N ≤ 7 graphs: 0.25.
- A diversity IRC on a regular graph with e ∈ {2, 3}: 0.3.
- A diversity IRC on a spider: 0.2.
- A tree that is not weakly acyclic: 0.15.
- An equilibrium exists in every tested instance, for both utilities: 0.9.
