/*
input :
7 9
1 4
4 5
5 1
1 6
6 7
2 7
7 3
3 7
7 2

output :
3
1 4 5 -1
2 3 7 -1
6 -1
*/

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

// 전역 변수 선언
int V, E;
int a, b;
int SCC_NUM;
vector<int> graph[10005]; // 10005
vector<int> graph_inv[10005]; // 10005
bool visited[10005]; // 10005
int scc[10005]; // 10005
vector<int> st;
vector<int> ans[10005]; // 10005

bool comp(vector<int> a, vector<int> b){
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

    ans[SCC_NUM].push_back(s);
    for (int nxt: graph_inv[s]){
        if (scc[nxt]) continue;

        dfs2(nxt);
    }
}

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> V >> E;
    for (int i = 0; i < E; i++){
        cin >> a >> b;
        graph[a].push_back(b);
        graph_inv[b].push_back(a);
    }

    for (int i = 1; i <= V; i++){
        if (visited[i]) continue;

        dfs1(i);
    }

    while(!st.empty()){
        int p = st.back(); st.pop_back();
        if (scc[p]) continue;

        SCC_NUM++;
        dfs2(p);
        sort(ans[SCC_NUM].begin(), ans[SCC_NUM].end());
    }
    sort(ans + 1, ans + SCC_NUM + 1, comp);

    cout << SCC_NUM << '\n';
    for (int i = 1; i <= SCC_NUM; i++){
        for (int j = 0; j < ans[i].size(); j++){
            cout << ans[i][j] << ' ';
        }
        cout << "-1\n";
    }

    return 0;
}