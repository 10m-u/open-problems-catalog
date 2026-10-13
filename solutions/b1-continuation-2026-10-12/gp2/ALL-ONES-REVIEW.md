# Independent review of the all-ones Walsh/Fourier maximum

2026-10-12. Reviewed `../fourier/ALL-ONES.md` as the retained independent agent. The finite-horizon proof passes at the exact stated scope: the normalized all-ones Walsh column, every width w≥1, with an explicit maximizing frequency and its reflection. This is an internal mathematical review, not an external-review or novelty claim.

The digit factorization is correct: writing x in binary factors the normalized Fourier sum into w factors `(1−exp(−2πia·2^k/2^w))/2`. Their magnitudes give `∏_{j=1}^w |sin(πa/2^j)|`. Every even a has a zero first factor. For odd a the folded t_j lie in [0,1/2], start at 1/2 and satisfy `t_{j+1}∈{t_j/2,(1−t_j)/2}`. Conversely, each such finite path ends at an odd numerator over 2^w, and doubling/folding recovers its preceding points. It therefore corresponds to a genuine odd Fourier frequency. At width 1 the two reflected frequencies coincide, which is harmless.

For the comparison of the two branches set u=(1−t)/2 and v=t/2. Their ranges and order are correct. Writing s=sin(πt/2),

    f(t)=2s(1−s²),
    f'(t)=π cos(πt/2)(1−3 sin²(πt/2)).

Thus f has a unique maximum at the displayed t_* and is increasing on [0,3/8]. The claimed strict bounds 3/8<t_*<1/2 can be checked exactly: `sin²(3π/16)<1/3<sin²(π/4)`. For the first inequality use `cos(3π/8)=sqrt(2−sqrt2)/2>1/3`; squaring the positive quantities reduces this to `sqrt2<14/9`, which holds. The endpoint comparison is also exact:

    f(1/2)² = 1/2 > (2+sqrt2)/8 = f(1/4)².

Unimodality therefore implies f(u)≥f(1/4)≥f(v). This includes t=0 and t=1/2 without division by a potentially zero factor.

The later pair comparison is valid. Both g²(u) and g²(v) lie in [1/4,3/8]; that interval is invariant under g. The map g decreases, so its even iterates preserve the initial u≥v order. Pair products beginning at even iterates are evaluated by f on its increasing interval. Each such pair favors the u orbit, and an odd final factor starts at another even iterate and favors u because sin(πt) increases on [0,1/2]. The horizon-one case uses this last fact directly. Hence **entire** greedy continuations, not merely their first factors, are correctly compared.

A precise induction can be written as

    V_1(t)=sin(πt),
    V_h(t)=sin(πt)·max{V_{h−1}(t/2),V_{h−1}(g(t))}.

For every starting t, replace the two tails by their greedy values using the induction hypothesis, then apply the proved continuation comparison. This establishes greedy optimality for every finite horizon. Solving the affine recurrence gives `q_j=1/3+(-1)^{j−1}/(3·2^j)` and the proposed odd integer frequency. No uniqueness assertion about maximizers is needed.

The exponential estimate also passes. All q_j lie in [1/4,1/2], where the derivative of log sin(πt) is bounded in absolute value by π. The log of each factor divided by sqrt3/2 is therefore bounded by `π/(3·2^j)`, so the infinite product converges absolutely to a finite positive K. Its tail logarithm has absolute value at most `(π/3)·2^{-w}`, directly giving the claimed relative error `1+O(2^{-w})`. Multiplying by 2^w recovers the unnormalized maximum.

The separate checker `check_all_ones_review.py` compares direct finite Fourier sums with the factorization, exhausts small-width frequencies, and compares the greedy orbit against an independent finite-horizon dynamic program over rational starting points. Receipt: `ALL-ONES-REVIEW-CHECK-RESULTS.json`. These bounded computations support the audit; the exact pair comparison above supplies the all-size argument.

This review addresses the finite all-ones-column maximum and its asymptotic rate only. It does not claim that the maximizing frequencies are the only ones, establish a new literature result, or answer a different optimization problem over arbitrary Walsh masks.
