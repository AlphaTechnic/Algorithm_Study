/*
input :
4
1 1 5 31
1 1 6 30
5 15 8 31
6 10 12 10

output :
2
*/

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

typedef struct interval{
    int s, e;
}interval;

// 전역 변수 선언
int N;
int cnt;
bool success = true;
vector<interval> intervals;

pair<int, int> find_max_reach(int ind, int l_limit){
    int max_r = -1;
    while (true){
        ind += 1;
        if (ind == N) break;

        if (intervals[ind].s <= l_limit) {
            max_r = max(max_r, intervals[ind].e);
        }
        else break;
    }
    return {ind - 1, max_r};
}

bool comp(interval a1, interval a2){
    if (a1.s == a1.e) return a1.e < a2.e;
    return a1.s < a2.s;
}

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> N;
    for (int i = 0; i < N; i++){
        int a, b, c, d;
        cin >> a >> b >> c >> d;
        intervals.push_back({100 * a + b, 100 * c + d});
    }
    sort(intervals.begin(), intervals.end(), comp);

    int l_limit = 301;
    int in_ind = -1;
    while (true){
        if (l_limit > 1130) break;

        // in_ind에 비해 out_ind가 계속 증가해서 나와줘야 한다.
        // 바통을 이어받을 꽃이 있다는 의미
        pair<int, int> p = find_max_reach(in_ind, l_limit);
        if (in_ind == p.first){
            success = false; break;
        }

        in_ind = p.first;
        cnt++;
        l_limit = p.second;
    }

    if (success) cout << cnt;
    else cout << 0;

    return 0;
}