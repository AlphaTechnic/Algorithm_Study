"""
input :
3
8
0 0
7 0
100
0 0
30 50
10
1 1
1 1

output :
5
28
0
"""
import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def bfs(sy, sx, ey, ex):
    global N
    que = deque()
    que.append((sy, sx))
    visited[sy][sx] = 1

    while que:
        cy, cx = que.popleft()
        for dy, dx in move:
            ny, nx = cy + dy, cx + dx
            if not (0 <= ny < N and 0 <= nx < N): continue
            if visited[ny][nx]: continue

            visited[ny][nx] = visited[cy][cx] + 1
            que.append((ny, nx))

            if (ny, nx) == (ey, ex):
                return visited[ny][nx]
    return -1


if __name__ == "__main__":
    T = int(input())
    move = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
    for _ in range(T):
        N = int(input())
        sy, sx = map(int, input().rstrip().split())
        ey, ex = map(int, input().rstrip().split())
        if (sy, sx) == (ey, ex):
            print(0)
            continue

        visited = [[0 for _ in range(N)] for _ in range(N)]
        print(bfs(sy, sx, ey, ex) - 1)
