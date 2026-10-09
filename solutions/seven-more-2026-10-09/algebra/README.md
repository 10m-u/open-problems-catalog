# Algebra results, 9 October 2026

| Problem | Result and exact scope | Proof | Certificate |
|---|---|---|---|
| Q1715 | A 13-dimensional class-five Lie algebra has property F for every generating pair, over every characteristic-zero field, but is not free nilpotent. This refutes the proposed characterization. | [Q1715.md](Q1715.md) | [check_q1715.py](check_q1715.py), [q1715-certificate.json](q1715-certificate.json) |
| Q2305 | For every field and finite dimension, the partial inner automorphism monoid consists of invertible conjugations restricted to an explicitly characterized semilattice of rectangular matrix subspaces. Equality, product, inverse, and small-dimensional cases are specified. | [Q2305.md](Q2305.md) | [check_q2305.py](check_q2305.py), [q2305-certificate.json](q2305-certificate.json) |

The two scripts need only Python's standard library. Run them from any working
directory by supplying their paths; they emit deterministic JSON certificates
to standard output and fail if a check is false. Neither accesses the network.

[sources.md](sources.md) records source scope, retrieval failures, the newer
Q1715 follow-up, and the literature search boundary. These are submitted
proofs with exact reproducible controls; no external peer-review or historical
priority claim is made.
