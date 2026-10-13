# Final B2 factorization targets

13 October 2026. Root took these five unstarted targets while the retained agent handle remained pending initialization. No service delay counts as an attempt. Each route below constructs or analyzes a proposed full-target mechanism and records the obstruction that stops it. Shared ingredients are disclosed. None resolves its entire catalog target.

## Q2008 half-factorial Dedekind class groups

The exact target is every abelian group, without a cardinality restriction. The cached survey's Problem 15 and [Geroldinger–Göbel, pp. 841–843](https://imsc.uni-graz.at/geroldinger/45-half-factorial-subsets.pdf) were read. The latter supplies the prime-class realization theorem and proves the known Warfield case, including all countable groups. These are sourced prior results, not new proofs here. Write $\mathcal B(S)$ for zero-sum sequences over a group subset $S$; $S$ must generate the group **as a monoid** for the cited realization.

<a id="q2008-a1"></a>
### A1 unrestricted class-group realization

Use Claborn realization, then try to declare half-factoriality from the class group alone. Prime-class distribution is essential. In $C_3=\langle g\rangle$, allowing both $g,-g$ gives atoms $g^3$, $(-g)^3$ and $g(-g)$. Their common product has factorizations of lengths two and three. Thus even an atomic Dedekind realization with the requested class group need not be half-factorial. Realizing a controlled half-factorial prime-class subset is the missing step; unrestricted realization fails that obligation.

<a id="q2008-a2"></a>
### A2 explicit independent cyclic components

For a finite cyclic component of order $d$, choose only a generator: every zero-sum atom has $d$ letters, so a block's factorization length is its letter count divided by $d$. For an infinite cyclic component choose $S=\{-g\}\cup\{ng:n\ge1\}$. Every atom contains one positive letter $ng$ and $n$ negative letters. Every block's factorization length equals its number of positive letters. This subset generates the whole cyclic group as a monoid. In a direct sum of cyclic groups, take the union of these component subsets. Every minimal zero-sum block lies in one component, so lengths add componentwise. The cited realization gives half-factorial Dedekind domains for this family, including arbitrarily large direct sums.

This construction requires independent cyclic components. General abelian groups need not have such a decomposition; for example $\mathbb Q$ is divisible and not free abelian or a direct sum of finite cyclic groups. Its countable case is already covered by the stronger source theorem. The construction does not handle arbitrary groups outside the covered families.

<a id="q2008-a3"></a>
### A3 assemble the known countable realizations

Every finite or countable selection of elements lies in a countable subgroup, where the sourced theorem applies. Try taking a directed union of half-factorial generating subsets. The chosen subsets must be compatible: in $C_3$, each singleton $\{g\}$ and $\{-g\}$ is half-factorial and monoid-generating, but their union fails by A1. Separate existence on each subgroup supplies neither coherent choices nor compatible Dedekind embeddings. The route reduces the unrestricted problem to a coherence theorem it does not prove. The union control shares A1's block, for a different assembly mechanism.

<a id="q2008-a4"></a>
### A4 descend a free presentation

Present an arbitrary group as a quotient of a free abelian group and descend its half-factorial subset. Zero-sum atoms change in the quotient. In $\mathbb Z$, the subset $\{1,-1\}$ has only the zero-sum atom $(1,-1)$ and is half-factorial. Under reduction modulo three, the images acquire the pure triple atoms from A1 and lose half-factoriality. Relations cannot be imposed without controlling newly created atoms. The free-presentation construction therefore supplies no universal answer.

<a id="q2008-a5"></a>
### A5 compactness of prime-class selections

Half-factoriality can be expressed by excluding finite-support unequal-length block factorizations. Try a compact limit of local half-factorial selections. Monoid generation is not closed in the coordinatewise topology on subsets. In $\mathbb Z$, let $S_N=\{-1\}\cup\{n:n\ge N\}$. Each is half-factorial by A2 and generates $1=N+(N-1)(-1)$, hence all integers. The coordinatewise limit is $\{-1\}$ and cannot generate $1$. Compactness for forbidden finite configurations loses the existential generation witnesses. A coherent witness bound or another construction is required. This is a mechanism obstruction, not a negative answer to Q2008.

**Disposition:** five full-target failures. Countable/Warfield and independent-cyclic families remain known positive scopes. No abelian group is asserted to be a counterexample.

## Q2210 exact finite length sets in reduced power monoids

Keep the exact monoid of finite subsets of $\mathbb N_0$ containing zero. The cached [Reinhart revision, Theorem 1.1](https://arxiv.org/html/2508.10209v2) applies because $\mathcal P_{fin,\times}(\mathbb N_0)=\mathcal P_{fin,0}(\mathbb N_0)$. The known family $H^*$ generated by $\{1\}$ and $\{2,n\}$ realizes **every two-element set** $\{a,b\}$ with $2\le a<b$: add $(a-2)\{1\}$ to $\{2,b-a+2\}$. This broadens the source inventory relative to the old singleton-only partial, without a novelty claim.

<a id="q2210-a1"></a>
### A1 use the supplied length-family generators

Construct the desired $L$ in $H^*$. Its minimum is the sum of generator minima. At minimum two there is at most one nontrivial generator, so a three-element set such as $\{2,3,5\}$ is outside $H^*$. The additional sourced intervals $[k,k+2]$ do not by themselves give closure under arbitrary unions. The generator theorem does not establish the full realization conjecture.

<a id="q2210-a2"></a>
### A2 tune elasticity instead of all lengths

Full elasticity supplies all rational ratios of maximum to minimum. The target needs every interior membership as well. For example $\{2,5\}$ and $\{2,3,5\}$ have the same elasticity $5/2$. The two-element construction realizes the first exactly and says nothing about the second. Specifying ratio and even extrema leaves the interior lengths uncontrolled, so this proposed construction fails the exact-set obligation.

<a id="q2210-a3"></a>
### A3 concatenate witness sets by Minkowski sum

Try $L(A+B)=L(A)+L(B)$ to assemble more patterns. Take atoms $A=\{0,1,3\}$ and $B=\{0,2,3\}$. A three-point decomposable normalized set must be an arithmetic progression, so both are atoms. Their sum is $[0,6]$ and has a six-factor decomposition into $\{0,1\}$, as well as the displayed two-factor decomposition. Thus lengths outside $\{2\}$ appear. Separate digit blocks would need a theorem forbidding mixed factors; Minkowski concatenation alone is insufficient. The finite exact checker verifies the entire displayed length sets.

<a id="q2210-a4"></a>
### A4 use unions to select alternative factorization lengths

Try to make disjoint witness choices by set union. Take $A=\{0,1,2\}$ and $B=\{0,2,4\}$, each with exact length set $\{2\}$. Their union $\{0,1,2,4\}$ is an atom. Indeed a nontrivial decomposition must have maxima $(1,3)$ or $(2,2)$; the first forces a missing element three in a factor, and the second forces three in the sum when producing one and four. Thus union changes the desired lengths to $\{1\}$. It is not a selector for factorization alternatives.

<a id="q2210-a5"></a>
### A5 complete bounded witness synthesis

Enumerate every normalized set with maximum at most twelve. Every proper decomposition $A=B+C$ has positive maxima adding to $\max A$, and both factors are subsets of $A$. Enumerating all such sums and processing sets by maximum computes their exact length sets recursively, including atom detection. This is a complete algorithm on the declared finite domain and can synthesize witnesses found there. It supplies neither a bound on the maximum required for arbitrary $L$ nor a construction for all $L$. The new receipt is independent of the missing original sixteen-coordinate archive; it does not recover that archive.

**Disposition:** five full-target failures. The source's two-element theorem and the new bounded controls are retained separately from the old partial record.

## Q2213 prescribed product-one subsequences

The target covers all finite nonabelian groups, with terms arbitrarily reorderable. The cached Qu–Wang source's Theorem 1.1 and Corollary 4.1 cover groups of order $p^3$, and its introduction identifies other known classes. Its central-quotient ordering method requires additional structure; it is not an abelianization-only argument.

<a id="q2213-a1"></a>
### A1 turn the lower bound around

Adding $|G|-1$ identities to a product-one-free sequence of maximum length proves $E(G)\ge d(G)+|G|$, as retained previously. Trying to delete identities from an arbitrary sequence of the critical length leaves no guaranteed number of identities or product-one-free remainder. The construction proves a necessary lower bound, without an upper selection algorithm. Its attempted converse fails that obligation.

<a id="q2213-a2"></a>
### A2 solve the abelian quotient and lift

In $S_3$, five identities and one three-cycle form a length-six sequence with zero image in the abelianization $C_2$, but every ordering has the same nonidentity product. The quotient's prescribed-length solution can therefore land in the commutator subgroup without becoming product-one. Lifting requires control of all ordering products in the kernel, not just the quotient sum. This is a failed proof mechanism, not a length-critical counterexample to the conjecture.

<a id="q2213-a3"></a>
### A3 greedily pack short product-one blocks

Try selecting a subcollection of a maximal product-one block packing whose lengths sum to $|G|$. In $S_3$, the sequence $\tau^5\sigma^3$, with a transposition $\tau$ and a three-cycle $\sigma$, has a maximal packing of blocks of lengths $2,2,3$ and one leftover $\tau$. No subcollection sums to six. Nevertheless four $\tau$ and two $\sigma$ can be ordered product-one: $\tau\tau\tau\sigma\tau\sigma$, since $\tau\sigma$ has order two. Greedy whole-block selection loses a valid mixed subsequence. This eight-term control is below the true threshold; it exposes the loss of information, not a conjecture counterexample. A critical-length packing theorem with a reassembly argument is still missing.

<a id="q2213-a4"></a>
### A4 induct through central quotients

The Heisenberg proof arranges kernel products through a nontrivial central subgroup and bounded nilpotency structure. Trying to iterate that reduction on every group stops for centerless simple groups. For $A_5$, its center and abelianization are both trivial; a three-cycle plus 59 identities illustrates that even a prescribed-length trivial quotient product does not control the group product. The sourced order-$p^3$ theorem supplies no decreasing central-quotient induction for these groups. An ordering-value theorem for general kernels would be needed.

<a id="q2213-a5"></a>
### A5 exact all-multiset solver for a nonabelian group

Use dynamic programming on multiplicity vectors, with the set of **all** possible ordering products as state. Enumerate every $S_3$ multiset needed for the small Davenport threshold and length-six subsequences at lengths eight and nine. The exact computation proves $d(S_3)=3$ and $E(S_3)=9$. A product-one-free length-three witness and a length-eight sequence lacking a length-six product-one subsequence establish the lower sides; all length-four and length-nine multisets establish the upper sides. Longer sequences contain a tested prefix multiset. This resolves the one-group subcase, already within known dihedral results, but a finite table has no uniform all-group bound. The full-target algorithmic attempt fails that universal obligation.

**Disposition:** five full-target failures, retaining the exact $S_3$ check and the sourced order-$p^3$ scope. Abelianization and greedy packing share the loss of ordering data, but use different attempted selection procedures.

## Q2217 rank-one almost atomicity

The cached Dani et al. source was read through its Theorem 4.3, Lemma 5.4, Theorem 5.5 and Question 5.6. Atomicity does **not** ascend automatically. For linearly orderable monoids, Theorem 4.3 identifies atomic power monoids with atomic MCD monoids. The source's rank-two counterexample therefore cannot be replaced by an unproved blanket atomicity-ascent assertion.

<a id="q2217-a1"></a>
### A1 finite-generation or positive-gap candidates

Construct a proper Puiseux monoid with a positive lower gap $c$ and try to obstruct power atomicity. Every nonunit finite subset has maximum at least $c$, and maxima add under sumsets. Repeated proper factorization has length at most $\max S/c$; a terminal factorization into atoms therefore exists. Thus its power monoid is atomic, so no such candidate answers Q2217. This retains the prior necessary accumulation-at-zero condition.

<a id="q2217-a2"></a>
### A2 reciprocal odd-prime candidate and a finite MCD theorem

Let $M=\langle1/p:p\text{ odd prime}\rangle$. Every element has a unique canonical form

$$q=\ell(q)+\sum_p r_p(q)/p,\qquad \ell(q)\in\mathbb N_0,\quad 0\le r_p(q)<p,$$

with finite support. Reducing coefficients modulo their primes gives existence; multiplying a putative equality by the product of the involved primes gives equality of each residue and then of the integer part. Addition has nonnegative carries:

$$\ell(d+e)=\ell(d)+\ell(e)+\sum_p\left\lfloor\frac{r_p(d)+r_p(e)}p\right\rfloor.$$

If $\ell(q)=0$ and $q=d+e$, both integer parts and all carries vanish. Divisors $d$ therefore have support inside that of $q$ and residues bounded coordinatewise by those of $q$. There are at most $\prod_p(r_p(q)+1)$ such divisors. This also proves that $1/p$ is an atom; all elements are sums of these generators, so $M$ is atomic.

For a finite set $S$, subtract the common integer $h=\min_{q\in S}\ell(q)$, which belongs to $M$. At least one residual element $q_0$ has integer part zero. The common divisors of $S-h$ lie among the finite divisor set of $q_0$. Choose a maximal one $e$. Then $h+e$ is an MCD of $S$: any further common nonzero divisor of the residuals would give a larger common divisor $e+c$ of $S-h$. Thus $M$ is an MCD monoid, and Theorem 4.3 makes $\mathcal P_{fin}(M)$ atomic.

This is an all-size proof ruling out the natural accumulating reciprocal-prime candidate. Finite residue controls check the algorithm but are not its justification. Arbitrary accumulating Puiseux monoids remain outside it.

<a id="q2217-a3"></a>
### A3 dyadic divisibility obstruction

Use $D=\langle2^{-n}:n\ge0\rangle$ to give every finite positive support arbitrarily small singleton divisors. Every positive element splits into two positive halves, so $D$ has no atoms and $F(D)=\{0\}$. It is not almost atomic: adding any element of $F(D)$ cannot turn a positive element into an atomic one. This candidate supplies the desired divisibility pathology while failing the hypothesis on $M$.

<a id="q2217-a4"></a>
### A4 project the rank-two source construction

Map the source's $\mathbb Q^2$ monoid by $\phi(x,y)=x+\lambda y$ with rational $\lambda$. Any such map has a nontrivial kernel on its rank-two Grothendieck group, after clearing denominators. It cannot preserve the distinct additive relations used in the source's atom proof. At $\lambda=0$, the image is $\langle1/5,1/7\rangle$ and has a positive gap, so A1 rules it out. For nonzero rational slope the dyadic directions contaminate the first-coordinate separation of $1/35$ used in Theorem 5.5. No proof of atom preservation or of a persistent power obstruction follows. An irrational slope preserves rank two and fails the rank-one requirement. The proposed projection does not supply the required example.

<a id="q2217-a5"></a>
### A5 a common atomic shift

For each $s$ in a finite set choose $y_s\in F(M)$ with $s+y_s\in F(M)$. Then $Y=\sum_s y_s$ lies in $F(M)$ and every $s+Y$ lies in $F(M)$. This proves a valid common pointwise atomic shift. It does not prove the finite subset $S+\{Y\}$ factors into atoms in the power monoid. The source's atomic Puiseux examples already show the pointwise-to-power implication fails without MCD control. Moreover atoms of $\mathcal P_{fin}(F(M))$ need not stay atoms in $\mathcal P_{fin}(M)$ when factors use non-atomic divisors; Lemma 5.4 explicitly permits such divisors of sums of atoms. Adding divisor-closedness would force $M=F(M)$ by almost atomicity, reverting to the atomic case rather than proving the desired universal ascent. The missing finite-set divisibility control stops this route.

**Disposition:** five full-target failures. A2 rules out one entire accumulating family; A3 and A4 explicitly fail different hypotheses. The almost-atomic rank-one problem remains unresolved.

## Q2617 finitely presented ACCP domains without BF

No primary text was originally cached for this question. The [authors' arXiv v3](https://arxiv.org/pdf/2206.10115) was read at Proposition 3.2 and Section 7, including the normal form, Proposition 7.6 and Question 7.7. The preprint is distinguished from the cited final journal pagination. Source acquisition is not a solve attempt.

<a id="q2617-a1"></a>
### A1 finitely presented connected graded candidates

Let $R$ be a connected $\mathbb N$-graded domain over a field, with all elements finite sums of homogeneous pieces. Leading pieces of a nonzero product do not vanish, so $\deg(ab)=\deg a+\deg b$. A nonzero element of degree zero is a field unit; every nonunit has positive degree. Every nonunit factorization therefore has length at most its degree. Repeated splitting terminates and gives atoms. Thus these domains are BF, including homogeneous finitely presented candidates. The same argument works with a domain associated graded ring and field degree-zero part, as in the source's Proposition 3.2. This attempted homogeneous construction cannot produce a counterexample; a filtration whose leading ring remains a domain also cannot rescue it.

<a id="q2617-a2"></a>
### A2 reuse the finite non-BF source presentation

The source's domain $R=K\langle a,b\mid ba^2b=a^2,\ a^4b=ba^4\rangle$ has arbitrarily long atomic factorizations $a^2=b^n a^2b^n$. But $a^2R\subset ba^2R\subset b^2a^2R\subset\cdots$ is an infinite strict principal-right-ideal chain, with the left analogue too. The normal form distinguishes $b^la^2$ from $a^2b^m$ for $l\ge1,m\ge0$, proving strictness. Atomicity does not repair this defect. The candidate is finitely presented and non-BF while failing exactly the requested ACCP hypothesis.

<a id="q2617-a3"></a>
### A3 collapse that chain by making its generators units

Embed in the source's ambient right-orderable group algebra and invert the offending generators. If both $a,b$ are inverted, one obtains its group algebra $K[G]$, which the source proves BF in Lemma 7.2. Even inverting only $b$ makes the displayed unbounded-length sequence of factorizations disappear: all $b$ factors become units and do not count as atoms. The old non-BF certificate is no longer valid. No replacement non-BF witness or ACCP proof for that intermediate localization was obtained. Killing the chain and preserving unbounded proper lengths are separate obligations.

<a id="q2617-a4"></a>
### A4 finite presentation plus König's lemma

Represent factorizations by a tree of proper refinements. ACCP rules out an infinite refining branch. To infer a finite height from unbounded lengths, König's lemma would require finite branching. A root with one chain of length $n$ for every $n$ has unbounded finite height and no infinite branch. Finitely many algebra generators or defining relations do not prove finitely many divisors of a fixed element up to associates. A finite-branching theorem at that point is an additional hypothesis, not a consequence shown by this reduction. Thus the proposed universal impossibility proof fails.

<a id="q2617-a5"></a>
### A5 algebraize a well-founded unbounded factorization monoid

Construct a cancellative torsion-free commutative monoid with a distinguished $x$ and disjoint atom families $a_{n,1},\ldots,a_{n,n}$, $n\ge2$, imposing $x=\sum_i a_{n,i}$. Embed it in the rational vector space with independent $x,e_{n,i}$ for $i<n$, setting $a_{n,i}=e_{n,i}$ and $a_{n,n}=x-\sum_{i<n}e_{n,i}$. The positive functional $x\mapsto1$, $e_{n,i}\mapsto1/n$ shows the monoid is reduced.

Each element has a unique normal form $qx+\sum_{n,i}c_{n,i}a_{n,i}$, with $q\ge0$, nonnegative finite-support coefficients and $\min_i c_{n,i}=0$ for every family. Normalize by removing complete families; independence proves uniqueness. Under addition, $q$ adds with nonnegative carries. Each $a_{n,i}$ is an atom, while $L(x)$ contains every $n\ge2$. In a strictly descending divisibility chain, $q$ cannot increase and can decrease only finitely often. With $q$ constant, each step has zero carries, no new support and coordinatewise decreasing finite coefficients. An infinite chain is impossible. Thus this monoid satisfies ACCP but is not BF.

Its Grothendieck group has infinite independent rank, so the monoid is not finitely generated. Its semigroup algebra is a domain, but finite algebra generation fails: supports of finitely many polynomials generate only a finitely generated submonoid and cannot contain all the independent atom families. Monoid ACCP alone also does not supply a checked ring ACCP proof here. The construction explains the branching obstruction in A4 while failing the finite-presentation target. Encoding all families with a finite noncommutative shift, without recreating A2's infinite chain, remains the missing construction.

**Disposition:** five full-target failures. The graded exclusion is known background; the monoid in A5 is an illustrative construction, not a claimed ring counterexample. All 25 routes remain stopped full-target attempts, with their scoped results and shared mechanisms preserved.

[Exact finite controls](MONOID-CHECK.json) · [Checker](check_monoid_routes.py) · [Main-thread scope review](../ROOT-REVIEW.md).
