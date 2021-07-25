/*
input :
5
4 6 3 8 9

output :
9
*/

#include <iostream>
#include <algorithm>
using namespace std;
using ll = long long;

// 전역 변수 선언
int N, num;
ll participant_num;
int cnt[2000005];
int max_val = -1;
ll ans = -1;

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> N;
    while (N--){
        cin >> num;
        cnt[num]++;
        max_val = max(max_val, num);
    }

    for (ll i = 1; i <= max_val; i++){
        participant_num = 0;
        for (int j = i; j <= max_val; j += i){
            participant_num += cnt[j];
        }

        if (participant_num >= 2){
            ans = max(ans, participant_num * i);
        }
    }
    cout << ans;

    return 0;
}