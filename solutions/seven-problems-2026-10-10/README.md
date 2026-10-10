# Seven-problem research checkpoint — 2026-10-10

**Draft research packet; not a claim that seven open problems have been solved.**

Base commit: `c2ba59ec148d831bad6fcad332417b01986a242f`.

This checkpoint was requested before completion of the original research-and-integration task. The original local workspace did not survive into the PR-creation session. The mathematical notes below are reconstructed from the accessible records of that work, not represented as a byte-for-byte restoration of the missing files. Original review files, full checker programs, generated certificates, and the uncommitted catalog integration have not been recovered as files.

## Recorded outcomes and their boundaries

| Problem | Recorded outcome | Scope of this packet |
|---|---|---|
| [Q187](Q187.md) | Proposed affirmative proof | Uniform concentration of the fixed-Ferrers rook profile, with an exponential tail and almost-sure strengthening. |
| [Q294](Q294.md) | Proposed affirmative proof | Consistency of the **support-truncated** profile posterior for fixed comparator risk below one half; temperature diverges and is `o(m)`. |
| [Q1013](Q1013.md) | Partial result | Identification for stable causal Gaussian **AR(2)** models with nonzero roots and distinct sampled powers; the general higher-order problem is not resolved. |
| [Q3617](Q3617.md) | Proposed counterexample | A three-variable mask satisfying the combinatorial and series conditions, with a degree-two obstruction over every field. |
| [Q3709](Q3709.md) | Proposed affirmative proof | Submultiplicativity for every integer genus `h >= 1`; no assertion for arbitrary real exponents. |
| [Q3740](Q3740.md) | Published-resolution correction | The recorded source check attributes the closed-range implication to Sebastian Król, BLMS 2011, online 2010. This is not a new result. |
| [Q3778](Q3778.md) | Proposed exact-counting classification | `#P`-completeness under polynomial-time **Turing reductions**, even for connected bipartite simple graphs; not an approximation or sampling result. |

These are proposed conclusions to be reviewed, not independently certified theorem statuses. In particular, finite computational checks do not prove the general mathematical assertions or establish novelty.

## What this PR deliberately does not change

The canonical catalog JSON/CSV, problem pages, indices, exclusion list, and all existing research rounds are left untouched. Q3740 is not silently deleted, and no problem is promoted to a solved status by this checkpoint. Catalog updates require review and a consistent regeneration/validation pass.

## Validation and provenance

[VALIDATION.md](VALIDATION.md) distinguishes checks run for this reconstructed packet from historical checks whose original programs or output files are unavailable. Source references in the seven notes are carried forward from the earlier work. They are not a claim of a new exhaustive literature search during PR creation.

Before a non-draft integration, review the mathematical arguments and source formulations, restore or replace the complete per-problem verifiers and review artifacts, then apply and validate the proposed catalog changes. The partial scope of Q1013 and the existing publication credit for Q3740 must be preserved.
