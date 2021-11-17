"""
input :
19 29

ouput :
2
"""
import sys
import math
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def min_divisor(N):
    if N % 2 == 0:
        return 2
    for i in range(3, int(math.sqrt(N)) + 1, 2):
        if N % i == 0:
            return i
    return N


if __name__ == "__main__":
    a, b = map(int, input().rstrip().split())
    if a != b:
        print(2)
        exit(0)

    if a == b:
        if a % 2 == 0:
            print(2)
        else:
            print(min_divisor(a))
