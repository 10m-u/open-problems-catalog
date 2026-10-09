# Q256–Q257 source and bounded literature log

**Search date:** 2026-10-09. The search concerns exact proper total domination with open neighborhoods, not proper total coloring, Roman domination, or closed-neighborhood variants.

## Sources and alignment

| Source | Material inspected | Relevance and limitation |
|---|---|---|
| Sawyer Isaac Osborn, *From Total Domination to Graph Coloring*, Western Michigan University, 2026, [institutional record](https://scholarworks.wmich.edu/dissertations/4275/) and [thesis PDF](https://scholarworks.wmich.edu/cgi/viewcontent.cgi?article=5284&context=dissertations) | Institutional metadata and abstract; search-indexed PDF passages around Problem 4.3.8 | Confirms author, thesis, definition, and caterpillar question. Direct PDF retrieval returned HTTP 403. The precise thesis pagination and Q257 problem label are retained from the existing catalog, not represented as a newly completed full-PDF audit. |
| Sawyer Osborn and Ping Zhang, *Proper Total Domination in Trees*, **Symmetry** 17 (2025), 1429, [publisher](https://www.mdpi.com/2073-8994/17/9/1429), [DOI](https://doi.org/10.3390/sym17091429) | Publisher-indexed full-text passages for definition, §§2–5, Question 1 and Question 3 | Primary, author-written statements matching Q256 and Q257. Section 4 gives sufficient caterpillar conditions; §5 retains the characterization question. The paper already treats stars, double stars, diameter-four trees, starlike trees, and proper parameters at most 8. Direct browser-service opens returned HTTP 429; the full-text index was accessible through targeted search results. |
| Gary Chartrand, Ebrahim Salehi, and Ping Zhang, *Realizability in Proper Total Domination in Graphs*, **Discrete Mathematics Letters** 17 (2026), 37–44, [full PDF](https://www.dmlett.com/archive/v17/DML26_v17_pp37-44.pdf), DOI [10.47443/dml.2026.029](https://doi.org/10.47443/dml.2026.029) | Directly parsed eight-page PDF; especially abstract, Theorems 1.2–1.3, §2, §3 and concluding problem | Publication date 2026-04-12. The pair in §2 is minimum/maximum proper total domination, and the later triples concern unrestricted connected graphs. It does not supply a tree-specific classification of (gamma_t,gamma_pt). Its statement of unrestricted graph realizability allows diagonal pairs for a≥5, which our tree inequality excludes. |
| Sawyer Osborn and Ping Zhang, *Proper Total Domination in Generalized Fans and Wheels*, **Symmetry** 18 (2026), 1092, [publisher](https://www.mdpi.com/2073-8994/18/7/1092), DOI [10.3390/sym18071092](https://doi.org/10.3390/sym18071092) | Publisher-indexed concluding discussion and problem | Publication date 2026-06-27. It studies joins of paths/cycles with independent sets and proposes related join problems for caterpillars and other trees. Its discussion cites the prior caterpillar work, without a full caterpillar classification. Direct page retrieval returned HTTP 429. |
| Ritabrato Chatterjee, Emma Jent, Sawyer Osborn, Ping Zhang, *Proper total domination in graphs*, **Electronic Journal of Mathematics** 7 (2024), 58–68, [publisher PDF](https://shahindp.com/Electron_J_Math/v7/EJM24_v7_pp58-68.pdf) | Search-indexed theorem description and its exact restatement in the directly parsed 2026 paper | Establishes unrestricted graph pairs. We do not claim those results are new or transfer them to trees. A separate complete reading of the 2024 PDF was not needed for the elementary arguments in this packet. |

## Search queries and outcomes

Both available search indexes were used. The broader index was followed by targeted primary-source queries and a second search engine for source coverage and recent literature. Searches that returned unrelated proper-total-*coloring* results were not used as mathematical evidence.

| Query or action | Outcome |
|---|---|
| `"proper total domination" caterpillars Osborn` | Located the 2025 trees paper and June 2026 generalized-fans paper. |
| `"proper total domination" trees 2026` | Located the April 2026 realizability paper, the 2026 thesis, and follow-on papers on Cartesian products and joins. |
| `"proper total" "caterpillars" characterization` with recent-year search | Located the unresolved Question 1 in the original primary source; no exact later solution located. |
| `"proper total" "trees" "pairs"` with recent-year search | Located the general-graph realizability work; direct inspection distinguished its graph and parameter scope from Q257. |
| `site:mdpi.com/2073-8994/17/9/1429 "Question 3"` | Retrieved the exact tree-pair question and the paragraph distinguishing it from the earlier general-graph theorem. |
| `site:scholarworks.wmich.edu "Problem 4.3.10"` | No independently useful exact indexed passage for this label; do not claim its page was newly read. |
| `site:scholarworks.wmich.edu/cgi/viewcontent.cgi?article=5284 "Problem 4.3.8"` | Retrieved a passage explicitly identifying Problem 4.3.8 and its caterpillar characterization question. |
| `"proper total domination" "tree" "bound"` with recent-year search | Located the original paper and unrelated domination papers; no general fixed-total-parameter bound matching the new finite reduction located. |
| `"proper total" "caterpillars" algorithm` with recent-year search | No matching finite-state characterization located. Results on total b-coloring and total coloring were excluded as different invariants. |
| Direct opens of the thesis and MDPI primary pages | Encountered the access errors noted above. No attempt was made to bypass them. The publisher's search-indexed author text and the open 2026 PDF supplied the source alignment used here. |

## What this establishes

The authoritative 2025 paper explicitly asks both questions and uses exactly the definitions adopted in this packet. Inspected later primary sources did not resolve the two questions at their stated tree scopes. This is a bounded, dated check, not a proof that no prior solution or equivalent algorithm exists. The tiny-tree constructions in the packet overlap earlier published families and are explicitly treated as context; no historical priority is claimed for them.

No source PDF or bulk copyrighted source text is included in the repository. All mathematical arguments in the result files are self-contained original derivations in this research round, with source links identifying the problems and known context.
