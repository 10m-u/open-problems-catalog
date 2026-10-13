"""Independent bounded controls for definability, entropy and circuits.

Imports root verifiers read-only. Does not rerun optimizers or overwrite
root packets. Direct matrix sums and integer circuit semantics are separate.
"""
import cmath
from copy import deepcopy
import importlib.util
from itertools import product
import json
import math
from pathlib import Path
import random
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
BASE = HERE.parent


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def direct_matrix(w):
    p = 1 << w
    roots = [cmath.exp(2j * math.pi * x / p) for x in range(p)]
    return [[sum(roots[(a*x)%p] * (-1 if (b&x).bit_count()%2 else 1)
                 for x in range(p))/p for a in range(p)] for b in range(p)]


def multiply(a, z):
    return [sum(x*y for x,y in zip(row,z)) for row in a]


def entropy(z):
    probabilities = [abs(x)**2 for x in z]
    return -sum(p*math.log2(p) for p in probabilities if p > 0)


def h(p):
    return -sum(x*math.log2(x) for x in [p,1-p] if x > 0)


def integer_outputs(spec, inputs, w):
    p = 1 << w
    env = dict(zip(spec['inputs'],inputs))
    for name,op,*args in spec['gates']:
        operands = [env[x] for x in args]
        if op == 'add':
            env[name] = sum(operands)%p
        elif op == 'not':
            env[name] = (p-1)^operands[0]
        elif op == 'zero':
            env[name] = 0
        elif op == 'and':
            env[name] = operands[0]&operands[1]
        elif op == 'or':
            env[name] = operands[0]|operands[1]
        else:
            env[name] = operands[0]^operands[1]
    return [env[name] for name in spec['outputs']]


def main():
    rng = random.Random(20261012)
    matrices = {w:direct_matrix(w) for w in range(1,7)}
    blocks = mixtures = 0
    for w,mat in matrices.items():
        p = 1 << w
        for m in range(w):
            rows = list(range(1<<m,1<<(m+1)))
            cols = [(2*j+1)*(1<<(w-m-1)) for j in range(1<<m)]
            sub = [[mat[b][a] for a in cols] for b in rows]
            coherence = 1/((1<<m)*math.sin(math.pi/(1<<(m+1))))
            assert abs(max(abs(z) for row in sub for z in row)-coherence)<2e-13
            for i,j in product(range(1<<m),repeat=2):
                inner = sum(row[i].conjugate()*row[j] for row in sub)
                assert abs(inner-(1 if i==j else 0))<2e-12
            blocks += 1
        for t in range(1,w):
            z = [0j]*p
            for m in range(t,w):
                for j in range(1<<m):
                    z[(2*j+1)*(1<<(w-m-1))] = complex(rng.random()-.5,rng.random()-.5)
            norm = math.sqrt(sum(abs(x)**2 for x in z))
            z = [x/norm for x in z]
            y = multiply(mat,z)
            weights = []
            component_entropy = 0.
            for m in range(t,w):
                cols = [(2*j+1)*(1<<(w-m-1)) for j in range(1<<m)]
                rows = list(range(1<<m,1<<(m+1)))
                weight = sum(abs(z[a])**2 for a in cols)
                assert abs(weight-sum(abs(y[b])**2 for b in rows))<2e-12
                weights.append(math.sqrt(weight))
                component_entropy += weight*(entropy([z[a]/math.sqrt(weight) for a in cols])
                                              +entropy([y[b]/math.sqrt(weight) for b in rows]))
            assert abs(entropy(z)+entropy(y)-2*entropy(weights)-component_entropy)<2e-11
            mixtures += 1
    archive = json.loads((BASE/'fourier/VALIDATION.json').read_text())
    candidate_controls = []
    for record in archive['entropy_block_optimization']:
        t = record['t']
        mat = matrices[t+1]
        sub = [[mat[b][a] for a in range(1,1<<(t+1),2)]
               for b in range(1<<t,1<<(t+1))]
        z = [complex(x,y) for x,y in zip(record['candidate_real'],record['candidate_imag'])]
        assert abs(sum(abs(x)**2 for x in z)-1)<2e-12
        cost = entropy(z)+entropy(multiply(sub,z))
        assert abs(cost-record['upper_bound'])<2e-10
        candidate_controls.append(dict(t=t,cost=cost))
    theta = math.pi/16
    z = [math.cos(theta),0,1j*math.sin(theta),0]
    sub = [[matrices[3][b][a] for a in [1,3,5,7]] for b in range(4,8)]
    assert abs(entropy(z)+entropy(multiply(sub,z))-(1+2*h(math.sin(theta)**2)))<2e-12
    assert 1+2*h(math.sin(math.pi/32)**2) < -2*math.log2(1/(8*math.sin(math.pi/16)))

    circuits = module('review_circuits',BASE/'automatic-proofs/circuits.py')
    specialized = module('review_specialized',BASE/'automatic-proofs/check.py')
    saved = json.loads((BASE/'automatic-proofs/CIRCUIT-CERTIFICATES.json').read_text())
    for packet in saved:
        circuits.verify(packet)
    specialized.verify(json.loads((BASE/'automatic-proofs/CERTIFICATES.json').read_text()))
    altered = []
    a = deepcopy(saved[0]);a['edges'].pop();altered.append(a)
    a = deepcopy(saved[-1]);a['bad_terminal_states']=[];altered.append(a)
    a = deepcopy(saved[0]);a['states'][1][0] = 9;altered.append(a)
    for packet in altered:
        try:
            circuits.verify(packet)
        except (AssertionError,KeyError,IndexError):
            pass
        else:
            raise AssertionError('altered certificate accepted')
    circuit_cases = witness_cases = 0
    arities = {'add':2,'xor':2,'and':2,'or':2,'not':1,'zero':0}
    for index in range(20):
        names = ['x','y']
        gates = []
        for j in range(8):
            op = rng.choice(list(arities))
            args = [rng.choice(names) for _ in range(arities[op])]
            name = f'g{j}'
            gates.append([name,op,*args]);names.append(name)
        spec = dict(name=f'bounded_control_{index}',inputs=['x','y'],gates=gates,
                    outputs=rng.sample(names,2))
        packet = circuits.certificate(spec)
        circuits.verify(json.loads(json.dumps(packet)))
        alphabet,initial,step = circuits.compile_spec(spec)
        for w in range(1,6):
            for x,y in product(range(1<<w),repeat=2):
                state = initial
                for j in range(w):
                    state = step(state,((x>>j)&1,(y>>j)&1))
                a,b = integer_outputs(spec,(x,y),w)
                assert state[-2] == (a!=b) and state[-1]
                circuit_cases += 1
        if not packet['all_positive_widths_equal']:
            word = packet['counterexample_lsd_bits'];w=len(word)
            inputs = [sum(column[j]<<i for i,column in enumerate(word)) for j in range(2)]
            a,b = integer_outputs(spec,inputs,w)
            assert a!=b
            witness_cases += 1

    definability = module('review_definability',HERE/'check_definability.py')
    complement_cases = 0
    for x in range(1<<17):
        witness = definability.existential_complement_witness(x)
        # Independent base-four interpretation, excluding leading zeros.
        digits = []
        n=x
        while n:
            digits.append(n%4);n//=4
        bad = any(d in [0,3] for d in digits)
        assert (witness is not None) == bad == (not definability.in_k(x))
        complement_cases += 1
    result = dict(status='passed', entropy_blocks=blocks, mixed_block_identities=mixtures,
                  saved_candidate_costs=candidate_controls, analytic_two_character_control=True,
                  saved_generic_packets=len(saved), saved_specialized_packets=2,
                  altered_packets_rejected=len(altered), generated_circuits=20,
                  bounded_circuit_semantics=circuit_cases, direct_counterexample_checks=witness_cases,
                  complement_basefour_controls=complement_cases,
                  scope='independent finite controls; no new optimization, proof search or unbounded definability claim')
    (HERE/'ROOT-REVIEW-CHECK-RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
