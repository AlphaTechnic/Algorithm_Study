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
int SCC_NUM;
int node_num;
int a, b;

vector<int> graph[10005];
int dfn[10005];
int low[10005];
bool finished[10005];
int scc[10005];
vector<int> st;
vector<vector<int>> ans;


bool comp(vector<int> a, vector<int> b){
    return a[0] < b[0];
}


void dfs(int s){
    dfn[s] = low[s] = ++node_num;
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


    if (dfn[s] == low[s]){
        SCC_NUM++;

        vector<int> tmp;
        while (true){
            int nxt = st.back(); st.pop_back();
            tmp.push_back(nxt);
            scc[nxt] = SCC_NUM;
            finished[nxt] = true;

            if (nxt == s) break;
        }
        sort(tmp.begin(), tmp.end());
        ans.push_back(tmp);
    }
}


int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);

    cin >> V >> E;
    while(E--){
        cin >> a >> b;
        graph[a].push_back(b);
    }

    for (int i = 1; i <= V; i++){
        if (finished[i]) continue;

        dfs(i);
    }
    sort(ans.begin(), ans.end(), comp);

    cout << SCC_NUM << '\n';
    for (vector<int> nodes: ans){
        for (int i = 0; i < nodes.size(); i++){
            cout << nodes[i] << ' ';
        }
        cout << "-1\n";
    }
    return 0;
}