# B3 research continuation after the interrupted external run

7 October 2026. Programme: **B3, Positivity certificates for counting
sequences**, the 20-question group in the thesis-catalog programme survey.

The continuation has reconstructed and reviewed nine theorem scopes and
three exact obstructions. The most useful results are weighted interval
ultra-log-concavity through nine variables, positivity of the complete
leading 3x3 cycle Hankel block for every integer r>=2, a uniform interpolation
disk theorem through degree five, its all-degree equal-parameter version,
and an exact classification of uncoloured multiset Eulerian multiplicities
(2,b). The retained full questions remain open where these are subcases.

## What was available

This continuation started from the external agent's intermediate progress, which ended after its research phase and before its final audit and report. No continuation report, proofs, certificates or archive came with it.

The source definitions and previous work came from the local initial B3
packet, dated 6 October: a 45-page PDF, 20-question statement ledger, exact
question snapshot, and standalone positivity diagnostic. Its original
larger verification archive was also absent. Its three complete-proof
submissions were Q165, Q166 and Q325; ten questions had partial results and
seven were unresolved. Those are inherited submission categories, not new
catalog closures in this continuation.

Three AI agents worked in parallel on compositions and intervals, Stirling minors, and interpolation. The coordinating agent reconstructed the s-Eulerian arguments, and the interval agent independently reviewed them. The arguments and exact checks are in this folder.

## Results with their exact scope

| ID | Reviewed result | Remaining boundary |
|---|---|---|
| B3C-01 | Every integer-bounded linear interval family on m<=9 binary positions has a weighted rank sequence ULC of order m for all nonnegative real position weights. | Larger crossing families and general cycles remain open. |
| B3C-02 | For every m, the same normalized inequalities hold at indices 1..4 and m−4..m−1 within 1..m−1. | Does not establish the larger-dimensional middle inequalities. |
| B3C-03 | All-dimensional weighted ULC for laminar interval constraints. | Uses published convolution closure; crossing intervals are the next structural target. |
| B3C-04 | Every nonempty minor of the leading cycle Hankel block indexed by 0,1,2 is coefficientwise nonnegative for all integer r>=2. Its determinant has positive coefficients exactly at degrees 2..6. | Universal order-two and arbitrary order-three cycle minors are not proved here. |
| B3C-05 | For independent parameters a_i in [0,1], all interpolation roots satisfy abs(z+1/2)<=n−1/2 for every 1<=n<=5; boundary only at the two endpoint polynomials. Thus R_n=n in these degrees. | The quoted degree-six-to-eight certificates are missing. |
| B3C-06 | The same disk theorem holds in every degree for L(P)(u)=(u+a)^n, with strict interior roots for 0<a<1. | Equal parameters only. |
| B3C-07 | Every nonconstant s-Eulerian polynomial of degree d has some representing vector of length <=2d−1. | Universal sharpness for (1+ux)^d is not recovered. |
| B3C-08 | A nonunit s-Eulerian degree-two block has coefficients 1+h1*x+h2*x^2 with h1>h2>0. | This is not an all-degree simple-root theorem. |
| B3C-09 | For every positive integer b, 1+2b*x+binom(b,2)*x^2 is s-Eulerian iff b=2 or b(b+1)/2 is a square. | Exact uncoloured (2,b) subfamily; general coloured Q1262 remains open. |

The first two and fifth results have exact computer-assisted proof components.
Their finite computations are exhaustive over the mathematical objects
specified, and their written reductions supply the all-weight or
all-parameter quantifiers. The other infinite conclusions rest on their
displayed structural arguments, with finite controls checking calculations.
No publication novelty or proof-assistant verification is claimed.

Full definitions and proofs are in [the interval report](compositions/REPORT.md),
[the Stirling report](stirling/REPORT.md), [the interpolation report](interpolation/REPORT.md),
and [the Eulerian report](audit/eulerian-report.md). The coordinating
[proof review](audit/PROOF-REVIEW.md) records dependencies, quantifiers, and
the independent Eulerian review. [RESULTS.json](RESULTS.json) gives each
statement, stable catalog targets, evidence files, and limits.

## Obstructions that survived review

Three stronger routes fail, without refuting the underlying research targets:

- **B3C-10, one-bit matching.** In dimension six, impose
  x1+x2=x2+x3=x4+x5=x5+x6=1. The feasible words have ranks 2,3,3,4, but the
  rank-two word has no feasible rank-three superset. Central APP still holds.
- **B3C-11, coefficientwise ULC.** The unrestricted two-variable defect is
  w1^2−2w1*w2+w2^2. Its mixed coefficient is negative, while numerical
  nonnegativity holds for every real weight vector.
- **B3C-12, arbitrary shift mixtures.** The degree-four polynomial
  binom(z,4)+binom(z+4,4) violates the centered disk. It lies outside the
  sampled-value TP class, so it is not a Q1442 counterexample.

The separate known subset-family order-three obstruction was reproduced as
a scope control: at r=3 the minor with I=(1,2,3), J=(0,1,2) has coefficient
−16 at x^5. It does not refute the cycle question Q1160.

One audit correction was necessary: E_(2,6,3)=1+19x+16x^2. The first local
draft listed 1+18x+17x^2. An independent hand count and literal enumeration
found the error; the corrected inequality and (2,b) classification still
hold. The check now explicitly asserts this exceptional row.

## Recovery of the quoted progress

| Lead | Current disposition |
|---|---|
| L1, every order-two Hankel minor in both families | Proof not recovered. 23,328 exact finite controls pass; they do not prove the universal statement. |
| L2, first order-three cycle determinant | Reconstructed for all r>=2, strengthened to all minors of its leading block. |
| L3–L4, interpolation through degree eight | Reconstructed uniformly through degree five, including centered disk and boundary classification. Degrees six through eight are pending. |
| L5, repeated-parameter interpolation in all degrees | Reconstructed with a tridiagonal-matrix proof and a quantitative stronger bound. |
| L6, positive interpolation determinants | Precise coefficient conjecture saved; exact certificates through degree five. |
| L7–L8, central interval reduction and weighted ULC through nine variables | Reconstructed, independently checked, with additional all-size endpoint and laminar consequences. |
| L9, Schur counterexamples and matching obstruction | A precise matching obstruction is proved. Neither historical Schur statement was supplied; no Schur refutation is asserted. |
| L10–L11, quadratic classification and representation bound | Reconstructed and independently reviewed, with the coefficient correction above. |
| L12–L13, sharpness and simple negative roots in every nonunit block | Unverified recovery leads; not used by the accepted arguments. |

## Statement ledger and research directions

B3_statement_ledger.json contains all 20 exact
questions and stable statement IDs, preserving the initial status categories
and distinguishing inherited results from new scopes. The four main
catalog questions advanced are Q164, Q1160, Q1262 and Q1442. Q165/Q166/Q325
retain their initial proof-submission review status. There are no new full
question closures and no canonical resolution-ledger edits.

[NEW-QUESTIONS.md](NEW-QUESTIONS.md) and its JSON register separate precise
conjectures from missing-proof recovery. They use research-local IDs, without
adding global catalog numbers. The next structural directions are:

1. Prove the central symmetric linear-interval inequality
   q*c_q >= (q+1)*c_(q−1) for every q, concentrating on crossing intervals
   and nonlocal prefix-height exchanges. Laminar systems are handled;
   single-bit inclusion matching is obstructed.
2. Recover the universal Hankel TN2 argument or prove its equivalent
   adjacent fixed-sum inequalities for both families. For the cycle
   order-three question, start with the shifted block I=J=(1,2,3).
3. Find a structural positive expansion of the interpolation Hurwitz
   determinants, respecting independent parameters. Recovering the missing
   degree-six-to-eight certificates would restore the quoted cutoff, while
   a general expansion would settle the stronger disk target in all degrees.
4. Audit strict interlacing for nonunit s-Eulerian blocks. A simple-root
   theorem could force repeated linear factors into separate blocks and
   establish the sharpness of the 2d−1 representation bound.

These are proposed directions for the next bounded research round. This
checkpoint does not launch indefinite cutoff expansion or resume unrelated
waiting work. This round develops exact positivity evidence and submits nothing to OEIS.

## Verification and external-agent package

Run `python3 run_all.py` in this directory with Python 3.10+ and SymPy.
The local run used SymPy 1.14.0. It regenerates all mathematical certificates
without network access or model calls.
Only the packet's generated check files are rewritten.

Saved validation includes:

- Complete interval closures: 2,16,377,32,554 families in dimensions 2,4,6,8,
  reproduced with two distinct closure algorithms and identical hashes.
- Interpolation: all 4,816 positive coefficient entries for n=2..5;
  symbolic repeated-parameter recurrence controls; 80 exact original-P
  transform checks and 40 independently evaluated certificate checks.
- Stirling: 880 recurrence/assembly entries, 33 parameter controls for the
  principal determinant, 198 leading-block minor controls, symbolic
  determinant identities, and 23,328 finite order-two minors.
- Eulerian: 780 literal/refined-vector comparisons, 1,331 triple controls,
  exact exceptional rows, family formulas, contractions, multiset formulas,
  and complete volume-factorization recognition at b=1..20.

The ZIP includes these reports, scripts, certificates, exact question
snapshot, original B3 PDF and ledger, and the original standalone handoff.
`START-HERE.md` supplies the external entry point. SHA-256 manifest verification
is available before running the scripts. Absent artifacts are listed plainly;
the ZIP does not reconstruct the remote archive by implication.

BASELINE.json and VALIDATION.json record
source preservation and integration checks. All previous 159 result routes
are retained, with 12 new source-labelled B3 continuation records. The
classification grades and B-series membership remain unchanged.
