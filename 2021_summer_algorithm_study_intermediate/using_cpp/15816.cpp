/*
input :
3
1 10 20
4
2 1 20
1 5
2 1 20
2 1 1

output :
17 16 0
*/

#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#define PIV (1 << 22)
using namespace std;
using ll = long long;

// 전역 변수 선언
ll tree[2 * PIV];
ll N, M;
vector<ll> NUMS;

ll init_updates[1000003];
ll cmd[1000003][3];


void update(ll x){
    x += PIV;
    if (tree[x]) return;

    tree[x]++;
    while (x >>= 1){
        tree[x]++;
    }
}

ll query(ll l, ll r){
    l += PIV, r += PIV;

    ll ret = 0;
    while(l <= r){
        if (l & 1) ret += tree[l++];
        if (!(r & 1)) ret += tree[r--];
        l >>= 1, r >>= 1;
    }
    return ret;
}


int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> N;
    for (int i = 0; i < N; i++){
        cin >> init_updates[i];
        NUMS.push_back(init_updates[i]);
    }

    int type;
    cin >> M;
    for (int i = 0; i < M; i++){
        cin >> type;
        cmd[i][0] = type;
        switch (type){
            case 1:
                cin >> cmd[i][1];
                NUMS.push_back(cmd[i][1]);
                break;
            case 2:
                cin >> cmd[i][1] >> cmd[i][2];
                NUMS.push_back(cmd[i][1]);
                NUMS.push_back(cmd[i][2]);
                break;
            default:
                // no action
                break;
        }
    }

    // 좌표압축
    sort(NUMS.begin(), NUMS.end());
    NUMS.resize(unique(NUMS.begin(), NUMS.end()) - NUMS.begin());

    // init update 쿼리들 처리
    for (int i = 0; i < N; i++){
        int k = lower_bound(NUMS.begin(), NUMS.end(), init_updates[i]) - NUMS.begin();
        update(k);
    }

    // after update 및 구간합 쿼리들 처리
    for (int i = 0; i < M; i++){
        ll x, l, r; int comp_l, comp_r;
        switch (cmd[i][0]){
            case 1:
                x = lower_bound(NUMS.begin(), NUMS.end(), cmd[i][1]) - NUMS.begin();
                update(x);
                break;
            case 2:
                l = cmd[i][1], r = cmd[i][2];
                comp_l = lower_bound(NUMS.begin(), NUMS.end(), cmd[i][1]) - NUMS.begin();
                comp_r = lower_bound(NUMS.begin(), NUMS.end(), cmd[i][2]) - NUMS.begin();
                cout << r - l + 1 - query(comp_l, comp_r) << '\n';
                break;
            default:
                // no action
                break;
        }
    }
    return 0;
}