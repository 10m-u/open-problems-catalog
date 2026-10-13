# Exact parity-class optimum for rainbow Schur triples

12 October 2026. A local restricted proof for Q1860, without a novelty claim or a full-question closure. Primary [Hegde–Kumar–Pratibha](https://arxiv.org/abs/2609.18474), local `texts/papers/collections-8bce2eab4ff176c2.txt.gz`, Theorem2.3 constructs a parity colouring with density9/22. We prove that this is optimal over **all** three-colourings whose even integers have a single common colour, with no interval assumption on the odd colours.

Let M_par(N) maximize the number of ordered rainbow pairs (x,y), x+y≤N, in that class. Then

    M_par(N)/binom(N,2) = 9/22 + O(1/N).

An unrestricted maximizer has not been shown to belong to this class. Thus this is a partial theorem for Q1860 only. The original stronger Q1861 lower bound50368/90905 is preserved; this theorem does not determine the four-colour optimum or existence of its limit.

## Reduction to a continuum cut

Relabel the even colour3. An odd point of colour3 cannot occur in any rainbow triple: every Schur triple is either entirely even or has exactly two odd points and one even point. Recolouring such an odd point1 or2 never loses a rainbow triple. We can therefore assume that the odd points are partitioned into A (colour1) and B (colour2).

Every cross-colour unordered pair of odd endpoints x<z gives the two ordered mixed-parity rainbow triples (x,z−x) and (z−x,x), so there are2|A||B| mixed pairs. The odd+odd rainbow pairs number2|{(x,y)∈A×B:x+y≤N}|. With m=ceil(N/2), replace the odd grid by m equal cells of[0,1], and let S be the union of cells assigned colour1. Put a=|S| and

    F(S) = a(1−a) + ∫_{S×Sᶜ} 1{x+y≤1} dx dy.

The cell discretization changes the triangle test only on O(m) pairs intersecting a strip of widthO(1/N), uniformly for arbitrary choices of S. Thus R_N=2m²F(S)+O(N), and R_N/binom(N,2)=F(S)+O(1/N). The matching lower construction has S=[0,4/11]∪[10/11,1]. It remains to prove sup_S F(S)=9/22.

## A relaxed maximizer exists

Set K(x,y)=1+1{x+y≤1}. For a measurable 0≤s≤1 write

    F(s)=∫∫ K(x,y)s(x)(1−s(y)) dx dy.

This agrees with F(S) for s=1_S. The feasible subset of L² is weakly compact. The kernel is Hilbert–Schmidt, so its integral operator is compact; consequently its quadratic form is weakly continuous on this bounded set. The linear term is also weakly continuous. Hence F attains a maximum on the relaxed feasible set. The explicit indicator above has value9/22>3/8, so the maximum is strictly above3/8.

At a maximizer define f=2s−1 and

    g(x)=∫ K(x,y)(1−2s(y))dy
        =q+(1−x)−2∫₀^(1−x)s(y)dy,
    q=1−2∫s.

The first variation of F is g. Therefore s=1 almost everywhere on {g>0}, and s=0 almost everywhere on {g<0}. On {g=0}, s may initially be fractional. Also g is Lipschitz and g'(x)=f(1−x) almost everywhere, with g(0)=2q and g(1)=q.

## The two reflected gradients travel around a diamond

Put u(x)=g(x),v(x)=g(1−x). Then

    u'=f(1−x),    v'=−f(x).

Where u and v are both nonzero, the first-order condition gives u'=sign(v), v'=−sign(u). Thus d(|u|+|v|)/dx=0 there. A Lipschitz function has derivative0 almost everywhere on its zero level set. Consequently the set {u=0,v≠0} has measure0: on it u'=0 almost everywhere by that fact, but stationarity at1−x would require u'=sign(v). The reflected case also has measure0. Where both are zero the derivative of |u|+|v| is0 almost everywhere. Hence |u|+|v| is constant on the whole interval, equal to3|q|.

If q=0, this forces g≡0 and g'=0, so f=0 almost everywhere and s=1/2. Its value is3/8, contradicting the attained lower bound. Thus q≠0. Complementing s changes q's sign and preserves F, so assume q>0. Then u and v never vanish simultaneously. The zero sets have measure0, so s is an indicator almost everywhere and the maximizer is bang-bang.

The motion starts at (u,v)=(2q,q). Both coordinates are positive, with velocity(1,−1), until (3q,0) at timeq. It then runs successively around the diamond |u|+|v|=3q, with unit coordinate speeds; its period is12q. Its required endpoint is(q,2q), which is reached after11q and then every12q. Therefore

    1=(12j+11)q,    q=1/(12j+11),    j≥0.

The diamond trajectory has average |u|=3q/2 over a period. The omitted segment, from(q,2q) to(2q,q), has lengthq and the same average |u|. Thus the complete interval of length1 also has ∫₀¹|g|=3q/2.

By symmetry of K and ∫∫K=3/2,

    F(s)=3/8−(1/4)∫f Kf
        =3/8+(1/4)∫fg
        =3(1+q)/8.

Since j≥0, q≤1/11 and F≤9/22. Equality j=0 gives the positive-gradient set [0,4/11]∪[10/11,1], exactly the primary construction. This proves both the continuum maximum and the stated uniform asymptotic parity-class theorem.

## Limits of the route

This argument exploits the two odd colours and the universal even colour. With three arbitrary colour classes, the first-order conditions involve coupled three-state assignments; they do not reduce to this two-coordinate diamond. A theorem making all evens monochromatic without reducing the rainbow count would solve the remaining full Q1860 scope, but no such theorem was established. The restricted proof is a full mathematical result about a named class, not evidence that all colourings are in that class. Checker controls and the five full-target routes are filed separately.
