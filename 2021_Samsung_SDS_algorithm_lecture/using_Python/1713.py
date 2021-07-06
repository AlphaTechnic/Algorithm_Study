"""
input :
3
9
2 1 4 3 5 6 2 7 2

output :
2 6 7
"""

import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


N = int(input())
Q = int(input())
seq = list(map(int, input().split()))

board = deque()
candis_cnt = [0 for _ in range(101)]


def is_full(board):
    return len(board) == N


def get_candi_to_kickout():
    min_val = 10**9
    for candi in board:
        min_val = min(min_val, candis_cnt[candi])

    for ind, candi in enumerate(board):
        if candis_cnt[candi] == min_val:
            return ind, candi


for query in seq:
    if query not in board:
        if is_full(board):
            ind, kicked_candi = get_candi_to_kickout()

            candis_cnt[kicked_candi] = 0
            del board[ind]

            board.append(query)
            candis_cnt[query] += 1
        else:
            board.append(query)
            candis_cnt[query] += 1

    else:  # 이미 board에 올라가 있다.
        candis_cnt[query] += 1

board_list = list(board)
board_list.sort()
for candi in board_list:
    print(candi, end=' ')
