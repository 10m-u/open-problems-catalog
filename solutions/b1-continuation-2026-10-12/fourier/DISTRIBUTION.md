# Exact overlap distribution and the remaining tail problem

For every positive width \(w\ge1\), choose \(a,b\) independently uniformly
from \([0,2^w)\), and put
\(Z_w=|M_w[a,b]|\). The exact finite law has an atom at zero of mass
\[
 {2\over3}(1-4^{-w}).
\]
It has the trivial atom \(Z_w=1\) from \((0,0)\), of mass \(4^{-w}\),
and the following block mixture. For each \(0\le m<w\), give the
block weight \(4^{m-w}\); choose an odd \(d<2^{m+1}\) uniformly and
choose independent fair bits \(\epsilon_2,\ldots,\epsilon_{m+1}\).
Then its value is
\[
 \prod_{j=2}^{m+1}
 \left|\sin(\pi d/2^j)\right|^{\epsilon_j}
 \left|\cos(\pi d/2^j)\right|^{1-\epsilon_j}.
\]
An empty product is one. This gives a finite exact CDF by summing
the weights of products below any threshold, including all
multiplicities. No independence between different angle parameters
is being assumed: they all share the same odd \(d\).

## Derivation and a new exact moment

In block \(m\), there are \(2^m\) possible rows
\(a=2^{w-m-1}d\), and \(2^m\) nonzero mask columns. The higher
mask bits must vanish and bit \(m\) must be one. The remaining
mask bits select sine or cosine factors independently. The
nonzero count is \(1+\sum_{m=0}^{w-1}4^m=(4^w+2)/3\).
This proves the mixture and zero atom.

Unitarity gives \(E[Z_w^2]=2^{-w}\). In addition,
\[
 E[Z_w^4]={4\over3}(3/8)^w.
\]
For a fixed row, summing the fourth powers over all masks gives
\[
 \prod_{i=0}^{w-1}{3+\cos(4\pi a2^i/2^w)\over4}.
\]
The last factor is one. For the remaining factors, the frequencies
are \(2,4,\ldots,2^{w-1}\). In expanding their product, every
nonempty signed sum of these distinct powers is nonzero: the
largest selected power exceeds the sum of all smaller powers.
Its absolute value is less than \(2^w\). Therefore averaging over
the \(2^w\) rows kills every nonconstant Fourier term. The mean
row sum is \((3/4)^{w-1}\). Divide the total row sum by \(4^w\)
to obtain the formula. This also handles \(w=1\), where the
remaining product is empty.

Thus the squared-magnitude kurtosis is
\[
 {E[Z_w^4]\over E[Z_w^2]^2}={4\over3}(3/2)^w.
\]
The matrix becomes progressively less flat relative to its RMS
scale. It is not a matrix with all surviving entries comparable
to \(2^{-w/2}\). For any \(s>0\),
\[
 \Pr(Z_w\ge s)\le
 \min\{1,\;2^{-w}s^{-2},\;{4\over3}(3/8)^ws^{-4}\}.
\]
For \(0<\theta<1\), Paley–Zygmund applied to \(Z_w^2\) also gives
\[
 \Pr(Z_w\ge\sqrt{\theta\,2^{-w}})
 \ge {3\over4}(1-\theta)^2(2/3)^w.
\]
These are rigorous quantitative tail bounds, not matching
asymptotics at every moving threshold.

## Failed full-tail routes

The full ambition includes a sharp large-width tail law, not merely
an exponential-size list of exact finite products. Five routes
were pursued; the finite mixture and moment theorem remain useful
partial results.

1. **Independent angle model.** Replace the angles of an odd row
   by independent uniform dyadic angles and apply a product law.
   At the first two free digits the squared sine probabilities
   already obey the deterministic relation
   \(p_j=4p_{j+1}(1-p_{j+1})\). They cannot be sampled independently.
   Mask choices are independent conditional on the row, but that
   does not remove the row dependence. The resulting independent
   product law is not the distribution above.
2. **Flat block law.** Approximate a \(2^m\)-square unitary block
   by entries of size \(2^{-m/2}\). Its coherence stays above
   \(2/\pi\) as \(m\) grows, and the exact global fourth moment
   has the exponential kurtosis just computed. These rule out
   uniform flatness. A sparse exceptional component would require
   an explicit count of large entries, not a flat approximation.
3. **Central limit theorem for log coefficients.** Conditional
   on a row, the mask produces independent summands, so a
   triangular-array CLT is tempting. Rows \(d=1\) have sine
   factors of size \(O(2^{-j})\), with log contributions of order
   \(j\), whereas other rows have different orbits. There is no
   verified row-uniform normalization or variance limit; the
   zero atom must also be removed first. A conditional CLT for
   generic rows would not give the requested rare upper tail.
   In particular d=1 has log-mask variance of order \(m^3\)
   and largest summand of order m; this example alone does not
   violate Lindeberg. The failed step is a common row normalization
   and rare-tail conclusion, not a claimed counterexample to a CLT.
4. **Moment matching.** Use the exact second and fourth moments
   to solve for the tail. They do supply the inequalities above.
   They do not determine a law: finitely many moments leave
   infinitely many measures, and the two displayed bounds have
   different rates and threshold dependence. No matching lower
   bound at a fixed macroscopic threshold follows.
5. **Transfer pressure.** For real \(q>0\), moments reduce to
   products of
   \(|\sin(\pi t)|^q+|\cos(\pi t)|^q\) along dyadic orbits.
   A transfer operator for the two inverse branches is an exact
   route to pressure and a possible large-deviation principle.
   The fourth-moment expansion closes because distinct binary
   frequencies cannot cancel. For general \(q\) it is not a
   finite trigonometric polynomial; no spectral-gap argument,
   differentiable limiting pressure, or uniform passage from
   moments to sharp tails was proved. This route stops at that
   precise analytical obligation.

These are failures to settle the full tail ambition, not five
independent impossibility theorems. This target reaches its
five-attempt stopping limit; its finite law and moment theorem
are filed as partial.
