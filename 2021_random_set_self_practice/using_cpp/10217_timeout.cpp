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
using ll = long long;
#define SZ (105)
#define MAX (1000000000)

// 전역 변수 선언
int T;
int N, M, K;
int tm[SZ][SZ];
int cost[SZ][SZ];
bool vis[SZ];
int g_min_val = MAX;
vector<int> graph[SZ];


void dfs(int cur, int c, int t){
    vis[cur] = true;
    if (c > M){
        vis[cur] = false;
        return;
    }
    if (cur == N){
        g_min_val = min(g_min_val, t);
        vis[cur] = false;
    }

    for (int &nxt: graph[cur]){
        if (vis[nxt]) continue;

        dfs(nxt, c + cost[cur][nxt], t + tm[cur][nxt]);
    }
    vis[cur] = false;
}

void init(){
    memset(graph, {}, sizeof(graph));
    memset(tm, 0, sizeof(tm));
    memset(cost, 0, sizeof(cost));
    memset(vis, false, sizeof(vis));
    g_min_val = MAX;
}

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    freopen("input.txt", "r", stdin);

    cin >> T;
    while (T--){
        init();

        cin >> N >> M >> K;
        for (int i = 0; i < K; i++){
            int a, b, c, t;
            cin >> a >> b >> c >> t;
            graph[a].push_back(b);
            cost[a][b] = c;
            tm[a][b] = t;
        }

        dfs(1, 0, 0);  // S = 1, c = 0, t = 0

        if (g_min_val != MAX){
            cout << g_min_val << '\n';
        }
        else{
            cout << "Poor KCM" << '\n';
        }
    }
    return 0;
}