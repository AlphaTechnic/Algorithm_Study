/*
input :
5
1 2 3 4 5
6 4 6 1 2

output :
3 4 5 1 2
*/

#include <iostream>
#include <algorithm>
#define PIV (1 << 18)
using namespace std;

// 전역 변수 선언
int tree[2 * PIV];
int N;

void update(int ind, int val){
    ind += PIV;
    tree[ind] += val;

    while (ind >>= 1){
        tree[ind] += val;
    }
}


int search(int kth){
    int ind = 1;
    while (!(PIV <= ind)){
        if (kth <= tree[2 * ind]) ind *= 2;
        else{
            kth = kth - tree[2 * ind];
            ind = 2 * ind  + 1;
        }
    }
    return ind - PIV;
}

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> N;
    int length;
    for (int i = 1; i <= N; i++){
        cin >> length;
        update(i, length);
    }
    int kth, num;
    while(N--){
        cin >> kth;
        num = search(kth);
        cout << num << ' ';
        update(num, - tree[PIV + num]);
    }


    return 0;
}