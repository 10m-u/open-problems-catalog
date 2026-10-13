# Independent review of the three root foundations targets

12 October 2026. Read `ROOT-DEFINABILITY-ATTEMPTS.md`, its checker and
receipt, the local Haase–Starčak survey Sections 3–4, and the updated
primary paper [2306.10432v5](https://arxiv.org/html/2306.10432v5),
Sections 6–7. The **five failed full-target routes per question pass**
mathematical and stopping-count review. All three full questions remain
unresolved. Their existing partials are retained and not recounted.

For Q1375 the five objectives are a Boolean-game lower bound, a bit-online
decision construction, a representation-to-decision lower-bound transfer,
a prefix-controlled recursive hardness construction, and a bounded
numerical-game upper bound. The whole-integer/bit-online example has the
claimed opposite truth values. The updated paper indeed gives EXPSPACE
hardness for E*A*E* and 2-EXPSPACE hardness for E*A*E*A*, and explicitly
leaves the arbitrary fixed-prefix classification open. Polynomial-bit
games would be in PSPACE, contradicting the first hardness through the
deterministic space hierarchy; this avoids relying on an unproved
polynomial-hierarchy separation. Macro nesting lacks the stated prefix
and size control, so it is a failed proof route, not a counterexample to
all higher hardness constructions.

For Q1376 the routes address minimum generator bounds, a finite-cutoff
affine-growth test, a recognizing-monoid abstraction, existential run
verification, and an inclusion obstruction basis. The large redundant
moduli example does **not** refute a bound on minimum representations;
the report states that limitation. Under canonical encodings its union
should be described as the same fixed small full-number language, rather
than literally a one-state unrestricted word language. The masked K
construction defeats each fixed coefficient cutoff because every tested
positive coefficient is invertible modulo the larger prime. The monoid
failure is exact: finite accepted representatives and the full language
have the same accepting monoid image, while only the former is
existentially definable. The checker uses a finite **recognizing**
transition monoid of a nonminimal DFA; minimality is unnecessary to that
argument. The missing word confirms loss of coverage. The two remaining
routes fail through the known K expressivity obstruction and through the
full definable language's containment of K, respectively.

For Q1481 the routes distinguish first-order powers from existential
universality, absolute from relative growth, word encodings from numerical
interpretations, positive from negated uses of the input predicate, and
standard self-embeddings from extension embeddings. All examples preserve
the required unary input signature. Interleaving three tracks has an
unbounded additive length increase, so it cannot be an automatic function.
Because a regular input predicate is already BA-definable, adding it
cannot make that numerical interleaving graph first-order definable in BA.
The packing failure is therefore real, without claiming no other unary
universal predicate is possible.

The new complement-of-K construction is particularly useful and is correct.
In base four, membership in K means every active digit is 1 or 2. Its
complement has a digit 0 or 3 at a position \(h=4^j\leq x\). The
conditions \(P_2(h)\) and \(h\equiv1\pmod3\) select exactly powers
of four. In \(x=u+d h+r\), \(r<h\), the condition \(u=0\) or
\(V_2(s,u)\) with \(s\geq4h\) says the remaining higher part is
divisible by \(4h\). All conditions are existential with fixed
coefficients. At zero there is no active digit and no witness, consistently
with zero belonging to K. Consequently adjoining this already-existential
complement to a positive union/concatenation algebra cannot generate K,
while the relative quantifier-free atom \(\neg R_2(x)\) does define K.

The fifteen failures have distinct construction objectives, although
several share K as a witness. Reusing that witness is disclosed and does
not convert them into independent impossibility theorems. The packet's
full-target scope and five-per-question disposition are accepted.

The exact checker receipt verifies 65,536 complement values, the masked
slice, 272 affine residue controls, the bit game and the monoid example.
`check_root_reviews.py` supplies an additional direct complement check and
independent bounded controls, without claiming a definability algorithm.
