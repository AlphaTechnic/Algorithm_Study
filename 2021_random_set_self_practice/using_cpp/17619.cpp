/*
input :
4 2
1 5 2
3 7 4
7 9 1
10 13 4
1 3
1 4

output :
1
0
 */
#include <iostream>
#include <vector>
#include <algorithm>

#define SZ (100005)

using namespace std;

// 전역 변수 선언
typedef struct _interval {
    int a, b, y, idx;
} interval;

int N, Q;
interval arr[SZ];
int par[SZ];
int height[SZ];

bool comp(interval interval1, interval interval2) {
    return interval1.a < interval2.a;
}

int find(int x) {
    if (par[x] == 0) {
        return x;
    }
    return par[x] = find(par[x]);
}

bool uni(int a, int b) {
    a = find(a);
    b = find(b);
    if (a == b) return false;

    if (height[a] < height[b]) {
        swap(a, b);
    }
    par[b] = a;

    if (height[a] == height[b]) {
        height[a]++;
    }
    return true;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> N >> Q;
    for (int i = 0; i < N; i++) {
        int a, b, y;
        cin >> a >> b >> y;
        arr[i] = {a, b, y, i + 1};
    }
    sort(arr, arr + N, comp);

    int i = 0;
    int j = 0;
    while (j < N) {
        if (arr[i].b >= arr[j].a) {
            uni(arr[i].idx, arr[j].idx);
            j++;
        }
        else {
            i++;
        }
    }

    for (int q = 0; q < Q; q++) {
        int a, b;
        cin >> a >> b;
        if (find(a) == find(b)) {
            cout << 1 << '\n';
        }
        else {
            cout << 0 << '\n';
        }
    }
}
