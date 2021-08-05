"""
input :
4
1 1 5 31
1 1 6 30
5 15 8 31
6 10 12 10

output :
2
"""

import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline


def find_max_reach(ind, l_limit):
    max_r = -1
    while True:
        ind += 1
        if ind == N: break

        if intervals[ind][0] <= l_limit:
            max_r = max(max_r, intervals[ind][1])
        else:
            break
    return ind - 1, max_r


if __name__ == "__main__":
    N = int(input())
    intervals = []
    for _ in range(N):
        sa, sb, ea, eb = map(int, input().rstrip().split())
        start = sa * 100 + sb
        end = ea * 100 + eb
        intervals.append([start, end])

    intervals.sort()

    cnt = 0
    l_limit = 301
    success = True
    in_ind = -1
    while True:
        if l_limit > 1130:
            break

        # in_ind에 비해 out_ind는 계속 증가해서 나와야한다.
        # 바통을 이어받을 꽃이 있다는 의미
        out_ind, r = find_max_reach(in_ind, l_limit)
        if in_ind == out_ind:
            success = False
            break

        in_ind = out_ind
        cnt += 1
        l_limit = r

    if success:
        print(cnt)
    else:
        print(0)
