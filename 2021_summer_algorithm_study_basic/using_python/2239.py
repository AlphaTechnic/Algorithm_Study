"""
input :
103000509
002109400
000704000
300502006
060000050
700803004
000401000
009205800
804000107

output :
143628579
572139468
986754231
391542786
468917352
725863914
237481695
619275843
854396127
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def row_chk(r, num):
    if num in board[r]:
        return False
    return True


def col_chk(c, num):
    for i in range(9):
        if board[i][c] == num:
            return False
    return True


def block_chk(r, c, num):
    a = r - r % 3
    b = c - c % 3
    for i in range(a, a + 3):
        for j in range(b, b + 3):
            if board[i][j] == num:
                return False
    return True


def print_ans():
    for r in range(9):
        for c in range(9):
            print(board[r][c], end='')
        print()


def dfs(dep):
    if dep == len(blank_poses):
        print_ans()
        exit()

    for candi in range(1, 10):
        y = blank_poses[dep][0]; x = blank_poses[dep][1]
        if not row_chk(y, candi): continue
        if not col_chk(x, candi): continue
        if not block_chk(y, x, candi): continue

        board[y][x] = candi
        dfs(dep + 1)
        board[y][x] = 0


if __name__ == "__main__":
    board = []
    for _ in range(9):
        board.append(list(map(int, input().rstrip())))

    blank_poses = []
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                blank_poses.append([r, c])

    dfs(0)
