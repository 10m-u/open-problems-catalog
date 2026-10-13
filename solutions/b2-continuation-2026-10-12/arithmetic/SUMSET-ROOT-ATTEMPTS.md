# Q4302: roots of almost-complete sumsets

Read primary source `texts/papers/collections-fce1770edc3bcefd.txt.gz`, Theorem 1.3 and §5. Fix k≥2. The map a↦ka is bijective under the exact group hypothesis. Repetitions in kA are allowed. The target is a matching upper/lower scale, uniformly over the stated groups with constants depending on k, up to logarithmic factors.

<a id="q4302-a1"></a>
## Q4302 A1 — Optimize the known theorem without new estimates

The primary theorem gives f_k≥Ω̃(n^(1/k)) and f_k≤Õ(n^((2k−1)/(4k−3))). The exponent gap is

    (2k−1)/(4k−3)−1/k
      =(2k−3)(k−1)/(k(4k−3))>0.

For k=2 it is1/10. Logarithmic factors cannot absorb a fixed positive power of n. Thus the published bounds do not already imply the exact target, and changing unspecified log constants cannot close it. **Failed bound-interpolation route.**

<a id="q4302-a2"></a>
## Q4302 A2 — Choose a random root A independently of the forbidden complement

For S=G\B and random A of density q, the expected number of ordered representations of each forbidden b is roughly q^k n^(k−1), with lower-order collision terms. Taking this mean≫log n is the straightforward way to cover every allowed element, but then forbidden elements are represented too. Taking it≪1 to avoid B loses coverage. The target requires a correlated independent set in the Cayley sum hypergraph and simultaneous coverage of its complement. Independent sampling and a union bound do not provide both obligations. **Failed unconditioned random-root construction.**

<a id="q4302-a3"></a>
## Q4302 A3 — Solve by taking Fourier k-th roots

An identity 1_A^{*k}=1_S would permit a Fourier-root construction. The required condition is instead support(1_A^{*k})=S, with unknown positive representation multiplicities. Fourier roots of 1_S can be complex and their inverse transform need not be Boolean or nonnegative. Thus the operation solves a different equation and has no integral-root feasibility proof. This is an algebraic obstruction to the proposed inversion method, not a claim that S lacks a set root. **Failed indicator convolution inversion.**

<a id="q4302-a4"></a>
## Q4302 A4 — Remove only the diagonal-forbidden vertices

Every root must exclude k^−1B, because a∈A implies ka∈kA. Taking A=G\k^−1B enforces exactly this necessary diagonal condition, but ignores mixed sums. For G=Z/7Z,k=2,B={0}, it yields A=G\{0}; 1,6∈A then represent0, so 2A is not S. The diagonal map being bijective does not eliminate the other forbidden hyperedges. **Failed diagonal-only root construction.**

<a id="q4302-a5"></a>
## Q4302 A5 — Exhaust cyclic groups and infer the uniform asymptotic upper bound

Enumerating all A and their repeated k-fold sum supports gives exact f_k for a fixed finite group. Small cases include f_2(Z/5Z)=0: a root omitting0 has at most two elements, hence at most three distinct pair sums and cannot equal all four nonzero residues. This does not contradict an asymptotic theorem for sufficiently large n. A finite table gives neither arbitrary rank/noncyclic control nor an exponent bound as n grows. The exact routine is a useful domain control, not the required asymptotic proof. **Failed bounded group-table completion.**

Five routes fail to close the uniform sharp scale. The source lower bound remains valid, the positive exponent gap is explicit, and no finite small-group anomaly is promoted to an asymptotic counterexample.
