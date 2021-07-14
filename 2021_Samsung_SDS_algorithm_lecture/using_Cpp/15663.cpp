/*
input :
4 2
9 7 9 1

output :
1 7
1 9
7 1
7 9
9 1
9 7
9 9
*/

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

// 전역 변수 선언
int N, M;
int nums[8];
int ans[8];
int is_used[8];

void recur(int k){
    if (k == M) {
        for (int i = 0; i < M; i++){
            cout << ans[i] << " ";
        }
        cout << '\n';
        return;
    }

    int prev = 0;
    for (int i = 0; i < N; i++){
        if (is_used[i]) continue;
        if (prev == nums[i]) continue;

        ans[k] = nums[i];
        is_used[i] = true;
        prev = nums[i];
        recur(k + 1);
        is_used[i] = false;
    }
}

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    freopen("input.txt", "r", stdin);

    cin >> N >> M;
    for (int i = 0; i < N; i++){
        cin >> nums[i];
    }
    sort(nums, nums + N);
    recur(0);

    return 0 ;
}