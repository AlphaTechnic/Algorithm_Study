/*
input :
80875542

output :
88755420
*/

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

// 전역 변수 선언
vector<int> nums;
bool is_zero;
int tot;
string digits;

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    freopen("input.txt", "r", stdin);

    cin >> digits;
    for (int i = 0; i < digits.length(); i++){
        if (digits[i] == '0') is_zero = true;
        tot += digits[i] - '0';
        nums.push_back(digits[i] - '0');
    }
    if (!is_zero) {
        cout << -1;
        return 0;
    }
    if (tot % 3 != 0) {
        cout << -1;
        return 0;
    }

    sort(digits.begin(), digits.end(), greater<int>());
    for (int i = 0; i < nums.size(); i++){
        cout << digits[i];
    }

    return 0 ;
}