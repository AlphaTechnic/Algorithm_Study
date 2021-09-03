"""
input :
4

output :
5
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
MOD = 15746

if __name__ == "__main__":
    N = int(input())

    a = 1
    b = 2
    if N == 1:
        print(1)
        exit(0)
    if N == 2:
        print(2)
        exit(0)

    while N - 2:
        c = (a + b) % MOD
        b, a = c, b
        N -= 1

    print(c)
