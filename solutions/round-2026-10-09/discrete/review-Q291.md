# Independent review of the Q291 multiplayer RPS proof

Reviewer: discrete-mathematics workstream. Date: 2026-10-09.

**Verdict: accepted for the complete catalog statement, for every integer $m\ge2$.** The reviewed argument was communicated by the root workstream and independently checked against the primary game rules and payoff convention. No substantive gap was found. The argument permits unequal mixed strategies, pure paper players, and a pure scissors player in the hypothetical configuration.

## Source alignment

The primary thesis is Itai Maimon, *Homological Codes, their Extensions, and Certain Unfair Games* (UC San Diego, 2024), available at <https://escholarship.org/content/qt84c9t3c3/qt84c9t3c3.pdf>. Section 5.7 gives the game and reduces the desired support statement to Conjecture 5.7.6 on printed p. 162.

The subsequent paper *Different Forms of Imbalance in Strongly Playable Discrete Games II: Multi-Player RPS Games*, <https://arxiv.org/pdf/2511.13736>, Definition 2.1, uses the same priority rule: rock beats scissors even when paper is present; in the absence of that rock/scissors conflict, the usual winning action wins. The payoffs are shared among all players selecting the winning action. Definition 1.1 gives payoff $(m-k)/k$ to each of $k$ winners and $-1$ to each loser. An all-way tie counts as all players winning. The paper's Theorem 3.1 treats the support statement for $m<50$, while the later infeasibility conjecture remains unrestricted. These sources were inspected on 2026-10-09.

The review verifies the game-theoretic statement directly. It does not require reproducing every algebraic transformation in the thesis's displayed infeasibility system.

## 1. Payoff normalization

Applying the positive affine transformation $u\mapsto(u+1)/m$ to a player's payoff preserves every best-response comparison. The normalized payoff is $1/k$ for one of $k$ winners and zero for a loser. In an all-way tie it is $1/m$. All formulas below use this normalization.

## 2. Zero scissors-support players

If all opponents choose only rock or paper, choosing paper is strictly better than choosing rock for every possible opponents' pure profile. If every opponent chooses rock, paper wins alone, whereas rock shares the all-way tie. If any opponent chooses paper, paper has a positive share and rock loses. Thus in a putative equilibrium without scissors, every player must choose paper purely. A deviation to scissors then wins alone, improving $1/m$ to 1. This excludes the case for every $m\ge2$.

## 3. Exactly one scissors-support player

Suppose player $h$ is the unique player assigning positive probability $s>0$ to scissors. Every other player chooses only rock and paper. By the same pointwise comparison just used, player $h$ cannot support rock; its distribution is paper with probability $1-s$, scissors with probability $s$.

For an ordinary player $i\ne h$, let $q_i$ be its paper probability. With independent Bernoulli variables $X_i$ of means $q_i$, set

$$
A=\mathbb E\frac{1}{1+\sum_{i\ne h}X_i},
\qquad
Q=\prod_{i\ne h}q_i.
$$

These are exactly player $h$'s normalized payoffs for the pure actions paper and scissors. Paper always beats the opponents' rock/paper profile and shares with the other paper players. Scissors wins precisely when all opponents choose paper, in which case it wins alone.

Since scissors is in player $h$'s support, equilibrium would require $Q\ge A>0$. In particular, every $q_i>0$, including in boundary cases where another player chooses paper purely.

Fix an ordinary player $i$, and put

$$
T_i=\sum_{\substack{j\ne h\\j\ne i}}X_j,\qquad
B_i=\mathbb E\frac1{2+T_i},\qquad
D_i=\mathbb E\frac1{1+T_i}.
$$

Independence gives $A=(1-q_i)D_i+q_iB_i\ge B_i$.

If $i$ chooses paper, it can win only when $h$ also chooses paper. Then the winners are $h$, $i$, and the $T_i$ other paper players. Thus

$$
U_i(P)=(1-s)B_i.
$$

If $i$ chooses scissors, any other ordinary player's rock causes scissors to lose. If all those players choose paper, player $i$ wins alone when $h$ chooses paper, and shares with $h$ when $h$ chooses scissors. Hence

$$
U_i(S)=\left(1-\frac{s}{2}\right)
\prod_{\substack{j\ne h\\j\ne i}}q_j
=\left(1-\frac{s}{2}\right)\frac Q{q_i}.
$$

Every inequality in the proposed contradiction is now justified:

$$
U_i(P)
\le(1-s)A
\le(1-s)Q
\le(1-s)\frac Q{q_i}
<
\left(1-\frac{s}{2}\right)\frac Q{q_i}
=U_i(S).
$$

The non-strict steps use $1-s\ge0$, $A\le Q$, and $0<q_i\le1$. The final step is strict because $s>0$ and $Q/q_i>0$. But $q_i>0$ says that paper belongs to $i$'s support. A supported action cannot have strictly smaller payoff than a deviation. This is the contradiction.

## Boundary and scope checks

When $s=1$, the paper payoff above is zero and the scissors deviation payoff is positive, so the same proof applies. When $q_i=1$, division by $q_i$ is harmless and the last strict inequality persists. When $m=2$, the sum $T_i$ is zero and the product over other ordinary players is the empty product 1, giving the usual two-player case. Unequal $q_i$ never affect the comparison.

Independence is used in exactly the way appropriate to a mixed-strategy Nash equilibrium. The proof does not address correlated equilibrium, which is outside the catalog question.

Thus every mixed-strategy Nash equilibrium has at least two players assigning positive probability to scissors. No numerical search or symmetry assumption is needed for this conclusion.
