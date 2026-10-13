# B2 continuation III — 13 October 2026

## New results

The main manuscript is `RESEARCH-NOTE.pdf` (nine pages), with editable source
`RESEARCH-NOTE.tex`. Complete written proofs establish:

1. **Maximum-flat fibre rigidity and occupied-fibre inheritance** (Theorems 2.2–2.3).
   In an admissible two-colour partition of F_3^n, quotient along the direction
   of an affine subspace of maximum dimension contained in the remainder.
   All but at most one nonfull fibre have a monochromatic affine coloured
   complement. The set of occupied remainder fibres inherits admissibility.
2. **The sharp three-dimensional plane threshold** (Theorem 3.3).
   A plane-free admissible two-colour remainder in F_3^3 has at most 16 points,
   and a 16-point example is given.
3. **The all-dimension plane-free bound** (Theorem 4.1).
   For n >= 3, |R| <= (5/2) 2^n - 4. Consequently density at least 1/10 forces
   an affine plane for n >= 8. The latter dimension threshold is not claimed sharp.
4. **Entropy tail exponent rigidity** (Theorem 5.3).
   For a law with full support on the nonnegative integers and
   -log p_n = c n^beta + o(n^beta), stationarity under finite-coordinate mass
   transfers at ratio rho > 1 requires beta = log_2(4 rho/(1+rho)).
   The proof also gives explicit ascent directions when this relation fails.
5. **Universality and nonattainment for prescribed tail classes**
   (Theorem 6.1 and Corollary 6.2). Every fixed positive tail exponent and
   coefficient define a full-support class whose supremum equals the global
   entropy-ratio supremum. In particular, the one-sided Gaussian-tail class
   has that supremum but no maximizer.

The known entropy interval **1.4051810329 < C_* <= 2** is unchanged.
The preceding general midpoint bound **O(k log(2k))** is unchanged.
Neither catalog target is solved. These are advances relative to the supplied
research record, with no worldwide-priority, external-peer-review, or
proof-assistant-verification claim.

## Reproduce the finite checks

Python 3.10 or newer, standard library only:

```bash
python verify_midpoint.py
python verify_entropy_variation.py
```

The programs regenerate `MIDPOINT-CHECKS.json` and
`ENTROPY-VARIATION-CHECKS.json`. `VERIFICATION-LOG.txt` records the executed
checks under Python 3.13.5. The manuscript proves the general theorems;
finite enumeration is not presented as an all-dimension or infinite-tail proof.

`rational_entropy.py` retains the exact rational logarithm and entropy
arithmetic from continuation II. Its ninety-term positive atanh series,
rigorous tail bound, and outward rounding certify the finite diagnostic
mass-transfer ascent. That diagnostic is not a new lower bound on C_*.

To compile the manuscript, run `pdflatex RESEARCH-NOTE.tex` twice, or use
`latexmk -pdf RESEARCH-NOTE.tex`. Build products are not needed to run the tests.

## Record structure

- `RESULTS.json`: scoped result statements and proof locations.
- `PROVENANCE.json`: input hashes, source locations, and retained source correction.
- `SOURCES.md`: primary-source attribution and the distinction between old and new results.
- `AUDIT-NOTES.md`: proof-sensitive hypotheses and failed routes.
- `BASELINE-TARGETS.json`: preserved baseline catalog records, **not** the latest
  result summary. Their original labels and lower bounds are intentionally unchanged.
- `baseline/ENTROPY-CERTIFICATE.json`: unchanged continuation-II lower-bound receipt.
- `baseline/certify_entropy.py`: unchanged exact verifier for that prior receipt.
- `exploratory/`: a time-limited mixed-integer search, not part of any proof.
- `MANIFEST.sha256`: file-integrity hashes, excluding the manifest itself.

The original handoff, its other 79 targets, and all previous attempt counters
are unchanged. New result records are separate; they do not increment or
retroactively recategorize the earlier catalog attempts.
