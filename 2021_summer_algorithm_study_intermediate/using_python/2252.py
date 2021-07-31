"""
input :
3 2
1 3
2 3

output :
1 2 3
"""
import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().rstrip().split())
    graph = [[] for _ in range(N + 1)]
    indeg = [0 for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().rstrip().split())
        graph[a].append(b)
        indeg[b] += 1

    que = deque()
    for i in range(1, N + 1):
        if indeg[i] == 0:
            que.append(i)

    while len(que) != 0:
        cur = que.popleft()
        print(cur, end=' ')
        for nxt in graph[cur]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                que.append(nxt)
