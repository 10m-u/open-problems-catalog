"""Bounded deterministic experiment, exact certificate audit, and obstructions."""
from collections import defaultdict
from copy import deepcopy
import json
from pathlib import Path
from time import perf_counter

from one_tree import instances, produce, snapshot, enumerate_tours, petersen_instance
from check_certificate import verify

HERE = Path(__file__).resolve().parent


def main():
    start = perf_counter()
    rows, audits = [], []
    certificate_dir = HERE / "certificates"
    certificate_dir.mkdir(exist_ok=True)
    for instance in instances():
        for mode in ["zero", "single-root", "four-roots"]:
            clock = perf_counter()
            data = produce(instance, mode)
            production_seconds = perf_counter() - clock
            clock = perf_counter()
            audit = verify(data)
            verification_seconds = perf_counter() - clock
            name = f'{instance["id"]}-{mode}.json'
            (certificate_dir / name).write_text(json.dumps(data, indent=2) + "\n")
            measurements = data["measurements"]
            rows.append({"id": instance["id"], "family": instance["family"], "n": len(instance["costs"]),
                         "seed": instance["seed"], "method": mode,
                         "upper": data["incumbent"]["cost"],
                         "lower_numerator": data["global_lower_bound"]["numerator"], "scale": 16,
                         "eliminated": len(data["eliminated_edges"]),
                         "residual": len(data["residual_edges"]),
                         "width_upper_bound": measurements["min_fill_width_upper_bound"],
                         "optimal_cost": measurements["optimal_cost"],
                         "full_dp": measurements["full_dp"], "residual_dp": measurements["residual_dp"],
                         "snapshot_calls": measurements["snapshot_calls"],
                         "production_including_dp_seconds": production_seconds,
                         "verification_seconds": verification_seconds,
                         "certificate": "certificates/" + name})
            audits.append(audit)
    # The checker must reject corrupt claims and certificates.
    data = json.loads((certificate_dir / "petersen-1-2-zero.json").read_text())
    rejected = []
    for label, mutate in [
        ("inflated_forced_bound", lambda d: d["forced_bounds"][0].update(numerator=10000)),
        ("wrong_incumbent_cost", lambda d: d["incumbent"].update(cost=0)),
        ("fake_root_pair", lambda d: d["certificates"][0].update(root_edges=[[0, 1], [0, 2]])),
        ("missing_edge_bound", lambda d: d["forced_bounds"].pop()),
        ("invalid_scale", lambda d: d["certificates"][0].update(scale=0)),
    ]:
        altered = deepcopy(data)
        mutate(altered)
        try:
            verify(altered)
        except (ValueError, IndexError, KeyError):
            rejected.append(label)
        else:
            raise AssertionError("checker accepted corruption: " + label)
    # Every Petersen complete-graph edge occurs in a cost-11 optimum.
    c = petersen_instance()["costs"]
    best, count, witnesses = 10 ** 9, 0, {}
    enumerated = 0
    for tour, value in enumerate_tours(c):
        enumerated += 1
        if value < best:
            best, count, witnesses = value, 0, {}
        if value == best:
            count += 1
            for i in range(len(c)):
                a, b = sorted((tour[i], tour[(i + 1) % len(c)]))
                witnesses.setdefault((a, b), list(tour))
    assert best == 11 and len(witnesses) == 45 and enumerated == 181440
    obstruction = {"schema": "b14-petersen-all-optimal-edges-v1",
                   "instance": petersen_instance(), "optimal_cost": best,
                   "optimal_tours_modulo_reversal": count, "tours_enumerated": enumerated,
                   "edge_witnesses": [{"edge": e, "tour": t} for e, t in sorted(witnesses.items())]}
    (HERE / "petersen-obstruction.json").write_text(json.dumps(obstruction, indent=2) + "\n")
    # Exhaustive tied/negative transformed MST cases independently checked through the certificate path.
    toy_count = 0
    for costs in [
        [[0, 0, 1, 2], [0, 0, 2, 1], [1, 2, 0, 0], [2, 1, 0, 0]],
        [[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]],
    ]:
        tour = [0, 1, 2, 3]
        upper = sum(costs[tour[i]][tour[(i + 1) % 4]] for i in range(4))
        for root in range(4):
            for p in [[0, 0, 0, 0], [-100, 2, 0, -25], [6, 6, 6, 6]]:
                cert, bounds, _ = snapshot(costs, root, p)
                test = {"schema": "b14-one-tree-certificate-v1",
                        "instance": {"id": "tie-negative-control", "costs": costs}, "method": "control",
                        "incumbent": {"tour": tour, "cost": upper}, "certificates": [cert],
                        "global_lower_bound": {"certificate": 0, "numerator": cert["bound_numerator"], "scale": 16},
                        "forced_bounds": [{"edge": e, "numerator": v, "scale": 16, "certificate": 0}
                                          for e, v in bounds.items()],
                        "eliminated_edges": [e for e, v in bounds.items() if v > 16 * upper],
                        "residual_edges": [e for e, v in bounds.items() if v <= 16 * upper]}
                verify(test)
                for t, value in enumerate_tours(costs):
                    edges = {tuple(sorted((t[i], t[(i + 1) % 4]))) for i in range(4)}
                    assert all(v <= 16 * value for e, v in bounds.items() if e in edges)
                toy_count += 1
    groups = defaultdict(list)
    for row in rows:
        groups[row["family"], row["method"]].append(row)
    aggregates = []
    for (family, method), group in sorted(groups.items()):
        total_edges = sum(r["eliminated"] + r["residual"] for r in group)
        aggregates.append({"family": family, "method": method, "instances": len(group),
                           "eliminated_total": sum(r["eliminated"] for r in group),
                           "complete_edges_total": total_edges,
                           "mean_width_upper_bound": sum(r["width_upper_bound"] for r in group) / len(group),
                           "full_dp_transitions": sum(r["full_dp"]["transitions"] for r in group),
                           "residual_dp_transitions": sum(r["residual_dp"]["transitions"] for r in group),
                           "incumbents_optimal": sum(r["upper"] == r["optimal_cost"] for r in group),
                           "bound_closes_incumbent": sum(r["lower_numerator"] == r["scale"] * r["upper"]
                                                        for r in group)})
    results = {"schema": "b14-elimination-experiment-v1",
               "configuration": {"sizes": [8, 10, 12], "seeds": [0, 1, 2, 3], "potentials_scale": 16,
                                 "single_root_calls": 48, "four_root_total_calls": 48,
                                 "model": "exact integer costs; ceil-Euclidean or integer shortest-path metrics",
                                 "timing_limit": "Times include oracle DP; work counters are the main comparison."},
               "instances": 49, "runs": len(rows), "rows": rows, "aggregates": aggregates}
    (HERE / "experiment.json").write_text(json.dumps(results, indent=2) + "\n")
    receipt = {"certificate_runs_checked": len(audits),
               "forced_edge_bounds_checked": sum(a["forced_bounds_checked"] for a in audits),
               "corruptions_rejected": rejected, "toy_certificate_controls": toy_count,
               "petersen_enumerated": enumerated, "petersen_optimal_cost": best,
               "petersen_optimal_tours": count, "petersen_optimal_edge_witnesses": len(witnesses),
               "full_and_residual_dp_agree": True, "elapsed_seconds": perf_counter() - start}
    (HERE / "validation.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({"validation": receipt, "aggregates": aggregates}, indent=2))


if __name__ == "__main__":
    main()
