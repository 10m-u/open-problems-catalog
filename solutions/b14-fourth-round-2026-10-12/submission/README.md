# B14 fourth continuation — 2026-10-12

Read REPORT.md first. The complete mathematical arguments are proofs/COMPLETION-CERTIFICATES.md and proofs/BLOCKWISE-DESCENT.md.

## Verify the retained certificates without third-party libraries

From this directory:

```sh
python code/verify_saved_certificates.py
```

This independently verifies the saved integer metrics and their gain signs, the subtour flow certificates, the unique-tour certificate, and every retained DP recurrence for the nonseparable 180-city exact solution. It does not import the construction code. Do not pass Python's -O option: assertions must remain enabled.

## Regenerate the complete evidence

Use Python 3.10 or newer and a C++17 compiler. The tested environment is recorded in checks/ENVIRONMENT.json.

```sh
python -m pip install networkx numpy scipy sympy
bash code/run_checks.sh
```

The script compiles the independent complete-graph subset oracle, regenerates the small exact controls and the two 180-city instances, regenerates the block and flow certificates, and verifies the saved certificates. The 1,000-city experiment uses a fully explicit matrix; it is a structured-family scaling exercise. The nonseparable exact solver has an explicit default guard of at most 20 paired units, which is an implementation protection against accidentally requesting an enormous subset table, not a theorem restriction.

The core module solver and contracted solver use the standard library. SciPy proposes candidate metric-compression LP bases; SymPy reconstructs them exactly. A returned basis is accepted only after checking all integral comparisons and triangle inequalities. NetworkX is used for generating graph decompositions and flow witnesses, not by the independent saved-certificate reader.

## Use the module solver

```python
import sys
sys.path.insert(0, 'code')
from module_solver import random_instance, solve, forced_bounds
from contracted_solver import exact_contract

instance = random_instance('petersen', k=8, seed=17)
result = solve(instance)
assert result['lower'] == result['upper']  # endpoint-separable example
edge_lower_bounds = forced_bounds(instance, result)
kept = [e for e, lower in edge_lower_bounds.items()
        if lower <= result['upper']]

# Works with arbitrary bounded secondary repair costs, including excesses.
exact = exact_contract(instance, result)
assert exact['optimum'] == result['upper']
```

See check_contracted.py for the reproducible nonseparable generator, and module_solver.Necklace for the input representation. An instance must satisfy the two-port obstruction and primary-gap promise stated in the proof. Zero tolls provide a valid endpoint envelope for any nonnegative secondary repair costs. Internal path enumeration is deliberately simple; the proof also describes the better subset-DP dependence on a variable module size.

## Packet layout

- proofs/: full theorem statements, assumptions, arguments, limitations, and distinction from predecessors.
- code/: constructors, exact solvers, independent oracles and checkers.
- checks/: JSON receipts, all saved metric/flow/DP certificates, and environment details.
- instances/: complete original secondary matrices, structural cost specifications, tours, and exact costs for both 180-city instances.
- sources/: original programme, relevant predecessor notes, provenance and primary-source literature context.
- MANIFEST.json: byte sizes and SHA-256 hashes of all packaged payload files, excluding the manifest itself.

The compiled C++ binary and Python caches are not included in the archive. The run script builds the oracle locally. Rerunning experiments changes elapsed-time fields and therefore changes receipt hashes; the original manifest identifies the delivered state rather than promising byte-identical timings.

These are research artifacts with internally checked derivations, not externally peer-reviewed or formally verified mathematics. No catalog resolution or public-repository write was performed.
