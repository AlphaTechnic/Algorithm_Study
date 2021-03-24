import sys

sys.stdin = open("input.txt", "r")

N = int(input())

column_used = [False for _ in range(N)]
right_diagonal_used = [False for _ in range(2 * N - 1)]
left_diagonal_used = [False for _ in range(2 * N - 1)]
cnt = 0


def solve(level):
    if level == N:
        global cnt
        cnt += 1
        return
    for i in range(N):
        if column_used[i] or right_diagonal_used[i + level] or left_diagonal_used[N - 1 + i - level]:
            continue
        column_used[i] = True
        right_diagonal_used[i + level] = True
        left_diagonal_used[N - 1 + i - level] = True
        solve(level + 1)
        column_used[i] = False
        right_diagonal_used[i + level] = False
        left_diagonal_used[N - 1 + i - level] = False


solve(0)
print(cnt)
