// Control for research/round2-harder.md section 5 (Hopkins 2018, Conjecture 2.3.1).
// Build: g++ -O2 -o /tmp/chips hopkins_chipfiring_inversions.cpp ; run: /tmp/chips N  (N = 3..11; N=11 needs ~6.5M states, several GB RAM).
// Labeled chip-firing on Z, N chips at origin. Explores all firing choices (any 2 chips at an unstable site),
// computes the set of reachable final permutations' max inversion count, via memoized DFS on states.
#include <bits/stdc++.h>
using namespace std;
int N,M;                         // sites -M..M
typedef vector<uint8_t> St;       // pos[label] = site+M  (label 0..N-1)
struct H{size_t operator()(const St&s)const{size_t h=1469598103934665603ULL;for(auto c:s){h^=c;h*=1099511628211ULL;}return h;}};
unordered_map<St,uint8_t,H> memo;
int inv(const St&s){ // final: one chip per site; permutation = labels sorted by site
    vector<int> bysite(2*M+1,-1); for(int l=0;l<N;l++) bysite[s[l]]=l;
    vector<int> p; for(int x:bysite) if(x>=0) p.push_back(x);
    int c=0; for(int i=0;i<N;i++) for(int j=i+1;j<N;j++) if(p[i]>p[j]) c++; return c;}
int dfs(const St&s){
    auto it=memo.find(s); if(it!=memo.end()) return it->second;
    vector<vector<int>> at(2*M+1); for(int l=0;l<N;l++) at[s[l]].push_back(l);
    int best=-1; bool any=false;
    for(int site=0;site<2*M+1;site++){ auto&v=at[site]; if(v.size()<2) continue; any=true;
        for(size_t i=0;i<v.size();i++) for(size_t j=i+1;j<v.size();j++){
            St t=s; int a=min(v[i],v[j]), b=max(v[i],v[j]); t[a]--; t[b]++; best=max(best,dfs(t)); } }
    if(!any) best=inv(s);
    memo[s]=best; return best; }
bool terminal(const St&s){ vector<int> c(2*M+1,0); for(auto x:s) if(++c[x]>1) return false; return true; }
int main(int argc,char**argv){ N=atoi(argv[1]); M=N/2+1; St s(N,M); int r=dfs(s);
    size_t finals=0; for(auto&kv:memo) if(terminal(kv.first)) finals++;
    printf("N=%d max inversions=%d  (m=%d)  states=%zu  distinct final permutations=%zu\n",N,r,(N-1)/2,memo.size(),finals); }
