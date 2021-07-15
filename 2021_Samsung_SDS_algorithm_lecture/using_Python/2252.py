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

graph = dict()
que = deque()

if __name__ == "__main__":
    N, M = map(int, input().rstrip().split())

    for i in range(1, N + 1):
        graph[i] = []

    indeg = [0 for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().rstrip().split())
        graph[a].append(b)
        indeg[b] += 1

    for i in range(1, N + 1):
        if indeg[i] == 0:
            que.append(i)
            print(i, end=' ')

    while len(que) != 0:
        deg_zero = que.popleft()
        for i in graph[deg_zero]:
            indeg[i] -= 1
            if indeg[i] == 0:
                que.append(i)
                print(i, end=' ')
