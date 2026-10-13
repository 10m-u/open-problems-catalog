# Q2316: complete fixed-coordinate exclusion through 5,000

For the exact integer equation

\[
x^3+x+y^3+y+z^3+z=xyz+1,
\]

every hypothetical solution has all coordinates odd and
**min(|x|,|y|,|z|)>5000**. This is a restricted finite-coordinate
certificate, not an assertion of global nonexistence. Unlike a cube search,
the other two coordinates are unrestricted.

All terms on the left are even, so xyz is odd. Fix x=a odd, put
s=y+z (necessarily even) and t=yz. The equation is exactly

\[
(3s+a)t=s^3+s+a^3+a-1.
\]

Polynomial division gives

\[
27(s^3+s+a^3+a-1)
=(3s+a)(9s^2-3as+a^2+9)+R(a),\qquad
R(a)=26a^3+18a-27.
\]

Thus D=3s+a divides R(a) and D≡a modulo6. R(a) is strictly
increasing on the integers, with R(0)=-27 and R(1)=17, so it never
vanishes at an integer. D=0 would force R(a)=0 and cannot occur.
Every possible integer pair y,z therefore occurs in the finite list:

1. Enumerate all signed divisors D of R(a) with D≡a modulo6.
2. Set s=(D-a)/3. Require D to divide s³+s+a³+a-1 and set t to its quotient.
3. Require Δ=s²-4t to be a nonnegative integer square, and
   (s±√Δ)/2 to be odd integers.

These conditions are sufficient as well: the resulting y,z have sum s
and product t and give the original equation by direct substitution.
For each fixed a this is a complete decision procedure for its integer
fibre. It provides no uniform bound on a.

[check_q2316_fibers.py](check_q2316_fibers.py) emits complete factorizations
and admissible-divisor discriminants for every odd a with |a|≤5000.
It independently checks factor primality, product reconstruction, the
divisor lists and every proposed discriminant. All values are below2^64.
[FIBER-CHECK.json](FIBER-CHECK.json) reports 34,713 discriminant candidates
and no solution. [FIBER-CERTIFICATES.json](FIBER-CERTIFICATES.json) retains
the full finite certificate.

The earlier B2 report already derived this fixed-coordinate divisor
identity to exclude0,±1. The new contribution is the complete expanded
coordinate certificate and its scope, rather than a claim to a new
identity. Prior rational and local points remain valid.
