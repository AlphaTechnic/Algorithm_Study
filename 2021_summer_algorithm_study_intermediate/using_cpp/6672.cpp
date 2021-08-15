/*
input :
3 3
0 1
0 2
2 1
4 2
0 1
2 3
3 1
1 0
0 0

output :
1
2
2
*/

#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>

#define SZ (10005)
using namespace std;

typedef struct edge {
    int a, b;
};

// 전역 변수 선언
int V, E;
vector<int> graph[SZ];
vector<edge> BCC[SZ];
int dfn[SZ], low[SZ], child[SZ];
int AC[SZ];
vector<edge> ST;
int NODE_NUM, BCC_NUM;
int component_num;
int cnt[SZ];

void dfs(int p, int mp) {
    dfn[p] = low[p] = ++NODE_NUM;

    for (const int &chd: graph[p]) {
        if (chd == mp) continue;

        if (dfn[chd] == 0) {
            ST.push_back({p, chd});
            child[p]++;
            dfs(chd, p);
            low[p] = min(low[p], low[chd]);

            if (dfn[p] <= low[chd]) {
                if (mp != -1) AC[p] += 1;

                BCC_NUM++;
                while (true) {
                    edge ab = ST.back();
                    ST.pop_back();
                    BCC[BCC_NUM].push_back(ab);
                    if (ab.a == p && ab.b == chd) break;
                }
            }
        }
        else if (dfn[p] > dfn[chd]) {
            ST.push_back({p, chd});
            low[p] = min(low[p], dfn[chd]);
        }
    }
    if (mp == -1 && child[p] >= 2) {
        AC[p] += 1;
    }
}

void init() {
    for (int i = 0; i < V; i++) {
        graph[i].clear();
        BCC[i].clear();
    }
    ST.clear();
    memset(dfn, 0, sizeof(dfn));
    memset(low, 0, sizeof(low));
    memset(child, 0, sizeof(child));
    memset(AC, 0, sizeof(AC));
    memset(cnt, 0, sizeof(cnt));
    NODE_NUM = BCC_NUM = component_num = 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    while (true) {
        cin >> V >> E;
        if (V == 0 && E == 0) break;
        if (E == 0) {
            cout << V - 1 << '\n';
            continue; // 간선이 0개인 경우
        }

        init();

        for (int i = 0; i < E; i++) {
            int a, b;
            cin >> a >> b;
            graph[a].push_back(b);
            graph[b].push_back(a);
        }

        for (int i = 0; i < V; i++) {
            if (dfn[i]) continue;

            dfs(i, -1);
            component_num++;
        }

        // print ans
        int max_val = -1;
        for (int i = 0; i < V; i++){
            max_val = max(max_val, AC[i]);
        }
        cout << max_val + component_num << '\n';
    }

    return 0;
}