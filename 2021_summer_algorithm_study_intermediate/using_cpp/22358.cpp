/*
input :
3 2 1 1 3
1 2 10
2 3 5

output :
25
*/

#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
using namespace std;
using ll = long long;

typedef struct nd2cost{
    int nd, cost;
}nd2cost;

// 전역 변수 선언
int V, E, S, K, TAR;
vector<nd2cost> graph[100005];
ll dp[100005][11];
ll ans = -1;

ll recur(int cur, int cnt){
    if (cnt > K) return -1e16;
    if (cnt == K && cur == TAR) return 0;
    if (dp[cur][cnt] != -1) return dp[cur][cnt];

    ll ret = -1e16;
    for (nd2cost nxt: graph[cur]){
        if (cnt < K && nxt.nd < cur){ // 리프트 타고 올라감
            ret = max(ret, recur(nxt.nd, cnt + 1));
        }
        else if (nxt.nd > cur){ // 스키
            ret = max(ret, recur(nxt.nd, cnt) + nxt.cost);
        }
    }
    dp[cur][cnt] = ret;
    return dp[cur][cnt];
}

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> V >> E >> K >> S >> TAR;
    while(E--){
        int a, b, cost;
        cin >> a >> b >> cost;
        graph[a].push_back({b, cost});
        graph[b].push_back({a, cost});
    }
    memset(dp, -1, sizeof(dp));
    ll ans = recur(S, 0);

    if (ans < 0){
        cout << -1 << '\n';
    }
    else{
        cout << ans;
    }


    return 0;
}