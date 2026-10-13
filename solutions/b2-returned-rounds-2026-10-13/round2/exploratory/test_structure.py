import itertools,collections

def geom(n):
 P=list(itertools.product(range(3),repeat=n));id={x:i for i,x in enumerate(P)}
 mid=[[id[tuple(-(a+b)%3 for a,b in zip(x,y))]for y in P]for x in P]
 return P,id,mid

def closure(R,mid):
 R=set(R)
 while True:
  S=R|{mid[x][y]for x in R for y in R}
  if S==R:return S
  R=S

def bip(R,mid):
 N=len(mid);c={}
 for s in range(N):
  if s in R or s in c:continue
  c[s]=0;q=[s]
  for x in q:
   for y in range(N):
    if y==x or y in R or mid[x][y]not in R:continue
    if y not in c:c[y]=1-c[x];q.append(y)
    elif c[y]==c[x]:return None
 return c

def two_flats(B,mid):
 B=set(B)
 if not B:return True
 x=next(iter(B));rest=sorted(B-{x})
 for m in range(1<<len(rest)):
  A={x}|{v for i,v in enumerate(rest)if m>>i&1}
  A=closure(A,mid)
  if A<=B and closure(B-A,mid)<=B:return True
 return False
if __name__=='__main__':
 P,id,mid=geom(2);bad=[];hist=collections.Counter()
 for m in range(512):
  R={i for i in range(9)if m>>i&1}
  if closure(R,mid)!=set(range(9)):continue
  c=bip(R,mid)
  if c is None:continue
  hist[len(R)]+=1
  if not two_flats(set(range(9))-R,mid):bad.append(R)
 print('hist',hist,'bad',bad)
