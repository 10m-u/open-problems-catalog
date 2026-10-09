# Q270: the bunkbed inequality for every transitive tournament

**Result:** the inequality in Q270 holds for every $n,u,v$. The proof also permits any common horizontal-edge retention probability $p\in[0,1]$, with independent vertical-edge probabilities $q_j\in[0,1]$ that can vary by vertex.

This is a complete proof submitted in this research round, subject to independent mathematical review. Publication and historical novelty are not asserted.

## 1. Exact source and scope

The source question is Lawrence Hollom's Conjecture 6.6.4 in *Extremal, Probabilistic, and Infinitary Problems in Combinatorics*, printed page 158. The exact percolation model is Model 6.4.5, printed page 153: retain an independent uniform subset of the horizontal arcs and of the bidirectional vertical edges.

- [Primary thesis](https://api.repository.cam.ac.uk/server/api/core/bitstreams/a0069f85-e810-476b-ba41-c2babc9c2f0b/content), Model 6.4.5 and Conjecture 6.6.4.
- [Published paper](https://www.repository.cam.ac.uk/bitstreams/3a9595ae-7514-4075-b8e4-721c65d1cee0/download), *The bunkbed conjecture is not robust to generalisation*, European Journal of Combinatorics 128 (2025), 104188; Definition 1.1, Model 4.5, and Conjecture 6.4. DOI [10.1016/j.ejc.2025.104188](https://doi.org/10.1016/j.ejc.2025.104188).
- [Tomasz Przybyłowski's later paper](https://arxiv.org/html/2506.22284v2), *The acyclic directed bunkbed conjecture is false*. Its counterexample is a particular sparse acyclic graph, not a transitive tournament. It therefore does not resolve the question proved here.

The model and conjecture were checked against both primary versions on 9 October 2026. Focused searches for the transitive-tournament conjecture and later work located no existing resolution. This is a search-qualified statement, not a proof of novelty. No existing solution to Q270 was found in the repository's solution reports at base commit 8967f4f70776856b3dfc0b2494ed73167b15ee0c.

The directed graph $T_n$ has vertices $1,\ldots,n$ and all arcs $i\to j$ with $i<j$. Take two copies, indexed by $0,1$. At each vertex $j$, a single vertical edge can be traversed in both directions when retained. In the catalog model, every horizontal arc and vertical edge is independently retained with probability $1/2$.

The proof does not apply to arbitrary acyclic graphs or to the model in which corresponding horizontal edges are conditioned to occur in exactly one layer. Independence of the two layers' incoming arcs and the complete ordered predecessor sets are used explicitly.

## 2. The reachable-count process

We prove the more general probability statement above. Fix $u<v$. A directed path from $u^{(0)}$ to either copy of $v$ can visit only vertices whose indices lie between $u$ and $v$. Thus all vertices outside this interval may be discarded, and the interval may be relabelled $1,\ldots,\ell$, where $\ell=v-u+1$.

After exposing all edges within the first $j$ vertex pairs, let

$$
A_j=\#\{i\leq j:1^{(0)}\to i^{(0)}\},
\qquad
B_j=\#\{i\leq j:1^{(0)}\to i^{(1)}\}.
\tag{1}
$$

All horizontal edges point forward, so exposing later vertices cannot change reachability of earlier vertices. At the source,

$$
(A_1,B_1)=
\begin{cases}
(1,1),&\text{with probability }q_1,\\
(1,0),&\text{with probability }1-q_1.
\end{cases}
\tag{2}
$$

The pairs $(A_j,B_j)$ form a time-inhomogeneous Markov chain. To see this, condition on the entire exposed graph up to $j$, and suppose its counts are $(a,b)$. Before exposing the vertical edge at $j+1$, the probability that the new vertex in layer 0 receives no arc from a reachable predecessor is

$$
\alpha=(1-p)^a,
$$

and the corresponding probability in layer 1 is

$$
\beta=(1-p)^b.
$$

These two failures are independent, because they use disjoint collections of fresh independent arcs. Only $a,b$ matter: every earlier vertex is a predecessor, and all its outgoing arcs to this new vertex have the same retention probability $p$. Let $q=q_{j+1}$. The full transition table is

| Increment $(A_{j+1}-A_j,B_{j+1}-B_j)$ | Conditional probability |
|---|---|
| $(0,0)$ | $\alpha\beta$ |
| $(1,0)$ | $(1-q)(1-\alpha)\beta$ |
| $(0,1)$ | $(1-q)\alpha(1-\beta)$ |
| $(1,1)$ | $(1-\alpha)(1-\beta)+q[(1-\alpha)\beta+\alpha(1-\beta)]$ |

The first row covers the case in which neither layer receives an incoming reachable arc. If exactly one receives such an arc, retaining the vertical edge makes both new copies reachable. This accounts for the remaining rows.

Two properties of the transition kernel are decisive:

1. Swapping $a,b$ and swapping the two coordinates of the increment preserves every transition probability.
2. The difference $A_j-B_j$ changes by at most one at each step.

In particular, a count chain starting from $(a,a)$ has a law invariant under exchanging its coordinates at all later times. The original exposed graph need not itself be invariant under layer exchange. The assertion follows from the count chain's transition kernel.

## 3. Cancel paths that reach the diagonal

Let

$$
\tau=\inf\{j\geq1:A_j=B_j\},
\tag{3}
$$

with $\tau=\infty$ if equality never occurs. On $\{\tau>j\}$, equation (2) and the unit-step property imply

$$
A_j>B_j.
\tag{4}
$$

Indeed, the only initial state off the diagonal is $(1,0)$, and an integer-valued difference that changes by at most one cannot become nonpositive without first equalling zero.

Set $k=\ell-1$. The difference between the two target-reachability probabilities, conditional on the graph exposed through vertex $k$, is

$$
g(A_k,B_k)
=(1-q_\ell)\big[(1-p)^{B_k}-(1-p)^{A_k}\big].
\tag{5}
$$

One way to read (5) is to subtract the $(0,1)$ increment probability from the $(1,0)$ increment probability in the transition table. The $(1,1)$ and $(0,0)$ cases cancel. Thus the desired unconditional difference equals $\mathbb E g(A_k,B_k)$.

The function $g$ is antisymmetric: $g(b,a)=-g(a,b)$. On $\{\tau\leq k\}$, condition on the stopping time $\tau$ and its state $(A_\tau,B_\tau)=(a,a)$. The future count chain is symmetric under coordinate exchange, so

$$
\mathbb E\!\left[g(A_k,B_k)\mathbf1_{\{\tau\leq k\}}\right]=0.
\tag{6}
$$

This can be justified without any infinite stopping-time theorem: sum over the finitely many possible values $\tau=j\leq k$ and their finite count states, and apply the ordinary Markov property at each $j$.

On $\{\tau>k\}$, equation (4) gives $A_k>B_k$. Since $a\mapsto(1-p)^a$ is nonincreasing,

$$
g(A_k,B_k)\geq0.
\tag{7}
$$

Combining (5)–(7) proves

$$
\mathbb P(1^{(0)}\to\ell^{(0)})
-\mathbb P(1^{(0)}\to\ell^{(1)})
=\mathbb E\!\left[g(A_k,B_k)\mathbf1_{\{\tau>k\}}\right]
\geq0.
\tag{8}
$$

For $u=v$, the same-layer connection probability is one, and the other-layer connection probability is $q_u$: a horizontal forward path cannot return to $u$. For $u>v$, both probabilities vanish. These cases complete the result for every $n,u,v$. At $p=1$, the convention $(1-p)^0=1$ has its ordinary “no incoming arcs” meaning; the transition argument remains valid. ∎

## 4. A strict quantitative consequence

For $0<p<1$ and $u<v$, equation (8) also provides the lower bound

$$
\mathbb P(u^{(0)}\to v^{(0)})
-\mathbb P(u^{(0)}\to v^{(1)})
\geq(1-q_u)(1-q_v)p(1-p)^{v-u-1}.
\tag{9}
$$

To obtain it, require the source vertical edge to be absent, and require that none of the intervening vertex pairs receives a reachable incoming edge. The count state then remains $(1,0)$ up to $v-1$, an event of probability $(1-q_u)(1-p)^{v-u-1}$. On that event, $g(1,0)=(1-q_v)p$. All other paths that avoid the diagonal make nonnegative contributions, while paths that hit it have already canceled.

For the catalog's $p=q_j=1/2$ model, this gives

$$
\mathbb P(u^{(0)}\to v^{(0)})
-\mathbb P(u^{(0)}\to v^{(1)})
\geq 2^{-(v-u+2)}>0
\qquad(u<v).
\tag{10}
$$

This bound is not asserted to be sharp.

## 5. Reproducible verification

The file verify_q270.py performs two different exact calculations:

- It enumerates every retained-edge subset for $T_n$ with $n\leq4$, computes reachability on the resulting explicit graph, and compares all $u,v$ connection probabilities to the count-chain calculation.
- It propagates exact rational count distributions, including a separate flag recording whether the diagonal has ever been hit. It checks the cancellation identity (8), the strict bound (10), and symmetry after a diagonal starting state.

The full theorem follows from the Markov-chain argument, not from checking finitely many tournaments. The independent finite graph enumeration verifies that the count transition model represents the source's bidirectional-vertical-edge convention correctly.
