/*
input :
5 4
...##
..###
.....
.#..#

output :
3
5
*/

#include <iostream>
#include <queue>

#define SZ (1005)

using namespace std;
using pii = pair<int, int>;


// 전역 변수 선언
int R, C;
int board[SZ][SZ];
string ln;
int MXV;
int CNT;
bool vis[SZ][SZ];
int dy[4] = {0, 1, 0, -1};
int dx[4] = {1, 0, -1, 0};
//int tmp_val;


//void dfs(int cy, int cx) {
//    vis[cy][cx] = true;
//    tmp_val++;
//
//    for (int i = 0; i < 4; i++) {
//        int ny = cy + dy[i];
//        int nx = cx + dx[i];
//        if (!(0 <= ny && ny < R)) continue;
//        if (!(0 <= nx && nx < C)) continue;
//        if (vis[ny][nx]) continue;
//        if (board[ny][nx] == '.') continue;
//
//        dfs(ny, nx);
//    }
//}


int bfs(int cy, int cx) {
    queue<pii> que;
    que.push({cy, cx});
    vis[cy][cx] = true;
    int cnt = 1;

    while (!que.empty()) {
        auto [cy, cx] = que.front(); que.pop();
        for (int i = 0; i < 4; i++) {
            int ny = cy + dy[i];
            int nx = cx + dx[i];
            if (!(0 <= ny && ny < R)) continue;
            if (!(0 <= nx && nx < C)) continue;
            if (vis[ny][nx]) continue;
            if (board[ny][nx] == '.') continue;

            que.push({ny, nx});
            vis[ny][nx] = true;
            cnt++;
        }
    }
    return cnt;
}



int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> C >> R;
    for (int r = 0; r < R; r++) {
        cin >> ln;
        for (int c = 0; c < C; c++) {
            board[r][c] = ln[c];
        }
    }

    for (int r = 0; r < R; r++) {
        for (int c = 0; c < C; c++) {
            if (board[r][c] == '.') continue;
            if (vis[r][c]) continue;

//            dfs(r, c);
            MXV = max(MXV, bfs(r, c));
            CNT++;
        }
    }

    cout << CNT << '\n' << MXV << '\n';
}