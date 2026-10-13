# Colored multiset Eulerian results at restricted scope

The full Q1262 structural classification and Q1263 natural interpretation
remain unresolved. We read final [Deligeorgaki--Han--Solus](https://escholarship.org/content/qt135937h5/qt135937h5_noSplash_af6056425c67947c0d921d43ba376183.pdf),
Questions4.1/4.7 and the colored-word conventions. Published uniform-color
representations and interpretations are inputs, not new local solutions.

## Finite exact arbitrary-length recognition

For nonconstant P of degree d>=1 and volume V=P(1), prior reviewed degree compression gives
a representation of length at most2d-1 whenever any exists. Remove
leading/trailing units and adjacent unit copies. Every canonical sequence
has a nonunit ordered factorization of V, with optional single unit
separators. Thus listing those with length at most2d-1 is exhaustive for
existence. COLORED-PROBE.json records36 exact colored instances for the
specified multiplicity families and volume<=180; no exhaustive claim
beyond that recorded list is made. Known uniform-color cases are controls.
Independent literal colored-word enumeration reproduces every numerator.
The constant case P=1 is separate and is represented by s=(1);
the nonconstant bound2d-1 does not apply at d=0. The supplied probe
only scans nonconstant examples and is not a public general-purpose
recognizer with that special case implemented.

Examples of heterogeneous exclusions are

    A_(1,2)^(3,2)=1+20x+15x², volume36,
    A_(2,2)^(1,2)=1+13x+10x², volume24,
    A_(2,3)^(1,2)=1+24x+45x²+10x³, volume80.

No ordered factorization/separator candidate at the guaranteed length
bound matches any of these, excluding sequences of arbitrary length.
The first has27 candidates, the second22, and the third158. Explicit
positive heterogeneous examples and every representing compressed
vector found are also retained. These are finite classifications, not
a structural characterization of every pair m,r.

## Exact multiplicity-growth operator

If m_i=a is increased to a+1, color r_i=r stays fixed, and M=sum(m),
its Ehrhart values multiply by(rt+a+1)/(a+1). Differentiating the
generating function proves

    A_new=[1+(c(M+1)-1)x]A+c x(1-x)A', c=r/(a+1).

This is valid for every admissible m,r. It preserves the actual algebraic
recurrence, but neither s-Eulerian membership nor termwise positive
gamma transitions follows without more structure. A worked actual
membership loss and a formal negative gamma branch appear in the
attempt packets. No novelty claim is made for this elementary operator.

## Endpoint-color and small gamma interpretations

ENDPOINT-COLORS.md proves a natural positive symmetric-part partition
for every ordinary permutation with a common number of colors, and
explicit gamma orbits for one and two distinct letters with arbitrarily
many colors. Its repeated-letter counterexample limits that method.
These are named-family partials; no general gamma interpretation or
novelty claim is made.
