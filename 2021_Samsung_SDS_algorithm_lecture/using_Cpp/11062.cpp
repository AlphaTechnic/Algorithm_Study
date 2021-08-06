/*
input :
2
4
1 2 5 2
9
1 1 1 1 2 2 2 2 2

output :
6
8
*/

#include <iostream>
#include <algorithm>
#include <memory.h>
using namespace std;

// 전역 변수 선언
int T, N;
int cards[1005];
int dp[1005][1005];

int recur(int l, int r){
    if (l > r) return 0;
    if (dp[l][r]) return dp[l][r];
    // 카드 2장 남음
    if (r - l <= 1) return dp[l][r] = max(cards[l], cards[r]);

    // 근우 왼 -> 승우 선택
    int case1 = cards[l] + min(recur(l + 2, r), recur(l + 1, r - 1));
    // 근우 오른 -> 승우 선택
    int case2 = cards[r] + min(recur(l, r - 2), recur(l + 1, r - 1));
    return dp[l][r] = max(case1, case2);
}


int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    freopen("input.txt", "r", stdin);

    cin >> T;
    while(T--){
        cin >> N;
        for (int i = 0; i < N; i++){
            cin >> cards[i];
        }
        memset(dp, 0, sizeof(dp));
        cout << recur(0, N - 1) << '\n';
    }

    return 0;
}