/*
input :
1 1000

output :
25
 */

#include <iostream>
#include <cstring>
#define SZ (10000001)

using namespace std;
using ull = unsigned long long;

// 전역 변수 선언
bool IS_PRIME[SZ];
ull PRIME[SZ];

int cnt_primelike(ull p, ull L, ull R) {
    int cnt = 0;
    ull num = p * p;

    while (num < L) {
        num *= p;
    }
    while (num <= R) {
        cnt++;
        R = R / p;
    }
    return cnt;
}


int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    // 소수 전처리
    // 10^7 이하의 소수들
    memset(IS_PRIME, true, SZ);
    for (int i = 2; i < SZ; i++) {
        for (int j = i + i; j < SZ; j += i) {
            if (!IS_PRIME[i]) continue;
            IS_PRIME[j] = false;
        }
    }
    int idx = 0;
    for (int i = 2; i < SZ; i++) {
        if (IS_PRIME[i]) {
            PRIME[idx++] = i;
        }
    }

    ull L, R;
    cin >> L >> R;
    int cnt = 0;
    for (int i = 0; i < idx; i++) {
        if (PRIME[i] * PRIME[i] > R) {
            break;
        }
        cnt += cnt_primelike(PRIME[i], L, R);
    }
    cout << cnt << '\n';

    return 0;
}