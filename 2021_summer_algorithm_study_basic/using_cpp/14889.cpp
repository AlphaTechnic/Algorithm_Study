/*
input :
4
0 1 2 3
4 0 5 6
7 1 0 2
3 4 5 0

output :
0
*/

#include <iostream>
#include <algorithm>
#include <vector>
#include <math.h>
using namespace std;

// 전역 변수 선언
int N, min_val;
int board[23][23];
vector<int> A;
vector<int> B;
int visited[23];

void dfs(int cnt){
    if (cnt == N / 2){
        int tot1 = 0;
        int tot2 = 0;
        for (int i = 0; i < N; i++){
            if (!visited[i]) B.push_back(i);
        }

        for (int i = 0; i < cnt - 1; i++){
            for (int j = i + 1; j < cnt; j++){
                tot1 += board[A[i]][A[j]] + board[A[j]][A[i]];
                tot2 += board[B[i]][B[j]] + board[B[j]][B[i]];
            }
        }
        min_val = min(min_val, abs(tot1 - tot2));
        B.clear();
        return;
    }

    for (int i = 0; i < N; i++){
        if (visited[i]) continue;
        if (A.size() != 0 && A[A.size() - 1] > i) continue;

        visited[i] = true;
        A.push_back(i);

        dfs(cnt + 1);

        visited[i] = false;
        A.pop_back();
    }
}

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> N;
    for (int i = 0; i < N; i++){
        for (int j = 0; j < N; j++){
            cin >> board[i][j];
        }
    }

    min_val = 1000;
    dfs(0);
    cout << min_val;
    return 0;
}