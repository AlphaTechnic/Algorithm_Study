"""
input:
2

output:
1666
"""

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
cnt = 0
flag = 0
for num in range(666, 10 ** 18):
    num_str = str(num)
    if '666' in num_str:
        cnt += 1
        if cnt == N:
            print(num)
            flag = 1
            break
