"""
input :
2 3 1

output :
11
"""
import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


def what_area(sz, cy, cx):
    if 0 <= cy < 2 ** (sz - 1) and 0 <= cx < 2 ** (sz - 1):
        return 1
    elif (0 <= cy < 2 ** (sz - 1)) and (2 ** (sz - 1) <= cx < 2 ** sz):
        return 2
    elif (2 ** (sz - 1) <= cy < 2 ** sz) and (0 <= cx < 2 ** (sz - 1)):
        return 3
    elif (2 ** (sz - 1) <= cy < 2 ** sz) and (2 ** (sz - 1) <= cx < 2 ** sz):
        return 4


def recur(sz, cy, cx):
    if sz == 0:
        return 1

    area_t = what_area(sz, cy, cx)
    if area_t == 1:
        return recur(sz - 1, cy, cx)
    elif area_t == 2:
        return 1 * (2 ** ((sz - 1) * 2)) + recur(sz - 1, cy, cx - 2 ** (sz - 1))
    elif area_t == 3:
        return 2 * (2 ** ((sz - 1) * 2)) + recur(sz - 1, cy - 2 ** (sz - 1), cx)
    elif area_t == 4:
        return 3 * (2 ** ((sz - 1) * 2)) + recur(sz - 1, cy - 2 ** (sz - 1), cx - 2 ** (sz - 1))


if __name__ == "__main__":
    N, R, C = map(int, input().rstrip().split())

    print(recur(N, R, C) - 1)
