"""
input :
3

output :
6
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

MOD = 1000000009

if __name__ == "__main__":
    N = int(input())
    if N == 1:
        print(0)
    else:
        print((2 * (3 ** (N - 2)) % MOD) % MOD)
