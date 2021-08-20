/*
input :
3
3 4 3
2 5 2
5 2 2

output :
1
*/

#include <iostream>
#include <algorithm>
#include <queue>
#include <cstring>
#define SZ (1005)
#define MAX (1000000001)
using namespace std;

typedef struct height_yx{
    int height, y, x;
}height_yx;


// 전역 변수 선언
int N;
int heights[SZ][SZ];
bool visited[SZ][SZ];
int dy[4] = {0, 1, 0, -1};
int dx[4] = {1, 0, -1, 0};


bool bfs(int limit){
    queue<height_yx> que;
    memset(visited, false, sizeof(visited));

    height_yx hyx = {heights[0][0], 0, 0};
    que.push(hyx);
    visited[0][0] = true;

    while(!que.empty()) {
        height_yx c_hyx = que.front(); que.pop();
        for (int i = 0; i < 4; i++){
            int ny; int nx;
            ny = c_hyx.y + dy[i];
            nx = c_hyx.x + dx[i];
            if (!(0 <= ny && ny < N)) continue;
            if (!(0 <= nx && nx < N)) continue;
            if (visited[ny][nx]) continue;
            if (abs(c_hyx.height - heights[ny][nx]) > limit) continue;

            visited[ny][nx] = true;
            if (ny == N - 1 && nx == N - 1) return true;
            que.push({heights[ny][nx], ny, nx});
        }
    }
    return false;
}

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> N;
    if (N == 1){
        cout << 0;
        return 0;
    }
    for (int i = 0; i < N; i++){
        for (int j = 0; j < N; j++){
            cin >> heights[i][j];
        }
    }

    int l = 0;
    int r = MAX;
    int mid = (l + r) / 2;
    int mid_save = mid;
    while (l <= r) {
        if (bfs(mid)){
            mid_save = mid;
            r = mid - 1;
            mid = (l + r) / 2;
        }
        else{
            l = mid + 1;
            mid = (l + r) / 2;
        }
    }
    cout << mid_save;

    return 0;
}