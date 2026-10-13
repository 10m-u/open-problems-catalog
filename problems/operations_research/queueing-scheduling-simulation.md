# Queueing, Scheduling & Simulation

6 problems: 6 open.

[All subjects](../README.md) · [Index by number](../INDEX.md)

| Q | Title | Status |
|---|---|---|
| [Q345](queueing-scheduling-simulation.md#q345) | Consider N unit-speed servers with processor sharing: a server divides its capac… | Open |
| [Q654](queueing-scheduling-simulation.md#q654) | Can expiring computation opportunities beat the LP barrier? | Open |
| [Q657](queueing-scheduling-simulation.md#q657) | Variance-independent sublinear-machine approximation for general jobs | Open |
| [Q3094](queueing-scheduling-simulation.md#q3094) | Uniqueness of the overloaded zero-initial-state reneging fluid model | Open |
| [Q3095](queueing-scheduling-simulation.md#q3095) | Asymptotic optimality of GRAND(0) packing | Open |
| [Q4762](queueing-scheduling-simulation.md#q4762) | Does d≤5m/6 always guarantee such an assignment and valid schedule? | Open |

<a id="q345"></a>

## Q345. Consider N unit-speed servers with processor sharing: a server divides its capac…

**Status:** Open · **Kind:** conjecture (Conjecture 4.2) · **Collection** 4

Consider N unit-speed servers with processor sharing: a server divides its capacity equally among its unfinished replicas. Jobs arrive as a Poisson process of rate λ. Each job independently chooses d distinct servers uniformly, 1 ≤ d ≤ N, and places one replica at each. Its service requirements (X₁,…,X_d) have an arbitrary fixed joint distribution, with identical nonnegative marginals X satisfying 0 < E[X] < ∞; vectors are independent across jobs and independent of arrivals and assignments. Replicas are cancelled immediately when the first finishes. Does λ d E[min(X₁,…,X_d)] < N imply stability of the stochastic system, i.e. positive recurrence of the full queueing state process (including service requirements or attained service), rather than merely stability of its fluid model? For nonexchangeable replica laws, assign replica labels uniformly to the selected servers.

**Context.** Discovery path (lateral/sibling branch; student → supervisor):
Jakob Dalsgaard Thøstesen → Jevgenijs Ivanovs: https://data.math.au.dk/publications/phd/2023/math-phd-2023-jdt.pdf
Jevgenijs Ivanovs → Onno J. Boxma: https://pure.uva.nl/ws/files/1408093/94456_0_Thesis.pdf
Youri Raaijmakers → Onno J. Boxma: https://pure.tue.nl/ws/portalfiles/portal/189589319/20211201_Raaijmakers_hf.pdf Origin: Joint doctoral research with Borst and Boxma, presented in 2020 and published in 2021. Thesis Conjecture 4.2 isolates stochastic stability beyond their proved fluid-limit result.

**Source.** Youri Raaijmakers. *Job-Replication Trade-Offs: Performance Analysis of Redundancy Systems*. Eindhoven University of Technology, 2021. Advisor(s): Sem C. Borst; Onno J. Boxma. [primary source](https://pure.tue.nl/ws/portalfiles/portal/189589319/20211201_Raaijmakers_hf.pdf) · [record](https://research.tue.nl/en/publications/job-replication-trade-offs-performance-analysis-of-redundancy-sys/) Location: Conjecture 4.2, §4.3.6, printed p. 81; model §4.2 p. 65; fluid-limit/stochastic distinction pp. 64–65 and 80–81.

**Further links.** [1](https://data.math.au.dk/publications/phd/2023/math-phd-2023-jdt.pdf) · [2](https://pure.uva.nl/ws/files/1408093/94456_0_Thesis.pdf) · [3](https://doi.org/10.1016/j.peva.2021.102195) · [4](https://arxiv.org/abs/2103.10942) · [5](https://arxiv.org/abs/2401.07713) · [6](https://arxiv.org/html/2206.10164v2)


<a id="q654"></a>

## Q654. Can expiring computation opportunities beat the LP barrier?

**Status:** Open · **Kind:** open problem · **Collection** 7

All n options are initially available. Option j has known value v_j>0 and mutually independent integer processing/expiration times S_j,E_j with known laws. One processor selects an available option, runs it nonpreemptively, earns v_j and may repeat; a started option cannot expire. Can a polynomial-time adaptive policy beat ratio 1−1/e against the optimal nonanticipating policy, or is that a computational barrier? Use the explicitly bounded time-support input model, without claiming strong polynomiality in a binary-encoded horizon.

**Context.** Attribution: §6 asks to surpass the LP barrier using stronger methods.

**Source.** Yihua Xu; Rohan Ghuge; Sebastian Perez-Salazar. *Sequential Selection with Expirations*. 2026. [primary source](https://arxiv.org/pdf/2406.15691v2) Location: §3.3; §6, pp. 21–22.

**Literature check.** Status for question 654, checked 5 October 2026: February 2026 version retains the target; no later resolution located.


<a id="q657"></a>

## Q657. Variance-independent sublinear-machine approximation for general jobs

**Status:** Open · **Kind:** open problem · **Collection** 7

For n independent nonnegative jobs on m identical machines with known finite-support processing laws, can a polynomial-time adaptive approximation to minimum E[Σ\_j C_j] have sublinear m dependence independent of processing-time variances? Jobs are nonpreemptive, reveal duration through execution, and must all finish. Extend the Bernoulli Õ(√m) guarantee to general laws, displaying any polylog(n) factors explicitly; such factors must not be mistaken for a uniform o(m) ratio.

**Context.** Doctoral connection: Rudy Zhou; dissertation and supervision listed under question 655. Attribution: The joint SODA paper and Zhou’s thesis explicitly identify this extension.

**Source.** Anupam Gupta; Benjamin Moseley; Rudy Zhou. *Minimizing Completion Times for Stochastic Jobs via Batched Free Times*. 2023. [primary source](https://arxiv.org/pdf/2208.13696) Location: §5, p. 22; thesis §5.5, pp. 99–100.

**Literature check.** Status for question 657, checked 5 October 2026: Later Bernoulli approximations and value-hardness results do not resolve general-law approximation.

**Further links.** [1](https://arxiv.org/abs/2208.13696) · [2](https://arxiv.org/abs/2505.03349) · [3](https://arxiv.org/abs/2601.17425)


<a id="q3094"></a>

## Q3094. Uniqueness of the overloaded zero-initial-state reneging fluid model

**Status:** Open · **Kind:** open problem · **Collection** 31

Is there exactly one such path for every allowed parameter choice?

**Context.** Origin for question 3094: Unresolved exceptional case identified in the thesis and retained in the 2025 joint journal paper. Setup for question 3094: Fix integers J≥2,K≥1, α\_j,μ\_j>0, p_j∈(0,1), ∑p_j=1, and probability measures θ\_j on [0,∞) with θ\_j({0})=0. Assume ρ=∑α\_j/(Kμ\_j)>1. Seek weakly continuous finite nonnegative measure paths ζ\_j(t), initially zero, with ζ\_j(t)({0})=0 and L(t)=∑(p_j/μ\_j)ζ\_j(t)([0,∞))>0 for t>0, satisfying, for every f∈C_b¹([0,∞)) with f(0)=0, ⟨f,ζ\_j(t)⟩=−∫₀ᵗ⟨f′,ζ\_j(s)⟩ds−Kp_j∫₀ᵗ⟨f,ζ\_j(s)⟩/L(s)ds+α\_jt⟨f,θ\_j⟩.

**Source.** Eva Horne Loeser. *Fluid Limit for a Multi-Server, Multiclass Random Order of Service Queue with Reneging and Tracking of Residual Patience Times*. 2024. Advisor(s): Ruth Williams. [primary source](https://escholarship.org/uc/item/7j032606) Location: Definitions 3.0.1,4.0.1; p. 22 exceptional case; Theorem 5.1.1.

**Literature check.** Status for question 3094, checked 8 October 2026: Zero-initial overloaded case remains excepted in the checked 2025–2026 sources.


<a id="q3095"></a>

## Q3095. Asymptotic optimality of GRAND(0) packing

**Status:** Open · **Kind:** conjecture (Conjecture 10) · **Collection** 31

Does dist(x^r,X\*) converge in probability to zero as r→∞?

**Context.** Origin for question 3095: Original 2015 conjecture explicitly retained in the 2025 ranked-server paper. Setup for question 3095: Fix I≥1 and a finite coordinatewise downward-closed set K̄⊂Z_+^I containing 0,e₁,…,e_I; set K=K̄\\{0}. Type-i arrivals are independent Poisson of rate rλ\_i; independent service times are Exp(μ\_i), with λ\_i,μ\_i>0 and ∑λ\_i/μ\_i=1. Infinitely many servers allow configurations in K̄. An arrival chooses uniformly among occupied servers that can accommodate it, opening a new server only if none can; no migration occurs. In stationarity x_k^r is the number of servers in configuration k divided by r. Let X\* minimize ∑\_K x_k over x≥0 with ∑\_K k_i x_k=λ\_i/μ\_i for every i.

**Source.** Alexander L. Stolyar; Yuan Zhong. *Asymptotic optimality of a greedy randomized algorithm in a large-scale service system with general packing constraints*. 2015. [primary source](https://arxiv.org/abs/1306.4991) Location: Conjecture 10, p. 22; retained in Stolyar (2025), §7,p. 22.

**Literature check.** Status for question 3095, checked 8 October 2026: Explicitly retained in Stolyar’s 2025 ranked-server paper.


<a id="q4762"></a>

## Q4762. Does d≤5m/6 always guarantee such an assignment and valid schedule?

**Status:** Open · **Kind:** conjecture (Conjecture 8.1.1) · **Collection** 48

Does d≤5m/6 always guarantee such an assignment and valid schedule?

**Context.** Benjamin Mark Smith: Liverpool PhD2025; primary supervisor Sebastian Wild, secondary supervisor Leszek Gąsieniec. Setup: For integers m,k≥1 and positive integer deadlines f₁,…,f_k, permanently assign each of k tasks to one of m workers. On each day 0,1,2,…, every worker executes at most one assigned task. A valid infinite schedule executes task i at least once in every block of f_i consecutive days. Put d=Σᵢ1/f_i. Audited provenance and status: Subject: Discrete scheduling Periodic Scheduling: Pinwheels, Pareto Surfaces, and Polycules (and Powersort), August2025; thesis Conjecture8.1.1 p141, definitions pp18–20. Checked12October2026: no matching resolution located; finite-visits and single-worker results have different scope. Agarwal2609.10641v2,11September2026, Theorem1: polyamorous heat approximation4G\*; no fixed-partition bin-density result. https://arxiv.org/abs/2609.10641 Kawamura2606.27104v2,10August2026, Theorems1–2: single-worker density and two-period results. PNAS accepted version read; publisher final unread. https://arxiv.org/abs/2606.27104 https://doi.org/10.1073/pnas.2530214123 https://www.kurims.kyoto-u.ac.jp/~kawamura/pinwheel/ Publisher abstract read: online7August2026, issue11August2026; one-task-per-day scope. August10 accepted-version cover binds identical theorem numbering; full final body unread. https://www.pnas.org/doi/10.1073/pnas.2530214123 Kawamura proves the m=1 case; the all-m fixed-partition question remains the selected target.

**Source.** Benjamin Mark Smith. *Periodic Scheduling: Pinwheels, Pareto Surfaces, and Polycules (and Powersort)*. University of Liverpool, 2025. Advisor(s): Sebastian Wild; Leszek Gąsieniec. [primary source](https://livrepository.liverpool.ac.uk/3194461/) Location: Thesis Conjecture 8.1.1, p.141; definitions pp.18–20.

**Literature check.** Status: Checked12October2026: no matching resolution located; finite-visits and single-worker results have different scope.

**Further links.** [1](https://livrepository.liverpool.ac.uk/3194461/1/201381305_Aug2025.pdf) · [2](https://www.wild-inter.net/cv.html) · [3](https://arxiv.org/abs/2411.06292) · [4](https://livrepository.liverpool.ac.uk/3186293/1/SOSA%20-%20paper%20126.pdf) · [5](https://epubs.siam.org/doi/10.1137/1.9781611978315.23) · [6](https://arxiv.org/abs/2609.10641) · [7](https://arxiv.org/abs/2606.27104) · [8](https://doi.org/10.1073/pnas.2530214123) · [9](https://www.kurims.kyoto-u.ac.jp/~kawamura/pinwheel/) · [10](https://www.pnas.org/doi/10.1073/pnas.2530214123)

