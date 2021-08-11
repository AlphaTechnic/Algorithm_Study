/*
input :
3
3
2
1
2

output :
1/3
*/

#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;
using ll = long long;

// 전역 변수 선언
int N, K;
ll dp[1 << 15][100];
ll fact[16];
int nums_refined[15];
int pow_of_10[51];
string nums[15];

ll gcd(ll a, ll b){
    if (b == 0) return a;
    return gcd(b, a % b);
}

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> N;
    for (int i = 0; i < N; i++){
        cin >> nums[i];
    }
    cin >> K;

    for (int i = 0; i < N; i++){
        reverse(nums[i].begin(), nums[i].end());
    }

    // factorial 전처리
    fact[1] = 1;
    for (int i = 2; i <= 15; i++){
        fact[i] = fact[i - 1] * i;
    }

    // 10의 거듭제곱 % K
    pow_of_10[0] = 1;
    for (int i = 1; i < 51; i++){
        pow_of_10[i] = (pow_of_10[i - 1] * 10) % K;
    }

    // input data % K
    for (int i = 0; i < N; i++){
        int tot = 0;
        for (int j = 0; j < nums[i].length(); j++){
            tot += ((nums[i][j] - '0') * pow_of_10[j]) % K;
            tot %= K;
        }
        nums_refined[i] = tot;
    }


    // dp algorithm
    // dp[순열 seq][나머지]
    dp[0][0] = 1;
    for (int i = 0; i < (1 << N); i++){ // 모든 비트마스킹으로 표현된 state에 대하여
        for (int pre_remain = 0; pre_remain < K; pre_remain++){ // K로 나눈 나머지가 0, 1, 2, ..
            for (int kth = 0; kth < N; kth++){ // k번째 숫자 고르기
                if ((i & (1 << kth)) == 0){ // 상태 i에 k번째 수를 추가 -> 새로운 나머지를 탄생시킴

                    // 새로운 나머지
                    // = (현재 나머지 * 10^(새로 들어오는 수의 자리수)) + 새로 들어오는 수
                    int nxt_remain = (((pre_remain * pow_of_10[nums[kth].length()]) % K) + nums_refined[kth]) % K;

                    dp[i | (1 << kth)][nxt_remain] += dp[i][pre_remain];
                }
            }
        }
    }

    ll g = gcd(dp[(1 << N) - 1][0], fact[N]);
    cout << dp[(1 << N) - 1][0] / g << '/' << fact[N] / g << '\n';

    return 0;
}