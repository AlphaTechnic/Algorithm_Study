/*
input :
4

output :
5
*/

#include <iostream>
#include <algorithm>
using namespace std;

// 전역 변수 선언
int N;

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    freopen("input.txt", "r", stdin);

    cin >> N;
    if (N == 1) {
        cout << 1 << '\n';
        return 0;
    }
    if (N == 2) {
        cout << 2 << '\n';
        return 0;
    }

    int a = 1;
    int b = 2;
    int tmp;
    int c;
    while (N - 2 != 0){
        tmp = b;

        c = (a + b) % 15746;
        b = c;
        a = tmp;

        N--;
    }
    cout << c << '\n';

    return 0;
}