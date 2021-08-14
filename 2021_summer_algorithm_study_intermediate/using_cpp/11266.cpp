/*
input :
7 7
1 4
4 5
5 1
1 6
6 7
2 7
7 3

output :
3
1 6 7
*/

#include <iostream>
#include <algorithm>
#include <vector>
#define SZ (10005)
using namespace std;

typedef struct edge{
    int a, b;
}edge;


// 전역 변수 선언
int V, E;
vector<int> graph[SZ];
vector<edge> BCC[SZ];
int dfn[SZ], low[SZ], child[SZ];
bool IS_CUT[SZ];
vector<edge> ST;
int NODE_NUM, BCC_NUM;

void dfs(int p, int mp = -1){
    dfn[p] = low[p] = ++NODE_NUM;
    for (int chd: graph[p]){
        if (chd == mp) continue;  // 부모로 가는 tree edge는 제외. 아래로만 갈 수 있도록.

        if (dfn[chd] == 0){ // 첫 방문
            ST.push_back({p, chd});
            child[p]++;
            dfs(chd, p);
            low[p] = min(low[p], low[chd]);

            // BCC 생성
            if (dfn[p] <= low[chd]){
                if (mp != -1) IS_CUT[p] = true;

                BCC_NUM++;
                while (true){
                    edge ab = ST.back(); ST.pop_back();
                    BCC[BCC_NUM].push_back(ab);
                    if (ab.a == p and ab.b == chd) break;
                }
            }
        }
        else if (dfn[p] > dfn[chd]){ // 조상 touch
            low[p] = min(low[p], dfn[chd]);
            ST.push_back({p, chd});
        }
    }
    if (mp == -1 && child[p] >= 2){
        IS_CUT[p] = true;
    }
}

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> V >> E;
    for (int i = 1; i <= E; i++){
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    for (int i = 1; i <= V; i++){
        if (dfn[i]) continue;

        dfs(i, -1);
    }

    // print ans
    vector<int> ans;
    for (int i = 1; i <= V; i++){
        if (IS_CUT[i]) ans.push_back(i);
    }
    sort(ans.begin(), ans.end());
    cout << ans.size() << '\n';
    for (int num: ans){
        cout << num << ' ';
    }

    return 0;
}