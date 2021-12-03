/*
input :
5
0 0 8 4
0 5 8 5
2 6 -2 3
-2 3 2 5
-4 0 12 4
3 4 10 4

output :


 */
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Point {
    int x, y;

    explicit Point(int x = 0, int y = 0) : x(x), y(y) {};

    bool operator<(const Point &rhs) const {
        if (x != rhs.x) {
            return x < rhs.x;
        }
        return y < rhs.y;
    }

    bool operator==(const Point &rhs) const {
        return x == rhs.x && y == rhs.y;
    }
};

int ccw(Point p1, Point p2, Point p3) {
    int ret = (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x);

    if (ret > 0) {
        return 1;
    }
    if (ret < 0 ) {
        return -1;
    }
    return 0;
}

int intersect(Point A, Point B, Point C, Point D) {
    int AB_C = ccw(A, B, C);
    int AB_D = ccw(A, B, D);
    int CD_A = ccw(C, D, A);
    int CD_B = ccw(C, D, B);
    int chk1 = AB_C * AB_D;
    int chk2 = CD_A * CD_B;

    // 4개의 점이 일직선 상에 놓여있다.
    if (AB_C == 0 && AB_D == 0 && CD_A == 0 && CD_B == 0) {
        if (B < A) swap(A, B);
        if (D < C) swap(C, D);

        // 점이 하나만 겹친다.
        if (D == A || B == C) return 1;

        // 점이 겹치지 않는다.
        if (D < A || B < C) return 0;

        // 무수히 많은 교점이 있다.
        return -1;
    }
    return chk1 <= 0 && chk2 <= 0;
}

int point_on_line(Point p, Point A, Point B) {
    int ccw_val = ccw(p, A, B);
    int mnx = min(A.x, B.x);
    int mny = min(A.y, B.y);
    int mxx = max(A.x, B.x);
    int mxy = max(A.y, B.y);

    if (ccw_val == 0 && mnx <= p.x && p.x <= mxx && mny <= p.y && p.y <= mxy){
        return 1;
    }
    return 0;
}

int norm_square (Point A, Point B) {
    return (A.x - B.x) * (A.x - B.x) + (A.y - B.y) * (A.y - B.y);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    int N;
    cin >> N;

    int x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;

    vector<Point> points;
    points.push_back(Point(x1, y1));
    points.push_back(Point(x2, y1));
    points.push_back(Point(x2, y2));
    points.push_back(Point(x1, y2));

    Point A, B;
    int mxcnt = -1;
    int min_len = -1;
    int idx = -1;
    for (int i = 0; i < N; i++) {
        cin >> A.x >> A.y >> B.x >> B.y;

        int cnt = 0;
        int len_square = norm_square(A, B);
        for (int j = 0; j < 4; j++) {
            int intersect_flag = intersect(points[j], points[(j + 1) % 4], A, B);

            // 교점 무수히 많음
            if (intersect_flag < 0) {
                cnt = 3;
                break;
            }

            cnt += intersect_flag;
            cnt -= point_on_line(points[j], A, B);
        }

//        cout << cnt << '\n';

        if (mxcnt < cnt) {
            mxcnt = cnt;
            min_len = len_square;
            idx = i + 1;
        }
        else if (mxcnt == cnt && min_len > len_square) {
            min_len = len_square;
            idx = i + 1;
        }
    }

    cout << idx << '\n';
    return 0;
}