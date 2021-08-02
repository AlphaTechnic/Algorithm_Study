/*
input :
13 5
4 6 7 11 12

output :
62000
*/

#include <iostream>
#include <algorithm>
using namespace std;

// 전역 변수 선언
int N, M;
bool DAY_OFF[105];
int dp[105][105];

int recur(int day, int coupon){
    if (day >= N + 1) return 0;
    if (dp[day][coupon] != -1) return dp[day][coupon];

    int ret;
    if (DAY_OFF[day]){
        ret = recur(day + 1, coupon);
    }
    else{
        int a = recur(day + 1, coupon) + 10000;
        int b = recur(day + 3, coupon + 1) + 25000;
        int c = recur(day + 5, coupon + 2) + 37000;
        ret = min(min(a, b), c);

        if (coupon >= 3){
            ret = min(ret, recur(day + 1, coupon - 3));
        }
    }
    dp[day][coupon] = ret;
    return dp[day][coupon];
}

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> N >> M;
    while (M--){
        int num; cin >> num;
        DAY_OFF[num] = true;
    }

    // dp 테이블 초기화
    for (int i = 0; i <= N; i++){
        for (int j = 0; j <= N; j++){
            dp[i][j] = -1;
        }
    }

    cout << recur(1, 0);

    return 0;
}