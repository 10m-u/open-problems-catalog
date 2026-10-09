# Independent internal review of Q3101

Date: 2026-10-09. Reviewed file: [`../algebra/Q3101-odd-girth-obstructions.md`](../algebra/Q3101-odd-girth-obstructions.md).

**Disposition: accept the band theorem, the idempotent-subgraph extension, Lemma 7, and Corollary 8. Retain Q3101 as partial.** No unresolved mathematical defect was found. This is an internal review by a second AI research agent; it is neither external peer review nor an exhaustive novelty review.

## Source and scope

The exact Problem 7.3 was checked in the available primary PDF of [Paulista, arXiv:2511.10612v1](https://arxiv.org/pdf/2511.10612v1), printed p. 28, including a visual check of that page. Definitions and the semilattice/Rees structure statements were checked on printed pp. 3–5. The graph removes the center, and girth is the shortest cycle length of either parity. The source's even-girth construction in Theorem 3.5 uses idempotent transformation semigroups.

The draft correctly proves an obstruction for triangle-free graphs. It does not assert that the commuting graph of every band is triangle-free. Excluding bands from the odd-girth-at-least-five search leaves the source's larger class of completely regular semigroups unresolved.

## 1. The sandwich lemma for bands

For idempotents $a,c$ in a band, $t=aca$ commutes with $a$. If a middle vertex $b$ commutes with both endpoints, then $b$ commutes with $t$ by associativity and the two commutation relations. This does not require $t$ to be distinct from either endpoint in advance.

The draft explicitly closes the central-element loophole. If $t$ were central, then $tc=ct$; idempotence of the products gives

$$ac=(ac)^2=(aca)c=c(aca)=(ca)^2=ca,$$

contradicting the nonedge between the endpoints of an induced path. Thus $t$ is a graph vertex. Triangle-freeness now forces $t=a$ or $t=b$, because $a$ and $b$ are distinct adjacent noncentral elements. The second possibility again makes $t$ commute with $c$ and gives the same contradiction. Therefore $aca=a$, and the reversed argument gives $cac=c$.

No graph argument is applied to a central element, and the equality cases are handled rather than silently counted as a triangle.

## 2. Component labels and the band theorem

The source's semilattice decomposition supplies a component-label map satisfying

$$\sigma(xy)=\sigma(x)\wedge\sigma(y).$$

The two sandwich identities give both inequalities between the endpoint labels, so those labels agree. This step needs only the stated multiplicative partition; it does not require an additional unproved identification of the components with a chosen definition of Green's relation.

In a band every subgroup is trivial. Applying the Rees representation to each completely simple component therefore produces a rectangular band. In its coordinates, equality of $(i,\lambda)(j,\mu)$ and $(j,\mu)(i,\lambda)$ forces both $i=j$ and $\lambda=\mu$. Thus distinct elements in the same component do not commute.

A shortest odd cycle has no chord, since a chord would cut off a smaller odd cycle. In a triangle-free graph it has length at least five. Every consecutive length-two subpath is induced, so its endpoint labels agree. Addition by two visits every index modulo an odd cycle length; consequently every label agrees, contradicting the adjacency of distinct vertices within a rectangular component. This proves bipartiteness, including the possibility of an acyclic graph.

## 3. Completely regular extension: the equality-of-squares step

Lemma 4 is valid without assuming that $ac$ is idempotent. Put $x=ac$, $y=ca$. In a finite completely regular semigroup each belongs to a finite subgroup. Choose a positive integer $N$ divisible by both subgroup orders. The hypothesis $x^2=y^2$ gives a common power

$$h=x^{2N}=y^{2N},$$

and this is the identity for each of the two subgroups containing $x$ and $y$.

The four absorption identities follow from the displayed words and endpoint idempotence:

$$ah=h,quad hc=h,quad ch=h,quad ha=h.$$

Since $hx=x$ and $hy=y$ in their subgroups,

$$x=hac=(ha)c=hc=h,\qquad y=hca=(hc)a=ha=h.$$

Hence $x=y$. The argument does not cancel elements across different subgroups or treat the global semigroup as a group.

Now $t=aca$ in Lemma 5 may be nonidempotent, but it still commutes with $a$ and $b$. If $t$ is central or equals $b$, it commutes with $c$, which gives $(ac)^2=(ca)^2$. Lemma 4 supplies the contradiction. The sandwich identities and component-label argument therefore extend to idempotent endpoints even when the middle vertex is nonidempotent.

Within a completely simple Rees component, commuting elements must have the same row and column indices. The corresponding maximal subgroup has one idempotent. Distinct idempotents in that component consequently cannot commute, although distinct general elements may. Theorem 6 uses exactly this idempotent-only conclusion and does not overextend the rectangular-band argument.

## 4. Cycle vertices with nontrivial subgroup order

The finiteness assumption in Lemma 7 ensures that the subgroup inverse is a positive power of the original element, and conversely. The two elements therefore have equal centralizers in the entire semigroup. In particular, the inverse of a noncentral element remains noncentral.

If $x^{-1}\ne x$, they are distinct adjacent vertices. Degree at least two supplies a neighbor of $x$ different from its inverse; equality of centralizers makes it adjacent to the inverse as well. Triangle-freeness forces $x=x^{-1}$, which means subgroup order one or two.

In the order-two case, the subgroup identity $e=x^2$ differs from $x$ and commutes with every neighbor of $x$, because it is a power of $x$. If $e$ were noncentral, the same degree argument would produce a triangle. Thus $e$ belongs to the center of the **whole** semigroup, not merely its own subgroup. Every cycle vertex satisfies the degree assumption.

## 5. Corollary 8 and the number of nonidempotents

For an induced odd cycle with exactly one nonidempotent vertex, the graph on cycle indices with steps of size two is itself one cycle. Removing the exceptional index leaves a connected path through all idempotent indices. Every edge of that auxiliary path corresponds to an induced length-two path with idempotent endpoints in the original graph. Its middle vertex is allowed to be the nonidempotent vertex by Lemma 5.

All idempotent vertices thus have the same component label. Since at least two of them are adjacent in the original cycle, this contradicts the Rees-component fact above. The zero-nonidempotent case follows from Theorem 6.

The final passage from induced odd cycles to arbitrary odd cycles is also valid: repeatedly choose the odd cycle cut off by a chord. Its vertex set is a subset of the previous one, so it cannot acquire additional nonidempotent vertices. A hypothetical odd cycle with at most one therefore ends in an induced odd cycle with at most one, already excluded.

## Review boundary

The analytic proof was re-derived independently. The construction checker was not used as evidence for the universal statements, and this review does not certify any finite computational search as exhaustive beyond its declared scope. Completely regular semigroups with several noncentral involutions whose subgroup identities are central remain outside the exclusion theorem. Their possible odd girths are not resolved here, so the catalog status must remain partial.
