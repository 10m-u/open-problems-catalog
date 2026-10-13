# B14 — Third research round

**October 12, 2026.** The principal new result is the sharp exponential rate

\[
\lim_{n\to\infty}\left(\frac{\mathbb E M_n}{\sqrt{n!}}\right)^{1/n}
=0.597586978551345\ldots
\]

for Q3818/P5, with a matching exponential lower bound and a proof that
\(\mathbb E M_n=O((3/5)^n\sqrt{n!})\). The same rate holds for fixed independent
edge-cost distributions with a finite positive density at their finite lower
endpoint. It does not apply to dependent shortest-path metric distances.

Read **REPORT.pdf** or **REPORT.md** for the full proof, source distinction,
finite bounds, transfer theorem, scope limits, and verification record.

This is a proof developed in this continuation, not externally peer-reviewed
or formally verified. Novelty relative to the supplied handoff is clear;
priority in the wider literature is not established. No catalog or original
attachment was changed.

## Reproduce the new exact checks

From this directory, using Python 3.10 or later:

```sh
python checks/check_sharp_rate.py
```

No third-party package is needed. The output is
`checks/EXACT-CHECK-RESULTS.json`.

For the deterministic numerical evaluations, the supplied run used
mpmath 1.3.0:

```sh
python -m pip install 'mpmath==1.3.0'
python checks/evaluate_bounds.py
```

These numerical outputs are evaluations of proved bounds, not sampled
counts or directed-rounding certificates. The rational proof of the base
3/5 is in the exact checker and does not depend on mpmath.

## Replicate the selected predecessor checks

Supply the path to the original handoff ZIP:

```sh
python replicate_handoff.py --zip '/path/to/B14-complete-handoff-2026-10-12.zip'
```

This validates all 614 manifested payloads, extracts a temporary copy, and
runs four bounded checkers. The original ZIP remains read-only. The script
never runs catalog-filing commands. Per-check timeouts default to 60 seconds.
The results are written to `replication/REPLICATION-RESULTS.json` and the
associated logs and recomputed receipts.

## Files

`REPORT.md` and `REPORT.pdf` contain the mathematical result. `checks/`
contains the new source code and complete check receipts. `replication/`
contains the four replicated receipts and execution logs. `sources/`
contains exact copies of the predecessor count proof, its review, and the
handoff overview, with provenance hashes. `RESULTS.json` records the scope
of each contribution; `MANIFEST.json` records this packet's file hashes.

The all-size theorem is the written proof, not an extrapolation from the
finite computations. No general TSP algorithm, metric approximation bound,
search-runtime improvement, or high-probability count concentration is claimed.

## Rebuild the PDF

The supplied PDF was built with Pandoc and pdfLaTeX:

```sh
pandoc REPORT.md --from markdown --standalone --pdf-engine=pdflatex \
  -V fontfamily=mathpazo -V fontfamilyoptions=sc -V urlstyle=same \
  -H pdf-header.tex -o REPORT.pdf
```
