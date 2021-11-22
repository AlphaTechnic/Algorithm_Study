"""
input :
5 5
...&.
..###
#.###
.....
....@

output :
8
"""
import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


class BFS(object):
    def __init__(self, board, sy, sx):
        self.board = board
        self.sy = sy
        self.sx = sx
        self.R = len(board)
        self.C = len(board[0])

    def execute(self):
        que = deque()
        vis = [[0 for _ in range(self.C)] for _ in range(self.R)]

        que.append((self.sy, self.sx))
        vis[self.sy][self.sx] = 1
        while que:
            cy, cx = que.popleft()
            for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ny, nx = cy + dy, cx + dx
                if not 0 <= ny < self.R: continue
                if not 0 <= nx < self.C: continue
                if self.board[ny][nx] == '#': continue
                if vis[ny][nx]: continue

                que.append((ny, nx))
                vis[ny][nx] = vis[cy][cx] + 1
                if self.board[ny][nx] == '@':
                    return vis[ny][nx] - 2
        return -1


if __name__ == "__main__":
    R, C = map(int, input().rstrip().split())
    board = [list(input().rstrip()) for _ in range(R)]

    sy, sx = -1, -1
    ey, ex = -1, -1
    for r in range(R):
        for c in range(C):
            if board[r][c] == '&':
                sy, sx = r, c

    print(BFS(board, sy, sx).execute())
