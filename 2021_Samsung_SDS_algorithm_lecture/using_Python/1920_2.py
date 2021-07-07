"""
input :
5
4 1 5 2 3
5
1 3 7 9 5

output :
1
1
0
0
1
"""

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


N = int(input())
data = list(map(int, input().split()))
data_dic = dict()

for i in data:
    data_dic[i] = 1

Q = int(input())
query = list(map(int, input().split()))

for q in query:
    if q in data_dic:
        print(1)
    else:
        print(0)
