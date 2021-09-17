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
from collections import defaultdict

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

MAX = 10 ** 9


def bfs():
    global M
    que = deque()
    que.append((1, 0, 0))

    while que:
        cur_nd, cur_c, cur_t = que.popleft()
        if dp[(cur_nd, cur_c)] < cur_t:
            continue

        for nxt_nd, nxt_c, nxt_t in graph[cur_nd]:
            new_c = cur_c + nxt_c
            new_t = cur_t + nxt_t
            if new_c > M: continue
            if dp[(nxt_nd, new_c)] <= new_t: continue

            for i in range(new_c, M + 1):
                if dp[(nxt_nd, i)] > new_t:
                    dp[(nxt_nd, i)] = new_t
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

        dp = defaultdict(lambda: MAX)
        dp[(1, 0)] = 0
        bfs()

        if dp[(N, M)] < MAX:
            print(dp[(N, M)])
        else:
            print("Poor KCM")
