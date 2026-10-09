# Q3101: odd-cycle obstructions for bands and completely regular semigroups

Date: 2026-10-09. Status: **proved partial result; the full catalog question remains open**.

## Authoritative target and what is proved

Q3101 is Problem 7.3, printed p. 28, of Tânia Paulista, *Commuting graphs of inverse semigroups and completely regular semigroups*, arXiv:2511.10612v1 (13 November 2025). It asks whether every odd integer at least three occurs as the girth of the commuting graph of a finite noncommutative completely regular semigroup.

Source: <https://arxiv.org/pdf/2511.10612>. Definitions appear on pp. 3–5, and the even-girth construction is Theorem 3.5, pp. 16–20. **Girth means the length of the shortest cycle of any parity**, not the shortest odd cycle. The graph omits central elements.

This contribution proves:

1. The commuting graph of a finite band, if triangle-free, is bipartite. Consequently, no band realizes an odd girth at least five.
2. More generally, in a triangle-free commuting graph of a finite completely regular semigroup, the subgraph induced by the noncentral idempotents is bipartite.
3. Every nonidempotent vertex on a cycle of such a triangle-free graph is an involution in its subgroup, and that subgroup's identity is central in the whole semigroup.
4. Any odd cycle in such a graph contains at least two nonidempotent vertices.

A band is a semigroup in which every element is idempotent. The even-girth examples in Paulista's Theorem 3.5 are bands, so the first theorem rules out obtaining an odd girth merely by changing parameters in that subclass. It does not rule out all completely regular semigroups.

## 1. A direct proof for bands

**Lemma 1.** Let $B$ be a band, and let $a,c\in B$. If $aca$ is central, or if $aca$ commutes with $c$, then $ac=ca$.

**Proof.** In either case $(aca)c=c(aca)$. Since every element of $B$, including $ac$ and $ca$, is idempotent,

$$
ac=(ac)^2=(aca)c=c(aca)=(ca)^2=ca.
$$

$\square$

**Lemma 2.** Suppose the commuting graph of a band $B$ has no triangle. If $a-b-c$ is an induced path of length two, then

$$
aca=a,\qquad cac=c.
\tag{1}
$$

Here the vertices are noncentral and pairwise distinct, and being induced says $ac\ne ca$.

**Proof.** Set $t=aca$. It commutes with $a$ by idempotence, and with $b$ because $b$ commutes with both $a$ and $c$. It is noncentral by Lemma 1. If $t$ differed from both $a$ and $b$, these three noncentral commuting elements would give a triangle. Therefore $t=a$ or $t=b$. The latter is impossible: $b$ commutes with $c$, so Lemma 1 would imply $ac=ca$. Hence $aca=a$. Interchanging $a$ and $c$ proves the other identity. $\square$

For the next step we use the standard decomposition of a band into a semilattice of rectangular bands. This follows from the completely regular structure theorem and the Rees matrix characterization quoted as Theorems 2.2–2.3 on p. 5 of the primary source: the subgroup of a band at any idempotent is trivial. Thus there is a semilattice $Y$ and a partition

$$
B=\bigsqcup_{\alpha\in Y}B_\alpha,\qquad
B_\alpha B_\beta\subseteq B_{\alpha\wedge\beta},
$$

where each $B_\alpha$ is a rectangular band. Write $\sigma(x)=\alpha$ for $x\in B_\alpha$. In a rectangular band the multiplication has the form

$$
(i,\lambda)(j,\mu)=(i,\mu).
$$

Consequently, two distinct elements in the same rectangular band cannot commute.

If $a,c$ satisfy (1), then

$$
\sigma(a)=\sigma(aca)=\sigma(a)\wedge\sigma(c),\qquad
\sigma(c)=\sigma(cac)=\sigma(a)\wedge\sigma(c).
$$

Therefore $\sigma(a)=\sigma(c)$.

**Theorem 3.** A triangle-free commuting graph of a finite band is bipartite.

**Proof.** Suppose it has an odd cycle. Choose one of minimum odd length, denoted

$$
x_0-x_1-\cdots-x_{n-1}-x_0.
$$

It has no chord: a chord would divide an odd cycle into two cycles, one odd and shorter. Because the graph is triangle-free, $n\geq5$. Lemma 2 applied at each vertex gives

$$
\sigma(x_i)=\sigma(x_{i+2})\qquad(i\bmod n).
$$

Since $n$ is odd, repeatedly adding two modulo $n$ visits every index. Thus all cycle vertices lie in one rectangular component. Adjacent distinct vertices in that component cannot commute, a contradiction. The graph therefore has no odd cycle and is bipartite. $\square$

In particular, if the finite girth of a band's commuting graph is not three, it is even.

## 2. Extension to idempotents inside completely regular semigroups

The preceding sandwich argument can be extended without assuming that products of idempotents remain idempotent.

**Lemma 4.** Let $a,c$ be idempotents in a finite completely regular semigroup $S$. If

$$
(ac)^2=(ca)^2,
\tag{2}
$$

then $ac=ca$.

**Proof.** Put $x=ac$ and $y=ca$. Let $N$ be divisible by their subgroup orders. By (2),

$$
h=x^{2N}=y^{2N}
$$

is the identity of the subgroup containing $x$ and also of the subgroup containing $y$. The expression $h=(ac)^{2N}$ gives $ah=h$ and $hc=h$; the expression $h=(ca)^{2N}$ gives $ch=h$ and $ha=h$. Hence

$$
x=hx=hac=hc=h,
\qquad
y=hy=hca=ha=h.
$$

So $x=y$. $\square$

**Lemma 5.** Suppose $S$ is finite and completely regular and its commuting graph has no triangle. If $a-b-c$ is an induced path and $a,c$ are idempotents, then $aca=a$ and $cac=c$. The middle vertex $b$ need not be idempotent.

**Proof.** The element $t=aca$ commutes with $a$ and $b$, just as before. If $t$ were central, it would commute with $c$, yielding (2), contrary to $ac\ne ca$ and Lemma 4. Thus $t$ is noncentral. Triangle-freeness forces $t=a$ or $t=b$. The second option also makes $t$ commute with $c$, giving the same contradiction. This proves $aca=a$; interchange $a,c$ for the other identity. $\square$

Use the semilattice decomposition of $S$ into completely simple components from the source's Theorem 2.3. Lemma 5 again implies that its endpoint idempotents belong to the same component. In the Rees representation

$$
(i,g,\lambda)(j,h,\mu)=(i,gp_{\lambda j}h,\mu),
$$

commuting elements must have the same row and column indices. Each such subgroup has exactly one idempotent. Hence **two distinct idempotents in a single completely simple component cannot commute**.

**Theorem 6.** In a triangle-free commuting graph of a finite completely regular semigroup, the induced subgraph on noncentral idempotents is bipartite.

**Proof.** Apply the minimum-odd-cycle argument from Theorem 3 inside that induced subgraph. Lemma 5 identifies the component labels of vertices two steps apart. Oddness identifies all component labels, contradicting the last paragraph. $\square$

## 3. Necessary nontrivial subgroups in any remaining odd-girth example

**Lemma 7.** Let $x$ be a noncentral vertex of degree at least two in a triangle-free commuting graph of a finite completely regular semigroup. Either $x$ is idempotent, or $x$ has subgroup order two and $x^2\in Z(S)$.

**Proof.** The subgroup inverse $x^{-1}$ is a positive power of $x$, and conversely $x$ is a positive power of $x^{-1}$. Thus $x$ and $x^{-1}$ have the same centralizer; in particular, $x^{-1}$ is noncentral. If $x^{-1}\ne x$, choose a neighbor $y$ of $x$ different from $x^{-1}$, using the degree assumption. The three vertices $x,x^{-1},y$ form a triangle. Therefore $x=x^{-1}$, so its subgroup order is one or two.

Order one means that $x$ is idempotent. In order two, let $e=x^2\ne x$. The element $e$ commutes with $x$ and with all neighbors of $x$. If $e$ were noncentral, choose a neighbor different from $e$ to obtain another triangle. Thus $e$ is central. $\square$

**Corollary 8.** Any odd cycle in a triangle-free commuting graph of a finite completely regular semigroup contains at least two nonidempotent vertices. Each such vertex has subgroup order two and a central subgroup identity.

**Proof.** Choose an odd cycle of minimum length $n\geq5$, so it is induced. If all its vertices are idempotent, Theorem 6 is a contradiction. If exactly one vertex is nonidempotent, form the auxiliary cycle on the $n$ indices with edges joining $i$ to $i+2$ modulo $n$. Since $n$ is odd, this is a single cycle. Deleting the index of the nonidempotent vertex leaves a path connecting every remaining index. Lemma 5 identifies the component labels along every edge of this path, even when the middle vertex of the original length-two path is the deleted nonidempotent vertex. All $n-1$ idempotents therefore lie in the same completely simple component. Some two of them are adjacent on the original cycle, a contradiction.

Thus the minimum odd cycle has at least two nonidempotent vertices. The same conclusion holds for any odd cycle with at most one nonidempotent vertex: repeatedly taking the odd part cut off by a chord would produce a shorter odd cycle still with at most one. Lemma 7 applies to each nonidempotent cycle vertex because it has degree at least two. $\square$

## 4. Limits, prior work, and reproducibility

These results exclude every finite band and sharply restrict where an odd cycle can occur in a completely regular semigroup. They do **not** exclude odd cycles involving several elements of order two with central subgroup identities. No example of odd girth at least five is constructed here, and no universal impossibility theorem for the full class is claimed.

The number three is already a possible girth in the source. The new obstruction concerns odd values at least five. The bounded literature check also located Ajmal Ali, *On large arbitrary girth of a semigroup*, New Trends in Mathematical Sciences 6(1) (2018), 18–23, which constructs even-girth bands; it does not state the obstruction proved above. Its title should not be read as an odd-girth realization result:

- <https://doi.org/10.20852/ntmsci.2018.241>
- <https://www.ntmsci.com/ajaxtool/GetArticleByPublishedArticleId?PublishedArticleId=8379>

The source and the accessible preceding papers checked are recorded in `SOURCES.md`; no claim of exhaustive novelty is made. The complete proofs above supply the evidence for the stated partial results.

`verify_semigroups.py` constructs finite bands with girths 4, 6, 8, and 10 from Paulista's transformation construction, checks associativity and idempotence, computes girth independently by breadth-first search, and verifies every applicable sandwich identity in these examples. The bounds and counts are recorded in `verification.json`. The script also includes the general-semigroup nilpotent realization of a 5-cycle as an outside-hypothesis control: a graph-only or unrestricted-semigroup argument must not falsely exclude that example.
