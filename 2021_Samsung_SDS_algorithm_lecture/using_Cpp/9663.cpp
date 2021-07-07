/*
input :
4

output :
2
*/

#include <cstdio>

int N, ANS = 0;
int CHESS[14][14];

void recur(int line){
    // 종료 조건
    if (line == N){
        ANS++;
        return;
    }

    for (int row = 0; row < N; row++){
        // line 어딘가에 queen을 놓는다.
        if (CHESS[line][row] != -1) continue;
        CHESS[line][row] = line;

        // line에 놓았으니, 좌/ 우/ 하/ 좌대각/ 우대각 에는 queen을 못 놓게 처리

        // 좌, 우
        for (int x = 0; x < N; x++){
            if (CHESS[line][x] == -1){
                CHESS[line][x] = line;
            }
        }

        // 하
        for (int y = 0; y < N; y++){
            if (CHESS[y][row] == -1){
                CHESS[y][row] = line;
            }
        }

        // 좌대각
        for (int x = row, y = line; 0 <= x && y < N; x--, y++){
            if (CHESS[y][x] == -1){
                CHESS[y][x] = line;
            }
        }
        // 우대각
        for (int x = row, y = line; x < N && y < N; x++, y++){
            if (CHESS[y][x] == -1){
                CHESS[y][x] = line;
            }
        }

        recur(line + 1);

        // 원상 복구
        // 좌, 우
        for (int x = 0; x < N; x++){
            if (CHESS[line][x] == line){
                CHESS[line][x] = -1;
            }
        }

        // 하
        for (int y = 0; y < N; y++){
            if (CHESS[y][row] == line){
                CHESS[y][row] = -1;
            }
        }

        // 좌대각
        for (int x = row, y = line; 0 <= x && y < N; x--, y++){
            if (CHESS[y][x] == line){
                CHESS[y][x] = -1;
            }
        }
        // 우대각
        for (int x = row, y = line; x < N && y < N; x++, y++){
            if (CHESS[y][x] == line){
                CHESS[y][x] = -1;
            }
        }
    }
}


int main() {
    // init CHESS
    for (int i = 0; i < 14; i++){
        for (int j = 0; j < 14; j++){
            CHESS[i][j] = -1;
        }
    }
    scanf("%d", &N);

    recur(0);
    printf("%d", ANS);
    return 0;
}
