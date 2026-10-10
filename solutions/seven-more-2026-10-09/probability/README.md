# Q276 and Q277: exact finite-graph partial results

Date: 2026-10-09.

**Both unrestricted catalog questions remain open.** This directory proves two
restricted theorems by exhaustive integer-polynomial certificates:

| Catalog question | Proven scope | Exact certificates |
| --- | --- | ---: |
| Q276: stochastic decrease as the freezing rate increases | Every finite simple graph whose connected components each have at most five edges | 91,881 increasing-event derivatives |
| Q277: positive association of increasing events | Every finite simple graph whose connected components each have at most four edges | 71,637 unordered event-pair covariances |

The graph class in each row has no bound on its total number of vertices or
edges, because independent connected components preserve the corresponding
property. Arbitrary connected graphs, multigraphs, and infinite connected graphs
are outside these results.

## Files

- [Proof and certificate construction](Q276-Q277-proof.md).
- [Standard-library verifier](verify_constant_freezing.py).
- [Verification report](constant_freezing_verification.json), including graph
  representatives, event counts, certificate hashes, and controls.
- [Exact laws](constant_freezing_laws.json). Each law is a list of integer
  numerator polynomials over one positive denominator polynomial.
- [Dated source and literature log](source-log.md).

## Reproduce

From this directory, run:

```sh
python3 verify_constant_freezing.py
```

Python 3.10 or later is sufficient; no packages, network access, sampling, or
floating point arithmetic are required. The program regenerates the two JSON
files, checks every claimed coefficient sign, and exits unsuccessfully if a
certificate fails. Its independent full-state Markov calculation checks the
symbolic final law at three rational parameter values on every graph.

The negative control is substantial: for the three-edge path at freezing rate
one, the stronger FKG lattice inequality fails by exactly `-1/525`. Thus the
positive-association result does not rest on mistaking the lattice condition for
the event inequality.

## Proposed catalog disposition

Use the repository status `partial` for Q276 and Q277, with the respective
component-size theorem recorded as an independently derived, computer-assisted
partial result dated 2026-10-09. The unrestricted questions remain unresolved.
The source search did not establish priority for these finite cases; no claim
of publication novelty or a general solution is made.
