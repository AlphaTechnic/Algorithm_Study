/*
input :
13

output :
5
 */
#include <iostream>

using namespace std;

// 전역 변수 선언
int N;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    //freopen("input.txt", "r", stdin);

    cin >> N;
    if (N == 1 || N == 3) {
        cout << -1 << '\n';
        return 0;
    }

    int cnt = 0;
    while (N % 5 != 0) {
        N -= 2;
        cnt++;
    }
    cnt += (N / 5);
    cout << cnt << '\n';

    return 0;
}