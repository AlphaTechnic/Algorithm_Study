"""
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
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def ccw(A, B, C):
    return (B[0] - A[0]) * (C[1] - B[1]) - (B[1] - A[1]) * (C[0] - B[0])


def monotone_chain(points):
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


if __name__ == "__main__":
    N = int(input())
    points = list()
    for _ in range(N):
        a, b = map(int, input().rstrip().split())
        points.append([a, b])

    print(len(monotone_chain(points)))

