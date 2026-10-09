# Proofs, counterexamples and checks on thesis statements

Written proofs with exact computational checks, produced with AI assistance in this project. Not peer reviewed.

| Problem | Title | Status | Result |
|---|---|---|---|
| [Q34](../../problems/mathematics/combinatorics-graph-theory-part-1.md#q34) | What is m(Q_(d),4) for every d≥4, where m(G,r) is the fewest initially infected … | partial | m(Q_d;4) = d(d^2+3d+14)/24 + 1 (the Morrison-Noel lower bound) for infinitely many d, and within O(d) of it for all d. Consequently, for r = 4, (m(Q_d,4) - d^3/24)/d^2 -> 1/8. The exact value for every d and all r >= 5 remain open. |
| [Q68](../../problems/computer_science_ai/classical-statistical-machine-learning.md#q68) | For finite simplices and V(x,y)=x^(T)Ry/(x^(T)Sy), with R real and S nonnegative… | partial | For 2x2 ratio games the gradient descent-ascent field is D^-2 J grad H with separable H=A(p)+B(q) (cubic A, B from the pencil (N,D)); every interior equilibrium is a centre; all closed orbits are convex (normalisation to P g(xi)+R… |
| statement `049cdbf27846a9b67646` | Denis Chebikin: Question 4.3 | disproved | Chebikin circular-order axioms: both general questions answered negatively |
| statement `554e70d25a867d4b5fde` | Roberto E. Martinez II: Conjecture 6.100 | proved | Martinez: minimal polynomials and norms of i cot(pi/2n) and of cot products |
| statement `adab297f8aede12e8145` | Roberto E. Martinez II: Conjecture 6.103 | proved | Martinez: minimal polynomials and norms of i cot(pi/2n) and of cot products |
| statement `6183bbce3ba05e94be41` | Roberto E. Martinez II: Conjecture 6.104 | proved | Martinez: minimal polynomials and norms of i cot(pi/2n) and of cot products |
| statement `7dcc3dfc5e1d6d81270f` | Roberto E. Martinez II: Conjecture 6.105 | proved | Martinez: minimal polynomials and norms of i cot(pi/2n) and of cot products |
| statement `1503482190e17282e685` | Jonathan Andrew Noel: Question 5.22 | partial | Minimum percolating sets in Q_d for 4-neighbour bootstrap percolation |
| statement `8d732bedcf590385c84a` | Jonathan Andrew Noel: Problem 5.23 | partial | Minimum percolating sets in Q_d for 4-neighbour bootstrap percolation |
| statement `88de79e52b9f3672f7b6` | Jonathan Andrew Noel: Question 5.24 | partial | Minimum percolating sets in Q_d for 4-neighbour bootstrap percolation |
| statement `a89c4a7fea1f6a2b1d26` | Amin Karbasi: open | partial | Karbasi graph-sensitive lower bounds: sharp path cases and decision targets |
| statement `b3e1b3f70ded2389e6fa` | Natasha Morrison: Question 7.1 | partial | Minimum percolating sets in Q_d for 4-neighbour bootstrap percolation |
| statement `43e10d10544b09bd3194` | Natasha Morrison: Problem 7.2 | partial | Minimum percolating sets in Q_d for 4-neighbour bootstrap percolation |
| statement `b0f6a95636208fb9a7af` | Natasha Morrison: Question 7.3 | partial | Minimum percolating sets in Q_d for 4-neighbour bootstrap percolation |
| statement `0d1e1cc523bd2a4c63e8` | Gilles Baechler: proposed | partial | Baechler Lippmann spectrum recovery: uniqueness under uniform development |
| statement `72184819523abfd5529a` | Alexander Spence Wein: Question 4.2.8 | partial | Wein orbit-recovery degrees: exact cyclic Fourier-support cases |
| statement `3cd16ad221bb93b595f7` | Edward John Mottram: Question 2 | proved | Mottram: small-ball probability of a Brownian excursion at a fixed time |
| statement `a10ca07cc94f7e2db9e2` | Amir Ali Ahmadi: Conjecture 5.2.1 | proved | Ahmadi 2x2 non-monotonic Lyapunov conjecture (P = I, third-order Butz condition) |
| statement `41b1c7792350f621ca27` | Jayanti, Siddhartha Visveswara.: Open Problem 5.1 | partial | Jayanti constrained couplings: Gaussian affine support and shared-separator residuals |
| statement `c9757a96a30026468248` | Golowich, Noah: Problem 13.4.2 | partial | Extragradient on ratio games: last-iterate convergence for 2x2 games with an interior equilibrium |

## Files

- [ahmadi-lyapunov-checks.json](ahmadi-lyapunov-checks.json)
- [ahmadi_lyapunov_checks.py](ahmadi_lyapunov_checks.py)
- [circular-orders-check.py](circular-orders-check.py)
- [circular-orders-checks.json](circular-orders-checks.json)
- [circular-orders.md](circular-orders.md)
- [cyclic-orbit-degree.md](cyclic-orbit-degree.md)
- [cyclic-phase-checks.json](cyclic-phase-checks.json)
- [cyclic_phase_checks.py](cyclic_phase_checks.py)
- [cyclic_phase_lattice.py](cyclic_phase_lattice.py)
- [gaussian-affine-checks.json](gaussian-affine-checks.json)
- [gaussian-constrained-couplings.md](gaussian-constrained-couplings.md)
- [gaussian_affine_checks.py](gaussian_affine_checks.py)
- [gaussian_affine_coupling.py](gaussian_affine_coupling.py)
- [graph-testing-check.py](graph-testing-check.py)
- [graph-testing-checks.json](graph-testing-checks.json)
- [graph-testing.md](graph-testing.md)
- [hopkins-chipfiring-inversions.txt](hopkins-chipfiring-inversions.txt)
- [hopkins_chipfiring_inversions.cpp](hopkins_chipfiring_inversions.cpp)
- [lippmann-uniqueness-checks.json](lippmann-uniqueness-checks.json)
- [lippmann-uniqueness.md](lippmann-uniqueness.md)
- [lippmann_uniqueness_checks.py](lippmann_uniqueness_checks.py)
- [martinez-cot-checks.json](martinez-cot-checks.json)
- [martinez_cot_checks.py](martinez_cot_checks.py)
- [path-acceptable-actions.md](path-acceptable-actions.md)
- [path-action-sensing-checks.json](path-action-sensing-checks.json)
- [path_action_sensing.py](path_action_sensing.py)
- [path_action_sensing_checks.py](path_action_sensing_checks.py)
- [quick-closures.md](quick-closures.md)
- [ratio-game-eg-lyapunov.json](ratio-game-eg-lyapunov.json)
- [ratio-game-results.txt](ratio-game-results.txt)
- [ratio_game_drift_scan.py](ratio_game_drift_scan.py)
- [ratio_game_eg_lyapunov.py](ratio_game_eg_lyapunov.py)
- [ratio_game_orbit_convexity.py](ratio_game_orbit_convexity.py)
- [ratio_game_symbolic.py](ratio_game_symbolic.py)
- [round2-harder.md](round2-harder.md)
- [round3.md](round3.md)

