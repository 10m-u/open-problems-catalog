"""Controls for research/quick-closures.md, section 1 (Ahmadi 2008, Conjecture 5.2.1).

For a 2x2 Hurwitz A put V1 = A + A^T, V2 = A^2 + 2A^T A + A^T^2,
V3 = A^3 + 3A^T A^2 + 3A^T^2 A + A^T^3 (so x^T Vk x = d^k/dt^k |e^{At}x|^2 at t=0)
and M(t1, t2) = t2 V3 + t1 V2 + V1.  The note's explicit choice of (t1, t2):

  complex eigenvalues  (disc < 0):  t2 = 1/(4 det A),  t1 = -tr A/(2 det A)
  real distinct        (disc > 0):  t2 = 1/tr(A)^2,    t1 = -2/tr A
  Jordan block         (disc = 0, A != lam I): t2 = 1/tr(A)^2 + eps, t1 = -2/tr A
  scalar A = lam I:    t1 = t2 = 0

Checks
  1. symbolic identity in the complex case: M = p(tr A) (I + B^T B / w^2)/2;
  2. exact rational negativity on sampled rational A of every type;
  3. numerical negativity on 200k random Hurwitz A (incl. near-degenerate);
  4. exact certificates that the n = 3 analogue (nonnegative coefficients on
     derivatives 2..4, i.e. any Hurwitz co-system) fails.
Writes ahmadi-lyapunov-checks.json.
"""
import json
import pathlib

import numpy as np
import sympy as sp

OUT = pathlib.Path(__file__).with_name("ahmadi-lyapunov-checks.json")


def vmats(A):
    V = [A.T * 0 + sp.eye(A.shape[0]) if isinstance(A, sp.Matrix) else np.eye(A.shape[0])]
    for _ in range(3):
        V.append(A.T @ V[-1] + V[-1] @ A if not isinstance(A, sp.Matrix) else A.T * V[-1] + V[-1] * A)
    return V


def taus(tr, det, disc, scalar=False, eps=0):
    if scalar:
        return 0, 0
    if disc < 0:
        return -tr / (2 * det), 1 / (4 * det)
    return -2 / tr, 1 / tr**2 + (eps if disc == 0 else 0)


def symbolic_complex_identity():
    a, b, c, d = sp.symbols('a b c d', real=True)
    A = sp.Matrix([[a, b], [c, d]])
    tr, det = A.trace(), A.det()
    V = vmats(A)
    t1, t2 = -tr / (2 * det), 1 / (4 * det)
    M = t2 * V[3] + t1 * V[2] + V[1]
    s = sp.symbols('s')
    p = s * (t2 * s**2 + t1 * s + 1)
    mu = tr / 2
    B = A - mu * sp.eye(2)
    w2 = det - mu**2
    Q = (sp.eye(2) + B.T * B / w2) / 2
    diff = (M - p.subs(s, tr) * Q).applyfunc(sp.simplify)
    ptr = sp.factor(sp.simplify(p.subs(s, tr)))
    return {"M_minus_p(trA)Q_is_zero": diff == sp.zeros(2, 2), "p(trA)": str(ptr)}


def exact_samples(rng, count=600):
    kinds = {"complex": 0, "real_distinct": 0, "jordan": 0, "scalar": 0}
    fails = []
    for _ in range(count):
        kind = rng.choice(list(kinds))
        if kind == "scalar":
            lam = sp.Rational(-int(rng.integers(1, 9)), int(rng.integers(1, 5)))
            A = lam * sp.eye(2)
        elif kind == "jordan":
            lam = sp.Rational(-int(rng.integers(1, 9)), int(rng.integers(1, 5)))
            J = sp.Matrix([[lam, sp.Rational(int(rng.integers(1, 20)), int(rng.integers(1, 5)))], [0, lam]])
            P = sp.Matrix(2, 2, [sp.Rational(int(v), 3) for v in rng.integers(-6, 7, 4)])
            if P.det() == 0:
                continue
            A = P * J * P.inv()
        else:
            A = sp.Matrix(2, 2, [sp.Rational(int(v), int(rng.integers(1, 6))) for v in rng.integers(-20, 21, 4)])
        tr, det = A.trace(), A.det()
        if not (tr < 0 and det > 0):
            continue
        disc = tr**2 - 4 * det
        real_kind = "scalar" if A == (tr / 2) * sp.eye(2) else ("complex" if disc < 0 else ("jordan" if disc == 0 else "real_distinct"))
        V = vmats(A)
        eps = 0
        while True:
            t1, t2 = taus(tr, det, disc, scalar=(real_kind == "scalar"), eps=eps)
            M = t2 * V[3] + t1 * V[2] + V[1]
            if M[0, 0] < 0 and M.det() > 0:
                break
            if real_kind != "jordan" or eps > 1:
                fails.append((str(A), real_kind, str(eps)))
                break
            eps = sp.Rational(1, 1000) / tr**2 if eps == 0 else eps / 2
            if eps < sp.Rational(1, 10**12):
                fails.append((str(A), real_kind, "eps underflow"))
                break
        kinds[real_kind] += 1
    return {"counts": kinds, "failures": fails}


def numeric_samples(rng, count=200000):
    worst = -np.inf
    n_by = {"complex": 0, "real": 0}
    for _ in range(count):
        A = rng.normal(size=(2, 2)) * rng.choice([0.01, 1, 100], size=(2, 2))
        ev = np.linalg.eigvals(A)
        A = A - (np.max(ev.real) + rng.exponential(0.3)) * np.eye(2)
        tr, det = np.trace(A), np.linalg.det(A)
        disc = tr * tr - 4 * det
        if abs(disc) < 1e-9 * tr * tr:
            continue
        t1, t2 = taus(tr, det, disc)
        V = vmats(A)
        M = t2 * V[3] + t1 * V[2] + V[1]
        rel = np.linalg.eigvalsh(M)[-1] / np.linalg.norm(M)
        worst = max(worst, rel)
        n_by["complex" if disc < 0 else "real"] += 1
    return {"max_rel_lambda_max": float(worst), "counts": n_by}


N3_CERTS = [
    ([["-77/8", "-5/8", "-13/8"], ["9/8", "-7/4", "-5/4"], ["-69/8", "0", "-9/8"]], ["-219/1000", "11/100", "969/1000"]),
    ([["-17/8", "-33/8", "-9"], ["3/8", "-3/8", "1/2"], ["-1/2", "13/8", "-17/8"]], ["3/8", "-461/500", "1/10"]),
    ([["-13/8", "-25/8", "1/8"], ["-5/4", "-9/4", "-1"], ["-8", "0", "-3/2"]], ["433/1000", "-22/25", "-193/1000"]),
]


def n3_certificates():
    out = []
    for Arows, xs in N3_CERTS:
        A = sp.Matrix([[sp.Rational(v) for v in r] for r in Arows])
        x = sp.Matrix([sp.Rational(v) for v in xs])
        lam = sp.symbols('l')
        _, a1, a2, a3 = sp.Poly((lam * sp.eye(3) - A).det(), lam).all_coeffs()
        hurwitz = bool(a1 > 0 and a2 > 0 and a3 > 0 and a1 * a2 > a3)
        V = [sp.eye(3)]
        for _ in range(4):
            V.append(A.T * V[-1] + V[-1] * A)
        ders = [(x.T * V[k] * x)[0] for k in range(1, 5)]
        out.append({"A": Arows, "x": xs, "hurwitz_exact": hurwitz,
                    "derivatives_1_to_4": [str(v) for v in ders],
                    "all_positive": all(v > 0 for v in ders)})
    return out


def main():
    rng = np.random.default_rng(20260930)
    out = {
        "symbolic_complex_case": symbolic_complex_identity(),
        "exact_rational_samples": exact_samples(rng),
        "numeric_samples": numeric_samples(rng),
        "n3_extension_counterexamples": n3_certificates(),
    }
    OUT.write_text(json.dumps(out, indent=1))
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
