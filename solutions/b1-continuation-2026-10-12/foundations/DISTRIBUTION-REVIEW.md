# Independent review of the finite overlap law

Reviewed `../fourier/DISTRIBUTION.md` on 12 October 2026. The finite law,
zero count, second and fourth moments, and displayed moment tail bounds
pass mathematical review for integer widths \(w\geq1\).

For nonzero row \(a=2^{w-m-1}d\), with \(d\) odd, the factor at
denominator two forces the designated mask bit, all larger-position mask
bits are forced zero, and the other \(m\) bits independently select sine
or cosine. Thus the block contains \(4^m\) nonzero entries out of
\(4^w\). Row zero contributes only its one unit entry. This verifies all
mixture weights and multiplicities, including the two unit entries when
\(w=1\).

For the fourth moment, each row's sum over masks is the product of
\(\sin^4+\cos^4=(3+\cos4\theta)/4\). The denominator-two factor equals
one. Every nonconstant term in the other factors has a nonzero signed
binary frequency of absolute value below \(2^w\), so the finite row
average vanishes. The **mean** row sum is \((3/4)^{w-1}\); its total is
\(2^w(3/4)^{w-1}\), and division by \(4^w\) gives
\((4/3)(3/8)^w\). Markov and Paley–Zygmund then give the stated bounds.
The fourth-moment formula does not apply to width zero, whose matrix is
the one-by-one identity; the report should state its positive-width scope.

The five tail routes are not independently audited for stopping-count
purposes here. In particular, row \(d=1\) has variance on the order of
\(m^3\) for its logarithmic mask sum, but its largest centered summand is
only order \(m\). This does **not** itself violate Lindeberg: their ratio
is order \(m^{-1/2}\). It does show why a single row-independent
normalization needs justification. The report correctly frames that route
as an unproved uniformity and rare-tail step, rather than a proof that no
conditional central limit theorem exists.

The review checker `check_distribution_review.py` independently builds
the matrix by direct Fourier summation for widths 1–7 and compares the
entire finite multiset to the block mixture and both moments. Its receipt
is `DISTRIBUTION-REVIEW-CHECK-RESULTS.json`. These finite checks support the
algebraic review; they do not establish a sharp growing-width tail law.
