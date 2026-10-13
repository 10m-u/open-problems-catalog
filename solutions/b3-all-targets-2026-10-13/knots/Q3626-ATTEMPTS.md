# Q3626: M-convex support of the alternating-link refinement

Exact scope and primary conventions are in [SETUP](SETUP.md). A failed sufficient route is not a counterexample to the conjecture. Current full-target failure count: 5, accepted by root review. No further solve attempt is made unless a count is rejected.

<a id="q3626-a1"></a>
## A1 — lift ordinary matroid exchange through the tree statistics

Try to apply the graphic-matroid basis exchange theorem, then identify its exchanged edge variables with the four exponent coordinates. A color grouping with fixed edge colors would have the right formal shape. However, the source's positive-edge weight depends on which end of that edge is separated from the root by the rest of the tree. This dependency cannot be ignored.

There is an exact obstruction within actual special alternating links. Let G be the directed plane cycle with n edges e_i:v_i->v_(i+1 mod n), root v_0 and adjacent outer basepoint, with every crossing positive. Its vertices alternate incoming/outgoing, so this is a valid all-positive Tait diagram by source Lemma 5.3(i). Set r=n-1. Its spanning trees are T_k=E\{e_k}, 0<=k<=r. Exactly k edges of T_k point away from the root; hence

    P_G = sum_(k=0)^r x^(-k) y^(-(r-k)).                         (1)

For r>=2, apply the desired M-exchange to the exponents of T_r and T_0. It requires T_(r-1) and T_1, which are indeed present. But ordinary exchange only reassigns e_0 and e_r while leaving their common edges fixed: its only trees are T_0 and T_r. The required trees omit different edges in the **intersection** of T_0 and T_r. Thus the desired exponent exchange cannot be obtained by the ordinary two-basis exchange on the symmetric difference. For n=3 the midpoint requires T_1 twice; for n>=4 the two required trees are distinct. This is an all-size obstruction to the proposed lift, despite the target being true for these cycles.

The dimer reformulation by itself does not repair the lift. A relaxed 2-by-2 colored matching matrix can have permanent x^-1 z+y^-1 w. For alpha=(-1,0,1,0), beta=(0,-1,0,1), i=3, the only possible j are 1 and 4; neither supplies both exchanged support points. Its support is not M-convex. This matrix is **not asserted to be a reduced Tait overlay**, and is not a link counterexample. The actual source example P_41=1+(x^-1+y^-1)(z+w) fills the relevant exchanges and passes. The missing full lemma must use the special overlay/root constraints and perform exchanges beyond ordinary primal symmetric-difference reassignment.

Substantive partial: (1) proves Q3626 for every directed-cycle all-positive Tait diagram, without a finite-size restriction. Its support is the complete integer interval on the root direction (-1,1,0,0), and any two points admit the unit exchange toward one another. [Checker](check_boninger.py) verifies the formulas and both the relaxed failure and actual P_41 control; finite checks do not establish the all-size assertion.

<a id="q3626-a2"></a>
## A2 — normalized Lorentzian certificate for the full refinement

The special-alternating results suggest proving a stronger denormalized-Lorentzian statement, whose support would be M-convex. Source Boninger explicitly reports that this stronger bridge fails, including at the actual knot 8_10. Here is an exact worked certificate of that failure, rather than relying solely on the report.

Use the source's explicit

    P_810=(x^-2+x^-1 y^-1+y^-2) sum_(j=0)^4 z^j w^(4-j)
          +(x^-1+y^-1)(z+w)(z²+zw+w²).

Put F=x²y² P_810, a nonnegative homogeneous degree-six polynomial, and normalize N(F) by dividing every monomial coefficient by its exponent factorial. Direct differentiation gives

    d_y² d_w² N(F)=2xz+xw+z²/2+zw+w²/2.

Its Hessian on coordinates (x,z,w) is

    H = [[0,2,1],[2,1,1],[1,1,1]],  det H=-1, trace H=2.

H is real symmetric and nonsingular. A negative determinant requires an odd number of negative eigenvalues; the positive trace excludes three negative eigenvalues. Thus it has **two positive eigenvalues**. By the quadratic-derivative criterion in [Brändén–Huh](https://arxiv.org/pdf/1902.03719), N(F) is not Lorentzian. This disproves the proposed stronger certificate, not Q3626. Source footnote 1 and the monomial-normalization equivalence cited there explain why taking a larger clearing monomial cannot rescue this certificate.

The [checker](check_boninger.py) reconstructs all 23 monomials from the displayed products, computes the normalized derivative using exact factorial ratios, verifies the Hessian determinant, and separately checks actual P_810's M-exchanges and coefficient inequalities. They both pass. A support-specific proof that avoids Hessian signature remains possible. This route is distinct from A1's discrete tree-pair exchange mechanism, and its obstruction is an actual target polynomial.

<a id="q3626-a3"></a>
## A3 — promote marginal trapezoids and Alexander data to full support exchange

Try to combine the proved marginal symmetries/trapezoids (source Theorems 1.2 and 1.5), homogeneity and the Alexander specialization to force full support. The following worked formal polynomial shows that even strengthening those marginal hypotheses to ordinary log concavity is insufficient. Write X=x^-1, Y=y^-1, Z=z, W=w and put

    F=1+4(X²+Y²)(Z²+W²)+5XY(Z²+W²)
         +5ZW(X²+Y²)+4XYZW.                                  (2)

All coefficients are positive on its support, and every monomial has signed degree zero. It is invariant under X<->Y, Z<->W and simultaneous group interchange (the source mirror substitution). Its two source marginal specializations are both

    F(t^-1,t,1,1)=F(1,1,t^-1,t)=13t^-2+15+13t².

The even subsequences are symmetric and strictly trapezoidal/log-concave; the odd subsequences vanish. Its unsigned Alexander specialization is

    F(t^-1,t,t^-1,t)=4t^-4+10t^-2+13+10t²+4t⁴,

which is symmetric, positive, hole-free in the degree-two lattice and log-concave. The associated signed symmetrized row has value 4-10+13-10+4=1 at 1, as a knot Alexander polynomial must. Directly F(1,-1,1,-1)=1. Thus even adding that knot normalization does not repair the inference.

Yet its support has 0 and (-2,0,2,0), but not (-1,0,1,0). Their required unit exchange is missing, so it is not M-convex. No claim is made that (2) is P_K for an alternating link. It is an exact counterexample to the proposed **marginal-information implication**, not to the target. A full proof must control the joint tree statistics beyond those marginal theorems and the one-dimensional Alexander specialization. This differs from A2's actual Hessian obstruction and A1's specific exchange lift. The checker records all four specializations and the explicit missing exchange.

<a id="q3626-a4"></a>
## A4 — deletion/contraction induction with one scalar invariant per minor

Try to split trees according to an edge and induct on smaller Tait invariants. The usual graphic tree polynomial has a two-minor recurrence, and the source has useful minor closure: positive-edge contraction and negative-edge deletion preserve canonical Tait diagrams. However, it does not grant both branches for a general edge.

Work the recurrence explicitly for the positive directed n-cycle. Splitting on e_0 gives, with X=x^-1,Y=y^-1,

    P_Cn = X P_C(n-1) + Y^(n-1),

because the containing trees have activity counts 1,...,n-1 and the unique omitting tree has count 0. The contraction is again the valid positive cycle. The deletion branch is a directed path, with endpoints of unbalanced incoming/outgoing degree. It is **not** a canonical all-positive Tait diagram by Lemma 5.3; its conditional monomial cannot be replaced by the inductively available invariant of the same signed diagram. This obstruction already occurs at n=3 and persists at arbitrary n. The special cycle recurrence succeeds only because its omitted branch is a singleton and exactly adjacent to the contracted interval.

Even if both conditional supports were proved M-convex, their homogeneous positive union would not be sufficient: X² and Y² each have singleton M-convex support, while X²+Y² lacks the required XY exchange. Thus the attempted induction needs a new **cross-branch exchange compatibility theorem**, plus conditional root-direction states for minors outside the Tait class. Neither is supplied by the scalar minor invariant. This is a concrete worked induction failure, not a claim that deletion/contraction with richer states cannot succeed. It is different from A1's exchange between original full trees and A3's global marginal inference.

<a id="q3626-a5"></a>
## A5 — generate every alternating invariant from special factors by connected sum

The source's special-alternating Lorentzian result and multiplicativity suggest reducing all alternating links to products of known positive-special factors and their mirrors. The algebraic coverage fails even before needing a topological prime-factor classification. For an all-positive diagram, P involves only X=x^-1,Y=y^-1 and is homogeneous in X,Y of one fixed degree. Its mirror involves only Z=z,W=w of one fixed degree. Any product of such factors therefore has a **fixed** total X,Y degree R and a **fixed** total Z,W degree S in every monomial, independent of how many factors are used.

The actual P_41=1+(X+Y)(Z+W) has monomials of group degrees (0,0) and (1,1). No product of those known special/mirror factors, even with a fixed monomial shift, can equal it. Thus the proposed full generation reduction does not cover an actual alternating knot. One cannot use a connected-sum closure theorem to bypass all genuinely mixed-sign prime factors. This is different from A4's additive minor recurrence or A1's matroid exchange.

Retained positive construction: [CYCLE-PRODUCTS](CYCLE-PRODUCTS.md) proves both targets for arbitrary connected sums of directed-cycle positive diagrams and their mirrors, including empty products and all boundary rows. It is a complete named-family theorem, not a full Q3626 answer or novelty claim. The failed full generation route and its exact P_41 coverage obstruction are counted once; the partial family does not reset the counter.

All five routes have worked obligations and explicit scope: original tree exchange, a stronger analytic certificate, marginal-information promotion, minor induction, and multiplicative generation. A1/A4 use the same cycle family for different mechanisms; A2 is source-known stronger failure with an independently exact certificate. Root may reject/merge a count if it judges one insufficiently substantive. No full conjecture counterexample is asserted.
