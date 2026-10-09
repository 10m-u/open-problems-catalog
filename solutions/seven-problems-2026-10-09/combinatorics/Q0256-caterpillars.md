# Q256: a finite-state characterization of proper total domination in caterpillars

**Date:** 2026-10-09.

**Result type:** Proposed complete algorithmic characterization, with a self-contained proof.

**Verification level:** Exact finite controls and internal mathematical review; not peer reviewed.

## 1. Authoritative question and scope

Q256 asks which caterpillars possess a proper total dominating set. Its thesis location is Sawyer Isaac Osborn, *From Total Domination to Graph Coloring* (Western Michigan University, 2026), Problem 4.3.8, printed p. 75. The same question is Question 1 in §5 of Osborn and Ping Zhang, *Proper Total Domination in Trees*, **Symmetry** 17 (2025), 1429, DOI [10.3390/sym17091429](https://doi.org/10.3390/sym17091429).

The publisher's indexed full text was inspected for the definition, caterpillar setup, earlier sufficient conditions, and Question 1. Direct retrieval of the thesis PDF returned HTTP 403; its indexed text confirms the problem label. The source-access and literature limitations are recorded in [SEARCH-LOG.md](SEARCH-LOG.md).

For a finite simple graph, write

$$
\sigma_S(v)=|N(v)\cap S|.
$$

The set $S$ is **total dominating** when every $\sigma_S(v)>0$. It is **proper total dominating** when, additionally, $\sigma_S(u)\ne\sigma_S(v)$ on every edge $uv$. A vertex in $S$ must itself have a neighbor in $S$; closed neighborhoods are not used. The minimum size of such a proper set, when one exists, is $\gamma_{pt}(T)$.

The characterization below is a fixed finite-state acceptance criterion on the leaf counts of the spine. It supplies a necessary and sufficient condition, an optimal witness, and linear-time recognition from the spine representation. It does not purport to be a shortest forbidden-subtree list or a uniquely preferred structural form.

## 2. The leaf-word representation

Let $T$ be a caterpillar on at least three vertices. Its non-leaf vertices form a path

$$
v_1v_2\cdots v_k.
$$

Let $\ell_i$ be the number of pendant leaves adjacent to $v_i$. If $k=1$, require $\ell_1\ge2$. If $k\ge2$, require $\ell_1,\ell_k\ge1$, while the interior counts may vanish. These conventions make this the actual non-leaf spine. The trees $K_1$ and $K_2$, under conventions that call them caterpillars, have no proper total dominating set and are handled separately.

For any set $S$, put

$$
x_i=\mathbf1_{v_i\in S},\qquad
 y_i=|S\cap\{\text{leaves adjacent to }v_i\}|,\qquad
 q_i=\sigma_S(v_i),
$$

with $x_0=x_{k+1}=0$. Then

$$
q_i=x_{i-1}+x_{i+1}+y_i. \tag{1}
$$

A leaf forces its unique neighbor into every total dominating set. Thus, when $\ell_i>0$, one must have $x_i=1$, every pendant leaf has neighbor sum 1, and properness on the pendant edges requires $q_i\ge2$. When $\ell_i=0$, one has $y_i=0$ and merely requires $q_i\ge1$. The remaining edge conditions are exactly

$$
q_i\ne q_{i+1}\qquad(1\le i<k). \tag{2}
$$

Conversely, any integral choices satisfying these conditions define a proper total dominating set by selecting any $y_i$ of the leaves at each spine vertex. Its size is $\sum_i(x_i+y_i)$.

The rest of the argument makes this local description a *fixed* finite-state criterion, independent of the degrees or order of $T$.

## 3. A sharp cap on selected leaves

**Theorem 1.** If $T$ has a proper total dominating set, it has a minimum one for which

$$
0\le y_i\le3,\qquad 1\le q_i\le4
\quad\text{for every }i. \tag{3}
$$

Consequently, replacing every $\ell_i$ by $\min(\ell_i,3)$ preserves both feasibility and $\gamma_{pt}(T)$.

**Proof.** Choose a proper total dominating set of minimum size. Only a vertex with pendant leaves could violate (3): a spine vertex without leaves has $q_i=x_{i-1}+x_{i+1}\le2$. Fix a support vertex and put $s=x_{i-1}+x_{i+1}\in\{0,1,2\}$.

Suppose first that $s\ge1$ and either $y_i>3$ or $q_i>4$. In either case the old value of $q_i$ is at least 5. Each of the three new values

$$
q_i'\in\{2,3,4\}
$$

corresponds to a valid nonnegative leaf count $y_i'=q_i'-s\le3$, smaller than the old count. There are enough leaves because $y_i'<y_i\le\ell_i$. At most two spine neighbors forbid values of $q_i'$, so at least one of these three values differs from both neighboring sums. The pendant edges remain proper because $q_i'\ge2$. Changing which pendant leaves belong to $S$ changes no other vertex's neighbor sum. This constructs a smaller proper set, a contradiction.

Now suppose $s=0$ and (3) is violated. Then $y_i=q_i\ge4$. Any spine neighbor has membership bit 0 and therefore cannot have pendant leaves. Such a neighbor has degree 2 in $T$, so its neighbor sum is at most 2. Replacing $y_i$ by 3 is therefore proper on every incident spine edge and on every pendant edge. This again decreases $|S|$, a contradiction. If there are no spine neighbors, the same replacement is valid.

This proves (3). A minimum witness can be transferred to the truncated caterpillar by choosing its at most three selected leaves among the retained leaves. Conversely, a proper witness on the truncated caterpillar extends to the original one by leaving all added leaves unselected. Every support still belongs to the witness and still has neighbor sum at least 2. The minimum sizes and feasibility consequently agree. ∎

The cap 3 on selected leaves cannot be replaced by 2. Consider the leaf word

$$
(3,0,0,1).
$$

The final support forces its adjacent spine membership to be 1. The next two spine sums then force the other interior membership to be 0, and the first support's sum must be 3. A witness has

$$
x=(1,0,1,1),\qquad y=(3,0,0,1),\qquad q=(3,2,1,2),
$$

and size 7. Replacing the initial 3 by 2 makes the instance infeasible.

The neighbor-sum cap 4 is also necessary in general. For leaf word $(1,1,2,1)$, every spine vertex belongs to $S$; the two endpoint sums must be 2. The first interior sum is then forced to be 3, and the second is forced to be 4. All nine vertices are selected in the unique minimum witness.

## 4. A 16-state acceptance criterion

The alphabet is the four symbols $0,1,2,3$, with symbol 3 representing any count at least 3. Define the local predicate

$$
\mathcal V_\ell(a,b,d,r)
$$

for bits $a,b,d\in\{0,1\}$ and $r\in\{1,2,3,4\}$ as follows:

- If $\ell=0$, the predicate holds exactly when $r=a+d$.
- If $\ell>0$, it holds exactly when
  $$
  b=1,\quad r\ge2,\quad 0\le r-a-d\le\min(\ell,3).
  $$

The variables represent the left spine membership, current membership, right membership, and current neighbor sum. Positivity of $r$ is already built into its domain.

Use the state set

$$
\mathcal Q=\{(a,b,q): a,b\in\{0,1\},\ q\in\{1,2,3,4\}\},
$$

which has 16 states. After reading position $i$, the state records

$$
(a,b,q)=(x_i,x_{i+1},q_i).
$$

**Initialization.** At the first symbol $\ell_1$, allow exactly the states $(a,b,q)$ satisfying

$$
\mathcal V_{\ell_1}(0,a,b,q).
$$

**Transition.** When the next symbol is $\ell$, allow

$$
(a,b,q)\longrightarrow(b,d,r)
$$

exactly when

$$
q\ne r\quad\text{and}\quad\mathcal V_\ell(a,b,d,r). \tag{4}
$$

**Acceptance.** After the final symbol, accept exactly states whose second bit is 0. This enforces $x_{k+1}=0$.

**Theorem 2.** A valid leaf word represents a caterpillar with a proper total dominating set if and only if it is accepted by this fixed 16-state rule.

**Proof.** Any minimum proper set has the bounds in Theorem 1. Its successive triples satisfy initialization, (4), and acceptance by (1)–(2), so it yields an accepting run. Conversely, an accepting run consistently determines all the bits $x_i$ and sums $q_i$; the overlap in consecutive states makes the assignments agree. Set $y_i=q_i-x_{i-1}-x_{i+1}$. The local predicates give exactly the appropriate leaf capacities, forced support memberships, and positivity conditions. Transitions give properness on spine edges. Equation (1) and the paragraph following (2) construct a proper total dominating set. ∎

This is a necessary and sufficient characterization expressed entirely through a fixed finite alphabet and a fixed finite state set. In particular, the accepted leaf words form a regular language, after intersecting with the elementary valid-spine endpoint conditions.

## 5. Minimum cardinality and witness construction

Give an initialized state $(a,b,q)$ the cost

$$
a+q-b=x_1+y_1.
$$

Give a transition $(a,b,q)\to(b,d,r)$ the additional cost

$$
b+r-a-d=x_{i+1}+y_{i+1}. \tag{5}
$$

All these costs are nonnegative whenever the local predicate holds. The minimum total cost of an accepting run is exactly $\gamma_{pt}(T)$: every run gives a set of that cardinality, and Theorem 1 supplies a minimum witness represented by a run.

Maintaining the minimum cost at each of 16 states takes $O(k)$ arithmetic operations. Each state considers only the eight pairs $(d,r)$. Storing a predecessor per reachable state per layer uses $O(k)$ space and reconstructs a minimum witness. Decision or minimum-value computation alone uses constant working state space. The usual bit cost of arithmetic on the input leaf counts and vertex labels is separate from this unit-cost operation count. Extracting the spine from an explicit adjacency-list input takes $O(|V(T)|)$ time.

The implementation is [caterpillar.py](caterpillar.py). For example:

```sh
python solutions/seven-problems-2026-10-09/combinatorics/caterpillar.py 3 0 0 1
```

It returns minimum size 7 together with the spine memberships, leaf counts, neighbor sums, and an explicitly labeled vertex set. Infeasible valid input returns JSON `null`.

## 6. Verification and status

[verify.py](verify.py) compares the algorithm to independent enumeration of vertex subsets on every caterpillar among all unlabeled trees of orders 2 through 13. It additionally checks short leaf words with capacities above the cap, both sharpness examples, and a 200-vertex spine whose leaf multiplicities exceed 100,000. Full counts and witnesses are in [verification.json](verification.json).

The subset checker uses open neighborhoods directly, without calling the local predicate or transitions. Thus an erroneous recurrence is not merely tested against itself. The rooted-tree generator enumerates multisets of all smaller rooted shapes, then canonicalizes the unrooted trees at their centers; its finite coverage is described in the verification notes in [README.md](README.md).

The assertion at arbitrary order follows from Theorems 1–2, not from the finite computations. This is a proposed complete answer to the existential characterization as an explicit finite-state criterion. Novelty beyond the inspected literature is not independently established, and the result is not peer reviewed.
