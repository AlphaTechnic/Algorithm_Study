/*
input :
21 6 12
1 9
1 10
10 12
2 13
13 11
11 12
3 8
8 7
8 12
5 19
5 14
14 12
6 20
6 21
20 15
15 12
4 18
4 17
17 16
16 12

output :
16
*/

#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#define SZ (328005)
using namespace std;

// 전역 변수 선언
int V, S, R;
vector<int> graph[SZ];
vector<int> dfs_tree[SZ];
vector<int> res;

void gen_dfs_tree(int p, int mp){
    if (1 <= p <= S) return;

    for (int &chd: graph[p]){
        if (chd == mp) continue;
        dfs_tree[p].push_back(chd);
        gen_dfs_tree(chd, p);
    }
}

void bfs(int R){
    queue<pair<int, int>> que;
    que.push({R, 0});

    while (!que.empty()){
        pair<int, int> cur_dep = que.front(); que.pop();
        for (int &chd: graph[cur_dep.first]){
            if (1 <= chd && chd <= S){
                res.push_back(cur_dep.second + 1);
                if (res.size() == 2){
                    return;
                }
            }
            que.push({chd, cur_dep.second + 1});
        }
    }
    return;
}

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> V >> S >> R;
    for (int i = 0; i < V - 1; i++){
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    gen_dfs_tree(R, -1);

    bfs(R);
    cout << V - (res[0] + res[1]) - 1 << '\n';

    return 0;
}