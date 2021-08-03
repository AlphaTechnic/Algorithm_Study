/*
input :
9

output :
55
*/

#include <iostream>
#include <algorithm>
using namespace std;
using ll = long long;

// 전역 변수 선언
int N;
ll dp[1005];
int MOD = 10007;

ll fibo(int num){
    if (num == 0) return 1;
    if (num == 1) return 1;
    if (dp[num]) return dp[num];

    return dp[num] = ((fibo(num - 1)) % MOD + (fibo(num - 2)) % MOD) % MOD;
}

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> N;
    cout << fibo(N);

    return 0;
}