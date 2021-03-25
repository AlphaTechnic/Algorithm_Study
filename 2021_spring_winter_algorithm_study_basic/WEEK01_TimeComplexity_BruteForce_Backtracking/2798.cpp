//
// Created by 김주호 on 2021/03/25.
//

#include <bits/stdc++.h>

using namespace std;
#define endl '\n'
#define FOR(i, n) for (int i= 0; i<n; i++)

int N, M, a[101], ans;

int main() {
    freopen("../input.txt", "r", stdin);
    cin >> N >> M;

    FOR(i, N) cin >> a[i];

    FOR(i, N) FOR(j, N) FOR(k, N)
        if (i != j && j != k && k != i) {
            int total = a[i] + a[j] + a[k];
            if (total <= M && ans < total) ans = total;
        }

    cout << ans << endl;
    return 0;
}