import sys
sys.stdin = open("input.txt", "r")

N = int(input())
num_list = list(map(int, input().split()))
M = int(input())
target_list = list(map(int, input().split()))

num_list.sort()
for target in target_list:
    if target in num_list:
        print(1)
    else:
        print(0)
