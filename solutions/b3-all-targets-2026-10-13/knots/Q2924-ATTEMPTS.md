# Q2924: positive-braid rainbow ruling rows

The exact scope is [SETUP](SETUP.md) and primary [Su–Xie–Yu, Conjecture 2.3](https://arxiv.org/pdf/2603.27888v2): every positive braid, its rainbow Legendrian closure, component normalization z^b R(z), and log-concavity **with no internal zeros** of the coefficient row in z². Arbitrary Legendrian links are excluded. Current consecutive full-target failure count: 5, accepted by root review. Source/code errors and replay of published bounded coverage count zero. Stop solve work unless root rejects a count.

The engine [rulings.py](rulings.py) implements Definition 2.1 exactly. Permutations are tuples of **values**, so left multiplication by s_i swaps values i,i+1, not positions. It always permits that swap; staying contributes z and is permitted exactly when the value i occurs after i+1. Both endpoints are w0. The component count is the cycle count of the ordinary braid permutation. Every returning raw switch exponent s satisfies s-n+b>=0 and is even after that shift; the engine verifies these assertions before producing the row. Independent mask enumeration checks the source's twelve-letter Example 2.4, and 22 braid-relation/commutation controls test the convention. Receipts are [RULING-CHECK](RULING-CHECK.json) and [fresh families](RULING-FAMILY-CHECK.json).

<a id="q2924-a1"></a>
## A1 — construct a counterexample with repeated competing-descent blocks

The source reports coverage n<=6 and length<=15. A fresh actual construction route explores longer repeated multi-peak words, where several generators compete for the same permutation state and the one-peak factorization is not available directly. The six selected blocks are

    n=4: (1,2,3,2), (1,1,2,3,3,2), (1,2,1,3,2,3);
    n=5: (1,2,3,4,2,3), (1,1,2,3,4,4,3,2), (1,3,2,4,3,2).

For each block use repetitions k=3,...,8, retaining only word lengths exceeding 15. There are 35 actual positive braids of lengths 16 through 64. Repetition creates more than one index peak, and the adjacent generators give genuine shared-state interactions rather than merely commuting disconnected factors. Integer permutation-walk DP computes **every coefficient**, rather than sampling rulings or testing a few coefficients. All 35 rows have no holes and pass every log-concavity inequality. For example the four-strand word (1,2,3,2)^4 has b=2 and row

    [5,45,146,218,166,66,13,1].

Thus this actual counter-construction fails to refute the full conjecture. The family was chosen to amplify nonlocal state interactions, but neither its size nor the pattern proves all repetition indices, much less all positive braids. No previously reported n<=6,length<=15 replay is counted. The remaining obligation is an all-word theorem or an actual violating positive braid; the finite receipt is only a new bounded construction result. This counts as one failed actual construction route, not one per block or repetition.

<a id="q2924-a2"></a>
## A2 — strengthen the row to real-rootedness

Try to prove that every normalized ruling polynomial in w=z² has only real nonpositive roots, which would imply the desired row inequalities by Newton's inequalities. This stronger full-target sufficient route fails on an **actual** positive braid found in A1's family. The search witness is shared, but the obligation is different: A1 sought violation of the exact catalog inequalities; A2 requires a stronger root certificate and now has an exact obstruction to that certificate.

For beta=(sigma1 sigma2 sigma3 sigma2)^6 on four strands, the braid permutation has four cycles, so b=4. The normalized row is

    [1,18,177,1110,3711,7105,8361,6292,3076,970,190,21,1].

It is positive and log-concave. Its polynomial P(w) has degree 12. The independent rational Sturm implementation in [check_rulings.py](check_rulings.py) constructs P,P' and successive negative remainders, rescaling each remainder by a positive rational only. The sequence has degrees 12,11,...,0; its final constant proves gcd(P,P')=1. Sign variations at minus infinity and plus infinity are respectively 8 and 4. Hence **exactly four** roots are real, and eight are nonreal. With positive coefficients no real root is nonnegative. No floating root computation is used in the certificate.

This refutes the uniform real-rootedness strengthening for the target class, not Q2924: the actual coefficient row still satisfies the conjecture. A proof must tolerate these nonreal roots or avoid a real-rootedness certificate entirely. Source lookup and the earlier exploratory numerical root proposal are zero attempts; the developed actual-root obstruction and its exact verification constitute this one route. No novelty claim is made.

<a id="q2924-a3"></a>
## A3 — close the statewise log-concavity induction with nonnegative cross terms

Work directly with the source walk transfer, avoiding real-rootedness. If q has a left descent i and p=s_i q, then the new endpoint-q polynomial is

    f'_q(z)=z f_q(z)+f_p(z).                           (3)

The first term is the stay branch at q and the second the swap into q. Align their parity-compressed coefficient rows as a,b. The desired new inequality has exact slack

    (a_j+b_j)²-(a_(j-1)+b_(j-1))(a_(j+1)+b_(j+1))
      = [a_j²-a_(j-1)a_(j+1)] + [b_j²-b_(j-1)b_(j+1)]
        +2a_j b_j-a_(j-1)b_(j+1)-a_(j+1)b_(j-1).     (4)

Try the natural sufficient invariant: every endpoint row is log-concave with no holes, and every transition cross term on the last line is nonnegative. That would prove closure of all rows, including the returning row, at every word length. The new all-word cross-term claim fails on actual, fully legal permutation walks.

Take the four-strand prefix (1,3,2,2,1,1,3,1), append generator2, and use q=(4,3,2,1), p=(4,2,3,1). Exact DP and independent enumeration of all256 switch masks give

    f_q=1+5z²+8z⁴+5z⁶+z⁸,     f_p=2z⁵+z⁷.

The two aligned rows for (3) are

    a=[1,5,8,5,1],   b=[0,0,2,1,0],

both log-concave with no internal zeros. At j=1 the cross term is -2. The actual sum is [1,5,10,6,1], with three closure components, and remains log-concave: the first row's intrinsic slack17 compensates that negative cross term, giving total slack15. Thus a proof requiring nonnegative transition cross terms at every state cannot cover even this actual prefix. This is a failure of the proposed induction invariant, not of the source transition or target row.

For completeness, **statewise log-concavity alone** is also insufficient as an abstract transfer invariant: a=[1,1,1], b=[4,1,0] are individually log-concave and have interval supports, but their sum [5,2,1] fails 2²>=5. They can be parity-aligned as a stay row and swap row with unit leading coefficients and admissible switch-degree bounds; they are not asserted jointly reachable. The actual example above is what independently rules out the stronger nonnegative-cross-term remedy.

The exact remaining obligation is a quantitative estimate tying the *negative* cross term to the two state curvatures in (4), uniformly for every reachable state pair, or a weaker invariant that only closes the returning state. Bounded exploratory endpoint tests do not prove that estimate. This is one worked transfer-induction route; the abstract and actual controls are not two attempts. It differs from A2's stronger root certificate and from a coefficient-pair injection.

<a id="q2924-a4"></a>
## A4 — balance neighboring fibers by one meeting-time suffix exchange

Try a combinatorial injection W_(s-2)×W_(s+2) -> W_s×W_s directly, where W_k is the set of returning walks with k switches. Such an injection would prove each coefficient inequality, while a separate argument would still be required for no holes. The usual path mechanism exchanges the two suffixes at a time when the permutation states agree. The result is always legal: all later transition tests depend only on that state and the prescribed remaining letters.

The numerical condition for balancing is precise. If the prefix switch counts at a common time are u_- and u_+, the exchanged total counts are

    s-2+(u_+-u_-),       s+2-(u_+-u_-).

Both equal s if and only if u_+-u_-=2. Thus a full proof by **one common-state suffix exchange** requires every neighboring pair to have a meeting with prefix difference2. The source walk rules do not guarantee such a meeting.

For the actual four-strand word (1,3,1,3), take the walk making all swaps and the walk staying at every step. Their states are

    low: 4321 -> 4312 -> 3412 -> 3421 -> 4321;
    high:4321 -> 4321 -> 4321 -> 4321 -> 4321.

All swaps are allowed, and every high-path stay is legal at a descent of w0. The respective switch counts are0 and4, so the desired middle count is2. Their only meetings are times0 and4, with prefix differences0 and4. Therefore **no choice of one splice time** balances this pair. Independent mask enumeration gives the normalized row [1,2,1], so the actual target inequality holds; the proposed injection mechanism fails.

One could first commute generators1 and3 to change the word, make multiple cuts, or change states by additional local moves. None is excluded by this example, and each would need a globally defined, invertible rule for every fiber pair. The fixed-word one-splice approach as worked does not provide it. This is an actual path-pair obstruction, separate from A3's algebraic two-row induction. The known short-word coverage is not being recounted as a counter-construction; the new failed sufficient lemma and its exact legal-path witness count once.

<a id="q2924-a5"></a>
## A5 — generate arbitrary positive words by multiplicative one-peak factors

The primary Proposition 5.6 proves a genuine nested one-eye product formula, and Corollary 5.7 uses it to handle every one-peak index sequence. Try to extend that reduction to arbitrary words by cutting them into such factors, multiplying their known log-concave rows, and using convolution closure. This would give a full answer if a composition/factorization lemma justified the multiplication. Ordinary same-strand concatenation does not have the required one-eye decomposition.

Write M_beta(z) for the full permutation-state transfer matrix. Its returning entry F_beta counts raw switches. Matrix multiplication gives

    F_(beta gamma)=sum_q M_beta[w0,q] M_gamma[q,w0].    (7)

Multiplying the two returning entries keeps only q=w0; all other terms are legitimate walks whose **intermediate** permutation is different. They cannot be discarded by the endpoint normalization.

For a genuine adjacent-generator example, beta=gamma=(sigma1 sigma2) on three strands. Both factors are one-peak words, have one component and normalized row [1]. Their concatenation has normalized row [2,1]. The raw returning polynomials are z²,z² and z⁴+2z², respectively. The two missing z² terms come from the walks with switches at positions{1,3} and{2,4}; their states at the cut are231 and312 rather than321. Direct16-mask enumeration verifies the complete polynomial. No monomial normalization can turn the product row [1] into [2,1]. The target holds in all three actual examples.

The information loss has an all-size elementary formula already in the two-strand family: [TWO-STRAND-RESULT](TWO-STRAND-RESULT.md) proves

    F_(a+b)=F_a F_b+F_(a-1) F_(b-1), a,b>=1,

with explicit parity-normalized two-product formula. The extra term is nonzero at every positive split, not an accidental tiny-word discrepancy. For instance normalized rows at exponents1,2,3 are [1],[1,1],[2,1]. Four hundred exact controls agree with the matrix proof. This useful partial does not assert closure of arbitrary sums of log-concave rows.

Thus the attempted universalization of the **source's multiplicative structural reduction** fails: arbitrary one-peak pieces interact through off-diagonal states, beyond the single shared eye in Proposition 5.6. A correct extension must control all terms in (7), or prove a braid-normal-form/nested decomposition applicable to every positive word. Neither was obtained. This differs from A3's local single-letter curvature invariant and A4's walk-pair injection, although their residual tasks all reflect state interactions. The worked all-size defect and the actual adjacent-generator example belong to this one route. No new actual counterexample, impossibility claim or novelty claim is made.

## Stopping disposition

Five full-target routes are now filed, each with its attempted sufficient lemma or construction and exact obstruction/gap. The conjecture remains unresolved. Retain the all-size elementary two-strand proof and composition defect, fresh finite positive-word rows, actual stronger-root obstruction and exact restricted-method witnesses. Checks are evidence for those scopes, not an all-braid theorem. Root accepted the independent mathematics/count review; no sixth route is authorized under the stopping rule.
