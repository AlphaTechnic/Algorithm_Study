/*
input :
4

output :
3
*/

#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
using namespace std;

// 전역 변수 선언
int N;
int dp[1005][1005];
bool is_prime[1000000];

int cal(int a, int b){
    string ans;
    ans = to_string(a) + to_string(b);
    return stoi(ans);
}

int recur(int a, int b){
    if (a == 1 && b == 1) return 0;
    if (dp[a][b] != -1) return dp[a][b];

    int case1 = 0, case2 = 0;
    if (is_prime[cal(a, b)]){
        if (a > 1) case1 = recur(a - 1, b) + 1;
        if (b > 1) case2 = recur(a, b - 1) + 1;
    }
    else{
        if (a > 1) case1 = recur(a - 1, b);
        if (b > 1) case2 = recur(a, b - 1);
    }
    dp[a][b] = max(case1, case2);
    return dp[a][b];
}

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    // 소수 전처리
    memset(is_prime, true, sizeof(is_prime));
    for (int i = 2; i < 1000000; i++){
        for (int j = i + i; j < 1000000; j += i){
            if (!is_prime[j]) continue;

            is_prime[j] = false;
        }
    }

    // dp[i][j] : i원, j원이 들어있는 상황까지 왔을 때, 지나온 소수 개수의 최대값
    memset(dp, -1, sizeof(dp));
    cin >> N;
    cout << recur(N, N);

    return 0;
}