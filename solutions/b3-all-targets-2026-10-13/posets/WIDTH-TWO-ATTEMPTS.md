# Q3568: five proposed full-target failures

The target is ordinary coefficient positivity for every width-two
weak order polynomial. The primary [Section7.1](https://arxiv.org/html/2503.16403v3)
retains the question, with tests for both chains of size at most5 and
complement zigzags through200. We do not count those replays.
Independent route review accepted all five counts.

<a id="q3568-w01"></a>
## W01 — construct an actual negative coefficient beyond the chain bound

Generate naturally labelled posets consisting of two chains of size6,
using132 six-A/six-B reference words and three deterministic cross-edge
rules, close transitively and remove duplicate relations. All394 actual
posets have nonnegative scaled ordinary coefficients. The independent
chain partition certifies width at most2. Some have longer maximum
chains because of the added relations; this is beyond, not within, the
source's reported m,n<=5 chain-encoding bound. No exhaustiveness over
all6×6 encodings or arbitrary sizes is asserted. The exact relation
lists, h* and12!Ω rows are retained. This counter-construction fails
to find a target violation, with no conclusion for arbitrary posets.

<a id="q3568-w02"></a>
## W02 — extend the all-size weak-layer proof to every width-two poset

The proof in WIDTH-TWO-WEAK-ORDERS.md gives positivity and a vertical
root line for all ordinal sums of singleton/two-element layers. Try
to cover every width-two poset by that form, using width2 to group
incomparable elements into layers. The actual three-element chain2
plus isolated element defeats the proposed reduction: incomparability
is not transitive (the isolated point is incomparable to both chain
points, which are comparable). Its descent h*=1+2t differs from both
possible layer rows for N3, namely1 and1+t. It cannot be a weak order
or have the required (1+t)^k row. Its own Ω=t²(t+1)/2 is positive.
Thus width alone does not provide the claimed layer factorization.
A broader two-chain residual recurrence was not obtained. The partial
theorem remains valid at all sizes and does not reset this full-target
failure count.

<a id="q3568-w03"></a>
## W03 — transfer positivity from real-rooted descent data

Try a general Eulerian-transform lemma: nonnegative, real-rooted h*
would force nonnegative ordinary Ω. Work an actual finite poset
relaxation, the five-element star with one minimum and four incomparable
maxima. Its h* is1+11t+11t²+t³=(1+t)(1+10t+t²), real-rooted and
positive. But Ω(t)=sum_(j=1)^t j⁴ has

    120Ω(t)=24t⁵+60t⁴+40t³-4t.

The linear coefficient is negative. This poset has width4, so it is
not a target counterexample. It refutes the specified input-only
transform lemma and identifies the missing width-two structural
estimate. The primary reduction to the linear coefficient is not
discharged by root data alone. This differs from W02's isomorphism/
family-coverage failure.

<a id="q3568-w04"></a>
## W04 — identify the two-chain encoding with its skew cell poset

Try to transfer the source's cell-poset positivity theorem by identifying
R_(λ/µ) with P_(λ/µ), using their linear-extension/path correspondence.
For the actual2×2 rectangle the two-chain poset has two incomparable
chains of size2, whereas the cell poset is the four-element diamond.
Their exact rows are

    h*_R=1+4t+t²,  Ω_R=t²(t+1)²/4,
    h*_P=1+t,     Ω_P=t(t+1)²(t+2)/12.

At t=2 these give9 and6 weak maps, and their volumes are1/4 and1/12.
They cannot be the same poset or have the same order polynomial. The
source path correspondence counts extensions of R by plane partitions
of the cell shape at a particular bound; it does not identify weak
order maps for every t. A different transform relating their entire
polynomials could still work, but this attempted all-t bijection fails.
This is a worked exact encoding obstruction, not a dispute with the
source theorem or a target counterexample.

<a id="q3568-w05"></a>
## W05 — complete comparisons using coefficientwise monotonicity

Try to prove the arbitrary poset case by adding comparisons until
reaching positive weak-layer or chain cases and transferring ordinary
coefficient signs monotonically. For the actual two-point antichain,
Ω=t²; adding its comparison gives Ω_chain=t(t+1)/2. The difference
Ω_antichain-Ω_chain=t(t-1)/2 has negative linear coefficient, despite
nonnegative counts for every positive integer t. Thus pointwise order
map inclusion does not give coefficientwise monotonicity.

The exact comparison split Ω_P=Ω_(a<b)+Ω_(b<a)-Ω_(a=b) also contains
a subtraction: in this example the two chain linear contributions
1/2+1/2 are cancelled by the contracted point's coefficient1.
Individual positivity therefore cannot alone close that induction.
A new coefficientwise gluing estimate controlling the subtraction
would be needed for every two-chain state; none was proved. This
additive/comparison mechanism differs from W04's shape identity and
W02's layer factorization. The target holds in the example.

All five full-target routes have exact worked obligations and separately
labelled relaxed methods. No full counterexample or impossibility of
other methods is asserted. See POSET-ROUTES-CHECK.json for the controls.
