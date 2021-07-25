/*
input :
26 11

output :
15 19
*/

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
using ll = long long;

// 전역 변수 선언
ll MOD, A;
ll Ap_inv, Am_inv;
vector<ll> ans;

vector<ll> xGCD(ll a, ll b){
    ll x0 = 1; ll x1 = 0;
    ll y0 = 0; ll y1 = 1;
    while (b != 0){
        ll tmp;
        ll q = a / b;
        tmp = a;
        a = b; b = tmp % b;

        tmp = x1;
        x1 = x0 - q * x1; x0 = tmp;
        tmp = y1;
        y1 = y0 - q * y1; y0 = tmp;
    }
    vector<ll> ret;
    ret.push_back(a); ret.push_back(x0); ret.push_back(y0);
    return ret;
}

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> MOD >> A;
    Ap_inv = (MOD - A + MOD) % MOD;

    Am_inv = -1;
    ans = xGCD(A, MOD);
    if (ans[0] != 1) cout << Ap_inv << ' ' << Am_inv;
    else cout << Ap_inv << ' ' << (ans[1] + MOD) % MOD;

    return 0;
}