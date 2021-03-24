import sys
sys.stdin = open("input.txt", "r")

N = int(input())
num_list = [int(input()) for _ in range(N)]

num_list.sort()
for i in num_list:
    print(i)