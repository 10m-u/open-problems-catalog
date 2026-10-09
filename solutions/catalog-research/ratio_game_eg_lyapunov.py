"""Control for research/round3.md (2x2 ratio games, Golowich 2025 Problem 13.4.2).

For random 2x2 ratio games V = <x,Ry>/<x,Sy> with a unique interior equilibrium z* it checks:
  1. V^'(p*) == W'(q*)  (so every interior equilibrium is a centre of H);
  2. H strictly decreases under ONE exact extragradient step from every grid point of the
     sub-level set {H <= 0.9 h_max}, where h_max is the largest level whose orbit stays inside
     the open square and below the saddle level (eta = 2e-3);
  3. extragradient started at the outermost such grid point converges to z* (vectorised run).
Writes ratio-game-eg-lyapunov.json.
"""
import json
import pathlib

import numpy as np
from scipy.optimize import brentq

OUT = pathlib.Path(__file__).with_name("ratio-game-eg-lyapunov.json")


def coeffs(R, S):
    a, b, c, d = R[..., 0, 0], R[..., 0, 1], R[..., 1, 0], R[..., 1, 1]
    n = (d, b - d, c - d, a - b - c + d)
    a, b, c, d = S[..., 0, 0], S[..., 0, 1], S[..., 1, 0], S[..., 1, 1]
    return n, (d, b - d, c - d, a - b - c + d)


def funcs(R, S):
    (n0, n1, n2, n3), (d0, d1, d2, d3) = coeffs(R, S)
    V = lambda p: d0*n2 + d0*n3*p + d1*n2*p + d1*n3*p**2 - d2*n0 - d2*n1*p - d3*n0*p - d3*n1*p**2
    W = lambda q: d0*n1 + d0*n3*q - d1*n0 - d1*n2*q + d2*n1*q + d2*n3*q**2 - d3*n0*q - d3*n2*q**2
    D = lambda p, q: d0 + d1*p + d2*q + d3*p*q
    G = lambda p, q: (-W(q) / D(p, q)**2, V(p) / D(p, q)**2)      # (-f_p, f_q)
    A = lambda p: (d0*n2 - d2*n0)*p + (d0*n3 + d1*n2 - d2*n1 - d3*n0)*p**2/2 + (d1*n3 - d3*n1)*p**3/3
    B = lambda q: (d0*n1 - d1*n0)*q + (d0*n3 - d1*n2 + d2*n1 - d3*n0)*q**2/2 + (d2*n3 - d3*n2)*q**3/3
    return V, W, G, A, B


def main(target=300, eta=2e-3, steps=4000000, seed=21):
    rng = np.random.default_rng(seed)
    t = np.linspace(0, 1, 401)
    P, Q = np.meshgrid(t, t, indexing="ij")
    games, id_fail, increases, grid_points = [], 0, 0, 0
    while len(games) < target:
        R = rng.normal(size=(2, 2)); S = rng.uniform(0.05, 1, size=(2, 2))
        V, W, G, A, B = funcs(R, S)
        gs = np.linspace(0, 1, 4001)
        rp = np.where(V(gs[:-1]) * V(gs[1:]) < 0)[0]; rq = np.where(W(gs[:-1]) * W(gs[1:]) < 0)[0]
        if len(rp) != 1 or len(rq) != 1:
            continue
        ps = brentq(V, gs[rp[0]], gs[rp[0] + 1]); qs = brentq(W, gs[rq[0]], gs[rq[0] + 1])
        h = 1e-6
        dV = (V(ps + h) - V(ps - h)) / (2 * h); dW = (W(qs + h) - W(qs - h)) / (2 * h)
        if abs(dV - dW) > 1e-6 * max(1, abs(dV)):
            id_fail += 1
        s = np.sign(dV)
        H = lambda p, q: s * (A(p) + B(q) - A(ps) - B(qs))
        Hg = H(P, Q)
        hb = min(Hg[0].min(), Hg[-1].min(), Hg[:, 0].min(), Hg[:, -1].min())
        gp, gq = G(P, Q); speed = np.hypot(gp, gq)
        crit = (speed < 1e-3 * speed.max()) & (np.hypot(P - ps, Q - qs) > 0.02)
        hmax = min(hb, Hg[crit].min() if crit.any() else np.inf)
        if hmax <= 1e-8:
            continue
        mask = (Hg <= 0.9 * hmax) & (Hg > 1e-12)
        p0, q0 = P[mask], Q[mask]
        a, b = G(p0, q0); a, b = G(p0 + eta * a, q0 + eta * b)
        dH = H(p0 + eta * a, q0 + eta * b) - H(p0, q0)
        increases += int(np.sum(dH >= 0)); grid_points += int(mask.sum())
        i = np.argmax(np.where(mask, Hg, -1))
        games.append((R, S, P.flat[i], Q.flat[i], ps, qs))
    Rs = np.array([g[0] for g in games]); Ss = np.array([g[1] for g in games])
    p = np.array([g[2] for g in games]); q = np.array([g[3] for g in games])
    ps = np.array([g[4] for g in games]); qs = np.array([g[5] for g in games])
    _, _, Gv, _, _ = funcs(Rs, Ss)
    d0 = np.hypot(p - ps, q - qs)
    checkpoints = []
    for it in range(steps):
        a, b = Gv(p, q); a, b = Gv(p + eta * a, q + eta * b); p, q = p + eta * a, q + eta * b
        if (it + 1) % (steps // 4) == 0:
            checkpoints.append(float(np.max(np.hypot(p - ps, q - qs))))
    dist = np.hypot(p - ps, q - qs)
    out = {"games": len(games), "equilibria_with_Vprime_ne_Wprime": id_fail,
           "grid_points_checked": grid_points, "grid_points_with_H_not_decreasing": increases,
           "eta": eta, "steps": steps, "initial_distance_median": float(np.median(d0)),
           "max_distance_at_quarter_checkpoints": checkpoints, "final_distance_max": float(dist.max()), "converged_within_1e-4": int(np.sum(dist < 1e-4))}
    OUT.write_text(json.dumps(out, indent=1))
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
