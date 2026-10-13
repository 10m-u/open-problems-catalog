# Q1860: the full three-colour rainbow density

12 October 2026. Full target: lim Λ_(N,3)=9/22, with ordered rainbow pairs and denominator binom(N,2). Primary [Hegde–Kumar–Pratibha](https://arxiv.org/abs/2609.18474), local `texts/papers/collections-8bce2eab4ff176c2.txt.gz`, read throughout. Source proves9/22≤liminf≤limsup≤8/15. No new full closure is claimed. The five routes below include a complete new local restricted proof, which does not reset the full-target counter.

<a id="a1"></a>
## A1 — Optimize the parity class, then reduce every colouring to it

`PARITY-OPTIMUM.md` proves the exact asymptotic optimum9/22 over **every** colouring with monochromatic evens, without restricting odd colour sets to intervals. The continuum kernel K=1+1{x+y≤1}, compactness/first variation, and reflected-gradient diamond give all nonflat stationary maxima q=1/(12j+11), value3(1+q)/8. The maximum is attained at j=0, the source's odd cutoffs4/11 and10/11. This closes the entire proposed analytic subproblem.

The full proof still needs a monotonic transformation from an arbitrary three-colouring to one with monochromatic evens. The two-coordinate variation argument requires that assumption: arbitrary palettes on the evens introduce independent assignment choices at the output and both summands. A simple colour relabeling cannot make a nonconstant even colouring constant. No count-preserving compression of those choices was established. Thus the restricted theorem is useful but the proposed unrestricted reduction remains a precise unproved structural lemma. **One full-target failed route**, not a full solution.

<a id="a2"></a>
## A2 — Optimize the cyclic rainbow-triangle transfer's leading coefficient

The source injects each ordered rainbow Schur pair into2N+1 translated rainbow triangles of K_(2N+1). The universal three-edge-colour bound is F(m)=(1/15+o(1))m³. Therefore this certificate gives R≤(4/15+o(1))N² and Λ≤8/15. Its coefficient exceeds9/22 by41/330.

Increasing the cyclic graph size makes F(m)/m grow, so cannot fix this loss. Using fewer than2N+1 vertices no longer represents every distance1,…,N by its shortest cyclic distance, and loses the unique-long-gap recovery of the ordered pair. An improvement would need an upper bound specific to distance colourings or a count of the extra short-gap rainbow triangles, rather than the universal F(m). The unrefined transfer has an exact leading-coefficient obstruction. This is a global graph certificate route, distinct from A1's parity variational reduction.

<a id="a3"></a>
## A3 — Blow up a finite optimal colouring into a limit theorem

Given c on[M], replace integer a by a consecutive block of length t with colour c(a). For x=t(a−1)+r,y=t(b−1)+s, their sum has block index a+b−1 if r+s≤t, and a+b otherwise. Each carry branch occupies t²/2+O(t) ordered offset pairs. Consequently, for fixed M,

    lim_(t→∞) Λ_(Mt,3)(blow-up c)
      = [R(c)+R⁻(c)]/M²,

where R⁻ counts a,b with a+b−1≤M and colours c(a),c(b),c(a+b−1) all distinct. This is not2R(c)/M² in general.

For the source parity colouring R⁻=0 exactly: if a,b are odd then the shifted output is odd and only two odd colours occur; if exactly one is even then the shifted output is even, repeating colour3. With M=22 the exact counts are R=102,R⁻=0, so its block blow-up tends to51/242≈0.21074, while the base density is34/77≈0.44156. Letting M run through the source family makes the blow-up density approach9/44, half its original9/22. Thus the proposed universal blow-up stability lemma fails by a macroscopic amount. Carry-sensitive lifting is needed before finite optimality can be promoted to the asymptotic target.

<a id="a4"></a>
## A4 — Close the bound from the three class sizes alone

The source injection into differently coloured pairs yields R≤Σ_(i<j)n_i n_j, hence Λ≤1−Σp_i²+o(1)≤2/3+o(1). This cannot give9/22 without an additional relationship to addition. At the source's actual class proportions(5/22,6/22,11/22), it gives151/242≈0.62397, not9/22.

Moreover class histograms do not encode the necessary correlations. Arrange those same three proportions as consecutive intervals in that order. Only a summand from the first and second intervals can give a rainbow output in the third. Their cross area is25/968, so the normalized rainbow density is25/242≈0.10331, whereas the parity arrangement with the same proportions has9/22. Both are exact all-scale families up toO(1/N). The simple size-only certificate loses the location and residue geometry; its missing step is an addition-sensitive inequality, not a new optimization of Σp_i². This differs from A2's triangle certificate and A1's use of actual parity correlations.

<a id="a5"></a>
## A5 — Induct with a uniform optimal-coefficient bound on new triples

Appending N+1 changes only ordered pairs x+y=N+1, so a natural proposed induction asks for at most(9/22)N+O(1) new rainbow pairs for every prefix colouring. This sufficient increment estimate is false. For even N, colour1,…,N by parity colours1 and2, then give N+1 colour3. Every pair summing to N+1 has one odd and one even summand, so exactly N new ordered rainbow pairs appear; the prefix had none. This is an infinite exact family, exceeding the intended derivative coefficient by13N/22.

The family is not a counterexample to the desired quadratic bound: its old count has enormous slack. An induction would need a quantified tradeoff between prefix slack and possible boundary gain. No such invariant was established. This is a one-step extension proof obstruction, distinct from A3's scaling/carry loss.

## Disposition

Five full-target routes failed. The parity-class theorem is a positive restricted result; no hypothesis reducing arbitrary colourings to that class is supplied. `check_colourings.py` and `COLOUR-CHECK-RESULTS.json` contain exact controls. Request independent mathematical and count review.
