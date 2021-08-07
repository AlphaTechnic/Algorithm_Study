/*
input :
2 1
1 1
-1 -1

output :
OTL
*/

#include <iostream>
#include <algorithm>
#include <vector>
#define SZ (2 * 10000 + 5)
using namespace std;

// 전역 변수 선언
int N, M;
int SCC_NUM, NODE_NUM;
vector<int> graph[SZ];
int scc[SZ], dfn[SZ], low[SZ];
vector<int> ST;
bool finished[SZ];

void dfs(int s){
    dfn[s] = low[s] = ++NODE_NUM;
    ST.push_back(s);

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
        while (true){
            int node = ST.back(); ST.pop_back();
            scc[node] = SCC_NUM;
            finished[node] = true;

            if (node == s){
                break;
            }
        }
    }
}

int neg(int a){
    if (a <= N) return a + N;
    else return a - N;
}

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> M >> N;
    for (int i = 0; i < M; i++){
        int a, b;
        cin >> a >> b;
        if (a < 0) a = -a + N;
        if (b < 0) b = -b + N;
        graph[neg(a)].push_back(b);
        graph[neg(b)].push_back(a);
    }

    // 타잔 알고리즘 실행 -> scc가 만들어짐
    for (int i = 1; i <= 2 * N; i++){
        if (finished[i]) continue;
        dfs(i);
    }

    for (int i = 1; i <= N; i++){
        if (scc[i] == scc[i + N]){
            cout << "OTL" << '\n';
            return 0;
        }
    }
    cout << "^_^" << '\n';

    return 0;
}