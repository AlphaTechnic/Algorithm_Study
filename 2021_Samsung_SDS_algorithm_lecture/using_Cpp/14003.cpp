/*
input :
6
10 20 10 30 20 50

output :
4
10 20 30 50
*/

#include <iostream>
#include <algorithm>
using namespace std;
using ll = long long;

// 전역 변수 선언
#define PIV (1 << 20)
#define INF 1000000005
int tree[2 * PIV];
int N, num;


typedef struct num_ind{
    int val;
    int ind;
}num_ind;

bool comp(num_ind a, num_ind b){
    if (a.val == b.val){
        return a.ind > b.ind;
    }
    return a.val < b.val;
}

num_ind num_inds[PIV];
int arr[PIV];
int dp[PIV];
int ans[PIV];

void update(int n, int v){
    tree[n += PIV] = v;
    while (n >>= 1){
        tree[n] = max(tree[n], v);
    }
}

int query(int n){
    int l = PIV, r = n + PIV;
    int ret = 0;
    while (l <= r){
        if (l & 1) ret = max(ret, tree[l++]);
        if (!(r & 1)) ret = max(ret, tree[r--]);
        l >>= 1, r >>= 1;
    }
    return ret;
}


int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    freopen("input.txt", "r", stdin);

    cin >> N;
    for (int i = 0; i < N; i++){
        cin >> num;
        num_inds[i] = {num, i};
        arr[i] = num;
    }
    sort(num_inds, num_inds + N, comp);

    // max_val을 인덱스트리로 logN으로 찾아버림
    // dp를 만드려면,
    // 1. 본인보다 dp값 작은 애들을 모두 살펴야 함 -> val로 정렬
    // 2. 그 중 index도 작은 애들 모두 살펴야 함 -> index의 왼쪽에 대해서만 query 날림
    int length = 0;
    int max_val;
    for (int i = 0; i < N; i++){
        max_val = query(num_inds[i].ind - 1);
        max_val++;

        update(num_inds[i].ind, max_val);
        dp[num_inds[i].ind] = max_val;
        length = max(length, max_val);
    }
    cout << length << '\n';

    int cnt = length;
    int ret = INF;
    for (int i = N - 1; i >= 0; i--){
        if (dp[i] == cnt && arr[i] < ret){
            ans[--cnt] = arr[i];
            ret = arr[i];
        }
    }

    for (int i = 0; i < length; i++){
        cout << ans[i] << ' ';
    }
    cout << "\n";

    return 0 ;
}