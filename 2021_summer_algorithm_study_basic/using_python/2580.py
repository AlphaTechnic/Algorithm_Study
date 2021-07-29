"""
input :
0 3 5 4 6 9 2 7 8
7 8 2 1 0 5 6 0 9
0 6 0 2 7 8 1 3 5
3 2 1 0 4 6 8 9 7
8 0 4 9 1 3 5 0 6
5 9 6 8 2 0 4 1 3
9 1 7 6 5 2 0 8 0
6 0 3 7 0 1 9 5 2
2 5 8 3 9 4 7 6 0

output :
1 3 5 4 6 9 2 7 8
7 8 2 1 3 5 6 4 9
4 6 9 2 7 8 1 3 5
3 2 1 5 4 6 8 9 7
8 7 4 9 1 3 5 2 6
5 9 6 8 2 7 4 1 3
9 1 7 6 5 2 3 8 4
6 4 3 7 8 1 9 5 2
2 5 8 3 9 4 7 6 1
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def print_ans():
    for r in range(9):
        for c in range(9):
            print(board[r][c], end=' ')
        print()


def recur(lv):
    if lv == LIMIT:
        print_ans()
        exit()

    for candi in range(1, 10):
        ########################### manipulate
        conti_flag = 0
        y = empty_pos_list[lv][0]
        x = empty_pos_list[lv][1]

        # row
        if candi in board[y]: continue

        # cloumn
        for j in range(9):
            if board[j][x] == candi:
                conti_flag = 1
                break
        if conti_flag == 1:
            continue

        # block
        init_y = y - (y % 3)
        init_x = x - (x % 3)
        for i in range(3):
            for j in range(3):
                if board[init_y + i][init_x + j] == candi:
                    conti_flag = 1
                    break
            if conti_flag == 1:
                break
        if conti_flag == 1:
            continue

        board[y][x] = candi

        ########################### recur
        recur(lv + 1)

        ########################### restore
        board[y][x] = 0


if __name__ == "__main__":
    board = []
    used = [[0 for _ in range(9)] for _ in range(9)]

    for _ in range(9):
        line = list(map(int, input().split()))
        board.append(line)

    empty_pos_list = []
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                empty_pos_list.append([r, c])
    LIMIT = len(empty_pos_list)
    recur(0)


