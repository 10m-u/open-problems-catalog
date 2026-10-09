# Source verification and bounded literature search

Date of all checks: **2026-10-09**. Searches used quoted problem terminology and author/title searches. A failure to locate a later resolution is a bounded search result, not proof of historical novelty or absolute openness. Full source PDFs are not included in the repository.

## Selected catalog records

| Record | Initial status | Provisional | Source location | Prior repository results |
|---|---|---|---|---|
| Q3101 | open | false | Paulista, Problem 7.3, printed p. 28 | none linked from the record |
| Q3102 | open | false | Paulista, Problem 7.4, printed p. 28 | none linked from the record |

Catalog source: `data/problems.json`, records 3101 and 3102. Their source statement identifiers are `c70e8d3a2fbecae7293d` and `0e397ee2bdb8fdd8862d` respectively.

## Primary sources actually inspected

### 1. Tânia Paulista: authoritative problem statement

*Commuting graphs of inverse semigroups and completely regular semigroups*, arXiv:2511.10612v1, submitted 13 November 2025.

- Abstract/version page: <https://arxiv.org/abs/2511.10612>
- Full PDF: <https://arxiv.org/pdf/2511.10612>
- Relevant pages: pp. 3–5 (graph conventions, left paths, completely regular structure and Rees matrices), pp. 16–20 (Theorem 3.5), pp. 25–28 (knit degree and exact open problems).
- The downloaded PDF identifies itself as v1 and has 29 pages, 468,557 bytes.
- SHA-256: `bf1ae25296b0a223e408dced61d881470f790b3596696931c685f4ea345c9a1d`.

The exact hypotheses were checked from the PDF: finite noncommutative semigroups, central vertices omitted, all endpoint equations included in a left path, and ordinary girth. The source settles even girths and excludes knit degree one for completely regular semigroups. Problems 7.3 and 7.4 remain explicitly stated in the inspected version.

The arXiv HTML endpoint returned a fetch error, so it was not used as a substitute for the PDF's mathematics.

### 2. João Araújo, Michael Kinyon and Janusz Konieczny: earlier band work

*Minimal paths in the commuting graphs of semigroups*, European Journal of Combinatorics 32 (2011), 178–197.

- DOI: <https://doi.org/10.1016/j.ejc.2010.09.004>
- Author-hosted preprint, full text read: <https://cs.du.edu/~mathfiles/preprints/nsm-math-preprint-1006.pdf>
- The inspected PDF has 23 pages, 437,937 bytes.
- SHA-256: `703cbc4afc0607b06e22674aa5df8c3ee2580bcc1760412269eaf71fa1c44960`.
- Especially inspected: Section 5, Lemma 5.1 and Proposition 5.2, pp. 20–21; Section 6's questions.

Proposition 5.2 provides a related quasi-identity implication for bands. Its algebraic product construction does not by itself guarantee a noncentral middle vertex. The new Q3102 argument handles centrality explicitly and uses subgroup identities to reach the completely regular setting. No claim is made to have invented that preceding product-of-interior-vertices observation.

### 3. Tomer Bauer and Be'eri Greenfeld: outside-hypothesis controls

*Commuting graphs of boundedly generated semigroups*, European Journal of Combinatorics 56 (2016), 40–45; arXiv version uploaded 14 October 2017.

- HTML full text, inspected: <https://arxiv.org/html/1710.05250v1>
- PDF: <https://arxiv.org/pdf/1710.05250>
- DOI: <https://doi.org/10.1016/j.ejc.2016.02.009>
- Proposition 3: unrestricted-semigroup realization of a graph, with the optional monomial relations setting adjacent products to zero.
- Example 10: the nilpotent semigroup of knit degree three.

These constructions are used solely as attributed controls. Neither is a completely regular solution to the selected questions. The checker reconstructs Example 10 as an 11-element semigroup and the monomial 5-cycle realization as a 21-element semigroup.

### 4. Ajmal Ali and Zahid Raza: earlier band constructions

*On construction of some new types of semigroups*, Journal of Semigroup Theory and Applications 2017, Article 4.

- Publisher PDF, inspected through indexed full text: <https://scik.org/index.php/jsta/article/download/2774/1559>
- Relevant portions: band definitions and transformation constructions, Sections 1–4.

This is a construction paper. No theorem excluding odd cycles in triangle-free band commuting graphs was located there. The title and graph pictures were not treated as a claim about all odd girths. A direct HTTP download returned 403; the public indexed PDF text was available and was used for the bounded scope check.

### 5. Ajmal Ali: earlier even-girth bands

*On large arbitrary girth of a semigroup*, New Trends in Mathematical Sciences 6(1) (2018), 18–23; published 8 January 2018.

- DOI: <https://doi.org/10.20852/ntmsci.2018.241>
- Full publisher PDF, inspected: <https://www.ntmsci.com/ajaxtool/GetArticleByPublishedArticleId?PublishedArticleId=8379>
- Especially inspected: Introduction and Section 3, including Proposition 1 and the 9-element girth-six example.

The actual result concerns even girths. No general odd-girth exclusion for bands was located in this source. It is recorded to avoid mistaking the earlier even-girth construction for a new contribution of this round.

## Search queries and outcomes

| Queries, run 2026-10-09 | Outcome relevant to selection or novelty |
|---|---|
| `"knit degree" "3" "completely regular"`; `"knit degree" "band" "3"` | Returned Paulista's retained Problem 7.4, the 2011 paper, and the nilpotent Bauer–Greenfeld example; no later completely regular resolution located. |
| `"Commuting graphs of inverse semigroups" "girth" 2026` | Returned the current source and associated semigroup papers; no closure of the odd-girth question located. |
| `"commuting graph" "normal band"`; `"knit degree" "normal"`; `"commuting graph" "band" "bipartite"` | Returned structural background and specific constructions, not a general theorem settling the selected targets. |
| `"band" "commuting graph" "odd cycle"`; `"semigroup" "girth" "bands"`; `"triangle-free" "commuting" "band"` | Located the 2018 even-girth paper and other graph work. Full relevant primary sources were inspected as listed above. |

No result is called historically novel on the strength of these searches alone. Both proofs state their exact mathematical scope independently of priority.

## Selection change before substantive work

Q202 and Q203 were initially proposed because their Waldschmidt-constant questions shared a promising algebraic construction. Their canonical McMaster thesis endpoints returned explicit bot-access denial. Search snippets did not provide enough of the original construction or exact statement to support a faithful attack. Those two entries were set aside before any result was claimed. The final selected pair is Q3101 and Q3102, whose full authoritative source was accessible.

## Exact verification and optional finite-model exploration

The main verification command is:

```sh
python solutions/seven-problems-2026-10-09/algebra/verify_semigroups.py
```

It uses only the Python standard library. Its current output checks 13 explicit semigroups, all 49,725 associativity triples, every length-one/two/three left path in those examples, all applicable structural lemmas, and 674 constructive collapses across the three proof cases. The checks are not an exhaustive classification of all semigroups of bounded order.

Optional exploration uses `search_semigroups.py` with the external package `z3-solver==5.1.0.0` (reported engine version 5.1.0). `smt-exploration.json` records exactly four completed queries: bands of order 6 and 12 for Q3102, completely regular semigroups of order 8 for Q3102, and bands of order 8 with girth 5 for Q3101. They returned `unsat`; no independently checkable SMT proof artifact was emitted. These solver results are supplementary and are not premises of either mathematical proof.

Example optional command, after installing that package in a separate environment:

```sh
python solutions/seven-problems-2026-10-09/algebra/search_semigroups.py \
  --question Q3102 --variety completely-regular --order 8 --timeout-ms 60000
```
