"""
input :
2 6
7
10

output :
28
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def num_of_done(mid):
    cnt = 0
    for taken_time in taken_times:
        cnt += mid // taken_time
    return cnt


if __name__ == "__main__":
    N, M = map(int, input().rstrip().split())
    taken_times = []
    for _ in range(N):
        taken_times.append(int(input()))

    l = 1
    r = max(taken_times) * M
    mid_save = mid = (l + r) // 2
    while l <= r:
        if num_of_done(mid) >= M:
            mid_save = mid
            r = mid - 1
            mid = (l + r) // 2
        else:
            l = mid + 1
            mid = (l + r) // 2

    print(mid_save)
