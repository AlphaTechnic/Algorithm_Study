/*
input:
2 3 1

output :
11
*/

#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

// 전역 변수 선언
int N, qr, qc;
int cnt;

void recur(int r, int c, int SZ){
    if (SZ == 1){
        cnt += 1;
        if (r == qr && c == qc) cout << cnt - 1;
        return;
    }
    recur(r, c, SZ / 2);
    recur(r, c + SZ / 2, SZ / 2);
    recur(r + SZ / 2, c, SZ / 2);
    recur(r + SZ / 2, c + SZ / 2, SZ / 2);
}

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> N >> qr >> qc;
    recur(0, 0, pow(2, N));

    return 0;
}