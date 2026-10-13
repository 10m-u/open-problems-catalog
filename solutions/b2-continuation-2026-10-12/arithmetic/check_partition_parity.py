"""Independent 2D partition counts versus conjugation-fixed Euler parity."""
import json
from pathlib import Path


def counts(D,bound):
    trace_bound=2*bound
    parts=[]
    for a in range(1,trace_bound+1):
        for b in range(-a,a+1):
            if (a-b)%2==0 and D*b*b<a*a:
                parts.append((a,b))
    dp={(0,0):1}
    for pa,pb in parts:
        for a in range(pa,trace_bound+1):
            for b in range(-a,a+1):
                v=dp.get((a-pa,b-pb),0)
                if v and D*b*b<a*a:
                    dp[a,b]=dp.get((a,b),0)+v
    return [dp.get((2*n,0),0) for n in range(bound+1)]


def fixed_parity(D,bound):
    dp=[1]+[0]*bound
    for a in range(1,bound+1):
        pairs=sum(1 for b in range(1,a+1) if (a-b)%2==0 and D*b*b<a*a)
        for _ in range(1+pairs):
            for n in range(a,bound+1):
                dp[n]^=dp[n-a]
    return dp


def main():
    bound=12
    rows=[]
    for D in (5,13,17,21,29):
        c=counts(D,bound)
        parity=fixed_parity(D,bound)
        assert [x%2 for x in c]==parity
        assert all(c[n+1]>c[n] for n in range(1,bound))
        rows.append({"D":D,"counts":c,"parities":parity})
    assert rows[0]["counts"][3]==4
    out={"passed":True,"max_integer_argument":bound,"quadratic_fields":len(rows),
         "independent_trace_lattice_and_fixed_partition_controls":len(rows)*(bound+1),
         "rows":rows,"scope":"Exact finite values and parity-product controls, not infinite parity/divisibility"}
    Path(__file__).with_name("PARTITION-CHECK.json").write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps({k:v for k,v in out.items() if k!="rows"}))


if __name__=="__main__":
    main()
