#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
string txt;
vector<int> stk;
int L;
int closed_idx[51];


int recur(int s, int e){
    int cnt = 0;

    int idx = s;
    while (idx <= e){
        if (txt[idx] == '('){
            cnt--;
            cnt += (txt[idx - 1] - '0') * recur(idx + 1, closed_idx[idx] - 1);
            idx = closed_idx[idx];
        }
        else{
            cnt++;
        }
        idx++;
    }
    return cnt;
}

int main(){
    // 33(562(71(9)))
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> txt;
    L = txt.length();
    for (int i = 0; i < L; i++){
        if (txt[i] == '('){
            stk.push_back(i);
        }
        else if (txt[i] == ')'){
            int sidx = stk.back(); stk.pop_back();
            int eidx = i;
            closed_idx[sidx] = eidx;
        }
    }
    cout << recur(0, L - 1) << '\n';
    return 0;
}
