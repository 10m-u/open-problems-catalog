# Q49: finiteness of capillary three-wave resonances

Let F(n)=n(n−1)(n+2). All three indices are at least 2. Since F is positive and strictly increasing there, reorder a≤b<c. The exact equation becomes

    sqrt(F(a))+sqrt(F(b))=sqrt(F(c)).

The other sign choice is the same unordered resonance with its largest entry relabeled. Read primary source: Shao's cached thesis `texts/k647aebbd8c40.txt.gz`, equations (5.2.8)–(5.2.9), Propositions 5.2.1–5.2.2 and the adjoining elliptic/surface discussion. Its minimum-index≤10000 claim and earlier B2 all-indices≤1000000 report retain their original provenance; the missing original verification archive is not recovered by this continuation.

<a id="q49-a1"></a>
## Q49 A1 — Apply integral-point finiteness to the common squarefree kernel

The equation implies F(a)F(b) is a square; write F(a)=D u²,F(b)=D v² and F(c)=D(u+v)² with D squarefree. For fixed D, the nonsingular cubic D y²=F(n) is genus one and has finitely many integral points by Siegel. This leaves a union over unbounded D; finiteness of every fiber does not imply finiteness of the union. The additive relation between ordinates is an extra useful restriction, but no uniform D bound is proved. **Failed fixed-twist finiteness route.**

<a id="q49-a2"></a>
## Q49 A2 — Parameterize by the simple relation c=a+b

For positive a,b,

    F(a+b)−F(a)−F(b)=ab(3a+3b+2).

For a,b≥2 this is greater than 2 sqrt(F(a)F(b)). Indeed, after division by ab and squaring, the needed inequality is

    ab(3a+3b+2)² > 4(a−1)(a+2)(b−1)(b+2),

whose difference expands into a polynomial with positive coefficients after a=A+2,b=B+2, A,B≥0. Therefore sqrt(F(a+b))>sqrt(F(a))+sqrt(F(b)), and no resonance uses this linear parameterization. It yields the known strict c<a+b constraint, not a bound on a. More complicated c parameters remain unconstructed. **Failed sum-index construction.**

<a id="q49-a3"></a>
## Q49 A3 — Separate the leading irrational asymptotic from integer c

For a=b the target is F(c)=4F(a); the leading approximation is c≈4^(1/3)a plus a bounded correction. Irrationality of 4^(1/3) excludes exact equality c=4^(1/3)a, but not equality of the full cubic values. The actual known solutions (5,5,8),(10,10,16) already demonstrate this gap. For general b/a the leading value (a^(3/2)+b^(3/2))^(2/3) varies, so even the fixed irrational coefficient disappears. No uniform Diophantine separation matching the lower-order terms is established. **Failed leading-term irrationality argument.**

<a id="q49-a4"></a>
## Q49 A4 — Use the second squared-frequency root for Vieta descent

Treating F(c) as a variable, the quadratic has roots (sqrt(F(a))±sqrt(F(b)))². The lower root is integral because the upper resonance forces a common squarefree kernel. But descent in the frequency variable requires that lower root equal F(d) for an integer d≥2. F maps integers into a thin cubic sequence; an integral lower root is not generally in that image. At a=b=5, it is zero, whose integer preimages 0,1,−2 are outside the allowed domain. Thus this nominal descent already exits the domain at a known solution, and no integrality-preserving global index descent is proved. **Failed Vieta descent on cubic frequencies.**

<a id="q49-a5"></a>
## Q49 A5 — Infer integral finiteness from the general-type surface

The source's homogeneous sextic surface has Kodaira dimension 2. General type alone is not an unconditional theorem that every integral-point set is finite. Even conjectural non-Zariski-density would still require analyzing exceptional curves, which might carry infinitely many integral points. The geometric classification supplies a structural model but no proof excluding such curves or bounding their integral points uniformly. No unconditional finiteness argument is obtained from it. **Failed geometric-classification completion.**

Five worked routes fail to prove the exact finiteness target. The common-kernel reduction, index inequality, finite reported domains and source surface classification remain scoped evidence. No numerical restart or absence of software is counted.
