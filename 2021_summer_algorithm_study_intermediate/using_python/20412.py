"""
input :
13 5 2 9

output :
2 5
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def power(a, b):
    global m
    if b == 0: return 1

    if b & 1 == 1: return (power(a, b // 2) ** 2 * a) % m
    else: return (power(a, b // 2) ** 2) % m


if __name__ == "__main__":
    m, seed, X1, X2 = map(int, input().rstrip().split())
    a = (((X1 - X2 + m) % m) * power((seed - X1 + m) % m, m - 2)) % m
    c = ((X1 - (a * seed) % m) + m) % m
    print(a, c)