"""
input :
100 80

output :
6
"""

import sys
import math
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

X, Y = map(int, input().rstrip().split())

cur_val = int((Y*100 / X))
if cur_val >= 99:
    print(-1)
    exit()

tar_val = cur_val + 1

n = (tar_val * X - 100 * Y) / (100 - tar_val)
print(math.ceil(n))
