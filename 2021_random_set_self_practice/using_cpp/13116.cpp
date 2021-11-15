/*
input :
3
33 79
9 15
1022 1023

output :
40
10
5110
 */
#include <iostream>
#include <algorithm>
#include <cmath>
#define LOG (10)

using namespace std;

// 전역 변수들 선언
int Q;

double logB(double a, double base) {
    return log(a) / log(base);
}

int LCA(int a, int b) {
    // 무족권 a를 더 깊게
    if (a < b) swap(a, b);

    // a를 b와 같은 레벨로 끌어 올림
    int dep_diff = (int)logB(a, 2) - (int)logB(b, 2);
    for (int i = LOG; i >= 0; i--) {
        if ((dep_diff & (1 << i)) == (1 << i)) {
            a /= (1 << (1 << i));  // means 2^(1<<i)
        }
    }

    // a와 b가 같아져보렸다면,
    if (a == b) return a;

    // a와 b가 같이 jump jump
    for (int i = LOG; i >= 0; i--) {
        if ((a >> 1) != (b >> 1)) {
            a >>= 1;
            b >>= 1;
        }
    }
    return a >> 1;
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> Q;
    int a, b;
    for (int i = 0; i < Q; i++) {
        cin >> a >> b;
        cout << LCA(a, b) * 10 << '\n';
    }

    return 0;
}