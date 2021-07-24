/*
input :
5
1 1 1 1 1

output :
5 4 3 2 1
*/

#include <iostream>
#include <algorithm>
#include <deque>
#include <vector>
using namespace std;

// 전역 변수 선언
int N, num;
deque<int> ground, card_deq;
vector<int> actions;


void action1(){
    num = ground.front(); ground.pop_front();
    card_deq.push_front(num);
}

void action2(){
    int num1 = ground.front(); ground.pop_front();
    int num2 = card_deq.front(); card_deq.pop_front();
    card_deq.push_front(num1);
    card_deq.push_front(num2);
}

void action3(){
    num = ground.front(); ground.pop_front();
    card_deq.push_back(num);
}

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> N;
    for (int i = 1; i <= N; i++){
        ground.push_back(i);
    }

    for (int i = 0; i < N; i++){
        cin >> num; actions.push_back(num);
    }

    while(N--){
        int action = actions.back(); actions.pop_back();
        switch(action){
            case 1:
                action1();
                break;
            case 2:
                action2();
                break;
            case 3:
                action3();
                break;
            default:
                // no aciton
                exit(0);
        }
    }

    for (int num: card_deq){
        cout << num << ' ';
    }

    return 0;
}