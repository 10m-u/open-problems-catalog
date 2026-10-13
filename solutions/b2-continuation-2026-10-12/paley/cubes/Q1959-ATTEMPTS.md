# Q1959: projective 3-cubes in an interval

12 October 2026. Exact full target: the maximum size of a projective-3-cube-free subset of [N] is at most (2/3+o(1))N. All generators are positive integers, may repeat, and every nonempty subset sum must lie in A. The following five proposed proofs fail at the stated steps; none refutes the conjecture.

Primary source: [Meng, Sections 1 and 3](https://doi.org/10.37236/14052), local `texts/papers/collections-077f96b30fab35e0.txt.gz`. Its interval conjecture and cyclic theorem are different statements. Its doubling-chain bound is retained, not counted as a new solution.

<a id="a1"></a>
## A1 — Transfer the cyclic 2/3 theorem by an almost lossless embedding

Embed [N] into Z/MZ and apply the cyclic theorem to A. For M=2N this embedding preserves 3-cube freeness: if a modular cube were contained in A, all its generators are in [N]; each pair sum is ≤2N, and a wrapped pair would be0, outside A. Thus all three ordinary pair sums are ≤N. Adding them gives total generator sum ≤3N/2<2N, so no subset sum wraps and the same cube is an integer cube. The conclusion is only |A|≤4N/3, which is vacuous.

Taking M=N+o(N) instead does not preserve freeness. Let A=(N/3,N] and N=6q. It is integer-cube-free since any three generators in A have sum>N. In Z/NZ the repeated generator 5q has subset sums {5q,4q,3q}, all in A. More generally x≈5M/6 produces the same modular wrap pattern when M/N is sufficiently close to1. The required asymptotically lossless transfer therefore fails its central preservation lemma. This is a modular-carry obstruction, not a failure of the cyclic theorem.

<a id="a2"></a>
## A2 — Use the smallest doubled pair to make the translation error vanish

If A avoids every {x,2x}, Meng's doubling-chain calculation gives |A|≤2N/3+O(log N). Otherwise fix x with x,2x∈A. Cube freeness for (x,x,y) implies that A contains no three-term progression y,y+x,y+2x. Partition [N] into the x residue chains; a chain of length r contains at most ceil(2r/3) selected points. Hence |A|≤2N/3+2x/3. A pair with x=o(N) would settle this branch.

The proposed remaining lemma, that every relevant dense cube-free set has such a small pair, is false. For A=(N/3,N], the smallest possible doubled pair has x=floor(N/3)+1, a macroscopic step, while |A|=2N/3+O(1). The translation estimate leaves a linear error precisely on an actual extremal family. One needs an additional argument for sets whose first doubled pair is large; choosing the minimum step alone does not complete the proof. This differs from A1: it stays in the integers and loses at the chain endpoints rather than a modular embedding.

<a id="a3"></a>
## A3 — Prove the density bound with the full basic hyperedge linear relaxation

Consider variables 0≤a_t≤1 and, for every projective 3-cube C⊆[N], the valid inequality Σ_{t∈C}a_t≤|C|−1. Maximizing Σa_t is an exact proposed fractional-certificate route. It cannot prove the conjectured coefficient: the following assignment is feasible for **all N**:

    a_t=0       if N/4<t≤N/3;
    a_t=1/2     if t≤N/2 and t is outside that interval;
    a_t=1       if t>N/2.

Its total is N−floor(N/2)/2−(floor(N/3)−floor(N/4))/2 =17N/24+O(1), above 2N/3 by N/24+O(1).

Proof of feasibility: let T be the sum of the three positive generators and l=|C|. Then T≤N, and the proper distinct subset sums C\{T} are closed under the involution s↦T−s. Its only possible fixed point is T/2≤N/2. Consequently at most floor((l−1)/2)+1=floor((l+1)/2) points of C exceed N/2. Before lowering the weights in the hole, Σ_C a≤l/2+floor((l+1)/2)/2≤l−1 whenever l≥4.

For l=3 all generators equal some x. Indeed order the generators a≤b≤c. The strict chain a<a+b<a+b+c must be all of C. Because a≤b<a+b, this forces b=a. As c<a+b+c, it then forces c=a or2a; the latter introduces the fourth value a+c=3a, between2a and the total4a. Thus c=a. Thus C={x,2x,3x}. If x≤N/4, at most one of these is above N/2, so its weight sum is≤2. If x>N/4, then x≤N/3 and its zero weight combines with two weights≤1. This covers every cube, including degeneracies.

This is an exact all-size obstruction to the stated LP, not an integer cube-free set and not a claim against strengthened relaxations. Searches at different N are checker controls of this single route, not extra attempts.

<a id="a4"></a>
## A4 — Factor the seven linear-form correlations from density alone

Try to count cubes by sampling three independent generators from [1,N/3], then replacing the expectation of the product of the seven subset-sum indicators by the product of their means. The cyclic/interval residue data show why this implication is unavailable from density alone. Take N=12q and A={t∈[N]:t mod4≠0}, of density3/4>2/3. Each sampled generator is exactly uniform modulo4, and all ordinary subset sums lie in [N]. The product is1 exactly for residue triples (1,1,1) and (3,3,3); its expectation is2/4³=1/32, not (3/4)^7. This difference persists as q→∞. The Fourier coefficient at frequency1/4 also remains of order N, so an o(N) Fourier-uniformity premise cannot be inferred from the density threshold.

At the exact threshold, nonzero residues modulo3 have density2/3 and cube count0: an opposite-sign pair sums to0, or three identical residues do. Thus termwise positivity or an independence model even misses the basic extremal obstruction. A valid correlation-count route needs a structural alternative for the periodic branch, followed by a cube theorem in that branch; neither follows from the factored density expression. This tests higher correlation information, distinct from the one-hyperedge LP in A3.

<a id="a5"></a>
## A5 — Compress every cube-free set upward to the terminal interval

The terminal interval has a direct cube-free proof, suggesting an order compression toward it. But even one permitted upward shift can create a cube. For q≥1 the set {2q,4q,6q−1} is 3-cube-free: every triple of its positive generators has total at least6q, exceeding its maximum. Replacing the last point by6q creates the repeated-generator cube {2q,4q,6q}. Thus the elementary operation needed by this proposed compression does not preserve the forbidden configuration. A different global compression with a proof of preservation would be needed; a monotone shift toward the high interval does not supply it. This is an order-operation obstruction, independent of the modular carry and correlation routes.

## Disposition

Five distinct full-target proof routes failed; request independent scope/count review. The all-size fractional witness is a useful exact obstruction at its stated relaxation scope. The small-step estimate is conditional only. `check_cubes.py` and `CUBE-CHECK-RESULTS.json` supply exact bounded controls; no empirical extrapolation is used in the all-size proof.
