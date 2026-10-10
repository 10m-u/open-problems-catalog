# Source and literature checks

Checked on **2026-10-10**. These are bounded public-source searches,
not assertions that every possible publication has been searched.
The mathematical arguments in the accompanying notes are supplied
in full and do not rely on a search result as proof.

## Problem 212

| Source | Exact location and observation |
| --- | --- |
| [Dramburg, thesis](https://uu.diva-portal.org/smash/get/diva2:1954180/FULLTEXT01.pdf) | Section 2.5.3, printed page 31: locally finite nonnegative grading; no standard-grading assumption in this question. |
| [Dramburg--Sandøy](https://arxiv.org/pdf/2411.13283) | Question 3.10, printed page 15: asks for an automorphism sending an idempotent, or a complete primitive set, to degree-zero parts. |
| [Dramburg, September 2026 follow-up](https://arxiv.org/html/2609.03288v1#S6) | Question 6.2: distinguishes the standard semiconnected case from the broader locally finite nonnegative case; still poses the broader question. |
| [Author's original MathOverflow question](https://mathoverflow.net/questions/479788/are-idempotents-in-a-nonnegatively-graded-algebra-conjugate-to-homogeneous-idemp) | This earlier version includes generation in degrees zero and one. The cusp example does not satisfy that additional condition. No answer was displayed. |

Search strings included `"Dramburg" "idempotents" counterexample`,
`"locally finite" "idempotents" "cusp"`, and `"2609.03288"`.
No matching later general resolution was located. The question's
scope was taken from the thesis and associated paper, with the
stricter earlier and later variants explicitly separated.

## Problem 3893

| Source | Exact location and observation |
| --- | --- |
| [Holleben--Nicklasson, final published PDF](https://mdu.diva-portal.org/smash/get/diva2:2053155/FULLTEXT01.pdf) | Conjecture 1.3, page 3, and Conjecture 3.15, page 10; the final paper retains the conjecture. Theorem 3.10 supplies the independent-set cokernel construction used in the explicit-certificate section. |
| [Author preprint](https://arxiv.org/html/2502.00155v2) | Same conjecture and theorem numbering; accessible text verifies the definitions and existing partial results. |
| [Hoa--Phuoc--Son, September 2026](https://arxiv.org/html/2609.13888v1) | Classifies WLP for tadpole graphs, a different graph family; its stated theorems do not give a general whiskered-graph resolution. |
| [SSRN 7385138](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7385138) | Search retrieval marks the eight-vertex preprint **WITHDRAWN**. It was not used as proof or as a trusted computational input. |

Search strings included `"Holleben" "Nicklasson" "Conjecture 3.15"`,
`"whiskered" "Lefschetz" "independence number" proof`,
`"whiskered" "Lefschetz" "direct sum"`,
`"whiskered" "y_i" "automorphism" Lefschetz`, and
`"whiskered" "Lefschetz" "proved" "2026"`.
No general resolution was located in these searches. The new ingredient
in the accompanying proof is the simultaneous kernel obstruction and
the invariant-summand argument, rather than a repetition of the
already published cokernel construction alone.

## Reproduction results

```text
python solutions/seven-selected-2026-10-10/algebra/verify_212.py
PASS: determinant, idempotents, primitive-corner reductions, cross-corner reductions, and Bezout certificate (exact integers).

python solutions/seven-selected-2026-10-10/algebra/verify_3893.py
PASS: exact kernel/cokernel certificates for 48 graphs; shear inverse and intertwining on 1745 basis monomials.
```
