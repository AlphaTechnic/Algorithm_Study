/*
input :
15 15

output :
43688
*/

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

// 전역 변수 선언
int w, h;
int dp[102][102][2][2];
int MOD = 100000;


int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    freopen("input.txt", "r", stdin);

    cin >> w >> h;

    // 3번째 index : 0 - from 아래, 1 - from 왼
    // 4번째 index : 0 - 회전 불가, 1 - 회전 가능
    dp[1][1][0][0] = dp[1][1][1][0] = 1;
    for (int y = 1; y <= h; y++){
        for (int x = 1; x <= w; x++){
            dp[y][x][0][0] %= MOD;
            dp[y][x][0][1] %= MOD;
            dp[y][x][1][0] %= MOD;
            dp[y][x][1][1] %= MOD;
            dp[y + 1][x][0][0] = dp[y][x][1][1];
            dp[y + 1][x][0][1] = dp[y][x][0][1] + dp[y][x][0][0];
            dp[y][x + 1][1][0] = dp[y][x][0][1];
            dp[y][x + 1][1][1] = dp[y][x][1][0] + dp[y][x][1][1];
        }
    }
    cout << (dp[h][w][0][0] + dp[h][w][0][1] + dp[h][w][1][0] + dp[h][w][1][1]) % MOD << "\n";

    return 0 ;
}