# Q1861: determine both four-colour asymptotic extremes

12 October 2026. Full target: determine liminf and limsup of Λ_(N,4), including whether they coincide. Primary [Hegde–Kumar–Pratibha](https://arxiv.org/abs/2609.18474), local `texts/papers/collections-8bce2eab4ff176c2.txt.gz`, read throughout. Preserve the already accepted original B2 return's stronger liminf bound **50368/90905≈0.554073**, from its nine-interval colouring; the older primary10/21 bound is weaker. The original archive gap is separate. None of the following routes closes the full target or improves that preserved bound.

<a id="a1"></a>
## A1 — Get convergence from consecutive-block blow-up of every finite optimizer

A limit proof would follow from an arbitrarily fine count-preserving lift of good finite colourings. The natural consecutive-block lift instead obeys the exact carry formula in Q1860-A3: its limiting density is[R(c)+R⁻(c)]/M², not2R(c)/M². The permitted four-colour class contains the three-colour parity source family. For it R⁻=0 and the density drops asymptotically from9/22 to9/44 under this operation. At M=22 the exact base102 pairs give lifted limit51/242.

This disproves the universal count-preservation lemma that would promote arbitrary finite four-colour constructions to a common asymptotic extreme. It does not show that every good four-colour template fails to lift: the preserved nine-interval family does have a valid all-scale proof. What is missing for a convergence argument is a lift theorem for all near-optimizers, rather than one explicit lower-bound family. This reuses Q1860's carry computation at a distinct exact catalog target; no extra failure is counted for rerunning it.

<a id="a2"></a>
## A2 — Use prefix monotonicity and small normalized increments

Let M(N) be the maximum rainbow count. Restriction/extension give0≤M(N+1)−M(N)≤N: the only new possible pairs sum to N+1. Therefore |Λ_(N+1,4)−Λ_(N,4)|=O(1/N). These statements alone do not prove convergence. For example define the abstract count sequence

    B(N)=floor[binom(N,2)(3/5+(1/100)sin(log N))].

For all sufficiently large N it is increasing with increment≤N (differentiate the unrounded expression; its derivative lies strictly between0 andN, and rounding adds at most1). Its normalized values have liminf59/100 and limsup61/100. Those values lie within the preserved lower bound and universal upper bound3/4, so even the available bounds plus the exact increment constraints do not close this analytic argument. B is not asserted to be realized by colourings. It refutes only the implication from these scalar inequalities to convergence; one needs an additional uniform comparison between separated scales.

<a id="a3"></a>
## A3 — Apply a Fekete/concatenation argument to additive blocks

Try to concatenate two good colourings and regard each as an independent internal contribution, obtaining a superadditive extremal sequence. Translation fails the required preservation: a Schur relation a+b=c in the second template, shifted by t, becomes(a+t)+(b+t)=c+2t, whereas the copied output is c+t. If two equal blocks have length t, no triple with both summands in the upper block can lie in their union, since the sum exceeds2t. The first template may survive, but the second template's internal quadratic contribution does not.

Already the rainbow template1,2,3 on[3] loses its pair1+2=3 when copied to4,5,6. This algebraic obstruction differs from A1's two carry branches in a dilation: it is a translated-copy obstruction to the superadditive decomposition itself. It does not prove that some other extremal superadditivity theorem is false; the proposed concatenation is not its proof. A translation-compatible counting functional or a different multiplicative assembly remains absent.

<a id="a4"></a>
## A4 — Replace the nine-interval family by a two-prefix/two-tail palette template

We tested a different quantitative construction: colour[0,a] with1, (a,b] with2, and independently colour (b,1] uniformly with3 or4. This makes all tail interactions elementary. Let A be the area of x∈[0,a],y∈[a,b] with b≤x+y≤1, and B the area of x∈[0,b],y∈[b,1] with x+y≤1. The normalized expected rainbow density is4A+2B: the first cross-prefix case has probability1, and a prefix-tail case has probability1/2 with two summand orders. All other cases have repeated colours.

Exact rectangle integration and piecewise quadratic optimization give the family maximum **3/7**, at a=2/7,b=3/7. Details and exact cell controls are in `TWO-PREFIX.md` and the checker. This is below even10/21 and far below50368/90905. Thus this actual alternative construction cannot be the four-colour optimum; its simplified palette interactions discard useful correlations. Grid restarts are not additional attempts. The full target survives because more general colourings are outside the template.

<a id="a5"></a>
## A5 — Get the four-colour optimum by uniformly splitting a parity-optimal colour

Start with the full parity optimum proved in `PARITY-OPTIMUM.md`, then split one old colour into two colours independently with equal probability. A formerly rainbow triple remains rainbow. A triple with exactly two old colours becomes rainbow with probability1/2 precisely when its repeated colour is the one split (ignore x=y, onlyO(N) pairs). Three-equal triples cannot become rainbow with just two new colours. Therefore E R₄=R₃+(1/2)T_i, with T_i the exact count of two-colour triples whose repeated colour is i.

For the parity optimum S=[0,4/11]∪[10/11,1], the split of odd colour1 gives

    T₁/N²=[|S|²+∫_(S×S)1{x+y≤1}]/4
          =[25/121+17/121]/4=21/242.

Its density is9/22+21/242=60/121≈0.495868. Splitting odd colour2 gives T₂/N²=[36/121+9/242]/4=81/968 and density477/968≈0.492769. Splitting the common even colour adds no rainbow triples, since all-even triples use only the two split colours and mixed triples have only one even position. All three possibilities are therefore below the preserved50368/90905. This concrete refinement route is quantitatively exhausted for its stated starting construction. It is distinct from A4's new prefix template: it explicitly retains the source's residue/interval geometry but fails to create enough additional three-colour patterns.

## Disposition

Five worked full-target routes failed, with convergence and exact values still undetermined. A1–A3 examine different missing scale comparisons (carry lift, scalar increments, translation assembly); their relationship is disclosed. A4–A5 are two explicit quantitatively checked constructions, not repeated searches of the original nine-interval witness. Request independent count/scope review.
