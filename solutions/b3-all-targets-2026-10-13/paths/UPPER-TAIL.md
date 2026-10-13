# All-size upper-tail inequalities for path-height distributions

13 October 2026. These are partial scopes of Q4331 and Q4332. They leave
the complete coefficient sequences unresolved. No priority claim is made.
The source's [coefficient formula, Corollary 3.15](https://arxiv.org/html/2609.38084v1)
is used for A_n and B_n; the normalization argument below is supplied here.
The Motzkin/Riordan endpoint formulas below are derived by deleting horizontal
steps and counting their reinsertions. The [checker](check_heights.py) and
[receipt](HEIGHT-CHECK.json) supply independent exact controls.

## Q4331: upper-tail ultra-log-concavity

Put d=ceil(n/2), a_i=[t^i]A_n and b_i=[t^i]B_n. Write

    t_A=ceil((n+2)/4), t_B=floor((n+2)/4)+1.

**Theorem.** For every n>=1, a_i/binom(d,i) satisfies log-concavity at
every internal index t_A<i<d; b_i/binom(d,i) satisfies it at t_B<i<d.
The inequalities at i=1 are also automatic because a_0=b_0=0.

The exact upper-tail formulas are

    a_i=4(2i+1)8i(i+1)-3(n+1)!/
        [(n-2i+1)!(n+2i+3)!],                       i>=t_A,
    b_i=8i8i^2(2n-1)-(6n^2+n-2)!/
        [(n-2i+1)!(n+2i+1)!],                       i>=t_B.

After division by binom(d,i), each expression is a positive constant times
three positive factors: a linear factor in i, its displayed quadratic,
and

    W_i=i!(d-i)!/[(n-2i+1)!(n+2i+sigma)!],

where sigma=3 for A and 1 for B. The linear factors are log-concave.
The quadratics are positive on the stated formula ranges and have strictly
negative second logarithmic derivative: for A, its numerator after clearing
the positive denominator is -128i^2-128i-48(n+1)-64; for B, a quadratic
of the form c*i^2-e with c,e>0 gives numerator -2c^2*i^2-2c*e.
Thus their consecutive values are log-concave wherever the formulas apply.

The last factor has consecutive ratio

    W_i/W_(i-1)=
      2i(2d-2i+3)/[(2d+2i+sigma-1)(2d+2i+sigma)],    n=2d,
      2i(2d-2i+1)/[(2d+2i+sigma-2)(2d+2i+sigma-1)],  n=2d-1.

The numerator decreases from i to i+1 in the formula ranges: after dropping
the positive factor two, its difference is 2d+1-4i for even n and
2d-1-4i for odd n, both negative at i>=t_A and hence at i>=t_B.
The denominators increase. Therefore these ratios decrease, proving
log-concavity of W at the needed indices. Multiplying the three positive
log-concave factors proves the theorem, provided i-1 also lies in the
formula range, which explains the strict lower endpoint in the statement.
Small empty ranges are harmless. This strengthens ordinary upper-tail
log-concavity to the catalog's degree-normalized version in that range.

## Q4332: the final nontrivial inequality

Let the length be 2m or 2m+1 and write (a,b,c) for the counts at maximum
heights m,m-1,m-2, respectively. The polynomial statistic is one plus
height, so the final nontrivial log-concavity inequality is b^2>=a*c.

**Theorem.** This inequality holds for M_l and R_l at every length l>=0.
If the polynomial has fewer than three height coefficients, the statement
is interpreted as the applicable trivial boundary inequality.

For m>=5 put H=2m^2-7m+3 and use the following exact formulas:

| Family | a | b | c |
|---|---|---|---|
| M_(2m) | 1 | 2m^2+m-3 | H+(2m-5)binom(2m,2)+binom(2m,4) |
| M_(2m+1) | 2m+1 | (2m-3)(2m+1)+binom(2m+1,3) | H(2m+1)+(2m-5)binom(2m+1,3)+binom(2m+1,5) |
| R_(2m) | 1 | m(2m-3) | H+(2m-7)binom(2m-2,2)+2binom(2m-3,2)+binom(2m-2,4) |
| R_(2m+1) | 2m-1 | (2m-5)(2m-1)+4m-4+binom(2m-1,3) | (2m-1)(2m^2-11m+12)+(2m-2)(4m-12)+3(2m-3)+(2m-7)binom(2m-1,3)+2binom(2m-2,3)+binom(2m-1,5) |

Here is a derivation, rather than extrapolation from the finite controls.
Reflection at the upper ceiling gives Dyck counts of maximum heights
m,m-1,m-2 equal to 1,2m-3,H. Indeed in this range the exact-height formula
is binom(2m,m-h)-3binom(2m,m-h-1)+3binom(2m,m-h-2)-binom(2m,m-h-3);
the further reflected images are outside the possible range. A core Dyck
path of semilength j has 2j+1 slots for horizontal steps. Inserting q
indistinguishable horizontal steps into these slots gives binom(2j+q,q)
Motzkin paths. To get a specified height near m, only j=m,m-1,m-2 can
contribute. Substitution gives the two M rows.

For Riordan paths the slots at height zero are excluded. A core with k
irreducible components has 2j-k positive-height slots, so its insertion
count is binom(2j-k+q-1,q). For height j-1, the core has 2j-5 irreducible
possibilities and two possibilities with two components. For height m-2
in semilength m, the component counts are

    k=1: 2m^2-11m+12; k=2: 4m-12; k=3: 3.

They follow by isolating the unique component attaining height m-2:
strip its enclosing up/down steps for k=1; for k=2 the other component
has size one or two; for k=3 the other two are single up/down pairs.
Uniqueness holds at m>=5. These component counts add to H. Reinsert zero,
one, two, three, four or five horizontal steps as required by the total
length; this gives the two R rows.

Finally put m=u+5. The four defects b^2-a*c become, in table order,

    10u^4/3+206u^3/3+3163u^2/6+10709u/6+2251,
    56u^6/45+656u^5/15+5704u^4/9+4838u^3+
      1845853u^2/90+1374593u/30+42229,
    10u^4/3+166u^3/3+2071u^2/6+5767u/6+1011,
    56u^6/45+544u^5/15+3952u^4/9+2822u^3+
      912793u^2/90+579847u/30+15283.

Every coefficient is positive, proving the inequality for all m>=5.
The remaining lengths 0,...,9 are checked exactly by the included finite
state recurrence; these finitely many cases complete this endpoint theorem.
The proof says nothing about an arbitrary interior height.
