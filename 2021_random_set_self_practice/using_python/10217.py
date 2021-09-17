"""
input :
2
3 100 3
1 2 1 1
2 3 1 1
1 3 3 30
4 10 4
1 2 5 3
2 3 5 4
3 4 1 5
1 3 10 6

output :
2
Poor KCM
"""
import sys
from collections import deque

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

MAX = 10 ** 9


def dijkstra():
    global M
    que = deque()
    que.append((1, 0, 0))

    while que:
        cur_nd, cur_c, cur_t = que.popleft()
        if dp[cur_nd][cur_c] < cur_t:  # 이미 업뎃 완료
            continue

        for nxt_nd, nxt_c, nxt_t in graph[cur_nd]:
            new_c = cur_c + nxt_c
            new_t = cur_t + nxt_t
            if new_c > M: continue  # 조건에 안 맞아서 짤
            if dp[nxt_nd][new_c] <= new_t: continue  # 업데할 가치가 없어서 짤

            # 업데이트
            for i in range(new_c, M + 1):
                if dp[nxt_nd][i] > new_t:
                    dp[nxt_nd][i] = new_t
                else:
                    break
            que.append((nxt_nd, new_c, new_t))


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N, M, K = map(int, input().rstrip().split())

        graph = dict()
        for i in range(1, N + 1):
            graph[i] = []

        for _ in range(K):
            a, b, c, t = map(int, input().rstrip().split())
            graph[a].append((b, c, t))

        dp = [[MAX for _ in range(M + 1)] for _ in range(N + 1)]
        dp[1][0] = 0
        dijkstra()

        if dp[N][M] < MAX:
            print(dp[N][M])
        else:
            print("Poor KCM")
