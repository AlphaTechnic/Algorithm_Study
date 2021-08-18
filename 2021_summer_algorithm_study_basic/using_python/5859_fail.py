"""
input :
4 4
1 4 L
2 3 T
4 1 L
3 1 L

output :
4
"""
import pprint
import sys
sys.setrecursionlimit(10 ** 7)
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
pp = pprint.PrettyPrinter()


def dfs(p, mp, val):
    global success_flag
    visited[p] = val
    for nxt, c in graph[p]:
        if nxt == mp: continue

        if c == 'T':
            if visited[nxt] == -1:  # 첫 방문
                dfs(nxt, p, visited[p])
            elif visited[nxt] == 0 or visited[nxt] == 1:
                if visited[p] != visited[nxt]:  # 간선이 T면 노드 값이 같아야 함
                    success_flag = False
                    return
                else:
                    return

        elif c == 'L':
            if visited[nxt] == -1:  # 첫 방문
                if visited[p] == 0:
                    dfs(nxt, p, 1)
                elif visited[p] == 1:
                    dfs(nxt, p, 0)
            elif visited[nxt] == 0:  # 간선이 L이면 노드 값이 달라야 함
                if visited[p] != 1:
                    success_flag = False
                    return
                else:
                    return
            elif visited[nxt] == 1:
                if visited[p] != 0:
                    success_flag = False
                    return
                else:
                    return


if __name__ == "__main__":
    V, M = map(int, input().rstrip().split())
    graph = dict()
    for i in range(1, V + 1):
        graph[i] = list()

    cnt = 0
    chk = [[-1 for _ in range(V + 1)] for _ in range(V + 1)]
    for _ in range(M):
        a, b, c = input().rstrip().split()
        a, b = map(int, (a, b))

        if chk[a][b] == -1:
            chk[a][b] = chk[b][a] = c
        else:
            if chk[a][b] != c:
                break
            else:
                cnt += 1
                continue

        graph[a].append([b, c])
        graph[b].append([a, c])

        visited = [-1 for _ in range(V + 1)]
        success_flag = True
        dfs(a, -1, 0)

        if success_flag:
            cnt += 1
        else:
            break

    print(cnt)
