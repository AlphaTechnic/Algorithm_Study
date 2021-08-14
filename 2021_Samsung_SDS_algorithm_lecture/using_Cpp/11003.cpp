/*
input :
12 3
1 5 2 3 6 2 3 7 3 5 2 6

output :
1 1 1 2 2 2 2 2 3 3 2 2
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
        // deque를 부분증가수열로 관리
        // 안에 있는 찔빱들을 다 밀어버리고 신흥강자를 집어넣음
        scanf("%d", &num);
        while (!q.empty()){
            pair<int, int> tmp = q.back();
            if (tmp.second >= num) q.pop_back();
            else break;
        }
        q.push_back(make_pair(i, num));

        // front()가 유통기한이 다되었으면 deque에서 버림
        pair<int, int> tmp = q.front();
        if (tmp.first == i - L) {
            q.pop_front();
            tmp = q.front();
        }
        printf("%d ", tmp.second);
    }
}