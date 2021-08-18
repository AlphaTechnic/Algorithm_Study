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


if __name__ == "__main__":
    a, b, c, d = map(int, input().rstrip().split())
    e, f, g, h = map(int, input().rstrip().split())
    A = [a, b]
    B = [c, d]
    C = [e, f]
    D = [g, h]
    AB = [c - a, d - b]
    AC = [e - a, f - b]
    AD = [g - a, h - b]
    CA = [e - a, f - b]
    CB = [e - c, f - d]
    CD = [g - e, h - f]
    if ccw(AB, AC) * ccw(AB, AD) < 0 and ccw(CD, CA) * ccw(CD, CB) < 0:
        print(1)
    else:
        print(0)
