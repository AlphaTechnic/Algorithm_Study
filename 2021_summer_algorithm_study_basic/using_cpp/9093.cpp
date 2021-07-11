/*
input :
2
I am happy today
We want to win the first prize

output :
I ma yppah yadot
eW tnaw ot niw eht tsrif ezirp
*/

#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int N;
string buf;

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    freopen("input.txt", "r", stdin);

    cin >> N;
    cin.ignore();
    while (N--){
        getline(cin, buf);

        string tmp;
        for (int i = 0; i < buf.length(); i++){
            if (buf[i] == ' '){
                reverse(tmp.begin(), tmp.end());
                cout << tmp << ' ';
                tmp.clear();
            }
            else tmp += buf[i];
        }

        reverse(tmp.begin(), tmp.end());
        cout << tmp << '\n';
    }

    return 0;
}