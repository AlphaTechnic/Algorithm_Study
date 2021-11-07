"""
input :
4

output :
9
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())

    i = 0
    tot = 0
    while N != 0:
        if N & 1:
            tot += (3 ** i)
        i += 1
        N >>= 1
    print(tot)
