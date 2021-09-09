"""
input :
17 8
2
2 16

output :
6 2
"""
import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def A_to_dec(A, digits):
    scale = 0
    tot = 0
    for i in range(len(digits) - 1, -1, -1):
        tot += digits[i] * A ** scale
        scale += 1
    return tot


def dec_to_B(num_dec):
    res = deque()
    while True:
        res.appendleft(num_dec % B)
        num_dec = num_dec // B
        if num_dec == 0:
            break
    return res


if __name__ == "__main__":
    A, B = map(int, input().rstrip().split())
    N = int(input())
    digits = list(map(int, input().rstrip().split()))

    num_dec = A_to_dec(A, digits)
    ans = dec_to_B(num_dec)

    # print ans
    for num in ans:
        print(num, end=' ')
