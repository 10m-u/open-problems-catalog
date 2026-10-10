# Algebra source and scope audit

Checked 2026-10-09. Both selected entries were `open` and had empty `results`,
`ledger`, and `literature_partial` fields when selected. The repository's prior
solution Markdown files contained no Q1715/Q2305 result or property-F proof.
This log records a bounded source audit, not proof of global historical novelty.

## Q1715

**Primary definition and question:** Burde, Dekimpe and Moens,
*Commutative post-Lie algebra structures and linear equations for nilpotent Lie
algebras*, Journal of Algebra 526 (2019), 12–29.

- [Author-hosted PDF](https://homepage.univie.ac.at/dietrich.burde/papers/burde_57_cpa.pdf): direct retrieval timed out.
- [arXiv full HTML](https://arxiv.org/html/1711.01964v1) and [PDF](https://arxiv.org/pdf/1711.01964): successfully read; Definition 5.1 requires all generating pairs and solutions in the derived algebra. Section 5 ends with the exact proposed characterization. Proposition 5.6 addresses complex dimensions at most seven. The preceding discussion records the free two-generator dimensions through class ten.
- [arXiv abstract/version page](https://arxiv.org/abs/1711.01964): consulted for identification.

**Newer catalog reference:** Abdelwahab, Abdurasulov and Kaygorodov,
*The algebraic and geometric classification of commutative post-Lie algebras*,
[arXiv:2602.00614v1](https://arxiv.org/html/2602.00614v1), submitted 31 January
2026. The abstract, introduction, theorem scopes, and full-text search were
checked. Its classifications concern three-dimensional CPAs and
four-dimensional nilpotent CPAs. It cites the older source as prior work;
it does not state the property-F characterization or a thirteen-dimensional
counterexample. Full-text searches for `property` and `13-dimensional` returned
no match.

**Searches:** both a routine search and a stronger-coverage search were used.
Queries included `Burde "property F" "free-nilpotent" Lie algebras`,
`"property F" "nilpotent Lie" counterexample`,
`"Burde" "property F" "13"`, and
`"free-nilpotent" "property F" "quotient"`.
The retrieved relevant primary result was the source paper; no later matching
resolution was located. Search results about *Periodic derivations and
prederivations of Lie algebras* use a different property called F and were not
treated as evidence about this question.

**Result boundary:** the explicit table refutes the necessity direction of
the catalog's equivalence. It does not classify every algebra with property F
or prove a minimum counterexample dimension. Its mathematical validity is
established by the new proof and exact certificate, independently of the
bounded novelty search.

## Q2305

**Primary definition and question:** Araújo, Bentz, Kinyon, Konieczny, Malheiro
and Mercier, *The Inverse Monoid of Partial Inner Automorphisms of a Semigroup*.

- [arXiv full HTML](https://arxiv.org/html/2605.00041v1): successfully read. Section 3 supplies the exact domains and maps, Definition 3.8 defines the generated inverse monoid, and Problem 7.9 asks for the finite-dimensional vector-space case.
- [arXiv abstract/version page](https://arxiv.org/abs/2605.00041): successfully read; the returned submission history listed v1, 28 April 2026.
- [Publisher article](https://www.sciencedirect.com/science/article/pii/S0021869326003066): direct retrieval returned an internal error.
- [Institutional author PDF](https://novaresearch.unl.pt/files/168910237/Ara_jo_et_al._2026_..pdf): indexed search excerpt retained Problem 7.9, but a direct open returned HTTP 403. No inaccessible text is used in the proof.

**Searches:** queries included
`"The Inverse Monoid of Partial Inner Automorphisms" "matrix"`,
`"partial inner automorphisms" "matrix" "monoid"`, and
`"partial inner automorphisms" "7.9"`. Both search engines were used; the
stronger search located the journal and institutional versions. No later
matrix-monoid classification was located in the returned sources.

**Convention audit:** matrices act as endomorphisms and products use standard
rightmost-first composition in the proof. The zero matrix belongs to every
original domain and is fixed by every generator. Thus the generated monoid
contains no empty map; its absorbing element is the identity on the singleton
zero subsemigroup. The proof allows the two subspaces in a generator domain
to intersect, which is essential for nonsemisimple eigenvalue-one blocks.

**Result boundary:** the classification is proved for finite-dimensional
endomorphism monoids over fields, with dimensions zero and one treated
separately. It makes no assertion for modules over arbitrary rings,
infinite-dimensional vector spaces, or the general residual-finiteness
question Q2304.
