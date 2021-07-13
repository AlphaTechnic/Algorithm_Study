/*
input :
72

output :
2
2
2
3
3
*/

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

// 전역 변수 선언
bool chk[3200];
vector<int> primes;
int N;

bool comp(int a, int b){
    return true;
}

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    freopen("input.txt", "r", stdin);

    for (int i = 2; i < 3200; i++){
        if (chk[i] == true) continue;
        for (int j = i + i; j < 3200; j += i){
            chk[j] = true;
        }
    }

    for (int i = 2; i < 3200; i ++){
        if (chk[i] == false) primes.push_back(i);
    }

    cin >> N;
    for (int i = 0; i < primes.size(); i++){
        if (N % primes[i] == 0){
            while (true){
                cout << primes[i] << '\n';
                N /= primes[i];

                if (N % primes[i] != 0) break;
            }
        }
    }
    if (N > 1) cout << N;

    return 0 ;
}