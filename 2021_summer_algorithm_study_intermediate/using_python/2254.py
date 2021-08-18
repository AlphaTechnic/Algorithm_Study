"""
input :
8 -1 0
2 2
2 -2
-2 2
-2 -2
0 10
8 0
-12 1
1 -5

output :
2
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def ccw(A, B, C):
    ret = (B[0] - A[0]) * (C[1] - B[1]) - (B[1] - A[1]) * (C[0] - B[0])
    if ret > 0: return 1
    if ret == 0: return 0
    if ret < 0: return -1


def monotone_chain(points):
    points.sort()

    lower = list()
    for p in points:
        while True:
            if len(lower) >= 2 and ccw(lower[-2], lower[-1], p) < 0:
                lower.pop()
            else:
                break
        lower.append(p)

    upper = list()
    for p in reversed(points):
        while True:
            if len(upper) >= 2 and ccw(upper[-2], upper[-1], p) < 0:
                upper.pop()
            else:
                break
        upper.append(p)

    return lower[:-1] + upper[:-1]


def tytx_in_convex_hull(convex_hull):
    if len(convex_hull) <= 2: return False

    ind = 0
    chk_val = -1
    while True:
        if ind == 0:
            chk_val = ccw((ty, tx), convex_hull[ind - 1], convex_hull[ind])
        else:
            if ccw((ty, tx), convex_hull[ind - 1], convex_hull[ind]) != chk_val:
                return False
        ind += 1
        if ind == len(convex_hull):
            break
    return True


if __name__ == "__main__":
    N, ty, tx = map(int, input().rstrip().split())
    points = list()
    for _ in range(N):
        a, b = map(int, input().rstrip().split())
        points.append((a, b))

    cnt = 0
    while True:
        convex_hull = monotone_chain(points)
        if not tytx_in_convex_hull(convex_hull): break
        points = list(set(points) - set(convex_hull))

        cnt += 1
    print(cnt)