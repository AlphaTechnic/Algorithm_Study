"""
input :
3
4
7
10

output :
7
44
274
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def dfs(num):
    if dp[num] != 0: return dp[num]

    a = dfs(num - 1)
    b = dfs(num - 2)
    c = dfs(num - 3)
    dp[num] = a + b + c
    return dp[num]


if __name__ == "__main__":
    dp = [0, 1, 2, 4] + [0 for _ in range(8)]
    dfs(11)
    # print(dp)

    T = int(input())
    for _ in range(T):
        N = int(input())
        print(dp[N])
