# Probability research, 9 October 2026

Three complete arguments at the exact scope of their cited source questions are submitted in this directory. They are mathematical research claims supported by proofs and independent finite checks, not assertions of publication or historical priority. The [round overview](../README.md) records their catalog integration and independent internal reviews.

| Catalog problem | Result proved here | Proof |
|---|---|---|
| Q192 | Brownian motion conditioned on one high-order power integral being zero converges to the zero path in the uniform topology. Every fixed-radius escape probability decays faster than any prescribed exponential in the power. | [Q192-brownian-power-conditioning.md](Q192-brownian-power-conditioning.md) |
| Q270 | The bunkbed inequality holds for every transitive tournament. The proof permits any common horizontal probability and independent vertex-dependent vertical probabilities. | [Q270-transitive-tournament-bunkbed.md](Q270-transitive-tournament-bunkbed.md) |
| Q1060 | Four centered integer-supported marginals have unrestricted optimum 16 and NCD optimum $920/57$. Every unrestricted minimizer has covariance $\operatorname{Cov}(X_2,X_3)\geq1/2$. Nondegenerate counterexamples follow for every dimension at least four. | [Q1060-negative-covariance-counterexample.md](Q1060-negative-covariance-counterexample.md) |

## Verification

From the repository root, run:

    python solutions/round-2026-10-09/probability/verify_probability.py
    python solutions/round-2026-10-09/probability/verify_q270.py

Both scripts use the Python standard library. The first verifies Q1060's entire sixteen-atom pointwise dual identity, both exact optimizing distributions, all marginals and covariance matrices, and all subset costs. It also checks 1,035 exact instances of the deterministic peak inequality used in Q192. The second enumerates 66,066 explicit percolated graphs, checks every ordered vertex pair against the count process, and verifies the diagonal cancellation and parameter extensions.

The saved outputs are [probability-certificates.json](probability-certificates.json) and [Q270-certificates.json](Q270-certificates.json). The finite checks supplement the proofs: they do not establish an infinite-family theorem by extrapolation.

The optional exploratory [search_q1060.py](search_q1060.py) requires SciPy. It is unnecessary for certificate verification.

## Boundaries

Q192's proof does not resolve the full Brownian-signature conjecture Q191 or its comparison problem Q193. Q270's proof uses the complete ordered predecessor sets of a transitive tournament and does not establish the false general acyclic-graph conjecture. Q1060's counterexample concerns the maximum over all subsets with heterogeneous marginals, precisely the objective in the source's Remark 4.

Q294 was also inspected. The catalog's pointwise-truncated Gibbs formula differs from the source paper's displayed aggregate empirical-risk constraint. No closure of the source's full profile-posterior question is claimed in this directory.

Each proof identifies primary sources, search date, previous related repository work, and the limits of the claim.
