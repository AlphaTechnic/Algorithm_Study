"""
input :
6 4
3
5
6
2

output :
0
0
3
0
"""
import sys
from collections import deque

sys.stdin = open("input.txt")
input = sys.stdin.readline

V, Q = map(int, input().rstrip().split())


def get_path_in_binary_tree(dest):
    while dest != 0:
        path.appendleft(dest)
        dest = dest // 2


occupied = [False for _ in range(V + 1)]
for _ in range(Q):
    q = int(input())

    path = deque()
    get_path_in_binary_tree(q)

    for cur in path:
        if occupied[cur]:
            print(cur)
            break
    else:
        occupied[path[-1]] = True
        print(0)
