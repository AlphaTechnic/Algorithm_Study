"""
input :
1 1
5 5
7 3

output :
-1
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def ccw(vec1, vec2):
    return vec1[0] * vec2[1] - vec1[1] * vec2[0]


if __name__ == "__main__":
    a, b = map(int, input().rstrip().split())
    c, d = map(int, input().rstrip().split())
    e, f = map(int, input().rstrip().split())
    vec1 = [c - a, d - b]
    vec2 = [e - c, f - d]
    if ccw(vec1, vec2) > 0:
        print(1)
    elif ccw(vec1, vec2) < 0:
        print(-1)
    else:
        print(0)
