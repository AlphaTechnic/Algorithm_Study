"""
input :
5 0
-7 -3 -2 5 8

output :
1
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def dfs(dep, tot):
    global cnt

    if dep == N:
        if tot == S:
            cnt += 1
        return

    dfs(dep + 1, tot + nums[dep])
    dfs(dep + 1, tot)


if __name__ == "__main__":
    N, S = map(int, input().rstrip().split())
    nums = list(map(int, input().rstrip().split()))

    cnt = 0
    dfs(0, 0)

    # S가 0인 경우는 아무것도 안들어가는 경우도 카운트되어서 그걸 빼줘야함
    if S == 0:
        print(cnt - 1)
    else:
        print(cnt)
