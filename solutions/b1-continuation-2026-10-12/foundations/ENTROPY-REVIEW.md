# Independent entropy review

12 October 2026. Reviewed `../fourier/ENTROPY.md`, the corresponding
matrix/entropy code, and the saved vectors in `../fourier/VALIDATION.json`.
The direct-sum reduction and both coherence/character bounds pass.

The surviving cyclic subspaces are paired with disjoint Walsh subspaces by
the exact zero pattern. A block vector therefore has the same squared
norm in either basis. Shannon grouping applied twice gives precisely
\(2H(\lambda)+\sum_m\lambda_m[H_+(z_m)+H_\oplus(z_m)]\).
Its lower bound is the smallest block minimum; placing the vector in a
minimizing block attains that minimum. Existence follows from continuity
of entropy on the compact complex unit sphere, including zero coordinates.
This proves \(B_t(w)=\min_{t\leq m<w}b_m\), with no assumption on
monotonicity of \(b_m\).

The stated \(C_m\) is the maximum entry of each unitary block and decreases
with \(m\). Thus the [Maassen–Uffink
bound](https://doi.org/10.1103/PhysRevLett.60.1103) gives
\(B_t(w)\geq-2\log_2 C_t\). The first-block character's probabilities
factor into independent binary choices, giving the displayed sum of binary
entropies. For \(t=1\), both bounds are exactly one.

The explicit two-character vector for \(t=2\) has the claimed two pairs
of Walsh probabilities and entropy \(1+2h(\sin^2(\pi/16))\). It is
strictly below the character value. The proposed extension at \(t=3\)
violates the rigorous coherence lower bound, so that failed route has a
conclusive obstruction. Neither that vector nor numerical agreement is
a proof that it minimizes the entire block. Similarly, a gap between
coherence's lower bound and a known upper bound does not prove coherence
cannot be attained; that route is correctly stopped at its missing equality
construction. The width-induction route lacks exactly the stated block
monotonicity theorem. Numerical restarts provide candidate values without
a covering global lower certificate. Those five objectives are distinct
failed full-sharp-constant routes, not five impossibility results.

`check_root_reviews.py` independently constructs direct Fourier overlap
matrices through width six, checks paired blocks and coherence, evaluates
mixed-block Shannon identities, recomputes the saved candidate entropies,
and checks the explicit \(t=2\) vector. These are bounded controls plus
an algebraic review; no new optimization or global-minimum claim is made.
