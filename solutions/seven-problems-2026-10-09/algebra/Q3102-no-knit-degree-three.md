# Q3102: no knit degree three in a finite completely regular semigroup

Date: 2026-10-09. Status: **proposed complete negative answer**, with a self-contained proof below. This is an internally reviewed research contribution, not a claim of peer review.

## Authoritative target and scope

Q3102 records Problem 7.4, printed p. 28, of Tânia Paulista, *Commuting graphs of inverse semigroups and completely regular semigroups*, arXiv:2511.10612v1, submitted 13 November 2025. The full primary-source PDF was read, including the definitions on p. 4 and Theorem 6.3 on p. 27:

- <https://arxiv.org/pdf/2511.10612>
- <https://arxiv.org/abs/2511.10612>

The problem asks whether a finite noncommutative completely regular semigroup can have knit degree three. The vertices of its commuting graph are **only the noncentral elements**. A left path from a vertex $a$ to a different vertex $d$ has the additional requirement $ax=dx$ for **every** vertex $x$ on that path, including the endpoints. Knit degree is the minimum length of a left path, when any exists.

A semigroup is completely regular if every element belongs to a subgroup. The identity of such a subgroup need not be the identity of the whole semigroup, and it need not be central. Both distinctions matter in this proof.

Paulista already proves that knit degree one is impossible in this class. The result below rules out three. It does not assert that all left paths have length two: a semigroup without a left path of length three can have larger knit degree, as the source's cited constructions show.

## Main theorem

**Theorem.** If the commuting graph of a finite completely regular semigroup contains a left path of length three, it contains a left path of length two. Consequently, no finite completely regular semigroup has knit degree three.

### Step 1: replacing the endpoints by idempotents

Let

$$
a-b-c-d
$$

be a left path of length three. Thus all four vertices are distinct and noncentral, and

$$
ab=ba,\qquad bc=cb,\qquad cd=dc,
\tag{1}
$$

$$
a^2=da,\qquad ab=db,\qquad ac=dc,\qquad ad=d^2.
\tag{2}
$$

Because the semigroup is finite and completely regular, choose a positive integer $N$ divisible by the orders of $a$ and $d$ in their respective subgroups. Put

$$
e=a^N,\qquad f=d^N.
$$

These are the corresponding subgroup identities. From (2), for all positive integers $i,j$,

$$
a^i d^j=d^{i+j},\qquad d^i a^j=a^{i+j}.
\tag{3}
$$

For example, $ad^j=d^{j+1}$, and induction on $i$ gives the first equality; the second follows the same way from $da=a^2$. Therefore

$$
ef=f,\qquad fe=e.
\tag{4}
$$

The idempotents $e$ and $f$ are distinct. Indeed, if $e=f$, the subgroup identity property and (3) would give

$$
a=af=ad^N=d^{N+1}=d,
$$

contrary to the path endpoints being distinct. Equation (4) then shows that $e$ and $f$ do not commute, so **both are noncentral**.

For any $x$ with $ax=dx$, (3) gives $a^k x=d^k x$ for every $k\geq1$: when $k>1$,

$$
a^k x=a^{k-1}dx=d^k x.
$$

Apply this to $x=b,c$. Taking powers also preserves each relevant commutation relation in (1). We obtain

$$
eb=fb,\qquad ec=fc,\qquad eb=be,\qquad bc=cb,\qquad fc=cf.
\tag{5}
$$

No claim that $e-b-c-f$ is already a path is needed: some of these elements could coincide. The construction below checks distinctness for its final path directly.

### Step 2: the subgroup identity of the first interior vertex

Choose a positive integer $M$ divisible by the order of $b$ in its subgroup, and set

$$
u=b^M.
$$

Then $u^2=u$ and $ub=bu=b$. Equations (5), multiplied by powers of $b$, give

$$
eu=fu,\qquad eu=ue,\qquad uc=cu.
\tag{6}
$$

Define

$$
p=eu=fu,\qquad q=uf.
\tag{7}
$$

Equations (4) and (6) imply

$$
p^2=p,\qquad q^2=q,\qquad pq=q,\qquad qp=p.
\tag{8}
$$

Here are explicit calculations for the less immediate equalities:

$$
\begin{aligned}
q^2&=ufu f=u(eu)f=eu f=uef=uf=q,\\
pq&=eu^2f=euf=uef=uf=q,\\
qp&=ufeu=ueu=eu=p.
\end{aligned}
$$

Furthermore, $c$ commutes with $p$ and $q$. For $p$, use its expression $fu$; both $f$ and $u$ commute with $c$. The same observation applies to $q=uf$. Finally,

$$
pc=euc=uec=ufc=qc,
\tag{9}
$$

where the middle equality uses $ec=fc$.

### Step 3: three exhaustive cases

**Case A: $p\ne q$.** Equations (8) show that $p$ and $q$ do not commute, so they are noncentral. The original vertex $c$ is noncentral and commutes with both. It cannot equal either endpoint, because that would force $p$ and $q$ to commute. Hence

$$
p-c-q
$$

is a genuine path of length two in the commuting graph. It is a left path: its endpoint equations are $p^2=qp$ and $pq=q^2$ by (8), and its interior equation is (9).

**Case B: $p=q$ and $u$ is noncentral.** By (6) and (7), $u$ commutes with $e$ and $f$, and $eu=fu$. The noncommutation of $e$ and $f$ guarantees that $u$ is distinct from both. Thus

$$
e-u-f
$$

is a path of length two. It is a left path because $e^2=fe=e$, $ef=f^2=f$, and $eu=fu$.

**Case C: $p=q$ and $u$ is central.** Now use the original noncentral vertex $b$, rather than the central element $u$. Since $bu=b$, $u$ is central, and $fu=eu$,

$$
bf=buf=bf u=beu=be=eb=fb.
\tag{10}
$$

In $beu=be$, use $eu=ue$ and $bu=b$. Therefore $b$ commutes with both $e$ and $f$. It is distinct from both, again because $e$ and $f$ do not commute. The path

$$
e-b-f
$$

is a left path of length two: its endpoint conditions follow from (4), and $eb=fb$ is (5).

These three cases cover all possibilities. Each produces three distinct noncentral vertices and verifies all left-path equations. This proves the theorem. $\square$

## Relation to prior work

Araújo, Kinyon and Konieczny's *Minimal paths in the commuting graphs of semigroups*, European Journal of Combinatorics 32 (2011), 178–197, Proposition 5.2, proves a related implication between quasi-identities of bands. Its reduction takes the product of the two interior vertices as a new middle vertex. A central product cannot serve as a vertex of the commuting graph. The case split above supplies noncentral vertices and also handles nontrivial subgroups:

- <https://doi.org/10.1016/j.ejc.2010.09.004>
- Author-hosted full text: <https://cs.du.edu/~mathfiles/preprints/nsm-math-preprint-1006.pdf>

Bauer and Greenfeld's *Commuting graphs of boundedly generated semigroups*, Example 10, gives a semigroup of knit degree three with all products of three generators zero. It is **not** completely regular. The accompanying verification script reconstructs that example and confirms its knit degree, as a negative control against an accidental claim about all semigroups:

- <https://arxiv.org/html/1710.05250v1>
- <https://doi.org/10.1016/j.ejc.2016.02.009>

## Verification and limits

The theorem is established by the algebraic proof, not by bounded enumeration. `verify_semigroups.py` separately checks associativity, complete regularity, graph vertices, all three-vertex left paths, and the constructive reduction on explicit finite examples that exercise the cases above. It also checks the published nilpotent counterexample outside the hypothesis.

Finite-model search in `search_semigroups.py` is supplementary. An SMT `unsat` result is recorded only as solver evidence at its specified order; it is not used to infer the universal theorem. Searches and provenance are recorded in `SOURCES.md` and `verification.json`.

The result answers exactly the finite completely regular existence question Q3102. No claim is made here about arbitrary regular semigroups or about infinite completely regular semigroups with elements of infinite order.
