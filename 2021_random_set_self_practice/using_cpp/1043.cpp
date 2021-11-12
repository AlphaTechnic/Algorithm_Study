/*
input :
10 9
4 1 2 3 4
2 1 5
2 2 6
1 7
1 8
2 7 8
1 9
1 10
2 3 10
1 4

output :
4
*/
#include <iostream>
#include <set>
#include <algorithm>
#define SZ (55)

using namespace std;

// 전역변수 선언
int N, P, T;
set<int> tmans;
set<int> parties[SZ];
bool chk[SZ];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> N >> P;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int t;
        cin >> t;
        tmans.insert(t);
    }

    for (int i = 0; i < P; i++) {
        set<int> party;
        int num;
        cin >> num;
        for (int j = 0; j < num; j++) {
            int mem;
            cin >> mem;
            party.insert(mem);
        }
        parties[i] = party;
    }


    while (true) {
        int sz_save = tmans.size();
        for (int i = 0; i < P; i++) {
            for (set<int>::iterator iter1 = parties[i].begin(); iter1 != parties[i].end(); iter1++) {
                if (!chk[i]){
                    if (tmans.find(*iter1) != tmans.end()) { // *iter1 in tmans
                        for (set<int>::iterator iter2 = parties[i].begin(); iter2 != parties[i].end(); iter2++) {
                            tmans.insert(*iter2);
                        }
                        chk[i] = true;
                        break;
                    }
                }
            }
        }
        if (sz_save == tmans.size()) {
            break;
        }
    }

    int cnt = 0;
    for (int i = 0; i < P; i++) {
        if (!chk[i]) cnt++;
    }
    cout << cnt << '\n';

    return 0;
}

