import sys

sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
ans = [-1 for _ in range(M)]
is_used = [False for _ in range(N + 1)]  # False로 초기화


def permu(level):
    if level == M:
        for i in ans:
            print(i, end=' ')
        print('')
        return
    for i in range(1, N + 1):
        if is_used[i]:
            continue
        is_used[i] = True
        ans[level] = i
        permu(level + 1)
        is_used[i] = False

permu(0)
