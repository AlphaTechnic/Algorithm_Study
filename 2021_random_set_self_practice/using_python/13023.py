"""
input :
5 4
0 1
1 2
2 3
3 4

output :
1
"""
import sys
sys.setrecursionlimit(10 ** 7)
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def dfs(cur, cnt):
    global flag
    visited[cur] = True

    if cnt == 5:
        flag = True
        return
    for nxt in graph[cur]:
        if visited[nxt]: continue
        dfs(nxt, cnt + 1)

    visited[cur] = False


if __name__ == "__main__":
    V, E = map(int, input().rstrip().split())
    graph = dict()
    for i in range(V):
        graph[i] = list()

    for _ in range(E):
        a, b = map(int, input().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(V):
        visited = [False for _ in range(V)]
        flag = False
        dfs(i, 1)
        if flag:
            print(1)
            exit(0)
    print(0)
