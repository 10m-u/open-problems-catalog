# Independent review of the Q270 transitive-tournament bunkbed proof

Reviewer: discrete-mathematics workstream. Date: 2026-10-09.

**Verdict: accepted.** The proof in probability/Q270-transitive-tournament-bunkbed.md establishes the full catalog question and its stated extension to common horizontal retention $p\in[0,1]$ and independent vertex-dependent vertical retention probabilities $q_j\in[0,1]$. No substantive gap was found.

## Primary-source match

Independently inspected Lawrence Hollom's thesis, *Extremal, Probabilistic, and Infinitary Problems in Combinatorics*, at <https://api.repository.cam.ac.uk/server/api/core/bitstreams/a0069f85-e810-476b-ba41-c2babc9c2f0b/content>. Model 6.4.5, printed p. 153, samples a uniform subset of the bunkbed edges, and Conjecture 6.6.4, printed p. 158, asks the inequality specifically for transitive tournaments. The published counterpart, <https://www.repository.cam.ac.uk/bitstreams/3a9595ae-7514-4075-b8e4-721c65d1cee0/download>, agrees in Model 4.5 and Conjecture 6.4. Its original bunkbed construction uses undirected vertical edges; the separately defined fully directed model changes this convention. The reviewed proof uses the correct original convention.

## Reachable counts and conditioning

Since every horizontal arc increases the vertex index, later exposures cannot change earlier reachability. Vertices outside the interval from source to target can be deleted. Conditional on all earlier exposed edges, the sets of incoming arcs to the two new copies are disjoint fresh independent edge families. The probability that none comes from a reachable predecessor is $(1-p)^a$ in one layer and $(1-p)^b$ in the other, using only the counts $a,b$. Completeness of the predecessor sets in a transitive tournament justifies this reduction.

Every row of the displayed transition table is correct. If neither layer is reached horizontally, a retained vertical edge still reaches neither. If exactly one is reached, the vertical edge decides whether one or two new vertices are reached. If both are reached, the vertical edge is irrelevant. The table is equivariant under interchanging the counts, and their difference changes by at most one.

## The stopping-time cancellation

The event that the chain first hits the diagonal at time $j$ depends only on edges exposed through that time. Conditional on any such history with counts $(a,a)$, all future edge families retain their original independence and the future count law is symmetric under interchanging coordinates. This symmetry does not require the already exposed graph itself to be symmetric.

For each possible first diagonal time and diagonal state, the terminal antisymmetric function

$$
g(a,b)=(1-q_v)\big((1-p)^b-(1-p)^a\big)
$$

has conditional expectation zero. Summing these finitely many cases proves the cancellation on paths that have hit the diagonal. All remaining paths started at $(1,0)$ and cannot cross to a nonpositive count difference without hitting zero; hence their terminal $g$ is nonnegative. This is a valid finite Markov argument, with no unjustified independence after conditioning and no optional-stopping integrability issue.

## Boundaries and the strict bound

For $u=v$, same-layer reachability is 1 and cross-layer reachability is $q_u$, because a forward horizontal path cannot return. For $u>v$, both probabilities are zero. The transition proof covers $p=0$ and $p=1$, taking $0^0=1$ for the empty predecessor family. It also covers $q_u=1$ and $q_v=1$, where symmetry or the common target edge forces equality.

The event used for the lower bound is correctly measured. Require the source vertical edge to be absent and the reachable-count state to stay $(1,0)$ at every intervening pair. At each such pair only the source in layer 0 is reachable, so no new incoming reachable arc has probability $1-p$, independently of its vertical edge. The event therefore has probability

$$
(1-q_u)(1-p)^{v-u-1}.
$$

It avoids the diagonal and contributes $g(1,0)=(1-q_v)p$. All other surviving contributions are nonnegative. Thus the stated lower bound is valid, and at $p=q_j=1/2$ it is exactly $2^{-(v-u+2)}>0$ for $u<v$.

The proof appropriately restricts its conclusion to transitive tournaments with the independent horizontal-edge model. It does not establish the false general acyclic-digraph conjecture.
