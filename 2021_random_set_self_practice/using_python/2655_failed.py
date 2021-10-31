"""
input :
5
25 3 4
4 4 6
9 2 3
16 2 5
1 5 2

output :
3
5
3
1
"""
import sys

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    data = []
    IDX = []
    V = []
    W = []
    for i in range(N):
        data.append(list(map(int, input().rstrip().split())) + [i])

    data.sort(reverse=True)
    for _, val, wt, idx in data:
        IDX.append(idx)
        V.append(val)
        W.append(wt)

    # get dp for LDS
    dp = [1 for _ in range(N)]
    for i in range(1, N):
        for j in range(i):
            if W[j] >= W[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    # print(dp)

    # get maximum values
    dp2 = [V[0]] + [0 for _ in range(N - 1)]
    for i in range(1, N):
        for j in range(i):
            if dp[i] == 1:
                dp2[i] = V[i]
                continue
            if dp[i] == dp[j] + 1 and W[i] <= W[j]:
                dp2[i] = max(dp2[i], dp2[j] + V[i])
    # print(dp2)

    # dp2 reverse tracing
    res = []
    mxv = max(dp2)
    idx = dp2.index(mxv)
    res.append(idx)
    while True:
        mxv -= V[idx]
        if mxv == 0:
            break
        idx = dp2.index(mxv)
        res.append(idx)

    # print ans
    print(len(res))
    for i in res:
        print(IDX[i] + 1)
