# B2 new results — 13 October 2026

The main result is a complete written proof that every admissible midpoint
partition of F_3^n with k colours and remainder density at least 1/10 contains
an affine subspace of codimension O(k log(2k)). The primary source proves
O(k^2). The proof extends to every fixed odd prime p and to starting density
alpha > 0, with codimension O_p(k[log(2k) + log(1/alpha)]).

The second result is an exact entropy certificate: an eight-point rational
law has entropy-increment ratio in

    (1.4051809660756335725451283471012647256861,
     1.4051809660756335725451283471012647256862).

Consequently, the least universal sum–difference constant exceeds 1.40518.
This improves the handoff's witness near 1.3977846, not a verified
literature-wide record. A simpler five-point law already exceeds 1.405.

## Read first

`RESEARCH-NOTE.pdf` contains the statements, all-dimension proofs, explicit
lower construction, entropy certificates, verification scopes, and references.
`RESEARCH-NOTE.tex` is its editable mathematical source.

The pivotal new proof step is a weighted quotient-avoidance lemma. A colour
covered by M cosets can be removed at codimension s while multiplying any
nonnegative cost's average by at most 1/(1-M p^(-s)). Choosing the failure
probability at most 1/(2k) keeps total coloured-density growth below a factor
of two across k removals. Established polynomial Freiman–Ruzsa covering then
makes the requisite density threshold polynomial, rather than exponential,
in k.

An explicit block-zero construction has remainder density at least 9/10
and largest affine-subspace dimension exactly n-k when
n >= k ceil(log_p(10k)). This leaves a logarithmic factor between the new
general upper bound on necessary codimension and the constructive lower bound.

## Reproduce the exact checks

Use Python 3.10 or later; the three verification scripts need only the
standard library. Run them from this directory:

```sh
python certify_entropy.py
python check_midpoint_lemmas.py
python check_block_construction.py
```

They recreate `ENTROPY-CERTIFICATE.json`, `MIDPOINT-CHECKS.json`, and
`BLOCK-CONSTRUCTION-CHECKS.json`. All certificate comparisons use integers
or rational fractions. The checks do not independently verify the external
PFR theorem or substitute for the written general proof.

`explore_entropy.py` is optional numerical discovery code requiring NumPy
and SciPy. Its local optima are not global claims, and it is not needed to
verify either certified law.

To rebuild the manuscript with a LaTeX installation containing the packages
listed in the source, run twice:

```sh
pdflatex -interaction=nonstopmode -halt-on-error RESEARCH-NOTE.tex
```

## Scope and provenance

Q4296 and Q4660 retain **partial-progress** status: the exact extremal
function and sharp universal entropy constant are not determined.
The other 79 catalog targets are unchanged. No earlier failed-attempt
counter is reset, and no original catalog file is modified.

`BASELINE-TARGETS.json` preserves the two supplied catalog records.
`PROVENANCE.json` records exact original paths and SHA-256 hashes.
`RESULTS.json` contains scoped continuation records suitable for review
before any catalog integration. `SOURCES.md` records the primary literature.
`MANIFEST.json` hashes every other deliverable in this package.

The new mathematical derivations have not received external peer review or
formal proof-assistant verification. Novelty is established relative to the
supplied handoff and checked source statements, not against all literature.
