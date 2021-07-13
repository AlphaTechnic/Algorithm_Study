/*
input :
8
2
8
10
7
1
9
4
15

output :
1
1
1
3
5
2
5
1
*/

#include <iostream>
#include <algorithm>
using namespace std;
typedef pair<int, int> pii;

// 전역 변수 선언
int n, num;
pii player[500000];
int tr[1 << 20];

int seg_sum(int node, int s, int e, int l, int r){
    if (r < s || e < l) return 0;
    if (l <= s && e <= r){
        return tr[node];
    }

    int mid = (s + e) / 2;
    return seg_sum(2 * node, s, mid, l, r) + seg_sum(2 * node + 1, mid + 1, e, l, r);
}

void update(int node, int s, int e, int idx, int v){
    if (idx < s || e < idx) return;
    if (s == e) {
        tr[node] = v;
        return;
    }

    int mid = (s + e) / 2;
    update(2 * node, s, mid, idx, v);
    update(2 * node + 1, mid + 1, e, idx, v);
    tr[node] = tr[2 * node] + tr[2 * node + 1];
}

bool comp(pii p1, pii p2){
    return p1.second < p2.second;
}
int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    freopen("input.txt", "r", stdin);

    cin >> n;
    for (int i = 0; i < n; i++){
        int power;
        cin >> power;
        player[i].first = i;
        player[i].second = power;
    }

    // sort power -> for relabeling
    sort(player, player + n, comp);
    for (int i = 0; i < n; i++){
        player[i].second = ++num;
    }

    // sort original order
    sort(player, player + n);
    for (int i = 0; i < n; i++){
        int cur_power = player[i].second;
        int cnt = 0;

        if (cur_power > 1) cnt = seg_sum(1, 1, num, 1, cur_power - 1);
        update(1, 1, num, cur_power, 1);
        cout << (i + 1) - cnt << "\n";
    }
    return 0 ;
}