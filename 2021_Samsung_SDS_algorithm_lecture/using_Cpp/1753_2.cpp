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

typedef struct node{
    int to;
    int w;
}node;

int V, E;
int S;
int a, b, w;
//vector<pair<int, int>> graph[20002];
vector<node> graph[20002];

bool operator<(node a, node b){
    return a.w > b.w;
}

int dist[20002];
int INF = 4000000;


void dijkstra(int S){
    priority_queue<node> pq;
    dist[S] = 0;
    pq.push({S, 0});

    while (!pq.empty()){
        node cur;
        cur = pq.top(); pq.pop();

        if (dist[cur.to] < cur.w) continue;

        for (node nxt : graph[cur.to]){
            int new_cost = dist[cur.to] + nxt.w;
            if (new_cost >= dist[nxt.to]) continue;

            dist[nxt.to] = new_cost;
            pq.push({nxt.to, new_cost});
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
        graph[a].push_back({b, w});
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