# Analysis results, 9 October 2026

This subpacket addresses two exact catalog questions. The directory name reflects the original subject assignment; both selected questions are in functional analysis.

| Target | Result | Scope | Evidence |
|---|---|---|---|
| Q3236 | Proposed affirmative full proof: the actual sum quasinorm has the exact Fatou property and is rearrangement invariant. | All sigma-finite resonant spaces and all parent quasinorms in the source's definition. | [Complete proof](Q3236-proof.md), including distribution compactness, geometric-bin realization, an atomic argument, and an example of non-attainment. |
| Q3454 | Quantitative partial theorem under pairwise commutation of corresponding support projections. | Removes the ultrahermitian assumption from the stated commuting-support result; arbitrary noncommuting supports remain untreated. | [Complete partial proof](Q3454-proof.md), with explicit threshold and inverse-difference bound. |

The general Q3236 proof is a research proposal for mathematical review, not an established literature result. Q3454 is not marked solved. The catalog integration and review links are recorded in the [round overview](../README.md).

## Reproduction

Run, from the repository root:

```bash
python solutions/round-2026-10-09/algebra/verify_results.py
```

The [exact checker](verify_results.py) uses rational arithmetic only. The checked [output](verification.json) records 128 breakpoint calculations for Q3236's auxiliary example, six Moore–Penrose matrix examples, and the sharp scalar threshold for Q3454. Every check passed. These computations verify examples and identities; the analytical proofs supply the general results.

## Boundaries and provenance

The starting repository commit was `8967f4f70776856b3dfc0b2494ed73167b15ee0c`. Exact-identifier searches found no earlier solution files for these two targets. Their primary papers were read directly and linked in the proof files. Literature searches were bounded and do not certify novelty or priority. Repository delivery is recorded in the round overview; no person-directed external communications were sent.

Q202/Q203 were briefly considered but not claimed: the realization problem requires more source verification, and the available thesis download ceased returning its contents. Other initially inspected targets were dropped before a result was claimed. These are not counted as solved or advanced.
