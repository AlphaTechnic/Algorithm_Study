/*
input :
239

output :
9
*/

#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
using namespace std;

// 전역 변수 선언
int N;
int dp[1000005];
int ans[1000005];

int recur(int x){
    if (dp[x] != -1) return dp[x];
    if (x <= 9) return dp[x] = 0;

    vector<int> sub_nums;
    int power_of_10 = 10;
    while (power_of_10 <= x){
        int tmp = x;
        while (tmp){
            sub_nums.push_back(tmp % power_of_10);
            tmp /= 10;
        }
        power_of_10 *= 10;
    }

    dp[x] = 0;
    sort(sub_nums.begin(), sub_nums.end());
    sub_nums.erase(unique(sub_nums.begin(), sub_nums.end()), sub_nums.end());
    for (int i = 0; i < sub_nums.size(); i++){
        // x인 상황이 필승포지션으로 결론 났다면, 혹시 패배하는 경우가 있는지를 들여다 볼 필요가 없다.
        if (dp[x] == 1) break;

        if (sub_nums[i] == 0) continue;
        if (sub_nums[i] == x) continue;

        // x - sub_nums[i]인 상황에서 패배하는 경우가 단 하나라도 있다면, x인 상황은 필승 포지션
        dp[x] = dp[x] | !recur(x - sub_nums[i]);

        if (dp[x] == 1) ans[x] = sub_nums[i];
    }
    return dp[x];
}

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> N;
    memset(dp, -1, sizeof(dp));
    memset(ans, -1, sizeof(ans));

    recur(N);
    cout << ans[N] << '\n';

    return 0;
}