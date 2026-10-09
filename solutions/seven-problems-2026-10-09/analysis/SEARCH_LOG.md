# Source verification and bounded literature search

Date: **2026-10-09**. Problems: **Q3286 and Q3287**.

## Authoritative statement and formula

- Ao Sun, *Studies in Multivariate Pareto Records*, Johns Hopkins University, 2025. [Official repository record](https://jscholarship.library.jhu.edu/items/3c4d15c0-ee1d-43c7-94ef-dfb997ae860f); [official PDF](https://jscholarship.library.jhu.edu/server/api/core/bitstreams/7ca48c8a-5406-49b2-979f-adf49c725f4d/content).
- Read Theorem 4.8 and Remark 4.10, printed pp. 72–73; Appendix D.2–D.3, printed pp. 246–263; and Remark D.6, printed p. 263. Verified p. 72 visually as well as by text extraction. The parameter is $a>0$, dimension is fixed at $d\ge2$, and $a^{\overline d}$ denotes a rising factorial. Remark D.6 asks both endpoint limits for total records $R_n$.
- The PDF could be downloaded from the official URL. A later text-view fetch returned HTTP 403, so the downloaded official PDF was used. No access controls were bypassed, and the copyrighted source PDF is not included in this contribution.
- Prior repository scan: Q3286 and Q3287 had `status: open`, `provisional: false`, and empty result arrays. No existing solution report for these IDs was found.

## Queries issued

The following searches were performed in two search engines; the final group used a 730-day recency filter. Queries are recorded literally for reproduction.

| Engine | Query | Relevant outcome |
|---|---|---|
| 2 | `"Ao Sun" "records" variance Dirichlet` | Located the thesis and Fill–Sun's record-setting-probability paper. |
| 2 | `"Studies in Multivariate Pareto Records" "D.6"` | Located no later resolution of Remark D.6. |
| 2 | `"Dirichlet" "records" "dispersion"` | No relevant later endpoint theorem found. |
| 1 | `"Ao Sun" "Dirichlet" "variance" "records"` | Thesis and related Pareto-record papers; no exact endpoint result found. |
| 1 | `"Studies in Multivariate Pareto Records" "D.6"` | No exact later resolution found. |
| 1, recent | `"Dirichlet" "records" "Sun" variance limit` | No relevant resolution found. |
| 1, recent | `"Pareto records" "dispersion"` | Located 2026 frontier/maxima work; no exact dispersion-parameter theorem found. |
| 1, recent | `"Ao Sun" "Berry" "records"` | Located the 2026 Fill paper and older related work. |

## Related primary sources checked

- James Allen Fill and Ao Sun, *On the probability of a Pareto record* (2024), [publisher full text](https://www.cambridge.org/core/journals/probability-in-the-engineering-and-informational-sciences/article/on-the-probability-of-a-pareto-record/8E3DFE944DEA9F45F4B716F39EAFB446), [arXiv:2402.17220](https://arxiv.org/abs/2402.17220). This concerns the probability of setting a record as the sampling law varies; it is background to the marginalized Dirichlet model, not a resolution of the variance-ratio endpoint questions.
- James Allen Fill, *A New Fine-Scale Berry-Esseen-Type Gumbel-Limit Theorem for Multivariate Maxima*, AofA 2026, published 2026-07-13, [official proceedings page and abstract](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.AofA.2026.21). Its abstract concerns the minimum $\ell^1$-norm of maxima under independent exponential coordinates. This does not establish the $a$-limits in Q3286 or Q3287.

## Limitations of this search

The negative search conclusion is bounded and dated, not an exhaustive novelty claim. Search snippets for irrelevant results were not used as mathematical evidence. The analytic results in `REPORT.md` rely on the thesis's explicitly identified fixed-parameter coefficient identity and derive the parameter limits directly. No claim is made that the limiting constants themselves first occur here, or that weak convergence of Dirichlet observations by itself permits exchanging the two asymptotic operations.
