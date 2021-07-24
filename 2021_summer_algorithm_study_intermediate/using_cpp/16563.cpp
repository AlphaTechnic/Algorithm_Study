/*
input :
5
5 4 45 64 54

output :
5
2 2
3 3 5
2 2 2 2 2 2
2 3 3 3
*/

#include <iostream>
#include <algorithm>
using namespace std;

// 전역 변수 선언
int N;
int num;
int least_primes[5000005];


void factorize(int num){
    while (true){
        if (least_primes[num] == 0){
            cout << num << ' ';
            break;
        }
        cout << least_primes[num] << ' ';
        num /= least_primes[num];
    }
}

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> N;
    // 전처리
    for (int i = 2; i < 2240; i++){
        for (int j = i + i; j < 5000001; j += i){
            if (least_primes[j] != 0) continue;
            least_primes[j] = i;
        }
    }
    ///////////////////////////

    while(N--){
        cin >> num;
        factorize(num);
        cout << '\n';
    }

    return 0;
}