/*
input :
28

output :
3
2 3 4
 */

#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    int N;
    cin >> N;

    int cnt = 0;
    int idx = 0;
    vector<int> vec;

    while (N != 0) {
        if ((N & 1) == 1) {
            cnt++;
            vec.push_back(idx);
        }
        N >>= 1;
        idx++;
    }

    cout << cnt << '\n';
    for (int i = 0; i < vec.size(); i++) {
        cout << vec[i] << ' ';
    }
    cout << '\n';

    return 0;
}