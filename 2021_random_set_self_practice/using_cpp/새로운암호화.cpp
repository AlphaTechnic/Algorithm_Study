/*
input :
2 4

output :
5
 */

#include <iostream>

using namespace std;
using ll = long long;

ll cum_xor(ll number) {
    // 0 ~ number까지 cum_xor
    ll cum_xor;
    ll grp_num;
    if ((number & 1) == 1) {
        grp_num = (number + 1) / 2;
        cum_xor = ((grp_num & 1) == 1) ? 1 : 0;
    }
    else {
        grp_num = number / 2;
        cum_xor = ((grp_num & 1) == 1) ? 1 ^ number : 0 ^ number;
    }
    return cum_xor;
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    ll a, b;
    cin >> a >> b;

    ll res = cum_xor(b) ^ cum_xor(a - 1);
    cout << res << '\n';

    return 0;
}