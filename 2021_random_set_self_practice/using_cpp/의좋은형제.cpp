/*
input :
100 100
4

output :
131 69
 */

#include <iostream>

using namespace std;

// 전역변수 선언
int a, b;
int N;

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> a >> b;
    cin >> N;

    int Q;
    while (true) {
        Q = (a & 1 == 1) ? (a + 1) / 2 : a / 2;
        a -= Q;
        b += Q;
        N--;
        if (N == 0) break;


        Q = (b & 1 == 1) ? (b + 1) / 2 : b / 2;
        b -= Q;
        a += Q;
        N--;
        if (N == 0) break;
    }
    cout << a << ' ' << b << '\n';

    return 0;
}

