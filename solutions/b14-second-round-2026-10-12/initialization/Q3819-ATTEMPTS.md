# Q3819: four further sufficient routes and their obstructions

Date: 12 October 2026. These continue the [reviewed centroid-inversion route](FINAL-ROUTE-REVIEW.md), counted as attempt 1. Each route below concerns the full existence-of-a-short-improving-path question, but only its specified sufficient argument is refuted. None is a counterexample to Q3819. Short improving paths exist in every example. Internal review by the main thread is pending; no novelty or external peer-review claim is made.

The permitted moves transfer one point between nonempty clusters, recompute means, and strictly decrease within-cluster squared error $\Phi$. The actual source is [Manthey and van Rhijn, STACS 2024, §5, p.52:14](https://drops.dagstuhl.de/storage/00lipics/lipics-vol289-stacs2024/LIPIcs.STACS.2024.52/LIPIcs.STACS.2024.52.pdf). Its particular exponential pivot sequence does not answer the short-path existence question. Lemma 4 supplies

\[
\Delta_{A\to B}(x)
=\frac{|B|}{|B|+1}(x-\mu_B)^2
-\frac{|A|}{|A|-1}(x-\mu_A)^2.
\tag{1}
\]

Every computation below was also checked by directly recomputing $\Phi(C)=\sum x^2-(\sum x)^2/|C|$, independently of (1).

## Attempt 2: lift fixed-size uncrossing swaps into two improving moves

A tempting polynomial construction sorts membership through size-preserving swaps of inverted points, with at most a quadratic number of pair corrections, and simulates each swap by two improving transfers. The simulation lemma is false.

If $x<y$, with $x$ in the higher-centroid cluster and $y$ in the lower-centroid cluster, swapping them at fixed cluster sizes decreases SSE: writing $h=y-x>0$, the gain is

\[
2h(\mu_{\rm high}-\mu_{\rm low})
+h^2\left(\frac1{|C_{\rm high}|}+\frac1{|C_{\rm low}|}\right)>0.
\]

For the distinct points $\{-4,-3,-2,-1,0\}$, take

\[
A=\{-3,-2\},\quad B=\{-4,-1,0\},\quad
\mu_A=-5/2<\mu_B=-5/3.
\]

The swap of $-4\in B$ and $-3\in A$ lowers $\Phi$ from $55/6$ to $20/3$. Both possible first transfers are legal. Moving $-3$ first raises $\Phi$ to 10 and is forbidden. Moving $-4$ first lowers $\Phi$ to $5/2$, after which the second transfer would raise it to $20/3$ and is forbidden. Thus neither two-transfer order is an improving path realizing the beneficial swap. This rejects the fixed-size swap lift, not adaptive transfers that change cluster sizes or stop after its first move. The first improving transfer already reaches a local optimum; zero-gain moves remain forbidden.

## Attempt 3: bound the path by a uniform objective-decrease scale

Try to prove that every nonlocal partition has an improving transfer of gain at least $\Phi/\operatorname{poly}(n,k)$, then select such moves and use geometric decrease. Such a bound independent of the coordinates is false even at $n=4,k=2$.

For any $0<\delta<1/12$, put

\[
t=\frac{1+\sqrt{3-6\delta}}2,\qquad
A=\{0,1\},\quad B=\{t,t+1\}.
\]

Here $1<t<(1+\sqrt3)/2$ and $\Phi=1$. There are exactly four legal transfers. The two inner-point transfers, $1$ from $A$ to $B$ and $t$ from $B$ to $A$, each have gain

\[
\frac12-\frac23(t-1/2)^2=\delta.
\]

The two outer-point transfers have gain $1/2-(2/3)(t+1/2)^2<0$. Thus the largest available gain is exactly $\delta$, arbitrarily small at fixed $n,k$ and fixed $\Phi$. Either inner transfer reaches a local optimum in one move. For example after moving 1, the reverse gain is $-\delta$, while the other two possible donations have gains $(2-2t-t^2)/3<0$ and $-(t+1)^2/3<0$. This rejects a uniform progress scale, not polynomial-length paths. A coordinate-precision-dependent estimate is a different claim and would not answer the stated question.

## Attempt 4: descend monotonically toward the polynomial-time global solution

One-dimensional globally optimal clustering can be computed using ordered interval partitions. Try to guide the transfers toward such an optimum, using disagreement with its assignment as a discrete polynomially bounded potential. Even dynamically ranking clusters by their centroids does not make this disagreement decrease.

For $X=\{0,1,2,3,6,9\}$ and $k=3$, start from

\[
\{0,1,2\},\quad\{3\},\quad\{6,9\},\qquad\Phi=13/2.
\]

The unique global optimum, up to cluster names, is

\[
\{0,1,2,3\},\quad\{6\},\quad\{9\},\qquad\Phi=5.
\]

The checker certifies uniqueness by enumerating all 90 unlabeled nonempty three-cluster partitions of these six points, not merely interval candidates. Rank each current cluster and each optimal cluster by its centroid, and count points whose current rank differs from their optimal rank. Initially only points 3 and 6 disagree, giving count 2.

The **only** improving transfer is point 2 from the first cluster to the singleton middle cluster. The resulting partition is $\{0,1\},\{2,3\},\{6,9\}$, with objective $11/2$. Centroid ranks remain strict and unchanged. Points 2, 3 and 6 now disagree, giving count 3. Moreover, this new partition has no improving transfer. Thus every improving path is forced to increase that disagreement and terminate at a nonglobal local optimum.

This rejects monotone descent toward a selected global optimum, even with a unique optimum and dynamically ordered names. It is distinct from attempt 1's pairwise inversion count: the initial partition here already consists of ordered intervals, and the tested statistic refers to an independently computed global assignment. The one-move local path fully satisfies Q3819 on this example.

## Attempt 5: smooth at a uniform scale and pull the path back

Try to apply the source's smoothed running-time theorem at a Gaussian noise scale determined only by $n,k$, then transfer its path and local-optimality certificate to the original input through stability of the strict comparisons. The required uniform stability is false.

To remain within the published theorem's condition $4kd\le n$, use eight distinct points, $k=2,d=1$. Fix $h=1/100$, set $a=(1+h)/2$, and take

\[
A=\{0,h,1,1+h\},\qquad
B=\{t,t+h,t+1,t+1+h\}.
\]

The two innermost transfers, $1+h$ from $A$ to $B$ and $t$ in the reverse direction, have gain $(4/3)a^2-(4/5)(t-a)^2$. The critical threshold is $t_0=a(1+\sqrt{5/3})$. At $t=t_0$ these two gains are zero, while the six other gains are strictly negative: their source-center distances are no larger, and their target-center distances are strictly larger. For $t<t_0$ sufficiently close there are exactly two improving moves. For $t'>t_0$ sufficiently close all eight moves are strictly worsening, so the same initial assignment is a strict local optimum. The displacement $t'-t$ can be arbitrarily small at fixed $n=8,k=2$. A positive affine rescaling places the points inside $[0,1]$, as required by the source, without changing move signs.

Consequently no positive perturbation radius depending only on $n,k$ can preserve the local-optimality decision on every instance. For any fixed positive Gaussian standard deviation, the strict local configuration has an open coordinate box around it. Independent Gaussian perturbations assign that box positive probability. On this event, the noisy algorithm can terminate with zero moves at the initial assignment, whose pullback is not locally optimal for the original input. For $t\uparrow t_0$, choosing a fixed translated local configuration and a smaller fixed open box gives a failure probability bounded below by a positive constant depending on the chosen noise scale, not by a constant uniform across all scales. This last qualification is essential.

For an individual input one can choose smaller perturbations depending on its comparison margins. Those margins approach zero in this family. The source's running-time ceiling depends polynomially on $1/\sigma$ and also contains $k^{12k}$ in dimension one. Thus that direct transfer does not supply the required polynomial in variable $n,k$ independent of coordinates. This does not disprove a different robust smoothed argument or a deterministic path theorem.

Attempts 3 and 5 share a coordinate-sensitivity mechanism, with separately checked four-point and eight-point witnesses, but reject different sufficient premises: a minimum original-objective gain versus stability of a stochastic theorem transfer. They should not be presented as unrelated phenomena, or split again into additional failures for the precision and $k^{12k}$ dependencies.

## Controls and failure-count scope

[check_q3819_routes.py](check_q3819_routes.py) independently recomputes every legal transfer in the finite swap and global-target examples, verifies the optimal partition's uniqueness over all partitions, and checks rational threshold approximants on both sides of $t_0$ without floating point. Receipt: [Q3819-ROUTE-CHECK-RESULTS.json](Q3819-ROUTE-CHECK-RESULTS.json).

Together with the previously reviewed inversion route, these are five specified rejected sufficient arguments for Q3819, subject to the main thread's independent review and counting assessment. This does not establish a lower bound on its shortest improving path. In particular, the examples have at most two-step paths to local optima. Under the user's per-problem stopping rule, no further Q3819 solve attempt will be started after all five have been accepted as substantive failures. Other B14 problems remain separate.
