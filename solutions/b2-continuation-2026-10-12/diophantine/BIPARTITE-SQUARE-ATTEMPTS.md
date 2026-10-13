# Q2216: an absolute bound for bipartite square tuples

Read primary `texts/papers/collections-072f6f1fb4537620.txt.gz`, introduction, Questions1.3 and the main theorem scopes. The exact target asks for one absolute bound on min(|A|,|B|) for both ε=±1, with all positive coordinates unrestricted. There are no constraints on products within A or within B.

<a id="q2216-a1"></a>
## Q2216 A1 — Use uniform rational-point bounds on a four-row curve

Fix four distinct a_i. The equations y_i²=a_i x+ε define a degree-16 multiquadratic cover of the x-line. Its four finite branch points −ε/a_i are distinct and infinity has inertia2; Riemann–Hurwitz gives 2g−2=−32+5·8=8, hence g=5. The rational-point Uniformity Conjecture would bound the number of x uniformly, giving an absolute |B| bound whenever |A|≥4, and thus an absolute bound on the minimum. This is a clean sufficient conditional reduction, but that conjecture is unproved. **Failed unconditional uniformity proof.**

<a id="q2216-a2"></a>
## Q2216 A2 — Replace uniformity by fixed-curve Faltings

For each fixed four-row set the genus-five curve has finitely many rational points. Its bound need not be uniform as the a_i vary, and the target allows every coefficient size. Finiteness of each fiber does not bound all fiber sizes. A coefficient-uniform point theorem is precisely the missing obligation. **Failed fixed-curve-to-absolute-bound argument.**

<a id="q2216-a3"></a>
## Q2216 A3 — Bound the opposite side from two Pell rows

At ε=1, A={1,2} and v²−2u²=−1 give b=u²−1 with b+1=u² and2b+1=v². The negative Pell orbit contains infinitely many positive b, beginning24,840,28560. At ε=−1, v²−2u²=1 gives b=u²+1, beginning5,145,4901. Thus two rows admit arbitrarily large finite B for either sign, so a uniform bound on B from just two rows is impossible. The minimum remains2 and does not refute Q2216. The higher-row interaction is missing. **Failed two-row Pell bound.**

<a id="q2216-a4"></a>
## Q2216 A4 — Set k=2 in the published higher-power bipartite estimates

The source theorem's unconditional absolute minimum bounds require k≥3, and its ABC-assisted refinements likewise state k≥3. Degree, genus and approximation exponents in those estimates do not continue automatically to2. The two-row Pell family is a concrete reason that square constraints behave differently. No new square-specific estimate is obtained from replacing the exponent symbol. **Failed higher-power specialization.**

<a id="q2216-a5"></a>
## Q2216 A5 — Apply the integer Diophantine-tuple bound to A∪B

The required cross-products leave all within-side products unconstrained. The two-row example has1·2+1=3, so A∪B is already not a usual +1 Diophantine tuple. Standard clique bounds therefore do not apply to its complete bipartite square graph. A theorem extracting a uniformly large clique from every large bipartite example would be needed, but is not proved and does not follow from the cross-edge conditions. **Failed bipartite-to-clique transfer.**

Five worked routes fail to close the unconditional absolute-minimum question. The genus-five conditional reduction and both unbounded two-row Pell families remain useful boundary information.
