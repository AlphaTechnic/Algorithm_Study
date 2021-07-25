/*
input :
5
5 2
5 3
10 5
20 10
10 0

output :
10
10
252
184756
1
*/

#include <iostream>
#include <algorithm>
using namespace std;
using ll = long long;

// 전역 변수 선언
ll Q, N, K;
ll A, B;
ll p = 1000000007;
ll fact[4000005];

ll power(ll a, ll b){
    if (b == 0) return 1;

    if (b % 2 == 1) {
        ll num = power(a, b / 2) % p;
        return (((num * num) % p) * a) % p;
    }
    else{
        ll num = power(a, b / 2) % p;
        return (num * num) % p;
    }
}


int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    // factorial 전처리
    fact[0] = fact[1] = 1;
    for (int i = 2; i <= 4000000; i++){
        fact[i] = (fact[i - 1] * (i % p)) % p;
    }

    cin >> Q;
    while (Q--){
        cin >> N >> K;

        A = fact[N];
        B = (fact[N - K] * fact[K]) % p;

        // 페르마의 소정리 -> a^(-1) = a^(p-2)
        cout << (A * power(B, p - 2)) % p << '\n';
    }
    return 0;
}