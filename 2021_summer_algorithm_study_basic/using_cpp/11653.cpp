/*
input :
12
Junkyu 50 60 100
Sangkeun 80 60 50
Sunyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taewhan 50 60 90

output :
Donghyuk
Sangkeun
Sunyoung
nsj
Wonseob
Sanghyun
Sei
Kangsoo
Haebin
Junkyu
Soong
Taewhan
*/

#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
typedef struct score{
    string name;
    int ko;
    int en;
    int ma;
}score;

int N;
string name;
int a, b, c;


bool comp(score a, score b){
    if (a.ko == b.ko && a.en == b.en && a.ma == b.ma) return a.name < b.name;
    else if (a.ko == b.ko && a.en == b.en) return a.ma > b.ma;
    else if (a.ko == b.ko) return a.en < b.en;
    return a.ko > b.ko;
}
score scores[100005];

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    freopen("input.txt", "r", stdin);

    cin >> N;
    for (int i = 0; i < N; i++){
        score data;
        cin >> name >> a >> b >> c;
        data.name = name; data.ko = a; data.en = b; data.ma = c;
        scores[i] = data;
    }

    sort(scores, scores + N, comp);
    for (int i = 0; i < N; i++){
        cout << scores[i].name << '\n';
    }

    return 0 ;
}