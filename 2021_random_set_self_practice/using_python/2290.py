"""
input :
2 1234567890

output :
      --   --        --   --   --   --   --   --
   |    |    | |  | |    |       | |  | |  | |  |
   |    |    | |  | |    |       | |  | |  | |  |
      --   --   --   --   --        --   --
   | |       |    |    | |  |    | |  |    | |  |
   | |       |    |    | |  |    | |  |    | |  |
      --   --        --   --        --   --   --
"""
import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline


def hori1(s, sz):
    for c in range(s + 2, s + sz + 2):
        board[0][c] = '-'


def hori2(s, sz):
    for c in range(s + 2, s + sz + 2):
        board[sz + 1][c] = '-'


def hori3(s, sz):
    for c in range(s + 2, s + sz + 2):
        board[2 * sz + 2][c] = '-'


def vert1(s, sz):
    for r in range(1, sz + 1):
        board[r][s + 1] = '|'


def vert2(s, sz):
    for r in range(1, sz + 1):
        board[r][s + sz + 2] = '|'


def vert3(s, sz):
    for r in range(sz + 2, 2 * sz + 2):
        board[r][s + 1] = '|'


def vert4(s, sz):
    for r in range(sz + 2, 2 * sz + 2):
        board[r][s + sz + 2] = '|'


def draw0(s, sz):
    hori1(s, sz)
    hori3(s, sz)
    vert1(s, sz)
    vert2(s, sz)
    vert3(s, sz)
    vert4(s, sz)


def draw1(s, sz):
    vert2(s, sz)
    vert4(s, sz)


def draw2(s, sz):
    hori1(s, sz)
    hori2(s, sz)
    hori3(s, sz)
    vert2(s, sz)
    vert3(s, sz)


def draw3(s, sz):
    hori1(s, sz)
    hori2(s, sz)
    hori3(s, sz)
    vert2(s, sz)
    vert4(s, sz)


def draw4(s, sz):
    hori2(s, sz)
    vert1(s, sz)
    vert2(s, sz)
    vert4(s, sz)


def draw5(s, sz):
    hori1(s, sz)
    hori2(s, sz)
    hori3(s, sz)
    vert1(s, sz)
    vert4(s, sz)


def draw6(s, sz):
    hori1(s, sz)
    hori2(s, sz)
    hori3(s, sz)
    vert1(s, sz)
    vert3(s, sz)
    vert4(s, sz)


def draw7(s, sz):
    hori1(s, sz)
    vert2(s, sz)
    vert4(s, sz)


def draw8(s, sz):
    hori1(s, sz)
    hori2(s, sz)
    hori3(s, sz)
    vert1(s, sz)
    vert2(s, sz)
    vert3(s, sz)
    vert4(s, sz)


def draw9(s, sz):
    hori1(s, sz)
    hori2(s, sz)
    hori3(s, sz)
    vert1(s, sz)
    vert2(s, sz)
    vert4(s, sz)


def make_digit(s, sz, digit):
    fun = num2fun[digit]
    fun(s, sz)


if __name__ == "__main__":
    num2fun = {
        '0': draw0, '1': draw1, '2': draw2, '3': draw3, '4': draw4,
        '5': draw5, '6': draw6, '7': draw7, '8': draw8, '9': draw9
    }
    S, str_nums = input().rstrip().split()
    S = int(S)
    l = len(str_nums)

    board = [[' ' for _ in range((S + 3) * l)] for _ in range(2 * S + 3)]
    for i, digit in enumerate(str_nums):
        make_digit(i * (S + 3), S, digit)

    for r in range(2 * S + 3):
        for c in range(1, (S + 3) * l):
            print(board[r][c], end='')
        print()
