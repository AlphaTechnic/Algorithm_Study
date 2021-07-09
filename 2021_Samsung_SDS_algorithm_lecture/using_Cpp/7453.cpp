/*
input :
6
-45 22 42 -16
-41 -27 56 30
-36 53 -37 77
-36 30 -75 -46
26 -38 -10 62
-32 -54 -6 45

output :
5
*/

#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;
typedef long long LL;

int n;
vector<int> a, b, c, d;
vector<int> ab, cd;

LL get_cnt_by_two_pointer(){
    sort(ab.begin(), ab.end());
    sort(cd.begin(), cd.end());

    int p_ab = 0;
    int p_cd = cd.size() -1;

    LL tot = 0;
    LL tmp = 0;
    while (true){
        if (p_ab == ab.size()){
            break;
        }

        if (p_ab >= 1 && ab[p_ab] == ab[p_ab - 1]){
            tot += tmp;
            p_ab++;
            continue;
        }

        int T = -ab[p_ab];
        while (p_cd >= 0 && T < cd[p_cd]) p_cd--;  // p_cd 왼쪽으로 이동

        tmp = 0;
        while (p_cd >= 0 && T == cd[p_cd]) { // Target을 만나면,
            p_cd--;
            tmp++;
            tot++;
        }
        p_ab++; // p_ab 오른쪽으로 한 칸 이동
    }
    return tot;
}


int main(){
    freopen("input.txt", "r", stdin);
    scanf("%d", &n);
    for (int i = 0; i < n; i++){
        int u, v, w, x;
        scanf("%d%d%d%d", &u, &v, &w, &x);
        a.push_back(u);
        b.push_back(v);
        c.push_back(w);
        d.push_back(x);
    }
    // a, b로 만들 수 있는 합의 조합 -> ab
    // c, d로 만들 수 있는 합의 조합 -> cd
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            ab.push_back(a[i] + b[j]);
            cd.push_back(c[i] + d[j]);
        }
    }

    printf("%lld", get_cnt_by_two_pointer());
}