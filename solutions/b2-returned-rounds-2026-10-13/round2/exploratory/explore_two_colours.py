from pathlib import Path
import itertools, collections,json
P=list(itertools.product(range(3),repeat=3)); idx={x:i for i,x in enumerate(P)}
mid=[[idx[tuple(-(a+b)%3 for a,b in zip(x,y))] for y in P] for x in P]
def iscap(R):return all(mid[x][y] not in R for x,y in itertools.combinations(R,2))
def oddcycle(R):
 c={};parents={}
 for s in range(27):
  if s in R or s in c:continue
  c[s]=0;parents[s]=None;q=collections.deque([s])
  while q:
   x=q.popleft()
   for y in range(27):
    if y==x or y in R or mid[x][y] not in R:continue
    if y not in c:c[y]=1-c[x];parents[y]=x;q.append(y)
    elif c[y]==c[x]:
     ax=[];ay=[];a=x;b=y
     while a is not None:ax.append(a);a=parents[a]
     while b is not None:ay.append(b);b=parents[b]
     while ax and ay and ax[-1]==ay[-1]:common=ax.pop();ay.pop()
     return ax+[common]+ay[::-1]
 return None
R0={idx[x] for x in [(0,0,0),(1,0,0),(0,1,0),(0,0,1)]};nodes=0;solutions=[];seen=set();hist=collections.Counter()
def run(R):
 global nodes
 key=frozenset(R)
 if key in seen:return
 seen.add(key);nodes+=1;hist[len(R)]+=1
 cy=oddcycle(R)
 if cy is None:solutions.append(sorted(R));return
 for x in cy:
  if iscap(R|{x}):run(R|{x})
run(R0)
print('nodes',nodes,'histogram',hist,'solutions',[[P[i] for i in s]for s in solutions])
json.dump({'nodes':nodes,'histogram':dict(hist),'solutions':[[P[i]for i in s]for s in solutions]},open(Path(__file__).with_name('TWO-COLOUR-CAP-SEARCH.json'),'w'),indent=2)
