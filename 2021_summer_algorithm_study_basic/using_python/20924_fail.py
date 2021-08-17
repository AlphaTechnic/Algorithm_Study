"""
input :
12 1
1 2 1
2 3 2
3 4 3
4 5 1
5 6 2
6 7 1
5 8 1
4 9 2
4 10 3
10 11 1
10 12 3

output :
6 6
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)


def find_giga(R):
    global V
    cur = R
    cnt = 0
    tot = 0
    visited[cur] = True

    if len(graph[cur]) >= 2:
        return cur, 0

    while True:
        if len(graph[cur]) >= 3:  # 기가노드
            return cur, tot
        if cur != R and len(graph[cur]) == 1:  # 리프노드
            return cur, tot
        if cur == R:
            cnt += 1
            tot += graph[cur][0][1]
            visited[cur] = True
            cur = graph[cur][0][0]
            continue
        if cnt == V - 1:  # 마지막 노드에 도달 -> 기가노드
            return cur, tot

        # 나머지 기둥 노드들 -> 간선 2개 가지고 있음
        for i in range(2):
            if visited[graph[cur][i][0]]: continue
            cnt += 1
            tot += graph[cur][i][1]
            visited[cur] = True
            cur = graph[cur][i][0]

    return cur, tot


def dfs(giga_nd, tot):
    global branch_len; global R;

    visited[giga_nd] = True
    if giga_nd != R and len(graph[giga_nd]) == 1:
        branch_len = max(branch_len, tot)
        return

    for nxt, c in graph[giga_nd]:
        if visited[nxt]: continue

        dfs(nxt, tot + c)


if __name__ == "__main__":
    V, R = map(int, input().rstrip().split())
    graph = dict()
    for i in range(1, V + 1):
        graph[i] = list()

    for _ in range(V - 1):
        a, b, c = map(int, input().rstrip().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    branch_len = 0
    pillar_len = 0
    visited = [False for _ in range(V + 1)]
    giga_nd, pillar_len = find_giga(R)
    visited = [False for _ in range(V + 1)]
    dfs(giga_nd, 0)

    print(pillar_len, branch_len)
