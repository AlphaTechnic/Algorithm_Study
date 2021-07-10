/*
input :
1 3

output :
0.33333333333333333333333333333333
*/

#include <iostream>
#include <iomanip> // for std::setprecision()
using namespace std;

long double a, b;
int main(){
    cout << setprecision(32);
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    freopen("input.txt", "r", stdin);

    cin >> a >> b;
    cout << a / b;

    return 0;
}