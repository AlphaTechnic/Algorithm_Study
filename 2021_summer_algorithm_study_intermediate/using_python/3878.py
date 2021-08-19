"""
input :
10
3 3
100 700
200 200
600 600
500 100
500 300
800 500
3 3
100 300
400 600
400 100
600 400
500 900
300 300
3 4
300 300
500 300
400 600
100 100
200 900
500 900
800 100
1 2
300 300
100 100
500 500
1 1
100 100
200 100
2 2
0 0
500 700
1000 1400
1500 2100
2 2
0 0
1000 1000
1000 0
0 1000
3 3
0 100
4999 102
10000 103
5001 102
10000 102
0 101
3 3
100 100
200 100
100 200
0 0
400 0
0 400
3 3
2813 1640
2583 2892
2967 1916
541 3562
9298 3686
7443 7921

output :
YES
NO
NO
NO
YES
YES
NO
NO
NO
YES
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def ccw(A, B, C):
    ret = (B[0] - A[0]) * (C[1] - B[1]) - (B[1] - A[1]) * (C[0] - B[0])
    if ret > 0: return 1
    if ret == 0: return 0
    if ret < 0: return -1


def disjoint(a, b, c, d):
    return max(a, b) < min(c, d) or min(a, b) > max(c, d)


def monotone_chain(points):
    if len(points) <= 2: return points
    points.sort()

    lower = list()
    for p in points:
        while True:
            if len(lower) >= 2 and ccw(lower[-2], lower[-1], p) <= 0:
                lower.pop()
            else:
                break
        lower.append(p)

    upper = list()
    for p in reversed(points):
        while True:
            if len(upper) >= 2 and ccw(upper[-2], upper[-1], p) <= 0:
                upper.pop()
            else:
                break
        upper.append(p)

    return lower[:-1] + upper[:-1]


def p_in_convex_hull(convex_hull, p):
    if len(convex_hull) <= 2: return False

    for i in range(len(convex_hull)):
        if ccw(p, convex_hull[i - 1], convex_hull[i]) < 0:
            return False
    return True


def disjoint(a, b, c, d):
    return max(a, b) < min(c, d) or min(a, b) > max(c, d)


def intersect(p1, p2, q1, q2):
    AB2CD = ccw(p1, p2, q1) * ccw(p1, p2, q2)
    CD2AB = ccw(q1, q2, p1) * ccw(q1, q2, p2)
    if AB2CD == 0 and CD2AB == 0:
        return not disjoint(p1[0], p2[0], q1[0], q2[0]) and not disjoint(p1[1], p2[1], q1[1], q2[1])
    return AB2CD <= 0 and CD2AB <= 0


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        B, W = map(int, input().rstrip().split())
        b_points = []
        for _ in range(B):
            a, b = map(int, input().rstrip().split())
            b_points.append((a, b))
        w_points = []
        for _ in range(W):
            a, b = map(int, input().rstrip().split())
            w_points.append((a, b))

        b_hull = monotone_chain(b_points)
        w_hull = monotone_chain(w_points)

        RES = True
        FINISH = False
        # (점과 점) 혹은 (라인과 점)이 들어왔을 때 예외케이스
        if len(b_hull) == 1 and len(w_hull) == 1:
            RES = True
            FINISH = True
        if len(b_hull) == 2 and len(w_hull) == 1:
            if intersect(b_hull[0], b_hull[1], w_hull[0], w_hull[0]):
                RES = False
            FINISH = True
        elif len(b_hull) == 1 and len(w_hull) == 2:
            if intersect(w_hull[0], w_hull[1], b_hull[0], b_hull[0]):
                RES = False
            FINISH = True
        elif len(b_hull) == 2 and len(w_hull) == 2:
            if intersect(b_hull[0], b_hull[1], w_hull[0], w_hull[1]):
                RES = False
            FINISH = True

        # 일반적인 경우
        # b_hull의 어떠한 점도 w_hull에 있으면 안됨
        # w_hull의 어떠한 점도 b_hull에 있으면 안됨
        if not FINISH:
            for p in b_hull:
                if p_in_convex_hull(w_hull, p):
                    RES = False
                    break

            if RES:
                for p in w_hull:
                    if p_in_convex_hull(b_hull, p):
                        RES = False
                        break

        if RES:
            print("YES")
        else:
            print("NO")

        b_points.clear()
        w_points.clear()
