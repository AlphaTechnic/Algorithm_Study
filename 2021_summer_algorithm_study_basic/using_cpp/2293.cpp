/*
input :
3 10
1
2
5

output :
10
*/

#include <iostream>
#include <algorithm>
using namespace std;

// 전역 변수 선언
int dp[10001] = {1};
int coin[101];

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    int n, k;
    cin >> n >> k;

    for (int i = 1; i <=n; i++){
        cin >> coin[i];
        for (int j = coin[i]; j <= k; j++){
            dp[j] += dp[j - coin[i]];
        }
    }
    cout << dp[k] << '\n';

    return 0;
}