# Q3113: smooth polynomial values

The target quantifies over every nonconstant integral polynomial and every positive ε. The cached primary source `texts/papers/collections-0dc4593e61766f95.txt.gz`, §6.3, Question 6.4, restates the question and attributes the known quadratic case to Bober–Fretwell–Martin–Wooley. A smooth value means its absolute value has no prime divisor greater than n^ε.

## An unconditional constructive linear case

Let f(n)=an+b, a≠0. Put g=gcd(|a|,|b|), a'=a/g, b'=b/g, s=sign(a). Choose B>1 in the residue class s b' modulo |a'|. This class is coprime to |a'|, so B is also; when |a'|=1 there is no restriction. Take

    m=1+k φ(|a'|),       n=(s B^m−b')/a'.

Euler's theorem makes n an integer. For all sufficiently large k it is positive and strictly increases, and f(n)=s g B^m≠0. All prime divisors lie in the fixed finite set dividing gB. Its largest prime is eventually at most n^ε for every ε>0. This proves the full requested smoothness assertion for every linear polynomial, including negative leading coefficient and b=0, without Dirichlet's theorem or an assumed prime in a progression. It is a scoped constructive result, with no originality claim.

<a id="q3113-a1"></a>
## Q3113 A1 — Extend the fixed-prime-support construction

The construction solves an exponential equation an+b=s g B^m because the inverse map is linear. For a higher-degree f, prescribing the same values requires integral points on f(n)=s g B^m, not a residue-class inversion. Even n²+1=B^m with a fixed B may have only finitely many solutions. Thus the fixed-support proof does not establish the all-degree target. **Failed full-target extension; linear theorem retained.**

<a id="q3113-a2"></a>
## Q3113 A2 — Factor f and intersect the known smooth-value sets

Suppose f=∏ f_i with constituent linear or quadratic factors. Infinitely many n satisfying each separate smoothness condition do not guarantee an infinite simultaneous intersection. The constructed linear subsequences may be unrelated exponential sequences. If all constituents were smooth at the same n, their product would be smooth, but the available individual theorems do not assert that joint condition. An intersection or density theorem is the missing step; separate infinitude is logically insufficient. **Failed individual-factor transfer.**

<a id="q3113-a3"></a>
## Q3113 A3 — Force divisibility by a smooth modulus using CRT

Choose roots modulo powers of small primes, and combine them into f(n)≡0 mod M. CRT can give an n of size comparable to M, when compatible local roots exist. For degree d, |f(n)| is of order n^d, so after dividing by M≈n, the uncontrolled cofactor still has size n^(d−1). Divisibility by a large smooth part supplies no bound on the prime factors of that cofactor. Iterating with much larger M makes the chosen n larger too. No argument forces the entire cofactor below n^ε or smooth. **Failed divisibility-only construction.**

<a id="q3113-a4"></a>
## Q3113 A4 — Replace polynomial values by independent random integers

At magnitude n^d, the heuristic proportion of n^ε-smooth integers is positive for fixed d/ε, suggesting infinitude. Turning this into a proof requires controlling the distribution of the thin sequence f(n) relative to the smooth set. Local admissibility and the ordinary density of smooth integers do not give an error estimate for this polynomial sequence. The random model is the attempted statistical argument, with a precise missing correlation theorem; it is not execution evidence for a density statement. **Failed heuristic-to-proof route.**

<a id="q3113-a5"></a>
## Q3113 A5 — Factor after polynomial substitution

If f(g(t)) splits into factors with degree at most ε deg g, evaluating at t gives a sufficient small-prime bound relative to n=g(t), up to constants and a small ε margin. Test the simple degree-amplifying substitutions g(t)=t^m on f(X)=X³−2. The composition t^(3m)−2 is Eisenstein at 2 for every m; its largest irreducible factor has degree 3m, and the required degree ratio stays 3. This proposed substitution family cannot supply an arbitrarily small ratio. More sophisticated substitutions remain possible, but none is constructed for arbitrary f. **Failed monomial-composition route.**

The linear theorem is complete at its scope; the all-degree question stops at five failures and remains unresolved.
