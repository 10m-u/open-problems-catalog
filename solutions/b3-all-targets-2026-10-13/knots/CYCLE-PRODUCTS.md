# Complete cycle-product subfamily for Q3626 and Q3627

Use the canonical positive directed-cycle Tait diagrams C_n, n>=2, and their mirrors. For any finite lists n_1,...,n_a and m_1,...,m_b, take their oriented connected sum. With X=x^-1,Y=y^-1,Z=z,W=w, source multiplicativity and the exact cycle tree enumeration give

    P = product_i sum_(k=0)^(n_i-1) X^k Y^(n_i-1-k)
        product_j sum_(l=0)^(m_j-1) Z^l W^(m_j-1-l).             (1)

The mirror formula follows from source property (iv). Empty products give the constant factor 1 and are allowed. Theorem: every polynomial (1) has M-convex Laurent support and satisfies all Q3627 inequalities at every alpha in Z⁴, including missing coefficients and every i,j.

Put R=sum(n_i-1), S=sum(m_j-1). Its support is exactly

    {(-k,-(R-k),l,S-l): 0<=k<=R, 0<=l<=S}.                    (2)

All coefficients are positive there. To prove exchange, compare any two points. Within the first coordinate pair their sums agree; a strict surplus in one coordinate gives a deficit in the other, and a unit exchange moves both k values inward while preserving their bounds. The same holds for the last pair. Each possible surplus is in one of these pairs, so this supplies both exchanged points. This includes R=0 or S=0, where the relevant surplus never occurs.

The coefficient at (-k,-(R-k),l,S-l) is a_k b_l. Each row a,b is a convolution of uniform interval rows. Such a row is log-concave with no internal zeros. Here is an elementary all-size justification. The Toeplitz matrix of a uniform interval row has every order-two minor nonnegative: if both off-diagonal entries are 1, the two diagonal indices lie between their indices and hence are also in the interval. Otherwise the off-diagonal product is zero. Products of these Toeplitz matrices correspond to convolution; every order-two minor of a product is a finite nonnegative Cauchy–Binet sum. The minors with adjacent rows/columns give c_k²>=c_(k-1)c_(k+1). Interval supports remain intervals under convolution, so no internal zeros are introduced. The empty-product row is a singleton and satisfies the same statements.

For a root direction within the first pair, the joint inequality is b_l² times the corresponding a-row inequality. Within the last pair it is a_k² times the b-row inequality. For a direction joining the two pairs, **both neighbors cannot be in (2)**: they have different sums on the first pair, whereas (2) has fixed sum -R. Their product is zero. If a midpoint is outside support but both neighbors were inside, their first/last-pair sums would force the midpoint to have the same sums; in an internal direction, the interval bounds would force it into support. Thus all missing-midpoint inequalities hold as well. The case i=j is tautological.

The proof covers arbitrary lengths and arbitrary numbers of factors. [Exact checker](check_boninger.py) only supports it with bounded product controls. It does not settle mixed-sign prime links or either full target. This is a local internally reviewed subfamily proof (ROOT-REVIEW.md#boninger-final), with no novelty claim; the special-alternating literature already proves broader unmixed factors.
