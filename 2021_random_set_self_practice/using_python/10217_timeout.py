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
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

g_min_val = 10 ** 9
g_M = -1


def dfs(cur, E, c, t):
    global g_M, g_min_val
    vis[cur] = True
    if c > M:
        vis[cur] = False
        return
    if cur == E:
        g_min_val = min(g_min_val, t)
        vis[cur] = False
        return

    for nxt in graph[cur]:
        if vis[nxt]: continue
        dfs(nxt, E, c + cost[(cur, nxt)], t + time[(cur, nxt)])

    vis[cur] = False


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N, M, K = map(int, input().rstrip().split())
        g_M = M
        g_min_val = 10 ** 9

        time = dict()
        cost = dict()
        graph = dict()
        for i in range(1, N + 1):
            graph[i] = []

        for _ in range(K):
            a, b, c, t = map(int, input().rstrip().split())
            graph[a].append(b)
            graph[b].append(a)
            cost[(a, b)] = cost[(b, a)] = c
            time[(a, b)] = time[(b, a)] = t

        S = 1
        E = N
        vis = [False for _ in range(N + 1)]
        dfs(S, E, 0, 0)

        if g_min_val != 10 ** 9:
            print(g_min_val)
        else:
            print("Poor KCM")
