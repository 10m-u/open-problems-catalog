# Linear Algebra & Matrix Theory

3 problems: 3 open.

[All subjects](../README.md) · [Index by number](../INDEX.md)

| Q | Title | Status |
|---|---|---|
| [Q3984](linear-algebra-matrix-theory.md#q3984) | Is C(6)=32? | Open |
| [Q3985](linear-algebra-matrix-theory.md#q3985) | Is C(7)=42? | Open |
| [Q3990](linear-algebra-matrix-theory.md#q3990) | Does ρ\_CP(B) have the distribution of ∏\_{j=1}^n(1+Y_j²), where Y_j are iid with the law of \|X\|… | Open |

<a id="q3984"></a>

## Q3984. Is C(6)=32?

**Status:** Open · **Kind:** open problem · **Collection** 40

Is C(6)=32?

**Context.** Work over C. Starting from 1 and x, allow arbitrary complex linear combinations for free. Each multiplication of two previously computed polynomials costs one operation. Let P_m⊂C[x]\_{≤2^m} be the polynomials obtainable using at most m such multiplications; let its bar denote Zariski closure in this coefficient space. Put C(m)=max{d:C[x]\_{≤d}⊂bar(P_m)}.

**Source.** Elias Jarlebring and Gustaf Lorentzon. *The Polynomial Set Associated with a Fixed Number of Matrix-Matrix Multiplications*. 2026. [primary source](https://doi.org/10.1137/25M1779036) Location: Complex-coefficient part of Conjecture5.2, p.572.

**Literature check.** Status: Paper-origin. These concern universal polynomial inclusion, not a single Taylor polynomial. The July final retains both conjectures. Jarlebring’s September2026 GAMM abstract conjectures C(m)=m²−m without specifying the coefficient field; it makes no resolution claim. https://indico3.mpi-magdeburg.mpg.de/event/58/contributions/1074/ No matching proof or disproof found on 10 October 2026.

**Further links.** [1](https://indico3.mpi-magdeburg.mpg.de/event/58/contributions/1074/)


<a id="q3985"></a>

## Q3985. Is C(7)=42?

**Status:** Open · **Kind:** open problem · **Collection** 40

Is C(7)=42?

**Context.** Work over C. Starting from 1 and x, allow arbitrary complex linear combinations for free. Each multiplication of two previously computed polynomials costs one operation. Let P_m⊂C[x]\_{≤2^m} be the polynomials obtainable using at most m such multiplications; let its bar denote Zariski closure in this coefficient space. Put C(m)=max{d:C[x]\_{≤d}⊂bar(P_m)}.

**Source.** Elias Jarlebring and Gustaf Lorentzon. *The Polynomial Set Associated with a Fixed Number of Matrix-Matrix Multiplications*. 2026. [primary source](https://doi.org/10.1137/25M1779036) Location: Conjecture5.3, p.573.

**Literature check.** Status: Paper-origin. These concern universal polynomial inclusion, not a single Taylor polynomial. The July final retains both conjectures. Jarlebring’s September2026 GAMM abstract conjectures C(m)=m²−m without specifying the coefficient field; it makes no resolution claim. https://indico3.mpi-magdeburg.mpg.de/event/58/contributions/1074/ No matching proof or disproof found on 10 October 2026.

**Further links.** [1](https://indico3.mpi-magdeburg.mpg.de/event/58/contributions/1074/)


<a id="q3990"></a>

## Q3990. Does ρ\_CP(B) have the distribution of ∏\_{j=1}^n(1+Y_j²), where Y_j are iid with the law of |X|…

**Status:** Open · **Kind:** open problem · **Collection** 40

Does ρ\_CP(B) have the distribution of ∏\_{j=1}^n(1+Y_j²), where Y_j are iid with the law of |X| conditioned on |X|≤1 for a standard Cauchy variable X?

**Context.** For n≥1 put N=2^n and B=R_{θ\_1}⊗⋯⊗R_{θ\_n}, where R_θ=[[cosθ,sinθ],[−sinθ,cosθ]] and the θ\_j are independent uniform variables on [0,2π). Apply exact Gaussian elimination with complete pivoting, choosing a largest absolute entry of the remaining block, breaking ties by column index then row index. Define ρ\_CP(B)=max_k||B^(k)||max/||B||max, including the original matrix and all elimination stages.

**Source.** John Peca-Medlin. *Complete pivoting growth of butterfly matrices and butterfly Hadamard matrices*. 2026. [primary source](https://doi.org/10.1080/03081087.2026.2660796) Location: precise paper restatement of the 2021 dissertation’s GECP-distribution direction (pp.199–200).

**Literature check.** Status: Origin: precise paper restatement of the 2021 dissertation’s GECP-distribution direction (pp.199–200). Doctoral context: UC Irvine Mathematics PhD 2021; advisors Michael Cranston and Thomas Trogdon; Numerical, spectral, and group properties of random butterfly matrices. The accepted version explicitly specifies this law despite inconsistent max/min displays elsewhere; publisher discussion confirms the unresolved ordering restriction. No matching resolution found on 10 October 2026.

