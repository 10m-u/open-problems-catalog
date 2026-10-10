# Open problems from doctoral theses and recent papers

A catalog of **3788 open mathematical problems**: conjectures and questions left open in doctoral theses and recent
papers. Each comes with its source, its exact location in that source, a dated literature check, and every result
obtained on it. Problems already solved elsewhere are left out.

| | Count |
|---|---:|
| Problems in the catalog | 3788 |
| Open | 3642 |
| Open, with partial results here | 96 |
| Solved here | 50 (35 proved, 15 disproved) |
| Excluded as solved elsewhere | 12 |
| Automatically extracted thesis statements (unreviewed) | 10001 |

## Where to start

- **[Problems by subject](problems/README.md)**: one page per subject. Each problem has a stable number (Q1–Q3800)
  and an anchor, for example `problems/mathematics/combinatorics-graph-theory.md#q123`.
- **[Index by number](problems/INDEX.md)**: every problem, its subject and status, in blocks of 500.
- **[Solutions](solutions/README.md)**: proofs, counterexamples, partial results, research reports, scripts and
  certificates, grouped by research round. Each problem page links to the results on it.
- **[Thesis statements](statements/README.md)**: 10001 further conjectures and open-problem sentences extracted
  automatically from theses. These are raw candidates, not curated problems.
- **[Sources](sources/README.md)**: every cited document with a link. [`tools/fetch_sources.py`](tools/README.md)
  downloads them for local use.
- **[Data](data/)**: `problems.json` and `problems.csv` (everything on the problem pages), `statements.jsonl.gz`,
  `sources.json` and `excluded.json`.

## What the entries are

- **Statements are concise paraphrases.** They are written to be self-contained, with setup and notation in the
  "Context" paragraph. The cited source and location are authoritative; check them before working on a problem.
- **Literature checks are bounded and dated.** Each problem records a search for later resolutions, with its date.
  A problem listed as open may have been solved since, or in a source the search missed.
- **Provisional entries.** One collection (Q2401–2500) is a provisional recovery draft and is marked as such.

## Status of the results

Results come from several research rounds, and **their evidence differs**. Each solutions folder states its own
level. None of it is peer reviewed. Much of the work was done with AI research assistance:

- Round reports B1–B8, B13 and the 2026-10-05 packet are filed as received from an AI research agent. Their proofs are
  written but were not independently re-derived.
- The B3 continuation adds a human proof review and exact computational controls.
- B9 is preregistered. Its counterexamples are re-verified by separately written checkers, and its proof's lemmas
  are machine-checked.
- `catalog-research` contains written proofs with exact computational checks.
- `round-2026-10-09` contains five proposed affirmative proofs, two counterexamples, two hardness theorems and one partial theorem, with separate internal AI reviews and exact computational controls. The two complexity questions retain partial status because their negative algorithmic consequences are conditional.
- `seven-problems-2026-10-09` contains four proposed complete answers (three affirmative and one nonexistence theorem) and three proved partial results. Each has a separate internal AI review. Reproducible checks combine exact finite controls with supplementary numerical integration; the three unresolved general questions retain partial status.
- `seven-more-2026-10-09` contains two proposed affirmative resolutions, two exact counterexamples and three partial results, each with a separate internal AI review and reproducible exact controls. The general freezing-process and unrestricted Cayley-word questions remain unresolved.

"Solved here" means a result on this repository's own record at the scope stated on the problem page. It does not
mean an independently verified theorem. Reports of errors are welcome.

## What was excluded

**12 numbered problems are excluded** ([list](problems/EXCLUDED.md)), for one of these reasons:
- the problem is resolved in the published literature;
- a resolution is claimed in [openai/math](https://github.com/openai/math);
- a recent preprint reports a closure;
- a corrected edition of the source answered it.

The same rule removed 30 of the automatically extracted thesis statements.

**Source texts are not included.** Most are under copyright. Links are given instead.

## Licence

Everything original in this repository (catalog pages, data files, solution reports and code) is dedicated to
the public domain under [CC0 1.0](LICENSE). The problem statements are quoted or closely paraphrased from the
cited theses and papers; their wording remains with those authors and is included for identification and
reference. CC0 does not extend to it.

Snapshot date: 2026-10-09.
