# Discrete problems in the seven-problem round

Date: 2026-10-09.

| Problem | Proposed status | Result |
|---|---|---|
| [Q3499](Q3499-proof.md) | Disproved | The 13-gon face lattice has Ehrhart linear coefficient \(-298495711/35302608\). Exact certificates include every coefficient and two independent arithmetic derivations. |
| [Q3480](Q3480-proof.md) | Partial | An exact finite-state enumeration for each fixed alphabet and rational generating functions for four-letter words and Cayley words of maximum four. The unrestricted closed enumeration remains open. |

The [source log](SOURCES.md) records dated primary-source checks and bounded literature searches. Each result has a generator and a separately written verifier using Python's standard library. The verifier scripts import no generator code. These reports have not undergone external review.

```sh
python solutions/seven-more-2026-10-09/discrete/q3499_generate.py
python solutions/seven-more-2026-10-09/discrete/q3499_verify.py
python solutions/seven-more-2026-10-09/discrete/q3480_enumerate.py
python solutions/seven-more-2026-10-09/discrete/q3480_verify.py
```
