# Q3188: proof that antagonistic play matches zero-sum play for every two-move set

**Question (Q3188, statement `01d031a3c2d35630a767`).** If |S| = 2, is
z(h) = o¹_AvA(h) − o²_AvA(h) for every h ≥ 0? This is Conjecture 15 of Bhagat, Kulkarni,
Larsson and Murali, *Tie-breaking in self interest cumulative subtraction games*,
arXiv:2510.24280v2, p. 12, with the outcome function of their Definition 2 (pp. 4–5).

**Answer: yes.** Theorem 1 below proves it for every S = {a < b} and every h. The
argument is self-contained. The check script `q3188_proof_check.py` tests every lemma
mechanically against a separately written game-tree evaluator. It found no failure for
any pair with b ≤ 70 and h ≤ 1500.

The model is Definition 2 exactly. A player maximizes their own cumulation. When several
moves give the same cumulation, an antagonistic player picks the one that leaves the
opponent the least. No restriction of the catalog statement was needed.

## Notation

- S = {a, b} with 1 ≤ a < b. Write Δ = b − a.
- u(h) = o¹_AvA(h) and v(h) = o²_AvA(h).
- z is the zero-sum value: z(h) = 0 for h < a, and otherwise z(h) = max_{s∈S, s≤h} (s − z(h − s)).
- From heap h ≥ a, the move s gives the mover own_h(s) = s + v(h − s) and the opponent
  opp_h(s) = u(h − s). AvA picks a move maximizing own_h(s), breaking ties by the smaller
  opp_h(s). Then u(h) is the maximum own_h(s), and v(h) = opp_h(s*) for the chosen s*.

**A one-player comparison game.** Let g(y), the greedy move, be b if y ≥ b and a if
a ≤ y < b. Define G and V by G(y) = V(y) = 0 for y < a and, for y ≥ a,

  V(y) = G(y − g(y)),  G(y) = max_{s∈S, s≤y} (s + V(y − s)).

G(y) is the most the player to move can collect against an opponent who always takes the
largest legal move. V(y) is what the player moving second from y collects in that game.
Two facts are immediate: 0 ≤ G(y) ≤ y, and G(y) ≥ b whenever y ≥ b.

Put δ(t) = G(t + Δ) − G(t) and ε(t) = V(t + Δ) − V(t) for t ≥ 0.

The proof shows that AvA play *is* this comparison game: u = G and v = V (Theorem 1).
The whole difficulty is one property of G, Corollary 7: whenever adding Δ tokens helps
the second player by more than Δ, it does not help the first player at all.

## Lemma 1 (monotonicity): δ(t) ≥ 0 and ε(t) ≥ 0 for every t

The proof is a joint induction on t. The V-part at t uses only the G-part below t, and
the G-part at t uses only the V-part below t.

*V-part.*
- If t < a, then V(t) = 0 ≤ V(t + Δ).
- If a ≤ t < b ≤ t + Δ, then V(t) = G(t − a) and V(t + Δ) = G(t + Δ − b) = G(t − a), so the
  two are equal.
- If a ≤ t and t + Δ < b, then V(t + Δ) = G(t − a + Δ) ≥ G(t − a) = V(t), by the G-part at
  t − a.
- If t ≥ b, then V(t + Δ) = G(t − b + Δ) ≥ G(t − b) = V(t), by the G-part at t − b.

*G-part.* If t < a then G(t) = 0. Otherwise let s* be a maximizing move at t.
- If s* = a and t + Δ ≥ b, playing b from t + Δ reaches t + Δ − b = t − a, the same position
  s* reaches from t. So G(t + Δ) ≥ b + V(t − a) = G(t) + Δ.
- If s* = a and t + Δ < b, then G(t + Δ) ≥ a + V(t − a + Δ) ≥ a + V(t − a) = G(t), by the
  V-part at t − a.
- If s* = b, then t ≥ b and G(t + Δ) ≥ b + V(t − b + Δ) ≥ b + V(t − b) = G(t), by the V-part at
  t − b. ∎

## Lemma 2: ε(t) ≤ Δ for t < b, and ε(t) = δ(t − b) for t ≥ b

*(b)* For t ≥ b both t and t + Δ have greedy move b. So V(t + Δ) = G(t − a) and
V(t) = G(t − b), and t − a = (t − b) + Δ.

*(a)* Let t < b.
- If t + Δ ≥ b, then t ≥ a, and V(t) = G(t − a) = G(t + Δ − b) = V(t + Δ). So ε(t) = 0.
- If t + Δ < b, then t < a and V(t) = 0. Also V(t + Δ) is 0 or G(t + Δ − a) ≤ t + Δ − a < Δ. ∎

## Lemma 3 (excess chains): if δ(t) > Δ, then either t < a, or t ≥ a + b and δ(t − a − b) > Δ

Suppose δ(t) > Δ and t ≥ a. Then t + Δ ≥ b, and

  G(t + Δ) = max(a + V(t − a + Δ), b + V(t − a)).

The second term is at most G(t) + Δ, because G(t) ≥ a + V(t − a). So the first term
attains G(t + Δ), and

  a + V(t − a + Δ) > G(t) + Δ ≥ a + V(t − a) + Δ,

that is, ε(t − a) > Δ. By Lemma 2(a), t − a ≥ b. By Lemma 2(b), δ(t − a − b) = ε(t − a) > Δ. ∎

So every t with δ(t) > Δ lies on a chain t₀, t₀ + (a+b), t₀ + 2(a+b), … that starts at some
t₀ < a.

## Lemma 4 (closed form for G)

Write y = 2bN + ρ with 0 ≤ ρ < 2b, and θ(e) = e − G(e) for 0 ≤ e < 2b. Then

  G(y) = bN + ρ − min { θ(ρ + iΔ) : 0 ≤ i ≤ N, ρ + iΔ < 2b }.

*Proof.* For y ≥ 2b, both y − a and y − b are at least b, so V(y − s) = G(y − s − b) and

  G(y) = max(a + G(y − a − b), b + G(y − 2b))   (y ≥ 2b).   (R)

Call the step y ↦ y − (a+b), with gain a, an A-round, and the step y ↦ y − 2b, with gain b,
a B-round. (R) may be applied at any heap ≥ 2b.

Unfolding (R) until the heap first drops below 2b gives, by induction on y,
G(y) = max (ia + jb + G(y′)). The maximum is over pairs (i, j) for which i A-rounds and j
B-rounds can be ordered so that every round starts from a heap ≥ 2b, and
y′ = y − i(a+b) − 2bj lies in [0, 2b).

Heaps decrease along any ordering, so the binding constraint is the start of the last
round, y′ + (that round's length) ≥ 2b. Hence (i, j) ≠ (0, 0) is admissible exactly when
y′ ∈ [0, 2b) and either j ≥ 1 (end with a B-round) or y′ ≥ Δ (end with an A-round). The pair
(0, 0) is admissible exactly when y < 2b.

For a given i, y − i(a+b) = 2b(N − i) + ρ + iΔ. So y′ ∈ [0, 2b) forces ρ + iΔ = 2bM + y′ and
j = N − i + M for some M ≥ 0. Substituting iΔ = 2bM + y′ − ρ, the value is

  ia + jb + G(y′) = bN + ρ − bM − θ(y′).

θ(e) < b on [0, 2b). For e < b this holds because θ(e) ≤ e. For e ≥ b it holds because
G(e) ≥ b. So any term with M ≥ 1 is below the term i = 0, which is always admissible
because (0, N) is.

Among the terms with M = 0, take i ≤ N. If N − i ≥ 1 the pair is admissible. If i = N ≥ 1,
then y′ = ρ + NΔ ≥ Δ, so it is admissible. If i = N = 0, then y = ρ < 2b, and the pair is
again admissible. ∎

## Lemma 5: if b ≥ 2a, then δ(t) ≤ Δ for every t

By Lemma 3 it is enough to show δ(t) ≤ Δ for t < a.

There G(t) = 0, and t + Δ < a + Δ = b, so from heap t + Δ both players can only take a.
Therefore G(t + Δ) = a⌈k/2⌉ with k = ⌊(t + Δ)/a⌋ ≥ 1.
- If k ≤ 2, this is a ≤ Δ.
- If k ≥ 3, then ka ≤ t + Δ ≤ a − 1 + Δ gives Δ ≥ (k − 1)a + 1 > ⌈k/2⌉a. ∎

## Lemma 6: if b < 2a, then δ(t) > Δ implies δ(t + b) = 0

*The defect θ for b < 2a.* G(e) = 0 on [0, a), G(e) = a on [a, b), and G(e) = b on
[b, 2b). The first two are immediate because Δ < a. On [b, 2b):
- Playing b, the mover may see the opponent take a, after which fewer than Δ < a tokens
  remain. The mover's total is b.
- Playing a, the opponent takes b or a. What then remains is less than Δ < a, because
  e − a < b gives e − 2a < Δ. The mover's total is a.

So θ(e) = e on [0, a), θ(e) = e − a on [a, b), and θ(e) = e − b on [b, 2b).

For e and e + Δ in [0, 2b), the step θ(e + Δ) − θ(e) therefore takes three values:
- Δ inside a piece;
- Δ − a < 0 when e < a ≤ e + Δ;
- 0 when a ≤ e < b ≤ e + Δ.

No step crosses both a and b. The only decreasing step is the one across a.

*Where δ exceeds Δ.* Let t = 2bN + ρ.

Suppose first ρ + Δ ≥ 2b. Only i = 0 enters G(t), and t + Δ = 2b(N + 1) + ρ′ with
ρ′ = ρ + Δ − 2b. Lemma 4 then gives δ(t) ≤ Δ − b + θ(ρ) < Δ. This holds for every a < b, not
just b < 2a.

Suppose instead ρ + Δ < 2b. Write θᵢ = θ(ρ + iΔ). Let m₀ be the minimum of θᵢ over
0 ≤ i ≤ N, and m₁ the minimum over 1 ≤ i ≤ N + 1, both restricted to ρ + iΔ < 2b. Lemma 4
gives δ(t) = Δ + m₀ − m₁. So δ(t) > Δ means m₁ < m₀, which needs index N + 1 in range and
θ_{N+1} < θᵢ for every i ≤ N.

θ_{N+1} < θ_N forces the step from ρ + NΔ to ρ + (N+1)Δ to cross a: ρ + NΔ < a ≤ ρ + (N+1)Δ.
In particular ρ < a.

*The shadow at t + b.* Now t + b = 2bN + (ρ + b). Since ρ < a, we have ρ + b + Δ < 2b. For
0 ≤ i ≤ N + 1,

  b ≤ ρ + b + iΔ ≤ ρ + NΔ + Δ + b < a + Δ + b = 2b.

So every index is in range, and θ(ρ + b + iΔ) = ρ + iΔ. Hence m₀′ = ρ and m₁′ = ρ + Δ, and
δ(t + b) = Δ + ρ − (ρ + Δ) = 0. ∎

## Corollary 7: ε(x) > Δ implies δ(x) = 0

By Lemma 2(a), x ≥ b. By Lemma 2(b), δ(x − b) = ε(x) > Δ.
- If b ≥ 2a this is impossible, by Lemma 5.
- Otherwise Lemma 6 at t = x − b gives δ(x) = 0. ∎

## Theorem 1

For S = {a < b} and every h ≥ 0:

  u(h) = G(h), v(h) = V(h), and z(h) = u(h) − v(h).

*Proof.* Induction on h. Below a, everything is 0. Let h ≥ a and assume the claims below
h.

*First coordinate.* u(h) = max_s (s + v(h − s)) = max_s (s + V(h − s)) = G(h).

*Second coordinate.* If a ≤ h < b, then only a is legal, and v(h) = u(h − a) = G(h − a) = V(h).

Let h ≥ b and x = h − b, so that h − a = x + Δ. Then

  own_h(a) − own_h(b) = ε(x) − Δ,  opp_h(a) − opp_h(b) = δ(x).

- If ε(x) < Δ, AvA plays b, and v(h) = G(x) = V(h).
- If ε(x) > Δ, AvA plays a. Corollary 7 gives δ(x) = 0, so v(h) = G(x + Δ) = G(x) = V(h).
- If ε(x) = Δ, the antagonistic rule takes the smaller of G(x + Δ) and G(x). That is G(x),
  by Lemma 1.

*Difference.* By the induction hypothesis, own_h(s) − opp_h(s) = s − z(h − s) for each legal s.
So z(h) is the largest own − opp over the legal moves. The two options are never strictly
better for both players at once:
- ε(x) − Δ > 0 together with δ(x) > 0 is excluded by Corollary 7;
- ε(x) − Δ < 0 together with δ(x) < 0 is excluded by Lemma 1.

Let s* be the AvA choice and s′ the other move.
- If own_h(s*) > own_h(s′), then opp_h(s*) ≤ opp_h(s′).
- If the two are equal, the tie-break gives the same inequality.

Either way s* maximizes own − opp, so u(h) − v(h) = own_h(s*) − opp_h(s*) = z(h). ∎

## What the proof adds beyond the conjecture

1. **AvA play is a best response to a greedy opponent.** The first player's AvA payoff is
   the most they can collect against an opponent who always removes the larger legal
   amount. The second player's payoff is v(h) = u(h − b) for h ≥ b. AvA may still sacrifice
   (play a) on the board; Corollary 7 says it does so only when that leaves the opponent's
   payoff unchanged.

2. **Closed forms.** z(h) = G(h) − G(h − b) for h ≥ b, with G from Lemma 4. When b < 2a, θ is
   explicit, so z, u and v have explicit formulas in N = ⌊h/2b⌋ and ρ = h mod 2b. Lemma 4 also
   shows directly that z is eventually periodic with period 2b. Once N exceeds 2b/Δ, the index
   set {i ≤ N : ρ + iΔ < 2b} stops depending on N, so G(h + 2b) = G(h) + b.

3. **Why three moves fail.** Lemma 3 uses the identity h + Δ − b = h − a, which lets the
   pair (h − b, h − a) share an option. With three moves the reduction to a single greedy
   opponent breaks down. The exploratory scan found the first three-move discrepancy at
   S = {6, 13, 17}, h = 76, where s₂ = 13 > 2s₃ = 12 and s₁ = 17 < s₂ + s₃ = 19. It lies in
   the region where the source's Conjecture 16 permits discrepancies.

## Mechanical checks

`q3188_proof_check.py` computes AvA outcomes by memoized recursion over the explicit game
tree, written separately from `subtraction.py`. It checks u = G, v = V, z = G − V,
Lemma 4's closed form, Lemma 1, Lemma 2, Lemma 3, Lemma 5 and Lemma 6, and Lemma 6's base
block [a − Δ, a).

| Range | Pairs | Failing pairs | Output |
|---|---:|---:|---|
| b ≤ 40, h ≤ 600 | 780 | 0 | `q3188_proof_check_b40_H600.json` |
| b ≤ 70, h ≤ 1500 | 2,415 | 0 | `q3188_proof_check_b70_H1500.json` |

The b ≤ 40 run exercised 5,906 positions with δ > Δ. A mutation test confirmed the check
can fail: swapping in the friendly tie-break makes it report AvA ≠ (G, V) at S = {3, 5},
h = 14, the source's first FvF/AvA discrepancy.

These runs are evidence that the write-up has no slip. The proof is the argument above.
The earlier scan `q3188_scan.py` (b ≤ 60, h ≤ 4000, 0 mismatches) was the preregistered
test that came before the proof.
