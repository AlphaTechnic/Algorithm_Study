/*
input :
15
1 2
1 3
2 4
3 7
6 2
3 8
4 9
2 5
5 11
7 13
10 4
11 15
12 5
14 7
6
6 11
10 9
2 6
7 6
8 13
8 15

output :
2
4
2
1
3
1
*/

#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
#include <map>

#define SZ (50005)
using namespace std;


// 전역 변수 선언
int V, Q;
vector<int> graph[SZ];
int depth[SZ];
int par[SZ];
bool vis[SZ];
map<pair<int, int>, int> cache;

void dfs(int cur, int dep) {
    vis[cur] = true;
    depth[cur] = dep;
    for (auto &nxt: graph[cur]) {
        if (vis[nxt]) continue;

        par[nxt] = cur;
        dfs(nxt, dep + 1);
    }
}

int LCA(int a, int b) {
    if (depth[b] > depth[a]) {
        swap(a, b);
    }

    while (depth[a] != depth[b]) {
        a = par[a];
    }
    while (a != b) {
        a = par[a];
        b = par[b];
    }
    return a;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> V;
    for (int i = 0; i < V - 1; i++) {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    memset(par, -1, sizeof(par));
    dfs(1, 1);

    cin >> Q;

    for (int i = 0; i < Q; i++) {
        int a, b;
        cin >> a >> b;
        if (cache[{a, b}] != 0) {
            cout << cache[{a, b}] << '\n';
            continue;
        }
        cache[{a, b}] = cache[{b, a}] = LCA(a, b);
        cout << cache[{a, b}] << '\n';
    }

    return 0;
}