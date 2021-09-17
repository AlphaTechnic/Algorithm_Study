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


def ccw(p1, p2, p3):  # ad - bc
    ret = (p2[0] - p1[0]) * (p3[1] - p2[1]) - (p2[1] - p1[1]) * (p3[0] - p2[0])
    if ret > 0:
        return 1
    elif ret < 0:
        return -1
    else:
        return 0


if __name__ == "__main__":
    p1 = list(map(int, input().rstrip().split()))
    p2 = list(map(int, input().rstrip().split()))
    p3 = list(map(int, input().rstrip().split()))
    print(ccw(p1, p2, p3))
