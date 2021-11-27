/*
input :
5
0.000 0.000
1.000 1.000
2.000 0.000
3.000 1.500
2.235 2.483

output :
RIGHT
LEFT
LEFT
 */
#include <iostream>
#define SZ (10003)

using namespace std;

typedef struct coordinate {
    double x;
    double y;
}coordinate;


class Prisoner {
public:
    int N;
    coordinate seq[SZ];

    void input();
    int ccw(coordinate p1, coordinate p2, coordinate p3);
    void go();
};

void Prisoner::input() {
    // input
    freopen("input.txt", "r", stdin);
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> this->N;
    double a;
    double b;
    for (int i = 0; i < this->N; i++) {
        cin >> a;
        cin >> b;
        seq[i] = {a, b};
    }
}

int Prisoner::ccw(coordinate p1, coordinate p2, coordinate p3) {
    double ret = (p2.x - p1.x) * (p3.y - p2.y) - (p2.y - p1.y) * (p3.x - p2.x);
    if (ret > 0) {
        return 1;
    }
    else if (ret < 0) {
        return -1;
    }
    else{
        return 0;
    }
}

void Prisoner::go() {
    int idx = 0;
    while (idx != this->N - 2) {
        int ret = ccw(seq[idx], seq[idx + 1], seq[idx + 2]);
        switch (ret) {
            case 1:
                cout << "LEFT\n";
                break;
            case -1:
                cout << "RIGHT\n";
                break;
            default:
                /* invalid entry */
                break;
        }
        idx++;
    }
}

int main() {
    Prisoner prisoner;
    prisoner.input();
    prisoner.go();

    return 0;
}