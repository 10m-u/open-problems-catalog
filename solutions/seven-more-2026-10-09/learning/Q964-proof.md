# Q964: sublinear regret when the evolution rate is c/T

Date: 2026-10-09. **Proposed complete affirmative answer.** This is a written
research argument with exact finite controls and a separate internal review;
it is not a formally certified or externally peer-reviewed theorem.

## 1. Question and result

The model and benchmark are those of Sections 2 and 7 of Khosravi, Paes Leme,
Podimata and Tsorvantzis, *Preferences Evolve And So Should Your Bandits*
([version 5](https://arxiv.org/html/2307.11655v5)). There are K arms with
unknown parameters (r_i,b_i) in [0,1]^2. Starting at q_0=1, action I_t
produces a Bernoulli observation with conditional mean r_{I_t}q_t and then
updates the unobserved state by

\[
q_{t+1}=(1-\lambda)q_t+\lambda b_{I_t}.
\]

Here t=0,...,T-1. Rewards have the usual conditional Bernoulli law given the
history. The benchmark knows all parameters and chooses the best complete
length-T action sequence. Its reward is not multiplied by an approximation
factor. The catalog asks whether worst-case expected regret is o(T) for
known \(\lambda=c/T\), fixed c>0 and fixed K.

**Theorem.** For every fixed integer K>=1 and real c>0, there is an explicitly
specified horizon-aware policy such that, uniformly over all
\((r_i,b_i)\in[0,1]^{2K}\),

\[
R_T=O_{K,c}\!\left(T^{4/5}(\log T)^{1/5}\right)=o(T),
\qquad \lambda=c/T\in(0,1].
\]

The policy observes neither the state nor any arm parameter. It does not
assume a replenishing arm, a reward bounded away from zero, a reward gap, or
separated end states. A grid dynamic program implements its planning step
in O(KT^3) arithmetic operations, with an additive reward loss at most 1/2.
No optimality of the exponent 4/5 is asserted.

The idea is to measure the transient response while all states are still
close to one. A reference arm measures how another arm changes the state;
an adjacent reference-only experiment removes the reference arm's own
effect. Only reward-weighted end-state estimation is necessary.

## 2. Exploration schedule and estimators

For now fix an integer block length L>=1 and a confidence level
\(\delta\in(0,1)\). Put

\[
N=(4K+2)L,\quad W=3K+2,\quad
\eta=\sqrt{\frac{\log(2W/\delta)}{2L}},\quad
\epsilon_r=\eta+\lambda N,\quad
E=\frac{\lambda^2N(N-1)}2,\quad
\xi=\frac{4\eta+4E}{\lambda L}.
\tag{1}
\]

If N>=T, use any fixed arm throughout and retain the trivial regret bound
T. Otherwise execute the following schedule, using all observations only
as described below.

1. **Pilot.** Play each arm for L rounds. Its empirical average is
   \(\widehat r_i\in[0,1]\). Choose a reference arm j maximizing
   \(\widehat r_i\), breaking ties by the smallest index.
2. **Calibration.** Play j for two consecutive blocks of L rounds. Let
   their empirical averages be C_0 and C_1, and set \(D_0=C_1-C_0\).
3. **Probe each arm.** For every i=1,...,K, play j for L rounds, then i for
   L rounds, then j for L rounds. Let A_i and B_i be the empirical averages
   in the first and third blocks. Set
   \[
   D_i=B_i-A_i,\qquad d_i=\frac{D_i-D_0}{\lambda L}.
   \tag{2}
   \]
4. If \(\widehat r_j>0\), set
   \[
   \widehat b_i=\operatorname{clip}_{[0,1]}
       \left(1+\frac{d_i}{\widehat r_j}\right).
   \tag{3}
   \]
   If \(\widehat r_j=0\), set every \(\widehat b_i=1\).

There are K pilot blocks, two calibration blocks and 3K probe blocks, for
exactly N rounds. There are W empirical averages in use. The reference
arm is selected once, after the pilot; the remainder of exploration is
then fixed. In particular a zero-reward arm can still be probed through j.

For the remaining H=T-N rounds, compute a near-optimal length-H sequence
under parameters \((\widehat r,\widehat b)\), initial state **one**, and the
known \(\lambda\), with planning loss at most 1/2. Play that sequence. The
true state after exploration is not observed or reset. Section 5 bounds
the cost of using initial state one in the planner.

## 3. Transient identification

### Lemma 1: uniform first-order state expansion

For every action history, every parameter vector in the stated cube, and
every 0<=t<=N,

\[
q_t=1+\lambda\sum_{s<t}(b_{I_s}-1)+e_t,
\qquad 0\le e_t\le \frac{\lambda^2t(t-1)}2\le E.
\tag{4}
\]

**Proof.** Convexity of the update gives q_t in [0,1]. Also
\(1-q_{t+1}\le(1-q_t)+\lambda\), hence \(1-q_t\le\lambda t\).
Subtracting the proposed linear part from the recurrence gives

\[
e_{t+1}-e_t=\lambda(1-q_t).
\]

It follows that e_t>=0 and
\(e_t\le\lambda^2\sum_{s<t}s=\lambda^2t(t-1)/2\). This reasoning is
pathwise, so it remains valid when the chosen reference depends on pilot
observations. No asymptotic approximation was used. □

### Lemma 2: simultaneous concentration and reward estimates

With probability at least 1-delta, every one of the W empirical averages
differs by at most eta from the average of its conditional means, and on
that event

\[
\|\widehat r-r\|_\infty\le\epsilon_r.
\tag{5}
\]

**Proof.** Within each measured block, subtract the conditional mean from
each observation. These are bounded martingale differences with conditional
range length one. The conditional Hoeffding bound gives probability at
most \(2\exp(-2L\eta^2)=\delta/W\) for either-sided deviation exceeding
eta. This also applies to blocks whose identity was selected from past
data. A union bound gives the simultaneous event. Every pilot conditional
mean r_i q_t differs from r_i by at most \(1-q_t\le\lambda N\).
Adding the sampling error proves (5). □

### Lemma 3: the two differences isolate each arm's state effect

On the event of Lemma 2, for every i,

\[
|d_i-r_j(b_i-1)|\le\xi.
\tag{6}
\]

**Proof.** Replace q_t by the linear part of (4) in each conditional reward
mean. This replacement changes a mean in a j-block by at most r_j E<=E,
and a difference between two block averages by at most 2E.

At corresponding offsets in the two adjacent calibration blocks, the
linear state changes by exactly \(\lambda L(b_j-1)\). Thus D_0 differs
from \(\lambda Lr_j(b_j-1)\) by at most \(2\eta+2E\).

For the probe j^L i^L j^L, compare offset k in the first block with offset
k in the third, for each k=0,...,L-1. Between the two times there are
exactly L actions j and L actions i. The linear state difference is
therefore \(\lambda L[(b_j-1)+(b_i-1)]\), independently of k and of the
earlier history. Hence D_i differs from
\(\lambda Lr_j[(b_j-1)+(b_i-1)]\) by at most \(2\eta+2E\).
Subtract and divide by the positive \(\lambda L\). This proves (6).
It also covers i=j without any change. □

### Lemma 4: reward-weighted parameter accuracy

Write \(r_{\max}=\max_i r_i\) and
\(\Delta_b=\max_i|\widehat b_i-b_i|\). On the same event,

\[
r_{\max}\Delta_b\le\xi+4\epsilon_r.
\tag{7}
\]

**Proof.** The choice of reference and (5) imply
\(r_{\max}\le r_j+2\epsilon_r\).
Suppose first that \(\widehat r_j>0\). Projection onto [0,1] cannot increase
the distance to b_i in [0,1]. Therefore (3) and (6) give

\[
\widehat r_j|\widehat b_i-b_i|
 \le |d_i-\widehat r_j(b_i-1)|
 \le\xi+\epsilon_r.
\]

Using \(|\widehat b_i-b_i|\le1\) to replace \(\widehat r_j\) by r_j costs
at most another epsilon_r. Replacing r_j by r_max costs at most
2 epsilon_r. Maximize over i to obtain (7).

If \(\widehat r_j=0\), all empirical pilot averages are zero, so (5) gives
\(r_{\max}\le\epsilon_r\). Since Delta_b<=1, (7) holds as well. There is
no division by a small true reward anywhere in this conclusion. □

## 4. A fully specified planner

The statistical argument is already sufficient with finite exhaustive
sequence optimization. The following grid construction gives an efficient
alternative in the horizon T.

Let M=T^2 and \(G=\{0,1/M,...,1\}\). For g in G and arm i define

\[
F_i(g)=\frac1M\left\lfloor
 M\big((1-\lambda)g+\lambda\widehat b_i\big)\right\rfloor.
\]

Set V_0(g)=0 and recursively, for h=1,...,H,

\[
V_h(g)=\max_i\{\widehat r_i g+V_{h-1}(F_i(g))\}.
\tag{8}
\]

Store a maximizing action with a deterministic tie rule. Start at grid
state one, follow the stored actions and update the internal state with
F_i. This outputs a sequence independent of subsequent reward observations.
The grid state is internal to the planner, not an observed environment state.

**Lemma 5.** The resulting sequence has continuous estimated-model reward
within 1/2 of the best length-H estimated-model sequence from one.

**Proof.** Fix any sequence. Let z_t be its continuous estimated-model
state and g_t its rounded state, both starting from one. Monotonicity and
rounding down imply \(0\le z_t-g_t\le t/M\), by induction. Consequently
the continuous reward exceeds the rounded reward by a number in
\([0,H(H-1)/(2M)]\subset[0,1/2]\).

Equation (8) maximizes the rounded reward over all sequences, including a
continuous-model maximizing sequence. The continuous reward of the grid
optimizer is at least its rounded reward, so it is within 1/2 of the
continuous optimum. □

There are H(M+1) state-time pairs and K choices each, giving O(KT^3)
arithmetic operations. This is an arithmetic-operation claim, not an
assertion of exact finite-bit computation with arbitrary noncomputable
real c. For rational lambda the empirical estimators and this planner can
all be calculated with rational arithmetic. Only the block-length rule
uses elementary scalar rounding.

## 5. Regret against the original full-horizon benchmark

**Lemma 6.** On the simultaneous concentration event,

\[
\operatorname{OPT}_T-
 \sum_{t=0}^{T-1}r_{I_t}q_t
\le N+2T(\xi+5\epsilon_r+\lambda N)+\frac12.
\tag{9}
\]

Here the sum contains conditional expected rewards along the realized
action sequence, not the noisy observations used for estimation.

**Proof.** Every state after N rounds, under either the learner or the
benchmark, lies in \([\max(0,1-\lambda N),1]\). Fix any tail sequence of
length H and compare its true states starting from any such state with its
estimated-model states starting from one. The state update is a contraction,
so induction or the geometric-sum formula gives

\[
|q_{N+t}-\widehat q_t|
 \le (1-\lambda)^t\lambda N
       +(1-(1-\lambda)^t)\Delta_b
 \le\lambda N+\Delta_b.
\]

The one-step reward discrepancy is at most

\[
|r_iq_{N+t}-\widehat r_i\widehat q_t|
 \le\epsilon_r+r_{\max}(\lambda N+\Delta_b)
 \le\xi+5\epsilon_r+\lambda N=:w.
\tag{10}
\]

This holds simultaneously for every tail sequence; in particular the
selected plan and the benchmark tail can depend on the instance or data.
The true benchmark tail is at most its estimated-model reward plus Tw.
The estimated-model optimum is at most the learner's estimated-model
reward plus 1/2 by Lemma 5. The learner's estimated-model reward is at
most its true tail reward plus Tw. Finally the benchmark earns at most N
in the prefix, while the learner's prefix reward is nonnegative. Adding
these comparisons proves (9). Thus the exploration's lasting influence on
the state has been charged, even though no reset occurs. □

The deterministic sum in (9) is between zero and T for every realized
history. Taking expectations and using the failure probability delta gives
the explicit bound

\[
R_T\le N+2T\left[
 \frac{4\eta+4E}{\lambda L}+5\eta+6\lambda N
 \right]+\frac12+\delta T.
\tag{11}
\]

This proof compares to the undiscounted parameter-informed optimal
length-T sequence specified in the question.

## 6. Choice of block length

For T>=2 set delta=T^{-2}, \(\ell_T=\log(2(3K+2)T^2)\), and

\[
L=\left\lceil T^{4/5}\ell_T^{1/5}\right\rceil.
\tag{12}
\]

For fixed K, N=(4K+2)L<T for all sufficiently large T. With lambda=c/T,

\[
\begin{aligned}
N&=O_K(T^{4/5}\ell_T^{1/5}),\\
\eta&=O(T^{-2/5}\ell_T^{2/5}),\\
\frac{\eta}{\lambda L}
 &=O_c(T^{-1/5}\ell_T^{1/5}),\\
\frac{E}{\lambda L}
 &=O_{K,c}(T^{-1/5}\ell_T^{1/5}),\\
\lambda N&=O_{K,c}(T^{-1/5}\ell_T^{1/5}).
\end{aligned}
\]

Substitution in (11) proves the theorem. The finitely many admissible
horizons with N>=T use the stipulated fallback; their regret is at most T
and is absorbed into the constant depending on K,c. The statement is
uniform over all arm parameters, including parameters that vary with T.
The constants are not asserted to be uniform as c tends to zero or infinity,
and K is fixed as in the catalog question.

## 7. Evidence and remaining questions

`check_q964.py` uses exact rational arithmetic to verify the state remainder,
the offset-matching identities, the clipped reward-weighted inequality, and
the grid planner against an independent exhaustive sequence optimizer on
small cases. Those controls exercise boundary rewards, zero reference
estimates, repeated reference arms, and varied histories. They supplement
the all-horizon proof; no stochastic simulation is used as a proof of a
regret rate.

The original source remains the authority for the model and open question.
The dated search log is `SOURCES.md`. Novelty is not certified. The present
argument settles the catalog's known-c/T existence question if correct;
it does not settle optimal regret rates, unknown-lambda guarantees, or
uniform dependence on a growing number of arms.
