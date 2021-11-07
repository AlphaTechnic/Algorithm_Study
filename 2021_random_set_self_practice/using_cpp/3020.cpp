/*
input :
6 7
1
5
3
3
5
1

output :
2 3
 */
#include <iostream>
#define SZH (500005)
using namespace std;

// 전역 변수 선언
int N, H;
int chk[SZH];
int accum_tot[SZH];

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);
    cin >> N >> H;
    for (int i = 0; i < N; i += 2) {
        int num;
        cin >> num;
        chk[0]++;
        chk[num]--;

        cin >> num;
        chk[H - num]++;
        chk[H]--;
    }

//    for (int i = 0; i <= H; i++) {
//        cout << chk[i] << ' ';
//    }
//    cout << '\n';

    int tot = 0;
    for (int i = 0; i < H; i++) {
        tot += chk[i];
        accum_tot[i] = tot;
    }

//    for (int i = 0; i <= H; i++) {
//        cout << accum_tot[i] << ' ';
//    }
//    cout << '\n';

    int mnv = SZH;
    int num = 0;
    for (int i = 0; i < H; i++) {
        if (accum_tot[i] < mnv) {
            mnv = accum_tot[i];
            num = 1;
        }
        else if (accum_tot[i] == mnv) {
            num++;
        }
    }
    cout << mnv << ' ' << num << '\n';

    return 0;
}