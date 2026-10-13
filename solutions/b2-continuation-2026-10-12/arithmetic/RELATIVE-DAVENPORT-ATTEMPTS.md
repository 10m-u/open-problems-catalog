# Q3116/Q3117/Q3466: relative zero sums and factorization

Read primary sources `texts/papers/collections-639462956a10507c.txt.gz`, §2, Lemma 3.12, §4, Theorem 5.17, and `texts/papers/collections-c5c66320b738dd07.txt.gz`, §6, especially Example 6.3 and Conjecture 6.4. The cosets in Q3116 denote subsets of G. d_{0}(G)=0 is the special singleton convention, not the classical Davenport constant.

## Exact finite algorithm for d_S(G)

For a zero-sum-free sequence, keep its total t and the set R of all subset sums including the empty sum0. Adding g is permitted exactly when −g∉R, and replaces R by R∪(R+g) and t by t+g. Equal states (R,t) can retain the largest attained length. Every permitted step increases |R|: otherwise R+g=R would imply −g∈R by finite translation invariance. Thus the graph is acyclic, bounded by |G|−1 steps, and exact dynamic programming computes every d_{g}(G), then d_S=max_{g∈S}d_g. This is an executable finite tool, not a proof of the monotonicity over all groups.

<a id="q3116-a1"></a>
## Q3116 A1 — Extend the cyclic formula componentwise

For G=Z/n and H=⟨m⟩, source Theorem 2.13 gives d_{g+H}=n−gcd(g,m), and β∈⟨α⟩ implies the required gcd divisibility. An arbitrary subgroup of a noncyclic product need not decompose into its coordinate subgroups: the diagonal subgroup in C₂×C₂ is the smallest example. Independent coordinate optimizations do not describe its cosets or the zero-sum-free condition of the combined sequence. No product formula extending the cyclic proof is established. **Failed cyclic-to-product formula.**

<a id="q3116-a2"></a>
## Q3116 A2 — Use multiplication by the quotient multiplier as an automorphism

If the multiplier is coprime to exp(G), multiplication is an automorphism preserving H and gives equality of the two d-values. The premise allows nonunits. In C₄ the sequence (1,1) is zero-sum-free, while multiplying it by2 yields the zero-sum sequence (2,2). Thus nonunit multiplication need not preserve admissible sequences and cannot be used as the same bijection. **Failed nonunit automorphism extension.**

<a id="q3116-a3"></a>
## Q3116 A3 — Append a correction from total β to total α

Appending a sequence of total α−β corrects the coset but may create a forbidden zero subsum. In C₃ with H=0, α=1,β=2, the maximal β-sequence (1,1) cannot simply append2: the result contains1+2=0. A different maximal α-sequence (2,2) exists, so this does not refute the conjecture; it refutes the length-preserving extension argument. A replacement lemma preserving length and freeness remains absent. **Failed correction-concatenation proof.**

<a id="q3116-a4"></a>
## Q3116 A4 — Bound each coset using only the quotient

A zero-sum-free sequence in G can acquire zero subsums in G/H. In C₄,H={0,2}, the sequence (2) is admissible in G but projects to the zero singleton. Therefore projection is not an admissibility-preserving upper-bound map. The source's safe lifting inequality goes in the other direction and does not compare the two original cosets. Kernel contributions must be retained. **Failed quotient-only upper bound.**

<a id="q3116-a5"></a>
## Q3116 A5 — Exhaust finite groups using the subset-sum state algorithm

The algorithm above checks all sequence lengths without an arbitrary cutoff in each chosen group. Its cyclic controls agree with the source formula; selected small noncyclic groups give no counterexample. Group order and rank remain unbounded, so this exact finite test does not certify the universal conjecture. There is no finite list of group types or size descent reducing all instances to these controls. **Failed bounded group classification.**

<a id="q3117-a1"></a>
## Q3117 A1 — Deduce elasticity monotonicity from ring inclusion

Inclusion does not preserve atoms. In R=Z[2i], the element2 is irreducible because every nonunit has norm at least4; in T=Z[i] it is reducible as −i(1+i)². Conversely a T-atom need not lie in R. Hence equalities of atom products in one ring cannot simply be reused as equal-length atomic factorizations in the other. A supremum over factorizations is not monotone by set inclusion alone. **Failed atom-inclusion proof.**

<a id="q3117-a2"></a>
## Q3117 A2 — Use only class-group Davenport monotonicity

Extension gives a surjection Cl(R)→Cl(O_K), so D cannot increase upon passage to the maximal-order class group. The source's conductor-coprime sharpness result supplies ρ(R)≥max(1,D(Cl(R))/2)≥ρ(O_K), and the same holds for T. This does settle the comparison with the maximal order. But ρ(T) may include larger contributions from elements at the conductor, which are not bounded by D(Cl(T))/2. Comparing only the coprime parts cannot establish ρ(R)≥ρ(T). **Failed full-chain class-group proof; known lower leg retained.**

<a id="q3117-a3"></a>
## Q3117 A3 — Clear conductor denominators in a T-factorization

Multiplying a T-element by an integer conductor makes it belong to R, but the chosen scalar introduces new atomic factorizations and the T-factors may split or cease to be elements of R. There is no uniform preservation of the ratio of longest to shortest lengths. The atom2 example already shows why scalar multiplication does not turn the factor lists into matched R-atoms. **Failed conductor-clearing transfer.**

<a id="q3117-a4"></a>
## Q3117 A4 — Apply the quadratic primary-conductor theorem everywhere

Theorem 5.17 proves the desired nested-order comparison in quadratic fields for conductors powers of the same inert or ramified rational prime. Split primes, products of conductor primes and higher-degree fields are outside that statement. The proof compares explicit valuation and relative-Davenport terms available in that special classification; no analogous all-order formula is proved. **Failed unrestricted special-case extension.**

<a id="q3117-a5"></a>
## Q3117 A5 — Localize at each conductor prime and take separate maxima

Factorization lengths couple the prime ideal valuations through global principal-ideal and class constraints. A list of local longest/shortest ratios need not describe a global factorization, nor does their pointwise comparison produce a transfer homomorphism between the two orders. The source's relative-Davenport terms precisely record some of those global constraints. No equality expressing general elasticity as a maximum of uncoupled local elasticities is established. **Failed independent-local-factors proof.**

<a id="q3466-a1"></a>
## Q3466 A1 — Extrapolate the first irregular cyclotomic example

At K=Q(ζ₃₇), source Example 6.3 gives Cl(K)=C₃₇, weighted minimal-zero-sum maximum3 and elasticity ratio37/3. One large value proves neither unboundedness nor divergence through every sufficiently late irregular prime. A numerical/class-group example does not supply a uniform limit estimate. **Failed one-field extrapolation.**

<a id="q3466-a2"></a>
## Q3466 A2 — Use the growing field degree to force strong Galois action

|Gal(Q(ζ_p)/Q)|=p−1 grows, but an action's image on a group can be much smaller than the acting group. In the abstract example C_M with trivial action of any large cyclic group, the weighted and unweighted zero-sum monoids coincide, so the ratio is1. This is not a cyclotomic-field counterexample; it refutes the degree-only mechanism. A quantitative theorem about the actual class-group representation is missing. **Failed degree-to-action argument.**

<a id="q3466-a3"></a>
## Q3466 A3 — Use irregularity to lower-bound only the numerator

Irregularity gives p|h_K, hence an element of orderp in Cl(K) and D(Cl(K))≥p. Thus ρ(O_K)≥p/2. To obtain divergence one still needs ρ(N_K)=o(p), or a correspondingly stronger numerator bound. The trivial denominator bound by the unweighted constant does not provide such a separation. **Failed numerator-only limit proof.**

<a id="q3466-a4"></a>
## Q3466 A4 — Treat every irregular class group as the transitive C_p example

The p=37 proof uses a cyclic group and an action transitive on its nonzero elements. General class groups may have several primary components and eigenspaces, with no such transitivity. The action cannot be declared full Aut(C_p) on the entire group merely because p divides its order. Additional components can affect weighted minimal sequences and the norm elasticity. No uniform classification reduces all irregular fields to that example. **Failed cyclic-transitive model.**

<a id="q3466-a5"></a>
## Q3466 A5 — Replace the relevant weighted monoid constant by weighted zero-sum existence

The source distinguishes D_Γ(G), forcing one weighted zero subsequence, from D(B_Γ(G)), bounding sequences that cannot be partitioned into two weighted zero sequences. Even at p=37 these are2 and3 respectively. A short zero subsequence may leave a remainder with no weighted zero relation. The norm elasticity uses the second invariant; a bound on the first does not automatically bound it. No uniform remainder-partition lemma is proved. **Failed weighted-constant substitution.**

Five routes per exact target fail. The finite algorithm, cyclic and primary-conductor source cases, the already-established maximal-order lower leg and numerator estimate retain their scopes. No abstract group/action counterexample is mislabeled as a number-field counterexample.
