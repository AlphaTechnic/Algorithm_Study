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
using namespace std;

// 전역 변수 선언
int N, K;
vector<int> seed;
vector<bool> choice;
int board[23][23];
vector<vector<int>> combi;
vector<vector<int>> permu1;
vector<vector<int>> permu2;
int min_val;

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> N;
    K = N / 2;
    for (int i = 0; i < N; i++){
        seed.push_back(i);
        if (i < K) choice.push_back(true);
        else choice.push_back(false);
    }
    for (int i = 0; i < N; i++){
        for (int j = 0; j < N; j++){
            cin >> board[i][j];
        }
    }

    // make combi
    K = N / 2;
    do{
        vector<int> tmp;
        for (int i = 0; i < N; i++){
            if (choice[i]) tmp.push_back(seed[i]);
        }
        combi.push_back(tmp);
        tmp.clear();
    } while(prev_permutation(choice.begin(), choice.end()));


    min_val = 1000;
    for (int i = 0; i < combi.size() / 2; i++){
        // make permutation
        do{
            vector<int> tmp;
            for (int j = 0; j < 2; j++){
                tmp.push_back(combi[i][j]);
            }
            permu1.push_back(tmp);
            tmp.clear();
            reverse(combi[i].begin() + 2, combi[i].end());
        }while(next_permutation(combi[i].begin(), combi[i].end()));
        do{
            vector<int> tmp;
            for (int j = 0; j < 2; j++){
                tmp.push_back(combi[combi.size() - i - 1][j]);
            }
            permu2.push_back(tmp);
            tmp.clear();
            reverse(combi[combi.size() - i - 1].begin() + 2, combi[combi.size() - i - 1].end());
        }while(next_permutation(combi[combi.size() - i - 1].begin(), combi[combi.size() - i - 1].end()));


        int tot1 = 0;
        int tot2 = 0;
        for (vector<int> tmp : permu1){
            tot1 += board[tmp[0]][tmp[1]];
        }
        for (vector<int> tmp : permu2){
            tot2 += board[tmp[0]][tmp[1]];
        }
        min_val = min(min_val, abs(tot1 - tot2));
        permu1.clear();
        permu2.clear();
    }
    cout << min_val;

    return 0;
}