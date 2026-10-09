# Q3489: exact connected-set evaluation at −2 is #P-hard

Date: 2026-10-09. Research result, not peer reviewed. The mathematical argument is independent of the finite computations below. Historical novelty has only been checked by the bounded searches recorded at the end.

## 1. Statement, source, and result

For a finite simple undirected graph $G$, put

$$
C_G(x)=\sum_{\substack{\varnothing\ne S\subseteq V(G)\\G[S]\text{ connected}}}x^{|S|}.
$$

The empty set is excluded; a singleton is connected. The graph need not be connected. Catalog Q3489 asks whether the signed integer $C_G(-2)$, written in binary, can be computed in polynomial time.

The primary source is Lucas Mol, *On Connectedness and Graph Polynomials* (Dalhousie PhD thesis, 2016), §6.4, printed p. 166. Its immediately stated question is “Can nRel(G; 2) be found in polynomial time?” The identity

$$
\operatorname{nRel}(G;2)=(-1)^{|V(G)|}C_G(-2)
$$

makes this exactly equivalent to the catalog formulation. The same paragraph asks about connected-set evaluation at the remaining points $z$ for which $z+1$ is a root of unity. Theorem 4.1.2, printed pp. 91–92, already proves #P-hardness when $z\ne-1$ and $z+1$ is not a root of unity. That existing theorem, and the #P-completeness of counting connected induced vertex subsets, are background; they are not new claims of this note. [M, SSS]

**Theorem 1.** Exact evaluation of $C_G(-2)$ is #P-hard under polynomial-time Turing reductions. In fact there is an explicit polynomial-size, single-oracle-call reduction from counting connected induced vertex subsets to this evaluation. The evaluation belongs to GapP and is computable in polynomial time if and only if FP = #P.

The conclusion is a standard counting-complexity classification. It does not prove the unresolved separation FP ≠ #P. Because the evaluation can be negative, this note does not call it a #P-complete function.

**Theorem 2.** More generally, for every fixed algebraic number $z\ne0$, exact evaluation of $C_G(z)$ is #P-hard under polynomial-time Turing reductions. Here output is represented exactly in a fixed number field containing $z$. Evaluation at $z=0$ is identically zero. Thus the additional root-of-unity question in the source also has a complexity classification. The restriction to algebraic numbers specifies an ordinary finite bit model of exact computation.

## 2. The pendant-leaf identity and Q3489

Let $L(G)$ be obtained from $G$ by adjoining one new degree-one vertex $v'$ adjacent to each old vertex $v$. Write $n=|V(G)|$. Then

$$
\boxed{C_{L(G)}(x)=n x+C_G\bigl(x(1+x)\bigr).}\tag{1}
$$

To prove (1), classify each nonempty connected vertex set $T\subseteq V(L(G))$ by its intersection $S$ with the original vertex set. If $S=\varnothing$, the set consists of one new leaf, giving the term $nx$. If $S\ne\varnothing$, no leaf whose parent is outside $S$ can occur in $T$. Moreover $G[S]$ must be connected, since degree-one vertices cannot connect two original vertices. Conversely, any connected nonempty $S$ and any subset of its incident new leaves give a connected $T$. The sum of their weights is $x^{|S|}(1+x)^{|S|}$. Summing over $S$ proves (1).

At $x=-2$, this gives

$$
\boxed{C_G(2)=C_{L(G)}(-2)+2n.}\tag{2}
$$

The transformation uses $2n$ vertices and $m+n$ edges. Both the construction and the additive correction have polynomial bit complexity. By the source's already established #P-hardness at $2$, equation (2) proves Theorem 1's hardness claim.

### A complete one-call reduction, without relying on the source's interpolation

For completeness, let $G[K_k]$ denote the graph formed by replacing each vertex with a $k$-clique and replacing every original edge with all $k^2$ edges between its endpoint cliques. A selected set is connected exactly when the set of nonempty selected cliques induces a connected graph in $G$. Inside each such clique every nonempty subset is allowed. Therefore

$$
C_{G[K_k]}(x)=C_G\bigl((1+x)^k-1\bigr).\tag{3}
$$

This familiar identity also appears as the special case of [M, Lemma 4.1.1]. Its short proof here fixes the precise convention used by the reduction.

On input $G$ of order $n\ge1$, choose $k=n+1$, construct

$$
H=L\bigl(G[K_k]\bigr),\qquad b=3^k-1,
$$

and query the $-2$-evaluation oracle once. Equations (2)–(3) yield

$$
Y=C_H(-2)+2nk=C_G(b)=\sum_{j=1}^n c_jb^j,
$$

where $c_j$ is the number of connected $j$-vertex sets of $G$. Since

$$
0\le c_j\le {n\choose j}\le2^n<b,
$$

the base-$b$ digits of $Y$ are exactly $c_0=0,c_1,\ldots,c_n$. Repeated integer division by $b$, followed by summing the digits, recovers $C_G(1)$. There are $2n(n+1)$ vertices in $H$, at most $O(n^4)$ edges, $O(n)$ bits in $b$, and $O(n^2)$ bits in $Y$. The construction, oracle output, and decoding all have polynomial size. The empty graph is handled separately by returning zero.

Counting connected induced vertex subsets is #P-complete [SSS]. Consequently the displayed map is a polynomial-time metric reduction from that counting problem to the signed evaluation. No numerical approximation or interpolation conditioning enters this reduction.

### Upper bound and the exact conditional answer

Define $E(G)$ and $O(G)$ by summing $2^{|S|}$ over connected subsets of even and odd order, respectively. Both are #P functions: guess $S$, check its connectivity and parity in polynomial time, then make one independent nondeterministic binary choice per selected vertex. Thus

$$
C_G(-2)=E(G)-O(G)\in\mathrm{GapP}.
$$

There are at most $n$ bits needed to guess $S$, and at most $n$ further branching bits; padding can keep computation paths at equal length if desired. Also $|C_G(-2)|\le3^n-1$, so the signed binary output has $O(n)$ bits.

If the evaluation is in FP, hardness puts every #P function in FP. Conversely, if FP = #P, the two counts $E(G)$ and $O(G)$, and hence their difference, are computable in polynomial time. This proves the stated equivalence.

## 3. A general rooted-attachment identity

Fix a finite rooted graph $(F,r)$. For every old vertex $v$ of $G$, take a disjoint copy of $F$ and identify its root with $v$. Keep all edges of $G$, and add no other edges between different copies. Denote the result by $G\star(F,r)$. Define the root-containing polynomial

$$
R_{F,r}(x)=\sum_{\substack{r\in U\subseteq V(F)\\F[U]\text{ connected}}}x^{|U|}.
$$

Then

$$
\boxed{C_{G\star(F,r)}(x)=C_G\bigl(R_{F,r}(x)\bigr)+nC_{F-r}(x).}\tag{4}
$$

If a connected selected set contains no old vertex, it lies in a single copy of $F-r$; the contribution of all such sets is $nC_{F-r}(x)$. Otherwise, its selected old vertices form a nonempty connected set $S\subseteq V(G)$. In each copy attached at $v\in S$, the selected vertices must induce a connected set containing the root. A disconnected local piece could not reach any other copy, because the root is its sole point of attachment. Conversely every such collection of rooted connected sets gives a connected global set. Their weight, summed over local choices, is $R_{F,r}(x)^{|S|}$. This proves (4).

Since $F$ is fixed, (4) gives a one-call polynomial-time reduction from evaluation at $R_{F,r}(z)$ to evaluation at $z$. It applies equally to disconnected $G$.

## 4. The exceptional point −1

Use $F=C_5$, rooted at any vertex. For a proper connected $j$-vertex subset of the cycle containing the root there are exactly $j$ choices, for $1\le j\le4$. There is one choice using the whole cycle. Thus

$$
R_{C_5,r}(x)=x+2x^2+3x^3+4x^4+x^5,
\qquad R_{C_5,r}(-1)=1.
$$

Deleting the root leaves a four-vertex path, with polynomial

$$
C_{P_4}(x)=4x+3x^2+2x^3+x^4,
\qquad C_{P_4}(-1)=-2.
$$

Equation (4) now gives the explicit relation

$$
\boxed{C_{G\star(C_5,r)}(-1)=C_G(1)-2n.}\tag{5}
$$

This graph has $5n$ vertices and $m+5n$ edges. It follows directly from [SSS] that evaluation at $-1$ is #P-hard. As with $-2$, its natural upper bound is GapP, since it is the difference between the numbers of connected subsets of even and odd order.

## 5. The remaining root-of-unity points

We give the complete reduction for Theorem 2. The established hard region is

$$
z\ne-1\quad\text{and}\quad z+1\text{ is not a root of unity}.\tag{6}
$$

It remains to consider $z=\zeta-1$, where $\zeta$ is a root of unity. The case $\zeta=1$ is $z=0$, the easy point. Suppose henceforth $\zeta\ne1$.

Attaching one leaf implements

$$
w=z(1+z)=\zeta^2-\zeta,
\qquad w+1=\zeta^2-\zeta+1.
$$

Since $|\zeta|=1$,

$$
w+1=\zeta\bigl(2\operatorname{Re}\zeta-1\bigr),
\quad |w+1|=|2\operatorname{Re}\zeta-1|.\tag{7}
$$

If the right-hand side is neither $0$ nor $1$, then $w\ne-1$ and $w+1$ cannot be a root of unity, so (6) applies. If it is zero, then $w=-1$, which is hard by (5); this covers the primitive sixth roots $\zeta=e^{\pm i\pi/3}$.

The remaining possibility $|2\operatorname{Re}\zeta-1|=1$ forces $\operatorname{Re}\zeta=1$ or $0$. The former is the excluded $\zeta=1$. The latter gives $\zeta=\pm i$. At those two points attach two independent leaves to every old vertex. The rooted gadget is the three-vertex star rooted at its center, so

$$
w=z(1+z)^2=-z=1-\zeta,
\qquad |w+1|=|2-\zeta|=\sqrt5.
$$

Thus $w$ belongs to the established hard region (6). The correction term in (4) is $2nz$. This covers every remaining exceptional point and proves Theorem 2.

### Exact arithmetic for the generic hard region

To avoid relying on an informal complex-number model, fix an algebraic $w$ satisfying (6), and represent field elements in a fixed rational basis of $\mathbb Q(w)$. Let $\alpha_j=(1+w)^j-1$ for $j=1,\ldots,n$. These are nonzero and pairwise distinct because $1+w\ne0$ is not a root of unity. Equation (3), together with the known value $C_G(0)=0$, determines the degree-at-most-$n$ polynomial $C_G$ from the oracle values at these $n$ points. Vandermonde interpolation over the fixed field recovers $C_G(1)$. The powers $\alpha_j$, graph sizes, and field-coordinate bit lengths are polynomial in $n$; exact rational linear algebra has polynomial bit complexity. This proves the version of (6) used here in the usual bit model.

For fixed algebraic $z$, an upper bound in FP$^{\#P}$ follows by counting the $n$ coefficients and combining them with $1,z,\ldots,z^n$. No claim about exact evaluation at an arbitrary uncomputable complex constant is intended.

## 6. Independent computational controls

`verify_connected_set.py` directly enumerates nonempty subsets in the actual constructed graphs. It does not use the attachment formula to obtain the left sides being checked. It compares complete integer coefficient vectors against polynomial composition on the right sides.

The checks cover the pendant-leaf identity for all labeled graphs through five vertices; the rooted-$C_5$ attachment identity for all labeled graphs through three vertices; clique-substitution identities and the full one-call digit-decoding reduction on small graphs; and 440 exact rational checks of the norm calculation in (7). All 1,100 pendant-leaf graphs, 12 two-leaf graphs, 12 rooted-cycle graphs, 152 clique-substitution graphs, three complete single-call reductions, and 440 norm checks passed. The companion JSON records these counts and the single-call examples. Finite checks are controls for construction and convention errors, not substitutes for the proofs.

## 7. Sources and literature boundary

**[M]** Lucas Mol. *On Connectedness and Graph Polynomials*. PhD thesis, Dalhousie University, 2016. Primary PDF: <https://central.bac-lac.gc.ca/.item?app=Library&id=TC-NSHD-71408&oclc_number=1033184059&op=pdf>. Alternate institutional locator: <https://dal.scholaris.ca/bitstreams/42938e10-2ef1-4c00-a222-139c7449c91b/download>. Inspected the full primary PDF text, especially definitions in Chapter 4, Lemma 4.1.1 (printed p. 89), Theorem 4.1.2 (pp. 91–92), and §6.4 (p. 166), on 2026-10-09. Some direct URL opens initially failed; opening the indexed Canadian-library result subsequently returned the complete 184-page PDF text. The institutional alternate returned a fetch error.

**[SSS]** K. Sutner, A. Satyanarayana, C. Suffel. *The Complexity of the Residual Node Connectedness Reliability Problem*. SIAM Journal on Computing 20(1), 149–155 (1991). DOI: <https://doi.org/10.1137/0220009>. The publisher's abstract was inspected at <https://epubs.siam.org/doi/abs/10.1137/0220009> on 2026-10-09. It explicitly states #P-completeness of counting connected induced vertex subgraphs, including split graphs and planar bipartite graphs. The original proof in the paywalled full article was not re-derived here. Only the unrestricted established hardness theorem is used.

Bounded literature searches on 2026-10-09 used both available search engines with phrases including `"connected set polynomial" "-2" complexity`, `"connected set polynomial" corona`, `"connected set polynomial" "minus two"`, `"connected set polynomial" "root of unity"`, `"connected set polynomial" "hard" "-1"`, and `"connected set polynomial" "dichotomy"`. Results returned the thesis, graph-polynomial root studies, connected-set enumeration papers, and unrelated graph-corona results. No publication resolving the exceptional evaluations was located. This is a bounded search result, not a proof of priority. The algebraic identities and reductions can be assessed independently of historical novelty.
