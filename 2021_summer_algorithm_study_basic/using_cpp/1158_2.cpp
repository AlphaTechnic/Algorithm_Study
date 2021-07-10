/*
input :
7 3

output :
<3, 6, 2, 7, 5, 1, 4>
*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N, K;
int delta;
int idx;
vector<int> nums;
int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    freopen("input.txt", "r", stdin);

    cin >> N >> K;
    for (int i = 1; i <= N; i++){
        nums.push_back(i);
    }

    cout << '<';
    delta = K - 1;
    idx += delta;
    idx %= nums.size();

    cout << nums[idx];
    nums.erase(nums.begin() + idx);

    while (nums.size() != 0){
        idx += delta;
        idx %= nums.size();
        cout << ", " << nums[idx];
        nums.erase(nums.begin() + idx);
    }
    cout << ">" << '\n';

    return 0;
}