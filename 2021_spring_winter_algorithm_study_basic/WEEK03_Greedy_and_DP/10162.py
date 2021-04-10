"""
input :
100

ouput :
0 1 4
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

times = [300, 60, 10]
cnts = [0, 0, 0]
N = int(input())

for i in range(3):
    cnts[i] = N // times[i]
    N = N % times[i]

if N == 0:
    print(cnts[0], cnts[1], cnts[2])
else:
    print(-1)