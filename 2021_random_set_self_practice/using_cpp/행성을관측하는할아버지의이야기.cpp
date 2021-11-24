/*
input :
4 3
1 3
2 3
4 2

output :
0 1
1 1
3 0
0 2
 */
#include <iostream>
#define INF (1 << 20)
#define SZ (205)

using namespace std;

// 전역 변수 선언
int V, E;
int a, b;
int dist_par[SZ][SZ];
int dist_chd[SZ][SZ];


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    for (int i = 0; i < SZ; i++){
        for (int j = 0; j < SZ; j++) {
            dist_par[i][j] = INF;
            dist_chd[i][j] = INF;
        }
    }

    cin >> V >> E;
    for (int i = 1; i <= E; i++) {
        cin >> a >> b;
        dist_par[b][a] = 1;
        dist_chd[a][b] = 1;
    }

    // 플로이드
    for (int k = 1; k <= V; k++) {
        for (int a = 1; a <= V; a++) {
            for (int b = 1; b <= V; b++) {
                dist_par[a][b] = min(dist_par[a][b], dist_par[a][k] + dist_par[k][b]);
                dist_chd[a][b] = min(dist_chd[a][b], dist_chd[a][k] + dist_chd[k][b]);
            }
        }
    }
    for (int v = 1; v <= V; v++) {
        int cnt_par = 0;
        int cnt_chd = 0;
        for (int nxt = 1; nxt <= V; nxt++) {
            if (dist_par[v][nxt] < INF) cnt_par++;
            if (dist_chd[v][nxt] < INF) cnt_chd++;
        }
        cout << cnt_par << ' ' << cnt_chd << '\n';
    }
}