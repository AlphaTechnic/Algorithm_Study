/*
input :
(()[[]])([])

output :
28
*/

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

// 전역 변수 선언
char paren[128];
string text;

bool is_valid(){
    vector<int> st;
    for (char ch : text){
        if (paren[ch] != 0){
            st.push_back(ch);
        }
        else{  // ch가 닫는 괄호
            if (st.empty()) return false;
            if (ch != paren[st.back()]) return false;
            st.pop_back();
        }
    }
    if (!st.empty()) return false;
    return true;
}

int get_val(){
    vector<int> st;
    for (char ch : text) {
        if (paren[ch] != 0) {
            st.push_back(ch - 128);  // 괄호문자의 ASCII 값과 계산결과 값이 섞이지 않게 하기 위한 조정
        }
        else {  // ch가 닫는 괄호인 경우
            if (ch == ')') {
                int tot = 0;
                int ele;
                while (true) {
                    ele = st.back(); st.pop_back();
                    if (ele == '(' - 128) break;

                    tot += ele;
                }
                int score = max(tot, 1) * 2;
                st.push_back(score);
            }
            else { // ch == ']'
                int tot = 0;
                int ele;
                while (true) {
                    ele = st.back(); st.pop_back();
                    if (ele == '[' - 128) break;

                    tot += ele;
                }
                int score = max(tot, 1) * 3;
                st.push_back(score);
            }
        }
    }
    int ans = 0;
    for (int num : st){
        ans += num;
    }
    return ans;
}

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    paren['('] = ')'; paren['['] = ']';

    cin >> text;
    if (!is_valid()){
        cout << 0;
        return 0;
    }
    cout << get_val();

    return 0 ;
}