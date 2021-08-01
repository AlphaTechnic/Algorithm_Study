"""
input :
3 3
123
456
789

output :
3264
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def split1(R, C):  # 세로로 쪼개기
    if C <= 2: return 0
    max_val = 0
    for i in range(1, C - 1):
        for j in range(i + 1, C):
            s1 = sum([board[a][b] for a in range(R) for b in range(i)])
            s2 = sum([board[a][b] for a in range(R) for b in range(i, j)])
            s3 = sum([board[a][b] for a in range(R) for b in range(j, C)])
            max_val = max(max_val, s1 * s2 * s3)
    return max_val


def split2(R, C):  # 가로로 쪼개기
    if R <= 2: return 0
    max_val = 0
    for i in range(1, R - 1):
        for j in range(i + 1, R):
            s1 = sum([board[a][b] for a in range(i) for b in range(C)])
            s2 = sum([board[a][b] for a in range(i, j) for b in range(C)])
            s3 = sum([board[a][b] for a in range(j, R) for b in range(C)])
            max_val = max(max_val, s1 * s2 * s3)
    return max_val


def split3(R, C):  # 위 2, 아래 1
    if R <= 1: return 0
    if C <= 1: return 0
    max_val = 0
    for i in range(1, C):
        for j in range(1, R):
            s1 = sum([board[a][b] for a in range(j) for b in range(i)])
            s2 = sum([board[a][b] for a in range(j) for b in range(i, C)])
            s3 = sum([board[a][b] for a in range(j, R) for b in range(C)])
            max_val = max(max_val, s1 * s2 * s3)
    return max_val


def split4(R, C):  # 위 1, 아래 2
    if R <= 1: return 0
    if C <= 1: return 0
    max_val = 0
    for i in range(1, R):
        for j in range(1, C):
            s1 = sum([board[a][b] for a in range(i) for b in range(C)])
            s2 = sum([board[a][b] for a in range(i, R) for b in range(j)])
            s3 = sum([board[a][b] for a in range(i, R) for b in range(j, C)])
            max_val = max(max_val, s1 * s2 * s3)
    return max_val


def split5(R, C):  # 왼 2, 오 1
    if R <= 1: return 0
    if C <= 1: return 0
    max_val = 0
    for i in range(1, R):
        for j in range(1, C):
            s1 = sum([board[a][b] for a in range(i) for b in range(j)])
            s2 = sum([board[a][b] for a in range(i, R) for b in range(j)])
            s3 = sum([board[a][b] for a in range(R) for b in range(j, C)])
            max_val = max(max_val, s1 * s2 * s3)
    return max_val


def split6(R, C):  # 왼 1, 오 2
    if R <= 1: return 0
    if C <= 1: return 0
    max_val = 0
    for i in range(1, R):
        for j in range(1, C):
            s1 = sum([board[a][b] for a in range(i) for b in range(j, C)])
            s2 = sum([board[a][b] for a in range(i, R) for b in range(j, C)])
            s3 = sum([board[a][b] for a in range(R) for b in range(j)])
            max_val = max(max_val, s1 * s2 * s3)
    return max_val


if __name__ == "__main__":
    N, M = map(int, input().rstrip().split())
    board = []
    for _ in range(N):
        board.append(list(map(int, list(input().rstrip()))))
    # print(board)

    funs = [split1, split2, split3, split4, split5, split6]
    max_val = 0
    for fun in funs:
        max_val = max(fun(N, M), max_val)
    print(max_val)
