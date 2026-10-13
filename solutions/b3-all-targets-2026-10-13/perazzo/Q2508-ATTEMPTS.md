# Q2508 full-target attempts

Target: classify every legal Perazzo form with unimodal Hilbert function,
over characteristic zero, n>=m>=3, d>=3. The m=2 solution is excluded.
Prior imported maximal/minimal and WLP examples are not new attempts.
Five proposed full-target routes below have explicit failures. Local
count5 is pending independent mathematical and counting review. The
classification remains open; useful narrower proofs are retained in
[DERIVATIVE-RANKS.md](DERIVATIVE-RANKS.md).

<a id="q2508-a1"></a>
## A1 — classification between the published universal rank extrema

Try stratifying every catalecticant between the source's asserted minimum
and maximum, then resolving the remaining adjacent inequalities.
Derive the exact decomposition h_i=r_i+r_(d-i)+rank B_i rather than
assuming block independence. The source lower-bound step fails on the
legal binary-plus-pure family: d4,m3,n4 gives actual (1,8,8,8,1), below
its claimed h2 minimum10. Its nonzero catalecticant blocks have overlapping
images. The proposed bounding region excludes actual solutions, so it
cannot support a full classification. The derivative-rank identity is
a retained reduction, not itself a structural answer.

<a id="q2508-a2"></a>
## A2 — induction on degree with a fixed Perazzo presentation

Try the source's general-derivative lemma as a closure step reducing
the classification from degree d to d-1 at fixed n,m. For every e>=3
the same binary-plus-pure family meets its numerical hypothesis, but
every directional map W->D_1W has rank at most e+1<q=e+2. A general
derivative loses an essential X direction. Thus this prescribed induction
does not remain in its fixed-n hypothesis. A1 and A2 share a witness
family but obstruct different obligations: universal rank bounds versus
closure under a degree-reducing operation. An induction with changing
presentations and extra cone data remains a separate possible method.

<a id="q2508-a3"></a>
## A3 — classify W and remove G as a harmless gauge term

Try reducing all F to G=0, then classifying W by its derivative ranks.
Only G in S_1 W is removable by a linear X shift. The restricted pairing
B_i measures the obstruction. The actual quartic family with r3 and
identical W changes from (1,15,14,15,1) at Q0 to (1,15,15,15,1) at
rank-one Q. Thus W alone does not determine even unimodality. The worked
replacement gives an exact all-r rank-Q classification within this family,
but arbitrary J_i and G classes remain to be classified.

<a id="q2508-a4"></a>
## A4 — real-rooted Hilbert polynomials as a complete certificate

Try identifying all unimodal Perazzo forms through a stronger polynomial
positivity certificate: their Hilbert polynomials having only real
nonpositive roots. This would give log-concavity and a factor-based
classification if it were necessary as well as sufficient. For the actual
flat quartic F_3 the polynomial 1+8z+8z^2+8z^3+z^4 is unimodal, but its
degree4 gamma coefficients are (1,4,-6). A palindromic positive polynomial
with real nonpositive roots factors into reciprocal pairs
(1+z)^2+c z with c>=0 (and any factors at -1), so its gamma coefficients
must all be nonnegative. Here gamma2=-6 proves the certificate fails.
This actual new family computation is not a replay of the source's
Hessian/WLP obstruction. A root-based sufficient subclass cannot furnish
the necessary full classification.

<a id="q2508-a5"></a>
## A5 — propagate a generic-stratum classifier by semicontinuity

Try classifying generic maximal-rank strata, then carrying the answer to
all special forms by openness or closedness of unimodality. Work two
actual one-parameter families. The fixed-W quartic Q=tU_1^2 is generically
unimodal and not unimodal at0, so closed specialization fails. Independently
the explicit degree6 family W_t=W_binary+tW_generic is generically
(1,10,21,20,21,10,1) and specializes to the unimodal flat row at0,
so an open neighborhood inference fails. Exact rational derivative ranks
at t1 establish the nonempty generic rank stratum; nonzero minors prove
the all-but-finitely-many parameter statement. A3/A5 share one control,
but A5 keeps the full G contribution and fails geometric propagation,
with a second independent W-deformation witness. A complete analysis of
all rank strata is still needed.

## Pending stop

Five different proposed full-target methods have failed. The exact
restricted-pairing formula, the all-degree flat family, the all-r quartic
rank classification, and the two deformation limits are retained. None
claims to classify all Perazzo forms. Source corrections are local
review candidates and have not been published or communicated externally.
No sixth route is begun while the honest counting review is pending.
