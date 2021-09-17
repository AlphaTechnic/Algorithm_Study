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
from collections import defaultdict
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

MAX = 10 ** 9
g_M = -1
g_E = -1


def recur(cur, c):
    global g_M, g_E
    if c > M:
        return MAX
    if cur == g_E:
        return 0
    if dp[(cur, c)] != MAX:
        return dp[(cur, c)]

    ret = MAX
    for nxt in graph[cur]:
        ret = min(ret, recur(nxt, c + cost[(cur, nxt)]) + time[(cur, nxt)])
    dp[(cur, c)] = ret
    return dp[(cur, c)]


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N, M, K = map(int, input().rstrip().split())
        g_M = M
        g_E = N

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

        dp = defaultdict(lambda: MAX)
        ans = recur(1, 0)
        if ans >= MAX or ans == -1:
            print("Poor KCM")
        else:
            print(ans)
