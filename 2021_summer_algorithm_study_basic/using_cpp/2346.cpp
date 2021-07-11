/*
input :
5
3 2 1 -3 -1

output :
1 4 5 3 2
 */

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N, balloon_num;
int ind;
int dx;
vector<pair<int, int>> balloons;

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    freopen("input.txt", "r", stdin);

    cin >> N;
    if (N == 1){
        cout << 1;
        return 0;
    }

    for (int i = 1; i <= N; i++){
        cin >> dx;
        balloons.push_back({i, dx});
    }

    balloon_num = balloons[0].first;
    dx = (balloons[0].second > 0)? (balloons[0].second - 1) : (balloons[0].second);
    cout << balloon_num << " ";
    balloons.erase(balloons.begin());

    // 여기서 새로운 ind로 ind 조정
    ind += dx;
    if (ind >= (int)balloons.size()){
        ind = (ind - balloons.size()) % balloons.size();
    }
    else if (ind < 0){
        ind = (balloons.size() * 1000 + ind) % balloons.size();
    }

    while (true){
        balloon_num = balloons[ind].first;
        dx = (balloons[ind].second > 0)? (balloons[ind].second - 1) : (balloons[ind].second);
        cout << balloon_num << " ";
        balloons.erase(balloons.begin() + ind);

        if (balloons.empty()) break;

        // 여기서 새로운 ind로 ind 조정
        ind += dx;
        if (ind >= (int)balloons.size()){
            ind = (ind - balloons.size()) % balloons.size();
        }
        else if (ind < 0){
            ind = (balloons.size() * 1000 + ind) % balloons.size();
        }
    }

    return 0;
}