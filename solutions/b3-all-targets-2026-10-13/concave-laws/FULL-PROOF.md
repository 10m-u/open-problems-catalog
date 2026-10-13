# Q4082: sharp variance bound for discrete alpha-concave laws

Full proof accepted after root and retained-agent independent review.
See [Q4082-REVIEW.md](../stirling/Q4082-REVIEW.md) and its exact receipt. The precise target is Conjecture 4.7 of
[Alqasem–Aravinda–Marsiglietti](https://arxiv.org/html/2610.05439v1).
The proof has no finite-support, symmetry or slope restriction on X.
No originality or external peer-review claim is made.

Set alpha=-1/beta, beta>3, k=(beta-2)^2(beta-3)/(beta-1)^3 and
D=(beta-1)/(beta-2). We prove

    M(X)^2[1+k Var(X)]<=1.

MEAN-MATCHED-COMPARISON.md reduces this to a two-sided affine law with
the same maximum mass and mean, dominating X in convex order. ONE-SIDED.md
proves the exact sharp bound for each normalized one-sided affine law,
using analytic bounds and the finite rational middle-region certificate.
It remains to glue the two tails; this note supplies that step.

## First-moment bound for one affine tail

For w_j=(1+lambda j)^(-beta), let F=1+S=sum w_j and A=sum j w_j. Then

    A<=D S F.

Let G have Gamma(beta,1) density rho and set f(x)=1/(e^(lambda x)-1).
Tonelli gives S=E f(G) and A=E[f(G)(1+f(G))]. Write
V(x)=x-(beta-1)log(x)+constant. The one-dimensional variance inequality
for this density is

    Var(f(G)) <= E[G^2 f'(G)^2]/(beta-1).

Here is a direct proof, including the needed regularity. Let h=f-E f and
g(x)=rho(x)^(-1) integral_(x)^infinity h(t)rho(t)dt. Then
h=V'g-g'. Integration by parts gives

    E h^2 = E[h'g],
    E h^2 = E[g'^2+V''g^2] >= E[V''g^2].

Cauchy applied to the first identity yields
(E h^2)^2<=E[h'^2/V''] E[V''g^2]<=E[h'^2/V''] E h^2.
Dividing proves the inequality (the zero-variance case is immediate).
At zero f behaves as 1/(lambda x), rho as x^(beta-1), and g is bounded;
the boundary terms vanish for beta>2. At infinity g is bounded and rho
decays exponentially. All derivative integrals used are finite for beta>2.
Thus no unverified boundary truncation is required for this f.

Now x^2 f'(x)^2=(lambda x)^2 f(x)^2(1+f(x))^2<=f(x)(1+f(x)),
because (lambda x)^2 f(x)(1+f(x))<=1 by sinh(t/2)>=t/2.
Consequently Var(f(G))<=A/(beta-1). Since A=S+S^2+Var(f(G)),

    A <= S+S^2+A/(beta-1),

which rearranges to A<=D S(S+1). A zero tail has S=A=0.

## Gluing the two affine tails

Let each tail, including its unnormalized atom at zero, have moments
(F_i,A_i,B_i), and put S_i=F_i-1. The two-sided normalization is
T=F_1+F_2-1=1+S_1+S_2. Its mean numerator is A_1-A_2 and its second
moment numerator is B_1+B_2. The desired inequality is

    L_T=T^4-T^2-kT(B_1+B_2)+k(A_1-A_2)^2>=0.

The proved one-sided inequalities imply

    k B_i <= F_i^3-F_i+k A_i^2/F_i.

Substituting and simplifying exactly gives

    L_T >= 3 T S_1 S_2(T+1)
       -k[S_2 A_1^2/F_1+S_1 A_2^2/F_2+2A_1A_2].

The first-moment bound A_i<=D S_i F_i controls the bracket by

    D^2 S_1S_2[S_1F_1+S_2F_2+2F_1F_2]
      =D^2 S_1S_2 T(T+1).

Therefore

    L_T >= (3-kD^2) S_1S_2 T(T+1)>=0,

since kD^2=(beta-3)/(beta-1)<1. This proves the sharp bound for every
two-sided affine law, including one-sided and point-mass limiting cases.

Finally the mean-matched comparator has M(Z)=M(X) and Var(Z)>=Var(X).
Apply its bound and multiply by the positive k. Translation removes the
mode-zero normalization. This proves the full frozen catalog assertion,
with all proof components and the exact certificate independently reviewed. The source's one-sided asymptotic example establishes that
the coefficient k cannot be increased, at the same fixed alpha.
