# Sharp quotiented entropy: reduction and stopping record

Let \(B_t(w)\) be the infimum of the sum of cyclic and Walsh Shannon
entropies, in bits, for unit vectors orthogonal to the cyclic frequencies
with \(v_2(a)\ge w-t\), where \(1\le t<w\). Exact overlap factorization
splits the surviving space into paired unitary blocks of dimensions
\(2^m\), \(t\le m<w\). Denote the sharp entropy sum within block m by b_m.

## An exact direct-sum reduction

Write a unit vector as \(\bigoplus_m\sqrt{\lambda_m}z_m\), with each
\(z_m\) unit and \(\sum\lambda_m=1\). Both bases respect this block
decomposition, so their probability distributions have the same block
weights. The Shannon grouping identity gives
\[
 H_+(z)+H_\oplus(z)=2H(\lambda)+
       \sum_m\lambda_m\bigl(H_+(z_m)+H_\oplus(z_m)\bigr).
\]
It follows, with attainment by a vector in one minimizing block, that
\[
 B_t(w)=\min_{t\le m<w} b_m .
\]
The finite-dimensional minima exist by continuity on compact unit spheres.
This proves that cross-block mixing cannot improve the minimum. It does
**not** prove \(b_m\) is nondecreasing, or that \(B_t(w)=b_t\) at every width.
Equality of measured values across several widths is not that theorem.

Block coherence is
\[
 C_m={1\over2^m\sin(\pi/2^{m+1})},
\]
and decreases with m: \(\sin x/x\) increases as x decreases in
\((0,\pi/2]\), so its reciprocal decreases. The entropy uncertainty
bound therefore yields \(B_t(w)\ge-2\log_2 C_t\). A single character
in the first block supplies the finite upper bound
\[
 B_t(w)\le \sum_{j=2}^{t+1}h(\sin^2(\pi/2^j)).
\]
For t=1 both bounds equal 1, giving the already known exact \(B_1=1\).
The direct-sum reduction is useful for certifying future searches.

## Five failed routes for the full sharp-constant ambition

1. **Character extremizer.** Try to equate the upper bound above with
   the minimum. At t=2 it gives approximately 1.600876, while the
   explicit two-character construction has entropy sum
   \(1+2h(\sin^2(\pi/16))\approx1.466653257\). In the width3
   block, order cyclic frequencies as (1,3,5,7) and take coefficients
   \((\cos(\pi/16),0,i\sin(\pi/16),0)\).
   Digit factorization gives Walsh squared magnitudes
   \(\cos^2(\pi/16)/2\) twice and \(\sin^2(\pi/16)/2\) twice.
   Its cyclic entropy is h and Walsh entropy is 1+h. The same
   block occurs at every width greater than2.
   Direct block optimization independently finds that smaller value.
   A character therefore need not minimize; row entropies alone cannot
   establish the sharp constants.
2. **Extend the two-character formula.** Propose
   \(1+2h(\sin^2(\pi/2^{t+2}))\) for every t. It already disagrees
   with the exact \(B_1=1\). More decisively at t=3 it is about
   1.156348, below the rigorous coherence lower bound
   \(-2\log_2[1/(8\sin(\pi/16))]\), about 1.284.
   Thus the proposed family is impossible; a measured upper bound of
   1.647080 alone would not have disproved it.
3. **Saturate the coherence inequality.** Use the exact maximum overlap
   to claim equality in entropy uncertainty. Its lower bound at t=2
   is about 1.23, below the explicit 1.46665 candidate. The proof of
   the coherence inequality discards information about all the other
   entries and support compatibility. No vector achieving its equality
   conditions for general m was constructed; no matching upper bound
   results. Computing coherence is not a computation of b_m.
4. **Induct on blocks.** Apply the exact direct-sum identity to assert
   width independence and use the first surviving block's optimum.
   This requires a monotonicity theorem \(b_{m+1}\ge b_m\).
   Blocks are different unitary matrices with increasing dimensions,
   not identical copies of the same smaller block. The grouping
   argument only compares a true direct sum; it does not establish
   this inequality for a single larger block. No entropy-preserving
   reduction from its unit sphere to the preceding block was proved.
5. **Numerical global certification.** Optimize complex block vectors
   with nine deterministic seeded starts at each t=1–4, using the
   analytic gradient and normalization on the sphere. Save the actual
   vectors and recomputed entropy sums in VALIDATION.json. This produces
   upper bounds, not global lower bounds: stationarity and agreement of
   restarts do not exclude another basin. Entropy derivatives are
   singular at zero probabilities; a claimed convex/Hessian certificate
   cannot simply cover those strata. No interval or analytic certificate
   covering all complex phases, supports and larger blocks was obtained.

This broader target reaches five full-target failures. Exact B1, the
direct-sum reduction, and bounds are retained. The old inquiry's B2
expression is used as a verified candidate upper bound; numerical agreement
alone is not accepted here as a proof of global minimality. No closed form
or global certificate for all t has been established.

The numerical checker is separate from these mathematical claims. It also
verifies the overlap mixture and fourth moment on every matrix entry through
width8 and the all-ones product maximum through width19. Literature source
for entropy uncertainty: [Maassen and Uffink](https://doi.org/10.1103/PhysRevLett.60.1103).
