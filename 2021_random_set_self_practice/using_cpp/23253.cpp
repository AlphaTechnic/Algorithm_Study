/*
input :
4 2
2
3 1
2
4 2

output :
Yes
 */
#include <iostream>
#include <algorithm>

using namespace std;
#define MAX (200005)
// 전역 변수 선언

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    int N, DUMMY;
    cin >> N >> DUMMY;
    for (int i = 0; i < DUMMY; i++){
        int stksz;

        cin >> stksz;
        int mnv = MAX;
        for (int j = 0; j < stksz; j++){
            int tmp;

            cin >> tmp;
            if (mnv > tmp) {
                mnv = tmp;
            }
            else{
                cout << "No" << '\n';
                return 0;
            }
        }
    }
    cout << "Yes" << '\n';
    return 0;
}