#!/usr/bin/env python3
"""Fresh exhaustive genomic-Q example using the primary §7 definitions."""
from itertools import product
from pathlib import Path
from hashlib import sha256
import json

HERE=Path(__file__).resolve().parent
POSITIONS=((1,4),(2,3),(2,4),(3,3))
def family(letter):return (letter+1)//2
def prime(letter):return letter%2==1
def q_tableau(entries):
    for p,a in entries.items():
        if p[0]==p[1] and prime(a):return False
        for q,b in entries.items():
            if ((p[0]==q[0] and p[1]<q[1]) or
                (p[1]==q[1] and p[0]<q[0])) and a>b:return False
            if p==q:continue
            if a==b and ((not prime(a) and p[1]==q[1]) or
                         (prime(a) and p[0]==q[0])):return False
    return True
def blocks(sequence,number):
    if not sequence:return
    for cut in product((False,True),repeat=len(sequence)-1):
        if sum(cut)+1!=number:continue
        out=[];start=0
        for j,c in enumerate(cut,1):
            if c:out.append(sequence[start:j]);start=j
        out.append(sequence[start:]);yield out
def gene_valid(entries,G,ptype=False):
    for i,p in enumerate(G):
        for q in G[i+1:]:
            if (ptype or entries[p]==entries[q]) and (p[0]==q[0] or p[1]==q[1]):
                return False
    return True
def ballot_word(word):
    hat=[a+1 for a in reversed(word)]
    counts={}
    for a in word+hat:
        k=family(a)
        if k>1 and counts.get(k,0)>=counts.get(k-1,0):return False
        if not prime(a):counts[k]=counts.get(k,0)+1
    return True
def every_genotype(entries,genes):
    for chosen in product(*genes):
        word=[entries[p] for p in sorted(chosen,key=lambda p:(p[0],-p[1]))]
        if not ballot_word(word):return False
    return True
def pgen(entries,genes):
    if not all(gene_valid(entries,G,True) for G in genes):return False
    genemap={p:i for i,G in enumerate(genes) for p in G}
    for p,a in entries.items():
        if not prime(a):continue
        southwest=[q for q,b in entries.items()
                   if family(a)==family(b) and q[0]>=p[0] and q[1]<=p[1] and q!=p]
        if not any(not prime(entries[q]) for q in southwest):return False
        if not any(genemap[q]!=genemap[p] for q in southwest):return False
    return True
def main():
    accepted=[];paccepted=[];qfillings=partitions=0
    for letters in product(range(1,5),repeat=4):
        entries=dict(zip(POSITIONS,letters))
        if not q_tableau(entries):continue
        qfillings+=1
        families=[]
        for k,number in ((1,2),(2,1)):
            sequence=sorted([p for p,a in entries.items() if family(a)==k],
                key=lambda p:(0,p[0],p[1]) if prime(entries[p]) else (1,p[1],p[0]))
            families.append(list(blocks(sequence,number)))
        for G1,G2 in product(*families):
            genes=G1+G2
            if not all(gene_valid(entries,G) for G in genes):continue
            partitions+=1
            if not every_genotype(entries,genes):continue
            row={'letters':list(letters),'genes':[[list(p) for p in G] for G in genes]}
            accepted.append(row)
            if pgen(entries,genes):paccepted.append(row)
    assert len(accepted)==6,accepted
    assert len(paccepted)==1,paccepted
    receipt={'status':'PASS','alphabet':'1prime,1,2prime,2 encoded 1,2,3,4',
       'positions':POSITIONS,'semistandard_q_fillings':qfillings,
       'content_21_gene_partitions':partitions,'q_ballot_count':len(accepted),
       'p_ballot_count':len(paccepted),'q_ballot_objects':accepted,
       'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
       'scope':'Literal Example 8.5 enumeration. Actual LG coefficient -5 is primary-source evidence, not computed by this enumerator.'}
    (HERE/'Q-GENOMIC-CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))
if __name__=='__main__':main()

