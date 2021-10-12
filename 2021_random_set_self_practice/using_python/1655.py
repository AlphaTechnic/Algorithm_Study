"""
input :
7
1
5
2
10
-99
7
5

output :
1
1
2
2
2
2
5
"""
import sys
from heapq import *

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    mnh = []
    mxh = []
    a = int(input())
    mxh.append((-a, a))
    print(a)

    for _ in range(N - 1):
        a = int(input())

        if a <= mxh[0][1]:
            heappush(mxh, (-a, a))
            if len(mxh) == len(mnh) + 2:
                _, a = heappop(mxh)
                heappush(mnh, (a, a))
        else:
            heappush(mnh, (a, a))
            if len(mnh) == len(mxh) + 1:
                _, a = heappop(mnh)
                heappush(mxh, (-a, a))

        print(mxh[0][1])
