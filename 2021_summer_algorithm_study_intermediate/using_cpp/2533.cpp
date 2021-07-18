/*
input :
8
1 2
1 3
1 4
2 5
2 6
4 7
4 8

output :
3
 */

#include <iostream>
#include <vector>
using namespace std;

int N;
int a, b;
vector<int> graph[1000005];
bool visited[1000005];
int dp[1000005][2];


void gen_dp(int root){
    visited[root] = true;
    dp[root][0] = 0;
    dp[root][1] = 1;

    for (int child : graph[root]){
        if (visited[child]) continue;

        gen_dp(child);
        dp[root][0] += dp[child][1];
        dp[root][1] += min(dp[child][0], dp[child][1]);
    }
}


int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    freopen("input.txt", "r", stdin);

    cin >> N;
    while (N != 1){
        N--;

        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    gen_dp(1);
    cout << min(dp[1][0], dp[1][1]);

    return 0;
}