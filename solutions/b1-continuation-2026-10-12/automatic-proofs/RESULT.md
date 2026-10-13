# Executable automatic proofs for word arithmetic

[check.py](check.py) generates and checks complete finite transition
certificates for three identities at every positive width:

1. The low bit of modular addition equals the low bit of XOR.
2. Addition equals XOR exactly when AND is zero or the top-bit mask.
3. Addition of the top-bit mask equals XOR with that mask.

All input bits are universally covered. The reachable graph is closed under
every input symbol, and every possible terminal state is checked for a
counterexample. Thus the all-width result does not depend on the bounded
arithmetic controls. Two deliberately false variants are checked separately.

The representation reads least significant bits first and uses an external
end marker: a length-w word encodes the power-of-two bound P. Modular carry
is discarded at that marker. In the second identity, the AND flag is delayed
one digit so its final bit is excluded. This is how the top-bit exception is
represented, including width one.

In the third identity the mask has one at the last bit and zero at every
earlier bit. The checker tracks both a previous-mask bit and the presence of
an earlier one; terminal eligibility enforces that exact mask language.

This establishes a usable finite certificate lane for the programme's first
uniform identities and a concrete encoding boundary. Fixed compositions of
addition, XOR and AND remain synchronous regular: take products of primitive
machines and existentially project internal wires. A projection is an NFA;
subset construction and end/padding closure supply the standard FO operations.
[circuits.py](circuits.py) additionally implements the fixed acyclic circuit
compiler, with modular addition, XOR, AND, OR, NOT and zero gates. It decides
whether two outputs agree at every positive word width by exploring a finite
carry-state graph. It emits either a closed certificate or an actual shortest
counterexample word. Addition gates each have a carry bit; all other gates are
stateless. A product with a sticky difference flag and a nonempty-word flag
therefore has at most \(2^{a+2}\) states for a addition gates, so exploration
terminates. Induction over gates and word positions establishes that each
transition emits the exact corresponding word-circuit bits. Terminal carry
discard makes the result modular at every width.

The serialized certificates verify addition associativity and commutativity,
AND distribution over XOR, and De Morgan; a false addition-equals-XOR claim
returns a two-bit witness, independently checked with integer arithmetic.
There is no implemented general-purpose FO compiler. The original return's
nonautomatic Fourier-support and exact
bit-length boundaries still apply; this implementation does not extend them.

Java and Lean launchers are available locally. No Walnut installation or
original export archive was found in the project inventory. Therefore this
is newly generated verification, not replay of the missing original archive
and not a Walnut run. A complete compiled formalization of the infinitary
Q2168 argument was not part of this mathematical stopping target and is not
claimed. The exact Q2168 written solution remains separately retained.
