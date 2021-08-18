"""
input :
1 1 5 5
1 5 5 1

output :
1
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def ccw(vec1, vec2):
    return vec1[0] * vec2[1] - vec1[1] * vec2[0]


def disjoint(a, b, c, d):
    return max(a, b) < min(c, d) or min(a, b) > max(c, d)


def intersect(p1, p2, q1, q2):
    a, b = p1
    c, d = p2
    e, f = q1
    g, h = q2
    AB = [c - a, d - b]
    AC = [e - a, f - b]
    AD = [g - a, h - b]
    CD = [g - e, h - f]
    CA = [a - e, b - f]
    CB = [c - e, d - f]
    ab2cd = ccw(AB, AC) * ccw(AB, AD)
    cd2ab = ccw(CD, CA) * ccw(CD, CB)
    if ab2cd == 0 and cd2ab == 0:
        return not disjoint(a, c, e, g) and not disjoint(b, d, f, h)
    return ab2cd <= 0 and cd2ab <= 0


if __name__ == "__main__":
    a, b, c, d = map(int, input().rstrip().split())
    e, f, g, h = map(int, input().rstrip().split())
    A = [a, b]
    B = [c, d]
    C = [e, f]
    D = [g, h]

    if intersect(A, B, C, D):
        print(1)
    else:
        print(0)
