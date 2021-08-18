/*
input :
8
1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2

output :
5
*/

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
using ll = long long;

struct Point{
    ll x, y;
    Point() {};
    Point(ll x, ll y) : x(x), y(y) {};
    Point operator+(const Point &rhs) const {
        return Point(x + rhs.x, y + rhs.y);
    };
    Point operator-(const Point &rhs) const {
        return Point(x - rhs.x, y - rhs.y);
    };
    bool operator<(Point &rhs){
        if (x == rhs.x) return y < rhs.y;
        return x < rhs.x;
    }
};

ll cross (const Point &A, const Point &B){
    ll ret = A.x * B.y - A.y * B.x;
    if (ret > 0) return 1;
    else if (ret == 0) return 0;
    else return -1;
}

ll cross (const Point &A, const Point &B, const Point &C){
    return cross(B - A, C - B);
}

bool intersect (Point A, Point B, Point C, Point D){
    ll ab = cross(A, B, C) * cross(A, B, D);
    ll cd = cross(C, D, A) * cross(C, D, B);
    return ab < 0 && cd < 0;
}
// 전역 변수 선언
Point A, B, C, D;


int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> A.x >> A.y >> B.x >> B.y;
    cin >> C.x >> C.y >> D.x >> D.y;
    cout << intersect(A, B, C, D);

    return 0;
}