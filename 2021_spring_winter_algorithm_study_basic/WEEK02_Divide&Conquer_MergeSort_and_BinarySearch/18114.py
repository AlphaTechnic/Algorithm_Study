"""
input :
5 5
1 2 3 4 5
"""

import sys
import bisect
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


N, M = map(int, input().rstrip().split())
num_dic = dict()
for num in map(int, input().split()):
    num_dic[num] = True

# 1개 조합
if M in num_dic:
    print(1)
    exit()

# 2개 조합
for num in num_dic:
    if M > num:
        target = M - num
        if target in num_dic and num != target:
            print(1)
            exit()


# 3개 조합
num_dic_keys = list(num_dic.keys())
for i in range(N):
    for j in range(i+1, N):
        if M > num_dic_keys[i] + num_dic_keys[j]:
            target = M - (num_dic_keys[i] + num_dic_keys[j])
            if target in num_dic and num_dic_keys[i] != target and num_dic_keys[j] != target:
                print("!!!!!")
                print(1)
                exit()

print(0)
