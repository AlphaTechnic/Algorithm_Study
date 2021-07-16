/*
input :
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6

output :
0
2
3
7
INF
*/

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int V, E;
int S;
int a, b, w;
vector<pair<int, int>> graph[20002];
int dist[20002];
int INF = 4000000;


void dijkstra(int S){
    priority_queue<pair<int, int>> min_heap;
    dist[S] = 0;
    min_heap.push({0, S});

    while (!min_heap.empty()){
        pair<int, int> cur;
        cur = min_heap.top(); min_heap.pop();
        int cur_w = cur.first; int cur_node = cur.second;

        if (dist[cur_node] < - cur_w) continue;

        for (pair<int, int> nxt : graph[cur_node]){
            int nxt_w = nxt.first; int nxt_node = nxt.second;
            int new_cost = dist[cur_node] + nxt_w;
            if (new_cost > dist[nxt_node]) continue;

            dist[nxt_node] = new_cost;
            min_heap.push({-new_cost, nxt_node});
        }
    }
}


int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    freopen("input.txt", "r", stdin);

    cin >> V >> E;
    cin >> S;

    for (int i = 0; i < E; i++){
        cin >> a >> b >> w;
        graph[a].push_back({w, b});
    }
    for (int i = 1; i < V + 1; i++){
        dist[i] = INF;
    }

    dijkstra(S);
    for (int i = 1; i < V + 1; i++){
        if (dist[i] == INF)
            cout << "INF" << '\n';
        else
            cout << dist[i] << '\n';
    }
    return 0;
}