# B2 continuation II — further results

**Date:** 13 October 2026. **Targets:** Q4296 and Q4660.

The main document is **RESEARCH-NOTE.pdf** (with editable LaTeX source). It contains complete proofs of the scoped statements below, the exact witness specification, and the distinction between proof, exact finite calculation, and exploration. Worldwide priority is not established. No external peer review or proof-assistant verification is claimed.

## Main results

**Two-colour classification, all dimensions.** An admissible two-colour remainder in F_3^n that contains no affine line is empty, a singleton, two points, or a four-point affine parallelogram. An elementary affine-plane incidence proof establishes the classification; it does not rely on a solver or on enumerating all ambient dimensions. See Theorem 2.1.

**Parallel maximal-subspace rigidity.** The full fibres of any quotient inherit an admissible colouring. For two colours, if the largest affine dimension of the remainder is d, there are exactly 1, 2, or 4 parallel d-flats in every direction in which a maximal flat occurs. Four such flats have parallelogram quotient structure. See Lemma 3.1 and Corollary 3.2.

**Exact initial values and stronger obstruction.** For the density-1/10 target, f(1,2)=f(2,2)=f(3,2)=0 and f(4,2)=1. Colour-reusing ambient extension gives, for k>=2 and n>=k ceil(log_3(10k))+2, admissible examples whose largest affine subspace has dimension exactly n-k-2. See Corollary 3.3 and Proposition 3.4.

**Entropy support-boundary theorem.** For P_epsilon=(1-epsilon)P+epsilon delta_z, the coefficient of epsilon log(1/epsilon) in the ratio change is

    [2 u_minus(z) - 1 - rho(P)(2 u_plus(z) - 1)] / Delta_plus(P),

where u_plus and u_minus are the escaping masses into previously unoccupied sum and difference outputs. For rho>1, every positive leading direction belongs to (A+A-A)\A, so there are at most |A|^3 candidate atom locations. See Theorem 4.1 and Corollary 4.2.

**Two classes of finite entropy candidates are not globally extremal.** A finite law with rho>1 is not globally optimal if it fully occupies an arithmetic progression, or if either support endpoint carries at least half the mass. The AP result holds regardless of the endpoint masses; one adjacent endpoint always gives ascent. The finite boundary screen is necessary only: the uniform law on {0,1,4} passes every leading test and is nevertheless far from the best known witness in this package. See Corollaries 4.3–4.4 and Remark 4.5.

**Exact improved witness.** A twelve-point rational law proves

    C_* > 1.4051810329,

with its actual ratio rigorously enclosed between

    1.4051810329220149462009831947934829507300
    1.4051810329220149462009831947934829507301.

See Proposition 5.1 and ENTROPY-CERTIFICATE.json. The improvement over the preceding eight-point witness is about 6.68464e-8, not a major narrowing of the universal range.

## Reproduce the proof controls

Python 3.10 or newer, standard library only:

```bash
python verify_all.py
```

The three constituent commands are:

```bash
python certify_entropy.py
python verify_midpoint.py
python verify_entropy_boundary.py
```

Run without Python's `-O` flag: the programs use assertions as verification checks. The JSON receipts are deterministic; VERIFICATION.log records a successful run. Entropy calculations use exact fractions, not floating-point logarithms.

The entropy certifier accepts an optional integer support vector, so sparse-support laws can also be certified. The reusable `boundary_report(support, weights)` function in `verify_entropy_boundary.py` computes rigorous coefficient intervals at every candidate new atom, reports positive, negative, or undetermined signs, and never treats passing the screen as a global optimality certificate. BOUNDARY-CHECKS.json includes the full twelve-point and {0,1,4} reports and an exact five-to-six-point ascent.

The midpoint program checks all 512 plane subsets, all 39 planes of F_3^3, the point/pair/triple incidence identities, all 19,683 two-colour labelled plane partitions, and 23,196 quotient colour assignments. These are finite controls on the manuscript's general proofs, not substitutes for them.

## Source correction and unresolved scope

Q4660's catalog label “Conjecture 1.10” points to a different statement. Li's actual Conjecture 1.10 is sum–product; Q4660's stated sum–difference sharpness question occurs in Section 8. SOURCES.md and PROVENANCE.json record this correction separately without editing the input record.

The prior general O(k log(2k)) upper codimension theorem remains the best general guarantee established in this continuation. The logarithmic gap has not been removed. The universal entropy upper bound remains 2; no global optimum and no sharpness proof are supplied. No result here settles the separate sum–product conjecture. The full Q4296 and Q4660 statuses remain partial, and the other 79 targets and earlier attempt counters are untouched.

## Package contents

- RESEARCH-NOTE.pdf / .tex: complete mathematical manuscript.
- certify_entropy.py / ENTROPY-CERTIFICATE.json: exact entropy lower bound and prior-witness control.
- verify_midpoint.py / MIDPOINT-CHECKS.json: finite incidence, quotient, construction, and negative controls.
- verify_entropy_boundary.py / BOUNDARY-CHECKS.json: exact support-mass checks, complete boundary screens, and concrete ascent.
- verify_all.py / VERIFICATION.log: one-command verification and run receipt.
- RESULTS.json: scoped result records, with the full targets left partial.
- BASELINE-TARGETS.json / PROVENANCE.json / SOURCES.md: unchanged target records, input hashes, source locations, and attribution limits.
- exploratory/: numerical discovery and solver logs, explicitly not global certificates.
- MANIFEST.json: SHA-256 hashes of the other delivered files.

The optional exploratory programs require NumPy and SciPy, and some are time-limited. Their output is not part of the exact proof. Rebuilding the PDF requires a standard LaTeX installation; run `pdflatex RESEARCH-NOTE.tex` twice.
