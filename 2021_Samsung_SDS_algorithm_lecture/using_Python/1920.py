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


def binary_search(data, q):
    l = 0
    r = len(data) - 1

    while (l <= r):
        m = (l + r) // 2
        if q > data[m]:
            l = m + 1
        elif q < data[m]:
            r = m - 1
        else:  # q == data[m]
            return 1
    return 0


N = int(input())
data = list(map(int, input().split()))
data.sort()

Q = int(input())
query = list(map(int, input().split()))

for q in query:
    print(binary_search(data, q))
