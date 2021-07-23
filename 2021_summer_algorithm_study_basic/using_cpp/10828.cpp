/*
input :
14
push 1
push 2
top
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
top

output :
2
2
0
2
1
-1
0
1
-1
0
3
*/

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

// 전역 변수 선언
int N;
vector<int> st;
string cmd;

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> N;
    while(N--){
        cin >> cmd;
        if (cmd[0] == 'p' && cmd[1] == 'u'){
            // push
            int num;
            cin >> num;
            st.push_back(num);
        }
        else if (cmd[0] == 'p' && cmd[1] == 'o'){
            // pop
            if (!st.empty()) cout << st.back() << '\n', st.pop_back();
            else cout << -1 << '\n';
        }
        else if (cmd[0] == 'e'){
            // empty
            if (st.empty()) cout << 1<< '\n';
            else cout << 0 << '\n';
        }
        else if (cmd[0] == 't'){
            // top
            if (!st.empty()) cout << st.back() << '\n';
            else cout << -1 << '\n';
        }
        else{
            // size
            cout << st.size() << '\n';
        }
    }

    return 0 ;
}