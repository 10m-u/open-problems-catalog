# Exact optimum of the tested four-colour palette template

12 October 2026. This is the Q1861-A4 failed construction, not a proposed universal optimality theorem. The family uses colour1 on[0,a], colour2 on(a,b], and independent uniform3/4 on(b,1], with0≤a≤b≤1. Counting ordinary Schur triples gives expected normalized density L=4A+2B, as explained in that route.

Write z₊=max(z,0). Exact rectangle inclusion-exclusion gives

    2A=(1−a)²−(1−2a)₊²−(1−b)²+(1−a−b)₊²
        −(b−a)²+(b−2a)₊²,
    B=b−3b²/2               if b≤1/2,
      (1−b)²/2              if b≥1/2.

For b≤1/2 no sum from the two prefix intervals exceeds1. If a≤b/2, A=a²/2; if a≥b/2, A=2ab−3a²/2−b²/2. For each fixed b the maximum is at a=2b/3 and A=b²/6. Therefore L≤2b−7b²/3≤3/7, with equality b=3/7,a=2/7.

For b≥1/2 the remaining cells have the following exact upper bounds. These follow by optimizing the stated quadratic first in a over the stated interval and then in b; the boundaries are a=1/2,b=2a,a+b=1. No branch is omitted.

| Cell (always b≥1/2) | Expression for L | Maximum bound |
|---|---|---|
| a≥1/2 | 4(b−a)(1−b)+(1−b)² | 1/3 |
| a≤1/2, a+b≤1, b≥2a | 2a²+(1−b)² | 3/8 |
| a≤1/2, a+b≤1, b≤2a | 8ab−6a²−b²−2b+1 | 5/12 |
| a≤1/2, a+b≥1, b≥2a | 4a(1−b)−(1−b)² | 1/3 |
| a≤1/2, a+b≥1, b≤2a | 4ab−8a²−3b²+4a+2b−1 | 2/5 |

For detail, the first and fourth rows reduce to (1−b)(3b−1), whose maximum is1/3. In the second row a≤min(b/2,1−b); the two b ranges split at2/3, giving maxima3/8 and1/3. In the third row the unconstrained a maximizer is2b/3: it is feasible up to b=3/5, yielding the convex function1−2b+5b²/3 on[1/2,3/5], of maximum5/12. After that the endpoint a=1−b gives18b−15b²−5, decreasing after3/5 and bounded by2/5. In the fifth row the a maximizer is(b+1)/4, feasible for b≥3/5; its value is−5b²/2+3b−1/2≤2/5. Before that endpoint a=1−b gives the same18b−15b²−5≤2/5. These cover even empty/degenerate boundary intervals consistently.

All five bounds are≤5/12<3/7. Hence the template has exact maximum3/7. Rounding endpoints for integer[N] and coincident summands contributes onlyO(N), so its asymptotic expected optimum is also3/7. It is strictly below both the primary10/21 lower bound and the stronger preserved50368/90905 return bound. This proves the proposed template cannot solve the full four-colour extremal problem.
