/*
input :
3
P..
.KK
...
3 2 4
7 4 2
2 3 1

output :
2
*/

#include <cstdio>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

typedef pair<int, int> pii;

int n, height_board[50][50];
int dy[] = {-1, -1, 0, 1, 1, 1, 0, -1};
int dx[] = {0, 1, 1, 1, 0, -1, -1, -1};
int cnt_k;
int y_post, x_post;
char pos_board[50][51];
vector<int> heights;

int bfs(int l, int h){
    int cnt = 0;
    bool visited[50][50] = {false, };
    queue<pii> que;

    que.push(pii(y_post, x_post));
    visited[y_post][x_post] = true;
    if(height_board[y_post][x_post] < l || height_board[y_post][x_post] > h) return -1;

    while (!que.empty() && cnt < cnt_k){
        pii cur = que.front();
        que.pop();

        for (int i = 0; i < 8; i++){
            int ny = cur.first + dy[i];
            int nx = cur.second + dx[i];

            if (!(0 <= ny && ny < n)) continue;
            if (!(0 <= nx && nx < n)) continue;
            if (visited[ny][nx]) continue;
            if (height_board[ny][nx] < l || height_board[ny][nx] > h) continue;

            if (pos_board[ny][nx] == 'K') cnt++;
            visited[ny][nx] = true;

            que.push(pii(ny, nx));
        }
    }
    return cnt;
}


int main(){
    freopen("input.txt", "r", stdin);
    scanf("%d", &n);
    for (int i = 0; i < n; i++){
        scanf("%s", pos_board[i]);
    }
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            if (pos_board[i][j] == 'K'){
                cnt_k++;
            }
            else if (pos_board[i][j] == 'P'){
                y_post = i;
                x_post = j;
            }
        }
    }
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            scanf("%d", &height_board[i][j]);
            heights.push_back(height_board[i][j]);
        }
    }

    sort(heights.begin(), heights.end());
    unique(heights.begin(), heights.end());
    int ans = heights.back() - heights[0];
    for (int l = 0, h = 0; l < heights.size() && h < heights.size() && l <= h;){
        if (bfs(heights[l], heights[h]) == cnt_k){
            if (heights[h] - heights[l] < ans) ans = heights[h] - heights[l];
            l++;
        }
        else{
            h++;
        }
    }
    printf("%d", ans);
}