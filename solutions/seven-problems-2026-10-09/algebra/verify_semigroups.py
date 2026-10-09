#!/usr/bin/env python3
"""Exact, standard-library verification of the Q3101/Q3102 controls.

Run from the repository root:
  python solutions/seven-problems-2026-10-09/algebra/verify_semigroups.py

Writes verification.json and finite-examples.json next to this script.
No numerical tolerance, external algebra package, SMT solver, or network is used.
"""
from collections import Counter, deque
from itertools import combinations, permutations, product
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent


def table_from_operation(labels, operation):
    position = {x: i for i, x in enumerate(labels)}
    return [[position[operation(x, y)] for y in labels] for x in labels]


def transformations_table(maps):
    assert len(set(maps)) == len(maps)
    return table_from_operation(maps, lambda a, b: tuple(b[a[i]] for i in range(len(a))))


def band10():
    # An explicitly supplied finite algebra: associativity is independently checked below.
    labels = ['a','b','c','d','ab','ac','bc','bd','ca','abc']
    table = [
        [0,4,5,3,4,5,9,7,8,9], [4,1,6,7,4,9,6,7,9,9],
        [8,6,2,5,9,5,6,9,8,9], [0,4,5,3,4,5,9,7,8,9],
        [4,4,9,7,4,9,9,7,9,9], [8,9,5,5,9,5,9,9,8,9],
        [9,6,6,9,9,9,6,9,9,9], [4,4,9,7,4,9,9,7,9,9],
        [8,9,5,5,9,5,9,9,8,9], [9,9,9,9,9,9,9,9,9,9],
    ]
    return labels, table


def quotient(table, identified):
    n = len(table)
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def join(a,b):
        a,b = find(a),find(b)
        if a == b: return False
        parent[max(a,b)] = min(a,b)
        return True
    for a,b in identified: join(a,b)
    changed = True
    while changed:
        changed = False
        for a,b in combinations(range(n),2):
            if find(a) != find(b): continue
            for x in range(n):
                changed |= join(table[a][x],table[b][x])
                changed |= join(table[x][a],table[x][b])
    classes = sorted({find(x) for x in range(n)})
    ind = {c:i for i,c in enumerate(classes)}
    images = [ind[find(x)] for x in range(n)]
    result = [[images[table[a][b]] for b in classes] for a in classes]
    return result, images


def constants_extension(table):
    # Right regular representation on B with a new identity adjoined, plus all constants.
    n = len(table)
    maps = [tuple([table[x][s] for x in range(n)]+[s]) for s in range(n)]
    maps += [tuple([x]*(n+1)) for x in range(n+1)]
    maps = list(dict.fromkeys(maps))
    return [str(m) for m in maps], transformations_table(maps)


def cyclic_product(table, order):
    n = len(table)
    labels = list(product(range(n),range(order)))
    op = lambda a,b:(table[a[0]][b[0]],(a[1]+b[1])%order)
    return labels, table_from_operation(labels,op)


def zero_union_with_s3():
    # The first factor is a right-zero semigroup of size two times C2.
    a = [('A',i,g) for i in range(2) for g in range(2)]
    g = [('G',p) for p in permutations(range(3))]
    zero = ('zero',)
    labels = a+g+[zero]
    def op(x,y):
        if x[0]=='A' and y[0]=='A':return ('A',y[1],(x[2]+y[2])%2)
        if x[0]=='G' and y[0]=='G':return ('G',tuple(y[1][x[1][i]] for i in range(3)))
        return zero
    return labels,table_from_operation(labels,op)


def paulista_even_girth(n):
    if n==2:
        maps=[(0,0,0),(1,1,1),(0,1,0),(0,1,1)]
    else:
        points=list(product(range(n),range(1,n)))
        index={p:i for i,p in enumerate(points)}
        maps=[]
        for i in range(n):
            maps.append(tuple(index[(k,(k-i)%n or 1)] for k,j in points))
        maps += [tuple([i]*len(points)) for i in range(len(points))]
    return [str(m) for m in maps],transformations_table(maps)


def involution_on_right_zero():
    # Units 1,t with t^2=1 act on four right-zero elements; two are fixed, two swapped.
    labels=[('G',0),('G',1)]+[('B',i) for i in range(4)]
    perm=[0,1,3,2]
    def op(a,b):
        if a[0]=='G' and b[0]=='G':return ('G',(a[1]+b[1])%2)
        if b[0]=='B':return b
        return ('B',a[1] if b[1]==0 else perm[a[1]])
    return labels,table_from_operation(labels,op)


def rees_cyclic(order):
    labels=list(product(range(2),range(order),range(2)))
    sandwich=[[0,0],[0,1%order]]
    def op(a,b):
        return (a[0],(a[1]+sandwich[a[2]][b[0]]+b[1])%order,b[2])
    return labels,table_from_operation(labels,op)


def nilpotent_knit_three():
    # Bauer--Greenfeld Example 10: length-three words are zero.
    zero_pairs={(0,1),(3,1),(0,2),(3,2),(1,0),(1,2),(2,1),(2,3)}
    def pair(i,j):
        if (i,j) in zero_pairs:return ('0',)
        if (i,j)==(3,0):return ('p',0,0)
        if (i,j)==(0,3):return ('p',3,3)
        return ('p',i,j)
    labels=[('g',i) for i in range(4)]
    labels += sorted({pair(i,j) for i,j in product(range(4),repeat=2)}- {('0',)})
    labels += [('0',)]
    def op(a,b):
        if a[0]==b[0]=='g':return pair(a[1],b[1])
        return ('0',)
    return labels,table_from_operation(labels,op)


def nilpotent_cycle_five():
    # Monomial graph realization in Bauer--Greenfeld Proposition 3, edges set to zero.
    def pair(i,j):
        if (i-j)%5 in (1,4):return ('0',)
        return ('p',i,j)
    labels=[('g',i) for i in range(5)]
    labels += sorted({pair(i,j) for i,j in product(range(5),repeat=2)}- {('0',)})
    labels += [('0',)]
    def op(a,b):
        if a[0]==b[0]=='g':return pair(a[1],b[1])
        return ('0',)
    return labels,table_from_operation(labels,op)


def graph(table):
    n=len(table)
    central=[a for a in range(n) if all(table[a][b]==table[b][a] for b in range(n))]
    vertices=[a for a in range(n) if a not in central]
    adj={a:{b for b in vertices if b!=a and table[a][b]==table[b][a]} for a in vertices}
    return central,vertices,adj


def girth(adj):
    best=None
    for s in adj:
        distances={s:0}
        parents={s:None}
        q=deque([s])
        while q:
            x=q.popleft()
            for y in adj[x]:
                if y not in distances:
                    distances[y]=distances[x]+1
                    parents[y]=x
                    q.append(y)
                elif parents[x]!=y and parents[y]!=x:
                    length=distances[x]+distances[y]+1
                    best=length if best is None else min(best,length)
    return best


def bipartite(adj):
    color={}
    for s in adj:
        if s in color:continue
        color[s]=0
        q=deque([s])
        while q:
            x=q.popleft()
            for y in adj[x]:
                if y not in color:color[y]=1-color[x];q.append(y)
                elif color[y]==color[x]:return False
    return True


def is_left_path(table, path, adj):
    if len(set(path))!=len(path) or len(path)<2:return False
    if any(x not in adj for x in path):return False
    if any(y not in adj[x] for x,y in zip(path,path[1:])):return False
    a,d=path[0],path[-1]
    return all(table[a][x]==table[d][x] for x in path)


def powers_identity(table,a):
    # Purely periodic powers characterize membership in a subgroup for a finite element.
    powers=[]
    x=a
    while x not in powers:
        powers.append(x)
        x=table[x][a]
    if x!=a:return None
    identity=next((x for x in powers if table[x][x]==x and table[x][a]==a and table[a][x]==a),None)
    assert identity is not None
    return identity,len(powers)


def collapse(table,path,identities,central):
    a,b,c,d=path
    e,f=identities[a][0],identities[d][0]
    u=identities[b][0]
    p,q=table[e][u],table[u][f]
    if p!=q:return [p,c,q],'A:distinct_pq'
    if u not in central:return [e,u,f],'B:noncentral_u'
    return [e,b,f],'C:central_u'


def check(name,labels,table,expected_cr=None,expected_girth='unchecked'):
    n=len(table)
    assert all(len(row)==n and all(isinstance(v,int) and 0<=v<n for v in row) for row in table)
    for a,b,c in product(range(n),repeat=3):
        assert table[table[a][b]][c]==table[a][table[b][c]],(name,'associativity',a,b,c)
    identities=[powers_identity(table,a) for a in range(n)]
    cr=all(v is not None for v in identities)
    if expected_cr is not None:assert cr==expected_cr,name
    band=all(table[a][a]==a for a in range(n))
    central,vertices,adj=graph(table)
    g=girth(adj)
    if expected_girth!='unchecked':assert g==expected_girth,(name,g,expected_girth)
    left_counts={}
    first_paths={}
    case_counts=Counter()
    for length in (1,2,3):
        count=0
        for path in permutations(vertices,length+1):
            if not is_left_path(table,path,adj):continue
            count+=1
            first_paths.setdefault(str(length),list(path))
            if cr and length==3:
                reduced,case=collapse(table,path,identities,central)
                assert is_left_path(table,reduced,adj),(name,'collapse',path,reduced,case)
                assert len(reduced)==3
                case_counts[case]+=1
        left_counts[str(length)]=count
    if cr:assert left_counts['1']==0,name
    idem=[a for a in vertices if table[a][a]==a]
    square_pairs=0
    sandwich_paths=0
    degree_vertices=0
    if cr:
        # Lemma 4 is checked even when the graph has triangles.
        all_idem=[a for a in range(n) if table[a][a]==a]
        for a,c in product(all_idem,repeat=2):
            ac,ca=table[a][c],table[c][a]
            if table[ac][ac]==table[ca][ca]:
                assert ac==ca,(name,'idempotent_square_lemma',a,c)
                square_pairs+=1
    if cr and g!=3:
        assert bipartite({a:adj[a]&set(idem) for a in idem}),name
        if band:assert bipartite(adj),name
        for a,c in permutations(idem,2):
            if c in adj[a]:continue
            for b in sorted(adj[a]&adj[c]):
                assert table[table[a][c]][a]==a,(name,'sandwich',a,b,c)
                assert table[table[c][a]][c]==c,(name,'sandwich',c,b,a)
                sandwich_paths+=1
        for x in vertices:
            if len(adj[x])<2:continue
            degree_vertices+=1
            identity,order=identities[x]
            assert order in (1,2),(name,'order',x,order)
            if order==2:assert identity in central,(name,'central_identity',x,identity)
    digest=hashlib.sha256(json.dumps(table,separators=(',',':')).encode()).hexdigest()
    return dict(name=name,order=n,associativity_triples=n**3,completely_regular=cr,band=band,
                central_elements=central,noncentral_vertices=len(vertices),edges=sum(map(len,adj.values()))//2,
                girth=g,bipartite=bipartite(adj),left_path_counts=left_counts,first_left_paths=first_paths,
                constructive_collapse_cases=dict(sorted(case_counts.items())),
                idempotent_equal_square_pairs=square_pairs,idempotent_sandwich_paths=sandwich_paths,
                degree_at_least_two_vertices_checked=degree_vertices,table_sha256=digest)


def main():
    examples=[]
    labels,t=band10()
    examples.append(('band10',labels,t,True,'unchecked'))
    labels,t2=cyclic_product(t,2)
    examples.append(('band10_times_C2',labels,t2,True,'unchecked'))
    quotient_table,images=quotient(t,[(4,7)])
    labels,t3=constants_extension(quotient_table)
    examples.append(('quotient_band_constants_extension',labels,t3,True,'unchecked'))
    labels,t4=zero_union_with_s3()
    examples.append(('right_group_zero_union_S3',labels,t4,True,3))
    for n in range(2,6):
        labels,tn=paulista_even_girth(n)
        examples.append((f'paulista_girth_{2*n}',labels,tn,True,2*n))
    labels,t5=involution_on_right_zero()
    examples.append(('C2_right_zero_action',labels,t5,True,None))
    for order in (2,3):
        labels,tn=rees_cyclic(order)
        examples.append((f'Rees_C{order}',labels,tn,True,None if order==2 else 3))
    labels,tn=nilpotent_knit_three()
    examples.append(('Bauer_Greenfeld_knit_3',labels,tn,False,None))
    labels,tn=nilpotent_cycle_five()
    examples.append(('Bauer_Greenfeld_cycle_5',labels,tn,False,5))
    results=[]
    fixtures=[]
    for name,labels,table,expected_cr,expected_girth in examples:
        result=check(name,labels,table,expected_cr,expected_girth)
        results.append(result)
        fixtures.append(dict(name=name,labels=labels,multiplication_table=table))
    cases=Counter()
    for item in results:cases.update(item['constructive_collapse_cases'])
    assert set(cases)=={'A:distinct_pq','B:noncentral_u','C:central_u'},cases
    negative=next(x for x in results if x['name']=='Bauer_Greenfeld_knit_3')
    assert negative['left_path_counts']['1']==negative['left_path_counts']['2']==0
    assert negative['left_path_counts']['3']>0
    report=dict(date='2026-10-09',arithmetic='exact integer table lookups',status='all checks passed',
                example_count=len(results),total_associativity_triples=sum(x['associativity_triples'] for x in results),
                collapse_case_totals=dict(sorted(cases.items())),examples=results,
                limitations=['These explicit finite controls do not replace the universal proofs.',
                             'No exhaustive classification of all semigroups up to an order is claimed.'])
    (ROOT/'verification.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
    (ROOT/'finite-examples.json').write_text(json.dumps(fixtures,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='examples'},indent=2))

if __name__=='__main__':main()
