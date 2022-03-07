import sys
from collections import defaultdict
from collections import deque

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


def get_input():
    R, C = map(int, input().rstrip().split())
    board = []
    tar_board = []
    constraint = []
    for _ in range(R):
        line = input().rstrip()
        board.append(list(map(int, line)))
    for _ in range(R):
        line = input().rstrip()
        tar_board.append(list(map(int, line)))
    for _ in range(R):
        line = list(input().rstrip())
        constraint.append(list(map(int, line)))
    return R, C, board, tar_board, constraint


def list2tup(board_list):
    ret = []
    for line in board_list:
        ret.append(''.join(map(str, line)))
    return tuple(ret)


def tup2list(board_tup):
    ret = []
    for r in range(len(board_tup)):
        tmp = []
        for c in range(len(board_tup[0])):
            tmp.append(int(board_tup[r][c]))
        ret.append(tmp)
    return ret


def eq(arr1, arr2):
    num1 = 0
    num2 = 0
    for r in range(len(arr1)):
        for c in range(len(arr1[0])):
            if arr1[r][c] == 1:
                num1 += 1
            if arr2[r][c] == 1:
                num2 += 1
    return num1 == num2


def row_swap(board, constraint):
    ret = []
    board = tup2list(board)
    constraint = tup2list(constraint)

    R = len(board)
    C = len(board[0])
    for r in range(R):
        for c in range(C - 1):
            if constraint[r][c] == 0 or constraint[r][c + 1] == 0:
                continue
            board[r][c], board[r][c + 1] = board[r][c + 1], board[r][c]
            constraint[r][c] -= 1
            constraint[r][c + 1] -= 1
            ret.append((list2tup(board), list2tup(constraint)))
            board[r][c], board[r][c + 1] = board[r][c + 1], board[r][c]
            constraint[r][c] += 1
            constraint[r][c + 1] += 1
    return tuple(ret)


def col_swap(board, constraint):
    ret = []
    board = tup2list(board)
    constraint = tup2list(constraint)

    R = len(board)
    C = len(board[0])
    for r in range(R - 1):
        for c in range(C):
            if constraint[r][c] == 0 or constraint[r + 1][c] == 0:
                continue
            board[r][c], board[r + 1][c] = board[r + 1][c], board[r][c]
            constraint[r][c] -= 1
            constraint[r + 1][c] -= 1
            ret.append((list2tup(board), list2tup(constraint)))
            board[r][c], board[r + 1][c] = board[r + 1][c], board[r][c]
            constraint[r][c] += 1
            constraint[r + 1][c] += 1
    return tuple(ret)


def right_diag_swap(board, constraint):
    ret = []
    board = tup2list(board)
    constraint = tup2list(constraint)

    R = len(board)
    C = len(board[0])
    for r in range(0, R - 1):
        for c in range(1, C):
            if constraint[r][c] == 0 or constraint[r + 1][c - 1] == 0:
                continue
            board[r][c], board[r + 1][c - 1] = board[r + 1][c - 1], board[r][c]
            constraint[r][c] -= 1
            constraint[r + 1][c - 1] -= 1
            ret.append((list2tup(board), list2tup(constraint)))
            board[r][c], board[r + 1][c - 1] = board[r + 1][c - 1], board[r][c]
            constraint[r][c] += 1
            constraint[r + 1][c - 1] += 1
    return tuple(ret)


def left_diag_swap(board, constraint):
    ret = []
    board = tup2list(board)
    constraint = tup2list(constraint)

    R = len(board)
    C = len(board[0])
    for r in range(0, R - 1):
        for c in range(0, C - 1):
            if constraint[r][c] == 0 or constraint[r + 1][c + 1] == 0:
                continue
            board[r][c], board[r + 1][c + 1] = board[r + 1][c + 1], board[r][c]
            constraint[r][c] -= 1
            constraint[r + 1][c + 1] -= 1
            ret.append((list2tup(board), list2tup(constraint)))
            board[r][c], board[r + 1][c + 1] = board[r + 1][c + 1], board[r][c]
            constraint[r][c] += 1
            constraint[r + 1][c + 1] += 1
    return tuple(ret)


def bfs(init_board, tar_board, init_constraint):
    tar_board = list2tup(tar_board)
    visited = defaultdict(int)
    que = deque()
    visited[(list2tup(init_board), list2tup(init_constraint))] = 1
    que.append((list2tup(init_board), list2tup(init_constraint)))

    while que:
        cur_board, cur_constraint = que.popleft()
        if cur_board == tar_board:
            return visited[(cur_board, cur_constraint)] - 1

        for nxt_board, nxt_constraint in row_swap(cur_board, cur_constraint):
            if not visited[(nxt_board, nxt_constraint)]:
                visited[(nxt_board, nxt_constraint)] = visited[(cur_board, cur_constraint)] + 1
                que.append((nxt_board, nxt_constraint))
        for nxt_board, nxt_constraint in col_swap(cur_board, cur_constraint):
            if not visited[(nxt_board, nxt_constraint)]:
                visited[(nxt_board, nxt_constraint)] = visited[(cur_board, cur_constraint)] + 1
                que.append((nxt_board, nxt_constraint))
        for nxt_board, nxt_constraint in right_diag_swap(cur_board, cur_constraint):
            if not visited[(nxt_board, nxt_constraint)]:
                visited[(nxt_board, nxt_constraint)] = visited[(cur_board, cur_constraint)] + 1
                que.append((nxt_board, nxt_constraint))
        for nxt_board, nxt_constraint in left_diag_swap(cur_board, cur_constraint):
            if not visited[(nxt_board, nxt_constraint)]:
                visited[(nxt_board, nxt_constraint)] = visited[(cur_board, cur_constraint)] + 1
                que.append((nxt_board, nxt_constraint))
    return -1


if __name__ == "__main__":
    R, C, board, tar_board, constraint = get_input()
    # 1의 개수부터 다르면 절대 목표에 도달 못함
    if not eq(board, tar_board):
        print(-1)
        exit(0)
    print(bfs(board, tar_board, constraint))
