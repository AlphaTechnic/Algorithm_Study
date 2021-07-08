#include <cstdio>
#include <vector>
using namespace std;

int N;
int ALPHA_CNT; // 서로 다른 알파벳의 갯수
char WORD[10][10];
int CHK[128]; // ASCII가 128개
bool USED[10];
int MAPPING[10];
vector<char> ALPHA;
int ANS;
/*
 * MAPPING ind 0 1 2 3 4 5
 * MAPPING val 9 7 1 2 5 6
 * ALPHA   val Z A X Y D E
 * */

void do_mapping(){
    for (int i = 0; i < ALPHA_CNT; i++){
        CHK[ALPHA[i]] = MAPPING[i];
    }
}

int to_num(char c){
    return CHK[c];
}

// k번째 문자열을 계산한 값
int get_val(int k){
    int res = 0;
    for (int i = 0; WORD[k][i] != 0; i++){
        int num = to_num(WORD[k][i]);
        res *= 10, res += num;
    }
    return res;
}

int calc(){
    int tot = 0;
    for (int i = 0; i < N; i++){
        tot += get_val(i);
    }
    return tot;
}

// 모든 경우의 matching을 일일이 get
void brute_force(int who){
    // 종료 조건
    if (who == ALPHA_CNT){
        do_mapping();
        int tmp = calc();
        if (tmp > ANS) ANS = tmp;

//        for (int i = 0; i < ALPHA_CNT; i++){
//            printf("%d ", MAPPING[i]);
//        }
//        printf("\N");
        return;
    }

    for (int i = 0; i <= 9; i++){
        if(USED[i]) continue;

        USED[i] = true;
        MAPPING[who] = i;

        brute_force(who + 1);

        MAPPING[who] = 0; // 꼭 필요한 작업은 아님
        USED[i] = false;

    }

}

int main(){
    freopen("input.txt", "r", stdin);
    scanf("%d", &N);
    for (int i = 0; i < N; i++){
        scanf("%s", WORD[i]);
        for (int j = 0; WORD[i][j] != 0; j++){
            if(!CHK[WORD[i][j]]){
                ALPHA_CNT++;
                CHK[WORD[i][j]] = 1;
                ALPHA.push_back(WORD[i][j]);
            }
        }
    }

    // 작업 : 숫자들을 하나씩 MAPPING
    brute_force(0);
    printf("%d", ANS);
}