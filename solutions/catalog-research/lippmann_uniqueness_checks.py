"""Controls for research/lippmann-uniqueness.md (Baechler 2018, section 4.7 conjecture).

Units: depth z in multiples of the plate thickness Z, so line n sits at
alpha_n = n*pi and the viewing variable is k = 4*pi*Z/lambda'.  The thesis's
discretised operator is Phi[m, n] = H_Z^tau(n Omega_Z, m Omega_s), i.e.

    u(k) = int_0^1 e^{-tau z} (a0 + sum_n p_n 2 rho cos(n pi z + theta)) e^{-j k z} dz,
    a0 = (1 + rho^2) sum_n p_n,   data v(k) = |u(k)|^2.

Checks
  1. closed-form Phi agrees with direct quadrature and with e^s G(s) - K(s);
  2. real r, tau = 0: |u|^2 = 4 sin^2(k/2) E^2 + 4 cos^2(k/2) O^2;
  3. nonnegativity is necessary: a real signed pair with equal data;
  4. the tau > 0 reversal obstruction  G(-2tau) - e^{2tau} K(-2tau) = e^{2tau} int_0^1 h e^{-2tau z};
  5. searches for distinct nonnegative spectra with equal visible-band data;
  6. local conditioning of p -> |Phi p|^2 on the visible band.
Writes lippmann-uniqueness-checks.json next to this file.
"""
import json
import pathlib

import numpy as np
from scipy.integrate import quad
from scipy.optimize import least_squares, minimize

OUT = pathlib.Path(__file__).with_name("lippmann-uniqueness-checks.json")


def phi(ns, ks, rho, theta, tau):
    def e(b):
        b = np.asarray(b, complex)
        small = np.abs(b) < 1e-12
        return np.where(small, 1.0 + 0j, (np.exp(b) - 1) / np.where(small, 1, b))
    k = np.asarray(ks, float)[:, None]
    a = (np.pi * np.asarray(ns, float))[None, :]
    base = (1 + rho**2) * e(-tau - 1j * k)
    osc = rho * (np.exp(1j * theta) * e(-tau + 1j * (a - k)) + np.exp(-1j * theta) * e(-tau - 1j * (a + k)))
    return base + osc


def h_of(z, ns, p, rho, theta):
    return (1 + rho**2) * np.sum(p) + 2 * rho * sum(pn * np.cos(n * np.pi * z + theta) for n, pn in zip(ns, p))


def poles(ns, p, rho, theta):
    """s-plane poles s_i and residues c_i of K(s) = sum c_i/(s - s_i); eps_i = (-1)^n."""
    r = rho * np.exp(1j * theta)
    s, c, eps = [0j], [(1 + rho**2) * np.sum(p) + 0j], [1]
    for n, pn in zip(ns, p):
        s += [-1j * n * np.pi, 1j * n * np.pi]
        c += [r * pn, np.conj(r) * pn]
        eps += [(-1) ** n] * 2
    return np.array(s), np.array(c), np.array(eps)


def KG(sv, ns, p, rho, theta):
    s, c, eps = poles(ns, p, rho, theta)
    d = np.asarray(sv)[:, None] - s[None, :]
    return (c / d).sum(1), (eps * c / d).sum(1)


def visible(zum=5.0, m=300):
    ns = np.arange(int(np.ceil(4 * zum / 0.7)), int(np.floor(4 * zum / 0.39)) + 1)
    lam = np.linspace(0.39, 0.70, m)
    return ns, 4 * np.pi * zum / lam


REGIMES = [
    ("air r=0.2, uniform", 0.2, 0.0, 0.0),
    ("ideal mirror r=-1, uniform", 1.0, np.pi, 0.0),
    ("mercury r=0.71e^{-148deg}, uniform", 0.71, np.deg2rad(-148), 0.0),
    ("air, decay tau=2", 0.2, 0.0, 2.0),
    ("mercury, decay tau=2", 0.71, np.deg2rad(-148), 2.0),
    ("r=0.5e^{60deg}, decay tau=1", 0.5, np.deg2rad(60), 1.0),
]


def check_foundation(rng):
    worst_q, worst_kg = 0.0, 0.0
    for name, rho, th, tau in REGIMES:
        ns = np.array([3, 4, 7])
        p = rng.uniform(0, 1, 3)
        ks = np.linspace(1, 30, 25)
        u = phi(ns, ks, rho, th, tau) @ p
        for k, uk in zip(ks, u):
            f = lambda z, part: part(np.exp(-tau * z) * h_of(z, ns, p, rho, th) * np.exp(-1j * k * z))
            q = quad(f, 0, 1, args=(np.real,), limit=200)[0] + 1j * quad(f, 0, 1, args=(np.imag,), limit=200)[0]
            worst_q = max(worst_q, abs(q - uk) / abs(uk))
        sv = -tau - 1j * ks
        K, G = KG(sv, ns, p, rho, th)
        worst_kg = max(worst_kg, np.max(np.abs(np.exp(sv) * G - K - u) / np.abs(u)))
    return {"closed_form_vs_quadrature_max_rel": worst_q, "eG_minus_K_vs_closed_form_max_rel": worst_kg}


def check_real_split(rng):
    worst = 0.0
    for rho, th in [(0.2, 0.0), (1.0, np.pi), (0.6, 0.0)]:
        ns = np.array([28, 29, 30, 31, 33])
        p = rng.uniform(0, 1, len(ns))
        ks = np.linspace(80, 110, 400) + 1e-3
        v = np.abs(phi(ns, ks, rho, th, 0.0) @ p) ** 2
        b = 2 * rho * np.cos(th)
        a0 = (1 + rho**2) * p.sum()
        E = -a0 / ks + sum(b * pn * ks / ((n * np.pi) ** 2 - ks**2) for n, pn in zip(ns, p) if n % 2 == 0)
        O = sum(b * pn * ks / ((n * np.pi) ** 2 - ks**2) for n, pn in zip(ns, p) if n % 2 == 1)
        pred = 4 * np.sin(ks / 2) ** 2 * E**2 + 4 * np.cos(ks / 2) ** 2 * O**2
        worst = max(worst, np.max(np.abs(pred - v) / v.max()))
    return {"sum_of_squares_identity_max_rel": worst}


def check_signed_pair():
    ns = np.array([29, 30, 31])
    p = np.array([1.0, 2.0, -1.0])          # odd-index sum is zero
    q = np.array([-1.0, 2.0, 1.0])          # odd part flipped
    out = {"p": p.tolist(), "p_prime": q.tolist()}
    ks = np.linspace(0.2, 60 * np.pi, 6000)
    for name, rho, th, tau in [("air uniform", 0.2, 0.0, 0.0), ("ideal mirror uniform", 1.0, np.pi, 0.0),
                               ("mercury uniform (complex r)", 0.71, np.deg2rad(-148), 0.0),
                               ("air with decay", 0.2, 0.0, 2.0)]:
        P = phi(ns, ks, rho, th, tau)
        vp, vq = np.abs(P @ p) ** 2, np.abs(P @ q) ** 2
        out[name] = float(np.max(np.abs(vp - vq)) / vp.max())
    return out


def check_reversal_obstruction(rng):
    worst, min_integral = 0.0, np.inf
    for _ in range(200):
        k = rng.integers(1, 5)
        ns = np.sort(rng.choice(np.arange(1, 40), k, replace=False))
        p = rng.exponential(1, k)
        rho, th, tau = rng.uniform(0.05, 1), rng.uniform(-np.pi, np.pi), rng.uniform(0.05, 4)
        K, G = KG(np.array([-2 * tau + 0j]), ns, p, rho, th)
        lhs = (G[0] - np.exp(2 * tau) * K[0]).real
        integral = quad(lambda z: np.exp(-2 * tau * z) * h_of(z, ns, p, rho, th), 0, 1, limit=400)[0]
        worst = max(worst, abs(lhs - np.exp(2 * tau) * integral) / abs(lhs))
        min_integral = min(min_integral, integral / ((1 - rho) ** 2 * p.sum() + 1e-300))
    return {"identity_max_rel": worst, "cases": 200,
            "min_integral_over_(1-rho)^2_sum_p": min_integral}


def search_random_and_sparse(rng):
    res = {}
    for name, rho, th, tau in REGIMES:
        ns, ks = visible()
        P = phi(ns, ks, rho, th, tau)
        exact, far, conds = 0, 0, []
        for rep in range(8):
            p = np.zeros(len(ns))
            if rep < 4:
                p = rng.uniform(0, 1, len(ns))
            else:
                idx = rng.choice(len(ns), rng.integers(1, 4), replace=False)
                p[idx] = rng.uniform(0.3, 1, len(idx))
            v = np.abs(P @ p) ** 2
            J = 2 * np.real(np.conj(P @ p)[:, None] * P)
            sv = np.linalg.svd(J, compute_uv=False)
            conds.append(sv[0] / sv[-1])
            for t in range(25):
                x0 = rng.uniform(0, 2 * p.max(), len(p))
                r = least_squares(lambda x: (np.abs(P @ x) ** 2 - v) / v.max(), x0, bounds=(0, np.inf),
                                  xtol=1e-14, ftol=1e-14, gtol=1e-14, max_nfev=3000)
                if r.cost < 1e-16:
                    exact += 1
                    if np.linalg.norm(r.x - p) > 1e-4 * np.linalg.norm(p):
                        far += 1
        res[name] = {"exact_fits": exact, "exact_fits_away_from_truth": far,
                     "jacobian_condition_min": float(min(conds)), "jacobian_condition_max": float(max(conds))}
    return res


def search_pairs(rng):
    """Jointly optimise (p, p') >= 0, forced apart, to match wide-band data."""
    res = {}
    for ns in [[3, 4], [3, 4, 5], [4, 5, 6, 7], [2, 4], [2, 4, 6]]:
        ns = np.array(ns)
        ks = np.linspace(0.3, (ns.max() + 4) * np.pi, 400)
        for name, rho, th, tau in REGIMES[:1] + REGIMES[2:3] + REGIMES[4:]:
            P = phi(ns, ks, rho, th, tau)
            N = len(ns)

            def f(x):
                p, q = x[:N] ** 2, x[N:] ** 2
                vp, vq = np.abs(P @ p) ** 2, np.abs(P @ q) ** 2
                d = np.sum((p - q) ** 2) / (p @ p + q @ q)
                return (np.sum((vp - vq) ** 2) / (np.sum(vp**2) + 1e-30)
                        + 10 * max(0, 0.2 - d) ** 2 + (p.sum() + q.sum() - 2) ** 2)
            best = min(minimize(f, rng.normal(size=2 * N), method="BFGS",
                                options={"maxiter": 3000, "gtol": 1e-14}).fun for _ in range(15))
            res[f"{[int(n) for n in ns]} {name}"] = best
    return res


def main():
    rng = np.random.default_rng(20260930)
    out = {
        "foundation": check_foundation(rng),
        "real_r_uniform_split": check_real_split(rng),
        "signed_pair_equal_data_max_rel": check_signed_pair(),
        "reversal_obstruction": check_reversal_obstruction(rng),
        "visible_band_searches": search_random_and_sparse(rng),
        "adversarial_pair_min_objective": search_pairs(rng),
    }
    OUT.write_text(json.dumps(out, indent=1, default=float))
    print(json.dumps(out, indent=1, default=float))


if __name__ == "__main__":
    main()
