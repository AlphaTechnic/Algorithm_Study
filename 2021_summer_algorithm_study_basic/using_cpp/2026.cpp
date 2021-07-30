/*
4 6 8
1 2
1 3
1 6
2 3
2 6
3 6
4 5
5 6

output :
1
2
3
6
*/

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

// 전역 변수 선언
vector<int> members;
int K, N, F;
int CNT;
bool isused[905];
int adj_mat[905][905];


void print_ans(){
    for (int mem: members){
        cout << mem << '\n';
    }
}


bool chk_all_friends(int i){
    for (int mem: members){
        if (!adj_mat[mem][i]) return false;
    }
    return true;
}


void recur(int dep){
    if (dep == N) return;
    if (CNT == K){
        print_ans();
        exit(0);
    }

    for (int i = dep; i <= N; i++){
        if (adj_mat[i][0] < K - 1) continue;
        if (isused[i]) continue;
        if (!chk_all_friends(i)) continue;

        isused[i] = true;
        members.push_back(i);
        CNT++;

        recur(dep + 1);

        isused[i] = false;
        members.pop_back();
        CNT--;

        recur(dep + 1);
    }

}

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> K >> N >> F;
    while(F--){
        int a, b;
        cin >> a >> b;
        adj_mat[a][b] = 1; adj_mat[a][0] += 1;
        adj_mat[b][a] = 1; adj_mat[b][0] += 1;
    }

    recur(0);
    cout << -1;

    return 0;
}