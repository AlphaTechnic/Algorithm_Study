"""
input :
10 2
"""

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

Red, Brown = map(int, input().split())

# Brwon을 2덩어리로 인수분해
two_factors = []
for i in range(1, Brown // 2 + 2):
    if Brown % i == 0:
        two_factors.append((i, Brown // i))

for a, b in two_factors:
    if (a + b) * 2 + 4 == Red:
        print(b + 2, a + 2)
        break
