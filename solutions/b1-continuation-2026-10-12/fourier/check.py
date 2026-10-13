#!/usr/bin/env python3
"""Direct Fourier checks and bounded, uncertified entropy optimization."""
from pathlib import Path
import json
import numpy as np
from scipy.optimize import minimize

HERE = Path(__file__).resolve().parent


def matrix(w):
    p = 1 << w
    x = np.arange(p)
    f = np.exp(2j * np.pi * x[:, None] * x[None, :] / p) / np.sqrt(p)
    h = np.array([[(-1) ** ((int(b) & int(z)).bit_count() % 2)
                   for z in x] for b in x]) / np.sqrt(p)
    return h @ f


def entropy(z):
    p = np.abs(z) ** 2
    return float(-np.sum(p[p > 0] * np.log2(p[p > 0])))


def objective(raw, u):
    n = len(raw) // 2
    zraw = raw[:n] + 1j * raw[n:]
    norm = np.linalg.norm(zraw)
    z = zraw / norm
    y = u @ z
    value = entropy(z) + entropy(y)
    def gradient(v):
        p = np.abs(v) ** 2
        return -2 * v * (np.log(np.maximum(p, 1e-300)) + 1) / np.log(2)
    g = gradient(z) + u.conj().T @ gradient(y)
    g = (g - z * np.real(np.vdot(z, g))) / norm
    return value, np.r_[g.real, g.imag]


def run():
    checks = []
    for w in range(1, 9):
        m = matrix(w)
        z = np.abs(m.T)
        zero = int(np.sum(z < 1e-11))
        assert zero == (2 * ((1 << (2 * w)) - 1)) // 3
        fourth = float(np.mean(z ** 4))
        assert np.isclose(fourth, (4 / 3) * (3 / 8) ** w, atol=1e-14)
        law = [1.]
        for size in range(w):
            for d in range(1, 1 << (size + 1), 2):
                for mask in range(1 << size):
                    val = 1.
                    for j in range(2, size + 2):
                        angle = np.pi * d / (1 << j)
                        val *= abs(np.sin(angle) if (mask >> (j - 2)) & 1
                                   else np.cos(angle))
                    law.append(val)
        assert np.allclose(sorted(law), sorted(z[z > 1e-11]), atol=1e-11)
        checks.append({"width": w, "entries": z.size, "zeros": zero,
                       "fourth_moment": fourth, "exact_mixture_verified": True})
    allones = []
    for w in range(1, 20):
        a = np.arange(1, 1 << w, 2, dtype=float)
        val = np.ones_like(a)
        for j in range(1, w + 1):
            val *= np.abs(np.sin(np.pi * a / (1 << j)))
        predicted = np.prod([np.sin(np.pi * (1/3 + (-1)**(j-1)/(3*(1 << j))))
                             for j in range(1, w + 1)])
        assert np.isclose(np.max(val), predicted, rtol=1e-10, atol=1e-12)
        allones.append({"width": w, "odd_frequencies": len(a),
                        "maximum": float(predicted)})
    rng = np.random.default_rng(20261012)
    opt = []
    for t in range(1, 5):
        w = t + 1
        m = matrix(w)
        rows = np.arange(1 << t, 1 << (t + 1))
        cols = np.arange(1, 1 << (t + 1), 2)
        u = m[np.ix_(rows, cols)]
        assert np.allclose(u.conj().T @ u, np.eye(1 << t), atol=1e-12)
        coherence = 1 / ((1 << t) * np.sin(np.pi / (1 << (t + 1))))
        assert np.isclose(np.max(np.abs(u)), coherence)
        if t == 2:
            analytic = np.array([np.cos(np.pi / 16), 0,
                                 1j * np.sin(np.pi / 16), 0])
            p = np.sin(np.pi / 16) ** 2
            assert np.allclose(sorted(np.abs(u @ analytic) ** 2),
                               sorted([p / 2, p / 2, (1-p) / 2, (1-p) / 2]))
        starts = [np.r_[np.eye(1 << t)[0], np.zeros(1 << t)]]
        starts += [rng.normal(size=2 << t) for _ in range(8)]
        best = None
        for initial in starts:
            result = minimize(objective, initial, args=(u,), jac=True,
                              method="L-BFGS-B",
                              options={"maxiter": 1200, "ftol": 1e-13,
                                       "gtol": 1e-9})
            if best is None or result.fun < best.fun:
                best = result
        z = best.x[:1 << t] + 1j * best.x[1 << t:]
        z /= np.linalg.norm(z)
        opt.append({"t": t, "block_dimension": 1 << t, "restarts": len(starts),
                    "upper_bound": float(objective(best.x, u)[0]),
                    "coherence_lower_bound": float(-2 * np.log2(coherence)),
                    "candidate_real": z.real.tolist(), "candidate_imag": z.imag.tolist(),
                    "global_optimum_certified": False})
    result = {"distribution_checks": checks, "allones_checks": allones,
              "entropy_block_optimization": opt}
    (HERE / "VALIDATION.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"distribution_entries": sum(c["entries"] for c in checks),
                      "allones_widths": len(allones), "entropy": [
                          {k: r[k] for k in ("t", "upper_bound", "coherence_lower_bound")}
                          for r in opt]}))


if __name__ == "__main__":
    run()
