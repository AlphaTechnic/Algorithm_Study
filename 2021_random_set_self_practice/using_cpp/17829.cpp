/*
input :
4
-6 -8 7 -4
-5 -5 14 11
11 11 -1 -1
4 9 -2 -4

output :
11
 */
#include <iostream>
#include <algorithm>
#define SZ (1029)

using namespace std;

// 전역 변수 선언
int N;
int bd[SZ][SZ];


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> N;
    for (int r = 0; r < N; r++) {
        for (int c = 0; c < N; c++) {
            cin >> bd[r][c];
        }
    }

    int ansr = 0;
    int ansc = 0;
    int rsave = 0;
    int csave = 0;
    int iter = N / 2;
    for (int k = 0; k < iter; k++) {
        while (rsave < N) {
            int r = rsave;
            int c = csave;
            while (c < N) {
                int arr[4];
                int idx = 0;
                for (int i = r; i < r + 2; i++) {
                    for (int j = c; j < c + 2; j++) {
                        arr[idx++] = bd[i][j];
                    }
                }
                sort(arr, arr + 4);
                bd[ansr][ansc++] = arr[2];
                c += 2;
            }
            rsave += 2;
            ansr++;
            ansc = 0;
        }
        ansr = ansc = rsave = csave = 0;
        N = N / 2;
    }
    cout << bd[0][0] << '\n';

    return 0;
}