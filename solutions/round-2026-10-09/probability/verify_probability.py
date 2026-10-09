"""Exact certificates for the probability reports; Python standard library only.

Q1060 checks exhaust the entire finite support and certify a universal dual
inequality, rather than relying on floating-point LP output. Q192 checks are
auxiliary exact examples of its deterministic peak lemma, not Brownian simulation.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import random


def rational(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, dict):
        return {str(k): rational(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [rational(v) for v in value]
    return value


def verify_q1060():
    states = list(product((0, 1), repeat=4))
    names = [''.join(map(str, b)) for b in states]
    expected_p = [F(1, 2), F(1, 3), F(1, 6), F(1, 2)]
    values = [[8*b[0]-4, 3*b[1]-1, 6*b[2]-1, 8*b[3]-4]
              for b in states]
    optimum = {'0001': 11, '0010': 2, '0011': 1, '0101': 6,
               '0110': 4, '1000': 11, '1001': 6, '1010': 1, '1100': 6}
    ncd = {'0001': 1175, '0010': 266, '0011': 171, '0100': 120,
           '0101': 700, '0110': 304, '1000': 1175, '1001': 690,
           '1010': 171, '1100': 700}
    reports = {}
    for label, numerators, denominator, target in [
        ('unrestricted', optimum, 48, F(16)),
        ('ncd', ncd, 5472, F(920, 57)),
    ]:
        weights = [F(numerators.get(name, 0), denominator) for name in names]
        assert all(w >= 0 for w in weights) and sum(weights) == 1
        marginals = [sum(w*b[j] for w, b in zip(weights, states)) for j in range(4)]
        assert marginals == expected_p
        means = [sum(w*x[j] for w, x in zip(weights, values)) for j in range(4)]
        assert means == [0]*4
        covariance = [[sum(w*x[i]*x[j] for w, x in zip(weights, values))
                       for j in range(4)] for i in range(4)]
        costs = {name: sum(w*sum(x[i] for i in range(4) if subset[i])**2
                           for w, x in zip(weights, values))
                 for name, subset in zip(names, states)}
        assert max(costs.values()) == target
        if label == 'unrestricted':
            assert covariance[1][2] == F(1, 2)
            assert covariance == [[16, -1, -3, -8], [-1, 2, F(1, 2), -1],
                                  [-3, F(1, 2), 5, -3], [-8, -1, -3, 16]]
        else:
            assert all(covariance[i][j] <= 0 for i in range(4)
                       for j in range(4) if i != j)
            assert covariance[1][2] == 0
        reports[label] = {'probabilities': dict(zip(names, weights)),
                          'marginals': marginals, 'means': means,
                          'covariance': covariance, 'subset_costs': costs,
                          'objective': max(costs.values())}

    dual = {}
    for name, b, x in zip(names, states, values):
        x1, x2, x3, x4 = x
        lhs = (12*((x2+x4)**2+(x2+x3+x4)**2+(x1+x2)**2+(x1+x2+x3)**2)
               +9*(x1+x4)**2+16*x2*x3)
        affine = 904-48*b[1]+192*b[2]
        s = sum(b)
        residual = 576*(s-1)*(s-2)
        assert lhs == affine+residual
        assert residual >= 0
        dual[name] = {'left': lhs, 'affine': affine, 'residual': residual}
    expected_affine = 904-48*expected_p[1]+192*expected_p[2]
    assert expected_affine == 920
    coefficient_sum = 4*12+9
    assert coefficient_sum == 57
    assert F(expected_affine, coefficient_sum)-16 == F(8, 57)
    assert (expected_affine-coefficient_sum*16)/16 == F(1, 2)
    reports['pointwise_identity'] = dual
    reports['certified_gap'] = F(8, 57)
    reports['forced_covariance_at_any_optimizer'] = F(1, 2)
    reports['all_n_nondegenerate_extension_inequality'] = F(1, 16) < F(8, 57)
    return reports


def integral_even_power(path, m):
    """Exact integral for linear interpolation at a uniform grid."""
    interval = F(1, len(path)-1)
    total = F(0)
    for left, right in zip(path, path[1:]):
        if left == right:
            total += interval*left**(2*m)
        else:
            total += interval*(right**(2*m+1)-left**(2*m+1))/((2*m+1)*(right-left))
    return total


def verify_q192_peak_lemma():
    paths = [[F(0), F(1)], [F(0), F(-3)], [F(0), F(2), F(0)],
             [F(0), F(0), F(0), F(-1)], [F(0), F(1), F(-2), F(3), F(0)]]
    rng = random.Random(192)
    for _ in range(64):
        path = [F(0)]
        for _ in range(8):
            path.append(path[-1]+F(rng.randint(-4, 4), 6))
        paths.append(path)
    count = 0
    for path in paths:
        maximum = max(map(abs, path))
        if not maximum:
            continue
        # A Lipschitz constant is also a 1/4-Hölder constant on [0,1].
        k = (len(path)-1)*max(abs(b-a) for a, b in zip(path, path[1:]))
        assert k >= maximum
        for m in (1, 2, 3, 8, 16):
            integral = integral_even_power(path, m)
            for factor in (F(1), F(1, 2), F(1, 10)):
                epsilon = maximum*factor
                delta = (epsilon/(2*k))**4
                assert 0 < delta <= 1
                assert integral >= (epsilon/2)**(2*m)*delta
                count += 1
    return {'paths': len(paths), 'exact_inequalities_checked': count,
            'scope': 'Auxiliary exact piecewise-linear checks; all-path proof is in the report.',
            'all_passed': True}


if __name__ == '__main__':
    certificate = rational({'Q1060': verify_q1060(), 'Q192': verify_q192_peak_lemma()})
    destination = Path(__file__).with_name('probability-certificates.json')
    destination.write_text(json.dumps(certificate, indent=2)+'\n')
    print('Q1060: exact optima 16 and 920/57; gap 8/57; all 16 dual states certified.')
    print('Q192: %d exact deterministic peak inequalities passed.'
          % certificate['Q192']['exact_inequalities_checked'])
    print(destination.name)
