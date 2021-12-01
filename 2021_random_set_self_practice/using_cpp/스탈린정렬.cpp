/*
input :
7
1 5 6 2 3 4 7

output :
2
 */

#include <iostream>
#include <algorithm>

#define PIV (1 << 20)

using namespace std;
using pii = pair<int, int>;

// 전역 변수 선언
int TREE[2 * PIV];
int N;
pii idx2val[PIV];


void update(int idx, int val) {
    idx += PIV;
    TREE[idx] = val;

    while (true) {
        idx >>= 1;
        if (idx == 0) break;
        TREE[idx] = max(TREE[2 * idx], TREE[2 * idx + 1]);
    }
}


int query(int l, int r) {
    l += PIV;
    r += PIV;

    int ret = 0;
    while (l <= r) {
        if ((l & 1) == 1) {
            ret = max(ret, TREE[l++]);
        }
        if ((r & 1) == 0) {
            ret = max(ret, TREE[r--]);
        }
        l >>= 1;
        r >>= 1;
    }
    return ret;
}


bool comp(pii p1, pii p2) {
    return p1.second < p2.second;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> N;
    int val;
    for (int i = 0; i < N; i++) {
        cin >> val;
        idx2val[i] = {i, val};
    }
    sort(idx2val, idx2val + N, comp);
    for (int i = 0; i < N; i++) {
        idx2val[i].second = i + 1;
    }
    sort(idx2val, idx2val + N);

    int tmp_mxv;
    int mxv = 0;
    for (int i = 0; i < N; i++) {
        tmp_mxv = query(0, idx2val[i].second - 1);

        mxv = max(mxv, tmp_mxv + 1);
        update(idx2val[i].second, tmp_mxv + 1);
    }

    cout << N - mxv;
}
