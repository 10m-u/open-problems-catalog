# Q2215: near-squares as an additive sumset

Read primary `texts/papers/collections-4f60c780b143a455.txt.gz`, Conjecture 1.1 and introduction. Its proved shifted-perfect-power theorem is **multiplicative** for exponents at least3; the exact present target is **additive** and about squares. A,B contain positive integers.

## Fixed-shift bounds and complete finite-summand exclusion

Suppose R=A+B and let E(X)=|(R△Q)∩[1,X]|. Choose a_1<a_2∈A, Δ=a_2−a_1. For every b∈B, both b+a_1,b+a_2 belong to R. If both are squares, write (t−s)(t+s)=Δ; the finitely many positive factor pairs of Δ bound all such b. All other b produce an off-square element of R. Each such element can be chosen by at most two b, one for each a_i. Therefore

    |B∩[1,X]|≤2 E(X+a_2)+C_Δ.

The symmetric argument with b_1<b_2∈B gives |A∩[1,X]|≤2E(X+b_2)+C'. Under E(X)=o(√X), both counting functions are o(√X). **Neither summand can be finite**: if A were finite then |R∩[1,X]|≤|A|·|B∩[1,X]|=o(√X), contradicting |R∩[1,X]|=√X+o(√X). This excludes a finite summand of any cardinality≥2, with the opposite summand unrestricted.

Also |R∩[1,X]|≤|A∩[1,X]|·|B∩[1,X]|. With fixed K=max(a_2,b_2), the two displayed bounds imply E(X+K)≥c X^(1/4) for all sufficiently large X if such a decomposition exists. This is a useful necessary error scale, weaker than the full desired exclusion at o(√X), and is not claimed as an improvement over the primary source's cited stronger special error theorem.

<a id="q2215-a1"></a>
## Q2215 A1 — Complete the proof from two fixed shifts

The derived o(√X) summand bounds and Ω(X^(1/4)) error bound are compatible with both summands infinite and of intermediate size. Their product can still cover about√X outputs. Thus the fixed-shift argument settles finite summands but leaves the sparse infinite/infinite case. **Failed full exclusion by two shifts; scoped theorem retained.**

<a id="q2215-a2"></a>
## Q2215 A2 — Apply additive-energy bounds after discarding the exceptional set

Counting a set of o(√X) exceptional outputs does not bound their representation multiplicities. A single output can have up to min(|A∩[1,X]|,|B∩[1,X]|) representations; its contribution to additive energy is squared. The Cauchy lower bound for energy concerns all representations, while ordinary fixed-difference square bounds concern clean outputs. No estimate shows the weighted error contribution is negligible at the stated unweighted error hypothesis. **Failed unweighted-error energy transfer.**

<a id="q2215-a3"></a>
## Q2215 A3 — Apply the known near-square irreducibility criterion

The primary source cites a theorem under error o(√X/2^((3+ε)log X/log log X)). This is a genuinely narrower hypothesis than o(√X). For example √X/log X satisfies the latter while exceeding the former threshold by an unbounded factor. No interpolation removes the additional decay. **Failed known-error-bound extension.**

<a id="q2215-a4"></a>
## Q2215 A4 — Transfer the source's proved shifted-power theorem

Its theorem concerns multiplicative AB and powers k≥3. The additive map A+B does not become AB by shifting entries, and setting k=2 is outside the theorem. The bipartite Diophantine estimates used there also lose their relevant uniform bounds at exponent2. No reduction preserving both operation and perturbation count is constructed. **Failed operation/exponent transfer.**

<a id="q2215-a5"></a>
## Q2215 A5 — Construct a counterexample from two translates of squares

Take A={u,v}, u<v, and B={n²−u:n²>u}. Then R is eventually Q∪(Q+v−u). The two square sequences intersect only finitely often by the fixed-difference factor-pair equation. Hence the translated branch adds Θ(√X) off-square outputs, violating the o(√X) hypothesis. This counterfamily fails at the exact perturbation scale. It shares the fixed-gap identity with A1 but tests a constructive counterexample rather than a universal exclusion proof. **Failed two-translate counterconstruction.**

Five full-target routes fail; the infinite/infinite case at the prescribed small error remains unresolved.
