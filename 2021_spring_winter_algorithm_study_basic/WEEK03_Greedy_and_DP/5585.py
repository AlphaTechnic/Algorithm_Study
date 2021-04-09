"""
input :
380

output :
4
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
scales = [500, 100, 50, 10, 5, 1]
change = 1000 - N

cnt = 0
for scale in scales:
    cnt += change // scale
    change = change % scale
    if change == 0:
        break

print(cnt)