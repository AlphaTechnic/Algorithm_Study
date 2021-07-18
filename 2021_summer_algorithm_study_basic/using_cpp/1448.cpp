/*
input :
6
2
3
2
3
2
4

output :
10
 */

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

// 전역 변수 선언
int N, num;
int arr[1000005];

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    freopen("input.txt", "r", stdin);

    cin >> N;
    for (int i = 0; i < N; i++){
        cin >> num;
        arr[i] = num;
    }

    sort(arr, arr + N);
    for (int i = N - 1; i > 1; i--){
        if (arr[i - 2] + arr[i - 1] > arr[i]){
            cout << arr[i - 2] + arr[i - 1] + arr[i];
            return 0;
        }
    }

    cout << -1;
    return 0 ;
}