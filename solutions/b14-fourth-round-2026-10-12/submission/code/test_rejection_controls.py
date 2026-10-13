"""Negative controls for the independent certificate reader; originals unchanged."""
from __future__ import annotations
from pathlib import Path
import json,shutil,tempfile,time
import verify_saved_certificates as V
ROOT=Path(__file__).resolve().parents[1]

def main():
    specs=[
      ('dp_wrong_value','checks/CONTRACTED-DP-CERTIFICATE.json',lambda x:x[0]['root_cases'][0]['rows'][0].__setitem__(2,x[0]['root_cases'][0]['rows'][0][2]+1),'contracted'),
      ('dp_missing_state','checks/CONTRACTED-DP-CERTIFICATE.json',lambda x:x[0]['root_cases'][0]['rows'].pop(),'contracted'),
      ('dp_missing_root_case','checks/CONTRACTED-DP-CERTIFICATE.json',lambda x:x[0]['root_cases'].pop(),'contracted'),
      ('flow_capacity_violation','checks/SUBTOUR-FLOW-CERTIFICATES.json',lambda x:x['flows'][0]['net'][0].__setitem__(2,100),'flows'),
      ('flow_missing_target','checks/SUBTOUR-FLOW-CERTIFICATES.json',lambda x:x['flows'].pop(),'flows'),
      ('metric_asymmetry','checks/ORDINAL-CERTIFICATES.json',lambda x:x[0]['surrogate']['d'][0].__setitem__(1,x[0]['surrogate']['d'][0][1]+1),'ordinal'),
      ('wrong_unique_optimum','instances/unique-180-city-separation.json',lambda x:x.__setitem__('optimum',x['optimum']+1),'unique'),
      ('wrong_nonseparable_optimum','instances/nonseparable-180-city.json',lambda x:x.__setitem__('optimum',x['optimum']-1),'contracted')]
    ts=time.perf_counter();results=[]
    for name,file,mutate,function in specs:
        with tempfile.TemporaryDirectory() as temp:
            P=Path(temp)
            for folder in ['checks','instances']:shutil.copytree(ROOT/folder,P/folder)
            x=json.loads((P/file).read_text());mutate(x);(P/file).write_text(json.dumps(x))
            V.ROOT=P
            try:getattr(V,function)()
            except AssertionError:results.append(dict(control=name,rejected=True))
            else:raise AssertionError('Damaged certificate accepted: '+name)
    V.ROOT=ROOT
    out=dict(status='PASS',damaged_certificates_rejected=len(results),controls=results,originals_modified=False,elapsed_seconds=time.perf_counter()-ts)
    (ROOT/'checks/REJECTION-CONTROLS.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
