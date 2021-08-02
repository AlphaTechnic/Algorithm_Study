/*
input :
SUN FUN SWIM

output :
YES
*/

#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

// 전역 변수 선언
string str_a, str_b, str_c;
int to_int[128];
vector<char> chars;
bool isused[10];
int LIMIT;

int cal(string some_str){
    int digit = 1;
    int tot = 0;
    for (int i = some_str.size() - 1; i >= 0; i--){
        tot += to_int[some_str[i]] * digit;
        digit *= 10;
    }
    return tot;
}


bool correct_res(){
    return cal(str_c) == cal(str_a) + cal(str_b);
}

void recur(int dep){
    if (dep == LIMIT){
        if (correct_res()){
            cout << "YES";
            exit(0);
        }
        return;
    }

    for (int i = 0; i < 10; i++){
        if (isused[i]) continue;

        to_int[chars[dep]] = i;
        isused[i] = true;

        recur(dep + 1);

        to_int[chars[dep]] = -1;
        isused[i] = false;
    }
}

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> str_a >> str_b >> str_c;
    for (char ch: str_a) to_int[ch] = -1;
    for (char ch: str_b) to_int[ch] = -1;
    for (char ch: str_c) to_int[ch] = -1;
    for (int i = 0; i < 128; i++){
        if (to_int[i] == -1){
            chars.push_back(i);
            LIMIT += 1;
        }
    }

    recur(0);
    cout << "NO";

    return 0;
}