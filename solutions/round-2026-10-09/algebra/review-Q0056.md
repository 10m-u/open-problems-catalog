# Independent review of the Q56 reduction

**Verdict: accepted as a conditional negative resolution in the standard binary rational-input model.** The reduction proves NP-hardness of the proposed high-precision approximation guarantee already for mode size two, CP rank at most two, zero sparse component, and zero dual weights. The uniform-marginal optimal-transport corollary is also valid. This review does not assert that P differs from NP or certify historical novelty.

Reviewed on 9 October 2026: `../optimization/Q0056.md`, the exact checker `../optimization/check_q0056.py`, and its recorded output `../optimization/q0056-checks.json`.

## Source alignment

I read the primary [Altschuler thesis](https://jasonaltschuler.github.io/altschuler_PhD_thesis.pdf), Definition 6.7.2 and §6.7.2, including Theorem 6.7.4 and its following discussion on printed page 190. The source asks whether the constant-rank approximate-minimum runtime can depend polynomially on $\log(C_{\max}/\varepsilon)$ in place of $C_{\max}/\varepsilon$. The permitted representation supplies a rank factorization and bounds the low-rank and sparse tensor entries by $O(C_{\max})$. The report's positive two-term construction satisfies these conditions directly, without cancellation. The source's separate hardness for variable rank would not alone answer this question; the audited reduction fixes the rank bound at two.

## Reduction, precision, and encoding

For positive integers $a_1,\ldots,a_k$, let $P=\prod_i a_i$. A nonsquare $P$ cannot have an equal-product partition and is handled immediately. If $P=t^2$, the stated factorization gives

$$
C_b=\frac12\left(\prod_i a_i^{-b_i}+\prod_i a_i^{-(1-b_i)}\right)
=\frac{A_b+P/A_b}{2P},\qquad A_b=\prod_{i:b_i=1}a_i.
$$

Both numerator summands are integers. An equal-product partition gives minimum $1/t$. Otherwise their sum is strictly larger than the integer $2t$, so the minimum is at least $1/t+1/(2P)$. This lower bound is valid even if it is not the sharpest possible gap.

With $\varepsilon=1/(8P)$, a two-sided additive value estimate is at most $1/t+1/(8P)$ in the YES case and at least $1/t+3/(8P)$ in the NO case. The comparison threshold $1/t+1/(4P)$ therefore separates the cases strictly. A feasible approximately minimizing index also suffices, because its rational cost can be evaluated exactly.

The supplied factors, including the factor $1/2$ absorbed in one mode, are positive rationals at most one. The maximum tensor entry is $(P+1)/(2P)\in[1/2,1]$. If $L$ is the binary input length, then $\log P=O(L)$; all factor coordinates, products, square roots, precision parameters, and thresholds have polynomial encoding length and are computable in polynomial time. Finally

$$
C_{\max}/\varepsilon=4(P+1),\qquad
\log(C_{\max}/\varepsilon)=O(L).
$$

Thus the hypothetical guarantee would yield a polynomial-time decision algorithm for PRODUCT PARTITION. This is a bit-complexity claim, as stated in the report; an unspecified unit-cost real-arithmetic interpretation should not be substituted.

The included ordinary-hardness reduction from EXACT COVER BY 3-SETS is correct. With universe-prime product $B$ and product $P_0$ of all triple encodings, appending $P_0$ and $B^2$ makes the full product $(P_0B)^2$. A partition half of product $P_0B$ contains exactly one appended integer. Either choice yields an exact cover among the selected original triples or their complement. The empty-universe case is handled separately, and all encodings have polynomial length. Ordinary NP-hardness is sufficient for the claimed implication.

## Uniform-marginal corollary and verification

Complement symmetry $C_b=C_{1-b}$ is exact. For a minimum entry at $b^*$, the distribution assigning mass $1/2$ to each of $b^*$ and $1-b^*$ has uniform binary marginals and attains that entry as its expected cost. No coupling has smaller expected cost than the minimum entry. The fixed-uniform-marginal MOT optimum therefore equals the entry minimum, so the identical gap proves the corollary directly.

I inspected the exact rational checker and its recorded successful run over 3,002 integer lists and 141,568 tensor entries, including square YES, square NO, and nonsquare cases. Its controls cover the factor formula, maximum, precision separation, and complement coupling. These checks support the formulas; the general reduction above supplies the proof.

No mathematical gap was found. The stated distinction between a deterministic implication P = NP and a bounded-error randomized implication NP $\subseteq$ BPP is correct. The proof does not exclude algorithms polynomial in $1/\varepsilon$ or algorithms with additional input restrictions.
