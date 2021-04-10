"""
input :
10

ouput :
55
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
if N == 0:
    print(0)
    exit()

fibos = [-1 for _ in range(N+1)]
fibos[0] = 0
fibos[1] = 1
for i in range(2, N+1):
    fibos[i] = fibos[i-2] + fibos[i-1]

print(fibos[N])