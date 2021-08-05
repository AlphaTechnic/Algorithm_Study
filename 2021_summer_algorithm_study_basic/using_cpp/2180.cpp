/*
input :
3
2 0
1 2
0 3

output :
5
*/

#include <iostream>
#include <algorithm>
#include <vector>
#define MOD (40000)
using namespace std;
using ll = long long;

typedef struct ab{
    double a, b;
};

// 전역 변수 선언
int N;
vector<ab> ab_vec;

bool comp(ab struct1, ab struct2){
    if (struct1.a == 0) return false;
    if (struct2.a == 0) return true;
    return struct1.b / struct1.a < struct2.b / struct2.a;
}

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> N;
    while (N--){
        double a, b;
        cin >> a >> b;
        ab_vec.push_back({a, b});
    }
    sort(ab_vec.begin(), ab_vec.end(), comp);

    ll tot = 0;
    for (ab struct1: ab_vec){
        tot += (((ll)struct1.a * tot) % MOD + (ll)struct1.b) % MOD;
    }
    cout << tot % MOD;

    return 0;
}