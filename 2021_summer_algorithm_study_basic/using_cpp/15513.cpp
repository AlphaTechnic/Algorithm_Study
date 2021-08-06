/*
input :
3
2 3000
5 5000
7 2000

output :
2 3 1
*/

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

typedef struct ppi{
    int price, prob, ind;
};

// 전역 변수 선언
int N;
ppi ppis[1000005];

bool comp(ppi obj1, ppi obj2){
    if ((10000 - obj1.prob) * obj2.price == (10000 - obj2.prob) * obj1.price)
        return obj1.ind < obj2.ind;
    return (10000 - obj1.prob) * obj2.price < (10000 - obj2.prob) * obj1.price;
}

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> N;
    for (int i = 0; i < N; i++){
        int price, prob;
        cin >> price >> prob;
        ppis[i] = {price, prob, i + 1};
    }

    sort(ppis, ppis + N, comp);

    for (int i = 0; i < N; i++){
        cout << ppis[i].ind << ' ';
    }
    cout << '\n';

    return 0;
}