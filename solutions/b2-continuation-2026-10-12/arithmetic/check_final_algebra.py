"""Exact controls for reciprocity, failed extension templates and resonance inequality."""
import json
from pathlib import Path
from sympy import symbols, Poly, cyclotomic_poly, expand, factor, factorint


def main():
    x,t,A,B = symbols("x t A B")
    count = 0
    for n in range(2,21):
        for m in range(n,21):
            f = cyclotomic_poly(n,x)*cyclotomic_poly(m,x)
            degree = Poly(f,x).degree()
            h = f+1
            reciprocal = expand(x**degree * h.subs(x,1/x))
            assert expand(reciprocal-h) == x**degree-1
            count += 1
    relation=(t*t-t+2)**3-(t+2)**5
    quotient=t**5+2*t**4+11*t**3+13*t**2+16*t+4
    assert expand(relation-(t-6)*quotient)==0
    assert all(c>0 for c in Poly(quotient,t).all_coeffs())
    a,b=A+2,B+2
    difference=expand(a*b*(3*a+3*b+2)**2-4*(a-1)*(a+2)*(b-1)*(b+2))
    assert all(c>0 for c in Poly(difference,A,B).coeffs())
    assert factorint(25922)=={2:1,13:1,997:1}
    assert factorint(530)=={2:1,5:1,53:1}
    assert factorint(7)=={7:1} and factorint(13)=={13:1} and factorint(97)=={97:1}
    out={"passed":True,"exact_product_reciprocity_controls":count,
         "seed_template_factorization":str(factor(relation)),
         "resonance_positive_difference":str(difference),
         "powered_shift_unique_prime":13,
         "scope":"Algebraic identities and individual failed-template controls; no full conjecture closures"}
    Path(__file__).with_name("FINAL-ALGEBRA-CHECK.json").write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps(out))


if __name__ == "__main__":
    main()
