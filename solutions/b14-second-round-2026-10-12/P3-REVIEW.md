# Independent review: polynomial expected descent on the full sparse Exp model

12 October 2026. The retained agent proposed the normalized anti-concentration
argument below; the main thread independently checked its conditioning,
piecewise-linear proof, tail summation and source comparison. This review
accepts the full P3 convergence ambition, subject to the stated arithmetic
model. No originality or external peer-review claim is made.

## The precise accepted claim

For a fixed connected simple graph with n>=3 vertices and m edges, assign
independent Exp(1) weights and use its all-vertex shortest-path metric.
Every strictly improving 2-opt descent, from any tour and with any pivot,
has expected move count at most

    10 m(m-1) n^5 (1+log(n!)).

For m<=cn this is O_c(n^8 log n). The bound is uniform over all descents,
so an initializer or pivot depending on the observed weights is allowed.
The implementable declared rule is NN from vertex zero, label-based ties,
then first improving legal pair in lexicographic edge-position order,
restarting the scan after each reversal. It uses at most O(n^2) gain
evaluations per move and for its final scan; matrix construction by
Floyd–Warshall costs O(n^3). Expected real-arithmetic work is therefore
O_c(n^10 log n). Exact finite-bit runtime for sampled irrational weights
is a separate question.

## Independent proof audit

Let W be the sum of generating weights and z=w/W. The z-vector is uniform
on the (m-1)-simplex. Fix an edge e, condition on the OTHER-coordinate
ratios v_f=z_f/(1-z_e), and write t=z_e. Crucially this does not condition
on their actual z_f values, which would determine t. The Dirichlet density
factorization gives independent t~Beta(1,m-1), with density bounded by m-1.

For any vertex pair, partition its finite simple paths by whether they
use e. Their least other-coordinate costs A and B depend only on v.
The distance is min((1-t)B,(1-t)A+t), with missing classes represented
by infinity and ignored. A bridge is covered by the single finite line.
Each distance switches at most once. A four-distance exchange gain has
at most five pieces,

    g(t)=b(1-t)+a t, with a in {-2,-1,0,1,2}.

On a piece with a!=0 and 0<g<=epsilon<1,

    |a-b| = |a-g|/(1-t) >= (1-epsilon)/(1-t) >= 1-epsilon.

Thus the selected small-positive part of one piece has length at most
epsilon/(1-epsilon). Its conditional probability is at most that length
times m-1. The five pieces give at most
5(m-1)epsilon/(1-epsilon).

At a weight vector with positive gain, the selected shortest paths give
g(z)=sum_e gamma_e z_e. At least one integer coefficient gamma_e is
nonzero. Almost surely the shortest paths are unique; the measure-zero
ties may be discarded. Therefore selecting the required edge costs a
union bound over m edges, not an independence assumption. For epsilon<=1/2,
one ordered quadruple has small-positive probability at most
10m(m-1)epsilon. At most n^4 quadruples then give

    Pr(eta_min<=epsilon) <= 10m(m-1)n^4 epsilon,

where eta_min is the smallest positive exchange gain divided by W and
equals infinity if no positive gain exists. Flat pieces with positive
gain are not incorrectly counted under an arbitrary chosen edge: the
union uses an edge with its NONZERO raw path coefficient.

Every metric distance is at most W, hence every initial tour costs at
most nW. Strict descent therefore has N<=n/eta_min. It also visits
distinct tours, so N<n!. For x>=2n, substitute epsilon=n/x. For x<2n,
the trivial probability bound one is at most
10m(m-1)n^5/x (m>=2). Summing the uniform bound through n! and using
the harmonic-sum ceiling 1+log(n!) proves the displayed expectation.
No independence between initial length and minimum gain is used, and
no Gamma tail or expectation-of-a-ratio substitution is needed.

## Prior art and finite controls

Polynomial expected convergence was already proved in
[Klootwijk, Manthey and Visser, TCS 866 (2021), Theorem 20](https://doi.org/10.1016/j.tcs.2021.03.016):
O(n^8 log^3(n) beta/alpha), with their cut parameters. A connected
simple graph has alpha>=1/floor(n^2/4) and beta<=1, so that theorem
already gives a polynomial bound on every graph here. The conditioned-edge
coefficient method also appears in its Lemmas 18–19. The present local
normalization proof supplies the stated cut-free bound; it is not a
claim to originate polynomial convergence.

[audit_p3_gain.py](audit_p3_gain.py) independently enumerates all simple
paths in nine fixed graph cases on four to six vertices, uses exact
rational arithmetic and distinct binary path-sum perturbations, and
checks 1512 ordered quadruples, 20376 ordinary and 20376 normalized
pieces. It verifies homogeneous coefficient reconstruction and the
eligible small-positive interval-length bounds. These finite controls
support, rather than replace, the all-size probability proof.
[Receipt](P3-INDEPENDENT-CHECK-RESULTS.json).

**Disposition:** P3 is answered for the full stated sparse exponential
move-count model. This does not bound NN's initial approximation ratio,
solve Q3817, or give an exact TSP algorithm. The deterministic quadratic
tree bound remains a stronger restricted result.
