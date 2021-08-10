/*
input :
4 4 8
3
0 10
1 10
2 1

output :
9
*/

#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

typedef struct sz2cnt{
    int sz, cnt;
}sz2cnt;

// 전역 변수 선언
int CUBE_NUM;
bool POSSIBLE = true;
int N;
int X, Y, Z;
sz2cnt sz2cnts[25];

bool comp(sz2cnt obj1, sz2cnt obj2){
    return obj1.sz > obj2.sz;
}

void recur(int X, int Y, int Z){
    if (!(POSSIBLE)) return;
    if (X == 0 || Y == 0 || Z == 0) return;

    for (int i = 0; i < N; i++){
        if (!(sz2cnts[i].sz <= X && sz2cnts[i].sz <= Y && sz2cnts[i].sz <= Z)) continue;
        if (sz2cnts[i].cnt <= 0) continue;

        CUBE_NUM ++; sz2cnts[i].cnt --;

        recur(X, Y, Z - sz2cnts[i].sz);
        recur(sz2cnts[i].sz, Y - sz2cnts[i].sz, sz2cnts[i].sz);
        recur(X - sz2cnts[i].sz, Y, sz2cnts[i].sz);
        return;
    }
    POSSIBLE = false;
}


int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> X >> Y >> Z;
    cin >> N;
    for(int i = 0; i < N; i++){
        int sz, cnt;
        sz2cnt obj;

        cin >> sz >> cnt;
        obj.sz = pow(2, sz);
        obj.cnt = cnt;
        sz2cnts[i] = obj;
    }

    sort(sz2cnts, sz2cnts + N, comp);
    recur(X, Y, Z);

    if (POSSIBLE) cout << CUBE_NUM;
    else cout << -1;

    return 0;
}