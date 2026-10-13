# Q3902 full-target attempt ledger

Exact target: gamma positivity of h* for every reflexive symmetric
homology or cohomology polytope, with the saturated ambient lattice.
Statement `ede55ed8ecc1ee3fb171`. The full universal assertion now has a
accepted attributed literature counterexample.
One failed proof route preceded the closure; partial results did not
reset that counter. No five-failure stopping disposition is asserted.

<a id="q3902-a1"></a>
## A1 — binary-code crosspolytopes and nonnegative forest assembly

Develop a gamma formula for every reflexive independent-column
configuration and then assemble a general boundary polytope from
nonnegative scalar weighted full-rank spanning-forest numerators.
[CROSSPOLYTOPES.md](CROSSPOLYTOPES.md) proves the binary-code formula
at all dimensions and lattice indices, hence closes all reflexive
homology examples with vanishing top homology. The actual triangle
graph disproves the assembly identity: all full-rank forests have
gamma=(1,0), but the full polytope has gamma=(1,2). Additional gluing
terms cannot be omitted. This is one failed full-target route with a
useful restricted theorem; the crosspolytope proof is not a separate
failed attempt or a full-target closure.

Evidence: CROSSPOLYTOPES.md, check_crosspolytopes.py,
CROSSPOLYTOPE-CHECK.json. The scoped theorem and failure count are accepted by independent root review.

<a id="q3902-literature-closure"></a>
## Resolution — primary series-parallel graph counterexample

The later primary Ferroni preprint arXiv:2607.02424v1 supplies the actual
simple graph with five paths of eight edges, whose reflexive homology
polytope has dimension 36 and gamma_16=-9799680. The primary dissection
identity and lattice hypotheses were audited, the complete numerator
reconstructed independently from marked sign words, and its gamma
expansion checked in two exact ways. This is an attributed full-target
counterexample, not a lookup counted as a failed route, a new local
counterexample claim, or a closure of the standalone cohomology or
Question 9.3 assertions. See Q3902-LITERATURE-CLOSURE.md, check_ferroni.py
and FERRONI-CHECK.json. Root review accepted the closure; further solving is stopped.
