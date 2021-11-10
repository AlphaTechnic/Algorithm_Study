/*
input :
3

output :
6
 */
#include <iostream>
#include <cmath>

using namespace std;

// 전역 변수 선언
int N;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> N;
    if (N == 1) {
        cout << 0 << '\n';
        return 0;
    }

    cout << 2 * pow(3, N - 2) << '\n';

    return 0;
}