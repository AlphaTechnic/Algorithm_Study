#include<iostream>

using namespace std;

int d[200001 * 4], e[200001];
int N, i, x;

int get(int p, int left, int right) {
    if (left == right) {
        return d[p] = e[left];
    }
    return d[p] = get(p * 2, left, (left + right) / 2) + get(p * 2 + 1, (left + right) / 2 + 1, right);
}

int f(int p, int left, int right, int v) {
    if (left == right) {
        return left;
    }
    if (d[p * 2] < v) {
        return f(p * 2 + 1, (left + right) / 2 + 1, right, v - d[p * 2]);
    }
    return f(p * 2, left, (left + right) / 2, v);
}


int update(int p, int left, int right, int x) {
    if (x < left || right < x) {
        return d[p];
    }
    if (left == right) {
        return d[p] = 0;
    }
    return d[p] = update(p * 2, left, (left + right) / 2, x) + update(p * 2 + 1, (left + right) / 2 + 1, right, x);
}

int main() {
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    cin >> N;
    for (i = 1; i <= N; i++) {
        cin >> e[i];
    }
    get(1, 1, N);
    for (i = 0; i < N; i++) {
        cin >> x;
        x = f(1, 1, N, x);
        cout << x << " ";
        update(1, 1, N, x);
    }
}
