# Common color dilation and a primitive-color obstruction for Q1262

This is a new structural partial and failed full-target inference, not a
recount of the earlier finite recognizer. The all-length exclusion below
depends on the already proved degree-dependent compression theorem.

## A dimension-matched forward dilation lemma

Put M=sum(m). The colored numerator is the Ehrhart numerator of the
M-dimensional product of scaled simplices with lattice-point polynomial

    L_(m,r)(u)=product_i binom(r_i u+m_i,m_i).

The primary [Deligeorgaki--Han--Solus, Corollary2.2 and Section4.1](https://escholarship.org/content/qt135937h5/qt135937h5_noSplash_af6056425c67947c0d921d43ba376183.pdf)
also identifies E_s with the Ehrhart numerator of the lecture-hall
simplex 0<=z_1/s_1<=...<=z_L/s_L<=1.

Suppose A_m^r=E_s and L=len(s)<=M. Pad s by M-L leading ones.
This preserves E_s: each added inversion-sequence coordinate is forced
zero and contributes no new ascent. Let the padded vector be s'.
Both underlying polytopes now have dimension M, so equality of their
numerators means equality of their entire Ehrhart polynomials, with
the same denominator(1-x)^(M+1).

For every positive integer t, dilating a polytope replaces L(u) by
L(tu). Color replacement r->tr dilates the product, and s'->ts'
dilates the lecture-hall simplex by its displayed inequalities.
Consequently

    A_m^(tr)=E_(ts') for every t>=1.               (1)

The dimension condition is essential to this proof; equality of
numerators alone in different dimensions does not identify lattice
counts. This is a forward closure lemma, not a characterization of
all representable colored inputs or all possible representing lengths.

## Primitive-color reduction is not an equivalence

One natural structural classification attempt is to divide a color
vector by the common gcd, classify the primitive vectors, then use
forward dilation to recover exactly the same membership on each ray.
This would require the converse of(1): a representable dilation would
have to imply a representable primitive input. An actual pair defeats
that inference.

Take m=(1,1),r=(4,5), whose gcd is1. From
(4u+1)(5u+1) the numerator is

    A_(1,1)^(4,5)=1+27x+12x^2, volume40.

The previously reviewed degree-two compression theorem reduces every
possible representation of arbitrary length to a canonical sequence
of length<=3. Enumerating all ordered nonunit factorizations of40,
with optional single unit separators and that length bound, gives22
candidates. Literal inversion-sequence enumeration of every candidate
shows none has row(1,27,12); all rows are retained in DILATION-CHECK.json.
Thus this primitive input is **not** s-Eulerian at any representing length.

Dilate both colors by3. The new input r=(12,15) has numerator

    1+205x+154x^2=E_(8,45).

This equality can be proved directly, without inferring it from a
bounded test. For any positive integers a,b, the two-coordinate row is

    E_(a,b)=1+[(ab+a+b+gcd(a,b)-4)/2]x
                 +[((a-1)(b-1)-gcd(a,b)+1)/2]x^2. (2)

To derive its last coefficient, both coordinates must be positive and
e_1/a<e_2/b. The reflection(e_1,e_2)->(a-e_1,b-e_2) pairs the strict
opposite inequalities; there are gcd(a,b)-1 equal pairs. Constant
coefficient1 and total count ab give the middle coefficient. Degree
one or constant boundaries are included by zero coefficients.

More generally (2) proves the all-size heterogeneous-color family

    A_(1,1)^(12t,15t)=E_(8t,45t)
      =1+(180t^2+27t-2)x+(180t^2-27t+1)x^2

for every integer t>=1, since gcd(8t,45t)=t. It also follows from(1)
at matched dimension2. Its color ray has an unrepresentable primitive
point(4,5) but representable points at every multiplier3t.

## Full-target outcome

The attempted primitive-ray equivalence fails, so simply removing
the common color gcd cannot classify Q1262. The forward lemma and
the infinite heterogeneous-color family remain useful partials.
Membership may vary with arithmetic on the multiplier; determining
all multipliers on this ray, or all color/multiplicity inputs, is not
claimed. No sixth full-target route is started pending count review.
