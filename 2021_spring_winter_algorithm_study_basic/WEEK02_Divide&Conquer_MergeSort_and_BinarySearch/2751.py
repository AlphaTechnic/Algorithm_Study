"""
5
5
4
3
2
1
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
num_list = []
for _ in range(N):
    num_list.append(int(input()))

num_list.sort()
for num in num_list:
    print(num)