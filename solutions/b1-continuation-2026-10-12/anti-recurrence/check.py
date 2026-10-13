#!/usr/bin/env python3
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


def generate(a, n):
    forbidden = set()
    last_b = 0
    ans = []
    for _ in range(n):
        block = []
        while len(block) < len(a):
            last_b += 1
            if last_b not in forbidden:
                block.append(last_b)
        value = sum(c * b for c, b in zip(a, block))
        assert value > last_b and (not ans or value > ans[-1])
        ans.append(value)
        forbidden.add(value)
    return ans


def inspect(a, n=20000):
    tau = sum(a)
    kappa = len(a) * tau + 1
    aa = generate(a, n)
    ds = [v - kappa * (i + 1) for i, v in enumerate(aa)]
    # Does one residue of the parent determine the next tau defects?
    observed = {}
    witness = None
    for j in range(1, n // tau + 1):
        key = aa[j - 1] % kappa
        out = tuple(ds[tau * (j - 1):tau * j])
        if key in observed and observed[key][1] != out:
            witness = {"residue": key, "parent_indices": [observed[key][0], j],
                       "child_defects": [observed[key][1], out]}
            break
        observed[key] = (j, out)
    first_outside = next((i + 1 for i, v in enumerate(aa)
                          if not kappa * i + 1 <= v <= kappa * (i + 1)), None)
    progression_bad = next((j for j in range(n // tau)
                            if aa[tau * j] != aa[0] + tau * kappa * j), None)
    # Kernel prefixes bound states of an LSD-first DFAO, not the source's
    # MSD-first machine. No finite count proves an infinite kernel.
    prefix = 64
    counts = []
    for exponent in range(5):
        step = tau ** exponent
        subseqs = {tuple(ds[r + step * i] for i in range(prefix))
                   for r in range(step) if r + step * (prefix - 1) < n}
        counts.append({"exponent": exponent, "distinct_available_prefixes": len(subseqs)})
    contexts = []
    for radius in range(5):
        known = {}
        bad = None
        for j in range(radius + 1, min(n // tau, n - radius) + 1):
            key = (aa[j - 1] % kappa, tuple(ds[j - 1 - radius:j + radius]))
            out = tuple(ds[tau * (j - 1):tau * j])
            if key in known and known[key][1] != out:
                bad = {"parents": [known[key][0], j], "state": key,
                       "outputs": [known[key][1], out]}
                break
            known[key] = (j, out)
        contexts.append({"radius": radius, "observed_states": len(known),
                         "conflict": bad})
    return {"coefficients": a, "terms": n, "tau": tau, "kappa": kappa,
            "defect_range": [min(ds), max(ds)],
            "first_outside_own_interval": first_outside,
            "first_progression_failure_parent": progression_bad,
            "residue_substitution_counterexample": witness,
            "kernel_prefix_counts": counts, "context_tests": contexts}


if __name__ == "__main__":
    result = [inspect(a) for a in [(1, 1), (1, 2), (2, 1), (1, 3), (1, 4),
                                   (1, 1, 4), (1, 4, 1), (4, 1, 1)]]
    (HERE / "EXPERIMENT.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))
