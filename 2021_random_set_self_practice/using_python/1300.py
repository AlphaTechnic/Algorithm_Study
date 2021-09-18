"""
input :
3
7

output :
6
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def num_of_smaller_than(mid):
    global N
    cnt = 0
    for i in range(1, N + 1):
        cnt += min(N, mid // i)
    return cnt


if __name__ == "__main__":
    N = int(input())
    K = int(input())

    l = 1
    r = 10 ** 9 + 1
    mid_save = mid = (l + r) // 2
    while l <= r:
        if num_of_smaller_than(mid) >= K:
            mid_save = mid
            r = mid - 1
            mid = (l + r) // 2
        else:
            l = mid + 1
            mid = (l + r) // 2
    print(mid_save)
