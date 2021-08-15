/*
input :
7 8
1 4
4 5
5 1
1 6
6 7
2 7
7 3
2 3

output :
2
1 6
6 7
*/

#include <iostream>
#include <algorithm>
#include <vector>
#define SZ (100005)
using namespace std;

typedef struct edge{
    int a, b;
}edge;

// 전역 변수 선언
int V, E;
int NODE_NUM, BCC_NUM;
vector<int> graph[SZ];
vector<edge> BCC[SZ];
int dfn[SZ], low[SZ];
vector<edge> ST;
vector<edge> CUT_EDGES;

void dfs(int p, int mp){
    dfn[p] = low[p] = ++NODE_NUM;
    for (int chd: graph[p]){
        if (chd == mp) continue;

        if (dfn[chd] == 0){
            ST.push_back({p, chd});
            dfs(chd, p);
            low[p] = min(low[p], low[chd]);

            // BCC 감지
            if (dfn[p] <= low[chd]){
                if (dfn[p] < low[chd]) CUT_EDGES.push_back({p, chd});

                BCC_NUM++;
                while (true){
                    edge ab = ST.back(); ST.pop_back();
                    BCC[BCC_NUM].push_back(ab);

                    if (ab.a == p && ab.b == chd) break;
                }
            }
        }
        else if (dfn[p] > dfn[chd]){
            low[p] = min(low[p], dfn[chd]);
            ST.push_back({p, chd});
        }
    }
}


bool comp(edge obj1, edge obj2){
    if (obj1.a == obj2.a) return obj1.b < obj2.b;
    return obj1.a < obj2.a;
}

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> V >> E;
    for (int i = 0; i < E; i++){
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    for (int i = 1; i <= V ; i++){
        if (dfn[i]) continue;

        dfs(i, -1);
    }

    // print ans
    cout << CUT_EDGES.size() << '\n';
    for (edge &ab: CUT_EDGES){
        if (ab.a > ab.b) {
            swap(ab.a, ab.b);
        }
    }
    sort(CUT_EDGES.begin(), CUT_EDGES.end(), comp);

    for (edge ab: CUT_EDGES){
        cout << ab.a << ' ' << ab.b << '\n';
    }

    return 0;
}