"""
input :
15 15
2 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1 0 1 1 1 1
1 1 1 1 1 1 1 1 1 1 0 1 0 0 0
1 1 1 1 1 1 1 1 1 1 0 1 1 1 1

output:
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
7 8 9 10 11 12 13 14 15 16 17 18 19 20 21
8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
11 12 13 14 15 16 17 18 19 20 0 0 0 0 25
12 13 14 15 16 17 18 19 20 21 0 29 28 27 26
13 14 15 16 17 18 19 20 21 22 0 30 0 0 0
14 15 16 17 18 19 20 21 22 23 0 31 32 33 34
"""
import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def bfs(tar_y, tar_x):
    que = deque()
    que.append([tar_y, tar_x])
    visited[tar_y][tar_x] = 1

    while que:
        cy, cx = que.popleft()
        for dy, dx in move:
            ny, nx = cy + dy, cx + dx
            if not (0 <= ny < R and 0 <= nx < C): continue
            if visited[ny][nx]: continue
            if board[ny][nx] == 0: continue

            visited[ny][nx] = visited[cy][cx] + 1
            que.append([ny, nx])


if __name__ == "__main__":
    R, C = map(int, input().rstrip().split())
    board = []
    for _ in range(R):
        board.append(list(map(int, input().rstrip().split())))

    tar_y = -1
    tar_x = -1
    for r in range(R):
        for c in range(C):
            if board[r][c] == 2:
                tar_y = r
                tar_x = c

    move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    visited = [[0 for _ in range(C)] for _ in range(R)]
    bfs(tar_y, tar_x)

    for r in range(R):
        for c in range(C):
            if board[r][c] == 0:
                visited[r][c] = 1

    for r in range(R):
        for c in range(C):
            print(visited[r][c] - 1, end=' ')
        print()
