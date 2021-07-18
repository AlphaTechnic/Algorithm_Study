"""
input :
8
1 2
1 3
1 4
2 5
2 6
4 7
4 8

output :
3
"""

import sys
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline


def gen_dp(root):
    visited[root] = True
    dp[root][0] = 0  # 부모가 얼리어답터가 아님
    dp[root][1] = 1  # 부모가 얼리어답터

    for child in graph[root]:
        if visited[child]: continue  # 부모는 방문하지 않게 됨

        gen_dp(child)
        dp[root][0] += dp[child][1]  # 부모가 얼리어답터가 아니면, 자식들은 무조건 얼리어답터
        dp[root][1] += min(dp[child][0], dp[child][1])  # 부모가 얼리어답터이면, 자식들은 얼리어답터일 수도 있고, 아닐 수도 있음


if __name__ == "__main__":
    N = int(input())
    graph = dict()
    for i in range(N + 1):
        graph[i] = []

    for _ in range(N - 1):
        a, b = map(int, input().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False for _ in range(N + 1)]

    # dp[x][c] = node x를 루트로 하고, 얼리어답터 유무를 c(0 또는 1)로 할 때, 최소 얼리어답터의 개수
    dp = [[0 for _ in range(2)] for _ in range(N + 1)]

    gen_dp(1)
    print(min(dp[1][0], dp[1][1]))
