/*
input :
5 60
30 10 20 35 40
3 0 3 5 4

output :
6
*/

#include <iostream>
#include <algorithm>
using namespace std;
using ll = long long;

// 전역 변수 선언
int N, M;
int MEM[105];
int costs[105];
int dp[105][10005];
int res;

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    freopen("input.txt", "r", stdin);

    cin >> N >> M;
    if (M == 0) {
        cout << 0; return 0;
    }
    for (int i = 1; i <= N; i++){
        cin >> MEM[i];
    }
    for (int i = 1; i <= N; i++){
        cin >> costs[i];
        res += costs[i];
    }

    for (int i = 1; i <= N; i++){
        for (int j = 1; j <= res; j++){
            if (j < costs[i]){ // i번째 MEM 안 넣음
                dp[i][j] = dp[i - 1][j];
            }
            else{
                dp[i][j] = max(dp[i - 1][j - costs[i]] + MEM[i], dp[i - 1][j]);
            }

            if (dp[i][j] >= M){
                res = min(res, j);
            }
        }
    }
    cout << res;

    return 0;
}