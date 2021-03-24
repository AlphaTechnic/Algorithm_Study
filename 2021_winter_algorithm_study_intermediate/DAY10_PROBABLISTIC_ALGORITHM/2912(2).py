import sys
import random
import bisect
sys.stdin = open("input.txt", "r")


N, C = map(int, input().split())
nanjang = [(0, 0) for _ in range(N+1)]

arr = [0] + list(map(int, input().split()))
for ind in range(1, N+1):
    color = arr[ind]
    nanjang[ind] = (color, ind)
nanjang.sort()

M = int(input())
for _ in range(M):
    s, e = map(int, input().split())
    for i in range(20):
        color = arr[random.randint(s, e)]
        stand = (e-s+1) / 2
        numm = bisect.bisect_right(nanjang, (color, e)) - bisect.bisect_left(nanjang, (color, s))
        if (e-s+1) / 2 < bisect.bisect_right(nanjang, (color, e)) - bisect.bisect_left(nanjang, (color, s)):
            print("yes", color)
            break
    else:
        print("no")
