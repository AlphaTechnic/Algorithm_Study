/*
input :
5 10
9 13
1 2
3 4
5 6
1 2
3 4
5 6
1 20
1 20

output :
1 2 3 4 10 9 8 7 13 12 11 5 6 14 15 16 17 18 19 20
 */

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int s, e;
vector<int> cards = {0};

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    freopen("input.txt", "r", stdin);

    // 카드 생성
    for (int i = 1; i <= 20; i++){
        cards.push_back(i);
    }

    // 입력 받은 query 수행
    while (true){
        cin >> s >> e;
        if (cin.fail()) break;

        reverse(cards.begin() + s, cards.begin() + e + 1);
    }

    // 결과 출력
    for (int i = 1; i <= 20; i++){
        cout << cards[i] << " ";
    }
    return 0;
}