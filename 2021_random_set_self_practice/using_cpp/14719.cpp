#include <iostream>
#include <algorithm>

using namespace std;

#define PIV (1 << 9)
#define SZ (505)
int TREE[2 * PIV];

void update(int idx, int x) {
    idx += PIV;
    TREE[idx] = x;
    while (true) {
        idx >>= 1;
        if (idx == 0) {
            return;
        }
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


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    int H, N;
    int arr[SZ];

    cin >> H >> N;
    if (N <= 2) {
        cout << 0 << '\n';
        return 0;
    }

    for (int i = 0; i < N; i++) {
        cin >> arr[i];
        update(i, arr[i]);
    }

    int tot = 0;
    for (int i = 1; i < N - 1; i++) {
        int lmx, rmx;
        int mnv;

        lmx = query(0, i - 1);
        rmx = query(i + 1, N);
        mnv = min(lmx, rmx);
        if (arr[i] < mnv) {
            tot += (mnv - arr[i]);
        }
    }
    cout << tot << '\n';

    return 0;
}
