/*
input :
4 8
XFDFFFCX
ELFXLFFX
LFLXXLFX
DLFFFFLD

output :
31
*/

#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <cstring>
using namespace std;

typedef struct pos{
    int y, x, state;
}pos;

// 전역 변수 선언
int R, C;
int caty, catx;
int ey, ex;
int board[1005][1005];
int visited[1005][1005];
string line;
queue<pos> que;
int dy[4] = {0, 1, 0, -1};
int dx[4] = {1, 0, -1, 0};
int nny, nnx;

void move_fun(int cy, int cx){
    nnx = cx;
    nny = cy;
    while (true){
        nny += 1;
        if (board[nny][nnx] != 'X'){
            return;
        }
    }
}

void bfs(){
    que.push({caty, catx, board[caty][catx]});
    visited[caty][catx] = 0;

    while (!que.empty()){
        pos cyx = que.front(); que.pop();
        if (cyx.y == ey && cyx.x == ex){
            return;
        }

        int ny, nx;
        if (cyx.state == 'F' or cyx.state == 'C'){
            int dir1[2] = {0, 2};
            for (int& i: dir1){
                ny = cyx.y + dy[i]; nx = cyx.x + dx[i];
                if (!(0 <= ny && ny < R)) continue;
                if (!(0 <= nx && nx < C)) continue;
                if (board[ny][nx] == 'D') continue;
                if (visited[ny][nx] != -1) continue;
                visited[ny][nx] = visited[cyx.y][cyx.x] + 1;
                que.push({ny, nx, board[ny][nx]});
            }

            int dir2[2] = {1, 3};
            for (int& i: dir2){
                ny = cyx.y + dy[i]; nx = cyx.x + dx[i];
                if (!(0 <= ny && ny < R)) continue;
                if (!(0 <= nx && nx < C)) continue;
                if (board[ny][nx] != 'L') continue;
                if (visited[ny][nx] != -1) continue;
                visited[ny][nx] = visited[cyx.y][cyx.x];
                que.push({ny, nx, board[ny][nx]});
            }
        }
        else if (cyx.state == 'L'){
            int dir3[3] = {1, 3};
            for (int& i: dir3){
                ny = cyx.y + dy[i]; nx = cyx.x + dx[i];
                if (!(0 <= ny && ny < R)) continue;
                if (!(0 <= nx && nx < C)) continue;
                if (board[ny][nx] == 'D') continue;
                if (visited[ny][nx] != -1) continue;
                visited[ny][nx] = visited[cyx.y][cyx.x] + 5;
                que.push({ny, nx, board[ny][nx]});
            }
        }
        else if (cyx.state == 'X'){
            move_fun(cyx.y, cyx.x);
            if (!(0 <= nny && nny < R)) continue;
            if (!(0 <= nnx && nnx < C)) continue;
            if (board[nny][nnx] == 'D') continue;
            if (visited[nny][nnx] != -1) continue;
            visited[nny][nnx] = visited[cyx.y][cyx.x] + 10;
            que.push({nny, nnx, board[nny][nnx]});
        }
    }
}

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> R >> C;
    for (int r = 0; r < R; r++){
        cin >> line;
        for (int c = 0; c < C; c++){
            board[r][c] = line[c];
            if (board[r][c] == 'C') {
                caty = r, catx = c;
            }
            else if (board[r][c] == 'E') {
                ey = r, ex = c;
            }
        }
    }
    memset(visited, -1, sizeof(visited));
    bfs();

    if (visited[ey][ex] == -1){
        cout << "dodo sad" << '\n';
    }
    else{
        cout << visited[ey][ex] << '\n';
    }

    return 0;
}