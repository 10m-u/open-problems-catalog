"""Exact-arithmetic reference implementation for the Q964 exploration/planner.

The environment supplies pull(arm), a single Bernoulli observation. It owns
the latent state; the learner never reads that state. Arm indices are zero-based.
The polynomial planner is for reproducibility, not large-horizon performance.
"""

from fractions import Fraction
from math import ceil, log


def clip(value):
    return min(Fraction(1), max(Fraction(0), value))


def block_length(k, horizon):
    if k < 1 or horizon < 2:
        raise ValueError("k >= 1 and horizon >= 2 are required")
    # Floating evaluation only chooses an integer exploration budget. The
    # analysis permits any such budget and does not rely on exact rounding.
    return ceil(horizon ** 0.8 * log(2 * (3 * k + 2) * horizon**2) ** 0.2)


def estimates_from_averages(pilots, calibration, probes, lam, length):
    lam = Fraction(lam)
    if not pilots or not 0 < lam <= 1 or length < 1:
        raise ValueError("nonempty pilots, 0 < lambda <= 1, and L >= 1 required")
    if len(probes) != len(pilots):
        raise ValueError("one probe pair is required per arm")
    rhat = tuple(Fraction(v) for v in pilots)
    if any(not 0 <= value <= 1 for value in rhat):
        raise ValueError("pilot averages must lie in [0, 1]")
    reference = max(range(len(rhat)), key=lambda i: rhat[i])
    d0 = Fraction(calibration[1]) - Fraction(calibration[0])
    effects = tuple(
        (Fraction(after) - Fraction(before) - d0) / (lam * length)
        for before, after in probes
    )
    bhat = tuple(
        clip(1 + value / rhat[reference]) if rhat[reference] else Fraction(1)
        for value in effects
    )
    return {
        "rhat": rhat,
        "bhat": bhat,
        "reference": reference,
        "effects": effects,
        "observations_used": (4 * len(rhat) + 2) * length,
    }


def explore(k, length, lam, pull):
    """Use exactly (4*k+2)*length calls to pull, with no state observations."""
    if k < 1 or length < 1 or not 0 < lam <= 1:
        raise ValueError("invalid exploration parameters")

    def average(arm):
        total = 0
        for _ in range(length):
            observed = pull(arm)
            if observed not in (0, 1):
                raise ValueError("pull must return a Bernoulli observation")
            total += observed
        return Fraction(total, length)

    pilots = [average(i) for i in range(k)]
    j = max(range(k), key=lambda i: pilots[i])
    calibration = [average(j), average(j)]
    probes = []
    for i in range(k):
        before = average(j)
        average(i)  # Excitation observations are not used by this estimator.
        after = average(j)
        probes.append((before, after))
    return estimates_from_averages(pilots, calibration, probes, lam, length)


def grid_plan(rhat, bhat, lam, horizon, grid_size):
    """Return an optimal rounded-model sequence from internal state one.

    The continuous-model suboptimality is <= H*(H-1)/(2*grid_size).
    The theorem uses grid_size=T**2 for remaining horizon H<=T.
    """
    rhat, bhat = tuple(map(Fraction, rhat)), tuple(map(Fraction, bhat))
    lam = Fraction(lam)
    if not rhat or len(rhat) != len(bhat) or horizon < 0 or grid_size < 1:
        raise ValueError("invalid planner dimensions")
    if not 0 <= lam <= 1 or any(not 0 <= x <= 1 for x in rhat + bhat):
        raise ValueError("all model parameters must be in [0, 1]")
    k = len(rhat)
    grid = [Fraction(g, grid_size) for g in range(grid_size + 1)]
    transitions = [
        [int(grid_size * ((1 - lam) * g + lam * bhat[i])) for i in range(k)]
        for g in grid
    ]
    values = [Fraction(0)] * (grid_size + 1)
    policies = []
    for _ in range(horizon):
        new_values, actions = [], []
        for index, g in enumerate(grid):
            choices = [
                rhat[i] * g + values[transitions[index][i]] for i in range(k)
            ]
            action = max(range(k), key=lambda i: choices[i])
            new_values.append(choices[action])
            actions.append(action)
        policies.append(actions)
        values = new_values
    state = grid_size
    sequence = []
    for remaining in range(horizon, 0, -1):
        action = policies[remaining - 1][state]
        sequence.append(action)
        state = transitions[state][action]
    return tuple(sequence), values[grid_size]


def run_policy(k, horizon, c, pull):
    """Execute the theorem's policy; returns its action sequence and estimates.

    Exact rational c is supported. The O(K*T**3) reference planner can be
    expensive; no hidden-state observation or reward reset is performed.
    """
    c = Fraction(c)
    if k < 1 or horizon < 1 or not 0 < c <= horizon:
        raise ValueError("k,T >= 1 and 0 < c <= T required")
    lam = c / horizon
    length = block_length(k, horizon) if horizon >= 2 else 1
    actions = []

    def logged_pull(arm):
        actions.append(arm)
        return pull(arm)

    budget = (4 * k + 2) * length
    if budget >= horizon:
        for _ in range(horizon):
            logged_pull(0)
        return tuple(actions), None
    estimates = explore(k, length, lam, logged_pull)
    tail, _ = grid_plan(
        estimates["rhat"], estimates["bhat"], lam,
        horizon - budget, horizon**2,
    )
    for arm in tail:
        logged_pull(arm)
    return tuple(actions), estimates
