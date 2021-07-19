/*
input :
10 3
3
4
5
6
7
8
9
10
11
12

output :
60
*/

#include <iostream>
#include <algorithm>
using namespace std;
using ll = long long;

// 전역 변수 선언
#define PIV (1 << 18)
int N, K;
int mid;
ll ans;
int tree[2 * PIV];
int m[2 * PIV]; // sliding window로 이 전 값을 빼내야되기 때문에 정의


int query(int mid){
    int idx = 1;
    while (idx < PIV){
        if (tree[idx *= 2] < mid){
            mid -= tree[idx++];
        }
    }
    return idx - PIV;
}


void update(int num, int chk){
    num += PIV;
    tree[num] += chk;
    while (num >>= 1){
        tree[num] += chk;
    }
    
}

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    freopen("input.txt", "r", stdin);

    cin >> N >> K;
    for (int i = 0; i < K; i++){
        cin >> m[i];
        update(m[i], 1);
    }

    for (int i = 0; i <= N - K; i++){
        mid = query((K + 1) / 2);
        ans += mid;
        
        update(m[i], -1);
        cin >> m[i + K];
        update(m[i + K], 1);
    }
    cout << ans;

    return 0 ;
}