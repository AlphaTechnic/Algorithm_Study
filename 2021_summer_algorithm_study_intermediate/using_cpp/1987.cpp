/*
input :
2 4
CAAB
ADCB

output :
3
*/

#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
using namespace std;

// 전역 변수 선언
int R, C;
int board[21][21];
int max_val;
bool visited[21][21];
bool chk_path[128];
string line;
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

void dfs(int cy, int cx, int cnt){
    max_val = max(max_val, cnt);

    for (int i = 0; i < 4; i++){
        int ny = cy + dy[i];
        int nx = cx + dx[i];
        if (!(0 <= ny && ny < R)) continue;
        if (!(0 <= nx && nx < C)) continue;
        if (chk_path[board[ny][nx]]) continue;

        chk_path[board[ny][nx]] = true;
        visited[ny][nx] = true;
        dfs(ny, nx, cnt + 1);
        chk_path[board[ny][nx]] = false;
        visited[ny][nx] = false;
    }
}

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> R >> C;
    for (int i = 0; i < R; i++){
        cin >> line;
        for (int j = 0; j < C; j++){
            board[i][j] = line[j];
        }
    }

    max_val = 0;
    chk_path[board[0][0]] = true;
    dfs(0, 0, 0);

    cout << max_val + 1 << '\n';

    return 0;
}