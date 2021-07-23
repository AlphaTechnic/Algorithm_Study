"""
input :
4 2
IVA
IVO
ANA
TOM

output :
5
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

chk_board = [0 for _ in range(21)]


def initial_chk():
    global ans
    for i in range(K + 1):
        ans += chk_board[Query[i]]
        chk_board[Query[i]] += 1


def slide_chk():
    global ans
    for i in range(N - K - 1):
        chk_board[Query[i]] -= 1
        ans += chk_board[Query[i + K + 1]]
        chk_board[Query[i + K + 1]] += 1


if  __name__ == "__main__":
    N, K = map(int, input().rstrip().split())
    Query = list()
    for _ in range(N):
        Query.append(len(input().rstrip()))

    ans = 0
    initial_chk()
    slide_chk()
    print(ans)
