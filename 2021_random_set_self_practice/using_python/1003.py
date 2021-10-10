"""
input :
3
0
1
3

output:
1 0
0 1
1 2
"""
import sys

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


def recur(N):
    if N == 0:
        cnt0[N] = 1
        cnt1[N] = 0
        return 1, 0
    if N == 1:
        cnt0[N] = 0
        cnt1[N] = 1
        return 0, 1
    if cnt0[N] != -1:
        return cnt0[N], cnt1[N]

    a0, a1 = recur(N - 1)
    b0, b1 = recur(N - 2)
    cnt0[N] = a0 + b0
    cnt1[N] = a1 + b1
    return cnt0[N], cnt1[N]


if __name__ == "__main__":
    # 전처리
    cnt0 = [-1 for _ in range(41)]
    cnt1 = [-1 for _ in range(41)]
    recur(40)

    T = int(input())
    for _ in range(T):
        N = int(input())
        print(cnt0[N], cnt1[N])
