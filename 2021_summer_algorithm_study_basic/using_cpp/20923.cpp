/*
input :
10 12
1 2
2 2
1 2
2 3
3 1
2 2
2 5
2 1
5 1
2 3

output :
do
*/

#include <iostream>
#include <algorithm>
#include <deque>
using namespace std;

// 전역 변수 선언
int CARD_NUM, GAME_NUM;
int a, b;
int d, s;
deque<int> do_cards, su_cards;
deque<int> do_ground, su_ground;


int do_open(){
    int num = do_cards.back(); do_cards.pop_back();
    if (do_cards.size() == 0){
        cout << "su"; exit(0);
    }
    do_ground.push_back(num);
    return num;
}

int su_open(){
    int num = su_cards.back(); su_cards.pop_back();
    if (su_cards.size() == 0){
        cout << "do"; exit(0);
    }
    su_ground.push_back(num);
    return num;
}

void do_ring(){
    while (su_ground.size() != 0){
        int num = su_ground.front(); su_ground.pop_front();
        do_cards.push_front(num);
    }
    while (do_ground.size() != 0){
        int num = do_ground.front(); do_ground.pop_front();
        do_cards.push_front(num);
    }
}

void su_ring(){
    while (do_ground.size() != 0){
        int num = do_ground.front(); do_ground.pop_front();
        su_cards.push_front(num);
    }
    while (su_ground.size() != 0){
        int num = su_ground.front(); su_ground.pop_front();
        su_cards.push_front(num);
    }
}

void init_ds(){
    s = -1; d = -1;
}


int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> CARD_NUM >> GAME_NUM;
    while (CARD_NUM--){
        cin >> a >> b;
        do_cards.push_back(a);
        su_cards.push_back(b);
    }

    init_ds();
    while (true){
        d = do_open();
        if (d == 5){
            do_ring();
            init_ds();
        }
        else if (d + s == 5){
            su_ring();
            init_ds();
        }
        GAME_NUM--; if (GAME_NUM == 0) break;

        s = su_open();
        if (s == 5){
            do_ring();
            init_ds();
        }
        else if (d + s == 5){
            su_ring();
            init_ds();
        }
        GAME_NUM--; if (GAME_NUM == 0) break;
    }

    if (do_cards.size() > su_cards.size()) cout << "do";
    else if (do_cards.size() == su_cards.size()) cout << "dosu";
    else cout << "su";

    return 0;
}