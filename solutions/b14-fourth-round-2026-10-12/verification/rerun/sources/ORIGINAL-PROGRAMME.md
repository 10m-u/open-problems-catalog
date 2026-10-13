# B14 — Solving traveling salesman problems

Build methods that find shorter tours, prove that tours are optimal, or explain when a tractable method succeeds. Start with symmetric TSP, especially metric and Euclidean instances. The most useful first direction is to combine a good incumbent tour with certified edge elimination and an exact treatment of the remaining graph. A second direction studies the local-search landscape and the effect of initialization. Approximation theory supplies longer-term targets and structural guidance.

**Initial register:** eight existing catalog questions, six programme questions, and a ranked first research round. The programme questions below are proposed investigations; they are not new catalog entries or established conjectures. The catalog questions retain their original statements and status records. No B14 result has yet been filed.

Catalog membership · Live question matches · [Research index](../README.md)

## What solving means

For a complete undirected graph on $n\geq3$ vertices with symmetric nonnegative costs $c_{ij}$, a tour visits every vertex once and returns to its start. Write $OPT(c)$ for the minimum tour cost. Rational costs have a finite binary encoding; Euclidean instances also require a declared distance and rounding convention.

| Goal | Evidence of success | Main methods |
|---|---|---|
| Exact solution | A feasible tour of cost $U$, together with a valid lower bound $L=U$ | Dynamic programming, branch-and-cut, certified elimination, decomposition |
| Approximation theorem | A stated model and a proved bound $U\leq\alpha OPT$, with the algorithm's runtime | LP rounding, spanning trees, parity correction, geometric dissection |
| Better practical search | Improved cost or time under the same computation budget, across held-out instances | Lin–Kernighan search, restarts, tour merging, guided branching |

A metric satisfies $c_{ij}\leq c_{ik}+c_{kj}$. A graph metric takes shortest-path distances in a connected weighted graph. A Euclidean metric uses distances between points in a fixed-dimensional space. Independent random weights on the edges of a complete graph generally do **not** form a metric; Q3818 uses that model. Asymmetric TSP has directed costs and needs separate arguments.

When $L>0$, $U/L-1$ is a certified upper bound on the relative optimality gap. A small observed gap is useful even when equality is out of reach. General exact polynomial-time TSP remains a P-versus-NP-scale ambition; the working targets here are specific algorithmic and structural improvements.

## Established starting points

**Exact methods.** Concorde provides an established exact solver and a comparison for any new certification method. Its authors report optimal solutions for the 110 TSPLIB TSP instances, including an 85,900-city instance. This demonstrates the reach of exact computation on particular instances. [Concorde](https://www.math.uwaterloo.ca/tsp/concorde/)

For small instances, use subset dynamic programming as the reference oracle. Fix a root $r$. For $S\subseteq V\setminus\{r\}$ and $j\in S$, let $D(S,j)$ be the least cost of a path from $r$ through exactly $S$, ending at $j$. Then

$$
D(\{j\},j)=c_{rj},\qquad
D(S,j)=\min_{i\in S\setminus\{j\}}\bigl[D(S\setminus\{j\},i)+c_{ij}\bigr],
$$

and $OPT=\min_j[D(V\setminus\{r\},j)+c_{jr}]$. The direct implementation takes $O(n^2 2^n)$ arithmetic operations and $O(n2^n)$ storage. It is a correctness oracle for a bounded experiment, not a scalable baseline.

**Lower bounds.** The symmetric subtour LP minimizes $c^Tx$ subject to

$$
x(\delta(v))=2\quad(v\in V),\qquad
x(\delta(S))\geq2\quad(\varnothing\ne S\subsetneq V),\qquad
0\leq x_e\leq1.
$$

Here $\delta(S)$ is the set of edges crossing from $S$ to its complement, and $x(F)=\sum_{e\in F}x_e$. Integer feasible points are tours; fractional points give a lower bound. Minimum-cut separation avoids listing every subtour inequality. Branch-and-cut adds valid inequalities and branching until an optimum is certified. A feasible tour supplies the upper bound.

**Metric approximation.** Christofides–Serdyukov uses a minimum spanning tree, a minimum-cost perfect matching on its odd-degree vertices, and Euler-tour shortcutting. It guarantees $3/2$ for symmetric metric TSP. Karlin, Klein and Oveis Gharan proved a randomized $3/2-\epsilon$ guarantee for some $\epsilon>10^{-36}$, then the corresponding subtour-LP bound; their later work derandomizes the approach. The improvement is a structural breakthrough and a source of rounding techniques. [Randomized algorithm](https://arxiv.org/abs/2007.01409v6), [LP bound](https://arxiv.org/abs/2105.10043v3), [deterministic algorithm](https://arxiv.org/abs/2212.06296)

**Geometry.** Fixed-dimensional Euclidean TSP already has a polynomial-time approximation scheme. Mömke and Zhou give a randomized scheme with running time $2^{O(1/\epsilon^{d-1})}n$ for fixed dimension $d\geq2$, in their April 2025 version. A useful new target must improve implementation, constants, certification, or a specified extension rather than propose the existence of a Euclidean PTAS. [Euclidean approximation scheme](https://arxiv.org/abs/2411.02585v2)

**Formulation boundary.** Fiorini and coauthors proved that the TSP polytope has no polynomial-size linear extended formulation, even without a symmetry restriction. Compact *relaxations*, instance-dependent cuts and restricted graph families remain useful. An exact universal polynomial-size LP description is already ruled out. [Extension-complexity theorem](https://arxiv.org/abs/1111.0837v5)

## Catalog questions and their uses

Grades follow the existing B-series convention: **S** means the same object or a direct sub-question; **M** means a shared method or close analogue; **L** means an exploratory connection. These grades express relevance. The exact statements remain on the linked catalog pages.

### Sparse random metrics

**Q3817, S.** Give each edge of any connected simple graph $G$ an independent exponential weight of rate one. Form its shortest-path metric on all vertices. Starting at $v$, nearest neighbor repeatedly visits the closest unvisited vertex, then returns to $v$. For each fixed $c\geq1$, does a constant $C_c$ bound

$$
\mathbb E[NN_v/OPT]\leq C_c
$$

uniformly over $n\geq3$, $|E(G)|\leq cn$, and every start vertex?

Klootwijk and Manthey prove a nearest-neighbor bound under an additional fast-growing-cut condition. They also prove a constant expected ratio for the worst 2-opt local optimum on arbitrary sparse graphs, without that condition. Thus Q3817 concerns the greedy initializer; the corresponding local-optimum quality bound is already available. [Algorithmica 2023, §§4.2, 5–6](https://doi.org/10.1007/s00453-023-01167-3)

**Use:** investigate how narrow cuts, bridges and repeated returns affect greedy tours. Begin with paths, stars, trees and chains of small dense blocks. Relate excess crossings to an instancewise lower bound before taking expectations. A bound on $\mathbb E[NN]/\mathbb E[OPT]$ does not establish the displayed expectation of a ratio.

### Counting local optima

**Q3818, S.** Assign independent uniform $[0,1]$ costs to the edges of $K_n$. Let $M_n$ count distinct undirected tours, identifying rotations and reversal, that admit no strictly improving cycle-preserving two-edge exchange. Is

$$
\mathbb E[M_n]=O(\sqrt{n!})?
$$

Manthey and van Rhijn prove an upper bound $O(1.2098^n\sqrt{n!})$, and prove that counting 2-opt local optima is #P-complete. Their Conjecture 17 asks whether the exponential factor can be removed. [MFCS 2025, §4 and Conjecture 17](https://doi.org/10.4230/LIPIcs.MFCS.2025.73)

**Use:** study the dependencies among the inequalities defining a fixed tour's local optimality. Symmetry gives

$$
\mathbb E[M_n]=\frac{(n-1)!}{2}\Pr(\text{a fixed tour is 2-optimal}).
$$

The probability becomes an integration problem after conditioning on the tour-edge costs. Dependencies caused by shared replacement edges are central. Counting optima alone does not determine their costs, attraction-basin sizes, or the number of descent steps.

### Finding short optimality certificates

**Q549, M.** For a bounded rational polytope containing no integer point, can one find a general-disjunction branch-and-bound refutation in time polynomial in the input encoding and the smallest refutation's leaf count? Branches use integer splits $a^Tx\leq b$ versus $a^Tx\geq b+1$; leaves require LP-infeasibility certificates. Coefficient encoding belongs in the accounting. Gläser's thesis poses this automatization question. [Dissertation, §§5–6](https://tuprints.ulb.tu-darmstadt.de/server/api/core/bitstreams/3c676d11-8374-4609-b9d5-8f98004ba917/content)

**Use:** after finding a tour of integer cost $U$, impose a cost cutoff $c^Tx\leq U-1$ on the integer TSP formulation. Refuting that system proves optimality. Rational costs can first be scaled to integers with bit complexity recorded. The open transfer is whether a branching policy can find small TSP certificates. A small certificate and the ability to discover it are distinct questions; Concorde's cut system also differs from the bare branching calculus.

**Q550, L.** Consider the matching relaxation $\sum_{e\ni v}x_e\leq1$, $0\leq x\leq1$, and $\sum_e x_e\geq(|V|-\delta+1)/2$, promised to contain no integer point. Can a variable-branch refutation be found in

$$
f(\operatorname{tw}(G))\,\operatorname{poly}(|G|,\delta,T_{\rm var})
$$

time, where $T_{\rm var}$ is the minimum variable-branch leaf count? Existing parameterized results also place the certificate size and deficiency parameter inside the parameter dependence. Exact relaxation and statement, [Gläser, Question 5.26](https://tuprints.ulb.tu-darmstadt.de/server/api/core/bitstreams/3c676d11-8374-4609-b9d5-8f98004ba917/content)

**Use:** a controlled example of the difference between efficiently solving a graph problem and efficiently discovering a proof in a restricted calculus. Matching is polynomial-time solvable; this question concerns the restricted refutation system. Its treewidth idea motivates measuring the width of a TSP graph after elimination, but gives no TSP runtime theorem.

### Structured cheap-edge graphs

For a simple graph $H$ on $n\geq3$ vertices, set $c_{uv}=1$ on its edges and $c_{uv}=2$ on all other pairs. These costs are metric, and $OPT=n$ exactly when $H$ has a Hamiltonian cycle. This elementary reduction makes the following existence questions relevant to structured (1,2)-TSP. A constructive proof could yield tours attaining the trivial lower bound $n$; an existence theorem alone need not give an efficient construction.

**Q1852, M.** For $n\geq4$ and $k\geq2$, must every spanning subgraph $H\subseteq P_n^k$ satisfying

$$
\deg_H(v)\geq\tfrac12\deg_{P_n^k}(v)+2\quad\text{for every }v
$$

contain a Hamiltonian cycle? Here $P_n^k$ joins vertices at path distance at most $k$. [Espuny Díaz and coauthors, Conjecture 6](https://doi.org/10.37236/13474)

**Q1853, M.** For $n\geq3$ and $1\leq k\leq\lfloor n/2\rfloor$, must every spanning $H\subseteq C_n^k$ with minimum degree at least $k+1$ contain a Hamiltonian cycle? [Same paper, Conjecture 1](https://doi.org/10.37236/13474)

**Use:** investigate boundary connectivity states along the underlying path or cyclic order. First ask which degree conditions force a compatible completion across each boundary. These unweighted targets supply restricted instances; arbitrary geometric proximity graphs need additional hypotheses.

**Q1953, M.** Is every connected bicirculant Hamiltonian except $K_2$ and $G(m,2)$ with $m\equiv5\pmod6$? A bicirculant is a finite simple regular graph with an automorphism having exactly two equally sized vertex orbits. The generalized Petersen graph $G(m,2)$ has edges $u_i u_{i+1},u_i v_i,v_i v_{i+2}$, with indices modulo $m$. [Bonvicini, Pisanski and Žitnik, Conjecture 1](https://arxiv.org/abs/2604.21607)

**Use:** exploit symmetry to organize cheap-edge instances and compress descriptions of candidate constructions. A Hamiltonian tour need not itself preserve the graph's automorphism. Restricting the search to symmetric tours would require a separate completeness argument.

### A comparison problem for descent paths

**Q3819, L.** Partition a set of $n$ real points into $k$ nonempty clusters and minimize within-cluster squared error. A permitted move transfers one point, preserves nonempty clusters, recomputes means, and strictly decreases the objective. Does every initial partition admit an improving path of polynomial length to a local optimum? [Manthey and van Rhijn, STACS 2024, §5](https://doi.org/10.4230/LIPIcs.STACS.2024.52)

**Use:** distinguish the existence of a short descent path from a polynomial bound for a particular pivot rule. The same distinction matters for 2-opt and Lin–Kernighan. This is a one-dimensional clustering question; no reduction to TSP is asserted. Keep it as a method comparison rather than a first-round target.

The catalog's retained status checks for these entries date from 5–10 October 2026 and report no full resolution found. They are bounded literature checks, not proofs of openness. None of these eight stable IDs currently has a catalog resolution mark. Source results above are background facts, with their own scope.

## Programme questions

### B14 P1 Certified elimination with useful residual structure

**Question.** Given a feasible tour of cost $U$, which combination of reduced-cost bounds and local exchange arguments removes the most edges safely per unit of computation? Does the residual graph become easier for exact search in a measurable way?

For an edge $e$, compute a valid lower bound $L_e$ on tours containing it. If $L_e>U$, no optimal tour uses $e$. Record the bound and its certificate with the deletion. Start with dual information from a relaxation, then consider combinatorial elimination. Cook, Helsgaun, Hougardy and Schroeder already combine these ideas; their 2023 study reduces most tested complete graphs to fewer than $3n$ edges. The research target is improved selection, certification and downstream structure. [Local elimination](https://arxiv.org/abs/2307.07054)

**First deliverable:** compare elimination methods at equal time budgets, recording residual edge count, degree distribution, decomposition width, verification cost and subsequent exact-solver work. A certificate must be checked against the original costs. Sparsity by itself does not imply small treewidth or easy TSP.

### B14 P2 Compress connectivity states after elimination

**Question.** Can exact search on the residual graph retain substantially fewer boundary states by using forced edges, degree restrictions and dual information?

A decomposition state must record each boundary vertex's current degree and how unfinished path ends connect. Forbid a completed cycle while unvisited vertices remain. Merging states only by boundary degrees loses this connectivity information and can accept disjoint cycles. Known bounded-width dynamic programming is the starting point; a new contribution needs a proved state reduction, a better parameter dependence, or useful integration with P1.

**First deliverable:** an explicit state-equivalence rule with a proof that every completion has the same feasibility and relative cost behavior. Check the rule against subset-DP optima on small weighted graphs. Q1852–Q1853 provide ordered graph families; Q550 provides a proof-search comparison. Discard the compression rule if one retained representative can lose the best completion.

### B14 P3 Initialization and the cost of reaching a local optimum

**Question.** On Q3817's sparse exponential shortest-path metrics, what can be proved about the number of improving 2-opt moves after nearest-neighbor initialization, for a precisely specified pivot rule?

Specify best improvement or first improvement, edge scanning order, starting vertex and tie handling. The existing bound for the worst local optimum already controls final expected tour quality. The additional target is the cost of getting there, or a sharper initializer-specific guarantee. The source's concluding section explicitly proposes studying initialization together with local search. [Klootwijk and Manthey, §6](https://doi.org/10.1007/s00453-023-01167-3)

**First deliverable:** a proof or an explicit obstructing family for one graph class, beginning with trees or chains of bounded-size blocks. In experiments, record moves, move-evaluation work and final cost separately. Continuous random weights and tiny improvements require more than the observation that the objective strictly decreases.

### B14 P4 Locate and explain difficult subtour LP supports

**Question.** Which support and cut structures make the ratio $OPT/LP$ large, and can a restricted family support a stronger rounding theorem?

The central long-term target is the $4/3$ integrality-gap conjecture for symmetric metric TSP. Cook, Hougardy and Petrich's September 2026 version reports exact verification through $n=16$, and through $n=18$ for half-integral extreme points. It also corrects incomplete earlier enumerations. Use their published representatives to investigate specific obstructions rather than repeat the full enumeration. [Paper, §§1–3](https://arxiv.org/html/2603.12995v5), [authors' dataset](https://doi.org/10.60507/FK2/JK95PC)

**First deliverable:** select a small, named family of fractional supports; reproduce its gap calculation with exact certificates; inspect near-tight cuts, tree parity and the cost of correction. Then formulate a rounding lemma with explicit assumptions. A finite search can refute a conjecture with a valid counterexample, or prove a bounded case; confirming samples does not prove the unrestricted gap bound. An existential gap theorem and an efficient rounding algorithm are separate deliverables.

### B14 P5 Remove the extra factor in the local-optimum count

**Question.** Can Q3818's fixed-tour probability be bounded sharply enough to remove the factor $1.2098^n$ from the known upper bound?

Read the paper's polytope-volume formulation and identify the inequality family responsible for the loss. Candidate approaches include conditioning on tour-edge sums, integrating replacement edges in a dependency-aware order, and exploiting the cyclic incidence structure rather than applying independent-event estimates.

**First deliverable:** reproduce the existing derivation for one bounded case, then prove a tighter inequality for an explicit family of exchange constraints. Small-instance enumeration can check conventions and suggest the next lemma. Estimates should include variance and sampling error: the local-optimality event becomes rare. A stronger local-search runtime or tour-quality claim would need its own argument.

### B14 P6 Use learned guidance inside a certified solver

**Question.** Can a policy trained to choose branches, cuts or elimination checks reduce time to a certified answer on new instance families?

Try guidance on top of a correct solver before designing a new end-to-end tour generator. Feasibility checks, valid bounds and exhaustive fallback remain responsible for correctness. A learned score alone cannot justify deleting an edge. Q549 supplies the distinction between discovering a certificate and having a certificate; P1 supplies a concrete place to spend computation.

**First deliverable:** compare a policy against the same solver's ordinary rule, random selection and a simple hand-built score. Match training and inference costs, random seeds, stopping rules and hardware. Hold out entire graph or geometric families, as well as larger sizes. Report proof time and remaining gap alongside tour cost. This is an experimental proposal, with no asserted runtime guarantee or novelty.

## A useful first research round

Begin with **P1 and P2 as one practical thread**: the object is a certified sparse graph containing an optimum, followed by an exact method that benefits from its measured structure. The first theoretical companion should be **P5**, because it has a precise published conjecture and a known derivation to improve. Use **Q3817/P3** for a probabilistic thread once a graph family and pivot rule have been fixed. P4 is the longer approximation-theory thread; P6 depends on having a trustworthy solver and comparison set.

| Step | Deliverable | Condition for continuing |
|---|---|---|
| Fix a model | A short specification of costs, encoding, tour convention and objective | Instances and claims use the same model |
| Reproduce a baseline | Verified small-instance optima, lower bounds and local-optimum checks | Independent checks agree |
| Try one structural idea | An elimination rule, boundary-state lemma, probability inequality or obstructing family | A theorem with explicit assumptions, or a measured effect that survives controls |
| Test transfer | A comparison on a different instance family or a stronger bounded case | The gain survives the changed setting, or the failure is explained |
| File a result | Statement, proof or experiment, original instance, checker and remaining question | Evidence supports exactly the filed scope |

This is the proposed first round. Starting the programme creates its question register and research direction; expensive benchmark runs, solver training and full enumerations need their own scoped work decision.

## Instance families and measurement

Use a compact comparison set before scaling:

- Small integer-cost symmetric instances with subset-DP optima.
- Exact Euclidean distances and TSPLIB-style integer distances as separately labeled families.
- Clustered and narrow-bridge geometric instances, to test sensitivity to separators.
- Shortest-path metrics on trees, grids and chains of blocks with independent exponential edge weights, matching Q3817's assumptions.
- Independent uniform complete-graph costs for Q3818, kept separate from metric instances.
- Structured (1,2)-metrics built from path powers, cycle powers and bicirculants.

For each run retain the instance or its generation seed, distance convention, tour, independently recomputed cost, valid lower bound, elapsed time, algorithm settings and timeout. Use several seeds and retain failures. Compare time to a chosen certified gap as well as time to a good tour. For local-search analysis, distinguish tour count, basin size, final quality and descent length.

[TSPLIB's documentation](https://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/) defines its integer distances and several distinct problem types. Read the relevant edge-weight specification before treating coordinates as ordinary Euclidean distances. Concorde and Lin–Kernighan implementations supply practical reference methods; the [Concorde downloads](https://www.math.uwaterloo.ca/tsp/concorde/downloads/downloads.htm) include the Linkern heuristic.

## Result filing and stable identities

Keep substantive B14 proofs, experiments and instance certificates in a dedicated research directory when the first result exists. Record concise decisions and pointers in the agent workspace. Add a catalog resolution only when the exact catalog scope is established; a programme-local lemma may be useful while its source question remains open.

| Catalog question | Stable statement ID | Grade |
|---|---|:---:|
| Q3817 | `5be5b12412c27b8f10e5` | S |
| Q3818 | `1ab793013b1b4b6d4773` | S |
| Q549 | `b9a6eb3295c70a2650fa` | M |
| Q1852 | `485e3db2ff80a9c3f88c` | M |
| Q1853 | `b0595805fe9a6a579e48` | M |
| Q1953 | `acaff2fff07a60387e2d` | M |
| Q550 | `b2c816fbbf814f26e51a` | L |
| Q3819 | `86957b46ff680574e1f7` | L |

Membership and grades are maintained in candidate-programmes.json and reading-notes.txt. The public catalog's corresponding question pages preserve the same numbered identities; this programme is filed in the private research catalog.
