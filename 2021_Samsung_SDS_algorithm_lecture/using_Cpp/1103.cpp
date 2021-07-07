/*
input :
3 7
3942178
1234567
9123532

output:
5
*/
#include <cstdio>

int R, C, ANS;
int dy[] = {0, 1, 0, -1};
int dx[] = {1, 0, -1, 0};
int LIMIT;
int MAX_CNT[50][50]; // BOARD와 크기가 같은 배열 : prunning 용
char BOARD[50][51];

void dfs(int cy, int cx, int cnt){
    if (ANS < cnt) ANS = cnt;
    if (ANS > LIMIT) return;
    if (!(0 <= cy && cy < R && 0 <= cx && cx < C)) return;
    if (BOARD[cy][cx] == -1) return;
    if (cnt <= MAX_CNT[cy][cx]) return;

    MAX_CNT[cy][cx] = cnt;
    int mul = BOARD[cy][cx];

    for (int i = 0; i < 4; i++){
        dfs(cy + dy[i] * mul, cx + dx[i] * mul, cnt + 1);
    }
}

int main(){
    freopen("input.txt", "r", stdin);

    scanf("%d%d", &R, &C);
    LIMIT = R*C;

    // init MAX_CNT
    for (int i = 0; i < R; i++){
        for (int j = 0; i < C; i++){
            MAX_CNT[i][j] = -1;
        }
    }

    // init BOARD
    for (int i = 0; i < R; i++){
        scanf("%s", BOARD[i]);
        for (int j = 0; j < C; j++){
            if (BOARD[i][j] == 'H') BOARD[i][j] = -1;
            else BOARD[i][j] = BOARD[i][j] - '0';
        }
    }

    dfs(0, 0 ,0);
    if (ANS > LIMIT) ANS = -1;
    printf("%d", ANS);
}