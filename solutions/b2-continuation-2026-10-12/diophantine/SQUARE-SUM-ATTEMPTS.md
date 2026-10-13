# Q3208: a five-by-five square-sumset

Exact target: two sets of five integers such that every cross-sum is an integer square. Read source: `texts/papers/collections-9997b9d36ee232d0.txt.gz`, Choudhry's 2026 Integers paper, especially its initial constructions, scaling lemmas and final question. Rational solutions can be cleared by multiplying both sets by a common denominator squared, so a rational five-by-five construction would suffice.

## Complete unbounded nonextension of the published four-by-four seed

The published seed is

    A={324,54756,119716,264196},
    B={0,79200,227205,1258560}.

Every cross-sum is a square. For a fixed set V containing v_0<v_1, any integer u with u+v_0=s²,u+v_1=t² gives

    (t−s)(t+s)=Δ=v_1−v_0.

Take nonnegative square roots, so t>s≥0. Enumerate all positive factor pairs d e=Δ, d≤e, with e−d even. Then s=(e−d)/2 and u=s²−v_0; test the other entries in V by exact integer square roots. This is a complete enumeration of u even when u is negative and otherwise unrestricted.

[SQUARE-SUM-SEED-CHECK.json](SQUARE-SUM-SEED-CHECK.json) records that the only u compatible with all B are the existing A, and the only u compatible with all A are the existing B. Consequently this exact seed permits **no fifth row and no fifth column**, at any integer height. This is a complete seed theorem, not a bounded-coordinate search and not an exclusion of other seeds.

<a id="q3208-a1"></a>
## Q3208 A1 — Add a row and a column to the known seed

The complete factor-pair procedure above was executed in both directions. Both candidate sets equal the existing entries, so neither augmentation can start. Simultaneously adding a row and column cannot avoid their required sums with the four retained opposite entries. **Failed fixed-seed construction; full nonextension result retained.**

<a id="q3208-a2"></a>
## Q3208 A2 — Combine the source's five-by-three and four-by-four constructions

Each gives one side of the desired cardinality pattern. A five-by-three example does not supply a fourth or fifth common neighbor, and its parameters need not include the four-by-four seed. Opposite translation A↦A+h,B↦B−h by an integer preserves the integer common-neighbor problem, so it cannot repair A1. Squared scaling preserves the square equations but can change integrality: an integer neighbor of a scaled seed may correspond to a noninteger rational neighbor of the original. The integer seed certificate therefore does not exclude extensions after arbitrary squared scaling. This would require a complete rational-neighbor analysis, which is not supplied. A gluing argument also needs compatibility between all old cross-sums and the new block; no such parameter identification is obtained from the independent examples. **Failed construction-gluing route, with the rational/scaled extension obligation still open.**

<a id="q3208-a3"></a>
## Q3208 A3 — Obtain global impossibility from small-modulus obstructions

The square conditions are compatible modulo any finite list of moduli: take all entries in both sets divisible by the common multiple, making every cross-sum zero modulo each modulus. In particular reduction modulo 16 admits five distinct integers in each set with all sums congruent to 0. Residue data impose no uniform height bound and cannot alone exclude the target. This is a test of a local impossibility proof, not evidence that every locally compatible seed lifts. **Failed finite-congruence exclusion.**

<a id="q3208-a4"></a>
## Q3208 A4 — Use identical sets with square diagonals

Set A=B={2t_i²:i=1,…,5}. The diagonal sums 4t_i² are squares. Cross-sums require 2(t_i²+t_j²) to be square too; t_i=1,t_j=2 already gives 10. Repeated equal t_i would satisfy the obvious diagonal construction but reduce cardinality below five. Prescribing the five diagonals therefore does not solve the ten additional coupled equations. **Failed diagonal-square construction.**

<a id="q3208-a5"></a>
## Q3208 A5 — Use finiteness of common neighbors for a fixed five-set

For fixed five distinct a_i, the curve y_i²=x+a_i has a degree-32 multiquadratic map to the x-line. The five finite branch points and infinity each have inertia 2, giving 2g−2=−64+6·16=32 and g=17. Faltings gives finitely many rational common neighbors of this fixed A. It gives neither an upper bound of four nor uniform nonexistence as A varies. The five-set could in principle have five rational neighbors; denominator clearing would yield an integer solution. **Failed fixed-curve finiteness-to-nonexistence route.**

Five construction/proof routes failed to settle the global existence question. The seed exclusion has unrestricted new-entry scope, and the exact five-by-five catalog question remains unresolved.
