"""
input :
10

output :
55
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())

memo = dict()
def fibo(lv):
    if lv in memo: return memo[lv]
    if lv == 0: return 0
    if lv == 1: return 1

    memo[lv] = fibo(lv - 1) + fibo(lv - 2)
    return memo[lv]


print(fibo(N))