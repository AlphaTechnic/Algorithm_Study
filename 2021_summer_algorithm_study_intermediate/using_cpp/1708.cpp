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

bool disjoint(ll s, ll e, ll l, ll r){
    return max(s, e) < min(l, r) || min(s, e) > max(l, r);
}

bool intersect (Point A, Point B, Point C, Point D){
    ll ab = cross(A, B, C) * cross(A, B, D);
    ll cd = cross(C, D, A) * cross(C, D, B);
    if (ab == 0 && cd == 0){
        return !disjoint(A.x, B.x, C.x, D.x) && !disjoint(A.y, B.y, C.y, D.y);
    }
    return ab <= 0 && cd <= 0;
}

vector<Point> grahm_scan(vector<Point> points){
    if (points.size() <= 2) return points;
    int N = points.size();
    swap(points[0], *min_element(points.begin(), points.end(), [] (Point a, Point b){
        if (a.y == b.y) return a.x < b.x;
        return a.y < b.y;
    }));

    // 원점으로 평행이동
    for (int i = 1; i < N; i++){
        points[i] = points[i] - points[0];
    }
    points[0].x = points[0].y = 0;

    // 각도 순으로 정렬
    sort(points.begin() + 1, points.end(), [] (Point a, Point b){
        ll c = cross(a, b);
        if (c == 0) return (a.x * a.x + a.y * a.y) < (b.x * b.x + b.y * b.y);
        return c > 0;
    });

    vector<Point> ST;
    for (int i = 0; i < N; i++){
        while (true){
            if (ST.size() >= 2 && cross(ST[ST.size() - 2], ST[ST.size() - 1], points[i]) <= 0){
                ST.pop_back();
            }
            else {
                break;
            }
        }
        ST.push_back(points[i]);
    }
    return ST;
}


// 전역 변수 선언
Point A, B, C, D;
vector<Point> points;
int N;


int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> N;
    for (int i = 0; i < N; i++){
        Point P;
        cin >> P.x >> P.y;
        points.push_back(P);
    }
    vector<Point> ans = grahm_scan(points);
    cout << ans.size();

    return 0;
}