// Independent exact oracle: all forced-edge tour optima by endpoint Held--Karp.
// Reads n and a symmetric integer cost matrix; outputs OPT and the n*n forced
// optimum matrix. There is no necklace logic in this program.
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <limits>
#include <vector>
int main(){
  int n; if(!(std::cin>>n)||n<3||n>18)return 2;
  std::vector<int64_t> c(n*n); for(auto &v:c)if(!(std::cin>>v))return 3;
  const int64_t INF=std::numeric_limits<int64_t>::max()/8;
  size_t states=size_t(1)<<n;std::vector<int64_t> forced(n*n,INF);
  int64_t opt=INF;
  for(int root=0;root<n;++root){
    std::vector<int64_t> dp(states*n,INF);dp[(size_t(1)<<root)*n+root]=0;
    for(size_t mask=0;mask<states;++mask){
      if(!(mask&(size_t(1)<<root)))continue;
      for(int v=0;v<n;++v){
        auto a=dp[mask*n+v];if(a==INF)continue;
        size_t rem=(states-1)^mask;
        while(rem){int u=__builtin_ctzll(rem);rem&=rem-1;
          auto &dest=dp[(mask|(size_t(1)<<u))*n+u];
          dest=std::min(dest,a+c[v*n+u]);
        }
      }
    }
    for(int v=0;v<n;++v)if(v!=root){
      auto x=dp[(states-1)*n+v]+c[v*n+root];forced[root*n+v]=x;opt=std::min(opt,x);
    }
  }
  for(int u=0;u<n;++u)for(int v=0;v<n;++v)if(u!=v && forced[u*n+v]!=forced[v*n+u])return 4;
  std::cout<<opt<<'\n';
  for(int u=0;u<n;++u){for(int v=0;v<n;++v)std::cout<<(u==v?0:forced[u*n+v])<<' ';std::cout<<'\n';}
}
