"""
input :
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10
"""

import sys
import bisect
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().rstrip().split()))
num_list.sort()

Q = int(input())
query_list = list(map(int, input().rstrip().split()))
for query in query_list:
    print(bisect.bisect_right(num_list, query) - bisect.bisect_left(num_list, query), end=' ')
