# Automatic graphs and diagonal BVASS predecessors

The exact graph questions use a finite-word synchronous presentation.
For Q3077, K_m has both arcs between each pair. If the input has a
self-loop, K_m maps to that one vertex for every m. Otherwise any such
map is injective, and its image is a clique in the symmetric part
R(x,y)∧R(y,x), which remains synchronously regular.

The source baseline was read in Morvan's thesis Sections VIII.6 and X.2.
Its fixed-k regular-coloring results are distinct from unknown finite
palette size. [Primary source](https://arxiv.org/abs/2510.07422).

## Two exact obstruction examples

**Large finite cliques without an infinite clique.** Let the regular
vertex language be a*b*. Join distinct words precisely when they have
the same length, in both directions. Equality of lengths and inequality
of words are synchronous regular. Its length-n component is K_(n+1).
There is no infinite clique, because each length component is finite.
Thus decidability of infinite-clique existence does not decide bounded
finite-clique size.

**Bounded cliques without a finite coloring.** The shift graph has
vertices (i,j) with 0≤i<j, represented by the convolution of unary
integers. Join (i,j) and (j,k), i<j<k, in both directions.
All comparisons and equalities of unary integers are synchronous
regular. This graph is triangle-free. Indeed, for three edges among
three pair vertices, equality of end/start coordinates would have to
give an increasing cycle, or two different successors with equal
first coordinate, which cannot be adjacent.

It has no coloring with k colors for any finite k. For every i let
C_i be the nonempty set of colors used on (i,j), j>i.
Some i<j have C_i=C_j, since there are finitely many subsets of
the palette. The color of (i,j) belongs to C_j, so a vertex (j,l)
has that same color. Those two vertices are adjacent, a contradiction.
This is a full argument about the example, not a solution of the
general decision questions.

## Q3075: recursively enumerable completeness of finite regular coloring

1. **Enumerate color certificates.** Enumerate every finite tuple
   of DFAs, then check that their languages partition the regular
   vertex set and each class has no edge internally, using regular
   inclusion and emptiness. This proves the Σ⁰₁ upper bound.
   It does not prove hardness or decide the negative instances.
2. **Reuse fixed-k hardness.** A fixed-k NO instance can become
   YES when more colors are allowed. Even K_(k+1) is a NO
   for k and YES for a finite palette. Therefore the identity
   reduction from fixed-k regular coloring does not preserve
   NO at arbitrary finite palette size. No gadget controlling
   all finite palettes was found.
3. **Encode reachability via color propagation along paths.**
   A two-color constraint propagates alternating values along
   a connected path and can reflect a difficult reachability
   cut. With an arbitrary palette, proper coloring enforces
   only inequality at each edge, and a third color breaks
   deterministic alternation. The attempted path gadget
   does not force one global binary assignment. It would
   need a proof excluding every larger regular coloring.
4. **Bound the state size of a regular certificate.**
   Checking a proposed tuple is decidable. The attempted
   decision procedure enumerates tuples only up to a state
   bound derived from the edge automaton. No such computable
   bound for arbitrary palette size was proved. A finite
   presentation does not itself bound the size of a
   recognizable separator. The search remains a semidecision.
5. **Reduce colorability to bounded cliques.**
   The shift graph above has clique size at most two and
   no finite proper coloring at all. Thus bounded clique
   size cannot be a sufficient certificate for regular
   finite coloring. Ramsey considerations do not repair
   that proposed characterization.

Outcome: five failures; the Σ⁰₁ upper bound remains partial.

## Q3076: Σ⁰₂ completeness of finite proper coloring

1. **Compactness and finite restrictions.** For fixed k, finite
   proper coloring is equivalent to k-colorability of every
   finite induced subgraph. Enumerate vertices by word
   order and check each finite prefix. The full property
   has the form ∃k∀n C(G,k,n) with C decidable, proving
   the Σ⁰₂ upper bound. It supplies no matching reduction.
2. **Convert all proper colors into regular languages.**
   A coloring is an arbitrary function on the vertex set.
   The finite-prefix compactness proof chooses a path
   through an infinite tree of assignments; it provides
   no automaton for any chosen branch or color class.
   The attempted regularization theorem was not proved.
3. **Lift fixed-palette hardness to a second quantifier.**
   Hardness of one fixed-k problem does not imply that
   ∃k of those problems is Σ⁰₂-hard. A reduction must
   coordinate every palette size in the same output graph.
   A disjoint union of unrelated fixed-k instances gives
   only a supremum of chromatic numbers, not the
   required equivalence to an arbitrary Σ⁰₂ input.
4. **Make machine-run components into expanding cliques.**
   One-step machine transitions can be automatic. Testing
   that a word is an entire valid arbitrarily long run
   is not given by that one-step relation. Pairwise
   local constraints allow a clique to skip missing
   time steps; requiring a complete consecutive history
   needs an additional verified construction. No
   automatic reduction implementing it was obtained.
5. **Detect stabilization of finite-prefix chromatic numbers.**
   Their sequence is computable and nondecreasing. Boundedness
   is exactly the ∃k∀n problem from route 1; observing
   a long plateau cannot certify that it never rises.
   The shift graph supplies unbounded chromatic behavior
   while retaining clique bound two. No effective
   stabilization modulus was proved.

Outcome: five failures. The Σ⁰₂ upper bound is not a completeness result.

## Q3077: decide bounded bidirectional clique size

1. **Test for an infinite clique.** The length-component graph
   above has arbitrarily large finite cliques and no
   infinite clique. This proposed equivalence is false.
2. **Enumerate forbidden clique sizes.** For each fixed m,
   decide the FO sentence asserting a K_m homomorphism.
   If some m fails, the search halts with a bound.
   This is a semidecision of boundedness. When all
   m succeed, it produces no finite negative certificate.
3. **Pump a clique tuple through the edge automaton.**
   Pumping can lengthen the words in a fixed m-tuple;
   it does not create a new independent coordinate.
   The product machine already uses m(m-1) edge
   constraints, so its state count grows with m.
   No bound on clique size independent of this
   expanding tuple machine was obtained.
4. **Use a regular homogeneous-set witness.**
   The length-component graph admits regular sets of
   vertices, but an infinite clique cannot meet different
   lengths. Regularity of the vertex language does not
   turn its unbounded finite cliques into one regular
   infinite clique. That witness search misses this
   explicit automatic example.
5. **Use finite coloring as the boundedness certificate.**
   A k-coloring indeed bounds clique size by k in a
   loop-free graph. The converse fails by the shift
   graph's exact triangle-free infinite-chromatic
   construction. A coloring-based boundedness method
   is therefore incomplete even before requiring
   its classes to be regular.

Outcome: five failures; a general decidability proof is absent.

## Q3079: semilinearity of same-leaf 2-BVASS predecessors

The target asks for possible x∈N² when every leaf is the *same*
(q,x) and the root is a fixed configuration t. The forward
semilinearity theorem in
[Bizière et al.](https://arxiv.org/abs/2506.22561)
was read locally. The author
[problem page](https://automata.exchange/25.8-semilinearity-of-2-bvass-backward-reachability-set/)
explicitly distinguishes the backward question.

1. **Reverse a forward 2-BVASS.** Reversing a unary step
   is harmless. Reversing a branch x+y=z needs every
   possible split of z, not a transition adding one
   fixed vector. This is a top-down split rule of
   a different formalism. The forward semilinearity
   theorem cannot be invoked after this reversal.
2. **Prove the entire relation semilinear first.**
   In the one-state, one-counter branch-only system,
   a root y from leaves x is exactly y=kx for k≥1.
   This relation is divisibility and is nonsemilinear.
   Thus the proposed stronger intermediate theorem
   is false, even in dimension one. For fixed y
   its divisor set is finite, so this does not
   refute the retained fixed-target question.
3. **Store the input as frozen extra counters.**
   To run forward with symbolic x, extra counters
   would have to remember both coordinates at
   every leaf. Ordinary branching adds those
   registers too, instead of copying one frozen
   input to each child. The proposed construction
   both changes dimension and loses same-leaf
   equality. No 2-dimensional encoding was given.
4. **Union the semilinear solutions for each tree shape.**
   For a fixed shape with k leaves, the root has
   form kx+c, with linear nonnegativity constraints
   at its nodes. Its possible x are semilinear.
   There are infinitely many shapes. Infinite
   unions of semilinear sets need not be semilinear.
   No finite shape/pumping bound was proved.
   Branches and negative unary moves can balance
   to arbitrarily large trees even at a fixed root.
5. **Apply uniform cone acceleration backward.**
   The forward algorithm accelerates fixed-input
   reachable periods. In the diagonal predecessor
   family, a subtree's kx term depends on its
   leaf count; combining children requires their
   unknown leaf values to agree. Cone closure
   discards those equalities and exact prefix
   nonnegativity constraints. No exact finite
   family of periods for all k was derived.

Outcome: five failures. Forward and backward semilinearity are
kept separate; no catalog mark of disproved is appropriate.
