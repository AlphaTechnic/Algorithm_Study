/*
input :
2 7
3 5

output :
31 35
*/

#include <iostream>
#include <algorithm>
using namespace std;

// 전역 변수 선언
int a, b, c, d;
int p, q;

int gcd(int a, int b){
    if (b == 0) return a;
    return gcd(b, a % b);
}

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    freopen("input.txt", "r", stdin);

    cin >> a >> b >> c >> d;
    q = a * d + b * c;
    p = b * d;
    int g = gcd(p, q);
    cout << q / g << ' ' << p / g;

    return 0 ;
}