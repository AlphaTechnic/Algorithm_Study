"""
input :
4 4
2 2 2 1
2 2 1 3
2 1 3 3
1 3 3 3
4 4 4 1
4 4 1 3
4 1 3 3
1 3 3 3

output :
YES
"""
import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def board_copy():
    for r in range(R):
        for c in range(C):
            board_cpy[r][c] = board[r][c]


def board_restore():
    for r in range(R):
        for c in range(C):
            board[r][c] = board_cpy[r][c]


def group_update(frm, to):
    global R; global C;
    visited = [[False for _ in range(C)] for _ in range(R)]
    que = deque()
    cy = frm[0]
    cx = frm[1]
    que.append([cy, cx])
    visited[cy][cx] = True
    board[cy][cx] = to

    while que:
        cy, cx = que.popleft()
        for dy, dx in move:
            ny, nx = cy + dy, cx + dx
            if not (0 <= ny < R and 0 <= nx < C): continue
            if board_cpy[ny][nx] != board_cpy[cy][cx]: continue
            if visited[ny][nx]: continue

            visited[ny][nx] = True
            board[ny][nx] = to
            que.append([ny, nx])


def is_equal():
    for r in range(R):
        for c in range(C):
            if board[r][c] != after_baord[r][c]:
                return False
    return True


if __name__ == "__main__":
    R, C = map(int, input().rstrip().split())
    board = []
    for _ in range(R):
        board.append(list(map(int, input().rstrip().split())))
    board_cpy = [[0 for _ in range(C)] for _ in range(C)]
    board_copy()

    after_baord = []
    for _ in range(R):
        after_baord.append(list(map(int, input().rstrip().split())))

    move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for r in range(R):
        for c in range(C):
            board_restore()
            group_update([r, c], after_baord[r][c])
            if is_equal():
                print("YES")
                exit()
    print("NO")
