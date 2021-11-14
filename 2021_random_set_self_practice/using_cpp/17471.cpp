/*
input :
6
5 2 3 4 1 2
2 2 4
4 1 3 6 5
2 4 2
2 1 3
1 2
1 2

output :
1
 */
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>

#define SZ (15)

using namespace std;

// 전역 변수 선언
int N;
int vcost[SZ];
vector<int> graph[SZ];
bool vis[SZ];
int CC_num;
int grp_c;
bool grpA[SZ];
int grp_cost[2];


void dfs(int cur) {
    grp_c += vcost[cur];
    vis[cur] = true;
    for (auto nxt: graph[cur]) {
        if (vis[nxt]) continue;

        dfs(nxt);
    }
}

void dfs2(int cur, bool is_grpA) {
    grp_c += vcost[cur];
    vis[cur] = true;
    for (auto nxt: graph[cur]) {
        if (vis[nxt]) continue;
        if (grpA[nxt] != is_grpA) continue;

        dfs2(nxt, is_grpA);
    }
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> N;
    for (int i = 1; i <= N; i++) {
        cin >> vcost[i];
    }

    for (int i = 1; i <= N; i++){
        int num;
        cin >> num;

        vector<int> adjs;
        for (int j = 0; j < num; j++) {
            int v;
            cin >> v;
            adjs.push_back(v);
        }
        graph[i] = adjs;
    }

    vector<int> grp_nums;
    for (int i = 1; i <= N; i++) {
        if (vis[i]) continue;

        dfs(i);
        grp_nums.push_back(grp_c);
        grp_c = 0;
        CC_num++;
    }

    // CC 가 3개 이상이다? => 노답
    if (grp_nums.size() >= 3) {
        cout << -1 << '\n';
        return 0;
    }

    // CC 가 2개라면? => 무조건 한가지의 경우를 출력해야 함. grp1cost - grp2cost
    if (grp_nums.size() == 2) {
        cout << abs(grp_nums[1] - grp_nums[0]) << '\n';
        return 0;
    }

    // CC가 1개라면? => 모든 양분할 조합의 경우를 고려 (brute force)
    int mnv = 1000000000;
    for (int i = 1; i < (1 << N) - 1; i++) {
        memset(grpA, false, sizeof(grpA));
        int vidx = 1;
        int combi = i;
        while (combi != 0) {
            bool torf = (bool)(combi & 1);
            grpA[vidx++] = torf;
            combi >>= 1;
        }

        memset(vis, false, sizeof(vis));
        grp_c = 0;
        for (int j = 1; j <= N; j++) {
            if (grpA[j]) {
                dfs2(j, true);
                grp_cost[0] = grp_c;
                break;
            }
        }
        grp_c = 0;
        for (int k = 1; k <= N; k++) {
            if (!grpA[k]) {
                dfs2(k, false);
                grp_cost[1] = grp_c;
                break;
            }
        }

        bool success_flag = true;
        for (int v = 1; v <= N; v++) {
            if (!vis[v]) {
                success_flag = false;
                break;
            }
        }
        if (success_flag) {
            mnv = min(mnv, abs(grp_cost[0] - grp_cost[1]));
        }
    }
    cout << mnv << '\n';

    return 0;
}
