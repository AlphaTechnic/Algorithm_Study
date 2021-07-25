/*
input :
13 5 2 9

output :
2 5
*/

#include <iostream>
#include <algorithm>
using namespace std;
using ll = long long;

// 전역 변수 선언
ll m, seed, X1, X2;
ll a, b;

ll power(ll a, ll b){
    if (b == 0) return 1;

    if (b & 1 == 1) {
        ll num = power(a, b / 2);
        return ((num * num % m) * a) % m;
    }
    else {
        ll num = power(a, b / 2);
        return (num * num) % m;
    }
}

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> m >> seed >> X1 >> X2;
    a = (((X1 - X2 + m) % m) * power((seed - X1 + m) % m, m - 2)) % m;
    b = ((X1 - (a * seed) % m) + m) % m;
    cout << a << ' ' << b;

    return 0;
}