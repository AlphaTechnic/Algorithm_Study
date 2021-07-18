/*
input :
5
10
1
5
2
3

output :
3
*/

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
typedef pair<int, int> pii;

// 전역 변수 선언
int N, num;
pii arr[500005];
int diff[500005];

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    freopen("input.txt", "r", stdin);

    cin >> N;
    for (int i = 0; i < N; i++){
        cin >> num;
        arr[i] = {num, i};
    }
    sort(arr, arr + N);

//    for (int i = 0; i < N; i++){
//        cout << '(' << arr[i].first << ' ' << arr[i].second << ") ";
//    }

    int ans = 0;
    for (int i = 0; i < N; i++){
        diff[i] = arr[i].second - i;
        ans = max(ans, diff[i]);
    }

    cout << ans + 1;

    return 0 ;
}