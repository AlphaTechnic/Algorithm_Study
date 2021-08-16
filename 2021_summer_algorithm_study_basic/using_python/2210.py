"""
input :
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 2 1
1 1 1 1 1

output :
15
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def dfs(cy, cx, cnt):
    global num_str
    if cnt == 5:
        num_set.add(num_str)
        return

    for dy, dx in move:
        ny, nx = cy + dy, cx + dx
        if not (0 <= ny < 5 and 0 <= nx < 5): continue

        num_str += board[ny][nx]
        dfs(ny, nx, cnt + 1)
        num_str = num_str[:-1]


if __name__ == "__main__":
    board = []
    for _ in range(5):
        board.append(list(input().rstrip().split()))

    num_set = set()
    move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for r in range(5):
        for c in range(5):
            num_str = ""
            num_str += board[r][c]
            dfs(r, c, 0)

    print(len(num_set))
