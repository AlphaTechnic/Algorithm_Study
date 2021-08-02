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


def square_possible(r, c, sz):
    for i in range(r, r + sz):
        for j in range(c, c + sz):
            if board[i][j] == 0:
                return -1
    return sz


def square_chk(sz):
    r_loop = R - sz + 1
    c_loop = C - sz + 1
    for r in range(r_loop):
        for c in range(c_loop):
            val = square_possible(r, c, sz)
            if val != -1:
                return sz
    return -1


if __name__ == "__main__":
    R, C = map(int, input().rstrip().split())
    board = []
    for _ in range(R):
        board.append(list(map(int, list(input().rstrip()))))

    max_val = 0
    for sz in range(min(R, C), 0, -1):
        a = square_chk(sz)
        if a > max_val:
            max_val = a
            break
    print(max_val ** 2)
