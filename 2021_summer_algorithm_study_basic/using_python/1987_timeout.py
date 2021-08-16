"""
input :
2 4
CAAB
ADCB

output :
3
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def dfs(cy, cx, cnt):
    global max_val
    max_val = max(max_val, cnt)

    for dy, dx in move:
        ny, nx = cy + dy, cx + dx
        if not (0 <= ny < R and 0 <= nx < C): continue
        if visited[ny][nx]: continue
        if chk_path[ord(board[ny][nx])]: continue

        chk_path[ord(board[ny][nx])] = True
        visited[ny][nx] = True
        dfs(ny, nx, cnt + 1)
        chk_path[ord(board[ny][nx])] = False
        visited[ny][nx] = False


if __name__ == "__main__":
    R, C = map(int, input().rstrip().split())
    board = []
    for _ in range(R):
        board.append(list(input().rstrip()))

    max_val = 0
    move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    visited = [[False for _ in range(C)] for _ in range(R)]
    chk_path = [False for _ in range(128)]
    chk_path[ord(board[0][0])] = True
    dfs(0, 0, 0)
    print(max_val + 1)