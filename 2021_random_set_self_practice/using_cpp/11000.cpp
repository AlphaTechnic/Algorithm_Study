/*
input :
3
1 3
2 4
3 5

output :
2
*/
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#define SZ (200005)

using namespace std;
using pii = pair<int, int>;


// 전역 변수 선언
int N;
pii interval[SZ];
priority_queue<int, vector<int>, greater<int>> pq;

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> N;
    for (int i = 0; i < N; i++) {
        int a, b;
        cin >> a >> b;
        interval[i] = {a, b};
    }
    sort(interval, interval + N);

    auto [s0, e0] = interval[0];
    pq.push(e0);

    for (int i = 1; i < N; i++){
        auto [si, ei] = interval[i];
        if (pq.top() <= si) {  // 제일 빨리 끝나는 강의실의 바통을 이어받을 수 있는 interval이 나타나면,
            pq.pop();  // pop() 하나 때리고 push
        }
        pq.push(ei);
    }
    cout << pq.size() << '\n';

    return 0;
}