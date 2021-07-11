/*
input :
dcbagfekjih

output :
abcdefghijk
*/

#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

string text;
vector<string> strings;
string ans(51, 'z');
int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    freopen("input.txt", "r", stdin);

    cin >> text;
    for (int i = 0; i < text.length() - 2; i++){
        for (int j = i + 1; j < text.length() - 1; j++){
            string tmp = text;
            reverse(tmp.begin(), tmp.begin() + i + 1);
            reverse(tmp.begin() + i + 1, tmp.begin() + j + 1);
            reverse(tmp.begin() + j + 1, tmp.end());

            ans = min(ans, tmp);
        }
    }
    cout << ans << '\n';

    return 0;
}