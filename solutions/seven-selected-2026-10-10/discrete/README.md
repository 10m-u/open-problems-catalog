# Exact partial results for Q3840 and Q3841

**Scope:** both catalog entries use status `partial`; their general questions remain unresolved. This contribution establishes the complete classifications when one specified cycle is `C_5`, and gives further positive families by graph coverings. The nonexistence claims use a small exhaustive computation over exact integers. The infinite existence claims have explicit constructive proofs.

| Catalog problem | Result proved here | Remaining scope |
| --- | --- | --- |
| Q3840 | `C_5 □ P_m` has a proper total dominating set exactly for `m = 3,5,7` or `m >= 9`. | A classification for every odd circumference `n >= 7`. |
| Q3841 | For odd `m >= 5`, `C_5 □ C_m` has such a set exactly for `m >= 7`. | A classification when both odd circumferences are at least 7. |

See [Q3840](Q3840.md), [Q3841](Q3841.md), and the [source log](sources.md). Neither proof is presented as a complete solution to its two-parameter catalog question. No claim of priority over all literature is made; the precise comparison is to the inspected sources.

## Reproduce the exact certificates

From the repository root:

```sh
python3 solutions/seven-selected-2026-10-10/discrete/verify.py
```

The verifier requires only the Python standard library. Its deterministic output is checked in as [verification.json](verification.json). It constructs all 4,310 legal states and 10,800 legal arcs directly from the definitions. It does not load a precomputed transition graph, use a numerical solver, or infer nonexistence from a timeout. Positive witnesses are separately checked against explicit graph neighborhoods.

## Definitions and exact transfer lemma

A selected set `S` is proper total dominating when every vertex has a positive number of neighbors in `S`, and adjacent vertices have different such numbers. Write this neighbor count as `sigma_S(v)`.

Index the five positions around each cycle by `i = 0,...,4`. A row is a vector in `{0,1}^5`, recording membership in `S`. All row strings in this directory list coordinates in that order. For three consecutive rows `a,b,c`, define

$$
 T(a,b,c)_i=b_{i-1}+b_{i+1}+a_i+c_i,
 \qquad i\pmod 5.
$$

This is the exact neighbor-count vector in the middle row. A triple `(a,b,c)` is **legal** if every entry of `T(a,b,c)` is positive and adjacent entries around the 5-cycle differ. Define a directed graph on all legal triples by putting an arc

$$
 (a,b,c)\longrightarrow(b,c,d)
$$

exactly when

$$
 T(a,b,c)_i\ne T(b,c,d)_i\quad\text{for all }i.
$$

There are at most `32^3 = 32768` candidate triples; all are examined. Arc generation examines every possible fourth row after matching the two overlapping rows.

**Transfer lemma.** For `m >= 1`, a proper total dominating set in `C_5 □ P_m` is equivalent to a directed walk with `m` states, whose first state has first row `0^5` and whose last state has third row `0^5`. For `m >= 3`, such a set in `C_5 □ C_m` is equivalent to a closed directed walk of length `m`.

**Proof.** Given membership rows `b_1,...,b_m` for a cylinder, set `b_0=b_{m+1}=0^5`. The `j`th state is `(b_{j-1},b_j,b_{j+1})`. Its legality is precisely positivity and properness on the horizontal edges of row `j`; the arc to the next state tests all vertical edges between these rows. At an endpoint the omitted neighbor contributes zero, exactly as prescribed. Conversely, the overlapping coordinates of a state walk recover all membership rows and all these edge tests. This also holds for `m=1`, where a single state must satisfy both boundary conditions.

For a torus, use row indices modulo `m`. Closing the state walk identifies its overlapping rows at both ends. Thus the same tests include the wraparound vertical edges. Conversely, a closed walk reconstructs these cyclic membership rows. Repeated states and arcs are allowed: they are periodic membership patterns, not an obstruction. The restriction `m >= 3` ensures the two vertical neighbors are distinct. This proves the equivalences. ∎

## A two-row insertion lemma

Let

$$
 C=10010,\qquad D=11011.
$$

If a valid cylinder or torus contains three consecutive membership rows `C,D,C`, insert any number of copies of the pair `C,D` immediately after the middle `D`. The resulting larger product also has a proper total dominating set.

**Proof.** The old middle `D` has vector

$$
 T(C,D,C)=(4,1,2,3,2).
$$

A new `C` between two `D` rows has vector

$$
 T(D,C,D)=(2,3,1,2,4).
$$

Both vectors are positive and proper around the 5-cycle, including their last-to-first entries. They differ at every coordinate. Every inserted row has one of these vectors. All old rows keep their old neighbor-count vectors: the row meeting either end of the inserted block sees the same membership row as before. The new vertical edges inside the block pass the displayed coordinatewise test; its last edge has the same endpoint vectors as the original edge. Repeating the insertion proves the assertion for any nonnegative number of pairs. For cylinders the displayed triple is internal; for tori it may cross the row-index origin. ∎

## Covering lemma

If `pi:H -> G` is a graph covering, meaning that it maps each vertex neighborhood bijectively onto the neighborhood of its image, then a proper total dominating set `S` of `G` pulls back to one of `H`.

Indeed,

$$
 \sigma_{\pi^{-1}(S)}(x)=\sigma_S(\pi(x)),
$$

and images of adjacent vertices remain adjacent. Positivity and properness therefore pull back. Reduction of the cycle coordinate modulo 5 is such a covering from `C_(5k) □ P_m` onto `C_5 □ P_m`, and from `C_(5k) □ C_m` onto `C_5 □ C_m`, for every integer `k >= 1`. The conclusions for odd circumferences use odd `k`. This lemma gives sufficient families only; nonexistence need not pull back.
