"""
5
4 1 5 2 3
5
1 3 7 9 5
"""

import sys
import bisect
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def search_num_by_bisect(target_num):
    global N
    ind = bisect.bisect_left(num_list, target_num)
    if ind == N: return False
    if num_list[ind] != target_num: return False
    return True


N = int(input())
num_list = list(map(int, input().rstrip().split()))
num_list.sort()

Q = int(input())
query_list = list(map(int, input().rstrip().split()))

for query in query_list:
    if search_num_by_bisect(query):
        print(1)
    else:
        print(0)





