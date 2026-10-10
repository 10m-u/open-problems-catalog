# Validation and recovery record

Date: 2026-10-10.

Pull request: [Research checkpoint #4](https://github.com/10m-u/open-problems-catalog/pull/4).

Base commit: `c2ba59ec148d831bad6fcad332417b01986a242f`.

Branch: `research/seven-problems-2026-10-10`.

## Included material

The checkpoint contains a [scope summary](README.md) and seven reconstructed mathematical notes: [Q187](Q187.md), [Q294](Q294.md), [Q1013](Q1013.md), [Q3617](Q3617.md), [Q3709](Q3709.md), [Q3740](Q3740.md), and [Q3778](Q3778.md). This validation record completes the packet.

The original uncommitted workspace was unavailable in the session that created the PR. The notes were reconstructed from accessible records of the earlier research, including displayed mathematical arguments. They are not represented as byte-for-byte restorations of the original files. Source references were carried forward from those records; no new exhaustive literature search is claimed.

## Checks performed during PR creation

GitHub confirmed the checkpoint branch and each committed note. A read of the PR's changed-file list after the seven notes were committed showed those seven Markdown files and the packet README, with no changes outside `solutions/seven-problems-2026-10-10/`. This record is an additional file in that same folder.

These are publication and scope checks, not proof checks. No mathematical verifier, repository-wide test suite, catalog exporter, or catalog-integration validator was executed against the reconstructed packet. No external-link availability audit, formal proof-assistant verification, or external peer review is claimed. A local clone attempt failed because the execution environment could not resolve GitHub; the GitHub connector was used for the actual branch, commits, and PR.

The canonical JSON/CSV, problem pages, indices, exclusions, and earlier research folders are not intentionally modified by this checkpoint. No merge or automatic merge has been requested.

## Historical checks not reproduced here

The earlier research records describe the following computational controls. Their original programs, output certificates, and separate review artifacts have **not** been recovered as files in this PR, and these checks have **not** been rerun on the reconstructed text.

| Problem | Controls described in the earlier record | Current status |
|---|---|---|
| Q187 | Small Ferrers-board enumeration; swap legality and bijectivity; antidiagonal unit-change bounds; exact dilation marginals. | Unreproduced; no checker or certificate included. |
| Q294 | Exact finite-model posterior calculations and a complementary-classifier control distinguishing support truncation from an untruncated density. | Unreproduced; no checker or certificate included. |
| Q1013 | Exact real-root and algebraic alias checks, including a zero-lag-one covariance example. | Unreproduced; no checker or certificate included. |
| Q3617 | Exhaustive mask-axiom checks, formal-series recurrences, and a finite-field quadratic-space search. | Unreproduced; no checker or certificate included. |
| Q3709 | Exact finite character-degree and central-sector comparisons. | Unreproduced; no checker or certificate included. |
| Q3740 | Exact operator-polynomial identities, a periodic-kernel control, and a converse example. | Unreproduced; no checker or certificate included. |
| Q3778 | Independent small-graph partition counts, subdivision-polynomial checks, and exact interpolation on paths and cycles. | Unreproduced; no checker or certificate included. |

Historical reports of successful checks are not converted into passing test results for this PR. Finite checks would not, by themselves, prove the general results or establish novelty even after reproduction.

## Scope limitations that must survive review

Q1013 remains a partial AR(2) result, with stable-causal, nonzero-root, and distinct-sampled-power assumptions. The general higher-order conjecture is not resolved by that note.

Q294 concerns the **support-truncated** profile posterior, with fixed comparator risk strictly below one half. It does not cover the untruncated or mean-error-only formulations or the separate integrated-Bayesian comparison.

Q3709 is restricted to integer genus `h>=1`. Q3778 concerns exact counting under polynomial-time Turing reductions, not approximation or sampling.

Q3740 is a proposed published-resolution correction, credited to Król (2010/2011), not a new theorem. The previous investigation inspected publisher abstract and metadata, not the paid full text. Its bibliographic attribution should be rechecked before any exclusion is applied.

## Remaining requirements before catalog integration

Review each reconstructed argument against the precise source statement and verify the external inputs, including the dilation identity for Q187, the multiplier/Clifford conventions for Q3709, and the hardness input for Q3778. Restore or replace the missing verifiers, execute them, and commit their actual reproducible outputs. Obtain mathematical review without presenting an internal review as external peer review.

Only then prepare consistent catalog data, page, index, and exclusion changes and run the repository's regeneration and validation workflow. This checkpoint does not contain the original uncommitted catalog integration and does not promote any problem to a solved status.
