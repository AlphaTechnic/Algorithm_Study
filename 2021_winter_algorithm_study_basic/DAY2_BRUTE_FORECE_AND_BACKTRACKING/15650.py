import sys

sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
ans = [-1 for _ in range(M)]


def combi(level, num):
    if level == M:
        for i in ans:
            print(i, end=' ')
        print('')

    else:
        for i in range(num, N + 1):
            ans[level] = i
            combi(level + 1, i + 1)

combi(0, 1)