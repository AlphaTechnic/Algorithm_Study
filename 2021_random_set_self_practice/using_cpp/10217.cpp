/*
input :
2
3 100 3
1 2 1 1
2 3 1 1
1 3 3 30
4 10 4
1 2 5 3
2 3 5 4
3 4 1 5
1 3 10 6

output :
2
Poor KCM
*/

#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>

using namespace std;
#define SZ (105)
#define MAX (1000000000)

// 전역 변수 선언
typedef struct edge{
    int to;
    int c;
    int t;
}edge;


int T;
int N, M, K;
int dp[SZ][10005];
vector<edge> graph[SZ];


int recur(int cur, int c) {
    if (c > M) {
        return MAX;
    }
    if (cur == N) {
        return 0;
    }
    if (dp[cur][c] != -1) {
        return dp[cur][c];
    }

    int ret = MAX;
    for (auto & edge: graph[cur]) {
        ret = min(ret, recur(edge.to, c + edge.c) + edge.t);
    }
    dp[cur][c] = ret;

    return dp[cur][c];
}

void init() {
    for (auto & vec : graph){
        vec.clear();
    }
    memset(dp, -1, sizeof(dp));
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> T;
    while (T--) {
        init();

        cin >> N >> M >> K;
        for (int i = 0; i < K; i++) {
            int a, b, c, t;
            cin >> a >> b >> c >> t;
            edge info = {b, c, t};
            graph[a].push_back(info);
        }

        int ans = recur(1, 0);  // S = 1, c = 0

        if (ans != -1 && ans < MAX) {
            cout << ans << '\n';
        }
        else {
            cout << "Poor KCM" << '\n';
        }
    }
    return 0;
}