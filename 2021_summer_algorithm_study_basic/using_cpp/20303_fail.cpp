/*
input :
10 6 6
9 15 4 4 1 5 19 14 20 5
1 3
2 5
4 9
6 2
7 8
6 10

output :
57
*/

#include <iostream>
#include <algorithm>
#include <vector>
#define SZ (30005)
using namespace std;

// 전역 변수 선언
int V, E, K;
int node_vals[SZ];
vector<int> graph[SZ];
vector<int> P;
vector<int> W;
bool visited[SZ];
int cnt, tot;
int dp[SZ][3001];


void dfs(int p){
    visited[p] = true;
    cnt += 1; tot += node_vals[p];
    for (int &nxt: graph[p]){
        if (visited[nxt]) continue;
        dfs(nxt);
    }
}


int recur(int i, int w){
    if (i == P.end() - P.begin()){
        return 0;
    }
    if (dp[i][w]) return dp[i][w];

    int case1 = 0;
    if (w + W[i] < K){
        case1 = P[i] + recur(i + 1, w + W[i]);
    }
    int case2 = recur(i + 1, w);

    dp[i][w] = max(case1, case2);
    return dp[i][w];
}


int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> V >> E >> K;
    for (int i = 1; i <= V; i++){
        cin >> node_vals[i];
    }

    for (int i = 0; i < E; i++){
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    for (int i = 1; i <= V; i++){
        if (visited[i]) continue;

        cnt = 0; tot = 0;
        dfs(i);
        P.push_back(tot);
        W.push_back(cnt);
    }


    // 여기서부터 그냥 냅색문제
    // dp[i][j] : i번째 보석까지 봄. j 무게 제한인 상황에서 뽑아내는 최대 가치

    // 탑다운 터짐
//    cout << recur(0, 0);

    // 바텀 업
    int leng = P.end() - P.begin();
    for (int i = 0; i < leng; i++){
        for (int j = 0; j < 3001; j++){
            if (W[i] < j){
                dp[i][j] = max(P[i] + dp[i - 1][j - W[i]], dp[i - 1][j]);
            }
            else {
                dp[i][j] = dp[i - 1][j];
            }
        }
    }
    cout << dp[leng - 1][K];

    return 0;
}