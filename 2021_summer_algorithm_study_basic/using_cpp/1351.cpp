/*
input :
7 2 3

output :
7
*/

#include <iostream>
#include <algorithm>
#include <map>
using namespace std;
using ll = long long;

// 전역 변수 선언
ll N, P, Q;
map<ll, ll> dp;

ll recur(ll num){
    if (num == 0) return 1;
    if (dp.find(num) != dp.end()) return dp[num];

    return dp[num] = recur(num / P) + recur(num / Q);
}


int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> N >> P >> Q;
    cout << recur(N);

    return 0;
}