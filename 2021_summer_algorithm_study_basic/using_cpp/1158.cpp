/*
input :
7 3

output :
<3, 6, 2, 7, 5, 1, 4>
*/

#include <iostream>
#include <deque>
#include <algorithm>
using namespace std;

int N, K;
int f;
int buf;
deque<int> nums;
int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    freopen("input.txt", "r", stdin);

    cin >> N >> K;
    for (int i = 1; i <= N; i++){
        nums.push_back(i);
    }

    cout << '<';
    while (true){
        for (int i = 0; i < K % nums.size(); i++){
            f = nums.front();
            nums.pop_front();
            nums.push_back(f);
        }
        buf = nums.back();
        nums.pop_back();

        if (!nums.empty()){
            cout << buf << ", ";
        }
        else{
            cout << buf;
            break;
        }
    }
    cout << '>';

    return 0;
}