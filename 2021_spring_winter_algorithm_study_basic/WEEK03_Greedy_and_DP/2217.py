"""
input :
2
10
15

ouput :
20
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
ropes = []
for _ in range(N):
    ropes.append(int(input()))
ropes.sort(reverse=True)

candi = []
for n in range(N):
    candi.append(ropes[n]*(n+1))
print(max(candi))