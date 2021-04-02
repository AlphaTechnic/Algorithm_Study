"""
input :
2 4 7

O(logn)으로 탐색해야 시간초과가 나지 않는다.
"""

import sys

sys.setrecursionlimit(10 ** 8)
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, R, C = map(int, input().split())

ind = 0


def divide_and_conquer(start_r, start_c, size):
    global ind
    if size == 2:
        if R == start_r and C == start_c:
            pass
        elif R == start_r and C == start_c + 1:
            ind += 1
        elif R == start_r + 1 and C == start_c:
            ind += 2
        elif R == start_r + 1 and C == start_c + 1:
            ind += 3
        return

    half_r_pos = start_r + size // 2
    end_r_pos = start_r + size
    half_c_pos = start_c + size // 2
    end_c_pos = start_c + size
    if start_r <= R < half_r_pos and start_c <= C < half_c_pos:
        divide_and_conquer(start_r, start_c, size // 2)
    elif start_r <= R < half_r_pos and half_c_pos <= C < end_c_pos:
        ind += 1 * (size // 2) ** 2
        divide_and_conquer(start_r, half_c_pos, size // 2)
    elif half_r_pos <= R < end_r_pos and start_c <= C < half_c_pos:
        ind += 2 * (size // 2) ** 2
        divide_and_conquer(half_r_pos, start_c, size // 2)
    elif half_r_pos <= R < end_r_pos and half_c_pos <= C < end_c_pos:
        ind += 3 * (size // 2) ** 2
        divide_and_conquer(half_r_pos, half_c_pos, size // 2)


divide_and_conquer(0, 0, 2 ** N)
print(ind)
