# Independent internal review: Q3102

**Date:** 2026-10-09.

**Reviewer:** Separate combinatorics research agent; did not develop the submitted argument.

**Artifact:** [Q3102-no-knit-degree-three.md](../algebra/Q3102-no-knit-degree-three.md).

**Verdict:** The mathematical proof is accepted at its stated finite completely regular scope. No gap was found. This is internal AI review, not external peer review or formal verification.

## 1. Independent source check

The reviewer independently retrieved the complete 29-page author PDF at [arXiv:2511.10612](https://arxiv.org/pdf/2511.10612), whose first page identifies version 1 and the date 13 November 2025.

- Printed p. 4, §2.2: the graph's vertices are precisely the noncentral semigroup elements; a left path has distinct endpoints, and the two endpoints have equal left products with **every** vertex on the path, including both endpoints.
- Printed p. 4, Theorem 2.1: completely regular means that every element belongs to a subgroup of the semigroup.
- Printed p. 27, Theorem 6.3: the source excludes knit degree one for finite completely regular semigroups.
- Printed p. 28, Problem 7.4: the exact question asks whether a finite noncommutative completely regular semigroup has knit degree three.

The proof addresses the exact last question: a length-three left path is transformed into a valid length-two left path. Its centrality checks are necessary because the graph does not include central elements. No connectedness of the whole graph is required by the source or the proof.

## 2. Endpoint reduction

The original path $a-b-c-d$ supplies $a^2=da$ and $ad=d^2$, as well as equal left products on $b$ and $c$. Associativity alone then gives

$$
a^i d^j=d^{i+j},\qquad d^i a^j=a^{i+j}
$$

for positive $i,j$. These equations were checked without commuting $a$ and $d$ or introducing a global identity.

A common positive multiple $N$ of the finite orders of $a$ and $d$ inside their own subgroups gives idempotents $e=a^N$ and $f=d^N$. The equations imply $ef=f$ and $fe=e$. If $e=f$, then $a=af=d^{N+1}=d$, which contradicts the distinct original endpoints. Thus $e\ne f$, and the equations show that both new endpoints are noncentral.

The implication $ax=dx\Rightarrow a^k x=d^k x$ uses the displayed mixed-power identity and is valid for $x=b,c$. Consequently the proof correctly obtains $eb=fb$ and $ec=fc$. The commutation of $e$ with $b$ and of $f$ with $c$ follows by taking powers of elements already known to commute.

## 3. Interior idempotent calculation

Let $u$ be the subgroup identity obtained as a positive power of $b$. The argument correctly uses

$$
u^2=u,\quad bu=ub=b,\quad eu=ue=fu,\quad uc=cu.
$$

Set $p=eu=fu$ and $q=uf$. The reviewer rederived

$$
p^2=p,\quad q^2=q,\quad pq=q,\quad qp=p.
$$

For example, $q^2=ufuf=u(eu)f=euf=uef=uf$, and $qp=ufeu=ueu=eu$. These calculations do not assume that $u$ and $f$ commute. That commutation is obtained only in the later case $p=q$.

Both $p$ and $q$ commute with $c$, since each is a product of $u$ and $f$, both of which commute with $c$. Finally $pc=euc=uec=ufc=qc$. The distinction between equality of left products and commutation is maintained correctly.

## 4. All cases produce permitted graph vertices

| Case | New path | Independent checks |
|---|---|---|
| $p\ne q$ | $p-c-q$ | The unequal products $pq=q$ and $qp=p$ make $p,q$ noncentral. The original $c$ is noncentral and commutes with each. Equality of $c$ with either endpoint would force $p,q$ to commute, so all three vertices are distinct. The three left-product requirements follow from $p^2=qp$, $pc=qc$, and $pq=q^2$. |
| $p=q$, $u$ noncentral | $e-u-f$ | Equality $p=q$ gives $fu=uf$, while $eu=ue$ was already known. Noncommuting $e,f$ cannot equal a vertex commuting with both. The endpoint equations are $e^2=fe$ and $ef=f^2$; the middle equation is $eu=fu$. |
| $p=q$, $u$ central | $e-b-f$ | Centrality of $u$ and $bu=b$ give $bf=buf=bfu=beu=be=eb=fb$. Thus the original noncentral $b$ commutes with both endpoints. It is distinct from them because they do not commute with each other. The same endpoint equations and $eb=fb$ supply the left-path condition. |

The last case is essential: using the central $u$ itself as a graph vertex would be invalid. The argument explicitly replaces it with the original noncentral $b$ and proves the needed extra commutation. The three cases are exhaustive.

## 5. Scope and conclusion

The proof uses complete regularity only through finite subgroup powers and subgroup identities. It makes no cancellation across different subgroups and no assumption that local identities are global or central. Finiteness supplies the positive exponents used to obtain the identities. The conclusion is therefore warranted for the exact finite source problem; no conclusion about arbitrary regular semigroups or infinite subgroups was inferred.

A semigroup with knit degree three would have a length-three left path and no length-two left path. The proved transformation contradicts that combination. The correct catalog interpretation is a **proposed complete negative answer** to the existence question, not a counterexample semigroup and not an assertion that all finite completely regular semigroups have knit degree two.

The mathematical acceptance does not depend on finite-model searches or an SMT unsatisfiability result. Separate computational controls are supplementary and are recorded with the algebra packet.
