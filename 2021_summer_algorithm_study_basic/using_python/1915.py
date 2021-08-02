"""
input :
4 4
0100
0111
1110
0010

output :
4
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    R, C = map(int, input().rstrip().split())
    board = []
    for _ in range(R):
        board.append(list(map(int, list(input().rstrip()))))

    for r in range(1, R):
        for c in range(1, C):
            if board[r][c] == 0: continue
            board[r][c] += min(board[r - 1][c - 1], board[r - 1][c], board[r][c - 1])

    max_val = 0
    for r in range(R):
        for c in range(C):
            max_val = max(max_val, board[r][c])
    print(max_val ** 2)
