"""
input :
4

output :
5
"""
import sys

sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
MOD = 15746


def recur(length):
    global cnt, N
    if length == N:
        cnt = (cnt + 1) % MOD
        return
    if length > N:
        return

    recur(length + 1)
    recur(length + 2)


if __name__ == "__main__":
    N = int(input())

    cnt = 0
    recur(0)
    print(cnt % MOD)
