# Q4659/Q4660: weighted entropy sum-product and sum-difference

The exact variables are discrete **real-valued** laws of finite Shannon entropy, with independent copies. An integer-supported example is admissible but does not exhaust that domain. Read primary `texts/papers/collections-d817f7a73f6a21bd.txt.gz`, Theorems 1.6–1.7, Lemma 7.5 and §8. The source already proves the universal sum-difference upper constant 2; Q4660 asks whether it is the *least* constant.

## A rigorous lower bound for the universal sum-difference constant

Take X∈{0,1} with P(X=1)=1/10. Let h=H(X), s=H(X+X'), d=H(X−X'). Its sum probabilities are (81,18,1)/100; its difference probabilities are (82,9,9)/100. Thus the least universal constant is at least

    R=(100 log₂10−82 log₂82+144 log₂3)
       /(100 log₂10−180 log₂3−18).

The denominator is positive since 10^100>3^180·2^18. Moreover R>4/3 follows from the exact integer comparison

    3^1152·2^72 > 10^100·82^246.

This is an unconditional explicit lower bound, not tightness of 2 or an originality claim.

### Exact certification of the saved three-point-law route

During review of A5, the saved numerical witness was replaced by the nearby
exact law on {1,3,5} with probabilities (913,79,8)/1000. Its sum weights are
(833569,144254,20849,1264,64)/10^6; its difference weights are
(7304,72759,839874,72759,7304)/10^6. Natural logarithms can be used because
the ratio of entropy increments is independent of logarithm base.

[certify_entropy_law.py](certify_entropy_law.py) bounds each required log
with rational arithmetic: reduce its argument to [1,2], use
log r=2Σ_{j≥0}t^(2j+1)/(2j+1), t=(r−1)/(r+1), and bound the positive tail
after J terms by 2t^(2J+1)/((2J+1)(1−t²)). Here |t|≤1/3 and J=60.
[CERTIFIED-LAW-CHECK.json](CERTIFIED-LAW-CHECK.json) proves the sum increment
is positive and the ratio lies between
1.39778460678578706484097027537185551 and
1.39778460678578706484097027537185552. In particular the least universal
constant exceeds **139/100**. This certifies one existing A5 lower-bound
construction; it is not a sixth full-target solve attempt, a global optimizer
or a claim of an improvement over published bounds. Constant 2 remains
unproved sharp.

<a id="q4659-a1"></a>
## Q4659 A1 — Replace cardinalities in Solymosi's theorem by entropies

The set theorem bounds |A+A|²|AA| from below. For uniform X on A, H(X)=log|A|, but H(X+X')≤log|A+A| and H(XX')≤log|AA|. The direction of these inequalities does not transfer a cardinality lower bound into an entropy lower bound. Representation counts make the output laws nonuniform, even for an interval. A separate weighted incidence/energy theorem is necessary. **Failed cardinality-to-entropy substitution.**

<a id="q4659-a2"></a>
## Q4659 A2 — Combine the source's two known linear estimates

For zero-free X put u=H(X+X')/H(X)−1 and m=H(XX')/H(X). The source gives m≥2−6u−o(1) and m≥5/4−3u/4−o(1), while injectivity after conditioning gives m≥1. At u=1/7 these constraints allow m=8/7, and the requested weighted expression becomes 2+2u+m=24/7<4. Therefore these estimates alone do not force the conjectured coefficient. This feasible scalar pair is not asserted to arise from an actual law. **Failed known-bound interpolation.**

<a id="q4659-a3"></a>
## Q4659 A3 — Create a counterexample by adding an atom at zero

For X equal to0 with probability p and otherwise a zero-free Y, conditioning on the two zero indicators costs at most two bits. Writing Λ(X)=2H(X+X')+H(XX')−4H(X), the exact entropy identities and that bounded conditioning loss give

    Λ(X)=(1−p)²Λ(Y)+O(1),
    H(X)=(1−p)H(Y)+O(1).

The absolute error is uniform in p. Consequently a zero atom contracts a normalized negative deficit rather than creating an asymptotic one from a law with no such deficit. For a long shifted uniform interval the leading coefficient is exactly4 for every fixed p<1, as in source §8. This attempted zero-mass counterfamily is tight but does not violate the target. **Failed zero-atom construction.**

<a id="q4659-a4"></a>
## Q4659 A4 — Amplify a finite-law deficit by radix tensorization

For independent digits Z_i, a sufficiently large radix makes X=Σ B^i Z_i and its sum encode coordinate sums without carries; entropy of X and the sum can add. But XX'=Σ_{i,j}B^(i+j)Z_iZ'_j mixes cross products. It does not encode the coordinate products independently. More fundamentally a field has no nontrivial orthogonal idempotents, so no ring embedding of R^t with its coordinate operations into R exists for t>1. An additive digit embedding supplies no multiplicative tensor identity. No entropy amplification preserving both operations is proved. **Failed simultaneous tensor counterexample.**

<a id="q4659-a5"></a>
## Q4659 A5 — Use a multiplicative progression to suppress product entropy

Let X be uniform on {2^i:0≤i<n}. Product entropy is that of i+j, namely log₂n+O(1). Sums identify an unordered pair of exponents uniquely, including equal pairs, so H(X+X')=2log₂n−1+1/n. The weighted expression is 5log₂n+O(1), above the requested4log₂n. This unbounded-entropy structured family cannot supply a counterexample even though multiplication has small entropy growth. **Failed multiplicative-progression counterfamily.**

<a id="q4660-a1"></a>
## Q4660 A1 — Prove sharpness using a Bernoulli law

The exact p=1/10 calculation gives a lower bound strictly greater than4/3. At p=1/2, the two output entropies coincide and the ratio is1. As p→0 or1, the leading rare-event entropy terms make the ratio tend to1 as well. This family supplies a nontrivial lower bound but no sequence approaching2, and an optimization within it is not an upper bound for all real laws. **Failed Bernoulli sharpness construction.**

<a id="q4660-a2"></a>
## Q4660 A2 — Use long uniform intervals

For X uniform on {1,…,n}, X+X' and X−X' have the same triangular probability multiset, so the ratio of entropy increments is exactly1 for every n≥2. These arbitrarily large-entropy inputs cannot attain2. **Failed interval extremizer.**

<a id="q4660-a3"></a>
## Q4660 A3 — Transfer the sharp combinatorial sum-difference example

A sharp set cardinality ratio controls logarithms of support sizes. Entropy subtracts the average logarithm of representation multiplicity, and that loss can differ for sums and differences. A cardinality-tight example therefore needs probability-mass control before it becomes entropy-tight. The source explicitly distinguishes these tightness questions. No equal-loss or near-uniform output theorem is obtained. **Failed support-tightness transfer.**

<a id="q4660-a4"></a>
## Q4660 A4 — Tensor a fixed entropy ratio to make it approach2

For a finite integer law with bounded support, use a large base B to encode t independent copies without carries in sums and differences. The three relevant entropies multiply by t, so both entropy increments multiply by t and their ratio is unchanged. The operation can increase entropy but cannot improve a fixed nonextremal ratio. This is a valid tensorization calculation with a precise sharpness obstruction; it differs from Q4659's missing product identity. **Failed ratio amplification.**

<a id="q4660-a5"></a>
## Q4660 A5 — Optimize over small supports as a universal certificate

Directly convolving probability laws on finite integer supports tests the ratio without imposing uniform weights. The saved checker explores a declared set of such laws and keeps its best witness. The exact rational certification above gives a lower-bound witness exceeding139/100. A finite search or one rigorously certified law neither reaches an asymptotic2 family nor proves a smaller universal constant for arbitrary countable real support. A numerical optimum has no global inequality certificate. **Failed bounded weighted-law extremizer search; certified scoped lower bound retained.**

Five routes per full target fail. The Bernoulli lower bound, uniform-interval identity and exact tensor scope are retained. Finite-law tests do not disprove the large-entropy quantified statement, and upper constant2 is not mislabeled as its optimality proof.
