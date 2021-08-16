"""
input :
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1

output :
8
"""
import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def bfs():
    que = deque()
    for r, c in pivots:
        que.append((r, c))
        visited[r][c] = 1

    max_val = 1
    while que:
        cy, cx = que.popleft()
        for dy, dx in move:
            ny, nx = cy + dy, cx + dx
            if not (0 <= ny < R and 0 <= nx < C): continue
            if visited[ny][nx]: continue
            if board[ny][nx] == -1: continue

            visited[ny][nx] = visited[cy][cx] + 1
            max_val = max(max_val, visited[ny][nx])
            que.append((ny, nx))
    return max_val


def chk_all_covered():
    for r in range(R):
        for c in range(C):
            if not visited[r][c]:
                if board[r][c] != -1:
                    return False
    return True


if __name__ == "__main__":
    C, R = map(int, input().rstrip().split())
    board = list()
    for _ in range(R):
        board.append(list(map(int, input().rstrip().split())))

    pivots = []
    for r in range(R):
        for c in range(C):
            if board[r][c] == 1:
                pivots.append((r, c))

    visited = [[0 for _ in range(C)] for _ in range(R)]
    move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    res = bfs()
    if chk_all_covered():
        print(res - 1)
    else:
        print(-1)