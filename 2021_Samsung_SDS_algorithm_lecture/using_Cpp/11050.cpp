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
int N, K;
int nCk(int N, int K){
    int ans = 1;

    for(int i = 1, j = N; i <= K; i++, j--){
        ans *= j;
        ans /= i;
    }
    return ans;
}

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    freopen("input.txt", "r", stdin);

    cin >> N >> K;
    cout << nCk(N, K);
    return 0 ;
}