# Source and literature log

Date checked: 2026-10-09. Catalog problems: Q276 and Q277.

## Primary material inspected

| Source | Access and material checked | Relevance |
| --- | --- | --- |
| Mottram, *Percolation with constant freezing*, [arXiv:1309.1752v2](https://arxiv.org/abs/1309.1752v2), [PDF](https://arxiv.org/pdf/1309.1752) | PDF opened; Section 1.4, Definition 2.1, and Algorithm 2.3 read | Confirms both questions, the generator used in the recursion, and the distinction between association and the FKG lattice condition |
| Mottram dissertation, [Cambridge PDF route](https://www.repository.cam.ac.uk/bitstreams/72e98faf-8e12-4374-9a2e-c0c8ad6840e1/download) | Exact catalog URL attempted; tool reported it inaccessible | Source-location metadata retained from the catalog; contents were verified against the author's available paper instead |
| [arXiv HTML route](https://arxiv.org/html/1309.1752v2) | Search indexed the route, but opening it returned an internal access error | No substantive claim relies on the unavailable HTML version |

## Literature search

The following exact-topic searches were issued on 2026-10-09:

```text
"percolation with constant freezing" "FKG"
"percolation with constant freezing" monotonicity
"percolation with constant freezing" "positive association"
"percolation with constant freezing" "monotonicity"
"percolation with constant freezing" "FKG inequality"
```

Both available search engines were used, with the stronger engine used for the
verification pass. Relevant results led back to Mottram's primary paper;
secondary mirrors and unrelated freezing models were not used as mathematical
sources. No later resolution or published finite-case enumeration matching the
present scope was located. This is a bounded search result and does not prove
that such work is absent.

## Attribution and disposition

The exact final-law recursion, graph/event enumeration, polynomial certificates,
and componentwise deductions in this directory were independently derived for
this task. The general problems are **not solved here**. Use the repository status
`partial` for Q276 and Q277, adding only the precise restricted theorem attached
to each. This status records progress and does not close the unrestricted
questions.

No publication-priority assertion is attached to the finite cases. There is no
simulation evidence being promoted to a proof: the stated parameter ranges are
certified by integer-polynomial inequalities.
