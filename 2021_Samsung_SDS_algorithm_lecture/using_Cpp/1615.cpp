/*
input :
5 6
1 5
2 2
3 2
4 3
5 1
5 3

output :
8
*/

#include <iostream>
#include <algorithm>
#define PIV (1<<11)
using namespace std;
using ll = long long;

// 전역 변수 선언
struct l_and_r{
    int a, b;
};
l_and_r match[PIV * PIV];

int tree[2 * PIV];
int N, M;
ll ans;


void update(int i){
    i += PIV;
    tree[i] += 1;
    while(i >>= 1){
        tree[i] += 1;  // 누적 update
    }
}

int query(int l, int r){
    l += PIV, r += PIV;
    int ret = 0;

    while(l <= r){
        if ((l & 1)){ // 홀수
            ret += tree[l++];
        }
        if (!(r & 1)){
            ret += tree[r--];
        }
        l >>= 1, r >>= 1;
    }
    return ret;
}


bool operator<(l_and_r obj1, l_and_r obj2){
    if (obj1.a == obj2.a){
        return obj1.b < obj2.b;
    }
    return obj1.a < obj2.a;
}

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    freopen("input.txt", "r", stdin);

    cin >> N >> M;
    for (int i = 0; i < M; i++){
        cin >> match[i].a >> match[i].b;
    }
    sort(match, match + M);


    for (int i = 0; i < M; i++){
        ans += query(match[i].b + 1, N);
        update(match[i].b);
    }
    cout << ans << '\n';

    return 0 ;
}