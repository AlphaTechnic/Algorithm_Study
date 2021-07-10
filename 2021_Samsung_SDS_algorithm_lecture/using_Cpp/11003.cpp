/*
input :
12 3

output :
1 5 2 3 6 2 3 7 3 5 2 6
*/

#include <cstdio>
#include <deque>
using namespace std;

int N, L, num;
deque<pair<int, int>> q;

int main(){
    freopen("input.txt", "r", stdin);
    scanf("%d%d", &N, &L);
    for (int i = 0; i < N; i++){
        scanf("%d", &num);
        while (!q.empty()){
            pair<int, int> tmp = q.back();
            if (tmp.second >= num) q.pop_back();
            else break;
        }
        q.push_back(make_pair(i, num));

        pair<int, int> tmp = q.front();
        if (tmp.first == i - L) {
            q.pop_front();
            tmp = q.front();
        }
        printf("%d ", tmp.second);
    }
}