"""
input :
7 2 3

output :
7
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def recur(num):
    global P; global Q
    if num == 0:
        return 1
    if num in dp:
        return dp[num]

    a = recur(num // P)
    b = recur(num // Q)
    dp[num] = a + b
    return dp[num]


if __name__ == "__main__":
    N, P, Q = map(int, input().rstrip().split())

    dp = dict()
    print(recur(N))
