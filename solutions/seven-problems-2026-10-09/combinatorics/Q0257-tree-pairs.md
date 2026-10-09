# Q257: strict separation, exact small slices, and a finite witness bound

**Date:** 2026-10-09.

**Result type:** Proposed partial theorems; the general realizability question remains open.

**Verification level:** Exact finite controls and internal mathematical review; not peer reviewed.

## 1. Source question and conventions

Q257 asks which pairs $(a,b)$ occur as

$$
(\gamma_t(T),\gamma_{pt}(T))
$$

for a finite tree $T$ possessing a proper total dominating set. The source is Sawyer Isaac Osborn, *From Total Domination to Graph Coloring* (2026), Problem 4.3.10, printed p. 76. The same question appears as Question 3 of §5 in Osborn–Zhang, [*Proper Total Domination in Trees*](https://doi.org/10.3390/sym17091429), **Symmetry** 17 (2025), 1429.

Both parameters use open neighborhoods: a total dominating set $S$ satisfies $\sigma_S(v)=|N(v)\cap S|>0$, and a proper one also has unequal sums at adjacent vertices. A tree with no proper set does not produce a finite pair.

The source already determines several tree families and all trees with proper total domination number at most 8. The later [Chartrand–Salehi–Zhang paper](https://doi.org/10.47443/dml.2026.029), *Discrete Mathematics Letters* 17 (2026), 37–44, treats unrestricted connected graphs and an additional upper proper-total parameter; it does not solve the tree-pair question. Accordingly, the small constructions below are not advertised as new tree families. The additions are self-contained exclusions for fixed total domination number, a strict inequality for every tree, and a finite witness bound preserving both parameters. See [SEARCH-LOG.md](SEARCH-LOG.md) for bounded literature coverage.

## 2. Every tree has strict separation

**Theorem 1.** If a finite tree $T$ has a proper total dominating set, then

$$
\gamma_t(T)+1\le\gamma_{pt}(T). \tag{1}
$$

**Proof.** Let $S$ be any proper total dominating set. The induced forest $T[S]$ has no isolated vertices, because vertices in $S$ themselves require neighbors in $S$. It has a leaf $u$, so $\sigma_S(u)=1$. Every neighbor $w$ of $u$ in $T$ has positive neighbor sum different from 1, hence $\sigma_S(w)\ge2$. Removing $u$ therefore leaves all its neighbors dominated; every other vertex has unchanged neighbor sum. Thus $S\setminus\{u\}$ is total dominating. Apply this to a minimum proper set. ∎

In particular, no diagonal pair $(a,a)$ is realizable by a tree. This differs from the unrestricted graph problem, where diagonal pairs can occur.

## 3. A structural observation about connected total dominating sets

**Lemma 2.** If $D$ is a total dominating set of a tree and $T[D]$ is connected, then every vertex outside $D$ is a leaf attached to a vertex of $D$.

**Proof.** Every outside vertex has a neighbor in $D$. It cannot have two such neighbors, since their path inside the connected tree $T[D]$ would create a cycle. Two outside vertices cannot be adjacent: their respective neighbors in $D$, together with that edge and a path inside $T[D]$, would again create a cycle (including the case of the same neighbor). Thus each outside vertex has exactly its one neighbor in $D$. ∎

## 4. The complete slice a = 2

**Theorem 3.** The pairs with $a=2$ are exactly

$$
(2,3),\qquad(2,5). \tag{2}
$$

**Proof.** A two-vertex total dominating set consists of adjacent vertices. Lemma 2 implies that the tree is $K_2$, a star, or a double star.

The tree $K_2$ has no proper set. For a star with at least two leaves, the center is forced into every total dominating set. A proper set must select at least two leaves, because the center's sum must differ from the leaf sum 1. Selecting the center and two leaves works, so its pair is $(2,3)$.

For a genuine double star, let $u,v$ be its adjacent non-leaf vertices, with $p,q\ge1$ leaves respectively. Both $u,v$ are forced into every total dominating set. If $y,z$ leaves are selected on the two sides, their sums are $1+y,1+z$. Properness is exactly

$$
y,z\ge1,\qquad y\ne z.
$$

Such a choice exists precisely when $\max(p,q)\ge2$, and its minimum has $y+z=3$. The proper parameter is therefore 5. If $p=q=1$, the tree is $P_4$, which has no proper set. This proves necessity and gives examples for both pairs. ∎

## 5. The complete slice a = 3

For integers $p,r\ge1$ and $q\ge0$, let $C(p,q,r)$ be the caterpillar with three-vertex spine $u,v,w$, with respectively $p,q,r$ pendant leaves.

**Theorem 4.** Every tree with $\gamma_t(T)=3$ is a tree $C(p,q,r)$. Among them:

$$
\gamma_{pt}(C(p,q,r))=
\begin{cases}
6,&q\ge1,\\
7,&q=0\text{ and }p,r\ge2,
\end{cases} \tag{3}
$$

and there is no proper total dominating set if $q=0$ and $\min(p,r)=1$. Thus the complete slice is

$$
(3,6),\qquad(3,7). \tag{4}
$$

**Proof.** A three-vertex total dominating set induces an isolate-free forest on three vertices, necessarily $P_3$. Lemma 2 says that all remaining vertices are leaves attached to this path. Each endpoint of the path must have at least one attached leaf; otherwise the tree is a star or double star and has a two-vertex total dominating set. Conversely, every $C(p,q,r)$ has the spine as a three-vertex total dominating set. Its diameter is 4, so it cannot have a two-vertex total dominating set: a dominating edge would put any two vertices at distance at most 3. Its total parameter is exactly 3.

Suppose $q\ge1$. All three spine vertices are support vertices, so all are selected in a proper set. Each outer support needs at least one selected leaf. Those two leaves alone would give all three spine sums the value 2 and would be improper. At least three leaves in total are therefore required. Selecting one leaf at each spine vertex gives sums $(2,3,2)$ and is proper. Thus the minimum is 6.

Suppose $q=0$. The two outer supports $u,w$ are selected, so $\sigma_S(v)=2$. Each outer support has a leaf neighbor with sum 1 and is adjacent to $v$, so its sum must be at least 3. If $v$ is selected, at least two leaves on each outer support are required, giving minimum size $3+2+2=7$; that choice works whenever $p,r\ge2$. If $v$ is unselected, at least three leaves at each support are needed, giving size at least 8 and requiring $p,r\ge3$. This cannot give feasibility in any additional case or improve the size-7 construction. The asserted classification follows. ∎

Examples realizing (2) and (4) are the leaf words $(2)$, $(1,2)$, $(1,1,1)$, and $(2,0,2)$, respectively.

## 6. A finite representative for every realizable pair

The next result gives a uniform finite search space for any fixed $a$. It is deliberately a coarse bound; no sharpness is asserted.

For a tree on at least three vertices, its **core** $H$ is the tree induced by its non-leaf vertices. A **support** is a core vertex adjacent to one or more leaves of the original tree.

**Lemma 5.** If $\gamma_t(T)=a$, then the core has at most $2a-2$ vertices.

**Proof.** Fix a minimum total dominating set $D$, and let $c$ be the number of components of $T[D]$. Its components have at least two vertices, so $c\le a/2$. Let $R$ be the non-leaf vertices outside $D$, with $r=|R|$. Delete the leaves outside $D$, then contract each component of $T[D]$. The result is a tree on $c+r$ vertices.

Each vertex of $R$ is adjacent to a contracted $D$-component, since $D$ is total dominating. Each also retains degree at least 2: a leaf outside $D$ could not have had its unique neighbor outside $D$. Let $m$ count edges from $R$ to the contracted components and let $e$ count edges within $R$. There are no edges between distinct contracted $D$-components. Therefore

$$
m+e=c+r-1,\quad m\ge r,\quad m+2e\ge2r.
$$

The first two inequalities give $e\le c-1$, and the first and third give $r\le c-1+e\le2c-2$. Hence the number of non-leaf vertices is at most

$$
a+r\le a+2c-2\le2a-2.
$$

The argument also covers $c=1,r=0$. ∎

**Lemma 6.** At a support vertex $v$, put $d=\deg_H(v)$. Deleting pendant leaves at $v$ beyond $d+2$, at every support simultaneously, preserves both $\gamma_t$ and $\gamma_{pt}$, including the absence of a proper set.

**Proof.** Let $S$ be a minimum proper set in the original tree, if one exists. Write $s=|N_H(v)\cap S|$ and let $y$ be its selected leaves at $v$. If $y>d+2$, consider the $d+1$ candidate sums

$$
q'\in\{\max(2,s),\max(2,s)+1,\ldots,\max(2,s)+d\}.
$$

Each corresponds to an available nonnegative leaf count $y'=q'-s\le d+2<y$. At most $d$ core neighbors forbid these sums. At least one candidate is consequently distinct from all neighboring core sums, and every candidate differs from the pendant-leaf sum 1. Replacing the selected leaves at $v$ by $y'$ changes only $\sigma_S(v)$, so it gives a smaller proper set, a contradiction. Thus every minimum proper set selects at most $d+2$ leaves at each support.

The reduced tree retains at least one leaf at every original support, so supports are forced into all its total dominating sets. A proper set on the reduced tree extends to the original by leaving deleted leaves unselected. A minimum proper set on the original transfers to the reduced tree by relabeling its selected leaves among the retained ones. Feasibility and the minimum proper size therefore agree.

For ordinary total domination, a minimum set selects at most one leaf at a support: if it selected two, deleting one of those selected leaves would change only the support's neighbor sum, which would remain positive. The same transfer and extension argument preserves $\gamma_t$. ∎

**Theorem 7.** Every pair $(a,b)$ realizable by a tree has a representative tree with at most

$$
6a-4 \tag{5}
$$

vertices. In particular,

$$
a+1\le b\le6a-4. \tag{6}
$$

**Proof.** Apply Lemma 6 and let the resulting core have $h$ vertices and $p$ supports. Every support is forced into every total dominating set, so $p\le a$. A non-support core vertex has core degree at least 2. Since the core is a tree,

$$
\sum_{v\text{ support}}\deg_H(v)
\le 2(h-1)-2(h-p)=2p-2.
$$

This also holds for a one-vertex core. The reduced tree has at most

$$
h+\sum_{v\text{ support}}(\deg_H(v)+2)
\le h+4p-2
\le(2a-2)+4a-2=6a-4
$$

vertices by Lemma 5. Both parameters are preserved. Its proper parameter is at most its order, and Theorem 1 gives the lower bound. ∎

This converts the infinite existence question at fixed $a$ into an exact finite search: enumerate trees up to order $6a-4$, and compute both parameters by subset enumeration. It does **not** give a useful closed-form description of all the attainable values of $b$, and it is not offered as a complete resolution of Q257.

## 7. Finite checks and what remains open

[verify.py](verify.py) exhausts all unlabeled trees of orders 2 through 13, computes both parameters directly from subsets, checks strict separation and the core bound, verifies every nontrivial leaf truncation in that range, and compares all caterpillars with the separate 16-state implementation. The saved [verification.json](verification.json) includes a smallest observed representative and explicit witnesses for each observed pair.

The four pairs with $a\in\{2,3\}$ are classified at arbitrary order by Theorems 3–4. The finite records for larger $a$ establish only existence of their explicit witnesses. They do not establish nonexistence of missing pairs; in particular, the order-13 search does not reach the representative bound even for all $a=3$ instances.

The complete pair classification for $a\ge4$, a sharp upper bound as a function of $a$, and an efficient structural description of the attainable values remain open here. No diagonal pairs should be marked realizable for trees, and Q257 should retain **open with partial results** status.
