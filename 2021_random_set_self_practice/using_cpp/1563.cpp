/*
input :
4

output :
43
 */
#include <iostream>
#define MOD (1000000)
#define SZ (1005)

using namespace std;
using ll = long long;

// 전역 변수 선언
int N;
int dp[SZ][SZ][2][3];

ll recur(int day, int O, int L, int A) {
    if (L >= 2) return 0;
    if (A >= 3) return 0;
    if (day == N) return 1;
    if (dp[day][O][L][A] != 0) return dp[day][O][L][A];

    int a = recur(day + 1, O + 1, L, 0) % MOD;  // 참석
    int b = recur(day + 1, O, L + 1, 0) % MOD;  // 지각
    int c = recur(day + 1, O, L, A + 1) % MOD;  // 결석
    dp[day][O][L][A] = (a + b + c) % MOD;
    return dp[day][O][L][A];
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> N;
    cout << recur(0, 0, 0, 0);
}