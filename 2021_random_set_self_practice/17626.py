"""
input :
26

output :
2
"""
import sys
from itertools import combinations_with_replacement
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def solution1(N):
    if N in square_num:
        return True
    return False


def solution2(N):
    combis = combinations_with_replacement(square_num, 2)
    for a, b in combis:
        if a + b == N:
            return True
    return False


def solution3(N):
    combis = combinations_with_replacement(square_num, 3)
    for a, b, c in combis:
        if a + b + c == N:
            return True
    return False


if __name__ == "__main__":
    # 제곱수 전처리
    square_num = set()
    i = 1
    while i * i <= 50000:
        square_num.add(i * i)
        i += 1

    N = int(input())
    if solution1(N):
        print(1)
    elif solution2(N):
        print(2)
    elif solution3(N):
        print(3)
    else:
        print(4)
