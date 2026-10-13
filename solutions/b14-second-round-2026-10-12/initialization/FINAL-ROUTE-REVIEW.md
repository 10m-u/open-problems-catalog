# Independent review of the Haar and centroid-inversion routes

Reviewed internally on 12 October 2026 by the continuing B14 sub-agent. Both proposed obstructions are valid. They reject the specified proof routes; neither disproves its catalog question. This is an internal mathematical audit, with no novelty or external peer-review claim.

## Q1953: two offsets cannot cover all connected cyclic Haar graphs

The actual target is the Hamiltonicity conjecture for connected regular bicirculants, with the stated $K_2$ and generalized-Petersen exceptions. Its source is [Bonvicini, Pisanski and Žitnik, Conjecture 1](https://arxiv.org/abs/2604.21607), locally archived as collections-f0c6c0c22c39f930.txt.gz. The paper proves the reduction to connected cyclic Haar graphs in Theorem 1.3. Proving the Haar case would complete that route; merely finding two convenient offsets is a much stronger restriction.

Use vertices $u_i,v_i$ for $i\in\mathbb Z_m$, with an offset $s$ supplying the perfect matching $u_i v_{i+s}$. A two-edge alternating walk changes its $u$ index by a difference of offsets. Consequently,

\[
H(m,S)\text{ is connected}\quad\Longleftrightarrow\quad
\gcd\bigl(m,\{s-t:s,t\in S\}\bigr)=1.
\]

For two distinct offsets $s,t$, their matching union is 2-regular, and advancing along it changes the index by $s-t$. It therefore has exactly $\gcd(m,s-t)$ components, each a cycle of length $2m/\gcd(m,s-t)$. A two-offset Hamilton cycle exists exactly when one pair has a unit difference modulo $m$.

Let $m=pqr$ for distinct odd primes, and take $S=\{0,pq,pr,qr\}$. The collective gcd is 1. Each difference from 0 has two prime factors; the differences between nonzero offsets are $p(q-r)$, $q(p-r)$ and $r(p-q)$, each divisible by a prime factor of $m$. Thus every pair has nonunit difference, and every two-offset spanning subgraph is disconnected. This proves the proposed completeness claim false on an infinite named family.

The exact $m=105$ check gives:

| Offsets | Number of components |
| --- | ---: |
| 0,15 | 15 |
| 0,21 | 21 |
| 0,35 | 35 |
| 15,21 | 3 |
| 15,35 | 5 |
| 21,35 | 7 |

There is an even more direct source-scope safeguard than Theorem 1.5(iii): the three nonzero offsets already form a **connected cubic spanning cyclic Haar graph**. Indeed, no prime factor $p,q,r$ divides both $pq-pr$ and $pq-qr$, so their collective gcd with $m$ is 1. The source's Theorem 2.1 states that connected cubic cyclic Haar graphs are Hamiltonian. Hence every graph in this obstruction family is already known to be Hamiltonian via that cubic spanning subgraph. Theorem 1.5(iii), for odd $m$ that is a product of at most three prime powers, is also applicable. Write “a product of at most three prime powers,” not an inequality involving the numerical sizes of those powers.

**Verdict:** valid obstruction to completeness of the two-offset selection proof. It does not refute Q1953, the author's Haar reduction, or proofs using three or more offsets.

## Q3819: a forced improving move can create centroid-ranked inversions

The source question explicitly asks for existence of a polynomial-length improving path from every initial one-dimensional clustering. It does not require every pivot rule to have short paths. See [Manthey and van Rhijn, STACS 2024, §5, p.52:14](https://drops.dagstuhl.de/storage/00lipics/lipics-vol289-stacs2024/LIPIcs.STACS.2024.52/LIPIcs.STACS.2024.52.pdf). Their exponential sequence in Theorem 1 is expressly for a particular sequence/pivot rule and does not answer the existence question. Lemma 4 gives the transfer formula used below.

For a transfer of $x$ from a source of size $p\ge2$ and mean $a$ to a target of size $q\ge1$ and mean $b$, the exact new-minus-old objective is

\[
\Delta(x)=\frac q{q+1}(x-b)^2-\frac p{p-1}(x-a)^2.
\]

This follows independently from $\Phi(C)=\sum_{x\in C}x^2-(\sum_{x\in C}x)^2/|C|$. It is valid with recomputed centroids and nonempty source; improvement means $\Delta<0$.

Start with

\[
A=\{-6,0,1/1000,2/1000,3/1000,4/1000\},\qquad B=\{8/5\}.
\]

The initial means are $a=-599/600$ and $b=8/5$. All six legal transfer increments were checked as exact rational numbers. The increment for $-6$ is $-342001/300000<0$; all five others are positive, the smallest being $510011/7500000>0$. The singleton $B$ cannot donate. Thus every improving path must start by moving $-6$ to $B$.

Initially the centroid rank is $A<B$, and the sorted point labels are $A,A,A,A,A,A,B$, with zero inversions. After the forced move, the means become $a=1/500$ and $b=-11/5$, so the centroid rank is $B<A$. The sorted labels are then $B,A,A,A,A,A,B$. Each of the five small $A$ points preceding $8/5\in B$ gives one inversion, for exactly five. There are no centroid ties.

The obstruction also admits a complete two-step improving path. In the new configuration the only improving transfer is $8/5$ from $B$ to $A$, with increment $-8025599/300000$. After it the clusters are

\[
A=\{0,1/1000,2/1000,3/1000,4/1000,8/5\},\qquad B=\{-6\}.
\]

Their means are $161/600$ and $-6$. Every one of the six legal transfers is now strictly worsening, and $B$ cannot donate. Thus this final partition is a local optimum. The exact objectives along the path are

\[
\frac{2251501}{75000}\;>\;\frac{2888001}{100000}\;>\;\frac{159601}{75000}.
\]

The direct objective differences agree with the transfer formula for all 19 legal transfers across the three configurations.

**Verdict:** valid obstruction to a proof requiring centroid-ranked inversion count to decrease, or even to stay constant, at every selected improving move. Since the first move is forced, choosing a different pivot cannot repair that monotonicity invariant. The example has a two-move path to a local optimum and is not a counterexample to Q3819. It does not exclude an amortized argument or a different invariant.

## Audit limits and stopping-rule correction

The checks above use exact gcd and rational arithmetic and do not estimate probabilities or enumerate large families. The Haar conclusion follows for all distinct odd primes from the group calculation; the clustering obstruction uses seven distinct real points and two nonempty clusters, exactly within the stated question.

The user subsequently clarified that five consecutive substantive failed solve attempts apply **per problem**. These are one rejected route each for Q1953 and Q3819. They do not consume Q3817's failure count or justify stopping B14 overall. The continuing agent will resume its assigned Q3817 work after this review.
