/*
input :
5 2 2
1
2
3
4
5
1 3 6
2 2 5
1 5 2
2 3 5

output :
17
12
*/

#include <iostream>

#define PIV (1 << 20) // 2^16 -> 10만 쯤

using namespace std;
typedef long long ll;
ll tree[PIV * 2];
int N, U, Q;
ll num;


void update(int n, ll v){
    n += PIV;
    tree[n] = v;

    n /= 2; // 바로 위 부모에서 시작
    while (n > 0){
        // 조상 = 왼쪽 자식 + 오른쪽 자식
        tree[n] = tree[2 * n] + tree[2 * n + 1];
        n /= 2;
    }
}

ll query(int l, int r){
    l += PIV, r += PIV;
    ll ret = 0;

    while(l <= r){
        if (l % 2 == 1) ret += tree[l++];
        if (r % 2 == 0) ret += tree[r--];
        l /= 2;
        r /= 2;
    }
    return ret;
}

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    freopen("input.txt", "r", stdin);

    cin >> N >> U >> Q;
    for (int i = 1; i <= N; i++){
        cin >> num;
        update(i, num);
    }

    int type;
    int b;
    ll c;
    for (int i = 0; i < U + Q; i++){
        cin >> type >> b >> c;
        switch (type){
            case 1:
                update(b, c);
                break;
            case 2:
                cout << query(b, c) << '\n';
                break;
            default:
                break;
        }
    }

    return 0;
}