/*
input :
4
3 1
2 3
3 1
3 2

output :
3
*/

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int N;
int a, b;
vector<int> nums = {0};
int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    freopen("input.txt", "r", stdin);

    for (int i = 1; i <= 3; i++){
        nums.push_back(i);
    }

    cin >> N;
    for (int i = 0; i < N; i++){
        cin >> a >> b;
        swap(nums[a], nums[b]);
    }

    // index의 의미가 컵 번호
    for (int i = 1; i <= 3; i++){
        if (nums[i] == 1) cout << i;
    }
}