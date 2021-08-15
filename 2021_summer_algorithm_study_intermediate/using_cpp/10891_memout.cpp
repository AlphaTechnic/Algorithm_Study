/*
input :
4 4
1 2
2 3
3 1
3 4

output :
Cactus
*/

#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#define SZ (100005)
using namespace std;

typedef struct edge{
    int a, b;
}edge;


// 전역 변수 선언
int V, E;
vector<int> graph[SZ];
vector<edge> BCC[SZ];
int dfn[SZ], low[SZ];
vector<edge> ST;
int NODE_NUM, BCC_NUM;

void dfs(int p, int mp = -1){
    dfn[p] = low[p] = ++NODE_NUM;
    for (int chd: graph[p]){
        if (chd == mp) continue;  // 부모로 가는 tree edge는 제외. 아래로만 갈 수 있도록.

        if (dfn[chd] == 0){ // 첫 방문
            ST.push_back({p, chd});
            dfs(chd, p);
            low[p] = min(low[p], low[chd]);

            // BCC 생성
            if (dfn[p] <= low[chd]){
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
}

int get_node_num(vector<edge> edges){
    set<int> chk_set;
    for (edge &ab: edges){
        chk_set.insert(ab.a);
        chk_set.insert(ab.b);
    }
    return chk_set.size();
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
    map<int, set<int>> nd2bccnums;
    for (int i = 1; i <= V; i++){
        nd2bccnums[i] = {};
    }
    for (int b_num = 1; b_num <= BCC_NUM; b_num++){
        for (edge &ab: BCC[b_num]){
            nd2bccnums[ab.a].insert(b_num);
            nd2bccnums[ab.b].insert(b_num);
        }
    }
    for (int nd = 1; nd < V; nd++){
        int cnt = 0;

        for (int b_num: nd2bccnums[nd]){
            if (BCC[b_num].size() >= 3){
                cnt += 1;
                if (cnt > 1){
                    cout << "Not cactus" << '\n';
                    return 0;
                }
                if (BCC[b_num].size() != get_node_num(BCC[b_num])){
                    cout << "Not cactus" << '\n';
                    return 0;
                }
            }
        }
    }
    cout << "Cactus" << '\n';

    return 0;
}