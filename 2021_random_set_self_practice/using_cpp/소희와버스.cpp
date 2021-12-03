/*
input :
5 5
3 3
2 5
5 6
4 9
6 1

output :
3
 */
#include <iostream>
#include <vector>

using namespace std;

// 전역 변수 선언
int N, T;


int min_wait_time(int T, int s, int p) {
    if (T <= s) {
        return s - T;
    }
    int remain = (T - s) % p;
    return remain == 0 ? 0 : p - remain;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> N >> T;
    int s, p;
    int val;
    int mnv = 100005;
    int idx_of_mnv = -1;
    for (int i = 0; i < N; i++) {
        cin >> s >> p;
        val = min_wait_time(T, s, p);
        if (val < mnv) {
            mnv = val;
            idx_of_mnv = i + 1;
        }
    }

    cout << idx_of_mnv << '\n';

    return 0;
}