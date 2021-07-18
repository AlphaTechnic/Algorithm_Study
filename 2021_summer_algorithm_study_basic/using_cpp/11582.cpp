/*
input :
8
1 5 2 4 2 9 7 3
2

output :
1 2 4 5 2 3 7 9
*/

#include <iostream>
#include <algorithm>
using namespace std;

int N, K;
int arr[2000000];
int tmp[2000000];
int num;


void merge(int s, int e){
    if (e - s + 1 == (N / K) * 2) return;

    int idx1, idx2, idx_tar;
    int mid = (s + e) / 2;
    idx1 = idx_tar = s; idx2 = mid + 1;

    while(idx1 <= mid && idx2 <= e){
        if (arr[idx1] < arr[idx2]) tmp[idx_tar++] = arr[idx1++];
        else tmp[idx_tar++] = arr[idx2++];
    }

    while(idx1 <= mid){
        tmp[idx_tar++] = arr[idx1++];
    }
    while(idx2 <= e){
        tmp[idx_tar++] = arr[idx2++];
    }

    for (int i = s; i <= e; i++){
        arr[i] = tmp[i];
    }
}


void merge_sort(int s, int e){
    if (s == e) return;
    int mid = (s + e) / 2;

    merge_sort(s, mid);
    merge_sort(mid + 1, e);
    merge(s, e);
}


int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    freopen("input.txt", "r", stdin);

    cin >> N;
    for (int i = 0; i < N; i++){
        cin >> num;
        arr[i] = num;
    }
    cin >> K;

    merge_sort(0, N - 1);
    for (int i = 0; i < N; i++){
        cout << arr[i] << ' ';
    }

    return 0 ;
}