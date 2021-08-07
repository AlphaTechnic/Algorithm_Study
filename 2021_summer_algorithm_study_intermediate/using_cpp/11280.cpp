/*
input :
3 4
-1 2
-2 3
1 3
3 2

output :
1
*/

#include <iostream>
#include <algorithm>
#include <vector>
#define SZ (2 * 10000 + 5)
using namespace std;

// 전역 변수 선언
int N, M, cnt;
int SCC_NUM;
int NODE_NUM;

int dfn[SZ], low[SZ];
int scc[SZ], finished[SZ], ans[SZ];
vector<int> graph[SZ];
vector<int> ST;


bool comp(vector<int> vec1, vector<int> vec2){
    return vec1[0] < vec2[0];
}

void dfs(int s){
    dfn[s] = low[s] = ++NODE_NUM;
    ST.push_back(s);

    for (int nxt: graph[s]){
        if (dfn[nxt] == 0){ // 아직 방문이 안 되었다는 얘기
            dfs(nxt);
            low[s] = min(low[s], low[nxt]);
        }
        else{ // 방문한 곳을 또 방문. 즉, 부모쪽으로 다시 거슬러 올라간 상황
            if (finished[nxt]) continue;
            low[s] = min(low[s], dfn[nxt]);
        }
    }

    if (dfn[s] == low[s]){
        SCC_NUM++;

        while (true){
            int node = ST.back(); ST.pop_back();
            finished[node] = true;
            scc[node] = SCC_NUM;

            if (node == s) break;
        }
    }
}


int neg(int a){
    if (a <= N) {
        return a + N;
    }
    else {
        return a - N;
    }
}

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> N >> M;
    while (M--){
        int a, b; cin >> a >> b;
        if (a < 0) a = -a + N;
        if (b < 0) b = -b + N;
        graph[opp(a)].push_back(b);
        graph[opp(b)].push_back(a);
    }

    for (int i = 1; i <= 2 * N; i++){
        if (finished[i]) continue;

        dfs(i);
    }

    for (int i = 1; i <= N; i++){
        if (scc[i] == scc[i + N]){
            cout << '0' << '\n';
            return 0;
        }
    }
    cout << '1' << '\n';

    return 0;
}
