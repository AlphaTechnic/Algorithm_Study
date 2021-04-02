"""
input :
2 4 7

O(n)으로 모든 board를 탐색하는 방법은 시간초과
"""

import sys

sys.setrecursionlimit(10 ** 8)
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, R, C = map(int, input().split())
board = [[0 for _ in range(2 ** N)] for _ in range(2 ** N)]

cnt = 0


def divide_and_conquer(start_r, start_c, size):
    global cnt
    if size == 2:
        for r in range(start_r, start_r + size):
            for c in range(start_c, start_c + size):
                board[r][c] = cnt
                cnt += 1
        return

    for r in range(start_r, start_r + size, size // 2):
        for c in range(start_c, start_c + size, size // 2):
            divide_and_conquer(r, c, size // 2)


divide_and_conquer(0, 0, 2 ** N)
# for r in range(2 ** N):
#     for c in range(2 ** N):
#         print(board[r][c], end=' ')
#     print()
print(board[R][C])

print("시간 초과의 이유 : O(n) -> (2 ** 15) ** 2 =", (2 ** 15) ** 2)
