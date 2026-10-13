# Uniform colored permutations: endpoint symmetric parts and small gamma orbits

This is a local all-size family partial for Q1263, independent review
accepted (ROOT-REVIEW.md#colored-final). It does not interpret both gamma vectors for every colored
multiset. No novelty claim is made; the primary already treats
[colored Eulerian special cases](https://escholarship.org/content/qt135937h5/qt135937h5_noSplash_af6056425c67947c0d921d43ba376183.pdf).

## An all-size positive symmetric-part partition

Take ordinary permutations of N distinct letters, each with common
colors1,...,r, r>=2. Order colored letters by color then symbol, and
append the sentinel(N+1)^1. Let U be the descent enumerator of words
whose last color is1 or r; let V enumerate all remaining words.

Map every symbol i to N+1-i and every color c to r+1-c, keeping
positions fixed. For distinct letters this complements the strict
comparison at each of the N-1 internal adjacent positions, including
equal-color comparisons. If the last color is extreme, the last
sentinel descent is also complemented. Thus the involution sends
d to N-d on that subset, proving U=x^N U(1/x).

If the last color is interior, both old and new last colors exceed1,
so both have a sentinel descent. Only the N-1 internal descents
are complemented, giving d'=N+1-d. Thus V=x^(N+1)V(1/x).
Also V is divisible by x. Therefore U and V/x are respectively
symmetric with respect to N and N-1, and A=U+x(V/x). Their degrees
are at most those bounds; when r=2, V/x is the zero polynomial.
The polynomial A has degree N: the descending symbol order with all
colors r has all N descents. By uniqueness of
the degree-N symmetric decomposition, a=U and b=V/x. This proves
an actual word-subset interpretation of ordinary coefficients of
both parts for every N,r. It does not by itself interpret gamma.
For r=2 the interior subset is empty. For r=1 the polynomial has
degree N-1; use the ordinary uncolored theory instead.

## Explicit gamma orbits for N=2 and all r>=2

The actual numerator and its decomposition are

    A=1+(r²+2r-2)x+(r-1)²x²,
    a=1+(4r-2)x+x²=(1+x)²+4(r-1)x,
    b=r(r-2)(1+x).

Among extreme-last-color words, take the four words12 and21
with both colors1, or both colors r. Their descents are respectively
0,1,1,2. On these four words, toggling the underlying order and
toggling the common color between1 and r are two commuting
involutions; together they act transitively. Thus this is an explicit
four-word orbit with enumerator(1+x)². Every other extreme
word has exactly one descent. Their count is4r-4, giving the
4(r-1) singleton gamma1 objects. Thus gamma_a=(1,4(r-1)).

Interior-last-color words are paired by the same complement-symbol/
color involution. It swaps underlying orders12 and21 and changes
d to3-d, so each orbit has one descent1 word and one descent2
word. No word is fixed. There are2r(r-2) such words, hence
r(r-2) orbits with enumerator x(1+x), giving eta_b=(r(r-2)).
These are explicit actual word orbits, not integer encodings.

For N=1, the two extreme colors give1+x, and each interior color
is a singleton contributingx. Thus gamma_a=(1),eta_b=(r-2).
The degree-zero r=1 one-letter case is separate and immediate.

## Why the general multiset extension fails

The proof requires distinct symbols. A pair of identical colored
letters has no descent before or after complementing both color and
symbol; the indicator is not complemented. Also i->N+1-i need
not preserve general multiplicity and heterogeneous-color vectors.
The actual repeated-letter counterexample in Q1263 G02 shows even
common colors do not rescue the literal endpoint partition.
The full conditional bi-gamma interpretation remains unresolved.
