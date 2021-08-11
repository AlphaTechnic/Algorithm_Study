/*
input :
4
1 2 3 4
4
1 2 3 1
5
5 1 2 3 6
14
8 7 1 4 3 5 4 1 6 8 10 4 6 5
5
1 3 5 1 3
0

output :
4
4
2
12
0
*/

#include <iostream>
#include <algorithm>
#include <cstring>
#include <cmath>
using namespace std;

// 전역 변수 선언
int N;
int nums[305];
int dp[305][305];

int recur(int l, int r) {
    // dp[l][r] : l에서 r까지 없앨 수 있는 최대 수
    if (dp[l][r] != -1) return dp[l][r];

    // base case
    int len = r - l  + 1;
    int diff = abs(nums[r] - nums[l]);
    if (len == 1) return 0;
    if (len == 2) return dp[l][r] = diff < 2? 2 : 0;

    int in_val = recur(l + 1, r - 1);
    if (diff < 2 && in_val == len - 2) dp[l][r] = max(dp[l][r], in_val + 2);

    for (int k = l; k < r; k++) {
        dp[l][r] = max(dp[l][r], recur(l, k) + recur(k + 1, r));
    }

    return dp[l][r];
}


int main()
{
    ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    while (true){
        cin >> N;
        if (N == 0) break;

        memset(dp, -1, sizeof(dp));
        for (int i = 0; i < N; i++){
            cin >> nums[i];
        }
        cout << recur(0, N - 1) << '\n';
    }
    return 0;
}