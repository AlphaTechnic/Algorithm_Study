/*
input :
5
8 9 1 2 10

output:
3
*/

#include <iostream>
#include <algorithm>
using namespace std;

// 전역 변수 선언
int N;
int nums[1005];
int dp[1005];

bool comp(int a, int b){
    return true;
}

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> N;
    for (int i = 0; i < N; i++){
        cin >> nums[i];
    }
    for (int i = 0; i < N; i++){
        dp[i] = 1;
    }

    for (int i = 1; i <= N; i++){
        for (int j = 0; j < i; j++){
            if (nums[j] < nums[i]){
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
    }
    int max_val = 0;
    for (int i = 0; i < N; i++){
        max_val = max(max_val, dp[i]);
    }
    cout << max_val;

    return 0;
}