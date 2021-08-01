/*
input :
3 3
1 3 2 3 3 1
2 1
1 2
0

output :
1 3
2
*/

#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
using namespace std;

// 전역 변수 선언
int V, E;
int SCC_NUM;
vector<int> graph[5005];
vector<int> graph_inv[5005];
vector<int> st;
bool visited[5005];
int scc[5005];

bool comp(vector<int> a, vector<int> b){
    if (a.size() == 0) return true;
    if (b.size() == 0) return false;
    return a[0] < b[0];
}

void dfs1(int s){
    visited[s] = true;
    for (int nxt: graph[s]){
        if (visited[nxt]) continue;
        dfs1(nxt);
    }
    st.push_back(s);
}

void dfs2(int s){
    scc[s] = SCC_NUM;
    for (int nxt: graph_inv[s]){
        if (scc[nxt] != 0) continue;

        dfs2(nxt);
    }
}

bool sink_chk(vector<int> group){
    int group_scc = scc[group[0]];
    for (int node: group){
        for (int adj: graph[node]){
            if (scc[adj] != group_scc) return false;
        }
    }
    return true;
}

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    while (true){
        for (auto& nodes: graph) nodes.clear();
        for (auto& nodes: graph_inv) nodes.clear();
        memset(visited, false, sizeof(visited));
        memset(scc, 0, sizeof(scc));
        SCC_NUM = 0;

        cin >> V;
        if (V == 0) return 0;
        cin >> E;

        while(E--){
            int a, b;
            cin >> a >> b;
            graph[a].push_back(b);
            graph_inv[b].push_back(a);
        }

        // stack에 넣는 코사라주 dfs1()
        for (int i = 1; i <= V; i++){
            if (visited[i]) continue;

            dfs1(i);
        }

        // stack에서 빼면서 역간선 graph에 대해 dfs2()
        while (!st.empty()){
            int cur = st.back(); st.pop_back();
            if (scc[cur]) continue;

            SCC_NUM++;
            dfs2(cur);
        }

        // SCC 결과 생성
        vector<int> res[5005];
        for (int i = 1; i <= V; i++){
            res[scc[i]].push_back(i);
        }
        sort(res + 1, res + SCC_NUM + 1, comp);

        // 하나의 scc그룹이 outdegree가 없는지 체크하고, 없으면 ans에 넣음
        vector<int> ans;
        for (vector<int> group: res){
            if (group.size() == 0) continue;
            if (!sink_chk(group)) continue;

            for (int i: group) ans.push_back(i);
        }
        sort(ans.begin(), ans.end());

        for (int node: ans){
            cout << node << ' ';
        }
        cout << '\n';
    }
}