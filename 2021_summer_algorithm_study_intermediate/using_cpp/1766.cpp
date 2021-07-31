/*
input :
3 2
1 3
2 3

output :
1 2 3
*/

#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <functional>
using namespace std;

// 전역 변수 선언
int N, M;
int a, b;
vector<int> graph[32005];
int indeg[32005];
priority_queue<int, vector<int>, greater<int>> min_heap;


int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> N >> M;
    while (M--){
        cin >> a >> b;
        graph[a].push_back(b);
        indeg[b] += 1;
    }

    for (int i = 1; i <= N; i++){
        if (indeg[i] == 0){
            min_heap.push(i);
        }
    }

    while (min_heap.size() != 0){
        int cur = min_heap.top(); min_heap.pop();
        cout << cur << ' ';
        for (int nxt: graph[cur]){
            indeg[nxt] -= 1;
            if (indeg[nxt] == 0){
                min_heap.push(nxt);
            }
        }
    }

    return 0;
}