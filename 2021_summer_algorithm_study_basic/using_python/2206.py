"""
input :
6 4
0100
1110
1000
0000
0111
0000

output :
15
"""
import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def bfs():
    global R; global C;
    que = deque()
    que.append((0, 0, 0))
    visited[0][0][0] = 1

    while que:
        cy, cx, is_break = que.popleft()

        for dy, dx in move:
            ny, nx = cy + dy, cx + dx
            if not (0 <= ny < R and 0 <= nx < C): continue
            if visited[ny][nx][is_break]: continue

            if board[ny][nx] == '0':
                visited[ny][nx][is_break] = visited[cy][cx][is_break] + 1
                que.append((ny, nx, is_break))
            elif board[ny][nx] == '1' and is_break == 0:  # '1'에 들어오려면 뿌수면서(break을 하면서) 들어와야됨
                visited[ny][nx][1] = visited[cy][cx][0] + 1
                que.append((ny, nx, 1))

            if (ny, nx) == (R - 1, C - 1):
                return visited[ny][nx][is_break]
    return -1


if __name__ == "__main__":
    R, C = map(int, input().rstrip().split())

    board = []
    for _ in range(R):
        board.append(list(input().rstrip()))
    if (R, C) == (1, 1):
        if board[0][0] == '1': print(-1)
        else: print(1)
        exit()

    visited = [[[0 for _ in range(2)] for _ in range(C)] for _ in range(R)]
    move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    print(bfs())
