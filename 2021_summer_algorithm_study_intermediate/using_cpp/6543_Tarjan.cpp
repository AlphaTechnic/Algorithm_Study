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
int NODE_NUM;
vector<int> graph[5005];
vector<int> st;
int scc[5005];
int dfn[5005];
int low[5005];
bool finished[5005];

bool comp(vector<int> a, vector<int> b){
    if (a.size() == 0) return true;
    if (b.size() == 0) return false;
    return a[0] < b[0];
}

void dfs(int s){
    dfn[s] = low[s] = ++NODE_NUM;
    st.push_back(s);

    for (int nxt: graph[s]){
        if (dfn[nxt] == 0){
            dfs(nxt);
            low[s] = min(low[s], low[nxt]);
        }
        else{
            if (finished[nxt]) continue;

            low[s] = min(low[s], dfn[nxt]);
        }
    }

    if (low[s] == dfn[s]){
        SCC_NUM++;
        while (true){
            int node = st.back(); st.pop_back();
            finished[node] = true;
            scc[node] = SCC_NUM;

            if (node == s) break;
        }
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
        memset(scc, 0, sizeof(scc));
        memset(dfn, 0, sizeof(dfn));
        memset(low, 0, sizeof(low));
        memset(finished, false, sizeof(finished));
        SCC_NUM = 0; NODE_NUM = 0;

        cin >> V;
        if (V == 0) return 0;
        cin >> E;

        while(E--){
            int a, b;
            cin >> a >> b;
            graph[a].push_back(b);
        }

        for (int i = 0; i <= V; i++){
            if (finished[i]) continue;
            dfs(i);
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