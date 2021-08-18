/*
input :
4 3
1 4 L
2 3 T
4 1 T

output :
2
*/

#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#define SZ (1005)
using namespace std;

// 전역 변수 선언
int V, E;
int cnt;
int adj_mat[SZ][SZ];
int visited[SZ];
vector<int> st;

bool dfs(int p, int val){
    st.push_back(p);
    visited[p] = val;

    while (!st.empty()){
        int cur = st.back(); st.pop_back();
        for (int nxt = 1; nxt <= V; nxt++){
            if (adj_mat[cur][nxt] == -1) continue;
            if (adj_mat[cur][nxt] == 'L'){
                if (!visited[nxt]){
                    visited[nxt] = visited[cur] * (-1);
                    st.push_back(nxt);
                }
                else{
                    if (visited[nxt] != visited[cur] * (-1)) return false;
                }
            }
            else if (adj_mat[cur][nxt] == 'T'){
                if (!visited[nxt]){
                    visited[nxt] = visited[cur];
                    st.push_back(nxt);
                }
                else{
                    if (visited[nxt] != visited[cur]) return false;
                }
            }
        }
    }
    return true;
}

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> V >> E;
    cnt = 0;
    memset(adj_mat, -1, sizeof(adj_mat));

    for (int i = 0; i < E; i++){
        int a, b;
        char ANS;
        cin >> a >> b >> ANS;

        if (adj_mat[a][b] == -1){
            adj_mat[a][b] = ANS;
            adj_mat[b][a] = ANS;
        }
        else if (adj_mat[a][b] != ANS) break;

        memset(visited, 0, sizeof(visited));
        if (!dfs(a, -1)){
            break;
        }
        else{
            cnt += 1;
        }
    }
    cout << cnt;
    return 0;
}