/*
input :
103000509
002109400
000704000
300502006
060000050
700803004
000401000
009205800
804000107

output :
143628579
572139468
986754231
391542786
468917352
725863914
237481695
619275843
854396127
*/

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

// 전역 변수 선언
int board[10][10];
string line;
vector<vector<int>> blank_poses;


bool row_chk(int r, int num){
    for (int i = 0; i < 9; i++){
        if (board[r][i] == num) return false;
    }
    return true;
}

bool col_chk(int c, int num){
    for (int i = 0; i < 9; i++){
        if (board[i][c] == num) return false;
    }
    return true;
}

bool block_chk(int r, int c, int num){
    int a = r - r % 3;
    int b = c - c % 3;
    for (int i = a; i < a + 3; i++){
        for (int j = b; j < b + 3; j++){
            if (board[i][j] == num){
                return false;
            }
        }
    }
    return true;
}


void print_ans(){
    for (int r = 0; r < 9; r++){
        for (int c = 0; c < 9; c++){
            cout << board[r][c];
        }
        cout << '\n';
    }
}

void dfs(int dep){
    if (dep == blank_poses.size()){
        print_ans();
        exit(0);
    }

    for (int candi = 1; candi < 10; candi++){
        int y = blank_poses[dep][0];
        int x = blank_poses[dep][1];
        if (!row_chk(y, candi)) continue;
        if (!col_chk(x, candi)) continue;
        if (!block_chk(y, x, candi)) continue;

        board[y][x] = candi;
        dfs(dep + 1);
        board[y][x] = 0;
    }

}

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    for (int r = 0; r < 9; r++){
        cin >> line;
        for (int c = 0; c < 9; c++){
            board[r][c] = line[c] - '0';
            if (board[r][c] == 0){
                blank_poses.push_back({r, c});
            }
        }
    }

    dfs(0);

    return 0;
}