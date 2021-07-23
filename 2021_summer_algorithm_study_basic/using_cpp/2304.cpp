/*
input :
7
2 4
11 4
15 8
4 6
5 3
8 10
13 6

output :
98
*/

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

// 전역 변수 선언
int height[1001];
int N;


int get_area(){
    int tot = 0;

    // left -> right
    int max1 = 0;
    int x1 = 0;  // 최대값을 만드는 x 값
    for (int i = 0; i < 1001; i++){
        if (height[i] > max1){
            tot += max1 * (i - x1);
            max1 = height[i];
            x1 = i;
        }
    }

    // right -> left
    int max2 = 0;
    int x2 = 0;  // 최대값을 만드는 x 값
    for (int i = 1000; i >= 0; i--){
        if (height[i] > max2){
            tot += max2 * (x2 - i);
            max2 = height[i];
            x2 = i;
        }
    }

    tot += max1 * (x2 - x1 + 1);
    return tot;
}

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> N;
    int a, b;
    for (int i = 0; i < N; i++){
        cin >> a >> b;
        height[a] = b;
    }

    cout << get_area();

    return 0 ;
}