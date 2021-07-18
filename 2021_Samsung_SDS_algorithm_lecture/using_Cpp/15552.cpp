/*
input :
5
1 1
12 34
5 500
40 60
1000 1000

output:
2
46
505
100
2000
*/

#include <iostream>
using namespace std;

int N;
int a, b;
int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    freopen("input.txt", "r", stdin);

    cin >> N;
    for (int i = 0; i < N; i++){
        cin >> a >> b;
        cout << a + b << '\n';
    }
    return 0;
}
