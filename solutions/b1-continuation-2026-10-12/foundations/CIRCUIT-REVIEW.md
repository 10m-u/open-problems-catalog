# Independent review of the generic circuit certificate lane

12 October 2026. Reviewed `../automatic-proofs/circuits.py`, `check.py`,
`RESULT.md` and their emitted JSON certificates. The all-positive-width
claim passes for valid fixed acyclic circuits with distinct input/gate
names and the documented operations.

Induct over word positions and then topologically over gates. Each addition
gate's one carry bit and its current operand bits produce its exact next
sum bit and carry. The other gates are bitwise and stateless. These are
the bits of the intended width-modular circuit; carry is discarded at any
chosen terminal width. A sticky difference bit records any output mismatch,
and the nonempty flag excludes width zero. Every positive-length input word
ends in one reachable state, so a closed complete transition graph with no
bad terminal proves equality at every positive width. The loose bound
\(2^{a+2}\) on states is valid for \(a\) addition gates.

The verifier reconstructs every transition, requires completeness and
reachability, and recomputes the bad-state list. A false packet must supply
a word actually reaching a bad state; its arithmetic check independently
confirms unequal integers. Breadth-first generation makes the emitted
first bad-state witness shortest. The verifier checks validity of that
witness, rather than independently certifying its minimality.

The specialized certificate also handles its end conditions correctly.
The AND flag is delayed by one digit, so an AND bit at the final position
is excluded and exactly the top-mask exception remains. The toggle mask's
previous/current bit flags enforce one at the final position and zero
earlier, including width one. The low-bit check starts with zero carry.

The reported scope is accurate: fixed acyclic circuits over modular
addition, XOR, AND, OR, NOT and zero. There is no general FO compiler,
Walnut replay, Fourier-support recognizer, or formal-assistant verification
of the entire mathematical programme claimed. The generic lane is wider
than the initial three identities and carries an actual finite decision
procedure, rather than only bounded testing.

One optional parser tightening: `compile_spec` could assert that its input
names are distinct. The current dictionary semantics silently aliases a
repeated input name. This does not affect the saved valid specs or the
theorem for valid circuits; it is a malformed-input validation issue.

`check_root_reviews.py` verifies every saved generic/specialized packet,
compares 20 additional bounded circuits to direct integer semantics, and
rejects three altered certificate controls. It writes only the independent
receipt in this directory and does not regenerate root artifacts.
