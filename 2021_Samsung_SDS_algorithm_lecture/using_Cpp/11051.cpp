/*
input :
5 2

output :
10
*/

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

// 전역 변수 선언
int MOD = 10007;
int N, K;
int cache[1001][1001];

int recur(int n, int k){
    if (k == 0) return 1;
    if (n == k) return 1;

    if (cache[n][k] != 0) return cache[n][k];

    cache[n][k] = (recur(n - 1, k) + recur(n - 1, k - 1)) % MOD;
    return cache[n][k];
}

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    freopen("input.txt", "r", stdin);

    cin >> N >> K;
    cout << recur(N, K);
    return 0 ;
}