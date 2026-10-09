# Circular-order axioms: negative answers to both questions

2026-09-30. First resolution work from bridge B11.

**Result.** Both general questions in Denis Chebikin's Question 4.3.4 have negative answers. There is a seven-element relation satisfying Lemma 4.3.3 with no circular extension. Removing one triple produces another relation satisfying the same axioms, with exactly one extension, but missing eighteen consequences of that extension. The second example is extendible, so its failure of completeness is substantive rather than a consequence of quantifying over no extensions.

These are hand proofs with exhaustive finite controls, not proof-assistant certificates. No claim of novelty or smallest counterexample is made. The extension obstruction is classical: Megiddo's 1976 paper uses the equivalent partial-cyclic-order axioms and supplies a thirteen-element counterexample. The contribution here is checking the thesis question against that literature and supplying small explicit certificates for both parts. [Megiddo, *Partial and Complete Cyclic Orders*, Definition 2 and Example 5](https://theory.stanford.edu/~megiddo/pdf/cyclic.pdf).

## Exact source and model

Thesis: *Polytopes, generating functions, and new statistics related to descents and inversions in permutations* (2008), §4.3, Definition 4.3.1, Lemmas 4.3.2–4.3.3 and Question 4.3.4. [MIT source](https://dspace.mit.edu/server/api/core/bitstreams/baed69ab-74e6-4e3f-aa0f-1c6c6770fe83/content); local text; subject page. Exact extract: `049cdbf27846a9b67646`, labelled `Question 4.3` by the extractor; its leading `4` belongs to the full label `4.3.4`. The PDF was checked directly because text extraction drops membership and nonmembership signs in Lemma 4.3.3.

Write `xyz` for the cyclic triple containing `(x,y,z)`, `(y,z,x)` and `(z,x,y)`. All vertices in a triple are distinct. Reflection gives the other orientation, a different triple. The thesis's conditions are:

- **A:** `xyz ∈ R` implies `xzy ∉ R`.
- **B:** `xyz, xzw ∈ R` imply `xyw, yzw ∈ R`.

The thesis writes the second antecedent as `zwx`, a rotation of `xzw`, and includes all four subtriples of the cyclic four-tuple. This is exactly the same rule. Megiddo states one of the two conclusions; the other follows by cyclically rotating the premises.

A circular extension is a clockwise ordering of every vertex, up to rotation. The thesis's definition of a circular poset additionally demands that the relation contain every triple shared by all extensions. Thus local closure under B and semantic closure over actual circles are different proposed properties.

## Two explicit relations

Use `X={0,1,2,3,4,5,6}`. Start with the following three complete four-element cyclic orders, including every subtriple:

| Clockwise four-tuple | Its four cyclic triples |
|---|---|
| `(0,2,1,4)` | `021, 024, 014, 142` |
| `(0,2,5,6)` | `025, 026, 056, 256` |
| `(1,4,5,6)` | `145, 146, 156, 456` |

Add the six triples

`034, 036, 132, 136, 253, 345`.

Call this eighteen-triple relation `R`. Let `S=R\{034}`, with seventeen triples.

Both satisfy A: none of the reversed cyclic triples appears. For B, an inspection of the antecedent pairs shows that their four-element supports can only be `{0,1,2,4}`, `{0,2,5,6}` or `{1,4,5,6}`. On each support the table already supplies the complete, consistent four-tuple. Every required conclusion is therefore present. The removed triple `034` participates in none of these antecedent pairs, so the same verification applies to S. The checker audits all 840 ordered quadruples for each relation.

## Proof that S has exactly one extension

Rotate any proposed extension to begin with 0, and write `<` for the resulting linear order of vertices 1 through 6. The relations shared by R and S give

`2 < 1 < 4`, `2 < 5 < 6`, and `3 < 6`.

Whenever `a<b` is known, a cyclic relation `abc` says either `b<c` or `c<a`. This is a disjunction; silently treating it as the first alternative would lose the obstruction.

First, `456` and `5<6` imply either `4<5` or `6<4`. Suppose `6<4`. Then `3<6<4`, so `345` implies either `4<5` or `5<3`. Since `5<6<4`, the first alternative is impossible, leaving

`2 < 5 < 3 < 6 < 4`.

Now `132`, together with `2<1`, requires either `1<3` or `3<2`. The latter is impossible, so `1<3`. But `146`, together with `1<4`, requires either `4<6` or `6<1`; both contradict `1<3<6<4`. Thus `6<4` is impossible and **`4<5`**.

Next, `253` and `2<5` require either `5<3` or `3<2`. If `3<2`, then

`3 < 2 < 1 < 4 < 5 < 6`.

The relation `136`, with `3<6`, requires either `1<3` or `6<1`, and this chain excludes both. Consequently **`5<3`**.

Combining the inequalities determines the entire order:

`2 < 1 < 4 < 5 < 3 < 6`.

Conversely, direct inspection shows that the circular order

**`(0,2,1,4,5,3,6)`**

satisfies every triple in S. This proves existence and uniqueness, up to rotation. ∎

## The two negative answers

**Question (1): extension.** Any extension of R would also extend S and hence have the order just proved. But R's additional triple `034` requires `3<4`, whereas that order has `4<3`. Therefore R has no circular extension, despite satisfying A and B. ∎

**Question (2): completeness.** S is extendible, and its only extension orients `043` clockwise. S contains neither `043` nor `034`. Hence S omits a triple forced by every valid extension. Indeed the unique extension contains all `C(7,3)=35` cyclic triples, while S records only seventeen, leaving eighteen missing consequences. ∎


## Reproduction and remaining scope

Run:

```sh
python3 solutions/catalog-research/circular-orders-check.py
```

Add `--write` to regenerate [the result JSON](circular-orders-checks.json). [The checker](circular-orders-check.py) uses only the Python standard library. It checks A/B directly and independently tests triples by their positions in every one of the 720 circles with 0 fixed first. Reflections remain included. It finds zero extensions for R, one for S, and eighteen missing consequences for S.

Discovery used a bounded SAT search, followed by reduction and the hand proof above. The retained verification requires no SAT solver. Exploratory solver claims about smaller sizes are not used to claim minimality.

The general Question 4.3.4 is settled negatively. The thesis's subsequent questions about ribbon-like classes, chain analogues and generating functions are separate; their present literature status was not audited here.
