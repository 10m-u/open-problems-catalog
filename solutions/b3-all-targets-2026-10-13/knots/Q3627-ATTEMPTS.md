# Q3627: coefficient log concavity of the alternating-link refinement

Exact scope and primary conventions are in [SETUP](SETUP.md). A failed sufficient route is not a counterexample to the conjecture. Current full-target failure count: 5, accepted by root review. No further solve attempt is made unless a count is rejected.

<a id="q3627-a1"></a>
## A1 — symmetric-difference injection on pairs of spanning trees

For c_alpha² >= c_(alpha+d)c_(alpha-d), d=e_i-e_j, try to inject pairs of trees of neighbor statistics into pairs of midpoint statistics using the standard graphic-matroid symmetric-difference exchange. The root-dependent edge statistics make this mechanism fail on an actual valid family.

Use the directed all-positive n-cycle from [Q3626 A1](Q3626-ATTEMPTS.md#q3626-a1), with T_k=E\{e_k} and weight x^(-k)y^(-(r-k)), r=n-1. For 1<=k<=r-1, the neighbor fibers contain the single pair (T_(k-1),T_(k+1)); the midpoint fiber contains (T_k,T_k). The edge e_k is present in **both** input trees. Every reassignment restricted to their symmetric difference keeps e_k in both outputs, so cannot produce the required midpoint pair. Even n=3 supplies this obstruction, with neighbor trees T_0,T_2 and midpoint T_1. Changing a single underlying tree edge can also change the root direction of an arbitrarily long common path; the statistic is not a fixed color count of its edge set.

The target holds with equality in this family: every supported coefficient is 1, and all root-direction midpoints between neighbors are present. Cross-coordinate products involving z or w are zero, since their exponents are fixed at zero. Thus the calculation simultaneously supplies an all-size positive subcase and refutes the proposed *specific injection mechanism*. It does not preclude a nonlocal tree-pair injection, a flow on the overlay, or a geometric proof.

The [checker](check_boninger.py) verifies all these finite controls. The cycle calculation above, rather than its finite replay, proves the unrestricted family. This is one failed full-target coefficient-injection route, separately from Q3626's support-exchange obligation; neither counter is reset by the positive subcase.

<a id="q3627-a2"></a>
## A2 — derive all coefficient inequalities from a denormalized-Lorentzian lift

Try the stronger normalized-Hessian certificate, as in the special-alternating proof strategy. [Q3626 A2](Q3626-ATTEMPTS.md#q3626-a2) supplies the exact actual P_810 obstruction: the normalized degree-six lift has quadratic derivative 2xz+xw+(z+w)²/2, whose (x,z,w) Hessian has determinant -1 and trace 2, hence two positive eigenvalues. It cannot be Lorentzian. The coefficient implication itself is correct (Brändén–Huh Proposition 4.4); it is the stronger all-input hypothesis that fails.

This is a full-target sufficient proof attempt with an exact signature obstruction, distinct from A1's combinatorial injection. The source already identifies the stronger failure; our calculation makes it independently reproducible. The 23 actual coefficients still satisfy every target inequality, including zero/missing midpoint controls. Thus neither the conjecture nor its general coefficient-only formulation is refuted.

<a id="q3627-a3"></a>
## A3 — recover joint inequalities from the proved marginal rows

Try to promote the source's marginal trapezoids to joint coefficient log concavity, even granting stronger log-concave marginals and a log-concave unsigned Alexander row. The formal polynomial (2) in [Q3626 A3](Q3626-ATTEMPTS.md#q3626-a3) satisfies all those hypotheses, signed homogeneity, both group symmetries and knot normalization. However, at alpha=(-1,-1,1,1), its coefficient is 4, while the two neighbors along e_3-e_4 both have coefficient 5. The inequality reads 16>=25 and fails. This is a failure **inside a fully occupied slice**, separate from the additional missing midpoints between its origin and degree-two layer.

The row and column marginal coefficients are (13,14,13) before the extra origin term; adding that term gives the source even rows (13,15,13). The unsigned Alexander row is (4,10,13,10,4). Both are log-concave, so a marginal log-concavity assumption cannot supply the missing conditional inequality. No alternating-link realization is asserted. The exact construction refutes the proposed joint-from-marginals lemma, not Q3627; the source Tait structure is the missing additional hypothesis.

<a id="q3627-a4"></a>
## A4 — close a two-branch minor induction using coefficient inequalities alone

Work the scalar deletion/contraction route, rather than original-tree exchange. The actual directed-cycle recurrence is P_Cn=X P_C(n-1)+Y^(n-1), as derived in [Q3626 A4](Q3626-ATTEMPTS.md#q3626-a4). Its coefficient row is a consecutive interval, so it succeeds on cycles. But one branch is not a canonical smaller Tait invariant, and the root-dependent conditional statistics must be retained.

A universal positive-sum closure lemma for individually root-direction-log-concave homogeneous branches is false: X² and Y² each satisfy every inequality, but their sum has zero XY coefficient between two coefficients 1. More generally, writing midpoint/neighbor coefficients of two branches as a_0,a_+,a_- and b_0,b_+,b_-, the combined defect contains the unbounded cross term

    2a_0 b_0 - a_+ b_- - b_+ a_-.

The two individual inequalities place no lower bound on this term. In the displayed monomial example it is -1. This identifies the exact extra algebraic obligation for the actual tree split: cross-branch alignment, not just branchwise inequalities. No such theorem was obtained from the canonical scalar minors. This is one failed induction attempt with a stated structural and algebraic gap, not a target counterexample or a claim against richer boundary-state recurrences. It shares the branch architecture with Q3626 A4, while testing the coefficient rather than support obligation.

<a id="q3627-a5"></a>
## A5 — use bare root-direction log concavity as a product closure theorem

P is multiplicative under connected sum. Try to propagate the target inequality by convolution, granting M-convex support as well. In one dimension, ordinary log-concave interval rows do have convolution closure; this does not establish the multivariate conditional inequality. Here is an exact homogeneous Laurent obstruction to that **general product lemma**.

Let X=x^-1,Y=y^-1,Z=z and q=4. Define

    A=qXYZ²+XZ+YZ+q,
    B=XYZ²+qXZ+qYZ+1.

Both have the same four-point M-convex support {(0,0,0,0),(-1,0,1,0),(0,-1,1,0),(-1,-1,2,0)}. Their signed degree is zero. Every root-direction coefficient inequality is satisfied: no root direction has three supported consecutive points, so every nontrivial neighbor product vanishes. The common support's exchange can also be checked directly as the unit square with dependent third coordinate.

In their product, at alpha=(-1,-1,2,0), the coefficient is 4q=16. The neighbors along e_1-e_3 both have coefficient q²+1=17. Thus 16²<17². The product even has the complete nine-point square support and remains M-convex; failure is genuinely a filled conditional coefficient inequality. These are **formal polynomials**, not asserted alternating-link invariants. They refute the proposed weak-class convolution theorem, not the connected-sum conjecture for actual links.

Additional hypotheses on actual factors, such as a stronger joint concavity/injection structure, may supply closure. That structure has not been proved at full scope; A2 already excludes the simplest all-input Lorentzian candidate. [CYCLE-PRODUCTS](CYCLE-PRODUCTS.md) gives a complete unrestricted connected-sum subfamily where one-dimensional closure is sufficient. This multiplicative conditional-convolution route is distinct from A4's additive branch closure, though both require more information than the individual inequalities.

Five full-target routes are now filed: symmetric-difference injection, stronger Hessian certificate, joint recovery from marginals, additive minor induction, and multiplicative conditional convolution. Exact relaxed controls are not target counterexamples; retained partials do not reset the counter. Root review decides the final attempt count.
