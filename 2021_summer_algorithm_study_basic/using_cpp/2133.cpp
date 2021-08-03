/*
input :
2

output :
3
*/

#include <iostream>
#include <algorithm>
using namespace std;

// 전역 변수 선언
int N;
int dp[35] = {1, 0, 3};

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> N;
    for (int i = 4; i <= N; i += 2){
        dp[i] = 3 * dp[i - 2];
        for (int j = 4; j <= i; j += 2){
            dp[i] += 2 * dp[i - j];
        }
    }
    cout << dp[N];

    return 0;
}