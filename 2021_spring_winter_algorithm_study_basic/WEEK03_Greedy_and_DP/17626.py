"""
input :
11339

output :
3
"""

import sys
import math

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
R = int(math.sqrt(N))

escape_flag = 0
ans = []
for i in range(R + 1):
    for j in range(R + 1):
        for k in range(R + 1):
            for l in range(R + 1):
                if N == i ** 2 + j ** 2 + k ** 2 + l ** 2:
                    ans.append(i)
                    ans.append(j)
                    ans.append(k)
                    ans.append(l)
                    escape_flag = 1
                    break
            if escape_flag == 1:
                break
        if escape_flag == 1:
            break
    if escape_flag == 1:
        break

cnt = 0
for i in ans:
    if i != 0:
        cnt += 1

print(cnt)
