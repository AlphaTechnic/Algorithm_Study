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
    for i in range(0, len(num_str)-2):
        if num_str[i] == '6' and num_str[i+1] == '6' and num_str[i+2] == '6':
            cnt += 1
            if cnt == N:
                print(num)
                flag = 1
                break
            break
    if flag == 1:
            break

